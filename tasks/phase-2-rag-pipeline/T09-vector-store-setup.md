# T09 — Set Up Vector Store (Chroma / pgvector)

**Phase:** 2 — RAG Pipeline  
**Priority:** P0 — Critical  
**Effort:** 3–5 days  
**Depends on:** T08 (chunking strategy — need the metadata schema before designing the store)  
**Status:** Not started

---

## Context

The vector store holds the dense vector representations of all tender chunks. Every query to the system triggers a similarity search against this store. The store choice and schema design affect: retrieval accuracy, multi-tender isolation, metadata filtering speed, and production scalability.

**Two-environment strategy:**
- **Development:** Chroma (runs in-process, no server, persists to disk)
- **Production:** pgvector (PostgreSQL extension — same DB as application data, SQL-native filtering, proven at scale)

The schema must be designed with multi-tender support from day one (see T15). A single tender deployed now that requires schema changes later is expensive to migrate.

---

## Tasks

### 9.1 Set up Chroma for development

```python
# src/bmrcl_rag/vector_store.py
import chromadb
from chromadb.config import Settings

def get_chroma_client(persist_path: str = "./data/chroma_db") -> chromadb.Client:
    return chromadb.PersistentClient(
        path=persist_path,
        settings=Settings(anonymized_telemetry=False)
    )

def get_or_create_collection(client, collection_name: str = "bmrcl_tender"):
    return client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
    )
```

### 9.2 Design the metadata schema

Chroma stores metadata as key-value pairs alongside each embedding. The schema must support the filtering queries the retrieval chain will use:

```python
# Metadata fields stored per chunk in Chroma
CHUNK_METADATA_SCHEMA = {
    "tender_id": str,       # "BMRCL-DLN-P1-2026-157"
    "volume": int,          # 1, 2, 3, 4
    "section": str,         # "C", "E", "vol2-part3"
    "section_title": str,   # "EQC", "GCC", "Scope of Work"
    "clause_id": str,       # "3.1.A.(i)", "8.8", "ITT-13.2"
    "okf_type": str,        # "tender_section", "addendum", "clarification"
    "okf_status": str,      # "draft", "stable"
    "verified_tier": str,   # "unverified", "machine-confirmed", "human-reviewed"
    "pdf_page": int,
    "source_sha256": str,
    "stale": bool,          # True if stale_after has passed
    "has_addendum": bool,   # True if this clause was modified by an addendum
    "addendum_number": int, # 0 if no addendum, else the addendum number
}
```

### 9.3 Set up pgvector for production

```sql
-- Migration: 001_create_tender_chunks.sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE tender_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    chunk_id TEXT UNIQUE NOT NULL,
    tender_id TEXT NOT NULL,
    volume INTEGER,
    section TEXT,
    section_title TEXT,
    clause_id TEXT,
    okf_type TEXT,
    okf_status TEXT,
    verified_tier TEXT,
    pdf_page INTEGER,
    source_sha256 TEXT,
    stale BOOLEAN DEFAULT FALSE,
    has_addendum BOOLEAN DEFAULT FALSE,
    addendum_number INTEGER DEFAULT 0,
    chunk_text TEXT NOT NULL,
    embedding vector(1536),  -- OpenAI text-embedding-3-small
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX ON tender_chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
CREATE INDEX ON tender_chunks (tender_id);
CREATE INDEX ON tender_chunks (verified_tier);
CREATE INDEX ON tender_chunks (stale);
```

### 9.4 Build the vector store abstraction

Create an abstract interface that works with both Chroma (dev) and pgvector (prod), controlled by an environment variable:

```python
# src/bmrcl_rag/vector_store.py

class VectorStore:
    def upsert(self, chunks: list[TenderChunk], embeddings: list[list[float]]) -> None: ...
    def query(self, embedding: list[float], n_results: int, filters: dict) -> list[ChunkResult]: ...
    def delete_by_tender(self, tender_id: str) -> None: ...

class ChromaVectorStore(VectorStore): ...
class PgVectorStore(VectorStore): ...

def get_vector_store() -> VectorStore:
    backend = os.getenv("VECTOR_STORE_BACKEND", "chroma")
    if backend == "chroma":
        return ChromaVectorStore(persist_path=os.getenv("CHROMA_PERSIST_PATH", "./data/chroma"))
    elif backend == "pgvector":
        return PgVectorStore(dsn=os.getenv("DATABASE_URL"))
    raise ValueError(f"Unknown backend: {backend}")
```

### 9.5 Implement the retrieval-side filter

The retrieval chain (T11) will pass filters to narrow results by tender, section, and trust tier. Implement the filter translation:

```python
def build_chroma_filter(filters: dict) -> dict:
    """
    Translates high-level filters to Chroma's where clause format.
    Chroma uses MongoDB-style operators.
    """
    where = {"tender_id": filters["tender_id"]}
    if filters.get("exclude_stale"):
        where["stale"] = {"$eq": False}
    if filters.get("verified_only"):
        where["verified_tier"] = {"$in": ["machine-confirmed", "human-reviewed"]}
    if filters.get("volume"):
        where["volume"] = {"$eq": filters["volume"]}
    return where
```

---

## Acceptance Criteria

- [ ] Chroma collection created and persists across restarts
- [ ] pgvector migration script runs cleanly on a fresh PostgreSQL instance
- [ ] `VectorStore.upsert()` accepts a batch of chunks + embeddings and stores them
- [ ] `VectorStore.query()` with `tender_id` filter only returns chunks from that tender
- [ ] `VectorStore.query()` with `exclude_stale=True` filter excludes stale chunks
- [ ] `VectorStore.query()` with `verified_only=True` excludes `unverified` chunks
- [ ] Schema supports multiple tenders without collision (add a second tender's data and verify they don't interfere)

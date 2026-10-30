# T13 — Build Q&A FastAPI Endpoint

**Phase:** 3 — API and Application  
**Priority:** P0 — Critical  
**Effort:** 1 week  
**Depends on:** T11 (retrieval chain working)  
**Status:** Not started

---

## Context

The Q&A endpoint is the primary interface to the tender AI. It takes a natural language question, retrieves the most relevant clauses using the hybrid retrieval chain (T11), constructs a prompt with the retrieved context, and returns an LLM-generated answer with source citations (PDF page numbers and clause IDs).

**Source citation is mandatory.** An answer without a source citation is not acceptable for procurement compliance — users must be able to verify the answer against the original document.

---

## Tasks

### 13.1 Set up FastAPI project

```
src/
└── bmrcl_api/
    ├── __init__.py
    ├── main.py          ← FastAPI app
    ├── routes/
    │   ├── query.py     ← /query endpoint
    │   └── health.py    ← /health endpoint
    ├── models.py        ← Pydantic request/response schemas
    └── config.py        ← environment variables
```

### 13.2 Define request and response schemas

```python
# src/bmrcl_api/models.py
from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str
    tender_id: str = "BMRCL-DLN-P1-2026-157"
    max_results: int = 5
    exclude_stale: bool = True      # exclude addendum-superseded clauses
    verified_only: bool = False     # require human-reviewed chunks

class SourceCitation(BaseModel):
    chunk_id: str
    clause_id: str
    section_title: str
    volume: int
    pdf_page: int
    clause_text: str       # the full retrieved clause text
    verified_tier: str     # "unverified" | "human-reviewed"
    stale: bool
    addendum_note: str | None  # e.g. "Modified by Addendum 2 (2026-10-15)"

class QueryResponse(BaseModel):
    answer: str
    sources: list[SourceCitation]
    retrieval_time_ms: float
    generation_time_ms: float
    model_used: str
    warning: str | None    # e.g. "2 of 5 sources are unverified"
```

### 13.3 Implement the `/query` endpoint

```python
# src/bmrcl_api/routes/query.py
import time
from anthropic import Anthropic

client = Anthropic()

@router.post("/query", response_model=QueryResponse)
async def query_tender(req: QueryRequest):
    t0 = time.time()
    
    # 1. Retrieve relevant chunks
    chunks = retrieve(
        query=req.question,
        store=get_vector_store(),
        bm25_index=get_bm25_index(),
        bm25_chunks=get_bm25_chunks(),
        tender_id=req.tender_id,
        n_results=req.max_results,
        filters={"exclude_stale": req.exclude_stale, "verified_only": req.verified_only},
    )
    retrieval_ms = (time.time() - t0) * 1000
    
    # 2. Build context prompt
    context = "\n\n---\n\n".join([
        f"[Clause {c.chunk.metadata['clause_id']}, Vol{c.chunk.metadata['volume']} "
        f"Section {c.chunk.metadata['section']}, PDF page {c.chunk.metadata['pdf_page']}]\n"
        f"{c.chunk.text}"
        for c in chunks
    ])
    
    # 3. Generate answer
    t1 = time.time()
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=(
            "You are a tender document assistant for BMRCL procurement. "
            "Answer questions using ONLY the provided clause context. "
            "Always cite the clause ID and PDF page number when referencing a clause. "
            "If the context does not contain enough information, say so explicitly. "
            "Never invent clause numbers or financial figures."
        ),
        messages=[
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {req.question}"}
        ]
    )
    generation_ms = (time.time() - t1) * 1000
    
    # 4. Build source citations
    sources = [build_citation(c) for c in chunks]
    
    # 5. Warn if unverified sources were used
    unverified_count = sum(1 for s in sources if s.verified_tier == "unverified")
    warning = f"{unverified_count} of {len(sources)} sources are unverified (pending human review)" if unverified_count else None
    
    return QueryResponse(
        answer=response.content[0].text,
        sources=sources,
        retrieval_time_ms=round(retrieval_ms, 1),
        generation_time_ms=round(generation_ms, 1),
        model_used="claude-sonnet-4-6",
        warning=warning,
    )
```

### 13.4 Add `/health` endpoint

```python
@router.get("/health")
async def health():
    return {
        "status": "ok",
        "vector_store": "connected",
        "chunks_indexed": get_total_chunk_count(),
    }
```

### 13.5 Add request logging

Log every query to `query_logs/YYYY-MM-DD.jsonl`:

```json
{"timestamp": "...", "question": "...", "tender_id": "...", "chunks_retrieved": 5, "retrieval_ms": 120, "generation_ms": 890, "answer_length": 342}
```

This becomes the raw data for monitoring (T18).

---

## Acceptance Criteria

- [ ] `/query` returns a valid `QueryResponse` with at least 1 source citation
- [ ] Source citations include `pdf_page` and `clause_id`
- [ ] `warning` field is populated when any source is `unverified`
- [ ] `stale: true` sources include an `addendum_note`
- [ ] `/health` endpoint returns 200 with chunk count
- [ ] Every request logged to `query_logs/`
- [ ] OpenAPI docs auto-generated at `/docs`
- [ ] Response time < 3 seconds for typical questions (including retrieval + generation)

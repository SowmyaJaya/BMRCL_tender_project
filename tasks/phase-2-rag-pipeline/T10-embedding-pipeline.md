# T10 — Build the Embedding Pipeline

**Phase:** 2 — RAG Pipeline  
**Priority:** P0 — Critical  
**Effort:** 1 week  
**Depends on:** T08 (chunking), T09 (vector store)  
**Status:** Not started

---

## Context

The embedding pipeline converts text chunks into dense vector representations and upserts them into the vector store. Two design concerns are critical:

1. **Gate on review status:** The pipeline must refuse to embed any chunk whose source JSON has `review_status: pending_manual_review`. Unreviewed data must never enter the vector store.
2. **Deterministic chunk IDs:** If a chunk's text changes (due to a review correction or addendum), the embedding can be updated by upserting the same chunk ID with a new vector. Full re-indexing should only be needed when the chunk schema changes.

---

## Tasks

### 10.1 Choose and configure the embedding model

**Recommended:** `text-embedding-3-small` (OpenAI)
- 1536 dimensions
- ~62k tokens context window
- Cost: ~$0.02 per 1M tokens
- Use `tiktoken` to count tokens and warn if any chunk exceeds 8192 tokens

```python
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def embed_texts(texts: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
    """Embeds a batch of texts. Handles rate limiting with exponential backoff."""
    response = client.embeddings.create(input=texts, model=model)
    return [item.embedding for item in response.data]
```

**Alternative (open source, no API cost):** `all-MiniLM-L6-v2` (384 dims, runs locally via `sentence-transformers`)

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts: list[str]) -> list[list[float]]:
    return model.encode(texts, normalize_embeddings=True).tolist()
```

Document the chosen model in `pyproject.toml` and in `src/bmrcl_rag/config.py`.

---

### 10.2 Build the pipeline CLI

```bash
python -m bmrcl_rag embed \
  --json-dir parsed_json/ \
  --tender-id "BMRCL-DLN-P1-2026-157" \
  --batch-size 100 \
  --dry-run
```

Flags:
- `--dry-run`: extract chunks, count them, check review gate, but do not call the embedding API
- `--force-reembed`: re-embed chunks even if their chunk_id already exists in the store
- `--only-volume 1`: embed only a specific volume

---

### 10.3 Implement batched embedding with rate limiting

```python
import time

def embed_chunks_batched(
    chunks: list[TenderChunk],
    batch_size: int = 100,
    sleep_between_batches: float = 0.5,
) -> list[tuple[TenderChunk, list[float]]]:
    results = []
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        texts = [c.text for c in batch]
        embeddings = embed_texts(texts)
        results.extend(zip(batch, embeddings))
        print(f"Embedded {min(i + batch_size, len(chunks))}/{len(chunks)} chunks")
        if i + batch_size < len(chunks):
            time.sleep(sleep_between_batches)
    return results
```

---

### 10.4 Implement incremental updates

Track which chunk IDs are already in the vector store. Only embed new or changed chunks:

```python
def get_existing_chunk_ids(store: VectorStore, tender_id: str) -> set[str]:
    """Returns the set of chunk_ids already in the store for this tender."""
    ...

def embed_incremental(chunks: list[TenderChunk], store: VectorStore, tender_id: str) -> int:
    existing = get_existing_chunk_ids(store, tender_id)
    new_chunks = [c for c in chunks if c.chunk_id not in existing]
    print(f"{len(existing)} already indexed, {len(new_chunks)} new chunks to embed")
    ...
    return len(new_chunks)
```

---

### 10.5 Write an embedding cost estimator

```python
def estimate_embedding_cost(chunks: list[TenderChunk], price_per_million_tokens: float = 0.02) -> dict:
    import tiktoken
    enc = tiktoken.get_encoding("cl100k_base")
    total_tokens = sum(len(enc.encode(c.text)) for c in chunks)
    cost_usd = (total_tokens / 1_000_000) * price_per_million_tokens
    return {"total_chunks": len(chunks), "total_tokens": total_tokens, "estimated_cost_usd": round(cost_usd, 4)}
```

Run `--dry-run` before the first real embed to see the cost estimate.

---

## Acceptance Criteria

- [ ] Pipeline raises on any unreviewed chunk (review gate enforced)
- [ ] Dry run prints chunk count and cost estimate without hitting the API
- [ ] After running, every chunk in the manifest appears in the vector store
- [ ] Running again with no changes embeds 0 new chunks (incremental update works)
- [ ] Chunks from two different tenders are stored without collision
- [ ] Embedding vectors are stored with all required metadata fields (see T09 schema)

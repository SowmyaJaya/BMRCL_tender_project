# T11 — Implement Hybrid Retrieval Chain

**Phase:** 2 — RAG Pipeline  
**Priority:** P0 — Critical  
**Effort:** 1 week  
**Depends on:** T10 (chunks embedded in vector store)  
**Status:** Not started

---

## Context

A retrieval chain takes a natural language query and returns the most relevant tender clauses. For tender documents, **hybrid search** — combining dense vector similarity with sparse BM25 keyword search — significantly outperforms either method alone:

- **Dense search** catches semantic paraphrases: "when can BMRCL stop the project?" retrieves GCC Clause 8.8 (Suspension) even though the query doesn't use the word "suspend"
- **BM25 keyword search** catches exact terms that embeddings often blur: clause numbers (`"ITT-13.2"`), financial figures (`"₹ 3.79 Crores"`), legal terminology (`"liquidated damages"`)

Neither alone is sufficient. A question like "What is the EMD amount?" — where `EMD` stands for `Earnest Money Deposit` — requires both: dense search to match the concept, BM25 to match the exact acronym.

---

## Tasks

### 11.1 Implement dense retrieval

```python
# src/bmrcl_rag/retrieval.py

def dense_retrieve(
    query: str,
    store: VectorStore,
    tender_id: str,
    n_results: int = 10,
    filters: dict = None,
) -> list[ChunkResult]:
    query_embedding = embed_texts([query])[0]
    return store.query(
        embedding=query_embedding,
        n_results=n_results,
        filters={"tender_id": tender_id, **(filters or {})}
    )
```

---

### 11.2 Implement BM25 sparse retrieval

Build a BM25 index over the chunk texts at startup (or load from disk if pre-built):

```python
from rank_bm25 import BM25Okapi
import pickle

def build_bm25_index(chunks: list[TenderChunk]) -> tuple[BM25Okapi, list[TenderChunk]]:
    tokenized = [c.text.lower().split() for c in chunks]
    return BM25Okapi(tokenized), chunks

def bm25_retrieve(query: str, bm25: BM25Okapi, chunks: list[TenderChunk], n_results: int = 10) -> list[ChunkResult]:
    scores = bm25.get_scores(query.lower().split())
    top_indices = scores.argsort()[-n_results:][::-1]
    return [ChunkResult(chunk=chunks[i], score=float(scores[i])) for i in top_indices]
```

---

### 11.3 Implement Reciprocal Rank Fusion (RRF)

RRF is the standard method for merging dense and sparse ranked lists. It is rank-based, not score-based, so it handles different score scales gracefully.

```python
def reciprocal_rank_fusion(
    dense_results: list[ChunkResult],
    sparse_results: list[ChunkResult],
    k: int = 60,
) -> list[ChunkResult]:
    """
    Merges two ranked lists using RRF.
    RRF score = sum(1 / (k + rank)) across all lists.
    """
    scores: dict[str, float] = {}
    chunk_map: dict[str, ChunkResult] = {}

    for rank, result in enumerate(dense_results, 1):
        scores[result.chunk.chunk_id] = scores.get(result.chunk.chunk_id, 0) + 1 / (k + rank)
        chunk_map[result.chunk.chunk_id] = result

    for rank, result in enumerate(sparse_results, 1):
        scores[result.chunk.chunk_id] = scores.get(result.chunk.chunk_id, 0) + 1 / (k + rank)
        chunk_map[result.chunk.chunk_id] = result

    sorted_ids = sorted(scores, key=lambda cid: scores[cid], reverse=True)
    return [chunk_map[cid] for cid in sorted_ids]
```

---

### 11.4 Build the full retrieval function

```python
def retrieve(
    query: str,
    store: VectorStore,
    bm25_index: BM25Okapi,
    bm25_chunks: list[TenderChunk],
    tender_id: str,
    n_results: int = 5,
    filters: dict = None,
) -> list[ChunkResult]:
    """
    Hybrid retrieval: dense + BM25 merged via RRF.
    Filters applied to dense side; BM25 filtered post-hoc by tender_id.
    """
    dense = dense_retrieve(query, store, tender_id, n_results=20, filters=filters)
    sparse = bm25_retrieve(query, bm25_index, bm25_chunks, n_results=20)
    # Filter sparse by tender_id post-hoc (BM25 index is per-tender)
    sparse = [r for r in sparse if r.chunk.metadata["tender_id"] == tender_id]
    fused = reciprocal_rank_fusion(dense, sparse)
    return fused[:n_results]
```

---

### 11.5 Implement metadata filtering

Support these filter modes in the retrieval API:

```python
# Filter options
filters = {
    "exclude_stale": True,      # exclude clauses superseded by addendums
    "verified_only": False,     # only return human-reviewed chunks
    "volume": 1,                # restrict to a specific volume
    "section": "C",             # restrict to a specific section
}
```

---

### 11.6 Write retrieval evaluation tests

Create 10 hand-crafted (query, expected_clause_id) pairs from the tender documents:

```python
EVAL_PAIRS = [
    ("What is the EMD amount?", "nit/item/2"),
    ("What is the estimated cost of work?", "nit/item/1"),
    ("What work experience is needed to qualify?", "vol1-C/eqc-3.1.A.i"),
    ("What are the milestone completion dates?", "annexure-1/milestone/1"),
    ("Under what conditions can BMRCL suspend work?", "vol1-E/gcc-8.8"),
    ("What insurance is required?", "vol1-E/gcc-..."),
    ("What are the SHE penalty rates?", "vol3.../penalty/..."),
    ("What key personnel are required?", "annexure-2/personnel/1"),
    ("What is the completion period?", "nit/item/..."),
    ("What happens if a bidder withdraws their bid?", "vol1-B/itt-17"),
]

def test_retrieval_top5_hit_rate():
    """All 10 expected clauses appear in top-5 results for their query."""
    hits = 0
    for query, expected_chunk_suffix in EVAL_PAIRS:
        results = retrieve(query, ...)
        result_ids = [r.chunk.chunk_id for r in results]
        if any(expected_chunk_suffix in rid for rid in result_ids):
            hits += 1
    assert hits / len(EVAL_PAIRS) >= 0.8, f"Hit rate: {hits}/{len(EVAL_PAIRS)}"
```

---

## Acceptance Criteria

- [ ] `retrieve()` function works with both Chroma and pgvector backends
- [ ] Hit rate ≥ 80% on the 10 eval pairs (8 out of 10 expected clauses in top-5)
- [ ] `exclude_stale=True` filter correctly excludes addendum-superseded clauses
- [ ] Retrieval latency < 500ms for a single query on the full corpus
- [ ] BM25 correctly retrieves clause ITT-13.2 when query contains exact string "ITT-13.2"

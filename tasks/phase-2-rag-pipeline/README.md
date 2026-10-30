# Phase 2 — RAG Pipeline

**Goal:** A queryable tender knowledge base with clause-level retrieval and source citation.  
**Depends on:** Phase 1 complete — all data reviewed, OKF bundle valid, addendums processed.

---

## Why This Matters

Raw JSON files cannot be queried by an LLM without a retrieval layer. The key design decision here is chunking strategy: for legal and tender documents, **clause-level chunking** is mandatory. Fixed-size token chunking cuts across legal reasoning units — for example, splitting a 600-token indemnification clause into three overlapping chunks produces three half-clauses that each sound plausible but none of which accurately represent the clause. Research (2026) confirms that clause-level retrieval is the correct primitive for contract and legal document QA.

The retrieval chain uses **hybrid search**: dense vector similarity (catches semantic paraphrases) combined with BM25 keyword matching (catches exact clause numbers, financial figures, and legal terminology that embeddings often miss). Neither alone is sufficient for tender QA.

---

## Tasks in This Phase

| Task | Description | Effort |
|---|---|---|
| [T08](T08-chunking-strategy.md) | Design clause-level chunking strategy | 3–5 days |
| [T09](T09-vector-store-setup.md) | Set up Chroma (dev) + pgvector (prod) | 3–5 days |
| [T10](T10-embedding-pipeline.md) | Build and run the embedding pipeline | 1 week |
| [T11](T11-retrieval-chain.md) | Implement hybrid retrieval chain | 1 week |
| [T12](T12-eqc-eligibility-checker.md) | Build deterministic EQC eligibility checker | 3–5 days |

---

## Phase Exit Criteria

- [ ] All reviewed JSON chunks embedded in vector store with metadata
- [ ] Hybrid search returns correct clauses for 10 hand-crafted test queries
- [ ] Retrieval correctly filters by volume, section, and OKF trust tier
- [ ] EQC checker correctly evaluates 5 test company profiles against criteria
- [ ] No unreviewed chunks in the vector store (enforced by pipeline gate)

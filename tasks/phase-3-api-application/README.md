# Phase 3 — API and Application

**Goal:** A working FastAPI backend that answers tender questions with source citations.  
**Depends on:** Phase 2 complete — retrieval chain working, EQC checker built.

---

## Tasks in This Phase

| Task | Description | Effort |
|---|---|---|
| [T13](T13-qa-api-endpoint.md) | Build Q&A FastAPI endpoint | 1 week |
| [T14](T14-addendum-aware-retrieval.md) | Implement addendum-aware retrieval | 1 week |
| [T15](T15-multi-tender-namespace.md) | Multi-tender namespace architecture | 2 weeks |

---

## Phase Exit Criteria

- [ ] `/query` endpoint returns answers with PDF page citations
- [ ] Addendum-affected clauses surface their supersession provenance
- [ ] Vector store schema supports multiple tenders without namespace collision
- [ ] API documented with OpenAPI / Swagger

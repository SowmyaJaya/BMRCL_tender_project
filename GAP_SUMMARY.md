# BMRCL Tender AI — Gap Summary

**Project:** BMRCL_tender_project (github.com/SowmyaJaya/BMRCL_tender_project)  
**Tender:** BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157  
**Snapshot date:** 2026-10-28  
**Overall production readiness:** ~18%

---

## The One-Paragraph Picture

The project has a well-structured data curation layer: raw tender PDFs have been converted into an **OKF (Open Knowledge Format) markdown bundle** and **~40 clause-level JSON files** with SHA-256 provenance anchoring. That foundation is the right approach for a production AI system. However, (1) the extraction pipeline code that produced these artifacts was never committed, (2) every JSON file is still marked `pending_manual_review` — no data has been verified, (3) the OKF bundle has 8 compliance gaps that prevent any AI agent from traversing it correctly, (4) four source documents remain completely unprocessed (Vol4, BOQ Excel, 3 addendums, pre-bid Q&A), and (5) the entire application stack — vector embeddings, RAG pipeline, LLM integration, API, and UI — does not exist. There are zero lines of application code in the repository.

---

## Gap Inventory

| ID | Gap | Phase | Priority | Effort | Status |
|---|---|---|---|---|---|
| G01 | No ingestion pipeline code committed | 1 | 🔴 P0 | M | Not started |
| G02 | Zero human review of extracted data (all 40+ JSON pending) | 1 | 🔴 P0 | L | Not started |
| G03 | OKF bundle structurally incomplete — no index.md, no inter-file links | 1 | 🟠 P1 | S | Not started |
| G04 | OKF frontmatter non-compliant on all 18 files (8 issues each) | 1 | 🟠 P1 | S | Not started |
| G05 | Vol 4 (drawings PDF) not processed into OKF + JSON | 1 | 🟠 P1 | M | Not started |
| G06 | BOQ Excel (financial bid) not parsed | 1 | 🟠 P1 | S | Not started |
| G07 | All 3 addendums unprocessed — RAG will return superseded clauses | 1 | 🟠 P1 | M | Not started |
| G08 | Pre-bid Q&A replies unprocessed | 1 | 🟡 P2 | S | Not started |
| G09 | No chunking strategy for RAG | 2 | 🔴 P0 | S | Not started |
| G10 | No vector store or embedding pipeline | 2 | 🔴 P0 | M | Not started |
| G11 | No retrieval chain (hybrid search) | 2 | 🔴 P0 | M | Not started |
| G12 | No EQC eligibility checker | 2 | 🟠 P1 | M | Not started |
| G13 | No Q&A API endpoint | 3 | 🔴 P0 | M | Not started |
| G14 | No addendum-aware retrieval | 3 | 🟠 P1 | M | Not started |
| G15 | No multi-tender namespace architecture | 3 | 🟡 P2 | L | Not started |
| G16 | No CI/CD or test suite | 4 | 🟠 P1 | M | Not started |
| G17 | No authentication or rate limiting | 4 | 🟡 P2 | M | Not started |
| G18 | No monitoring or observability | 4 | 🟡 P2 | S | Not started |



---

## Gaps by Phase

### Phase 1 — Data Foundation (Prerequisite for everything else)

**Readiness: 30% complete. Core PDFs exist; nothing is verified or fully structured.**

The OKF bundle exists but is not traversable by an AI agent. The JSON store exists but no clause has been human-reviewed. Four source documents (Vol4, BOQ, 3 addendums, pre-bid Q&A) are raw PDFs with no extracted representation. The ingestion code does not exist in the repository.

Gaps: G01, G02, G03, G04, G05, G06, G07, G08

**Unblocked today:** G01 (commit code), G03 (fix OKF structure), G04 (fix frontmatter), G06 (parse BOQ), G08 (parse pre-bid Q&A)  
**Blocked on G01:** G02 (needs the review tool), G05, G07 (need extraction pipeline)

---

### Phase 2 — RAG Pipeline (Blocked on Phase 1 completion)

**Readiness: 0%. No code exists.**

The chunking strategy must be designed before any embedding work begins. Clause-level chunking (using the existing JSON clause IDs as chunk boundaries) is the correct approach for legal/tender documents — fixed-size chunking cuts across legal reasoning units and produces retrieval that fails under scrutiny. The vector store, embedding pipeline, and retrieval chain must all be built sequentially.

Gaps: G09, G10, G11, G12

**Can start planning (not implementing):** G09 (chunking design spec), G12 (EQC checker logic — deterministic, no RAG dependency)  
**Blocked on Phase 1 + G09:** G10, G11

---

### Phase 3 — API and Application (Blocked on Phase 2)

**Readiness: 0%. No code exists.**

The Q&A API endpoint wraps the retrieval chain. Addendum-aware retrieval requires the addendum delta JSON from Phase 1 and the retrieval chain from Phase 2. Multi-tender namespace support must be designed into the vector store schema from the start — retrofitting it is expensive.

Gaps: G13, G14, G15

---

### Phase 4 — Production Hardening (Parallel with Phase 2/3)

**Readiness: 0%. Git repository exists; no workflows, no tests.**

CI/CD and tests can begin as soon as Phase 1 is complete (the first tests are data integrity tests, not application tests). Auth and monitoring should be designed in Phase 2 and implemented in Phase 3.

Gaps: G16, G17, G18

---

## Critical Path

```
G01 (commit pipeline) 
  └─► G02 (review data) ──────────────────────────────────────────────►┐
  └─► G03 (OKF index.md + links)                                        │
  └─► G04 (OKF frontmatter fix)                                         │
  └─► G05 (Vol4 processing)                                             │
  └─► G06 (BOQ processing)                                              │
  └─► G07 (addendum processing) ─────────────────────────────────────►  │
  └─► G08 (pre-bid Q&A)                                                 │
                                                                         │
G09 (chunking design) ─► G10 (vector store + embeddings) ──────────────►┤
                      └─► G12 (EQC checker — no RAG dependency)          │
                                                                         │
                          G11 (retrieval chain) ─────────────────────────►┤
                                                                          │
                                              G13 (Q&A API) ─────────────►┤
                                              G14 (addendum retrieval)    │
                                              G15 (multi-tender)          │
                                                                          │
                          G16 (CI/CD tests) ────────────────────────────► PRODUCTION
                          G17 (auth)
                          G18 (monitoring)
```

---

## Quick Wins (High Impact, Low Effort — Start Here)

These can be done immediately with no dependencies:

1. **G04 — Fix OKF frontmatter** (1–2 days): Update `status`, add `description`, `resource`, `generated`, `verified: []` on all 18 MD files. Script-automatable.
2. **G03 — Create OKF index files** (1 day): Add `index.md` at bundle root and each volume level. Add inter-file links between related sections.
3. **G06 — Parse BOQ Excel** (1–2 days): Read `BOQ_338417.xls`, output structured JSON per line item.
4. **G09 — Document chunking strategy** (1 day): Write a design document + proof-of-concept chunker. No vector store needed yet.
5. **G12 — EQC eligibility checker logic** (2–3 days): Deterministic rule engine from `eqc_criteria.json`. No LLM, no RAG, no database.

---

## Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| Embedding unreviewed data (G02 unresolved) | High — LLM quotes wrong financial thresholds | Gate embedding pipeline on `review_status: reviewed_ok` |
| Addendums ignored in RAG (G07 unresolved) | High — legally superseded clauses returned as current | `stale_after` field in OKF; version graph in retrieval |
| Ingestion code lost (G01 unresolved) | High — no way to re-extract if PDFs are updated | Immediate priority; commit before anything else |
| Fixed-size chunking used for legal docs | Medium — retrieval cuts legal reasoning units | Enforce clause-level chunking policy in G09 |
| Multi-tender namespace ignored until Phase 3 | Medium — expensive retrofit | Design namespace into vector store schema in G10 |

---

## Detailed Task Files

All tasks are documented with context, subtasks, and acceptance criteria in:

```
tasks/
├── README.md
├── phase-1-data-foundation/    T01–T07
├── phase-2-rag-pipeline/       T08–T12
├── phase-3-api-application/    T13–T15
└── phase-4-hardening/          T16–T18
```

# Task Index — BMRCL Tender AI

This directory contains the full task breakdown for building a production-grade AI system on top of the BMRCL tender document corpus. Each task file is self-contained: it explains the context, the current state, the goal, all subtasks, and acceptance criteria.

---

## How to Pick Up a Task

1. Read `GAP_SUMMARY.md` at the project root for the overall picture.
2. Check the dependency column below — do not start a task whose dependency is incomplete.
3. Open the task file. Read the **Context** and **Current State** sections fully before writing any code.
4. Use the **Acceptance Criteria** section as your definition of done.
5. Update the task file's **Status** line when you start and when you finish.

---

## Task Map

### Phase 1 — Data Foundation

| Task | Title | Priority | Effort | Depends On |
|---|---|---|---|---|
| [T01](phase-1-data-foundation/T01-ingestion-pipeline.md) | Commit the ingestion pipeline | P0 | 1–2 weeks | — |
| [T02](phase-1-data-foundation/T02-data-review-workflow.md) | Human review of all extracted data | P0 | 2–3 weeks | T01 |
| [T03](phase-1-data-foundation/T03-okf-compliance-fix.md) | Fix OKF bundle structure and frontmatter | P1 | 3–5 days | — |
| [T04](phase-1-data-foundation/T04-vol4-processing.md) | Process Vol 4 (drawings) into OKF + JSON | P1 | 1–2 weeks | T01 |
| [T05](phase-1-data-foundation/T05-boq-processing.md) | Parse BOQ Excel into structured JSON | P1 | 2–3 days | T01 |
| [T06](phase-1-data-foundation/T06-addendum-processing.md) | Process 3 addendums into delta OKF + JSON | P1 | 1–2 weeks | T01 |
| [T07](phase-1-data-foundation/T07-prebid-processing.md) | Process pre-bid Q&A replies | P2 | 2–3 days | T01 |

### Phase 2 — RAG Pipeline

| Task | Title | Priority | Effort | Depends On |
|---|---|---|---|---|
| [T08](phase-2-rag-pipeline/T08-chunking-strategy.md) | Design and implement clause-level chunking | P0 | 3–5 days | T01, T02 |
| [T09](phase-2-rag-pipeline/T09-vector-store-setup.md) | Set up vector store (Chroma/pgvector) | P0 | 3–5 days | T08 |
| [T10](phase-2-rag-pipeline/T10-embedding-pipeline.md) | Build embedding pipeline | P0 | 1 week | T08, T09 |
| [T11](phase-2-rag-pipeline/T11-retrieval-chain.md) | Implement hybrid retrieval chain | P0 | 1 week | T10 |
| [T12](phase-2-rag-pipeline/T12-eqc-eligibility-checker.md) | Build EQC deterministic eligibility checker | P1 | 3–5 days | T02 (data reviewed) |

### Phase 3 — API and Application

| Task | Title | Priority | Effort | Depends On |
|---|---|---|---|---|
| [T13](phase-3-api-application/T13-qa-api-endpoint.md) | Build Q&A FastAPI endpoint | P0 | 1 week | T11 |
| [T14](phase-3-api-application/T14-addendum-aware-retrieval.md) | Implement addendum-aware retrieval | P1 | 1 week | T11, T06 |
| [T15](phase-3-api-application/T15-multi-tender-namespace.md) | Multi-tender namespace architecture | P2 | 2 weeks | T09, T13 |

### Phase 4 — Hardening

| Task | Title | Priority | Effort | Depends On |
|---|---|---|---|---|
| [T16](phase-4-hardening/T16-cicd-test-suite.md) | CI/CD pipeline and test suite | P1 | 1–2 weeks | T01 (Phase 1 complete) |
| [T17](phase-4-hardening/T17-auth-rate-limiting.md) | Authentication and rate limiting | P2 | 1 week | T13 |
| [T18](phase-4-hardening/T18-monitoring-observability.md) | Monitoring and observability | P2 | 3–5 days | T13 |

---

## Start Here (No Dependencies)

These tasks can begin immediately:

- **T03** — Fix OKF frontmatter compliance on 18 existing files (scripting task, no pipeline needed)
- **T05** — Parse BOQ Excel (standalone Python script)
- **T07** — Parse pre-bid Q&A PDF (standalone Python script)
- **T08** — Design the chunking strategy (design document first, no code dependencies)
- **T12** — Build EQC eligibility checker (reads existing `eqc_criteria.json`)

---

## Project Tech Stack

| Layer | Technology |
|---|---|
| PDF extraction | PyMuPDF (`fitz`) |
| OCR (Vol 4) | Azure Document Intelligence or AWS Textract |
| Excel parsing | `xlrd` (for `.xls`) |
| OKF bundle | Plain markdown + YAML (`pyyaml`) |
| Vector store (dev) | Chroma |
| Vector store (prod) | pgvector (PostgreSQL extension) |
| Embedding model | `text-embedding-3-small` (OpenAI) |
| RAG framework | LlamaIndex |
| API | FastAPI |
| Auth | python-jose + passlib |
| CI/CD | GitHub Actions |
| Language | Python 3.11+ |

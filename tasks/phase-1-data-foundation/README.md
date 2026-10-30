# Phase 1 — Data Foundation

**Goal:** A complete, OKF-compliant, human-verified, fully-extracted data corpus ready for embedding.  
**Status:** In progress — Vols 1–3 extracted but unverified. Vol4, BOQ, addendums, pre-bid Q&A not processed.

---

## Why This Phase Comes First

Every downstream phase (RAG, API, UI) depends on the quality and completeness of the data layer. Embedding data that has not been human-reviewed will cause an LLM to confidently cite incorrect financial thresholds, superseded clauses, or malformed table rows. Fix the data first; build the application on top of it.

The OKF bundle is the human-and-agent-readable knowledge graph of the tender corpus. The JSON store is the machine-readable structured extraction. Both must be complete and consistent before any embedding work begins.

---

## Tasks in This Phase

| Task | Description | Effort |
|---|---|---|
| [T01](T01-ingestion-pipeline.md) | Commit the extraction pipeline code | 1–2 weeks |
| [T02](T02-data-review-workflow.md) | Human review of all 40+ JSON files | 2–3 weeks |
| [T03](T03-okf-compliance-fix.md) | Fix OKF bundle structure and frontmatter | 3–5 days |
| [T04](T04-vol4-processing.md) | Process Vol 4 drawings | 1–2 weeks |
| [T05](T05-boq-processing.md) | Parse BOQ Excel | 2–3 days |
| [T06](T06-addendum-processing.md) | Process 3 addendums | 1–2 weeks |
| [T07](T07-prebid-processing.md) | Process pre-bid Q&A replies | 2–3 days |

---

## Phase Exit Criteria

This phase is complete when:

- [ ] The ingestion pipeline code is in the repository with `requirements.txt`
- [ ] Every JSON file has `review_status` updated from `pending_manual_review`
- [ ] Every OKF markdown file has a valid `generated` block, `verified` block, correct `status` enum, `description`, and `resource`
- [ ] `OKF_bundle/Technical/index.md` exists with `okf_version: "0.2"`
- [ ] Inter-file links exist between related OKF sections
- [ ] Vol4, BOQ, addendums, and pre-bid Q&A are represented in both OKF and JSON
- [ ] `stale_after` is set on all base-volume sections superseded by an addendum

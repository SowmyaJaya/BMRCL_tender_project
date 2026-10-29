# T02 — Human Review of All Extracted Data

**Phase:** 1 — Data Foundation  
**Priority:** P0 — Critical   
**Depends on:** T01 (ingestion pipeline committed, review tooling can be built)  
**Status:** Not started

---

## Context

Every JSON file in `parsed_json/` carries `"review_status": "pending_manual_review"`. This flag is not cosmetic — it means the extracted data has not been validated against its source PDF. Table extraction from government PDFs is error-prone for several reasons:

- **Rotated tables:** Vol1 Section C (EQC) contains tables printed sideways. PyMuPDF reads coordinates in the unrotated coordinate system, which can misorder rows and columns.
- **Multi-line cells:** A table cell like "Tenderer should have completed/ **substantially completed** One work of *Similar nature*, where the value of the work is equal to or exceed ₹ 3.79 Crores" spans multiple text blocks in PyMuPDF. These can be joined incorrectly.
- **Merged header cells:** Column headers that span two columns get split by PyMuPDF into separate text blocks and may be attributed to the wrong column.
- **Currency formatting:** Values like `INR 4.74 Crores` or `₹ 3.79 Crores` or `INR 7.11 Lakhs` must be read exactly — a misread financial threshold in the EQC criteria could disqualify a valid bidder or pass an ineligible one.

**This is not optional.** Embedding unreviewed data into a vector store will cause an LLM to confidently cite wrong numbers. A system that tells a bidder they qualify when they don't, or vice versa, is a legal liability.

---

## Current State

All 40+ JSON files have `"review_status": "pending_manual_review"`. The corresponding OKF markdown files have no `verified` block. There is no review tooling.

Fields most likely to contain extraction errors:
- Financial thresholds in `eqc_criteria.json` and `eqc_tables.json`
- Table cell boundaries in all `attachment_*_tables.json` files
- Clause numbering in `gcc_clauses.json`, `itt_clauses.json`, `scc_entries.json`
- Milestone dates and liquidated damages amounts in `milestones.json`
- Equipment/personnel quantity tables in `annexure_2_personnel.json`, `annexure_3_equipment.json`

---

## Goal

Every JSON file reviewed against its source PDF page. Financial fields verified by a second reviewer. `review_status` updated. OKF `verified` blocks populated.

---

## Tasks

### 2.1 Build a review CLI tool

Create `src/bmrcl_pipeline/review_tool.py` — a command-line tool that shows a reviewer the extracted text side-by-side with instructions for the source PDF page.

```bash
python -m bmrcl_pipeline review \
  --json parsed_json/vol1/section_c_eqc/eqc_criteria.json \
  --pdf BMRCL_TenderData/Tender_Documents/Vol1DLNP1.pdf
```

For each item in the JSON:
1. Print the extracted text
2. Print the `pdf_page` number and `bbox` coordinates
3. Prompt: `[OK] [EDIT] [FLAG]`
   - `OK` → marks that item's `review_status` as `reviewed_ok`
   - `EDIT` → opens an editor to correct the text in-place, then marks `reviewed_corrected`
   - `FLAG` → marks as `reviewed_flagged` with a free-text note for escalation

The tool must write a review session log to `review_logs/YYYY-MM-DD-{filename}.json`.

---

### 2.2 Define the review protocol

Document in `tasks/phase-1-data-foundation/REVIEW_PROTOCOL.md`:

- **Financial fields** require two independent reviewers. Any discrepancy between reviewers triggers escalation.
- **Clause text** requires one reviewer who checks: (a) clause number is correct, (b) text is complete and not truncated, (c) cross-references to other clauses are intact.
- **Table rows** require one reviewer who checks: (a) rows are in correct order, (b) column values are in correct columns, (c) no rows are missing.
- **Review order priority:** `eqc_criteria.json` first (financial thresholds), then `milestones.json` (dates/LD amounts), then `gcc_clauses.json` and `itt_clauses.json`, then remaining files.

---

### 2.3 Execute the review

Work through all JSON files using the review tool. Priority order:

1. `parsed_json/vol1/section_c_eqc/eqc_criteria.json` — financial thresholds for eligibility
2. `parsed_json/vol1/section_c_eqc/eqc_tables.json` — EQC tables
3. `parsed_json/vol2/annexure_1_milestones/milestones.json` — milestone dates, LD rates
4. `parsed_json/vol1/section_a_nit/nit_items.json` — EMD, fees, key commercial terms
5. All `attachment_*_tables.json` files
6. `parsed_json/vol1/section_e_gcc/gcc_clauses.json` — 31 clauses
7. `parsed_json/vol1/section_b_itt/itt_clauses.json`
8. Remaining files

---

### 2.4 Update OKF `verified` blocks

After each JSON file is reviewed, update the corresponding OKF markdown file's frontmatter:

```yaml
# Before (current state):
# [no verified block]

# After review by first reviewer:
verified:
  - by: human:reviewer-name
    at: "2026-11-01T09:00:00Z"
    method: "pdf-side-by-side-comparison"

# After second reviewer (financial files only):
verified:
  - by: human:reviewer-1-name
    at: "2026-11-01T09:00:00Z"
    method: "pdf-side-by-side-comparison"
  - by: human:reviewer-2-name
    at: "2026-11-02T14:00:00Z"
    method: "independent-pdf-verification"
```

Also update `status: draft` → `status: stable` once the file has passed all required reviews.

---

### 2.5 Gate the embedding pipeline on review status

Add a pre-flight check to the embedding pipeline (T10):

```python
def validate_review_gate(json_files: list[Path]) -> None:
    """Raises if any file has review_status != 'reviewed_ok' or 'reviewed_corrected'."""
    unreviewed = [
        f for f in json_files
        if load_json(f).get("review_status") == "pending_manual_review"
    ]
    if unreviewed:
        raise ValueError(
            f"Cannot embed: {len(unreviewed)} files still pending review.\n"
            + "\n".join(str(f) for f in unreviewed)
        )
```

This ensures no unreviewed data ever enters the vector store.

---

## Acceptance Criteria

- [ ] All 40+ JSON files have `review_status` set to `reviewed_ok` or `reviewed_corrected` (no `pending_manual_review` remaining)
- [ ] All financial fields in `eqc_criteria.json` and `milestones.json` reviewed by two independent reviewers
- [ ] All OKF markdown files have a populated `verified` block with at least one `human:` entry
- [ ] `eqc_criteria.json` financial thresholds match the source PDF exactly:
  - Criterion 3.1.A.(i): ₹ 3.79 Crores
  - Criterion 3.1.A.(ii): ₹ 2.37 Crores each (×2 works)
  - Check all others against Vol1 PDF page 32
- [ ] The embedding pipeline (`validate_review_gate`) rejects any JSON still in `pending_manual_review`
- [ ] Review session logs committed to `review_logs/`

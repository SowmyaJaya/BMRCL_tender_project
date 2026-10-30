# T06 — Process Addendums/Corrigendums into Delta OKF + JSON

**Phase:** 1 — Data Foundation  
**Priority:** P1 — High  
**Effort:** 1–2 weeks  
**Depends on:** T01 (pipeline), T03 (OKF base files must exist for stale_after to be set)  
**Status:** Not started

---

## Context

Three addendum PDFs exist in `BMRCL_TenderData/Addendum_Corrigendum/`:
- `DLN_P1_AandC1_157.PDF` — Addendum & Corrigendum 1
- `AandC2_DLN_P1_157.PDF` — Addendum & Corrigendum 2
- `AandC3_DLN_P1_157.PDF` — Addendum & Corrigendum 3

Addendums are **legal supersessions**. When BMRCL issues an addendum, it legally modifies, deletes, or replaces specific clauses in the base volumes. A RAG system that ignores addendums will return **outdated clause text** as if it were current — which is both technically wrong and potentially a legal problem for any bidder relying on the system.

**The pre-bid query replies** (`RepliesPrebidqueriesDLNP1157.PDF`) are also legally binding clarifications and should be treated similarly.

This is different from a simple document extraction task. Addendums reference specific clause numbers from the base volumes and say "replace clause X with Y" or "delete sub-clause Z". The system must:
1. Extract the addendum's delta (which clauses it affects and how)
2. Link the delta back to the affected base-volume clause
3. Mark the affected OKF file as stale
4. Build a version graph so retrieval always returns the effective text

---

## Tasks

### 6.1 Extract each addendum

Apply the T01 ingestion pipeline to each addendum PDF. Addendums are typically structured as:

```
CORRIGENDUM / ADDENDUM No. X
Tender No: BMRCL/...
Date: DD/MM/YYYY

S.No. | Vol/Section | Clause No. | Existing Text | Revised Text | Remarks
```

Parse this table into a structured delta format.

---

### 6.2 Define the clause delta JSON schema

```json
{
  "source_id": "bmrcl-addendum-2",
  "source_path": "data/AandC2_DLN_P1_157.PDF",
  "source_sha256": "...",
  "addendum_number": 2,
  "publication_date": "2026-10-15",
  "review_status": "pending_manual_review",
  "deltas": [
    {
      "delta_id": "AandC2-001",
      "affected_volume": 1,
      "affected_section": "B",
      "affected_clause": "ITT-13.2",
      "action": "replace",
      "original_text": "The Tender Security (EMD) shall be...",
      "revised_text": "The Tender Security (EMD) shall be submitted in the form of...",
      "effective_date": "2026-10-15",
      "remarks": ""
    }
  ]
}
```

Possible `action` values: `replace`, `delete`, `insert`, `amend` (partial modification with only the changed portion specified).

Save to `parsed_json/addenda/addendum_1.json`, `addendum_2.json`, `addendum_3.json`.

---

### 6.3 Update OKF `stale_after` on affected base sections

For each delta in an addendum, find the corresponding OKF markdown file and set `stale_after` to the addendum's publication date:

```python
def apply_stale_marker(okf_path: Path, stale_date: str) -> None:
    """Sets stale_after in the OKF frontmatter of an affected section."""
    content = okf_path.read_text()
    # parse frontmatter, set stale_after, rewrite
    ...
```

Example: If Addendum 2 modifies clause ITT-13.2 (in `secB.md`), set:
```yaml
stale_after: "2026-10-15T00:00:00Z"
```

This tells any agent that `secB.md` contains at least one clause that was superseded on that date.

---

### 6.4 Create OKF files for each addendum

Create `OKF_bundle/Technical/Addenda/addendum_1.md`, `addendum_2.md`, `addendum_3.md`:

```yaml
---
okf_version: "0.2"
type: addendum
title: "Addendum & Corrigendum No. 2"
description: "Legal modifications to base tender documents. Replaces specific clauses in Vols 1–2. Effective 2026-10-15."
status: stable
resource: /BMRCL_TenderData/Addendum_Corrigendum/AandC2_DLN_P1_157.PDF
sources:
  - path: /BMRCL_TenderData/Addendum_Corrigendum/AandC2_DLN_P1_157.PDF
    author: "BMRCL"
    last_modified: "2026-10-15"
    sha256: "..."
generated:
  by: process:pdf-extraction-pipeline
  at: "..."
verified: []
tender_no: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157
addendum_number: 2
effective_date: "2026-10-15"
affected_sections:
  - "/OKF_bundle/Technical/Vol1/secB.md"
  - "/OKF_bundle/Technical/Vol1/secC.md"
---

# Addendum & Corrigendum No. 2

[List of clause modifications with before/after text]

## Affected Sections

- [Section B — Instructions to Tenderers](/OKF_bundle/Technical/Vol1/secB.md) — Clause ITT-13.2 revised
- [Section C — EQC](/OKF_bundle/Technical/Vol1/secC.md) — ...
```

---

### 6.5 Build the clause version graph

In `parsed_json/clause_versions.json`, maintain a version history per clause:

```json
{
  "clause_registry": {
    "ITT-13.2": {
      "base_version": {
        "text": "...",
        "source": "Vol1DLNP1.pdf",
        "pdf_page": 15
      },
      "versions": [
        {
          "addendum": 2,
          "effective_date": "2026-10-15",
          "action": "replace",
          "text": "..."
        }
      ],
      "effective_text": "...",
      "effective_as_of": "2026-10-15"
    }
  }
}
```

The `effective_text` field always reflects the current legal text. This is what the RAG pipeline embeds (see T14 for retrieval-side handling).

---

## Acceptance Criteria

- [ ] All 3 addendum PDFs parsed into `parsed_json/addenda/addendum_{1,2,3}.json`
- [ ] Each delta entry has: `delta_id`, `affected_clause`, `action`, `original_text`, `revised_text`, `effective_date`
- [ ] `stale_after` set in OKF frontmatter of every section affected by any addendum
- [ ] `clause_versions.json` built with all addendum modifications applied
- [ ] `effective_text` in `clause_versions.json` matches the final legal text (verified against addendum PDFs)
- [ ] OKF addendum files created and linked from `OKF_bundle/Technical/Addenda/index.md`
- [ ] Addenda directory linked from bundle root `index.md`

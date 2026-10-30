# T03 — Fix OKF Bundle Structure and Frontmatter

**Phase:** 1 — Data Foundation  
**Priority:** P1 — High   
**Depends on:** Nothing — start immediately (no pipeline code needed)  
**Status:** Not started

---

## Context

Google Cloud's **Open Knowledge Format (OKF) v0.2** (published June 2026) is the specification this project's markdown bundle is built on. An OKF bundle is a directory of markdown files with YAML frontmatter, interconnected by markdown links, that an AI agent can traverse without any SDK or vector database.

The 18 existing markdown files in `OKF_bundle/Technical/` implement the OKF pattern correctly in spirit but have 8 specific compliance gaps that prevent an AI agent from traversing the bundle correctly:

1. `status: source-derived` — not a valid OKF enum value
2. No `description` field — agent cannot preview file relevance without opening it
3. No `resource` field — no pointer to the underlying PDF asset
4. No `generated` block — no record of who/what created the file
5. No `verified` block — review status is buried in JSON, not in the OKF layer
6. No `stale_after` — addendum-affected sections have no staleness signal
7. No `sources` provenance block — SHA-256 is in JSON but not in OKF frontmatter
8. No inter-file links — files are isolated; the OKF graph layer is completely unused

Additionally, the bundle is missing its structural files:
- No `index.md` at bundle root or volume level
- No `log.md`
- No `okf_version` declaration

---

## OKF v0.2 Spec Summary (Reference)

**Required:** `type` (only mandatory field)  
**Recommended:** `title`, `description`, `resource`, `tags`  
**Trust families:**
- `sources` — derivation materials with SHA-256 and author
- `generated` — who/what wrote this file and when (`process:<id>` or `human:<id>`)
- `verified` — list of confirmation events (empty list = unverified tier)
- `status` — lifecycle: `draft | stable | deprecated`
- `stale_after` — ISO 8601 absolute instant after which content may be outdated

**Bundle structure:**
- `index.md` at each directory level: curated entry point for agent traversal
- `log.md`: change history
- Inter-file links: standard markdown links, preferably bundle-relative (`/OKF_bundle/Technical/Vol1/secA.md`)

---

## Goal

All 18 OKF markdown files are fully OKF v0.2-compliant. Bundle has `index.md` files and inter-file links. An AI agent can enter at `index.md`, read the type and description of each section without opening it, and follow links to navigate the full tender document graph.

---

## Compliant Frontmatter Template

Apply this template to all 18 files, substituting the correct values per file:

```yaml
---
okf_version: "0.2"
type: tender_section
title: "Section A — Notice Inviting Tender"
description: "NIT for BMRCL Phase-3 demolition package DLN-P1: key commercial terms, EMD, fees, submission dates, and eligibility pointer."
status: draft
stale_after: "2027-03-31T00:00:00Z"
resource: /BMRCL_TenderData/Tender_Documents/Vol1DLNP1.pdf
tags:
  - nit
  - bmrcl
  - government-procurement
  - phase-3
sources:
  - path: /BMRCL_TenderData/Tender_Documents/Vol1DLNP1.pdf
    author: "BMRCL"
    last_modified: "2026-09-09"
    sha256: "74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c"
generated:
  by: process:pdf-extraction-pipeline
  at: "2026-10-27T00:00:00Z"
verified: []
# Project-specific extensions (OKF-legal: unknown keys are tolerated)
tender_no: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157
section: A
clause_range: "Key Details 1-15; Instructions 1-8"
pdf_pages: "7-8"
---
```

**SHA-256 values by volume:**
- Vol1: `74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c`
- Vol2: `e44cc4945aec704af8350cca6388b3fe3b741d76577f7da70cee6a836662582b`
- Vol3: look up from `parsed_json/vol3/part_1_she_management/she_management_clauses.json`

---

## Tasks

### 3.1 Write a frontmatter update script

Build `scripts/fix_okf_frontmatter.py` that reads each `.md` file, parses the YAML frontmatter, applies the required fields, and rewrites the file.

```python
import yaml
import re
from pathlib import Path
from datetime import datetime

VOLUME_SHA = {
    1: "74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c",
    2: "e44cc4945aec704af8350cca6388b3fe3b741d76577f7da70cee6a836662582b",
    3: "<fill in>",
}

def fix_frontmatter(md_path: Path, volume: int) -> None:
    content = md_path.read_text(encoding="utf-8")
    # parse existing frontmatter
    # apply fixes: status, description, resource, generated, verified, sources, stale_after
    # rewrite file
    ...
```

Run it against all 18 files. Commit the script alongside the updated files.

---

### 3.2 Fix `status` field

Change `status: source-derived` → `status: draft` on all 18 files.  
After T02 (human review) is complete for a file, update to `status: stable`.

---

### 3.3 Add `description` field

Write a one-sentence summary for each file. The description should answer: "What does this section contain and why would an agent open it?"

Examples:
- `secA.md`: `"NIT for BMRCL Phase-3 demolition package DLN-P1: key commercial terms, EMD amount (₹7.11L), submission dates, and eligibility pointer."`
- `secC.md`: `"Eligibility qualification criteria (EQC) with financial thresholds — at least one similar work ≥ ₹3.79 Crores in last 7 years."`
- `secE.md`: `"General Conditions of Contract (GCC) — 31 clauses governing contract execution, payment, variations, suspension, and termination."`

---

### 3.4 Add `resource`, `sources`, and `generated` blocks

Apply as per the template above. The `generated.at` timestamp should reflect when the file was produced (check git history: commit `75bd87a` "Add parsed JSON for BMRCL Volumes 1–3" dated 2026-10-27).

---

### 3.5 Add `stale_after` field

For sections not affected by any addendum, set a conservative date (e.g., one year from tender notice: `2027-09-09T00:00:00Z`).

For sections that will be superseded once addendums are processed (T06), come back and set `stale_after` to the addendum publication date.

---

### 3.6 Create bundle `index.md` files

**`OKF_bundle/Technical/index.md`** — bundle root entry point:

```yaml
---
okf_version: "0.2"
type: index
title: "BMRCL Tender AI — Knowledge Bundle"
description: "Complete OKF knowledge bundle for BMRCL tender DLN-P1/2026/157. Entry point for agent traversal."
tender_no: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157
---

# BMRCL Tender AI — Knowledge Bundle

Tender: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157  
Scope: Partial and Full Demolition of Buildings, JP Nagar 4th Phase to Mysore Road Station

## Volumes

- [Volume 1 — Contract and Legal](/OKF_bundle/Technical/Vol1/index.md)
- [Volume 2 — Scope and Technical Specifications](/OKF_bundle/Technical/Vol2/index.md)
- [Volume 3 — SHE Plan](/OKF_bundle/Technical/Vol3/index.md)
```

**`OKF_bundle/Technical/Vol1/index.md`:**

```yaml
---
type: index
title: "Volume 1 — Contract and Legal"
description: "Contract structure, eligibility, instructions to tenderers, GCC, SCC, and bid forms."
---

# Volume 1 — Contract and Legal

- [Section A — Notice Inviting Tender (NIT)](/OKF_bundle/Technical/Vol1/secA.md) — Key commercial terms, EMD, dates
- [Section B — Instructions to Tenderers (ITT)](/OKF_bundle/Technical/Vol1/secB.md) — Submission rules, evaluation process
- [Section C — Eligibility Qualification Criteria (EQC)](/OKF_bundle/Technical/Vol1/secC.md) — Financial thresholds, experience requirements
- [Section D — Technical Bid Forms](/OKF_bundle/Technical/Vol1/secD.md) — Attachments 6–12, submission checklist
- [Section E — General Conditions of Contract (GCC)](/OKF_bundle/Technical/Vol1/secE.md) — 31 contract clauses
- [Section F — Special Conditions of Contract (SCC)](/OKF_bundle/Technical/Vol1/secF.md) — Project-specific modifications to GCC
- [Section G — Contract Forms](/OKF_bundle/Technical/Vol1/secG.md) — Agreement and bank guarantee forms
```

Create similar `index.md` files for Vol2 and Vol3.

---

### 3.7 Add inter-file markdown links

Add a **"Related Sections"** block at the bottom of each file body with links to directly related sections. Use bundle-relative paths (`/OKF_bundle/Technical/...`).

Required links (minimum):

| File | Must link to |
|---|---|
| `secA.md` (NIT) | `secB.md` (ITT instructions), `secC.md` (EQC eligibility) |
| `secB.md` (ITT) | `secC.md` (EQC), `secD.md` (bid forms), `secE.md` (GCC) |
| `secC.md` (EQC) | `secD.md` (evidence forms), `secB.md` (evaluation clauses 18–22) |
| `secD.md` (forms) | `secC.md` (criteria the forms evidence), `secG.md` (contract forms) |
| `secE.md` (GCC) | `secF.md` (SCC modifications), `secG.md` (contract forms) |
| `Vol2/part3.md` (scope) | `Vol2/part1.md` (general), `Vol2/appendices` (milestones, personnel) |
| `Vol3/part1.md` (SHE) | `Vol3/part2.md` (safety), `Vol3/part5.md` (penalties) |

---

### 3.8 Write an OKF frontmatter linter

Create `scripts/lint_okf.py` — validates all `.md` files in the bundle:

```python
REQUIRED_FIELDS = ["type", "title", "description", "status", "resource", "generated", "verified"]
VALID_STATUS = {"draft", "stable", "deprecated"}

def lint_file(path: Path) -> list[str]:
    """Returns list of error strings. Empty = compliant."""
    ...
```

Exit code 1 if any file fails. This will become part of the CI pipeline (T16).

---

## Acceptance Criteria

- [ ] All 18 `.md` files pass `scripts/lint_okf.py` with zero errors
- [ ] `status` field on all files is `draft`, `stable`, or `deprecated` (none use `source-derived`)
- [ ] All files have non-empty `description`, `resource`, `sources`, `generated`, and `verified` fields
- [ ] `index.md` exists at bundle root and in each volume directory
- [ ] Each `index.md` lists all concept files in its directory with links
- [ ] All inter-file links in the required links table above are present
- [ ] Links use bundle-relative paths starting with `/OKF_bundle/`
- [ ] `okf_version: "0.2"` declared in bundle-root `index.md`

---

## Resources

- OKF v0.2 spec: github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
- OKF bundle examples: okf.md/examples/
- `pyyaml` docs for frontmatter parsing

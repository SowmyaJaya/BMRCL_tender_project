# T01 — Commit the Ingestion Pipeline

**Phase:** 1 — Data Foundation  
**Priority:** P0 — Critical   
**Depends on:** Nothing — start immediately  
**Status:** Not started

---

## Context

The `parsed_json/` and `OKF_bundle/` directories contain ~40 JSON files and 18 markdown files extracted from the BMRCL tender PDFs. These are the outputs of an extraction pipeline. That pipeline — the Python code that reads PDFs, extracts tables, generates OKF markdown, and serialises clause-level JSON — **does not exist in the repository**. It was run locally and never committed.

This is the highest-priority gap in the entire project. Without this code:
- If a PDF changes (e.g., an addendum supersedes it), there is no way to re-extract without reverse-engineering the process
- There is no way to onboard a new tender
- Dependencies are unknown — nobody can set up the environment

The JSON files give strong clues about what the pipeline did: PyMuPDF was used (`bbox` coordinates are in PyMuPDF point format), table detection used `extraction_method: "detected_table_with_direct_cell_text"`, and page rotation was handled. The OKF frontmatter shows YAML generation with volume/section metadata.

---

## Current State

```
repository/
├── BMRCL_TenderData/    ← raw PDFs (committed)
├── OKF_bundle/          ← output markdown (committed, no code)
├── parsed_json/         ← output JSON (committed, no code)
└── [NO CODE]            ← the pipeline that produced the above is missing
```

---

## Goal

A Python package in the repository that can reproducibly extract OKF markdown and structured JSON from any BMRCL-format tender PDF set.

```
repository/
├── src/
│   └── bmrcl_pipeline/
│       ├── __init__.py
│       ├── pdf_reader.py        ← PyMuPDF text + table extraction
│       ├── table_extractor.py   ← coordinate-aware table parsing
│       ├── okf_generator.py     ← produces OKF-compliant markdown
│       ├── json_serializer.py   ← produces clause-level JSON
│       └── cli.py               ← CLI entrypoint
├── requirements.txt
├── pyproject.toml
└── README.md (updated with setup instructions)
```

---

## Tasks

### 1.1 Reconstruct the PDF reader

Reverse-engineer from the JSON output what the PDF reader was doing.

- Set up `fitz` (PyMuPDF) as the base reader
- Implement `extract_pages(pdf_path) → List[PageData]` where `PageData` carries: `page_number`, `rotation`, `text_blocks` (with `bbox`), `raw_text`
- Verify the SHA-256 hashing: `hashlib.sha256(open(pdf_path, 'rb').read()).hexdigest()` — must match `source_sha256` in existing JSON files
- Handle rotated pages (Vol1 Section C EQC tables are likely rotated 90°)

```python
# src/bmrcl_pipeline/pdf_reader.py
import fitz
import hashlib
from dataclasses import dataclass

@dataclass
class PageData:
    page_number: int        # 1-indexed (matches pdf_page in JSON)
    rotation: int           # degrees: 0, 90, 180, 270
    text_blocks: list       # list of {bbox, text, block_number}
    raw_text: str

def compute_sha256(pdf_path: str) -> str:
    with open(pdf_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def extract_pages(pdf_path: str) -> list[PageData]:
    ...
```

**Acceptance:** Running `extract_pages("BMRCL_TenderData/Tender_Documents/Vol1DLNP1.pdf")` and hashing the file must produce `74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c`.

---

### 1.2 Reconstruct the table extractor

The existing JSON stores table rows as fragments with `physical_row`, `column`, `bbox`, and `table_id`. Reconstruct the table detection logic.

- Implement `detect_tables(page: PageData) → List[TableData]` using heuristic column alignment (text blocks that share similar x-coordinates across rows)
- Implement `extract_table_rows(table: TableData) → List[Dict]` that produces the `fragments` structure seen in `eqc_criteria.json`
- Handle multi-line cells (text that wraps across PyMuPDF text blocks within the same logical cell)

**Note:** Look at `parsed_json/vol1/section_c_eqc/eqc_tables.json` for the expected output structure. The `table_bbox` field shows the bounding box of the full table; column bboxes show how columns were detected.

---

### 1.3 Build the OKF markdown generator

Given extracted page data and section metadata, produce a valid OKF v0.2-compliant markdown file.

- Implement `generate_okf_file(section_meta: dict, content: str) → str`
- Frontmatter must include: `type`, `title`, `description`, `status: draft`, `resource`, `tags`, `sources` (with SHA-256), `generated`, `verified: []`, plus project-specific fields (`tender_no`, `section`, `clause_range`, `pdf_pages`)
- Body must use standard markdown headings
- File must be written to `OKF_bundle/Technical/Vol{n}/` with the appropriate filename

See [T03](T03-okf-compliance-fix.md) for the exact OKF frontmatter template.

---

### 1.4 Build the JSON serializer

Given extracted and table-parsed data, produce the clause-level JSON structure.

- Implement `serialize_section(section_data) → dict` that produces the structure matching existing JSON files
- Always include: `source_id`, `source_path`, `source_sha256`, `section`, `title`, `review_status: "pending_manual_review"`, `extraction_method`
- For clause arrays, include `criterion_id` / clause number as first-class keys (these become RAG chunk boundaries)

---

### 1.5 Build the CLI entrypoint

```bash
python -m bmrcl_pipeline extract \
  --pdf BMRCL_TenderData/Tender_Documents/Vol1DLNP1.pdf \
  --volume 1 \
  --output-okf OKF_bundle/Technical/Vol1/ \
  --output-json parsed_json/vol1/
```

- Accept `--dry-run` flag (validate but do not write)
- Accept `--force-reextract` flag (re-extract even if output already exists)
- Print a summary: pages processed, tables detected, OKF files written, JSON files written

---

### 1.6 Set up packaging

Create `requirements.txt` with pinned versions:

```
pymupdf==1.24.x
pyyaml==6.0.x
click==8.1.x
xlrd==2.0.x       # for BOQ Excel (Task T05)
```

Create `pyproject.toml` with project metadata. Create or update `README.md` with setup instructions (`pip install -r requirements.txt`, then CLI usage).

---

## Acceptance Criteria

- [ ] Running the pipeline on `Vol1DLNP1.pdf` produces JSON that, when SHA-256 compared against `source_sha256` in existing JSON files, matches exactly
- [ ] All existing JSON files can be regenerated from scratch by the pipeline
- [ ] `requirements.txt` exists with pinned versions
- [ ] A new developer can set up the environment with `pip install -r requirements.txt` and run the pipeline in under 10 minutes
- [ ] The CLI has a `--help` flag with usage instructions

---

## Resources

- PyMuPDF documentation: `fitz.open()`, `page.get_text("dict")`, `page.get_text("blocks")`
- Existing JSON for reference: `parsed_json/vol1/section_c_eqc/eqc_criteria.json` (complex table example), `parsed_json/vol1/section_a_nit/nit_items.json` (simple text example)
- OKF v0.2 spec: github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

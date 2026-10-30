# T04 — Process Vol 4 (Drawings) into OKF + JSON

**Phase:** 1 — Data Foundation  
**Priority:** P1 — High  
**Effort:** 1–2 weeks  
**Depends on:** T01 (ingestion pipeline committed)  
**Status:** Not started

---

## Context

`BMRCL_TenderData/Tender_Documents/Vol4DLNP1.pdf` exists but has **no OKF markdown and no JSON representation**. Vol 4 of a BMRCL demolition tender typically contains:
- Site plans and corridor alignment drawings
- Structural drawings of buildings to be demolished
- Utility clearance layouts
- Milestone-linked work completion maps

Bidders need this volume to price the BOQ accurately (e.g., estimating cubic metres of RCC to demolish requires the drawings). A tender AI that cannot answer questions about the drawings corpus is incomplete.

**The challenge:** Drawing PDFs are mostly image-based (scanned engineering drawings). PyMuPDF's text extraction will produce little or no usable text. A different extraction approach is needed.

---

## Tasks

### 4.1 Inspect Vol 4 to determine its content type

```python
import fitz
doc = fitz.open("BMRCL_TenderData/Tender_Documents/Vol4DLNP1.pdf")
for page in doc:
    text = page.get_text("text")
    print(f"Page {page.number+1}: {len(text)} chars, {len(page.get_images())} images")
```

Based on the output, choose one of two extraction paths:

**Path A (text-extractable):** If Vol 4 contains schedules, tables, and annotated text, use the standard PyMuPDF pipeline from T01.

**Path B (image-dominant):** If Vol 4 is mostly scanned engineering drawings, use OCR with layout analysis (Azure Document Intelligence or AWS Textract). Extract: drawing title blocks (drawing number, scale, revision), annotation text (dimensions, material callouts), and table data from title block schedules.

---

### 4.2 Path A — Text extraction (if applicable)

Apply the standard T01 pipeline. Produce:
- `OKF_bundle/Technical/Vol4/` with OKF markdown files
- `parsed_json/vol4/` with structured JSON

Add Vol4 to the bundle root `index.md`.

---

### 4.3 Path B — OCR extraction (if image-dominant)

Set up Azure Document Intelligence (or AWS Textract as fallback):

```python
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

client = DocumentAnalysisClient(endpoint=ENDPOINT, credential=AzureKeyCredential(KEY))

with open("BMRCL_TenderData/Tender_Documents/Vol4DLNP1.pdf", "rb") as f:
    poller = client.begin_analyze_document("prebuilt-layout", f)
result = poller.result()
```

For each page, extract:
- Tables (Azure DI returns structured table objects)
- Key-value pairs from title blocks
- Paragraph text from notes and specifications

Produce a JSON schema for drawings:

```json
{
  "source_id": "bmrcl-volume-4",
  "source_sha256": "...",
  "extraction_method": "azure-document-intelligence-layout",
  "drawings": [
    {
      "page": 1,
      "drawing_number": "BMRCL-DLN-P1-001",
      "title": "Site Plan — JP Nagar 4th Phase Station",
      "scale": "1:500",
      "revision": "R0",
      "annotations": ["..."],
      "review_status": "pending_manual_review"
    }
  ]
}
```

---

### 4.4 Create OKF files for Vol 4

Create `OKF_bundle/Technical/Vol4/index.md` and one concept file per drawing set (group by corridor segment or structure type).

OKF type for drawings: `type: tender_drawing_set`

---

### 4.5 Add Vol 4 to bundle index

Update `OKF_bundle/Technical/index.md` to include:
```markdown
- [Volume 4 — Drawings and Site Plans](/OKF_bundle/Technical/Vol4/index.md)
```

---

## Acceptance Criteria

- [ ] Vol 4 PDF inspected and extraction path documented
- [ ] All pages of Vol 4 represented in either OKF markdown or a structured JSON drawing index
- [ ] Each drawing entry has: drawing number, page reference, extraction method, `review_status`
- [ ] Vol 4 linked from bundle root `index.md`
- [ ] SHA-256 of Vol4 PDF captured in `source_sha256`

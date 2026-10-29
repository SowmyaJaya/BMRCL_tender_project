# T05 — Parse BOQ Excel into Structured JSON

**Phase:** 1 — Data Foundation  
**Priority:** P1 — High  
**Effort:** 2–3 days  
**Depends on:** Nothing — start immediately (pure Python, no pipeline dependency)  
**Status:** Not started

---

## Context

`BMRCL_TenderData/Tender_Documents/BOQ_338417.xls` is the **Bill of Quantities** — the financial skeleton of the tender. It lists every unit of work that bidders must price. For the demolition tender, this includes items like: cubic metres of RCC demolition, linear metres of boundary wall removal, number of structures to be dismantled, debris disposal quantities, etc.

This is arguably the single most important document for a bidder using an AI system. Common queries include:
- "What is the total estimated quantity of RCC demolition?"
- "Which BOQ items are linked to Milestone 1?"
- "What is the unit rate for debris disposal?"
- "What is the total estimated contract value?"

The file uses `.xls` format (not `.xlsx`) — an older Excel format. Use `xlrd` library (not `openpyxl`, which does not support `.xls`).

---

## Tasks

### 5.1 Inspect the BOQ structure

```python
import xlrd

wb = xlrd.open_workbook("BMRCL_TenderData/Tender_Documents/BOQ_338417.xls")
print("Sheets:", wb.sheet_names())
for sheet in wb.sheets():
    print(f"\n--- {sheet.name} ({sheet.nrows} rows x {sheet.ncols} cols) ---")
    for i in range(min(10, sheet.nrows)):
        print([sheet.cell_value(i, j) for j in range(sheet.ncols)])
```

Document the structure: sheet names, column headers, hierarchy (sections → sub-sections → line items), merged cell handling.

---

### 5.2 Parse BOQ into structured JSON

Expected JSON schema:

```json
{
  "source_id": "bmrcl-boq",
  "source_path": "data/BOQ_338417.xls",
  "source_sha256": "...",
  "tender_no": "BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157",
  "title": "Bill of Quantities",
  "extraction_method": "xlrd-structured-parse",
  "review_status": "pending_manual_review",
  "sheets": [
    {
      "sheet_name": "...",
      "sections": [
        {
          "section_code": "A",
          "section_title": "Demolition Works",
          "items": [
            {
              "item_code": "A-001",
              "description": "Demolition of RCC structure including...",
              "unit": "Cum",
              "estimated_quantity": 150.0,
              "unit_rate": null,
              "amount": null,
              "notes": ""
            }
          ]
        }
      ]
    }
  ]
}
```

Note: `unit_rate` and `amount` are typically blank in the issued BOQ (bidders fill these in). Capture them as `null` if empty.

---

### 5.3 Handle merged cells

BOQ Excel files typically use merged cells for section headers. `xlrd` reads these as non-empty in the first cell and empty in subsequent cells. Implement a forward-fill for merged section headers:

```python
def forward_fill_merged(sheet, row_idx, col_idx):
    """Returns cell value, filling forward from last non-empty cell in column."""
    val = sheet.cell_value(row_idx, col_idx)
    if val == '':
        # look up from previous rows
        ...
    return val
```

---

### 5.4 Create OKF file for BOQ

Create `OKF_bundle/Technical/BOQ/index.md`:

```yaml
---
okf_version: "0.2"
type: bill_of_quantities
title: "Bill of Quantities — DLN-P1"
description: "Priced schedule of quantities for all demolition works. Line items grouped by work type with estimated quantities and units."
status: draft
resource: /BMRCL_TenderData/Tender_Documents/BOQ_338417.xls
sources:
  - path: /BMRCL_TenderData/Tender_Documents/BOQ_338417.xls
    sha256: "..."
generated:
  by: process:boq-excel-parser
  at: "..."
verified: []
tender_no: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157
---
```

Link the BOQ from `OKF_bundle/Technical/index.md` and from `Vol2/part3.md` (scope of work).

---

## Acceptance Criteria

- [ ] `xlrd.open_workbook()` successfully reads the file without errors
- [ ] All BOQ line items parsed into JSON with: `item_code`, `description`, `unit`, `estimated_quantity`
- [ ] Merged section headers handled (no blank `section_title` values)
- [ ] SHA-256 of `BOQ_338417.xls` captured in JSON
- [ ] OKF file created and linked from bundle index
- [ ] Running the parser twice on the same file produces identical output (deterministic)

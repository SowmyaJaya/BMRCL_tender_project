# T15 — Multi-Tender Namespace Architecture

**Phase:** 3 — API and Application  
**Priority:** P2 — Medium  
**Effort:** 2 weeks  
**Depends on:** T09 (vector store schema designed with tender_id from the start), T13 (API endpoint)  
**Status:** Not started

---

## Context

The current project supports one tender (`DLN-P1`). A production system for BMRCL or a procurement consultancy must support multiple tenders simultaneously — for example, comparing EQC thresholds across DLN-P1, DLN-P2, and a road contract tender.

The vector store already stores `tender_id` as a metadata field (T09). This task builds the tender registry and the cross-tender query capability on top of it.

---

## Tasks

### 15.1 Build a tender registry

Create `data/tender_registry.json`:

```json
{
  "tenders": {
    "BMRCL-DLN-P1-2026-157": {
      "display_name": "BMRCL Phase-3 DLN-P1 Demolition",
      "tender_no": "BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157",
      "organisation": "BMRCL",
      "scope": "Demolition of buildings, JP Nagar to Mysore Road",
      "estimated_value_inr_crores": 4.74,
      "okf_bundle_path": "OKF_bundle/Technical/",
      "json_store_path": "parsed_json/",
      "status": "active",
      "indexed_at": "2026-10-28T00:00:00Z",
      "chunk_count": 342
    }
  }
}
```

Add a `/tenders` endpoint to list all registered tenders:

```python
@router.get("/tenders")
async def list_tenders():
    return {"tenders": load_tender_registry()}
```

### 15.2 Implement tender onboarding pipeline

Create a CLI command that takes a raw PDF set and produces OKF + JSON + embeddings:

```bash
python -m bmrcl_pipeline onboard \
  --tender-id "BMRCL-DLN-P2-2026-158" \
  --pdf-dir raw_pdfs/DLN-P2/ \
  --volume-map vol1=Contract.pdf vol2=Specs.pdf vol3=SHE.pdf \
  --output-base tenders/DLN-P2/
```

This runs the full pipeline: extract → OKF → JSON → chunk → embed → register.

### 15.3 Implement cross-tender comparison query

Extend the `/query` endpoint to support querying across multiple tenders:

```python
class QueryRequest(BaseModel):
    ...
    tender_ids: list[str] | None = None   # None = single tender_id; list = multi-tender
    comparison_mode: bool = False          # if True, format answer as comparison table
```

Example: "Compare the EQC financial thresholds across DLN-P1 and DLN-P2."

The retrieval runs separately per tender, results are merged, and the LLM is prompted to produce a comparison.

### 15.4 Isolate OKF bundles per tender

When onboarding a new tender, create its OKF bundle under:
```
tenders/{tender_id}/OKF_bundle/
tenders/{tender_id}/parsed_json/
```

The bundle root `index.md` declares the tender_id:
```yaml
okf_version: "0.2"
type: index
tender_id: "BMRCL-DLN-P2-2026-158"
```

---

## Acceptance Criteria

- [ ] Tender registry JSON exists and is used by the API
- [ ] `/tenders` endpoint lists all registered tenders
- [ ] Query with `tender_id: "BMRCL-DLN-P1"` only returns chunks from DLN-P1
- [ ] Query with `tender_ids: ["DLN-P1", "DLN-P2"]` returns results from both
- [ ] Onboarding CLI successfully processes a second mock tender without affecting DLN-P1 data

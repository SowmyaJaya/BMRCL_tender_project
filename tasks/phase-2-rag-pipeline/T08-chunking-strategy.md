# T08 — Design and Implement Clause-Level Chunking

**Phase:** 2 — RAG Pipeline  
**Priority:** P0 — Critical  
**Effort:** 3–5 days  
**Depends on:** T01 (pipeline), T02 (data reviewed — do not embed unreviewed data)  
**Status:** Not started

---

## Context

Chunking is the most consequential design decision in the RAG pipeline. For legal and tender documents, the wrong chunking strategy produces retrieval that **fails under scrutiny**: fragments of clauses that sound plausible but are legally incorrect.

**Why fixed-size chunking fails for tender documents:**

A standard 512-token chunk boundary has a roughly 50% chance of landing mid-clause on a 1000-token GCC clause. The result is three chunks: the end of the previous clause + the start of the target clause, the middle of the target clause, and the end of the target clause + start of the next clause. None of these is a clean, legally coherent unit. When an LLM is asked "under what conditions can BMRCL suspend the contract?", it retrieves the middle chunk of GCC Clause 8.8 — which has no subject (the subject was in the first chunk) and no consequence (which was in the third chunk) — and produces an answer that sounds authoritative but is incomplete.

**The correct approach for this corpus:** Clause-level chunking using the existing JSON structure as chunk boundaries. The JSON files already have natural chunk identifiers: `criterion_id` (e.g., `3.1.A.(i)`), clause numbers, and section codes. These are the legal units of reasoning and must be preserved as atomic chunks.

**Research confirmation (2026):** "Clause-level retrieval is the right primitive for contract review, not chunk-level. A contract review agent without clause-citation eval is a liability, not a tool." — FutureAGI, 2026.

---

## Chunk Design

### Chunk schema

```python
from dataclasses import dataclass

@dataclass
class TenderChunk:
    chunk_id: str          # deterministic: "{tender_id}/{section}/{clause_id}"
    text: str              # the full clause text, no truncation
    metadata: dict         # used for filtering in retrieval
```

```python
# metadata structure
{
    "tender_id": "BMRCL-DLN-P1-2026-157",
    "volume": 1,
    "section": "C",
    "section_title": "Eligibility Qualification Criteria",
    "clause_id": "3.1.A.(i)",
    "okf_type": "tender_section",
    "okf_status": "draft",           # or "stable" post-review
    "verified_tier": "unverified",   # or "human-reviewed"
    "pdf_page": 32,
    "source_sha256": "74441e...",
    "stale": False,                  # True if stale_after has passed
    "addendum_delta": None,          # or {"addendum_number": 2, "effective_date": "..."}
}
```

### Chunk boundaries by JSON file type

| JSON file type | Chunk boundary | Chunk ID pattern |
|---|---|---|
| `eqc_criteria.json` | Each `criteria[]` item | `{tender}/{section}/eqc/{criterion_id}` |
| `gcc_clauses.json` | Each `clauses[]` item | `{tender}/{section}/gcc/{clause_number}` |
| `itt_clauses.json` | Each `clauses[]` item | `{tender}/{section}/itt/{clause_number}` |
| `scc_entries.json` | Each `entries[]` item | `{tender}/{section}/scc/{clause_number}` |
| `milestones.json` | Each `milestones[]` row | `{tender}/annexure-1/milestone/{serial_number}` |
| `scope_clauses.json` | Each `clauses[]` item | `{tender}/vol2/scope/{clause_number}` |
| `nit_items.json` | Each `key_details[]` item | `{tender}/nit/item/{number}` |
| `safety_clauses.json` | Each `clauses[]` item | `{tender}/vol3/safety/{clause_number}` |

### Parent-document retrieval (two-level chunking)

For very long clauses (>800 tokens), implement two-level chunks:
- **Small chunk** (256–400 tokens): optimised for retrieval precision — the specific sub-clause
- **Parent chunk** (full clause): returned as context to the LLM after retrieval

This is the 2026 best practice for legal documents: retrieve small, generate with large context.

---

## Tasks

### 8.1 Build the chunk extractor

```python
# src/bmrcl_pipeline/chunker.py

def extract_chunks_from_json(json_path: Path, tender_id: str) -> list[TenderChunk]:
    """
    Reads a reviewed JSON file and extracts clause-level chunks.
    Raises if review_status == 'pending_manual_review'.
    """
    data = json.loads(json_path.read_text())
    
    if data.get("review_status") == "pending_manual_review":
        raise ValueError(f"Cannot chunk unreviewed file: {json_path}")
    
    chunks = []
    # dispatch by file type / section
    if "criteria" in data:
        chunks.extend(_chunk_eqc_criteria(data, tender_id))
    elif "clauses" in data:
        chunks.extend(_chunk_clauses(data, tender_id))
    # ... etc
    return chunks
```

### 8.2 Build chunk ID generator

Chunk IDs must be **deterministic and stable**: the same source data always produces the same chunk ID. This allows updates (re-embed a changed clause) without full re-indexing.

```python
def make_chunk_id(tender_id: str, section: str, clause_id: str) -> str:
    """
    Returns a stable, URL-safe chunk ID.
    Example: "BMRCL-DLN-P1-2026-157/vol1-C/eqc-3.1.A.i"
    """
    safe_clause = clause_id.replace(".", "-").replace("(", "").replace(")", "")
    return f"{tender_id}/{section}/{safe_clause}"
```

### 8.3 Handle addendum-superseded clauses

If a chunk's clause has an entry in `clause_versions.json`, use the `effective_text` as the chunk text (not the base text), and add the addendum metadata:

```python
if clause_id in clause_versions:
    text = clause_versions[clause_id]["effective_text"]
    metadata["addendum_delta"] = {
        "addendum_number": clause_versions[clause_id]["versions"][-1]["addendum"],
        "effective_date": clause_versions[clause_id]["effective_as_of"]
    }
```

### 8.4 Write a chunk manifest

After extraction, write `parsed_json/chunk_manifest.json`:

```json
{
  "tender_id": "BMRCL-DLN-P1-2026-157",
  "generated_at": "...",
  "total_chunks": 342,
  "chunks_by_volume": {"1": 180, "2": 120, "3": 42},
  "unreviewed_chunks_blocked": 0,
  "stale_chunks": 5
}
```

### 8.5 Write tests for the chunker

```python
def test_eqc_criterion_chunk_id_stable():
    """Same input always produces same chunk_id."""

def test_unreviewed_file_raises():
    """extract_chunks_from_json raises on pending_manual_review."""

def test_addendum_superseded_clause_uses_effective_text():
    """Chunk text for superseded clause comes from clause_versions.json."""

def test_no_mid_clause_truncation():
    """No chunk text ends with an incomplete sentence or unclosed parenthesis."""
```

---

## Acceptance Criteria

- [ ] Chunker processes all reviewed JSON files without error
- [ ] Chunker raises `ValueError` on any `pending_manual_review` file
- [ ] All chunk IDs are deterministic (run twice, get same IDs)
- [ ] Chunk text for addendum-affected clauses uses `effective_text` from `clause_versions.json`
- [ ] Chunk manifest generated with correct total count
- [ ] All tests pass
- [ ] No chunk text is truncated mid-sentence

---

## Resources

- "Chunking Strategies for Legal & Reference RAG Systems": edtek.ai/kb/chunking-strategies-legal-reference-documents/
- "How to Build a Contract Review RAG Agent (2026)": futureagi.com/blog/contract-review-rag-build-evaluate-2026/
- Existing JSON structure: `parsed_json/vol1/section_c_eqc/eqc_criteria.json` (clause-level example)

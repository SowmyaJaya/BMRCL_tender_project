# T14 — Implement Addendum-Aware Retrieval

**Phase:** 3 — API and Application  
**Priority:** P1 — High  
**Effort:** 1 week  
**Depends on:** T11 (retrieval chain), T06 (addendums processed into delta JSON)  
**Status:** Not started

---

## Context

Three addendums have been issued for this tender. Addendums legally supersede base-volume clauses. A retrieval system that ignores addendums will return outdated clause text as the answer to a query like "What is the EMD form requirement?" — giving a bidder wrong information if the addendum changed that requirement.

The addendum handling has two sides:
1. **Embedding side (T10):** Embed the `effective_text` (not the base text) for superseded clauses. This is already handled by the chunker in T08.
2. **Retrieval side (this task):** Surface addendum provenance in the response so users know a clause was modified.

This task also handles the case where a user queries an old clause number that was deleted by an addendum — the system should say "Clause X was deleted by Addendum 2" rather than returning nothing.

---

## Tasks

### 14.1 Implement the clause version resolver

```python
def resolve_clause_version(
    clause_id: str,
    clause_versions: dict,
    as_of_date: date | None = None,
) -> dict:
    """
    Returns the effective clause text and provenance as of as_of_date.
    as_of_date defaults to today (= latest effective version).
    """
    if clause_id not in clause_versions:
        return {"clause_id": clause_id, "status": "not_found"}
    
    entry = clause_versions[clause_id]
    if not entry["versions"]:
        return {
            "clause_id": clause_id,
            "text": entry["base_version"]["text"],
            "source": "base_volume",
            "addendum": None,
        }
    
    # Find the latest version effective on or before as_of_date
    applicable = [v for v in entry["versions"] if date.fromisoformat(v["effective_date"]) <= (as_of_date or date.today())]
    if not applicable:
        return {"clause_id": clause_id, "text": entry["base_version"]["text"], "source": "base_volume"}
    
    latest = max(applicable, key=lambda v: v["effective_date"])
    return {
        "clause_id": clause_id,
        "text": latest["text"] if latest["action"] != "delete" else None,
        "source": f"addendum_{latest['addendum']}",
        "addendum": latest["addendum"],
        "effective_date": latest["effective_date"],
        "action": latest["action"],
    }
```

### 14.2 Enrich retrieved chunks with addendum provenance

In the retrieval chain, after retrieving chunks, resolve each chunk's clause version and add the provenance to the source citation:

```python
def enrich_with_addendum_info(chunks: list[ChunkResult], clause_versions: dict) -> list[ChunkResult]:
    for result in chunks:
        clause_id = result.chunk.metadata.get("clause_id")
        if clause_id and result.chunk.metadata.get("has_addendum"):
            version_info = resolve_clause_version(clause_id, clause_versions)
            result.addendum_note = (
                f"Modified by Addendum {version_info['addendum']} "
                f"(effective {version_info['effective_date']})"
            )
    return chunks
```

### 14.3 Handle deleted clauses

If a query retrieves a chunk that was **deleted** by an addendum (action = "delete"), return a special response:

```python
# In the query response:
{
    "answer": "Clause ITT-13.2 was deleted by Addendum 2 (effective 2026-10-15) and is no longer applicable.",
    "sources": [
        {
            "clause_id": "ITT-13.2",
            "stale": True,
            "addendum_note": "DELETED by Addendum 2 (2026-10-15). This clause no longer applies.",
            "clause_text": "[DELETED]"
        }
    ]
}
```

### 14.4 Add `as_of_date` parameter to the query endpoint

Extend `QueryRequest` to support historical queries:

```python
class QueryRequest(BaseModel):
    ...
    as_of_date: date | None = None  # None = latest; set to query a historical state
```

This allows a user to ask: "What was the EMD requirement before Addendum 2?" — useful for auditing.

---

## Acceptance Criteria

- [ ] Query for a superseded clause returns the addendum-effective text, not the base text
- [ ] Source citation for a superseded clause shows `addendum_note` with addendum number and effective date
- [ ] Query for a deleted clause returns a clear deletion message, not a hallucinated answer
- [ ] `as_of_date=2026-10-01` (before Addendum 2) returns the pre-addendum text for affected clauses
- [ ] `as_of_date` defaults to today (latest effective state)

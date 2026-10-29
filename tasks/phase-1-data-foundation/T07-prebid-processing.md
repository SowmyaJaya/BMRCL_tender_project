# T07 — Process Pre-Bid Q&A Replies

**Phase:** 1 — Data Foundation  
**Priority:** P2 — Medium  
**Effort:** 2–3 days  
**Depends on:** T01 (ingestion pipeline)  
**Status:** Not started

---

## Context

`BMRCL_TenderData/RepliesPrebidqueriesDLNP1157.PDF` contains BMRCL's official replies to questions raised by prospective bidders at the pre-bid meeting. These replies are legally binding and often resolve ambiguities in the base documents.

In OKF terms, each Q&A pair is a `type: clarification` concept that links back to the clause or section it clarifies.

---

## Tasks

### 7.1 Extract Q&A pairs

Parse the PDF. The typical structure is a table:

```
S.No | Clause Reference | Query | BMRCL Reply
```

Produce `parsed_json/prebid_replies/prebid_qna.json`:

```json
{
  "source_id": "bmrcl-prebid-replies",
  "source_sha256": "...",
  "review_status": "pending_manual_review",
  "replies": [
    {
      "serial_number": 1,
      "clause_reference": "ITT-4.0",
      "query": "Can a consortium of two companies bid jointly?",
      "reply": "Yes, Joint Ventures are permitted subject to the JV agreement being submitted with the technical bid per clause 9.3.",
      "pdf_page": 2,
      "links_to_okf": "/OKF_bundle/Technical/Vol1/secB.md"
    }
  ]
}
```

### 7.2 Create OKF clarification files

Create `OKF_bundle/Technical/PreBid/prebid_replies.md`:

```yaml
---
okf_version: "0.2"
type: clarification_set
title: "Pre-Bid Query Replies"
description: "Official BMRCL replies to pre-bid queries — legally binding clarifications to base tender documents."
status: stable
resource: /BMRCL_TenderData/RepliesPrebidqueriesDLNP1157.PDF
generated:
  by: process:pdf-extraction-pipeline
  at: "..."
verified: []
---
```

### 7.3 Add cross-links to affected OKF sections

For each reply that references a specific clause, add a link from that OKF section file to `prebid_replies.md`:

```markdown
<!-- In secB.md, at the relevant clause: -->
> **Pre-bid clarification:** See [Pre-Bid Reply #1](/OKF_bundle/Technical/PreBid/prebid_replies.md) for BMRCL's clarification on JV eligibility.
```

---

## Acceptance Criteria

- [ ] All Q&A pairs parsed into `parsed_json/prebid_replies/prebid_qna.json`
- [ ] Each reply has a `clause_reference` linking it to a specific section
- [ ] OKF clarification file created and linked from bundle index
- [ ] High-impact replies (those that change interpretation of EQC, EMD, or milestone clauses) cross-linked from the affected OKF section files

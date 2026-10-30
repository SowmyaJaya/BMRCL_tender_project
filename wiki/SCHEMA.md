---
type: schema
title: "Wiki Schema — BMRCL Tender DLN-P1"
description: "Conventions and workflows for the LLM-maintained wiki: folder layout, page types, citation and link rules, status, supersession, and the no-compliance-decision rule."
status: draft
tender_no: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157
last_updated: "2026-10-30"
---

# Wiki Schema — BMRCL Tender DLN-P1

This file tells the LLM how to build and maintain `wiki/`. Read it before every ingest, query or lint run. If a rule here conflicts with an instruction in a page, this file wins. Change it only on purpose, and log the change in `log.md`.

## 1. Sources and their roles

The wiki is a synthesis layer. It is not a source. Every claim must trace back to one of these sources:

| Layer | Location | Role | Holds |
|---|---|---|---|
| Source documents | `BMRCL_TenderData/` | Authority of last resort | Tender PDFs (Vol 1–4), BOQ workbook, three corrigendum PDFs, pre-bid replies PDF |
| OKF bundle | `OKF_bundle/` | Navigation and link targets | One file per section or part: headings, clause outlines, PDF and booklet page comments. Corrigenda files also hold transcribed old and new values. |
| Parsed JSON | `parsed_json/` | Clause-level detail | Extracted clause text, tables and page numbers. Records carry `review_status` (currently `pending_manual_review` or `pending_visual_review`). |

Rules:

- Most OKF section files are **topic outlines**, not full text. Do not infer clause content from a heading alone. Take wording and values from `parsed_json/`, or from a file that states them explicitly, such as NIT Key Details, the Vol 4 BOQ abstract or a corrigendum.
- `parsed_json/` has no files that cover the pre-bid replies (`RepliesPrebidqueriesDLNP1157.PDF`). Until they are ingested, a wiki page must not suggest that the pre-bid replies have been considered.
- Never add facts from outside these three layers. That includes general knowledge about BMRCL, Indian procurement law or "typical" contract terms.

## 2. Folder layout

```text
wiki/
├── SCHEMA.md                      # this file
├── index.md                       # catalog of every wiki page, one-line summary each
├── log.md                         # append-only ingest / query / lint record
├── cross_reference_master.md      # source clause → target clause, relation type, explicit or inferred
├── commercial_entity_index.md     # money, durations, securities, dates; defining clause + every citing clause
├── contractual_obligation_map.md  # who owes what to whom, by stage; document-precedence chain
├── safety_penalty_network.md      # unsafe act/condition → charges (56.0) → stoppage (57.0) → awards (58.0)
├── parties_and_roles.md           # Employer, Engineer, Consultant, Contractor, appellate authority, contacts
├── glossary.md                    # abbreviations and aliases (e.g. Vol 3 says "BMRC", elsewhere "BMRCL")
├── timeline.md                    # tender calendar (with corrigendum chain) and contract-lifecycle periods
├── source_quirks.md               # known numbering gaps, deletions, OCR or extraction anomalies
├── review_queue.md                # claims resting on pending-review data
├── concepts/                      # cross-cutting synthesis pages, one topic each
└── qa/                            # filed answers to queries
```

File names use `lower_snake_case.md`. Do not create folders that are not listed here without first updating this schema.

## 3. Page types

Every page starts with YAML frontmatter. The opening `---` sits alone on line 1, the file is UTF-8 without a BOM, and `type` is required.

| `type` | Used for | Required extra fields |
|---|---|---|
| `schema` | this file | — |
| `catalog` | `index.md` | — |
| `log` | `log.md` | — |
| `hub` | the root-level map pages (cross-reference, commercial, obligations, safety network, parties, glossary, timeline, quirks, review queue) | `sources`, `last_ingested` |
| `concept` | pages in `concepts/` | `sources`, `last_ingested` |
| `qa` | pages in `qa/` | `question`, `asked`, `sources` |

Common frontmatter:

```yaml
---
type: concept
title: "Tender Security (EMD)"
status: draft            # draft | reviewed  (see section 6)
sources:                 # every OKF file and JSON file this page draws on
  - OKF_bundle/Technical/Vol1/secA.md
  - OKF_bundle/Technical/Vol1/secB.md
  - parsed_json/vol1/section_b_itt/itt_clauses.json
last_ingested: "2026-10-30"
tags: [tender-security, emd]
---
```

### Body layout for `hub` and `concept` pages

1. **Summary.** Two to five sentences synthesised from the sources, with no uncited facts.
2. **Key parameters.** A table of `Parameter | Value | Citation | Status`. Each value gets its own citation. Add `Superseded` or `Pending review` in the status column where it applies.
3. **Where it appears.** Heading links to every source location that defines or cites the topic.
4. **Relations.** Typed links to other wiki pages and source headings (see section 5).
5. **Open questions and contradictions.** Gaps, conflicts between sources, and quirks, each linked to `source_quirks.md` or `review_queue.md`.

### Body layout for `qa` pages

Question, answer, citations, a list of wiki pages used, and caveats. A qa page must not contain a fact that is missing from the cited sources.

## 4. Citation and link rules

### 4.1 Link format (Obsidian)

Use wiki links with the vault-relative path, an exact heading anchor and short display text:

```text
[[OKF_bundle/Technical/Vol1/secB#Clause 13.0 — Tender Security (EMD)|ITT 13.0]]
```

- **Vault root** is the project root (`BMRCL_tender_project/`). Paths start with `OKF_bundle/`, `wiki/` or `parsed_json/`. Leave off the `.md` extension.
- **The anchor** is the full heading text exactly as written in the target file, after the `#` characters. Keep the em dash `—`, capitals and punctuation as they are. For example, the heading is `Clause 13.0 — Tender Security (EMD)`, not `13.0 Tender Security`.
- **Short paths** such as `[[Vol1/secB]]` are not allowed. They only resolve if Obsidian finds a unique match. The two links in `secA.md` already use this short form and are recorded as a lint item (see section 8).
- **Links to other wiki pages** use `[[wiki/concepts/tender_security|Tender Security]]`.
- **Display text** uses the document's own short forms: `ITT 13.0`, `GCC 8.7`, `SCC 3`, `EQC 3.1`, `NIT Key Detail 10`, `Contract Data Item 14`, `Vol 2 Part 3 Clause 15`, `SHE 56.0`, `Corrigendum 2 Change 1`.

### 4.2 Citations

Every factual claim carries a two-part citation, a heading link plus a page:

```text
… is INR 7.11 Lakhs ([[OKF_bundle/Technical/Vol1/secA#Key Detail 2 — Tender Security (EMD)|NIT Key Detail 2]], PDF p. 7)
```

- **Page numbers** are **PDF page numbers of the named source document**. Take them from the `<!-- Source: PDF page … -->` comment under the heading, or from a JSON record's `pdf_page`. Write `PDF p. 7` or `PDF pp. 11–12`.
- **Booklet page numbers** are a different numbering system. Cite them only when they help, and label them: `booklet p. 001`.
- **Corrigendum pages** are pages of the corrigendum PDF itself, not of the volume it amends. Write `AandC2 PDF p. 2`.
- **Narrow ranges.** A heading's comment can span several pages. When a JSON record gives a narrower page, use the JSON page.
- **Multiple sources.** If a claim combines more than one source, cite each one.
- **No uncited claims.** If a claim cannot be cited, leave it out or put it in `review_queue.md` as an open question. Do not write it as fact.
- **Explicit vs inferred.** In `cross_reference_master.md`, mark each relation `explicit` when the source text names the target clause, or `inferred` when it is the LLM's reading. Inferred relations are never written as if they were source text.

## 5. Relations

Allowed relation types: `defines`, `cites`, `modifies`, `deletes`, `replaces`, `supersedes`, `superseded_by`, `clarifies`, `requires`, `evidenced_by`, `governs`, `related_to`, `belongs_to`. Use the same names in frontmatter and in relation tables.

Precedence relations, such as "SCC prevails over GCC", must cite the clause that sets the precedence: the SCC introduction ([[OKF_bundle/Technical/Vol1/secF#Special Conditions of Contract|SCC]]) and GCC 1.5 "Priority of Documents" (under [[OKF_bundle/Technical/Vol1/secE#Clause 1 — Definitions and Interpretation|GCC 1]]). Do not assume any ordering the documents do not state.

## 6. Status: draft vs reviewed

- `draft` is the default for every page, because all extracted data is still pending human review.
- `reviewed` is set by a human only, once every cited value on the page has been checked against the source PDF. The LLM never sets `reviewed`.
- **Every claim on a draft page is provisional.** In addition, list each claim that depends on a `pending_*` JSON record or an OCR-derived corrigendum value in `review_queue.md`, giving the page, the claim, the source record and what needs checking.
- **Unreviewed edits demote the page.** If a `reviewed` page gets new unreviewed content, set it back to `draft` and log the change.

## 7. Supersession (corrigenda and later amendments)

The three corrigenda form a chain:

- **Corrigendum 1** (01.10.2026) replaces the dates in NIT Key Details 5, 10, 11 and 12.
- **Corrigendum 2** (08.10.2026) replaces the minor-value-item bands in GCC 12.3.1, expands the clause list of Contract Data Item 14, and adds SCC Clauses 4–10, which delete specific GCC sub-clauses.
- **Corrigendum 3** (13.10.2026) amends serial 1 of Corrigendum 1, replacing the same four NIT dates again.

Rules:

1. **Keep every value.** Record the original value and each replacement in order, each with its own citation and notice date. Never delete or overwrite the original.
2. **Mark superseded values.** Show a superseded value as `~~old value~~ → new value` and name the amending notice and change. In tables, set the status column to, for example, `Superseded by Corrigendum 3 Change 2`.
3. **"Latest" means latest among supplied documents.** Write "latest value in the supplied documents", never "final value". Corrigendum 3 states that it does not by itself establish that no later amendment exists.
4. **Deletion is scoped.** A deletion removes only the named sub-clause. For example, SCC 4 deletes GCC 4.5, not GCC Clause 4. Keep the deleted provision visible with status `Deleted by Corrigendum 2 (SCC 4)`.
5. **"NOT APPLICABLE" can survive an amendment.** Corrigendum 2 Change 2 expands the clause list of Contract Data Item 14 but keeps NOT APPLICABLE. Pages must not suggest that price variation became applicable.
6. **Update everything affected.** When a corrigendum is ingested, update every page that cites the affected clause (`timeline.md`, `commercial_entity_index.md`, concept pages, `cross_reference_master.md`), add `supersedes` / `superseded_by` relations, and log which pages changed.
7. **Pre-bid replies.** Treat any future ingest of pre-bid replies the same way, recording each item as `clarifies` or `modifies`. Until then, record in `source_quirks.md` that they have not been ingested.

## 8. Operations

### Ingest

Handle one OKF file plus its matching JSON at a time, in this order:

1. Vol 1, Sections A to G
2. Vol 2, Parts 1, 2, 3, 4A and 4B
3. Vol 3, Parts I to V, then the appendices, general instructions and forms
4. Vol 4, Section J
5. Corrigenda 1, 2 and 3

For each source:

1. Read the OKF file and its JSON.
2. Create or update every affected hub and concept page.
3. Add cross-references.
4. Add new quirks to `source_quirks.md` and pending items to `review_queue.md`.
5. Update `index.md`.
6. Append a `log.md` entry with the date, source, pages created or updated, and open issues.

### Query

1. Answer from wiki pages first, then confirm each cited value against the OKF file or JSON before stating it.
2. If the answer has lasting value, file it under `qa/` and link it from `index.md`.
3. If the sources do not answer the question, say so and add the gap to `review_queue.md`.

### Lint

Report these checks, then fix or queue each finding:

- orphan pages
- links whose file or heading anchor does not resolve
- short-path links
- citations missing a page number
- deleted or superseded values cited without being marked
- values that disagree across pages
- repeated specifications across volumes that disagree
- precedence or override relations without a citation
- `reviewed` pages with unreviewed edits
- frontmatter missing `type`

Known items at the start:

- **Short-path links in `secA.md`:** `[[Vol1/secB|…]]` and `[[Vol1/secC|…]]`.
- **Candidate numbering anomalies for `source_quirks.md`:** ITT skips 18.3; GCC contents list 14.6 with no body text; GCC 3.6, 8.10 and 17.9–17.12 appear in the body but not the contents; Contract Data skips items 7 and 13; several Section D attachments and two EQC sub-clauses are marked DELETED. Confirm each one against the JSON before recording it.

### Log

`log.md` is append-only. Each entry looks like this:

```text
## 2026-10-30 — ingest — OKF_bundle/Technical/Vol1/secA.md
- Created: …
- Updated: …
- Queued for review: …
- Notes: …
```

## 9. The wiki never decides compliance

The wiki records what the documents say and how clauses relate to each other. It does **not** decide whether a bidder qualifies or is responsive, whether a clause applies to a given situation, or whether something complies. When a question asks for one of those judgements:

1. Set out the relevant provisions with citations.
2. Note any conflicts or open points.
3. State that the decision rests with BMRCL's evaluation under the tender documents.

Do not use words such as "eligible", "compliant", "qualifies" or "is responsive" as conclusions. They may appear only inside quotations of source text.

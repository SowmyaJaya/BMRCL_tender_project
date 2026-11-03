---
type: qa
title: Post-Rebase Provenance Migration
status: draft
question: Why did the audit report stale evidence after rebasing, and what was verified before migrating it?
asked: '2026-11-01T13:54:09+00:00'
sources:
- wiki/SCHEMA.md
last_ingested: '2026-11-01T13:54:09+00:00'
wiki_pages_used:
- wiki/SCHEMA.md
- wiki/index.md
- wiki/log.md
- wiki/review_queue.md
wiki_pages_used_basis: Relevant maintained pages checked during this schema-alignment pass.
last_schema_aligned: '2026-11-01T14:33:52+00:00'
---

# Post-Rebase Provenance Migration

## Question

Why did the audit report stale evidence after rebasing, and what was verified before migrating it?

## Answer

This records a source-identity migration, not a fresh ingest or human approval.

- Parsed JSON files were byte-for-byte unchanged between the reviewed snapshots.
- Section-file changes were repaired YAML delimiters, navigation metadata, line endings and removal of stray conflict-marker lines. Source indices were revised upstream and are retained.
- All 794 distinct saved citation records were matched uniquely by OKF path, exact heading, JSON path and JSON pointer. 791 differ only in ID/hash; three also remove a stray conflict-marker line. Tender quotes, page references and heading targets were checked before migration.
- All 822 claim texts are unchanged. Active claim/evidence IDs and dependent references were migrated; prior IDs are retained in claim history and the migration manifest.
- Governing SCHEMA.md from GitHub is preserved byte-for-byte. No source or parsed JSON file is rewritten.
- Original checkpoint markers and prior log bytes are unchanged. Old signatures do not match the new source/schema hashes; these remain historical evidence, not fabricated new batch completions.
- The auditor now excludes inline/fenced code examples from live-link checks. Actual source integrity and live-heading checks remain enabled.

#### Remaining review

Run the audit after migration. Historical batch signatures may remain flagged; do not rerun ingestion merely to clear them. The latest GitHub schema also introduces requirements not certified by the structural audit: page/QA type vocabulary, relation names, parameter tables, claim-level review queue coverage and un-ingested pre-bid replies. These require a separate alignment/review pass. No claim has been promoted to reviewed.

#### Migration evidence

`output/provenance_migration/rebase_v1/migration.json` contains the reviewed record mappings, payload hashes, original quote differences and claim-ID mappings. It preserves the reconstruction trail without changing historical logs.

## Citations

- [[wiki/SCHEMA|SCHEMA.md]]

## Wiki pages used

- [[wiki/SCHEMA|SCHEMA.md]]
- [[wiki/index|index.md]]
- [[wiki/log|log.md]]
- [[wiki/review_queue|review_queue.md]]

## Caveats

Draft only. Existing audit snapshots and historical counts in the answer retain their original context. PDF verification, source completeness, amendment interpretation and human approval are not established by formatting or a structural audit.

---
type: qa
title: Draft Wiki Handover and Remaining Review
status: draft
updated_at: '2026-11-01T12:14:18+00:00'
last_provenance_migrated: '2026-11-01T13:54:09+00:00'
question: What does Draft Wiki Handover and Remaining Review record about the draft wiki?
asked: '2026-11-01'
asked_basis: Recorded project workflow date; exact historical question timestamp was not recorded.
wiki_pages_used:
- wiki/SCHEMA.md
- wiki/index.md
- wiki/log.md
- wiki/review_queue.md
wiki_pages_used_basis: Relevant maintained pages checked during this schema-alignment pass.
sources:
- wiki/SCHEMA.md
- wiki/index.md
- wiki/log.md
- wiki/review_queue.md
last_schema_aligned: '2026-11-01T14:33:52+00:00'
---

# Draft Wiki Handover and Remaining Review

## Question

What does Draft Wiki Handover and Remaining Review record about the draft wiki?

## Answer

> Historical pre-rebase handover. Source identities have since been migrated; consult [[wiki/qa/provenance_migration|Provenance migration]] and the newest audit. Earlier counts and IDs below remain historical snapshots.

This is an editorial handover record. It does not approve exhaustive source coverage, semantic accuracy, legal applicability, bid responsiveness or PDF verification. All knowledge remains draft.

#### Latest structural alignment — audit pending

The structural alignment adds nine synthesis pages and one QA register: expected totals are 40 Markdown pages, 26 concept pages and 813 active draft claims/findings. Earlier counts below are historical snapshots. Run a fresh audit before reporting the new totals as audited. Full coverage/PDF review and strict v1.0 source-scope alignment remain pending.

#### Snapshot and technical checks

- Before consolidation: 29 Markdown pages, 782 claims/findings, zero structural/provenance errors and zero exact duplicate-text groups, according to the supplied audit.
- After this pass: 768 active draft claims/findings. Fourteen repeated claims were consolidated in eight reviewed groups. Original claims are retained in editorial history and the append-only log; all previously cited evidence IDs remain cited.
- This operation rebuilt all source citation records and found exact matches for saved citations. It made no API requests and changed no source, schema, ingestion script or original checkpoint marker.
- Previous audit before structural alignment: 30 Markdown pages, 768 active draft claims/findings, zero structural/provenance errors, zero exact duplicate groups, six similar-text pairs, 20 review flags and 17 amendment records. The following tables retain the pre-handover audit snapshot. Human review, PDF verification and exhaustive coverage review remain pending.

#### The 20 audit flags

There is one legacy Section A batch-status flag and 19 source-level citation-coverage flags. Twenty-one source sections have complete current-plan checkpoints. Section A has historical ingest activity without matching modern checkpoints; do not manufacture checkpoint markers or rerun solely to suppress this flag.

| Source | Batch status | Uncited units |
|---|---|---:|
| OKF_bundle/Technical/Vol1/secA.md | legacy_ingest_record_no_matching_checkpoints | 26 |
| OKF_bundle/Technical/Vol1/secB.md | checkpoints_complete | 22 |
| OKF_bundle/Technical/Vol1/secC.md | checkpoints_complete | 25 |
| OKF_bundle/Technical/Vol1/secD.md | checkpoints_complete | 61 |
| OKF_bundle/Technical/Vol1/secE.md | checkpoints_complete | 18 |
| OKF_bundle/Technical/Vol1/secF.md | checkpoints_complete | 0 |
| OKF_bundle/Technical/Vol1/secG.md | checkpoints_complete | 1 |
| OKF_bundle/Technical/Vol2/vol2_part1.md | checkpoints_complete | 0 |
| OKF_bundle/Technical/Vol2/vol2_part2.md | checkpoints_complete | 0 |
| OKF_bundle/Technical/Vol2/vol2_part3.md | checkpoints_complete | 22 |
| OKF_bundle/Technical/Vol2/vol2_part4A.md | checkpoints_complete | 24 |
| OKF_bundle/Technical/Vol2/vol2_part4B.md | checkpoints_complete | 32 |
| OKF_bundle/Technical/Vol3/vol3_part1.md | checkpoints_complete | 2 |
| OKF_bundle/Technical/Vol3/vol3_part2.md | checkpoints_complete | 1 |
| OKF_bundle/Technical/Vol3/vol3_part3.md | checkpoints_complete | 5 |
| OKF_bundle/Technical/Vol3/vol3_part4.md | checkpoints_complete | 3 |
| OKF_bundle/Technical/Vol3/vol3_part5.md | checkpoints_complete | 2 |
| OKF_bundle/Technical/Vol3/vol3_appendices_instructions_forms.md | checkpoints_complete | 83 |
| OKF_bundle/Financial/vol4_secJ.md | checkpoints_complete | 20 |
| OKF_bundle/addendum_and_corrigendum/A_and_C1.md | checkpoints_complete | 1 |
| OKF_bundle/addendum_and_corrigendum/A_and_C2.md | checkpoints_complete | 11 |
| OKF_bundle/addendum_and_corrigendum/A_and_C3.md | checkpoints_complete | 1 |

#### What remains uncited

The audit lists 360 uncited evidence units. This is not 360 missing requirements. Some are navigation, repeat extracts, blank bidder fields or workbook formulas; others need detailed comparison. Routing below is an editorial triage, not evidence that every condition in cited records has been summarized.

| Source record | Route |
|---|---|
| `J0468ddbd727814c1` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/10 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J0adf7b5fdc527b05` parsed_json/boq/boq_formulas.json#/formulas/5 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `J0cea698a7507793e` parsed_json/boq/boq_formulas.json#/formulas/0 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `J0d34d3e8a0aff1ca` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/66 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J0d9971d4ac090656` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/82 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J0d99a6551e4868d0` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/8 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J0da1279acc3c9611` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/5/cells/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J0ddf53bad6a43a7a` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/21 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J0e3617a036fddd21` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/18 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J0ee01172d6f6eb2e` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/0 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J0fadb1dd946817dc` parsed_json/vol3/part_4_environmental_management_corrected/environment_clauses.json#/preamble_retained_lines/1 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J117b3700b8b7a1c6` parsed_json/vol1/section_e_gcc/gcc_8_8_suspension_table.json#/introducing_paragraph | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J11a53a77573fcda3` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/6 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J11a95a7443cbb38c` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/4/supporting_document_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J12f1a1650e3a35f9` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/clauses/2/fragments/7 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J13be95b621cb6fbe` parsed_json/vol3/part_4_environmental_management_corrected/environment_clauses.json#/preamble/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J13d59d24375dc7ad` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/49 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J15cd011d4bd730bc` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/34 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J17245bb4e0f740d9` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/51 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J17ea874b658096ac` parsed_json/vol1/section_a_nit/nit_items.json#/key_details/14 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J1a2723c33e6bad51` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/13 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J1d2faeaae1749c38` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/39 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J2084b860aba98bc2` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/47 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J2098d50160d7f17b` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/69 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J21b3a0438fe37606` parsed_json/vol3/part_5_penalty_awards/penalty_awards_clauses.json#/preamble_retained_lines/1 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J21c6d5049d180006` parsed_json/vol1/section_b_itt/itt_clauses.json#/group_headings/1 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J221753f922f8f8c1` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/3/cells/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J23237bd377e80627` parsed_json/vol1/section_a_nit/nit_table.json#/rows/7 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J23da5d635347be2e` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/5 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J255b63a76071a0fe` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/31 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J271a99516e64a732` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/64 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J273150437131471e` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/2 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J2853bcc18fe2a265` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/6 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J2887f6b12d219167` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/0 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J28ab0c860ce419a9` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/9/cells/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J2ae7b1412b989474` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/44 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J2c2815392c3f89aa` parsed_json/vol1/section_a_nit/nit_items.json#/instructions/2 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J2d36e7fa7099afde` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/preamble_retained_lines/3 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J2e63653168a5a2bf` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/preamble_retained_lines/2 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J2fa91e0115807c00` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/4 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J303957536ed2bcc1` parsed_json/boq/boq_formulas.json#/formulas/8 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `J35f0a858ee9bcef8` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/32 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J371b751714457301` parsed_json/boq/boq_formulas.json#/formulas/9 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `J37f215f1ecb3627e` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/68 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J3a021e8a63cb7308` parsed_json/boq/boq_formulas.json#/formulas/10 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `J3af495b6fa5fe254` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/12 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J3b5098d2b23b545d` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/48 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J3c0c4026f85bc537` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/4 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J3c2c55c003cb03b6` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/clauses/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J3d439b6e96aef6b3` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/0/supporting_document_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J3dbec9f6592b9865` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/preamble_retained_lines/5 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J3df7310043165c02` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/2/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J3fb98e49853a595b` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/10 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J3fbc4f96b4d523bd` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/5 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J41aba86e1f33124d` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/45 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J41c60d14aaea0cd5` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/12 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J436c904b744cbdec` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/0 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J455d0ecb1ad7a038` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/20 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J460827a0820e6f3b` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/3 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J46d649f1deb14af1` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/6/supporting_document_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J472cc1b43d682382` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/2 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J4782af34c44663a6` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/19 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J47f69598d107365a` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/preamble_retained_lines/2 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J48375859802a2278` parsed_json/vol2/annexure_2_personnel/personnel_requirements.json#/personnel_requirements/1/cells/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J4843e402e9e014e4` parsed_json/boq/boq_formulas.json#/formulas/12 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `J48ced736f76e6966` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/18 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J48d8b0854eb5f88e` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/23 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J49542091d0c6ba0e` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/19 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J49afabc4c1f6ddce` parsed_json/boq/boq_formulas.json#/formulas/3 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `J4aea04fd3a033354` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/clauses/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J4bd612d754042577` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/10 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J4cd571067e4b108e` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/3 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J4e7455cb1704106b` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/7 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J510bb15cc6a11995` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/55 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J513c54651bca3526` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/6 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J51d1534d7fbcb7c8` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/13 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J520b2028c030965f` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/16 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J53446f2c3363bce8` parsed_json/vol3/part_3_health_welfare/health_welfare_clauses.json#/preamble_retained_lines/2 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J547523ea9cb22bf1` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/8 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J59237122eaa6e9a1` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/12 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J595fcef53aaaaf69` parsed_json/vol1/section_a_nit/nit_items.json#/instructions/6 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J59fb6204ebf5e34a` parsed_json/vol1/section_a_nit/nit_table.json#/rows/5 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J5c28ed2c1f25fe1f` parsed_json/vol1/section_b_itt/itt_clauses.json#/group_headings/2 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J5d0b4059c9d3fda7` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/17 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J5d29f693642204aa` parsed_json/vol1/section_b_itt/itt_clauses.json#/group_headings/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J5e800eb14b061407` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/71 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J5eef61d119f31a70` parsed_json/vol1/section_a_nit/nit_table.json#/rows/14 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J5f6badbf1413432c` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/3/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J5fef39b84656af25` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/42 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J5ff29dd6099d4818` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/8/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J605126706d8b9f2b` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/technical_specifications_heading/1 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J638b31d53a69f412` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/7 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J6444839890d0044f` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/2/requirement_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J64673eddac225d64` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/preamble_retained_lines/1 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J64f1c7f5e9000afa` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/20 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J667405bce57bb3f6` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/1 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J6688958f950c4bd3` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/35 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J6892beb009d4b05b` parsed_json/vol3/part_3_health_welfare/health_welfare_clauses.json#/preamble_retained_lines/1 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J68d0b53c92525cc0` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/note_groups/financial_standing/2 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J6af0edf984e84fd8` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/preamble_retained_lines/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J6b77a322f1ea86df` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/subclause_headings/3 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J6bf71626ca7ea49e` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/14 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J6d787af9b1fd5b24` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/7/cells/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J6ed2d0ef63c3c7df` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/10 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J6ffb02ac855d96e0` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/preamble_retained_lines/1 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J7005344f89413496` parsed_json/vol1/section_e_gcc/gcc_clauses.json#/preamble/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J710c8b748fb3476a` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/11 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J7239d1482d982de6` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/26 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J7403b67623f0beb9` parsed_json/vol1/section_d_technical_bid/attachment_8_tables.json#/signature_template | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J7433e7e135f98682` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/72 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J74554234fa3d3ce3` parsed_json/boq/boq_formulas.json#/formulas/6 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `J769ac8ad1a0e4c46` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/5 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J77231a4869e57e47` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/3/cells/2 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J78e18a1e9f8f794e` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/2 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J7a00703dd7f5655c` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/7/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J7af5dbf3aba43039` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/3/supporting_document_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J7ba7f547681ed813` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/5 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J7bcf6cf939e6916d` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/15 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J7bfe26aaccc9ed0f` parsed_json/vol1/section_d_technical_bid/attachment_7_tables.json#/full_form_context/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J7c536f7f8c361416` parsed_json/vol1/section_d_technical_bid/attachment_9_tables.json#/personnel_requirements/1/proposed_personnel_fields/0 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J7db3227ee1402bae` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/1/cells/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J7e00b941fa01209f` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/15 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J7f0e844fbbd24eb0` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/9 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J8111b0372c43e966` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/6/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J811ce485904f95d7` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/8 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J813ee4700ff59684` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/24 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J8158b69f3a970a56` parsed_json/vol3/appendix_1_mou/mou_clauses.json#/source_page_context/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J81dce0a5d47a4376` parsed_json/boq/boq_formulas.json#/formulas/11 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `J81e70795f6360838` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/65 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J822fec3367ebf4d8` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/18 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J827aa1668ca7aded` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/4 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J83133297a1322f92` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/7 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J841235964e6f0d02` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/4 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J843190e3e3f0329b` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/5/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J84aa0920dfdbdf6d` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/1/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J84aae70a0b2a56c7` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/46 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J856bcf4a5df1c5c5` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/15 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J8693e89fbf8eec5b` parsed_json/vol3/part_3_health_welfare/health_welfare_clauses.json#/preamble/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J86cd515c6519be7a` parsed_json/vol1/section_d_technical_bid/technical_bid_forms.json#/forms/12 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J87694b4c5576e402` parsed_json/vol1/section_c_eqc/eqc_tables.json#/context_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J88222ba5f1e37504` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/22 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J884fd567022b6dee` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/17 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J89e28d8651b09623` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/54 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J8a5ecc9b73a6dd71` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/4/cells/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J8d1c918ae5c4e660` parsed_json/vol3/part_4_environmental_management_corrected/environment_clauses.json#/preamble_retained_lines/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J8e09674e229c7923` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/79 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J8f0d707b66fe303d` parsed_json/vol1/section_a_nit/nit_items.json#/instructions/5 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J8f9c0c48cbc8da29` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/subclause_headings/24 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J8fe0bd1d12604021` parsed_json/vol1/section_d_technical_bid/attachment_7_tables.json#/main_table/entry_rows/1/fields/0 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J9089f1f7fd8af77c` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/0/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J913f1100ed5d7063` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/27 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J92431f370b1a5377` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/57 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J92927582cc70ea26` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/1/requirement_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J931f6cc21019bd75` parsed_json/vol3/part_3_health_welfare/health_welfare_clauses.json#/preamble_retained_lines/3 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J9377c9bcdc378775` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/source_page_context/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J93e9dc23656f6f34` parsed_json/vol1/section_c_eqc/eqc_tables.json#/context_fragments/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J941b308cc7e2c7bf` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/5 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J946771a3abc9d949` parsed_json/vol4/pricing_clauses.json#/context_records/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J959d05b1d7a77f45` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/preamble_retained_lines/4 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J959dadf2bcbbb133` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/56 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J9628737cbb626e51` parsed_json/vol1/section_a_nit/nit_table.json#/rows/8 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J9653a59e78d2f511` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/52 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `J972025ecd82a6497` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/4 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J979724c9736c4343` parsed_json/vol1/section_a_nit/nit_items.json#/instructions/7 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J97d4ffd76095bf1c` parsed_json/vol1/section_e_gcc/gcc_clauses.json#/contents_pages/2 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `J97dea94ba5f02331` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/0/requirement_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J9a02254d4357774e` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/3 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J9a92d1c6546c0716` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/1/supporting_document_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J9ca953a4443b448d` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/8 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `J9cd4eb0a104c23ae` parsed_json/vol1/section_d_technical_bid/attachment_9_tables.json#/personnel_requirements/1/proposed_personnel_fields/2 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J9daf9c587e3f3db5` parsed_json/vol1/section_d_technical_bid/attachment_9_tables.json#/personnel_requirements/0/proposed_personnel_fields/1 | Blank bidder-entry field: no supplied bidder value to ingest |
| `J9e8754c2b99b1235` parsed_json/vol1/section_d_technical_bid/attachment_9_tables.json#/signature_template | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `J9f646a709497754c` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/78 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Ja1fb5f53016aeeb6` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/8 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Ja539fc568447da87` parsed_json/boq/boq_formulas.json#/formulas/16 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `Ja5d9d4cfbaa8f859` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/21 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `Ja628d9ee542e3e97` parsed_json/vol1/section_d_technical_bid/attachment_9_tables.json#/personnel_requirements/0/proposed_personnel_fields/3 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Ja68748306e9fa9e4` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/11 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Ja6f942467e5f6e10` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/subclause_headings/4 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Ja822ac425387377b` parsed_json/boq/boq_formulas.json#/formulas/14 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `Ja8ee2930648f45f0` parsed_json/boq/boq_formulas.json#/formulas/4 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `Ja9f98b09bf42b427` parsed_json/boq/boq_formulas.json#/formulas/15 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `Jaba4d538e607cecd` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/other_numbered_lines/5 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jac3398a7b2baa7f0` parsed_json/vol3/part_1_she_management/she_management_clauses.json#/repeated_headings/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jac54624a6cfd2d25` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/1 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jac9ada794f78374f` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/other_numbered_lines/7 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jae65d33a8dff91e2` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/19 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jaece68616aa08e46` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/14 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jaf0a2eedef8fa37a` parsed_json/boq/boq_formulas.json#/formulas/1 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `Jaf0af5f043880beb` parsed_json/vol1/section_c_eqc/eqc_tables.json#/tables/4/recovered_text_blocks/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jaf462764ba80c8a1` parsed_json/vol1/section_e_gcc/gcc_clauses.json#/contents_pages/3 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jafe21291d739c6cd` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/preamble_retained_lines/3 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jb04ca277ac518f0f` parsed_json/vol1/section_c_eqc/eqc_tables.json#/context_fragments/4 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jb276628dd30c2782` parsed_json/vol1/section_b_itt/itt_clauses.json#/group_headings/3 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jb284a3fe78c7d94c` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/1 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jb4d85274c1c71f93` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/16 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jb76a173cbf27067e` parsed_json/vol1/section_g_forms/contract_form_2_bank_details.json#/details/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jb83137459e2e83aa` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/83 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jb953b2c54a339d6f` parsed_json/vol4/pricing_document.json#/pages/2 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jba34b64a073ff743` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/7 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `Jba640b9d378869c6` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/clauses/2/fragments/8 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jbaa84b556c78389e` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/43 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jbabe0e2f4fc1c277` parsed_json/vol1/section_a_nit/nit_table.json#/rows/6 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jbc2e8d9b6827da64` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/5/supporting_document_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jbe1f1d5a5db532f7` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/25 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jc021a3608442a758` parsed_json/vol1/section_d_technical_bid/attachment_10_tables.json#/introductory_context | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc0e09cfe6834b043` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/2 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jc184a4371bdb4252` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/37 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jc3b3d93c33ef32d3` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/24 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc3d5cb4e89882e8b` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/81 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jc4d02cd9dd13bfcd` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc56050bb60de48e0` parsed_json/vol4/pricing_clauses.json#/records/21 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc5d54fd8cf8ef063` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/16 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc72ecfe32db2a0a9` parsed_json/vol3/part_1_she_management/she_management_clauses.json#/source_page_context/4 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc81644f52bab1c26` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/80 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jc81a306a979e8b19` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/note_groups/bid_capacity/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc8538d8982c7fa7c` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc85b55390a4b380a` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/8 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jc8a0f447a027c3cc` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/10 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc931637aed74b0b4` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/preamble_retained_lines/4 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jc953ca668bcaa68a` parsed_json/vol1/section_a_nit/nit_table.json#/rows/13 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jc9798a640826ba43` parsed_json/vol3/part_5_penalty_awards/penalty_awards_clauses.json#/preamble_retained_lines/2 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jc9e19f43420725a3` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/41 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jca94b3699c4a86e2` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/61 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jcb367d326177e449` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/preamble_retained_lines/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jcc2240085ec1ef0c` parsed_json/vol1/section_c_eqc/eqc_tables.json#/tables/4/recovered_text_blocks/2 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jcc8c1825e69bafb2` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/59 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jcd2568aaed8cc0f6` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/4 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jcedab090d6bcc92a` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/other_numbered_lines/3 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jd0167f9e68854f9f` parsed_json/vol3/part_2_safety/safety_clauses.json#/preamble_retained_lines/1 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jd5036dcaffc4bc3e` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/3/requirement_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jd6fa1aef4d39cbd5` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/11 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jd8677505210e0f53` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/6/cells/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jd990de961acd2785` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/77 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jdb4d14cb6042c3b0` parsed_json/vol2/annexure_2_personnel/personnel_requirements.json#/personnel_requirements/0/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jdbdc22efa9b82a49` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/7 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jdbf2bd814c0945f8` parsed_json/vol1/section_d_technical_bid/attachment_7_tables.json#/notes/4 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jdc4e2120c9f468b6` parsed_json/vol1/section_d_technical_bid/attachment_10_tables.json#/signature_template | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jdcea2dbf79e4e3b4` parsed_json/vol2/annexure_2_personnel/personnel_requirements.json#/personnel_requirements/1/cells/8 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jdd1a3a01772fa082` parsed_json/boq/boq_formulas.json#/formulas/2 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `Jde1f164df333fc5e` parsed_json/vol1/section_a_nit/nit_items.json#/instructions/3 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jdee190d1fe6cbe48` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/3 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jdf63dd06a79f1990` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/6 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Je01ceb5ddaf2e36b` parsed_json/vol3/part_3_health_welfare/health_welfare_clauses.json#/preamble_retained_lines/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Je1c68d64a763739c` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/9 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `Je1e4b46a094ea01a` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/11 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Je1efb7873352e846` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/38 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Je27986558ae6dc74` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/11 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Je39abf6b05cdbb5c` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/other_numbered_lines/4 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Je3e243e8c0208f5b` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/2/supporting_document_fragments/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Je3e634e27b210668` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/60 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Je64dd6e131c9e5dc` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/subclause_headings/10 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Je7f1fa260207dd9d` parsed_json/boq/boq_formulas.json#/formulas/7 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `Je928f34c61ec5248` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/67 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jebdce75602024252` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/36 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jec3d9082f1a8a9e6` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/other_numbered_lines/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jef9f612df6f97d6e` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/11 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `Jf005d4628a8fa534` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/10 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jf0a8251c0f2de883` parsed_json/boq/boq_formulas.json#/formulas/13 | Workbook formula: retain as technical evidence, not an independent tender obligation |
| `Jf0e3cc0d25cbe5e8` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/9/cells/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jf0e907527f8d20b6` parsed_json/vol1/section_d_technical_bid/technical_bid_forms.json#/forms/24 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jf2518d4806d2d14c` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/14 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `Jf289ed9d95e5bbc6` parsed_json/vol3/appendix_3_site_she_plan/site_she_plan.json#/topics/1 | Site SHE Plan checklist detail: overview exists; detailed mapping remains pending |
| `Jf3207643b3027773` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/1/fields/9 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jf41d3caca979cff8` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/subclause_headings/12 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jf4cdd5adb3fa9550` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/other_numbered_lines/2 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jf5241d0f1d72a08c` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/5 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jf54a4073b3b2905a` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/subclause_headings/13 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jf77d65e45569f470` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/0/fields/0 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jf7aafb99bceac94f` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/9 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jf88df0beb02f1953` parsed_json/vol1/section_c_eqc/eqc_tables.json#/tables/1/recovered_text_blocks/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jf8d9472289dfeeb8` parsed_json/vol1/section_c_eqc/eqc_tables.json#/tables/4/recovered_text_blocks/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jf996b522b76d94f8` parsed_json/vol1/section_d_technical_bid/attachment_6_tables.json#/main_form_table/entry_rows/2/fields/6 | Blank bidder-entry field: no supplied bidder value to ingest |
| `Jfb8b7e5623554375` parsed_json/vol3/appendix_2_statutory_requirements/statutory_requirements.json#/items/50 | Statutory reference map: column/PDF review pending; no legal-applicability decision |
| `Jfba60b3443d03162` parsed_json/vol1/section_c_eqc/eqc_criteria.json#/criteria/3/requirement_fragments/1 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jfd0ca628a87a09a2` parsed_json/vol1/section_a_nit/nit_items.json#/instructions/0 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jfd26c6c78a0dab52` parsed_json/vol1/section_e_gcc/gcc_8_8_suspension_table.json#/gcc_context_reference | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jfd5938653511cf82` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/technical_specifications_heading/0 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jfdccace9d9f1486c` parsed_json/vol2/part_4b_restoration/restoration_clauses.json#/other_numbered_lines/17 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jfeb2de344217634c` parsed_json/vol1/section_b_itt/itt_clauses.json#/group_headings/4 | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jff0a9a831e0d2d9c` parsed_json/vol1/section_b_itt/itt_clauses.json#/contents_page | Heading/navigation: inspect parent text rather than generate a claim for each line |
| `Jff7eb842c50bd083` parsed_json/vol2/part_4a_demolition/demolition_clauses.json#/other_numbered_lines/6 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `Jffb5b0f588d043b1` parsed_json/vol2/annexure_3_equipment/equipment_requirements.json#/equipment_requirements/0/cells/2 | Compare against existing claims and full adjacent context; do not presume covered or missing from citation count |
| `S03af74f19086a6c2` OKF_bundle/Technical/Vol1/secE.md#Clause 14 — Risk and Responsibility | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S04983d595153565f` OKF_bundle/Technical/Vol1/secB.md#Clause 13.0 — Tender Security (EMD) | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S0fd63f857c8410bd` OKF_bundle/Technical/Vol1/secA.md#Instruction 1 — Downloading Tender Documents | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S10806e0a600ec851` OKF_bundle/Technical/Vol1/secB.md#Clause 15.0 — Submission of Tenders | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S1bbf0a629ac9ed66` OKF_bundle/Technical/Vol1/secD.md#Attachment-5 — Works of Similar Nature | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S1c8dd3aca8efc269` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Change 3 — Add SCC Clause 4: Sub-Contractor | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S237896007c736b1b` OKF_bundle/Technical/Vol1/secD.md#Attachment-12A — Surety Bond for Bid Security | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S237bf77f7ddc58f6` OKF_bundle/Technical/Vol1/secB.md#Clause 7.0 — Amendment to Tender Documents | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S2439d67f1c1cfcf2` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Change 6 — Add SCC Clause 7: Mobilization Advance | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S2494691bcbff5518` OKF_bundle/Technical/Vol1/secB.md#Clause 12.0 — Tender Validity | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S273df4086e11f166` OKF_bundle/Technical/Vol2/vol2_part4A.md#3.13 References | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S28592365bc753f54` OKF_bundle/Technical/Vol1/secD.md#Attachment-6 — Summary of Information Provided in Attachment-5 | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S2b1740f1fec15462` OKF_bundle/Technical/Vol1/secE.md#Clause 18 — Service of Notices | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S3012864a0d4b92bc` OKF_bundle/Technical/Vol1/secD.md#Attachment-12 — Form of Bank Guarantee for Tender Security / Earnest Money Deposit | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S301cec9a6a990c14` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Change 8 — Add SCC Clause 9: Special/Acceleration Advance | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S3070d7d18746d4d0` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Addendum and Corrigendum No. 2 | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S33963bbc6b791f9d` OKF_bundle/Technical/Vol1/secD.md#Letter of Technical Bid | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S357a9367f3e83733` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Change 9 — Add SCC Clause 10: Professional Indemnity Insurance | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S391d01694f8acee3` OKF_bundle/Technical/Vol1/secD.md#Attachment-15 — Format for Memorandum of Understanding (MoU) for Joint Venture Participation (Deleted) | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S3c92a51fa84ad2cc` OKF_bundle/Technical/Vol3/vol3_appendices_instructions_forms.md#Appendix No. 4 — WORKPLACE POLICY ON HIV/AIDS PREVENTION & CONTROL FOR WORKMEN ENGAGED BY CONTRACTORS | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S4064a41785c322f4` OKF_bundle/Technical/Vol1/secB.md#Clause 14.0 — Format and Signing of Tenders | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S408136d712a2b2f4` OKF_bundle/Technical/Vol1/secB.md#Clause 20.0 — Clarification of Tenders | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S41f117edab663915` OKF_bundle/Technical/Vol1/secA.md#Notice Inviting Tender | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S43bb31ad247c0ae2` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Change 1 — Variation to Quantities of Minor Value Items | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S45c2f4623b351114` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Reading Note | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S47ff92cc86699d12` OKF_bundle/Technical/Vol2/vol2_part3.md#Clause 21 — Demolition of Buildings/Structures | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S4962f1dd8a48d375` OKF_bundle/Technical/Vol1/secB.md#Clause 5.0 — Contents of Tender Documents | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S4e8c42672c309327` OKF_bundle/Technical/Vol1/secB.md#Clause 18.0 — Tender Opening | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S503fafa60c52bd1a` OKF_bundle/Technical/Vol1/secC.md#Clause 1.0 — General Information and Qualification Requirement | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S5068646deee9051c` OKF_bundle/Technical/Vol1/secA.md#Instruction 3 — Digital Signature Requirement | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S5142b8d776d57bbd` OKF_bundle/Technical/Vol1/secE.md#Clause 8 — Commencement, Completion and Delay | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S51435fae16856e2e` OKF_bundle/addendum_and_corrigendum/A_and_C3.md#Addendum and Corrigendum No. 3 | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S5577508a9a6cb5e4` OKF_bundle/Technical/Vol1/secA.md#Key Detail 6 — Site Visit | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S5853e6b6f333abd4` OKF_bundle/Technical/Vol1/secE.md#Clause 1 — Definitions and Interpretation | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S5857f4e8ffbd3a0c` OKF_bundle/Technical/Vol1/secB.md#Clause 23.0 — Award Criteria | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S5b1e8e270749935e` OKF_bundle/Technical/Vol1/secC.md#Eligibility cum Qualification Criteria | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S64b8a64fc9fec37f` OKF_bundle/Technical/Vol1/secD.md#Attachment-13A — Liquidity Calculation (Deleted) | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S664da7955d45f3de` OKF_bundle/Technical/Vol1/secE.md#Clause 2 — The Employer | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S744bcd6533c4b541` OKF_bundle/Technical/Vol1/secD.md#Attachment-9A — Format of Curriculum Vitae (CV) for Proposed Key Personnel | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S8717125e4175178d` OKF_bundle/Technical/Vol1/secB.md#Clause 16.0 — Failure to Submit Tenders in Time | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S8b81a5dd2d5435c0` OKF_bundle/Technical/Vol1/secE.md#Clause 15 — Insurance | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S9037fd2d2cca6b3a` OKF_bundle/Technical/Vol1/secE.md#Clause 12 — Variations | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S951ed3a6ad382092` OKF_bundle/Technical/Vol1/secA.md#Key Detail 15 — eProcurement Portal | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S9e71c7ee47e1dbdc` OKF_bundle/Technical/Vol1/secD.md#Attachment-8 — Financial Information: Updated Annual Turnover | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `S9f20fb4ea1f27c01` OKF_bundle/Technical/Vol1/secA.md#Instruction 7 — Eligibility and Qualification | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sa082179f289f55d7` OKF_bundle/Technical/Vol1/secD.md#Attachment-7 — Works in Hand | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sa2acac94dfb2a159` OKF_bundle/Technical/Vol1/secA.md#Instruction 8 — Portal Updates | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sa35e17eac49a12a7` OKF_bundle/Technical/Vol1/secA.md#Key Detail 8 — Last Date and Time for Seeking Clarification | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sa3a3f569b8e2c24d` OKF_bundle/Technical/Vol1/secB.md#Clause 17.0 — Modification and Withdrawal of Tenders | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sa406117b710ac2e3` OKF_bundle/Technical/Vol1/secB.md#Clause 19.0 — Process to Be Confidential | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sa5d25160c134a181` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Existing Wording | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sa8cea48a82122bdd` OKF_bundle/Technical/Vol1/secA.md#Instruction 4 — Submission Deadline and Responsibility | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sb6a401e8e6e3fde0` OKF_bundle/Technical/Vol2/vol2_part4B.md#Clause 17 — Earthwork Including General Filling, Dewatering and Backfilling | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sb9089cae55f6d535` OKF_bundle/Technical/Vol1/secE.md#Contract Data | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sc3ab96ba7407fa96` OKF_bundle/addendum_and_corrigendum/A_and_C1.md#Addendum and Corrigendum No. 1 | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sc500727ae7139050` OKF_bundle/Technical/Vol1/secD.md#Attachment-13 — Form of Banker's Certificate for Liquidity | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sc554ede249a9cbb6` OKF_bundle/Technical/Vol1/secA.md#Key Detail 7 — Pre-Bid Meeting | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sce6c7e00baf1565e` OKF_bundle/Technical/Vol1/secD.md#Attachment-4 — Tenderer's Information | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Scf171b2ab42331f5` OKF_bundle/Technical/Vol1/secA.md#Instruction 6 — Tender Security | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sd2b1c2d6e70571a6` OKF_bundle/Technical/Vol1/secE.md#Clause 13 — Determination/Termination of the Contract | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sd7d43189aba79e0d` OKF_bundle/Technical/Vol1/secA.md#Key Detail 9 — Venue for Pre-Bid Meeting | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sdb9cd12dba341afa` OKF_bundle/Technical/Vol1/secC.md#Clause 2.0 — Eligible Tenderers | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sdef58c5acc5d5f20` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Replacement Wording | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sdfdce1bb71a0cbae` OKF_bundle/Technical/Vol1/secE.md#Clause 3 — The Engineer | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Se25430b88069b052` OKF_bundle/Technical/Vol1/secE.md#Clause 16 — Force Majeure | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Se32f2c70eeda152a` OKF_bundle/Technical/Vol1/secE.md#Clause 4 — The Contractor | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Seb8c567ae8147316` OKF_bundle/Technical/Vol1/secD.md#Attachment-4A — Tender Fee Payment Details and Tender Security Details | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sef72307faddda982` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Change 4 — Add SCC Clause 5: Incentives for Early Completion | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sf0036c7a759f2645` OKF_bundle/Technical/Vol1/secE.md#Clause 17 — Claims, Disputes and Conciliation | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sf325d2c73e9570c4` OKF_bundle/Technical/Vol1/secB.md#Clause 21.0 — Determination of Responsiveness | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sf33954fce365298c` OKF_bundle/Technical/Vol1/secC.md#Clause 3.0 — Qualification Criteria | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sf3fe23e992b05de2` OKF_bundle/Technical/Vol1/secA.md#Key Detail 14 — Opening of Financial Bid | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sf5d69d0bbf816e63` OKF_bundle/Technical/Vol1/secB.md#Clause 22.0 — Evaluation of Tender | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sf765c38b65ea8d20` OKF_bundle/Technical/Vol1/secD.md#Attachment-11 — Format for Power of Attorney for Bidding | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sf7669d19716ac809` OKF_bundle/addendum_and_corrigendum/A_and_C2.md#Change 7 — Add SCC Clause 8: Advance Against Plant & Machinery | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sfd22b8d3c8334a5b` OKF_bundle/Technical/Vol1/secB.md#Clause 25.0 — Notification of Award | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |
| `Sfd86bbc45b71c86f` OKF_bundle/Technical/Vol1/secB.md#Clause 24.0 — Employer's Right to Accept Any Tender and to Reject Any or All Tenders | OKF outline/section extract: compare substantive JSON; no new claim solely for this ID |

#### Similar-text decisions

The audit reported 21 pairs, forming nine groups. Eight groups were consolidated after comparing meaning and combining citations. The four Section D empty-template summaries remain separate because their combined 21 evidence IDs exceed the renderer contract limit of 20; no citation was dropped to force a merge. Similarity alone does not justify deletion.

| Previous first claim | Previous second claim | Decision |
|---|---|---|
| wiki/commercial_entity_index.md#C00cf5172d9e0ef71 | wiki/commercial_entity_index.md#C4148ecd0407d6f2d | Consolidated as C542b46bd5d3babb5 |
| wiki/concepts/financial_document_and_boq_overview.md#Ca3df89a6aadc3ebc | wiki/concepts/financial_document_and_boq_overview.md#C14767ebf3bdcffdc | Consolidated as C8e532db78cc0f946 |
| wiki/concepts/financial_document_and_boq_overview.md#Ca3df89a6aadc3ebc | wiki/concepts/financial_document_and_boq_overview.md#C3c029413f855f5e6 | Consolidated as C8e532db78cc0f946 |
| wiki/concepts/financial_document_and_boq_overview.md#Ca3df89a6aadc3ebc | wiki/concepts/financial_document_and_boq_overview.md#Cc7dfebb58b982cbe | Consolidated as C8e532db78cc0f946 |
| wiki/concepts/financial_document_and_boq_overview.md#Ca854d21449e5bb09 | wiki/concepts/financial_document_and_boq_overview.md#C71803482202cf6b6 | Consolidated as Cb73b503cb47bc02c |
| wiki/concepts/financial_document_and_boq_overview.md#Ce169bc47f7309c0d | wiki/concepts/financial_document_and_boq_overview.md#C9b3f4ce9e49c0e11 | Consolidated as C34b0e9c0b2651965 |
| wiki/concepts/financial_document_and_boq_overview.md#Ce169bc47f7309c0d | wiki/concepts/financial_document_and_boq_overview.md#C2d15946aaa4d0b64 | Consolidated as C34b0e9c0b2651965 |
| wiki/concepts/financial_document_and_boq_overview.md#Ce169bc47f7309c0d | wiki/concepts/financial_document_and_boq_overview.md#C6682ee2f65312098 | Consolidated as C34b0e9c0b2651965 |
| wiki/concepts/financial_document_and_boq_overview.md#C14767ebf3bdcffdc | wiki/concepts/financial_document_and_boq_overview.md#Cc7dfebb58b982cbe | Consolidated as C8e532db78cc0f946 |
| wiki/concepts/general_conditions_of_contract_overview.md#Cb58a7c3188a6c13e | wiki/concepts/general_conditions_of_contract_overview.md#C55dd80104db34e20 | Consolidated as Cb6628ca1c28ec235 |
| wiki/concepts/general_conditions_of_contract_overview.md#C4e3296251ffaf00e | wiki/concepts/general_conditions_of_contract_overview.md#Cf2f5088c32aa59fb | Consolidated as C4e3296251ffaf00e |
| wiki/concepts/she_manual_part1_overview.md#C2f02f1e45c26017e | wiki/concepts/she_manual_part1_overview.md#C9cba85544b388fa7 | Consolidated as C2f02f1e45c26017e |
| wiki/concepts/she_manual_part1_overview.md#C9cba85544b388fa7 | wiki/concepts/she_manual_part1_overview.md#C08cd6a8105cbd87e | Consolidated as C2f02f1e45c26017e |
| wiki/concepts/she_manual_part1_overview.md#C02b6c08ab29f46e3 | wiki/concepts/she_manual_part1_overview.md#C08cd6a8105cbd87e | Consolidated as C2f02f1e45c26017e |
| wiki/source_quirks.md#C0237a5e2bbe86d28 | wiki/source_quirks.md#C07b20d28bdfdad3a | Retained: citation-bound template-summary group; not a contradiction finding |
| wiki/source_quirks.md#C0237a5e2bbe86d28 | wiki/source_quirks.md#C407af648aa3407ea | Retained: citation-bound template-summary group; not a contradiction finding |
| wiki/source_quirks.md#C0237a5e2bbe86d28 | wiki/source_quirks.md#C62c86bd2b7d399b1 | Retained: citation-bound template-summary group; not a contradiction finding |
| wiki/source_quirks.md#C07b20d28bdfdad3a | wiki/source_quirks.md#C407af648aa3407ea | Retained: citation-bound template-summary group; not a contradiction finding |
| wiki/source_quirks.md#C07b20d28bdfdad3a | wiki/source_quirks.md#C62c86bd2b7d399b1 | Retained: citation-bound template-summary group; not a contradiction finding |
| wiki/source_quirks.md#C407af648aa3407ea | wiki/source_quirks.md#C62c86bd2b7d399b1 | Retained: citation-bound template-summary group; not a contradiction finding |
| wiki/source_quirks.md#C50fba38cd9368a50 | wiki/source_quirks.md#Cc3dfe7ca7235c338 | Consolidated as C50fba38cd9368a50 |

#### Amendment review

All 17 parsed amendment records are cited. This does not approve their transcription, meaning, supersession or legal effect. C1/C3 schedule histories and C2 deletion/Contract Data changes are preserved. The source-specific GCC notes distinguish historical text from amendment context; no general hierarchy or blanket deletion has been inferred.

#### Human-review queue

The following questions remain recorded. Some may be answered by source comparison; others require PDF inspection or official clarification. They are not cleared by this handover.

- wiki/concepts/contract_forms_overview.md#Cbc799ff5087bea31: Whether contract forms may be modified at the time of finalization of the contract as noted in the index page of Section G.
- wiki/concepts/general_conditions_of_contract_overview.md#C83e868feeefc8e7a: Reconcile the historical GCC 4.5 subcontracting statement with Corrigendum 2 new SCC 4, which instructs that the entire listed subclause stands deleted. Preserve both source versions; this finding does not decide remaining subcontracting rights or obligations.
- wiki/concepts/general_conditions_of_contract_overview.md#C91113f62b7e67b8e: Reconcile the historical GCC price-variation discussion with Corrigendum 2 new SCC 6 and amended Contract Data Item 14. The deletion instruction lists GCC 11.1.2 and 11.1.2.1 through 11.1.2.4, while Item 14 retains NOT APPLICABLE. This does not delete all of GCC Clause 11 or decide unrelated GST/change-in-law provisions.
- wiki/concepts/general_conditions_of_contract_overview.md#Ccbee310449417dd2: Source discrepancy: Contract Data specifies a six-month Defects Liability Period, whereas Clause 6 in the unexecuted Contract Agreement template specifies twelve months. The source wording uses Taking Over Certificates and Final Taking Over Certificate respectively. Record both durations and seek clarification; this wiki does not establish which provision controls.
- wiki/concepts/general_conditions_of_contract_overview.md#Cdeaf08aff3d6d3f7: GCC 4.32 contains generic conditional wording on Engineer-approved explosives, while Volume 2 Scope Clause 11 expressly states that use of explosives will not be permitted. Preserve both source statements and cross-reference the scope prohibition beside the GCC summary; the generic text must not be presented alone as permission for this demolition package. This draft finding does not decide document precedence or legal applicability.
- wiki/concepts/she_manual_part1_overview.md#C3e933afd1cc15fb5: Source discrepancy: SHE 7.8.1 requires agenda circulation at least seven working days before the scheduled meeting, while Form SF/001 states at least two days. Preserve the different wording without selecting precedence. Monthly Site SHE Committee meetings under 7.4 and weekly Construction SHE Committee meetings under 7.5 are distinct source provisions.
- wiki/review_queue.md#Cba64500725e367d6: Final transcription and applicability review remains pending for Addendum and Corrigendum No. 1 and No. 3.
- wiki/review_queue.md#C9670a32e8b57a07f: Verify whether any subsequent corrigenda modify the financial thresholds or work experience values specified in Section C EQC Clause 3.1.
- wiki/review_queue.md#C31bec186848cbb97: Verify whether foreign currency conversion procedures under EQC clause notes apply uniformly to all past financial turnover and work experience calculations without exception.
- wiki/review_queue.md#C3e826561f973ef99: Verify whether all blank template fields across Section D attachments are correctly mapped to expected bidder data inputs without missing formatting instructions or notes.
- wiki/review_queue.md#C4781cf53d06982f7: Verify whether Corrigendum No. 2 deletion instructions targeting specific GCC subclauses supersede the Contract Data table entries or if the Contract Data designations remain the controlling operative rules.
- wiki/review_queue.md#Cc74a321ba11317e3: Verify whether Corrigendum No. 2 deletion instructions targeting specific GCC subclauses (such as Sub-Clauses 4.5, 8.10, 11.2.1 through 11.2.3, and 15.1) supersede the Contract Data table entries or if the Contract Data designations remain the controlling operative rules.
- wiki/review_queue.md#C2ac4fe98c0a9bd6b: Verify the operational impact of Corrigendum No. 2 deleting multiple major GCC sub-clauses (including sub-contracting restrictions, early completion incentives, price variation bands, and various advances) while keeping the Contract Data label for Price Variation as NOT APPLICABLE with an expanded clause-reference list.
- wiki/review_queue.md#C1efba09fa7ef6721: Verify the operational and legal impact of Corrigendum No. 2 deleting multiple major GCC sub-clauses (sub-contracting under 4.5, early completion incentives under 8.10, price variation under 11.1.2 series, mobilization and equipment advances under 11.2 series, special/acceleration advance under 11.2.3, and professional indemnity insurance under 15.1) while keeping the Contract Data label for Price Variation as NOT APPLICABLE with an expanded clause-reference list.
- wiki/review_queue.md#C6ac52843624e08d3: Verify the operational and legal impact of Corrigendum No. 2 deleting multiple major GCC sub-clauses while keeping the Contract Data label for Price Variation as NOT APPLICABLE with an expanded clause-reference list.
- wiki/review_queue.md#C51e62850ea361994: Verify whether additional operational personnel tables or specialist safety officer requirements exist in un-ingested parts of Volume 2 or Volume 3 beyond the Project Manager specification in Annexure 2.
- wiki/review_queue.md#C2eaa33ff43a8a95b: Verify whether the proposed deployment quantities for plant and equipment in Annexure 3 of Volume 2 Part 3 are subject to adjustment based on specific site fronts handed over by BMRCL.
- wiki/review_queue.md#Cfa4fa31d74efccb7: Verify whether monetary penalties associated with repeated non-compliance under SHE audit findings cross-reference specific General Conditions of Contract clauses or if they are solely governed by administrative notices.
- wiki/review_queue.md#C6c51234c4fa19751: Verify whether general instructions such as BMRC/SHE/CEO/001 and BMRC/SHE/CEO/0011 referenced in Vol 3 Part II safety clauses are fully appended or available in separate unpublished administrative annexes.
- wiki/review_queue.md#Cda6fc585e455a9ec: Verify the exact angle specification in Clause 19.0(ii) for overhead protection, where the source text states an angle 'not more than 200' which appears to represent a typographical error for 20 degrees.
- wiki/review_queue.md#Cb405571e8c4ab6a4: Verify whether specific monetary penalty amounts or tariff schedules for safety non-compliance are detailed elsewhere in the tender or if they are entirely deferred to the General Conditions of Contract / Special Conditions of Contract penalty provisions.
- wiki/review_queue.md#C5ce32079bd8a103e: Verify whether the schedules referenced in BOCWR (Schedules III, IV, V, X, XI) are fully appended or incorporated by reference in other volumes of the tender package.
- wiki/review_queue.md#C03b81b1818d05482: Verify whether general instruction BMRC/SHE/CEO/011 referenced in illumination clause 44.2.1 contains additional quantitative lighting thresholds not explicitly listed in Part III text.
- wiki/review_queue.md#Ca247666b0b1d561c: Verify if subsequent amendments alter any of the penalty amounts specified in Volume 3 Part V across all categories.
- wiki/review_queue.md#C4e17ee15caf5c2f7: Verify whether compound penalty ceilings are consistently applied across all sub-contractor tiers under Tender Package P1.
- wiki/review_queue.md#Cea6075db08417b5f: Verify column reconstruction for Appendix 2 statutory requirements items to ensure all manual references (S-xx) and statutory rules (R-xx) map correctly to their intended obligations.
- wiki/review_queue.md#C844f7607f92ba80d: Verify column boundaries and cross-references for Appendix 2 statutory requirement items (e.g., items 41 through 77) due to unseparated text fragments in parsed records.
- wiki/review_queue.md#C9f4cecf8ab82b106: Verify whether the duplicate entries for medical examination for occupational health hazards in Appendix 2 (item numbers 76 and 82) represent distinct statutory sub-provisions or an editorial duplication in the source document.
- wiki/review_queue.md#C72864da8f99e695d: Verify whether the reference to DMRC in Appendix 4 represents a typographical error for BMRC in the tender documentation and confirm the intended governing entity.
- wiki/review_queue.md#C9861497e248cc2a0: Verify whether contract value tiers in General Instruction BMRC/SHE/CEO/001 (which lists 'More than 25' Cr in row headers) contain a typographical omission in the source text regarding crore thresholds compared to BMRC/SHE/CEO/003 ('More than 250 Cr').
- wiki/review_queue.md#C1556ff94660e2c27: Verify whether additional operational roles or specialized subcontractor staff missing from the visible fragment of BMRC/SHE/CEO/007's training matrix are captured in subsequent pages of the SHE Manual appendices.
- wiki/review_queue.md#Cc372e5ccecdeaeb6: Verify whether layout review status for general instructions BMRC/SHE/CEO/008, 009, and 010 remains pending across all downstream sections.
- wiki/review_queue.md#C103c6df5b8a15007: Verify whether the detailed graphical or tabular content for Warning Traffic Signs under General Instruction BMRC/SHE/CEO/012 is presented in subsequent unparsed sections or attachments.
- wiki/review_queue.md#C01985474b5623760: Verify how the lump-sum salvage credit offered under Schedule-C is incorporated into final contract evaluation given its placeholder status in the published tender document.
- wiki/review_queue.md#C54e78c77828cf29b: Verify whether any subsequent corrigenda modify the Schedule A estimated cost of ₹ 4,69,41,306.00 or introduce changes to Schedule B and Schedule C pricing instructions in Volume 4 Section J.
- wiki/review_queue.md#Cc263bab219b8a11a: Verify whether the addition of SCC clauses deleting specific GCC subclauses (such as subclauses 4.5, 8.10, 11.1.2 through 11.1.2.4, 11.2.1, 11.2.2, 11.2.3, and 15.1) requires corresponding textual removal from GCC source files or is fully managed by SCC precedence instructions.
- wiki/review_queue.md#C2fa485c62ca4ea5a: All parsed amendment records for Corrigendum No. 3 remain in pending_manual_review status and require final verification against the original PDF source document.
- wiki/review_queue.md#C6737cf2615f314f1: Verify whether Corrigendum No. 2 additions of SCC clauses deleting GCC Sub-Clauses 4.5, 8.10, 11.1.2 series, 11.2.1, 11.2.2, 11.2.3, and 15.1 supersede the original GCC baseline provisions without altering Contract Data labels.

#### Acceptance boundary

Draft ingestion and the scoped correction passes are recorded. Structural checks passed in the supplied audit. Exhaustive requirement coverage, full cross-clause reconciliation, source PDF verification and promotion to reviewed remain pending. A deadline does not change these review boundaries.

## Citations

- [[wiki/SCHEMA|SCHEMA.md]]
- [[wiki/index|index.md]]
- [[wiki/log|log.md]]
- [[wiki/review_queue|review_queue.md]]

## Wiki pages used

- [[wiki/SCHEMA|SCHEMA.md]]
- [[wiki/index|index.md]]
- [[wiki/log|log.md]]
- [[wiki/review_queue|review_queue.md]]

## Caveats

Draft only. Existing audit snapshots and historical counts in the answer retain their original context. PDF verification, source completeness, amendment interpretation and human approval are not established by formatting or a structural audit.

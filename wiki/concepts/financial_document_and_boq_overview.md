---
type: concept
title: Financial Document and Bill of Quantities Overview (Section J)
tender_no: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157
status: draft
review_status: pending_manual_review
generator: bmrcl-dynamic-wiki-v2
created_at: '2026-10-31T15:57:39+00:00'
updated_at: '2026-11-01T13:54:09+00:00'
last_ingested: '2026-11-01T11:17:08+00:00'
model: gemini-3.5-flash-lite
sources:
- OKF_bundle/Financial/vol4_secJ.md
- parsed_json/boq/boq_formulas.json
- parsed_json/boq/boq_workbook.json
- parsed_json/vol4/boq_abstract.json
- parsed_json/vol4/pricing_clauses.json
- parsed_json/vol4/pricing_document.json
claims:
- kind: parameter
  text: The estimated cost put to tender for Schedule-B (Items under Schedule of Rate published by KPWD) is INR 5,00,000.00, bringing the total estimated cost for Schedules A and B to INR 4,74,41,306.00.
  evidence_ids:
  - J76eb6bf2592fa9ee
  - Jaf44a3c272fd15bf
  - S212cc0e74fc3292f
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C6acf07c2994f34b5
  citations:
  - id: J76eb6bf2592fa9ee
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/boq_abstract.json
    json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
    json_pointer: /records/2
    json_record_id: vol4/boq_abstract/A+B
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"47441306.00\",\n  \"amount_raw\": \"4,74,41,306.00\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      368.74,\n      100.77,\n      401.54\n    ],\n    [\n      102.17,\n      368.74,\n      194.06,\n      401.54\n    ],\n    [\n      195.45999999999998,\n      368.74,\n      406.82,\n      401.54\n    ],\n    [\n      408.21999999999997,\n      368.74,\n      534.17,\n      401.54\n    ]\n  ],\n  \"cells\": [\n    \"\",\n    \"\",\n    \"Total of Schedules (A+B)\",\n    \"4,74,41,306.00\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/A+B\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A+B\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jaf44a3c272fd15bf
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/boq_abstract.json
    json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
    json_pointer: /records/1
    json_record_id: vol4/boq_abstract/B
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"500000.00\",\n  \"amount_raw\": \"5,00,000.00\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      330.94,\n      100.77,\n      367.34000000000003\n    ],\n    [\n      102.17,\n      330.94,\n      194.06,\n      367.34000000000003\n    ],\n    [\n      195.45999999999998,\n      330.94,\n      406.82,\n      367.34000000000003\n    ],\n    [\n      408.21999999999997,\n      330.94,\n      534.17,\n      367.34000000000003\n    ]\n  ],\n  \"cells\": [\n    \"2\",\n    \"SCHEDULE-B\",\n    \"Items under Schedule of Rate published \\nby KPWD\",\n    \"5,00,000.00\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/B\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"B\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: S212cc0e74fc3292f
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: 2.0 — Abstract of Bill of Quantities (BOQ)
    source_document: Vol4DLNP1.pdf
    pdf_pages:
    - 8
    quote: "- **Schedule-A — Demolition and Dismantling**\n  - Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ\n  - **Estimated Cost:** INR 4,69,41,306.00\n\n- **Schedule-B — KPWD Schedule-of-Rate Items**\n  - Items under Schedule of Rate published by KPWD\n  - **Estimated Cost:** INR 5,00,000.00\n\n- **Total of Schedules A+B:** INR 4,74,41,306.00\n\n- **Schedule-C — Salvage Credit to BMRCL**\n  - Credit for salvageable items from dismantled/demolished private properties in which the owner has no interest\n  - **Source Reference:** Para 15 of Part-3 of Employer’s Requirement\n  - **Estimated Cost Field:** `----`\n  - **Pricing Basis:** Lump-sum credit under Preamble Instruction 3"
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  created_at: '2026-10-31T15:57:39+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C7334dfceeb4cdec6
    previous_evidence_ids:
    - J40111fda7648d44d
    - Jbd5c1b7c43155768
    - S469ca02217533c37
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Schedule-C represents a lump-sum credit to BMRCL for salvageable items out of dismantled or demolished private properties with no owner interest, shown with a placeholder ('----') in the BOQ abstract.
  evidence_ids:
  - J3b6ef5b6db6162f6
  - S212cc0e74fc3292f
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C91deff25ac841e85
  citations:
  - id: J3b6ef5b6db6162f6
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/boq_abstract.json
    json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
    json_pointer: /records/3
    json_record_id: vol4/boq_abstract/C
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": null,\n  \"amount_raw\": \"----\",\n  \"amount_status\": \"Source placeholder; not a zero or submitted quote\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      402.94,\n      100.77,\n      477.26\n    ],\n    [\n      102.17,\n      402.94,\n      194.06,\n      477.26\n    ],\n    [\n      195.45999999999998,\n      402.94,\n      406.82,\n      477.26\n    ],\n    [\n      408.21999999999997,\n      402.94,\n      534.17,\n      477.26\n    ]\n  ],\n  \"cells\": [\n    \"3\",\n    \"SCHEDULE-C\",\n    \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’).\",\n    \"----\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/C\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"C\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: S212cc0e74fc3292f
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: 2.0 — Abstract of Bill of Quantities (BOQ)
    source_document: Vol4DLNP1.pdf
    pdf_pages:
    - 8
    quote: "- **Schedule-A — Demolition and Dismantling**\n  - Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ\n  - **Estimated Cost:** INR 4,69,41,306.00\n\n- **Schedule-B — KPWD Schedule-of-Rate Items**\n  - Items under Schedule of Rate published by KPWD\n  - **Estimated Cost:** INR 5,00,000.00\n\n- **Total of Schedules A+B:** INR 4,74,41,306.00\n\n- **Schedule-C — Salvage Credit to BMRCL**\n  - Credit for salvageable items from dismantled/demolished private properties in which the owner has no interest\n  - **Source Reference:** Para 15 of Part-3 of Employer’s Requirement\n  - **Estimated Cost Field:** `----`\n  - **Pricing Basis:** Lump-sum credit under Preamble Instruction 3"
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  created_at: '2026-10-31T15:57:39+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Caef6fe0d113e35a9
    previous_evidence_ids:
    - J2ce3b55e064d0935
    - S469ca02217533c37
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Schedule A of the BOQ abstract specifies partial and full demolition and dismantling works amounting to ₹ 4,69,41,306.00.
  evidence_ids:
  - J241ce183fcecf015
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C95906234658b2af8
  citations:
  - id: J241ce183fcecf015
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/boq_abstract.json
    json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
    json_pointer: /records/0
    json_record_id: vol4/boq_abstract/A
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"46941306.00\",\n  \"amount_raw\": \"4,69,41,306.00\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      280.39,\n      100.77,\n      329.54\n    ],\n    [\n      102.17,\n      280.39,\n      194.06,\n      329.54\n    ],\n    [\n      195.45999999999998,\n      280.39,\n      406.82,\n      329.54\n    ],\n    [\n      408.21999999999997,\n      280.39,\n      534.17,\n      329.54\n    ]\n  ],\n  \"cells\": [\n    \"1\",\n    \"SCHEDULE-A\",\n    \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ\",\n    \"4,69,41,306.00\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/A\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:00:35+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C5200ca9d5085e2b7
    previous_evidence_ids:
    - J23599c81d83cf26f
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Tenderers must quote percentage rates in two decimals for Schedule A (At Par / Excess / Less), 'At Par' only for Schedule B, and a lump sum credit amount to BMRCL on salvage of materials for Schedule C.
  evidence_ids:
  - Jf17d55c6acfde864
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: Ccff130cee7928894
  citations:
  - id: Jf17d55c6acfde864
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 6
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/5
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 6,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\nPricing Document-Preamble \\n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n305\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        227.51991271972656,\n        74.64318084716797,\n        377.9470520019531,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"Pricing Document-Preamble \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        99.36321258544922,\n        526.3881225585938,\n        177.9987030029297\n      ],\n      \"block_number\": 5,\n      \"text\": \"1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.3868408203125,\n        238.59861755371094\n      ],\n      \"block_number\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99929809570312,\n        247.923095703125,\n        526.387451171875,\n        326.4385681152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99847412109375,\n        335.7630310058594,\n        526.3863525390625,\n        387.0384826660156\n      ],\n      \"block_number\": 8,\n      \"text\": \"4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99948120117188,\n        396.36297607421875,\n        526.3870239257812,\n        420.3984680175781\n      ],\n      \"block_number\": 9,\n      \"text\": \"5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3870239257812,\n        467.31842041015625\n      ],\n      \"block_number\": 10,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3883666992188,\n        514.2384033203125\n      ],\n      \"block_number\": 11,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        523.5628662109375,\n        526.3883666992188,\n        602.1983642578125\n      ],\n      \"block_number\": 12,\n      \"text\": \"8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        611.5228271484375,\n        526.3880615234375,\n        649.1182861328125\n      ],\n      \"block_number\": 13,\n      \"text\": \"9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        658.4427490234375,\n        526.3875732421875,\n        709.71826171875\n      ],\n      \"block_number\": 14,\n      \"text\": \"10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99981689453125,\n        719.042724609375,\n        526.3865966796875,\n        756.6382446289062\n      ],\n      \"block_number\": 15,\n      \"text\": \"11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"305\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:00:35+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C49dd622e159286ee
    previous_evidence_ids:
    - J6f83ecf77cc57b25
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: summary
  text: Volume 4 Section J establishes the Financial Document, Letter of Price Bid, pricing rules and instructions, and Bill of Quantities (BOQ) abstract and item schedules for BMRCL Tender Package P1.
  evidence_ids:
  - Je35bc79dc160b3f0
  - Jabb0383ef371ea9a
  - J241ce183fcecf015
  - J05ebc60fd5ad4602
  - Jf17d55c6acfde864
  - Jf28ae5cc3f92b618
  - S10ec60af02b3e977
  - S212cc0e74fc3292f
  - S4bb84d1785d9399d
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: Ca5070fb096d89441
  citations:
  - id: Je35bc79dc160b3f0
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 6
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/5
    json_record_id: vol4/pricing_preamble/6
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"6\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/6\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3866577148438,\n        440.0784606933594\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        443.2829284667969,\n        526.3870239257812,\n        453.638427734375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"and statutory levies as per the laws in force as on last day of the month previous to the\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        456.9629211425781,\n        446.9472351074219,\n        467.31842041015625\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"month of invitation of this tender, except Goods and Services Tax (GST).\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\\nand statutory levies as per the laws in force as on last day of the month previous to the\\nmonth of invitation of this tender, except Goods and Services Tax (GST).\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jabb0383ef371ea9a
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/7
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 8,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\nContract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\nSl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n(Rs) \\n1 \\nSCHEDULE-A \\nPartial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n4,69,41,306.00\\n2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\nTotal of Schedules (A+B)\\n4,74,41,306.00\\n3 \\nSCHEDULE-C \\nCredit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n---- \\n \\n \\n \\n \\n \\n \\n \\n \\n \\n307\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        123.11994934082031,\n        74.64318084716797,\n        475.146728515625,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99957275390625,\n        88.32317352294922,\n        520.5064697265625,\n        140.43870544433594\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        72.0000228881836,\n        144.60321044921875,\n        526.3865966796875,\n        240.7587127685547\n      ],\n      \"block_number\": 6,\n      \"text\": \"Contract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.96002960205078,\n        244.203125,\n        528.9071655273438,\n        260.9186706542969\n      ],\n      \"block_number\": 7,\n      \"text\": \"Sl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n\"\n    },\n    {\n      \"bbox\": [\n        460.4398193359375,\n        256.92315673828125,\n        484.86712646484375,\n        267.2786560058594\n      ],\n      \"block_number\": 8,\n      \"text\": \"(Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        294.8431396484375,\n        186.78732299804688,\n        305.1986389160156\n      ],\n      \"block_number\": 9,\n      \"text\": \"1 \\nSCHEDULE-A \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        282.1231689453125,\n        405.0671081542969,\n        317.7986145019531\n      ],\n      \"block_number\": 10,\n      \"text\": \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n\"\n    },\n    {\n      \"bbox\": [\n        456.11981201171875,\n        294.72314453125,\n        529.6943969726562,\n        305.0786437988281\n      ],\n      \"block_number\": 11,\n      \"text\": \"4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        332.64312744140625,\n        529.6943969726562,\n        355.5986328125\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        271.31988525390625,\n        374.8830871582031,\n        529.6962280273438,\n        385.23858642578125\n      ],\n      \"block_number\": 13,\n      \"text\": \"Total of Schedules (A+B)\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        429.96307373046875,\n        187.02545166015625,\n        440.3185729980469\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nSCHEDULE-C \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        404.64306640625,\n        405.0672302246094,\n        465.6385498046875\n      ],\n      \"block_number\": 15,\n      \"text\": \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n\"\n    },\n    {\n      \"bbox\": [\n        463.7998046875,\n        429.96307373046875,\n        481.507080078125,\n        440.3185729980469\n      ],\n      \"block_number\": 16,\n      \"text\": \"---- \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        480.4830322265625,\n        75.06725311279297,\n        572.7985229492188\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\n \\n \\n \\n \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        576.0029296875,\n        526.386962890625,\n        586.3584594726562\n      ],\n      \"block_number\": 18,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        600.48291015625,\n        526.386962890625,\n        610.8384399414062\n      ],\n      \"block_number\": 19,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 20,\n      \"text\": \"307\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: J241ce183fcecf015
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/boq_abstract.json
    json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
    json_pointer: /records/0
    json_record_id: vol4/boq_abstract/A
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"46941306.00\",\n  \"amount_raw\": \"4,69,41,306.00\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      280.39,\n      100.77,\n      329.54\n    ],\n    [\n      102.17,\n      280.39,\n      194.06,\n      329.54\n    ],\n    [\n      195.45999999999998,\n      280.39,\n      406.82,\n      329.54\n    ],\n    [\n      408.21999999999997,\n      280.39,\n      534.17,\n      329.54\n    ]\n  ],\n  \"cells\": [\n    \"1\",\n    \"SCHEDULE-A\",\n    \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ\",\n    \"4,69,41,306.00\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/A\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: J05ebc60fd5ad4602
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 6
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/1
    json_record_id: vol4/pricing_preamble/2
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"2\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/2\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.38671875,\n        197.6786346435547\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        200.88311767578125,\n        526.3868408203125,\n        211.23863220214844\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"(provisional). The basis of payment will be the actual quantities of work ordered and\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        214.5631103515625,\n        526.3862915039062,\n        224.9186248779297\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"carried out, as measured by the Contractor and verified by the Engineer and valued at\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        228.24310302734375,\n        457.9883117675781,\n        238.59861755371094\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"the rates in the accepted priced “Price Bid – Summary of Bill of Quantities”.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated\\n(provisional). The basis of payment will be the actual quantities of work ordered and\\ncarried out, as measured by the Contractor and verified by the Engineer and valued at\\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jf17d55c6acfde864
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 6
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/5
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 6,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\nPricing Document-Preamble \\n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n305\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        227.51991271972656,\n        74.64318084716797,\n        377.9470520019531,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"Pricing Document-Preamble \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        99.36321258544922,\n        526.3881225585938,\n        177.9987030029297\n      ],\n      \"block_number\": 5,\n      \"text\": \"1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.3868408203125,\n        238.59861755371094\n      ],\n      \"block_number\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99929809570312,\n        247.923095703125,\n        526.387451171875,\n        326.4385681152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99847412109375,\n        335.7630310058594,\n        526.3863525390625,\n        387.0384826660156\n      ],\n      \"block_number\": 8,\n      \"text\": \"4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99948120117188,\n        396.36297607421875,\n        526.3870239257812,\n        420.3984680175781\n      ],\n      \"block_number\": 9,\n      \"text\": \"5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3870239257812,\n        467.31842041015625\n      ],\n      \"block_number\": 10,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3883666992188,\n        514.2384033203125\n      ],\n      \"block_number\": 11,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        523.5628662109375,\n        526.3883666992188,\n        602.1983642578125\n      ],\n      \"block_number\": 12,\n      \"text\": \"8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        611.5228271484375,\n        526.3880615234375,\n        649.1182861328125\n      ],\n      \"block_number\": 13,\n      \"text\": \"9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        658.4427490234375,\n        526.3875732421875,\n        709.71826171875\n      ],\n      \"block_number\": 14,\n      \"text\": \"10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99981689453125,\n        719.042724609375,\n        526.3865966796875,\n        756.6382446289062\n      ],\n      \"block_number\": 15,\n      \"text\": \"11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"305\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jf28ae5cc3f92b618
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 1
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/0
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 1,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \"  \\n \\n \\n    \\n \\n \\n \\n \\n \\n \\n \\n \\n                       \\nBANGALORE METRO RAIL PROJECT, PHASE-3 \\n \\nName of the Work: “Partial and Full Demolition/Dismantling of \\nBuildings/Structures identified in Bangalore Metro Rail Project Phase-3.” \\nContract Package-P1: “Partial and Full Demolition/Dismantling of \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore \\nRoad Station (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1 of \\nBangalore Metro Rail Project Phase-3.”       \\n \\n \\n        \\nTender No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157 \\nSEPTEMBER-2026 \\nFINANCIAL DOCUMENT \\n(Pricing Document) \\nVOLUME - 4  \\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        63.9599723815918,\n        19.569625854492188,\n        302.403564453125,\n        44.40032958984375\n      ],\n      \"block_number\": 0,\n      \"text\": \"  \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        63.9599723815918,\n        97.07410430908203,\n        66.45352172851562,\n        104.04034423828125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        63.9599723815918,\n        122.51410675048828,\n        73.89351654052734,\n        129.4803466796875\n      ],\n      \"block_number\": 2,\n      \"text\": \"    \\n\"\n    },\n    {\n      \"bbox\": [\n        14.400049209594727,\n        147.95411682128906,\n        304.29351806640625,\n        154.92034912109375\n      ],\n      \"block_number\": 3,\n      \"text\": \" \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        14.400049209594727,\n        173.3941192626953,\n        16.893596649169922,\n        180.3603515625\n      ],\n      \"block_number\": 4,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        14.400049209594727,\n        198.8340606689453,\n        16.893596649169922,\n        205.80029296875\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        14.400049209594727,\n        224.27406311035156,\n        491.492431640625,\n        231.24029541015625\n      ],\n      \"block_number\": 6,\n      \"text\": \" \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        49.79998016357422,\n        250.77337646484375,\n        544.8611450195312,\n        358.8686218261719\n      ],\n      \"block_number\": 7,\n      \"text\": \" \\n                       \\nBANGALORE METRO RAIL PROJECT, PHASE-3 \\n \\nName of the Work: “Partial and Full Demolition/Dismantling of \\nBuildings/Structures identified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        68.3995361328125,\n        364.299072265625,\n        544.8632202148438,\n        476.8801574707031\n      ],\n      \"block_number\": 8,\n      \"text\": \"Contract Package-P1: “Partial and Full Demolition/Dismantling of \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore \\nRoad Station (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1 of \\nBangalore Metro Rail Project Phase-3.”       \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        108.47999572753906,\n        492.7681579589844,\n        153.18820190429688,\n        515.2801513671875\n      ],\n      \"block_number\": 9,\n      \"text\": \"        \\n\"\n    },\n    {\n      \"bbox\": [\n        101.75995635986328,\n        65.61921691894531,\n        498.2138366699219,\n        78.78872680664062\n      ],\n      \"block_number\": 10,\n      \"text\": \"Tender No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157 \\n\"\n    },\n    {\n      \"bbox\": [\n        239.87989807128906,\n        600.3389282226562,\n        366.7764892578125,\n        613.5084838867188\n      ],\n      \"block_number\": 11,\n      \"text\": \"SEPTEMBER-2026 \\n\"\n    },\n    {\n      \"bbox\": [\n        222.4799041748047,\n        498.3390197753906,\n        386.7032470703125,\n        511.508544921875\n      ],\n      \"block_number\": 12,\n      \"text\": \"FINANCIAL DOCUMENT \\n\"\n    },\n    {\n      \"bbox\": [\n        238.0798797607422,\n        514.4190063476562,\n        371.10076904296875,\n        527.5885620117188\n      ],\n      \"block_number\": 13,\n      \"text\": \"(Pricing Document) \\n\"\n    },\n    {\n      \"bbox\": [\n        262.55303955078125,\n        540.5789794921875,\n        350.4632568359375,\n        553.74853515625\n      ],\n      \"block_number\": 14,\n      \"text\": \"VOLUME - 4  \\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: S10ec60af02b3e977
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: 1.0 — Pricing Document Preamble and Instructions
    source_document: Vol4DLNP1.pdf
    pdf_pages:
    - 6
    quote: "- **Read BOQ with the Complete Tender and Contract Documents** (Instruction 1)\n- **Provisional Quantities and Payment for Measured Work** (Instruction 2)\n- **Price Bid Preparation in the Prescribed XLS Sheet** (Instruction 3; ITT 10)\n  - Schedule-A: percentage rate to two decimals; At Par / Excess / Less\n  - Schedule-B: At Par only\n  - Schedule-C: lump-sum salvage credit to BMRCL\n- **Proportionate Recovery and Adjustment of Salvage Credit** (Instruction 4)\n- **Salvage Credit Based on Quoted Price** (Instruction 5)\n- **Taxes and Statutory Levies Included, Except GST** (Instruction 6)\n- **Measurement of Completed Work** (Instruction 7)\n- **Completed-Work Pricing and Included Execution Costs** (Instruction 8)\n- **Included Safety and Protection Costs** (Instruction 9)\n- **Overheads, Profit, Risks and Defect-Remedy Obligations** (Instruction 10)\n- **Accommodation, Insurance, Wages and Approval Costs** (Instruction 11)\n\n\n\n- **Execution Standards and Engineer’s Directions** (Instruction 12)\n- **Incidental Removal Works Without Separate Payment** (Instruction 13)\n- **Temporary Relocation and Protection of Utilities** (Instruction 14)\n- **Temporary Works, Power and Supports at Contractor’s Cost** (Instruction 15)\n- **Permanent Supports and Restoration Payment Provisions** (Instruction 16)\n- **Balcony and Canopy Area at 50%; Chejjas Excluded from Payment** (Instruction 17)\n- **Demolition Depth and Refilling of Low-Level Areas** (Instruction 18)\n- **Removal Within the Line of Cut, Excluding Trees** (Instruction 19)\n- **Total Floor Area as the Sum of Built Areas of All Floors** (Instruction 20)\n- **Building Additions or Deletions and Accepted Percentage Rates** (Instruction 21)"
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  - id: S212cc0e74fc3292f
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: 2.0 — Abstract of Bill of Quantities (BOQ)
    source_document: Vol4DLNP1.pdf
    pdf_pages:
    - 8
    quote: "- **Schedule-A — Demolition and Dismantling**\n  - Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ\n  - **Estimated Cost:** INR 4,69,41,306.00\n\n- **Schedule-B — KPWD Schedule-of-Rate Items**\n  - Items under Schedule of Rate published by KPWD\n  - **Estimated Cost:** INR 5,00,000.00\n\n- **Total of Schedules A+B:** INR 4,74,41,306.00\n\n- **Schedule-C — Salvage Credit to BMRCL**\n  - Credit for salvageable items from dismantled/demolished private properties in which the owner has no interest\n  - **Source Reference:** Para 15 of Part-3 of Employer’s Requirement\n  - **Estimated Cost Field:** `----`\n  - **Pricing Basis:** Lump-sum credit under Preamble Instruction 3"
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  - id: S4bb84d1785d9399d
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    pdf_pages:
    - 1
    - 2
    - 3
    - 4
    - 5
    - 6
    - 7
    - 8
    - 9
    - 10
    quote: This section contains the financial document for BMRCL Tender No. `BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157`, covering the Letter of Price Bid, pricing instructions, BOQ abstract and work schedules.
    page_basis: OKF reference, not independently PDF-verified
    page_precision: document_metadata_range
  created_at: '2026-10-31T16:02:22+00:00'
  status: draft
  editorial_history:
  - corrected_at: '2026-11-01T11:49:40+00:00'
    method: reviewed repetition consolidation
    previous_claims:
    - kind: summary
      text: Volume 4 Section J provides the financial document, Letter of Price Bid, pricing rules and instructions, and the Bill of Quantities (BOQ) abstract for BMRCL Tender Package P1.
      evidence_ids:
      - J026debd7f34d6fd9
      - J23599c81d83cf26f
      - J277f317485dab92c
      - S19382a03427e15ba
      - S469ca02217533c37
      - S95cca961b3adbe67
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: Ca3df89a6aadc3ebc
      citations:
      - id: J026debd7f34d6fd9
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/5
        json_record_id: vol4/pricing_preamble/6
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"6\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/6\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3866577148438,\n        440.0784606933594\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        443.2829284667969,\n        526.3870239257812,\n        453.638427734375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"and statutory levies as per the laws in force as on last day of the month previous to the\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        456.9629211425781,\n        446.9472351074219,\n        467.31842041015625\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"month of invitation of this tender, except Goods and Services Tax (GST).\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\\nand statutory levies as per the laws in force as on last day of the month previous to the\\nmonth of invitation of this tender, except Goods and Services Tax (GST).\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J23599c81d83cf26f
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 8
        sheet_cells: ''
        json_path: parsed_json/vol4/boq_abstract.json
        json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
        json_pointer: /records/0
        json_record_id: vol4/boq_abstract/A
        source_review_status: pending_manual_review
        quote: "{\n  \"amount_inr_decimal\": \"46941306.00\",\n  \"amount_raw\": \"4,69,41,306.00\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      280.39,\n      100.77,\n      329.54\n    ],\n    [\n      102.17,\n      280.39,\n      194.06,\n      329.54\n    ],\n    [\n      195.45999999999998,\n      280.39,\n      406.82,\n      329.54\n    ],\n    [\n      408.21999999999997,\n      280.39,\n      534.17,\n      329.54\n    ]\n  ],\n  \"cells\": [\n    \"1\",\n    \"SCHEDULE-A\",\n    \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ\",\n    \"4,69,41,306.00\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/A\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J277f317485dab92c
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/1
        json_record_id: vol4/pricing_preamble/2
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"2\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/2\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.38671875,\n        197.6786346435547\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        200.88311767578125,\n        526.3868408203125,\n        211.23863220214844\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"(provisional). The basis of payment will be the actual quantities of work ordered and\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        214.5631103515625,\n        526.3862915039062,\n        224.9186248779297\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"carried out, as measured by the Contractor and verified by the Engineer and valued at\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        228.24310302734375,\n        457.9883117675781,\n        238.59861755371094\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"the rates in the accepted priced “Price Bid – Summary of Bill of Quantities”.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated\\n(provisional). The basis of payment will be the actual quantities of work ordered and\\ncarried out, as measured by the Contractor and verified by the Engineer and valued at\\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”.\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: S19382a03427e15ba
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: 1.0 — Pricing Document Preamble and Instructions
        source_document: Vol4DLNP1.pdf
        pdf_pages:
        - 6
        quote: "- **Read BOQ with the Complete Tender and Contract Documents** (Instruction 1)\n- **Provisional Quantities and Payment for Measured Work** (Instruction 2)\n- **Price Bid Preparation in the Prescribed XLS Sheet** (Instruction 3; ITT 10)\n  - Schedule-A: percentage rate to two decimals; At Par / Excess / Less\n  - Schedule-B: At Par only\n  - Schedule-C: lump-sum salvage credit to BMRCL\n- **Proportionate Recovery and Adjustment of Salvage Credit** (Instruction 4)\n- **Salvage Credit Based on Quoted Price** (Instruction 5)\n- **Taxes and Statutory Levies Included, Except GST** (Instruction 6)\n- **Measurement of Completed Work** (Instruction 7)\n- **Completed-Work Pricing and Included Execution Costs** (Instruction 8)\n- **Included Safety and Protection Costs** (Instruction 9)\n- **Overheads, Profit, Risks and Defect-Remedy Obligations** (Instruction 10)\n- **Accommodation, Insurance, Wages and Approval Costs** (Instruction 11)\n\n\n\n- **Execution Standards and Engineer’s Directions** (Instruction 12)\n- **Incidental Removal Works Without Separate Payment** (Instruction 13)\n- **Temporary Relocation and Protection of Utilities** (Instruction 14)\n- **Temporary Works, Power and Supports at Contractor’s Cost** (Instruction 15)\n- **Permanent Supports and Restoration Payment Provisions** (Instruction 16)\n- **Balcony and Canopy Area at 50%; Chejjas Excluded from Payment** (Instruction 17)\n- **Demolition Depth and Refilling of Low-Level Areas** (Instruction 18)\n- **Removal Within the Line of Cut, Excluding Trees** (Instruction 19)\n- **Total Floor Area as the Sum of Built Areas of All Floors** (Instruction 20)\n- **Building Additions or Deletions and Accepted Percentage Rates** (Instruction 21)"
        page_basis: OKF reference, not independently PDF-verified
        page_precision: section_reference
      - id: S469ca02217533c37
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: 2.0 — Abstract of Bill of Quantities (BOQ)
        source_document: Vol4DLNP1.pdf
        pdf_pages:
        - 8
        quote: "- **Schedule-A — Demolition and Dismantling**\n  - Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ\n  - **Estimated Cost:** INR 4,69,41,306.00\n\n- **Schedule-B — KPWD Schedule-of-Rate Items**\n  - Items under Schedule of Rate published by KPWD\n  - **Estimated Cost:** INR 5,00,000.00\n\n- **Total of Schedules A+B:** INR 4,74,41,306.00\n\n- **Schedule-C — Salvage Credit to BMRCL**\n  - Credit for salvageable items from dismantled/demolished private properties in which the owner has no interest\n  - **Source Reference:** Para 15 of Part-3 of Employer’s Requirement\n  - **Estimated Cost Field:** `----`\n  - **Pricing Basis:** Lump-sum credit under Preamble Instruction 3"
        page_basis: OKF reference, not independently PDF-verified
        page_precision: section_reference
      - id: S95cca961b3adbe67
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        pdf_pages:
        - 1
        - 2
        - 3
        - 4
        - 5
        - 6
        - 7
        - 8
        - 9
        - 10
        quote: This section contains the financial document for BMRCL Tender No. `BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157`, covering the Letter of Price Bid, pricing instructions, BOQ abstract and work schedules.
        page_basis: OKF reference, not independently PDF-verified
        page_precision: document_metadata_range
      created_at: '2026-10-31T15:57:39+00:00'
      status: draft
    - kind: summary
      text: Volume 4 Section J sets forth the Financial Document, Letter of Price Bid, pricing rules and instructions, and Bill of Quantities (BOQ) abstract for BMRCL Tender Package P1.
      evidence_ids:
      - Jbd236df1211c8d28
      - J23599c81d83cf26f
      - J6f83ecf77cc57b25
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: C14767ebf3bdcffdc
      citations:
      - id: Jbd236df1211c8d28
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 1
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_document.json
        json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
        json_pointer: /pages/0
        json_record_id: null
        source_review_status: pending_manual_review
        quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 1,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \"  \\n \\n \\n    \\n \\n \\n \\n \\n \\n \\n \\n \\n                       \\nBANGALORE METRO RAIL PROJECT, PHASE-3 \\n \\nName of the Work: “Partial and Full Demolition/Dismantling of \\nBuildings/Structures identified in Bangalore Metro Rail Project Phase-3.” \\nContract Package-P1: “Partial and Full Demolition/Dismantling of \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore \\nRoad Station (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1 of \\nBangalore Metro Rail Project Phase-3.”       \\n \\n \\n        \\nTender No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157 \\nSEPTEMBER-2026 \\nFINANCIAL DOCUMENT \\n(Pricing Document) \\nVOLUME - 4  \\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        63.9599723815918,\n        19.569625854492188,\n        302.403564453125,\n        44.40032958984375\n      ],\n      \"block_number\": 0,\n      \"text\": \"  \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        63.9599723815918,\n        97.07410430908203,\n        66.45352172851562,\n        104.04034423828125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        63.9599723815918,\n        122.51410675048828,\n        73.89351654052734,\n        129.4803466796875\n      ],\n      \"block_number\": 2,\n      \"text\": \"    \\n\"\n    },\n    {\n      \"bbox\": [\n        14.400049209594727,\n        147.95411682128906,\n        304.29351806640625,\n        154.92034912109375\n      ],\n      \"block_number\": 3,\n      \"text\": \" \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        14.400049209594727,\n        173.3941192626953,\n        16.893596649169922,\n        180.3603515625\n      ],\n      \"block_number\": 4,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        14.400049209594727,\n        198.8340606689453,\n        16.893596649169922,\n        205.80029296875\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        14.400049209594727,\n        224.27406311035156,\n        491.492431640625,\n        231.24029541015625\n      ],\n      \"block_number\": 6,\n      \"text\": \" \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        49.79998016357422,\n        250.77337646484375,\n        544.8611450195312,\n        358.8686218261719\n      ],\n      \"block_number\": 7,\n      \"text\": \" \\n                       \\nBANGALORE METRO RAIL PROJECT, PHASE-3 \\n \\nName of the Work: “Partial and Full Demolition/Dismantling of \\nBuildings/Structures identified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        68.3995361328125,\n        364.299072265625,\n        544.8632202148438,\n        476.8801574707031\n      ],\n      \"block_number\": 8,\n      \"text\": \"Contract Package-P1: “Partial and Full Demolition/Dismantling of \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore \\nRoad Station (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1 of \\nBangalore Metro Rail Project Phase-3.”       \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        108.47999572753906,\n        492.7681579589844,\n        153.18820190429688,\n        515.2801513671875\n      ],\n      \"block_number\": 9,\n      \"text\": \"        \\n\"\n    },\n    {\n      \"bbox\": [\n        101.75995635986328,\n        65.61921691894531,\n        498.2138366699219,\n        78.78872680664062\n      ],\n      \"block_number\": 10,\n      \"text\": \"Tender No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157 \\n\"\n    },\n    {\n      \"bbox\": [\n        239.87989807128906,\n        600.3389282226562,\n        366.7764892578125,\n        613.5084838867188\n      ],\n      \"block_number\": 11,\n      \"text\": \"SEPTEMBER-2026 \\n\"\n    },\n    {\n      \"bbox\": [\n        222.4799041748047,\n        498.3390197753906,\n        386.7032470703125,\n        511.508544921875\n      ],\n      \"block_number\": 12,\n      \"text\": \"FINANCIAL DOCUMENT \\n\"\n    },\n    {\n      \"bbox\": [\n        238.0798797607422,\n        514.4190063476562,\n        371.10076904296875,\n        527.5885620117188\n      ],\n      \"block_number\": 13,\n      \"text\": \"(Pricing Document) \\n\"\n    },\n    {\n      \"bbox\": [\n        262.55303955078125,\n        540.5789794921875,\n        350.4632568359375,\n        553.74853515625\n      ],\n      \"block_number\": 14,\n      \"text\": \"VOLUME - 4  \\n\"\n    }\n  ]\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J23599c81d83cf26f
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 8
        sheet_cells: ''
        json_path: parsed_json/vol4/boq_abstract.json
        json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
        json_pointer: /records/0
        json_record_id: vol4/boq_abstract/A
        source_review_status: pending_manual_review
        quote: "{\n  \"amount_inr_decimal\": \"46941306.00\",\n  \"amount_raw\": \"4,69,41,306.00\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      280.39,\n      100.77,\n      329.54\n    ],\n    [\n      102.17,\n      280.39,\n      194.06,\n      329.54\n    ],\n    [\n      195.45999999999998,\n      280.39,\n      406.82,\n      329.54\n    ],\n    [\n      408.21999999999997,\n      280.39,\n      534.17,\n      329.54\n    ]\n  ],\n  \"cells\": [\n    \"1\",\n    \"SCHEDULE-A\",\n    \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ\",\n    \"4,69,41,306.00\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/A\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J6f83ecf77cc57b25
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_document.json
        json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
        json_pointer: /pages/5
        json_record_id: null
        source_review_status: pending_manual_review
        quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 6,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\nPricing Document-Preamble \\n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n305\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        227.51991271972656,\n        74.64318084716797,\n        377.9470520019531,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"Pricing Document-Preamble \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        99.36321258544922,\n        526.3881225585938,\n        177.9987030029297\n      ],\n      \"block_number\": 5,\n      \"text\": \"1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.3868408203125,\n        238.59861755371094\n      ],\n      \"block_number\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99929809570312,\n        247.923095703125,\n        526.387451171875,\n        326.4385681152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99847412109375,\n        335.7630310058594,\n        526.3863525390625,\n        387.0384826660156\n      ],\n      \"block_number\": 8,\n      \"text\": \"4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99948120117188,\n        396.36297607421875,\n        526.3870239257812,\n        420.3984680175781\n      ],\n      \"block_number\": 9,\n      \"text\": \"5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3870239257812,\n        467.31842041015625\n      ],\n      \"block_number\": 10,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3883666992188,\n        514.2384033203125\n      ],\n      \"block_number\": 11,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        523.5628662109375,\n        526.3883666992188,\n        602.1983642578125\n      ],\n      \"block_number\": 12,\n      \"text\": \"8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        611.5228271484375,\n        526.3880615234375,\n        649.1182861328125\n      ],\n      \"block_number\": 13,\n      \"text\": \"9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        658.4427490234375,\n        526.3875732421875,\n        709.71826171875\n      ],\n      \"block_number\": 14,\n      \"text\": \"10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99981689453125,\n        719.042724609375,\n        526.3865966796875,\n        756.6382446289062\n      ],\n      \"block_number\": 15,\n      \"text\": \"11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"305\\n\"\n    }\n  ]\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      created_at: '2026-10-31T16:00:35+00:00'
      status: draft
    - kind: summary
      text: Volume 4 Section J establishes the Financial Document, Letter of Price Bid, pricing rules and instructions, and Bill of Quantities (BOQ) abstract and item schedules for BMRCL Tender Package P1.
      evidence_ids:
      - J026debd7f34d6fd9
      - J15df25270985d9b6
      - J277f317485dab92c
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: C3c029413f855f5e6
      citations:
      - id: J026debd7f34d6fd9
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/5
        json_record_id: vol4/pricing_preamble/6
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"6\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/6\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3866577148438,\n        440.0784606933594\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        443.2829284667969,\n        526.3870239257812,\n        453.638427734375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"and statutory levies as per the laws in force as on last day of the month previous to the\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        456.9629211425781,\n        446.9472351074219,\n        467.31842041015625\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"month of invitation of this tender, except Goods and Services Tax (GST).\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\\nand statutory levies as per the laws in force as on last day of the month previous to the\\nmonth of invitation of this tender, except Goods and Services Tax (GST).\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J15df25270985d9b6
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 8
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_document.json
        json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
        json_pointer: /pages/7
        json_record_id: null
        source_review_status: pending_manual_review
        quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 8,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\nContract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\nSl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n(Rs) \\n1 \\nSCHEDULE-A \\nPartial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n4,69,41,306.00\\n2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\nTotal of Schedules (A+B)\\n4,74,41,306.00\\n3 \\nSCHEDULE-C \\nCredit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n---- \\n \\n \\n \\n \\n \\n \\n \\n \\n \\n307\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        123.11994934082031,\n        74.64318084716797,\n        475.146728515625,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99957275390625,\n        88.32317352294922,\n        520.5064697265625,\n        140.43870544433594\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        72.0000228881836,\n        144.60321044921875,\n        526.3865966796875,\n        240.7587127685547\n      ],\n      \"block_number\": 6,\n      \"text\": \"Contract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.96002960205078,\n        244.203125,\n        528.9071655273438,\n        260.9186706542969\n      ],\n      \"block_number\": 7,\n      \"text\": \"Sl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n\"\n    },\n    {\n      \"bbox\": [\n        460.4398193359375,\n        256.92315673828125,\n        484.86712646484375,\n        267.2786560058594\n      ],\n      \"block_number\": 8,\n      \"text\": \"(Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        294.8431396484375,\n        186.78732299804688,\n        305.1986389160156\n      ],\n      \"block_number\": 9,\n      \"text\": \"1 \\nSCHEDULE-A \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        282.1231689453125,\n        405.0671081542969,\n        317.7986145019531\n      ],\n      \"block_number\": 10,\n      \"text\": \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n\"\n    },\n    {\n      \"bbox\": [\n        456.11981201171875,\n        294.72314453125,\n        529.6943969726562,\n        305.0786437988281\n      ],\n      \"block_number\": 11,\n      \"text\": \"4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        332.64312744140625,\n        529.6943969726562,\n        355.5986328125\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        271.31988525390625,\n        374.8830871582031,\n        529.6962280273438,\n        385.23858642578125\n      ],\n      \"block_number\": 13,\n      \"text\": \"Total of Schedules (A+B)\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        429.96307373046875,\n        187.02545166015625,\n        440.3185729980469\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nSCHEDULE-C \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        404.64306640625,\n        405.0672302246094,\n        465.6385498046875\n      ],\n      \"block_number\": 15,\n      \"text\": \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n\"\n    },\n    {\n      \"bbox\": [\n        463.7998046875,\n        429.96307373046875,\n        481.507080078125,\n        440.3185729980469\n      ],\n      \"block_number\": 16,\n      \"text\": \"---- \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        480.4830322265625,\n        75.06725311279297,\n        572.7985229492188\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\n \\n \\n \\n \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        576.0029296875,\n        526.386962890625,\n        586.3584594726562\n      ],\n      \"block_number\": 18,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        600.48291015625,\n        526.386962890625,\n        610.8384399414062\n      ],\n      \"block_number\": 19,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 20,\n      \"text\": \"307\\n\"\n    }\n  ]\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J277f317485dab92c
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/1
        json_record_id: vol4/pricing_preamble/2
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"2\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/2\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.38671875,\n        197.6786346435547\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        200.88311767578125,\n        526.3868408203125,\n        211.23863220214844\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"(provisional). The basis of payment will be the actual quantities of work ordered and\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        214.5631103515625,\n        526.3862915039062,\n        224.9186248779297\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"carried out, as measured by the Contractor and verified by the Engineer and valued at\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        228.24310302734375,\n        457.9883117675781,\n        238.59861755371094\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"the rates in the accepted priced “Price Bid – Summary of Bill of Quantities”.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated\\n(provisional). The basis of payment will be the actual quantities of work ordered and\\ncarried out, as measured by the Contractor and verified by the Engineer and valued at\\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”.\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      created_at: '2026-10-31T16:02:22+00:00'
      status: draft
    - kind: summary
      text: Volume 4 Section J provides the Financial Document, Letter of Price Bid, pricing rules, and Bill of Quantities (BOQ) abstract for BMRCL Tender Package P1.
      evidence_ids:
      - J026debd7f34d6fd9
      - J15df25270985d9b6
      - J277f317485dab92c
      - J6f83ecf77cc57b25
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: Cc7dfebb58b982cbe
      citations:
      - id: J026debd7f34d6fd9
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/5
        json_record_id: vol4/pricing_preamble/6
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"6\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/6\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3866577148438,\n        440.0784606933594\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        443.2829284667969,\n        526.3870239257812,\n        453.638427734375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"and statutory levies as per the laws in force as on last day of the month previous to the\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        456.9629211425781,\n        446.9472351074219,\n        467.31842041015625\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"month of invitation of this tender, except Goods and Services Tax (GST).\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\\nand statutory levies as per the laws in force as on last day of the month previous to the\\nmonth of invitation of this tender, except Goods and Services Tax (GST).\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J15df25270985d9b6
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 8
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_document.json
        json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
        json_pointer: /pages/7
        json_record_id: null
        source_review_status: pending_manual_review
        quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 8,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\nContract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\nSl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n(Rs) \\n1 \\nSCHEDULE-A \\nPartial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n4,69,41,306.00\\n2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\nTotal of Schedules (A+B)\\n4,74,41,306.00\\n3 \\nSCHEDULE-C \\nCredit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n---- \\n \\n \\n \\n \\n \\n \\n \\n \\n \\n307\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        123.11994934082031,\n        74.64318084716797,\n        475.146728515625,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99957275390625,\n        88.32317352294922,\n        520.5064697265625,\n        140.43870544433594\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        72.0000228881836,\n        144.60321044921875,\n        526.3865966796875,\n        240.7587127685547\n      ],\n      \"block_number\": 6,\n      \"text\": \"Contract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.96002960205078,\n        244.203125,\n        528.9071655273438,\n        260.9186706542969\n      ],\n      \"block_number\": 7,\n      \"text\": \"Sl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n\"\n    },\n    {\n      \"bbox\": [\n        460.4398193359375,\n        256.92315673828125,\n        484.86712646484375,\n        267.2786560058594\n      ],\n      \"block_number\": 8,\n      \"text\": \"(Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        294.8431396484375,\n        186.78732299804688,\n        305.1986389160156\n      ],\n      \"block_number\": 9,\n      \"text\": \"1 \\nSCHEDULE-A \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        282.1231689453125,\n        405.0671081542969,\n        317.7986145019531\n      ],\n      \"block_number\": 10,\n      \"text\": \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n\"\n    },\n    {\n      \"bbox\": [\n        456.11981201171875,\n        294.72314453125,\n        529.6943969726562,\n        305.0786437988281\n      ],\n      \"block_number\": 11,\n      \"text\": \"4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        332.64312744140625,\n        529.6943969726562,\n        355.5986328125\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        271.31988525390625,\n        374.8830871582031,\n        529.6962280273438,\n        385.23858642578125\n      ],\n      \"block_number\": 13,\n      \"text\": \"Total of Schedules (A+B)\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        429.96307373046875,\n        187.02545166015625,\n        440.3185729980469\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nSCHEDULE-C \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        404.64306640625,\n        405.0672302246094,\n        465.6385498046875\n      ],\n      \"block_number\": 15,\n      \"text\": \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n\"\n    },\n    {\n      \"bbox\": [\n        463.7998046875,\n        429.96307373046875,\n        481.507080078125,\n        440.3185729980469\n      ],\n      \"block_number\": 16,\n      \"text\": \"---- \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        480.4830322265625,\n        75.06725311279297,\n        572.7985229492188\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\n \\n \\n \\n \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        576.0029296875,\n        526.386962890625,\n        586.3584594726562\n      ],\n      \"block_number\": 18,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        600.48291015625,\n        526.386962890625,\n        610.8384399414062\n      ],\n      \"block_number\": 19,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 20,\n      \"text\": \"307\\n\"\n    }\n  ]\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J277f317485dab92c
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/1
        json_record_id: vol4/pricing_preamble/2
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"2\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/2\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.38671875,\n        197.6786346435547\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        200.88311767578125,\n        526.3868408203125,\n        211.23863220214844\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"(provisional). The basis of payment will be the actual quantities of work ordered and\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        214.5631103515625,\n        526.3862915039062,\n        224.9186248779297\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"carried out, as measured by the Contractor and verified by the Engineer and valued at\"\n    },\n    {\n      \"bbox\": [\n        89.87957000732422,\n        228.24310302734375,\n        457.9883117675781,\n        238.59861755371094\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"the rates in the accepted priced “Price Bid – Summary of Bill of Quantities”.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated\\n(provisional). The basis of payment will be the actual quantities of work ordered and\\ncarried out, as measured by the Contractor and verified by the Engineer and valued at\\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”.\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J6f83ecf77cc57b25
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_document.json
        json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
        json_pointer: /pages/5
        json_record_id: null
        source_review_status: pending_manual_review
        quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 6,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\nPricing Document-Preamble \\n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n305\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        227.51991271972656,\n        74.64318084716797,\n        377.9470520019531,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"Pricing Document-Preamble \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        99.36321258544922,\n        526.3881225585938,\n        177.9987030029297\n      ],\n      \"block_number\": 5,\n      \"text\": \"1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.3868408203125,\n        238.59861755371094\n      ],\n      \"block_number\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99929809570312,\n        247.923095703125,\n        526.387451171875,\n        326.4385681152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99847412109375,\n        335.7630310058594,\n        526.3863525390625,\n        387.0384826660156\n      ],\n      \"block_number\": 8,\n      \"text\": \"4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99948120117188,\n        396.36297607421875,\n        526.3870239257812,\n        420.3984680175781\n      ],\n      \"block_number\": 9,\n      \"text\": \"5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3870239257812,\n        467.31842041015625\n      ],\n      \"block_number\": 10,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3883666992188,\n        514.2384033203125\n      ],\n      \"block_number\": 11,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        523.5628662109375,\n        526.3883666992188,\n        602.1983642578125\n      ],\n      \"block_number\": 12,\n      \"text\": \"8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        611.5228271484375,\n        526.3880615234375,\n        649.1182861328125\n      ],\n      \"block_number\": 13,\n      \"text\": \"9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        658.4427490234375,\n        526.3875732421875,\n        709.71826171875\n      ],\n      \"block_number\": 14,\n      \"text\": \"10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99981689453125,\n        719.042724609375,\n        526.3865966796875,\n        756.6382446289062\n      ],\n      \"block_number\": 15,\n      \"text\": \"11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"305\\n\"\n    }\n  ]\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      created_at: '2026-10-31T16:03:48+00:00'
      status: draft
  - previous_claim_id: C8e532db78cc0f946
    previous_evidence_ids:
    - J026debd7f34d6fd9
    - J15df25270985d9b6
    - J23599c81d83cf26f
    - J277f317485dab92c
    - J6f83ecf77cc57b25
    - Jbd236df1211c8d28
    - S19382a03427e15ba
    - S469ca02217533c37
    - S95cca961b3adbe67
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  updated_at: '2026-11-01T11:49:40+00:00'
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: The total estimated cost for Schedule-A (Partial & Full demolition and dismantling work) is ₹ 4,69,41,306.00.
  evidence_ids:
  - Je67086ad8617857f
  - Jabb0383ef371ea9a
  - J241ce183fcecf015
  - S212cc0e74fc3292f
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C1a2679c7c01e761f
  citations:
  - id: Je67086ad8617857f
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: BOQ_338417.xls
    source_sha256: be376d7be062f1b7d481a0c1e07a132896504f5218450cdb02d039c495425896
    pdf_pages: []
    sheet_cells: BoQ1 row 13
    json_path: parsed_json/boq/boq_workbook.json
    json_sha256: 569d85cec3466a8ae5a5140c1186aba149aa87755785d0b4ed2b48921f9dfff0
    json_pointer: /schedules/0
    json_record_id: boq/schedule_a
    source_review_status: pending_manual_review
    quote: "{\n  \"description\": \"SCHEDULE-A: Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ\",\n  \"description_cell\": \"B13\",\n  \"estimated_cost_or_credit_label\": {\n    \"address\": \"F13\",\n    \"cell_type\": \"number\",\n    \"column\": 6,\n    \"formula_hidden_style\": false,\n    \"locked\": true,\n    \"number_format\": \"#,##0.00\",\n    \"row\": 13,\n    \"value\": 46941306.0,\n    \"xf_index\": 167\n  },\n  \"excel_row\": 13,\n  \"percentage_selection\": {\n    \"address\": \"N13\",\n    \"cell_type\": \"text\",\n    \"column\": 14,\n    \"formula_hidden_style\": false,\n    \"locked\": false,\n    \"number_format\": \"0.00%\",\n    \"row\": 13,\n    \"value\": \"Select\",\n    \"xf_index\": 130\n  },\n  \"quote_input\": {\n    \"address\": \"M13\",\n    \"cell_type\": \"formatted_blank\",\n    \"column\": 13,\n    \"formula_hidden_style\": false,\n    \"locked\": false,\n    \"number_format\": \"0.00\",\n    \"row\": 13,\n    \"value\": \"\",\n    \"xf_index\": 143\n  },\n  \"record_id\": \"boq/schedule_a\",\n  \"review_status\": \"pending_manual_review\",\n  \"saved_amount\": {\n    \"address\": \"BA13\",\n    \"cell_type\": \"number\",\n    \"column\": 53,\n    \"formula_hidden_style\": false,\n    \"locked\": true,\n    \"number_format\": \"0.00\",\n    \"row\": 13,\n    \"value\": 0.0,\n    \"xf_index\": 173\n  },\n  \"schedule\": \"A\",\n  \"sheet\": \"BoQ1\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jabb0383ef371ea9a
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/7
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 8,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\nContract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\nSl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n(Rs) \\n1 \\nSCHEDULE-A \\nPartial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n4,69,41,306.00\\n2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\nTotal of Schedules (A+B)\\n4,74,41,306.00\\n3 \\nSCHEDULE-C \\nCredit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n---- \\n \\n \\n \\n \\n \\n \\n \\n \\n \\n307\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        123.11994934082031,\n        74.64318084716797,\n        475.146728515625,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99957275390625,\n        88.32317352294922,\n        520.5064697265625,\n        140.43870544433594\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        72.0000228881836,\n        144.60321044921875,\n        526.3865966796875,\n        240.7587127685547\n      ],\n      \"block_number\": 6,\n      \"text\": \"Contract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.96002960205078,\n        244.203125,\n        528.9071655273438,\n        260.9186706542969\n      ],\n      \"block_number\": 7,\n      \"text\": \"Sl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n\"\n    },\n    {\n      \"bbox\": [\n        460.4398193359375,\n        256.92315673828125,\n        484.86712646484375,\n        267.2786560058594\n      ],\n      \"block_number\": 8,\n      \"text\": \"(Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        294.8431396484375,\n        186.78732299804688,\n        305.1986389160156\n      ],\n      \"block_number\": 9,\n      \"text\": \"1 \\nSCHEDULE-A \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        282.1231689453125,\n        405.0671081542969,\n        317.7986145019531\n      ],\n      \"block_number\": 10,\n      \"text\": \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n\"\n    },\n    {\n      \"bbox\": [\n        456.11981201171875,\n        294.72314453125,\n        529.6943969726562,\n        305.0786437988281\n      ],\n      \"block_number\": 11,\n      \"text\": \"4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        332.64312744140625,\n        529.6943969726562,\n        355.5986328125\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        271.31988525390625,\n        374.8830871582031,\n        529.6962280273438,\n        385.23858642578125\n      ],\n      \"block_number\": 13,\n      \"text\": \"Total of Schedules (A+B)\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        429.96307373046875,\n        187.02545166015625,\n        440.3185729980469\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nSCHEDULE-C \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        404.64306640625,\n        405.0672302246094,\n        465.6385498046875\n      ],\n      \"block_number\": 15,\n      \"text\": \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n\"\n    },\n    {\n      \"bbox\": [\n        463.7998046875,\n        429.96307373046875,\n        481.507080078125,\n        440.3185729980469\n      ],\n      \"block_number\": 16,\n      \"text\": \"---- \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        480.4830322265625,\n        75.06725311279297,\n        572.7985229492188\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\n \\n \\n \\n \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        576.0029296875,\n        526.386962890625,\n        586.3584594726562\n      ],\n      \"block_number\": 18,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        600.48291015625,\n        526.386962890625,\n        610.8384399414062\n      ],\n      \"block_number\": 19,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 20,\n      \"text\": \"307\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: J241ce183fcecf015
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/boq_abstract.json
    json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
    json_pointer: /records/0
    json_record_id: vol4/boq_abstract/A
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"46941306.00\",\n  \"amount_raw\": \"4,69,41,306.00\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      280.39,\n      100.77,\n      329.54\n    ],\n    [\n      102.17,\n      280.39,\n      194.06,\n      329.54\n    ],\n    [\n      195.45999999999998,\n      280.39,\n      406.82,\n      329.54\n    ],\n    [\n      408.21999999999997,\n      280.39,\n      534.17,\n      329.54\n    ]\n  ],\n  \"cells\": [\n    \"1\",\n    \"SCHEDULE-A\",\n    \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ\",\n    \"4,69,41,306.00\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/A\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: S212cc0e74fc3292f
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: 2.0 — Abstract of Bill of Quantities (BOQ)
    source_document: Vol4DLNP1.pdf
    pdf_pages:
    - 8
    quote: "- **Schedule-A — Demolition and Dismantling**\n  - Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ\n  - **Estimated Cost:** INR 4,69,41,306.00\n\n- **Schedule-B — KPWD Schedule-of-Rate Items**\n  - Items under Schedule of Rate published by KPWD\n  - **Estimated Cost:** INR 5,00,000.00\n\n- **Total of Schedules A+B:** INR 4,74,41,306.00\n\n- **Schedule-C — Salvage Credit to BMRCL**\n  - Credit for salvageable items from dismantled/demolished private properties in which the owner has no interest\n  - **Source Reference:** Para 15 of Part-3 of Employer’s Requirement\n  - **Estimated Cost Field:** `----`\n  - **Pricing Basis:** Lump-sum credit under Preamble Instruction 3"
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  created_at: '2026-10-31T16:02:22+00:00'
  status: draft
  consolidated_claim_ids:
  - C1ab250f373745adc
  editorial_history:
  - corrected_at: '2026-11-01T11:49:40+00:00'
    method: reviewed repetition consolidation
    previous_claims:
    - kind: parameter
      text: The estimated cost put to tender for Schedule-A (Partial & Full demolition and dismantling work) is INR 4,69,41,306.00.
      evidence_ids:
      - J23599c81d83cf26f
      - S469ca02217533c37
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: Ca854d21449e5bb09
      citations:
      - id: J23599c81d83cf26f
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 8
        sheet_cells: ''
        json_path: parsed_json/vol4/boq_abstract.json
        json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
        json_pointer: /records/0
        json_record_id: vol4/boq_abstract/A
        source_review_status: pending_manual_review
        quote: "{\n  \"amount_inr_decimal\": \"46941306.00\",\n  \"amount_raw\": \"4,69,41,306.00\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      280.39,\n      100.77,\n      329.54\n    ],\n    [\n      102.17,\n      280.39,\n      194.06,\n      329.54\n    ],\n    [\n      195.45999999999998,\n      280.39,\n      406.82,\n      329.54\n    ],\n    [\n      408.21999999999997,\n      280.39,\n      534.17,\n      329.54\n    ]\n  ],\n  \"cells\": [\n    \"1\",\n    \"SCHEDULE-A\",\n    \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ\",\n    \"4,69,41,306.00\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/A\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: S469ca02217533c37
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: 2.0 — Abstract of Bill of Quantities (BOQ)
        source_document: Vol4DLNP1.pdf
        pdf_pages:
        - 8
        quote: "- **Schedule-A — Demolition and Dismantling**\n  - Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ\n  - **Estimated Cost:** INR 4,69,41,306.00\n\n- **Schedule-B — KPWD Schedule-of-Rate Items**\n  - Items under Schedule of Rate published by KPWD\n  - **Estimated Cost:** INR 5,00,000.00\n\n- **Total of Schedules A+B:** INR 4,74,41,306.00\n\n- **Schedule-C — Salvage Credit to BMRCL**\n  - Credit for salvageable items from dismantled/demolished private properties in which the owner has no interest\n  - **Source Reference:** Para 15 of Part-3 of Employer’s Requirement\n  - **Estimated Cost Field:** `----`\n  - **Pricing Basis:** Lump-sum credit under Preamble Instruction 3"
        page_basis: OKF reference, not independently PDF-verified
        page_precision: section_reference
      created_at: '2026-10-31T15:57:39+00:00'
      status: draft
    - kind: parameter
      text: The total estimated cost for Schedule-A (Partial & Full demolition and dismantling work) is ₹ 4,69,41,306.00.
      evidence_ids:
      - J110eb79934e3efe2
      - J15df25270985d9b6
      - J23599c81d83cf26f
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: C71803482202cf6b6
      citations:
      - id: J110eb79934e3efe2
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: BOQ_338417.xls
        source_sha256: be376d7be062f1b7d481a0c1e07a132896504f5218450cdb02d039c495425896
        pdf_pages: []
        sheet_cells: BoQ1 row 13
        json_path: parsed_json/boq/boq_workbook.json
        json_sha256: 569d85cec3466a8ae5a5140c1186aba149aa87755785d0b4ed2b48921f9dfff0
        json_pointer: /schedules/0
        json_record_id: boq/schedule_a
        source_review_status: pending_manual_review
        quote: "{\n  \"description\": \"SCHEDULE-A: Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ\",\n  \"description_cell\": \"B13\",\n  \"estimated_cost_or_credit_label\": {\n    \"address\": \"F13\",\n    \"cell_type\": \"number\",\n    \"column\": 6,\n    \"formula_hidden_style\": false,\n    \"locked\": true,\n    \"number_format\": \"#,##0.00\",\n    \"row\": 13,\n    \"value\": 46941306.0,\n    \"xf_index\": 167\n  },\n  \"excel_row\": 13,\n  \"percentage_selection\": {\n    \"address\": \"N13\",\n    \"cell_type\": \"text\",\n    \"column\": 14,\n    \"formula_hidden_style\": false,\n    \"locked\": false,\n    \"number_format\": \"0.00%\",\n    \"row\": 13,\n    \"value\": \"Select\",\n    \"xf_index\": 130\n  },\n  \"quote_input\": {\n    \"address\": \"M13\",\n    \"cell_type\": \"formatted_blank\",\n    \"column\": 13,\n    \"formula_hidden_style\": false,\n    \"locked\": false,\n    \"number_format\": \"0.00\",\n    \"row\": 13,\n    \"value\": \"\",\n    \"xf_index\": 143\n  },\n  \"record_id\": \"boq/schedule_a\",\n  \"review_status\": \"pending_manual_review\",\n  \"saved_amount\": {\n    \"address\": \"BA13\",\n    \"cell_type\": \"number\",\n    \"column\": 53,\n    \"formula_hidden_style\": false,\n    \"locked\": true,\n    \"number_format\": \"0.00\",\n    \"row\": 13,\n    \"value\": 0.0,\n    \"xf_index\": 173\n  },\n  \"schedule\": \"A\",\n  \"sheet\": \"BoQ1\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J15df25270985d9b6
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 8
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_document.json
        json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
        json_pointer: /pages/7
        json_record_id: null
        source_review_status: pending_manual_review
        quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 8,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\nContract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\nSl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n(Rs) \\n1 \\nSCHEDULE-A \\nPartial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n4,69,41,306.00\\n2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\nTotal of Schedules (A+B)\\n4,74,41,306.00\\n3 \\nSCHEDULE-C \\nCredit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n---- \\n \\n \\n \\n \\n \\n \\n \\n \\n \\n307\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        123.11994934082031,\n        74.64318084716797,\n        475.146728515625,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99957275390625,\n        88.32317352294922,\n        520.5064697265625,\n        140.43870544433594\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        72.0000228881836,\n        144.60321044921875,\n        526.3865966796875,\n        240.7587127685547\n      ],\n      \"block_number\": 6,\n      \"text\": \"Contract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.96002960205078,\n        244.203125,\n        528.9071655273438,\n        260.9186706542969\n      ],\n      \"block_number\": 7,\n      \"text\": \"Sl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n\"\n    },\n    {\n      \"bbox\": [\n        460.4398193359375,\n        256.92315673828125,\n        484.86712646484375,\n        267.2786560058594\n      ],\n      \"block_number\": 8,\n      \"text\": \"(Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        294.8431396484375,\n        186.78732299804688,\n        305.1986389160156\n      ],\n      \"block_number\": 9,\n      \"text\": \"1 \\nSCHEDULE-A \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        282.1231689453125,\n        405.0671081542969,\n        317.7986145019531\n      ],\n      \"block_number\": 10,\n      \"text\": \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n\"\n    },\n    {\n      \"bbox\": [\n        456.11981201171875,\n        294.72314453125,\n        529.6943969726562,\n        305.0786437988281\n      ],\n      \"block_number\": 11,\n      \"text\": \"4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        332.64312744140625,\n        529.6943969726562,\n        355.5986328125\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        271.31988525390625,\n        374.8830871582031,\n        529.6962280273438,\n        385.23858642578125\n      ],\n      \"block_number\": 13,\n      \"text\": \"Total of Schedules (A+B)\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        429.96307373046875,\n        187.02545166015625,\n        440.3185729980469\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nSCHEDULE-C \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        404.64306640625,\n        405.0672302246094,\n        465.6385498046875\n      ],\n      \"block_number\": 15,\n      \"text\": \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n\"\n    },\n    {\n      \"bbox\": [\n        463.7998046875,\n        429.96307373046875,\n        481.507080078125,\n        440.3185729980469\n      ],\n      \"block_number\": 16,\n      \"text\": \"---- \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        480.4830322265625,\n        75.06725311279297,\n        572.7985229492188\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\n \\n \\n \\n \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        576.0029296875,\n        526.386962890625,\n        586.3584594726562\n      ],\n      \"block_number\": 18,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        600.48291015625,\n        526.386962890625,\n        610.8384399414062\n      ],\n      \"block_number\": 19,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 20,\n      \"text\": \"307\\n\"\n    }\n  ]\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J23599c81d83cf26f
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 8
        sheet_cells: ''
        json_path: parsed_json/vol4/boq_abstract.json
        json_sha256: 72270396d4fa6937594cd8531e2e59d34d2ab164007793bc1a3ca2b775a056a0
        json_pointer: /records/0
        json_record_id: vol4/boq_abstract/A
        source_review_status: pending_manual_review
        quote: "{\n  \"amount_inr_decimal\": \"46941306.00\",\n  \"amount_raw\": \"4,69,41,306.00\",\n  \"cell_clips\": [\n    [\n      60.900000000000006,\n      280.39,\n      100.77,\n      329.54\n    ],\n    [\n      102.17,\n      280.39,\n      194.06,\n      329.54\n    ],\n    [\n      195.45999999999998,\n      280.39,\n      406.82,\n      329.54\n    ],\n    [\n      408.21999999999997,\n      280.39,\n      534.17,\n      329.54\n    ]\n  ],\n  \"cells\": [\n    \"1\",\n    \"SCHEDULE-A\",\n    \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ\",\n    \"4,69,41,306.00\"\n  ],\n  \"pdf_pages\": [\n    8\n  ],\n  \"record_id\": \"vol4/boq_abstract/A\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      created_at: '2026-10-31T16:02:22+00:00'
      status: draft
      consolidated_claim_ids:
      - C1ab250f373745adc
  - previous_claim_id: Cb73b503cb47bc02c
    previous_evidence_ids:
    - J110eb79934e3efe2
    - J15df25270985d9b6
    - J23599c81d83cf26f
    - S469ca02217533c37
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  updated_at: '2026-11-01T11:49:40+00:00'
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: The total estimated cost for Schedule-B (Items under Schedule of Rate published by KPWD) is ₹ 5,00,000.00, bringing the total estimated cost of Schedules A and B to ₹ 4,74,41,306.00.
  evidence_ids:
  - Jad825d224737bbc4
  - Jabb0383ef371ea9a
  - Jadc4a1acf83198bb
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C43d474e29a31aa7f
  citations:
  - id: Jad825d224737bbc4
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: BOQ_338417.xls
    source_sha256: be376d7be062f1b7d481a0c1e07a132896504f5218450cdb02d039c495425896
    pdf_pages: []
    sheet_cells: BoQ1 row 14
    json_path: parsed_json/boq/boq_workbook.json
    json_sha256: 569d85cec3466a8ae5a5140c1186aba149aa87755785d0b4ed2b48921f9dfff0
    json_pointer: /schedules/1
    json_record_id: boq/schedule_b
    source_review_status: pending_manual_review
    quote: "{\n  \"description\": \"SCHEDULE-B: Items under Schedule of Rate published by KPWD\",\n  \"description_cell\": \"B14\",\n  \"estimated_cost_or_credit_label\": {\n    \"address\": \"F14\",\n    \"cell_type\": \"number\",\n    \"column\": 6,\n    \"formula_hidden_style\": false,\n    \"locked\": true,\n    \"number_format\": \"#,##0.00\",\n    \"row\": 14,\n    \"value\": 500000.0,\n    \"xf_index\": 167\n  },\n  \"excel_row\": 14,\n  \"percentage_selection\": {\n    \"address\": \"N14\",\n    \"cell_type\": \"text\",\n    \"column\": 14,\n    \"formula_hidden_style\": false,\n    \"locked\": false,\n    \"number_format\": \"0.00%\",\n    \"row\": 14,\n    \"value\": \"Select\",\n    \"xf_index\": 130\n  },\n  \"quote_input\": {\n    \"address\": \"M14\",\n    \"cell_type\": \"formatted_blank\",\n    \"column\": 13,\n    \"formula_hidden_style\": false,\n    \"locked\": false,\n    \"number_format\": \"0.00\",\n    \"row\": 14,\n    \"value\": \"\",\n    \"xf_index\": 143\n  },\n  \"record_id\": \"boq/schedule_b\",\n  \"review_status\": \"pending_manual_review\",\n  \"saved_amount\": {\n    \"address\": \"BA14\",\n    \"cell_type\": \"number\",\n    \"column\": 53,\n    \"formula_hidden_style\": false,\n    \"locked\": true,\n    \"number_format\": \"0.00\",\n    \"row\": 14,\n    \"value\": 0.0,\n    \"xf_index\": 173\n  },\n  \"schedule\": \"B\",\n  \"sheet\": \"BoQ1\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jabb0383ef371ea9a
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/7
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 8,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\nContract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\nSl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n(Rs) \\n1 \\nSCHEDULE-A \\nPartial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n4,69,41,306.00\\n2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\nTotal of Schedules (A+B)\\n4,74,41,306.00\\n3 \\nSCHEDULE-C \\nCredit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n---- \\n \\n \\n \\n \\n \\n \\n \\n \\n \\n307\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        123.11994934082031,\n        74.64318084716797,\n        475.146728515625,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99957275390625,\n        88.32317352294922,\n        520.5064697265625,\n        140.43870544433594\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        72.0000228881836,\n        144.60321044921875,\n        526.3865966796875,\n        240.7587127685547\n      ],\n      \"block_number\": 6,\n      \"text\": \"Contract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.96002960205078,\n        244.203125,\n        528.9071655273438,\n        260.9186706542969\n      ],\n      \"block_number\": 7,\n      \"text\": \"Sl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n\"\n    },\n    {\n      \"bbox\": [\n        460.4398193359375,\n        256.92315673828125,\n        484.86712646484375,\n        267.2786560058594\n      ],\n      \"block_number\": 8,\n      \"text\": \"(Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        294.8431396484375,\n        186.78732299804688,\n        305.1986389160156\n      ],\n      \"block_number\": 9,\n      \"text\": \"1 \\nSCHEDULE-A \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        282.1231689453125,\n        405.0671081542969,\n        317.7986145019531\n      ],\n      \"block_number\": 10,\n      \"text\": \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n\"\n    },\n    {\n      \"bbox\": [\n        456.11981201171875,\n        294.72314453125,\n        529.6943969726562,\n        305.0786437988281\n      ],\n      \"block_number\": 11,\n      \"text\": \"4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        332.64312744140625,\n        529.6943969726562,\n        355.5986328125\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        271.31988525390625,\n        374.8830871582031,\n        529.6962280273438,\n        385.23858642578125\n      ],\n      \"block_number\": 13,\n      \"text\": \"Total of Schedules (A+B)\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        429.96307373046875,\n        187.02545166015625,\n        440.3185729980469\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nSCHEDULE-C \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        404.64306640625,\n        405.0672302246094,\n        465.6385498046875\n      ],\n      \"block_number\": 15,\n      \"text\": \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n\"\n    },\n    {\n      \"bbox\": [\n        463.7998046875,\n        429.96307373046875,\n        481.507080078125,\n        440.3185729980469\n      ],\n      \"block_number\": 16,\n      \"text\": \"---- \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        480.4830322265625,\n        75.06725311279297,\n        572.7985229492188\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\n \\n \\n \\n \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        576.0029296875,\n        526.386962890625,\n        586.3584594726562\n      ],\n      \"block_number\": 18,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        600.48291015625,\n        526.386962890625,\n        610.8384399414062\n      ],\n      \"block_number\": 19,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 20,\n      \"text\": \"307\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jadc4a1acf83198bb
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 10
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/9
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 10,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 7 of 7 \\n \\n                                                         Pricing document- Bill of Quantities (BOQ)\\n \\nSchedule - A \\nItem \\nNo. \\nDescription of Item of work \\nUnit \\nQuantity  \\nRate     \\n(in Rs) \\nTotal Amount   \\n(In Rs) \\nbrick work, fencing, stone slab wall, \\nchain link fencing etc. disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts \\nand complete. \\n4 \\nDemolition/dismantling \\nof \\nsteel \\nstructures \\nsuch \\nas \\nsign \\nboards, \\nhoardings etc., of all heights, length and \\nwidth \\nby \\nmechanical \\nand \\nmanual \\nmethods. (Dismantled/released material \\nto be handed over to the concerned \\nauthority at the locations specified by \\nowning \\nauthority \\nand \\nremoval \\nof \\nresulting debris with all lead and lifts).  \\nMT \\n \\n25 \\n7518.00 \\n1,87,950.00 \\n \\n                   Total of Schedule-A\\n4,69,41,306.00\\nSchedule-B \\n \\nITEMS UNDER SCHEDULE OF RATE \\nPUBLISHED BY KPWD \\n1 \\nItems \\nnot \\ncovered \\nin \\nthe \\nabove \\nSchedule A to be executed under \\nCommon SR for the year 2023-24 \\npublished by Karnataka public Works \\nDepartment \\nwith \\nissue \\nrates \\nand \\namendments issued upto date of tender \\nsubmission.  \\nLump\\nsum\\n---------\\n---------\\n5,00,000.00\\nTotal Schedule A+B\\n4,74,41,306.00\\n \\n \\n \\n \\n309\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 7 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.35997009277344,\n        75.12316131591797,\n        463.0339660644531,\n        85.47867584228516\n      ],\n      \"block_number\": 4,\n      \"text\": \"                                                         Pricing document- Bill of Quantities (BOQ)\\n\"\n    },\n    {\n      \"bbox\": [\n        78.47997283935547,\n        97.32317352294922,\n        363.4272766113281,\n        107.6786880493164\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\nSchedule - A \\n\"\n    },\n    {\n      \"bbox\": [\n        67.19996643066406,\n        129.48321533203125,\n        92.94723510742188,\n        139.83872985839844\n      ],\n      \"block_number\": 6,\n      \"text\": \"Item \\n\"\n    },\n    {\n      \"bbox\": [\n        69.59996795654297,\n        129.48321533203125,\n        466.9871520996094,\n        152.55870056152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"No. \\nDescription of Item of work \\nUnit \\nQuantity  \\nRate     \\n(in Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        475.1998291015625,\n        129.48321533203125,\n        555.30712890625,\n        139.83872985839844\n      ],\n      \"block_number\": 8,\n      \"text\": \"Total Amount   \\n\"\n    },\n    {\n      \"bbox\": [\n        493.4397888183594,\n        142.20318603515625,\n        530.7070922851562,\n        152.55870056152344\n      ],\n      \"block_number\": 9,\n      \"text\": \"(In Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        104.63995361328125,\n        171.48321533203125,\n        304.50909423828125,\n        295.7184143066406\n      ],\n      \"block_number\": 10,\n      \"text\": \"brick work, fencing, stone slab wall, \\nchain link fencing etc. disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts \\nand complete. \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        304.443115234375,\n        304.5073547363281,\n        416.07855224609375\n      ],\n      \"block_number\": 11,\n      \"text\": \"4 \\nDemolition/dismantling \\nof \\nsteel \\nstructures \\nsuch \\nas \\nsign \\nboards, \\nhoardings etc., of all heights, length and \\nwidth \\nby \\nmechanical \\nand \\nmanual \\nmethods. (Dismantled/released material \\nto be handed over to the concerned \\nauthority at the locations specified by \\nowning \\nauthority \\nand \\nremoval \\nof \\nresulting debris with all lead and lifts).  \\n\"\n    },\n    {\n      \"bbox\": [\n        320.15985107421875,\n        304.443115234375,\n        339.067138671875,\n        314.7986145019531\n      ],\n      \"block_number\": 12,\n      \"text\": \"MT \\n\"\n    },\n    {\n      \"bbox\": [\n        328.0798645019531,\n        323.1630859375,\n        331.14715576171875,\n        333.5185852050781\n      ],\n      \"block_number\": 13,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        375.1197814941406,\n        304.443115234375,\n        542.7108154296875,\n        314.7986145019531\n      ],\n      \"block_number\": 14,\n      \"text\": \"25 \\n7518.00 \\n1,87,950.00 \\n\"\n    },\n    {\n      \"bbox\": [\n        63.23997497558594,\n        424.6830749511719,\n        549.6143188476562,\n        435.5185852050781\n      ],\n      \"block_number\": 15,\n      \"text\": \" \\n                   Total of Schedule-A\\n4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        276.119873046875,\n        444.9630432128906,\n        339.6651916503906,\n        455.31854248046875\n      ],\n      \"block_number\": 16,\n      \"text\": \"Schedule-B \\n\"\n    },\n    {\n      \"bbox\": [\n        78.47997283935547,\n        464.4030456542969,\n        304.5071716308594,\n        487.3585510253906\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\nITEMS UNDER SCHEDULE OF RATE \\nPUBLISHED BY KPWD \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        534.123046875,\n        84.66725158691406,\n        544.4785766601562\n      ],\n      \"block_number\": 18,\n      \"text\": \"1 \\n\"\n    },\n    {\n      \"bbox\": [\n        104.63996887207031,\n        496.32305908203125,\n        304.50732421875,\n        582.5186157226562\n      ],\n      \"block_number\": 19,\n      \"text\": \"Items \\nnot \\ncovered \\nin \\nthe \\nabove \\nSchedule A to be executed under \\nCommon SR for the year 2023-24 \\npublished by Karnataka public Works \\nDepartment \\nwith \\nissue \\nrates \\nand \\namendments issued upto date of tender \\nsubmission.  \\n\"\n    },\n    {\n      \"bbox\": [\n        313.9198913574219,\n        496.2030334472656,\n        343.9411926269531,\n        506.55853271484375\n      ],\n      \"block_number\": 20,\n      \"text\": \"Lump\\n\"\n    },\n    {\n      \"bbox\": [\n        321.35986328125,\n        508.802978515625,\n        344.0085144042969,\n        519.1585083007812\n      ],\n      \"block_number\": 21,\n      \"text\": \"sum\\n\"\n    },\n    {\n      \"bbox\": [\n        374.7598571777344,\n        496.2030334472656,\n        549.6143188476562,\n        506.55853271484375\n      ],\n      \"block_number\": 22,\n      \"text\": \"---------\\n---------\\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        357.4798583984375,\n        591.2429809570312,\n        549.6143188476562,\n        601.9585571289062\n      ],\n      \"block_number\": 23,\n      \"text\": \"Total Schedule A+B\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        611.282958984375,\n        75.06725311279297,\n        621.6384887695312\n      ],\n      \"block_number\": 24,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        635.762939453125,\n        526.386962890625,\n        646.1184692382812\n      ],\n      \"block_number\": 25,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        660.4829711914062,\n        75.06725311279297,\n        670.8385009765625\n      ],\n      \"block_number\": 26,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        684.9629516601562,\n        75.06725311279297,\n        695.3184814453125\n      ],\n      \"block_number\": 27,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 28,\n      \"text\": \"309\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:02:22+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Cc75381c0d3dbfdc8
    previous_evidence_ids:
    - J0ef80cf1b1d4a05f
    - J15df25270985d9b6
    - J4c4726ee3a58c841
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Schedule-C specifies a credit to BMRCL for salvageable items out of dismantled or demolished private properties on which the owner has no interest, listed as a lump-sum amount without a predefined numerical estimate in the abstract summary.
  evidence_ids:
  - Jabb0383ef371ea9a
  - Jd3c8d7b4ff66f4b1
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C08459f8e8703216f
  citations:
  - id: Jabb0383ef371ea9a
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/7
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 8,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\nContract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\nSl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n(Rs) \\n1 \\nSCHEDULE-A \\nPartial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n4,69,41,306.00\\n2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\nTotal of Schedules (A+B)\\n4,74,41,306.00\\n3 \\nSCHEDULE-C \\nCredit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n---- \\n \\n \\n \\n \\n \\n \\n \\n \\n \\n307\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        123.11994934082031,\n        74.64318084716797,\n        475.146728515625,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99957275390625,\n        88.32317352294922,\n        520.5064697265625,\n        140.43870544433594\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        72.0000228881836,\n        144.60321044921875,\n        526.3865966796875,\n        240.7587127685547\n      ],\n      \"block_number\": 6,\n      \"text\": \"Contract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.96002960205078,\n        244.203125,\n        528.9071655273438,\n        260.9186706542969\n      ],\n      \"block_number\": 7,\n      \"text\": \"Sl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n\"\n    },\n    {\n      \"bbox\": [\n        460.4398193359375,\n        256.92315673828125,\n        484.86712646484375,\n        267.2786560058594\n      ],\n      \"block_number\": 8,\n      \"text\": \"(Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        294.8431396484375,\n        186.78732299804688,\n        305.1986389160156\n      ],\n      \"block_number\": 9,\n      \"text\": \"1 \\nSCHEDULE-A \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        282.1231689453125,\n        405.0671081542969,\n        317.7986145019531\n      ],\n      \"block_number\": 10,\n      \"text\": \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n\"\n    },\n    {\n      \"bbox\": [\n        456.11981201171875,\n        294.72314453125,\n        529.6943969726562,\n        305.0786437988281\n      ],\n      \"block_number\": 11,\n      \"text\": \"4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        332.64312744140625,\n        529.6943969726562,\n        355.5986328125\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        271.31988525390625,\n        374.8830871582031,\n        529.6962280273438,\n        385.23858642578125\n      ],\n      \"block_number\": 13,\n      \"text\": \"Total of Schedules (A+B)\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        429.96307373046875,\n        187.02545166015625,\n        440.3185729980469\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nSCHEDULE-C \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        404.64306640625,\n        405.0672302246094,\n        465.6385498046875\n      ],\n      \"block_number\": 15,\n      \"text\": \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n\"\n    },\n    {\n      \"bbox\": [\n        463.7998046875,\n        429.96307373046875,\n        481.507080078125,\n        440.3185729980469\n      ],\n      \"block_number\": 16,\n      \"text\": \"---- \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        480.4830322265625,\n        75.06725311279297,\n        572.7985229492188\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\n \\n \\n \\n \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        576.0029296875,\n        526.386962890625,\n        586.3584594726562\n      ],\n      \"block_number\": 18,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        600.48291015625,\n        526.386962890625,\n        610.8384399414062\n      ],\n      \"block_number\": 19,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 20,\n      \"text\": \"307\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jd3c8d7b4ff66f4b1
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: BOQ_338417.xls
    source_sha256: be376d7be062f1b7d481a0c1e07a132896504f5218450cdb02d039c495425896
    pdf_pages: []
    sheet_cells: BoQ1 row 15
    json_path: parsed_json/boq/boq_workbook.json
    json_sha256: 569d85cec3466a8ae5a5140c1186aba149aa87755785d0b4ed2b48921f9dfff0
    json_pointer: /schedules/2
    json_record_id: boq/schedule_c
    source_review_status: pending_manual_review
    quote: "{\n  \"description\": \"SCHEDULE-C: Credit to BMRCL for salvageable items out of dismantled/demolished private properties on which the owner has no interest (as elaborated in Para 15 of Part-3 of ‘Employer’s Requirement’).\",\n  \"description_cell\": \"B15\",\n  \"estimated_cost_or_credit_label\": {\n    \"address\": \"F15\",\n    \"cell_type\": \"text\",\n    \"column\": 6,\n    \"formula_hidden_style\": false,\n    \"locked\": true,\n    \"number_format\": \"#,##0.00\",\n    \"row\": 15,\n    \"value\": \"Credit to BMRCL in Lumpsum Amount\",\n    \"xf_index\": 166\n  },\n  \"excel_row\": 15,\n  \"percentage_selection\": {\n    \"address\": \"N15\",\n    \"cell_type\": \"formatted_blank\",\n    \"column\": 14,\n    \"formula_hidden_style\": false,\n    \"locked\": true,\n    \"number_format\": \"#,##0.00\",\n    \"row\": 15,\n    \"value\": \"\",\n    \"xf_index\": 129\n  },\n  \"quote_input\": {\n    \"address\": \"M15\",\n    \"cell_type\": \"formatted_blank\",\n    \"column\": 13,\n    \"formula_hidden_style\": false,\n    \"locked\": false,\n    \"number_format\": \"0.00\",\n    \"row\": 15,\n    \"value\": \"\",\n    \"xf_index\": 131\n  },\n  \"record_id\": \"boq/schedule_c\",\n  \"review_status\": \"pending_manual_review\",\n  \"saved_amount\": {\n    \"address\": \"BA15\",\n    \"cell_type\": \"number\",\n    \"column\": 53,\n    \"formula_hidden_style\": false,\n    \"locked\": true,\n    \"number_format\": \"0.00\",\n    \"row\": 15,\n    \"value\": 0.0,\n    \"xf_index\": 162\n  },\n  \"schedule\": \"C\",\n  \"sheet\": \"BoQ1\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:02:22+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Ce0b66778d130a2d8
    previous_evidence_ids:
    - J15df25270985d9b6
    - Jd9a712a10137d028
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Schedule-A item 1 specifies partial demolition and dismantling of structures of different heights at a quantity of 31,245.00 Sqm with a rate of ₹ 1,087.00 per Sqm, resulting in an amount of ₹ 3,39,63,315.00.
  evidence_ids:
  - J3f50dc005015beb7
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C5123a54e163baa33
  citations:
  - id: J3f50dc005015beb7
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 9
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /boq_items/0
    json_record_id: schedule_a/item_1
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"33963315.00\",\n  \"amount_inr_raw\": \"3,39,63,315.00\",\n  \"description\": \"Partial \\ndemolition/dismantling \\nby \\nmechanical and manual methods of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan \\none \\nfloors, \\n(RCC \\nframed \\nstructures, wall bearing structures with \\nRCC roof. All other structures such as \\nAC roof etc), comprising of cement \\nconcrete, stone masonry, brick work, \\nsteel \\nwork, \\nwood \\nwork \\netc.  \\nDisposal of unserviceable materials with \\nall leads and lifts and stacking of \\nserviceable \\nmaterials, \\nthe \\nstacked \\nserviceable material shall be disposed \\nof with all leads and lifts in which the \\nproperty owner has no interest, removal \\nof resulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects.\",\n  \"fragments\": [\n    {\n      \"description\": \"Partial \\ndemolition/dismantling \\nby \\nmechanical and manual methods of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan \\none \\nfloors, \\n(RCC \\nframed \\nstructures, wall bearing structures with \\nRCC roof. All other structures such as \\nAC roof etc), comprising of cement \\nconcrete, stone masonry, brick work, \\nsteel \\nwork, \\nwood \\nwork \\netc.  \\nDisposal of unserviceable materials with \\nall leads and lifts and stacking of \\nserviceable \\nmaterials, \\nthe \\nstacked \\nserviceable material shall be disposed \\nof with all leads and lifts in which the \\nproperty owner has no interest, removal \\nof resulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects.\",\n      \"pdf_page\": 9,\n      \"table_row\": 2\n    }\n  ],\n  \"item_number\": \"1\",\n  \"pdf_pages\": [\n    9\n  ],\n  \"quantity_decimal\": \"31245.00\",\n  \"quantity_raw\": \"31245.00\",\n  \"rate_inr_decimal\": \"1087.00\",\n  \"rate_inr_raw\": \"1087.00\",\n  \"record_id\": \"schedule_a/item_1\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\",\n  \"unit\": \"Sqm\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:02:22+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Ce45273834ae1f048
    previous_evidence_ids:
    - J50ed4496a3873130
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Schedule-A item 2 specifies full demolition and dismantling of structures at a quantity of 21,760.00 Sqm with a rate of ₹ 548.00 per Sqm, resulting in an amount of ₹ 1,19,24,480.00.
  evidence_ids:
  - J56d5c0e99ab43b9b
  - Jb1c8db24c756e2db
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C480df6a468c882b8
  citations:
  - id: J56d5c0e99ab43b9b
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 9
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/8
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 9,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 6 of 7 \\n \\n                                                         Pricing document- Bill of Quantities (BOQ)\\n \\nSchedule - A \\nItem \\nNo. \\nDescription of Item of work \\nUnit \\nQuantity  \\nRate     \\n(in Rs) \\nTotal Amount   \\n(In Rs) \\n1 \\nPartial \\ndemolition/dismantling \\nby \\nmechanical and manual methods of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan \\none \\nfloors, \\n(RCC \\nframed \\nstructures, wall bearing structures with \\nRCC roof. All other structures such as \\nAC roof etc), comprising of cement \\nconcrete, stone masonry, brick work, \\nsteel \\nwork, \\nwood \\nwork \\netc.  \\nDisposal of unserviceable materials with \\nall leads and lifts and stacking of \\nserviceable \\nmaterials, \\nthe \\nstacked \\nserviceable material shall be disposed \\nof with all leads and lifts in which the \\nproperty owner has no interest, removal \\nof resulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects. \\nSqm \\n31245.00 \\n1087.00 \\n3,39,63,315.00 \\n2 \\nFull \\ndemolition/dismantling \\nby \\nmechanical and manual methods, of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan one floors (RCC framed structures, \\nwall bearing structures with RCC roof. \\nAll other structures such as AC roof \\netc), comprising of cement concrete, \\nstone masonry, brick work, steel work, \\nwood work etc.          Disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects. \\nSqm \\n21760.00 \\n548.00 \\n1,19,24,480.00 \\n3 \\nDemolition /dismantling compound walls \\nof all shapes and heights by mechanical \\nand manual methods, comprising of \\ncement concrete, stone masonry work, \\nRmt \\n5183.00 \\n167.00 \\n8,65,561.00 \\n308\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 6 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.35997009277344,\n        75.12316131591797,\n        463.0339660644531,\n        85.47867584228516\n      ],\n      \"block_number\": 4,\n      \"text\": \"                                                         Pricing document- Bill of Quantities (BOQ)\\n\"\n    },\n    {\n      \"bbox\": [\n        78.47997283935547,\n        97.32317352294922,\n        363.4272766113281,\n        107.6786880493164\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\nSchedule - A \\n\"\n    },\n    {\n      \"bbox\": [\n        67.19996643066406,\n        129.48321533203125,\n        92.94723510742188,\n        139.83872985839844\n      ],\n      \"block_number\": 6,\n      \"text\": \"Item \\n\"\n    },\n    {\n      \"bbox\": [\n        69.59996795654297,\n        129.48321533203125,\n        466.9871520996094,\n        152.55870056152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"No. \\nDescription of Item of work \\nUnit \\nQuantity  \\nRate     \\n(in Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        475.1998291015625,\n        129.48321533203125,\n        555.30712890625,\n        139.83872985839844\n      ],\n      \"block_number\": 8,\n      \"text\": \"Total Amount   \\n\"\n    },\n    {\n      \"bbox\": [\n        493.4397888183594,\n        142.20318603515625,\n        530.7070922851562,\n        152.55870056152344\n      ],\n      \"block_number\": 9,\n      \"text\": \"(In Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        171.36322021484375,\n        307.6270446777344,\n        434.798583984375\n      ],\n      \"block_number\": 10,\n      \"text\": \"1 \\nPartial \\ndemolition/dismantling \\nby \\nmechanical and manual methods of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan \\none \\nfloors, \\n(RCC \\nframed \\nstructures, wall bearing structures with \\nRCC roof. All other structures such as \\nAC roof etc), comprising of cement \\nconcrete, stone masonry, brick work, \\nsteel \\nwork, \\nwood \\nwork \\netc.  \\nDisposal of unserviceable materials with \\nall leads and lifts and stacking of \\nserviceable \\nmaterials, \\nthe \\nstacked \\nserviceable material shall be disposed \\nof with all leads and lifts in which the \\nproperty owner has no interest, removal \\nof resulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects. \\n\"\n    },\n    {\n      \"bbox\": [\n        312.2396545410156,\n        171.48321533203125,\n        550.392822265625,\n        181.83872985839844\n      ],\n      \"block_number\": 11,\n      \"text\": \"Sqm \\n31245.00 \\n1087.00 \\n3,39,63,315.00 \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        443.5230407714844,\n        304.50909423828125,\n        706.9585571289062\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nFull \\ndemolition/dismantling \\nby \\nmechanical and manual methods, of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan one floors (RCC framed structures, \\nwall bearing structures with RCC roof. \\nAll other structures such as AC roof \\netc), comprising of cement concrete, \\nstone masonry, brick work, steel work, \\nwood work etc.          Disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects. \\n\"\n    },\n    {\n      \"bbox\": [\n        316.7999267578125,\n        443.6430969238281,\n        550.39306640625,\n        453.99859619140625\n      ],\n      \"block_number\": 13,\n      \"text\": \"Sqm \\n21760.00 \\n548.00 \\n1,19,24,480.00 \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        715.8029174804688,\n        304.50738525390625,\n        764.0784301757812\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nDemolition /dismantling compound walls \\nof all shapes and heights by mechanical \\nand manual methods, comprising of \\ncement concrete, stone masonry work, \\n\"\n    },\n    {\n      \"bbox\": [\n        318.00018310546875,\n        715.8029174804688,\n        542.7114868164062,\n        726.158447265625\n      ],\n      \"block_number\": 15,\n      \"text\": \"Rmt \\n5183.00 \\n167.00 \\n8,65,561.00 \\n\"\n    },\n    {\n      \"bbox\": [\n        39.599998474121094,\n        24.479991912841797,\n        63.57600021362305,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"308\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jb1c8db24c756e2db
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 9
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /boq_items/1
    json_record_id: schedule_a/item_2
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"11924480.00\",\n  \"amount_inr_raw\": \"1,19,24,480.00\",\n  \"description\": \"Full \\ndemolition/dismantling \\nby \\nmechanical and manual methods, of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan one floors (RCC framed structures, \\nwall bearing structures with RCC roof. \\nAll other structures such as AC roof \\netc), comprising of cement concrete, \\nstone masonry, brick work, steel work, \\nwood work etc.          Disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects.\",\n  \"fragments\": [\n    {\n      \"description\": \"Full \\ndemolition/dismantling \\nby \\nmechanical and manual methods, of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan one floors (RCC framed structures, \\nwall bearing structures with RCC roof. \\nAll other structures such as AC roof \\netc), comprising of cement concrete, \\nstone masonry, brick work, steel work, \\nwood work etc.          Disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects.\",\n      \"pdf_page\": 9,\n      \"table_row\": 3\n    }\n  ],\n  \"item_number\": \"2\",\n  \"pdf_pages\": [\n    9\n  ],\n  \"quantity_decimal\": \"21760.00\",\n  \"quantity_raw\": \"21760.00\",\n  \"rate_inr_decimal\": \"548.00\",\n  \"rate_inr_raw\": \"548.00\",\n  \"record_id\": \"schedule_a/item_2\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\",\n  \"unit\": \"Sqm\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:02:22+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C4158f93a98200163
    previous_evidence_ids:
    - J8e3ee1efdd152a76
    - Jc5eaa48fed8a39dd
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Schedule-A item 3 specifies demolition and dismantling of compound walls at a quantity of 5,183.00 Rmt with a rate of ₹ 167.00 per Rmt, resulting in an amount of ₹ 8,65,561.00.
  evidence_ids:
  - J56d5c0e99ab43b9b
  - J9c0d0eea0a2aaeec
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C6fcd4b66d74bbd5d
  citations:
  - id: J56d5c0e99ab43b9b
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 9
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/8
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 9,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 6 of 7 \\n \\n                                                         Pricing document- Bill of Quantities (BOQ)\\n \\nSchedule - A \\nItem \\nNo. \\nDescription of Item of work \\nUnit \\nQuantity  \\nRate     \\n(in Rs) \\nTotal Amount   \\n(In Rs) \\n1 \\nPartial \\ndemolition/dismantling \\nby \\nmechanical and manual methods of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan \\none \\nfloors, \\n(RCC \\nframed \\nstructures, wall bearing structures with \\nRCC roof. All other structures such as \\nAC roof etc), comprising of cement \\nconcrete, stone masonry, brick work, \\nsteel \\nwork, \\nwood \\nwork \\netc.  \\nDisposal of unserviceable materials with \\nall leads and lifts and stacking of \\nserviceable \\nmaterials, \\nthe \\nstacked \\nserviceable material shall be disposed \\nof with all leads and lifts in which the \\nproperty owner has no interest, removal \\nof resulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects. \\nSqm \\n31245.00 \\n1087.00 \\n3,39,63,315.00 \\n2 \\nFull \\ndemolition/dismantling \\nby \\nmechanical and manual methods, of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan one floors (RCC framed structures, \\nwall bearing structures with RCC roof. \\nAll other structures such as AC roof \\netc), comprising of cement concrete, \\nstone masonry, brick work, steel work, \\nwood work etc.          Disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects. \\nSqm \\n21760.00 \\n548.00 \\n1,19,24,480.00 \\n3 \\nDemolition /dismantling compound walls \\nof all shapes and heights by mechanical \\nand manual methods, comprising of \\ncement concrete, stone masonry work, \\nRmt \\n5183.00 \\n167.00 \\n8,65,561.00 \\n308\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 6 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.35997009277344,\n        75.12316131591797,\n        463.0339660644531,\n        85.47867584228516\n      ],\n      \"block_number\": 4,\n      \"text\": \"                                                         Pricing document- Bill of Quantities (BOQ)\\n\"\n    },\n    {\n      \"bbox\": [\n        78.47997283935547,\n        97.32317352294922,\n        363.4272766113281,\n        107.6786880493164\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\nSchedule - A \\n\"\n    },\n    {\n      \"bbox\": [\n        67.19996643066406,\n        129.48321533203125,\n        92.94723510742188,\n        139.83872985839844\n      ],\n      \"block_number\": 6,\n      \"text\": \"Item \\n\"\n    },\n    {\n      \"bbox\": [\n        69.59996795654297,\n        129.48321533203125,\n        466.9871520996094,\n        152.55870056152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"No. \\nDescription of Item of work \\nUnit \\nQuantity  \\nRate     \\n(in Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        475.1998291015625,\n        129.48321533203125,\n        555.30712890625,\n        139.83872985839844\n      ],\n      \"block_number\": 8,\n      \"text\": \"Total Amount   \\n\"\n    },\n    {\n      \"bbox\": [\n        493.4397888183594,\n        142.20318603515625,\n        530.7070922851562,\n        152.55870056152344\n      ],\n      \"block_number\": 9,\n      \"text\": \"(In Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        171.36322021484375,\n        307.6270446777344,\n        434.798583984375\n      ],\n      \"block_number\": 10,\n      \"text\": \"1 \\nPartial \\ndemolition/dismantling \\nby \\nmechanical and manual methods of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan \\none \\nfloors, \\n(RCC \\nframed \\nstructures, wall bearing structures with \\nRCC roof. All other structures such as \\nAC roof etc), comprising of cement \\nconcrete, stone masonry, brick work, \\nsteel \\nwork, \\nwood \\nwork \\netc.  \\nDisposal of unserviceable materials with \\nall leads and lifts and stacking of \\nserviceable \\nmaterials, \\nthe \\nstacked \\nserviceable material shall be disposed \\nof with all leads and lifts in which the \\nproperty owner has no interest, removal \\nof resulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects. \\n\"\n    },\n    {\n      \"bbox\": [\n        312.2396545410156,\n        171.48321533203125,\n        550.392822265625,\n        181.83872985839844\n      ],\n      \"block_number\": 11,\n      \"text\": \"Sqm \\n31245.00 \\n1087.00 \\n3,39,63,315.00 \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        443.5230407714844,\n        304.50909423828125,\n        706.9585571289062\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nFull \\ndemolition/dismantling \\nby \\nmechanical and manual methods, of all \\ntypes of structures of different heights \\nconsisting of ground floor and/or more \\nthan one floors (RCC framed structures, \\nwall bearing structures with RCC roof. \\nAll other structures such as AC roof \\netc), comprising of cement concrete, \\nstone masonry, brick work, steel work, \\nwood work etc.          Disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts, \\nincluding \\nnecessary \\nstrengthening \\nmethods for the buildings proposed for \\ndemolition and also for neighbouring \\nbuildings, complete in all respects. \\n\"\n    },\n    {\n      \"bbox\": [\n        316.7999267578125,\n        443.6430969238281,\n        550.39306640625,\n        453.99859619140625\n      ],\n      \"block_number\": 13,\n      \"text\": \"Sqm \\n21760.00 \\n548.00 \\n1,19,24,480.00 \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        715.8029174804688,\n        304.50738525390625,\n        764.0784301757812\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nDemolition /dismantling compound walls \\nof all shapes and heights by mechanical \\nand manual methods, comprising of \\ncement concrete, stone masonry work, \\n\"\n    },\n    {\n      \"bbox\": [\n        318.00018310546875,\n        715.8029174804688,\n        542.7114868164062,\n        726.158447265625\n      ],\n      \"block_number\": 15,\n      \"text\": \"Rmt \\n5183.00 \\n167.00 \\n8,65,561.00 \\n\"\n    },\n    {\n      \"bbox\": [\n        39.599998474121094,\n        24.479991912841797,\n        63.57600021362305,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"308\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: J9c0d0eea0a2aaeec
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 9
    - 10
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /boq_items/2
    json_record_id: schedule_a/item_3
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"865561.00\",\n  \"amount_inr_raw\": \"8,65,561.00\",\n  \"description\": \"Demolition /dismantling compound walls \\nof all shapes and heights by mechanical \\nand manual methods, comprising of \\ncement concrete, stone masonry work,\\nbrick work, fencing, stone slab wall, \\nchain link fencing etc. disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts \\nand complete.\",\n  \"fragments\": [\n    {\n      \"description\": \"Demolition /dismantling compound walls \\nof all shapes and heights by mechanical \\nand manual methods, comprising of \\ncement concrete, stone masonry work,\",\n      \"pdf_page\": 9,\n      \"table_row\": 4\n    },\n    {\n      \"description\": \"brick work, fencing, stone slab wall, \\nchain link fencing etc. disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts \\nand complete.\",\n      \"pdf_page\": 10,\n      \"table_row\": 2\n    }\n  ],\n  \"item_number\": \"3\",\n  \"pdf_pages\": [\n    9,\n    10\n  ],\n  \"quantity_decimal\": \"5183.00\",\n  \"quantity_raw\": \"5183.00\",\n  \"rate_inr_decimal\": \"167.00\",\n  \"rate_inr_raw\": \"167.00\",\n  \"record_id\": \"schedule_a/item_3\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\",\n  \"unit\": \"Rmt\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:02:22+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C7f85f27136b4298b
    previous_evidence_ids:
    - J8e3ee1efdd152a76
    - Je1901893441800a6
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Schedule-A item 4 specifies demolition and dismantling of steel structures such as sign boards and hoardings at a quantity of 25.00 MT with a rate of ₹ 7,518.00 per MT, resulting in an amount of ₹ 1,87,950.00.
  evidence_ids:
  - Jadc4a1acf83198bb
  - J9d5475ed2f3c7c6d
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C39d282efdfc73231
  citations:
  - id: Jadc4a1acf83198bb
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 10
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/9
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 10,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 7 of 7 \\n \\n                                                         Pricing document- Bill of Quantities (BOQ)\\n \\nSchedule - A \\nItem \\nNo. \\nDescription of Item of work \\nUnit \\nQuantity  \\nRate     \\n(in Rs) \\nTotal Amount   \\n(In Rs) \\nbrick work, fencing, stone slab wall, \\nchain link fencing etc. disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts \\nand complete. \\n4 \\nDemolition/dismantling \\nof \\nsteel \\nstructures \\nsuch \\nas \\nsign \\nboards, \\nhoardings etc., of all heights, length and \\nwidth \\nby \\nmechanical \\nand \\nmanual \\nmethods. (Dismantled/released material \\nto be handed over to the concerned \\nauthority at the locations specified by \\nowning \\nauthority \\nand \\nremoval \\nof \\nresulting debris with all lead and lifts).  \\nMT \\n \\n25 \\n7518.00 \\n1,87,950.00 \\n \\n                   Total of Schedule-A\\n4,69,41,306.00\\nSchedule-B \\n \\nITEMS UNDER SCHEDULE OF RATE \\nPUBLISHED BY KPWD \\n1 \\nItems \\nnot \\ncovered \\nin \\nthe \\nabove \\nSchedule A to be executed under \\nCommon SR for the year 2023-24 \\npublished by Karnataka public Works \\nDepartment \\nwith \\nissue \\nrates \\nand \\namendments issued upto date of tender \\nsubmission.  \\nLump\\nsum\\n---------\\n---------\\n5,00,000.00\\nTotal Schedule A+B\\n4,74,41,306.00\\n \\n \\n \\n \\n309\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 7 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.35997009277344,\n        75.12316131591797,\n        463.0339660644531,\n        85.47867584228516\n      ],\n      \"block_number\": 4,\n      \"text\": \"                                                         Pricing document- Bill of Quantities (BOQ)\\n\"\n    },\n    {\n      \"bbox\": [\n        78.47997283935547,\n        97.32317352294922,\n        363.4272766113281,\n        107.6786880493164\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\nSchedule - A \\n\"\n    },\n    {\n      \"bbox\": [\n        67.19996643066406,\n        129.48321533203125,\n        92.94723510742188,\n        139.83872985839844\n      ],\n      \"block_number\": 6,\n      \"text\": \"Item \\n\"\n    },\n    {\n      \"bbox\": [\n        69.59996795654297,\n        129.48321533203125,\n        466.9871520996094,\n        152.55870056152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"No. \\nDescription of Item of work \\nUnit \\nQuantity  \\nRate     \\n(in Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        475.1998291015625,\n        129.48321533203125,\n        555.30712890625,\n        139.83872985839844\n      ],\n      \"block_number\": 8,\n      \"text\": \"Total Amount   \\n\"\n    },\n    {\n      \"bbox\": [\n        493.4397888183594,\n        142.20318603515625,\n        530.7070922851562,\n        152.55870056152344\n      ],\n      \"block_number\": 9,\n      \"text\": \"(In Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        104.63995361328125,\n        171.48321533203125,\n        304.50909423828125,\n        295.7184143066406\n      ],\n      \"block_number\": 10,\n      \"text\": \"brick work, fencing, stone slab wall, \\nchain link fencing etc. disposal of \\nunserviceable materials with all leads \\nand lifts and stacking of serviceable \\nmaterials, \\nthe \\nstacked \\nserviceable \\nmaterial shall be disposed of with all \\nleads and lifts in which the property \\nowner has no interest, removal of \\nresulting debris with all lead and lifts \\nand complete. \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        304.443115234375,\n        304.5073547363281,\n        416.07855224609375\n      ],\n      \"block_number\": 11,\n      \"text\": \"4 \\nDemolition/dismantling \\nof \\nsteel \\nstructures \\nsuch \\nas \\nsign \\nboards, \\nhoardings etc., of all heights, length and \\nwidth \\nby \\nmechanical \\nand \\nmanual \\nmethods. (Dismantled/released material \\nto be handed over to the concerned \\nauthority at the locations specified by \\nowning \\nauthority \\nand \\nremoval \\nof \\nresulting debris with all lead and lifts).  \\n\"\n    },\n    {\n      \"bbox\": [\n        320.15985107421875,\n        304.443115234375,\n        339.067138671875,\n        314.7986145019531\n      ],\n      \"block_number\": 12,\n      \"text\": \"MT \\n\"\n    },\n    {\n      \"bbox\": [\n        328.0798645019531,\n        323.1630859375,\n        331.14715576171875,\n        333.5185852050781\n      ],\n      \"block_number\": 13,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        375.1197814941406,\n        304.443115234375,\n        542.7108154296875,\n        314.7986145019531\n      ],\n      \"block_number\": 14,\n      \"text\": \"25 \\n7518.00 \\n1,87,950.00 \\n\"\n    },\n    {\n      \"bbox\": [\n        63.23997497558594,\n        424.6830749511719,\n        549.6143188476562,\n        435.5185852050781\n      ],\n      \"block_number\": 15,\n      \"text\": \" \\n                   Total of Schedule-A\\n4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        276.119873046875,\n        444.9630432128906,\n        339.6651916503906,\n        455.31854248046875\n      ],\n      \"block_number\": 16,\n      \"text\": \"Schedule-B \\n\"\n    },\n    {\n      \"bbox\": [\n        78.47997283935547,\n        464.4030456542969,\n        304.5071716308594,\n        487.3585510253906\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\nITEMS UNDER SCHEDULE OF RATE \\nPUBLISHED BY KPWD \\n\"\n    },\n    {\n      \"bbox\": [\n        75.47997283935547,\n        534.123046875,\n        84.66725158691406,\n        544.4785766601562\n      ],\n      \"block_number\": 18,\n      \"text\": \"1 \\n\"\n    },\n    {\n      \"bbox\": [\n        104.63996887207031,\n        496.32305908203125,\n        304.50732421875,\n        582.5186157226562\n      ],\n      \"block_number\": 19,\n      \"text\": \"Items \\nnot \\ncovered \\nin \\nthe \\nabove \\nSchedule A to be executed under \\nCommon SR for the year 2023-24 \\npublished by Karnataka public Works \\nDepartment \\nwith \\nissue \\nrates \\nand \\namendments issued upto date of tender \\nsubmission.  \\n\"\n    },\n    {\n      \"bbox\": [\n        313.9198913574219,\n        496.2030334472656,\n        343.9411926269531,\n        506.55853271484375\n      ],\n      \"block_number\": 20,\n      \"text\": \"Lump\\n\"\n    },\n    {\n      \"bbox\": [\n        321.35986328125,\n        508.802978515625,\n        344.0085144042969,\n        519.1585083007812\n      ],\n      \"block_number\": 21,\n      \"text\": \"sum\\n\"\n    },\n    {\n      \"bbox\": [\n        374.7598571777344,\n        496.2030334472656,\n        549.6143188476562,\n        506.55853271484375\n      ],\n      \"block_number\": 22,\n      \"text\": \"---------\\n---------\\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        357.4798583984375,\n        591.2429809570312,\n        549.6143188476562,\n        601.9585571289062\n      ],\n      \"block_number\": 23,\n      \"text\": \"Total Schedule A+B\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        611.282958984375,\n        75.06725311279297,\n        621.6384887695312\n      ],\n      \"block_number\": 24,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        635.762939453125,\n        526.386962890625,\n        646.1184692382812\n      ],\n      \"block_number\": 25,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        660.4829711914062,\n        75.06725311279297,\n        670.8385009765625\n      ],\n      \"block_number\": 26,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        684.9629516601562,\n        75.06725311279297,\n        695.3184814453125\n      ],\n      \"block_number\": 27,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 28,\n      \"text\": \"309\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: J9d5475ed2f3c7c6d
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 10
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /boq_items/3
    json_record_id: schedule_a/item_4
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"187950.00\",\n  \"amount_inr_raw\": \"1,87,950.00\",\n  \"description\": \"Demolition/dismantling \\nof \\nsteel \\nstructures \\nsuch \\nas \\nsign \\nboards, \\nhoardings etc., of all heights, length and \\nwidth \\nby \\nmechanical \\nand \\nmanual \\nmethods. (Dismantled/released material \\nto be handed over to the concerned \\nauthority at the locations specified by \\nowning \\nauthority \\nand \\nremoval \\nof \\nresulting debris with all lead and lifts).\",\n  \"fragments\": [\n    {\n      \"description\": \"Demolition/dismantling \\nof \\nsteel \\nstructures \\nsuch \\nas \\nsign \\nboards, \\nhoardings etc., of all heights, length and \\nwidth \\nby \\nmechanical \\nand \\nmanual \\nmethods. (Dismantled/released material \\nto be handed over to the concerned \\nauthority at the locations specified by \\nowning \\nauthority \\nand \\nremoval \\nof \\nresulting debris with all lead and lifts).\",\n      \"pdf_page\": 10,\n      \"table_row\": 3\n    }\n  ],\n  \"item_number\": \"4\",\n  \"pdf_pages\": [\n    10\n  ],\n  \"quantity_decimal\": \"25\",\n  \"quantity_raw\": \"25\",\n  \"rate_inr_decimal\": \"7518.00\",\n  \"rate_inr_raw\": \"7518.00\",\n  \"record_id\": \"schedule_a/item_4\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"A\",\n  \"unit\": \"MT\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:02:22+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Ca4669849d9171fd8
    previous_evidence_ids:
    - J4c4726ee3a58c841
    - Jbdf4e472845e8372
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Pricing rule 6 dictates that the Tender Price or Quoted Price includes all applicable taxes, duties, cess, royalties, and statutory levies in force as of the last day of the month previous to the month of tender invitation, except Goods and Services Tax (GST).
  evidence_ids:
  - Je35bc79dc160b3f0
  - Jf17d55c6acfde864
  - S10ec60af02b3e977
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C904d49cbfbc57854
  citations:
  - id: Je35bc79dc160b3f0
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 6
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/5
    json_record_id: vol4/pricing_preamble/6
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"6\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/6\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3866577148438,\n        440.0784606933594\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        443.2829284667969,\n        526.3870239257812,\n        453.638427734375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"and statutory levies as per the laws in force as on last day of the month previous to the\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        456.9629211425781,\n        446.9472351074219,\n        467.31842041015625\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"month of invitation of this tender, except Goods and Services Tax (GST).\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\\nand statutory levies as per the laws in force as on last day of the month previous to the\\nmonth of invitation of this tender, except Goods and Services Tax (GST).\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jf17d55c6acfde864
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 6
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/5
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 6,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\nPricing Document-Preamble \\n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n305\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        227.51991271972656,\n        74.64318084716797,\n        377.9470520019531,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"Pricing Document-Preamble \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        99.36321258544922,\n        526.3881225585938,\n        177.9987030029297\n      ],\n      \"block_number\": 5,\n      \"text\": \"1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.3868408203125,\n        238.59861755371094\n      ],\n      \"block_number\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99929809570312,\n        247.923095703125,\n        526.387451171875,\n        326.4385681152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99847412109375,\n        335.7630310058594,\n        526.3863525390625,\n        387.0384826660156\n      ],\n      \"block_number\": 8,\n      \"text\": \"4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99948120117188,\n        396.36297607421875,\n        526.3870239257812,\n        420.3984680175781\n      ],\n      \"block_number\": 9,\n      \"text\": \"5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3870239257812,\n        467.31842041015625\n      ],\n      \"block_number\": 10,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3883666992188,\n        514.2384033203125\n      ],\n      \"block_number\": 11,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        523.5628662109375,\n        526.3883666992188,\n        602.1983642578125\n      ],\n      \"block_number\": 12,\n      \"text\": \"8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        611.5228271484375,\n        526.3880615234375,\n        649.1182861328125\n      ],\n      \"block_number\": 13,\n      \"text\": \"9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        658.4427490234375,\n        526.3875732421875,\n        709.71826171875\n      ],\n      \"block_number\": 14,\n      \"text\": \"10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99981689453125,\n        719.042724609375,\n        526.3865966796875,\n        756.6382446289062\n      ],\n      \"block_number\": 15,\n      \"text\": \"11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"305\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: S10ec60af02b3e977
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: 1.0 — Pricing Document Preamble and Instructions
    source_document: Vol4DLNP1.pdf
    pdf_pages:
    - 6
    quote: "- **Read BOQ with the Complete Tender and Contract Documents** (Instruction 1)\n- **Provisional Quantities and Payment for Measured Work** (Instruction 2)\n- **Price Bid Preparation in the Prescribed XLS Sheet** (Instruction 3; ITT 10)\n  - Schedule-A: percentage rate to two decimals; At Par / Excess / Less\n  - Schedule-B: At Par only\n  - Schedule-C: lump-sum salvage credit to BMRCL\n- **Proportionate Recovery and Adjustment of Salvage Credit** (Instruction 4)\n- **Salvage Credit Based on Quoted Price** (Instruction 5)\n- **Taxes and Statutory Levies Included, Except GST** (Instruction 6)\n- **Measurement of Completed Work** (Instruction 7)\n- **Completed-Work Pricing and Included Execution Costs** (Instruction 8)\n- **Included Safety and Protection Costs** (Instruction 9)\n- **Overheads, Profit, Risks and Defect-Remedy Obligations** (Instruction 10)\n- **Accommodation, Insurance, Wages and Approval Costs** (Instruction 11)\n\n\n\n- **Execution Standards and Engineer’s Directions** (Instruction 12)\n- **Incidental Removal Works Without Separate Payment** (Instruction 13)\n- **Temporary Relocation and Protection of Utilities** (Instruction 14)\n- **Temporary Works, Power and Supports at Contractor’s Cost** (Instruction 15)\n- **Permanent Supports and Restoration Payment Provisions** (Instruction 16)\n- **Balcony and Canopy Area at 50%; Chejjas Excluded from Payment** (Instruction 17)\n- **Demolition Depth and Refilling of Low-Level Areas** (Instruction 18)\n- **Removal Within the Line of Cut, Excluding Trees** (Instruction 19)\n- **Total Floor Area as the Sum of Built Areas of All Floors** (Instruction 20)\n- **Building Additions or Deletions and Accepted Percentage Rates** (Instruction 21)"
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  created_at: '2026-10-31T16:02:22+00:00'
  status: draft
  editorial_history:
  - corrected_at: '2026-11-01T11:49:40+00:00'
    method: reviewed repetition consolidation
    previous_claims:
    - kind: parameter
      text: Pricing rules mandate that quoted prices include all applicable taxes, duties, cess, royalties, and statutory levies in force on the last day of the month previous to tender invitation, except Goods and Services Tax (GST).
      evidence_ids:
      - J026debd7f34d6fd9
      - S19382a03427e15ba
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: Ce169bc47f7309c0d
      citations:
      - id: J026debd7f34d6fd9
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/5
        json_record_id: vol4/pricing_preamble/6
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"6\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/6\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3866577148438,\n        440.0784606933594\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        443.2829284667969,\n        526.3870239257812,\n        453.638427734375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"and statutory levies as per the laws in force as on last day of the month previous to the\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        456.9629211425781,\n        446.9472351074219,\n        467.31842041015625\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"month of invitation of this tender, except Goods and Services Tax (GST).\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\\nand statutory levies as per the laws in force as on last day of the month previous to the\\nmonth of invitation of this tender, except Goods and Services Tax (GST).\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: S19382a03427e15ba
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: 1.0 — Pricing Document Preamble and Instructions
        source_document: Vol4DLNP1.pdf
        pdf_pages:
        - 6
        quote: "- **Read BOQ with the Complete Tender and Contract Documents** (Instruction 1)\n- **Provisional Quantities and Payment for Measured Work** (Instruction 2)\n- **Price Bid Preparation in the Prescribed XLS Sheet** (Instruction 3; ITT 10)\n  - Schedule-A: percentage rate to two decimals; At Par / Excess / Less\n  - Schedule-B: At Par only\n  - Schedule-C: lump-sum salvage credit to BMRCL\n- **Proportionate Recovery and Adjustment of Salvage Credit** (Instruction 4)\n- **Salvage Credit Based on Quoted Price** (Instruction 5)\n- **Taxes and Statutory Levies Included, Except GST** (Instruction 6)\n- **Measurement of Completed Work** (Instruction 7)\n- **Completed-Work Pricing and Included Execution Costs** (Instruction 8)\n- **Included Safety and Protection Costs** (Instruction 9)\n- **Overheads, Profit, Risks and Defect-Remedy Obligations** (Instruction 10)\n- **Accommodation, Insurance, Wages and Approval Costs** (Instruction 11)\n\n\n\n- **Execution Standards and Engineer’s Directions** (Instruction 12)\n- **Incidental Removal Works Without Separate Payment** (Instruction 13)\n- **Temporary Relocation and Protection of Utilities** (Instruction 14)\n- **Temporary Works, Power and Supports at Contractor’s Cost** (Instruction 15)\n- **Permanent Supports and Restoration Payment Provisions** (Instruction 16)\n- **Balcony and Canopy Area at 50%; Chejjas Excluded from Payment** (Instruction 17)\n- **Demolition Depth and Refilling of Low-Level Areas** (Instruction 18)\n- **Removal Within the Line of Cut, Excluding Trees** (Instruction 19)\n- **Total Floor Area as the Sum of Built Areas of All Floors** (Instruction 20)\n- **Building Additions or Deletions and Accepted Percentage Rates** (Instruction 21)"
        page_basis: OKF reference, not independently PDF-verified
        page_precision: section_reference
      created_at: '2026-10-31T15:57:39+00:00'
      status: draft
    - kind: parameter
      text: Pricing preamble rules dictate that quoted prices include all taxes, duties, cess, royalties, and statutory levies as in force on the last day of the month previous to the month of tender invitation, excluding Goods and Services Tax (GST).
      evidence_ids:
      - J026debd7f34d6fd9
      - J6f83ecf77cc57b25
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: C9b3f4ce9e49c0e11
      citations:
      - id: J026debd7f34d6fd9
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/5
        json_record_id: vol4/pricing_preamble/6
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"6\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/6\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3866577148438,\n        440.0784606933594\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        443.2829284667969,\n        526.3870239257812,\n        453.638427734375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"and statutory levies as per the laws in force as on last day of the month previous to the\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        456.9629211425781,\n        446.9472351074219,\n        467.31842041015625\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"month of invitation of this tender, except Goods and Services Tax (GST).\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\\nand statutory levies as per the laws in force as on last day of the month previous to the\\nmonth of invitation of this tender, except Goods and Services Tax (GST).\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J6f83ecf77cc57b25
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_document.json
        json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
        json_pointer: /pages/5
        json_record_id: null
        source_review_status: pending_manual_review
        quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 6,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\nPricing Document-Preamble \\n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n305\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        227.51991271972656,\n        74.64318084716797,\n        377.9470520019531,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"Pricing Document-Preamble \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        99.36321258544922,\n        526.3881225585938,\n        177.9987030029297\n      ],\n      \"block_number\": 5,\n      \"text\": \"1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.3868408203125,\n        238.59861755371094\n      ],\n      \"block_number\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99929809570312,\n        247.923095703125,\n        526.387451171875,\n        326.4385681152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99847412109375,\n        335.7630310058594,\n        526.3863525390625,\n        387.0384826660156\n      ],\n      \"block_number\": 8,\n      \"text\": \"4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99948120117188,\n        396.36297607421875,\n        526.3870239257812,\n        420.3984680175781\n      ],\n      \"block_number\": 9,\n      \"text\": \"5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3870239257812,\n        467.31842041015625\n      ],\n      \"block_number\": 10,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3883666992188,\n        514.2384033203125\n      ],\n      \"block_number\": 11,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        523.5628662109375,\n        526.3883666992188,\n        602.1983642578125\n      ],\n      \"block_number\": 12,\n      \"text\": \"8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        611.5228271484375,\n        526.3880615234375,\n        649.1182861328125\n      ],\n      \"block_number\": 13,\n      \"text\": \"9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        658.4427490234375,\n        526.3875732421875,\n        709.71826171875\n      ],\n      \"block_number\": 14,\n      \"text\": \"10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99981689453125,\n        719.042724609375,\n        526.3865966796875,\n        756.6382446289062\n      ],\n      \"block_number\": 15,\n      \"text\": \"11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"305\\n\"\n    }\n  ]\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      created_at: '2026-10-31T16:00:35+00:00'
      status: draft
    - kind: parameter
      text: Pricing rule 6 dictates that the Tender Price or Quoted Price includes all applicable taxes, duties, cess, royalties, and statutory levies in force as of the last day of the month previous to the month of tender invitation, except Goods and Services Tax (GST).
      evidence_ids:
      - J026debd7f34d6fd9
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: C2d15946aaa4d0b64
      citations:
      - id: J026debd7f34d6fd9
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/5
        json_record_id: vol4/pricing_preamble/6
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"6\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/6\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3866577148438,\n        440.0784606933594\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        443.2829284667969,\n        526.3870239257812,\n        453.638427734375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"and statutory levies as per the laws in force as on last day of the month previous to the\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        456.9629211425781,\n        446.9472351074219,\n        467.31842041015625\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"month of invitation of this tender, except Goods and Services Tax (GST).\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\\nand statutory levies as per the laws in force as on last day of the month previous to the\\nmonth of invitation of this tender, except Goods and Services Tax (GST).\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      created_at: '2026-10-31T16:02:22+00:00'
      status: draft
    - kind: parameter
      text: Quoted prices include all applicable taxes, duties, cess, royalties, and statutory levies in force as on the last day of the month previous to the month of invitation, except Goods and Services Tax (GST).
      evidence_ids:
      - J026debd7f34d6fd9
      - J6f83ecf77cc57b25
      relation_type: none
      explicitness: not_a_relation
      from_id: ''
      to_id: ''
      id: C6682ee2f65312098
      citations:
      - id: J026debd7f34d6fd9
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_clauses.json
        json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
        json_pointer: /records/5
        json_record_id: vol4/pricing_preamble/6
        source_review_status: pending_manual_review
        quote: "{\n  \"label\": \"6\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/6\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3866577148438,\n        440.0784606933594\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        443.2829284667969,\n        526.3870239257812,\n        453.638427734375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"and statutory levies as per the laws in force as on last day of the month previous to the\"\n    },\n    {\n      \"bbox\": [\n        89.87982940673828,\n        456.9629211425781,\n        446.9472351074219,\n        467.31842041015625\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"month of invitation of this tender, except Goods and Services Tax (GST).\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\\nand statutory levies as per the laws in force as on last day of the month previous to the\\nmonth of invitation of this tender, except Goods and Services Tax (GST).\",\n  \"type\": \"pricing_rule\"\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      - id: J6f83ecf77cc57b25
        okf_path: OKF_bundle/Financial/vol4_secJ.md
        okf_sha256: 9439a74058830fd65e3d20892e276927f56b1c5717d424ea357f19aca5698795
        heading: Financial Document and Bill of Quantities
        source_document: Vol4DLNP1.pdf
        source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
        pdf_pages:
        - 6
        sheet_cells: ''
        json_path: parsed_json/vol4/pricing_document.json
        json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
        json_pointer: /pages/5
        json_record_id: null
        source_review_status: pending_manual_review
        quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 6,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\nPricing Document-Preamble \\n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n305\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        227.51991271972656,\n        74.64318084716797,\n        377.9470520019531,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"Pricing Document-Preamble \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        99.36321258544922,\n        526.3881225585938,\n        177.9987030029297\n      ],\n      \"block_number\": 5,\n      \"text\": \"1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.3868408203125,\n        238.59861755371094\n      ],\n      \"block_number\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99929809570312,\n        247.923095703125,\n        526.387451171875,\n        326.4385681152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99847412109375,\n        335.7630310058594,\n        526.3863525390625,\n        387.0384826660156\n      ],\n      \"block_number\": 8,\n      \"text\": \"4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99948120117188,\n        396.36297607421875,\n        526.3870239257812,\n        420.3984680175781\n      ],\n      \"block_number\": 9,\n      \"text\": \"5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3870239257812,\n        467.31842041015625\n      ],\n      \"block_number\": 10,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3883666992188,\n        514.2384033203125\n      ],\n      \"block_number\": 11,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        523.5628662109375,\n        526.3883666992188,\n        602.1983642578125\n      ],\n      \"block_number\": 12,\n      \"text\": \"8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        611.5228271484375,\n        526.3880615234375,\n        649.1182861328125\n      ],\n      \"block_number\": 13,\n      \"text\": \"9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        658.4427490234375,\n        526.3875732421875,\n        709.71826171875\n      ],\n      \"block_number\": 14,\n      \"text\": \"10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99981689453125,\n        719.042724609375,\n        526.3865966796875,\n        756.6382446289062\n      ],\n      \"block_number\": 15,\n      \"text\": \"11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"305\\n\"\n    }\n  ]\n}"
        page_basis: Parsed record provenance; not independently PDF-verified
        heading_alignment: document_heading_fallback_not_a_subclause_match
      created_at: '2026-10-31T16:03:48+00:00'
      status: draft
  - previous_claim_id: C34b0e9c0b2651965
    previous_evidence_ids:
    - J026debd7f34d6fd9
    - J6f83ecf77cc57b25
    - S19382a03427e15ba
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  updated_at: '2026-11-01T11:49:40+00:00'
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: The total estimated cost for Schedule-B (Items under KPWD Schedule of Rate) is ₹ 5,00,000.00, making the combined total of Schedules A and B ₹ 4,74,41,306.00.
  evidence_ids:
  - Jabb0383ef371ea9a
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C287d51717cf1e68a
  citations:
  - id: Jabb0383ef371ea9a
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/7
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 8,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\nContract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\nSl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n(Rs) \\n1 \\nSCHEDULE-A \\nPartial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n4,69,41,306.00\\n2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\nTotal of Schedules (A+B)\\n4,74,41,306.00\\n3 \\nSCHEDULE-C \\nCredit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n---- \\n \\n \\n \\n \\n \\n \\n \\n \\n \\n307\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        123.11994934082031,\n        74.64318084716797,\n        475.146728515625,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99957275390625,\n        88.32317352294922,\n        520.5064697265625,\n        140.43870544433594\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        72.0000228881836,\n        144.60321044921875,\n        526.3865966796875,\n        240.7587127685547\n      ],\n      \"block_number\": 6,\n      \"text\": \"Contract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.96002960205078,\n        244.203125,\n        528.9071655273438,\n        260.9186706542969\n      ],\n      \"block_number\": 7,\n      \"text\": \"Sl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n\"\n    },\n    {\n      \"bbox\": [\n        460.4398193359375,\n        256.92315673828125,\n        484.86712646484375,\n        267.2786560058594\n      ],\n      \"block_number\": 8,\n      \"text\": \"(Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        294.8431396484375,\n        186.78732299804688,\n        305.1986389160156\n      ],\n      \"block_number\": 9,\n      \"text\": \"1 \\nSCHEDULE-A \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        282.1231689453125,\n        405.0671081542969,\n        317.7986145019531\n      ],\n      \"block_number\": 10,\n      \"text\": \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n\"\n    },\n    {\n      \"bbox\": [\n        456.11981201171875,\n        294.72314453125,\n        529.6943969726562,\n        305.0786437988281\n      ],\n      \"block_number\": 11,\n      \"text\": \"4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        332.64312744140625,\n        529.6943969726562,\n        355.5986328125\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        271.31988525390625,\n        374.8830871582031,\n        529.6962280273438,\n        385.23858642578125\n      ],\n      \"block_number\": 13,\n      \"text\": \"Total of Schedules (A+B)\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        429.96307373046875,\n        187.02545166015625,\n        440.3185729980469\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nSCHEDULE-C \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        404.64306640625,\n        405.0672302246094,\n        465.6385498046875\n      ],\n      \"block_number\": 15,\n      \"text\": \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n\"\n    },\n    {\n      \"bbox\": [\n        463.7998046875,\n        429.96307373046875,\n        481.507080078125,\n        440.3185729980469\n      ],\n      \"block_number\": 16,\n      \"text\": \"---- \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        480.4830322265625,\n        75.06725311279297,\n        572.7985229492188\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\n \\n \\n \\n \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        576.0029296875,\n        526.386962890625,\n        586.3584594726562\n      ],\n      \"block_number\": 18,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        600.48291015625,\n        526.386962890625,\n        610.8384399414062\n      ],\n      \"block_number\": 19,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 20,\n      \"text\": \"307\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:03:48+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C3d443e5e93bf2018
    previous_evidence_ids:
    - J15df25270985d9b6
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Schedule-C represents credit to BMRCL for salvageable items out of dismantled/demolished private properties where owners have no interest, indicated as lump sum amount to be offered by tenderers.
  evidence_ids:
  - Jabb0383ef371ea9a
  - Jf17d55c6acfde864
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: Cd8a5a29655e5c7f6
  citations:
  - id: Jabb0383ef371ea9a
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 8
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/7
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 8,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\nContract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\nSl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n(Rs) \\n1 \\nSCHEDULE-A \\nPartial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n4,69,41,306.00\\n2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\nTotal of Schedules (A+B)\\n4,74,41,306.00\\n3 \\nSCHEDULE-C \\nCredit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n---- \\n \\n \\n \\n \\n \\n \\n \\n \\n \\n307\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 5 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        123.11994934082031,\n        74.64318084716797,\n        475.146728515625,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99957275390625,\n        88.32317352294922,\n        520.5064697265625,\n        140.43870544433594\n      ],\n      \"block_number\": 5,\n      \"text\": \" \\n \\nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \\nidentified in Bangalore Metro Rail Project Phase-3.” \\n\"\n    },\n    {\n      \"bbox\": [\n        72.0000228881836,\n        144.60321044921875,\n        526.3865966796875,\n        240.7587127685547\n      ],\n      \"block_number\": 6,\n      \"text\": \"Contract \\nPackage-P1: \\n“Partial \\nand \\nFull \\nDemolition/Dismantling \\nof \\nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \\nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \\nRail Project Phase-3.” \\nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \\n09.09.2026 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        66.96002960205078,\n        244.203125,\n        528.9071655273438,\n        260.9186706542969\n      ],\n      \"block_number\": 7,\n      \"text\": \"Sl.No \\nSchedule \\nSchedule Description \\nTotal Estimated Cost \\n\"\n    },\n    {\n      \"bbox\": [\n        460.4398193359375,\n        256.92315673828125,\n        484.86712646484375,\n        267.2786560058594\n      ],\n      \"block_number\": 8,\n      \"text\": \"(Rs) \\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        294.8431396484375,\n        186.78732299804688,\n        305.1986389160156\n      ],\n      \"block_number\": 9,\n      \"text\": \"1 \\nSCHEDULE-A \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        282.1231689453125,\n        405.0671081542969,\n        317.7986145019531\n      ],\n      \"block_number\": 10,\n      \"text\": \"Partial & Full demolition and dismantling \\nwork as per details given in Schedule-A \\nof the BOQ \\n\"\n    },\n    {\n      \"bbox\": [\n        456.11981201171875,\n        294.72314453125,\n        529.6943969726562,\n        305.0786437988281\n      ],\n      \"block_number\": 11,\n      \"text\": \"4,69,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        332.64312744140625,\n        529.6943969726562,\n        355.5986328125\n      ],\n      \"block_number\": 12,\n      \"text\": \"2 \\nSCHEDULE-B \\nItems under Schedule of Rate published \\nby KPWD \\n5,00,000.00\\n\"\n    },\n    {\n      \"bbox\": [\n        271.31988525390625,\n        374.8830871582031,\n        529.6962280273438,\n        385.23858642578125\n      ],\n      \"block_number\": 13,\n      \"text\": \"Total of Schedules (A+B)\\n4,74,41,306.00\\n\"\n    },\n    {\n      \"bbox\": [\n        77.87996673583984,\n        429.96307373046875,\n        187.02545166015625,\n        440.3185729980469\n      ],\n      \"block_number\": 14,\n      \"text\": \"3 \\nSCHEDULE-C \\n\"\n    },\n    {\n      \"bbox\": [\n        200.1597442626953,\n        404.64306640625,\n        405.0672302246094,\n        465.6385498046875\n      ],\n      \"block_number\": 15,\n      \"text\": \"Credit to BMRCL for salvageable items \\nout of dismantled/demolished private \\nproperties on which the owner has no \\ninterest (as elaborated in Para 15 of Part-\\n3 of ‘Employer’s Requirement’). \\n\"\n    },\n    {\n      \"bbox\": [\n        463.7998046875,\n        429.96307373046875,\n        481.507080078125,\n        440.3185729980469\n      ],\n      \"block_number\": 16,\n      \"text\": \"---- \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        480.4830322265625,\n        75.06725311279297,\n        572.7985229492188\n      ],\n      \"block_number\": 17,\n      \"text\": \" \\n \\n \\n \\n \\n \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        576.0029296875,\n        526.386962890625,\n        586.3584594726562\n      ],\n      \"block_number\": 18,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        523.3197021484375,\n        600.48291015625,\n        526.386962890625,\n        610.8384399414062\n      ],\n      \"block_number\": 19,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 20,\n      \"text\": \"307\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jf17d55c6acfde864
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 6
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/5
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 6,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\nPricing Document-Preamble \\n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n305\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        227.51991271972656,\n        74.64318084716797,\n        377.9470520019531,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"Pricing Document-Preamble \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        99.36321258544922,\n        526.3881225585938,\n        177.9987030029297\n      ],\n      \"block_number\": 5,\n      \"text\": \"1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.3868408203125,\n        238.59861755371094\n      ],\n      \"block_number\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99929809570312,\n        247.923095703125,\n        526.387451171875,\n        326.4385681152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99847412109375,\n        335.7630310058594,\n        526.3863525390625,\n        387.0384826660156\n      ],\n      \"block_number\": 8,\n      \"text\": \"4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99948120117188,\n        396.36297607421875,\n        526.3870239257812,\n        420.3984680175781\n      ],\n      \"block_number\": 9,\n      \"text\": \"5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3870239257812,\n        467.31842041015625\n      ],\n      \"block_number\": 10,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3883666992188,\n        514.2384033203125\n      ],\n      \"block_number\": 11,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        523.5628662109375,\n        526.3883666992188,\n        602.1983642578125\n      ],\n      \"block_number\": 12,\n      \"text\": \"8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        611.5228271484375,\n        526.3880615234375,\n        649.1182861328125\n      ],\n      \"block_number\": 13,\n      \"text\": \"9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        658.4427490234375,\n        526.3875732421875,\n        709.71826171875\n      ],\n      \"block_number\": 14,\n      \"text\": \"10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99981689453125,\n        719.042724609375,\n        526.3865966796875,\n        756.6382446289062\n      ],\n      \"block_number\": 15,\n      \"text\": \"11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"305\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:03:48+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Ca4769b1d63199e13
    previous_evidence_ids:
    - J15df25270985d9b6
    - J6f83ecf77cc57b25
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Tenderers must quote percentage rates in two decimals for Schedule-A (selecting At Par / Excess / Less), quote At Par for Schedule-B, and offer a lump sum credit for Schedule-C.
  evidence_ids:
  - Jf17d55c6acfde864
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C13a655796690e902
  citations:
  - id: Jf17d55c6acfde864
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 6
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /pages/5
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"page_type\": \"text\",\n  \"pdf_page\": 6,\n  \"review_status\": \"pending_manual_review\",\n  \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n \\n \\nBangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\nPricing Document-Preamble \\n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n305\\n\",\n  \"text_blocks\": [\n    {\n      \"bbox\": [\n        14.760004043579102,\n        37.509437561035156,\n        519.9669799804688,\n        56.52032470703125\n      ],\n      \"block_number\": 0,\n      \"text\": \" BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        62.5140495300293,\n        74.49351501464844,\n        69.48028564453125\n      ],\n      \"block_number\": 1,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        777.8273315429688,\n        74.38514709472656,\n        786.9194946289062\n      ],\n      \"block_number\": 2,\n      \"text\": \" \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        802.54736328125,\n        525.8132934570312,\n        823.079833984375\n      ],\n      \"block_number\": 3,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.                            September 2026 \\nSection Page 3 of 7 \\n \\n\"\n    },\n    {\n      \"bbox\": [\n        227.51991271972656,\n        74.64318084716797,\n        377.9470520019531,\n        84.99869537353516\n      ],\n      \"block_number\": 4,\n      \"text\": \"Pricing Document-Preamble \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99996948242188,\n        99.36321258544922,\n        526.3881225585938,\n        177.9987030029297\n      ],\n      \"block_number\": 5,\n      \"text\": \"1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \\nshall be read in conjunction with the entire Tender and Contract Document including \\nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \\nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \\nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \\nCorrigendum and Addendums. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.999267578125,\n        187.3231201171875,\n        526.3868408203125,\n        238.59861755371094\n      ],\n      \"block_number\": 6,\n      \"text\": \"2. The quantities given in the Price document - “Bill of Quantities” are estimated \\n(provisional). The basis of payment will be the actual quantities of work ordered and \\ncarried out, as measured by the Contractor and verified by the Engineer and valued at \\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99929809570312,\n        247.923095703125,\n        526.387451171875,\n        326.4385681152344\n      ],\n      \"block_number\": 7,\n      \"text\": \"3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \\nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \\nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \\nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \\nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \\nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99847412109375,\n        335.7630310058594,\n        526.3863525390625,\n        387.0384826660156\n      ],\n      \"block_number\": 8,\n      \"text\": \"4. The Lump sum amount indicated for Schedule C will be recovered from the running \\naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \\nthe value of credit to BMRCL will be increased/decreased according to the value of work \\ndone from the ‘on account’ bills on pro-rata basis. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99948120117188,\n        396.36297607421875,\n        526.3870239257812,\n        420.3984680175781\n      ],\n      \"block_number\": 9,\n      \"text\": \"5. The Contractor should note that the credit to BMRCL on salvage materials should be in \\nreference to the quoted price and not on the estimate cost put to tender. \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99951171875,\n        429.72296142578125,\n        526.3870239257812,\n        467.31842041015625\n      ],\n      \"block_number\": 10,\n      \"text\": \"6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \\nand statutory levies as per the laws in force as on last day of the month previous to the \\nmonth of invitation of this tender, except Goods and Services Tax (GST). \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3883666992188,\n        514.2384033203125\n      ],\n      \"block_number\": 11,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with \\nthe requirements as stated in the Technical Specifications and as given in the Price \\ndocument- Bill of Quantities or elsewhere in the tender documents. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00054931640625,\n        523.5628662109375,\n        526.3883666992188,\n        602.1983642578125\n      ],\n      \"block_number\": 12,\n      \"text\": \"8. The quoted price is for completed and finished items of work and complete in all respects \\ncomplying with the provisions of the Contract. It will be deemed to have included all \\nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \\ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \\nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \\nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        611.5228271484375,\n        526.3880615234375,\n        649.1182861328125\n      ],\n      \"block_number\": 13,\n      \"text\": \"9. The quoted price will be deemed to have included all the safety measures at work sites/ \\ncasting yard, safety measures for workmen & road users, safety of the public and \\nprotection of adjoining land & building while working. \\n\"\n    },\n    {\n      \"bbox\": [\n        72.00051879882812,\n        658.4427490234375,\n        526.3875732421875,\n        709.71826171875\n      ],\n      \"block_number\": 14,\n      \"text\": \"10. The quoted price will be deemed to have included establishment & overhead charges, \\ncontractor’s profit, supervision, other charges together with all general risks, liabilities \\nand obligations set out or implied in the contract and including remedy of any defects \\nduring the Defect Liability Period.  \\n\"\n    },\n    {\n      \"bbox\": [\n        71.99981689453125,\n        719.042724609375,\n        526.3865966796875,\n        756.6382446289062\n      ],\n      \"block_number\": 15,\n      \"text\": \"11. The quoted price will be deemed to have included accommodations for staff & workmen, \\nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \\ncharges payable to various departments for obtaining necessary approvals if any. \\n\"\n    },\n    {\n      \"bbox\": [\n        546.0439453125,\n        24.479991912841797,\n        570.0199584960938,\n        41.38799285888672\n      ],\n      \"block_number\": 16,\n      \"text\": \"305\\n\"\n    }\n  ]\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:03:48+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C5aa2f3b8c729db32
    previous_evidence_ids:
    - J6f83ecf77cc57b25
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Underlying BOQ workbook structure includes automated cell formulas and number-to-words functions such as SpellNumber and SpellNumberMC for calculation and verification of tender sums.
  evidence_ids:
  - J2b6c7e3129c261f6
  - J4a966f61d68d291f
  - J9a979874374a2792
  - Jccbc53a1c3e23834
  - Jfd74b52b70d7661d
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C0a72f78784598aaa
  citations:
  - id: J2b6c7e3129c261f6
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: BOQ_338417.xls
    source_sha256: be376d7be062f1b7d481a0c1e07a132896504f5218450cdb02d039c495425896
    pdf_pages: []
    sheet_cells: BoQ1!$BA$17
    json_path: parsed_json/boq/boq_formulas.json
    json_sha256: 18510e28dc0b4317ad4bc91fe6fbe98e28f75ea237c16f686fbc59e1107c248b
    json_pointer: /formulas/18
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"address\": \"$BA$17\",\n  \"column\": 53,\n  \"formula\": \"=IF(ISBLANK(F17),0,IF(E17=\\\"Excess (+)\\\",ROUND(BA16+(BA16*F17),2),IF(E17=\\\"Less (-)\\\",ROUND(BA16+(BA16*F17*(-1)),2),0)))\",\n  \"has_array_formula\": false,\n  \"number_format\": \"0.0000\",\n  \"row\": 17,\n  \"sheet\": \"BoQ1\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: J4a966f61d68d291f
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: BOQ_338417.xls
    source_sha256: be376d7be062f1b7d481a0c1e07a132896504f5218450cdb02d039c495425896
    pdf_pages: []
    sheet_cells: BoQ1!$BC$17
    json_path: parsed_json/boq/boq_formulas.json
    json_sha256: 18510e28dc0b4317ad4bc91fe6fbe98e28f75ea237c16f686fbc59e1107c248b
    json_pointer: /formulas/20
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"address\": \"$BC$17\",\n  \"column\": 55,\n  \"formula\": \"=SpellNumber(L17,BB17)\",\n  \"has_array_formula\": false,\n  \"number_format\": \"General\",\n  \"row\": 17,\n  \"sheet\": \"BoQ1\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: J9a979874374a2792
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: BOQ_338417.xls
    source_sha256: be376d7be062f1b7d481a0c1e07a132896504f5218450cdb02d039c495425896
    pdf_pages: []
    sheet_cells: BoQ1!$C$18
    json_path: parsed_json/boq/boq_formulas.json
    json_sha256: 18510e28dc0b4317ad4bc91fe6fbe98e28f75ea237c16f686fbc59e1107c248b
    json_pointer: /formulas/21
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"address\": \"$C$18\",\n  \"column\": 3,\n  \"formula\": \"=SpellNumberMC($E$2,BA16)\",\n  \"has_array_formula\": false,\n  \"number_format\": \"General\",\n  \"row\": 18,\n  \"sheet\": \"BoQ1\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jccbc53a1c3e23834
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: BOQ_338417.xls
    source_sha256: be376d7be062f1b7d481a0c1e07a132896504f5218450cdb02d039c495425896
    pdf_pages: []
    sheet_cells: BoQ1!$BB$17
    json_path: parsed_json/boq/boq_formulas.json
    json_sha256: 18510e28dc0b4317ad4bc91fe6fbe98e28f75ea237c16f686fbc59e1107c248b
    json_pointer: /formulas/19
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"address\": \"$BB$17\",\n  \"column\": 54,\n  \"formula\": \"=ROUND(BA17,0)\",\n  \"has_array_formula\": false,\n  \"number_format\": \"0.0000\",\n  \"row\": 17,\n  \"sheet\": \"BoQ1\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jfd74b52b70d7661d
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: BOQ_338417.xls
    source_sha256: be376d7be062f1b7d481a0c1e07a132896504f5218450cdb02d039c495425896
    pdf_pages: []
    sheet_cells: BoQ1!$BC$16
    json_path: parsed_json/boq/boq_formulas.json
    json_sha256: 18510e28dc0b4317ad4bc91fe6fbe98e28f75ea237c16f686fbc59e1107c248b
    json_pointer: /formulas/17
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"address\": \"$BC$16\",\n  \"column\": 55,\n  \"formula\": \"=SpellNumberMC($E$2,BA16)\",\n  \"has_array_formula\": false,\n  \"number_format\": \"General\",\n  \"row\": 16,\n  \"sheet\": \"BoQ1\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-10-31T16:03:48+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Ce3e2967100b11604
    previous_evidence_ids:
    - Ja5b8d9eefe7304dc
    - Jc2ebb3df673fa4a6
    - Jcf2bda6a1228367d
    - Jdd1a2e344dcc692a
    - Jec7126612a9ce37c
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: summary
  text: Pricing rules specify that work execution must follow the Bill of Quantity descriptions, technical specifications, standards of MORTH, KPWD, CPWD, drawings, engineering practices, and instructions of the Engineer.
  evidence_ids:
  - Jbed462ebb1fb6ea8
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C2105bec694a6cf13
  citations:
  - id: Jbed462ebb1fb6ea8
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/11
    json_record_id: vol4/pricing_preamble/12
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"12\",\n  \"pdf_pages\": [\n    7\n  ],\n  \"record_id\": \"vol4/pricing_preamble/12\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99996948242188,\n        74.76317596435547,\n        526.3866577148438,\n        85.11869049072266\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"12. The work is to be executed as per Bill of Quantity description, Technical Specifications,\"\n    },\n    {\n      \"bbox\": [\n        89.87928009033203,\n        88.44316864013672,\n        526.3867797851562,\n        98.7986831665039\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"specifications of MORTH, KPWD, CPWD, drawings, best engineering practices and/or\"\n    },\n    {\n      \"bbox\": [\n        89.87926483154297,\n        102.12316131591797,\n        232.98648071289062,\n        112.47867584228516\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"as directed by the Engineer.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"12. The work is to be executed as per Bill of Quantity description, Technical Specifications,\\nspecifications of MORTH, KPWD, CPWD, drawings, best engineering practices and/or\\nas directed by the Engineer.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:03:15+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Cbfb7bf902527857c
    previous_evidence_ids:
    - Ja084d2ef6281865d
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: summary
  text: The removal of items such as hoardings, interior lighting, interior furniture, ACP cladding, and structural glazing within the line of cut is treated as incidental work with no separate payment considered.
  evidence_ids:
  - J6286c3376d46f205
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C40d6c2a95a9fc2f8
  citations:
  - id: J6286c3376d46f205
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/12
    json_record_id: vol4/pricing_preamble/13
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"13\",\n  \"pdf_pages\": [\n    7\n  ],\n  \"record_id\": \"vol4/pricing_preamble/13\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.999267578125,\n        121.80315399169922,\n        526.3859252929688,\n        132.15867614746094\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"13. Removal of hoardings, interior lighting and interior furniture etc., ACP cladding and\"\n    },\n    {\n      \"bbox\": [\n        89.87854766845703,\n        135.3631591796875,\n        526.3856201171875,\n        145.7186737060547\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"structural glazing etc., which are existing within the line of cut are incidental to work.  No\"\n    },\n    {\n      \"bbox\": [\n        89.87853240966797,\n        149.04315185546875,\n        335.7059326171875,\n        159.39866638183594\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"separate payment will be considered for payment.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"13. Removal of hoardings, interior lighting and interior furniture etc., ACP cladding and\\nstructural glazing etc., which are existing within the line of cut are incidental to work.  No\\nseparate payment will be considered for payment.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:03:15+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Ccf5eb31e9579e19c
    previous_evidence_ids:
    - Jc3d6f8ec0e5c8075
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: summary
  text: Where power, water, or other utilities must be maintained during demolition, such lines must be temporarily relocated and protected prior to commencing demolition work.
  evidence_ids:
  - J3a4bdedbf4a7b7e6
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C93d6028b623b0b04
  citations:
  - id: J3a4bdedbf4a7b7e6
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/13
    json_record_id: vol4/pricing_preamble/14
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"14\",\n  \"pdf_pages\": [\n    7\n  ],\n  \"record_id\": \"vol4/pricing_preamble/14\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99853515625,\n        168.72314453125,\n        526.3860473632812,\n        179.0786590576172\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"14. If it is necessary to maintain any power, water or other utilities during demolition, such\"\n    },\n    {\n      \"bbox\": [\n        89.87882232666016,\n        182.403076171875,\n        526.3866577148438,\n        192.7585906982422\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"lines shall be temporarily relocated, as necessary and protected before commencement\"\n    },\n    {\n      \"bbox\": [\n        89.87883758544922,\n        195.96307373046875,\n        190.74612426757812,\n        206.31858825683594\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"of demolition work.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"14. If it is necessary to maintain any power, water or other utilities during demolition, such\\nlines shall be temporarily relocated, as necessary and protected before commencement\\nof demolition work.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:03:15+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Cb5422c1f20d0be44
    previous_evidence_ids:
    - J4fa380d8bf61e3ac
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: summary
  text: When advised by the Consultant or BMRCL, the contractor must provide permanent supports and related restoration works before or after demolition to maintain Line of Clearance (LOC), paid according to accepted BOQ rates for items available in the Common Schedule of Rates (Common SR) for the year 2023-24.
  evidence_ids:
  - J181fa7ffc9bc4a10
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: Cab7131b75622be5e
  citations:
  - id: J181fa7ffc9bc4a10
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/15
    json_record_id: vol4/pricing_preamble/16
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"16\",\n  \"pdf_pages\": [\n    7\n  ],\n  \"record_id\": \"vol4/pricing_preamble/16\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99887084960938,\n        289.92303466796875,\n        526.3864135742188,\n        300.2785339355469\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"16. If advised by the Consultant/BMRCL, the contractor has to give permanent supports like\"\n    },\n    {\n      \"bbox\": [\n        89.87915802001953,\n        303.60302734375,\n        526.3859252929688,\n        313.9585266113281\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"wall, columns (Steel, RCC, etc.), including plastering, painting, plumbing, water supply\"\n    },\n    {\n      \"bbox\": [\n        89.87914276123047,\n        317.16302490234375,\n        526.3861694335938,\n        327.5185241699219\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"and sanitary works, electrical restoration works, etc. to the supported portion of the\"\n    },\n    {\n      \"bbox\": [\n        89.87914276123047,\n        330.8429870605469,\n        526.3868408203125,\n        341.198486328125\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"building before or after total/partial demolition, wherever necessary to maintain LOC, for\"\n    },\n    {\n      \"bbox\": [\n        89.87914276123047,\n        344.5229797363281,\n        526.3902587890625,\n        354.87847900390625\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"which payment will be made as per  accepted rate in BoQ schedule for items available in\"\n    },\n    {\n      \"bbox\": [\n        89.87914276123047,\n        358.2029724121094,\n        519.7941284179688,\n        368.5584716796875\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"Common SR for the year 2023-24 (Schedule of Rates),  for the execution of such work.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"16. If advised by the Consultant/BMRCL, the contractor has to give permanent supports like\\nwall, columns (Steel, RCC, etc.), including plastering, painting, plumbing, water supply\\nand sanitary works, electrical restoration works, etc. to the supported portion of the\\nbuilding before or after total/partial demolition, wherever necessary to maintain LOC, for\\nwhich payment will be made as per  accepted rate in BoQ schedule for items available in\\nCommon SR for the year 2023-24 (Schedule of Rates),  for the execution of such work.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:03:15+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C32a5e3b30a12412e
    previous_evidence_ids:
    - Jbe1b6f365da89484
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: The method of measurement for completed work follows the requirements stated in the Technical Specifications and the Bill of Quantities or elsewhere in the tender documents.
  evidence_ids:
  - Jb360bf15c6254704
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: Cfd31e912b60a85df
  citations:
  - id: Jb360bf15c6254704
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 6
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/6
    json_record_id: vol4/pricing_preamble/7
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"7\",\n  \"pdf_pages\": [\n    6\n  ],\n  \"record_id\": \"vol4/pricing_preamble/7\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        72.00054931640625,\n        476.6429138183594,\n        526.3876342773438,\n        486.9984130859375\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with\"\n    },\n    {\n      \"bbox\": [\n        89.88085174560547,\n        490.3229064941406,\n        526.3883666992188,\n        500.67840576171875\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"the requirements as stated in the Technical Specifications and as given in the Price\"\n    },\n    {\n      \"bbox\": [\n        89.88085174560547,\n        503.8829040527344,\n        417.6679382324219,\n        514.2384033203125\n      ],\n      \"pdf_page\": 6,\n      \"text\": \"document- Bill of Quantities or elsewhere in the tender documents.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"7. The method of measurement of completed work for payment shall be in accordance with\\nthe requirements as stated in the Technical Specifications and as given in the Price\\ndocument- Bill of Quantities or elsewhere in the tender documents.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:03:15+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Cbfe6dab4e461ef3d
    previous_evidence_ids:
    - Jf67d9260f1fad647
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: For area calculations regarding payment under property valuation guidelines, 50% of the area of any existing balcony and canopy is considered, whereas chejjas or similar coverings and shadows are excluded from payment.
  evidence_ids:
  - Jd9bd6bab9dfee535
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C8f9cff79544bc61f
  citations:
  - id: Jd9bd6bab9dfee535
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/16
    json_record_id: vol4/pricing_preamble/17
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"17\",\n  \"pdf_pages\": [\n    7\n  ],\n  \"record_id\": \"vol4/pricing_preamble/17\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.99984741210938,\n        377.8829345703125,\n        526.3875732421875,\n        388.2384338378906\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"17. 50% area of Balcony and Canopy if exists will be considered for calculating area for\"\n    },\n    {\n      \"bbox\": [\n        89.88016510009766,\n        391.44293212890625,\n        526.3853759765625,\n        401.7984313964844\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"payment as per the guide lines for valuation of properties. The area of chejjas or such\"\n    },\n    {\n      \"bbox\": [\n        89.88016510009766,\n        405.1229248046875,\n        397.38720703125,\n        415.4784240722656\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"similar coverings/shadows will not be considered for payment.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"17. 50% area of Balcony and Canopy if exists will be considered for calculating area for\\npayment as per the guide lines for valuation of properties. The area of chejjas or such\\nsimilar coverings/shadows will not be considered for payment.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:08:11+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C27b3ae9837ecedcd
    previous_evidence_ids:
    - J3c853fabd4214cdc
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Demolition and dismantling work must be carried out up to the ground level and/or basement level as applicable, including any underground water storage structures, with refilling of low-level areas up to ground level falling within the contractor's scope of work.
  evidence_ids:
  - Jdcdf13c0aabc9e14
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C097f9e563368cd4c
  citations:
  - id: Jdcdf13c0aabc9e14
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/17
    json_record_id: vol4/pricing_preamble/18
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"18\",\n  \"pdf_pages\": [\n    7\n  ],\n  \"record_id\": \"vol4/pricing_preamble/18\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        71.9998779296875,\n        424.80291748046875,\n        526.38720703125,\n        435.1584167480469\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"18. The demolition and dismantling shall be carried out up to ground and/or up to basement\"\n    },\n    {\n      \"bbox\": [\n        89.88018035888672,\n        438.4828796386719,\n        526.3875732421875,\n        448.83837890625\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"level as the case may be including underground water storage structures if any. Refilling\"\n    },\n    {\n      \"bbox\": [\n        89.88018035888672,\n        452.0428771972656,\n        472.6297912597656,\n        462.39837646484375\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"the low-level areas up to ground level is within the scope of contractor’s work.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"18. The demolition and dismantling shall be carried out up to ground and/or up to basement\\nlevel as the case may be including underground water storage structures if any. Refilling\\nthe low-level areas up to ground level is within the scope of contractor’s work.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:08:11+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C7d2c2a535153eee1
    previous_evidence_ids:
    - J98d1e29fbe253728
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Existing items within the proposed line of cut, excluding trees, must be dismantled, demolished, and their debris transported and disposed of.
  evidence_ids:
  - J7cf43a77f3241ea2
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: Ce0fe4be8498ba2de
  citations:
  - id: J7cf43a77f3241ea2
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/18
    json_record_id: vol4/pricing_preamble/19
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"19\",\n  \"pdf_pages\": [\n    7\n  ],\n  \"record_id\": \"vol4/pricing_preamble/19\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        72.00090026855469,\n        471.7228698730469,\n        526.3887329101562,\n        482.078369140625\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"19. The items existing excluding trees within the proposed line of cut have to be dismantled\"\n    },\n    {\n      \"bbox\": [\n        89.8812026977539,\n        485.4028625488281,\n        382.74884033203125,\n        495.75836181640625\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"and demolished and debris to be transported and disposed.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"19. The items existing excluding trees within the proposed line of cut have to be dismantled\\nand demolished and debris to be transported and disposed.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:08:11+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C21257317f6bcb5ce
    previous_evidence_ids:
    - Jd795e6f56622f314
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Total floor area for payment is defined as the summation of the total built area of all floors in the buildings indicated in Schedule A.
  evidence_ids:
  - J9c37cfe6c5cdd275
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C8ca3b75b1cfcaef6
  citations:
  - id: J9c37cfe6c5cdd275
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/19
    json_record_id: vol4/pricing_preamble/20
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"20\",\n  \"pdf_pages\": [\n    7\n  ],\n  \"record_id\": \"vol4/pricing_preamble/20\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        72.00192260742188,\n        505.08282470703125,\n        526.3892211914062,\n        515.4383544921875\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"20. The total floor area means the summation of total built area of all floors in the buildings\"\n    },\n    {\n      \"bbox\": [\n        89.8822250366211,\n        518.642822265625,\n        211.03143310546875,\n        528.9983520507812\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"indicated in Schedule A.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"20. The total floor area means the summation of total built area of all floors in the buildings\\nindicated in Schedule A.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:08:11+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C905c25e31f6d35e9
    previous_evidence_ids:
    - Jcd2d676f90f355c1
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: If buildings are added or deleted in the Bill of Quantities, the rates per square meter for such additions or deletions remain the same as specified, and payment is adjusted using the percentage quoted and accepted in the Summary Cost.
  evidence_ids:
  - Jd6b6e3ab9bef397d
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C7f11643db410199b
  citations:
  - id: Jd6b6e3ab9bef397d
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_clauses.json
    json_sha256: eb058f420d9bb04539482ff2016dcd2680c5cb2e6d9da4050b51f4beb4976608
    json_pointer: /records/20
    json_record_id: vol4/pricing_preamble/21
    source_review_status: pending_manual_review
    quote: "{\n  \"label\": \"21\",\n  \"pdf_pages\": [\n    7\n  ],\n  \"record_id\": \"vol4/pricing_preamble/21\",\n  \"review_status\": \"pending_manual_review\",\n  \"source_document\": \"Vol4DLNP1.pdf\",\n  \"source_lines\": [\n    {\n      \"bbox\": [\n        72.00222778320312,\n        538.2028198242188,\n        526.3898315429688,\n        548.558349609375\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"21. In case some buildings are deleted or added in BOQ, the rates per sqm for that\"\n    },\n    {\n      \"bbox\": [\n        89.88249969482422,\n        552.7227783203125,\n        526.3902587890625,\n        563.0783081054688\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"deletion/addition will be same as given above. For payment purpose, the %age quoted\"\n    },\n    {\n      \"bbox\": [\n        89.88249969482422,\n        567.2427978515625,\n        420.6696472167969,\n        577.5983276367188\n      ],\n      \"pdf_page\": 7,\n      \"text\": \"and accepted in the Summary Cost will be used for the above rate.\"\n    }\n  ],\n  \"source_sha256\": \"d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b\",\n  \"text\": \"21. In case some buildings are deleted or added in BOQ, the rates per sqm for that\\ndeletion/addition will be same as given above. For payment purpose, the %age quoted\\nand accepted in the Summary Cost will be used for the above rate.\",\n  \"type\": \"pricing_rule\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T07:08:11+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C0c72f6bb397ae6e8
    previous_evidence_ids:
    - Jcb4233cb85d132a2
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: summary
  text: Schedule B provides an estimated cost of INR 5,00,000.00 for items not covered in Schedule A, to be executed under the Common SR for the year 2023-24 published by the Karnataka Public Works Department with issue rates and amendments up to the date of tender submission.
  evidence_ids:
  - Jafe6730cc94e67f7
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C547fd4a9e883b09e
  citations:
  - id: Jafe6730cc94e67f7
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 10
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /boq_items/4
    json_record_id: schedule_b/item_1
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"500000.00\",\n  \"amount_inr_raw\": \"5,00,000.00\",\n  \"description\": \"Items \\nnot \\ncovered \\nin \\nthe \\nabove \\nSchedule A to be executed under \\nCommon SR for the year 2023-24 \\npublished by Karnataka public Works \\nDepartment \\nwith \\nissue \\nrates \\nand \\namendments issued upto date of tender \\nsubmission.\",\n  \"fragments\": [\n    {\n      \"description\": \"Items \\nnot \\ncovered \\nin \\nthe \\nabove \\nSchedule A to be executed under \\nCommon SR for the year 2023-24 \\npublished by Karnataka public Works \\nDepartment \\nwith \\nissue \\nrates \\nand \\namendments issued upto date of tender \\nsubmission.\",\n      \"pdf_page\": 10,\n      \"table_row\": 7\n    }\n  ],\n  \"item_number\": \"1\",\n  \"pdf_pages\": [\n    10\n  ],\n  \"quantity_raw\": \"---------\",\n  \"rate_inr_raw\": \"---------\",\n  \"record_id\": \"schedule_b/item_1\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"B\",\n  \"unit\": \"Lump\\nsum\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T11:17:08+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Cbec164e090971b8e
    previous_evidence_ids:
    - J8e7b0bc9a6c15f10
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: Schedule B estimated cost amount is 500000.00 INR, structured with lump sum unit terms.
  evidence_ids:
  - Jafe6730cc94e67f7
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: Cb0c108acbe989b4d
  citations:
  - id: Jafe6730cc94e67f7
    okf_path: OKF_bundle/Financial/vol4_secJ.md
    okf_sha256: 5d2e43480b6c02206fddcc3a604c39f7a8b7e9151264f6fd244328f09f8e9c87
    heading: Financial Document and Bill of Quantities
    source_document: Vol4DLNP1.pdf
    source_sha256: d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b
    pdf_pages:
    - 10
    sheet_cells: ''
    json_path: parsed_json/vol4/pricing_document.json
    json_sha256: e818be1fb28ea74092cb53a451b92e169c6e8a07afec0add897be67d5844a2b3
    json_pointer: /boq_items/4
    json_record_id: schedule_b/item_1
    source_review_status: pending_manual_review
    quote: "{\n  \"amount_inr_decimal\": \"500000.00\",\n  \"amount_inr_raw\": \"5,00,000.00\",\n  \"description\": \"Items \\nnot \\ncovered \\nin \\nthe \\nabove \\nSchedule A to be executed under \\nCommon SR for the year 2023-24 \\npublished by Karnataka public Works \\nDepartment \\nwith \\nissue \\nrates \\nand \\namendments issued upto date of tender \\nsubmission.\",\n  \"fragments\": [\n    {\n      \"description\": \"Items \\nnot \\ncovered \\nin \\nthe \\nabove \\nSchedule A to be executed under \\nCommon SR for the year 2023-24 \\npublished by Karnataka public Works \\nDepartment \\nwith \\nissue \\nrates \\nand \\namendments issued upto date of tender \\nsubmission.\",\n      \"pdf_page\": 10,\n      \"table_row\": 7\n    }\n  ],\n  \"item_number\": \"1\",\n  \"pdf_pages\": [\n    10\n  ],\n  \"quantity_raw\": \"---------\",\n  \"rate_inr_raw\": \"---------\",\n  \"record_id\": \"schedule_b/item_1\",\n  \"review_status\": \"pending_manual_review\",\n  \"schedule\": \"B\",\n  \"unit\": \"Lump\\nsum\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T11:17:08+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: C7a34dc6b5fedef18
    previous_evidence_ids:
    - J8e7b0bc9a6c15f10
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
entity_relations:
- relation_type: related_to
  target: concepts/salvage_ownership_and_credit.md
  title: Salvage Ownership and Schedule C Credit
  evidence_ids:
  - Jf17d55c6acfde864
last_provenance_migrated: '2026-11-01T13:54:09+00:00'
last_schema_aligned: '2026-11-01T14:33:52+00:00'
---

# Financial Document and Bill of Quantities Overview (Section J)

> Draft source synthesis. Pending PDF and human review; no compliance or applicability decision.

## Summary

Volume 4 Section J establishes the Financial Document, Letter of Price Bid, pricing rules and instructions, and Bill of Quantities (BOQ) abstract and item schedules for BMRCL Tender Package P1. [^e1] [^e2] [^e3] [^e4] [^e5] [^e6] [^e7] [^e8] [^e9]

Pricing rules specify that work execution must follow the Bill of Quantity descriptions, technical specifications, standards of MORTH, KPWD, CPWD, drawings, engineering practices, and instructions of the Engineer. [^e10]

## Key parameters

| Parameter | Value | Citation | Status |
|---|---|---|---|
| Financial Section J — C6acf07c2994f34b5 | The estimated cost put to tender for Schedule-B (Items under Schedule of Rate published by KPWD) is INR 5,00,000.00, bringing the total estimated cost for Schedules A and B to INR 4,74,41,306.00. | [^e11] [^e12] [^e8] | Pending review |
| Financial Section J — C91deff25ac841e85 | Schedule-C represents a lump-sum credit to BMRCL for salvageable items out of dismantled or demolished private properties with no owner interest, shown with a placeholder ('----') in the BOQ abstract. | [^e13] [^e8] | Pending review |
| Financial Section J — C95906234658b2af8 | Schedule A of the BOQ abstract specifies partial and full demolition and dismantling works amounting to ₹ 4,69,41,306.00. | [^e3] | Pending review |
| Financial Section J — Ccff130cee7928894 | Tenderers must quote percentage rates in two decimals for Schedule A (At Par / Excess / Less), 'At Par' only for Schedule B, and a lump sum credit amount to BMRCL on salvage of materials for Schedule C. | [^e5] | Pending review |
| Financial Section J — C1a2679c7c01e761f | The total estimated cost for Schedule-A (Partial & Full demolition and dismantling work) is ₹ 4,69,41,306.00. | [^e14] [^e2] [^e3] [^e8] | Pending review |
| Financial Section J — C43d474e29a31aa7f | The total estimated cost for Schedule-B (Items under Schedule of Rate published by KPWD) is ₹ 5,00,000.00, bringing the total estimated cost of Schedules A and B to ₹ 4,74,41,306.00. | [^e15] [^e2] [^e16] | Pending review |
| Financial Section J — C08459f8e8703216f | Schedule-C specifies a credit to BMRCL for salvageable items out of dismantled or demolished private properties on which the owner has no interest, listed as a lump-sum amount without a predefined numerical estimate in the abstract summary. | [^e2] [^e17] | Pending review |
| Financial Section J — C5123a54e163baa33 | Schedule-A item 1 specifies partial demolition and dismantling of structures of different heights at a quantity of 31,245.00 Sqm with a rate of ₹ 1,087.00 per Sqm, resulting in an amount of ₹ 3,39,63,315.00. | [^e18] | Pending review |
| Financial Section J — C480df6a468c882b8 | Schedule-A item 2 specifies full demolition and dismantling of structures at a quantity of 21,760.00 Sqm with a rate of ₹ 548.00 per Sqm, resulting in an amount of ₹ 1,19,24,480.00. | [^e19] [^e20] | Pending review |
| Financial Section J — C6fcd4b66d74bbd5d | Schedule-A item 3 specifies demolition and dismantling of compound walls at a quantity of 5,183.00 Rmt with a rate of ₹ 167.00 per Rmt, resulting in an amount of ₹ 8,65,561.00. | [^e19] [^e21] | Pending review |
| Financial Section J — C39d282efdfc73231 | Schedule-A item 4 specifies demolition and dismantling of steel structures such as sign boards and hoardings at a quantity of 25.00 MT with a rate of ₹ 7,518.00 per MT, resulting in an amount of ₹ 1,87,950.00. | [^e16] [^e22] | Pending review |
| Financial Section J — C904d49cbfbc57854 | Pricing rule 6 dictates that the Tender Price or Quoted Price includes all applicable taxes, duties, cess, royalties, and statutory levies in force as of the last day of the month previous to the month of tender invitation, except Goods and Services Tax (GST). | [^e1] [^e5] [^e7] | Pending review |
| Financial Section J — C287d51717cf1e68a | The total estimated cost for Schedule-B (Items under KPWD Schedule of Rate) is ₹ 5,00,000.00, making the combined total of Schedules A and B ₹ 4,74,41,306.00. | [^e2] | Pending review |
| Financial Section J — Cd8a5a29655e5c7f6 | Schedule-C represents credit to BMRCL for salvageable items out of dismantled/demolished private properties where owners have no interest, indicated as lump sum amount to be offered by tenderers. | [^e2] [^e5] | Pending review |
| Financial Section J — C13a655796690e902 | Tenderers must quote percentage rates in two decimals for Schedule-A (selecting At Par / Excess / Less), quote At Par for Schedule-B, and offer a lump sum credit for Schedule-C. | [^e5] | Pending review |
| Financial Section J — C0a72f78784598aaa | Underlying BOQ workbook structure includes automated cell formulas and number-to-words functions such as SpellNumber and SpellNumberMC for calculation and verification of tender sums. | [^e23] [^e24] [^e25] [^e26] [^e27] | Pending review |
| Financial Section J — Cfd31e912b60a85df | The method of measurement for completed work follows the requirements stated in the Technical Specifications and the Bill of Quantities or elsewhere in the tender documents. | [^e28] | Pending review |
| Financial Section J — C8f9cff79544bc61f | For area calculations regarding payment under property valuation guidelines, 50% of the area of any existing balcony and canopy is considered, whereas chejjas or similar coverings and shadows are excluded from payment. | [^e29] | Pending review |
| Financial Section J — C097f9e563368cd4c | Demolition and dismantling work must be carried out up to the ground level and/or basement level as applicable, including any underground water storage structures, with refilling of low-level areas up to ground level falling within the contractor's scope of work. | [^e30] | Pending review |
| Financial Section J — Ce0fe4be8498ba2de | Existing items within the proposed line of cut, excluding trees, must be dismantled, demolished, and their debris transported and disposed of. | [^e31] | Pending review |
| Financial Section J — C8ca3b75b1cfcaef6 | Total floor area for payment is defined as the summation of the total built area of all floors in the buildings indicated in Schedule A. | [^e32] | Pending review |
| Financial Section J — C7f11643db410199b | If buildings are added or deleted in the Bill of Quantities, the rates per square meter for such additions or deletions remain the same as specified, and payment is adjusted using the percentage quoted and accepted in the Summary Cost. | [^e33] | Pending review |
| Financial Section J — Cb0c108acbe989b4d | Schedule B estimated cost amount is 500000.00 INR, structured with lump sum unit terms. | [^e34] | Pending review |

## Where it appears

- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/2`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/1`)
- [[OKF_bundle/Financial/vol4_secJ#2.0 — Abstract of Bill of Quantities (BOQ)|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/3`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/0`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_document.json#/pages/5`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_clauses.json#/records/5`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/pricing_document.json#/pages/7`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_clauses.json#/records/1`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 1 (`parsed_json/vol4/pricing_document.json#/pages/0`)
- [[OKF_bundle/Financial/vol4_secJ#1.0 — Pricing Document Preamble and Instructions|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF pp. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1 row 13 (`parsed_json/boq/boq_workbook.json#/schedules/0`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1 row 14 (`parsed_json/boq/boq_workbook.json#/schedules/1`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 10 (`parsed_json/vol4/pricing_document.json#/pages/9`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1 row 15 (`parsed_json/boq/boq_workbook.json#/schedules/2`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 9 (`parsed_json/vol4/pricing_document.json#/boq_items/0`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 9 (`parsed_json/vol4/pricing_document.json#/pages/8`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 9 (`parsed_json/vol4/pricing_document.json#/boq_items/1`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF pp. 9, 10 (`parsed_json/vol4/pricing_document.json#/boq_items/2`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 10 (`parsed_json/vol4/pricing_document.json#/boq_items/3`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BA$17 (`parsed_json/boq/boq_formulas.json#/formulas/18`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BC$17 (`parsed_json/boq/boq_formulas.json#/formulas/20`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$C$18 (`parsed_json/boq/boq_formulas.json#/formulas/21`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BB$17 (`parsed_json/boq/boq_formulas.json#/formulas/19`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BC$16 (`parsed_json/boq/boq_formulas.json#/formulas/17`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/11`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/12`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/13`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/15`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_clauses.json#/records/6`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/16`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/17`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/18`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/19`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/20`)
- [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 10 (`parsed_json/vol4/pricing_document.json#/boq_items/4`)

## Relations

| Source | Relation | Target | Classification | Citation | Status |
|---|---|---|---|---|---|

- **related_to (inferred editorial navigation):** [[wiki/concepts/salvage_ownership_and_credit|Salvage Ownership and Schedule C Credit]]. [^e5]

## Open questions and contradictions

No additional conflict is recorded on this page. Verification remains open in [[wiki/review_queue|the review queue]]; absence of a recorded contradiction is not approval.

## Amendment states

Historical source quotations are retained. A superseded field or deleted subclause does not make the entire page superseded.

| Parameter | Value | Citation | Status |
|---|---|---|---|

## Additional source statements

- The removal of items such as hoardings, interior lighting, interior furniture, ACP cladding, and structural glazing within the line of cut is treated as incidental work with no separate payment considered. [^e35]
- Where power, water, or other utilities must be maintained during demolition, such lines must be temporarily relocated and protected prior to commencing demolition work. [^e36]
- When advised by the Consultant or BMRCL, the contractor must provide permanent supports and related restoration works before or after demolition to maintain Line of Clearance (LOC), paid according to accepted BOQ rates for items available in the Common Schedule of Rates (Common SR) for the year 2023-24. [^e37]
- Schedule B provides an estimated cost of INR 5,00,000.00 for items not covered in Schedule A, to be executed under the Common SR for the year 2023-24 published by the Karnataka Public Works Department with issue rates and amendments up to the date of tender submission. [^e34]

## Claim register

Claim IDs and evidence records are retained in frontmatter. Every draft claim has an entry in [[wiki/review_queue|the claim-level review queue]].

## Citation notes

[^e1]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_clauses.json#/records/5`)
[^e2]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/pricing_document.json#/pages/7`)
[^e3]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/0`)
[^e4]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_clauses.json#/records/1`)
[^e5]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_document.json#/pages/5`)
[^e6]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 1 (`parsed_json/vol4/pricing_document.json#/pages/0`)
[^e7]: [[OKF_bundle/Financial/vol4_secJ#1.0 — Pricing Document Preamble and Instructions|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6
[^e8]: [[OKF_bundle/Financial/vol4_secJ#2.0 — Abstract of Bill of Quantities (BOQ)|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8
[^e9]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF pp. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
[^e10]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/11`)
[^e11]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/2`)
[^e12]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/1`)
[^e13]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/3`)
[^e14]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1 row 13 (`parsed_json/boq/boq_workbook.json#/schedules/0`)
[^e15]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1 row 14 (`parsed_json/boq/boq_workbook.json#/schedules/1`)
[^e16]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 10 (`parsed_json/vol4/pricing_document.json#/pages/9`)
[^e17]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1 row 15 (`parsed_json/boq/boq_workbook.json#/schedules/2`)
[^e18]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 9 (`parsed_json/vol4/pricing_document.json#/boq_items/0`)
[^e19]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 9 (`parsed_json/vol4/pricing_document.json#/pages/8`)
[^e20]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 9 (`parsed_json/vol4/pricing_document.json#/boq_items/1`)
[^e21]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF pp. 9, 10 (`parsed_json/vol4/pricing_document.json#/boq_items/2`)
[^e22]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 10 (`parsed_json/vol4/pricing_document.json#/boq_items/3`)
[^e23]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BA$17 (`parsed_json/boq/boq_formulas.json#/formulas/18`)
[^e24]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BC$17 (`parsed_json/boq/boq_formulas.json#/formulas/20`)
[^e25]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$C$18 (`parsed_json/boq/boq_formulas.json#/formulas/21`)
[^e26]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BB$17 (`parsed_json/boq/boq_formulas.json#/formulas/19`)
[^e27]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BC$16 (`parsed_json/boq/boq_formulas.json#/formulas/17`)
[^e28]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_clauses.json#/records/6`)
[^e29]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/16`)
[^e30]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/17`)
[^e31]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/18`)
[^e32]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/19`)
[^e33]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/20`)
[^e34]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 10 (`parsed_json/vol4/pricing_document.json#/boq_items/4`)
[^e35]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/12`)
[^e36]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/13`)
[^e37]: [[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/15`)

<details>
<summary>Supporting source passages</summary>

### Je35bc79dc160b3f0

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_clauses.json#/records/5`)

> {
>   "label": "6",
>   "pdf_pages": [
>     6
>   ],
>   "record_id": "vol4/pricing_preamble/6",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         71.99951171875,
>         429.72296142578125,
>         526.3866577148438,
>         440.0784606933594
>       ],
>       "pdf_page": 6,
>       "text": "6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,"
>     },
>     {
>       "bbox": [
>         89.87982940673828,
>         443.2829284667969,
>         526.3870239257812,
>         453.638427734375
>       ],
>       "pdf_page": 6,
>       "text": "and statutory levies as per the laws in force as on last day of the month previous to the"
>     },
>     {
>       "bbox": [
>         89.87982940673828,
>         456.9629211425781,
>         446.9472351074219,
>         467.31842041015625
>       ],
>       "pdf_page": 6,
>       "text": "month of invitation of this tender, except Goods and Services Tax (GST)."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties,\nand statutory levies as per the laws in force as on last day of the month previous to the\nmonth of invitation of this tender, except Goods and Services Tax (GST).",
>   "type": "pricing_rule"
> }

### Jabb0383ef371ea9a

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/pricing_document.json#/pages/7`)

> {
>   "page_type": "text",
>   "pdf_page": 8,
>   "review_status": "pending_manual_review",
>   "text": " BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \n \n \n \nBangalore Metro Rail Corporation Ltd.                            September 2026 \nSection Page 5 of 7 \n \nPRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \n \n \nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \nidentified in Bangalore Metro Rail Project Phase-3.” \nContract \nPackage-P1: \n“Partial \nand \nFull \nDemolition/Dismantling \nof \nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \nRail Project Phase-3.” \nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \n09.09.2026 \n \nSl.No \nSchedule \nSchedule Description \nTotal Estimated Cost \n(Rs) \n1 \nSCHEDULE-A \nPartial & Full demolition and dismantling \nwork as per details given in Schedule-A \nof the BOQ \n4,69,41,306.00\n2 \nSCHEDULE-B \nItems under Schedule of Rate published \nby KPWD \n5,00,000.00\nTotal of Schedules (A+B)\n4,74,41,306.00\n3 \nSCHEDULE-C \nCredit to BMRCL for salvageable items \nout of dismantled/demolished private \nproperties on which the owner has no \ninterest (as elaborated in Para 15 of Part-\n3 of ‘Employer’s Requirement’). \n---- \n \n \n \n \n \n \n \n \n \n307\n",
>   "text_blocks": [
>     {
>       "bbox": [
>         14.760004043579102,
>         37.509437561035156,
>         519.9669799804688,
>         56.52032470703125
>       ],
>       "block_number": 0,
>       "text": " BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \n \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         62.5140495300293,
>         74.49351501464844,
>         69.48028564453125
>       ],
>       "block_number": 1,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         777.8273315429688,
>         74.38514709472656,
>         786.9194946289062
>       ],
>       "block_number": 2,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         802.54736328125,
>         525.8132934570312,
>         823.079833984375
>       ],
>       "block_number": 3,
>       "text": "Bangalore Metro Rail Corporation Ltd.                            September 2026 \nSection Page 5 of 7 \n \n"
>     },
>     {
>       "bbox": [
>         123.11994934082031,
>         74.64318084716797,
>         475.146728515625,
>         84.99869537353516
>       ],
>       "block_number": 4,
>       "text": "PRICING DOCUMENT- ABSTRACT OF BILL OF QUANTITIES (BOQ) \n"
>     },
>     {
>       "bbox": [
>         71.99957275390625,
>         88.32317352294922,
>         520.5064697265625,
>         140.43870544433594
>       ],
>       "block_number": 5,
>       "text": " \n \nName of the Work-: “Partial and Full Demolition/Dismantling of Buildings/Structures \nidentified in Bangalore Metro Rail Project Phase-3.” \n"
>     },
>     {
>       "bbox": [
>         72.0000228881836,
>         144.60321044921875,
>         526.3865966796875,
>         240.7587127685547
>       ],
>       "block_number": 6,
>       "text": "Contract \nPackage-P1: \n“Partial \nand \nFull \nDemolition/Dismantling \nof \nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore Road \nStation (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1of Bangalore Metro \nRail Project Phase-3.” \nTender Notification No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157, Dated. \n09.09.2026 \n \n"
>     },
>     {
>       "bbox": [
>         66.96002960205078,
>         244.203125,
>         528.9071655273438,
>         260.9186706542969
>       ],
>       "block_number": 7,
>       "text": "Sl.No \nSchedule \nSchedule Description \nTotal Estimated Cost \n"
>     },
>     {
>       "bbox": [
>         460.4398193359375,
>         256.92315673828125,
>         484.86712646484375,
>         267.2786560058594
>       ],
>       "block_number": 8,
>       "text": "(Rs) \n"
>     },
>     {
>       "bbox": [
>         77.87996673583984,
>         294.8431396484375,
>         186.78732299804688,
>         305.1986389160156
>       ],
>       "block_number": 9,
>       "text": "1 \nSCHEDULE-A \n"
>     },
>     {
>       "bbox": [
>         200.1597442626953,
>         282.1231689453125,
>         405.0671081542969,
>         317.7986145019531
>       ],
>       "block_number": 10,
>       "text": "Partial & Full demolition and dismantling \nwork as per details given in Schedule-A \nof the BOQ \n"
>     },
>     {
>       "bbox": [
>         456.11981201171875,
>         294.72314453125,
>         529.6943969726562,
>         305.0786437988281
>       ],
>       "block_number": 11,
>       "text": "4,69,41,306.00\n"
>     },
>     {
>       "bbox": [
>         77.87996673583984,
>         332.64312744140625,
>         529.6943969726562,
>         355.5986328125
>       ],
>       "block_number": 12,
>       "text": "2 \nSCHEDULE-B \nItems under Schedule of Rate published \nby KPWD \n5,00,000.00\n"
>     },
>     {
>       "bbox": [
>         271.31988525390625,
>         374.8830871582031,
>         529.6962280273438,
>         385.23858642578125
>       ],
>       "block_number": 13,
>       "text": "Total of Schedules (A+B)\n4,74,41,306.00\n"
>     },
>     {
>       "bbox": [
>         77.87996673583984,
>         429.96307373046875,
>         187.02545166015625,
>         440.3185729980469
>       ],
>       "block_number": 14,
>       "text": "3 \nSCHEDULE-C \n"
>     },
>     {
>       "bbox": [
>         200.1597442626953,
>         404.64306640625,
>         405.0672302246094,
>         465.6385498046875
>       ],
>       "block_number": 15,
>       "text": "Credit to BMRCL for salvageable items \nout of dismantled/demolished private \nproperties on which the owner has no \ninterest (as elaborated in Para 15 of Part-\n3 of ‘Employer’s Requirement’). \n"
>     },
>     {
>       "bbox": [
>         463.7998046875,
>         429.96307373046875,
>         481.507080078125,
>         440.3185729980469
>       ],
>       "block_number": 16,
>       "text": "---- \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         480.4830322265625,
>         75.06725311279297,
>         572.7985229492188
>       ],
>       "block_number": 17,
>       "text": " \n \n \n \n \n \n \n"
>     },
>     {
>       "bbox": [
>         523.3197021484375,
>         576.0029296875,
>         526.386962890625,
>         586.3584594726562
>       ],
>       "block_number": 18,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         523.3197021484375,
>         600.48291015625,
>         526.386962890625,
>         610.8384399414062
>       ],
>       "block_number": 19,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         546.0439453125,
>         24.479991912841797,
>         570.0199584960938,
>         41.38799285888672
>       ],
>       "block_number": 20,
>       "text": "307\n"
>     }
>   ]
> }

### J241ce183fcecf015

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/0`)

> {
>   "amount_inr_decimal": "46941306.00",
>   "amount_raw": "4,69,41,306.00",
>   "cell_clips": [
>     [
>       60.900000000000006,
>       280.39,
>       100.77,
>       329.54
>     ],
>     [
>       102.17,
>       280.39,
>       194.06,
>       329.54
>     ],
>     [
>       195.45999999999998,
>       280.39,
>       406.82,
>       329.54
>     ],
>     [
>       408.21999999999997,
>       280.39,
>       534.17,
>       329.54
>     ]
>   ],
>   "cells": [
>     "1",
>     "SCHEDULE-A",
>     "Partial & Full demolition and dismantling \nwork as per details given in Schedule-A \nof the BOQ",
>     "4,69,41,306.00"
>   ],
>   "pdf_pages": [
>     8
>   ],
>   "record_id": "vol4/boq_abstract/A",
>   "review_status": "pending_manual_review",
>   "schedule": "A"
> }

### J05ebc60fd5ad4602

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_clauses.json#/records/1`)

> {
>   "label": "2",
>   "pdf_pages": [
>     6
>   ],
>   "record_id": "vol4/pricing_preamble/2",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         71.999267578125,
>         187.3231201171875,
>         526.38671875,
>         197.6786346435547
>       ],
>       "pdf_page": 6,
>       "text": "2. The quantities given in the Price document - “Bill of Quantities” are estimated"
>     },
>     {
>       "bbox": [
>         89.87957000732422,
>         200.88311767578125,
>         526.3868408203125,
>         211.23863220214844
>       ],
>       "pdf_page": 6,
>       "text": "(provisional). The basis of payment will be the actual quantities of work ordered and"
>     },
>     {
>       "bbox": [
>         89.87957000732422,
>         214.5631103515625,
>         526.3862915039062,
>         224.9186248779297
>       ],
>       "pdf_page": 6,
>       "text": "carried out, as measured by the Contractor and verified by the Engineer and valued at"
>     },
>     {
>       "bbox": [
>         89.87957000732422,
>         228.24310302734375,
>         457.9883117675781,
>         238.59861755371094
>       ],
>       "pdf_page": 6,
>       "text": "the rates in the accepted priced “Price Bid – Summary of Bill of Quantities”."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "2. The quantities given in the Price document - “Bill of Quantities” are estimated\n(provisional). The basis of payment will be the actual quantities of work ordered and\ncarried out, as measured by the Contractor and verified by the Engineer and valued at\nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”.",
>   "type": "pricing_rule"
> }

### Jf17d55c6acfde864

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_document.json#/pages/5`)

> {
>   "page_type": "text",
>   "pdf_page": 6,
>   "review_status": "pending_manual_review",
>   "text": " BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \n \n \n \nBangalore Metro Rail Corporation Ltd.                            September 2026 \nSection Page 3 of 7 \n \nPricing Document-Preamble \n1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \nshall be read in conjunction with the entire Tender and Contract Document including \nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \nCorrigendum and Addendums. \n2. The quantities given in the Price document - “Bill of Quantities” are estimated \n(provisional). The basis of payment will be the actual quantities of work ordered and \ncarried out, as measured by the Contractor and verified by the Engineer and valued at \nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \n3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \n4. The Lump sum amount indicated for Schedule C will be recovered from the running \naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \nthe value of credit to BMRCL will be increased/decreased according to the value of work \ndone from the ‘on account’ bills on pro-rata basis. \n5. The Contractor should note that the credit to BMRCL on salvage materials should be in \nreference to the quoted price and not on the estimate cost put to tender. \n6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \nand statutory levies as per the laws in force as on last day of the month previous to the \nmonth of invitation of this tender, except Goods and Services Tax (GST). \n7. The method of measurement of completed work for payment shall be in accordance with \nthe requirements as stated in the Technical Specifications and as given in the Price \ndocument- Bill of Quantities or elsewhere in the tender documents. \n8. The quoted price is for completed and finished items of work and complete in all respects \ncomplying with the provisions of the Contract. It will be deemed to have included all \nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \n9. The quoted price will be deemed to have included all the safety measures at work sites/ \ncasting yard, safety measures for workmen & road users, safety of the public and \nprotection of adjoining land & building while working. \n10. The quoted price will be deemed to have included establishment & overhead charges, \ncontractor’s profit, supervision, other charges together with all general risks, liabilities \nand obligations set out or implied in the contract and including remedy of any defects \nduring the Defect Liability Period.  \n11. The quoted price will be deemed to have included accommodations for staff & workmen, \nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \ncharges payable to various departments for obtaining necessary approvals if any. \n305\n",
>   "text_blocks": [
>     {
>       "bbox": [
>         14.760004043579102,
>         37.509437561035156,
>         519.9669799804688,
>         56.52032470703125
>       ],
>       "block_number": 0,
>       "text": " BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \n \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         62.5140495300293,
>         74.49351501464844,
>         69.48028564453125
>       ],
>       "block_number": 1,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         777.8273315429688,
>         74.38514709472656,
>         786.9194946289062
>       ],
>       "block_number": 2,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         802.54736328125,
>         525.8132934570312,
>         823.079833984375
>       ],
>       "block_number": 3,
>       "text": "Bangalore Metro Rail Corporation Ltd.                            September 2026 \nSection Page 3 of 7 \n \n"
>     },
>     {
>       "bbox": [
>         227.51991271972656,
>         74.64318084716797,
>         377.9470520019531,
>         84.99869537353516
>       ],
>       "block_number": 4,
>       "text": "Pricing Document-Preamble \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         99.36321258544922,
>         526.3881225585938,
>         177.9987030029297
>       ],
>       "block_number": 5,
>       "text": "1. The Pricing Document-Bill of Quantities (BOQ) & Abstract to Bill of Quantities (BOQ) \nshall be read in conjunction with the entire Tender and Contract Document including \nInstructions to Tenderers, General Conditions of Contract (including ‘Contract Data’), \nSpecial Conditions of Contract, Notice Inviting Tender, Technical Specifications, \nEmployer’s Requirements, Scope of work,  Schedule, Attachments, Appendix, Annexure, \nCorrigendum and Addendums. \n"
>     },
>     {
>       "bbox": [
>         71.999267578125,
>         187.3231201171875,
>         526.3868408203125,
>         238.59861755371094
>       ],
>       "block_number": 6,
>       "text": "2. The quantities given in the Price document - “Bill of Quantities” are estimated \n(provisional). The basis of payment will be the actual quantities of work ordered and \ncarried out, as measured by the Contractor and verified by the Engineer and valued at \nthe rates in the accepted priced “Price Bid – Summary of Bill of Quantities”. \n"
>     },
>     {
>       "bbox": [
>         71.99929809570312,
>         247.923095703125,
>         526.387451171875,
>         326.4385681152344
>       ],
>       "block_number": 7,
>       "text": "3. Tenderer shall quote in the Price Bid (.xls format) sheet only in accordance with the ITT \nclause 10. Tenderer is advised to quote their percentage rate in two decimals for \nSchedule-A. Tenderer has to select option “At Par / Excess / Less” and enter percentage \nrate in figures on estimated cost to Schedule-A, for Schedule-B tenderer is required to \nselect percentage option as ‘At Par’ only and for Schedule-C tenderer shall offer Credit \nto BMRCL on Salvage of Materials, in ‘Lump sum’ amount. \n"
>     },
>     {
>       "bbox": [
>         71.99847412109375,
>         335.7630310058594,
>         526.3863525390625,
>         387.0384826660156
>       ],
>       "block_number": 8,
>       "text": "4. The Lump sum amount indicated for Schedule C will be recovered from the running \naccount bills proportionately. In case of any variation in Quantities (increase/decrease), \nthe value of credit to BMRCL will be increased/decreased according to the value of work \ndone from the ‘on account’ bills on pro-rata basis. \n"
>     },
>     {
>       "bbox": [
>         71.99948120117188,
>         396.36297607421875,
>         526.3870239257812,
>         420.3984680175781
>       ],
>       "block_number": 9,
>       "text": "5. The Contractor should note that the credit to BMRCL on salvage materials should be in \nreference to the quoted price and not on the estimate cost put to tender. \n"
>     },
>     {
>       "bbox": [
>         71.99951171875,
>         429.72296142578125,
>         526.3870239257812,
>         467.31842041015625
>       ],
>       "block_number": 10,
>       "text": "6. The ‘Tender Price’ or ‘Quoted Price’ includes all applicable taxes, duties, cess, royalties, \nand statutory levies as per the laws in force as on last day of the month previous to the \nmonth of invitation of this tender, except Goods and Services Tax (GST). \n"
>     },
>     {
>       "bbox": [
>         72.00054931640625,
>         476.6429138183594,
>         526.3883666992188,
>         514.2384033203125
>       ],
>       "block_number": 11,
>       "text": "7. The method of measurement of completed work for payment shall be in accordance with \nthe requirements as stated in the Technical Specifications and as given in the Price \ndocument- Bill of Quantities or elsewhere in the tender documents. \n"
>     },
>     {
>       "bbox": [
>         72.00054931640625,
>         523.5628662109375,
>         526.3883666992188,
>         602.1983642578125
>       ],
>       "block_number": 12,
>       "text": "8. The quoted price is for completed and finished items of work and complete in all respects \ncomplying with the provisions of the Contract. It will be deemed to have included all \nconstructional plant, machinery tools, fuel, oil, consumables, electric power, water, \ntransportation, disposal of debris at BBMP/GBA identified C&D waste management \nfacility (dismantled/demolished material), all leads & lifts, all temporary works & false \nworks, fencing, watering, lighting, maintenance, night working and inspection facilities. \n"
>     },
>     {
>       "bbox": [
>         72.00051879882812,
>         611.5228271484375,
>         526.3880615234375,
>         649.1182861328125
>       ],
>       "block_number": 13,
>       "text": "9. The quoted price will be deemed to have included all the safety measures at work sites/ \ncasting yard, safety measures for workmen & road users, safety of the public and \nprotection of adjoining land & building while working. \n"
>     },
>     {
>       "bbox": [
>         72.00051879882812,
>         658.4427490234375,
>         526.3875732421875,
>         709.71826171875
>       ],
>       "block_number": 14,
>       "text": "10. The quoted price will be deemed to have included establishment & overhead charges, \ncontractor’s profit, supervision, other charges together with all general risks, liabilities \nand obligations set out or implied in the contract and including remedy of any defects \nduring the Defect Liability Period.  \n"
>     },
>     {
>       "bbox": [
>         71.99981689453125,
>         719.042724609375,
>         526.3865966796875,
>         756.6382446289062
>       ],
>       "block_number": 15,
>       "text": "11. The quoted price will be deemed to have included accommodations for staff & workmen, \nall insurance costs for labour & works, the payment of all wages, salaries, fees if any, \ncharges payable to various departments for obtaining necessary approvals if any. \n"
>     },
>     {
>       "bbox": [
>         546.0439453125,
>         24.479991912841797,
>         570.0199584960938,
>         41.38799285888672
>       ],
>       "block_number": 16,
>       "text": "305\n"
>     }
>   ]
> }

### Jf28ae5cc3f92b618

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 1 (`parsed_json/vol4/pricing_document.json#/pages/0`)

> {
>   "page_type": "text",
>   "pdf_page": 1,
>   "review_status": "pending_manual_review",
>   "text": "  \n \n \n    \n \n \n \n \n \n \n \n \n                       \nBANGALORE METRO RAIL PROJECT, PHASE-3 \n \nName of the Work: “Partial and Full Demolition/Dismantling of \nBuildings/Structures identified in Bangalore Metro Rail Project Phase-3.” \nContract Package-P1: “Partial and Full Demolition/Dismantling of \nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore \nRoad Station (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1 of \nBangalore Metro Rail Project Phase-3.”       \n \n \n        \nTender No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157 \nSEPTEMBER-2026 \nFINANCIAL DOCUMENT \n(Pricing Document) \nVOLUME - 4  \n",
>   "text_blocks": [
>     {
>       "bbox": [
>         63.9599723815918,
>         19.569625854492188,
>         302.403564453125,
>         44.40032958984375
>       ],
>       "block_number": 0,
>       "text": "  \n \n"
>     },
>     {
>       "bbox": [
>         63.9599723815918,
>         97.07410430908203,
>         66.45352172851562,
>         104.04034423828125
>       ],
>       "block_number": 1,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         63.9599723815918,
>         122.51410675048828,
>         73.89351654052734,
>         129.4803466796875
>       ],
>       "block_number": 2,
>       "text": "    \n"
>     },
>     {
>       "bbox": [
>         14.400049209594727,
>         147.95411682128906,
>         304.29351806640625,
>         154.92034912109375
>       ],
>       "block_number": 3,
>       "text": " \n \n"
>     },
>     {
>       "bbox": [
>         14.400049209594727,
>         173.3941192626953,
>         16.893596649169922,
>         180.3603515625
>       ],
>       "block_number": 4,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         14.400049209594727,
>         198.8340606689453,
>         16.893596649169922,
>         205.80029296875
>       ],
>       "block_number": 5,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         14.400049209594727,
>         224.27406311035156,
>         491.492431640625,
>         231.24029541015625
>       ],
>       "block_number": 6,
>       "text": " \n \n \n"
>     },
>     {
>       "bbox": [
>         49.79998016357422,
>         250.77337646484375,
>         544.8611450195312,
>         358.8686218261719
>       ],
>       "block_number": 7,
>       "text": " \n                       \nBANGALORE METRO RAIL PROJECT, PHASE-3 \n \nName of the Work: “Partial and Full Demolition/Dismantling of \nBuildings/Structures identified in Bangalore Metro Rail Project Phase-3.” \n"
>     },
>     {
>       "bbox": [
>         68.3995361328125,
>         364.299072265625,
>         544.8632202148438,
>         476.8801574707031
>       ],
>       "block_number": 8,
>       "text": "Contract Package-P1: “Partial and Full Demolition/Dismantling of \nBuildings/Structures identified from JP Nagar 4th Phase Station to Mysore \nRoad Station (from Ch: (-) 0.330 Km to Ch: 10.550 Km) in Corridor-1 of \nBangalore Metro Rail Project Phase-3.”       \n \n \n"
>     },
>     {
>       "bbox": [
>         108.47999572753906,
>         492.7681579589844,
>         153.18820190429688,
>         515.2801513671875
>       ],
>       "block_number": 9,
>       "text": "        \n"
>     },
>     {
>       "bbox": [
>         101.75995635986328,
>         65.61921691894531,
>         498.2138366699219,
>         78.78872680664062
>       ],
>       "block_number": 10,
>       "text": "Tender No: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157 \n"
>     },
>     {
>       "bbox": [
>         239.87989807128906,
>         600.3389282226562,
>         366.7764892578125,
>         613.5084838867188
>       ],
>       "block_number": 11,
>       "text": "SEPTEMBER-2026 \n"
>     },
>     {
>       "bbox": [
>         222.4799041748047,
>         498.3390197753906,
>         386.7032470703125,
>         511.508544921875
>       ],
>       "block_number": 12,
>       "text": "FINANCIAL DOCUMENT \n"
>     },
>     {
>       "bbox": [
>         238.0798797607422,
>         514.4190063476562,
>         371.10076904296875,
>         527.5885620117188
>       ],
>       "block_number": 13,
>       "text": "(Pricing Document) \n"
>     },
>     {
>       "bbox": [
>         262.55303955078125,
>         540.5789794921875,
>         350.4632568359375,
>         553.74853515625
>       ],
>       "block_number": 14,
>       "text": "VOLUME - 4  \n"
>     }
>   ]
> }

### S10ec60af02b3e977

[[OKF_bundle/Financial/vol4_secJ#1.0 — Pricing Document Preamble and Instructions|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6

> - **Read BOQ with the Complete Tender and Contract Documents** (Instruction 1)
> - **Provisional Quantities and Payment for Measured Work** (Instruction 2)
> - **Price Bid Preparation in the Prescribed XLS Sheet** (Instruction 3; ITT 10)
>   - Schedule-A: percentage rate to two decimals; At Par / Excess / Less
>   - Schedule-B: At Par only
>   - Schedule-C: lump-sum salvage credit to BMRCL
> - **Proportionate Recovery and Adjustment of Salvage Credit** (Instruction 4)
> - **Salvage Credit Based on Quoted Price** (Instruction 5)
> - **Taxes and Statutory Levies Included, Except GST** (Instruction 6)
> - **Measurement of Completed Work** (Instruction 7)
> - **Completed-Work Pricing and Included Execution Costs** (Instruction 8)
> - **Included Safety and Protection Costs** (Instruction 9)
> - **Overheads, Profit, Risks and Defect-Remedy Obligations** (Instruction 10)
> - **Accommodation, Insurance, Wages and Approval Costs** (Instruction 11)
> 
> 
> 
> - **Execution Standards and Engineer’s Directions** (Instruction 12)
> - **Incidental Removal Works Without Separate Payment** (Instruction 13)
> - **Temporary Relocation and Protection of Utilities** (Instruction 14)
> - **Temporary Works, Power and Supports at Contractor’s Cost** (Instruction 15)
> - **Permanent Supports and Restoration Payment Provisions** (Instruction 16)
> - **Balcony and Canopy Area at 50%; Chejjas Excluded from Payment** (Instruction 17)
> - **Demolition Depth and Refilling of Low-Level Areas** (Instruction 18)
> - **Removal Within the Line of Cut, Excluding Trees** (Instruction 19)
> - **Total Floor Area as the Sum of Built Areas of All Floors** (Instruction 20)
> - **Building Additions or Deletions and Accepted Percentage Rates** (Instruction 21)

### S212cc0e74fc3292f

[[OKF_bundle/Financial/vol4_secJ#2.0 — Abstract of Bill of Quantities (BOQ)|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8

> - **Schedule-A — Demolition and Dismantling**
>   - Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ
>   - **Estimated Cost:** INR 4,69,41,306.00
> 
> - **Schedule-B — KPWD Schedule-of-Rate Items**
>   - Items under Schedule of Rate published by KPWD
>   - **Estimated Cost:** INR 5,00,000.00
> 
> - **Total of Schedules A+B:** INR 4,74,41,306.00
> 
> - **Schedule-C — Salvage Credit to BMRCL**
>   - Credit for salvageable items from dismantled/demolished private properties in which the owner has no interest
>   - **Source Reference:** Para 15 of Part-3 of Employer’s Requirement
>   - **Estimated Cost Field:** `----`
>   - **Pricing Basis:** Lump-sum credit under Preamble Instruction 3

### S4bb84d1785d9399d

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF pp. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

> This section contains the financial document for BMRCL Tender No. `BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157`, covering the Letter of Price Bid, pricing instructions, BOQ abstract and work schedules.

### Jbed462ebb1fb6ea8

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/11`)

> {
>   "label": "12",
>   "pdf_pages": [
>     7
>   ],
>   "record_id": "vol4/pricing_preamble/12",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         71.99996948242188,
>         74.76317596435547,
>         526.3866577148438,
>         85.11869049072266
>       ],
>       "pdf_page": 7,
>       "text": "12. The work is to be executed as per Bill of Quantity description, Technical Specifications,"
>     },
>     {
>       "bbox": [
>         89.87928009033203,
>         88.44316864013672,
>         526.3867797851562,
>         98.7986831665039
>       ],
>       "pdf_page": 7,
>       "text": "specifications of MORTH, KPWD, CPWD, drawings, best engineering practices and/or"
>     },
>     {
>       "bbox": [
>         89.87926483154297,
>         102.12316131591797,
>         232.98648071289062,
>         112.47867584228516
>       ],
>       "pdf_page": 7,
>       "text": "as directed by the Engineer."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "12. The work is to be executed as per Bill of Quantity description, Technical Specifications,\nspecifications of MORTH, KPWD, CPWD, drawings, best engineering practices and/or\nas directed by the Engineer.",
>   "type": "pricing_rule"
> }

### J76eb6bf2592fa9ee

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/2`)

> {
>   "amount_inr_decimal": "47441306.00",
>   "amount_raw": "4,74,41,306.00",
>   "cell_clips": [
>     [
>       60.900000000000006,
>       368.74,
>       100.77,
>       401.54
>     ],
>     [
>       102.17,
>       368.74,
>       194.06,
>       401.54
>     ],
>     [
>       195.45999999999998,
>       368.74,
>       406.82,
>       401.54
>     ],
>     [
>       408.21999999999997,
>       368.74,
>       534.17,
>       401.54
>     ]
>   ],
>   "cells": [
>     "",
>     "",
>     "Total of Schedules (A+B)",
>     "4,74,41,306.00"
>   ],
>   "pdf_pages": [
>     8
>   ],
>   "record_id": "vol4/boq_abstract/A+B",
>   "review_status": "pending_manual_review",
>   "schedule": "A+B"
> }

### Jaf44a3c272fd15bf

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/1`)

> {
>   "amount_inr_decimal": "500000.00",
>   "amount_raw": "5,00,000.00",
>   "cell_clips": [
>     [
>       60.900000000000006,
>       330.94,
>       100.77,
>       367.34000000000003
>     ],
>     [
>       102.17,
>       330.94,
>       194.06,
>       367.34000000000003
>     ],
>     [
>       195.45999999999998,
>       330.94,
>       406.82,
>       367.34000000000003
>     ],
>     [
>       408.21999999999997,
>       330.94,
>       534.17,
>       367.34000000000003
>     ]
>   ],
>   "cells": [
>     "2",
>     "SCHEDULE-B",
>     "Items under Schedule of Rate published \nby KPWD",
>     "5,00,000.00"
>   ],
>   "pdf_pages": [
>     8
>   ],
>   "record_id": "vol4/boq_abstract/B",
>   "review_status": "pending_manual_review",
>   "schedule": "B"
> }

### J3b6ef5b6db6162f6

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 8 (`parsed_json/vol4/boq_abstract.json#/records/3`)

> {
>   "amount_inr_decimal": null,
>   "amount_raw": "----",
>   "amount_status": "Source placeholder; not a zero or submitted quote",
>   "cell_clips": [
>     [
>       60.900000000000006,
>       402.94,
>       100.77,
>       477.26
>     ],
>     [
>       102.17,
>       402.94,
>       194.06,
>       477.26
>     ],
>     [
>       195.45999999999998,
>       402.94,
>       406.82,
>       477.26
>     ],
>     [
>       408.21999999999997,
>       402.94,
>       534.17,
>       477.26
>     ]
>   ],
>   "cells": [
>     "3",
>     "SCHEDULE-C",
>     "Credit to BMRCL for salvageable items \nout of dismantled/demolished private \nproperties on which the owner has no \ninterest (as elaborated in Para 15 of Part-\n3 of ‘Employer’s Requirement’).",
>     "----"
>   ],
>   "pdf_pages": [
>     8
>   ],
>   "record_id": "vol4/boq_abstract/C",
>   "review_status": "pending_manual_review",
>   "schedule": "C"
> }

### Je67086ad8617857f

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1 row 13 (`parsed_json/boq/boq_workbook.json#/schedules/0`)

> {
>   "description": "SCHEDULE-A: Partial & Full demolition and dismantling work as per details given in Schedule-A of the BOQ",
>   "description_cell": "B13",
>   "estimated_cost_or_credit_label": {
>     "address": "F13",
>     "cell_type": "number",
>     "column": 6,
>     "formula_hidden_style": false,
>     "locked": true,
>     "number_format": "#,##0.00",
>     "row": 13,
>     "value": 46941306.0,
>     "xf_index": 167
>   },
>   "excel_row": 13,
>   "percentage_selection": {
>     "address": "N13",
>     "cell_type": "text",
>     "column": 14,
>     "formula_hidden_style": false,
>     "locked": false,
>     "number_format": "0.00%",
>     "row": 13,
>     "value": "Select",
>     "xf_index": 130
>   },
>   "quote_input": {
>     "address": "M13",
>     "cell_type": "formatted_blank",
>     "column": 13,
>     "formula_hidden_style": false,
>     "locked": false,
>     "number_format": "0.00",
>     "row": 13,
>     "value": "",
>     "xf_index": 143
>   },
>   "record_id": "boq/schedule_a",
>   "review_status": "pending_manual_review",
>   "saved_amount": {
>     "address": "BA13",
>     "cell_type": "number",
>     "column": 53,
>     "formula_hidden_style": false,
>     "locked": true,
>     "number_format": "0.00",
>     "row": 13,
>     "value": 0.0,
>     "xf_index": 173
>   },
>   "schedule": "A",
>   "sheet": "BoQ1"
> }

### Jad825d224737bbc4

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1 row 14 (`parsed_json/boq/boq_workbook.json#/schedules/1`)

> {
>   "description": "SCHEDULE-B: Items under Schedule of Rate published by KPWD",
>   "description_cell": "B14",
>   "estimated_cost_or_credit_label": {
>     "address": "F14",
>     "cell_type": "number",
>     "column": 6,
>     "formula_hidden_style": false,
>     "locked": true,
>     "number_format": "#,##0.00",
>     "row": 14,
>     "value": 500000.0,
>     "xf_index": 167
>   },
>   "excel_row": 14,
>   "percentage_selection": {
>     "address": "N14",
>     "cell_type": "text",
>     "column": 14,
>     "formula_hidden_style": false,
>     "locked": false,
>     "number_format": "0.00%",
>     "row": 14,
>     "value": "Select",
>     "xf_index": 130
>   },
>   "quote_input": {
>     "address": "M14",
>     "cell_type": "formatted_blank",
>     "column": 13,
>     "formula_hidden_style": false,
>     "locked": false,
>     "number_format": "0.00",
>     "row": 14,
>     "value": "",
>     "xf_index": 143
>   },
>   "record_id": "boq/schedule_b",
>   "review_status": "pending_manual_review",
>   "saved_amount": {
>     "address": "BA14",
>     "cell_type": "number",
>     "column": 53,
>     "formula_hidden_style": false,
>     "locked": true,
>     "number_format": "0.00",
>     "row": 14,
>     "value": 0.0,
>     "xf_index": 173
>   },
>   "schedule": "B",
>   "sheet": "BoQ1"
> }

### Jadc4a1acf83198bb

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 10 (`parsed_json/vol4/pricing_document.json#/pages/9`)

> {
>   "page_type": "text",
>   "pdf_page": 10,
>   "review_status": "pending_manual_review",
>   "text": " BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \n \n \n \nBangalore Metro Rail Corporation Ltd.                            September 2026 \nSection Page 7 of 7 \n \n                                                         Pricing document- Bill of Quantities (BOQ)\n \nSchedule - A \nItem \nNo. \nDescription of Item of work \nUnit \nQuantity  \nRate     \n(in Rs) \nTotal Amount   \n(In Rs) \nbrick work, fencing, stone slab wall, \nchain link fencing etc. disposal of \nunserviceable materials with all leads \nand lifts and stacking of serviceable \nmaterials, \nthe \nstacked \nserviceable \nmaterial shall be disposed of with all \nleads and lifts in which the property \nowner has no interest, removal of \nresulting debris with all lead and lifts \nand complete. \n4 \nDemolition/dismantling \nof \nsteel \nstructures \nsuch \nas \nsign \nboards, \nhoardings etc., of all heights, length and \nwidth \nby \nmechanical \nand \nmanual \nmethods. (Dismantled/released material \nto be handed over to the concerned \nauthority at the locations specified by \nowning \nauthority \nand \nremoval \nof \nresulting debris with all lead and lifts).  \nMT \n \n25 \n7518.00 \n1,87,950.00 \n \n                   Total of Schedule-A\n4,69,41,306.00\nSchedule-B \n \nITEMS UNDER SCHEDULE OF RATE \nPUBLISHED BY KPWD \n1 \nItems \nnot \ncovered \nin \nthe \nabove \nSchedule A to be executed under \nCommon SR for the year 2023-24 \npublished by Karnataka public Works \nDepartment \nwith \nissue \nrates \nand \namendments issued upto date of tender \nsubmission.  \nLump\nsum\n---------\n---------\n5,00,000.00\nTotal Schedule A+B\n4,74,41,306.00\n \n \n \n \n309\n",
>   "text_blocks": [
>     {
>       "bbox": [
>         14.760004043579102,
>         37.509437561035156,
>         519.9669799804688,
>         56.52032470703125
>       ],
>       "block_number": 0,
>       "text": " BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \n \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         62.5140495300293,
>         74.49351501464844,
>         69.48028564453125
>       ],
>       "block_number": 1,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         777.8273315429688,
>         74.38514709472656,
>         786.9194946289062
>       ],
>       "block_number": 2,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         802.54736328125,
>         525.8132934570312,
>         823.079833984375
>       ],
>       "block_number": 3,
>       "text": "Bangalore Metro Rail Corporation Ltd.                            September 2026 \nSection Page 7 of 7 \n \n"
>     },
>     {
>       "bbox": [
>         66.35997009277344,
>         75.12316131591797,
>         463.0339660644531,
>         85.47867584228516
>       ],
>       "block_number": 4,
>       "text": "                                                         Pricing document- Bill of Quantities (BOQ)\n"
>     },
>     {
>       "bbox": [
>         78.47997283935547,
>         97.32317352294922,
>         363.4272766113281,
>         107.6786880493164
>       ],
>       "block_number": 5,
>       "text": " \nSchedule - A \n"
>     },
>     {
>       "bbox": [
>         67.19996643066406,
>         129.48321533203125,
>         92.94723510742188,
>         139.83872985839844
>       ],
>       "block_number": 6,
>       "text": "Item \n"
>     },
>     {
>       "bbox": [
>         69.59996795654297,
>         129.48321533203125,
>         466.9871520996094,
>         152.55870056152344
>       ],
>       "block_number": 7,
>       "text": "No. \nDescription of Item of work \nUnit \nQuantity  \nRate     \n(in Rs) \n"
>     },
>     {
>       "bbox": [
>         475.1998291015625,
>         129.48321533203125,
>         555.30712890625,
>         139.83872985839844
>       ],
>       "block_number": 8,
>       "text": "Total Amount   \n"
>     },
>     {
>       "bbox": [
>         493.4397888183594,
>         142.20318603515625,
>         530.7070922851562,
>         152.55870056152344
>       ],
>       "block_number": 9,
>       "text": "(In Rs) \n"
>     },
>     {
>       "bbox": [
>         104.63995361328125,
>         171.48321533203125,
>         304.50909423828125,
>         295.7184143066406
>       ],
>       "block_number": 10,
>       "text": "brick work, fencing, stone slab wall, \nchain link fencing etc. disposal of \nunserviceable materials with all leads \nand lifts and stacking of serviceable \nmaterials, \nthe \nstacked \nserviceable \nmaterial shall be disposed of with all \nleads and lifts in which the property \nowner has no interest, removal of \nresulting debris with all lead and lifts \nand complete. \n"
>     },
>     {
>       "bbox": [
>         75.47997283935547,
>         304.443115234375,
>         304.5073547363281,
>         416.07855224609375
>       ],
>       "block_number": 11,
>       "text": "4 \nDemolition/dismantling \nof \nsteel \nstructures \nsuch \nas \nsign \nboards, \nhoardings etc., of all heights, length and \nwidth \nby \nmechanical \nand \nmanual \nmethods. (Dismantled/released material \nto be handed over to the concerned \nauthority at the locations specified by \nowning \nauthority \nand \nremoval \nof \nresulting debris with all lead and lifts).  \n"
>     },
>     {
>       "bbox": [
>         320.15985107421875,
>         304.443115234375,
>         339.067138671875,
>         314.7986145019531
>       ],
>       "block_number": 12,
>       "text": "MT \n"
>     },
>     {
>       "bbox": [
>         328.0798645019531,
>         323.1630859375,
>         331.14715576171875,
>         333.5185852050781
>       ],
>       "block_number": 13,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         375.1197814941406,
>         304.443115234375,
>         542.7108154296875,
>         314.7986145019531
>       ],
>       "block_number": 14,
>       "text": "25 \n7518.00 \n1,87,950.00 \n"
>     },
>     {
>       "bbox": [
>         63.23997497558594,
>         424.6830749511719,
>         549.6143188476562,
>         435.5185852050781
>       ],
>       "block_number": 15,
>       "text": " \n                   Total of Schedule-A\n4,69,41,306.00\n"
>     },
>     {
>       "bbox": [
>         276.119873046875,
>         444.9630432128906,
>         339.6651916503906,
>         455.31854248046875
>       ],
>       "block_number": 16,
>       "text": "Schedule-B \n"
>     },
>     {
>       "bbox": [
>         78.47997283935547,
>         464.4030456542969,
>         304.5071716308594,
>         487.3585510253906
>       ],
>       "block_number": 17,
>       "text": " \nITEMS UNDER SCHEDULE OF RATE \nPUBLISHED BY KPWD \n"
>     },
>     {
>       "bbox": [
>         75.47997283935547,
>         534.123046875,
>         84.66725158691406,
>         544.4785766601562
>       ],
>       "block_number": 18,
>       "text": "1 \n"
>     },
>     {
>       "bbox": [
>         104.63996887207031,
>         496.32305908203125,
>         304.50732421875,
>         582.5186157226562
>       ],
>       "block_number": 19,
>       "text": "Items \nnot \ncovered \nin \nthe \nabove \nSchedule A to be executed under \nCommon SR for the year 2023-24 \npublished by Karnataka public Works \nDepartment \nwith \nissue \nrates \nand \namendments issued upto date of tender \nsubmission.  \n"
>     },
>     {
>       "bbox": [
>         313.9198913574219,
>         496.2030334472656,
>         343.9411926269531,
>         506.55853271484375
>       ],
>       "block_number": 20,
>       "text": "Lump\n"
>     },
>     {
>       "bbox": [
>         321.35986328125,
>         508.802978515625,
>         344.0085144042969,
>         519.1585083007812
>       ],
>       "block_number": 21,
>       "text": "sum\n"
>     },
>     {
>       "bbox": [
>         374.7598571777344,
>         496.2030334472656,
>         549.6143188476562,
>         506.55853271484375
>       ],
>       "block_number": 22,
>       "text": "---------\n---------\n5,00,000.00\n"
>     },
>     {
>       "bbox": [
>         357.4798583984375,
>         591.2429809570312,
>         549.6143188476562,
>         601.9585571289062
>       ],
>       "block_number": 23,
>       "text": "Total Schedule A+B\n4,74,41,306.00\n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         611.282958984375,
>         75.06725311279297,
>         621.6384887695312
>       ],
>       "block_number": 24,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         523.3197021484375,
>         635.762939453125,
>         526.386962890625,
>         646.1184692382812
>       ],
>       "block_number": 25,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         660.4829711914062,
>         75.06725311279297,
>         670.8385009765625
>       ],
>       "block_number": 26,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         684.9629516601562,
>         75.06725311279297,
>         695.3184814453125
>       ],
>       "block_number": 27,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         546.0439453125,
>         24.479991912841797,
>         570.0199584960938,
>         41.38799285888672
>       ],
>       "block_number": 28,
>       "text": "309\n"
>     }
>   ]
> }

### Jd3c8d7b4ff66f4b1

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1 row 15 (`parsed_json/boq/boq_workbook.json#/schedules/2`)

> {
>   "description": "SCHEDULE-C: Credit to BMRCL for salvageable items out of dismantled/demolished private properties on which the owner has no interest (as elaborated in Para 15 of Part-3 of ‘Employer’s Requirement’).",
>   "description_cell": "B15",
>   "estimated_cost_or_credit_label": {
>     "address": "F15",
>     "cell_type": "text",
>     "column": 6,
>     "formula_hidden_style": false,
>     "locked": true,
>     "number_format": "#,##0.00",
>     "row": 15,
>     "value": "Credit to BMRCL in Lumpsum Amount",
>     "xf_index": 166
>   },
>   "excel_row": 15,
>   "percentage_selection": {
>     "address": "N15",
>     "cell_type": "formatted_blank",
>     "column": 14,
>     "formula_hidden_style": false,
>     "locked": true,
>     "number_format": "#,##0.00",
>     "row": 15,
>     "value": "",
>     "xf_index": 129
>   },
>   "quote_input": {
>     "address": "M15",
>     "cell_type": "formatted_blank",
>     "column": 13,
>     "formula_hidden_style": false,
>     "locked": false,
>     "number_format": "0.00",
>     "row": 15,
>     "value": "",
>     "xf_index": 131
>   },
>   "record_id": "boq/schedule_c",
>   "review_status": "pending_manual_review",
>   "saved_amount": {
>     "address": "BA15",
>     "cell_type": "number",
>     "column": 53,
>     "formula_hidden_style": false,
>     "locked": true,
>     "number_format": "0.00",
>     "row": 15,
>     "value": 0.0,
>     "xf_index": 162
>   },
>   "schedule": "C",
>   "sheet": "BoQ1"
> }

### J3f50dc005015beb7

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 9 (`parsed_json/vol4/pricing_document.json#/boq_items/0`)

> {
>   "amount_inr_decimal": "33963315.00",
>   "amount_inr_raw": "3,39,63,315.00",
>   "description": "Partial \ndemolition/dismantling \nby \nmechanical and manual methods of all \ntypes of structures of different heights \nconsisting of ground floor and/or more \nthan \none \nfloors, \n(RCC \nframed \nstructures, wall bearing structures with \nRCC roof. All other structures such as \nAC roof etc), comprising of cement \nconcrete, stone masonry, brick work, \nsteel \nwork, \nwood \nwork \netc.  \nDisposal of unserviceable materials with \nall leads and lifts and stacking of \nserviceable \nmaterials, \nthe \nstacked \nserviceable material shall be disposed \nof with all leads and lifts in which the \nproperty owner has no interest, removal \nof resulting debris with all lead and lifts, \nincluding \nnecessary \nstrengthening \nmethods for the buildings proposed for \ndemolition and also for neighbouring \nbuildings, complete in all respects.",
>   "fragments": [
>     {
>       "description": "Partial \ndemolition/dismantling \nby \nmechanical and manual methods of all \ntypes of structures of different heights \nconsisting of ground floor and/or more \nthan \none \nfloors, \n(RCC \nframed \nstructures, wall bearing structures with \nRCC roof. All other structures such as \nAC roof etc), comprising of cement \nconcrete, stone masonry, brick work, \nsteel \nwork, \nwood \nwork \netc.  \nDisposal of unserviceable materials with \nall leads and lifts and stacking of \nserviceable \nmaterials, \nthe \nstacked \nserviceable material shall be disposed \nof with all leads and lifts in which the \nproperty owner has no interest, removal \nof resulting debris with all lead and lifts, \nincluding \nnecessary \nstrengthening \nmethods for the buildings proposed for \ndemolition and also for neighbouring \nbuildings, complete in all respects.",
>       "pdf_page": 9,
>       "table_row": 2
>     }
>   ],
>   "item_number": "1",
>   "pdf_pages": [
>     9
>   ],
>   "quantity_decimal": "31245.00",
>   "quantity_raw": "31245.00",
>   "rate_inr_decimal": "1087.00",
>   "rate_inr_raw": "1087.00",
>   "record_id": "schedule_a/item_1",
>   "review_status": "pending_manual_review",
>   "schedule": "A",
>   "unit": "Sqm"
> }

### J56d5c0e99ab43b9b

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 9 (`parsed_json/vol4/pricing_document.json#/pages/8`)

> {
>   "page_type": "text",
>   "pdf_page": 9,
>   "review_status": "pending_manual_review",
>   "text": " BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \n \n \n \nBangalore Metro Rail Corporation Ltd.                            September 2026 \nSection Page 6 of 7 \n \n                                                         Pricing document- Bill of Quantities (BOQ)\n \nSchedule - A \nItem \nNo. \nDescription of Item of work \nUnit \nQuantity  \nRate     \n(in Rs) \nTotal Amount   \n(In Rs) \n1 \nPartial \ndemolition/dismantling \nby \nmechanical and manual methods of all \ntypes of structures of different heights \nconsisting of ground floor and/or more \nthan \none \nfloors, \n(RCC \nframed \nstructures, wall bearing structures with \nRCC roof. All other structures such as \nAC roof etc), comprising of cement \nconcrete, stone masonry, brick work, \nsteel \nwork, \nwood \nwork \netc.  \nDisposal of unserviceable materials with \nall leads and lifts and stacking of \nserviceable \nmaterials, \nthe \nstacked \nserviceable material shall be disposed \nof with all leads and lifts in which the \nproperty owner has no interest, removal \nof resulting debris with all lead and lifts, \nincluding \nnecessary \nstrengthening \nmethods for the buildings proposed for \ndemolition and also for neighbouring \nbuildings, complete in all respects. \nSqm \n31245.00 \n1087.00 \n3,39,63,315.00 \n2 \nFull \ndemolition/dismantling \nby \nmechanical and manual methods, of all \ntypes of structures of different heights \nconsisting of ground floor and/or more \nthan one floors (RCC framed structures, \nwall bearing structures with RCC roof. \nAll other structures such as AC roof \netc), comprising of cement concrete, \nstone masonry, brick work, steel work, \nwood work etc.          Disposal of \nunserviceable materials with all leads \nand lifts and stacking of serviceable \nmaterials, \nthe \nstacked \nserviceable \nmaterial shall be disposed of with all \nleads and lifts in which the property \nowner has no interest, removal of \nresulting debris with all lead and lifts, \nincluding \nnecessary \nstrengthening \nmethods for the buildings proposed for \ndemolition and also for neighbouring \nbuildings, complete in all respects. \nSqm \n21760.00 \n548.00 \n1,19,24,480.00 \n3 \nDemolition /dismantling compound walls \nof all shapes and heights by mechanical \nand manual methods, comprising of \ncement concrete, stone masonry work, \nRmt \n5183.00 \n167.00 \n8,65,561.00 \n308\n",
>   "text_blocks": [
>     {
>       "bbox": [
>         14.760004043579102,
>         37.509437561035156,
>         519.9669799804688,
>         56.52032470703125
>       ],
>       "block_number": 0,
>       "text": " BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157                                        Financial Document \n \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         62.5140495300293,
>         74.49351501464844,
>         69.48028564453125
>       ],
>       "block_number": 1,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         777.8273315429688,
>         74.38514709472656,
>         786.9194946289062
>       ],
>       "block_number": 2,
>       "text": " \n"
>     },
>     {
>       "bbox": [
>         71.99996948242188,
>         802.54736328125,
>         525.8132934570312,
>         823.079833984375
>       ],
>       "block_number": 3,
>       "text": "Bangalore Metro Rail Corporation Ltd.                            September 2026 \nSection Page 6 of 7 \n \n"
>     },
>     {
>       "bbox": [
>         66.35997009277344,
>         75.12316131591797,
>         463.0339660644531,
>         85.47867584228516
>       ],
>       "block_number": 4,
>       "text": "                                                         Pricing document- Bill of Quantities (BOQ)\n"
>     },
>     {
>       "bbox": [
>         78.47997283935547,
>         97.32317352294922,
>         363.4272766113281,
>         107.6786880493164
>       ],
>       "block_number": 5,
>       "text": " \nSchedule - A \n"
>     },
>     {
>       "bbox": [
>         67.19996643066406,
>         129.48321533203125,
>         92.94723510742188,
>         139.83872985839844
>       ],
>       "block_number": 6,
>       "text": "Item \n"
>     },
>     {
>       "bbox": [
>         69.59996795654297,
>         129.48321533203125,
>         466.9871520996094,
>         152.55870056152344
>       ],
>       "block_number": 7,
>       "text": "No. \nDescription of Item of work \nUnit \nQuantity  \nRate     \n(in Rs) \n"
>     },
>     {
>       "bbox": [
>         475.1998291015625,
>         129.48321533203125,
>         555.30712890625,
>         139.83872985839844
>       ],
>       "block_number": 8,
>       "text": "Total Amount   \n"
>     },
>     {
>       "bbox": [
>         493.4397888183594,
>         142.20318603515625,
>         530.7070922851562,
>         152.55870056152344
>       ],
>       "block_number": 9,
>       "text": "(In Rs) \n"
>     },
>     {
>       "bbox": [
>         75.47997283935547,
>         171.36322021484375,
>         307.6270446777344,
>         434.798583984375
>       ],
>       "block_number": 10,
>       "text": "1 \nPartial \ndemolition/dismantling \nby \nmechanical and manual methods of all \ntypes of structures of different heights \nconsisting of ground floor and/or more \nthan \none \nfloors, \n(RCC \nframed \nstructures, wall bearing structures with \nRCC roof. All other structures such as \nAC roof etc), comprising of cement \nconcrete, stone masonry, brick work, \nsteel \nwork, \nwood \nwork \netc.  \nDisposal of unserviceable materials with \nall leads and lifts and stacking of \nserviceable \nmaterials, \nthe \nstacked \nserviceable material shall be disposed \nof with all leads and lifts in which the \nproperty owner has no interest, removal \nof resulting debris with all lead and lifts, \nincluding \nnecessary \nstrengthening \nmethods for the buildings proposed for \ndemolition and also for neighbouring \nbuildings, complete in all respects. \n"
>     },
>     {
>       "bbox": [
>         312.2396545410156,
>         171.48321533203125,
>         550.392822265625,
>         181.83872985839844
>       ],
>       "block_number": 11,
>       "text": "Sqm \n31245.00 \n1087.00 \n3,39,63,315.00 \n"
>     },
>     {
>       "bbox": [
>         75.47997283935547,
>         443.5230407714844,
>         304.50909423828125,
>         706.9585571289062
>       ],
>       "block_number": 12,
>       "text": "2 \nFull \ndemolition/dismantling \nby \nmechanical and manual methods, of all \ntypes of structures of different heights \nconsisting of ground floor and/or more \nthan one floors (RCC framed structures, \nwall bearing structures with RCC roof. \nAll other structures such as AC roof \netc), comprising of cement concrete, \nstone masonry, brick work, steel work, \nwood work etc.          Disposal of \nunserviceable materials with all leads \nand lifts and stacking of serviceable \nmaterials, \nthe \nstacked \nserviceable \nmaterial shall be disposed of with all \nleads and lifts in which the property \nowner has no interest, removal of \nresulting debris with all lead and lifts, \nincluding \nnecessary \nstrengthening \nmethods for the buildings proposed for \ndemolition and also for neighbouring \nbuildings, complete in all respects. \n"
>     },
>     {
>       "bbox": [
>         316.7999267578125,
>         443.6430969238281,
>         550.39306640625,
>         453.99859619140625
>       ],
>       "block_number": 13,
>       "text": "Sqm \n21760.00 \n548.00 \n1,19,24,480.00 \n"
>     },
>     {
>       "bbox": [
>         75.47997283935547,
>         715.8029174804688,
>         304.50738525390625,
>         764.0784301757812
>       ],
>       "block_number": 14,
>       "text": "3 \nDemolition /dismantling compound walls \nof all shapes and heights by mechanical \nand manual methods, comprising of \ncement concrete, stone masonry work, \n"
>     },
>     {
>       "bbox": [
>         318.00018310546875,
>         715.8029174804688,
>         542.7114868164062,
>         726.158447265625
>       ],
>       "block_number": 15,
>       "text": "Rmt \n5183.00 \n167.00 \n8,65,561.00 \n"
>     },
>     {
>       "bbox": [
>         39.599998474121094,
>         24.479991912841797,
>         63.57600021362305,
>         41.38799285888672
>       ],
>       "block_number": 16,
>       "text": "308\n"
>     }
>   ]
> }

### Jb1c8db24c756e2db

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 9 (`parsed_json/vol4/pricing_document.json#/boq_items/1`)

> {
>   "amount_inr_decimal": "11924480.00",
>   "amount_inr_raw": "1,19,24,480.00",
>   "description": "Full \ndemolition/dismantling \nby \nmechanical and manual methods, of all \ntypes of structures of different heights \nconsisting of ground floor and/or more \nthan one floors (RCC framed structures, \nwall bearing structures with RCC roof. \nAll other structures such as AC roof \netc), comprising of cement concrete, \nstone masonry, brick work, steel work, \nwood work etc.          Disposal of \nunserviceable materials with all leads \nand lifts and stacking of serviceable \nmaterials, \nthe \nstacked \nserviceable \nmaterial shall be disposed of with all \nleads and lifts in which the property \nowner has no interest, removal of \nresulting debris with all lead and lifts, \nincluding \nnecessary \nstrengthening \nmethods for the buildings proposed for \ndemolition and also for neighbouring \nbuildings, complete in all respects.",
>   "fragments": [
>     {
>       "description": "Full \ndemolition/dismantling \nby \nmechanical and manual methods, of all \ntypes of structures of different heights \nconsisting of ground floor and/or more \nthan one floors (RCC framed structures, \nwall bearing structures with RCC roof. \nAll other structures such as AC roof \netc), comprising of cement concrete, \nstone masonry, brick work, steel work, \nwood work etc.          Disposal of \nunserviceable materials with all leads \nand lifts and stacking of serviceable \nmaterials, \nthe \nstacked \nserviceable \nmaterial shall be disposed of with all \nleads and lifts in which the property \nowner has no interest, removal of \nresulting debris with all lead and lifts, \nincluding \nnecessary \nstrengthening \nmethods for the buildings proposed for \ndemolition and also for neighbouring \nbuildings, complete in all respects.",
>       "pdf_page": 9,
>       "table_row": 3
>     }
>   ],
>   "item_number": "2",
>   "pdf_pages": [
>     9
>   ],
>   "quantity_decimal": "21760.00",
>   "quantity_raw": "21760.00",
>   "rate_inr_decimal": "548.00",
>   "rate_inr_raw": "548.00",
>   "record_id": "schedule_a/item_2",
>   "review_status": "pending_manual_review",
>   "schedule": "A",
>   "unit": "Sqm"
> }

### J9c0d0eea0a2aaeec

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF pp. 9, 10 (`parsed_json/vol4/pricing_document.json#/boq_items/2`)

> {
>   "amount_inr_decimal": "865561.00",
>   "amount_inr_raw": "8,65,561.00",
>   "description": "Demolition /dismantling compound walls \nof all shapes and heights by mechanical \nand manual methods, comprising of \ncement concrete, stone masonry work,\nbrick work, fencing, stone slab wall, \nchain link fencing etc. disposal of \nunserviceable materials with all leads \nand lifts and stacking of serviceable \nmaterials, \nthe \nstacked \nserviceable \nmaterial shall be disposed of with all \nleads and lifts in which the property \nowner has no interest, removal of \nresulting debris with all lead and lifts \nand complete.",
>   "fragments": [
>     {
>       "description": "Demolition /dismantling compound walls \nof all shapes and heights by mechanical \nand manual methods, comprising of \ncement concrete, stone masonry work,",
>       "pdf_page": 9,
>       "table_row": 4
>     },
>     {
>       "description": "brick work, fencing, stone slab wall, \nchain link fencing etc. disposal of \nunserviceable materials with all leads \nand lifts and stacking of serviceable \nmaterials, \nthe \nstacked \nserviceable \nmaterial shall be disposed of with all \nleads and lifts in which the property \nowner has no interest, removal of \nresulting debris with all lead and lifts \nand complete.",
>       "pdf_page": 10,
>       "table_row": 2
>     }
>   ],
>   "item_number": "3",
>   "pdf_pages": [
>     9,
>     10
>   ],
>   "quantity_decimal": "5183.00",
>   "quantity_raw": "5183.00",
>   "rate_inr_decimal": "167.00",
>   "rate_inr_raw": "167.00",
>   "record_id": "schedule_a/item_3",
>   "review_status": "pending_manual_review",
>   "schedule": "A",
>   "unit": "Rmt"
> }

### J9d5475ed2f3c7c6d

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 10 (`parsed_json/vol4/pricing_document.json#/boq_items/3`)

> {
>   "amount_inr_decimal": "187950.00",
>   "amount_inr_raw": "1,87,950.00",
>   "description": "Demolition/dismantling \nof \nsteel \nstructures \nsuch \nas \nsign \nboards, \nhoardings etc., of all heights, length and \nwidth \nby \nmechanical \nand \nmanual \nmethods. (Dismantled/released material \nto be handed over to the concerned \nauthority at the locations specified by \nowning \nauthority \nand \nremoval \nof \nresulting debris with all lead and lifts).",
>   "fragments": [
>     {
>       "description": "Demolition/dismantling \nof \nsteel \nstructures \nsuch \nas \nsign \nboards, \nhoardings etc., of all heights, length and \nwidth \nby \nmechanical \nand \nmanual \nmethods. (Dismantled/released material \nto be handed over to the concerned \nauthority at the locations specified by \nowning \nauthority \nand \nremoval \nof \nresulting debris with all lead and lifts).",
>       "pdf_page": 10,
>       "table_row": 3
>     }
>   ],
>   "item_number": "4",
>   "pdf_pages": [
>     10
>   ],
>   "quantity_decimal": "25",
>   "quantity_raw": "25",
>   "rate_inr_decimal": "7518.00",
>   "rate_inr_raw": "7518.00",
>   "record_id": "schedule_a/item_4",
>   "review_status": "pending_manual_review",
>   "schedule": "A",
>   "unit": "MT"
> }

### J2b6c7e3129c261f6

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BA$17 (`parsed_json/boq/boq_formulas.json#/formulas/18`)

> {
>   "address": "$BA$17",
>   "column": 53,
>   "formula": "=IF(ISBLANK(F17),0,IF(E17=\"Excess (+)\",ROUND(BA16+(BA16*F17),2),IF(E17=\"Less (-)\",ROUND(BA16+(BA16*F17*(-1)),2),0)))",
>   "has_array_formula": false,
>   "number_format": "0.0000",
>   "row": 17,
>   "sheet": "BoQ1"
> }

### J4a966f61d68d291f

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BC$17 (`parsed_json/boq/boq_formulas.json#/formulas/20`)

> {
>   "address": "$BC$17",
>   "column": 55,
>   "formula": "=SpellNumber(L17,BB17)",
>   "has_array_formula": false,
>   "number_format": "General",
>   "row": 17,
>   "sheet": "BoQ1"
> }

### J9a979874374a2792

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$C$18 (`parsed_json/boq/boq_formulas.json#/formulas/21`)

> {
>   "address": "$C$18",
>   "column": 3,
>   "formula": "=SpellNumberMC($E$2,BA16)",
>   "has_array_formula": false,
>   "number_format": "General",
>   "row": 18,
>   "sheet": "BoQ1"
> }

### Jccbc53a1c3e23834

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BB$17 (`parsed_json/boq/boq_formulas.json#/formulas/19`)

> {
>   "address": "$BB$17",
>   "column": 54,
>   "formula": "=ROUND(BA17,0)",
>   "has_array_formula": false,
>   "number_format": "0.0000",
>   "row": 17,
>   "sheet": "BoQ1"
> }

### Jfd74b52b70d7661d

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `BOQ_338417.xls`, workbook BoQ1!$BC$16 (`parsed_json/boq/boq_formulas.json#/formulas/17`)

> {
>   "address": "$BC$16",
>   "column": 55,
>   "formula": "=SpellNumberMC($E$2,BA16)",
>   "has_array_formula": false,
>   "number_format": "General",
>   "row": 16,
>   "sheet": "BoQ1"
> }

### Jb360bf15c6254704

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 6 (`parsed_json/vol4/pricing_clauses.json#/records/6`)

> {
>   "label": "7",
>   "pdf_pages": [
>     6
>   ],
>   "record_id": "vol4/pricing_preamble/7",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         72.00054931640625,
>         476.6429138183594,
>         526.3876342773438,
>         486.9984130859375
>       ],
>       "pdf_page": 6,
>       "text": "7. The method of measurement of completed work for payment shall be in accordance with"
>     },
>     {
>       "bbox": [
>         89.88085174560547,
>         490.3229064941406,
>         526.3883666992188,
>         500.67840576171875
>       ],
>       "pdf_page": 6,
>       "text": "the requirements as stated in the Technical Specifications and as given in the Price"
>     },
>     {
>       "bbox": [
>         89.88085174560547,
>         503.8829040527344,
>         417.6679382324219,
>         514.2384033203125
>       ],
>       "pdf_page": 6,
>       "text": "document- Bill of Quantities or elsewhere in the tender documents."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "7. The method of measurement of completed work for payment shall be in accordance with\nthe requirements as stated in the Technical Specifications and as given in the Price\ndocument- Bill of Quantities or elsewhere in the tender documents.",
>   "type": "pricing_rule"
> }

### Jd9bd6bab9dfee535

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/16`)

> {
>   "label": "17",
>   "pdf_pages": [
>     7
>   ],
>   "record_id": "vol4/pricing_preamble/17",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         71.99984741210938,
>         377.8829345703125,
>         526.3875732421875,
>         388.2384338378906
>       ],
>       "pdf_page": 7,
>       "text": "17. 50% area of Balcony and Canopy if exists will be considered for calculating area for"
>     },
>     {
>       "bbox": [
>         89.88016510009766,
>         391.44293212890625,
>         526.3853759765625,
>         401.7984313964844
>       ],
>       "pdf_page": 7,
>       "text": "payment as per the guide lines for valuation of properties. The area of chejjas or such"
>     },
>     {
>       "bbox": [
>         89.88016510009766,
>         405.1229248046875,
>         397.38720703125,
>         415.4784240722656
>       ],
>       "pdf_page": 7,
>       "text": "similar coverings/shadows will not be considered for payment."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "17. 50% area of Balcony and Canopy if exists will be considered for calculating area for\npayment as per the guide lines for valuation of properties. The area of chejjas or such\nsimilar coverings/shadows will not be considered for payment.",
>   "type": "pricing_rule"
> }

### Jdcdf13c0aabc9e14

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/17`)

> {
>   "label": "18",
>   "pdf_pages": [
>     7
>   ],
>   "record_id": "vol4/pricing_preamble/18",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         71.9998779296875,
>         424.80291748046875,
>         526.38720703125,
>         435.1584167480469
>       ],
>       "pdf_page": 7,
>       "text": "18. The demolition and dismantling shall be carried out up to ground and/or up to basement"
>     },
>     {
>       "bbox": [
>         89.88018035888672,
>         438.4828796386719,
>         526.3875732421875,
>         448.83837890625
>       ],
>       "pdf_page": 7,
>       "text": "level as the case may be including underground water storage structures if any. Refilling"
>     },
>     {
>       "bbox": [
>         89.88018035888672,
>         452.0428771972656,
>         472.6297912597656,
>         462.39837646484375
>       ],
>       "pdf_page": 7,
>       "text": "the low-level areas up to ground level is within the scope of contractor’s work."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "18. The demolition and dismantling shall be carried out up to ground and/or up to basement\nlevel as the case may be including underground water storage structures if any. Refilling\nthe low-level areas up to ground level is within the scope of contractor’s work.",
>   "type": "pricing_rule"
> }

### J7cf43a77f3241ea2

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/18`)

> {
>   "label": "19",
>   "pdf_pages": [
>     7
>   ],
>   "record_id": "vol4/pricing_preamble/19",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         72.00090026855469,
>         471.7228698730469,
>         526.3887329101562,
>         482.078369140625
>       ],
>       "pdf_page": 7,
>       "text": "19. The items existing excluding trees within the proposed line of cut have to be dismantled"
>     },
>     {
>       "bbox": [
>         89.8812026977539,
>         485.4028625488281,
>         382.74884033203125,
>         495.75836181640625
>       ],
>       "pdf_page": 7,
>       "text": "and demolished and debris to be transported and disposed."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "19. The items existing excluding trees within the proposed line of cut have to be dismantled\nand demolished and debris to be transported and disposed.",
>   "type": "pricing_rule"
> }

### J9c37cfe6c5cdd275

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/19`)

> {
>   "label": "20",
>   "pdf_pages": [
>     7
>   ],
>   "record_id": "vol4/pricing_preamble/20",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         72.00192260742188,
>         505.08282470703125,
>         526.3892211914062,
>         515.4383544921875
>       ],
>       "pdf_page": 7,
>       "text": "20. The total floor area means the summation of total built area of all floors in the buildings"
>     },
>     {
>       "bbox": [
>         89.8822250366211,
>         518.642822265625,
>         211.03143310546875,
>         528.9983520507812
>       ],
>       "pdf_page": 7,
>       "text": "indicated in Schedule A."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "20. The total floor area means the summation of total built area of all floors in the buildings\nindicated in Schedule A.",
>   "type": "pricing_rule"
> }

### Jd6b6e3ab9bef397d

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/20`)

> {
>   "label": "21",
>   "pdf_pages": [
>     7
>   ],
>   "record_id": "vol4/pricing_preamble/21",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         72.00222778320312,
>         538.2028198242188,
>         526.3898315429688,
>         548.558349609375
>       ],
>       "pdf_page": 7,
>       "text": "21. In case some buildings are deleted or added in BOQ, the rates per sqm for that"
>     },
>     {
>       "bbox": [
>         89.88249969482422,
>         552.7227783203125,
>         526.3902587890625,
>         563.0783081054688
>       ],
>       "pdf_page": 7,
>       "text": "deletion/addition will be same as given above. For payment purpose, the %age quoted"
>     },
>     {
>       "bbox": [
>         89.88249969482422,
>         567.2427978515625,
>         420.6696472167969,
>         577.5983276367188
>       ],
>       "pdf_page": 7,
>       "text": "and accepted in the Summary Cost will be used for the above rate."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "21. In case some buildings are deleted or added in BOQ, the rates per sqm for that\ndeletion/addition will be same as given above. For payment purpose, the %age quoted\nand accepted in the Summary Cost will be used for the above rate.",
>   "type": "pricing_rule"
> }

### Jafe6730cc94e67f7

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 10 (`parsed_json/vol4/pricing_document.json#/boq_items/4`)

> {
>   "amount_inr_decimal": "500000.00",
>   "amount_inr_raw": "5,00,000.00",
>   "description": "Items \nnot \ncovered \nin \nthe \nabove \nSchedule A to be executed under \nCommon SR for the year 2023-24 \npublished by Karnataka public Works \nDepartment \nwith \nissue \nrates \nand \namendments issued upto date of tender \nsubmission.",
>   "fragments": [
>     {
>       "description": "Items \nnot \ncovered \nin \nthe \nabove \nSchedule A to be executed under \nCommon SR for the year 2023-24 \npublished by Karnataka public Works \nDepartment \nwith \nissue \nrates \nand \namendments issued upto date of tender \nsubmission.",
>       "pdf_page": 10,
>       "table_row": 7
>     }
>   ],
>   "item_number": "1",
>   "pdf_pages": [
>     10
>   ],
>   "quantity_raw": "---------",
>   "rate_inr_raw": "---------",
>   "record_id": "schedule_b/item_1",
>   "review_status": "pending_manual_review",
>   "schedule": "B",
>   "unit": "Lump\nsum"
> }

### J6286c3376d46f205

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/12`)

> {
>   "label": "13",
>   "pdf_pages": [
>     7
>   ],
>   "record_id": "vol4/pricing_preamble/13",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         71.999267578125,
>         121.80315399169922,
>         526.3859252929688,
>         132.15867614746094
>       ],
>       "pdf_page": 7,
>       "text": "13. Removal of hoardings, interior lighting and interior furniture etc., ACP cladding and"
>     },
>     {
>       "bbox": [
>         89.87854766845703,
>         135.3631591796875,
>         526.3856201171875,
>         145.7186737060547
>       ],
>       "pdf_page": 7,
>       "text": "structural glazing etc., which are existing within the line of cut are incidental to work.  No"
>     },
>     {
>       "bbox": [
>         89.87853240966797,
>         149.04315185546875,
>         335.7059326171875,
>         159.39866638183594
>       ],
>       "pdf_page": 7,
>       "text": "separate payment will be considered for payment."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "13. Removal of hoardings, interior lighting and interior furniture etc., ACP cladding and\nstructural glazing etc., which are existing within the line of cut are incidental to work.  No\nseparate payment will be considered for payment.",
>   "type": "pricing_rule"
> }

### J3a4bdedbf4a7b7e6

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/13`)

> {
>   "label": "14",
>   "pdf_pages": [
>     7
>   ],
>   "record_id": "vol4/pricing_preamble/14",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         71.99853515625,
>         168.72314453125,
>         526.3860473632812,
>         179.0786590576172
>       ],
>       "pdf_page": 7,
>       "text": "14. If it is necessary to maintain any power, water or other utilities during demolition, such"
>     },
>     {
>       "bbox": [
>         89.87882232666016,
>         182.403076171875,
>         526.3866577148438,
>         192.7585906982422
>       ],
>       "pdf_page": 7,
>       "text": "lines shall be temporarily relocated, as necessary and protected before commencement"
>     },
>     {
>       "bbox": [
>         89.87883758544922,
>         195.96307373046875,
>         190.74612426757812,
>         206.31858825683594
>       ],
>       "pdf_page": 7,
>       "text": "of demolition work."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "14. If it is necessary to maintain any power, water or other utilities during demolition, such\nlines shall be temporarily relocated, as necessary and protected before commencement\nof demolition work.",
>   "type": "pricing_rule"
> }

### J181fa7ffc9bc4a10

[[OKF_bundle/Financial/vol4_secJ#Financial Document and Bill of Quantities|Financial Section J]], `Vol4DLNP1.pdf`, PDF p. 7 (`parsed_json/vol4/pricing_clauses.json#/records/15`)

> {
>   "label": "16",
>   "pdf_pages": [
>     7
>   ],
>   "record_id": "vol4/pricing_preamble/16",
>   "review_status": "pending_manual_review",
>   "source_document": "Vol4DLNP1.pdf",
>   "source_lines": [
>     {
>       "bbox": [
>         71.99887084960938,
>         289.92303466796875,
>         526.3864135742188,
>         300.2785339355469
>       ],
>       "pdf_page": 7,
>       "text": "16. If advised by the Consultant/BMRCL, the contractor has to give permanent supports like"
>     },
>     {
>       "bbox": [
>         89.87915802001953,
>         303.60302734375,
>         526.3859252929688,
>         313.9585266113281
>       ],
>       "pdf_page": 7,
>       "text": "wall, columns (Steel, RCC, etc.), including plastering, painting, plumbing, water supply"
>     },
>     {
>       "bbox": [
>         89.87914276123047,
>         317.16302490234375,
>         526.3861694335938,
>         327.5185241699219
>       ],
>       "pdf_page": 7,
>       "text": "and sanitary works, electrical restoration works, etc. to the supported portion of the"
>     },
>     {
>       "bbox": [
>         89.87914276123047,
>         330.8429870605469,
>         526.3868408203125,
>         341.198486328125
>       ],
>       "pdf_page": 7,
>       "text": "building before or after total/partial demolition, wherever necessary to maintain LOC, for"
>     },
>     {
>       "bbox": [
>         89.87914276123047,
>         344.5229797363281,
>         526.3902587890625,
>         354.87847900390625
>       ],
>       "pdf_page": 7,
>       "text": "which payment will be made as per  accepted rate in BoQ schedule for items available in"
>     },
>     {
>       "bbox": [
>         89.87914276123047,
>         358.2029724121094,
>         519.7941284179688,
>         368.5584716796875
>       ],
>       "pdf_page": 7,
>       "text": "Common SR for the year 2023-24 (Schedule of Rates),  for the execution of such work."
>     }
>   ],
>   "source_sha256": "d611ce86a28e84279e4cbbd66171d465a12d8e2efdaf37e6cac54cb5ee19246b",
>   "text": "16. If advised by the Consultant/BMRCL, the contractor has to give permanent supports like\nwall, columns (Steel, RCC, etc.), including plastering, painting, plumbing, water supply\nand sanitary works, electrical restoration works, etc. to the supported portion of the\nbuilding before or after total/partial demolition, wherever necessary to maintain LOC, for\nwhich payment will be made as per  accepted rate in BoQ schedule for items available in\nCommon SR for the year 2023-24 (Schedule of Rates),  for the execution of such work.",
>   "type": "pricing_rule"
> }

</details>

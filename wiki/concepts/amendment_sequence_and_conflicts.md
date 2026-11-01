---
type: concept
title: Amendment Sequence and Unresolved Source Conflicts
tender_no: BMRCL/Phase-3/JPN-MRS/Demolition/DLN-P1/2026/157
status: draft
review_status: pending_manual_review
generator: bmrcl-dynamic-wiki-v2
created_at: '2026-11-01T12:14:18+00:00'
updated_at: '2026-11-01T13:54:09+00:00'
last_ingested: '2026-11-01T12:14:18+00:00'
model: source-backed editorial synthesis; no API call
sources:
- OKF_bundle/Technical/Vol1/secA.md
- OKF_bundle/Technical/Vol1/secE.md
- OKF_bundle/Technical/Vol1/secG.md
- OKF_bundle/Technical/Vol3/vol3_appendices_instructions_forms.md
- OKF_bundle/Technical/Vol3/vol3_part1.md
- OKF_bundle/addendum_and_corrigendum/A_and_C1.md
- OKF_bundle/addendum_and_corrigendum/A_and_C3.md
- parsed_json/addendum_corrigendum/corrigenda_amendments.json
- parsed_json/vol1/section_a_nit/nit_items.json
- parsed_json/vol1/section_a_nit/nit_table.json
- parsed_json/vol1/section_e_gcc/contract_data_table.json
- parsed_json/vol1/section_g_forms/contract_forms.json
- parsed_json/vol3/forms/she_committee_forms.json
- parsed_json/vol3/part_1_she_management/she_management_clauses.json
claims:
- kind: summary
  text: This page brings together the cited requirements for amendment sequence and unresolved source conflicts. Each source statement retains its own stage, conditions and review limitations.
  evidence_ids:
  - Sc18621fd1b08f3e0
  - J981b70cc6e283023
  - Jcbe0f7287bb5da91
  - S69a6c3139d9e4c35
  - J6b36427c3b2760b1
  - S833aa656a16da78a
  - J827a319dc3712125
  - Jeb83d1b7a6d87fee
  - Jcc49f8beaf50a801
  - J9eeb4ca708ebff86
  - J6af8ef325f51b6bf
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C1e9ca2df5b17997f
  citations:
  - id: Sc18621fd1b08f3e0
    okf_path: OKF_bundle/Technical/Vol1/secA.md
    okf_sha256: 1d19d2821187107d8bead3c38cac38cb70cac496bf9b5b067362f9b891f92cfb
    heading: Key Detail 10 — Online Tender Submission
    source_document: Vol1DLNP1.pdf
    pdf_pages:
    - 7
    quote: '- **Submission Period:** 03.10.2026, from 10.00 AM, to 09.10.2026, up to 3.00 PM (IST).'
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  - id: J981b70cc6e283023
    okf_path: OKF_bundle/Technical/Vol1/secA.md
    okf_sha256: 1d19d2821187107d8bead3c38cac38cb70cac496bf9b5b067362f9b891f92cfb
    heading: Key Detail 10 — Online Tender Submission
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol1/section_a_nit/nit_items.json
    json_sha256: ffa851d3dc75c862bbb9df376985067951c7005c988fb0a1002a897b32525b6b
    json_pointer: /key_details/9
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"fragments\": [\n    {\n      \"pdf_page\": 7,\n      \"text\": \"10  Tender  submission  Date  and  Time  03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n         (online)                                3.00 PM) (IST)\"\n    }\n  ],\n  \"number\": 10,\n  \"review_status\": \"pending_manual_review\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_number_match
  - id: Jcbe0f7287bb5da91
    okf_path: OKF_bundle/Technical/Vol1/secA.md
    okf_sha256: 1d19d2821187107d8bead3c38cac38cb70cac496bf9b5b067362f9b891f92cfb
    heading: Key Detail 10 — Online Tender Submission
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol1/section_a_nit/nit_table.json
    json_sha256: e4e595fa155f932fe793f28df02a9836eb06f24ca4352db151622db258ce6b10
    json_pointer: /rows/9
    json_record_id: null
    source_review_status: pending_visual_review
    quote: "{\n  \"cell_bboxes\": [\n    [\n      70.54588003719554,\n      479.5196228027344,\n      95.63999938964844,\n      507.71961975097656\n    ],\n    [\n      95.63999938964844,\n      479.5196228027344,\n      284.63999938964844,\n      507.71961975097656\n    ],\n    [\n      284.63999938964844,\n      479.5196228027344,\n      525.6140926585477,\n      507.71961975097656\n    ]\n  ],\n  \"extracted_cells\": [\n    \"10\",\n    \"Tender  submission  Date  and  Time\\n(online)\",\n    \"03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n3.00 PM) (IST)\"\n  ],\n  \"number\": 10,\n  \"original_row_fragments\": [\n    {\n      \"pdf_page\": 7,\n      \"text\": \"10  Tender  submission  Date  and  Time  03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n         (online)                                3.00 PM) (IST)\"\n    }\n  ],\n  \"pdf_page\": 7,\n  \"requirement\": \"Tender  submission  Date  and  Time\\n(online)\",\n  \"review_status\": \"pending_visual_review\",\n  \"token_preservation_check\": \"passed\",\n  \"value\": \"03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n3.00 PM) (IST)\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_number_match
  - id: S69a6c3139d9e4c35
    okf_path: OKF_bundle/addendum_and_corrigendum/A_and_C1.md
    okf_sha256: 8b340a5039e27927eab4df9c9d385ebe89253a3c5e947647c885055e9c4277fd
    heading: Change 2 — Online Tender Submission Date and Time
    source_document: DLN_P1_AandC1_157.PDF
    pdf_pages:
    - 1
    quote: '- **Amends:** [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]]

      - **Change type:** Replace submission-window dates

      - **Old value:** 03.10.2026 from 10.00 AM to 09.10.2026 up to 3.00 PM IST

      - **New value:** 09.10.2026 from 10.00 AM to 15.10.2026 up to 3.00 PM IST

      - **Evidence:** `DLN_P1_AandC1_157.PDF`, PDF page 1, amendment serial 1

      - **Affected booklet page:** 001


      Both the opening date and closing date of the submission window change.'
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  - id: J6b36427c3b2760b1
    okf_path: OKF_bundle/addendum_and_corrigendum/A_and_C1.md
    okf_sha256: 8b340a5039e27927eab4df9c9d385ebe89253a3c5e947647c885055e9c4277fd
    heading: Change 2 — Online Tender Submission Date and Time
    source_document: DLN_P1_AandC1_157.PDF
    source_sha256: 26b25a4e3c3d3206635d0ddae6ce70c00e51468ebb4fe5d93f5e9d65902942d1
    pdf_pages:
    - 1
    sheet_cells: ''
    json_path: parsed_json/addendum_corrigendum/corrigenda_amendments.json
    json_sha256: 41af12b27292ebbdcf0de3bbd3c72bf1a52ac20ad7977041d1ed344c3240e712
    json_pointer: /amendments/0
    json_record_id: corrigendum_1/nit_key_detail_10
    source_review_status: pending_manual_review
    quote: "{\n  \"affected_reference\": \"Key Detail 10\",\n  \"affected_section\": \"NIT\",\n  \"booklet_page_reference\": \"001\",\n  \"corrigendum_number\": 1,\n  \"document_date\": \"2026-10-01\",\n  \"existing_selected_text\": \"03.10.2026 (From 10.00 AM) to 09.10.2026 (up to 3.00 PM) (IST)\",\n  \"field_provenance\": \"Prepared from visual inspection of the source scan; not automatically inferred from OCR\",\n  \"label\": \"Tender submission Date and Time (online)\",\n  \"ocr_evidence_relative_to_project\": \"output/corrigenda/ocr/run_20261030T051229372457Z/corrigendum_1/ocr.json\",\n  \"operation\": \"replace_date_time_fields\",\n  \"pdf_pages\": [\n    1\n  ],\n  \"printed_amendment_serial\": \"1\",\n  \"record_id\": \"corrigendum_1/nit_key_detail_10\",\n  \"replacement_selected_text\": \"09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)\",\n  \"review_status\": \"pending_manual_review\",\n  \"scope\": \"Date/time fields only; other wording, venue and submission conditions are retained in the source OCR\",\n  \"source_document\": \"DLN_P1_AandC1_157.PDF\",\n  \"source_sha256\": \"26b25a4e3c3d3206635d0ddae6ce70c00e51468ebb4fe5d93f5e9d65902942d1\",\n  \"transcription_scope\": \"Selected amendment wording and fields, not a complete verbatim table transcription\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: amendment_entry_navigation
  - id: S833aa656a16da78a
    okf_path: OKF_bundle/addendum_and_corrigendum/A_and_C3.md
    okf_sha256: d9cb8b7ff09a2dd9ff83e9ea35ba6330264539603a982a5daac47275ff44decb
    heading: Change 2 — Online Tender Submission Date and Time
    source_document: AandC3_DLN_P1_157.PDF
    pdf_pages:
    - 1
    quote: '- **Underlying NIT entry:** [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]]

      - **Change type:** Replace the submission-window closing date

      - **Old value:** 09.10.2026 from 10.00 AM to 15.10.2026 up to 3.00 PM IST

      - **New value:** 09.10.2026 from 10.00 AM to 23.10.2026 up to 3.00 PM IST

      - **Evidence:** `AandC3_DLN_P1_157.PDF`, PDF page 1, amendment serial 1

      - **Replaces:** Corrigendum 1, serial 1, Key Detail 10 date fields


      The opening date remains 09.10.2026. It is not changed to 16.10.2026.'
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  - id: J827a319dc3712125
    okf_path: OKF_bundle/addendum_and_corrigendum/A_and_C3.md
    okf_sha256: d9cb8b7ff09a2dd9ff83e9ea35ba6330264539603a982a5daac47275ff44decb
    heading: Change 2 — Online Tender Submission Date and Time
    source_document: AandC3_DLN_P1_157.PDF
    source_sha256: 623067baa7cb9d7b2863567fea861767f42102f9e16ff3c2b547afed554280de
    pdf_pages:
    - 1
    sheet_cells: ''
    json_path: parsed_json/addendum_corrigendum/corrigenda_amendments.json
    json_sha256: 41af12b27292ebbdcf0de3bbd3c72bf1a52ac20ad7977041d1ed344c3240e712
    json_pointer: /amendments/13
    json_record_id: corrigendum_3/nit_key_detail_10
    source_review_status: pending_manual_review
    quote: "{\n  \"affected_reference\": \"Key Detail 10\",\n  \"affected_section\": \"NIT\",\n  \"corrigendum_number\": 3,\n  \"document_date\": \"2026-10-13\",\n  \"existing_selected_text\": \"09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)\",\n  \"field_provenance\": \"Prepared from visual inspection of the source scan; not automatically inferred from OCR\",\n  \"label\": \"Tender submission Date and Time (online)\",\n  \"ocr_evidence_relative_to_project\": \"output/corrigenda/ocr/run_20261030T051229372457Z/corrigendum_3/ocr.json\",\n  \"operation\": \"replace_date_time_fields\",\n  \"pdf_pages\": [\n    1\n  ],\n  \"printed_amendment_serial\": \"1\",\n  \"printed_cross_reference\": \"Sl.No 1 of Addendum and Corrigendum No. 1 Dated 01-10-2026\",\n  \"record_id\": \"corrigendum_3/nit_key_detail_10\",\n  \"replacement_selected_text\": \"09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST)\",\n  \"replaces_record_id\": \"corrigendum_1/nit_key_detail_10\",\n  \"review_status\": \"pending_manual_review\",\n  \"scope\": \"Date/time fields only; other wording, venue and submission conditions are retained in the source OCR\",\n  \"source_document\": \"AandC3_DLN_P1_157.PDF\",\n  \"source_sha256\": \"623067baa7cb9d7b2863567fea861767f42102f9e16ff3c2b547afed554280de\",\n  \"transcription_scope\": \"Selected amendment wording and fields, not a complete verbatim table transcription\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: amendment_entry_navigation
  - id: Jeb83d1b7a6d87fee
    okf_path: OKF_bundle/Technical/Vol1/secE.md
    okf_sha256: d72224b0c08c509f8485b0d971bd10c690c5dace89c225ac4a8fcb0f9f2c9dad
    heading: General Conditions of Contract and Contract Data
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 143
    sheet_cells: ''
    json_path: parsed_json/vol1/section_e_gcc/contract_data_table.json
    json_sha256: c50606c1aae8c00241df233c1dca694aab3deefbb1a6d2156b880f44beae0938
    json_pointer: /items/10
    json_record_id: null
    source_review_status: pending_visual_review
    quote: "{\n  \"cell_bboxes\": [\n    [\n      72.21599807739258,\n      99.359619140625,\n      104.15999603271484,\n      146.27963256835938\n    ],\n    [\n      104.15999603271484,\n      99.359619140625,\n      256.3199920654297,\n      146.27963256835938\n    ],\n    [\n      256.3199920654297,\n      99.359619140625,\n      568.2239837646484,\n      146.27963256835938\n    ]\n  ],\n  \"item_number\": 12,\n  \"pdf_page\": 143,\n  \"raw_cells\": [\n    \"12\",\n    \"Defects Liability Period\\n\\n(GCC Sub-Clause 10)\",\n    \"Defects Liability Period is 6 months from the date of Taking over\\nmentioned in Taking Over Certificates being issued for whole of\\nthe work.\"\n  ],\n  \"requirement\": \"Defects Liability Period\\n\\n(GCC Sub-Clause 10)\",\n  \"review_status\": \"pending_visual_review\",\n  \"source_row_label\": \"12\",\n  \"table_bbox\": [\n    72.21599807739258,\n    46.2596435546875,\n    568.2239837646484,\n    476.3396186828613\n  ],\n  \"value\": \"Defects Liability Period is 6 months from the date of Taking over\\nmentioned in Taking Over Certificates being issued for whole of\\nthe work.\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jcc49f8beaf50a801
    okf_path: OKF_bundle/Technical/Vol1/secG.md
    okf_sha256: 78eac979b2d8f01921b45df904f4bb99ae14aed1895d97a7853eb017c3ed315c
    heading: Contract Form 1 — Contract Agreement
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 147
    - 148
    - 149
    - 150
    sheet_cells: ''
    json_path: parsed_json/vol1/section_g_forms/contract_forms.json
    json_sha256: 41670e8866feba3a9ff42e73f2e1da67ed58b020778fce98ad11cf7bc8e2571f
    json_pointer: /forms/0
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"document_role\": \"template\",\n  \"form_id\": \"contract_form_1\",\n  \"form_number\": \"1\",\n  \"fragments\": [\n    {\n      \"pdf_page\": 147,\n      \"text\": \"CONTRACT FORM- 1\\n\\n\\n                      CONTRACT AGREEMENT\\n\\n       This Contract Agreement (hereinafter called the “Contract”) is made at Bangalore on ……..…day of\\n\\n    ……………by and between:\\n\\n       Bangalore Metro Rail Corporation Limited, a company incorporated under companies act 1956\\n       represented by the Managing Director, with office located at  III Floor, BMTC Complex, K.H.Road,\\n        Shantinagar, Bangalore 560 027, hereinafter referred to as the “BMRCL” or the “Employer”, as the\\n       case may be, which expression shall unless excluded by or repugnant to the context or meaning thereof\\n      be deemed to include its successors and assigns of the one part, and;\\n\\n          .........................................................…………………….. [Note 1] comprising:\\n\\na)          ........................................................,  a  company  registered  and  existing  under  the  laws  of\\n\\n             ................................, with head office located at ........................................................, represented by\\n\\n       Mr.  ....................................... and Mr.  ....................................... authorised  to sign and bind the\\n\\n       company, under the Power of Attorney  dated...................................... and the Board Resolution\\n\\n            dated..................................... [Note 5] AND\\n\\nb)          ........................................................,  a  company  registered  and  existing  under  the  laws  of\\n\\n             ................................, with head office located at................................................................ represented\\n\\n       by Mr.  ....................................... and Mr.  ....................................... authorised to sign and bind the\\n\\n       company, under the Power of Attorney  dated...................................... and the Board Resolution\\n\\n            dated..................................... [Note 5] AND\\n\\nc)          ........................................................,  a  company  registered  and  existing  under  the  laws  of\\n\\n             ................................, with head office located at................................................................ represented\\n\\n       by Mr.  ....................................... and Mr.  ....................................... authorised to sign and bind the\\n\\n       company, under the Power of Attorney  dated...................................... and the Board Resolution\\n\\n            dated..................................... [Note 5]\\n\\n\\n\\n       [Note 2] who each of which shall be jointly and severally responsible to the Employer under the Contract\\n         for the Bangalore Metro Rail Project as per conditions agreed to by the Employer;\\n\\n\\n        Hereinafter [Note 3] collectively referred to as the “Contractor” which expression shall unless excluded\\n       by or repugnant to the context or meaning thereof be deemed to include its successors and assigns of\\n        the other part.\\n\\n\\n     WHEREAS the Contractor has established a ........................[Note 4] in accordance with Indian law and\\n        offered a tender for the construction of a rail based mass rapid transport system by execution and\\n        completion, and remedying any defects in the Works of:(Name of the work)----------------------------------\\n           ------------------------------------------------------------------------------------------------------------------------------\\n\\n      Tender Notification No ---------------------------------------------------- Dated --.--. ----. and agrees to undertake\\n       performance of the Work under the terms and conditions set forth in this Contract.\\n\\n\\n     AND WHEREAS the Employer agrees to hire and the Contractor agrees to be hired to implement\\n       the:(Name of the work)-------------------------------------------------------------------------------------------------------\\n           ---------------------------------------------------------\\n\\n       Tender Notification No ---------------------------------------------------- Dated --.--. ----.\\n\\n       Under the terms and conditions specified  in  this Contract Agreement and the other Contract\\n       Documents.\\n     Now THEREFORE the parties hereby agree as follows:\"\n    },\n    {\n      \"pdf_page\": 148,\n      \"text\": \"Clause 1 Words and Expression\\n\\n             In this Contract all the words and expressions shall have the same meanings as are respectively\\n           assigned to them in the conditions of contract hereinafter referred to,\\n\\n   Clause 2  the Contract Documents,\\n\\n          The following shall deem to form and be read and construed as a part of this Contract Agreement\\n\\n            provided any of the provisions therein are not inconsistent with the present contract agreement:\\n              1.  Letter of Acceptance.\\n\\n              2.  Clarifications, Addenda, Corrigenda Issued to Tender document (if any)\\n\\n              3.  Pricing Document\\n\\n              4.  Special Conditions of Contract\\n\\n              5.  Contract forms\\n\\n              6.  General Conditions of Contract\\n\\n              7.  Employer’s Requirement & Technical Specifications\\n\\n              8.  Drawings\\n\\n              9.  Any other document forming part of the Contract\\n\\n               All of the foregoing documents, together with this Contract Agreement, referred to herein as the\\n            Contract.  Also incorporated into the Contract, and made part hereof, are  all Standard codes,\\n             specifications of MORTH/CPWD/KPWD/IRS as applicable, and similar requirements that are referred\\n             to therein. The ‘Priority of documents’ will be as given in clause 1.5 of GCC.\\n\\n   Clause 3 Obligations of the Contractor:\\n\\n         The mutual rights and Obligations of the Employer and the Contractor shall be as set forth in the\\n            contract and in particular: -\\n\\n           3.1 The Contractor agrees, subject to the terms and conditions of the Contract, to perform efficiently\\n          and faithfully all of the work of (Name of the work)-------------------------------------------------------------------\\n                ---------------------------------------------------------------------------------------------\\n\\n          Tender Notification No  ---------------------------------------------------- Dated  --.--. ----.and other  facilities\\n             requisite for or incidental to the successful completion of the Works and in carrying out all duties and\\n            obligations imposed by the Contract.\\n\\n\\n            3.2 The Contractor shall remedy, at no extra cost to the Employer, the defect or failure (fair wear and\\n             tear excluded) after any part of the Work are taken over by the Employer until the end of Defects\\n               Liability Period.\\n\\n            3.3 The Contractor shall also remedy, at no extra cost to the Employer, the defect or failure of any\\n           equipment provided in the Works and any defects in materials supplied and workmanship up to end\\n             of warranty period.\\n\\n   Clause 4 Obligations of the Employer:\\n\\n         The Employer agrees, subject to the terms and conditions of the Contract, to pay the Contractor the\\n         amount specified, and at the rates and terms and in the manner set forth in the Contract.\\n\\n   Clause 5 Contract Price:\\n\\n             5.1. Employer agrees to pay the Contractor total amount mentioned below (hereinafter called 'the\\n            Contract Price') and the Contractor agrees to accept the total amount mentioned below for the\\n            execution, completion, maintenance / rectification of defects and guarantee for the works carried out\\n          by him as part of his obligations, responsibilities and liabilities under and according to the provisions\\n          and obligations imposed on him by the Contract.\\n\\n\\n\\n                    (i)      Indian Rupees……………………………………...  (....................................Rs.) and Output\\n\\n              GST as applicable.\"\n    },\n    {\n      \"pdf_page\": 149,\n      \"text\": \"5.2. The contract price mentioned above  will be increased or decreased during the period of\\n        performance of the contract as specifically provided,  if any, in the General or Special Conditions of\\n         Contract and no additional amount for any other account whatsoever shall be payable to the Contractor.\\n\\n Clause 6 Completion Time:\\n\\n       The Contractor shall complete whole of the Works within.............................. (.........) months from the\\n       Commencement Date (date of signing the ‘Contract Agreement’). The Defect Liability Period is 12\\n         (Twelve) months from the date mentioned in the Final Taking over Certificate for whole of the Works.\\n\\n Clause7 Integration\\n\\n       The Employer and the Contractor agree that this Contract Agreement, together with the other Contract\\n        Documents, expresses all of the agreements, understandings, promises, and covenants of the parties,\\n        and  integrates,  combines,  and  supersedes   all  prior  and  contemporaneous  negotiations,\\n         understandings, and agreements, whether written or oral and no modification or alteration of the\\n         Contract Documents shall be valid or binding on either party, unless expressed in writing and executed\\n          with the same formality as this Contract Agreement, except as may otherwise be specifically provided\\n           in the Contract Documents.\\n\\n Clause 8 Governing Law\\n\\n         This Contract is enforceable and construed under the applicable laws of the Republic of India.\\n\\n Clause 9 Language\\n\\n         This Contract Agreement and the other Contract Documents are made in the English language.\\n\\nClause 9-A Notices:\\n\\n       The Address for service of all documents / notices arising out of or in connection with this contract\\n          shall be:\\n           (a) Upon Employer: Bangalore Metro Rail Corporation Ltd, 3rd Floor, BMTC Complex, K.H. Road,\\n             Shantinagar, Bengaluru – 560027, Karnataka, India.\\n           Marked for the attention of Executive Director.\\n           (b) Upon the Contractor: --------------------------------------------------------------------(Name and address of\\n              the contractor)\\n           The above notices can be sent either by E-mail to the respective E-mail addresses of the parties\\n              or by registered post to the above mentioned addresses of the parties.\\n\\n Clause 10 Jurisdiction of Court\\n\\n       The Courts at Bangalore shall have the exclusive jurisdiction in respect of all the disputes arising out\\n          of this Agreement between the parties.\\n\\n\\n        IN WITNESS WHEREOF, the parties hereto have caused this Contract to be signed in their respective\\n\\n       names by their authorised representatives as of the day and year first above written\\n\\n                  For BMRCL                       [Note 6] for …………...................,\\n              The Employer                       The Contractor\\n              Bangalore Metro Rail                           (a) …………………………………….\\n                Corporation Limited                  …………………………………….\\n\\n\\n\\n                      (                         )                                    (                         )\\n                       --------------------------                                     --------------------------\\n\\n\\n               WITNESS\\n\\n\\n                                                               (b) For …………………………………….\\n                      (                         )              ……………………………\\n                       --------------------------\"\n    },\n    {\n      \"pdf_page\": 150,\n      \"text\": \"(                         )\\n                                                                                         --------------------------\\n\\n\\n                                                                           (c) …………………………………….\\n                              ……………………………\\n\\n\\n\\n                                                                                         (                         )\\n                                                                                         --------------------------\\n\\n\\n\\n\\n\\n                                                          WITNESS\\n\\n\\n\\n                                                                                               (                      )\\n                                                                                             --------------------------\\n\\n\\n\\n\\n\\n   Notes:  (for preparation of but not for inclusion in the engrossment of the Contract Agreement)\\n\\n   1           If the Contractor comprises a partnership, joint venture, liability will be joint and several, and each\\n\\n         member thereof must be identified.\\n\\n    2.       In the case that the Contractor comprises a single company, this line should be deleted entirely, as\\n\\n            also should be paragraphs (b) and (c) above.\\n\\n    3.       In the case that the Contractor comprises a single company, the word “collectively” should be deleted\\n\\n           from this line.\\n\\n    4.      Enter the appropriate nature of the Contractor; company, partnership, joint venture as the case may\\n\\n           be.\\n\\n    5.      Enter the date of the appropriate resolution.\\n\\n    6.          If the Contractor comprises a partnership, joint venture, each member thereof must execute.\\n\\n    7.     The required Stamp duty in accordance with Karnataka Stamp Act is to be borne by the contractor.\"\n    }\n  ],\n  \"heading_line\": \"CONTRACT FORM- 1\",\n  \"review_status\": \"pending_manual_review\",\n  \"title\": \"Contract Agreement\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_form_number_match
  - id: J9eeb4ca708ebff86
    okf_path: OKF_bundle/Technical/Vol3/vol3_part1.md
    okf_sha256: 6d3d536a7bdd68a40c05a233955b27e65e857ce6f72b9f0e755914d9adb85df6
    heading: Clause 7.0 — Contractor SHE Committee
    source_document: Vol3DLNP1.pdf
    source_sha256: 1ee3fc8dfd12f659f34446b0a6db74e1e1cdd4d593ca91b2a48d59bf1ef97d52
    pdf_pages:
    - 17
    - 18
    - 19
    sheet_cells: ''
    json_path: parsed_json/vol3/part_1_she_management/she_management_clauses.json
    json_sha256: b017881487993483cddcb5c17ffd7e2c6898a21f9463d8fab51b9e05d5e0a9df
    json_pointer: /clauses/6
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"clause_id\": \"7.0\",\n  \"fragments\": [\n    {\n      \"pdf_page\": 17,\n      \"text\": \"7.0      Contractor SHE Committee\\n\\n\\n          7.1         All employees should be  able  to  participate  in the making and monitoring  of\\n                  arrangements for safety, industrial health and environment at their place of work. The\\n                   establishment of site SHE committees in which employees and Contractor and sub-\\n                     contractor  management  are  represented  can  increase  the  involvement  and\\n                 commitment of employees. The contractor shall ensure the formation and monitor the\\n                     functioning of contractor SHE committees.\\n\\n\\n          7.2      Terms of Reference\\n\\n\\n          7.2.1    The Terms of Reference for the committee shall be as follows;\\n\\n\\n                                 i)    To establish company safety policies and practices\\n\\n                                    ii)   To monitor the adequacy of the contractor’s site SHE plan and ensure  its\\n                        implementation\\n\\n                                     iii)   To review SHE training\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"text\": \"iv)   To review the contractor’s monthly SHE report.\\n\\n           v)   To identify probable causes of accident and unsafe practices in building or other\\n                construction work and to suggest remedial measures.\\n\\n             vi)   To stimulate interest of Employer and building workers in safety by organizing\\n                safety week, safety competition, talks and film-shows on safety, preparing\\n               posters or taking similar other measures as and when required or as necessary.\\n\\n              vii)  To go round the construction site with a view to check unsafe practices and\\n                detect unsafe  conditions and  to recommend remedial measures  for  their\\n                  rectifications including first-aid medical and welfare facilities.\\n\\n               viii)  Committee team members should perform a  site inspection before every\\n              committee meetings and to monitor SHE inspection reports.\\n\\n             ix)   To bring to the notice of the Employer the hazards associated with use, handling\\n             and maintenance of the equipment used during the course of building and other\\n                construction work\\n\\n           x)   To suggest measures for improving welfare amenities in the construction site\\n             and other miscellaneous aspect of safety, health and welfare in building or other\\n                construction work.\\n\\n             xi)   To look into the health hazards associated with handling different types of\\n                explosives, chemicals and other construction materials and to suggest remedial\\n             measures including personal protective equipment.\\n\\n              xii)  To review the last safety committee meeting minutes and to take action against\\n               persons/sub-contractors for non-compliance if any.\\n\\n\\n7.3       Within 14 days of award of contract, the SHE committee shall be constituted and\\n           notification regarding the same shall be communicated to the members and employees\\n         as per the format provided in Form No.: SF 001\\n\\n\\n7.4       Site SHE Committee meeting shall be conducted at least once in a month with the\\n        minimum members listed below:\\n\\n         Chairman           Project Manager\\n\\n           Secretary       SHE Manager (In-charge)\\n        Members                     i)   Labour Welfare Officer\\n                                                           ii)   In charge of plant and machinery\\n                                                            iii)  In charge of site electrics\\n                                           iv)  In charge of stores.\\n                                    v)  Senior  Managers/  Engineers  heading   different  sub\\n                                        functions.\\n                                           vi)  Sub – contractor’s representative\\n                                               vii) Labour Contractor’s representative\\n                                                  viii) Workers’ representative\\n                                           ix)  Co-contractor representative.\\n                                    x)  SHE staffs\\n          Employer’s\\n                   BMRC SHE in charge and other representatives\\n          Representatives\\n\\n\\n 7.5    Construction SHE Committee meeting shall be conducted at least once in a week with the\\n      minimum members listed below:\\n\\n    Chairman  Project Manager\\n\\n     Secretary  SHE Manager (In-charge)\\n    Members     i)   Labour Welfare Officer\\n                               ii)   In charge of plant and machinery\\n                               iii)  In-charge of site electricity\\n                      iv)  Senior Managers / Engineers heading different sub functions\\n                   v)   Sub- Contractor’s representative\\n                      vi)  Labour contractor’s representative\\n                         vii)  Workers’ representatives\\n                          viii)  All SHE Staffs\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"text\": \"7.6      Co-contractors’ participation\\n\\n\\n          7.6.1      In case of depot, station and other contiguous areas where more than one main\\n                    contractors are working together, the Employer shall instruct the other contractors to\\n                        join for the monthly SHE committee meeting of the main civil contractor, so as to\\n                   discuss and decide about the common provision of security, lighting, toilet, drinking\\n                   water etc. and sharing the maintenance cost of the same etc.\\n\\n\\n          7.6.2    The general principle for sharing the cost shall be either based on the contract\\n                  value of works executed at the contiguous area or the daily average number of\\n               workmen employed by each contractor in the contiguous area.\\n\\n\\n          7.7     Minimum time between two monthly SHE Committee meetings\\n\\n\\n          7.7.1    A minimum period of 21 days shall be maintained between any two SHE monthly\\n                  committee meetings.\\n\\n\\n          7.8     Agenda\\n\\n\\n          7.8.1    The Secretary shall circulate the agenda of the meeting at least seven working days in\\n                 advance of the scheduled date of the meeting to all members.\\n\\n\\n          7.8.2    The agenda should broadly cover the following:\\n\\n\\n                                 i)     Confirmation of minutes\\n\\n                                    ii)    Chairman’s review/overview of site SHE performance / condition\\n\\n                                     iii)    Previous month SHE statistics\\n\\n                          iv)    Incident and Accident Investigation / dangerous occurrence / near miss report\\n\\n                      v)    Site SHE inspection\\n\\n                          vi)    Sub-contractors’ SHE issues\\n\\n                             vii)   Safety presentation by Members\\n\\n                               viii)  Report from Employer\\n\\n                          ix)   Matters arising\\n\\n                      x)   Any other business\\n\\n\\n          7.9      Minutes of the meeting\\n\\n\\n          7.9.1    The Minutes of the meeting shall be prepared as per the format provided at Form\\n                   No.: SF- 002 and sent to all members within 2 working days preferably by mail/fax\\n                    followed by hardcopy. Safety Committee meeting minutes shall also be displayed in\\n                    the notice board for wider publicity to all concerned.\\n\\n\\n          7.10     Disciplinary Action\\n\\n\\n          7.10.1   The chairman shall inform the members of any outstanding issues in the meeting and\\n                        in case of repeated offence/ non-compliance by some members or other co/sub\\n                    contractors and propose suitable disciplinary action including provisions of monitory\\n                    penalty as per the relevant contract clauses, the Employer shall ensure that the same\\n                          is implemented.\"\n    }\n  ],\n  \"heading_line\": \"          7.0      Contractor SHE Committee\",\n  \"retained_lines\": [\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 54,\n      \"text\": \"          7.0      Contractor SHE Committee\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 55,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 56,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 57,\n      \"text\": \"          7.1         All employees should be  able  to  participate  in the making and monitoring  of\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 58,\n      \"text\": \"                  arrangements for safety, industrial health and environment at their place of work. The\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 59,\n      \"text\": \"                   establishment of site SHE committees in which employees and Contractor and sub-\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 60,\n      \"text\": \"                     contractor  management  are  represented  can  increase  the  involvement  and\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 61,\n      \"text\": \"                 commitment of employees. The contractor shall ensure the formation and monitor the\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 62,\n      \"text\": \"                     functioning of contractor SHE committees.\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 63,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 64,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 65,\n      \"text\": \"          7.2      Terms of Reference\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 66,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 67,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 68,\n      \"text\": \"          7.2.1    The Terms of Reference for the committee shall be as follows;\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 69,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 70,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 71,\n      \"text\": \"                                 i)    To establish company safety policies and practices\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 72,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 73,\n      \"text\": \"                                    ii)   To monitor the adequacy of the contractor’s site SHE plan and ensure  its\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 74,\n      \"text\": \"                        implementation\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 75,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 76,\n      \"text\": \"                                     iii)   To review SHE training\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 77,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 78,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 79,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 3,\n      \"text\": \"             iv)   To review the contractor’s monthly SHE report.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 4,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 5,\n      \"text\": \"           v)   To identify probable causes of accident and unsafe practices in building or other\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 6,\n      \"text\": \"                construction work and to suggest remedial measures.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 7,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 8,\n      \"text\": \"             vi)   To stimulate interest of Employer and building workers in safety by organizing\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 9,\n      \"text\": \"                safety week, safety competition, talks and film-shows on safety, preparing\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 10,\n      \"text\": \"               posters or taking similar other measures as and when required or as necessary.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 11,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 12,\n      \"text\": \"              vii)  To go round the construction site with a view to check unsafe practices and\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 13,\n      \"text\": \"                detect unsafe  conditions and  to recommend remedial measures  for  their\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 14,\n      \"text\": \"                  rectifications including first-aid medical and welfare facilities.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 15,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 16,\n      \"text\": \"               viii)  Committee team members should perform a  site inspection before every\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 17,\n      \"text\": \"              committee meetings and to monitor SHE inspection reports.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 18,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 19,\n      \"text\": \"             ix)   To bring to the notice of the Employer the hazards associated with use, handling\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 20,\n      \"text\": \"             and maintenance of the equipment used during the course of building and other\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 21,\n      \"text\": \"                construction work\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 22,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 23,\n      \"text\": \"           x)   To suggest measures for improving welfare amenities in the construction site\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 24,\n      \"text\": \"             and other miscellaneous aspect of safety, health and welfare in building or other\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 25,\n      \"text\": \"                construction work.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 26,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 27,\n      \"text\": \"             xi)   To look into the health hazards associated with handling different types of\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 28,\n      \"text\": \"                explosives, chemicals and other construction materials and to suggest remedial\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 29,\n      \"text\": \"             measures including personal protective equipment.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 30,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 31,\n      \"text\": \"              xii)  To review the last safety committee meeting minutes and to take action against\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 32,\n      \"text\": \"               persons/sub-contractors for non-compliance if any.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 33,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 34,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 35,\n      \"text\": \"7.3       Within 14 days of award of contract, the SHE committee shall be constituted and\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 36,\n      \"text\": \"           notification regarding the same shall be communicated to the members and employees\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 37,\n      \"text\": \"         as per the format provided in Form No.: SF 001\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 38,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 39,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 40,\n      \"text\": \"7.4       Site SHE Committee meeting shall be conducted at least once in a month with the\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 41,\n      \"text\": \"        minimum members listed below:\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 42,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 43,\n      \"text\": \"         Chairman           Project Manager\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 44,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 45,\n      \"text\": \"           Secretary       SHE Manager (In-charge)\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 46,\n      \"text\": \"        Members                     i)   Labour Welfare Officer\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 47,\n      \"text\": \"                                                           ii)   In charge of plant and machinery\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 48,\n      \"text\": \"                                                            iii)  In charge of site electrics\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 49,\n      \"text\": \"                                           iv)  In charge of stores.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 50,\n      \"text\": \"                                    v)  Senior  Managers/  Engineers  heading   different  sub\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 51,\n      \"text\": \"                                        functions.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 52,\n      \"text\": \"                                           vi)  Sub – contractor’s representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 53,\n      \"text\": \"                                               vii) Labour Contractor’s representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 54,\n      \"text\": \"                                                  viii) Workers’ representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 55,\n      \"text\": \"                                           ix)  Co-contractor representative.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 56,\n      \"text\": \"                                    x)  SHE staffs\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 57,\n      \"text\": \"          Employer’s\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 58,\n      \"text\": \"                   BMRC SHE in charge and other representatives\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 59,\n      \"text\": \"          Representatives\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 60,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 61,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 62,\n      \"text\": \" 7.5    Construction SHE Committee meeting shall be conducted at least once in a week with the\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 63,\n      \"text\": \"      minimum members listed below:\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 64,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 65,\n      \"text\": \"    Chairman  Project Manager\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 66,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 67,\n      \"text\": \"     Secretary  SHE Manager (In-charge)\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 68,\n      \"text\": \"    Members     i)   Labour Welfare Officer\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 69,\n      \"text\": \"                               ii)   In charge of plant and machinery\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 70,\n      \"text\": \"                               iii)  In-charge of site electricity\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 71,\n      \"text\": \"                      iv)  Senior Managers / Engineers heading different sub functions\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 72,\n      \"text\": \"                   v)   Sub- Contractor’s representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 73,\n      \"text\": \"                      vi)  Labour contractor’s representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 74,\n      \"text\": \"                         vii)  Workers’ representatives\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 75,\n      \"text\": \"                          viii)  All SHE Staffs\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 76,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 77,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 78,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 79,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 80,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 3,\n      \"text\": \"          7.6      Co-contractors’ participation\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 4,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 5,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 6,\n      \"text\": \"          7.6.1      In case of depot, station and other contiguous areas where more than one main\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 7,\n      \"text\": \"                    contractors are working together, the Employer shall instruct the other contractors to\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 8,\n      \"text\": \"                        join for the monthly SHE committee meeting of the main civil contractor, so as to\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 9,\n      \"text\": \"                   discuss and decide about the common provision of security, lighting, toilet, drinking\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 10,\n      \"text\": \"                   water etc. and sharing the maintenance cost of the same etc.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 11,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 12,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 13,\n      \"text\": \"          7.6.2    The general principle for sharing the cost shall be either based on the contract\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 14,\n      \"text\": \"                  value of works executed at the contiguous area or the daily average number of\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 15,\n      \"text\": \"               workmen employed by each contractor in the contiguous area.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 16,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 17,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 18,\n      \"text\": \"          7.7     Minimum time between two monthly SHE Committee meetings\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 19,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 20,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 21,\n      \"text\": \"          7.7.1    A minimum period of 21 days shall be maintained between any two SHE monthly\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 22,\n      \"text\": \"                  committee meetings.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 23,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 24,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 25,\n      \"text\": \"          7.8     Agenda\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 26,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 27,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 28,\n      \"text\": \"          7.8.1    The Secretary shall circulate the agenda of the meeting at least seven working days in\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 29,\n      \"text\": \"                 advance of the scheduled date of the meeting to all members.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 30,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 31,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 32,\n      \"text\": \"          7.8.2    The agenda should broadly cover the following:\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 33,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 34,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 35,\n      \"text\": \"                                 i)     Confirmation of minutes\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 36,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 37,\n      \"text\": \"                                    ii)    Chairman’s review/overview of site SHE performance / condition\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 38,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 39,\n      \"text\": \"                                     iii)    Previous month SHE statistics\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 40,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 41,\n      \"text\": \"                          iv)    Incident and Accident Investigation / dangerous occurrence / near miss report\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 42,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 43,\n      \"text\": \"                      v)    Site SHE inspection\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 44,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 45,\n      \"text\": \"                          vi)    Sub-contractors’ SHE issues\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 46,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 47,\n      \"text\": \"                             vii)   Safety presentation by Members\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 48,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 49,\n      \"text\": \"                               viii)  Report from Employer\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 50,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 51,\n      \"text\": \"                          ix)   Matters arising\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 52,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 53,\n      \"text\": \"                      x)   Any other business\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 54,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 55,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 56,\n      \"text\": \"          7.9      Minutes of the meeting\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 57,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 58,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 59,\n      \"text\": \"          7.9.1    The Minutes of the meeting shall be prepared as per the format provided at Form\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 60,\n      \"text\": \"                   No.: SF- 002 and sent to all members within 2 working days preferably by mail/fax\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 61,\n      \"text\": \"                    followed by hardcopy. Safety Committee meeting minutes shall also be displayed in\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 62,\n      \"text\": \"                    the notice board for wider publicity to all concerned.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 63,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 64,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 65,\n      \"text\": \"          7.10     Disciplinary Action\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 66,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 67,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 68,\n      \"text\": \"          7.10.1   The chairman shall inform the members of any outstanding issues in the meeting and\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 69,\n      \"text\": \"                        in case of repeated offence/ non-compliance by some members or other co/sub\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 70,\n      \"text\": \"                    contractors and propose suitable disciplinary action including provisions of monitory\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 71,\n      \"text\": \"                    penalty as per the relevant contract clauses, the Employer shall ensure that the same\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 72,\n      \"text\": \"                          is implemented.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 73,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 74,\n      \"text\": \"\"\n    }\n  ],\n  \"review_status\": \"pending_manual_review\",\n  \"title\": \"Contractor SHE Committee\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_number_match
  - id: J6af8ef325f51b6bf
    okf_path: OKF_bundle/Technical/Vol3/vol3_appendices_instructions_forms.md
    okf_sha256: 5a0cf8acada1fc881077147ee1d1f7e8c890314febb3371cd8c6cf779f56e738
    heading: Safety, Health and Environment Manual – Appendices, General Instructions and Forms
    source_document: Vol3DLNP1.pdf
    source_sha256: 1ee3fc8dfd12f659f34446b0a6db74e1e1cdd4d593ca91b2a48d59bf1ef97d52
    pdf_pages:
    - 116
    sheet_cells: ''
    json_path: parsed_json/vol3/forms/she_committee_forms.json
    json_sha256: d4d64ab8440b97f6a9deeb0d9cd0b5995bfe88b324ae3231d2f53c8fcbc17a7e
    json_pointer: /forms/0
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"checks\": {\n    \"form_identifier\": \"passed\",\n    \"line_preservation_with_removal_logs\": \"passed\",\n    \"page_sequence\": \"passed\",\n    \"source_hash\": \"passed\"\n  },\n  \"document_role\": \"form_template\",\n  \"field_reconstruction_status\": \"not_performed\",\n  \"form_id\": \"SF/001\",\n  \"fragments\": [\n    {\n      \"pdf_page\": 116,\n      \"text\": \"BANGALORE METRO RAIL CORPORATION LTD.\\n\\n\\n\\n                     FORM No. : SF/001\\n\\n\\n\\n\\n               FORMATION OF SITE SHE COMMITTEE\\n\\n Contract No\\n\\n Contractor Name\\n\\n Contract Title\\n\\n\\n\\n                             CIRCULAR\\n\\n  Committee\\n\\n     The following SHE Committee is constituted with immediate effect:\\n\\n         Chairman:\\n\\n        Members:\\n\\n                    1)\\n\\n                    2)\\n\\n                    3)\\n\\n                    4)\\n\\n                    5)\\n\\n          Secretary:\\n\\n\\n  Periodicity\\n\\n    The committee will meet at least once in a month on the day (specify date)\\n\\n\\n  Agenda\\n\\n     Secretary will circulate agenda of the meeting at least two days in advance of the schedule\\n     date of the meeting.\\n\\n  Circulation\\n\\n  Gist of the meeting will be minuted in the standard format and circulated to the\\n  following under the signature of the secretary\\n\\n           1. Chairman                    3. BMRC Representatives\\n\\n           2. Members                     4. Others concerned\\n\\n\\n\\n\\n  Date:                                            Signed By:      --------------------------\\n\\n                                             CHAIRMAN\"\n    }\n  ],\n  \"pdf_pages\": [\n    116\n  ],\n  \"removed_lines\": [\n    {\n      \"pdf_page\": 116,\n      \"reason\": \"printed_booklet_page_number\",\n      \"source_line_number\": 1,\n      \"text\": \"300\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"reason\": \"manual_page_header\",\n      \"source_line_number\": 2,\n      \"text\": \"                                                                 Safety Health & Environment (SHE) Manual\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"reason\": \"combined_page_footer\",\n      \"source_line_number\": 80,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.              September 2026     Section Page 112 of 114\"\n    }\n  ],\n  \"retained_lines\": [\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 3,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 4,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 5,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 6,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 7,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 8,\n      \"text\": \"                  BANGALORE METRO RAIL CORPORATION LTD.\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 9,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 10,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 11,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 12,\n      \"text\": \"                     FORM No. : SF/001\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 13,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 14,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 15,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 16,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 17,\n      \"text\": \"               FORMATION OF SITE SHE COMMITTEE\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 18,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 19,\n      \"text\": \" Contract No\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 20,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 21,\n      \"text\": \" Contractor Name\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 22,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 23,\n      \"text\": \" Contract Title\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 24,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 25,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 26,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 27,\n      \"text\": \"                             CIRCULAR\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 28,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 29,\n      \"text\": \"  Committee\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 30,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 31,\n      \"text\": \"     The following SHE Committee is constituted with immediate effect:\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 32,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 33,\n      \"text\": \"         Chairman:\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 34,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 35,\n      \"text\": \"        Members:\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 36,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 37,\n      \"text\": \"                    1)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 38,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 39,\n      \"text\": \"                    2)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 40,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 41,\n      \"text\": \"                    3)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 42,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 43,\n      \"text\": \"                    4)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 44,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 45,\n      \"text\": \"                    5)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 46,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 47,\n      \"text\": \"          Secretary:\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 48,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 49,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 50,\n      \"text\": \"  Periodicity\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 51,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 52,\n      \"text\": \"    The committee will meet at least once in a month on the day (specify date)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 53,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 54,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 55,\n      \"text\": \"  Agenda\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 56,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 57,\n      \"text\": \"     Secretary will circulate agenda of the meeting at least two days in advance of the schedule\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 58,\n      \"text\": \"     date of the meeting.\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 59,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 60,\n      \"text\": \"  Circulation\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 61,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 62,\n      \"text\": \"  Gist of the meeting will be minuted in the standard format and circulated to the\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 63,\n      \"text\": \"  following under the signature of the secretary\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 64,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 65,\n      \"text\": \"           1. Chairman                    3. BMRC Representatives\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 66,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 67,\n      \"text\": \"           2. Members                     4. Others concerned\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 68,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 69,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 70,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 71,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 72,\n      \"text\": \"  Date:                                            Signed By:      --------------------------\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 73,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 74,\n      \"text\": \"                                             CHAIRMAN\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 75,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 76,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 77,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 78,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 79,\n      \"text\": \"\"\n    }\n  ],\n  \"review_status\": \"pending_manual_review\",\n  \"source_heading\": {\n    \"form_id\": \"SF/001\",\n    \"pdf_page\": 116,\n    \"source_text\": \"                     FORM No. : SF/001\"\n  },\n  \"source_page_context\": [\n    {\n      \"extraction_method\": \"geometric_sort\",\n      \"has_extracted_text\": true,\n      \"page_rect\": [\n        0.0,\n        0.0,\n        595.219970703125,\n        842.0\n      ],\n      \"pdf_page\": 116,\n      \"review_status\": \"pending_manual_review\",\n      \"rotation\": 0,\n      \"text\": \"300\\n                                                                 Safety Health & Environment (SHE) Manual\\n\\n\\n\\n\\n\\n                  BANGALORE METRO RAIL CORPORATION LTD.\\n\\n\\n\\n                     FORM No. : SF/001\\n\\n\\n\\n\\n               FORMATION OF SITE SHE COMMITTEE\\n\\n Contract No\\n\\n Contractor Name\\n\\n Contract Title\\n\\n\\n\\n                             CIRCULAR\\n\\n  Committee\\n\\n     The following SHE Committee is constituted with immediate effect:\\n\\n         Chairman:\\n\\n        Members:\\n\\n                    1)\\n\\n                    2)\\n\\n                    3)\\n\\n                    4)\\n\\n                    5)\\n\\n          Secretary:\\n\\n\\n  Periodicity\\n\\n    The committee will meet at least once in a month on the day (specify date)\\n\\n\\n  Agenda\\n\\n     Secretary will circulate agenda of the meeting at least two days in advance of the schedule\\n     date of the meeting.\\n\\n  Circulation\\n\\n  Gist of the meeting will be minuted in the standard format and circulated to the\\n  following under the signature of the secretary\\n\\n           1. Chairman                    3. BMRC Representatives\\n\\n           2. Members                     4. Others concerned\\n\\n\\n\\n\\n  Date:                                            Signed By:      --------------------------\\n\\n                                             CHAIRMAN\\n\\n\\n\\n\\n\\nBangalore Metro Rail Corporation Ltd.              September 2026     Section Page 112 of 114\",\n      \"text_blocks\": [\n        {\n          \"bbox\": [\n            36.59998321533203,\n            37.608280181884766,\n            550.6591796875,\n            46.05027770996094\n          ],\n          \"block_number\": 0,\n          \"text\": \"                                                                                                                                   Safety Health & Environment (SHE) Manual \\n\"\n        },\n        {\n          \"bbox\": [\n            71.99996948242188,\n            48.41946029663086,\n            74.76715087890625,\n            57.77189636230469\n          ],\n          \"block_number\": 1,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            71.99996948242188,\n            781.9227294921875,\n            503.2270812988281,\n            803.451416015625\n          ],\n          \"block_number\": 2,\n          \"text\": \"Bangalore Metro Rail Corporation Ltd.                              September 2026         Section Page 112 of 114 \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            100.5599594116211,\n            77.46939849853516,\n            103.32714080810547,\n            86.81187438964844\n          ],\n          \"block_number\": 3,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            200.3999786376953,\n            88.3893814086914,\n            435.4872741699219,\n            97.73185729980469\n          ],\n          \"block_number\": 4,\n          \"text\": \"BANGALORE METRO RAIL CORPORATION LTD. \\n\"\n        },\n        {\n          \"bbox\": [\n            238.79989624023438,\n            127.80321502685547,\n            340.2672119140625,\n            138.1587371826172\n          ],\n          \"block_number\": 5,\n          \"text\": \"FORM No. : SF/001 \\n\"\n        },\n        {\n          \"bbox\": [\n            71.99996948242188,\n            157.1494598388672,\n            74.76715087890625,\n            166.49192810058594\n          ],\n          \"block_number\": 6,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            184.31993103027344,\n            175.20318603515625,\n            394.6271667480469,\n            185.55870056152344\n          ],\n          \"block_number\": 7,\n          \"text\": \"FORMATION OF SITE SHE COMMITTEE \\n\"\n        },\n        {\n          \"bbox\": [\n            77.39997100830078,\n            194.34934997558594,\n            174.0071563720703,\n            203.8118133544922\n          ],\n          \"block_number\": 8,\n          \"text\": \"Contract No \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            77.39997100830078,\n            212.34934997558594,\n            174.00711059570312,\n            221.8118133544922\n          ],\n          \"block_number\": 9,\n          \"text\": \"Contractor Name \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            77.39997100830078,\n            230.34934997558594,\n            174.0071563720703,\n            239.8118133544922\n          ],\n          \"block_number\": 10,\n          \"text\": \"Contract Title \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            288.7198791503906,\n            248.45938110351562,\n            291.487060546875,\n            257.81182861328125\n          ],\n          \"block_number\": 11,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            82.19996643066406,\n            266.3493347167969,\n            316.8071594238281,\n            290.21185302734375\n          ],\n          \"block_number\": 12,\n          \"text\": \"CIRCULAR \\n Committee \\n\"\n        },\n        {\n          \"bbox\": [\n            99.23995971679688,\n            295.4994201660156,\n            396.007568359375,\n            304.85186767578125\n          ],\n          \"block_number\": 13,\n          \"text\": \"The following SHE Committee is constituted with immediate effect: \\n\"\n        },\n        {\n          \"bbox\": [\n            118.20028686523438,\n            309.8994445800781,\n            167.0474395751953,\n            333.7718505859375\n          ],\n          \"block_number\": 14,\n          \"text\": \"Chairman: \\nMembers: \\n\"\n        },\n        {\n          \"bbox\": [\n            118.20028686523438,\n            338.93939208984375,\n            188.1691131591797,\n            420.7717590332031\n          ],\n          \"block_number\": 15,\n          \"text\": \"1) \\n \\n2) \\n \\n3) \\n \\n4) \\n \\n5) \\n \\nSecretary: \\n\"\n        },\n        {\n          \"bbox\": [\n            406.2001953125,\n            425.8292541503906,\n            408.9673767089844,\n            435.1717529296875\n          ],\n          \"block_number\": 16,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            82.19996643066406,\n            443.8292541503906,\n            136.08714294433594,\n            453.1717529296875\n          ],\n          \"block_number\": 17,\n          \"text\": \"Periodicity \\n\"\n        },\n        {\n          \"bbox\": [\n            94.79996490478516,\n            458.4593200683594,\n            429.369140625,\n            467.811767578125\n          ],\n          \"block_number\": 18,\n          \"text\": \"The committee will meet at least once in a month on the day (specify date)  \\n\"\n        },\n        {\n          \"bbox\": [\n            82.19996643066406,\n            485.5892639160156,\n            121.6871566772461,\n            494.9317626953125\n          ],\n          \"block_number\": 19,\n          \"text\": \"Agenda \\n\"\n        },\n        {\n          \"bbox\": [\n            94.79996490478516,\n            500.2193298339844,\n            498.2474060058594,\n            521.0917358398438\n          ],\n          \"block_number\": 20,\n          \"text\": \"Secretary will circulate agenda of the meeting at least two days in advance of the schedule \\ndate of the meeting. \\n\"\n        },\n        {\n          \"bbox\": [\n            80.99996948242188,\n            531.0692749023438,\n            501.36761474609375,\n            566.4517211914062\n          ],\n          \"block_number\": 21,\n          \"text\": \"Circulation \\nGist of the meeting will be minuted in the standard format and circulated to the \\nfollowing under the signature of the secretary  \\n\"\n        },\n        {\n          \"bbox\": [\n            118.19999694824219,\n            571.6192626953125,\n            408.96710205078125,\n            609.8916625976562\n          ],\n          \"block_number\": 22,\n          \"text\": \"1. Chairman \\n \\n \\n3. BMRC Representatives \\n2. Members \\n \\n \\n4. Others concerned \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            82.19996643066406,\n            622.3792114257812,\n            490.8202819824219,\n            646.251708984375\n          ],\n          \"block_number\": 23,\n          \"text\": \" \\nDate: \\n \\n \\n \\n \\n Signed By: \\n-------------------------- \\n\"\n        },\n        {\n          \"bbox\": [\n            401.39984130859375,\n            654.471923828125,\n            463.1470947265625,\n            664.8385009765625\n          ],\n          \"block_number\": 24,\n          \"text\": \"CHAIRMAN \\n\"\n        },\n        {\n          \"bbox\": [\n            71.99996948242188,\n            693.17919921875,\n            74.76715087890625,\n            745.9716796875\n          ],\n          \"block_number\": 25,\n          \"text\": \" \\n \\n \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            546.0439453125,\n            24.479991912841797,\n            570.0199584960938,\n            41.38799285888672\n          ],\n          \"block_number\": 26,\n          \"text\": \"300\\n\"\n        }\n      ]\n    }\n  ],\n  \"table_reconstruction_status\": \"not_performed\",\n  \"title\": \"Formation of Site SHE Committee\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T12:14:18+00:00'
  status: draft
  amendment_annotations:
  - state: superseded
    scope: Baseline NIT Key Detail 10 date/time fields only
    text: 'Preserve the baseline source as history. C1 changes these fields, and C3 further replaces the C1 date/time fields. Latest supplied replacement: 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST). No claim is made about later notices.'
    evidence_ids:
    - J981b70cc6e283023
    - J6b36427c3b2760b1
    - J827a319dc3712125
  - state: superseded
    scope: Baseline NIT Key Detail 10 date/time fields only
    text: 'Preserve the baseline source as history. C1 changes these fields, and C3 further replaces the C1 date/time fields. Latest supplied replacement: 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST). No claim is made about later notices.'
    evidence_ids:
    - Jcbe0f7287bb5da91
    - J6b36427c3b2760b1
    - J827a319dc3712125
  - state: superseded
    scope: C1 date/time fields in the cited source record only
    text: The C1 values for Key Detail 10 are historical. C3 replaces 09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST) with 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST). This callout does not supersede the entire synthesized claim.
    evidence_ids:
    - J6b36427c3b2760b1
    - J827a319dc3712125
  editorial_history:
  - previous_claim_id: C88ec7c5b63e461c2
    previous_evidence_ids:
    - S09ae5a2a5bf6b41c
    - J54c382c09ffff5f9
    - J70459e3caeaaef12
    - Sfd1aa114f35e9e94
    - J51c423559e058474
    - S052ffbb3a0e241a0
    - J4805b52601f511db
    - J099b5fe5de51f74d
    - Jf9d2ada6599b727b
    - J09eb38685b1042c6
    - J81bb5479e7edcd11
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: The historical submission sequence is baseline 03-09 October 2026, C1 09-15 October, and C3 09-23 October, with the closing time 3 PM IST. These are recorded tender-history states, not live submission advice.
  evidence_ids:
  - Sc18621fd1b08f3e0
  - J981b70cc6e283023
  - Jcbe0f7287bb5da91
  - S69a6c3139d9e4c35
  - J6b36427c3b2760b1
  - S833aa656a16da78a
  - J827a319dc3712125
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: Cd7fc0fcc7de94429
  citations:
  - id: Sc18621fd1b08f3e0
    okf_path: OKF_bundle/Technical/Vol1/secA.md
    okf_sha256: 1d19d2821187107d8bead3c38cac38cb70cac496bf9b5b067362f9b891f92cfb
    heading: Key Detail 10 — Online Tender Submission
    source_document: Vol1DLNP1.pdf
    pdf_pages:
    - 7
    quote: '- **Submission Period:** 03.10.2026, from 10.00 AM, to 09.10.2026, up to 3.00 PM (IST).'
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  - id: J981b70cc6e283023
    okf_path: OKF_bundle/Technical/Vol1/secA.md
    okf_sha256: 1d19d2821187107d8bead3c38cac38cb70cac496bf9b5b067362f9b891f92cfb
    heading: Key Detail 10 — Online Tender Submission
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol1/section_a_nit/nit_items.json
    json_sha256: ffa851d3dc75c862bbb9df376985067951c7005c988fb0a1002a897b32525b6b
    json_pointer: /key_details/9
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"fragments\": [\n    {\n      \"pdf_page\": 7,\n      \"text\": \"10  Tender  submission  Date  and  Time  03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n         (online)                                3.00 PM) (IST)\"\n    }\n  ],\n  \"number\": 10,\n  \"review_status\": \"pending_manual_review\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_number_match
  - id: Jcbe0f7287bb5da91
    okf_path: OKF_bundle/Technical/Vol1/secA.md
    okf_sha256: 1d19d2821187107d8bead3c38cac38cb70cac496bf9b5b067362f9b891f92cfb
    heading: Key Detail 10 — Online Tender Submission
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol1/section_a_nit/nit_table.json
    json_sha256: e4e595fa155f932fe793f28df02a9836eb06f24ca4352db151622db258ce6b10
    json_pointer: /rows/9
    json_record_id: null
    source_review_status: pending_visual_review
    quote: "{\n  \"cell_bboxes\": [\n    [\n      70.54588003719554,\n      479.5196228027344,\n      95.63999938964844,\n      507.71961975097656\n    ],\n    [\n      95.63999938964844,\n      479.5196228027344,\n      284.63999938964844,\n      507.71961975097656\n    ],\n    [\n      284.63999938964844,\n      479.5196228027344,\n      525.6140926585477,\n      507.71961975097656\n    ]\n  ],\n  \"extracted_cells\": [\n    \"10\",\n    \"Tender  submission  Date  and  Time\\n(online)\",\n    \"03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n3.00 PM) (IST)\"\n  ],\n  \"number\": 10,\n  \"original_row_fragments\": [\n    {\n      \"pdf_page\": 7,\n      \"text\": \"10  Tender  submission  Date  and  Time  03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n         (online)                                3.00 PM) (IST)\"\n    }\n  ],\n  \"pdf_page\": 7,\n  \"requirement\": \"Tender  submission  Date  and  Time\\n(online)\",\n  \"review_status\": \"pending_visual_review\",\n  \"token_preservation_check\": \"passed\",\n  \"value\": \"03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n3.00 PM) (IST)\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_number_match
  - id: S69a6c3139d9e4c35
    okf_path: OKF_bundle/addendum_and_corrigendum/A_and_C1.md
    okf_sha256: 8b340a5039e27927eab4df9c9d385ebe89253a3c5e947647c885055e9c4277fd
    heading: Change 2 — Online Tender Submission Date and Time
    source_document: DLN_P1_AandC1_157.PDF
    pdf_pages:
    - 1
    quote: '- **Amends:** [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]]

      - **Change type:** Replace submission-window dates

      - **Old value:** 03.10.2026 from 10.00 AM to 09.10.2026 up to 3.00 PM IST

      - **New value:** 09.10.2026 from 10.00 AM to 15.10.2026 up to 3.00 PM IST

      - **Evidence:** `DLN_P1_AandC1_157.PDF`, PDF page 1, amendment serial 1

      - **Affected booklet page:** 001


      Both the opening date and closing date of the submission window change.'
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  - id: J6b36427c3b2760b1
    okf_path: OKF_bundle/addendum_and_corrigendum/A_and_C1.md
    okf_sha256: 8b340a5039e27927eab4df9c9d385ebe89253a3c5e947647c885055e9c4277fd
    heading: Change 2 — Online Tender Submission Date and Time
    source_document: DLN_P1_AandC1_157.PDF
    source_sha256: 26b25a4e3c3d3206635d0ddae6ce70c00e51468ebb4fe5d93f5e9d65902942d1
    pdf_pages:
    - 1
    sheet_cells: ''
    json_path: parsed_json/addendum_corrigendum/corrigenda_amendments.json
    json_sha256: 41af12b27292ebbdcf0de3bbd3c72bf1a52ac20ad7977041d1ed344c3240e712
    json_pointer: /amendments/0
    json_record_id: corrigendum_1/nit_key_detail_10
    source_review_status: pending_manual_review
    quote: "{\n  \"affected_reference\": \"Key Detail 10\",\n  \"affected_section\": \"NIT\",\n  \"booklet_page_reference\": \"001\",\n  \"corrigendum_number\": 1,\n  \"document_date\": \"2026-10-01\",\n  \"existing_selected_text\": \"03.10.2026 (From 10.00 AM) to 09.10.2026 (up to 3.00 PM) (IST)\",\n  \"field_provenance\": \"Prepared from visual inspection of the source scan; not automatically inferred from OCR\",\n  \"label\": \"Tender submission Date and Time (online)\",\n  \"ocr_evidence_relative_to_project\": \"output/corrigenda/ocr/run_20261030T051229372457Z/corrigendum_1/ocr.json\",\n  \"operation\": \"replace_date_time_fields\",\n  \"pdf_pages\": [\n    1\n  ],\n  \"printed_amendment_serial\": \"1\",\n  \"record_id\": \"corrigendum_1/nit_key_detail_10\",\n  \"replacement_selected_text\": \"09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)\",\n  \"review_status\": \"pending_manual_review\",\n  \"scope\": \"Date/time fields only; other wording, venue and submission conditions are retained in the source OCR\",\n  \"source_document\": \"DLN_P1_AandC1_157.PDF\",\n  \"source_sha256\": \"26b25a4e3c3d3206635d0ddae6ce70c00e51468ebb4fe5d93f5e9d65902942d1\",\n  \"transcription_scope\": \"Selected amendment wording and fields, not a complete verbatim table transcription\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: amendment_entry_navigation
  - id: S833aa656a16da78a
    okf_path: OKF_bundle/addendum_and_corrigendum/A_and_C3.md
    okf_sha256: d9cb8b7ff09a2dd9ff83e9ea35ba6330264539603a982a5daac47275ff44decb
    heading: Change 2 — Online Tender Submission Date and Time
    source_document: AandC3_DLN_P1_157.PDF
    pdf_pages:
    - 1
    quote: '- **Underlying NIT entry:** [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]]

      - **Change type:** Replace the submission-window closing date

      - **Old value:** 09.10.2026 from 10.00 AM to 15.10.2026 up to 3.00 PM IST

      - **New value:** 09.10.2026 from 10.00 AM to 23.10.2026 up to 3.00 PM IST

      - **Evidence:** `AandC3_DLN_P1_157.PDF`, PDF page 1, amendment serial 1

      - **Replaces:** Corrigendum 1, serial 1, Key Detail 10 date fields


      The opening date remains 09.10.2026. It is not changed to 16.10.2026.'
    page_basis: OKF reference, not independently PDF-verified
    page_precision: section_reference
  - id: J827a319dc3712125
    okf_path: OKF_bundle/addendum_and_corrigendum/A_and_C3.md
    okf_sha256: d9cb8b7ff09a2dd9ff83e9ea35ba6330264539603a982a5daac47275ff44decb
    heading: Change 2 — Online Tender Submission Date and Time
    source_document: AandC3_DLN_P1_157.PDF
    source_sha256: 623067baa7cb9d7b2863567fea861767f42102f9e16ff3c2b547afed554280de
    pdf_pages:
    - 1
    sheet_cells: ''
    json_path: parsed_json/addendum_corrigendum/corrigenda_amendments.json
    json_sha256: 41af12b27292ebbdcf0de3bbd3c72bf1a52ac20ad7977041d1ed344c3240e712
    json_pointer: /amendments/13
    json_record_id: corrigendum_3/nit_key_detail_10
    source_review_status: pending_manual_review
    quote: "{\n  \"affected_reference\": \"Key Detail 10\",\n  \"affected_section\": \"NIT\",\n  \"corrigendum_number\": 3,\n  \"document_date\": \"2026-10-13\",\n  \"existing_selected_text\": \"09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)\",\n  \"field_provenance\": \"Prepared from visual inspection of the source scan; not automatically inferred from OCR\",\n  \"label\": \"Tender submission Date and Time (online)\",\n  \"ocr_evidence_relative_to_project\": \"output/corrigenda/ocr/run_20261030T051229372457Z/corrigendum_3/ocr.json\",\n  \"operation\": \"replace_date_time_fields\",\n  \"pdf_pages\": [\n    1\n  ],\n  \"printed_amendment_serial\": \"1\",\n  \"printed_cross_reference\": \"Sl.No 1 of Addendum and Corrigendum No. 1 Dated 01-10-2026\",\n  \"record_id\": \"corrigendum_3/nit_key_detail_10\",\n  \"replacement_selected_text\": \"09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST)\",\n  \"replaces_record_id\": \"corrigendum_1/nit_key_detail_10\",\n  \"review_status\": \"pending_manual_review\",\n  \"scope\": \"Date/time fields only; other wording, venue and submission conditions are retained in the source OCR\",\n  \"source_document\": \"AandC3_DLN_P1_157.PDF\",\n  \"source_sha256\": \"623067baa7cb9d7b2863567fea861767f42102f9e16ff3c2b547afed554280de\",\n  \"transcription_scope\": \"Selected amendment wording and fields, not a complete verbatim table transcription\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: amendment_entry_navigation
  created_at: '2026-11-01T12:14:18+00:00'
  status: draft
  amendment_annotations:
  - state: superseded
    scope: Baseline NIT Key Detail 10 date/time fields only
    text: 'Preserve the baseline source as history. C1 changes these fields, and C3 further replaces the C1 date/time fields. Latest supplied replacement: 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST). No claim is made about later notices.'
    evidence_ids:
    - J981b70cc6e283023
    - J6b36427c3b2760b1
    - J827a319dc3712125
  - state: superseded
    scope: Baseline NIT Key Detail 10 date/time fields only
    text: 'Preserve the baseline source as history. C1 changes these fields, and C3 further replaces the C1 date/time fields. Latest supplied replacement: 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST). No claim is made about later notices.'
    evidence_ids:
    - Jcbe0f7287bb5da91
    - J6b36427c3b2760b1
    - J827a319dc3712125
  - state: superseded
    scope: C1 date/time fields in the cited source record only
    text: The C1 values for Key Detail 10 are historical. C3 replaces 09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST) with 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST). This callout does not supersede the entire synthesized claim.
    evidence_ids:
    - J6b36427c3b2760b1
    - J827a319dc3712125
  editorial_history:
  - previous_claim_id: C3f092a38a6dc0fd8
    previous_evidence_ids:
    - S09ae5a2a5bf6b41c
    - J54c382c09ffff5f9
    - J70459e3caeaaef12
    - Sfd1aa114f35e9e94
    - J51c423559e058474
    - S052ffbb3a0e241a0
    - J4805b52601f511db
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: The retained DLP discrepancy is six months in Contract Data versus twelve months in the unexecuted Contract Agreement template. Both statements remain visible; no controlling duration is selected here.
  evidence_ids:
  - Jeb83d1b7a6d87fee
  - Jcc49f8beaf50a801
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: C3275e00059822b5d
  citations:
  - id: Jeb83d1b7a6d87fee
    okf_path: OKF_bundle/Technical/Vol1/secE.md
    okf_sha256: d72224b0c08c509f8485b0d971bd10c690c5dace89c225ac4a8fcb0f9f2c9dad
    heading: General Conditions of Contract and Contract Data
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 143
    sheet_cells: ''
    json_path: parsed_json/vol1/section_e_gcc/contract_data_table.json
    json_sha256: c50606c1aae8c00241df233c1dca694aab3deefbb1a6d2156b880f44beae0938
    json_pointer: /items/10
    json_record_id: null
    source_review_status: pending_visual_review
    quote: "{\n  \"cell_bboxes\": [\n    [\n      72.21599807739258,\n      99.359619140625,\n      104.15999603271484,\n      146.27963256835938\n    ],\n    [\n      104.15999603271484,\n      99.359619140625,\n      256.3199920654297,\n      146.27963256835938\n    ],\n    [\n      256.3199920654297,\n      99.359619140625,\n      568.2239837646484,\n      146.27963256835938\n    ]\n  ],\n  \"item_number\": 12,\n  \"pdf_page\": 143,\n  \"raw_cells\": [\n    \"12\",\n    \"Defects Liability Period\\n\\n(GCC Sub-Clause 10)\",\n    \"Defects Liability Period is 6 months from the date of Taking over\\nmentioned in Taking Over Certificates being issued for whole of\\nthe work.\"\n  ],\n  \"requirement\": \"Defects Liability Period\\n\\n(GCC Sub-Clause 10)\",\n  \"review_status\": \"pending_visual_review\",\n  \"source_row_label\": \"12\",\n  \"table_bbox\": [\n    72.21599807739258,\n    46.2596435546875,\n    568.2239837646484,\n    476.3396186828613\n  ],\n  \"value\": \"Defects Liability Period is 6 months from the date of Taking over\\nmentioned in Taking Over Certificates being issued for whole of\\nthe work.\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  - id: Jcc49f8beaf50a801
    okf_path: OKF_bundle/Technical/Vol1/secG.md
    okf_sha256: 78eac979b2d8f01921b45df904f4bb99ae14aed1895d97a7853eb017c3ed315c
    heading: Contract Form 1 — Contract Agreement
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 147
    - 148
    - 149
    - 150
    sheet_cells: ''
    json_path: parsed_json/vol1/section_g_forms/contract_forms.json
    json_sha256: 41670e8866feba3a9ff42e73f2e1da67ed58b020778fce98ad11cf7bc8e2571f
    json_pointer: /forms/0
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"document_role\": \"template\",\n  \"form_id\": \"contract_form_1\",\n  \"form_number\": \"1\",\n  \"fragments\": [\n    {\n      \"pdf_page\": 147,\n      \"text\": \"CONTRACT FORM- 1\\n\\n\\n                      CONTRACT AGREEMENT\\n\\n       This Contract Agreement (hereinafter called the “Contract”) is made at Bangalore on ……..…day of\\n\\n    ……………by and between:\\n\\n       Bangalore Metro Rail Corporation Limited, a company incorporated under companies act 1956\\n       represented by the Managing Director, with office located at  III Floor, BMTC Complex, K.H.Road,\\n        Shantinagar, Bangalore 560 027, hereinafter referred to as the “BMRCL” or the “Employer”, as the\\n       case may be, which expression shall unless excluded by or repugnant to the context or meaning thereof\\n      be deemed to include its successors and assigns of the one part, and;\\n\\n          .........................................................…………………….. [Note 1] comprising:\\n\\na)          ........................................................,  a  company  registered  and  existing  under  the  laws  of\\n\\n             ................................, with head office located at ........................................................, represented by\\n\\n       Mr.  ....................................... and Mr.  ....................................... authorised  to sign and bind the\\n\\n       company, under the Power of Attorney  dated...................................... and the Board Resolution\\n\\n            dated..................................... [Note 5] AND\\n\\nb)          ........................................................,  a  company  registered  and  existing  under  the  laws  of\\n\\n             ................................, with head office located at................................................................ represented\\n\\n       by Mr.  ....................................... and Mr.  ....................................... authorised to sign and bind the\\n\\n       company, under the Power of Attorney  dated...................................... and the Board Resolution\\n\\n            dated..................................... [Note 5] AND\\n\\nc)          ........................................................,  a  company  registered  and  existing  under  the  laws  of\\n\\n             ................................, with head office located at................................................................ represented\\n\\n       by Mr.  ....................................... and Mr.  ....................................... authorised to sign and bind the\\n\\n       company, under the Power of Attorney  dated...................................... and the Board Resolution\\n\\n            dated..................................... [Note 5]\\n\\n\\n\\n       [Note 2] who each of which shall be jointly and severally responsible to the Employer under the Contract\\n         for the Bangalore Metro Rail Project as per conditions agreed to by the Employer;\\n\\n\\n        Hereinafter [Note 3] collectively referred to as the “Contractor” which expression shall unless excluded\\n       by or repugnant to the context or meaning thereof be deemed to include its successors and assigns of\\n        the other part.\\n\\n\\n     WHEREAS the Contractor has established a ........................[Note 4] in accordance with Indian law and\\n        offered a tender for the construction of a rail based mass rapid transport system by execution and\\n        completion, and remedying any defects in the Works of:(Name of the work)----------------------------------\\n           ------------------------------------------------------------------------------------------------------------------------------\\n\\n      Tender Notification No ---------------------------------------------------- Dated --.--. ----. and agrees to undertake\\n       performance of the Work under the terms and conditions set forth in this Contract.\\n\\n\\n     AND WHEREAS the Employer agrees to hire and the Contractor agrees to be hired to implement\\n       the:(Name of the work)-------------------------------------------------------------------------------------------------------\\n           ---------------------------------------------------------\\n\\n       Tender Notification No ---------------------------------------------------- Dated --.--. ----.\\n\\n       Under the terms and conditions specified  in  this Contract Agreement and the other Contract\\n       Documents.\\n     Now THEREFORE the parties hereby agree as follows:\"\n    },\n    {\n      \"pdf_page\": 148,\n      \"text\": \"Clause 1 Words and Expression\\n\\n             In this Contract all the words and expressions shall have the same meanings as are respectively\\n           assigned to them in the conditions of contract hereinafter referred to,\\n\\n   Clause 2  the Contract Documents,\\n\\n          The following shall deem to form and be read and construed as a part of this Contract Agreement\\n\\n            provided any of the provisions therein are not inconsistent with the present contract agreement:\\n              1.  Letter of Acceptance.\\n\\n              2.  Clarifications, Addenda, Corrigenda Issued to Tender document (if any)\\n\\n              3.  Pricing Document\\n\\n              4.  Special Conditions of Contract\\n\\n              5.  Contract forms\\n\\n              6.  General Conditions of Contract\\n\\n              7.  Employer’s Requirement & Technical Specifications\\n\\n              8.  Drawings\\n\\n              9.  Any other document forming part of the Contract\\n\\n               All of the foregoing documents, together with this Contract Agreement, referred to herein as the\\n            Contract.  Also incorporated into the Contract, and made part hereof, are  all Standard codes,\\n             specifications of MORTH/CPWD/KPWD/IRS as applicable, and similar requirements that are referred\\n             to therein. The ‘Priority of documents’ will be as given in clause 1.5 of GCC.\\n\\n   Clause 3 Obligations of the Contractor:\\n\\n         The mutual rights and Obligations of the Employer and the Contractor shall be as set forth in the\\n            contract and in particular: -\\n\\n           3.1 The Contractor agrees, subject to the terms and conditions of the Contract, to perform efficiently\\n          and faithfully all of the work of (Name of the work)-------------------------------------------------------------------\\n                ---------------------------------------------------------------------------------------------\\n\\n          Tender Notification No  ---------------------------------------------------- Dated  --.--. ----.and other  facilities\\n             requisite for or incidental to the successful completion of the Works and in carrying out all duties and\\n            obligations imposed by the Contract.\\n\\n\\n            3.2 The Contractor shall remedy, at no extra cost to the Employer, the defect or failure (fair wear and\\n             tear excluded) after any part of the Work are taken over by the Employer until the end of Defects\\n               Liability Period.\\n\\n            3.3 The Contractor shall also remedy, at no extra cost to the Employer, the defect or failure of any\\n           equipment provided in the Works and any defects in materials supplied and workmanship up to end\\n             of warranty period.\\n\\n   Clause 4 Obligations of the Employer:\\n\\n         The Employer agrees, subject to the terms and conditions of the Contract, to pay the Contractor the\\n         amount specified, and at the rates and terms and in the manner set forth in the Contract.\\n\\n   Clause 5 Contract Price:\\n\\n             5.1. Employer agrees to pay the Contractor total amount mentioned below (hereinafter called 'the\\n            Contract Price') and the Contractor agrees to accept the total amount mentioned below for the\\n            execution, completion, maintenance / rectification of defects and guarantee for the works carried out\\n          by him as part of his obligations, responsibilities and liabilities under and according to the provisions\\n          and obligations imposed on him by the Contract.\\n\\n\\n\\n                    (i)      Indian Rupees……………………………………...  (....................................Rs.) and Output\\n\\n              GST as applicable.\"\n    },\n    {\n      \"pdf_page\": 149,\n      \"text\": \"5.2. The contract price mentioned above  will be increased or decreased during the period of\\n        performance of the contract as specifically provided,  if any, in the General or Special Conditions of\\n         Contract and no additional amount for any other account whatsoever shall be payable to the Contractor.\\n\\n Clause 6 Completion Time:\\n\\n       The Contractor shall complete whole of the Works within.............................. (.........) months from the\\n       Commencement Date (date of signing the ‘Contract Agreement’). The Defect Liability Period is 12\\n         (Twelve) months from the date mentioned in the Final Taking over Certificate for whole of the Works.\\n\\n Clause7 Integration\\n\\n       The Employer and the Contractor agree that this Contract Agreement, together with the other Contract\\n        Documents, expresses all of the agreements, understandings, promises, and covenants of the parties,\\n        and  integrates,  combines,  and  supersedes   all  prior  and  contemporaneous  negotiations,\\n         understandings, and agreements, whether written or oral and no modification or alteration of the\\n         Contract Documents shall be valid or binding on either party, unless expressed in writing and executed\\n          with the same formality as this Contract Agreement, except as may otherwise be specifically provided\\n           in the Contract Documents.\\n\\n Clause 8 Governing Law\\n\\n         This Contract is enforceable and construed under the applicable laws of the Republic of India.\\n\\n Clause 9 Language\\n\\n         This Contract Agreement and the other Contract Documents are made in the English language.\\n\\nClause 9-A Notices:\\n\\n       The Address for service of all documents / notices arising out of or in connection with this contract\\n          shall be:\\n           (a) Upon Employer: Bangalore Metro Rail Corporation Ltd, 3rd Floor, BMTC Complex, K.H. Road,\\n             Shantinagar, Bengaluru – 560027, Karnataka, India.\\n           Marked for the attention of Executive Director.\\n           (b) Upon the Contractor: --------------------------------------------------------------------(Name and address of\\n              the contractor)\\n           The above notices can be sent either by E-mail to the respective E-mail addresses of the parties\\n              or by registered post to the above mentioned addresses of the parties.\\n\\n Clause 10 Jurisdiction of Court\\n\\n       The Courts at Bangalore shall have the exclusive jurisdiction in respect of all the disputes arising out\\n          of this Agreement between the parties.\\n\\n\\n        IN WITNESS WHEREOF, the parties hereto have caused this Contract to be signed in their respective\\n\\n       names by their authorised representatives as of the day and year first above written\\n\\n                  For BMRCL                       [Note 6] for …………...................,\\n              The Employer                       The Contractor\\n              Bangalore Metro Rail                           (a) …………………………………….\\n                Corporation Limited                  …………………………………….\\n\\n\\n\\n                      (                         )                                    (                         )\\n                       --------------------------                                     --------------------------\\n\\n\\n               WITNESS\\n\\n\\n                                                               (b) For …………………………………….\\n                      (                         )              ……………………………\\n                       --------------------------\"\n    },\n    {\n      \"pdf_page\": 150,\n      \"text\": \"(                         )\\n                                                                                         --------------------------\\n\\n\\n                                                                           (c) …………………………………….\\n                              ……………………………\\n\\n\\n\\n                                                                                         (                         )\\n                                                                                         --------------------------\\n\\n\\n\\n\\n\\n                                                          WITNESS\\n\\n\\n\\n                                                                                               (                      )\\n                                                                                             --------------------------\\n\\n\\n\\n\\n\\n   Notes:  (for preparation of but not for inclusion in the engrossment of the Contract Agreement)\\n\\n   1           If the Contractor comprises a partnership, joint venture, liability will be joint and several, and each\\n\\n         member thereof must be identified.\\n\\n    2.       In the case that the Contractor comprises a single company, this line should be deleted entirely, as\\n\\n            also should be paragraphs (b) and (c) above.\\n\\n    3.       In the case that the Contractor comprises a single company, the word “collectively” should be deleted\\n\\n           from this line.\\n\\n    4.      Enter the appropriate nature of the Contractor; company, partnership, joint venture as the case may\\n\\n           be.\\n\\n    5.      Enter the date of the appropriate resolution.\\n\\n    6.          If the Contractor comprises a partnership, joint venture, each member thereof must execute.\\n\\n    7.     The required Stamp duty in accordance with Karnataka Stamp Act is to be borne by the contractor.\"\n    }\n  ],\n  \"heading_line\": \"CONTRACT FORM- 1\",\n  \"review_status\": \"pending_manual_review\",\n  \"title\": \"Contract Agreement\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_form_number_match
  created_at: '2026-11-01T12:14:18+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Cf4ee510878d441b0
    previous_evidence_ids:
    - J099b5fe5de51f74d
    - Jf9d2ada6599b727b
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: parameter
  text: The SHE agenda discrepancy concerns seven working days in 7.8.1 versus two days in SF/001. Monthly Site SHE and weekly Construction SHE committees are distinct provisions, not automatically a frequency contradiction.
  evidence_ids:
  - J9eeb4ca708ebff86
  - J6af8ef325f51b6bf
  relation_type: none
  explicitness: not_a_relation
  from_id: ''
  to_id: ''
  id: Ccbcca28216d54274
  citations:
  - id: J9eeb4ca708ebff86
    okf_path: OKF_bundle/Technical/Vol3/vol3_part1.md
    okf_sha256: 6d3d536a7bdd68a40c05a233955b27e65e857ce6f72b9f0e755914d9adb85df6
    heading: Clause 7.0 — Contractor SHE Committee
    source_document: Vol3DLNP1.pdf
    source_sha256: 1ee3fc8dfd12f659f34446b0a6db74e1e1cdd4d593ca91b2a48d59bf1ef97d52
    pdf_pages:
    - 17
    - 18
    - 19
    sheet_cells: ''
    json_path: parsed_json/vol3/part_1_she_management/she_management_clauses.json
    json_sha256: b017881487993483cddcb5c17ffd7e2c6898a21f9463d8fab51b9e05d5e0a9df
    json_pointer: /clauses/6
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"clause_id\": \"7.0\",\n  \"fragments\": [\n    {\n      \"pdf_page\": 17,\n      \"text\": \"7.0      Contractor SHE Committee\\n\\n\\n          7.1         All employees should be  able  to  participate  in the making and monitoring  of\\n                  arrangements for safety, industrial health and environment at their place of work. The\\n                   establishment of site SHE committees in which employees and Contractor and sub-\\n                     contractor  management  are  represented  can  increase  the  involvement  and\\n                 commitment of employees. The contractor shall ensure the formation and monitor the\\n                     functioning of contractor SHE committees.\\n\\n\\n          7.2      Terms of Reference\\n\\n\\n          7.2.1    The Terms of Reference for the committee shall be as follows;\\n\\n\\n                                 i)    To establish company safety policies and practices\\n\\n                                    ii)   To monitor the adequacy of the contractor’s site SHE plan and ensure  its\\n                        implementation\\n\\n                                     iii)   To review SHE training\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"text\": \"iv)   To review the contractor’s monthly SHE report.\\n\\n           v)   To identify probable causes of accident and unsafe practices in building or other\\n                construction work and to suggest remedial measures.\\n\\n             vi)   To stimulate interest of Employer and building workers in safety by organizing\\n                safety week, safety competition, talks and film-shows on safety, preparing\\n               posters or taking similar other measures as and when required or as necessary.\\n\\n              vii)  To go round the construction site with a view to check unsafe practices and\\n                detect unsafe  conditions and  to recommend remedial measures  for  their\\n                  rectifications including first-aid medical and welfare facilities.\\n\\n               viii)  Committee team members should perform a  site inspection before every\\n              committee meetings and to monitor SHE inspection reports.\\n\\n             ix)   To bring to the notice of the Employer the hazards associated with use, handling\\n             and maintenance of the equipment used during the course of building and other\\n                construction work\\n\\n           x)   To suggest measures for improving welfare amenities in the construction site\\n             and other miscellaneous aspect of safety, health and welfare in building or other\\n                construction work.\\n\\n             xi)   To look into the health hazards associated with handling different types of\\n                explosives, chemicals and other construction materials and to suggest remedial\\n             measures including personal protective equipment.\\n\\n              xii)  To review the last safety committee meeting minutes and to take action against\\n               persons/sub-contractors for non-compliance if any.\\n\\n\\n7.3       Within 14 days of award of contract, the SHE committee shall be constituted and\\n           notification regarding the same shall be communicated to the members and employees\\n         as per the format provided in Form No.: SF 001\\n\\n\\n7.4       Site SHE Committee meeting shall be conducted at least once in a month with the\\n        minimum members listed below:\\n\\n         Chairman           Project Manager\\n\\n           Secretary       SHE Manager (In-charge)\\n        Members                     i)   Labour Welfare Officer\\n                                                           ii)   In charge of plant and machinery\\n                                                            iii)  In charge of site electrics\\n                                           iv)  In charge of stores.\\n                                    v)  Senior  Managers/  Engineers  heading   different  sub\\n                                        functions.\\n                                           vi)  Sub – contractor’s representative\\n                                               vii) Labour Contractor’s representative\\n                                                  viii) Workers’ representative\\n                                           ix)  Co-contractor representative.\\n                                    x)  SHE staffs\\n          Employer’s\\n                   BMRC SHE in charge and other representatives\\n          Representatives\\n\\n\\n 7.5    Construction SHE Committee meeting shall be conducted at least once in a week with the\\n      minimum members listed below:\\n\\n    Chairman  Project Manager\\n\\n     Secretary  SHE Manager (In-charge)\\n    Members     i)   Labour Welfare Officer\\n                               ii)   In charge of plant and machinery\\n                               iii)  In-charge of site electricity\\n                      iv)  Senior Managers / Engineers heading different sub functions\\n                   v)   Sub- Contractor’s representative\\n                      vi)  Labour contractor’s representative\\n                         vii)  Workers’ representatives\\n                          viii)  All SHE Staffs\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"text\": \"7.6      Co-contractors’ participation\\n\\n\\n          7.6.1      In case of depot, station and other contiguous areas where more than one main\\n                    contractors are working together, the Employer shall instruct the other contractors to\\n                        join for the monthly SHE committee meeting of the main civil contractor, so as to\\n                   discuss and decide about the common provision of security, lighting, toilet, drinking\\n                   water etc. and sharing the maintenance cost of the same etc.\\n\\n\\n          7.6.2    The general principle for sharing the cost shall be either based on the contract\\n                  value of works executed at the contiguous area or the daily average number of\\n               workmen employed by each contractor in the contiguous area.\\n\\n\\n          7.7     Minimum time between two monthly SHE Committee meetings\\n\\n\\n          7.7.1    A minimum period of 21 days shall be maintained between any two SHE monthly\\n                  committee meetings.\\n\\n\\n          7.8     Agenda\\n\\n\\n          7.8.1    The Secretary shall circulate the agenda of the meeting at least seven working days in\\n                 advance of the scheduled date of the meeting to all members.\\n\\n\\n          7.8.2    The agenda should broadly cover the following:\\n\\n\\n                                 i)     Confirmation of minutes\\n\\n                                    ii)    Chairman’s review/overview of site SHE performance / condition\\n\\n                                     iii)    Previous month SHE statistics\\n\\n                          iv)    Incident and Accident Investigation / dangerous occurrence / near miss report\\n\\n                      v)    Site SHE inspection\\n\\n                          vi)    Sub-contractors’ SHE issues\\n\\n                             vii)   Safety presentation by Members\\n\\n                               viii)  Report from Employer\\n\\n                          ix)   Matters arising\\n\\n                      x)   Any other business\\n\\n\\n          7.9      Minutes of the meeting\\n\\n\\n          7.9.1    The Minutes of the meeting shall be prepared as per the format provided at Form\\n                   No.: SF- 002 and sent to all members within 2 working days preferably by mail/fax\\n                    followed by hardcopy. Safety Committee meeting minutes shall also be displayed in\\n                    the notice board for wider publicity to all concerned.\\n\\n\\n          7.10     Disciplinary Action\\n\\n\\n          7.10.1   The chairman shall inform the members of any outstanding issues in the meeting and\\n                        in case of repeated offence/ non-compliance by some members or other co/sub\\n                    contractors and propose suitable disciplinary action including provisions of monitory\\n                    penalty as per the relevant contract clauses, the Employer shall ensure that the same\\n                          is implemented.\"\n    }\n  ],\n  \"heading_line\": \"          7.0      Contractor SHE Committee\",\n  \"retained_lines\": [\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 54,\n      \"text\": \"          7.0      Contractor SHE Committee\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 55,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 56,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 57,\n      \"text\": \"          7.1         All employees should be  able  to  participate  in the making and monitoring  of\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 58,\n      \"text\": \"                  arrangements for safety, industrial health and environment at their place of work. The\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 59,\n      \"text\": \"                   establishment of site SHE committees in which employees and Contractor and sub-\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 60,\n      \"text\": \"                     contractor  management  are  represented  can  increase  the  involvement  and\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 61,\n      \"text\": \"                 commitment of employees. The contractor shall ensure the formation and monitor the\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 62,\n      \"text\": \"                     functioning of contractor SHE committees.\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 63,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 64,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 65,\n      \"text\": \"          7.2      Terms of Reference\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 66,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 67,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 68,\n      \"text\": \"          7.2.1    The Terms of Reference for the committee shall be as follows;\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 69,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 70,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 71,\n      \"text\": \"                                 i)    To establish company safety policies and practices\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 72,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 73,\n      \"text\": \"                                    ii)   To monitor the adequacy of the contractor’s site SHE plan and ensure  its\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 74,\n      \"text\": \"                        implementation\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 75,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 76,\n      \"text\": \"                                     iii)   To review SHE training\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 77,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 78,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 17,\n      \"source_line_number\": 79,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 3,\n      \"text\": \"             iv)   To review the contractor’s monthly SHE report.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 4,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 5,\n      \"text\": \"           v)   To identify probable causes of accident and unsafe practices in building or other\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 6,\n      \"text\": \"                construction work and to suggest remedial measures.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 7,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 8,\n      \"text\": \"             vi)   To stimulate interest of Employer and building workers in safety by organizing\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 9,\n      \"text\": \"                safety week, safety competition, talks and film-shows on safety, preparing\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 10,\n      \"text\": \"               posters or taking similar other measures as and when required or as necessary.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 11,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 12,\n      \"text\": \"              vii)  To go round the construction site with a view to check unsafe practices and\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 13,\n      \"text\": \"                detect unsafe  conditions and  to recommend remedial measures  for  their\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 14,\n      \"text\": \"                  rectifications including first-aid medical and welfare facilities.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 15,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 16,\n      \"text\": \"               viii)  Committee team members should perform a  site inspection before every\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 17,\n      \"text\": \"              committee meetings and to monitor SHE inspection reports.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 18,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 19,\n      \"text\": \"             ix)   To bring to the notice of the Employer the hazards associated with use, handling\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 20,\n      \"text\": \"             and maintenance of the equipment used during the course of building and other\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 21,\n      \"text\": \"                construction work\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 22,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 23,\n      \"text\": \"           x)   To suggest measures for improving welfare amenities in the construction site\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 24,\n      \"text\": \"             and other miscellaneous aspect of safety, health and welfare in building or other\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 25,\n      \"text\": \"                construction work.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 26,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 27,\n      \"text\": \"             xi)   To look into the health hazards associated with handling different types of\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 28,\n      \"text\": \"                explosives, chemicals and other construction materials and to suggest remedial\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 29,\n      \"text\": \"             measures including personal protective equipment.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 30,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 31,\n      \"text\": \"              xii)  To review the last safety committee meeting minutes and to take action against\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 32,\n      \"text\": \"               persons/sub-contractors for non-compliance if any.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 33,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 34,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 35,\n      \"text\": \"7.3       Within 14 days of award of contract, the SHE committee shall be constituted and\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 36,\n      \"text\": \"           notification regarding the same shall be communicated to the members and employees\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 37,\n      \"text\": \"         as per the format provided in Form No.: SF 001\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 38,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 39,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 40,\n      \"text\": \"7.4       Site SHE Committee meeting shall be conducted at least once in a month with the\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 41,\n      \"text\": \"        minimum members listed below:\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 42,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 43,\n      \"text\": \"         Chairman           Project Manager\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 44,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 45,\n      \"text\": \"           Secretary       SHE Manager (In-charge)\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 46,\n      \"text\": \"        Members                     i)   Labour Welfare Officer\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 47,\n      \"text\": \"                                                           ii)   In charge of plant and machinery\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 48,\n      \"text\": \"                                                            iii)  In charge of site electrics\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 49,\n      \"text\": \"                                           iv)  In charge of stores.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 50,\n      \"text\": \"                                    v)  Senior  Managers/  Engineers  heading   different  sub\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 51,\n      \"text\": \"                                        functions.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 52,\n      \"text\": \"                                           vi)  Sub – contractor’s representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 53,\n      \"text\": \"                                               vii) Labour Contractor’s representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 54,\n      \"text\": \"                                                  viii) Workers’ representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 55,\n      \"text\": \"                                           ix)  Co-contractor representative.\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 56,\n      \"text\": \"                                    x)  SHE staffs\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 57,\n      \"text\": \"          Employer’s\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 58,\n      \"text\": \"                   BMRC SHE in charge and other representatives\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 59,\n      \"text\": \"          Representatives\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 60,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 61,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 62,\n      \"text\": \" 7.5    Construction SHE Committee meeting shall be conducted at least once in a week with the\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 63,\n      \"text\": \"      minimum members listed below:\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 64,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 65,\n      \"text\": \"    Chairman  Project Manager\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 66,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 67,\n      \"text\": \"     Secretary  SHE Manager (In-charge)\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 68,\n      \"text\": \"    Members     i)   Labour Welfare Officer\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 69,\n      \"text\": \"                               ii)   In charge of plant and machinery\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 70,\n      \"text\": \"                               iii)  In-charge of site electricity\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 71,\n      \"text\": \"                      iv)  Senior Managers / Engineers heading different sub functions\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 72,\n      \"text\": \"                   v)   Sub- Contractor’s representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 73,\n      \"text\": \"                      vi)  Labour contractor’s representative\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 74,\n      \"text\": \"                         vii)  Workers’ representatives\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 75,\n      \"text\": \"                          viii)  All SHE Staffs\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 76,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 77,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 78,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 79,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 18,\n      \"source_line_number\": 80,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 3,\n      \"text\": \"          7.6      Co-contractors’ participation\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 4,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 5,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 6,\n      \"text\": \"          7.6.1      In case of depot, station and other contiguous areas where more than one main\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 7,\n      \"text\": \"                    contractors are working together, the Employer shall instruct the other contractors to\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 8,\n      \"text\": \"                        join for the monthly SHE committee meeting of the main civil contractor, so as to\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 9,\n      \"text\": \"                   discuss and decide about the common provision of security, lighting, toilet, drinking\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 10,\n      \"text\": \"                   water etc. and sharing the maintenance cost of the same etc.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 11,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 12,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 13,\n      \"text\": \"          7.6.2    The general principle for sharing the cost shall be either based on the contract\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 14,\n      \"text\": \"                  value of works executed at the contiguous area or the daily average number of\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 15,\n      \"text\": \"               workmen employed by each contractor in the contiguous area.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 16,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 17,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 18,\n      \"text\": \"          7.7     Minimum time between two monthly SHE Committee meetings\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 19,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 20,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 21,\n      \"text\": \"          7.7.1    A minimum period of 21 days shall be maintained between any two SHE monthly\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 22,\n      \"text\": \"                  committee meetings.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 23,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 24,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 25,\n      \"text\": \"          7.8     Agenda\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 26,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 27,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 28,\n      \"text\": \"          7.8.1    The Secretary shall circulate the agenda of the meeting at least seven working days in\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 29,\n      \"text\": \"                 advance of the scheduled date of the meeting to all members.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 30,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 31,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 32,\n      \"text\": \"          7.8.2    The agenda should broadly cover the following:\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 33,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 34,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 35,\n      \"text\": \"                                 i)     Confirmation of minutes\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 36,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 37,\n      \"text\": \"                                    ii)    Chairman’s review/overview of site SHE performance / condition\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 38,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 39,\n      \"text\": \"                                     iii)    Previous month SHE statistics\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 40,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 41,\n      \"text\": \"                          iv)    Incident and Accident Investigation / dangerous occurrence / near miss report\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 42,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 43,\n      \"text\": \"                      v)    Site SHE inspection\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 44,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 45,\n      \"text\": \"                          vi)    Sub-contractors’ SHE issues\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 46,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 47,\n      \"text\": \"                             vii)   Safety presentation by Members\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 48,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 49,\n      \"text\": \"                               viii)  Report from Employer\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 50,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 51,\n      \"text\": \"                          ix)   Matters arising\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 52,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 53,\n      \"text\": \"                      x)   Any other business\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 54,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 55,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 56,\n      \"text\": \"          7.9      Minutes of the meeting\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 57,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 58,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 59,\n      \"text\": \"          7.9.1    The Minutes of the meeting shall be prepared as per the format provided at Form\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 60,\n      \"text\": \"                   No.: SF- 002 and sent to all members within 2 working days preferably by mail/fax\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 61,\n      \"text\": \"                    followed by hardcopy. Safety Committee meeting minutes shall also be displayed in\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 62,\n      \"text\": \"                    the notice board for wider publicity to all concerned.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 63,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 64,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 65,\n      \"text\": \"          7.10     Disciplinary Action\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 66,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 67,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 68,\n      \"text\": \"          7.10.1   The chairman shall inform the members of any outstanding issues in the meeting and\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 69,\n      \"text\": \"                        in case of repeated offence/ non-compliance by some members or other co/sub\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 70,\n      \"text\": \"                    contractors and propose suitable disciplinary action including provisions of monitory\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 71,\n      \"text\": \"                    penalty as per the relevant contract clauses, the Employer shall ensure that the same\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 72,\n      \"text\": \"                          is implemented.\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 73,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 19,\n      \"source_line_number\": 74,\n      \"text\": \"\"\n    }\n  ],\n  \"review_status\": \"pending_manual_review\",\n  \"title\": \"Contractor SHE Committee\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_number_match
  - id: J6af8ef325f51b6bf
    okf_path: OKF_bundle/Technical/Vol3/vol3_appendices_instructions_forms.md
    okf_sha256: 5a0cf8acada1fc881077147ee1d1f7e8c890314febb3371cd8c6cf779f56e738
    heading: Safety, Health and Environment Manual – Appendices, General Instructions and Forms
    source_document: Vol3DLNP1.pdf
    source_sha256: 1ee3fc8dfd12f659f34446b0a6db74e1e1cdd4d593ca91b2a48d59bf1ef97d52
    pdf_pages:
    - 116
    sheet_cells: ''
    json_path: parsed_json/vol3/forms/she_committee_forms.json
    json_sha256: d4d64ab8440b97f6a9deeb0d9cd0b5995bfe88b324ae3231d2f53c8fcbc17a7e
    json_pointer: /forms/0
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"checks\": {\n    \"form_identifier\": \"passed\",\n    \"line_preservation_with_removal_logs\": \"passed\",\n    \"page_sequence\": \"passed\",\n    \"source_hash\": \"passed\"\n  },\n  \"document_role\": \"form_template\",\n  \"field_reconstruction_status\": \"not_performed\",\n  \"form_id\": \"SF/001\",\n  \"fragments\": [\n    {\n      \"pdf_page\": 116,\n      \"text\": \"BANGALORE METRO RAIL CORPORATION LTD.\\n\\n\\n\\n                     FORM No. : SF/001\\n\\n\\n\\n\\n               FORMATION OF SITE SHE COMMITTEE\\n\\n Contract No\\n\\n Contractor Name\\n\\n Contract Title\\n\\n\\n\\n                             CIRCULAR\\n\\n  Committee\\n\\n     The following SHE Committee is constituted with immediate effect:\\n\\n         Chairman:\\n\\n        Members:\\n\\n                    1)\\n\\n                    2)\\n\\n                    3)\\n\\n                    4)\\n\\n                    5)\\n\\n          Secretary:\\n\\n\\n  Periodicity\\n\\n    The committee will meet at least once in a month on the day (specify date)\\n\\n\\n  Agenda\\n\\n     Secretary will circulate agenda of the meeting at least two days in advance of the schedule\\n     date of the meeting.\\n\\n  Circulation\\n\\n  Gist of the meeting will be minuted in the standard format and circulated to the\\n  following under the signature of the secretary\\n\\n           1. Chairman                    3. BMRC Representatives\\n\\n           2. Members                     4. Others concerned\\n\\n\\n\\n\\n  Date:                                            Signed By:      --------------------------\\n\\n                                             CHAIRMAN\"\n    }\n  ],\n  \"pdf_pages\": [\n    116\n  ],\n  \"removed_lines\": [\n    {\n      \"pdf_page\": 116,\n      \"reason\": \"printed_booklet_page_number\",\n      \"source_line_number\": 1,\n      \"text\": \"300\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"reason\": \"manual_page_header\",\n      \"source_line_number\": 2,\n      \"text\": \"                                                                 Safety Health & Environment (SHE) Manual\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"reason\": \"combined_page_footer\",\n      \"source_line_number\": 80,\n      \"text\": \"Bangalore Metro Rail Corporation Ltd.              September 2026     Section Page 112 of 114\"\n    }\n  ],\n  \"retained_lines\": [\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 3,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 4,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 5,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 6,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 7,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 8,\n      \"text\": \"                  BANGALORE METRO RAIL CORPORATION LTD.\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 9,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 10,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 11,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 12,\n      \"text\": \"                     FORM No. : SF/001\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 13,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 14,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 15,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 16,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 17,\n      \"text\": \"               FORMATION OF SITE SHE COMMITTEE\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 18,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 19,\n      \"text\": \" Contract No\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 20,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 21,\n      \"text\": \" Contractor Name\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 22,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 23,\n      \"text\": \" Contract Title\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 24,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 25,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 26,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 27,\n      \"text\": \"                             CIRCULAR\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 28,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 29,\n      \"text\": \"  Committee\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 30,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 31,\n      \"text\": \"     The following SHE Committee is constituted with immediate effect:\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 32,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 33,\n      \"text\": \"         Chairman:\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 34,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 35,\n      \"text\": \"        Members:\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 36,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 37,\n      \"text\": \"                    1)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 38,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 39,\n      \"text\": \"                    2)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 40,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 41,\n      \"text\": \"                    3)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 42,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 43,\n      \"text\": \"                    4)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 44,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 45,\n      \"text\": \"                    5)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 46,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 47,\n      \"text\": \"          Secretary:\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 48,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 49,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 50,\n      \"text\": \"  Periodicity\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 51,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 52,\n      \"text\": \"    The committee will meet at least once in a month on the day (specify date)\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 53,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 54,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 55,\n      \"text\": \"  Agenda\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 56,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 57,\n      \"text\": \"     Secretary will circulate agenda of the meeting at least two days in advance of the schedule\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 58,\n      \"text\": \"     date of the meeting.\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 59,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 60,\n      \"text\": \"  Circulation\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 61,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 62,\n      \"text\": \"  Gist of the meeting will be minuted in the standard format and circulated to the\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 63,\n      \"text\": \"  following under the signature of the secretary\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 64,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 65,\n      \"text\": \"           1. Chairman                    3. BMRC Representatives\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 66,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 67,\n      \"text\": \"           2. Members                     4. Others concerned\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 68,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 69,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 70,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 71,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 72,\n      \"text\": \"  Date:                                            Signed By:      --------------------------\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 73,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 74,\n      \"text\": \"                                             CHAIRMAN\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 75,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 76,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 77,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 78,\n      \"text\": \"\"\n    },\n    {\n      \"pdf_page\": 116,\n      \"source_line_number\": 79,\n      \"text\": \"\"\n    }\n  ],\n  \"review_status\": \"pending_manual_review\",\n  \"source_heading\": {\n    \"form_id\": \"SF/001\",\n    \"pdf_page\": 116,\n    \"source_text\": \"                     FORM No. : SF/001\"\n  },\n  \"source_page_context\": [\n    {\n      \"extraction_method\": \"geometric_sort\",\n      \"has_extracted_text\": true,\n      \"page_rect\": [\n        0.0,\n        0.0,\n        595.219970703125,\n        842.0\n      ],\n      \"pdf_page\": 116,\n      \"review_status\": \"pending_manual_review\",\n      \"rotation\": 0,\n      \"text\": \"300\\n                                                                 Safety Health & Environment (SHE) Manual\\n\\n\\n\\n\\n\\n                  BANGALORE METRO RAIL CORPORATION LTD.\\n\\n\\n\\n                     FORM No. : SF/001\\n\\n\\n\\n\\n               FORMATION OF SITE SHE COMMITTEE\\n\\n Contract No\\n\\n Contractor Name\\n\\n Contract Title\\n\\n\\n\\n                             CIRCULAR\\n\\n  Committee\\n\\n     The following SHE Committee is constituted with immediate effect:\\n\\n         Chairman:\\n\\n        Members:\\n\\n                    1)\\n\\n                    2)\\n\\n                    3)\\n\\n                    4)\\n\\n                    5)\\n\\n          Secretary:\\n\\n\\n  Periodicity\\n\\n    The committee will meet at least once in a month on the day (specify date)\\n\\n\\n  Agenda\\n\\n     Secretary will circulate agenda of the meeting at least two days in advance of the schedule\\n     date of the meeting.\\n\\n  Circulation\\n\\n  Gist of the meeting will be minuted in the standard format and circulated to the\\n  following under the signature of the secretary\\n\\n           1. Chairman                    3. BMRC Representatives\\n\\n           2. Members                     4. Others concerned\\n\\n\\n\\n\\n  Date:                                            Signed By:      --------------------------\\n\\n                                             CHAIRMAN\\n\\n\\n\\n\\n\\nBangalore Metro Rail Corporation Ltd.              September 2026     Section Page 112 of 114\",\n      \"text_blocks\": [\n        {\n          \"bbox\": [\n            36.59998321533203,\n            37.608280181884766,\n            550.6591796875,\n            46.05027770996094\n          ],\n          \"block_number\": 0,\n          \"text\": \"                                                                                                                                   Safety Health & Environment (SHE) Manual \\n\"\n        },\n        {\n          \"bbox\": [\n            71.99996948242188,\n            48.41946029663086,\n            74.76715087890625,\n            57.77189636230469\n          ],\n          \"block_number\": 1,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            71.99996948242188,\n            781.9227294921875,\n            503.2270812988281,\n            803.451416015625\n          ],\n          \"block_number\": 2,\n          \"text\": \"Bangalore Metro Rail Corporation Ltd.                              September 2026         Section Page 112 of 114 \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            100.5599594116211,\n            77.46939849853516,\n            103.32714080810547,\n            86.81187438964844\n          ],\n          \"block_number\": 3,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            200.3999786376953,\n            88.3893814086914,\n            435.4872741699219,\n            97.73185729980469\n          ],\n          \"block_number\": 4,\n          \"text\": \"BANGALORE METRO RAIL CORPORATION LTD. \\n\"\n        },\n        {\n          \"bbox\": [\n            238.79989624023438,\n            127.80321502685547,\n            340.2672119140625,\n            138.1587371826172\n          ],\n          \"block_number\": 5,\n          \"text\": \"FORM No. : SF/001 \\n\"\n        },\n        {\n          \"bbox\": [\n            71.99996948242188,\n            157.1494598388672,\n            74.76715087890625,\n            166.49192810058594\n          ],\n          \"block_number\": 6,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            184.31993103027344,\n            175.20318603515625,\n            394.6271667480469,\n            185.55870056152344\n          ],\n          \"block_number\": 7,\n          \"text\": \"FORMATION OF SITE SHE COMMITTEE \\n\"\n        },\n        {\n          \"bbox\": [\n            77.39997100830078,\n            194.34934997558594,\n            174.0071563720703,\n            203.8118133544922\n          ],\n          \"block_number\": 8,\n          \"text\": \"Contract No \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            77.39997100830078,\n            212.34934997558594,\n            174.00711059570312,\n            221.8118133544922\n          ],\n          \"block_number\": 9,\n          \"text\": \"Contractor Name \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            77.39997100830078,\n            230.34934997558594,\n            174.0071563720703,\n            239.8118133544922\n          ],\n          \"block_number\": 10,\n          \"text\": \"Contract Title \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            288.7198791503906,\n            248.45938110351562,\n            291.487060546875,\n            257.81182861328125\n          ],\n          \"block_number\": 11,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            82.19996643066406,\n            266.3493347167969,\n            316.8071594238281,\n            290.21185302734375\n          ],\n          \"block_number\": 12,\n          \"text\": \"CIRCULAR \\n Committee \\n\"\n        },\n        {\n          \"bbox\": [\n            99.23995971679688,\n            295.4994201660156,\n            396.007568359375,\n            304.85186767578125\n          ],\n          \"block_number\": 13,\n          \"text\": \"The following SHE Committee is constituted with immediate effect: \\n\"\n        },\n        {\n          \"bbox\": [\n            118.20028686523438,\n            309.8994445800781,\n            167.0474395751953,\n            333.7718505859375\n          ],\n          \"block_number\": 14,\n          \"text\": \"Chairman: \\nMembers: \\n\"\n        },\n        {\n          \"bbox\": [\n            118.20028686523438,\n            338.93939208984375,\n            188.1691131591797,\n            420.7717590332031\n          ],\n          \"block_number\": 15,\n          \"text\": \"1) \\n \\n2) \\n \\n3) \\n \\n4) \\n \\n5) \\n \\nSecretary: \\n\"\n        },\n        {\n          \"bbox\": [\n            406.2001953125,\n            425.8292541503906,\n            408.9673767089844,\n            435.1717529296875\n          ],\n          \"block_number\": 16,\n          \"text\": \" \\n\"\n        },\n        {\n          \"bbox\": [\n            82.19996643066406,\n            443.8292541503906,\n            136.08714294433594,\n            453.1717529296875\n          ],\n          \"block_number\": 17,\n          \"text\": \"Periodicity \\n\"\n        },\n        {\n          \"bbox\": [\n            94.79996490478516,\n            458.4593200683594,\n            429.369140625,\n            467.811767578125\n          ],\n          \"block_number\": 18,\n          \"text\": \"The committee will meet at least once in a month on the day (specify date)  \\n\"\n        },\n        {\n          \"bbox\": [\n            82.19996643066406,\n            485.5892639160156,\n            121.6871566772461,\n            494.9317626953125\n          ],\n          \"block_number\": 19,\n          \"text\": \"Agenda \\n\"\n        },\n        {\n          \"bbox\": [\n            94.79996490478516,\n            500.2193298339844,\n            498.2474060058594,\n            521.0917358398438\n          ],\n          \"block_number\": 20,\n          \"text\": \"Secretary will circulate agenda of the meeting at least two days in advance of the schedule \\ndate of the meeting. \\n\"\n        },\n        {\n          \"bbox\": [\n            80.99996948242188,\n            531.0692749023438,\n            501.36761474609375,\n            566.4517211914062\n          ],\n          \"block_number\": 21,\n          \"text\": \"Circulation \\nGist of the meeting will be minuted in the standard format and circulated to the \\nfollowing under the signature of the secretary  \\n\"\n        },\n        {\n          \"bbox\": [\n            118.19999694824219,\n            571.6192626953125,\n            408.96710205078125,\n            609.8916625976562\n          ],\n          \"block_number\": 22,\n          \"text\": \"1. Chairman \\n \\n \\n3. BMRC Representatives \\n2. Members \\n \\n \\n4. Others concerned \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            82.19996643066406,\n            622.3792114257812,\n            490.8202819824219,\n            646.251708984375\n          ],\n          \"block_number\": 23,\n          \"text\": \" \\nDate: \\n \\n \\n \\n \\n Signed By: \\n-------------------------- \\n\"\n        },\n        {\n          \"bbox\": [\n            401.39984130859375,\n            654.471923828125,\n            463.1470947265625,\n            664.8385009765625\n          ],\n          \"block_number\": 24,\n          \"text\": \"CHAIRMAN \\n\"\n        },\n        {\n          \"bbox\": [\n            71.99996948242188,\n            693.17919921875,\n            74.76715087890625,\n            745.9716796875\n          ],\n          \"block_number\": 25,\n          \"text\": \" \\n \\n \\n \\n\"\n        },\n        {\n          \"bbox\": [\n            546.0439453125,\n            24.479991912841797,\n            570.0199584960938,\n            41.38799285888672\n          ],\n          \"block_number\": 26,\n          \"text\": \"300\\n\"\n        }\n      ]\n    }\n  ],\n  \"table_reconstruction_status\": \"not_performed\",\n  \"title\": \"Formation of Site SHE Committee\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: document_heading_fallback_not_a_subclause_match
  created_at: '2026-11-01T12:14:18+00:00'
  status: draft
  editorial_history:
  - previous_claim_id: Cfe6e7ebefda814e0
    previous_evidence_ids:
    - J09eb38685b1042c6
    - J81bb5479e7edcd11
    previous_from_id: ''
    previous_to_id: ''
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
- kind: relation
  text: 'Editorial topic mapping for Amendment Sequence and Unresolved Source Conflicts: the two cited source records are connected for this topic only. The connection is inferred, not an explicit contractual reference, a document-precedence rule or a compliance decision.'
  evidence_ids:
  - J981b70cc6e283023
  - Jcbe0f7287bb5da91
  relation_type: related_to
  explicitness: inferred
  from_id: J981b70cc6e283023
  to_id: Jcbe0f7287bb5da91
  id: Cf311d90ab0a19024
  citations:
  - id: J981b70cc6e283023
    okf_path: OKF_bundle/Technical/Vol1/secA.md
    okf_sha256: 1d19d2821187107d8bead3c38cac38cb70cac496bf9b5b067362f9b891f92cfb
    heading: Key Detail 10 — Online Tender Submission
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol1/section_a_nit/nit_items.json
    json_sha256: ffa851d3dc75c862bbb9df376985067951c7005c988fb0a1002a897b32525b6b
    json_pointer: /key_details/9
    json_record_id: null
    source_review_status: pending_manual_review
    quote: "{\n  \"fragments\": [\n    {\n      \"pdf_page\": 7,\n      \"text\": \"10  Tender  submission  Date  and  Time  03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n         (online)                                3.00 PM) (IST)\"\n    }\n  ],\n  \"number\": 10,\n  \"review_status\": \"pending_manual_review\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_number_match
  - id: Jcbe0f7287bb5da91
    okf_path: OKF_bundle/Technical/Vol1/secA.md
    okf_sha256: 1d19d2821187107d8bead3c38cac38cb70cac496bf9b5b067362f9b891f92cfb
    heading: Key Detail 10 — Online Tender Submission
    source_document: Vol1DLNP1.pdf
    source_sha256: 74441e621d2e627d9132506a894883aff3b5fe3fdfa9600f5be3c7ec394d5c5c
    pdf_pages:
    - 7
    sheet_cells: ''
    json_path: parsed_json/vol1/section_a_nit/nit_table.json
    json_sha256: e4e595fa155f932fe793f28df02a9836eb06f24ca4352db151622db258ce6b10
    json_pointer: /rows/9
    json_record_id: null
    source_review_status: pending_visual_review
    quote: "{\n  \"cell_bboxes\": [\n    [\n      70.54588003719554,\n      479.5196228027344,\n      95.63999938964844,\n      507.71961975097656\n    ],\n    [\n      95.63999938964844,\n      479.5196228027344,\n      284.63999938964844,\n      507.71961975097656\n    ],\n    [\n      284.63999938964844,\n      479.5196228027344,\n      525.6140926585477,\n      507.71961975097656\n    ]\n  ],\n  \"extracted_cells\": [\n    \"10\",\n    \"Tender  submission  Date  and  Time\\n(online)\",\n    \"03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n3.00 PM) (IST)\"\n  ],\n  \"number\": 10,\n  \"original_row_fragments\": [\n    {\n      \"pdf_page\": 7,\n      \"text\": \"10  Tender  submission  Date  and  Time  03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n         (online)                                3.00 PM) (IST)\"\n    }\n  ],\n  \"pdf_page\": 7,\n  \"requirement\": \"Tender  submission  Date  and  Time\\n(online)\",\n  \"review_status\": \"pending_visual_review\",\n  \"token_preservation_check\": \"passed\",\n  \"value\": \"03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\\n3.00 PM) (IST)\"\n}"
    page_basis: Parsed record provenance; not independently PDF-verified
    heading_alignment: exact_number_match
  created_at: '2026-11-01T12:14:18+00:00'
  status: draft
  amendment_annotations:
  - state: superseded
    scope: Baseline NIT Key Detail 10 date/time fields only
    text: 'Preserve the baseline source as history. C1 changes these fields, and C3 further replaces the C1 date/time fields. Latest supplied replacement: 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST). No claim is made about later notices.'
    evidence_ids:
    - J981b70cc6e283023
    - J6b36427c3b2760b1
    - J827a319dc3712125
  - state: superseded
    scope: Baseline NIT Key Detail 10 date/time fields only
    text: 'Preserve the baseline source as history. C1 changes these fields, and C3 further replaces the C1 date/time fields. Latest supplied replacement: 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST). No claim is made about later notices.'
    evidence_ids:
    - Jcbe0f7287bb5da91
    - J6b36427c3b2760b1
    - J827a319dc3712125
  editorial_history:
  - previous_claim_id: C9b992464c99493d8
    previous_text: The cited provisions are grouped by topic for navigation; this is an inferred editorial connection, not an explicit hierarchy or a compliance determination.
    corrected_at: '2026-11-01T12:20:49+00:00'
    method: topic-specific editorial relation label
  - previous_claim_id: Ce1ee913ceff2e5ec
    previous_evidence_ids:
    - J54c382c09ffff5f9
    - J70459e3caeaaef12
    previous_from_id: J54c382c09ffff5f9
    previous_to_id: J70459e3caeaaef12
    migrated_at: '2026-11-01T13:54:09+00:00'
    method: Verified source-identity migration only; claim text unchanged
    migration_manifest: output/provenance_migration/rebase_v1/migration.json
  - previous_claim_id: C65f8a1db37a4b5f6
    previous_relation_type: relates_to
    corrected_at: '2026-11-01T14:33:52+00:00'
    method: Canonical schema relation vocabulary; text, endpoints and citations unchanged
  updated_at: '2026-11-01T12:20:49+00:00'
  last_provenance_migrated: '2026-11-01T13:54:09+00:00'
entity_relations:
- relation_type: related_to
  target: timeline.md
  title: Source topic page
  evidence_ids:
  - Sc18621fd1b08f3e0
source_scope_note: The complete creation prompt explicitly includes matching JSON with each OKF file. These are source-linked extracts, not independent external assumptions. PDF/source review remains pending.
editorial_method: Source-backed editorial synthesis; no new API generation call
last_provenance_migrated: '2026-11-01T13:54:09+00:00'
last_schema_aligned: '2026-11-01T14:33:52+00:00'
---

# Amendment Sequence and Unresolved Source Conflicts

> Draft source synthesis. Pending PDF and human review; no compliance or applicability decision.

## Summary

This page brings together the cited requirements for amendment sequence and unresolved source conflicts. Each source statement retains its own stage, conditions and review limitations. [^e1] [^e2] [^e3] [^e4] [^e5] [^e6] [^e7] [^e8] [^e9] [^e10] [^e11]

The cited source statements remain provisional pending recorded review.

## Key parameters

| Parameter | Value | Citation | Status |
|---|---|---|---|
| NIT Key Detail 10 — Cd7fc0fcc7de94429 | The historical submission sequence is baseline 03-09 October 2026, C1 09-15 October, and C3 09-23 October, with the closing time 3 PM IST. These are recorded tender-history states, not live submission advice. | [^e1] [^e2] [^e3] [^e4] [^e5] [^e6] [^e7] | Pending review; historical fields/provisions have scoped supersession below |
| Contract Data Item 12 — C3275e00059822b5d | The retained DLP discrepancy is six months in Contract Data versus twelve months in the unexecuted Contract Agreement template. Both statements remain visible; no controlling duration is selected here. | [^e8] [^e9] | Pending review |
| SHE 7.0 — Ccbcca28216d54274 | The SHE agenda discrepancy concerns seven working days in 7.8.1 versus two days in SF/001. Monthly Site SHE and weekly Construction SHE committees are distinct provisions, not automatically a frequency contradiction. | [^e10] [^e11] | Pending review |

## Where it appears

- [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]], `Vol1DLNP1.pdf`, PDF p. 7
- [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]], `Vol1DLNP1.pdf`, PDF p. 7 (`parsed_json/vol1/section_a_nit/nit_items.json#/key_details/9`)
- [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]], `Vol1DLNP1.pdf`, PDF p. 7 (`parsed_json/vol1/section_a_nit/nit_table.json#/rows/9`)
- [[OKF_bundle/addendum_and_corrigendum/A_and_C1#Change 2 — Online Tender Submission Date and Time|Corrigendum 1]], `DLN_P1_AandC1_157.PDF`, PDF p. 1
- [[OKF_bundle/addendum_and_corrigendum/A_and_C1#Change 2 — Online Tender Submission Date and Time|Corrigendum 1 Key Detail 10]], `DLN_P1_AandC1_157.PDF`, PDF p. 1 (`parsed_json/addendum_corrigendum/corrigenda_amendments.json#/amendments/0`)
- [[OKF_bundle/addendum_and_corrigendum/A_and_C3#Change 2 — Online Tender Submission Date and Time|Corrigendum 3]], `AandC3_DLN_P1_157.PDF`, PDF p. 1
- [[OKF_bundle/addendum_and_corrigendum/A_and_C3#Change 2 — Online Tender Submission Date and Time|Corrigendum 3 Key Detail 10]], `AandC3_DLN_P1_157.PDF`, PDF p. 1 (`parsed_json/addendum_corrigendum/corrigenda_amendments.json#/amendments/13`)
- [[OKF_bundle/Technical/Vol1/secE#General Conditions of Contract and Contract Data|Contract Data Item 12]], `Vol1DLNP1.pdf`, PDF p. 143 (`parsed_json/vol1/section_e_gcc/contract_data_table.json#/items/10`)
- [[OKF_bundle/Technical/Vol1/secG#Contract Form 1 — Contract Agreement|Contract Forms 1]], `Vol1DLNP1.pdf`, PDF pp. 147, 148, 149, 150 (`parsed_json/vol1/section_g_forms/contract_forms.json#/forms/0`)
- [[OKF_bundle/Technical/Vol3/vol3_part1#Clause 7.0 — Contractor SHE Committee|SHE 7.0]], `Vol3DLNP1.pdf`, PDF pp. 17, 18, 19 (`parsed_json/vol3/part_1_she_management/she_management_clauses.json#/clauses/6`)
- [[OKF_bundle/Technical/Vol3/vol3_appendices_instructions_forms#Safety, Health and Environment Manual – Appendices, General Instructions and Forms|SHE vol3_appendices_instructions_forms]], `Vol3DLNP1.pdf`, PDF p. 116 (`parsed_json/vol3/forms/she_committee_forms.json#/forms/0`)

## Relations

| Source | Relation | Target | Classification | Citation | Status |
|---|---|---|---|---|---|
| NIT Key Detail 10 | related_to | NIT Key Detail 10 | inferred | [^e2] [^e3] | Pending review |

- Editorial topic mapping for Amendment Sequence and Unresolved Source Conflicts: the two cited source records are connected for this topic only. The connection is inferred, not an explicit contractual reference, a document-precedence rule or a compliance decision. [^e2] [^e3]
- **related_to (inferred editorial navigation):** [[wiki/timeline|Source topic page]]. [^e1]

## Open questions and contradictions

No additional conflict is recorded on this page. Verification remains open in [[wiki/review_queue|the review queue]]; absence of a recorded contradiction is not approval.

## Amendment states

Historical source quotations are retained. A superseded field or deleted subclause does not make the entire page superseded.

| Parameter | Value | Citation | Status |
|---|---|---|---|
| Baseline NIT Key Detail 10 date/time fields only | ~~03.10.2026 (From 10.00 AM) to 09.10.2026 (up to 3.00 PM) (IST)~~ → ~~09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)~~ → 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST) | [^e2] [^e5] [^e7] | Superseded historical date/time fields by Corrigendum 3; latest among supplied notices; Pending review |
| Baseline NIT Key Detail 10 date/time fields only | ~~03.10.2026 (From 10.00 AM) to 09.10.2026 (up to 3.00 PM) (IST)~~ → ~~09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)~~ → 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST) | [^e3] [^e5] [^e7] | Superseded historical date/time fields by Corrigendum 3; latest among supplied notices; Pending review |
| C1 date/time fields in the cited source record only | ~~09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)~~ → 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST) | [^e5] [^e7] | Superseded historical date/time fields by Corrigendum 3; latest among supplied notices; Pending review |
| Baseline NIT Key Detail 10 date/time fields only | ~~03.10.2026 (From 10.00 AM) to 09.10.2026 (up to 3.00 PM) (IST)~~ → ~~09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)~~ → 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST) | [^e2] [^e5] [^e7] | Superseded historical date/time fields by Corrigendum 3; latest among supplied notices; Pending review |
| Baseline NIT Key Detail 10 date/time fields only | ~~03.10.2026 (From 10.00 AM) to 09.10.2026 (up to 3.00 PM) (IST)~~ → ~~09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)~~ → 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST) | [^e3] [^e5] [^e7] | Superseded historical date/time fields by Corrigendum 3; latest among supplied notices; Pending review |
| C1 date/time fields in the cited source record only | ~~09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)~~ → 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST) | [^e5] [^e7] | Superseded historical date/time fields by Corrigendum 3; latest among supplied notices; Pending review |
| Baseline NIT Key Detail 10 date/time fields only | ~~03.10.2026 (From 10.00 AM) to 09.10.2026 (up to 3.00 PM) (IST)~~ → ~~09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)~~ → 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST) | [^e2] [^e5] [^e7] | Superseded historical date/time fields by Corrigendum 3; latest among supplied notices; Pending review |
| Baseline NIT Key Detail 10 date/time fields only | ~~03.10.2026 (From 10.00 AM) to 09.10.2026 (up to 3.00 PM) (IST)~~ → ~~09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)~~ → 09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST) | [^e3] [^e5] [^e7] | Superseded historical date/time fields by Corrigendum 3; latest among supplied notices; Pending review |

## Additional source statements


## Claim register

Claim IDs and evidence records are retained in frontmatter. Every draft claim has an entry in [[wiki/review_queue|the claim-level review queue]].

## Citation notes

[^e1]: [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]], `Vol1DLNP1.pdf`, PDF p. 7
[^e2]: [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]], `Vol1DLNP1.pdf`, PDF p. 7 (`parsed_json/vol1/section_a_nit/nit_items.json#/key_details/9`)
[^e3]: [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]], `Vol1DLNP1.pdf`, PDF p. 7 (`parsed_json/vol1/section_a_nit/nit_table.json#/rows/9`)
[^e4]: [[OKF_bundle/addendum_and_corrigendum/A_and_C1#Change 2 — Online Tender Submission Date and Time|Corrigendum 1]], `DLN_P1_AandC1_157.PDF`, PDF p. 1
[^e5]: [[OKF_bundle/addendum_and_corrigendum/A_and_C1#Change 2 — Online Tender Submission Date and Time|Corrigendum 1 Key Detail 10]], `DLN_P1_AandC1_157.PDF`, PDF p. 1 (`parsed_json/addendum_corrigendum/corrigenda_amendments.json#/amendments/0`)
[^e6]: [[OKF_bundle/addendum_and_corrigendum/A_and_C3#Change 2 — Online Tender Submission Date and Time|Corrigendum 3]], `AandC3_DLN_P1_157.PDF`, PDF p. 1
[^e7]: [[OKF_bundle/addendum_and_corrigendum/A_and_C3#Change 2 — Online Tender Submission Date and Time|Corrigendum 3 Key Detail 10]], `AandC3_DLN_P1_157.PDF`, PDF p. 1 (`parsed_json/addendum_corrigendum/corrigenda_amendments.json#/amendments/13`)
[^e8]: [[OKF_bundle/Technical/Vol1/secE#General Conditions of Contract and Contract Data|Contract Data Item 12]], `Vol1DLNP1.pdf`, PDF p. 143 (`parsed_json/vol1/section_e_gcc/contract_data_table.json#/items/10`)
[^e9]: [[OKF_bundle/Technical/Vol1/secG#Contract Form 1 — Contract Agreement|Contract Forms 1]], `Vol1DLNP1.pdf`, PDF pp. 147, 148, 149, 150 (`parsed_json/vol1/section_g_forms/contract_forms.json#/forms/0`)
[^e10]: [[OKF_bundle/Technical/Vol3/vol3_part1#Clause 7.0 — Contractor SHE Committee|SHE 7.0]], `Vol3DLNP1.pdf`, PDF pp. 17, 18, 19 (`parsed_json/vol3/part_1_she_management/she_management_clauses.json#/clauses/6`)
[^e11]: [[OKF_bundle/Technical/Vol3/vol3_appendices_instructions_forms#Safety, Health and Environment Manual – Appendices, General Instructions and Forms|SHE vol3_appendices_instructions_forms]], `Vol3DLNP1.pdf`, PDF p. 116 (`parsed_json/vol3/forms/she_committee_forms.json#/forms/0`)

<details>
<summary>Supporting source passages</summary>

### Sc18621fd1b08f3e0

[[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]], `Vol1DLNP1.pdf`, PDF p. 7

> - **Submission Period:** 03.10.2026, from 10.00 AM, to 09.10.2026, up to 3.00 PM (IST).

### J981b70cc6e283023

[[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]], `Vol1DLNP1.pdf`, PDF p. 7 (`parsed_json/vol1/section_a_nit/nit_items.json#/key_details/9`)

> {
>   "fragments": [
>     {
>       "pdf_page": 7,
>       "text": "10  Tender  submission  Date  and  Time  03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\n         (online)                                3.00 PM) (IST)"
>     }
>   ],
>   "number": 10,
>   "review_status": "pending_manual_review"
> }

### Jcbe0f7287bb5da91

[[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]], `Vol1DLNP1.pdf`, PDF p. 7 (`parsed_json/vol1/section_a_nit/nit_table.json#/rows/9`)

> {
>   "cell_bboxes": [
>     [
>       70.54588003719554,
>       479.5196228027344,
>       95.63999938964844,
>       507.71961975097656
>     ],
>     [
>       95.63999938964844,
>       479.5196228027344,
>       284.63999938964844,
>       507.71961975097656
>     ],
>     [
>       284.63999938964844,
>       479.5196228027344,
>       525.6140926585477,
>       507.71961975097656
>     ]
>   ],
>   "extracted_cells": [
>     "10",
>     "Tender  submission  Date  and  Time\n(online)",
>     "03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\n3.00 PM) (IST)"
>   ],
>   "number": 10,
>   "original_row_fragments": [
>     {
>       "pdf_page": 7,
>       "text": "10  Tender  submission  Date  and  Time  03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\n         (online)                                3.00 PM) (IST)"
>     }
>   ],
>   "pdf_page": 7,
>   "requirement": "Tender  submission  Date  and  Time\n(online)",
>   "review_status": "pending_visual_review",
>   "token_preservation_check": "passed",
>   "value": "03.10.2026 (From 10.00 AM) to 09.10.2026 (up to\n3.00 PM) (IST)"
> }

### S69a6c3139d9e4c35

[[OKF_bundle/addendum_and_corrigendum/A_and_C1#Change 2 — Online Tender Submission Date and Time|Corrigendum 1]], `DLN_P1_AandC1_157.PDF`, PDF p. 1

> - **Amends:** [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]]
> - **Change type:** Replace submission-window dates
> - **Old value:** 03.10.2026 from 10.00 AM to 09.10.2026 up to 3.00 PM IST
> - **New value:** 09.10.2026 from 10.00 AM to 15.10.2026 up to 3.00 PM IST
> - **Evidence:** `DLN_P1_AandC1_157.PDF`, PDF page 1, amendment serial 1
> - **Affected booklet page:** 001
> 
> Both the opening date and closing date of the submission window change.

### J6b36427c3b2760b1

[[OKF_bundle/addendum_and_corrigendum/A_and_C1#Change 2 — Online Tender Submission Date and Time|Corrigendum 1 Key Detail 10]], `DLN_P1_AandC1_157.PDF`, PDF p. 1 (`parsed_json/addendum_corrigendum/corrigenda_amendments.json#/amendments/0`)

> {
>   "affected_reference": "Key Detail 10",
>   "affected_section": "NIT",
>   "booklet_page_reference": "001",
>   "corrigendum_number": 1,
>   "document_date": "2026-10-01",
>   "existing_selected_text": "03.10.2026 (From 10.00 AM) to 09.10.2026 (up to 3.00 PM) (IST)",
>   "field_provenance": "Prepared from visual inspection of the source scan; not automatically inferred from OCR",
>   "label": "Tender submission Date and Time (online)",
>   "ocr_evidence_relative_to_project": "output/corrigenda/ocr/run_20261030T051229372457Z/corrigendum_1/ocr.json",
>   "operation": "replace_date_time_fields",
>   "pdf_pages": [
>     1
>   ],
>   "printed_amendment_serial": "1",
>   "record_id": "corrigendum_1/nit_key_detail_10",
>   "replacement_selected_text": "09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)",
>   "review_status": "pending_manual_review",
>   "scope": "Date/time fields only; other wording, venue and submission conditions are retained in the source OCR",
>   "source_document": "DLN_P1_AandC1_157.PDF",
>   "source_sha256": "26b25a4e3c3d3206635d0ddae6ce70c00e51468ebb4fe5d93f5e9d65902942d1",
>   "transcription_scope": "Selected amendment wording and fields, not a complete verbatim table transcription"
> }

### S833aa656a16da78a

[[OKF_bundle/addendum_and_corrigendum/A_and_C3#Change 2 — Online Tender Submission Date and Time|Corrigendum 3]], `AandC3_DLN_P1_157.PDF`, PDF p. 1

> - **Underlying NIT entry:** [[OKF_bundle/Technical/Vol1/secA#Key Detail 10 — Online Tender Submission|NIT Key Detail 10]]
> - **Change type:** Replace the submission-window closing date
> - **Old value:** 09.10.2026 from 10.00 AM to 15.10.2026 up to 3.00 PM IST
> - **New value:** 09.10.2026 from 10.00 AM to 23.10.2026 up to 3.00 PM IST
> - **Evidence:** `AandC3_DLN_P1_157.PDF`, PDF page 1, amendment serial 1
> - **Replaces:** Corrigendum 1, serial 1, Key Detail 10 date fields
> 
> The opening date remains 09.10.2026. It is not changed to 16.10.2026.

### J827a319dc3712125

[[OKF_bundle/addendum_and_corrigendum/A_and_C3#Change 2 — Online Tender Submission Date and Time|Corrigendum 3 Key Detail 10]], `AandC3_DLN_P1_157.PDF`, PDF p. 1 (`parsed_json/addendum_corrigendum/corrigenda_amendments.json#/amendments/13`)

> {
>   "affected_reference": "Key Detail 10",
>   "affected_section": "NIT",
>   "corrigendum_number": 3,
>   "document_date": "2026-10-13",
>   "existing_selected_text": "09.10.2026 (From 10.00 AM) to 15.10.2026 (up to 3.00 PM) (IST)",
>   "field_provenance": "Prepared from visual inspection of the source scan; not automatically inferred from OCR",
>   "label": "Tender submission Date and Time (online)",
>   "ocr_evidence_relative_to_project": "output/corrigenda/ocr/run_20261030T051229372457Z/corrigendum_3/ocr.json",
>   "operation": "replace_date_time_fields",
>   "pdf_pages": [
>     1
>   ],
>   "printed_amendment_serial": "1",
>   "printed_cross_reference": "Sl.No 1 of Addendum and Corrigendum No. 1 Dated 01-10-2026",
>   "record_id": "corrigendum_3/nit_key_detail_10",
>   "replacement_selected_text": "09.10.2026 (From 10.00 AM) to 23.10.2026 (up to 3.00 PM) (IST)",
>   "replaces_record_id": "corrigendum_1/nit_key_detail_10",
>   "review_status": "pending_manual_review",
>   "scope": "Date/time fields only; other wording, venue and submission conditions are retained in the source OCR",
>   "source_document": "AandC3_DLN_P1_157.PDF",
>   "source_sha256": "623067baa7cb9d7b2863567fea861767f42102f9e16ff3c2b547afed554280de",
>   "transcription_scope": "Selected amendment wording and fields, not a complete verbatim table transcription"
> }

### Jeb83d1b7a6d87fee

[[OKF_bundle/Technical/Vol1/secE#General Conditions of Contract and Contract Data|Contract Data Item 12]], `Vol1DLNP1.pdf`, PDF p. 143 (`parsed_json/vol1/section_e_gcc/contract_data_table.json#/items/10`)

> {
>   "cell_bboxes": [
>     [
>       72.21599807739258,
>       99.359619140625,
>       104.15999603271484,
>       146.27963256835938
>     ],
>     [
>       104.15999603271484,
>       99.359619140625,
>       256.3199920654297,
>       146.27963256835938
>     ],
>     [
>       256.3199920654297,
>       99.359619140625,
>       568.2239837646484,
>       146.27963256835938
>     ]
>   ],
>   "item_number": 12,
>   "pdf_page": 143,
>   "raw_cells": [
>     "12",
>     "Defects Liability Period\n\n(GCC Sub-Clause 10)",
>     "Defects Liability Period is 6 months from the date of Taking over\nmentioned in Taking Over Certificates being issued for whole of\nthe work."
>   ],
>   "requirement": "Defects Liability Period\n\n(GCC Sub-Clause 10)",
>   "review_status": "pending_visual_review",
>   "source_row_label": "12",
>   "table_bbox": [
>     72.21599807739258,
>     46.2596435546875,
>     568.2239837646484,
>     476.3396186828613
>   ],
>   "value": "Defects Liability Period is 6 months from the date of Taking over\nmentioned in Taking Over Certificates being issued for whole of\nthe work."
> }

### Jcc49f8beaf50a801

[[OKF_bundle/Technical/Vol1/secG#Contract Form 1 — Contract Agreement|Contract Forms 1]], `Vol1DLNP1.pdf`, PDF pp. 147, 148, 149, 150 (`parsed_json/vol1/section_g_forms/contract_forms.json#/forms/0`)

> {
>   "document_role": "template",
>   "form_id": "contract_form_1",
>   "form_number": "1",
>   "fragments": [
>     {
>       "pdf_page": 147,
>       "text": "CONTRACT FORM- 1\n\n\n                      CONTRACT AGREEMENT\n\n       This Contract Agreement (hereinafter called the “Contract”) is made at Bangalore on ……..…day of\n\n    ……………by and between:\n\n       Bangalore Metro Rail Corporation Limited, a company incorporated under companies act 1956\n       represented by the Managing Director, with office located at  III Floor, BMTC Complex, K.H.Road,\n        Shantinagar, Bangalore 560 027, hereinafter referred to as the “BMRCL” or the “Employer”, as the\n       case may be, which expression shall unless excluded by or repugnant to the context or meaning thereof\n      be deemed to include its successors and assigns of the one part, and;\n\n          .........................................................…………………….. [Note 1] comprising:\n\na)          ........................................................,  a  company  registered  and  existing  under  the  laws  of\n\n             ................................, with head office located at ........................................................, represented by\n\n       Mr.  ....................................... and Mr.  ....................................... authorised  to sign and bind the\n\n       company, under the Power of Attorney  dated...................................... and the Board Resolution\n\n            dated..................................... [Note 5] AND\n\nb)          ........................................................,  a  company  registered  and  existing  under  the  laws  of\n\n             ................................, with head office located at................................................................ represented\n\n       by Mr.  ....................................... and Mr.  ....................................... authorised to sign and bind the\n\n       company, under the Power of Attorney  dated...................................... and the Board Resolution\n\n            dated..................................... [Note 5] AND\n\nc)          ........................................................,  a  company  registered  and  existing  under  the  laws  of\n\n             ................................, with head office located at................................................................ represented\n\n       by Mr.  ....................................... and Mr.  ....................................... authorised to sign and bind the\n\n       company, under the Power of Attorney  dated...................................... and the Board Resolution\n\n            dated..................................... [Note 5]\n\n\n\n       [Note 2] who each of which shall be jointly and severally responsible to the Employer under the Contract\n         for the Bangalore Metro Rail Project as per conditions agreed to by the Employer;\n\n\n        Hereinafter [Note 3] collectively referred to as the “Contractor” which expression shall unless excluded\n       by or repugnant to the context or meaning thereof be deemed to include its successors and assigns of\n        the other part.\n\n\n     WHEREAS the Contractor has established a ........................[Note 4] in accordance with Indian law and\n        offered a tender for the construction of a rail based mass rapid transport system by execution and\n        completion, and remedying any defects in the Works of:(Name of the work)----------------------------------\n           ------------------------------------------------------------------------------------------------------------------------------\n\n      Tender Notification No ---------------------------------------------------- Dated --.--. ----. and agrees to undertake\n       performance of the Work under the terms and conditions set forth in this Contract.\n\n\n     AND WHEREAS the Employer agrees to hire and the Contractor agrees to be hired to implement\n       the:(Name of the work)-------------------------------------------------------------------------------------------------------\n           ---------------------------------------------------------\n\n       Tender Notification No ---------------------------------------------------- Dated --.--. ----.\n\n       Under the terms and conditions specified  in  this Contract Agreement and the other Contract\n       Documents.\n     Now THEREFORE the parties hereby agree as follows:"
>     },
>     {
>       "pdf_page": 148,
>       "text": "Clause 1 Words and Expression\n\n             In this Contract all the words and expressions shall have the same meanings as are respectively\n           assigned to them in the conditions of contract hereinafter referred to,\n\n   Clause 2  the Contract Documents,\n\n          The following shall deem to form and be read and construed as a part of this Contract Agreement\n\n            provided any of the provisions therein are not inconsistent with the present contract agreement:\n              1.  Letter of Acceptance.\n\n              2.  Clarifications, Addenda, Corrigenda Issued to Tender document (if any)\n\n              3.  Pricing Document\n\n              4.  Special Conditions of Contract\n\n              5.  Contract forms\n\n              6.  General Conditions of Contract\n\n              7.  Employer’s Requirement & Technical Specifications\n\n              8.  Drawings\n\n              9.  Any other document forming part of the Contract\n\n               All of the foregoing documents, together with this Contract Agreement, referred to herein as the\n            Contract.  Also incorporated into the Contract, and made part hereof, are  all Standard codes,\n             specifications of MORTH/CPWD/KPWD/IRS as applicable, and similar requirements that are referred\n             to therein. The ‘Priority of documents’ will be as given in clause 1.5 of GCC.\n\n   Clause 3 Obligations of the Contractor:\n\n         The mutual rights and Obligations of the Employer and the Contractor shall be as set forth in the\n            contract and in particular: -\n\n           3.1 The Contractor agrees, subject to the terms and conditions of the Contract, to perform efficiently\n          and faithfully all of the work of (Name of the work)-------------------------------------------------------------------\n                ---------------------------------------------------------------------------------------------\n\n          Tender Notification No  ---------------------------------------------------- Dated  --.--. ----.and other  facilities\n             requisite for or incidental to the successful completion of the Works and in carrying out all duties and\n            obligations imposed by the Contract.\n\n\n            3.2 The Contractor shall remedy, at no extra cost to the Employer, the defect or failure (fair wear and\n             tear excluded) after any part of the Work are taken over by the Employer until the end of Defects\n               Liability Period.\n\n            3.3 The Contractor shall also remedy, at no extra cost to the Employer, the defect or failure of any\n           equipment provided in the Works and any defects in materials supplied and workmanship up to end\n             of warranty period.\n\n   Clause 4 Obligations of the Employer:\n\n         The Employer agrees, subject to the terms and conditions of the Contract, to pay the Contractor the\n         amount specified, and at the rates and terms and in the manner set forth in the Contract.\n\n   Clause 5 Contract Price:\n\n             5.1. Employer agrees to pay the Contractor total amount mentioned below (hereinafter called 'the\n            Contract Price') and the Contractor agrees to accept the total amount mentioned below for the\n            execution, completion, maintenance / rectification of defects and guarantee for the works carried out\n          by him as part of his obligations, responsibilities and liabilities under and according to the provisions\n          and obligations imposed on him by the Contract.\n\n\n\n                    (i)      Indian Rupees……………………………………...  (....................................Rs.) and Output\n\n              GST as applicable."
>     },
>     {
>       "pdf_page": 149,
>       "text": "5.2. The contract price mentioned above  will be increased or decreased during the period of\n        performance of the contract as specifically provided,  if any, in the General or Special Conditions of\n         Contract and no additional amount for any other account whatsoever shall be payable to the Contractor.\n\n Clause 6 Completion Time:\n\n       The Contractor shall complete whole of the Works within.............................. (.........) months from the\n       Commencement Date (date of signing the ‘Contract Agreement’). The Defect Liability Period is 12\n         (Twelve) months from the date mentioned in the Final Taking over Certificate for whole of the Works.\n\n Clause7 Integration\n\n       The Employer and the Contractor agree that this Contract Agreement, together with the other Contract\n        Documents, expresses all of the agreements, understandings, promises, and covenants of the parties,\n        and  integrates,  combines,  and  supersedes   all  prior  and  contemporaneous  negotiations,\n         understandings, and agreements, whether written or oral and no modification or alteration of the\n         Contract Documents shall be valid or binding on either party, unless expressed in writing and executed\n          with the same formality as this Contract Agreement, except as may otherwise be specifically provided\n           in the Contract Documents.\n\n Clause 8 Governing Law\n\n         This Contract is enforceable and construed under the applicable laws of the Republic of India.\n\n Clause 9 Language\n\n         This Contract Agreement and the other Contract Documents are made in the English language.\n\nClause 9-A Notices:\n\n       The Address for service of all documents / notices arising out of or in connection with this contract\n          shall be:\n           (a) Upon Employer: Bangalore Metro Rail Corporation Ltd, 3rd Floor, BMTC Complex, K.H. Road,\n             Shantinagar, Bengaluru – 560027, Karnataka, India.\n           Marked for the attention of Executive Director.\n           (b) Upon the Contractor: --------------------------------------------------------------------(Name and address of\n              the contractor)\n           The above notices can be sent either by E-mail to the respective E-mail addresses of the parties\n              or by registered post to the above mentioned addresses of the parties.\n\n Clause 10 Jurisdiction of Court\n\n       The Courts at Bangalore shall have the exclusive jurisdiction in respect of all the disputes arising out\n          of this Agreement between the parties.\n\n\n        IN WITNESS WHEREOF, the parties hereto have caused this Contract to be signed in their respective\n\n       names by their authorised representatives as of the day and year first above written\n\n                  For BMRCL                       [Note 6] for …………...................,\n              The Employer                       The Contractor\n              Bangalore Metro Rail                           (a) …………………………………….\n                Corporation Limited                  …………………………………….\n\n\n\n                      (                         )                                    (                         )\n                       --------------------------                                     --------------------------\n\n\n               WITNESS\n\n\n                                                               (b) For …………………………………….\n                      (                         )              ……………………………\n                       --------------------------"
>     },
>     {
>       "pdf_page": 150,
>       "text": "(                         )\n                                                                                         --------------------------\n\n\n                                                                           (c) …………………………………….\n                              ……………………………\n\n\n\n                                                                                         (                         )\n                                                                                         --------------------------\n\n\n\n\n\n                                                          WITNESS\n\n\n\n                                                                                               (                      )\n                                                                                             --------------------------\n\n\n\n\n\n   Notes:  (for preparation of but not for inclusion in the engrossment of the Contract Agreement)\n\n   1           If the Contractor comprises a partnership, joint venture, liability will be joint and several, and each\n\n         member thereof must be identified.\n\n    2.       In the case that the Contractor comprises a single company, this line should be deleted entirely, as\n\n            also should be paragraphs (b) and (c) above.\n\n    3.       In the case that the Contractor comprises a single company, the word “collectively” should be deleted\n\n           from this line.\n\n    4.      Enter the appropriate nature of the Contractor; company, partnership, joint venture as the case may\n\n           be.\n\n    5.      Enter the date of the appropriate resolution.\n\n    6.          If the Contractor comprises a partnership, joint venture, each member thereof must execute.\n\n    7.     The required Stamp duty in accordance with Karnataka Stamp Act is to be borne by the contractor."
>     }
>   ],
>   "heading_line": "CONTRACT FORM- 1",
>   "review_status": "pending_manual_review",
>   "title": "Contract Agreement"
> }

### J9eeb4ca708ebff86

[[OKF_bundle/Technical/Vol3/vol3_part1#Clause 7.0 — Contractor SHE Committee|SHE 7.0]], `Vol3DLNP1.pdf`, PDF pp. 17, 18, 19 (`parsed_json/vol3/part_1_she_management/she_management_clauses.json#/clauses/6`)

> {
>   "clause_id": "7.0",
>   "fragments": [
>     {
>       "pdf_page": 17,
>       "text": "7.0      Contractor SHE Committee\n\n\n          7.1         All employees should be  able  to  participate  in the making and monitoring  of\n                  arrangements for safety, industrial health and environment at their place of work. The\n                   establishment of site SHE committees in which employees and Contractor and sub-\n                     contractor  management  are  represented  can  increase  the  involvement  and\n                 commitment of employees. The contractor shall ensure the formation and monitor the\n                     functioning of contractor SHE committees.\n\n\n          7.2      Terms of Reference\n\n\n          7.2.1    The Terms of Reference for the committee shall be as follows;\n\n\n                                 i)    To establish company safety policies and practices\n\n                                    ii)   To monitor the adequacy of the contractor’s site SHE plan and ensure  its\n                        implementation\n\n                                     iii)   To review SHE training"
>     },
>     {
>       "pdf_page": 18,
>       "text": "iv)   To review the contractor’s monthly SHE report.\n\n           v)   To identify probable causes of accident and unsafe practices in building or other\n                construction work and to suggest remedial measures.\n\n             vi)   To stimulate interest of Employer and building workers in safety by organizing\n                safety week, safety competition, talks and film-shows on safety, preparing\n               posters or taking similar other measures as and when required or as necessary.\n\n              vii)  To go round the construction site with a view to check unsafe practices and\n                detect unsafe  conditions and  to recommend remedial measures  for  their\n                  rectifications including first-aid medical and welfare facilities.\n\n               viii)  Committee team members should perform a  site inspection before every\n              committee meetings and to monitor SHE inspection reports.\n\n             ix)   To bring to the notice of the Employer the hazards associated with use, handling\n             and maintenance of the equipment used during the course of building and other\n                construction work\n\n           x)   To suggest measures for improving welfare amenities in the construction site\n             and other miscellaneous aspect of safety, health and welfare in building or other\n                construction work.\n\n             xi)   To look into the health hazards associated with handling different types of\n                explosives, chemicals and other construction materials and to suggest remedial\n             measures including personal protective equipment.\n\n              xii)  To review the last safety committee meeting minutes and to take action against\n               persons/sub-contractors for non-compliance if any.\n\n\n7.3       Within 14 days of award of contract, the SHE committee shall be constituted and\n           notification regarding the same shall be communicated to the members and employees\n         as per the format provided in Form No.: SF 001\n\n\n7.4       Site SHE Committee meeting shall be conducted at least once in a month with the\n        minimum members listed below:\n\n         Chairman           Project Manager\n\n           Secretary       SHE Manager (In-charge)\n        Members                     i)   Labour Welfare Officer\n                                                           ii)   In charge of plant and machinery\n                                                            iii)  In charge of site electrics\n                                           iv)  In charge of stores.\n                                    v)  Senior  Managers/  Engineers  heading   different  sub\n                                        functions.\n                                           vi)  Sub – contractor’s representative\n                                               vii) Labour Contractor’s representative\n                                                  viii) Workers’ representative\n                                           ix)  Co-contractor representative.\n                                    x)  SHE staffs\n          Employer’s\n                   BMRC SHE in charge and other representatives\n          Representatives\n\n\n 7.5    Construction SHE Committee meeting shall be conducted at least once in a week with the\n      minimum members listed below:\n\n    Chairman  Project Manager\n\n     Secretary  SHE Manager (In-charge)\n    Members     i)   Labour Welfare Officer\n                               ii)   In charge of plant and machinery\n                               iii)  In-charge of site electricity\n                      iv)  Senior Managers / Engineers heading different sub functions\n                   v)   Sub- Contractor’s representative\n                      vi)  Labour contractor’s representative\n                         vii)  Workers’ representatives\n                          viii)  All SHE Staffs"
>     },
>     {
>       "pdf_page": 19,
>       "text": "7.6      Co-contractors’ participation\n\n\n          7.6.1      In case of depot, station and other contiguous areas where more than one main\n                    contractors are working together, the Employer shall instruct the other contractors to\n                        join for the monthly SHE committee meeting of the main civil contractor, so as to\n                   discuss and decide about the common provision of security, lighting, toilet, drinking\n                   water etc. and sharing the maintenance cost of the same etc.\n\n\n          7.6.2    The general principle for sharing the cost shall be either based on the contract\n                  value of works executed at the contiguous area or the daily average number of\n               workmen employed by each contractor in the contiguous area.\n\n\n          7.7     Minimum time between two monthly SHE Committee meetings\n\n\n          7.7.1    A minimum period of 21 days shall be maintained between any two SHE monthly\n                  committee meetings.\n\n\n          7.8     Agenda\n\n\n          7.8.1    The Secretary shall circulate the agenda of the meeting at least seven working days in\n                 advance of the scheduled date of the meeting to all members.\n\n\n          7.8.2    The agenda should broadly cover the following:\n\n\n                                 i)     Confirmation of minutes\n\n                                    ii)    Chairman’s review/overview of site SHE performance / condition\n\n                                     iii)    Previous month SHE statistics\n\n                          iv)    Incident and Accident Investigation / dangerous occurrence / near miss report\n\n                      v)    Site SHE inspection\n\n                          vi)    Sub-contractors’ SHE issues\n\n                             vii)   Safety presentation by Members\n\n                               viii)  Report from Employer\n\n                          ix)   Matters arising\n\n                      x)   Any other business\n\n\n          7.9      Minutes of the meeting\n\n\n          7.9.1    The Minutes of the meeting shall be prepared as per the format provided at Form\n                   No.: SF- 002 and sent to all members within 2 working days preferably by mail/fax\n                    followed by hardcopy. Safety Committee meeting minutes shall also be displayed in\n                    the notice board for wider publicity to all concerned.\n\n\n          7.10     Disciplinary Action\n\n\n          7.10.1   The chairman shall inform the members of any outstanding issues in the meeting and\n                        in case of repeated offence/ non-compliance by some members or other co/sub\n                    contractors and propose suitable disciplinary action including provisions of monitory\n                    penalty as per the relevant contract clauses, the Employer shall ensure that the same\n                          is implemented."
>     }
>   ],
>   "heading_line": "          7.0      Contractor SHE Committee",
>   "retained_lines": [
>     {
>       "pdf_page": 17,
>       "source_line_number": 54,
>       "text": "          7.0      Contractor SHE Committee"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 55,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 56,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 57,
>       "text": "          7.1         All employees should be  able  to  participate  in the making and monitoring  of"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 58,
>       "text": "                  arrangements for safety, industrial health and environment at their place of work. The"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 59,
>       "text": "                   establishment of site SHE committees in which employees and Contractor and sub-"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 60,
>       "text": "                     contractor  management  are  represented  can  increase  the  involvement  and"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 61,
>       "text": "                 commitment of employees. The contractor shall ensure the formation and monitor the"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 62,
>       "text": "                     functioning of contractor SHE committees."
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 63,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 64,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 65,
>       "text": "          7.2      Terms of Reference"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 66,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 67,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 68,
>       "text": "          7.2.1    The Terms of Reference for the committee shall be as follows;"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 69,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 70,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 71,
>       "text": "                                 i)    To establish company safety policies and practices"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 72,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 73,
>       "text": "                                    ii)   To monitor the adequacy of the contractor’s site SHE plan and ensure  its"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 74,
>       "text": "                        implementation"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 75,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 76,
>       "text": "                                     iii)   To review SHE training"
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 77,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 78,
>       "text": ""
>     },
>     {
>       "pdf_page": 17,
>       "source_line_number": 79,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 3,
>       "text": "             iv)   To review the contractor’s monthly SHE report."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 4,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 5,
>       "text": "           v)   To identify probable causes of accident and unsafe practices in building or other"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 6,
>       "text": "                construction work and to suggest remedial measures."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 7,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 8,
>       "text": "             vi)   To stimulate interest of Employer and building workers in safety by organizing"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 9,
>       "text": "                safety week, safety competition, talks and film-shows on safety, preparing"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 10,
>       "text": "               posters or taking similar other measures as and when required or as necessary."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 11,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 12,
>       "text": "              vii)  To go round the construction site with a view to check unsafe practices and"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 13,
>       "text": "                detect unsafe  conditions and  to recommend remedial measures  for  their"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 14,
>       "text": "                  rectifications including first-aid medical and welfare facilities."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 15,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 16,
>       "text": "               viii)  Committee team members should perform a  site inspection before every"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 17,
>       "text": "              committee meetings and to monitor SHE inspection reports."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 18,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 19,
>       "text": "             ix)   To bring to the notice of the Employer the hazards associated with use, handling"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 20,
>       "text": "             and maintenance of the equipment used during the course of building and other"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 21,
>       "text": "                construction work"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 22,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 23,
>       "text": "           x)   To suggest measures for improving welfare amenities in the construction site"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 24,
>       "text": "             and other miscellaneous aspect of safety, health and welfare in building or other"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 25,
>       "text": "                construction work."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 26,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 27,
>       "text": "             xi)   To look into the health hazards associated with handling different types of"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 28,
>       "text": "                explosives, chemicals and other construction materials and to suggest remedial"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 29,
>       "text": "             measures including personal protective equipment."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 30,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 31,
>       "text": "              xii)  To review the last safety committee meeting minutes and to take action against"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 32,
>       "text": "               persons/sub-contractors for non-compliance if any."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 33,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 34,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 35,
>       "text": "7.3       Within 14 days of award of contract, the SHE committee shall be constituted and"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 36,
>       "text": "           notification regarding the same shall be communicated to the members and employees"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 37,
>       "text": "         as per the format provided in Form No.: SF 001"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 38,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 39,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 40,
>       "text": "7.4       Site SHE Committee meeting shall be conducted at least once in a month with the"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 41,
>       "text": "        minimum members listed below:"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 42,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 43,
>       "text": "         Chairman           Project Manager"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 44,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 45,
>       "text": "           Secretary       SHE Manager (In-charge)"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 46,
>       "text": "        Members                     i)   Labour Welfare Officer"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 47,
>       "text": "                                                           ii)   In charge of plant and machinery"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 48,
>       "text": "                                                            iii)  In charge of site electrics"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 49,
>       "text": "                                           iv)  In charge of stores."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 50,
>       "text": "                                    v)  Senior  Managers/  Engineers  heading   different  sub"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 51,
>       "text": "                                        functions."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 52,
>       "text": "                                           vi)  Sub – contractor’s representative"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 53,
>       "text": "                                               vii) Labour Contractor’s representative"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 54,
>       "text": "                                                  viii) Workers’ representative"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 55,
>       "text": "                                           ix)  Co-contractor representative."
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 56,
>       "text": "                                    x)  SHE staffs"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 57,
>       "text": "          Employer’s"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 58,
>       "text": "                   BMRC SHE in charge and other representatives"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 59,
>       "text": "          Representatives"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 60,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 61,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 62,
>       "text": " 7.5    Construction SHE Committee meeting shall be conducted at least once in a week with the"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 63,
>       "text": "      minimum members listed below:"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 64,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 65,
>       "text": "    Chairman  Project Manager"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 66,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 67,
>       "text": "     Secretary  SHE Manager (In-charge)"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 68,
>       "text": "    Members     i)   Labour Welfare Officer"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 69,
>       "text": "                               ii)   In charge of plant and machinery"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 70,
>       "text": "                               iii)  In-charge of site electricity"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 71,
>       "text": "                      iv)  Senior Managers / Engineers heading different sub functions"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 72,
>       "text": "                   v)   Sub- Contractor’s representative"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 73,
>       "text": "                      vi)  Labour contractor’s representative"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 74,
>       "text": "                         vii)  Workers’ representatives"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 75,
>       "text": "                          viii)  All SHE Staffs"
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 76,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 77,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 78,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 79,
>       "text": ""
>     },
>     {
>       "pdf_page": 18,
>       "source_line_number": 80,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 3,
>       "text": "          7.6      Co-contractors’ participation"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 4,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 5,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 6,
>       "text": "          7.6.1      In case of depot, station and other contiguous areas where more than one main"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 7,
>       "text": "                    contractors are working together, the Employer shall instruct the other contractors to"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 8,
>       "text": "                        join for the monthly SHE committee meeting of the main civil contractor, so as to"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 9,
>       "text": "                   discuss and decide about the common provision of security, lighting, toilet, drinking"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 10,
>       "text": "                   water etc. and sharing the maintenance cost of the same etc."
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 11,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 12,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 13,
>       "text": "          7.6.2    The general principle for sharing the cost shall be either based on the contract"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 14,
>       "text": "                  value of works executed at the contiguous area or the daily average number of"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 15,
>       "text": "               workmen employed by each contractor in the contiguous area."
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 16,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 17,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 18,
>       "text": "          7.7     Minimum time between two monthly SHE Committee meetings"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 19,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 20,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 21,
>       "text": "          7.7.1    A minimum period of 21 days shall be maintained between any two SHE monthly"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 22,
>       "text": "                  committee meetings."
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 23,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 24,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 25,
>       "text": "          7.8     Agenda"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 26,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 27,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 28,
>       "text": "          7.8.1    The Secretary shall circulate the agenda of the meeting at least seven working days in"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 29,
>       "text": "                 advance of the scheduled date of the meeting to all members."
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 30,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 31,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 32,
>       "text": "          7.8.2    The agenda should broadly cover the following:"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 33,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 34,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 35,
>       "text": "                                 i)     Confirmation of minutes"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 36,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 37,
>       "text": "                                    ii)    Chairman’s review/overview of site SHE performance / condition"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 38,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 39,
>       "text": "                                     iii)    Previous month SHE statistics"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 40,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 41,
>       "text": "                          iv)    Incident and Accident Investigation / dangerous occurrence / near miss report"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 42,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 43,
>       "text": "                      v)    Site SHE inspection"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 44,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 45,
>       "text": "                          vi)    Sub-contractors’ SHE issues"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 46,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 47,
>       "text": "                             vii)   Safety presentation by Members"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 48,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 49,
>       "text": "                               viii)  Report from Employer"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 50,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 51,
>       "text": "                          ix)   Matters arising"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 52,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 53,
>       "text": "                      x)   Any other business"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 54,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 55,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 56,
>       "text": "          7.9      Minutes of the meeting"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 57,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 58,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 59,
>       "text": "          7.9.1    The Minutes of the meeting shall be prepared as per the format provided at Form"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 60,
>       "text": "                   No.: SF- 002 and sent to all members within 2 working days preferably by mail/fax"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 61,
>       "text": "                    followed by hardcopy. Safety Committee meeting minutes shall also be displayed in"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 62,
>       "text": "                    the notice board for wider publicity to all concerned."
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 63,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 64,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 65,
>       "text": "          7.10     Disciplinary Action"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 66,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 67,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 68,
>       "text": "          7.10.1   The chairman shall inform the members of any outstanding issues in the meeting and"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 69,
>       "text": "                        in case of repeated offence/ non-compliance by some members or other co/sub"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 70,
>       "text": "                    contractors and propose suitable disciplinary action including provisions of monitory"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 71,
>       "text": "                    penalty as per the relevant contract clauses, the Employer shall ensure that the same"
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 72,
>       "text": "                          is implemented."
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 73,
>       "text": ""
>     },
>     {
>       "pdf_page": 19,
>       "source_line_number": 74,
>       "text": ""
>     }
>   ],
>   "review_status": "pending_manual_review",
>   "title": "Contractor SHE Committee"
> }

### J6af8ef325f51b6bf

[[OKF_bundle/Technical/Vol3/vol3_appendices_instructions_forms#Safety, Health and Environment Manual – Appendices, General Instructions and Forms|SHE vol3_appendices_instructions_forms]], `Vol3DLNP1.pdf`, PDF p. 116 (`parsed_json/vol3/forms/she_committee_forms.json#/forms/0`)

> {
>   "checks": {
>     "form_identifier": "passed",
>     "line_preservation_with_removal_logs": "passed",
>     "page_sequence": "passed",
>     "source_hash": "passed"
>   },
>   "document_role": "form_template",
>   "field_reconstruction_status": "not_performed",
>   "form_id": "SF/001",
>   "fragments": [
>     {
>       "pdf_page": 116,
>       "text": "BANGALORE METRO RAIL CORPORATION LTD.\n\n\n\n                     FORM No. : SF/001\n\n\n\n\n               FORMATION OF SITE SHE COMMITTEE\n\n Contract No\n\n Contractor Name\n\n Contract Title\n\n\n\n                             CIRCULAR\n\n  Committee\n\n     The following SHE Committee is constituted with immediate effect:\n\n         Chairman:\n\n        Members:\n\n                    1)\n\n                    2)\n\n                    3)\n\n                    4)\n\n                    5)\n\n          Secretary:\n\n\n  Periodicity\n\n    The committee will meet at least once in a month on the day (specify date)\n\n\n  Agenda\n\n     Secretary will circulate agenda of the meeting at least two days in advance of the schedule\n     date of the meeting.\n\n  Circulation\n\n  Gist of the meeting will be minuted in the standard format and circulated to the\n  following under the signature of the secretary\n\n           1. Chairman                    3. BMRC Representatives\n\n           2. Members                     4. Others concerned\n\n\n\n\n  Date:                                            Signed By:      --------------------------\n\n                                             CHAIRMAN"
>     }
>   ],
>   "pdf_pages": [
>     116
>   ],
>   "removed_lines": [
>     {
>       "pdf_page": 116,
>       "reason": "printed_booklet_page_number",
>       "source_line_number": 1,
>       "text": "300"
>     },
>     {
>       "pdf_page": 116,
>       "reason": "manual_page_header",
>       "source_line_number": 2,
>       "text": "                                                                 Safety Health & Environment (SHE) Manual"
>     },
>     {
>       "pdf_page": 116,
>       "reason": "combined_page_footer",
>       "source_line_number": 80,
>       "text": "Bangalore Metro Rail Corporation Ltd.              September 2026     Section Page 112 of 114"
>     }
>   ],
>   "retained_lines": [
>     {
>       "pdf_page": 116,
>       "source_line_number": 3,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 4,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 5,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 6,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 7,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 8,
>       "text": "                  BANGALORE METRO RAIL CORPORATION LTD."
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 9,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 10,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 11,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 12,
>       "text": "                     FORM No. : SF/001"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 13,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 14,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 15,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 16,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 17,
>       "text": "               FORMATION OF SITE SHE COMMITTEE"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 18,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 19,
>       "text": " Contract No"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 20,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 21,
>       "text": " Contractor Name"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 22,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 23,
>       "text": " Contract Title"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 24,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 25,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 26,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 27,
>       "text": "                             CIRCULAR"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 28,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 29,
>       "text": "  Committee"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 30,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 31,
>       "text": "     The following SHE Committee is constituted with immediate effect:"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 32,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 33,
>       "text": "         Chairman:"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 34,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 35,
>       "text": "        Members:"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 36,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 37,
>       "text": "                    1)"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 38,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 39,
>       "text": "                    2)"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 40,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 41,
>       "text": "                    3)"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 42,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 43,
>       "text": "                    4)"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 44,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 45,
>       "text": "                    5)"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 46,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 47,
>       "text": "          Secretary:"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 48,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 49,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 50,
>       "text": "  Periodicity"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 51,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 52,
>       "text": "    The committee will meet at least once in a month on the day (specify date)"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 53,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 54,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 55,
>       "text": "  Agenda"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 56,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 57,
>       "text": "     Secretary will circulate agenda of the meeting at least two days in advance of the schedule"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 58,
>       "text": "     date of the meeting."
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 59,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 60,
>       "text": "  Circulation"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 61,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 62,
>       "text": "  Gist of the meeting will be minuted in the standard format and circulated to the"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 63,
>       "text": "  following under the signature of the secretary"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 64,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 65,
>       "text": "           1. Chairman                    3. BMRC Representatives"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 66,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 67,
>       "text": "           2. Members                     4. Others concerned"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 68,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 69,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 70,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 71,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 72,
>       "text": "  Date:                                            Signed By:      --------------------------"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 73,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 74,
>       "text": "                                             CHAIRMAN"
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 75,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 76,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 77,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 78,
>       "text": ""
>     },
>     {
>       "pdf_page": 116,
>       "source_line_number": 79,
>       "text": ""
>     }
>   ],
>   "review_status": "pending_manual_review",
>   "source_heading": {
>     "form_id": "SF/001",
>     "pdf_page": 116,
>     "source_text": "                     FORM No. : SF/001"
>   },
>   "source_page_context": [
>     {
>       "extraction_method": "geometric_sort",
>       "has_extracted_text": true,
>       "page_rect": [
>         0.0,
>         0.0,
>         595.219970703125,
>         842.0
>       ],
>       "pdf_page": 116,
>       "review_status": "pending_manual_review",
>       "rotation": 0,
>       "text": "300\n                                                                 Safety Health & Environment (SHE) Manual\n\n\n\n\n\n                  BANGALORE METRO RAIL CORPORATION LTD.\n\n\n\n                     FORM No. : SF/001\n\n\n\n\n               FORMATION OF SITE SHE COMMITTEE\n\n Contract No\n\n Contractor Name\n\n Contract Title\n\n\n\n                             CIRCULAR\n\n  Committee\n\n     The following SHE Committee is constituted with immediate effect:\n\n         Chairman:\n\n        Members:\n\n                    1)\n\n                    2)\n\n                    3)\n\n                    4)\n\n                    5)\n\n          Secretary:\n\n\n  Periodicity\n\n    The committee will meet at least once in a month on the day (specify date)\n\n\n  Agenda\n\n     Secretary will circulate agenda of the meeting at least two days in advance of the schedule\n     date of the meeting.\n\n  Circulation\n\n  Gist of the meeting will be minuted in the standard format and circulated to the\n  following under the signature of the secretary\n\n           1. Chairman                    3. BMRC Representatives\n\n           2. Members                     4. Others concerned\n\n\n\n\n  Date:                                            Signed By:      --------------------------\n\n                                             CHAIRMAN\n\n\n\n\n\nBangalore Metro Rail Corporation Ltd.              September 2026     Section Page 112 of 114",
>       "text_blocks": [
>         {
>           "bbox": [
>             36.59998321533203,
>             37.608280181884766,
>             550.6591796875,
>             46.05027770996094
>           ],
>           "block_number": 0,
>           "text": "                                                                                                                                   Safety Health & Environment (SHE) Manual \n"
>         },
>         {
>           "bbox": [
>             71.99996948242188,
>             48.41946029663086,
>             74.76715087890625,
>             57.77189636230469
>           ],
>           "block_number": 1,
>           "text": " \n"
>         },
>         {
>           "bbox": [
>             71.99996948242188,
>             781.9227294921875,
>             503.2270812988281,
>             803.451416015625
>           ],
>           "block_number": 2,
>           "text": "Bangalore Metro Rail Corporation Ltd.                              September 2026         Section Page 112 of 114 \n \n"
>         },
>         {
>           "bbox": [
>             100.5599594116211,
>             77.46939849853516,
>             103.32714080810547,
>             86.81187438964844
>           ],
>           "block_number": 3,
>           "text": " \n"
>         },
>         {
>           "bbox": [
>             200.3999786376953,
>             88.3893814086914,
>             435.4872741699219,
>             97.73185729980469
>           ],
>           "block_number": 4,
>           "text": "BANGALORE METRO RAIL CORPORATION LTD. \n"
>         },
>         {
>           "bbox": [
>             238.79989624023438,
>             127.80321502685547,
>             340.2672119140625,
>             138.1587371826172
>           ],
>           "block_number": 5,
>           "text": "FORM No. : SF/001 \n"
>         },
>         {
>           "bbox": [
>             71.99996948242188,
>             157.1494598388672,
>             74.76715087890625,
>             166.49192810058594
>           ],
>           "block_number": 6,
>           "text": " \n"
>         },
>         {
>           "bbox": [
>             184.31993103027344,
>             175.20318603515625,
>             394.6271667480469,
>             185.55870056152344
>           ],
>           "block_number": 7,
>           "text": "FORMATION OF SITE SHE COMMITTEE \n"
>         },
>         {
>           "bbox": [
>             77.39997100830078,
>             194.34934997558594,
>             174.0071563720703,
>             203.8118133544922
>           ],
>           "block_number": 8,
>           "text": "Contract No \n \n"
>         },
>         {
>           "bbox": [
>             77.39997100830078,
>             212.34934997558594,
>             174.00711059570312,
>             221.8118133544922
>           ],
>           "block_number": 9,
>           "text": "Contractor Name \n \n"
>         },
>         {
>           "bbox": [
>             77.39997100830078,
>             230.34934997558594,
>             174.0071563720703,
>             239.8118133544922
>           ],
>           "block_number": 10,
>           "text": "Contract Title \n \n"
>         },
>         {
>           "bbox": [
>             288.7198791503906,
>             248.45938110351562,
>             291.487060546875,
>             257.81182861328125
>           ],
>           "block_number": 11,
>           "text": " \n"
>         },
>         {
>           "bbox": [
>             82.19996643066406,
>             266.3493347167969,
>             316.8071594238281,
>             290.21185302734375
>           ],
>           "block_number": 12,
>           "text": "CIRCULAR \n Committee \n"
>         },
>         {
>           "bbox": [
>             99.23995971679688,
>             295.4994201660156,
>             396.007568359375,
>             304.85186767578125
>           ],
>           "block_number": 13,
>           "text": "The following SHE Committee is constituted with immediate effect: \n"
>         },
>         {
>           "bbox": [
>             118.20028686523438,
>             309.8994445800781,
>             167.0474395751953,
>             333.7718505859375
>           ],
>           "block_number": 14,
>           "text": "Chairman: \nMembers: \n"
>         },
>         {
>           "bbox": [
>             118.20028686523438,
>             338.93939208984375,
>             188.1691131591797,
>             420.7717590332031
>           ],
>           "block_number": 15,
>           "text": "1) \n \n2) \n \n3) \n \n4) \n \n5) \n \nSecretary: \n"
>         },
>         {
>           "bbox": [
>             406.2001953125,
>             425.8292541503906,
>             408.9673767089844,
>             435.1717529296875
>           ],
>           "block_number": 16,
>           "text": " \n"
>         },
>         {
>           "bbox": [
>             82.19996643066406,
>             443.8292541503906,
>             136.08714294433594,
>             453.1717529296875
>           ],
>           "block_number": 17,
>           "text": "Periodicity \n"
>         },
>         {
>           "bbox": [
>             94.79996490478516,
>             458.4593200683594,
>             429.369140625,
>             467.811767578125
>           ],
>           "block_number": 18,
>           "text": "The committee will meet at least once in a month on the day (specify date)  \n"
>         },
>         {
>           "bbox": [
>             82.19996643066406,
>             485.5892639160156,
>             121.6871566772461,
>             494.9317626953125
>           ],
>           "block_number": 19,
>           "text": "Agenda \n"
>         },
>         {
>           "bbox": [
>             94.79996490478516,
>             500.2193298339844,
>             498.2474060058594,
>             521.0917358398438
>           ],
>           "block_number": 20,
>           "text": "Secretary will circulate agenda of the meeting at least two days in advance of the schedule \ndate of the meeting. \n"
>         },
>         {
>           "bbox": [
>             80.99996948242188,
>             531.0692749023438,
>             501.36761474609375,
>             566.4517211914062
>           ],
>           "block_number": 21,
>           "text": "Circulation \nGist of the meeting will be minuted in the standard format and circulated to the \nfollowing under the signature of the secretary  \n"
>         },
>         {
>           "bbox": [
>             118.19999694824219,
>             571.6192626953125,
>             408.96710205078125,
>             609.8916625976562
>           ],
>           "block_number": 22,
>           "text": "1. Chairman \n \n \n3. BMRC Representatives \n2. Members \n \n \n4. Others concerned \n \n"
>         },
>         {
>           "bbox": [
>             82.19996643066406,
>             622.3792114257812,
>             490.8202819824219,
>             646.251708984375
>           ],
>           "block_number": 23,
>           "text": " \nDate: \n \n \n \n \n Signed By: \n-------------------------- \n"
>         },
>         {
>           "bbox": [
>             401.39984130859375,
>             654.471923828125,
>             463.1470947265625,
>             664.8385009765625
>           ],
>           "block_number": 24,
>           "text": "CHAIRMAN \n"
>         },
>         {
>           "bbox": [
>             71.99996948242188,
>             693.17919921875,
>             74.76715087890625,
>             745.9716796875
>           ],
>           "block_number": 25,
>           "text": " \n \n \n \n"
>         },
>         {
>           "bbox": [
>             546.0439453125,
>             24.479991912841797,
>             570.0199584960938,
>             41.38799285888672
>           ],
>           "block_number": 26,
>           "text": "300\n"
>         }
>       ]
>     }
>   ],
>   "table_reconstruction_status": "not_performed",
>   "title": "Formation of Site SHE Committee"
> }

</details>

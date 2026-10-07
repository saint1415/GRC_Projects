# AI Use Assessment: Commercial Generative AI Chatbot Used with CUI Engineering Documents (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (engineering subcontractor handling CUI drawings) |
| Tier / Vertical | Sole Proprietorship / Defense Industrial Base |
| AI use case | AI-001: a commercial generative AI chatbot on an individual paid plan (SYS-09). CUI text excerpts from two Prime A specifications, one ITAR-marked, were pasted on 6 occasions between 2026-03 and 2026-07. Found in the P03 self-review on 2026-07-16; CUI use stopped that day |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; AI 600-1 for generative AI risks |
| Assessor and decision | Owner, 2026-08-26, with the CMMC consultant's comments; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases: AI-001 and the deferred AI-002) |

## 1. What it does (Map)
The owner types or pastes text into the chatbot's web page and gets back drafts: report wording, emails, rewordings of dense specification paragraphs, and answers to general engineering questions. The provider processes and stores the conversation in its commercial cloud. On the individual plan, conversations could be used to train the provider's models unless the owner turned that off (the owner turned it off and deleted the history on 2026-07-17). No drawings or models were uploaded. Outputs never went into a drawing directly, but two reworded specification summaries were used to plan design work.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| DFARS 252.204-7012(b)(2)(ii)(D) | **Yes, violated** | A cloud service that stores or processes covered defense information must meet FedRAMP Moderate-equivalent requirements and the clause's incident paragraphs. This chatbot does not |
| DFARS 252.204-7012(c) cyber incident | **Assess** | A compromise includes disclosure to unauthorized persons or copying to unauthorized media (252.204-7012(a)). The owner told Prime A's subcontract administrator and counsel on 2026-07-17. The decision on reporting, and the reasoning, go in the incident log by 2026-09-30. If it is reportable, the 72-hour window has passed, partly because the owner has no medium assurance certificate (POAM-009); the report would be filed as soon as the certificate arrives, noting the delay |
| SP 800-171 3.1.20 | **Yes** | External system use with CUI must be verified and limited. No list existed; it cannot be on a POA&M (32 CFR 170.21(a)(2)(iii)) |
| ITAR 22 CFR 120.56 and 127.12 | **Assess** | If the provider's staff or storage gave a foreign person access to the ITAR-marked excerpt, that is a release. The encrypted-storage carve-out in 120.54(a)(5) cannot apply because the provider reads the text unencrypted. Export counsel advises on a voluntary disclosure |
| FTC Act Section 5 | Indirectly | Governs the provider's statements about data use; the owner keeps a copy of the terms in effect |
| State AI laws on consequential decisions | No | No decisions about individuals |

## 3. Risk screen (repository rubric)
**Tier: Low** for the use that remains allowed (public and non-CUI text, internal productivity, no decisions about people). **The tier does not matter for CUI**, because no tier allows CUI, FCI, or customer NDA data to go to a tool outside an approved system (POL-01 6.1 and 9.6). **Escalation to High:** if any output became the source for a dimension, tolerance, or material callout, it could affect the safety of a flight part, which the rubric treats as High.

## 4. Data-sharing rules (Govern)
1. No CUI, FCI, ITAR or EAR data, or customer NDA data goes into any AI tool unless the tool runs inside an approved system under POL-01 6.1, has a written P10 assessment, and the owner approves it in writing (POL-01 9.6).
2. Before pasting anything, the owner checks it against the CUI markings and the customer's data. When in doubt, it is not pasted.
3. Model training on the owner's content stays off; history is deleted monthly.

## 5. Human review of outputs (Measure and Manage)
The owner reads and edits every output and checks every technical statement against the source document. AI output is never the source for a dimension, tolerance, material, or export classification. Generative AI risks from AI 600-1 that matter here are confabulation (a plausible but wrong summary of a requirement) and information security (data leaving the owner's control). Accuracy has not been measured, so outputs are treated as drafts only.

## 6. Decision (approved 2026-08-31)
**AI-001: keep for non-CUI work only, with the rules above.** By 2026-09-30 (P01 R-007):
1. Record the reporting decision for the 2026-03 to 2026-07 pastes in the incident log, with Prime A's and counsel's input; report through DIBNet if it is reportable.
2. Export counsel advises whether a voluntary disclosure to DDTC (22 CFR 127.12) is warranted for the ITAR-marked excerpt.
3. Keep the provider's terms, the training setting screenshot, and the history deletion record.

**AI-002 (deferred):** the SYS-10 provider's AI add-on may be considered only after the Level 2 (Self) assessment (2027-01-15), and only if it is inside the FedRAMP-authorized boundary, listed in the CRM and SSP, makes no autonomous actions, and passes a 20-question accuracy check against known specification answers. This assessment is repeated first.

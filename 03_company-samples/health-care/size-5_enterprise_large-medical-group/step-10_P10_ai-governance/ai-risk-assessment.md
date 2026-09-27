# AI Governance Risk Assessment: Enterprise AI Portfolio and Ambient Clinical Documentation

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-specialty medical group; FL, GA, AL, SC) |
| Tier / Vertical | Enterprise / Health Care and Social Assistance |
| Scope | Enterprise AI portfolio (14 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 ambient clinical documentation (AI scribe) in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI council (chaired by the Chief Medical Information Officer), meeting of 2026-08-19; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 14 |
| Risk tier | High 6, Medium 7, Low 1 |
| Status | In production 11, Pilot 2, Suspended 1 |
| Council review complete | 9 of 14 |
| Not yet reviewed | 5: AI-006, AI-009, AI-010, AI-012, AI-014 (all due 2026-11-30, POAM-020) |
| Patient care decision support tools identified under 45 CFR 92.210 | 4 confirmed (AI-002, AI-003, AI-004, AI-005); AI-006 under review; AI-010 likely |
| High-tier tools with bias testing only on vendor-supplied data | 4 (AI-002, AI-003, AI-004, AI-005) |

**Main findings:** 5 use cases are running (or piloting) without council review, including one High-tier employment tool (AI-012, now suspended) and one High-tier lab pilot (AI-010). Bias testing for all four clinical decision support tools rests on vendor-supplied data, not the group's own patients. The AI scribe shows a higher error rate for Spanish-language visits, and consent documentation is below target.

## 2. GOVERN: AI council operating model
**Charter.** The AI council was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly.

**Members:** Chief Medical Information Officer (chair); Chief Privacy Officer; CISO; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce and HR tools); Laboratory Director; a nursing leader; the patient safety officer; the data science lead; and a patient-experience representative. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Council vote, then the executive risk committee | Local validation and bias testing on the group's data; 92.210 review; impact assessment; human review design; notice to affected people; monitoring plan |
| Medium | Council vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Council chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.6; STD-05.3). Procurement and IT change management now block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.8 (no Restricted data in AI tools without council approval and a BAA with no-training terms); POL-05 4.6 (approved tools only) and 4.7 (recording consent); POL-01 4.8 (no BAA, no PHI); STD-05.3 (approved AI tools list).

**Cadence:** monthly council meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

**Why 5 use cases lack review.** Four entered through vendor feature releases or acquired practices' systems before the intake block existed, and one (AI-010) started as a lab validation study. The council set review dates for all five (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| HIPAA Privacy and Security Rules | Yes, for every use case with PHI | Vendors that handle PHI are business associates; BAAs with no-training and deletion terms are required (POL-04 4.8) |
| Section 1557, 45 CFR 92.210 | Yes | The group receives federal financial assistance. It must not discriminate through patient care decision support tools, must make reasonable efforts to identify tools that use race, color, national origin, sex, age, or disability as inputs, and must make reasonable efforts to mitigate the risk. 45 CFR 92.4 covers automated and non-automated tools used to support clinical decision-making (section 5) |
| State recording consent laws | Yes, for AI-001 | Laws differ by state; the group applies all-party prior consent in all four states. Florida worked example: interception is lawful when all parties have given prior consent (Fla. Stat. 934.03(2)(d)) |
| FDA device requirements | Vendor duty | AI-002, AI-003, and AI-004 are regulated device software; the group uses them within their cleared or authorized indications |
| ONC HTI-1 decision support intervention transparency (45 CFR 170.315(b)(11)) | Vendor duty | Applies to certified health IT developers; the group uses the source attributes the EHR vendor publishes for AI-005, AI-006, and AI-009 |
| FTC Act Section 5 | Indirectly | Accuracy of AI claims to patients (AI-008) and vendor claims the group relies on |
| CLIA (42 CFR 493.1291(a)) | Yes, for AI-010 | Results must be accurately and reliably reported; the ML flagging model must be validated before production |
| Federal equal employment opportunity laws | Yes, for AI-012 | Counsel reviews adverse impact before any re-enable |
| Colorado SB26-189 | No | The group does not operate in Colorado. Note: its HIPAA covered entity carve-out does not extend to employment decisions |
| Medicare Advantage medical necessity rule (42 CFR 422.101(c)(1)(i)) | Context only | Applies to MA organizations; AI-011 only assembles the group's documentation for payers |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision (here, health care or employment) or able to affect physical safety.

| ID | Use case | Tier | Status | Council review | 92.210 tool |
|---|---|---|---|---|---|
| AI-001 | Ambient clinical documentation (AI scribe) drafting visit notes from recorded conversations | Medium | In production (about 650 providers) | Reviewed 2025-12-10; re-reviewed 2026-08-19 | No (documentation only; suggestion features disabled) |
| AI-002 | CT urgent-finding triage (intracranial hemorrhage, pulmonary embolism) reordering the radiologist worklist | High | In production (12 imaging centers) | Reviewed 2025-10-15 | Yes |
| AI-003 | Mammography computer-aided detection | High | In production | Reviewed 2025-10-15 | Yes |
| AI-004 | Autonomous diabetic retinopathy screening in primary care | High | In production (40 clinics) | Reviewed 2025-11-20 | Yes |
| AI-005 | Care management risk stratification for Medicare Advantage and value-based contracts | High | In production | Reviewed 2025-12-10 | Yes |
| AI-006 | Patient portal message draft replies | Medium | Pilot (120 providers) | Not reviewed (intake received 2026-07; review due 2026-11-30) | Under review |
| AI-007 | Computer-assisted coding suggestions | Medium | In production | Reviewed 2025-09-30 | No |
| AI-008 | Patient-app virtual assistant for scheduling, FAQs, and bill pay (SL-1) | Medium | In production | Reviewed 2026-02-11 | No |
| AI-009 | No-show prediction used for scheduling overbooking | Medium | In production | Not reviewed (review due 2026-11-30) | No (scheduling); fairness risk from proxies |
| AI-010 | Lab autoverification machine-learning flagging of results for technologist review | High | Pilot (validation environment only) | Not reviewed (review due 2026-11-30; required before production) | Likely yes (council to confirm) |
| AI-011 | Denial prediction and prior authorization packet assembly | Medium | In production | Reviewed 2026-03-18 | No |
| AI-012 | Applicant resume screening and ranking | High | Suspended (ranking disabled pending review) | Not reviewed (review due 2026-11-30) | No (not a health program tool) |
| AI-013 | Enterprise generative AI assistant for workforce productivity | Medium | In production | Reviewed 2026-01-14 | No |
| AI-014 | SOC alert triage assistant | Low | In production | Not reviewed (review due 2026-11-30) | No |

**Tiering notes:** AI-004 is High because negative results reach patients without specialist review. AI-010 is High because it would decide which lab results skip human review. AI-001 stays Medium because a provider reviews and signs every note; enabling diagnosis, order, or coding suggestions would re-tier it to High. AI-013 is Medium rather than Low because PHI is allowed in its approved tenant.

## 5. Section 1557 (45 CFR 92.210) duties
| Duty | What the group does | Status |
|---|---|---|
| (a) Do not discriminate through patient care decision support tools | Council review of every tool before use; monitoring of outcome gaps | Partially met: 5 use cases unreviewed |
| (b) Identify tools with race, color, national origin, sex, age, or disability inputs (ongoing) | Inventory column `protected_characteristic_inputs`; extend to non-automated tools (EHR alert rules, clinical calculators, eligibility criteria) by 2026-11-30 | Partially met: AI inventory done for reviewed tools; non-automated tools not yet inventoried |
| (c) Make reasonable efforts to mitigate discrimination risk for each identified tool | Local bias testing, threshold adjustments, human review, and documented mitigation for AI-002 to AI-005 | Partially met: mitigation documented for 3 tools; testing on vendor data only |

These rows match P03 G-100 to G-102 and POAM-020.

## 6. MEASURE: bias testing gap and plan
**Gap.** For AI-002 to AI-005, the only fairness evidence is the vendors' own validation data. None has been checked on the group's patients, who differ from vendor study populations (for example, a large Spanish-speaking population in Florida and a large rural population in Alabama and Georgia).

**Local testing plan (POAM-020, due 2027-03-31):**
| Tool | Metric | Groups compared | Threshold for action |
|---|---|---|---|
| AI-002 CT triage | Sensitivity against final radiologist reads | Sex; age band; imaging center | Any group's sensitivity more than 5 points below overall |
| AI-003 mammography CAD | Recall rate and cancer detection rate | Age band; breast density; race and ethnicity where recorded | Recall-rate ratio above 1.25 or detection gap above 5 points |
| AI-004 retinopathy screening | Ungradable rate; referral completion | Age band; language; clinic | Ungradable rate more than 5 points above overall |
| AI-005 risk stratification | Share of each group flagged for outreach relative to disease burden; outcome gaps | Race and ethnicity where recorded; sex; age band; payer | Flag-rate ratio below 0.8 for any group at equal disease burden |

**Data limits:** race and ethnicity fields are incomplete in the EHR for many patients, so the plan uses self-reported data where present, reports completeness, and adds language and payer as secondary views. Results go to the council and the Chief Compliance Officer as 92.210(c) evidence.

## 7. Full assessment: AI-001 ambient clinical documentation (AI scribe)
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Record the visit, transcribe it, and draft a note the provider edits and signs |
| Users | About 650 enrolled providers across all four states |
| Affected people | Patients whose visits are recorded (about 9,000 visits a day), family members or interpreters present, and providers |
| Data | Inputs: visit audio (ePHI). Outputs: transcript and draft note (ePHI). Audio deleted within 7 days of signing (contract) |
| Build or buy | Buy: vendor SaaS integrated with the EHR; BAA with no-training and no-secondary-use terms |
| Not intended | Diagnosis, order, or coding suggestions (disabled); patient-facing output; behavioral health visits (excluded) |

### 7.2 Recording consent across four states
- **Standard:** all-party prior consent for every recording, in every state, including telehealth visits where the patient is in another state. This avoids tracking which states require only one party's consent.
- **Florida worked example:** Fla. Stat. 934.03(2)(d) makes interception lawful when all parties have given prior consent, which the enterprise standard meets.
- **How consent is captured:** written notice at check-in; the provider asks before starting the recording and documents consent in the note with a structured field; interpreters and family members in the room are asked too; a patient can decline or stop recording at any time with no effect on care.
- **Minors:** consent from the parent or guardian and assent from the minor where appropriate; adolescent confidential visits are not recorded.
- **Current result:** consent documented in 91% of sampled recorded visits (target 100%). The missing 9% had verbal consent according to the providers but no structured field entry.

### 7.3 Risk tier
Medium (section 4). Escalation triggers: enabling suggestions, automatic filing without signature, behavioral health use, or use for adolescent confidential visits.

### 7.4 MEASURE (sample of 600 notes, June to August 2026)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Critical errors (medication, dose, laterality, allergy) must be 0 after signing; minor errors under 5% of notes | 3 critical errors in drafts, all caught before signing (0 after signing); minor errors 4.1% | Yes |
| Safe | Provider signature and attestation on every note | 99% attestation; 100% signed | Yes |
| Secure and resilient | SSO with MFA; vendor SOC 2 Type 2; BAA | All in place | Yes |
| Accountable and transparent | Notice and documented consent; notes labeled AI-assisted | Consent documented 91% | **No** |
| Explainable and interpretable | Transcript viewable beside the draft | Available | Yes |
| Privacy-enhanced | No training on group data; audio deleted within 7 days | Contract terms in place; deletion confirmed in a quarterly vendor attestation | Yes |
| Fair, with harmful bias managed | Minor-error rate by visit language and age band; flag a gap over 3 percentage points | Spanish-language visits 7.9% vs English 3.6%; age 75+ 4.6% | **No** (language gap) |

### 7.5 MANAGE
- **Human in the loop:** draft only; provider reviews against memory and the transcript, edits, signs, and attests. Providers must pause recording for sensitive topics the patient does not want recorded.
- **Language gap:** providers get a prompt to review Spanish-language drafts line by line; the vendor must deliver a Spanish model update and accuracy data by 2027-01-31; if the gap persists, Spanish-language visits are excluded until fixed.
- **Monitoring:** monthly 10-note sample per provider; quarterly error rates by language and age band; consent field completion reported monthly by clinic.
- **Incidents:** a critical documentation error is corrected through the EHR amendment process and reviewed by the patient safety officer; a vendor security incident follows P08 and the BAA terms.
- **Decommissioning:** stop and export if the vendor changes data-use terms, if critical errors reach signed notes two months in a row, or if the language gap is not closed by 2027-06-30.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the council; drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as SOC or patient safety events and follow P08 where security or PHI is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice, lose FDA status, or change data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the council's recommendation of 2026-08-19:
1. **AI-001:** approved to continue with conditions: consent field made mandatory before recording can start (by 2026-11-30); Spanish-language plan as in 7.5.
2. **AI-002 to AI-005:** approved to continue; local bias testing due 2027-03-31 (POAM-020); 92.210 mitigation records completed for all four.
3. **AI-006, AI-009, AI-014:** may continue in current scope until council review by 2026-11-30; no expansion.
4. **AI-010:** stays in the validation environment; production use requires council approval, CLIA validation, and 92.210 review.
5. **AI-012:** ranking stays disabled until council review and an adverse impact analysis are complete.
6. **92.210 inventory:** extend to non-automated tools by 2026-11-30.

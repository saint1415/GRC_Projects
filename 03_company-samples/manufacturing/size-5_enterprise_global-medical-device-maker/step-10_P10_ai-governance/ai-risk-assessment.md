# AI Governance Risk Assessment: Enterprise AI Portfolio and AI-001 LVEF Estimation

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded connected medical device manufacturer) |
| Tier / Vertical | Enterprise / Manufacturing (NAICS 334510) |
| Scope | Enterprise AI portfolio (11 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the AI-enabled device software function that estimates left ventricular ejection fraction (LVEF) from US-20 handheld ultrasound images (section 7) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) for AI-007 and AI-008; repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Medical Officer), meeting of 2026-08-26; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-08 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 11 |
| Risk tier | High 4, Medium 5, Low 2 |
| Status | In production 8, In development 1, Pilot 1, Suspended 1 |
| Committee review complete | 7 of 11 |
| Not yet reviewed | 4: AI-004, AI-006, AI-009, AI-011 (all due 2026-11-30, POAM-025) |
| AI that is itself a medical device function | 3: AI-001 (in development), AI-002 and AI-003 (cleared) |
| High-tier tools with a subgroup performance gap or untested subgroups | 3: AI-001 (BMI 35 or more), AI-002 (age and sex subgroups not monitored), AI-011 (inputs undisclosed) |

**Main findings:** 4 use cases are running (or piloting) without committee review, including a consumer-facing feature (AI-009) and a complaint triage assistant that touches FDA reporting decisions (AI-004). AI-001, the company's next AI device, estimates LVEF less accurately in patients with a body mass index of 35 or more, and its training data under-represents women. AI-002 is monitored overall but not by subgroup.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk and technology committee reviews quarterly.

**Members:** Chief Medical Officer (chair); CTO; CQRO; VP Product Security; Chief Privacy Officer; CISO; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce tools); Vice President, Consumer Health (for consumer features); the data science lead; and a clinical affairs director. Internal Audit observes.

**How the committee works with the QMS.** For AI that is a device function (AI-001, AI-002, AI-003), the committee does not replace design controls (21 CFR 820.10(c)) or FDA submissions. It reviews the same evidence at defined points (data plan approval, design freeze, and before each release) and can stop a release on fairness, security, or safety grounds. Its records are inputs to the design history file.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Subgroup validation on representative data; security review including AI-specific threats; privacy review; human oversight design; labeling or notice; monitoring plan; for device functions, design control and regulatory sign-off by the CQRO |
| Medium | Committee vote | Human oversight design; output quality monitoring; disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.6; STD-05.3). Procurement and IT change management block AI features without an inventory ID since 2026-03. The GRC team owns the inventory.

**Policies:** POL-04 4.9 (training data de-identified or approved; no PHI or consumer data for training without a legal basis and permission); POL-05 4.6 (approved AI tools only; no code, vulnerability details, signing material, PHI, or consumer data in unapproved tools); POL-01 4.5 (secure product development for every device release, including AI device functions); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

**Why 4 use cases lack review.** AI-004 and AI-011 are vendor features switched on before the intake block; AI-006 and AI-009 were built by product teams before the committee's intake form existed. The committee set review dates for all four (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FD&C Act device requirements and QMSR design controls (21 CFR Part 820) | Yes, for AI-001, AI-002, AI-003 | They are device software functions. AI-002 and AI-003 are cleared; AI-001 needs a 510(k) before it can be sold (pre-submission meeting held 2026-06) |
| FD&C Act section 524B (N31-33-R05) | Yes, for AI-001 (and AI-002, AI-003 through their systems) | The US-20 tablet app connects to the DDC, so the AI-001 submission is a cyber device submission needing the CVD plan, SBOM (including the model and ML framework), and cybersecurity processes (P03) |
| FDA draft guidance, *Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations* (January 2025; docket FDA-2024-D-4488) | Nonbinding **draft** | Recommends the content FDA expects: data management, model description, performance validation including subgroups, bias control, performance monitoring, and AI-specific cybersecurity. Still a draft as of 2026-09-25; recheck before the submission |
| FDA guidance, *Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions* (final; Federal Register notice of availability 2024-12-04, FR Doc. 2024-28361) | Nonbinding guidance | Governs how planned model updates can be authorized in advance. The AI-001 team intends to propose a PCCP for retraining with new data |
| HIPAA Security Rule (N62-R01) | Yes, for archived images and production outputs | US-20 images and LVEF results archived in the DDC are PHI held for hospitals; the training set is de-identified by the partner sites and is not PHI |
| FTC Health Breach Notification Rule (N62-R06) | Yes, for the data behind AI-009 | The consumer app is a personal health record; AI-009 uses its data, so any unauthorized disclosure of that data is analyzed under 16 CFR Part 318 |
| FTC Act Section 5 | Yes | Performance and benefit claims (AI-001 labeling and marketing; AI-009 messages) must be truthful and substantiated and match validated subgroup results |
| Section 1557, 45 CFR 92.210 | Customers, not the company | Hospitals and practices that receive federal financial assistance must make reasonable efforts to identify patient care decision support tools that use race, color, national origin, sex, age, or disability as inputs, and to mitigate discrimination risk. AI-003 uses age as an input. The company gives customers each tool's inputs and subgroup performance so they can meet this duty |
| Federal equal employment opportunity laws | Yes, for AI-011 | Counsel reviews adverse impact before any re-enable |
| QMSR production and process controls | Yes, for AI-005 | Production software used for inspection is validated for its intended use under the QMS |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision (here, health care or employment) or able to affect physical safety.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | LVEF estimation from US-20 ultrasound images | High | In development | Reviewed 2026-04-15; re-reviewed 2026-08-26 |
| AI-002 | ECG arrhythmia detection in the RCM platform | High | In production | Reviewed 2025-10-08; re-reviewed 2026-05-20 |
| AI-003 | Patient deterioration index in the DDC | High | In production | Reviewed 2025-12-03 |
| AI-004 | Complaint triage assistant (MDR reportability suggestions) | Medium | Pilot | Not reviewed (due 2026-11-30) |
| AI-005 | Automated optical inspection at FL-1 | Medium | In production | Reviewed 2026-02-18 |
| AI-006 | Predictive maintenance for fielded IV-300 pumps | Low | In production | Not reviewed (due 2026-11-30) |
| AI-007 | Enterprise generative AI coding assistant | Medium | In production | Reviewed 2026-02-11 |
| AI-008 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-21 |
| AI-009 | Consumer app blood pressure insights | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-010 | SOC alert triage assistant | Low | In production | Reviewed 2026-03-04 |
| AI-011 | Applicant resume screening and ranking | High | Suspended | Not reviewed (due 2026-11-30) |

**Tiering notes:**
- **AI-004 is Medium, not Low,** because a wrong suggestion could contribute to a missed MDR (P01 R-042). A person decides every complaint, which keeps it below High.
- **AI-007 is Medium** because its output enters device software and can introduce vulnerabilities or license obligations into a cyber device. Code review and design controls keep it below High.
- **AI-009 is Medium** because it speaks directly to consumers about their health. If it began suggesting treatment changes, it would be re-tiered to High and assessed as a possible device function.

## 5. Security of AI (AI-specific threats)
The VP Product Security added these threats to the threat models of the three device functions, as the FDA draft AI guidance recommends:
| Threat | Control |
|---|---|
| Model file tampering in the build or update path | Model files are built, signed, and released through DSF-MES like firmware (P02 SI-7, SC-12); the app verifies the model signature before loading |
| Poisoned training or retraining data | Data sets registered under PRC-04.1 with hashes; data changes reviewed; retraining only under a PCCP |
| Adversarial or out-of-distribution inputs | Image-quality gate refuses low-quality clips (AI-001); input range checks (AI-002, AI-003) |
| Model and framework vulnerabilities | Model, ML framework, and runtime listed in the SBOM and monitored like any other component (P03 G-009) |
| Use of AI tools that leak code or data | POL-05 4.6; unapproved AI domains blocked (P01 R-040) |

## 6. MEASURE: portfolio monitoring
| Use case | Metric | Result or status |
|---|---|---|
| AI-002 | Monthly sensitivity against technician review | 97.8% overall (2026 H1); subgroup monitoring by age and sex starts 2027 Q1 (SOC 2 PI1.3) |
| AI-003 | Quarterly calibration by hospital and subgroup | Within thresholds at 4 hospitals tested in 2026-02; expansion to all hospitals planned |
| AI-005 | Escape rate from downstream test | 0 escapes attributed to the model in 2026 H1 |
| AI-007 | Static analysis findings and license scan hits for AI-assisted changes | No worse than the baseline over 6 months |
| AI-004, AI-006, AI-009 | Not yet defined | Set at committee review |

## 7. Full assessment: AI-001 LVEF estimation
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Estimate LVEF from apical views acquired with the US-20 at the point of care, to help trained clinicians decide whether a full echocardiogram is needed. **Adjunct only:** it does not diagnose heart failure or replace a full echocardiogram |
| Users | Clinicians trained in point-of-care ultrasound in hospitals (emergency, hospital medicine, critical care) |
| Affected people | Adult patients being evaluated for heart function |
| Data: training and test | 21,400 studies from 6 partner sites, de-identified by the sites, with reference LVEF from cardiologist-read full echocardiograms. Women 36%; BMI 35 or more 9%; age 65 or more 52%; race and ethnicity recorded for 71% of studies. Held-out test set of 3,100 studies from 2 sites not used in training |
| Data: production | Cine clips and results on the hospital's tablet; archived in the DDC as PHI for the hospital (business associate). Production data is **not** used for retraining without a new agreement with the hospital and a PCCP |
| Build or buy | Build. Locked model; runs in the US-20 tablet app |
| Not intended | Pediatric patients; use without the image-quality gate; automatic documentation or orders; use by untrained users |

### 7.2 Risk tier
**High** (section 4). An underestimate could lead a clinician to skip a needed full echocardiogram; an overestimate could delay treatment.

### 7.3 MEASURE (held-out test set, 3,100 studies, as of 2026-08-26)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Mean absolute error (MAE) against the reference no more than 6 EF points; sensitivity for LVEF 40% or less at least 85% with a lower 95% bound of at least 80% | MAE 5.1; sensitivity 90%; specificity 88% | Yes (external validation still required) |
| Safe | Image-quality gate rejects clips it cannot estimate; labeling states limits; human factors test | Gate rejects 7% of clips; labeling drafted; human factors test scheduled 2026-12 | Partial |
| Secure and resilient | AI threats in the threat model; model file signed; model and framework in the SBOM | Done (section 5) | Yes |
| Accountable and transparent | Model card with training data sources, subgroup mix, and subgroup performance | Draft model card | Partial |
| Explainable and interpretable | Shows the frames and tracing used for the estimate, and a quality indicator | Working in the prototype | Yes |
| Privacy-enhanced | Training data de-identified by sites; production archive under BAAs; no secondary use | De-identification attestations on file | Yes |
| Fair, with harmful bias managed | Subgroup thresholds in 7.4 | Women: MAE 5.6, sensitivity 88%. Age 65 or more: MAE 5.3. **BMI 35 or more: MAE 7.4, sensitivity 81% (lower 95% bound 72%)** | **No.** Disparity for BMI 35 or more (P01 R-038) |

**Bias finding.** AI-001 is less accurate for patients with a BMI of 35 or more, where image quality is harder to achieve, and only 9% of training studies come from that group. Results for women pass the thresholds but rest on fewer studies (36%), so the confidence interval is wide.

### 7.4 Bias testing plan
| Element | Plan |
|---|---|
| Groups compared | BMI (under 30, 30 to 34.9, 35 or more), sex, age (18-64, 65-79, 80 and over), race and ethnicity where recorded, acquisition setting, and device operator experience |
| Metrics | MAE and bias (mean difference) per group; sensitivity and specificity for LVEF 40% or less with 95% confidence intervals; image-quality rejection rate per group |
| Thresholds | (1) No group's MAE more than 1.5 EF points above the overall MAE. (2) Each group's sensitivity lower 95% bound at least 80%. (3) Rejection rate for any group no more than twice the overall rate. Failing any threshold blocks design freeze |
| Sample size | At least 300 studies per BMI group and 40% women in the validation set; about 2 more partner sites with higher shares of patients with a BMI of 35 or more |
| When | Before design freeze (2027-03-31), in external clinical validation, and quarterly after release |
| Mitigations if a group fails | More data for that group; acquisition guidance for high-BMI patients; a stricter quality gate for that group; otherwise narrow the intended use and state the limitation in labeling |
| Records | Results go into the design history file, the model card, the labeling, and the 510(k) |

### 7.5 MANAGE
- **Human in the loop:** the clinician acquires the images, sees the estimate with the quality indicator and the frames used, and decides. The tool does not write to the chart or order tests.
- **Monitoring after release:** quarterly subgroup error from hospitals that share full echocardiogram results; quality-gate rejection rate by site; complaint trends.
- **Incidents:** a missed or wrong estimate linked to harm is a complaint evaluated for MDR reporting (21 CFR 820.35, 803.50); security events follow P08.
- **Decommissioning:** the DDC can switch AI-001 off per hospital through a feature flag, which it will do if post-release performance falls below a threshold and cannot be fixed quickly, or if the model file fails integrity verification.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool reports quarterly performance and subgroup metrics (inventory column `monitoring`) to the committee; drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as complaints or SOC events and follow P08 where security, PHI, or consumer data is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes and prohibit training on company data.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice, lose FDA status, or change data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the AI governance committee's recommendation of 2026-08-26:
1. **AI-001:** continue development with conditions before design freeze (2027-03-31): execute the bias testing plan, including 2 more partner sites; complete the model card; run the human factors test; propose a PCCP at the next FDA meeting (POAM-025).
2. **AI-002:** approved to continue; subgroup monitoring by age and sex from 2027 Q1.
3. **AI-003:** approved to continue; extend subgroup calibration to all hospitals by 2027-06-30.
4. **AI-004, AI-006, AI-009:** may continue in current scope until committee review by 2026-11-30; no expansion. AI-009 also needs the CQRO's regulatory assessment.
5. **AI-011:** ranking stays disabled until committee review and an adverse impact analysis are complete.
6. **AI-007 and AI-008:** approved to continue; AI-007 stays prohibited for cryptographic, signing, and key-handling code.

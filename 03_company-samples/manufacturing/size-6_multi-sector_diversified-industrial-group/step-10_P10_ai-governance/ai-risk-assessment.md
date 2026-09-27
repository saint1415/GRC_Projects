# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Medical Devices, Distribution, Testing, corporate) |
| Tier / Vertical | Multi-Sector / Manufacturing |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for the priority use cases: AI-001 (AI-enabled device software function for US-2 ultrasound image analysis, the focus), AI-008 (applicant screening), and AI-006 (Testing report drafting on client data) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 2 High, 6 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber, product, and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group General Counsel, Group Chief Privacy Officer, Group HR director, Chief Product Security Officer, Medical Devices chief medical officer, VP Quality and Regulatory Affairs, Distribution VP supply chain, Testing laboratory quality director. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Medical Devices design controls | For AI-001, the QMS design history file is the record of development, verification, and validation. This assessment is an input to it, not a replacement |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-03, under POL-01 4.13)
1. **Register before use.** Every AI use case that is part of a device, touches PHI, client data, or Federal contract information, or supports decisions about people is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: the council approves, a pre-deployment impact assessment and bias testing are required, and monitoring is reported quarterly.
3. **Data rules follow the data's owner** (POL-04 4.10): no-training contract terms for every AI vendor; BAAs where PHI is involved; written client consent for Testing client data; no Federal contract information outside the FCI enclave.
4. **Regulator overlays.** Each division supplement adds its rules: FDA device requirements for Medical Devices, federal contract rules for Distribution, client confidentiality and the information barrier for Testing, and state AI employment laws for group HR.
5. **Change gate.** A material change (new model, new vendor, new data source, new decision role) triggers re-assessment before release. For AI-001, planned model updates are handled through a predetermined change control plan (PCCP) if FDA authorizes one.
6. **Approved tools only** for workforce generative AI (POL-05 4.8).

**Where the program fell short in 2026.** The standard was adopted after the Testing drafting tool (AI-006) was piloted, and that pilot skipped the change gate and client consent (scenario gap 8). AI-001 was registered on time but its bias testing is incomplete. Both are under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | US-2 ultrasound image analysis (ejection fraction estimate, view quality) | Medical Devices | High | In development; submission planned 2027 Q2 |
| AI-002 | Predictive maintenance for IX-4 and PM-7 | Medical Devices | Medium | In production |
| AI-003 | Engineering coding assistant | Medical Devices | Medium | Pilot (400 engineers) |
| AI-004 | Demand forecasting | Distribution | Medium | In production |
| AI-005 | Customer service chatbot | Distribution | Medium | In production (commercial customers only) |
| AI-006 | Test report drafting assistant | Testing | Medium | Pilot restricted to consenting clients |
| AI-007 | AI-assisted fuzzing and crash triage | Testing | Low | Approved |
| AI-008 | Applicant screening and ranking | Group | High | Proposed; not approved |
| AI-009 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |

### 2.1 AI-001: AI-enabled device software function (focus)
| Item | Description |
|---|---|
| Purpose and intended use | A clinician acquires cardiac views with the US-2 point-of-care ultrasound. AI-001 estimates left ventricular ejection fraction from the clips and flags views of low quality so the clinician can re-acquire them. **Adjunct only:** it supports, and does not replace, the clinician's assessment |
| Users / operators | Emergency, critical care, and hospital medicine clinicians trained on US-2 |
| Affected people | Adult patients receiving point-of-care cardiac ultrasound, many of them acutely ill |
| Data: training and test | 48,000 clips from 11 partner sites, **de-identified by the sites** under the HIPAA safe harbor method (45 CFR 164.514(b)(2)) before transfer. Labels from 3 expert echocardiographers per clip with adjudication. Subgroup attributes recorded: sex, age band, body mass index (BMI), heart rhythm (including atrial fibrillation), probe model, and race and ethnicity where the site provided it (62% of clips). Patients with BMI of 35 or more are 11% of the set; atrial fibrillation 9% |
| Data: production | Images and results stay on the device and in the hospital's systems under hospital control. They are not sent to the DCC, so no business associate processing is involved unless a hospital later enables cloud archiving (which would need a BAA review) |
| Build or buy | Build. A locked model: it does not learn in the field. Future retraining only under an authorized PCCP or a new submission |
| Not intended | Pediatric patients; diagnosis without clinician review; use on non-US-2 images. Any of these requires re-assessment and regulatory review |

**Applicable laws and rules (AI-001):**
| Rule | Applies? | Why |
|---|---|---|
| FD&C Act device requirements and QMSR design controls (21 CFR 820.10(c)) | **Yes** | AI-001 is a device software function and needs FDA marketing authorization. The pathway will be confirmed at an FDA pre-submission meeting |
| FD&C Act section 524B (N31-33-R05) | **Yes** | US-2 includes sponsor software and connects to hospital networks and the internet for updates, so the submission needs the 524B content. Medical Devices already produces it for US-2 (P03) |
| FDA draft guidance, *AI-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations* (January 2025; docket FDA-2024-D-4488) | Nonbinding **draft** | Recommends data management, model description, subgroup performance validation, bias control, performance monitoring, and AI-specific cybersecurity content. Still a draft as of 2026-09-25; recheck before the submission |
| FDA guidance, *Marketing Submission Recommendations for a PCCP for AI-Enabled Device Software Functions* (final; December 2024) | Nonbinding guidance | Needed if Medical Devices wants to retrain without a new submission |
| Section 1557, 45 CFR 92.210 | **Hospitals, not the company** | Hospitals that receive federal financial assistance must make reasonable efforts to identify patient care decision support tools with inputs that measure race, color, national origin, sex, age, or disability, and mitigate discrimination risk. AI-001 does not use those attributes as inputs, but performance differs by subgroup; the company will give hospitals subgroup performance data in labeling |
| FTC Act Section 5 | Yes | Performance claims must match the validated subgroup results |
| Colorado SB26-189 | Likely not | The signed act carves out FDA-regulated devices (`00_universal-framework/cross-sector/us-cross-sector-obligations.md`). Counsel is confirming how the carve-out applies to a hospital's use of AI-001 |

### 2.2 AI-008: applicant screening (employment)
| Rule | Implication |
|---|---|
| Colorado SB26-189 (effective 2027-01-01) | Employment is a consequential decision. As a deployer, the group would owe notice at the point of interaction, an explanation after an adverse outcome, human review and correction rights, and 3-year records. No size exemption |
| Illinois HB 3773 (effective 2026-01-01) | Notice to candidates when AI is used; unlawful to use AI with a discriminatory effect or zip codes as a proxy |
| NYC Local Law 144 | Bias audit within 1 year before use, public summary, and candidate notice 10 business days before use, if roles located in New York City are filled with it |
| California Civil Rights Council ADS regulations (effective 2025-10-01) | Discriminatory use of an automated decision system is unlawful; anti-bias testing is relevant to defenses; 4-year record retention |
| Title VII | Disparate-impact liability still exists by statute, even though EEOC's 2023 technical assistance was withdrawn |

### 2.3 AI-006 and the Testing information barrier
| Rule or commitment | Implication |
|---|---|
| Client NDAs | Most NDAs limit use of client information to the engagement and prohibit disclosure to third parties. An AI vendor processing client data is a third party unless the client agrees |
| Laboratory accreditation | Requires the laboratory to protect client confidential information |
| POL-02 4.3 and POL-04 4.10 | No client data in AI tools without written client consent; no cross-client or cross-division reuse of prompts, outputs, or fine-tuning |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 (substantial factor in health care decisions and can affect physical safety), AI-008 (substantial factor in employment decisions).
- **Medium:** AI-002, AI-003, AI-004, AI-005, AI-006, AI-009. Humans make the final decision, but outputs enter devices' service records, device code, business decisions, customer interactions, or client reports.
- **Low:** AI-007. Internal productivity inside the isolated test range; engineers confirm every finding; no decisions about people.

**Re-tier triggers:** AI-002 acting on devices automatically (to High); AI-003 used for signing or cryptographic code (prohibited); AI-005 opened to federal accounts (re-assess under FAR 52.204-21); AI-006 used without client consent (prohibited).

## 4. MEASURE
### 4.1 AI-001 (internal held-out test set, 7,200 clips, as of 2026-08-27; external validation not started)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Mean absolute error (MAE) against expert consensus of 6 EF points or less overall; sensitivity for EF below 40% of at least 85% | MAE 5.1; sensitivity 88% | **Provisional.** External validation at 3 sites not in the training set is required |
| Safe | Labeling and interface make clear the estimate is adjunctive; low-quality views blocked from estimates; human factors test | Labeling drafted; human factors test scheduled 2026-11 | Partial |
| Secure and resilient | AI threats (adversarial inputs, poisoned training data, model file tampering) in the US-2 threat model; model file signed in the HSM service and verified at load; model and framework in the SBOM | Not yet done | **No** (POAM-019) |
| Accountable and transparent | Model card and labeling state training sources, subgroup mix, and subgroup performance | Model card outline | Partial |
| Explainable and interpretable | View quality indicator and the frames used for the estimate shown to the clinician | Working in the prototype | Yes |
| Privacy-enhanced | Training data de-identified by sites; production data stays under hospital control | De-identification attestations on file from all 11 sites | Yes |
| Fair, with harmful bias managed | Subgroup thresholds in section 4.2 | BMI 35 or more: MAE 7.4; atrial fibrillation: MAE 7.9; women 5.3 vs men 4.9; race and ethnicity groups within 0.8 of overall where data exist | **No.** BMI and atrial fibrillation gaps flagged (P01 MD-018) |

### 4.2 AI-001 bias testing plan
| Element | Plan |
|---|---|
| Groups compared | BMI (under 25, 25-34, 35 or more), heart rhythm (sinus, atrial fibrillation), sex, age (18-64, 65-79, 80 and over), probe model, image quality grade, and race and ethnicity where recorded |
| Metrics | MAE and bias (mean error) per group; sensitivity and specificity for EF below 40%; 95% confidence intervals; inter-reader agreement per group so labels are equally reliable |
| Thresholds | (1) No group's MAE more than 1.5 points above overall. (2) Each group's sensitivity for EF below 40% at least 85% (lower 95% bound at least 80%). (3) No systematic bias over 3 points in any group. Failing any threshold blocks design freeze |
| Sample size | At least 400 clips per BMI and rhythm group in the validation set; 2 more partner sites with higher shares of patients with obesity and atrial fibrillation |
| When | Before design freeze (2027-01-31), in external validation, and quarterly after release from complaint and hospital feedback data |
| Mitigations if a group fails | More data for that group; rebalance training; suppress estimates when image quality is low; otherwise narrow the intended use and state the limitation in labeling |
| Records | Design history file, model card, labeling, and the marketing submission |

### 4.3 AI-008 (pre-deployment, vendor data and a pilot on 2025 hiring data)
| Test | Result | Pass? |
|---|---|---|
| Selection rate ratio by sex and by race and ethnicity (flag below 0.8 of the highest group) | Sex 0.91; one race and ethnicity group 0.76 | **No** |
| Vendor documentation of training data categories and intended uses (a Colorado developer duty from 2027) | Partial | Partial |
| Candidate notice and human review workflow designed | Not designed | **No** |

### 4.4 AI-006 and other Medium use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-006 drafting | Share of pilot engagements with written client consent (target 100%) | 9 of 31 (29%) | **No** (POAM-018) |
| AI-006 drafting | Reviewer-detected factual errors in drafted reports (target under 2%) | 1.4% | Yes |
| AI-002 maintenance | Precision of high-priority work orders | 81% | Yes |
| AI-004 forecasting | Stockouts of critical items attributed to forecasts | 3 in 2026 | Yes (below threshold of 5) |
| AI-005 chatbot | Conversations with AI disclosure shown; escalations answered within 1 business day | 100%; 96% | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the clinician sees the images and the view quality indicator with every estimate; no estimate is shown for low-quality views; the estimate never enters the record without the clinician's action.
- **AI-008:** if approved, recruiters review every applicant, the tool cannot reject anyone, candidates get notice and a way to request human review.
- **AI-006:** engineers draft and sign; technical reviewers check every result against raw data; only consenting clients' data.
- **AI-002, AI-004, AI-005:** people decide every service action, order, and customer outcome.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-09, MD-018, MD-019, DS-012, TS-008.

**Incident handling:** an AI-001 malfunction or performance drop is a complaint, evaluated for MDR and correction reporting (21 CFR 820.35, 803.50, 806.10; P08). Client data exposure through AI-006 follows the Testing client notice path (P08). AI-008 complaints go to HR and counsel.

**Decommissioning:** AI-001 can be disabled by a signed configuration update; AI-006 and AI-009 access can be removed centrally in SYS-G1; AI-002, AI-004, and AI-005 fall back to manual processes covered by the BIA (P05).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 ultrasound image analysis | **Continue development with conditions** (council, 2026-08-27; board risk committee informed 2026-09-15) | Bias testing plan executed with 2 added sites before design freeze (2027-01-31); AI threats in the threat model, model file signed and verified, model and framework in the SBOM by 2026-12-31 (POAM-019); FDA pre-submission meeting covering the bias plan, external validation, and a PCCP; subgroup performance in labeling |
| AI-008 applicant screening | **Not approved** | Re-submit only with an independent bias audit that passes, candidate notice and human review workflows, vendor documentation meeting Colorado developer duties, and counsel's review for each state where it would be used |
| AI-006 report drafting | **Continue for consenting clients only** | Restricted by 2026-10-15; consent clause in all new agreements by 2026-11-30; data loss prevention on findings (POAM-018) |
| AI-003 coding assistant | **Continue pilot** | Not for cryptographic, signing, or key-handling code; second reviewer on every merge; license scanning |
| AI-005 chatbot | **Continue for commercial customers** | Federal accounts excluded until the vendor is inside the FCI enclave assessment (POAM-021) |
| AI-002, AI-004, AI-007, AI-009 | **Approved** | Standard monitoring; AI-009 prohibited for clinical, employment, or regulatory decisions |

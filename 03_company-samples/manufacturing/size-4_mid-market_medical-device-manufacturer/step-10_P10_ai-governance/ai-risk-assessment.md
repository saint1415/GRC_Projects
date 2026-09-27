# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed connected medical device manufacturer) |
| Tier / Vertical | Mid-Market / Manufacturing (NAICS 334510) |
| Scope | Portfolio of 6 AI use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv` |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-004, AI-005, and AI-006 |
| Assessors / date | Chief Medical Officer and Director of Clinical Affairs (clinical), VP Engineering and Product Security Manager (model and security), VP QA/RA (regulatory and QMS), vCISO and Security Manager (enterprise security), Compliance and Privacy Officer (privacy); 2026-08-24 to 2026-09-09 |
| Decision | Chief Operating Officer and Chief Medical Officer, 2026-09-17; High-tier decisions noted by the CEO |

## 1. Summary
AI appears in three different places at this company, and each needs a different control:
- **In the products** (AI-001 on the market, AI-002 in development). These are device software functions. FDA design controls, the authorized predetermined change control plan (PCCP) for AI-001, and section 524B govern them. This assessment feeds the design history file; it does not replace it.
- **In production and quality** (AI-003 optical inspection, AI-005 complaint summarization). These are QMS and production software, so the QMSR's software validation expectations apply (ISO 13485 clauses 7.5.6 and 4.1.6).
- **In the workforce** (AI-004 coding assistant, AI-006 public tools). These are enterprise tools under POL-05 and STD-05.

Only AI-001 had a governance process before this assessment (gap 13). The main findings:
- **AI-001:** postmarket sensitivity for the darkest skin tones has fallen below the company's threshold at hospitals using a new camera model.
- **AI-005:** switched on by Quality without validation, and the eQMS vendor's own SOC 2 report is qualified on the release of this feature (P09).
- **AI-006:** public AI tools are prohibited but not blocked.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Skin-image analysis device software function (on market) | High | Continue with conditions; camera-model investigation and PCCP retraining |
| AI-002 | Alarm artifact reduction model for VM-7 (in development) | High | Continue development with conditions before design freeze |
| AI-003 | Automated optical inspection on Line 1 | Medium | Approve with conditions; lock model version; validate updates |
| AI-004 | Enterprise coding assistant | Medium | Approve with conditions |
| AI-005 | eQMS complaint summarization | Medium (managed with High-tier controls until validated) | Conditional: validate by 2026-11-30 or switch off |
| AI-006 | Public AI assistants | Prohibited (would be High) | Block on company devices by 2026-11-30 |

Tiers: 2 High, 3 Medium, 0 Low, and 1 prohibited use.

## 2. GOVERN
- **Accountable owner for the AI program:** Chief Medical Officer, supported by the vCISO and the VP QA/RA. Each use case has a business owner (inventory).
- **Policies and standards:**
  - POL-01 4.15: AI tools and AI functions in products or quality processes must be approved before use.
  - POL-04 4.8: no Restricted or Confidential data in unapproved AI tools.
  - POL-05 4.8: approved tools only; human review of AI output; AI-assisted code gets normal review.
  - STD-05 AI use standard: due 2026-12-31.
- **Quality system link.** AI-001 and AI-002 are developed under design controls (21 CFR 820.10(c); ISO 13485 clause 7.3). AI-003 and AI-005 fall under production and QMS software validation (820.10(a); ISO 13485 clauses 7.5.6 and 4.1.6). This assessment is an input to those records.
- **Approved-tools list:** kept by the Security Manager. Today it lists AI-004 (enterprise contract) and, conditionally, AI-005.

### 2.1 Lightweight AI governance process
A mid-market company does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm that reuses existing roles and meetings.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Anyone who wants an AI tool, or an AI feature turned on in an existing tool (including vendor updates that add AI), submits a one-page intake: purpose, users, data, vendor, decisions affected, whether it touches a device, production, or the QMS | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; routing: device function to design controls, production or QMS software to validation, enterprise tool to security review | Security Manager with the VP QA/RA | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy, and a business or quality reviewer; validation plan if QMS or production software. **High:** full MAP and MEASURE assessment like this one, with a bias and performance plan | Security Manager; Compliance and Privacy Officer; VP QA/RA; Chief Medical Officer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (Chief Medical Officer, vCISO, VP QA/RA, Compliance and Privacy Officer), meeting monthly for 30 minutes. High: the AI review group recommends; the COO decides and informs the CEO. Device functions also follow design review | As listed | Monthly |
| 5. Monitor | Owners report the agreed metrics monthly (Medium) or monthly with a quarterly deep dive (High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: model change, new feature, new data type, new population or camera model, PCCP-authorized update, a safety event, or a vendor terms change | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. **Re-tier triggers** are listed for each use case in section 3.

## 3. MAP
| Item | AI-001 Skin images | AI-002 Alarm artifacts | AI-003 Optical inspection | AI-004 Coding assistant | AI-005 Complaint summaries |
|---|---|---|---|---|---|
| Purpose | Flag possible early pressure injuries for nurse assessment | Delay secondary notifications for likely artifact alarms by up to 15 seconds | Flag solder and placement defects | Suggest and explain code | Summarize complaints; suggest MDR reportability |
| Users | Nurses and wound care nurses at 22 hospitals | Clinicians at VM-7 hospitals (after clearance) | Line 1 operators | 140 engineers | 9 complaint handlers; Regulatory Affairs Manager |
| Affected people | Hospitalized adults at risk of pressure injury (about 3,500 images a day) | Monitored patients | None directly (device quality) | None directly (device software quality) | Patients and users whose events should reach FDA |
| Data | Skin images and identifiers (PHI) | Waveforms and alarm events | Board images | Source code | Complaint text, sometimes with identifiers |
| Build or buy | Build (locked model) | Build | Buy (vendor model, company fine-tuning) | Buy (enterprise contract) | Buy (vendor feature) |
| Generative AI? | No | No | No | Yes | Yes |
| Re-tier triggers | New camera model; new body site; pediatric use; PCCP update | Any change to what is delayed or for how long | Model update; new board family | Use on cryptographic or signing code | Suggestion shown before the human decision; automatic filing |

**Applicable laws and rules:**
| Rule | Applies to | Why |
|---|---|---|
| FD&C Act device requirements and QMSR design controls (21 CFR 820.10(c)) | AI-001, AI-002 | Device software functions need marketing authorization and design controls |
| Section 524B (N31-33-R05) | AI-001, AI-002 | Both are cyber devices; the CCC is a related system. The AI-002 submission needs the 524B package (P03 G-002) |
| FDA guidance, *Marketing Submission Recommendations for a PCCP for AI-Enabled Device Software Functions* (final; Federal Register notice of availability 2024-12-04, FR Doc. 2024-28361) | AI-001 | Nonbinding guidance on how planned model updates can be authorized in advance. AI-001's authorized PCCP allows retraining with new data under a fixed protocol and acceptance criteria |
| FDA draft guidance, *AI-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations* (notice of availability 2025-01-07, FR Doc. 2024-31543) | AI-002 | Nonbinding **draft**; no final version found in the Federal Register as of 2026-09-27. Recommends data management, model description, subgroup performance validation, and monitoring content. Recheck before the AI-002 submission |
| 21 CFR 803 and 806 | AI-001, AI-002, AI-005 | A missed injury linked to AI-001 is a complaint to evaluate for MDR; a correction to the model can be an 806 event; AI-005 touches the MDR decision process |
| QMS and production software validation (820.10(a); ISO 13485 clauses 4.1.6 and 7.5.6) | AI-003, AI-005 | Software used in production or the QMS must be validated before use and after changes |
| HIPAA Security and Privacy Rules (as business associate) | AI-001, AI-002, AI-005 | Production images, waveforms, and complaint text can be PHI held for hospitals |
| 45 CFR 92.210 (Section 1557) | Hospitals using AI-001 | Covered hospitals must make reasonable efforts to identify patient care decision support tools with inputs that measure race, color, national origin, sex, age, or disability, and mitigate discrimination risk. Skin images carry skin tone. The company gives hospitals subgroup performance data to support their duty |
| FTC Act Section 5 | AI-001, AI-002 | Marketing performance claims must be truthful and match validated subgroup results |
| State AI laws | AI-001, AI-002 | Customers are in 24 states. Colorado SB26-189 (effective 2027-01-01) carves out FDA-regulated devices, according to the repository's cross-sector file (`00_universal-framework/cross-sector/us-cross-sector-obligations.md`). Other states were not analyzed in this assessment; counsel review requested by 2026-12-31 |

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Sensitivity and specificity against wound-nurse bedside assessment, from quarterly hospital outcome samples | Sensitivity at least 85% overall; specificity at least 80% | 2026 Q2 (1,450 confirmed cases): sensitivity 88%, specificity 83% | Yes |
| AI-001 | Fair, harmful bias managed | Sensitivity by Fitzpatrick group; each group's lower 95% bound at least 80%; no group more than 5 points below overall | As stated | I-II 90%; III-IV 88%; **V-VI 81% (lower bound 76%)** | **No** |
| AI-001 | Fair (drift) | Sensitivity by camera model | No model more than 5 points below overall | New camera model at 4 hospitals: 79% overall, 72% for V-VI | **No** |
| AI-001 | Secure and resilient | Model file signed and verified like firmware; model and framework in the SBOM; adversarial images in the threat model | All true | All true (verified in P07 SI-7 tests) | Yes |
| AI-001 | Accountable and transparent | Model card and labeling state data sources, skin tone mix, and subgroup results | Current | Current as of clearance; not yet updated for postmarket results | Partial |
| AI-001 | Privacy-enhanced | Production images used for retraining only with hospital agreement and de-identification | Contract terms in place | 6 of 22 hospitals have signed retraining data terms | Partial |
| AI-002 | Safe | True alarms delayed (false artifact calls) on the held-out test set | Below 0.5% of true critical alarms; zero for asystole and ventricular fibrillation | 0.8% overall; zero for asystole and ventricular fibrillation | **No** (design iteration under way) |
| AI-002 | Fair, harmful bias managed | Artifact-call error rates by skin tone, age band, sex, and rhythm type | No subgroup more than 1.5 times the overall rate | Not yet measured; skin tone labels missing for 60% of training events | **No** (plan below) |
| AI-003 | Valid and reliable | Escape rate: defects found at board test that AOI passed | No more than the pre-model baseline (0.3%) | 0.21% (2026 H1) | Yes |
| AI-003 | Accountable | Model version locked and each update validated | 100% | 2 vendor updates in 2025 applied without validation | **No** |
| AI-004 | Secure | Static analysis findings per 1,000 lines, AI-assisted versus not | No worse than baseline | 1.9 versus 2.0 | Yes |
| AI-004 | Privacy and IP | License scan hits in AI-assisted code; secrets detected in prompts by data loss prevention | Zero unresolved | 3 license hits resolved; 0 secrets | Yes |
| AI-005 | Valid and reliable | Suggestion agreement with the final MDR decision (sample of 60 complaints, 2026-05 to 2026-08) | Missed reportable events: zero | 1 of 7 reportable events suggested "not reportable" (the handler reported it correctly) | **No** |
| AI-005 | Accountable | Human decision recorded before the suggestion is seen | 100% | 0% (suggestion shown first) | **No** |
| AI-006 | Privacy and IP | Traffic to public AI domains from company devices | Zero | 1,240 sessions in August 2026 from 96 users | **No** |

### 4.1 Bias testing plan (AI-001 postmarket and AI-002 premarket)
| Element | AI-001 (postmarket) | AI-002 (before design freeze) |
|---|---|---|
| Groups compared | Fitzpatrick I-II, III-IV, V-VI (primary); sex; age (18-64, 65-79, 80 and over); body site; **camera model** | Skin tone (because SpO2-driven alarms can behave differently across pigmentation); age band; sex; rhythm type; motion level |
| Metrics | Sensitivity, specificity, and predictive values per group with 95% confidence intervals; annotator agreement per skin tone group | Rate of true alarms delayed; rate of artifact alarms correctly delayed; per-group confidence intervals |
| Thresholds | Each group's sensitivity lower bound at least 80%; no group more than 5 points below overall; no camera model more than 5 points below overall | No subgroup more than 1.5 times the overall rate of delayed true alarms; zero delays for asystole and ventricular fibrillation in every subgroup |
| Sample size | At least 150 confirmed cases per skin tone group per quarter, pooled across hospitals | At least 200 true alarm events per subgroup in the held-out set; collect skin tone labels from partner hospitals |
| Reference standard | Wound-nurse bedside assessment, not the photo | Clinician-adjudicated alarm review |
| When | Quarterly; after any camera model change; after any PCCP retraining | Before design freeze (2027-01-31) and in the clinical validation |
| If a group fails | Investigation; PCCP retraining within the authorized protocol; if not fixed, narrow the supported camera models in labeling; evaluate whether a correction (806) is needed | Collect more data; redesign; narrow the intended use; no design freeze until thresholds are met |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** a nurse assesses every image; the standard skin assessment schedule never changes; nurses can dismiss a flag with a reason, and dismissal rates are monitored by skin tone group.
- **AI-002:** primary bedside alarms are never delayed or silenced; the delay applies only to secondary notifications, is capped at 15 seconds, and is logged; units can turn it off.
- **AI-003:** operators review every flag; board test and final test catch functional defects.
- **AI-004:** every change is reviewed; not used for cryptographic, signing, or key-handling code.
- **AI-005:** the handler records an independent MDR decision before seeing the suggestion; the Regulatory Affairs Manager reviews disagreements.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group; AI-001 and AI-002 also get a quarterly deep dive. Results feed the risk register (P01 R-033 to R-037).

**Incident handling:**
- Security events involving AI (adversarial images, model file tampering, prompt injection in AI-005) follow P08.
- A missed injury linked to AI-001, or a delayed true alarm linked to AI-002, is a complaint evaluated for MDR reporting (820.35(a); 803.50).
- A model change made to reduce a risk to health is evaluated as a possible correction (806.10).

**Decommissioning:**
- AI-001: switched off per hospital by feature flag if performance falls below a threshold and cannot be fixed quickly, if the model file fails integrity checks, or if a BAA amendment lapses.
- AI-003: revert to the locked prior model version if escapes exceed baseline.
- AI-005: switched off if not validated by 2026-11-30 or if the vendor changes data-use terms.
- Any tool: stopped if the vendor changes data-use terms or the model changes without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Continue with conditions** | Camera-model investigation and hospital notice with interim guidance (use the validated camera models) by 2026-10-31; PCCP retraining with more type V-VI images from the new camera model, under the authorized protocol, by 2027-01-31; updated model card and subgroup data to hospitals by 2027-01-31; VP QA/RA evaluates whether the interim notice is a correction under part 806 | COO and CMO, 2026-09-17; noted by the CEO |
| AI-002 | **Continue development with conditions** | Skin tone labels for training and test data; bias plan in section 4.1 executed; delayed-true-alarm rate below 0.5% before design freeze (2027-01-31); FDA pre-submission meeting request | COO and CMO, 2026-09-17; noted by the CEO |
| AI-003 | **Approve with conditions** | Lock the model version; validate each vendor update under the production software validation procedure; retroactive validation of the 2025 updates by 2026-12-31 | Plant Manager and VP QA/RA, 2026-09-17 |
| AI-004 | **Approve with conditions** | Keep the enterprise contract terms; data loss prevention for secrets; exclusion for cryptographic code enforced by repository rules by 2026-12-31 | VP Engineering, 2026-09-17 |
| AI-005 | **Conditional** | Hide suggestions until the handler decides (by 2026-10-15); validate under ISO 13485 clause 4.1.6 and obtain the model provider's no-training terms by 2026-11-30, or switch it off | VP QA/RA and COO, 2026-09-17 |
| AI-006 | **Prohibited; block** | Block public AI domains on company devices and add a data loss prevention rule for code by 2026-11-30 | Security Manager, 2026-09-17 |

The conditions are tracked as POAM-018 in P07 and in the risk register (P01 R-033 to R-037). The AI review group holds its first monthly meeting on 2026-10-06.

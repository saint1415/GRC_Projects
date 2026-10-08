# AI Governance Risk Assessment: AI Use-Case Portfolio, Led by the Sepsis Prediction Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed 112-bed community acute-care hospital) |
| Tier / Vertical | Mid-Market / Healthcare and Public Health |
| Scope | Portfolio of 6 AI and decision support use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv`. Full assessment of AI-001, the registry default use case |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-003 and AI-006 |
| Assessors / dates | Chief Medical Officer (clinical), Compliance and Privacy Officer (privacy, Section 1557 Coordinator), vCISO and Information Security Manager (security), CNO and the ED Medical Director (sepsis workflow), Quality Director (validation data); 2026-08-17 to 2026-08-28 |
| Decision | Chief Operating Officer and Chief Medical Officer on the recommendation of the Clinical Decision Support Committee, 2026-09-17; High-tier decisions noted by the CEO |

## 1. Summary
No AI tool at the hospital went through a security, privacy, or clinical review before use (EV-055). The sepsis model arrived switched on in an EHR upgrade; the imaging triage software was bought by Imaging; the ED scribe pilot started with a vendor's standard contract; the coding tool was bought by Revenue Cycle; and staff were found pasting text into public chatbots.

| ID | Use case | Risk tier | 92.210 in scope? | Decision |
|---|---|---|---|---|
| AI-001 | Sepsis prediction model (EHR vendor) | High | **Yes** (uses age) | Continue with conditions; universal screening; threshold review |
| AI-002 | Imaging triage, FDA-cleared (stroke and hemorrhage) | High | **Yes** (uses age to exclude children) | Continue with conditions |
| AI-003 | ED ambient AI scribe pilot | Medium | No, while suggestion features stay off | Continue pilot with conditions; expansion paused |
| AI-004 | EHR rule-based decision support (186 rules) | Medium | **Yes** | Continue; 1 race-based rule retired |
| AI-005 | Coding assistance | Medium | No (not clinical decision support) | Continue with a monthly accuracy audit |
| AI-006 | Public generative AI used by staff | High (if PHI entered) | No | Block for PHI; replace with an enterprise assistant under a BAA |

Tiers: 3 High, 3 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Chief Medical Officer, who chairs the **Clinical Decision Support Committee** (CMO, CNO, Pharmacy Director, ED Medical Director, a hospitalist, Quality Director, Compliance and Privacy Officer, Information Security Manager). The committee already approved order sets and alert rules; its charter was extended on 2026-09-17 to cover all AI tools. Each use case has a business owner (inventory).
- **Section 1557 duties:** Compliance and Privacy Officer, as Section 1557 Coordinator (45 CFR 92.7), keeps the 92.210(b) identification and (c) mitigation record for every patient care decision support tool.
- **Decision authority:** High tier: COO and CMO decide on the committee's recommendation and inform the CEO. Medium tier: the committee. Low tier: Information Security Manager.
- **Policies that apply:** POL-01 4.14 (approval before use, including vendor-enabled EHR features; 92.210 record), POL-04 4.6 (Restricted data only in approved tools with a no-training BAA), POL-05 4.8 to 4.10 (approved tools only; all-party recording consent; no changes to decision support settings outside committee change control). STD-05 AI use standard is due 2026-12-31.
- **Monitoring home:** results go to the committee monthly and into the hospital's quality assessment and performance improvement program (42 CFR 482.21), which already tracks sepsis outcomes.

### 2.1 Intake gate (lightweight process for a mid-market hospital)
| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | One-page intake for any AI tool or any AI feature a vendor upgrade makes available: purpose, users, patients affected, data, vendor, decisions affected | Requesting owner; IT change advisory board flags vendor feature releases | 15 minutes |
| 2. Triage | Provisional tier with the P10 rubric; purchasing gate (no purchase order without approval, POL-01 4.9) | Information Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy (BAA, no-training clause, retention), and a clinical or business reviewer. **High:** full MAP and MEASURE assessment like this one, with local validation, a bias plan, and a 92.210 record | Security, Privacy Officer, committee member | Low 1 week; Medium 2 weeks; High 6 weeks |
| 4. Decide | As in decision authority above | As listed | Monthly committee |
| 5. Monitor | Owner reports agreed metrics monthly (Medium) or monthly with a quarterly deep dive (High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: model version change, new feature, threshold change, new population, safety event | Committee | Annual |

## 3. MAP
### 3.1 AI-001 sepsis prediction model (full assessment)
| Item | Description |
|---|---|
| Purpose and intended use | Earlier recognition of sepsis in adults. Every 15 minutes the model scores each adult ED and inpatient encounter; above a threshold it alerts the assigned nurse, who performs the sepsis screen and calls the provider if positive |
| Users / operators | ED and inpatient nurses (receive alerts); ED physicians and hospitalists (act on screens) |
| Affected people | Adult ED and inpatient patients: about 29,000 scored encounters from 2025-11-03 to 2026-07-31 |
| Data | Inputs (from the vendor's source attribute display in the EHR): vital signs, laboratory results, nursing assessments, active medications, and **date of birth (age)**. The display states that race, ethnicity, language, and sex are not input features. Output: a risk score and an alert |
| Build or buy | Configure. The vendor built and trained the model; the hospital chooses where it runs and the alert threshold (the vendor default is in use) |
| Training data relevance | The vendor's source attributes describe training data from large multi-hospital systems; community hospitals of this size are represented in external validation, but subgroup results are not published |
| How it went live | Switched on in the November 2025 EHR upgrade at a nursing leader's request; no owner, threshold review, training, or validation (P01 R-024, R-025) |
| Not intended | Pediatric and obstetric patients; automatic orders; use as a diagnosis. The alert never replaces clinical judgment or the screening protocol |

### 3.2 The rest of the portfolio
| Item | AI-002 Imaging triage | AI-003 ED scribe | AI-004 Rule-based decision support | AI-005 Coding assistance | AI-006 Public generative AI |
|---|---|---|---|---|---|
| Purpose | Prioritize suspected large vessel occlusion and hemorrhage on head CT | Draft ED notes from recorded encounters | Interaction, dosing, renal, screening, and early warning alerts | Suggest codes and levels | Drafting letters and summaries |
| Users | Radiologists, overnight teleradiology, stroke team | 12 ED physicians | All prescribers, pharmacists, nurses | 14 coders | 214 staff (July 2026) |
| Affected people | About 38 head CT patients a day | About 60 ED patients a day, plus anyone else in the room | All patients | ED and outpatient patients (bills) | Any patient whose data is pasted |
| Data | CT images; DICOM metadata (age) | Audio; transcripts; notes | EHR data including age and sex | Documentation; codes | Whatever is pasted |
| Generative AI? | No (classification) | Yes | No | No (classification and extraction) | Yes |

**Applicable laws and rules (portfolio):**
| Rule | Applies to | Why |
|---|---|---|
| Section 1557, 45 CFR 92.210 | AI-001, AI-002, AI-004 | A patient care decision support tool is any automated or non-automated tool used to support clinical decision-making (45 CFR 92.4). The hospital must not discriminate through such tools (92.210(a)), must make reasonable efforts to identify tools whose input variables measure race, color, national origin, sex, age, or disability (92.210(b)), and must make reasonable efforts to mitigate the discrimination risk of each one identified (92.210(c)) |
| ONC HTI-1, 45 CFR 170.315(b)(11) | AI-001, AI-004 (indirectly) | Duties fall on the certified health IT developer: source attributes and intervention risk management for predictive decision support, available to the hospital's users. They are the hospital's main source of model documentation |
| ONC HTI-5 proposed rule (FR Doc 2025-23896, 2025-12-29; RIN 0955-AA09) | AI-001 | **Proposed only** (no final rule as of 2026-10-06). It would remove the source attribute and intervention risk management requirements of 170.315(b)(11). The hospital therefore writes the documentation duties into its EHR contract |
| FDA device status | AI-001 (vendor's determination); AI-002 (cleared device) | Whether a sepsis prediction function is a device or non-device clinical decision support turns on FD&C Act sec. 520(o)(1)(E) and FDA's Clinical Decision Support Software guidance (final guidance announced 2022-09-28, FR Doc 2022-20993; FDA's website may list later revisions). AI-002 is FDA-cleared, so a death or serious injury it contributes to is reportable under 21 CFR 803.30 |
| HIPAA Privacy and Security Rules | All | Vendors process ePHI as business associates; AI-006 has no BAA |
| Fla. Stat. 934.03(2)(d) | AI-003 | Interception of an oral communication is lawful when all parties have given prior consent |
| Medicare overpayments, 42 CFR 401.305 | AI-005 | Overpayments found through coding audits must be reported and returned by the later of 60 days after identification or the cost report due date (with suspension for a timely good-faith investigation) |
| CMS hospital QAPI, 42 CFR 482.21 | AI-001, AI-002 | Monitoring home for sepsis and stroke performance |
| State AI laws | None identified | The hospital operates only in Florida, and no Florida statute specific to clinical AI was identified for this review. Other states' AI laws (for example Colorado SB26-189) are out of scope because no services are offered there |

## 4. Risk tier
**AI-001: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`). The model influences a health care decision about a person and can affect physical safety. A missed alert can delay treatment of a condition where hours matter; a flood of false alerts teaches nurses to ignore the real ones. A nurse and a provider stand between the alert and any treatment, but the alert decides **who gets screened first**, which is a substantial factor in the timing of care.

**Minimum controls for High:** human review before action (in place by design), pre-deployment bias testing (**missed**; done now retrospectively), impact assessment (this document), notice to affected people (clinician transparency below; patient notice judged not required for an internal clinical alert, reviewed annually), and ongoing monitoring (section 6).

**Other tiers:** AI-002 High (safety; substantial factor in reading order for stroke). AI-006 High (no BAA; any PHI entered is an impermissible disclosure). AI-003, AI-004, and AI-005 Medium (a human makes every final decision, and none decides care on its own). **Re-tier triggers:** AI-003 becomes High if diagnosis or order suggestions are enabled; AI-005 becomes High if coding is ever automated without coder review.

## 5. MEASURE
### 5.1 AI-001 local validation
**Method.** The Quality Director ran an EHR report of all adult encounters from 2025-11-03 to 2026-07-31 with a sepsis diagnosis, a sepsis order set, or an alert, and applied Sepsis-3 clinical criteria. Two ED nurses and the CMO reviewed a random 100 of the resulting cases by chart; 94 of 100 met the case definition, so the report was accepted. An alert "caught" a case if it fired before, or within 1 hour of, the first sepsis order.

| Trustworthy characteristic | Test / metric | Result (2025-11-03 to 2026-07-31) | Pass? |
|---|---|---|---|
| Valid and reliable | Sensitivity at the vendor default threshold; target 75% or more | 271 of 410 confirmed sepsis cases caught (66%) | **No** |
| Valid and reliable | Positive predictive value; target 15% or more | 2,900 encounters alerted (10 per 100 scored); 271 were sepsis (9%) | **No** |
| Safe | Missed cases found by the existing protocol; harm review | 101 of the 139 missed cases were found by nurse triage screening; 38 were recognized later by a physician. Quality review found 4 cases with antibiotics delayed more than 3 hours; none had a death attributable to the delay | Partial |
| Safe | Alert response: screen documented within 1 hour; target 80% or more | 1,160 of 2,900 alerted encounters (40%) | **No.** Alert fatigue |
| Secure and resilient | Runs inside the hosted EHR under the vendor's SOC 2 controls (P09); behavior during EHR downtime | SOC 2 covers the platform, not the model; no alerts during downtime, and downtime procedures did not say so | Partial |
| Accountable and transparent | Source attributes available; owner named; staff trained | Attributes available but without subgroup performance; no owner or training before this review | **No** |
| Explainable and interpretable | Clinicians can see the main factors behind each score | Alert shows the top contributing factors (for example heart rate, lactate, age) | Yes |
| Privacy-enhanced | BAA limits vendor reuse of data | EHR vendor terms allow model improvement with customer data; BAA wording unclear | **No** (confirm by 2026-10-31) |
| Fair, with harmful bias managed | Subgroup sensitivity compared with overall (66%); flag a gap of more than 10 percentage points | Age 18-44: 22 of 41 (54%); 45-64: 70 of 112 (63%); 65+: 179 of 257 (70%). Black: 31 of 58 (53%); White: 196 of 286 (69%); Hispanic: 38 of 55 (69%); other or unknown: 6 of 11. Female 128 of 198 (65%); male 143 of 212 (67%). Spanish-preferred: 24 of 39 (62%) | **No.** Two flags (age 18-44; Black patients) |

**Bias findings.**
1. **Younger adults are missed more often.** The model uses age, and its sensitivity for adults 18-44 is 12 points below the overall rate. Younger septic patients compensate longer, so their scores cross the threshold later. This is exactly the age-input risk that 45 CFR 92.210(b)-(c) asks the hospital to identify and mitigate.
2. **Lower sensitivity for Black patients.** Race is not an input, yet 31 of 58 Black patients with sepsis were caught (53%), 13 points below the overall rate. 58 cases are enough to act on. The 92.210(a) prohibition covers discrimination through a tool even when the protected trait is not an input, so the hospital treats this as a finding to mitigate and to raise with the vendor.

**Bias and fairness testing plan (ongoing).**
| Element | Plan |
|---|---|
| Groups compared | Age (18-44, 45-64, 65 and over); sex; race and ethnicity as recorded in the EHR; preferred language (English, Spanish, other); payer (Medicaid or uninsured vs other) as a proxy for social need |
| Metrics | Sensitivity, positive predictive value, alert rate per 100 encounters, and alert-to-screen response rate, per group |
| Threshold | Flag any group whose sensitivity is more than 10 percentage points below the overall rate, or whose response rate differs by more than 10 points |
| Small numbers | About 45 sepsis cases a month. Groups with fewer than 30 cases in a quarter are reported as "watch" and pooled over a rolling 12 months |
| Vendor evidence | Request the vendor's validity and fairness results in its test and external data (170.315(b)(11)(iv)(B)(7)), by subgroup, and any results from community hospitals |
| Frequency | Monthly metrics to the committee; full subgroup review each quarter; re-validation within 60 days of any model version change |

### 5.2 Portfolio measures
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026-08 sample) | Pass? |
|---|---|---|---|---|---|
| AI-002 | Valid and reliable, safe | Discordance between flags and radiologist reports, 2026-05 to 2026-07 (3,400 head CTs) | Missed flags no more than the manufacturer's labeled performance | 290 flagged, 212 confirmed; 5 confirmed findings not flagged (all read within the normal time, 1 after 40 minutes) | Yes |
| AI-002 | Fair, harmful bias managed | Missed-flag rate by sex and age band (18-44, 45-64, 65+) | No subgroup more than 2 times the overall rate | Too few events to judge; continue quarterly; manufacturer subgroup data requested | Monitor |
| AI-002 | Fair, harmful bias managed | Patients under 18 never deprioritized | 0 delayed | 20 pediatric head CTs sampled: none flagged, all read in normal order | Yes |
| AI-003 | Accountable and transparent | Consent documented for everyone present | 100% | 22 of 40 notes (55%); 9 notes had another person present, 6 with no consent recorded | **No** |
| AI-003 | Valid and reliable | 120 notes compared with transcripts; critical errors (medication, dose, laterality, allergy) | 0 critical; minor under 5% | 2 critical (1 dose, 1 laterality; both caught at signing); minor 7% | **No** |
| AI-003 | Fair, harmful bias managed | Minor-error rate, Spanish-speaking vs English-speaking patients | Gap no more than 5 points | Spanish 13% vs English 6% | **No** |
| AI-003 | Privacy-enhanced | BAA prohibits training; audio deleted within 7 days of signing | Both contractual | BAA permits de-identified use; deletion only in documentation | **No** |
| AI-004 | Fair, harmful bias managed | 92.210(b) review of all 186 rules | 100% reviewed | 186 of 186 reviewed 2026-08-25: 58 use age, 19 use sex (12 also age), 1 used race (legacy pulmonary function interpretation rule); the LIS eGFR uses a race-free equation (confirmed with the Laboratory Director) | Yes (race rule retired) |
| AI-004 | Valid and reliable | Override rate per rule | Review any rule overridden more than 90% | 17 rules above 90% | Partial: under review |
| AI-005 | Valid and reliable | Monthly sample of 50 coded claims compared with documentation | Unsupported codes under 2% | 4 of 50 (8%) had an unsupported higher-level code | **No** |
| AI-006 | Privacy-enhanced | Web proxy review | No PHI to public tools | 214 users in July 2026; 3 confirmed pastes of patient details found in a sample of 25 sessions | **No** |
| All | Explainable and interpretable | Users can see the basis for each output | Available | Available for AI-001 to AI-005; not for AI-006 | Partial |

The 3 confirmed AI-006 pastes were referred to the Privacy Officer and handled under the insider-access runbook (P08) as possible breaches.

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the alert is a prompt to screen, never an order or a diagnosis. **Universal screening (the main mitigation):** nurses perform the sepsis screen at ED triage and at least once a shift for every adult inpatient, **whether or not the model alerts**. This protects the groups the model under-detects without withholding anything from others, which is the reasonable mitigation 92.210(c) asks for. Dismissals need a reason, reviewed monthly.
- **AI-002:** a radiologist reads every study; the flag changes order only.
- **AI-003:** the physician signs every note with an attestation; recording stops if anyone objects.
- **AI-004:** alerts are advisory; no automatic orders.
- **AI-005:** a certified coder approves every claim; suggestions above the documentation level need a second coder.
- **AI-006:** replaced by an enterprise assistant under a BAA with a no-training clause; public tools blocked on the web proxy for clinical and business networks.

**Transparency to clinicians:** a one-page guide and a 20-minute session for nurses, ED physicians, and hospitalists on AI-001: its inputs, local sensitivity and PPV, the groups where it performs worse, and that it does not replace screening. Downtime procedures now state that there are no sepsis alerts during an EHR outage.

**Change control:** thresholds and scope change only through the committee (POL-05 4.10). The EHR vendor must give notice before any model version change; the hospital re-validates within 60 days. A candidate lower threshold for AI-001 runs in the vendor's silent (score-only) mode for 60 days before any switch, to measure the extra alert burden.

**Monitoring:** section 5 metrics monthly; P01 R-024 to R-030 updated each quarter.

**Incident handling:** a missed sepsis case or a missed stroke flag with harm is reviewed as a patient safety event and reported to the vendor. If information reasonably suggests AI-002 (a device) caused or contributed to a death or serious injury, biomedical engineering and risk management report under 21 CFR 803.30 within 10 work days. A vendor security incident follows P08 and the BAA. Coding overpayments are reported and returned under 42 CFR 401.305.

**Decommissioning triggers:**
- AI-001: turn the alert off (keeping universal screening) if sensitivity stays below 55% for two consecutive quarters, if a subgroup flag persists two quarters after mitigation, or if the vendor will not provide validity and fairness documentation.
- AI-003: end the pilot if the BAA is not amended by 2026-12-31, or if critical errors continue for 2 consecutive months.
- AI-005: suspend suggestions if unsupported codes stay above 2% for 3 months after second-coder review starts.
- Any tool: stop if the vendor changes data-use terms or the model changes without notice.

## 7. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Continue with conditions.** Turning the alert off was considered and rejected: it catches most septic patients 65 and over, and universal screening covers the groups it misses | (1) Universal screening policy live 2026-10-01. (2) The Section 1557 Coordinator records the 92.210(b) identification (age) and the 92.210(c) mitigation, including the Black-patient sensitivity gap, by 2026-10-31. (3) Vendor supplies subgroup validity and fairness results, community hospital results, its written FDA regulatory status, and model change notice terms by 2026-11-30; documentation duties go into the contract at renewal so they survive if the HTI-5 proposal is finalized. (4) Privacy Officer confirms the BAA limits vendor data use by 2026-10-31. (5) Clinician training complete by 2026-11-15. (6) Silent-mode test of a lower threshold from 2026-10-01 for 60 days; committee decides by 2026-12-31 (P01 R-024 due date) | COO and CMO, 2026-09-17; noted by the CEO |
| AI-002 | **Continue with conditions** | Manufacturer subgroup performance data by 2026-12-31; quarterly discordance and subgroup monitoring; MDR step for AI-related events in the biomedical engineering procedure by 2026-12-31 | COO and CMO, 2026-09-17; noted by the CEO |
| AI-003 | **Continue pilot with conditions; no expansion** | Notice at ED registration, consent script, and a required EHR consent field by 2026-11-30; BAA amended (no training; 7-day audio deletion) by 2026-12-31; Spanish-language accuracy data from the vendor; monthly audit of 30 notes until 2 months at 100% consent | Clinical Decision Support Committee, 2026-09-17 |
| AI-004 | **Continue** | Race-based rule retired 2026-09-30 (done); review of 17 high-override rules by 2026-12-31; annual 92.210 review | Clinical Decision Support Committee, 2026-09-17 |
| AI-005 | **Continue with conditions** | Second-coder review for suggestions above the documented level from 2026-10-01; monthly 50-claim audit; counsel reviews the look-back for possible overpayments by 2026-11-30 | COO, 2026-09-17 |
| AI-006 | **Block and replace** | Public tools blocked for clinical and business networks by 2026-11-15; enterprise assistant with a BAA live by 2026-12-31; POL-05 4.8 training in the annual module | COO, 2026-09-17; noted by the CEO |

The conditions are tracked as POAM-024 in P07 and in the risk register (P01 R-024 to R-030). The committee's first AI review meeting under the extended charter is 2026-10-08.

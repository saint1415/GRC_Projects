# AI Risk Assessment: Sepsis Prediction Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural critical access hospital) |
| Tier / Vertical | Small / Healthcare and Public Health |
| AI use case | AI-001: the EHR vendor's sepsis prediction model (SYS-13), live for adult ED and inpatient encounters since 2026-03-02 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook. AI 600-1 (Generative AI Profile) does not apply: the model is a predictive model, not generative AI |
| Assessors / dates | Chief of Medical Staff, Quality and Compliance Manager (Section 1557 Coordinator), IT Manager, and the Director of Nursing; review 2026-08-17 to 2026-08-21 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases), built from the EHR release notes and source attribute display, the EHR decision support configuration, the identity provider app list and a staff survey (EV-049, EV-050, EV-006). How many staff use public chatbots, and what they paste, was not established (intake open request) |

## 1. GOVERN
- **Accountable owner:** Chief of Medical Staff (clinical performance and use). **Section 1557 duties:** Quality and Compliance Manager, as Section 1557 Coordinator (45 CFR 92.7). **Technical owner:** IT Manager (configuration, change control, vendor liaison).
- **Decision authority:** High-tier AI use cases need governing body approval on the recommendation of the medical staff quality committee. Medium tier: CEO. Low tier: IT Manager.
- **How the model went live (the governance gap).** The vendor made the model available in an EHR upgrade, and it was switched on at the request of a nursing leader to support the sepsis protocol. Nobody assessed it, set a threshold, trained staff, or named an owner (EV-049; P01 R-020, R-021). This assessment is being done after go-live.
- **Policies that apply:** POL-01 4.3 (risk review for new clinical systems and AI tools), POL-05 4.10 (no changes to clinical decision support settings outside change control), POL-04 4.8 (no Restricted data in unapproved AI tools).
- **Monitoring home:** results go to the medical staff quality committee monthly and into the CAH's quality assessment and performance improvement program (42 CFR 485.641).
- **Scale for a small hospital:** there is no AI committee. The four assessors review all AI use cases quarterly.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Earlier recognition of sepsis in adults. Every 15 minutes the model scores each adult ED and inpatient encounter; above a threshold it alerts the assigned nurse, who performs the sepsis screen and calls the provider if positive |
| Users / operators | ED and inpatient nurses (receive alerts); ED physicians and telehospitalists (act on screens) |
| Affected people | Adult ED and inpatient patients: about 2,780 scored encounters from 2026-03-02 to 2026-07-31 |
| Data | Inputs (from the vendor's source attribute display in the EHR): vital signs, laboratory results, nursing assessments, active medications, and **date of birth (age)**. The display says race, ethnicity, language, and sex are not input features. Output: a risk score and an alert |
| Build or buy | Buy and configure. The vendor built and trained the model; the hospital chooses where it runs and the alert threshold (the vendor default is in use) |
| Training data relevance | The vendor's source attributes describe training data from large multi-hospital systems. Rural and critical access hospitals are not described, and external validation sites are all larger hospitals |
| Not intended | Pediatric patients, obstetric patients, automatic orders, and use as a diagnosis. The alert must never replace clinical judgment or the sepsis screening protocol |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Section 1557, 45 CFR 92.210 (parent vertical ID N62-R07) | **Yes** | A "patient care decision support tool" is any automated or non-automated tool used to support clinical decision-making (45 CFR 92.4). The model uses **age** as an input, so the hospital must identify it (92.210(b)) and make reasonable efforts to mitigate the risk of discrimination (92.210(c)). The general prohibition (92.210(a)) also covers the other protected traits, even when they are not inputs |
| ONC HTI-1, 45 CFR 170.315(b)(11) | **Indirectly** | Duties fall on the certified health IT developer. For predictive decision support supplied with its product, the developer must support source attributes (including training data representativeness, fairness approach, external validation, and quantitative validity and fairness measures) and apply intervention risk management, and the product must let identified users at the hospital see those attributes. That is the hospital's main source of model documentation |
| ONC HTI-5 proposed rule (FR Doc 2025-23896, Dec. 29, 2025; RIN 0955-AA09) | **Proposed only** | It would remove the source attribute and intervention risk management requirements of 170.315(b)(11)(iv)-(vi). No final rule as of 2026-09-26, and the eCFR text (2026-09-23) still contains them. If finalized, the hospital would lose its regulatory source of documentation, so the contract should require it (section 6) |
| FDA device status | **Vendor's determination** | Whether a sepsis prediction function is a device or non-device clinical decision support turns on FD&C Act sec. 520(o)(1)(E) and FDA's Clinical Decision Support Software guidance (final guidance announced 2022-09-28, FR Doc 2022-20993; check FDA's site for later revisions). The hospital asks the vendor for its written regulatory status and records it |
| HIPAA Privacy and Security Rules | **Yes** | The vendor processes ePHI under the EHR BAA. The review found the vendor's terms allow use of customer data to improve its models; the Privacy Officer must confirm the BAA limits this to de-identified data or permitted data aggregation |
| CMS CAH conditions (QAPI, 42 CFR 485.641) | **Yes (monitoring home)** | Sepsis outcomes and model monitoring are tracked as a quality project |
| State AI laws | No | The hospital operates only in Florida; no Florida statute specific to clinical AI was identified for this review. Other states' AI laws are out of scope |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the model influences a health care decision about a person and can affect physical safety. A missed alert can delay treatment of a condition where hours matter; a flood of false alerts can teach nurses to ignore the real ones. Although a nurse and a provider stand between the alert and any treatment, the alert decides **who gets screened first**, which is a substantial factor in the timing of care.

**Minimum controls for High:** human review before action (in place by design), pre-deployment bias testing (**missed**; done now retrospectively), impact assessment (this document), notice to affected people (clinician transparency below; patient notice judged not required for an internal clinical alert, reviewed annually), and ongoing monitoring (section 5).

## 4. MEASURE
**Local validation method.** Two ED nurses and the Chief of Medical Staff reviewed charts for all adult encounters from 2026-03-02 to 2026-07-31 with a sepsis diagnosis, a sepsis order set, or an alert. Sepsis cases were confirmed using Sepsis-3 clinical criteria. An alert "caught" a case if it fired before, or within 1 hour of, the first sepsis order.

| Trustworthy characteristic | Test / metric | Result (2026-03-02 to 2026-07-31) | Pass? |
|---|---|---|---|
| Valid and reliable | Sensitivity at the vendor default threshold; target 75% or more | 37 of 58 confirmed sepsis cases caught (64%) | **No** |
| Valid and reliable | Positive predictive value; target 15% or more | 301 encounters alerted (10.8 per 100 scored encounters); 37 were sepsis (12%) | **No** |
| Safe | Missed cases caught by the existing protocol; harm review | 14 of the 21 missed cases were found by nurse triage screening; 7 were recognized later by the physician; no serious harm identified on review | Partial |
| Safe | Alert response: screen documented within 1 hour; target 80% or more | 118 of 301 alerted encounters (39%) | **No.** Alert fatigue |
| Secure and resilient | Runs inside the hosted EHR under the vendor's SOC 2 controls (P09); behavior during EHR downtime | SOC 2 covers the platform but not the model; no alerts during downtime, and downtime procedures do not say so | Partial |
| Accountable and transparent | Source attributes available in the EHR; owner named; staff trained | Attributes available but incomplete for local validity and fairness; no owner or training before this review | **No** |
| Explainable and interpretable | Clinicians can see the main factors behind each score | The alert shows the top contributing factors (for example heart rate, lactate, age) | Yes |
| Privacy-enhanced | BAA limits vendor reuse of data | Vendor terms allow model improvement using customer data; BAA wording unclear | **No** (confirm by 2026-10-31) |
| Fair, with harmful bias managed | Subgroup sensitivity compared with overall (64%); flag a gap of more than 10 percentage points | Age 18-64: 11 of 22 (50%) vs age 65+: 26 of 36 (72%). Black patients: 6 of 12 (50%) vs White non-Hispanic: 28 of 41 (68%); Hispanic: 3 of 5. Female 18 of 28 (64%) vs male 19 of 30 (63%) | **No.** Two flags (age 18-64; Black patients) |

**Bias findings.**
1. **Younger adults are missed more often.** The model uses age, and alert rates are three times higher for patients 65 and over than for adults under 65. Younger septic adults, often with fewer abnormal baseline values, reach the threshold later. This is exactly the age-input risk that 45 CFR 92.210(b)-(c) asks the hospital to identify and mitigate.
2. **Possible lower sensitivity for Black patients.** Race is not an input, but only 6 of 12 Black patients with sepsis were caught. Twelve cases are too few to conclude there is a real difference, and too many to ignore. The hospital treats it as a flag to act on, not a finding to dismiss.

**Bias and fairness testing plan (ongoing).**
| Element | Plan |
|---|---|
| Groups compared | Age (18-64, 65 and over); sex; race and ethnicity as recorded in the EHR; preferred language (English, Spanish, other); payer (Medicaid or uninsured vs other) as a proxy for social need |
| Metrics | Sensitivity, positive predictive value, alert rate per 100 encounters, and alert-to-screen response rate, per group |
| Threshold | Flag any group whose sensitivity is more than 10 percentage points below the overall rate, or whose alert response rate differs by more than 10 points |
| Small numbers | A small hospital sees about 12 sepsis cases a month. Groups with fewer than 20 cases are reported as "watch," pooled over rolling 12 months, and compared with the vendor's subgroup results. A flag is acted on whenever the mitigation does not reduce care for anyone else |
| Vendor evidence | Request the vendor's validity and fairness results in its test data and in external data (170.315(b)(11)(iv)(B)(7)(i)-(iv)), broken out by subgroup and any results from rural or critical access settings |
| Frequency | Monthly metrics to the medical staff quality committee; full subgroup review each quarter; re-validation after any model version change |

## 5. MANAGE
**Human-in-the-loop design:**
- The alert is a prompt to screen, never an order or a diagnosis.
- **Universal screening (the main mitigation):** nurses perform the sepsis screen at ED triage and at least once a shift for every inpatient, **whether or not the model alerts**. This protects the groups the model under-detects without withholding anything from others, which is the reasonable mitigation 92.210(c) asks for.
- Nurses and providers can dismiss an alert with a reason; dismiss reasons are reviewed monthly.
- Downtime procedures state that there are no sepsis alerts during an EHR outage and that manual screening continues.

**Transparency to clinicians:**
- A one-page guide and a 20-minute session for nurses, ED physicians, and telehospitalists: what the model uses, its local sensitivity and PPV, the groups where it performs worse, and that it does not replace screening.

**Change control:**
- The threshold and scope are changed only through the medical staff quality committee (POL-05 4.10).
- The vendor must give notice before a model version change; the hospital re-validates locally within 60 days of any change.
- A candidate lower threshold will be run in the vendor's "silent" (score-only) mode for 60 days before any switch, to measure the extra alert burden.

**Monitoring:** the metrics in section 4, monthly; P01 R-020 and R-021 are updated each quarter.

**Incident handling:** a missed sepsis case with harm is reviewed as a patient safety event and reported to the vendor. A vendor security incident follows P08 and the BAA.

**Decommissioning triggers:** turn the alert off (keeping universal screening) if sensitivity stays below 50% for two consecutive quarters, if a subgroup flag persists two quarters after mitigation, or if the vendor will not provide validity and fairness documentation.

## 6. Decision
**Continue with conditions.** Recommended by the medical staff quality committee and approved by the governing body on 2026-08-31 (High tier). Turning the alert off now was considered and rejected: it catches most septic patients 65 and over, and universal screening addresses the groups it misses. The conditions and dates:
1. Universal sepsis screening at ED triage and each inpatient shift is policy by 2026-09-15.
2. The Section 1557 Coordinator records the 92.210(b) identification (age input) and the 92.210(c) mitigation by 2026-09-30, and reviews AI-002 inputs (age and sex; confirm the laboratory's eGFR equation does not use race) by 2026-11-30.
3. The vendor supplies subgroup validity and fairness results, rural or CAH validation if any, its written FDA regulatory status, and model change notice terms by 2026-10-31. These documentation duties go into the contract at renewal, so they survive if the HTI-5 proposal is finalized.
4. The Privacy Officer confirms the BAA limits the vendor's use of hospital data for model improvement by 2026-10-31.
5. Clinician training is complete by 2026-10-31, and monthly monitoring starts in September 2026.
6. A silent-mode test of a lower threshold runs from 2026-10-01 for 60 days; the committee decides on the threshold by 2026-11-30 (P01 R-020 due date).

# AI Governance Risk Assessment: Enterprise AI Portfolio and Sepsis Prediction Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded for-profit hospital system: 8 hospitals, 1,970 beds; FL, GA, AL) |
| Tier / Vertical | Enterprise / Healthcare and Public Health |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the sepsis prediction model (SYS-15), in sections 7 to 9 |
| Inventory | `ai-use-case-inventory.csv` (12 use cases), built from the AI governance committee register as of 2026-04-30 (EV-076: 11 use cases, 8 reviewed), the AI feature intake and web filtering review (EV-077), the accounts payable vendor master (EV-039), the sepsis model configuration and upgrade record (EV-078) and the gap analysis AI inventory review of 2026-07-10 (EV-095), which added AI-006 after a vendor release in 2026-06. The `source_evidence` column names the source of each row. Not established: AI features embedded in other vendors' products that the register and the reviews did not surface (intake open request), workforce use of public AI tools from personal devices, and non-automated decision support tools (EHR alert rules, calculators, protocols), which are not yet inventoried |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook; NIST AI 600-1 (Generative AI Profile) for AI-002, AI-006, and AI-011; repository risk tier rubric |
| Assessors / dates | AI governance committee (chaired by the Chief Medical Information Officer); portfolio review and sepsis model local validation 2026-07-20 to 2026-08-14 by the data science team, two clinical nurse specialists, and the Section 1557 Coordinator |
| Decision | Executive risk committee, 2026-08-24, on the committee's recommendation of 2026-08-14 (section 10) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 4, Medium 6, Low 2 |
| Status | In production 11, Pilot 1 |
| Committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-006, AI-008, AI-010, AI-012 (all due 2026-11-30, POAM-024) |
| Patient care decision support tools identified under 45 CFR 92.210 | 4 confirmed (AI-001, AI-003, AI-004, AI-005); AI-006 under review |
| High-tier tools validated on local data at every hospital where they run | 1 of 4 (AI-003). AI-001 was revalidated in this review; AI-004 is validated only at H-01; AI-005's payer input is under review |

**Main findings:** the sepsis model's version 2 update went live on 2026-04-14 through a routine EHR upgrade without local revalidation, and this review found lower sensitivity than version 1 and two subgroup gaps (section 8). Four use cases entered through vendor feature releases and have not been reviewed. The Section 1557 inventory covers AI tools but not non-automated tools such as EHR alert rules and clinical calculators.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee and the quality and patient safety committee review quarterly.

**Members:** Chief Medical Information Officer (chair); Chief Nursing Officer; Chief Medical Officer's delegate; Chief Privacy Officer; CISO; Chief Compliance Officer (Section 1557 Coordinator role is delegated to the Director of Civil Rights Compliance, who attends); Chief Data and Analytics Officer; a delegate of the General Counsel; the patient safety officer; a laboratory director; a pharmacy leader; and a patient and family advisor. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Local validation on the system's data at each hospital where it will run; subgroup testing; 92.210 review; impact assessment; human review design; clinician training; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and change control.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.6). Since 2026-03, procurement and IT change control block AI features without an inventory ID. **New rule from this review:** a vendor model version change to a High-tier tool is a new deployment and needs local revalidation before go-live (the gap that let sepsis version 2 go live).

**Policies:** POL-04 4.8 (no Restricted data in AI tools without approval and a BAA with no-training terms); POL-05 4.6 (approved tools only) and 4.8 (no changes to decision support settings outside change control); POL-01 4.8 (no BAA, no PHI).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case; re-review on any model version change.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| HIPAA Privacy and Security Rules | Yes, for every use case with PHI | Vendors that handle PHI are business associates; BAAs with no-training and deletion terms are required |
| Section 1557, 45 CFR 92.210 | **Yes** | The system receives federal financial assistance. It must not discriminate through patient care decision support tools (92.210(a)), must make reasonable efforts to identify tools that use race, color, national origin, sex, age, or disability as inputs (92.210(b)), and must make reasonable efforts to mitigate the risk of discrimination (92.210(c)). 45 CFR 92.4 defines these tools as any automated or non-automated tool used to support clinical decision-making (section 5) |
| ONC HTI-1 decision support interventions, 45 CFR 170.315(b)(11) | **Vendor duty that the system relies on** | Applies to certified health IT developers: for predictive decision support interventions they supply, users must be able to see source attributes (including training data, fairness approach, and validity and fairness measures) and the developer must apply intervention risk management. The eCFR text current as of 2026-09-23 contains these requirements (170.315(b)(11)(iv)-(vi)), and the eCFR version history checked 2026-10-06 shows no change after 2025-10-01 |
| ONC HTI-5 proposed rule (90 FR 60970, 2025-12-29; FR Doc 2025-23896; RIN 0955-AA09) | **Proposed only** | It proposes to remove the source attribute requirements in 170.315(b)(11)(iv) and (v) and intervention risk management in (b)(11)(vi). If finalized, the system would lose its regulatory source of model documentation, so the vendor contract must require it (section 9) |
| FDA device status | **Vendor's determination** | Whether a clinical decision support function is a device turns on FD&C Act sec. 520(o)(1)(E) and FDA's Clinical Decision Support Software guidance (check FDA's site for the current version). AI-003 is FDA-cleared device software used within its indications; for AI-001 and AI-004 the system obtains the vendor's written regulatory status |
| State recording consent laws | Yes, for AI-002 | Laws differ by state; the system applies all-party prior consent in all three states. Florida worked example: interception is lawful when all parties have given prior consent (Fla. Stat. 934.03(2)(d)) |
| Federal equal employment opportunity laws | Yes, for AI-009 | Staffing forecasts affect schedules; the committee reviews for disparate effects |
| CMS hospital conditions (quality assessment and performance improvement) | Yes (monitoring home) | Sepsis outcomes and model monitoring are tracked in each hospital's quality program |
| State AI laws | No | No Florida, Georgia, or Alabama statute specific to clinical AI was identified for this review; other states' laws are out of scope |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision (here, health care or employment) or able to affect physical safety.

| ID | Use case | Tier | Status | Committee review | 92.210 tool |
|---|---|---|---|---|---|
| AI-001 | Clinical decision support (sepsis prediction) model | High | In production (H-01 to H-07) | Reviewed 2025-10-21 (version 1); re-reviewed 2026-08-14 after the version 2 update | Yes |
| AI-002 | Ambient clinical documentation (AI scribe) drafting ED and clinic notes from recorded conversations | Medium | In production (about 380 clinicians) | Reviewed 2025-12-09 | No (documentation only) |
| AI-003 | CT stroke and intracranial hemorrhage triage | High | In production (8 hospitals) | Reviewed 2025-11-18 | Yes |
| AI-004 | Inpatient deterioration index for rapid response team alerts | High | In production (H-01 to H-03) | Reviewed 2026-01-20 | Yes |
| AI-005 | Readmission risk model for discharge planning and transitional care calls | High | In production | Reviewed 2026-02-17 | Yes |
| AI-006 | Patient portal message draft replies | Medium | Pilot (60 clinicians) | Not reviewed (enabled by a vendor release in 2026-06; review due 2026-11-30) | Under review |
| AI-007 | Computer-assisted coding and clinical documentation integrity queries | Medium | In production | Reviewed 2025-09-23 | No |
| AI-008 | Surgical case duration prediction for operating room scheduling | Low | In production | Not reviewed (vendor feature; review due 2026-11-30) | No |
| AI-009 | Nurse staffing and census forecasting | Medium | In production | Reviewed 2026-03-17 | No |
| AI-010 | Prior authorization and denial prediction | Medium | In production | Not reviewed (review due 2026-11-30) | No |
| AI-011 | Enterprise generative AI assistant for workforce productivity | Medium | In production | Reviewed 2026-01-13 | No |
| AI-012 | SOC alert triage assistant | Low | In production | Not reviewed (review due 2026-11-30) | No |

**Tiering notes:** AI-001 and AI-004 are High because the alert decides who gets assessed first, which is a substantial factor in the timing of care. AI-005 is High because it decides who receives transitional care outreach. AI-002 stays Medium because a clinician reviews and signs every note. AI-009 is Medium because a person approves every schedule.

## 5. Section 1557 (45 CFR 92.210) duties
| Duty | What the system does | Status |
|---|---|---|
| (a) Do not discriminate through patient care decision support tools | Committee review before use; subgroup monitoring for High-tier tools | Partially met: 4 use cases unreviewed; sepsis version 2 not revalidated before go-live |
| (b) Identify tools with race, color, national origin, sex, age, or disability inputs (ongoing) | Inventory column `protected_characteristic_inputs`; extend to non-automated tools (EHR alert rules, calculators, protocols) by 2026-12-31 | Partially met: AI tools done; non-automated tools not yet inventoried |
| (c) Make reasonable efforts to mitigate discrimination risk for each identified tool | Universal screening for sepsis; subgroup thresholds reviewed; human review for all High-tier tools | Partially met: mitigation for AI-001 at 5 of 7 hospitals today; full plan in section 9 |

These rows match P03 (92.210(a)-(c)) and POAM-020 and POAM-024.

## 6. Portfolio controls (MANAGE)
- **Monitoring:** each High-tier tool reports quarterly performance and subgroup metrics to the committee (inventory column `monitoring`); drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as patient safety or SOC events and follow P08 where security or PHI is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts must require notice of model version changes at least 60 days ahead and delivery of validity and fairness documentation.
- **Decommissioning:** tools are retired if they fail monitoring thresholds two quarters in a row, lose FDA status, or change data-use terms; the inventory records retirement.

## 7. Full assessment of AI-001 (sepsis prediction model): GOVERN and MAP
| Item | Description |
|---|---|
| Accountable owner | Chief Medical Information Officer (clinical performance and use); the Director of Civil Rights Compliance records the 92.210 identification and mitigation; the EHR Technical Director owns configuration and change control |
| Purpose and intended use | Earlier recognition of sepsis in adults. Every 15 minutes the model scores each adult ED and inpatient encounter; above the threshold it alerts the assigned nurse, who performs the sepsis screen and calls the provider if positive |
| Users / operators | ED and inpatient nurses (alerts); ED physicians and hospitalists (act on positive screens) |
| Affected people | Adult ED and inpatient patients at H-01 to H-07; 41,200 adult inpatient encounters (including ED-to-inpatient) were scored from 2026-04-14 to 2026-07-31 |
| Data | Inputs, from the vendor's source attribute display: vital signs, laboratory results, nursing assessments, active medications, and **date of birth (age)**. The display says race, ethnicity, language, and sex are not inputs. Output: a risk score and an alert |
| Build or buy | Configure: the vendor built and trained the model; the system chooses scope and the alert threshold (one system-wide threshold since 2025) |
| What changed | Version 2 (vendor upgrade, 2026-04-14) retrained the model and changed its features. It went live with the routine EHR upgrade; the committee was not asked to review it |
| Not intended | Pediatric and obstetric patients; automatic orders; use as a diagnosis. The alert must never replace clinical judgment or the screening protocol |
| H-08 | Not in scope until the 2027-03-01 conversion; H-08 uses manual screening only |

## 8. MEASURE: local validation of version 2
**Method.** The data science team applied Sepsis-3 clinical criteria by algorithm to all 41,200 encounters and identified 2,480 sepsis cases (6.0%). Two clinical nurse specialists reviewed 200 randomly selected charts; the algorithm agreed with chart review in 92% of them. An alert "caught" a case if it fired before, or within 1 hour of, the first sepsis order. Version 1 results come from the 2025 validation.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Sensitivity at the current threshold; target 75% or more | 1,761 of 2,480 cases caught (71%); version 1 was 76% | **No** |
| Valid and reliable | Positive predictive value; target 20% or more | 6,920 encounters alerted (16.8 per 100 scored); 1,761 were sepsis (25%) | Yes |
| Safe | Alert response: screen documented within 1 hour; target 80% or more | 64% across the 7 hospitals (range 52% at H-05 to 79% at H-01) | **No.** Alert fatigue after the alert rate rose |
| Safe | Harm review of missed cases | Sample of 60 missed cases: 51 found by nurse screening; 9 recognized later by the physician; 2 referred to patient safety review | Partial |
| Secure and resilient | Runs inside the ECIS under its controls (P02); behavior during downtime | No alerts during EHR downtime; downtime procedures now say manual screening continues | Yes |
| Accountable and transparent | Source attributes available; owner named; change control | Attributes available but missing subgroup results for version 2; version 2 bypassed committee review | **No** |
| Explainable and interpretable | Clinicians see the main factors behind each score | The alert shows top contributing factors | Yes |
| Privacy-enhanced | BAA limits vendor reuse of data | BAA allows model improvement only with de-identified data (confirmed by the Privacy Officer 2026-08-10) | Yes |
| Fair, with harmful bias managed | Subgroup sensitivity compared with overall (71%); flag a gap of 7 points or more in groups with 100 or more cases | See the table below | **No.** 2 flags |

**Subgroup sensitivity (version 2, H-01 to H-07, 2026-04-14 to 2026-07-31):**
| Group | Sepsis cases | Caught | Sensitivity | Result |
|---|---|---|---|---|
| Age 18-64 | 980 | 617 | 63% | Flag |
| Age 65 and over | 1,500 | 1,144 | 76% | No flag |
| Female | 1,150 | 805 | 70% | No flag |
| Male | 1,330 | 956 | 72% | No flag |
| Black | 560 | 358 | 64% | Flag |
| White non-Hispanic | 1,380 | 1,021 | 74% | No flag |
| Hispanic | 470 | 329 | 70% | No flag |
| Other or unknown race | 70 | 53 | 76% | Watch (fewer than 100 cases) |
| Preferred language English | 2,090 | 1,489 | 71% | No flag |
| Preferred language Spanish | 310 | 214 | 69% | No flag |
| Other preferred language | 80 | 58 | 72% | Watch (fewer than 100 cases) |

**Bias findings.**
1. **Younger adults are missed more often (Age 18-64).** The model uses age, and younger septic adults reach the threshold later. This is the age-input risk 45 CFR 92.210(b)-(c) asks the system to identify and mitigate. The gap widened from 9 to 13 points between versions 1 and 2.
2. **Lower sensitivity for Black patients (Black).** Race is not an input, but with 560 cases the difference is unlikely to be chance. Likely contributors are differences in when laboratory tests are ordered and in baseline values. The general prohibition in 92.210(a) covers this even though race is not an input.
3. **Spanish-speaking patients** are 2 points below overall: within the threshold, but watched quarterly.

## 9. MANAGE: controls for AI-001
**Human-in-the-loop design:**
- The alert is a prompt to screen, never an order or a diagnosis.
- **Universal screening (the main mitigation):** nurses perform the sepsis screen at ED triage and at least once a shift for every adult inpatient, **whether or not the model alerts**. This protects the groups the model under-detects without withholding anything from others, the reasonable mitigation 92.210(c) asks for. Today it runs at H-01 to H-05; H-06 and H-07 start by 2026-10-31.
- Clinicians can dismiss an alert with a reason; dismiss reasons are reviewed monthly.

**Threshold and alert burden:**
- A lower threshold and an age-adjusted option will run in the vendor's silent (score-only) mode for 60 days from 2026-09-15 to measure sensitivity gains and extra alerts; the committee decides by 2026-11-30 (POAM-020).
- Hospitals with alert response below 70% (H-05, H-06) get unit-level coaching and a review of alert routing to charge nurses.

**Vendor documentation and change control:**
- The vendor must supply version 2 validity and fairness results by subgroup, external validation results, and its written FDA regulatory status by 2026-10-31.
- At renewal, the contract will require 60 days' notice of model changes, subgroup performance documentation, and a silent-mode option before any version goes live. These terms protect the system if the HTI-5 proposal removes the source attribute requirements.
- Any future version change is treated as a new deployment (section 2).

**Transparency to clinicians:** a one-page guide and a 20-minute session for nurses and physicians: what the model uses, its local performance, the groups where it performs worse, and that it does not replace screening. Completion target 90% by 2026-12-31.

**Monitoring:** monthly sensitivity, PPV, alert rate, and alert response by hospital; quarterly subgroup review; results to the committee and each hospital's quality program; P01 R-010 updated quarterly.

**Incident handling:** a missed sepsis case with harm is reviewed as a patient safety event and reported to the vendor. A vendor security incident follows P08 and the BAA.

**Decommissioning triggers:** turn the alert off (keeping universal screening) if sensitivity stays below 65% for two consecutive quarters, if a subgroup flag persists two quarters after mitigation, or if the vendor will not provide validity and fairness documentation.

## 10. Decisions
The executive risk committee approved these decisions on 2026-08-24, on the AI governance committee's recommendation of 2026-08-14:
1. **AI-001:** continue with conditions: universal screening at all 7 hospitals by 2026-10-31; silent-mode threshold test with a decision by 2026-11-30; vendor documentation by 2026-10-31; clinician training by 2026-12-31; 92.210(b) identification and (c) mitigation recorded by the Director of Civil Rights Compliance by 2026-09-30. Turning the alert off was considered and rejected: it catches most cases, and universal screening addresses the groups it misses.
2. **Version change rule:** any model version change to a High-tier tool needs local revalidation and committee approval before go-live (effective immediately).
3. **AI-004:** validate at H-02 and H-03 by 2027-03-31 before any expansion.
4. **AI-005:** complete the payer-as-proxy review by 2026-12-31.
5. **AI-006, AI-008, AI-010, AI-012:** may continue in current scope until committee review by 2026-11-30; no expansion (POAM-024).
6. **92.210 inventory:** extend to non-automated tools by 2026-12-31 (POAM-020).

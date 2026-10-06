# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Hospital System, Health Plan, College, corporate) |
| Tier / Vertical | Multi-Sector / Healthcare and Public Health |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for three priority use cases. **Priority 1:** the sepsis prediction model in all 9 hospitals (AI-001). **Priority 2:** the Health Plan prior authorization triage model in shadow mode (AI-006). **Priority 3:** the College's online exam proctoring (AI-008) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook; the Generative AI Profile (AI 600-1) for the generative use cases (AI-003, AI-005, AI-009, AI-010). AI 600-1 does not apply to AI-001, a predictive model |
| Assessors / dates | Group AI council (chaired by the Group Chief Risk Officer). Sepsis model validation at all 9 hospitals 2026-08-10 to 2026-08-21 by the System CMIO's clinical informatics team with each hospital's sepsis coordinator; council review 2026-08-28; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (10 use cases: 3 High, 6 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of enterprise risk; receives the High-tier list each quarter |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, System CMIO, Health Plan medical director, dean of nursing, College IT director. Approves High-tier use cases and the approved-tools list |
| Hospital System clinical decision support subcommittee (of each hospital's medical staff, meeting jointly) | Clinical approval, thresholds, and monitoring of clinical AI; reports into each hospital's quality assessment and performance improvement (QAPI) program, which must measure, analyze, and track quality indicators including adverse patient events (42 CFR 482.21(a)(2)) |
| Hospital System Section 1557 Coordinator (45 CFR 92.7) | Identification and mitigation duties for patient care decision support tools (45 CFR 92.210) |
| Health Plan utilization management committee | Approves any UM policy or procedure before use, including model-assisted workflows (42 CFR 422.137(b)) |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (model supply chain, prompt injection, data leakage) |
| Group Chief Privacy Officer | PHI and education record use, BAAs, consent, de-identification |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026, under POL-01 4.12)
1. **Register before use.** Every AI use case that touches PHI, member data, or student data, or that supports decisions about people, is registered in the inventory before deployment or material change. This includes AI features that vendors switch on inside existing products.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, local validation and bias testing, and quarterly monitoring reports.
3. **No contract, no data** (POL-01 4.8; POL-04 4.9). AI vendors that handle PHI sign BAAs with no-training and retention terms; vendors that handle education records are bound as school officials.
4. **Regulator overlays.** Each division supplement adds its regulator's rules: Section 1557 and QAPI for the hospitals, Medicare Advantage UM rules for the Health Plan, FERPA and state biometric rules for the College.
5. **Change gate.** A material change (new model version, new threshold, new decision role, new hospital) triggers re-assessment before release.
6. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short.** The standard was adopted in 2026, after the sepsis model had already gone live in all 9 hospitals in 2025 at the vendor's default threshold, validated only at the flagship (scenario gap 6; P01 HS-009, HS-010). It came in time to stop the Health Plan's triage model from moving past shadow mode without UM committee review (HP-005).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Sepsis prediction model | Hospital System | High | In production at 9 hospitals; continue with conditions |
| AI-002 | Inpatient deterioration index | Hospital System | Medium | In production |
| AI-003 | Ambient AI scribe pilot (ED physicians) | Hospital System | Medium | Approved for pilot |
| AI-004 | CT intracranial hemorrhage triage | Hospital System | High | In production at the flagship |
| AI-005 | Portal message reply drafting | Hospital System | Medium | Proposed |
| AI-006 | Prior authorization triage model | Health Plan | High | Proposed (shadow mode only) |
| AI-007 | Fraud, waste, and abuse claims model | Health Plan | Medium | In production |
| AI-008 | Online exam proctoring | College | Medium | In production |
| AI-009 | AI tutoring assistant | College | Low | Approved |
| AI-010 | Enterprise generative AI assistant | Group | Medium | Approved (pilot, about 3,000 users) |

### 2.1 Sepsis prediction model (AI-001): the priority use case
| Item | Description |
|---|---|
| Purpose and intended use | Earlier recognition of sepsis in adults. The model scores each adult ED and inpatient encounter every 15 minutes; above a threshold it alerts the assigned nurse, who performs the sepsis screen and calls the provider if positive |
| Users | ED and inpatient nurses (alerts); ED physicians and hospitalists (act on positive screens) |
| Affected people | Adult ED and inpatient patients at 9 hospitals: about 190,000 scored encounters from 2026-01-01 to 2026-06-30 |
| Data | Inputs per the developer's source attribute display in the EHR: vital signs, laboratory results, nursing assessments, active medications, and **date of birth (age)**. Race, ethnicity, language, and sex are not listed as inputs |
| Build or buy | Configure. The EHR vendor built and trained the model; the Hospital System chose where it runs and uses the vendor's default threshold at all 9 hospitals |
| Not intended | Pediatric or obstetric patients, automatic orders, or use as a diagnosis |

**Applicable rules:**
| Rule | Applies? | Why |
|---|---|---|
| Section 1557, 45 CFR 92.210 | **Yes** | The hospitals receive Medicare and Medicaid funds. A patient care decision support tool is any automated or non-automated tool used to support clinical decision-making (45 CFR 92.4). The model uses **age** as an input, so the Hospital System must make reasonable efforts to identify it (92.210(b)) and to mitigate the risk of discrimination (92.210(c)). The general prohibition (92.210(a)) also covers traits that are not inputs |
| Hospital QAPI, 42 CFR 482.21 | **Yes (monitoring home)** | Each hospital's QAPI program must track quality indicators including adverse patient events; sepsis outcomes and model performance are tracked there |
| ONC HTI-1, 45 CFR 170.315(b)(11) | **Indirectly** | Duties fall on the certified EHR developer, which must support source attributes for predictive decision support (including validity and fairness information) and let users at the hospitals see them. That display is the hospitals' main source of model documentation |
| ONC HTI-5 proposed rule (FR Doc 2025-23896, 2025-12-29; RIN 0955-AA09) | **Proposed only** | It would remove the source attribute and intervention risk management requirements of 170.315(b)(11)(iv)-(vi). No final rule as of 2026-09-26. The contract should require the same documentation (section 6) |
| FDA device status | **Vendor's determination** | Whether a sepsis prediction function is a device or non-device clinical decision support turns on FD&C Act sec. 520(o)(1)(E) and FDA's Clinical Decision Support Software guidance (final guidance announced 2022-09-28, FR Doc 2022-20993). The Hospital System asks the vendor for its written regulatory status |
| HIPAA | **Yes** | The vendor processes ePHI under the EHR BAA; any vendor use of data to improve models must be limited to what the BAA permits |
| State AI laws | **No specific duty identified** | The hospitals operate in Florida and two neighboring states; no state statute specific to clinical AI was identified for this review. The cross-sector file lists Colorado SB26-189 with a carve-out for HIPAA covered entities, and the hospitals do not operate in Colorado |

### 2.2 Prior authorization triage model (AI-006): Medicare Advantage rules
| Rule | What it requires | What it means for the model |
|---|---|---|
| 42 CFR 422.137(b) | No UM policy or procedure may be used unless the UM committee has reviewed and approved it | The model and its thresholds are UM procedures. It stays in shadow mode until the committee approves it |
| 42 CFR 422.137(d) | Annual review of all UM policies; approve only those meeting 422.101(b) and 422.101(c)(1); document reasons | Any approval must show the model applies only published coverage criteria |
| 42 CFR 422.101(c)(1)(i) | Medical necessity determinations based on coverage criteria, whether the item or service is reasonable and necessary, the enrollee's medical history, physician recommendations, and clinical notes, and medical director involvement where appropriate | The model may at most support a determination; reviewers must document an individualized review of the enrollee's record |
| 42 CFR 422.566(d) | A physician or appropriate professional reviews any expected adverse medical necessity decision before it is issued | The design must never let the model issue or draft a denial |
| 45 CFR 92.210 | Identify and mitigate discrimination risk in patient care decision support tools | Whether a UM tool "supports clinical decision-making" is under counsel review; the council applies the 92.210 steps as a precaution because the model uses age |

### 2.3 Online exam proctoring (AI-008): education and biometric rules
| Rule | Implication |
|---|---|
| FERPA, 34 CFR 99.31(a)(1)(i)(B) | The vendor may receive recordings as a school official only if it performs an institutional service, is under the College's direct control for use of the records, and follows the 99.33(a) redisclosure limits; the contract must say so |
| Florida biometric data definition, Fla. Stat. 501.702 | The statute defines biometric data as automatic measurements of biological characteristics used to identify a person and excludes photographs, video or audio recordings, and data generated from them. Whether face data the vendor computes from webcam video is biometric data is **unsettled** (counsel to confirm). The College **treats it as biometric data**: notice to students, limited retention, no use to identify students across exams |
| Florida Digital Bill of Rights applicability (Fla. Stat. 501.702 "controller") | **Does not apply.** A controller must have more than $1 billion in global gross annual revenue **and** meet one of three tests: 50% or more of revenue from selling online advertisements, operating a consumer smart speaker and voice command service, or operating an app store with at least 250,000 applications. The group's revenue exceeds $1 billion, but it meets none of the three tests |
| Colorado SB26-189 (effective 2027-01-01) | Covers technology that materially influences consequential education decisions. The College has online students in many states; counsel is reviewing whether proctoring flags reviewed by faculty "materially influence" academic decisions for Colorado residents. Federal preemption efforts and litigation make the law's status unsettled (cross-sector file) |

### 2.4 Other division use cases
| Rule | Use cases | Implication |
|---|---|---|
| 45 CFR 92.210 | AI-002, AI-004; AI-003 only if suggestion features are enabled | Inventory, input review, and mitigation, as for AI-001 |
| State recording consent laws | AI-003 | In all-party consent states (Florida, Fla. Stat. 934.03(2)(d), is the worked example), recording starts only after every party consents |
| FDA device requirements | AI-004 | Duties fall on the manufacturer; the Hospital System verified the clearance and labeled intended use before deployment |
| HIPAA and FERPA | All | BAAs or school-official terms with no-training clauses; minimum necessary |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 and AI-004 (substantial factor in the timing and order of care; can affect physical safety); AI-006 (would be a substantial factor in coverage and health care decisions if used).
- **Medium:** AI-002, AI-003, AI-005, AI-007, AI-008, AI-010. Humans make the final decision, but outputs enter records or influence decisions. AI-008 stays Medium because faculty review every flag before any academic action.
- **Low:** AI-009.

**Re-tier triggers:** any automatic academic consequence from proctoring flags (AI-008 to High); enabling scribe suggestions (AI-003 to High); any production use of AI-006 (re-assessment before release); expanding AI-004 beyond worklist ordering.

## 4. MEASURE
### 4.1 Sepsis model (AI-001): validation at all 9 hospitals
**Method.** For adult ED and inpatient encounters from 2026-01-01 to 2026-06-30, each hospital's sepsis coordinator and two clinicians reviewed every encounter with a sepsis diagnosis, a sepsis order set, or an alert. Cases were confirmed with Sepsis-3 clinical criteria. An alert "caught" a case if it fired before, or within 1 hour of, the first sepsis order.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Sensitivity at the vendor default threshold; target 75% or more | 974 of 1,412 confirmed cases caught (69.0%) | **No** |
| Valid and reliable | Sensitivity by hospital; flag any hospital more than 10 points below the overall rate | Flagship 303 of 410 (73.9%); community hospitals 58% to 72%; two hospitals at 58.0% (51 of 88) and 58.1% (43 of 74) | **No.** Two hospitals flagged |
| Valid and reliable | Positive predictive value; target 15% or more | 7,560 alerted encounters; 974 were sepsis (12.9%) | **No** |
| Safe | Alert response: screen documented within 1 hour; target 80% or more | 58% | **No.** Alert fatigue (HS-010) |
| Safe | Missed cases and harm review | 438 missed cases: 371 found by nurse screening, 67 recognized later by physicians; 4 referred to peer review (no conclusions yet) | Partial |
| Secure and resilient | Behavior during EHR downtime | No alerts during downtime; downtime procedures now say so and require manual screening | Yes |
| Accountable and transparent | Owner named; source attributes reviewed; staff trained | Owner named in 2026; source attributes available but without subgroup or community-hospital results; training at the flagship only | **No** |
| Explainable and interpretable | Clinicians can see the main factors behind each score | Top contributing factors shown with each alert | Yes |
| Privacy-enhanced | BAA limits vendor use of hospital data | EHR BAA limits vendor use to services for the Hospital System; model improvement only with de-identified data | Yes |
| Fair, with harmful bias managed | Subgroup sensitivity compared with overall (69.0%); flag a gap of more than 10 points | Age 18-64: 278 of 488 (57.0%) vs 65 and over: 696 of 924 (75.3%). Black patients 137 of 236 (58.1%); White non-Hispanic 662 of 902 (73.4%); Hispanic 141 of 214 (65.9%); other or unknown 34 of 60 (56.7%, watch: small group). Female 472 of 690 (68.4%) vs male 502 of 722 (69.5%). Preferred language other than English 81 of 131 (61.8%, watch) | **No.** Two flags (adults under 65; Black patients) |

**Bias findings.**
1. **Younger adults are missed more often.** Age is an input, and septic adults under 65 often reach the alert threshold later. This is the age-input risk that 45 CFR 92.210(b)-(c) asks the Hospital System to identify and mitigate.
2. **Lower sensitivity for Black patients.** Race is not an input, but 137 of 236 Black patients with sepsis were caught (58.1%), 11 points below the overall rate. The cause is not known. The council treats it as a finding to act on and has asked the vendor for its own subgroup results.
3. **The two weakest hospitals** are the two smallest community hospitals, where nurse-to-patient ratios on nights are higher and alert response is slowest.

**Bias and fairness testing plan (ongoing).**
| Element | Plan |
|---|---|
| Groups compared | Age (18-64, 65 and over); sex; race and ethnicity as recorded in the EHR; preferred language; payer (Medicaid or uninsured vs other); hospital |
| Metrics | Sensitivity, positive predictive value, alerts per 100 encounters, and alert-to-screen response rate, per group and per hospital |
| Threshold | Flag any group or hospital whose sensitivity is more than 10 points below the overall rate, or whose response rate differs by more than 10 points |
| Small numbers | Groups with fewer than 100 cases in a half-year are reported as "watch" and pooled over 12 months |
| Vendor evidence | Validity and fairness results in the vendor's test data and external validation, by subgroup and by hospital type |
| Frequency | Monthly metrics to each hospital's QAPI program; full subgroup review each quarter to the AI council; re-validation after any model version or threshold change |

### 4.2 Prior authorization triage model (AI-006): shadow mode, 2026-05 to 2026-07
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Agreement between the model's score and the final reviewer decision | 91% of 18,400 scored requests | Partial |
| Safe (automation risk) | Share of requests the model scored "likely does not meet criteria" that reviewers approved after reading the record | 34% | **No.** Shown to reviewers, these scores could steer them toward denial |
| Fair | "Likely does not meet" rate for members under 65 with a disability indicator vs other members | 1.4 times the rate for other members | **Flagged** |
| Governance | UM committee review (422.137(b)) | Not yet presented | **No** (required before any use) |

### 4.3 Online exam proctoring (AI-008): spring 2026 term
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Share of flags confirmed as misconduct after faculty review | 96 of 1,830 flags (5.2%) in 21,300 sessions | **No.** Most flags are false alarms |
| Fair | Flag rate for students testing with approved disability accommodations vs others | 14.1% vs 8.2% | **Flagged** |
| Fair | Flag rate for students on low-bandwidth connections (rural campuses) vs others | 12.0% vs 8.4% | **Flagged** |
| Accountable | Faculty review before any academic action | 100% of sampled cases | Yes |
| Privacy-enhanced | Contract terms on face data use and retention | Contract silent on face data; recordings kept 1 year | **No** |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the alert is a prompt to screen, never an order or a diagnosis. **Universal sepsis screening** at ED triage and at least once a shift for every inpatient, whether or not the model alerts, is the main mitigation for the groups the model under-detects; it does not withhold anything from others, which is the reasonable mitigation 92.210(c) asks for. Clinicians can dismiss an alert with a reason; dismiss reasons are reviewed monthly.
- **AI-006:** scores stay hidden from reviewers. If ever approved, reviewers must see the enrollee's record before any score, the model must never draft a denial, and a physician must review every expected adverse decision (422.566(d)).
- **AI-008:** faculty review every flag; no flag alone leads to an academic penalty; students see the evidence and can appeal; accommodations are entered so the tool does not flag accommodation behavior.

**Change control:** thresholds and scope change only through the clinical decision support subcommittee and the EHR change board (POL-05 4.9). The vendor must give notice before any model version change, and each hospital re-validates within 60 days.

**Monitoring:** monthly metrics to division owners and each hospital's QAPI program; quarterly High-tier report to the AI council and the board risk committee; P01 risks GR-04, HS-009, HS-010, HP-005, ED-010; POAM-024.

**Incident handling:** an AI failure that causes patient harm, discloses PHI or student data, or breaches a contract follows P08 and POL-03. A missed sepsis case with harm is reviewed as a patient safety event and reported to the vendor.

**Decommissioning:** each use case has an off switch and a fallback that the BIA already covers (P05 BP-H15 for sepsis alerting: manual screening). Turn AI-001 off at a hospital if its sensitivity stays below 55% for two consecutive quarters after mitigation.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 sepsis model | **Continue with conditions** (council, 2026-08-28; board risk committee informed 2026-09-15) | Universal sepsis screening confirmed at all 9 hospitals by 2026-10-15; the Section 1557 Coordinator documents the 92.210(b) identification (age input) and 92.210(c) mitigation by 2026-10-31; hospital-specific thresholds tested in silent mode from 2026-10-01 to 2026-11-30, with a subcommittee decision by 2026-12-31; vendor subgroup and community-hospital validation results, written FDA regulatory status, and model change notice terms by 2026-11-30, then written into the contract at renewal (so they survive if HTI-5 is finalized); analysis of the gap for Black patients with the vendor by 2026-12-31; nurse training at the 8 community hospitals by 2026-11-30 (POAM-024) |
| AI-006 prior authorization triage | **Not approved for production** | Stays in shadow mode; before any use it needs UM committee approval (422.137(b)), a design that shows the record before any score and never drafts denials, mitigation of the disability-indicator flag, and counsel's view on 92.210 |
| AI-008 proctoring | **Continue with conditions** | Contract amendment on face data use, retention (no more than one term), and school-official terms by 2026-12-31; accommodation settings for every approved student by the spring 2027 term; flag-rate review by group each term; counsel's Colorado review before 2027-01-01 |
| AI-004 CT triage | **Continue** | Quarterly turnaround and miss review by hospital; input review under 92.210 by 2026-12-31 |
| AI-002 deterioration index | **Continue** | Subgroup review with the sepsis plan (same inputs) by 2027-03-31 |
| AI-003 AI scribe pilot | **Approved for pilot** (60 ED physicians) | Consent captured before recording; error sampling of 300 notes before any expansion |
| AI-005 portal reply drafting | **Not yet approved** | Pre-deployment review, patient-facing disclosure, and accuracy testing |
| AI-007, AI-009, AI-010 | **Approved** | Standard monitoring; AI-010 prohibited for clinical, coverage, or academic decisions |

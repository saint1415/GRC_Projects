# Regulatory Gap Analysis: Cris Santos Company Holdings | Healthcare and Public Health | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Healthcare and Public Health (focus division: Hospital System) |
| Primary regulation | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24; eCFR text checked as of 2026-09-23) |
| Division regulations | Hospital System: HIPAA plus the hospital emergency preparedness condition of participation (42 CFR 482.15). Health Plan: HIPAA, Medicare Advantage (42 CFR Part 422), and state insurance law. College: GLBA Safeguards Rule (16 CFR 314.4, agreed in its Title IV Program Participation Agreement) and FERPA (34 CFR Part 99) |
| Gap tables | `gap-analysis.csv` (Hospital System, 96 rows: 69 HIPAA and 27 for 482.15); `gap-analysis-health-plan.csv` (32 rows); `gap-analysis-college.csv` (32 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads and privacy officers, the system emergency management director, and the College IT director (Qualified Individual), coordinated by the Group Chief Privacy Officer; reviewed by group internal audit |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv), with one row per requirement for each division and the group. This section restates the results for the rules analyzed here.

### 1.1 Who is what
| Entity | Role under the main rules | Basis |
|---|---|---|
| Hospital System | HIPAA covered entity (health care provider that bills electronically); Medicare-participating hospitals bound by the conditions of participation, including 482.15; EMTALA applies to each ED | 45 CFR 160.103; 42 CFR 482.15; 42 CFR 489.24 |
| Hospital System (community-connect service) | Business associate of 64 independent practices | 45 CFR 160.103 ("business associate") |
| Health Plan | HIPAA covered entity (health plan; the definition lists the Medicare Advantage program); MA organization; licensed insurer and HMO in 5 states; business associate of 40 self-funded employer plans | 45 CFR 160.103; 42 CFR Part 422; state insurance codes |
| College | Not a HIPAA covered entity (no clinic, no health plan billing). An educational institution receiving funds under ED programs (FERPA) and a Title IV participant that agreed to comply with 16 CFR Part 314 | 34 CFR 99.1 (per N61-R01); FSA Electronic Announcement GENERAL-23-09 (per N61-R02) |
| Corporate shared services | Business associate of both covered entities; service provider and affiliate of the College under the 2025 intercompany services agreement | Intercompany BAAs; 16 CFR 314.4(a), (f) |

No regulation in this analysis has a size exemption that this group meets. 45 CFR 164.306(b) lets each covered entity weigh its size, complexity, capabilities, and costs when choosing *how* to meet a HIPAA standard, not *whether*. The Safeguards Rule's small-institution exception (16 CFR 314.6, fewer than 5,000 consumers) does not apply: the College holds customer information on about 9,600 students and 31,000 former students.

### 1.2 Two separate covered entities, and the College in between
- **No affiliated covered entity.** Under 45 CFR 164.105(b), legally separate covered entities under common ownership *may* designate themselves a single affiliated covered entity, and the designation must be documented. **None exists.** The Hospital System and the Health Plan are separate covered entities, each with its own officials, risk analysis, and breach notices. PHI moving between them is a **disclosure**: the routine admission-notice feed relies on 164.506(c)(4) (both entities have a relationship with the shared members) and must meet minimum necessary. Because the feed is routine and recurring, the Hospital System needs a standard protocol for the disclosure (164.514(d)(3)(i)) and the Health Plan one for the request (164.514(d)(4)(ii)). Neither exists (group gap 7; EV-004, EV-051, EV-053).
- **Students are hospital workforce, not College data subjects, while on rotation.** HIPAA defines workforce to include trainees under the covered entity's direct control (160.103), so the Hospital System owes them access controls and training as workforce (164.308(a)(3), (a)(5)). The College's own records about those students, including immunization and clearance records, are education records under FERPA and are excluded from PHI (160.103, "protected health information", paragraph (2)(i)). The College sends placement information to the hospitals with the students' signed consent (34 CFR 99.30).

### 1.3 Excluded requirements, with reasons
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): neither covered entity is a clearinghouse.
- **164.314(a)(2)(ii)** (other arrangements with governmental entities): the Hospital System has none; public health reporting is a permitted disclosure.
- **164.314(b)** and its four implementation specifications (group health plans): the Hospital System is not a group health plan, and for the ASO plans the Health Plan is a business associate while the plan sponsors amend their own plan documents. The holding company's employee health plan is assessed separately by Group HR.
- **482.15(g)** (transplant hospitals): no hospital has a transplant program.
- **42 CFR Part 2:** no hospital is a Part 2 program (obligations register C-HPH-R06; EV-037, EV-053).
- **FTC Health Breach Notification Rule (16 CFR Part 318):** the two health divisions act as HIPAA covered entities or business associates, which 318.1 excludes; the College operates no personal health record.
- **NYDFS Part 500:** the Health Plan is not licensed in New York.
- **COPPA, CIPA, and HIPAA hybrid entity rules** for the College: adult students, not a K-12 E-Rate recipient, and no covered health care component.

## 2. Regulation-by-division matrix
| Requirement | Hospital System | Health Plan | College | Group (corporate) |
|---|---|---|---|---|
| C-HPH-R01 HIPAA Security Rule | **Primary.** Covered entity; also business associate of 64 practices | Applies. Covered entity; business associate of 40 ASO plans | Not applicable (not a covered entity); students are hospital workforce on rotation | Applies. Business associate of both covered entities |
| HIPAA Privacy Rule | Applies. Minimum necessary; disclosure protocol for routine feeds | Applies. Minimum necessary; request protocol; 422.118 | Not applicable | Applies through intercompany BAAs |
| C-HPH-R02 Breach Notification | Own notices: 164.404-164.408; notices to practices as business associate (164.410) | Own notices; notices to ASO plans (164.410) | Not applicable | Notices to both covered entities (164.410) |
| C-HPH-R03 Security Rule NPRM | Tracked only (proposed) | Tracked only | Not applicable | Tracked only |
| C-HPH-R04 FDA sec. 524B | Indirect: procurement lever for devices (SBOMs, patch support) | Not applicable | Not applicable | Group procurement terms |
| C-HPH-R05 FTC HBNR | Not applicable (covered entity) | Not applicable | Not applicable | Not applicable |
| C-HPH-R06 42 CFR Part 2 | Not applicable (no Part 2 program) | Not applicable | Not applicable | Not applicable |
| C-HPH-R07 CMS emergency preparedness | **Applies** to all 9 hospitals (482.15), through the unified and integrated program (482.15(f)) | Not applicable | Not applicable | Data centers support the plan |
| C-HPH-R08 HPH CPGs; C-HPH-R09 405(d) HICP | Voluntary; used as the maturity overlay (HICP volume for large organizations) | Voluntary | Not applicable | Voluntary |
| C-HPH-R10 HITECH recognized security practices | Applies as a mitigating factor (42 U.S.C. 17941) | Applies as a mitigating factor | Not applicable | Supports both |
| C-HPH-R11 CIRCIA | Proposed only: hospitals with 100 or more beds would be covered (all 9 qualify) | Not addressed here | Proposed only: Title IV institutions would be covered (N61-R06) | Not in effect |
| Section 1557, 45 CFR 92.210 | Applies (Medicare and Medicaid): sepsis model and other decision support tools | Counsel review before the AI triage pilot reaches production | Not applicable | Group AI Standard (P10) |
| EMTALA, 42 CFR 489.24 | Applies to every ED; governs diversion (P08) | Not applicable | Not applicable | Not applicable |
| Medicare Advantage, 42 CFR Part 422 | Not applicable | **Applies** (422.101, 422.118, 422.137, 422.566) | Not applicable | Not applicable |
| N52-R01 GLBA; N52-R07 NAIC Model #668 where enacted | Not applicable | **Applies** in each state of operation (generic) | Not applicable | Supports the Health Plan |
| N52-R04 NYDFS Part 500 | Not applicable | Not applicable (no New York license) | Not applicable | Not applicable |
| N61-R02 GLBA Safeguards Rule (Title IV) | Not applicable | Not applicable | **Primary.** Applies through the PPA; FSA tests it in the annual compliance audit | Affiliate and service provider (314.4(a), (f)) |
| N61-R01 FERPA | Not applicable (hospitals receive placement data with consent) | Not applicable | **Applies** | File service designated as a school official function (99.31(a)(1)(i)(B)) |
| FSA breach reporting (SAIG agreement) | Not applicable | Not applicable | Applies: report immediately | Supports |
| N52-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Same | Same | Coordinates |
| SOC 2 (contractual) | Planned for the community-connect service (P09) | Not in scope; SOC 1 for ASO claims (P09) | Not in scope (P09) | Group services carved in |

## 3. Method
1. **Requirements.** HIPAA Security Rule rows and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool). NIST's dataset numbers the written-contract specification 164.308(b)(4); this analysis shows the current rule's 164.308(b)(3). The 482.15, Privacy Rule, Medicare Advantage, Safeguards Rule, and FERPA rows follow each regulation's own paragraph structure as read on the eCFR (2026-09-23); summaries are paraphrased. State insurance rows are generic, based on NAIC Model #668, whose enacted text varies by state.
2. **Crosswalk.** HIPAA rows use the Health Care crosswalk in `02_industry-rules/health-care/`: the CSF 2.0 and SP 800-53 columns are an **author mapping**, and NIST's official OLIR 110 mapping (SP 800-53 Rev. 5.1.1) is shown beside it in `nist_official_sp800_53r5_1_1`. No official NIST mapping exists for the other regulations, so their rows carry an author mapping made for this analysis.
3. **Evidence.** Current state was established from the intake evidence (exports, documents, the College's 2025 compliance audit report, EV-076, and the walk-through of 3 hospitals on 2026-04-20 to 2026-04-22, EV-060), gap analysis interviews with each division's security, privacy, clinical, emergency management, and legal leads (EV-096 Hospital System, EV-097 Health Plan, EV-098 College), the June 2026 UM case audit (60 cases, EV-099), the FERPA consent file sample (EV-100), the supplement v2026 change logs (EV-101, EV-102), and P07 test results. The `evidence` column in each gap table cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

**Addressable is not optional.** For each addressable HIPAA specification, the entity must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). No addressable gap below is being documented as unreasonable.

## 4. Results
### 4.0 Group gaps
Eight gaps cross divisions or sit in shared services. They are numbered here and cited as group gaps 1 to 8 across this sample.
1. **Ransomware resilience of the shared data centers.** The EHR's production copy (DC1) and its replica (DC2) are joined to the same group directory forest, so one compromise can reach both. A full EHR restore from the immutable vault has never been tested; the estimated rebuild time is 5 to 7 days against an 8-hour RTO. The Health Plan claims core and the College's administrative file shares sit in the same data center (EV-009, EV-017, EV-021, EV-046, EV-047).
2. **Emergency preparedness for a cyber event.** The unified emergency plan and its risk assessments are built around hurricanes and surge. They do not cover a system-wide IT outage that puts all 9 hospitals on downtime at once, and there are no system-level criteria for ambulance diversion and patient transfers during an IT outage. Downtime workstations at 3 community hospitals have not been tested in the last 12 months (EV-057, EV-058, EV-048).
3. **Medical devices and clinical OT.** The device inventory is about 81% complete; about 6,900 devices (13%) run unsupported operating systems; device network segmentation is complete at 5 of 9 hospitals; 37 of 140 vendor remote support connections bypass group PAM (EV-054, EV-055, EV-056).
4. **Student and trainee access.** About 4,500 students a year rotate through the hospitals. Their EHR accounts are created from emailed rosters outside identity governance, sign in with a password only, and have no end dates; the hospitals rely on the schools for training records (EV-042, EV-043, EV-027).
5. **The College lags group standards.** It runs its own directory and is not on SYS-G1. MFA is enforced for email but not for the student information and financial aid system. Its written risk assessment dates from 2022, and its Qualified Individual has not given the board a written report since 2023 (EV-079, EV-078, EV-077).
6. **Sepsis prediction model.** The model went live at all 9 hospitals in 2025 at the vendor's default threshold; local validation was done only at the flagship, and the 45 CFR 92.210(b)-(c) steps were not documented (EV-064).
7. **PHI exchanged between the two covered entities.** About 140,000 Health Plan members were hospital patients in the last 12 months; routine feeds between the Hospital System and the Health Plan have no written minimum-necessary protocols (EV-038, EV-051, EV-004, EV-072).
8. **Multi-regulator incident notification.** One incident could trigger notices from two covered entities and many regulators; the group notification matrix has not been exercised, and the College's 2022 incident response plan is not part of the group plan (EV-012, EV-082).

### 4.1 Hospital System: HIPAA Security Rule (`gap-analysis.csv`, rows G-001 to G-069)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 15 | 14 | 0 | 1 |
| 164.310 Physical safeguards | 10 | 2 | 0 | 0 |
| 164.312 Technical safeguards | 11 | 1 | 0 | 0 |
| 164.314 Organizational requirements | 3 | 1 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 5 | 0 | 0 | 0 |
| **Total (69)** | **44** | **18** | **0** | **7** |

Of the 18 partially met rows, 5 are standards, 6 are **Required** implementation specifications, and 7 are **Addressable**. By gap risk: 5 High, 11 Moderate, 2 Low. The program is defined and mostly compliant; the gaps sit in **contingency planning for ransomware that reaches both data centers** (164.308(a)(7), (7)(ii)(B), (7)(ii)(D), all High), **student and trainee access** (164.308(a)(3) and its specifications, 164.312(d)), **medical devices** (164.308(a)(5)(ii)(B), 164.310(d)), and one contract gap: the intercompany BAA does not expressly cover the community-connect practices' PHI that corporate hosts as a subcontractor (164.314(a)(2)(iii)).

### 4.2 Hospital System: CMS emergency preparedness, 42 CFR 482.15 (rows G-070 to G-096)
| Area | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Program and (a) emergency plan (6 rows) | 2 | 4 | 0 | 0 |
| (b) policies and procedures (3 rows) | 1 | 2 | 0 | 0 |
| (c) communication plan (4 rows) | 2 | 2 | 0 | 0 |
| (d) training and testing (6 rows) | 5 | 1 | 0 | 0 |
| (e) power, (f) integrated systems, (g) transplant (8 rows) | 6 | 1 | 0 | 1 |
| **Total (27)** | **16** | **10** | **0** | **1** |

By gap risk: 3 High, 4 Moderate, 3 Low. The rule does not use the word "cyber", but its all-hazards risk assessment ((a)(1), and for a unified program the facility-based assessments in (f)(4)) and its medical documentation element ((b)(5)) are where a system-wide EHR outage belongs. The program is strong for hurricanes and surge and silent on a ransomware attack that takes all 9 hospitals to paper at once (group gap 2). One more point matters at this size: the transfer arrangements in (b)(7) mostly point to other group hospitals, which a system-wide outage would also affect.

### 4.3 Health Plan (`gap-analysis-health-plan.csv`)
| Regulation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| HIPAA Security Rule (14 selected rows) | 6 | 6 | 0 | 2 |
| HIPAA Privacy Rule | 2 | 1 | 1 | 0 |
| Medicare Advantage (42 CFR Part 422) | 8 | 1 | 0 | 0 |
| State insurance law, GLBA, NYDFS | 3 | 1 | 0 | 1 |
| **Total (32)** | **19** | **9** | **1** | **3** |

By gap risk: 8 Moderate, 2 Low. The Health Plan's Security Rule rows focus on the specifications where its evidence differs from the Hospital System's; the rest rely on the same documented common controls. **Not met:** 164.514(d)(4)(ii) (no protocol for the routine request for hospital admission notices, group gap 7). **Utilization management:** the UM committee meets 422.137(a)-(d), every expected adverse decision gets physician review (422.566(d)), and medical necessity decisions are made by reviewers on the enrollee's record (422.101(c)(1)(i)). The AI prior authorization triage pilot runs in shadow mode; under 422.137(b) it may not be used for any UM decision until the UM committee approves it (P10).

### 4.4 College (`gap-analysis-college.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| GLBA Safeguards Rule, 16 CFR 314.4 and 314.6 (22 rows) | 4 | 14 | 3 | 1 |
| FERPA, 34 CFR Part 99 (4 rows) | 2 | 2 | 0 | 0 |
| Title IV program requirements (2 rows) | 0 | 2 | 0 | 0 |
| Other education rules screened (4 rows) | 0 | 0 | 0 | 4 |
| **Total (32)** | **6** | **18** | **3** | **5** |

By gap risk: 1 High, 16 Moderate, 4 Low. **Not met:** 314.4(b)(2) (no reassessment since 2022, which the 2025 compliance audit also reported), 314.4(c)(5) (MFA not enforced on the student information and financial aid system; **High**), and 314.4(i) (no written annual report to the board since 2023). The College is the least mature division, as expected for a business acquired in 2023 that still runs its own directory (group gap 5).

## 5. Group roadmap
| # | Gap (group gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | No tested recovery if ransomware reaches both data centers (1) | Hospital, Health Plan, College | 164.308(a)(7)(ii)(B), (D); 482.15(b)(5) | High | Clean recovery environment; full EHR restore test; directory tier and zone separation (POAM-012, POAM-007) | Group CISO | 2027-03-31 (zones 2027-06-30) |
| 2 | Emergency plan has no system-wide IT outage scenario or diversion criteria (2) | Hospital | 482.15(a)(1)-(2), (f)(4) | High | Cyber and IT outage annex; non-group transfer arrangements; exercise as the 2026-12 additional exercise (POAM-023) | System emergency management director | 2026-12-31 |
| 3 | College MFA, risk assessment, and board report (5) | College | 16 CFR 314.4(b)(2), (c)(5), (i) | High | Enforce MFA (POAM-020); new risk assessment (POAM-019); annual report (POAM-025) | College IT director | 2026-12-31 |
| 4 | Student and trainee access (4) | Hospital, College | 164.308(a)(3)(ii)(A)-(C); 164.312(d); 34 CFR 99.30 | Moderate | Identity governance, end dates, and MFA for students; secure roster feed; affiliation agreements (POAM-001, POAM-014) | Group identity director | 2026-12-31 |
| 5 | Device vendor access and device networks (3) | Hospital | 164.312(d); 164.308(a)(5)(ii)(B) | High | Vendor access through PAM (POAM-013); segmentation at 4 hospitals (POAM-015) | Clinical engineering director | 2027-06-30 |
| 6 | Minimum necessary between the covered entities (7) | Hospital, Health Plan | 164.514(d)(3)(i), (d)(4)(ii); 422.118(a) | Moderate | Joint protocol and reduced ADT feed (POAM-016) | Group Chief Privacy Officer | 2026-12-31 |
| 7 | Multi-regulator notification not exercised (8) | All | 164.308(a)(6)(ii); Model #668 sec. 6; 16 CFR 314.4(h), (j); FSA SAIG agreement | Moderate | Complete the matrix; cross-division exercise (POAM-005, POAM-021) | Group General Counsel | 2026-12-31 |
| 8 | Community-connect PHI not covered by the intercompany BAA | Hospital, corporate | 164.314(a)(2)(iii) | Moderate | Amend the intercompany BAA | Group General Counsel | 2026-12-31 |
| 9 | Sepsis model Section 1557 duties (6) | Hospital | 45 CFR 92.210(b)-(c) | High | Identification and mitigation documented; validation at every hospital (POAM-024; P10) | System CMIO | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-023 to POAM-025 trace directly to this analysis.

**One exercise, several rules.** The hospitals' next additional annual exercise under 482.15(d)(2)(ii) should be the facilitated ransomware, EHR downtime, and diversion tabletop that 164.308(a)(7)(ii)(D), the College's incident response plan (314.4(h)), and the group IR plan all call for. Filed in the emergency program records with an after-action review (482.15(d)(2)(iii)), it produces evidence for each.

## 6. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The Federal Register shows no final rule as of 2026-09-25, and the regulatory agenda projects a final rule in July 2027. If it is finalized as proposed, these verified proposals would affect the two health divisions:
- The distinction between required and addressable would be removed. The Hospital System's 7 addressable gaps would become mandatory.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (largely met).
- MFA would be required, with limited exceptions (student accounts, device vendor connections, and SMS codes for brokers fall short).
- A written technology asset inventory and network map would be required (the device inventory is 81% complete).
- Penetration testing at least every 12 months, along with vulnerability scanning.
- Certain systems and data would have to be restorable within 72 hours (the EHR rebuild estimate is 5 to 7 days).
- A compliance audit at least every 12 months.
- Business associates would notify covered entities within 24 hours of activating a contingency plan (corporate to both covered entities; the Hospital System to its 64 practices; the Health Plan to its 40 ASO plans).

The `pending_rule_change` column flags 31 Hospital System HIPAA rows the proposal would affect. None of these is treated as a current obligation.

**CIRCIA** (proposed 6 CFR Part 226) is not in effect (no final rule as of 2026-09-25). If finalized as proposed, it would cover all 9 hospitals (100 or more beds) and the College (Title IV participant), with a 72-hour incident report and a 24-hour ransom payment report to CISA. It is tracked in the P08 matrix only.

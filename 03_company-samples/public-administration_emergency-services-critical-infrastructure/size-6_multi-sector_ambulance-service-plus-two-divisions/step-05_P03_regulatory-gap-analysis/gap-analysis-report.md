# Regulatory Gap Analysis: Cris Santos Company Holdings | Emergency Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Emergency Services (focus division: Ambulance Services) |
| Primary regulation | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24) (C-EMERGENCY-R04) |
| Division regulations | Ambulance Services: HIPAA plus state EMS records rules and Medicare ambulance documentation. Urgent Care: HIPAA plus Section 1557 decision support duties and state recording consent law. BDS: HIPAA business associate duties, PCI DSS, TCPA, client contracts, and the open CJIS question |
| Gap tables | `gap-analysis.csv` (Ambulance Services: all 69 Security Rule rows plus 8 state EMS and Medicare rows); `gap-analysis-urgent-care.csv` (26 rows); `gap-analysis-bds.csv` (31 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads and division privacy officers, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit |

## 1. Applicability
Applicability was checked first for every requirement in the vertical registry, because the Emergency Services sector research was written mostly for public agencies and 911 centers. A private ambulance group with a dispatch and billing subsidiary is a different kind of entity.

### 1.1 Emergency Services registry
| Registry ID | Requirement | Applies? | Reason |
|---|---|---|---|
| C-EMERGENCY-R04 | HIPAA Security Rule | **Yes** | See 1.2 |
| C-EMERGENCY-R01 | FBI CJIS Security Policy v6.1 | **Not determined (BDS only)** | The policy governs access to criminal justice information (CJI). No division has access to state or national criminal justice databases. Under 28 CFR 20.33(a)(7), a private contractor receives criminal history record information only under an agreement with a criminal justice agency, for the administration of criminal justice, with an approved security addendum; dispatching ambulances is not that. But one county's CAD-to-CAD feed delivered premise notes copied from a sheriff's law enforcement records system from 2024-11 to 2026-08-20 (gap 5). Whether those notes are CJI is for the county and its CJIS Systems Agency to determine. The field is suppressed, and BD-G28 tracks the decision. Ambulance Services and Urgent Care: **No** |
| C-EMERGENCY-R02, R03 | 28 CFR 20.21(f); 28 CFR Part 23 | **No** | These apply to state criminal history systems and to federally funded criminal intelligence systems. The group operates neither |
| C-EMERGENCY-R05 | CIRCIA | **Not yet (proposed only)** | No final rule was in the Federal Register as of 2026-09-25. As proposed, 6 CFR 226.2(b)(5) would cover any entity that provides emergency medical services to a population of 50,000 or more, regardless of size; the Ambulance division's 38 county service areas meet that test. Tracked in P08, not treated as an obligation |
| C-EMERGENCY-R06 | FCC EAS cybersecurity rule (47 CFR Part 11) | **No** | No division is an EAS participant or originates public alerts |

### 1.2 Who is what under HIPAA
| Entity | HIPAA role | Basis |
|---|---|---|
| Ambulance Services | Covered entity (health care provider that transmits claims electronically). Medicare pays an initial claim only if it is submitted electronically (42 CFR 424.32(d)(2)), and the small-supplier exception covers only suppliers with fewer than 10 full-time equivalent employees (424.32(d)(1)) | 45 CFR 160.103 |
| Urgent Care | Covered entity (health care provider that bills electronically) | 45 CFR 160.103 |
| BDS | Business associate of both internal divisions and of about 184 external clients (170 billing, 14 dispatch); directly subject to the Security Rule | 45 CFR 160.103 ("business associate"); 164.302 |
| Corporate shared services | Business associate of both covered entities and subcontractor business associate of BDS | Intercompany BAAs (2023) |

There is no size exemption. 45 CFR 164.306(b) lets each entity consider its size, complexity, capabilities, and costs when choosing *how* to meet a standard, not *whether* to meet it.

**Affiliated covered entity decision.** Under 45 CFR 164.105(b), legally separate covered entities under common ownership may designate themselves a single affiliated covered entity. Ambulance Services and Urgent Care have **not** done so. Each keeps its own security and privacy officials, its own risk analysis, and its own breach notices (P08). They share little PHI directly: both send data to BDS for billing, which acts for each as a business associate.

### 1.3 Excluded requirements, with reasons
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): no division is a clearinghouse.
- **164.314(a)(2)(ii)** (arrangements with governmental entities): no governmental entity acts as a business associate. County PSAPs exchange data with the group for dispatch and treatment.
- **164.314(b)** and its four implementation specifications (group health plans): no division sponsors a group health plan; the group's employee plan is assessed separately by Group HR.
- **42 CFR Part 2:** no division runs a federally assisted substance use disorder program.
- **FTC Health Breach Notification Rule (16 CFR Part 318):** every division acts as a HIPAA covered entity or business associate.
- **CMS emergency preparedness conditions:** an eCFR search of title 42 found these conditions only for named provider and supplier types (for example 42 CFR 482.15 for hospitals, 416.54 for ambulatory surgical centers, 491.12 for rural health clinics and FQHCs). Ambulance suppliers and clinics that bill as physician practices are not among them.
- **Florida Digital Bill of Rights:** not applicable. The group exceeds $1 billion in global gross annual revenue but meets none of the three additional tests in Fla. Stat. 501.702 (50% or more of revenue from online advertising, a consumer smart speaker and voice command service, or an app store with at least 250,000 applications).

## 2. Regulation-by-division matrix
| Requirement | Ambulance Services | Urgent Care | BDS | Group (corporate) |
|---|---|---|---|---|
| C-EMERGENCY-R04 HIPAA Security Rule | **Primary.** Covered entity | Applies. Covered entity | Applies. Business associate (164.302) | Applies. Business associate of both covered entities |
| N62-R02 HIPAA Privacy Rule | Applies. Release of records; minimum necessary | Applies. Identity verification; minimum necessary | Applies through BAAs (164.502(a)(3); 164.504(e)) | Applies through intercompany BAAs |
| N62-R03 Breach Notification | Own notices: 164.404-408 | Own notices: 164.404-408 | Notice to each affected client and internal division: 164.410 and BAA terms | Notice to both covered entities and BDS: 164.410 |
| N62-R04 Security Rule NPRM | Tracked only (proposed) | Tracked only | Tracked only | Tracked only |
| C-EMERGENCY-R01 CJIS Security Policy | No | No | **Not determined** (one county feed; BD-G28) | Supports the determination |
| C-EMERGENCY-R05 CIRCIA | Proposed only; would apply if finalized as proposed | Proposed only | Proposed only | Proposed only; reporting would be coordinated by the group |
| C-EMERGENCY-R06 FCC EAS | No | No | No | No |
| State EMS law (Florida worked example: Fla. Stat. 401.30; Rule 64J-1.014, F.A.C.) | **Applies** in each state of operation | No | Supports (holds records for Ambulance) | No |
| Medicare ambulance documentation (42 CFR 410.40(e), 410.41(c), 424.516(f)) | **Applies** | No | Supports (claims and retention) | No |
| N62-R07 Section 1557, 45 CFR 92.210 | Applies (Medicaid): AI call triage is treated as a decision support tool (P10) | **Applies** (Medicare and Medicaid): clinical calculators, scribe, symptom checker | Operates the AI triage tool for Ambulance | Group AI Standard (P10) |
| State recording law (Florida worked example: Fla. Stat. 934.03) | Applies to dispatch call recording (934.03(2)(g)) | Applies to the AI scribe (934.03(2)(d)) | Applies to communications center and contact center recording | No |
| N56-R06 PCI DSS v4.0.1 (contract) | No | Clinic card payments through the processor's terminals (merchant; outside this analysis) | **Applies** to the billing contact center, including as a service provider to clients | Supports |
| N56-R05 TCPA | No | No | Applies to outbound patient balance calls and texts | No |
| N56-R01, N56-R02, N56-R03 Disposal Rule, FCRA, Form I-9 | Via Group HR | Via Group HR | Via Group HR | **Applies** (Group HR hires for every division; assessed by Group HR outside this analysis) |
| SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Same | Same, plus third-party agent duties to clients where state law sets them | Coordinates |
| County ambulance agreements and client contracts | 38 agreements (outage notice, response standards) | No | 14 dispatch and about 170 billing client contracts | Group General Counsel |
| SOC 2 (contractual) | Out of scope (P09) | Out of scope (P09) | Revenue cycle Type 2 annually; dispatch readiness (P09) | Group services carved in |

## 3. Method
1. **Requirements.** HIPAA Security Rule rows and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool). Privacy Rule, Breach Notification, Section 1557, Medicare, and TCPA rows cite the eCFR text directly; Florida rows cite the statute or rule as the worked example. PCI DSS rows list requirement numbers with short topic labels written for this analysis, because the standard is copyrighted.
2. **Crosswalk.** Security Rule rows in `gap-analysis.csv` use the Health Care crosswalk in `02_industry-rules/health-care/`, an **author mapping**, because NIST has not published a HIPAA to CSF 2.0 mapping. NIST's official SP 800-53 mapping (OLIR 110) is shown next to it in the `nist_official_sp800_53r5_1_1` column. All other rows carry an author mapping made for this analysis.
3. **Evidence.** Interviews with each division's security, privacy, clinical, communications, and legal leads; document review; configuration exports; a sample of 40 non-emergency ambulance claims; a sample of 200 AI scribe visits; a sample of 200 recorded card payment calls; a mystery-caller test of 20 clinics; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable.

**Addressable is not optional.** For each addressable specification, the entity must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). One equivalent alternative is documented: dispatch consoles do not auto-lock (164.312(a)(2)(iii)) because telecommunicators must see live calls, so the badge-controlled dispatch floor is the equivalent measure.

## 4. Results
### 4.1 Ambulance Services (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 17 | 12 | 0 | 1 |
| 164.310 Physical safeguards | 9 | 3 | 0 | 0 |
| 164.312 Technical safeguards | 6 | 6 | 0 | 0 |
| 164.314 Organizational requirements | 4 | 0 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 5 | 0 | 0 | 0 |
| **HIPAA Security Rule total (69)** | **41** | **21** | **0** | **7** |
| State EMS records rules, Florida worked example (5) | 3 | 2 | 0 | 0 |
| Medicare ambulance documentation (3) | 1 | 2 | 0 | 0 |
| **All rows (77)** | **45** | **25** | **0** | **7** |

Of the 21 partially met HIPAA rows, 9 are standards, 7 are **Required** implementation specifications, and 5 are **Addressable**. Across all 25 partially met rows, gap risk is High for 4, Moderate for 14, and Low for 7. Ambulance Services is mostly compliant. Its gaps sit in two places: the shared dispatch platform it depends on (contingency, vendor access, and notification; gaps 1, 2, and 7) and the fleet devices its own fleet technology team runs outside group management (gap 4). The four High gaps are risk management (164.308(a)(1)(ii)(B)), password management for vehicles and routers (164.308(a)(5)(ii)(D), raised to High after P07 found 41 routers with the factory default password), the contingency plan (164.308(a)(7)), and the disaster recovery plan (164.308(a)(7)(ii)(B)).

### 4.2 Urgent Care (`gap-analysis-urgent-care.csv`)
| Regulation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| HIPAA Security Rule (15 selected rows) | 5 | 9 | 1 | 0 |
| HIPAA Privacy Rule and Breach Notification | 1 | 2 | 0 | 0 |
| Section 1557 (45 CFR 92.210) | 1 | 2 | 0 | 0 |
| State recording and breach law (Florida worked example) | 1 | 1 | 0 | 0 |
| CMS emergency preparedness, 42 CFR Part 2, FTC HBNR | 0 | 0 | 0 | 3 |
| **Total (26)** | **8** | **14** | **1** | **3** |

The Security Rule rows focus on the specifications where Urgent Care's evidence differs from the group common controls, which Urgent Care inherits (2025 inheritance matrix). **Not met:** 164.316(b)(2)(iii), because the Urgent Care supplement has not been re-aligned since 2024 (gap 8). The two High gaps (164.308(a)(1)(ii)(B) and (D)) both come from the 46 acquired clinics, whose legacy system is not reviewed, not federated, and not in the SIEM. **Recording consent:** 14 of 200 sampled AI scribe visits had no documented consent; in all-party consent states (Florida, Fla. Stat. 934.03(2)(d), is the worked example), recording may start only after every party consents.

### 4.3 Billing and Dispatch Services (`gap-analysis-bds.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| HIPAA Security Rule (business associate, 12 rows) | 2 | 10 | 0 | 0 |
| HIPAA Breach Notification (164.410) | 1 | 1 | 0 | 0 |
| HIPAA Privacy Rule (164.502(a)(3), 164.504(e)) | 0 | 3 | 0 | 0 |
| PCI DSS v4.0.1 (9 requirement rows) | 4 | 3 | 2 | 0 |
| TCPA and the CJIS determination | 0 | 2 | 0 | 0 |
| SOC 2 and client contracts | 1 | 1 | 1 | 0 |
| **Total (31)** | **8** | **20** | **3** | **0** |

**Not met:** PCI DSS Requirement 3 (9 of 200 sampled payment recordings contained a full card number, gap 9) and Requirement 12.9 (BDS has never been assessed as a service provider for its clients), and the absence of a SOC 2 report for dispatch services (9 of 14 clients asked for one in 2026). **High gaps:** risk management, CAD vendor access, the CAD disaster recovery plan, the subcontractor assurance and permitted-use rows for the AI triage service (164.308(b)(2) and 164.502(a)(3); gap 6), and card data in recordings.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | CAD resilience: no standby outside provider A; drills assume hours (1) | Ambulance, BDS | 164.308(a)(7), (7)(ii)(B)-(D); county agreements; client contracts | High | Provider B standby; failover tests; multi-day drills | Group dispatch and clinical platforms director | 2027-06-30 |
| 2 | CAD vendor and vehicle access outside group identity (2) | Ambulance, BDS | 164.308(a)(4); 164.308(a)(5)(ii)(D); 164.312(a)(2)(i), (d) | High | Vendor access through PAM; named MDC sign-in; router credentials | Group identity director; Ambulance fleet technology director | 2027-03-31 |
| 3 | Legacy account shared by the CAD and billing servers (3) | Ambulance, BDS | 164.308(a)(1)(ii)(B); 164.312(e)(1) | High | Move both into separate landing-zone accounts | Group cloud platform director | 2027-01-31 |
| 4 | AI triage processes client callers without coverage (6) | BDS | 164.308(b)(2); 164.502(a)(3); 45 CFR 92.210 | High | Exclude client calls; amend BAA; notify clients; P10 conditions | Group General Counsel | 2026-11-30 |
| 5 | Card numbers in contact center recordings (9) | BDS | PCI DSS Requirements 3, 7, 12.9 | High | Tone-masked keypad entry; purge recordings; service provider validation | BDS contact center director | 2027-06-30 |
| 6 | Fleet devices outside group management (4) | Ambulance | 164.308(a)(1)(ii)(A), (a)(5)(ii)(B); 164.310(d) | Moderate | Fleet inventory, configuration baseline, patch tracking | Ambulance Services fleet technology director | 2027-03-31 |
| 7 | Multi-party notification not exercised (7) | All | 164.308(a)(6)(ii); 164.314(a)(2)(i)(C); 164.404-410; county and client contracts; Form 8-K Item 1.05 | Moderate | Adopt the P08 matrix; client and county register; tabletop | Group General Counsel | 2026-12-15 |
| 8 | Acquired clinics and supplement drift (8) | Urgent Care | 164.308(a)(1)(ii)(D); 164.312(b), (d); 164.316(b)(2)(iii) | High | Interim monitoring; migration; re-issue supplement | Urgent Care chief information officer | 2027-06-30 |
| 9 | Possible CJI in the CAD (5) | BDS | CJISSECPOL v6.1; 28 CFR 20.33(a)(7) | Moderate | Act on the CJIS Systems Agency determination | BDS security and compliance lead | 2026-12-31 |
| 10 | Medicare documentation and state records duties | Ambulance | 42 CFR 410.40(e), 424.516(f); Fla. Stat. 401.30(4) | Moderate | Attach and retain certification statements; central release of records | Ambulance Services contract compliance director | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-015 to POAM-019 trace directly to this analysis).

## 6. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. If it is finalized as proposed, these verified proposals would affect the group:
- The required and addressable distinction would be removed. Ambulance Services' 5 partially met addressable rows would become mandatory.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (already largely met).
- MFA would be required (vehicle accounts, the CAD vendor accounts, and the acquired clinics' legacy system fall short).
- A written technology asset inventory and network map would be required (the fleet inventory is incomplete).
- Penetration testing at least every 12 months, and vulnerability scanning.
- Restoring certain systems and data within 72 hours (the CAD rebuild outside provider A has never been tested).
- A compliance audit at least every 12 months.
- Business associates would notify covered entities within 24 hours of activating a contingency plan. That would affect BDS (to both divisions and every client) and corporate.

The `pending_rule_change` column flags affected rows. None of these is treated as a current obligation. **CIRCIA** (C-EMERGENCY-R05) is also not in effect (final rule not published as of 2026-09-25); as drafted it would require reports to CISA within 72 hours of a reasonable belief that a covered cyber incident occurred and within 24 hours of a ransom payment.

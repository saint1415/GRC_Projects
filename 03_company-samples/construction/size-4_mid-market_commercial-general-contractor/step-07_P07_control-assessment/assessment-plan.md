# Security Assessment Plan and Summary: Cris Santos Company | Construction | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial and institutional building general contractor) |
| System assessed | Project Delivery and Payment Platform (PDPP), including the CUI Project Enclave (CPE) subsystem and the places CUI actually was during fieldwork (SYS-01, FC-4 tablets, the FC-4 trailer), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Construction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, and a specialist with SP 800-171 assessment experience), reporting to the board audit committee. The firm designs and operates no control. The Security Manager arranged access but did not select samples or rate findings. The firm is not the planned C3PAO |
| Assessment window | 2026-08-03 to 2026-08-21 (office, yard, and jobsite walkthroughs 2026-08-11 to 2026-08-13) |
| Plan approved | Chief Operating Officer (system owner), 2026-07-31, before fieldwork |
| Relationship to CMMC | A readiness assessment, not a CMMC assessment. The C3PAO Level 2 certification assessment must follow NIST SP 800-171A (June 2018) and the CMMC scoping rules (32 CFR 170.17(c)(1)); it is planned for 2027-04-12 to 2027-04-23. The controls below map to the SP 800-171 Rev. 2 requirements with the largest gaps in P03 |
| Also satisfies | Annual internal IT audit; reperformance of the P03 SPRS score calculation (POL-01 4.14) |
| Results accepted | Chief Operating Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 214 determination statements.** Every determination statement for each selected control was tested. Controls were selected because they:
- address the Very High and High risks in the risk register (P01): CUI outside the enclave, ransomware, business email compromise, subcontractor CUI, monitoring;
- map to SP 800-171 Rev. 2 requirements that are Not met or Partially met in the gap analysis (P03), so the CMMC roadmap can rely on tested results;
- test the FAR 52.204-25 (Section 889) and payment integrity controls that the company's federal and private owners depend on.

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Account lifecycle; SP 800-171 3.1.1, 3.9.2; R-023, R-024, R-052 | Focused | Focused (samples of 25 and 15; all 52 CPE accounts) |
| AC-3, AC-4, AC-20, SC-8(1) | CUI outside the enclave; 3.1.2, 3.1.3, 3.1.20, 3.13.8; R-003 (Very High) | Comprehensive | Comprehensive (all FC-4 folders; all 26 FC-4 tablets) |
| AC-5 | Payment separation of duties; R-002 (High) | Focused | Focused (25 bank changes) |
| AC-6 | Least privilege; 3.1.5; R-013 | Focused | Comprehensive (all SaaS and cloud administrators) |
| AC-17, CM-2, CM-6, SC-7, SI-2 | Jobsite routers and field baselines; 3.4.1, 3.4.2, 3.13.1; FAR 52.204-21(b)(1)(x), (xii); R-011 | Focused | Comprehensive for routers (all 22 scanned externally); focused for configurations (6 routers, 10 servers) |
| AC-19, MP-2 | Tablets and media; 3.1.18, 3.1.19, 3.8.1, 3.8.2; R-012 | Focused | Comprehensive (FC-4 tablets) |
| AT-2, AT-3 | Awareness and CUI training; 3.2.1 to 3.2.3; R-044 | Basic | Focused (15 interviews) |
| AU-6, SI-4 | Monitoring of the CPE and SaaS; 3.3.5, 3.14.6, 3.14.7; R-016 (High) | Focused | Focused |
| CA-2 | Assessment and SPRS accuracy; 3.12.1; DFARS 252.204-7019(b); R-008 (High) | Comprehensive | Comprehensive (score reperformed) |
| CM-8 | Inventory and CMMC scope; 32 CFR 170.19(c) | Focused | Focused (30 and 30 traces) |
| CP-4, CP-9 | Recovery; 3.8.9; R-005 (Very High), R-017 | Focused | Focused |
| IA-2(2), IA-2(8), IA-5 | MFA and authenticators; 3.5.3, 3.5.4; R-001 (High), R-040 | Focused | Focused |
| IR-4, IR-6 | Incident capability and DoD reporting; 3.6.1, 3.6.2; DFARS 252.204-7012(c); R-009 | Focused | Focused |
| MP-6, PE-3, PE-8 | Printed CUI and the FC-4 trailer; 3.8.3, 3.10.1 to 3.10.5; FAR 52.204-21(b)(1)(vii) to (ix) | Basic | Focused (FC-4 trailer, headquarters, yard) |
| RA-5 | Vulnerability scanning; 3.11.2, 3.11.3; R-035, R-042 | Focused | Focused (40 findings) |
| SA-4 | Subcontract and vendor terms; DFARS 252.204-7012(m); R-004 (High) | Focused | Comprehensive for FC-4 (all 15 subcontracts) |
| SR-3 | Section 889 supply chain; FAR 52.204-25(b); R-010 | Focused | Focused (FC-1 to FC-4 submittals and FC-2 rentals) |

**Not selected this year, with reasons.** Strong areas tested in 2025 (SI-3 endpoint protection, SC-28 encryption at rest in the corporate tenant) and areas fully inherited from providers (data center PE controls) were not retested. They will be in the C3PAO readiness check in 2027-03 (POAM-009).

## 2. Sampling approach
The firm used its attribute sampling table: 25 items for controls that operate many times a year, 5 to 15 for weekly or monthly controls, and the full population where it was small or the risk was Very High. Populations were extracted in the assessors' presence and samples chosen at random.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 286 | 25 | AC-2, PS-4 |
| Transfers involving FC-4 | 38 | 15 | AC-2 |
| CPE accounts | 52 | 52 | AC-2, IA-2(8) |
| SYS-01 FC-4 folders and external users | 230 external users from 14 firms | All folder permissions; 1 access test | AC-3, IA-2(2) |
| Bank-detail changes in the ERP vendor master | 212 | 25 | AC-5 |
| FC-4 rugged tablets | 26 | 26 | AC-19, MP-2, SC-8(1) |
| Jobsite cellular routers | 22 | 22 (external scan); 6 (configuration pull) | AC-17, CM-2, CM-6, IA-5, SC-7, SI-2 |
| Assets for inventory trace | about 1,000 | 30 floor-to-list; 30 list-to-floor | CM-8 |
| CPE weekly log reviews (2026) | 30 | 10 | AU-6 |
| MFA resets by the help desk | 64 | 10 | IA-5 |
| Critical and high vulnerability findings (Q1-Q2 2026) | 140 | 40 | RA-5 |
| Security incident tickets (2025-2026) | 46 | 10 | IR-4 |
| Staff for reporting and awareness interviews | 600 | 15 (including 4 FC-4 field staff) | AT-2, IR-6 |
| FC-4 subcontracts / IT and SaaS contracts / rental agreements | 15 / 38 / 6 | 15 / 10 / 6 | SA-4, SR-3 |
| FC-4 trailer visitors (July 2026, installation gate record) | 41 | 41 | PE-8 |

## 3. Methods and objects
- **Examine:**
  - policies POL-01 to POL-05, STD-04, and draft standards; the SSP (v0.9 and v1.0)
  - identity provider, CPE, SYS-01, and cloud exports; the ERP vendor-master change log and bank portal approvals
  - device management, scan, patch, backup, and SIEM source reports; CPE native logs
  - subcontracts, rental agreements, vendor contracts, SOC 2 reports, and the provider CRM
  - the 2025 SP 800-171 self-assessment, the score worksheet, and the P03 gap analysis
  - visitor logs, badge reports, key records, and destruction certificates
- **Interview:**
  - vCISO, IT Director, Security Manager, both security analysts, and the GRC analyst
  - Controller, 2 accounts payable staff, and the CFO
  - Director of Contracts and Compliance, FC-4 Project Executive, and the FC-4 superintendent
  - Vice President of Operations, HR Director, Director of Technology and Security Systems
  - the MSSP service lead
  - 15 randomly selected staff, including 4 FC-4 field staff
- **Test:**
  - an access test in SYS-01 with a trade subcontractor test account
  - a clipboard and download test from an enclave virtual desktop session
  - a relayed push-approval test against a separate test tenant (not production)
  - an external scan of all 22 jobsite router addresses
  - a sweep of all 26 FC-4 tablets for offline CUI sets and device management status
  - a simulated impossible-travel sign-in on a test account to check MSSP escalation
  - a restore of one BIM folder from the backup account
  - inventory traces at 3 jobsites and the yard
  - reperformance of the P03 SPRS score calculation (32 CFR 170.24)

## 4. Rules of engagement
- **CUI handling.** Assessors viewed CUI only inside the CPE, through time-limited accounts approved by the FC-4 Project Executive. Workpapers record locations, counts, and markings, not CUI content. No CUI left company or enclave systems.
- **No disruption to jobsites or payments.** Router scans were non-intrusive and run after hours. No production bank change or payment was altered. The phishing relay test used a test tenant and a test account.
- **Stop and notify.** Any critical exposure or possible legal duty is reported the same day to the Security Manager, the vCISO, and General Counsel. **Used twice:**
  - **2026-08-12, Section 889.** The SR-3 test found 6 rented jobsite cameras at the FC-2 federal courthouse jobsite that are private-label products of a covered manufacturer under FAR 52.204-25. The cameras were used for security of a Government facility. The Director of Contracts and Compliance reported to the FC-2 Contracting Officer on **2026-08-13** (within 1 business day, FAR 52.204-25(d)(2)(i)) and filed the follow-up on **2026-08-26** (within 10 business days, (d)(2)(ii)). The cameras were removed on 2026-08-14. The company added P01 R-051.
  - **2026-08-19, departed A&E guest.** The AC-2 test found a CPE guest account of an A&E employee who had left 47 days earlier. The account was disabled the same day and its sign-in history was preserved for the review in POAM-018. The company added P01 R-052. Sign-in history showed no use after the person left.
- **Possible incident referral.** The CUI found in SYS-01 and on tablets was referred to General Counsel and the Security Manager for the review required by DFARS 252.204-7012(c)(1)(i). The assessors did not investigate it (POAM-018).

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 131 |
| Other than satisfied | 83 |
| **Total** | **214** |

Other than satisfied statements by risk: 4 Very High, 29 High, 45 Moderate, 5 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 17 | 9 | Very High | POAM-001, POAM-008 |
| AC-3 | 0 | 1 | Very High | POAM-002 |
| AC-4 | 0 | 1 | Very High | POAM-002 |
| AC-5 | 1 | 1 | High | POAM-003 |
| AC-6 | 0 | 1 | Moderate | POAM-004 |
| AC-17 | 2 | 2 | Moderate | POAM-005 |
| AC-19 | 2 | 2 | High | POAM-006 |
| AC-20 | 2 | 1 | Very High | POAM-002 |
| AT-2 | 8 | 2 | Moderate | POAM-007, POAM-021 |
| AT-3 | 5 | 4 | Moderate | POAM-007 |
| AU-6 | 1 | 2 | High | POAM-008 |
| CA-2 | 9 | 2 | High | POAM-009 |
| CM-2 | 2 | 3 | Moderate | POAM-005 |
| CM-6 | 3 | 3 | Moderate | POAM-005 |
| CM-8 | 3 | 3 | Moderate | POAM-010 |
| CP-4 | 3 | 2 | High | POAM-011 |
| CP-9 | 5 | 1 | Moderate | POAM-011 |
| IA-2(2) | 0 | 1 | High | POAM-012 |
| IA-2(8) | 0 | 1 | High | POAM-012 |
| IA-5 | 7 | 3 | High | POAM-005, POAM-012 |
| IR-4 | 8 | 5 | High | POAM-013 |
| IR-6 | 0 | 2 | High | POAM-013 |
| MP-2 | 0 | 2 | High | POAM-006, POAM-014 |
| MP-6 | 3 | 1 | High | POAM-014 |
| PE-3 | 5 | 7 | High | POAM-014 |
| PE-8 | 1 | 2 | Moderate | POAM-014 |
| PS-4 | 4 | 1 | Moderate | POAM-001 |
| RA-5 | 7 | 2 | Moderate | POAM-015 |
| SA-4 | 13 | 3 | High | POAM-016, POAM-017 |
| SC-7 | 4 | 2 | Moderate | POAM-005 |
| SC-8(1) | 0 | 1 | High | POAM-002 |
| SI-2 | 8 | 2 | Moderate | POAM-005 |
| SI-4 | 7 | 5 | High | POAM-008 |
| SR-3 | 1 | 3 | Moderate | POAM-017 |

**No control was fully satisfied.** That matches the SSP, where 33 of the 34 controls are Partially implemented. In most cases the control works in the corporate environment or inside the CPE and fails where the work actually happens: the FC-4 trailer, jobsite routers, tablets, and the commercial project platform.

**Controls fully other than satisfied (8):** AC-3, AC-4, AC-6, IA-2(2), IA-2(8), IR-6, MP-2, and SC-8(1). Each has only 1 or 2 determination statements, so a single failing location fails the whole control.

**Strengths confirmed:**
- **Inside the enclave, CUI is well protected:** separate tenant, FIPS-validated cryptography, phishing-resistant MFA for all 52 accounts, and change control (20 of 20 changes approved).
- **Corporate detection and backups work:** the MSSP escalated the simulated sign-in in 22 minutes, and the backup restore succeeded from write-once storage.
- **Payment approvals exist and mostly operate:** 23 of 25 bank changes had call-back evidence and a second approver.
- **Section 889 reporting met both clocks** once covered equipment was found.

**Themes:**
1. **CUI followed the work out of the enclave** (AC-3, AC-4, AC-20, SC-8(1), MP-2, PE-3). This drives the Very High findings and the score of -23.
2. **The field is the edge** (AC-17, AC-19, CM-2, CM-6, SC-7, SI-2). Routers and tablets have no baseline, monitoring, or firmware management.
3. **Detection and reporting stop at the corporate boundary** (AU-6, SI-4, IR-4, IR-6). Nobody watches the CPE in real time, and nobody could file a DoD report when fieldwork began.
4. **Payment integrity depends on people not skipping steps** (AC-5, IA-2(8), IA-5). Overrides and help desk resets are the gaps a business email compromise would use.

**SPRS reperformance.** The firm reperformed the P03 score calculation from the requirement-level evidence and agreed a score of **-23** for the current scope (110 minus 133 points). The SPRS score of 71 posted on 2025-02-14 is not supported. The Director of Contracts and Compliance will post the corrected score by 2026-09-30, after General Counsel's review (POAM-009).

**POA&M.** All 34 controls had at least one Other than satisfied statement. They map to 17 POA&M items (POAM-001 to POAM-017), because related controls share an item. Six more items come from the gap analysis, the risk register, the SOC 2 readiness work, and the AI assessment (POAM-018 possible CUI incident review, POAM-019 CMMC Level 2 certification, POAM-020 MBSS remote access, POAM-021 AI governance conditions, POAM-022 vendor risk program, POAM-023 owner remittance notice and email authentication). The total is 23 items: 2 Very High, 13 High, and 8 Moderate. Status: 17 In progress and 6 Open. See `poam.csv`.

**How the POA&M relates to CMMC.** This POA&M is the company's internal work plan. For CMMC, a POA&M is allowed only for Conditional Level 2 status and only for limited requirements (32 CFR 170.21(a)(2)). The plan in P03 aims for all 110 requirements Met before the C3PAO assessment, so these items must close, not carry over.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-31 | Plan approved by the COO; sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Technical tests; office, yard, and jobsite walkthroughs (FC-4 trailer on 2026-08-11 and 2026-08-12) |
| 2026-08-12 | Stop-and-notify: Section 889 finding at FC-2 |
| 2026-08-19 | Stop-and-notify: departed A&E guest account |
| 2026-08-14 to 2026-08-21 | Analysis, SPRS reperformance, draft findings, management responses |
| 2026-09-17 | Results and POA&M accepted by the COO and presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (214 rows); `poam.csv` (23 items).

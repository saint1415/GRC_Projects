# Security Assessment Plan and Summary: Cris Santos Company | Real Estate and Rental and Leasing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC (PE-backed residential real estate brokerage with property management and title and closing services) |
| System assessed | Transaction Management and Closing Communications System (TMCC, CSC-TMCC-01: SYS-01 to SYS-08), per the SSP (P02), plus the payee change workflows in SYS-09, SYS-10, and SYS-13 that move client money |
| Tier / Vertical | Mid-Market / Real Estate and Rental and Leasing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control and is not the future SOC 2 service auditor (P09). The Security Manager (Qualified Individual) coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-17 to 2026-09-04 (office walkthroughs 2026-08-24 to 2026-08-27; technical tests 2026-08-25 to 2026-08-28) |
| Also satisfies | Regular testing of key controls under the FTC Safeguards Rule, 16 CFR 314.4(d)(1) (N53-R01); the annual internal IT audit; testing results for the Qualified Individual's annual report (314.4(i)(2)) |
| Results accepted | Chief Operating Officer, 2026-09-29; co-signed by the President of Title and Closing for Title and Closing findings; presented to the audit committee and to Title and Closing's board of managers the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25 to 40 controls. **32 controls, 223 determination statements.** Controls were selected because they:
- address the High risks in the risk register (P01), above all diverted client funds (R-001 to R-003, R-008, R-021) and agent accounts;
- cover Safeguards Rule elements and Florida trust fund duties that the gap analysis (P03) rated Partially met or Not met;
- support the SSP conditions (P02 section 4.2) and SOC 2 readiness for Title and Closing (P09).

Payee verification controls (AC-5, SI-7, AT-3) were tested in all three account families (title trust, sales escrow, property management) and in the agent payout process, because the 2025-11 loss came from outside Title and Closing.

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2 | Agent offboarding and access reviews; 314.4(c)(1)(i); R-006, G-012 | Focused | Focused (samples of 25) |
| AC-3 | Office-wide visibility in SYS-01; R-007, G-013 | Focused | Focused |
| AC-5 | Payee verification; Fla. Stat. 626.8473(4); R-002, R-003, G-060 | Comprehensive | Comprehensive (samples of 25 to 40 per account type) |
| AC-6 | Privileged and export rights; R-005, R-031 (High) | Comprehensive | Comprehensive (all 38 privileged accounts) |
| AT-2 | Agent training; 314.4(e)(1); R-001, G-027 | Focused | Focused |
| AT-3 | Payment fraud training; R-002, R-003 | Focused | Focused |
| AU-2 | SaaS logging; 314.4(c)(8); G-023 | Focused | Focused |
| AU-6 | Activity review; 314.4(c)(8); R-001, R-005 | Focused | Comprehensive (all mailboxes) |
| AU-11 | Log retention for investigations; 314.2(m) | Basic | Focused |
| CM-3 | Portal change control; 314.4(c)(7); R-008, G-022 | Comprehensive | Comprehensive (all 12 portal releases) |
| CM-6 | SaaS and server baselines; R-032 | Focused | Focused |
| CM-8 | Inventory; 314.4(c)(2); G-014 | Basic | Focused |
| CP-2 | Contingency planning; R-004, R-010, R-011 (BIA findings 1 to 3) | Comprehensive | Comprehensive |
| CP-4 | Recovery testing; R-014 | Focused | Focused |
| CP-9 | Backups; R-013 | Focused | Comprehensive (31 job days) |
| CP-10 | Recovery within BIA RTOs; R-010 | Focused | Focused |
| IA-2(1) | Privileged MFA; R-020, R-031 | Focused | Focused (25 of 38) |
| IA-2(2) | MFA for every user; 314.4(c)(5); R-001, G-019 | Focused | Comprehensive (all identities) |
| IA-5 | Authenticators and secrets; R-030 | Focused | Focused |
| IA-8 | Portal user authentication; R-009 | Basic | Focused |
| IR-4 | Incident handling and funds recovery; 314.4(h)(2); G-037 | Focused | Focused (10 of 14 incidents) |
| IR-6 | Reporting duty; 314.4(j)(2); R-019, G-048 | Focused | Focused |
| IR-8 | Written incident response plan; 314.4(h); G-035 | Focused | Basic |
| MP-6 | Disposal; Fla. Stat. 501.171(8); G-063 | Basic | Focused |
| PS-4 | Employee terminations; 314.4(c)(1)(i) | Focused | Focused (samples of 25) |
| RA-3 | Written risk assessment; 314.4(b) | Basic | Basic |
| RA-5 | Vulnerability management; 314.4(d)(2)(ii); R-029 | Focused | Focused |
| SA-9 | Service provider oversight; 314.4(f); R-015, R-016 | Focused | Focused (20 of 42) |
| SA-11 | Portal developer testing; 314.4(c)(4); R-008, G-017 | Focused | Focused |
| SC-28 | Encryption at rest; 314.4(c)(3); G-016 | Focused | Focused (30 laptops) |
| SI-4 | Monitoring and MSSP escalation; R-037, R-052 | Focused | Focused |
| SI-7 | Payment data integrity; High integrity rating; R-002, R-003, R-008 | Comprehensive | Comprehensive |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control operating many times a year with moderate risk, 40 items for high-risk funds controls, and 5 to 10 items for weekly or monthly controls. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Contractor agent departures (2025-07-01 to 2026-06-30) | 410 | 25 | AC-2 |
| Contractor agent onboardings | 380 | 25 | AC-2, AT-2 |
| Employee terminations | 96 | 25 (6 with bank platform access) | AC-2, PS-4 |
| Employee transfers | 40 | 25 | AC-2 |
| Privileged accounts (identity provider, productivity suite, SYS-01, SYS-02, cloud) | 38 | 25 for sign-in tests; all 38 for rights review | IA-2(1), AC-6 |
| Agent identities without MFA | about 310 | 10 sign-in observations | IA-2(2) |
| Title trust account wires | about 35,000 | 40 | AC-5 |
| Edits to existing SYS-02 payee bank details | 312 | 25 | AC-5, SI-7 |
| Sales escrow refund wires | 290 | 25 | AC-5 |
| Owner payout account changes (SYS-10) | 186 | 25 | AC-5, SI-7 |
| Agent payout account changes (SYS-13) | 142 | 25 | AC-5, SI-7 |
| Mailboxes (forwarding rule scan) | 2,250 | all | AU-6 |
| Portal releases (2026-01 to 2026-08) | 12 | 12 | CM-3, SA-11 |
| Infrastructure changes | 214 | 20 | CM-3 |
| Critical vulnerability findings (Q1-Q2 2026) | 40 | 40 | RA-5 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| Service providers with customer or consumer information | 42 | 20 | SA-9 |
| Incidents (2025-07 to 2026-06) | 14 | 10 | IR-4, IR-6 |
| Company laptops | 660 | 30 | SC-28 |
| Agent password resets by the service desk | 1,180 | 10 | IA-5 |
| Portal phone number changes | 96 | 10 | IA-8 |
| Staff and agents for interviews | 600 employees; 1,650 agents | 15 employees; 10 agents | AT-2, IR-6 |

## 3. Methods and objects
- **Examine:**
  - the 2024 policies and the 2026 drafts of POL-01 to POL-05 and the standards
  - the SSP draft, BIA draft, and risk register
  - identity provider, SYS-01, SYS-02, SYS-10, SYS-13, cloud, and bank platform exports
  - backup, scan, patch, and EDR reports
  - contracts, SOC 2 reports, and the intercompany services agreement
  - the incident log, the Title and Closing payee change attempt spreadsheet, and the 2025-11 loss file
  - change tickets, portal release emails, and the pipeline configuration
- **Interview:**
  - Security Manager (Qualified Individual), vCISO, IT Director, the 2 security analysts, and the GRC analyst
  - President of Title and Closing, Title Escrow Accounting Manager, Controller, and Broker of Record
  - Director of Agent Services, Director of Transaction Services, and Director of Property Management
  - General Counsel and HR Director
  - the MSSP service lead and the contract development firm's lead developer
  - 15 randomly selected employees and 10 randomly selected contractor agents
- **Test:**
  - sign-in tests on 25 privileged accounts and observation of 10 agent sign-ins
  - a scan of forwarding rules in all mailboxes
  - a visibility test with a sampled agent account in SYS-01
  - an attempt to edit an existing payee's bank details as a single user in the SYS-02 test environment
  - a simulated impossible-travel sign-in to test MSSP escalation, and EICAR test files on 5 endpoints
  - a restore of one portal database table from the backup account
  - benchmark configuration scans of 10 servers and default credential checks on 10 network devices

## 4. Rules of engagement
- No testing that could move or delay client funds. Payee edit tests ran only in the SYS-02 test environment, and no live payee data was changed.
- No customer information left company systems. Screenshots were redacted, and workpapers were stored in the firm's encrypted workpaper system under its engagement letter, which includes security and confidentiality terms (16 CFR 314.4(f)(2)).
- Agent sign-in observations were done with each agent's consent, and passwords were never shown to the assessors.
- Stop-and-notify rule: any exposure that could lead to diverted funds or acquired customer information is reported to the Security Manager and the IT Director the same day. **Used once:** on 2026-08-27 the mailbox scan found 6 agent mailboxes with rules forwarding mail to outside accounts, one created from an overseas IP address. The rules were removed on 2026-08-28, the attacker-created rule was opened as an incident under the P08 BEC runbook the same day, and the company logged it as P01 R-052 on 2026-09-04. The assessors did not investigate the incident.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 120 |
| Other than satisfied | 103 |
| **Total** | **223** |

Other than satisfied statements by risk: 23 High, 60 Moderate, 20 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 20 | 6 | High | POAM-003 |
| AC-3 | 0 | 1 | Moderate | POAM-004 |
| AC-5 | 0 | 2 | High | POAM-002 |
| AC-6 | 0 | 1 | High | POAM-004 |
| AT-2 | 4 | 6 | Moderate | POAM-006 |
| AT-3 | 6 | 3 | Moderate | POAM-002 |
| AU-2 | 3 | 3 | High | POAM-005 |
| AU-6 | 1 | 2 | High | POAM-005 |
| AU-11 | 0 | 1 | Moderate | POAM-005 |
| CM-3 | 4 | 6 | High | POAM-010 |
| CM-6 | 1 | 5 | Moderate | POAM-007 |
| CM-8 | 3 | 3 | Moderate | POAM-007 |
| CP-2 | 8 | 16 | High | POAM-008 |
| CP-4 | 2 | 3 | High | POAM-008 |
| CP-9 | 5 | 1 | High | POAM-008 |
| CP-10 | 0 | 2 | High | POAM-008 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-2(2) | 0 | 1 | High | POAM-001 |
| IA-5 | 6 | 4 | Moderate | POAM-012 |
| IA-8 | 0 | 1 | Low | POAM-011 |
| IR-4 | 6 | 7 | Moderate | POAM-009 |
| IR-6 | 1 | 1 | Moderate | POAM-020 |
| IR-8 | 9 | 8 | High | POAM-009 |
| MP-6 | 3 | 1 | Low | POAM-013 |
| PS-4 | 4 | 1 | Moderate | POAM-003 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 7 | 2 | Moderate | POAM-014 |
| SA-9 | 2 | 4 | Moderate | POAM-015 |
| SA-11 | 3 | 6 | High | POAM-010 |
| SC-28 | 0 | 1 | Moderate | POAM-022 |
| SI-4 | 9 | 3 | High | POAM-005 |
| SI-7 | 4 | 2 | High | POAM-002 |

**Fully satisfied (2 controls):** IA-2(1) and RA-3. IA-2(1) confirms the security key rollout for administrators; RA-3 confirms the written risk assessment the Safeguards Rule requires (314.4(b)).

**Fully other than satisfied (8 controls):** AC-3, AC-5, AC-6, AU-11, CP-10, IA-2(2), IA-8, and SC-28.

**Themes:**
1. **Title and Closing's own wires are well defended; the edges are not.** All 40 sampled title trust wires had dual approval and a callback record. Edits to existing payees, sales escrow refunds, owner payouts, and agent payouts had no independent check (AC-5, SI-7, AT-3).
2. **Contractor agents are the weakest identity population.** About 310 have no MFA, departures are disabled late, they get no annual training, and old forwarding rules sat in their mailboxes (IA-2(2), AC-2, AT-2, AU-6).
3. **SaaS is not watched and the portal's code is not governed.** Payee changes and exports inside SaaS are invisible to the MSSP, and the application that delivers wire instructions is released by email approval with shared credentials (AU-2, SI-4, CM-3, SA-11).
4. **Recovery is designed for the cloud and unproven for SaaS** (CP-2, CP-4, CP-10).

**POA&M:** 30 controls had at least one Other than satisfied statement. They map to 17 POA&M items, because related controls share an item. 5 more items come from the gap analysis, the SSP, the SOC 2 readiness assessment, and the AI assessment (POAM-016, POAM-017, POAM-018, POAM-019, POAM-021). The total is 22 items: 8 High, 12 Moderate, and 2 Low; 13 In progress and 9 Open. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-08-10 | Plan and sample requests issued |
| 2026-08-17 to 2026-08-21 | Document examination and interviews |
| 2026-08-24 to 2026-08-28 | Office walkthroughs (headquarters and 4 sales offices) and technical tests |
| 2026-08-31 to 2026-09-04 | Analysis, draft findings, management responses |
| 2026-09-29 | Results and POA&M accepted by the COO and presented to the audit committee and Title and Closing's board of managers |

Deliverables: this plan and summary; `assessment-results.csv` (223 rows); `poam.csv` (22 items).

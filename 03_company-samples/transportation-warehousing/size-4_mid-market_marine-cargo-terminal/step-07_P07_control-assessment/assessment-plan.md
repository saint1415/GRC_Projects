# Security Assessment Plan and Summary: Cris Santos Company | Transportation and Warehousing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed marine cargo terminal operator: Terminal 1, Terminal 2 and an off-dock depot) |
| System assessed | Terminal Operations and Gate Platform (TOGP, CSC-TOGP-01), per the SSP (P02), including its interfaces to crane and yard equipment OT (SYS-03) and security systems (SYS-09) |
| Tier / Vertical | Mid-Market / Transportation and Warehousing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors and 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control and has no regularly assigned cybersecurity duties. The GRC analyst coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (OT tests at T2 on the night of 2026-08-12 and at T1 on the night of 2026-08-13, with no vessel at berth) |
| Also satisfies | Annual internal IT audit; evidence for the Cybersecurity Assessment (33 CFR 101.650(e)(1)) and for the CySO duty to verify that measures operate as intended (101.625(d)(2)) |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |
| Handling | Contains security vulnerabilities of MTSA-regulated facilities. Handle as SSI (49 CFR 1520.5(b)(5); POL-04 4.2) |

## 1. Scope and controls selected
Mid-Market tier scope: 25 to 40 controls. **34 controls, 246 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the Subpart F measures with High gaps in the gap analysis (P03);
- confirm the strengths the company relies on (EDR, write-once backups) and support SOC 2 readiness for the carrier alliance (P09).

| Control | Why selected (risk ID or requirement) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Account lifecycle; 101.650(a)(7); R-013 | Focused | Focused (samples of 25) |
| AC-6, IA-2, IA-2(1) | Privileged and shared accounts, MFA; 101.650(a)(4)-(6); R-009 (High), R-014 | Comprehensive | Comprehensive (all 38 privileged accounts; 25 for MFA tests) |
| AC-17, MA-4 | Vendor remote access to OT; 101.650(e)(3)(v), (f)(3); R-003 (High), R-018, R-037 (High) | Comprehensive | Comprehensive (all vendor connection paths) |
| AT-2, AT-3 | Training deadline missed; 101.650(d); R-007 | Basic | Focused |
| AU-6, AU-9 | Log protection and review; 101.650(c)(1), (h)(2); R-021, R-026 | Focused | Focused |
| CM-6, CM-7, IA-5 | Configuration, allowlisting and default passwords; 101.650(a)(2)-(3), (b)(1)-(2); R-008, R-040 | Focused | Focused (40 devices; 8 servers) |
| CM-8 | Inventory; 101.650(b)(3); R-025 | Focused | Focused (30 devices at each terminal) |
| CP-2, CP-4, CP-9, CP-10 | Recovery; 101.650(g)(4); R-001 (Very High), R-004 and R-017 (High) | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability and reporting; 101.620(b)(6)-(7); 6.16-1; R-005, R-042 | Focused | Focused |
| MP-7, PE-3 | Ports and physical access to OT; 101.650(i); R-022, R-023 | Basic | Focused (both terminals) |
| RA-5, SI-2, SA-22 | Vulnerability management and unsupported components; 101.625(d)(15), 101.650(e)(3)(i); R-010, R-011 | Focused | Focused (21 of 21 KEVs) |
| SA-9, SR-8 | Vendor oversight and notification; 101.650(f)(1)-(2); R-041 | Focused | Comprehensive (27 of 27 contracts) |
| SA-11 | Portal secure development (SOC 2 scope); R-027, R-043 | Focused | Focused (10 releases) |
| SC-7, SC-8, SI-4 | Segmentation, encryption and monitoring; 101.650(c)(2), (h)(1)-(2); R-002 (High), R-033, R-050 | Focused | Focused (both terminals) |
| SI-3 | Confirm the EDR strength relied on in P08; R-001 | Basic | Focused (5 endpoints) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items; small populations are tested in full. The assessors chose samples at random from populations extracted in their presence. The same populations were used for the gap analysis (P03).

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 74 | 25 | AC-2, PS-4 |
| Transfers | 41 | 25 | AC-2 |
| New accounts (new hires) | 96 | 25 | AC-2, AT-2 |
| Privileged accounts (directory, identity provider, cloud, TOS, OT engineering, gate server local) | 38 | All 38 for rights; 25 for MFA sign-in tests | AC-6, IA-2(1) |
| Network-connected OT and gate devices | about 310 | 40 (default-credential test); 30 at each terminal (inventory comparison) | IA-5, CM-6, CM-8 |
| TOS and gate servers | 22 | 8 (benchmark scans) | CM-6, CM-7 |
| Endpoints | 520 workstations and laptops, 140 tablets | 5 (EDR test) | SI-3 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Vendors with access | 27 | 27 contracts | SA-9, SR-8 |
| T1 OEM remote sessions (2026-Q2) | 48 | 10 | MA-4 |
| Security tickets (2025-07 to 2026-06) | 31 | 10 (6 at T1, 4 at T2) | IR-4 |
| KEVs (2026 H1) | 21 | 21 | RA-5, SI-2 |
| Portal releases (2026 H1) | 34 | 10 | SA-11 |
| Supervisors for reporting-awareness interviews | about 90 | 12 (6 at each terminal) | IR-6, AT-2 |
| Sites for walkthroughs | 3 | T1 and T2 (depot by document review) | PE-3, MP-7, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:**
  - the 2024 policies and the 2026 drafts;
  - the SSP draft;
  - identity provider, directory, TOS, cloud and OT account exports;
  - backup, patch, scan, KEV and EDR reports;
  - vendor contracts and SOC 2 reports;
  - the incident ticket log and the 2025 exercise reports;
  - the 2024 IR and DR plans and the 2026-04-22 restore test report;
  - FSP reporting sections (read in the FSOs' offices; not copied).
- **Interview:**
  - Chief Operating Officer, vCISO, CySO, alternate CySO and both security analysts;
  - both FSOs;
  - T1 and T2 General Managers;
  - Director of Maintenance and Engineering and the OT network engineer;
  - TOS Application Manager, HR Director and Procurement Manager;
  - the MSSP service lead;
  - 12 supervisors and 2 hiring hall dispatchers.
- **Test:**
  - MFA sign-in tests on 25 privileged accounts;
  - default-credential tests on 40 OT and gate devices (with the crane OEM's approval, maintenance staff present, equipment idle);
  - a reachability test from the T2 gate network to a mobile harbor crane controller;
  - a local log deletion test on one T2 gate server;
  - USB tests on 6 T2 devices;
  - EICAR-style test files on 5 endpoints;
  - a simulated impossible-travel sign-in to test MSSP escalation;
  - a restore of one portal database table from the backup account;
  - benchmark configuration scans of 8 servers.

## 4. Rules of engagement
- **No testing that could move equipment or disrupt a vessel.** OT tests ran at night with no vessel at berth, cranes parked and locked out, and the Director of Maintenance and Engineering or a senior crane electrician present. Tests were read-only: no writes to PLCs, no active scanning of controllers (passive capture and credential checks on management interfaces only).
- **No SSI left company premises.** FSP content was read in the FSOs' offices. Workpapers that describe vulnerabilities are marked SSI and stored in the firm's encrypted workpaper system under an SSI nondisclosure agreement.
- **Stop-and-notify rule:** any critical exposure is reported to the CySO and the vCISO the same day. **Used once:** on the night of 2026-08-12 the assessors found the T2 OEM cellular appliance online with an active OEM session that had no approval record. The CySO confirmed with the OEM that it was a scheduled diagnostic. The same night the shared password was changed and the OEM agreed to call the T2 shift superintendent before each session. The full fix (off by default, sessions through the privileged remote access service) is POAM-003.
- **Default passwords found** on 4 T1 reefer monitoring gateways and 2 T2 OCR camera controllers were reported the same night, and those 6 devices were changed by 2026-08-21. Because only 40 of about 310 devices were tested, a sweep of all OT and gate devices for remaining defaults is due 2026-10-31, and the commissioning process gap remains open (POAM-007, POAM-013).

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 145 |
| Other than satisfied | 101 |
| **Total** | **246** |

Other than satisfied statements by risk: 52 High, 49 Moderate.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 20 | 6 | Moderate | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 1 | 3 | High | POAM-003 |
| AT-2 | 8 | 2 | Moderate | POAM-004 |
| AT-3 | 7 | 2 | Moderate | POAM-004 |
| AU-6 | 2 | 1 | Moderate | POAM-006 |
| AU-9 | 0 | 2 | Moderate | POAM-005 |
| CM-6 | 2 | 4 | Moderate | POAM-007 |
| CM-7 | 4 | 2 | Moderate | POAM-007 |
| CM-8 | 2 | 4 | High | POAM-008 |
| CP-2 | 11 | 13 | High | POAM-009 |
| CP-4 | 1 | 4 | High | POAM-010 |
| CP-9 | 5 | 1 | High | POAM-011 |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2 | 1 | 1 | Moderate | POAM-012 |
| IA-2(1) | 0 | 1 | High | POAM-012 |
| IA-5 | 7 | 3 | Moderate | POAM-013 |
| IR-4 | 8 | 5 | Moderate | POAM-014 |
| IR-6 | 1 | 1 | Moderate | POAM-015 |
| IR-8 | 11 | 6 | High | POAM-014 |
| MA-4 | 2 | 6 | High | POAM-003 |
| MP-7 | 1 | 1 | Moderate | POAM-016 |
| PE-3 | 8 | 4 | Moderate | POAM-017 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| RA-5 | 6 | 3 | High | POAM-018 |
| SA-9 | 3 | 3 | Moderate | POAM-019 |
| SA-11 | 5 | 4 | Moderate | POAM-020 |
| SA-22 | 1 | 1 | Moderate | POAM-021 |
| SC-7 | 3 | 3 | High | POAM-022 |
| SC-8 | 0 | 1 | Moderate | POAM-023 |
| SI-2 | 7 | 3 | Moderate | POAM-018 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 7 | 5 | High | POAM-024 |
| SR-8 | 0 | 1 | Moderate | POAM-019 |

**Fully satisfied (1 control):** SI-3. EDR detected and quarantined every test file within 4 minutes and alerted the MSSP. Strong partial results also confirm the other strengths in the scenario facts: write-once, encrypted backups with separate credentials (CP-9, 5 of 6 statements; 30 of 30 job days successful), MFA on every sampled identity provider and cloud administrator account, recorded and approved T1 OEM sessions (MA-4), and 24x7 MSSP escalation within 14 minutes for IT events (AU-6).

**Fully other than satisfied (6 controls):** AC-6, AU-9, CP-10, IA-2(1), SC-8 and SR-8.

**Themes:**
1. **The T1 and cloud standard has not reached T2.** Segmentation, monitoring, backups, physical access, port control and inventory all work at T1 and fail at T2 (SC-7, SI-4, CP-9, PE-3, MP-7, CM-8).
2. **Third-party access to OT is the largest exposure** (AC-17, MA-4, SA-9, SR-8). Only the T1 crane OEM uses the controlled path.
3. **Recovery is not proven** (CP-2, CP-4, CP-10): a 2024 plan, a missed RTO and an untested failover.
4. **Privileged and shared OT accounts** (AC-6, IA-2, IA-2(1), IA-5) undermine otherwise strong identity controls.

**POA&M:** 33 controls had at least one Other than satisfied statement. They map to 24 POA&M items (POAM-001 to POAM-024), because related controls share an item. Six more items come from the gap analysis and the AI assessment (POAM-025 Cybersecurity Assessment and Plan, POAM-026 SSI handling, POAM-027 AI governance conditions, POAM-028 customs hold override and release checks, POAM-029 drills and exercises, POAM-030 Florida personal information). The total is 30 items: 11 High, 18 Moderate and 1 Low; 20 In progress and 10 Open. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | Walkthroughs and technical tests (OT tests at night on 2026-08-12 at T2 and 2026-08-13 at T1) |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (246 rows); `poam.csv` (30 items).

# Security Assessment Plan and Summary: Cris Santos Company | Emergency Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (licensed private ambulance service; PE-backed) |
| System assessed | Dispatch and Patient Care Platform (DPCP), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Emergency Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control. The Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (site and vehicle walkthroughs 2026-08-10 to 2026-08-13; station network tests 2026-08-12) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8); annual internal IT audit |
| Results accepted | Chief Operating Officer, 2026-09-16; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls, 255 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover HIPAA Security Rule standards and Required specifications with gaps in the gap analysis (P03);
- test the controls that the County A continuity plan, the vendor SOC 2 reliance (P09), and the billing services SOC 2 readiness depend on.

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle; 164.308(a)(3)(ii)(C), (a)(4)(ii)(C); R-006 | Focused | Focused (samples of 25 and 20) |
| AC-6, IA-2(1) | Privileged access; R-022 (High) | Comprehensive | Comprehensive (all 31 privileged accounts reviewed; 25 tested for MFA) |
| AC-17, MA-4 | Vendor remote access; R-021 (High) | Focused | Focused |
| AC-19, IA-2 | MDC sign-in; 164.312(a)(2)(i), 164.312(d); R-005 | Focused | Focused (2 ambulances) |
| IA-5 | Device and shared credentials; R-050 | Focused | Comprehensive for station alerting (13 of 13 controllers) |
| AT-2 | Training; 164.308(a)(5) | Basic | Focused |
| AU-2, AU-6, AU-11 | Activity review and log retention; 164.308(a)(1)(ii)(D), 164.312(b); R-038, R-041 | Focused | Focused |
| CA-3 | County CAD-to-CAD exchanges; R-010, R-011 | Focused | Comprehensive (both exchanges) |
| CM-6, CM-7, CM-8 | Configuration and inventory; gaps 5 and 11; R-007, R-040 | Focused | Focused |
| CP-2, CP-2(5), CP-4, CP-7, CP-9, CP-10 | Contingency and recovery; 164.308(a)(7); R-001 (Very High), R-003, R-008 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability; 164.308(a)(6); R-042 | Focused | Basic |
| PE-3 | Physical access; 164.310(a) | Basic | Focused (5 of 14 sites) |
| RA-3, RA-5, SI-2 | Risk analysis and vulnerability management; R-004, R-035 | Focused | Focused |
| SA-9, SR-6 | Vendor oversight; 164.308(b); R-013, R-043 | Focused | Focused (samples of 15 and 20) |
| SC-7 | Station segmentation; R-023, R-050 | Focused | Focused (Station 3 test) |
| SC-28, SI-3, SI-4 | Encryption, EDR, monitoring; R-001, R-002, R-036 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Departures (2025-07-01 to 2026-06-30) | 128 | 25 | AC-2, PS-4 |
| Transfers between field and communications roles | 41 | 20 | AC-2 |
| New ePCR accounts | 186 | 25 | AC-2 |
| Privileged accounts (cloud, identity provider, CAD) | 31 | 25 for MFA test; all 31 for rights review | IA-2(1), AC-6 |
| Station alerting controllers | 13 | 13 (default-credential test) | IA-5 |
| Vehicle routers | 106 | 10 (configuration and credential test) | CM-7, IA-5 |
| Mobile devices | 642 | 30 (encryption) | SC-28 |
| Endpoints and servers for EDR test | 358 | 6 (3 office, 2 consoles, 1 cloud server) | SI-3 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| BAAs on file / vendors in accounts payable | 52 / about 700 | 15 / 20 | SA-9 |
| Incidents (2025-2026) | 29 | 10 | IR-4 |
| Critical vulnerability findings (Q1-Q2 2026) | 50 | 50 | RA-5, SI-2 |
| Servers for configuration scan (cloud and on-premises) | 18 | 10 | CM-6 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Sites for walkthroughs | 14 | 5 (headquarters with the primary center, Station 10 with the backup center, Stations 3, 7, and 12) | PE-3, SC-7, CM-8 |
| Ambulances inspected | 92 | 2 | AC-19, IA-2, CM-8 |

## 3. Methods and objects
- **Examine:**
  - policies (the 2023 set and drafts of the 2026 set) and the SSP draft
  - identity provider, CAD, ePCR, scheduling, and cloud exports
  - backup, patch, scan, and EDR reports
  - BAAs, AI feature order forms, and vendor files
  - the 2023 continuity and incident plans, the 2025 relocation drill report, and the county agreements
  - destruction certificates and badge reports
- **Interview:**
  - vCISO, Director of IT, Security Manager, and both analysts
  - Compliance and Privacy Officer
  - Director of Communications, 2 communications supervisors, and the Director of Field Operations
  - HR Director, Director of Revenue Cycle, and Director of Government Contracts
  - the MSSP service lead
  - 15 randomly selected staff
- **Test:**
  - MFA sign-in tests on sampled privileged accounts
  - default-credential tests on all 13 station alerting controllers and 10 routers (after hours, with the Director of Field Operations present)
  - a reachability test from crew Wi-Fi at Station 3
  - MDC sign-in tests on 2 ambulances
  - EICAR test files on 6 endpoints, including 2 consoles at the backup center
  - a simulated impossible-travel sign-in to test MSSP escalation
  - a restore of one CAD database snapshot into the isolated recovery network
  - benchmark configuration scans of 10 servers
  - an ePCR audit query on 10 randomly chosen patients

## 4. Rules of engagement
- No testing that could disrupt dispatch. Console tests ran at the backup center while it was not in use. Station alerting tests ran after hours with no units in quarters and with the communications supervisor informed. No test touched the county CAD-to-CAD links or the county radio systems.
- No PHI left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system under its BAA.
- Stop-and-notify rule: any critical exposure is reported to the Director of IT and the vCISO the same day. **Used once:** on 2026-08-12 the assessors reported that station alerting controllers were reachable from crew Wi-Fi at Station 3 and that 4 of the 13 controllers still had the manufacturer default password. The Director of Field Operations changed the 4 passwords on 2026-08-14, and the company logged the finding as P01 R-050 the same day.
- The 2 ePCR accesses with no apparent job reason (AU-6 test) were referred to the Compliance and Privacy Officer under the breach procedure, not investigated by the assessors.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 157 |
| Other than satisfied | 98 |
| **Total** | **255** |

Other than satisfied statements by risk: 40 High, 54 Moderate, 4 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 17 | 9 | Moderate | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 3 | 1 | Moderate | POAM-003 |
| AC-19 | 3 | 1 | Moderate | POAM-004 |
| AT-2 | 8 | 2 | Low | POAM-005 |
| AU-2 | 2 | 4 | Moderate | POAM-006 |
| AU-6 | 1 | 2 | High | POAM-007 |
| AU-11 | 0 | 1 | Moderate | POAM-006 |
| CA-3 | 1 | 7 | Moderate | POAM-008 |
| CM-6 | 2 | 4 | Moderate | POAM-009 |
| CM-7 | 4 | 2 | Moderate | POAM-009 |
| CM-8 | 2 | 4 | Moderate | POAM-010 |
| CP-2 | 13 | 11 | High | POAM-011 |
| CP-2(5) | 0 | 2 | High | POAM-011 |
| CP-4 | 2 | 3 | High | POAM-012 |
| CP-7 | 3 | 1 | Moderate | POAM-011 |
| CP-9 | 4 | 2 | High | POAM-012 |
| CP-10 | 0 | 2 | High | POAM-012 |
| IA-2 | 1 | 1 | Moderate | POAM-004 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 6 | 4 | High | POAM-013 |
| IR-4 | 10 | 3 | Moderate | POAM-014 |
| IR-6 | 2 | 0 | n/a | n/a |
| IR-8 | 12 | 5 | Moderate | POAM-014 |
| MA-4 | 2 | 6 | Moderate | POAM-003 |
| PE-3 | 10 | 2 | Low | POAM-015 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | High | POAM-016 |
| SA-9 | 2 | 4 | High | POAM-017 |
| SC-7 | 4 | 2 | High | POAM-018 |
| SC-28 | 1 | 0 | n/a | n/a |
| SI-2 | 7 | 3 | High | POAM-016 |
| SI-3 | 7 | 1 | Moderate | POAM-019 |
| SI-4 | 10 | 2 | Moderate | POAM-019 |
| SR-6 | 0 | 1 | High | POAM-017 |

**Fully satisfied (4 controls):** IA-2(1) (MFA on all 25 sampled privileged accounts), IR-6 (14 of 15 interviewed staff knew the reporting path), RA-3 (the 2026 risk assessment), and SC-28 (encryption at rest, 30 of 30 sampled devices). CP-9 came close: CAD database backups are complete and write-once, and the test restore succeeded in 38 minutes.

**Fully other than satisfied (5 controls):** AC-6, AU-11, CP-2(5), CP-10, and SR-6.

**Themes:**
1. The company can **detect** attacks and has protected its **CAD database**, but it has **not proven it can rebuild CAD** or run without it for days at both centers (CP-2, CP-2(5), CP-4, CP-7, CP-10).
2. **Vehicles, stations, and vendors** are where access is weakest: shared MDC accounts, default and written device passwords, flat station networks, and unmanaged vendor sessions (IA-2, IA-5, SC-7, MA-4).
3. **Visibility gaps** (AU-2, AU-6, AU-11, SI-4) mean an investigation could not show what an attacker took from CAD.
4. **Agreements lag reality**: neither county link has interconnection terms, and 6 PHI vendors have no BAA (CA-3, SA-9).

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 19 POA&M items (POAM-001 to POAM-019), because related controls share an item. Five more items come from the gap analysis, the SOC 2 readiness assessment, and the AI assessment (POAM-020 billing services SOC 2 and workspace review, POAM-021 breach decision log and client notices, POAM-022 AI governance, POAM-023 PCS retention, POAM-024 security standards). The total is 24 items: 10 High, 12 Moderate, and 2 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Site, station, and vehicle walkthroughs and technical tests |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-16 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (255 rows); `poam.csv` (24 items).

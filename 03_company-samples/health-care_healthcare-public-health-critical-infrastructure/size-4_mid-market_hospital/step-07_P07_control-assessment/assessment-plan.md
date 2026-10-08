# Security Assessment Plan and Summary: Cris Santos Company | Healthcare and Public Health | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed 112-bed community acute-care hospital) |
| System assessed | Hospital EHR and Clinical Systems (HECS: SYS-01 to SYS-08 and SYS-10), per the SSP (P02); building OT and communications tested only where they share HECS networks |
| Tier / Vertical | Mid-Market / Healthcare and Public Health |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, and a medical device security specialist), reporting to the board audit committee. The firm does not design or operate any assessed control. The Information Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-07-27 to 2026-08-14 (walkthroughs 2026-08-03 to 2026-08-06; device and network testing after hours on 2026-08-05) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8); annual internal IT audit |
| Results accepted | Chief Operating Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 243 determination statements** (every determination statement of each selected control). Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover HIPAA Security Rule standards and Required specifications with gaps in the gap analysis (P03), and the 482.15 contingency elements;
- support inherited-control reliance and SOC 2 readiness for the affiliated practice program (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle for employees and non-employees; 164.308(a)(3)(ii)(C), (a)(4)(ii)(C); R-013 | Focused | Focused (samples of 25) |
| AC-6, IA-5 | Privileged access and vendor credentials; R-009, R-054 | Comprehensive | Comprehensive (all privileged accounts; 20 devices and 6 servers for default credentials) |
| AC-17, MA-4 | Vendor remote access; R-010 | Focused | Comprehensive (all 46 vendors; 10 sessions) |
| IA-2, IA-2(1) | Unique IDs and MFA; 164.312(a)(2)(i), 164.312(d) | Focused | Focused (25 privileged accounts) |
| AT-2 | Training; 164.308(a)(5) | Basic | Focused |
| AU-2, AU-6 | Activity review gap; 164.308(a)(1)(ii)(D), 164.312(b); R-014, R-037 | Focused | Focused |
| CM-6, CM-8 | Configuration and device inventory; EV-013 and EV-027 (P03 164.310(d), 164.316(a)); R-007, R-040 | Focused | Focused |
| CP-2, CP-4, CP-8, CP-9, CP-10 | Contingency, communications, and recovery; 164.308(a)(7); 482.15(b)(5), (c)(3); R-001 (Very High), R-003, R-006, R-017 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability; 164.308(a)(6) | Focused | Basic |
| MP-6, PE-3 | Physical and media; 164.310 | Basic | Focused |
| RA-3, RA-5, SI-2 | Risk analysis and vulnerability management; R-033, R-034 | Focused | Focused |
| SA-9, SR-6 | Vendor oversight; 164.308(b); R-021, R-022 | Focused | Focused (samples of 20) |
| SA-22, SC-7 | Unsupported devices and segmentation; R-007, R-008, R-016 | Focused | Focused |
| SC-28, SI-3, SI-4, SI-7 | Encryption, EDR, monitoring, drug library integrity; R-002, R-015, R-037 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Employee terminations (2025-07-01 to 2026-06-30) | 142 | 25 | AC-2, PS-4 |
| Non-employee departures (contracted, agency, practice users) | about 210 | 25 | AC-2 |
| Transfers | 88 | 25 | AC-2 |
| New EHR accounts | 296 | 25 | AC-2 |
| Privileged accounts (all admin planes) | 58 | 25 for the MFA test; all 58 for the rights review | IA-2(1), AC-6 |
| Networked medical devices and clinical servers | about 1,650 devices; 6 servers | 20 device classes; 6 servers (default-credential test) | IA-5 |
| Vendors with remote access | 46 | all 46 for configuration; 10 sessions | AC-17, MA-4 |
| Endpoints | 960 | 30 (encryption); 5 (EDR test) | SC-28, SI-3 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| BAAs on file / vendors in accounts payable | 168 / about 1,400 | 20 / 20 | SA-9 |
| Incidents (2025-2026) | 41 | 10 | IR-4 |
| Critical vulnerability findings (Q1-Q2 2026) | 48 | 48 | RA-5, SI-2 |
| Servers for configuration scan | 52 | 10 | CM-6 |
| Device returns to vendors (2026) | 6 | 6 | MP-6 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Network closets | 41 | 12 | PE-3 |

## 3. Methods and objects
- **Examine:**
  - policies (the 2023 set and drafts of the 2026 set) and the SSP draft
  - identity provider, EHR, directory, and cloud exports
  - backup, patch, scan, and EDR reports
  - BAAs, vendor files, and vendor access platform logs
  - the incident log, the 2025 tabletop report, and the emergency operations plan
  - destruction certificates and device return records
- **Interview:**
  - vCISO, IT Director, Information Security Manager, and both analysts
  - Compliance and Privacy Officer
  - CNO, Director of Emergency Management, Director of Biomedical Engineering, Director of Facilities
  - Pharmacy, Laboratory, and Imaging Directors; HR Director
  - the MSSP service lead
  - 15 randomly selected staff and 3 unit managers
- **Test:**
  - MFA sign-in tests on sampled privileged accounts
  - default-credential tests on 20 device classes and 6 clinical servers (manufacturer-approved, after hours, biomedical engineering present)
  - passive network capture on the clinical VLAN (2026-08-04)
  - reachability test from a nursing workstation (2026-08-05)
  - test calls from 3 units with the campus network simulated down
  - EICAR test files on 5 endpoints
  - a simulated impossible-travel sign-in to test MSSP escalation
  - a restore of one file share folder from the backup account
  - benchmark configuration scans of 10 servers
  - an EHR audit query on 10 randomly chosen non-VIP patients

## 4. Rules of engagement
- No testing that could disrupt patient care. Device tests ran after hours with manufacturer approval and biomedical engineering present. Infusion pumps, ventilators, anesthesia machines, and monitors connected to patients were excluded from active testing; the reachability test only checked that ports answered.
- No PHI left hospital systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system under its BAA.
- Stop-and-notify rule: any critical exposure is reported to the IT Director and the vCISO the same day. **Used once:** on 2026-08-05 the assessors reported that the infusion pump server and dispensing cabinet server shared one vendor default local administrator password, and that 4 of 20 sampled devices accepted default credentials. The hospital logged the finding as P01 R-054 on 2026-08-07 and changed the server password with the manufacturers on 2026-09-30.
- The 2 EHR accesses without an apparent treatment relationship (AU-6 test) were referred to the Compliance and Privacy Officer under the breach procedure, not investigated by the assessors.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 149 |
| Other than satisfied | 94 |
| **Total** | **243** |

Other than satisfied statements by risk: 26 High, 51 Moderate, 17 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 18 | 8 | Moderate | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | High | POAM-003 |
| IA-2 | 1 | 1 | Moderate | POAM-004 |
| IA-2(1) | 0 | 1 | High | POAM-004 |
| IA-5 | 6 | 4 | High | POAM-005 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| AT-2 | 8 | 2 | Low | POAM-006 |
| AU-2 | 2 | 4 | Moderate | POAM-007 |
| AU-6 | 2 | 1 | High | POAM-007 |
| CM-6 | 3 | 3 | Moderate | POAM-008 |
| CM-8 | 2 | 4 | High | POAM-009 |
| CP-2 | 7 | 17 | High | POAM-010 |
| CP-4 | 0 | 5 | High | POAM-011 |
| CP-8 | 0 | 1 | High | POAM-010 |
| CP-9 | 4 | 2 | Moderate | POAM-012 |
| CP-10 | 0 | 2 | High | POAM-011 |
| IR-4 | 9 | 4 | Moderate | POAM-013 |
| IR-6 | 2 | 0 | n/a | n/a |
| IR-8 | 12 | 5 | Moderate | POAM-013 |
| MA-4 | 3 | 5 | High | POAM-003 |
| MP-6 | 3 | 1 | Moderate | POAM-014 |
| PE-3 | 9 | 3 | Low | POAM-015 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 7 | 2 | Moderate | POAM-016 |
| SI-2 | 8 | 2 | Moderate | POAM-016 |
| SA-9 | 3 | 3 | High | POAM-017 |
| SR-6 | 0 | 1 | Moderate | POAM-017 |
| SA-22 | 1 | 1 | Moderate | POAM-018 |
| SC-7 | 4 | 2 | High | POAM-019 |
| SC-28 | 1 | 0 | n/a | n/a |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 10 | 2 | Moderate | POAM-020 |
| SI-7 | 3 | 3 | Moderate | POAM-021 |

**Fully satisfied (4 controls):** IR-6 (all 15 interviewed staff knew how to report), RA-3 (the 2026 risk analysis), SC-28 (encryption of endpoints, servers, cloud storage, and backups), and SI-3 (EDR quarantined every test file within 4 minutes). These confirm the strengths listed in the scenario facts.

**Fully other than satisfied (6 controls):** AC-6, IA-2(1), CP-4, CP-8, CP-10, and SR-6.

**Themes:**
1. The hospital can **protect and detect** on its IT estate, but it has **not proven it can recover** its own clinical servers or run downtime beyond 4 hours (CP-2, CP-4, CP-8, CP-10). For a hospital that means diversion.
2. **Privileged, vendor, and default credentials** are the largest exposure (AC-6, IA-2(1), IA-5, AC-17, MA-4). The default-credential finding was new and went straight into the risk register as R-054.
3. **The clinical network is flat and dark.** From a nursing workstation the testers could reach monitors, analyzers, cabinets, the cath lab system, and the building automation controller, and none of those segments is monitored (SC-7, SI-4, CM-8, AU-2).

**POA&M:** 30 controls had at least one Other than satisfied statement. They map to 21 POA&M items (POAM-001 to POAM-021), because related controls share an item. Four more items come from the gap analysis, the cloud mapping, and the AI assessment (POAM-022 emergency plan IT outage annex, POAM-023 breach decision log and practice notification, POAM-024 AI governance, POAM-025 PHI in the interface test environment). The total is 25 items: 12 High, 11 Moderate, and 2 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-20 | Plan and sample requests issued |
| 2026-07-27 to 2026-07-31 | Document examination and interviews |
| 2026-08-03 to 2026-08-06 | Walkthroughs and technical tests (after-hours device testing 2026-08-05) |
| 2026-08-07 to 2026-08-14 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (243 rows); `poam.csv` (25 items).

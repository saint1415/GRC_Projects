# Security Assessment Plan and Summary: Cris Santos Company | Health Care | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed multi-specialty physician group with an ASC and an imaging center) |
| System assessed | Enterprise Clinical Platform (ECP, SYS-01 to SYS-08), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Health Care and Social Assistance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control. The company's Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (site walkthroughs 2026-08-10 to 2026-08-13; device testing after hours 2026-08-12) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8); annual internal IT audit |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 242 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover HIPAA Security Rule standards and Required specifications with gaps in the gap analysis (P03);
- support inherited-control reliance and SOC 2 readiness for the joint venture (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle gaps; 164.308(a)(3)(ii)(C), (a)(4)(ii)(C); R-008 | Focused | Focused (samples of 25) |
| AC-6, IA-5 | Privileged access; R-009 (High) | Comprehensive | Comprehensive (all privileged accounts) |
| AC-17, MA-4 | Vendor remote access; R-037, R-038 | Focused | Focused |
| IA-2, IA-2(1) | Unique IDs and MFA; 164.312(a)(2)(i), 164.312(d) | Focused | Focused |
| AT-2 | Training; 164.308(a)(5) | Basic | Focused |
| AU-2, AU-6, AU-11 | Activity review gap; 164.308(a)(1)(ii)(D), 164.312(b); R-007, R-041 | Focused | Focused |
| CM-2, CM-6, CM-8 | Configuration and inventory; gap 1 and gap 8; R-005, R-040 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | Contingency and recovery; 164.308(a)(7); R-001 (Very High), R-014 to R-016 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability; 164.308(a)(6); R-042 | Focused | Basic |
| MP-6, PE-3 | Physical and media; 164.310 | Basic | Focused (4 of 10 sites) |
| RA-3, RA-5, SI-2 | Risk analysis and vulnerability management; R-028 | Focused | Focused |
| SA-9, SR-6 | Vendor oversight; 164.308(b); R-010, R-011 | Focused | Focused (samples of 20) |
| SA-22, SC-7 | Legacy devices and segmentation; R-003, R-004 | Focused | Focused |
| SC-28, SI-3, SI-4 | Encryption, EDR, monitoring; R-002, R-036 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 118 | 25 | AC-2, PS-4 |
| Transfers | 64 | 25 | AC-2 |
| New EHR accounts | 212 | 25 | AC-2 |
| Privileged accounts (all admin planes) | 41 | 25 for MFA test; all 41 for rights review | IA-2(1), AC-6 |
| Networked medical devices in inventory | about 240 | 20 (default-credential test) | IA-5 |
| Endpoints | 870 | 30 (encryption); 5 (EDR test) | SC-28, SI-3 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| BAAs on file / vendors in accounts payable | 110 / about 900 | 20 / 20 | SA-9 |
| Incidents (2025-2026) | 37 | 10 | IR-4 |
| Critical vulnerability findings (Q1-Q2 2026) | 50 | 50 | RA-5, SI-2 |
| Servers for configuration scan | 38 | 10 | CM-6 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Sites for walkthroughs | 10 | 4 (Clinic 1 with the CBO, Clinic 5, the ASC, the imaging center) | PE-3, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:**
  - policies (the 2023 set and drafts of the 2026 set)
  - the SSP draft
  - IdP, EHR, directory, and cloud exports
  - backup, patch, scan, and EDR reports
  - BAAs and vendor files
  - the incident log and the 2025 tabletop report
  - the ASC emergency plan
  - destruction certificates and lease records
- **Interview:**
  - vCISO, IT Director, Security Manager, and both analysts
  - Compliance and Privacy Officer
  - ASC Administrator and Imaging Center Director
  - HR Director and Director of Revenue Cycle
  - the MSSP service lead
  - 15 randomly selected staff
- **Test:**
  - MFA sign-in tests on sampled privileged accounts
  - default-credential tests on 20 medical devices (vendor-approved, after hours, biomedical staff present)
  - reachability test from a workstation VLAN at Clinic 5
  - passive network capture at Clinic 5 and the ASC
  - EICAR test files on 5 endpoints
  - a simulated impossible-travel sign-in to test MSSP escalation
  - a restore of one file-share folder from the backup account
  - benchmark configuration scans of 10 servers
  - an EHR audit query on 10 randomly chosen non-VIP patients

## 4. Rules of engagement
- No testing that could disrupt patient care. Medical device tests ran after hours with manufacturer approval and the ASC Administrator or Imaging Center Director present. Infusion pumps were excluded from active testing.
- No PHI left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system under its BAA.
- Stop-and-notify rule: any critical exposure is reported to the IT Director and the vCISO the same day. **Used once:** on 2026-08-12 the assessors reported the 3 PACS vendor service accounts with domain administrator rights and non-expiring passwords. The company logged the finding as P01 R-050 on 2026-08-14.
- The 2 EHR accesses without an apparent treatment relationship (AU-6 test) were referred to the Compliance and Privacy Officer under the breach procedure, not investigated by the assessors.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 146 |
| Other than satisfied | 96 |
| **Total** | **242** |

Other than satisfied statements by risk: 46 High, 44 Moderate, 6 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 19 | 7 | Moderate | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | Moderate | POAM-003 |
| AT-2 | 8 | 2 | Low | POAM-004 |
| AU-2 | 1 | 5 | Moderate | POAM-005 |
| AU-6 | 2 | 1 | High | POAM-006 |
| AU-11 | 0 | 1 | Low | POAM-005 |
| CM-2 | 1 | 4 | Moderate | POAM-007 |
| CM-6 | 3 | 3 | Moderate | POAM-007 |
| CM-8 | 2 | 4 | High | POAM-008 |
| CP-2 | 6 | 18 | High | POAM-009 |
| CP-4 | 0 | 5 | High | POAM-010 |
| CP-9 | 6 | 0 | n/a | n/a |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2 | 1 | 1 | Moderate | POAM-011 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 6 | 4 | High | POAM-012 |
| IR-4 | 10 | 3 | Moderate | POAM-013 |
| IR-6 | 2 | 0 | n/a | n/a |
| IR-8 | 11 | 6 | Moderate | POAM-014 |
| MA-4 | 3 | 5 | Moderate | POAM-003 |
| MP-6 | 3 | 1 | Moderate | POAM-015 |
| PE-3 | 9 | 3 | Low | POAM-016 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | High | POAM-017 |
| SA-9 | 1 | 5 | High | POAM-018 |
| SA-22 | 1 | 1 | Moderate | POAM-019 |
| SC-7 | 4 | 2 | High | POAM-020 |
| SC-28 | 1 | 0 | n/a | n/a |
| SI-2 | 8 | 2 | Moderate | POAM-017 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 10 | 2 | Moderate | POAM-021 |
| SR-6 | 0 | 1 | High | POAM-018 |

**Fully satisfied (6 controls):** CP-9 (isolated, write-once, encrypted backups), IA-2(1) (MFA on all 25 sampled privileged accounts), IR-6, RA-3, SC-28, and SI-3 (EDR detected and quarantined every test file within 5 minutes). These confirm the strengths listed in the scenario facts.

**Fully other than satisfied (5 controls):** AC-6, AU-11, CP-4, CP-10, and SR-6.

**Themes:**
1. The company can **protect and detect**, but it has **not proven it can recover** its own workloads (CP-2, CP-4, CP-10).
2. **Privileged and vendor access** is the largest exposure (AC-6, IA-5, AC-17, MA-4).
3. **Visibility gaps** (CM-8, AU-2, SI-4) leave medical devices, PACS, and the interface engine outside monitoring.

**POA&M:** 28 controls had at least one Other than satisfied statement. They map to 21 POA&M items (POAM-001 to POAM-021), because related controls share an item. Three more items come from the gap analysis and the AI assessment (POAM-022 ASC emergency plan, POAM-023 breach decision log, POAM-024 AI governance). The total is 24 items: 11 High, 11 Moderate, and 2 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Site walkthroughs and technical tests |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (242 rows); `poam.csv` (24 items).

# Security Assessment Plan and Summary: Cris Santos Company | Critical Manufacturing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed power and distribution transformer manufacturer, Florida) |
| System assessed | ERP and Production Scheduling Platform (EPSP), per the SSP (P02), including the MES at both plants and the IT/OT boundaries |
| Tier / Vertical | Mid-Market / Critical Manufacturing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test practices from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors) with an OT security specialist subcontractor, reporting to the board audit committee. Neither firm designs or operates any assessed control. The Security Manager coordinated access but did not select samples or rate findings. The OT Security Engineer and the plant Controls Leads were present for every OT test but did not perform them |
| Assessment window | 2026-08-03 to 2026-08-21 (OT tests in the Saturday maintenance windows: Plant 1 on 2026-08-08, Plant 2 on 2026-08-15) |
| Also satisfies | Annual internal IT audit; evidence for the FMS SOC 2 readiness work (P09) and for utility supplier questionnaires |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **33 controls, 253 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- implement FAR 52.204-21 safeguards on systems that hold FCI (P03 G-107 to G-123);
- support the utility addendum duties and the CSF 2.0 gaps rated High in P03;
- give the evidence that inherited-control reliance and the FMS SOC 2 readiness depend on (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle; FAR (b)(1)(i); utility addendum sec. 3; R-039, R-041 | Focused | Focused (samples of 25) |
| AC-4, SC-7, CA-3 | Plant 2 boundary and interconnections; FAR (b)(1)(x); R-001 (Very High) | Comprehensive | Comprehensive (both plants, cloud hub) |
| AC-6, IA-5 | Least privilege and authenticators; R-038, R-051 | Comprehensive | Comprehensive (all 41 privileged accounts; 20 Plant 2 devices) |
| AC-17, MA-4 | OEM remote access; R-003 | Focused | Comprehensive (all 4 Plant 2 routers; 20 Plant 1 sessions) |
| IA-2, IA-2(1) | Unique IDs and MFA; FAR (b)(1)(v)-(vi) | Focused | Focused (25 privileged accounts) |
| AT-2 | Training; G-059 | Basic | Focused (15 staff interviews) |
| AU-2, AU-6, SI-4 | Monitoring coverage; R-005 | Focused | Focused |
| CM-2, CM-3, CM-7, CM-8 | Configuration and inventory at Plant 2; R-009, R-010, R-033 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | Recovery; R-002, R-006 | Comprehensive | Comprehensive (including a live ERP database restore) |
| IR-4, IR-6, IR-8 | Incident capability and notices; R-008, R-044 | Focused | Basic |
| PE-3 | Physical access; FAR (b)(1)(viii)-(ix) | Basic | Focused (3 server rooms, 2 control rooms) |
| RA-3, RA-5, SI-2 | Risk assessment, vulnerability and patch management; R-052 | Focused | Focused (50 critical findings) |
| SA-9, SR-6 | Supplier oversight; R-015, R-046 | Focused | Focused (7 of 22 Tier 1) |
| SI-3 | Malicious code protection; FAR (b)(1)(xiii)-(xv) | Focused | Focused (5 endpoint tests; Plant 2 MES and kiosks) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items; small populations were tested in full. The assessors chose samples at random from populations extracted in their presence. Where P03 used the same population, the same sample was reused.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 214 | 25 | AC-2, PS-4 |
| Transfers | 71 | 25 | AC-2 |
| New accounts | 236 | 25 | AC-2 |
| Privileged accounts (all planes) | 41 | 25 for the MFA test; all 41 for the rights review | IA-2(1), AC-6 |
| Plant 2 network devices, HMI web interfaces, kiosks | about 60 | 20 (default credential test) | IA-5 |
| Plant 2 OEM cellular routers | 4 | 4 | AC-17, MA-4 |
| Plant 1 OEM gateway sessions | 212 | 20 | MA-4 |
| Endpoints (EICAR test) | 640 | 5 | SI-3 |
| Plant 2 kiosks (walkdown and service scan) | 22 | 22 (inventory); 5 (service scan, USB test) | CM-8, CM-7 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| ERP changes / Plant 2 MES changes | about 140 / about 60 | 15 / 15 | CM-3 |
| Servers for configuration scan | 46 | 10 | CM-2 |
| Critical vulnerability findings (Q1-Q2 2026) | 50 | 50 | RA-5, SI-2 |
| Incidents | 41 | 10 | IR-4 |
| Tier 1 suppliers | 22 | 7 | SA-9, SR-6 |
| Staff for reporting and awareness interviews | 850 | 15 (8 office, 7 production) | IR-6, AT-2 |
| Plant 2 visitor log entries (July 2026) | 40 | 40 | PE-3 |

## 3. Methods and objects
- **Examine:**
  - policies (the 2024 set and drafts of the 2026 set), the SSP draft, the 2024 IR and DR plans
  - identity provider, ERP, MES, directory, and cloud exports; Domain Admins membership and trust configuration
  - backup, patch, scan, EDR, and SIEM reports; firewall rule bases at the cloud hub and both plants
  - supplier contracts, SOC 2 reports, and the obligations register
  - change records, the incident register, and the 2025 tabletop report
- **Interview:**
  - vCISO, IT Director, Security Manager, both analysts, the GRC analyst, and the OT Security Engineer
  - Director of Manufacturing Engineering, both Plant Managers, and both Controls Leads
  - General Counsel, HR Director, Production Planning Manager, Director of Field Service
  - the MSSP service lead
  - 15 randomly selected staff
- **Test:**
  - MFA sign-in tests on 25 sampled privileged accounts
  - reachability tests from an office workstation at each plant (Plant 1 on 2026-08-08, Plant 2 on 2026-08-15)
  - default credential tests on 20 Plant 2 devices (OEM-approved, maintenance window, Controls Lead present)
  - service scans and a USB mount test on 5 Plant 2 kiosks
  - EICAR test files on 5 endpoints at HQ and Plant 1
  - a simulated impossible-travel sign-in to test MSSP escalation (2026-08-11)
  - a restore of one ERP database daily copy from the backup account into an isolated recovery account (2026-08-18)
  - benchmark configuration scans of 10 servers
  - power and configuration check of the 4 Plant 2 OEM routers

## 4. Rules of engagement
- **Safety first.** No active testing of PLCs, drying ovens, oil processing, cranes, or the high-voltage test bay. OT tests were passive or limited to HMI web interfaces, switches, and kiosks, ran only in the Saturday maintenance windows with OEM approval, and stopped if a Controls Lead asked.
- No customer, FMS, or federal data left company systems. Evidence was stored in the firm's encrypted workpaper system.
- **Stop-and-notify rule:** any critical exposure is reported to the Security Manager and the vCISO the same day. **Used once:** on 2026-08-12 the assessors reported that the Plant 2 MES service account was a member of the corporate Domain Admins group through the two-way domain trust, with a password last set in 2019. The company removed the rights and rotated the password on 2026-08-19 and logged the finding as P01 R-051 on 2026-08-21. Because the trust remains two-way until 2026-10-31, the finding stays open (POAM-002).
- The Plant 2 reachability test found the drying oven controller reachable from the office network. The assessors did not interact with it and reported it to the Plant 2 Manager the same day.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 134 |
| Other than satisfied | 119 |
| **Total** | **253** |

Other than satisfied statements by risk: 24 High, 68 Moderate, 27 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 17 | 9 | Moderate | POAM-004 |
| AC-4 | 0 | 1 | High | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | High | POAM-003 |
| AT-2 | 7 | 3 | Moderate | POAM-013 |
| AU-2 | 2 | 4 | Moderate | POAM-007 |
| AU-6 | 1 | 2 | High | POAM-007 |
| CA-3 | 2 | 6 | Moderate | POAM-001 |
| CM-2 | 2 | 3 | Moderate | POAM-010 |
| CM-3 | 5 | 5 | Moderate | POAM-010 |
| CM-7 | 4 | 2 | Moderate | POAM-010 |
| CM-8 | 3 | 3 | Moderate | POAM-008 |
| CP-2 | 8 | 16 | High | POAM-005 |
| CP-4 | 2 | 3 | High | POAM-005, POAM-006 |
| CP-9 | 4 | 2 | High | POAM-006 |
| CP-10 | 0 | 2 | High | POAM-005 |
| IA-2 | 1 | 1 | Moderate | POAM-004 |
| IA-2(1) | 0 | 1 | Moderate | POAM-016 |
| IA-5 | 7 | 3 | High | POAM-002, POAM-004 |
| IR-4 | 6 | 7 | High | POAM-011 |
| IR-6 | 1 | 1 | High | POAM-018 |
| IR-8 | 8 | 9 | High | POAM-011, POAM-018 |
| MA-4 | 1 | 7 | High | POAM-003 |
| PE-3 | 9 | 3 | Low | POAM-014 |
| PS-4 | 3 | 2 | Moderate | POAM-004 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | Moderate | POAM-009 |
| SA-9 | 3 | 3 | Moderate | POAM-012 |
| SC-7 | 4 | 2 | High | POAM-001 |
| SI-2 | 5 | 5 | Moderate | POAM-009 |
| SI-3 | 6 | 2 | Moderate | POAM-015 |
| SI-4 | 7 | 5 | High | POAM-007 |
| SR-6 | 0 | 1 | Moderate | POAM-012 |

The Risk column shows the highest risk among that control's Other than satisfied statements.

**Fully satisfied (1 control):** RA-3 (the SP 800-30 risk assessment, including risks to employees and applicants, was documented, reviewed, and shared with the audit committee).

**Fully other than satisfied (5 controls):** AC-4, AC-6, CP-10, IA-2(1), and SR-6.

**Themes:**
1. **Plant 1 works; Plant 2 does not yet.** Most Other than satisfied statements in AC-17, MA-4, SC-7, CM-2, CM-7, SI-3, and SI-4 are Plant 2 only. The same controls were Satisfied at Plant 1, so the fix is to extend proven practice, not to invent it.
2. **The Plant 2 domain trust is the most serious finding.** The MES service account gave a path from the flat Plant 2 network to the corporate domain (AC-6, IA-5f.).
3. **Recovery is designed but unproven** (CP-2, CP-4, CP-10). The assessors' own ERP database restore worked, but took 9 hours for the database alone against a 24-hour RTO for the whole ERP.
4. **Customer notice duties are a control weakness, not only a paperwork gap** (IR-6b., IR-8a.05).

**What worked well:** immutable backups (CP-9: all 31 July job days complete, copies locked), EDR (SI-3: every test file quarantined within 3 minutes and alerted to the MSSP), MSSP escalation (AU-6: 18 minutes against a 30-minute target), MFA on all 25 sampled identity-provider privileged accounts, Plant 1 OEM sessions (20 of 20 approved, MFA, recorded), and the risk assessment (RA-3).

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 17 POA&M items (POAM-001 to POAM-016 and POAM-018), because related controls share an item. Five more items come from the gap analysis, the cloud mapping, the SOC 2 readiness work, and the AI assessment (POAM-017 product security, POAM-019 FMS, POAM-020 FAR clause items, POAM-021 AI governance, POAM-022 standards). The total is 22 items: 10 High, 11 Moderate, and 1 Low. See `poam.csv`. New findings went back into the risk register (R-051).

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-08 | Plant 1 OT tests (maintenance window) |
| 2026-08-10 to 2026-08-14 | Technical tests at HQ and in the cloud; stop-and-notify on 2026-08-12 |
| 2026-08-15 | Plant 2 OT tests (maintenance window) |
| 2026-08-17 to 2026-08-21 | ERP restore test (2026-08-18), analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (253 rows); `poam.csv` (22 items).

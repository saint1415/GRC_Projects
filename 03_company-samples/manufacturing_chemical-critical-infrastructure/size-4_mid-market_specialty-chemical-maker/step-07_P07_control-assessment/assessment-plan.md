# Security Assessment Plan and Summary: Cris Santos Company | Chemical | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed specialty chemical formulator and packager) |
| System assessed | Process Control and Batch Management System (PCBMS) at the Port plant, per the SSP (P02), plus 4 common controls it inherits from corporate |
| Tier / Vertical | Mid-Market / Chemical |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors) with an OT specialist subcontractor (1 ICS security engineer), reporting to the board audit committee. Neither firm designs or operates any assessed control, which also meets the auditor independence test for USCG Cybersecurity Plan audits (33 CFR 101.630(f)(4)). The OT Security Engineer coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-10 to 2026-08-28 (OT testing 2026-08-19 during a planned Blend Hall 1 outage) |
| Also satisfies | Annual internal IT audit; evidence for the USCG Cybersecurity Assessment (101.650(e)(1)) and the SOC 2 readiness work (P09) |
| Results accepted | Chief Operating Officer, 2026-09-22; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls (32 PCBMS controls and 4 inherited common controls), 260 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the USCG cybersecurity rule measures with the largest gaps in the gap analysis (P03);
- test the controls the PCBMS inherits from corporate (identity, HR, incident support, contracts).

| Control | Why selected (risk ID or requirement) | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-2, PS-4 | Shared console accounts and OT account lifecycle; 101.650(a)(6)-(7); R-005, R-017 | Focused | Focused (samples of 25) |
| AC-3, CM-5 | Control and SIS change restrictions; 68.73(a)(4)-(5); R-008 | Comprehensive | Comprehensive (tested on the outage) |
| AC-6, AC-17, MA-4 | Vendor and remote access; 101.650(a)(4)-(5), (f)(3); R-001 (High), R-015 | Comprehensive | Focused (20 sessions) |
| AT-2, AT-3 | USCG training deadline; 101.650(d); R-012 | Focused | Comprehensive (all 430 Port employees) |
| AU-6, AU-9, SI-4 | OT monitoring; 101.650(c)(1), (h)(2); R-002 (Very High), R-010 | Comprehensive | Focused |
| CA-3 | Information exchanges across the OT DMZ | Basic | Comprehensive (all exchanges) |
| CM-2, CM-3, CM-7, CM-8, MP-7 | Baselines, MOC, ports, inventory; 101.650(b), (i)(2); R-044, R-047, R-052 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | OT recovery; 101.650(g)(4); R-006 (High) | Comprehensive | Comprehensive |
| IA-5 | Default and shared passwords; 101.650(a)(2)-(3); R-011 | Comprehensive | Focused (30 devices) |
| IR-4, IR-6, IR-8 | Incident capability and MTSA reporting; 6.16-1; R-013, R-045 | Focused | Basic |
| PE-3 | Physical access to OT; 101.650(i)(1) | Basic | Focused (Port plant only) |
| RA-3, RA-5, SI-2 | Risk assessment and KEVs; 101.650(e); R-009 | Focused | Focused |
| SA-9, SR-8 | Vendor oversight and notice; 101.650(f)(1)-(2); R-033 | Focused | Comprehensive (all OT vendors) |
| SC-7 | IT/OT segmentation; 101.650(h)(1); R-002 | Comprehensive | Comprehensive (all 214 rules) |
| IA-2(1), IR-7 (common) | MFA from the identity provider; MSSP and insurer support | Basic | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for controls that operate many times a year, 5 to 10 for weekly or monthly controls. Samples were drawn at random from populations extracted in the assessors' presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 41 | 15 | AC-2 |
| DCS user accounts | 186 | 25 | AC-2, IA-2 |
| Gateway and OT administrator accounts | 41 | 41 (MFA test and rights review) | IA-2(1), AC-6 |
| Gateway sessions (2026-05 to 2026-07) | 312 | 20 | AC-17, MA-4 |
| Port OT devices for default credential test | about 340 reconciled | 30 (vendor-approved, during the outage) | IA-5 |
| Control system MOCs (2025-08 to 2026-07) | 63 | 15 | CM-3 |
| Firewall rules | 214 | 214 | SC-7 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Port employees and OT contractors (training) | 430 and 40 | All | AT-2 |
| OT sensor alerts (July 2026) | 14 | 14 | AU-6, SI-4 |
| Staff for reporting-awareness interviews | 430 | 15 | IR-6 |
| Port OT workstations (device control) | 52 | 52 (report) | MP-7 |

## 3. Methods and objects
- **Examine:** policies (2024 set and 2026 drafts); the SSP draft; DCS, SIS, gateway, and firewall exports; the OT sensor inventory and alerts; the MOC log; backup logs and the fire safe log; the OT contingency plan draft; the FSP reporting section; vendor contracts; training records.
- **Interview:** vCISO, Information Security Manager (CySO), OT Security Engineer, Controls Engineering Manager and 2 controls engineers, Process Safety Manager, Port Plant Manager, FSO, 4 Shift Supervisors, HR Director, the DCS integrator's lead engineer, the MSSP service lead, and 15 randomly chosen staff.
- **Test (2026-08-19, Blend Hall 1 outage):** DCS role enforcement; SIS download attempt with the keyswitch in run; default credential test on 30 OT devices; reachability tests from the supervisory zone and the business network; a simulated port scan to test OT sensor detection and response; clearing a DCS audit trail on the training station; restore of one historian client image; hash check of the latest offline backup; MFA tests on all 41 privileged accounts.

## 4. Rules of engagement
- **Safety first.** No active testing on running units. Active tests touched only Blend Hall 1 equipment that was down for the outage, the training station, and the OT DMZ. The Ammonia and Peroxide Units and the tank farm were tested passively only. Every test had a work permit, the Shift Supervisor's approval, and a controls engineer present, following SP 800-82 Rev. 3 cautions on testing OT.
- **SSI and CVI.** Evidence containing SSI (FSP sections, network maps) was reviewed on site and not copied into workpapers; the assessors are covered persons under the FSP for this engagement.
- **Stop-and-notify rule:** any critical exposure is reported to the OT Security Engineer and the CySO the same day. **Used once:** on 2026-08-19 the OT specialist logged in to the radar tank gauging server with the vendor default administrator password from the supervisory zone. The password was changed on 2026-08-20 and the company logged the finding as P01 R-011 and gap 15.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 162 |
| Other than satisfied | 98 |
| **Total** | **260** |

Other than satisfied statements by risk: 53 High, 40 Moderate, 5 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 17 | 9 | Moderate | POAM-002 |
| AC-3 | 1 | 0 | n/a | n/a |
| AC-6 | 0 | 1 | Moderate | POAM-003 |
| AC-17 | 2 | 2 | High | POAM-003 |
| AT-2 | 7 | 3 | High | POAM-010 |
| AT-3 | 6 | 3 | Moderate | POAM-010 |
| AU-6 | 0 | 3 | High | POAM-004 |
| AU-9 | 0 | 2 | Moderate | POAM-004 |
| CA-3 | 5 | 3 | Low | POAM-013 |
| CM-2 | 3 | 2 | Moderate | POAM-007 |
| CM-3 | 7 | 3 | Moderate | POAM-008 |
| CM-5 | 5 | 1 | High | POAM-006 |
| CM-7 | 4 | 2 | Moderate | POAM-007 |
| CM-8 | 2 | 4 | Moderate | POAM-007 |
| CP-2 | 14 | 10 | High | POAM-005 |
| CP-4 | 0 | 5 | High | POAM-005 |
| CP-9 | 5 | 1 | Moderate | POAM-005 |
| CP-10 | 0 | 2 | High | POAM-005 |
| IA-2 | 0 | 2 | High | POAM-002 |
| IA-5 | 6 | 4 | High | POAM-001 |
| IR-4 | 9 | 4 | Moderate | POAM-011 |
| IR-6 | 0 | 2 | High | POAM-011 |
| IR-7 | 2 | 0 | n/a | n/a |
| IR-8 | 12 | 5 | Moderate | POAM-011 |
| MA-4 | 6 | 2 | Moderate | POAM-003 |
| MP-7 | 1 | 1 | Moderate | POAM-007 |
| PE-3 | 10 | 2 | Low | POAM-014 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | High | POAM-009 |
| SA-9 | 3 | 3 | High | POAM-012 |
| SC-7 | 4 | 2 | High | POAM-001 |
| SI-2 | 7 | 3 | High | POAM-009 |
| SI-4 | 5 | 7 | High | POAM-004 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| PS-4 | 4 | 1 | Moderate | POAM-002 |
| SR-8 | 0 | 1 | High | POAM-012 |

**Fully satisfied (4 controls):** AC-3 (DCS roles and the SIS keyswitch held under test), IA-2(1) (MFA on all 41 privileged accounts), IR-7, and RA-3. These confirm the strengths listed in the scenario facts.

**Fully other than satisfied (8 controls):** AC-6, AU-6, AU-9, CP-4, CP-10, IA-2, IR-6, and SR-8.

**Themes:**
1. **Protect is ahead of Detect and Recover.** The DMZ, gateway, roles, and SIS keyswitch work (AC-3, SC-7 external interfaces), but nobody watches OT around the clock (AU-6, SI-4) and the company has never proven it can rebuild the DCS (CP-4, CP-10).
2. **Identity at the console and at the edge.** Shared console accounts (IA-2), manual OT deprovisioning (AC-2, PS-4), and a default password on the tank gauging server (IA-5) are the most direct paths to the scenarios in P01 R-001, R-005, and R-011.
3. **USCG evidence gaps.** Training (AT-2), 6.16-1 reporting (IR-6), vendor notice (SR-8), and KEV handling (RA-5, SI-2) are explicit Subpart F requirements, so these findings also count against the 2027-07-16 plan.

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 14 POA&M items (POAM-001 to POAM-014), because related controls share an item. Eight more items come from the gap analysis, the BIA, the SOC 2 readiness work, and the AI assessment (POAM-015 USCG Assessment and Plan, POAM-016 emergency notification, POAM-017 SSI shares, POAM-018 Inland plant, POAM-019 DOT security plan, POAM-020 AI governance, POAM-021 TTRS readiness, POAM-022 PHA cyber scenarios). The total is 22 items: 15 High, 5 Moderate, and 2 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-31 | Plan, rules of engagement, and sample requests issued |
| 2026-08-10 to 2026-08-14 | Document examination and interviews |
| 2026-08-17 to 2026-08-19 | Site walkthroughs; OT testing on 2026-08-19 during the Blend Hall 1 outage |
| 2026-08-20 to 2026-08-28 | Analysis, draft findings, management responses |
| 2026-09-22 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (260 rows); `poam.csv` (22 items).

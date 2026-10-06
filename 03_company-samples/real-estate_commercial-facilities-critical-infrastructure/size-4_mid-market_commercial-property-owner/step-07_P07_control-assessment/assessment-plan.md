# Security Assessment Plan and Summary: Cris Santos Company | Commercial Facilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial office and retail property owner-operator) |
| System assessed | Building Automation and Access Control System (BAACS), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Commercial Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test methods per NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, and 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control. The GRC Analyst coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (walkthroughs and tests 2026-08-10 to 2026-08-13; OT device tests after hours) |
| Also supports | CISA CPG 2.0 goal 2.C (independent validation); annual internal IT audit; evidence for SOC 2 readiness (P09) |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls, 252 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the High and Moderate CPG 2.0 gaps in the gap analysis (P03);
- support inherited-control reliance and SOC 2 readiness for the JV (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Account and credential lifecycle; CPG 3.D; R-007, R-038 | Focused | Focused (samples of 25 and 15) |
| AC-6 | Excess administrators and export rights; CPG 3.H; R-019, R-027 | Focused | Comprehensive (all platform roles) |
| AC-17, MA-4 | Integrator remote access; CPG 1.E, 3.F; R-002 | Comprehensive | Comprehensive (all 8 Platform B servers; 10 gateway sessions) |
| AC-4, SC-7, SC-7(5) | Segmentation and exposure; CPG 3.I, 3.S; R-001, R-008 | Comprehensive | Focused (all 14 rule sets; reachability tests at 2 properties) |
| IA-2, IA-2(1), IA-5 | Unique accounts, MFA, default passwords; CPG 3.A, 3.C, 3.F; R-009 | Focused | Focused (25 privileged accounts; 30 OT devices) |
| AT-3 | OT role-based training; CPG 3.J | Basic | Focused |
| AU-2, AU-6, AU-11, SI-4 | Logging and monitoring; CPG 3.Q, 4.B; R-029, R-041 | Focused | Focused |
| CM-2, CM-3, CM-7, CM-8 | Baselines, change control, inventory; CPG 2.A, 3.N; R-028, R-047 | Focused | Focused (40 controllers; 10 changes) |
| CP-2, CP-4, CP-9, CP-10 | Recovery; CPG 3.O, 6.A; R-001 (Very High), R-004 | Comprehensive | Comprehensive |
| IR-4, IR-8 | Incident capability; CPG 1.C; R-030 | Focused | Basic (10 incidents) |
| PE-2, PE-3, PE-8 | Physical protection of BAS servers and the SCC | Basic | Focused (6 of 14 properties) |
| RA-5, SI-2, SI-3, SA-22 | Vulnerabilities, patching, malware, unsupported systems; CPG 2.B, 4.A; R-010, R-039 | Focused | Focused (40 critical findings; 5 EDR tests) |
| SA-9, SR-6 | Vendor oversight; CPG 1.D, 1.E; R-023 | Focused | Comprehensive (41 contracts) |
| SI-12 | Retention of visitor and video data; Fla. Stat. 501.171(8); R-016 | Basic | Comprehensive (settings) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 12 items; small populations were tested in full. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 41 | 15 | AC-2 |
| Tenant credential revocation requests | about 2,600 | 25 | AC-2 |
| Privileged accounts (identity provider, cloud, platform, gateway) | 31 | 25 (MFA test); all 31 (rights review) | IA-2(1), AC-6 |
| OT devices (default credential test) | about 6,800 controllers, 410 door controllers, 46 NVRs | 30 at Tower 1, Park 2, and Retail 2 | IA-5 |
| Platform B controllers (inventory trace) | about 1,600 | 40 | CM-8 |
| Platform B program changes (from integrator invoices, January to June 2026) | 10 | 10 | CM-3 |
| Gateway sessions (July 2026) | 186 | 10 | AC-17, MA-4 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| Critical vulnerability findings (Q1-Q2 2026) | 40 | 40 | RA-5, SI-2 |
| Incidents (2025-2026) | 34 | 10 | IR-4 |
| Vendor contracts with access or data | 41 | 41 | SA-9, SR-6 |
| Properties for walkthroughs | 14 | 6 (Tower 1, Tower 2, Mixed-Use 1, Park 2, Retail 2, Retail 5) | PE-2, PE-3, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:**
  - policies (the 2024 set and the 2026 set), the SSP draft, and the standards drafts
  - identity provider, access control platform, BAS, and cloud exports
  - firewall rule exports for 14 sites, the MSSP external scan, backup, patch, scan, and EDR reports
  - vendor contracts and the SOC 2 review file
  - the incident queue, the 2024 IR plan, and the P08 runbooks
  - tower degraded-mode procedures and integrator service manuals
- **Interview:**
  - vCISO, IT Director, Security Manager, OT security analyst, GRC Analyst
  - VP of Engineering, Building Technology Manager, 4 chief engineers
  - Director of Security Operations and 2 SCC shift leads
  - HR Director, General Counsel, and the MSSP service lead
  - both BAS integrators
- **Test:**
  - MFA sign-in tests on 25 privileged accounts
  - default credential tests on 30 OT devices (read-only login attempts, after hours, integrator and chief engineer present)
  - reachability tests from the Tower 1 corporate VLAN and a Retail 2 office port
  - EICAR test files on 5 console PCs and the Platform A server
  - a simulated after-hours gateway login to test MSSP escalation
  - a restore of one historian table to the recovery subnet
  - an inventory trace of 40 Platform B controllers

## 4. Rules of engagement
- **No active scanning of OT devices.** Following SP 800-82 Rev. 3, field controllers, door controllers, and NVRs were not scanned. Default credential tests were single read-only login attempts, run after hours with the integrator and the chief engineer present, and stopped at the first success.
- No test could change a setpoint, schedule, or door state. Life-safety systems were out of scope and not touched.
- No personal information left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system.
- **Stop-and-notify rule:** any critical exposure is reported to the IT Director and the vCISO the same day. **Used once:** on 2026-08-12 the assessors reported that a test laptop on the Tower 1 corporate VLAN reached the Platform A server's management ports through a "temporary" any-any rule left from the 2025 cutover. The company logged it as P01 R-050 on 2026-08-14 and scheduled removal by 2026-09-30 (POAM-004).

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 131 |
| Other than satisfied | 121 |
| **Total** | **252** |

Other than satisfied statements by risk: 61 High, 47 Moderate, 13 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 19 | 7 | Moderate | POAM-001 |
| AC-4 | 0 | 1 | High | POAM-004 |
| AC-6 | 0 | 1 | Moderate | POAM-002 |
| AC-17 | 2 | 2 | High | POAM-003 |
| IA-2 | 0 | 2 | Moderate | POAM-005 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 7 | 3 | High | POAM-005 |
| AT-3 | 3 | 6 | Low | POAM-012 |
| AU-2 | 2 | 4 | High | POAM-006 |
| AU-6 | 2 | 1 | High | POAM-006 |
| AU-11 | 1 | 0 | n/a | n/a |
| CM-2 | 1 | 4 | Moderate | POAM-007 |
| CM-3 | 5 | 5 | Moderate | POAM-007 |
| CM-7 | 4 | 2 | Moderate | POAM-007 |
| CM-8 | 2 | 4 | High | POAM-008 |
| CP-2 | 10 | 14 | High | POAM-009 |
| CP-4 | 0 | 5 | High | POAM-010 |
| CP-9 | 4 | 2 | High | POAM-010 |
| CP-10 | 0 | 2 | High | POAM-010 |
| IR-4 | 8 | 5 | Moderate | POAM-011 |
| IR-8 | 10 | 7 | Moderate | POAM-011 |
| MA-4 | 1 | 7 | High | POAM-003 |
| PE-2 | 4 | 2 | Low | POAM-013 |
| PE-3 | 7 | 5 | Low | POAM-013 |
| PE-8 | 3 | 0 | n/a | n/a |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| RA-5 | 6 | 3 | Moderate | POAM-014 |
| SA-9 | 2 | 4 | High | POAM-016 |
| SA-22 | 1 | 1 | High | POAM-015 |
| SC-7 | 3 | 3 | High | POAM-004; POAM-018 |
| SC-7(5) | 1 | 1 | High | POAM-004 |
| SI-2 | 5 | 5 | Moderate | POAM-014 |
| SI-3 | 6 | 2 | Moderate | POAM-015 |
| SI-4 | 6 | 6 | High | POAM-006 |
| SI-12 | 2 | 2 | Moderate | POAM-017 |
| SR-6 | 0 | 1 | High | POAM-016 |

**Fully satisfied (3 controls):** IA-2(1) (security keys on all 25 sampled privileged accounts), AU-11 (retention of the logs that are collected), and PE-8 (visitor records for the data room and SCC).

**Fully other than satisfied (6 controls):** AC-4, AC-6, IA-2, CP-4, CP-10, and SR-6.

**Themes:**
1. **The towers and IT pass; Platform B fails.** Most Satisfied statements come from IT, the gateway, and the Platform A properties. Most Other than satisfied statements come from the 8 Platform B properties: an always-on integrator tool (MA-4 has 7 of 8 statements Other than satisfied), default passwords, no backups, unsupported servers, no change control.
2. **Recovery has never been proven anywhere** (CP-2, CP-4, CP-10), even where backups exist.
3. **Visibility stops at the IT edge** (AU-2, AU-6, SI-4, CM-8). OT activity and access control administrator actions are not logged or monitored, and 45% of OT devices are not inventoried.
4. **Rule hygiene matters as much as design.** The Tower 1 any-any rule showed that a well-designed OT zone can be undone by one change nobody reviewed.

**POA&M:** 33 controls had at least one Other than satisfied statement. They map to 18 POA&M items (POAM-001 to POAM-018), because related controls share an item. Four more items come from other deliverables: POAM-019 card data handling (P03), POAM-020 AI governance (P10), POAM-021 notice readiness (P03), and POAM-022 the standards set (P06). The total is 22 items: 11 High, 9 Moderate, and 2 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Walkthroughs and technical tests (OT tests after hours) |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (252 rows); `poam.csv` (22 items).

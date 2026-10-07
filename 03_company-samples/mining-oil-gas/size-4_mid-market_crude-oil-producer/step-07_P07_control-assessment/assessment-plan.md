# Security Assessment Plan and Summary: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed independent crude oil producer with a Panhandle gathering system) |
| System assessed | Field SCADA and Production Accounting System (FSPA), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Mining, Quarrying, and Oil and Gas Extraction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with the OT discussion in the SP 800-82 Rev. 3 overlay (Appendix F) used to judge OT-specific alternatives |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, and 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control and is not the external financial auditor. The Security Manager and the OT Security Engineer coordinated access but did not select samples or rate findings. The SCADA and Automation Manager escorted the team in the OCC, the BCC, and at field sites |
| Assessment window | 2026-08-03 to 2026-08-21 (field testing 2026-08-11 to 2026-08-13) |
| Benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary; P03). No binding federal sector rule requires this assessment. It also serves as the annual IT audit for the audit committee |
| Results accepted | Chief Operating Officer, 2026-09-16, with the VP Operations agreeing to the field-operations items; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls, 251 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01: R-001, R-002, R-003, R-006, R-020, R-036);
- test the High and Moderate gaps in the gap analysis (P03), most of which are gaps in scale outside the Panhandle;
- support the recovery values in the BIA (P05) and the SOC 2 readiness work for gathering and measurement services (P09).

| Control | Why selected (risk ID or gap) | Depth | Coverage |
|---|---|---|---|
| AC-17, MA-4 | Vendor remote access outside the jump host; R-004, R-036; P03 PR.AA-03, DE.CM-06 | Comprehensive | Comprehensive (every remote access path, external scan) |
| SC-7, CP-7 | Paths around the OT DMZ at the BCC and South Florida; R-001 (Very High); P03 PR.IR-01 | Comprehensive | Comprehensive (all IT/OT and external interfaces) |
| CP-2, CP-4, CP-9, CP-10 | SCADA recovery and BCC failover; R-003, R-014; P05 findings 1 and 2 | Comprehensive | Focused |
| AC-2, IA-2, IA-5, PS-4 | OT account lifecycle, shared accounts, field device credentials; R-010, R-041; P03 PR.AA-01 | Focused | Focused (samples of 25; 20 field devices) |
| IA-2(1) | MFA for privileged access; insurer requirement | Focused | Focused (25 of 38 privileged accounts) |
| AC-6, AC-6(5) | Owner deck exposure and OT administrator accounts; R-002, R-037, R-040 | Focused | Comprehensive |
| CM-2, CM-3, CM-5, SI-7 | Field controller, pump station setpoint, and flow computer integrity; R-006, R-007, R-008; P03 ID.RA-07 | Focused | Focused (samples of 15 and 20 changes) |
| CM-8 | OT inventory about 70% complete; R-012; P03 ID.AM-01 | Focused | Focused (6 field sites counted) |
| SI-2, SA-22, RA-5 | Unsupported OS and OT patching; R-005, R-012; P03 PR.PS-02 | Focused | Focused |
| SI-3, SI-4, AU-2, AU-6, AU-11 | Malware protection, OT monitoring coverage, logs; R-011, R-046; P03 DE.CM-01, DE.AE-02 | Focused | Focused |
| IR-3, IR-4, IR-8 | Incident capability, crisis management, pipeline notice link; R-028, R-029 | Focused | Focused (10 of 31 incidents) |
| SA-9, SR-6 | OT vendors never assessed; R-019, R-020; P03 GV.SC | Focused | Focused (20 of 64 contracts) |
| AT-2 | Field staff and controller training; P03 PR.AT-01 | Basic | Focused (30 field staff, 20 interviews) |
| PE-3, MP-7 | Field sites, control centers, removable media; R-024, R-026 | Basic | Focused (control centers and 12 field sites) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control that operates many times a year, 15 for weekly or monthly controls, and 20 where a population is spread across sites. The assessors chose samples at random from populations extracted in their presence. The same samples support the evidence in the gap analysis (P03 section 2).

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 38 | 15 | AC-2 |
| New accounts and hires | 110 | 25 | AC-2, AT-2 |
| Privileged accounts (IdP, cloud, directory, jump host) | 38 | 25 for the MFA test; all 38 for rights | IA-2(1), AC-6(5) |
| Jump host sessions (July 2026) | 212 | 25 | AC-17, MA-4 |
| Panhandle CAB changes (2025-08 to 2026-07) | 44 | 15 | CM-3 |
| South Florida and Alabama controller changes from work orders | 58 | 20 | CM-3 |
| Field devices for the default-credential test (cellular modems and radios) | about 300 | 20, plus the 4 packager gateways | IA-5 |
| Devices at sampled well pads (physical count) | 6 pads | 41 devices | CM-8 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| Corporate critical vulnerability findings (Q1-Q2 2026) | 46 | 46 | SI-2, RA-5 |
| Incidents (2025-2026) | 31 | 10 | IR-4 |
| Contracts with system or data access | 64 | 20 | SA-9 |
| Field crew and driver training records | 485 | 30 | AT-2 |
| Staff for reporting-awareness interviews | 850 | 20 (10 office, 6 field, 4 Production Controllers) | AT-2, IR-4 |
| Field sites for walkthroughs | 640 well sites and 24 facilities | 12 (4 tank batteries, 2 compression stations, 6 well pads), plus the OCC, BCC, South Florida office, and Central Facility | PE-3, CM-8, CM-5 |

## 3. Methods and objects
- **Examine:**
  - POL-01 to POL-05 (2024 versions and the 2026 drafts) and the draft standards
  - the SSP draft and the P04 diagram
  - IdP, OT directory, SCADA local account, cloud, and data platform permission exports
  - OT DMZ, site firewall, and cloud firewall rule exports
  - CAB tickets, controller work orders, the program repository report, and baselines
  - backup reports, the offline image log, and restore test records
  - patch, scan, EDR, allowlisting, and OT sensor reports
  - the 2024 incident response plan, the P08 drafts, the 2025 tabletop report, and the incident log
  - contracts, vendor review files, and training records
- **Interview:**
  - COO, VP Operations, VP IT, Security Manager, OT Security Engineer, SCADA and Automation Manager
  - Control Room Manager, Pipeline Compliance Manager, Measurement Supervisor, Production Accounting Director
  - the 3 Field Superintendents, HR Director, General Counsel
  - the MDR provider's service lead and the SCADA integrator's lead engineer
  - 20 randomly selected staff
- **Test:**
  - external scan of the company's internet addresses and the cellular carrier address ranges used by company devices (2026-08-12)
  - default-credential login test on 20 field devices and the 4 packager gateway login pages (management pages only, never the controllers behind them)
  - reachability test from a corporate workstation at the South Florida office toward the HMI segment and the BCC (2026-08-11)
  - MFA sign-in tests on 25 privileged accounts
  - test files on 5 corporate endpoints and 1 OCC engineering workstation
  - a simulated suspicious sign-in to test MDR escalation (escalated in 18 minutes)
  - physical counts of field devices at 6 pads, compared with the inventory
  - observation of HMI sign-in at a shift change at the OCC, the South Florida office, and the BCC

## 4. Rules of engagement
- **Safety first and no active scanning of OT.** SP 800-82 Rev. 3 advises caution with active scanning on an operational OT network because it can disrupt devices, so OT evidence came from configuration exports, passive sensor data, observation, and management-page logins only. No test touched a safety shutdown.
- Field device tests ran with a Production Controller watching the affected sites on SCADA, with the cellular carrier's approval, and the SCADA and Automation Manager could stop testing at any time.
- No royalty owner, employee, or shipper data left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system.
- **Stop-and-notify rule: used once.** On 2026-08-12 at 15:40 the external scan found 2 of the 4 compression station packager gateways accepting inbound internet connections with the packager's shared password, and from one of them the station PLC was reachable. The assessors stopped and notified the Security Manager, the OT Security Engineer, and the VP Operations. The OT Security Engineer blocked inbound internet access on all 4 gateways and had the passwords changed on 2026-08-13. The company logged the finding as P01 R-052 on 2026-08-14 and it is tracked as POAM-002.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 138 |
| Other than satisfied | 113 |
| **Total** | **251** |

Other than satisfied statements by risk: 3 Very High, 68 High, 37 Moderate, 5 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 18 | 8 | High | POAM-001 |
| AC-6 | 0 | 1 | Moderate | POAM-013 |
| AC-6(5) | 0 | 1 | Moderate | POAM-014 |
| AC-17 | 2 | 2 | High | POAM-002 |
| AT-2 | 7 | 3 | Low | POAM-017 |
| AU-2 | 3 | 3 | Moderate | POAM-015 |
| AU-6 | 2 | 1 | High | POAM-009 |
| AU-11 | 0 | 1 | Moderate | POAM-015 |
| CM-2 | 2 | 3 | High | POAM-008 |
| CM-3 | 5 | 5 | High | POAM-008 |
| CM-5 | 5 | 1 | Moderate | POAM-008 |
| CM-8 | 1 | 5 | Moderate | POAM-006 |
| CP-2 | 15 | 9 | High | POAM-005 |
| CP-4 | 1 | 4 | High | POAM-004; POAM-005 |
| CP-7 | 2 | 2 | Very High | POAM-003; POAM-005 |
| CP-9 | 4 | 2 | High | POAM-004 |
| CP-10 | 0 | 2 | High | POAM-004 |
| IA-2 | 0 | 2 | High | POAM-001 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 6 | 4 | High | POAM-001; POAM-002 |
| IR-3 | 0 | 1 | Moderate | POAM-016 |
| IR-4 | 8 | 5 | Moderate | POAM-016 |
| IR-8 | 11 | 6 | Moderate | POAM-016 |
| MA-4 | 1 | 7 | High | POAM-002 |
| MP-7 | 0 | 2 | Moderate | POAM-019 |
| PE-3 | 10 | 2 | Low | POAM-018 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| RA-5 | 7 | 2 | Moderate | POAM-011 |
| SA-9 | 2 | 4 | High | POAM-012 |
| SA-22 | 1 | 1 | High | POAM-010 |
| SC-7 | 1 | 5 | Very High | POAM-002; POAM-003 |
| SI-2 | 5 | 5 | High | POAM-010 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 5 | 7 | High | POAM-002; POAM-009 |
| SI-7 | 2 | 4 | Moderate | POAM-007; POAM-012 |
| SR-6 | 0 | 1 | High | POAM-012 |

**Fully satisfied (2 controls):** IA-2(1) and SI-3. MFA protected all 25 sampled privileged accounts, and EDR and allowlisting stopped every test file. These confirm the strengths in the scenario facts.

**Fully other than satisfied (8 controls):** AC-6, AC-6(5), AU-11, CP-10, IA-2, IR-3, MP-7, and SR-6.

**Themes:**
1. **The controls work where the program has reached.** At the OCC, the Panhandle, and in business IT, account management, change control, backups of cloud workloads, malware protection, and monitoring met most statements.
2. **Vendor paths and the BCC are the largest exposure** (SC-7, AC-17, MA-4, IA-5, CP-7). The stop-and-notify finding showed that an always-on vendor path was reachable from the internet.
3. **Recovery of SCADA is not proven** (CP-4, CP-9, CP-10). The images that a rebuild depends on sit where the threat can reach them, and no image restore or full failover has been tested.
4. **Field integrity and visibility gaps** (CM-3, CM-8, SI-4, SI-7, AU-2) leave South Florida and Alabama controllers, flow computers, and the pump station setpoints without the change control and monitoring the OCC has.

**POA&M:** 34 controls had at least one Other than satisfied statement. They map to 19 POA&M items (POAM-001 to POAM-019), because related controls share an item. 4 more items come from the gap analysis, the SOC 2 readiness work, and the AI assessment (POAM-020, POAM-021, POAM-022, and POAM-023). The total is 23 items: 1 Very High, 8 High, 11 Moderate, and 3 Low. See `poam.csv`. Each funded item in the FY2027 security plan (P01 section 4) maps to a POA&M item.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan, rules of engagement, and sample requests issued; rules of engagement approved by the VP Operations |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Control center and field site walkthroughs (2026-08-10 OCC and Central Facility; field testing 2026-08-11 to 2026-08-13) |
| 2026-08-12 | Stop-and-notify: packager gateways |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-16 | Results and POA&M accepted by the COO and presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (251 rows); `poam.csv` (23 items).

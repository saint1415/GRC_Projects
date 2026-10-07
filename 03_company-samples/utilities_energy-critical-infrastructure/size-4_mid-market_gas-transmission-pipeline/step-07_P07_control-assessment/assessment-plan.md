# Security Assessment Plan and Summary: Cris Santos Company | Energy | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed interstate natural gas transmission pipeline operator) |
| System assessed | Pipeline SCADA and Gas Control System (PSGCS, CSC-PSGCS-01): SYS-01 to SYS-07 and physical access control at the GCC, BCC, and compressor stations, per the SSP (P02). Supporting enterprise controls (vendor management, training, risk assessment) were assessed where the PSGCS inherits them |
| Tier / Vertical | Mid-Market / Energy |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (objective labels and determination statements from the NIST catalog in `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, and 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control. The GRC lead arranged access and evidence but did not select samples or rate findings. OT tests were run by company staff under the assessors' direction (see section 4) |
| Assessment window | 2026-08-03 to 2026-08-21 (site work 2026-08-10 to 2026-08-14; Compressor Station 4 and two M&R stations visited 2026-08-12) |
| Also satisfies | Assessment work under the TSA-approved Cybersecurity Assessment Plan (SD Pipeline-2021-02G Section III.G.2.a; C-ENERGY-R03); results feed the annual report due to TSA by 2026-11-20 (III.G.4). Annual internal IT audit |
| Results accepted | Chief Operating Officer, 2026-09-17; presented to the board audit committee the same day |

**SSI notice.** This summary is written so that it contains no Sensitive Security Information. The workpapers that map results to measures in the Cybersecurity Implementation Plan are SSI and are kept in the SSI repository under STD-10 (49 CFR Part 1520; SD 02G Section IV.B).

## 1. Scope and controls selected
Mid-Market tier scope: 25 to 40 controls. **34 controls, 253 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- test the TSA directive measures with gaps in the gap analysis (P03), so the results can be counted toward the one-third annual assessment minimum (SD 02G III.G.2.d);
- cover the control room management duties that depend on SCADA (49 CFR 192.631; C-ENERGY-R04);
- support SOC 2 readiness for the contract operations services (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | OT account lifecycle (gap 6); SD 02G III.C.4.b (G-022); R-021 | Focused | Focused (samples of 15 to 25) |
| AC-6, IA-5 | Privileged accounts and field device passwords (gap 1); SD 02G III.C.1.b, III.C.3 (G-017, G-019); R-002 (High), R-007 | Comprehensive | Comprehensive (all OT privileged accounts; 40 field devices) |
| AC-17, MA-4, SC-7 | Remote and vendor access, segmentation (gap 3); SD 02G II.A.4, III.B.1.b, III.B.2.a (G-004, G-011, G-013); R-002, R-003 | Comprehensive | Comprehensive (all 214 DMZ rules; 30 sessions; walkdown) |
| IA-2, IA-2(1) | Shared station logins and MFA (gap 1); SD 02G III.C.4 (G-020); R-006, R-018 | Focused | Focused (3 sites; 25 of 41 privileged accounts) |
| AU-2, AU-6, AU-11 | OT logging and retention (gap 10); SD 02G III.D.3 (G-034, G-035); R-034 | Focused | Focused |
| CM-3, CM-6 | Management of change and hardening; 192.631(c)(2), (f)(3) (G-091, G-104); R-022, R-027, R-040 | Focused | Focused (25 of 112 changes) |
| CM-8 | OT inventory (gap 4); SD 02G IV.C.2.a (G-060); R-031 | Focused | Focused (3 field sites) |
| CP-2, CP-4, CP-9, CP-10 | Recovery and shutdown decisions (gaps 7 and 8); SD 02G III.F.1, III.F.1.c (G-042, G-045); 192.631(c)(3), (c)(4); R-004 (High), R-010 (High), R-038 | Comprehensive | Comprehensive |
| IR-3, IR-4, IR-6, IR-8 | Incident response plan and reporting; SD 02G III.D.4, III.F (G-036, G-046); SD 01G II.C; R-001 (High), R-046 | Comprehensive (IR-4, IR-8); Focused (IR-3, IR-6) | Focused (10 of 31 incidents; 2 of 2 CISA reports) |
| MP-3 | SSI marking (gap 13); SD 02G IV.B; 49 CFR 1520.9(a), 1520.13 (G-058, G-117, G-118, G-120); R-029 | Focused | Comprehensive (all general file shares) |
| PE-3 | Control rooms and unmanned sites; R-016, R-043 | Basic | Focused (GCC, BCC, Compressor Station 4, 2 M&R stations) |
| RA-3, RA-5, SI-2 | Risk assessment and OT patching (gap 5); SD 02G III.E.2.b, III.E.3 (G-040, G-041); R-008, R-009 | Focused | Comprehensive for KEV (23 of 23) |
| SA-9, SR-6 | Third parties (gap 9); SD 02G II.A.4; R-012, R-023, R-048 | Focused | Focused (20 of 85 contracts; all 14 Tier 1 files) |
| SI-3, SI-4 | Malware protection and OT monitoring (gap 2); SD 02G III.D, III.D.2.b (G-024, G-031); R-005 (High), R-009 | Focused | Focused (4 monitored sites; 3 unmonitored stations by design review) |
| AT-3 | Role-based OT training; 192.631(h)(6) (G-113); R-039 | Basic | Focused |
| CA-2 | Cybersecurity Assessment Plan schedule (gap 11); SD 02G III.G.2.d (G-053); R-030 | Focused | Basic |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control that operates many times a year, 5 to 15 for small or periodic populations, and the whole population where it is small or the risk is Very High. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 74 | 25 | AC-2, PS-4 |
| Internal transfers (same period) | 41 | 15 | AC-2 |
| New OT accounts (same period) | 96 | 25 | AC-2 |
| Privileged accounts (OT domain, SCADA, gateway, identity provider) | 41 | 25 for the MFA test; all 41 for the rights review | IA-2(1), AC-6 |
| Field devices in the password reset register | about 310 | 40 (register); 10 (default-credential test: 6 cellular gateways, 4 RTUs) | IA-5 |
| Vendor and staff remote sessions through the gateway (Q2 2026) | about 640 | 30 | AC-17, MA-4 |
| SCADA and OT network changes (12 months) | 112 | 25 | CM-3 |
| DMZ firewall rules at the GCC and BCC | 214 | 214 | SC-7 |
| Open CISA KEV entries on OT components | 23 | 23 | RA-5, SI-2 |
| Vendor contracts (vendors with system or data access) | 85 | 20; all 14 Tier 1 assessment files | SA-9, SR-6 |
| Incidents (2025-2026) | 31 | 10 | IR-4 |
| CISA incident reports | 2 | 2 | IR-6 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Training records | 28 controllers; 14 SCADA and OT staff; 64 station technicians | 10; 8; 6 | AT-3 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6 |
| Sites for walkthroughs | GCC, BCC, 5 compressor stations, 46 M&R stations, 62 valve sites | GCC, BCC, Compressor Station 4, 2 M&R stations | PE-3, SC-7, CM-8, AC-17 |

## 3. Methods and objects
- **Examine:**
  - the 2024 policies and the 2026 policy set (P06), standards STD-01 to STD-10 (drafts where not issued)
  - the SSP (P02), the BIA (P05), the risk register (P01)
  - the three TSA plans (Cybersecurity Implementation Plan, Cybersecurity Incident Response Plan, Cybersecurity Assessment Plan), read in the SSI repository
  - the control room management manual, the emergency plan (192.615), the manual operation plan, and the BCC failover procedure
  - OT domain, SCADA, station HMI, gateway, and identity provider account exports
  - DMZ firewall rule exports, the OT inventory, the PLC backup register, and the offline media register
  - SIEM source lists and retention settings, MSSP monthly reports, and the incident register
  - vendor contracts, SOC 2 reports on file, and the OEM service agreement
- **Interview:**
  - Chief Operating Officer, vCISO, Security Manager, both OT Security Engineers, and the GRC lead
  - Director of Gas Control, 2 shift supervisors, and 3 controllers
  - SCADA and OT Engineering Manager and the IT Director
  - VP Operations and the Compressor Station 4 Supervisor
  - HR Director and the Supply Chain Manager
  - the MSSP service lead
  - 15 randomly selected staff on how to report an incident
- **Test:**
  - HMI sign-in tests at the GCC, the BCC, and Compressor Station 4
  - privileged logon tests for MFA on 25 sampled accounts
  - default-credential tests on 6 cellular gateways and 4 RTUs (read-only login attempts)
  - an inbound connection test from the business network to the SCADA network (expected to be blocked)
  - a network walkdown at Compressor Station 4, tracing every cable and radio from the station network to its endpoint
  - an EICAR test file on 2 control center HMIs (SCADA vendor approved) and 5 business endpoints
  - a simulated new-device alert at the BCC to test MSSP escalation
  - a restore of one SCADA configuration file from backup to a test server

## 4. Rules of engagement
- **Safety first.** No test could change the state of the pipeline. The Director of Gas Control approved each OT test in advance, the controller on duty was told before and after each one, and either could stop a test at any time.
- **No active scanning in OT** (STD-09). OT evidence came from configuration exports, passive sensor data, and hands-on checks by company staff. Default-credential tests were single read-only login attempts made by an OT Security Engineer with a field technician present. HMI tests used consoles not in active control.
- **SSI and Restricted data.** Screenshots of OT configurations were redacted. Workpapers with SSI were marked and stored in the SSI repository, not in the firm's general workpaper system.
- **Stop-and-notify rule:** any condition that could affect safe operation or give an outsider a path into OT is reported to the Security Manager and the Director of Gas Control the same day. **Used once:** during the Compressor Station 4 walkdown on 2026-08-12, the assessors found an OEM cellular modem connected to a unit control panel, outside the DMZ and not listed in the Cybersecurity Implementation Plan. The company disconnected it on 2026-08-13, logged it as P01 R-003 on 2026-08-14, and opened POAM-003. The Security Manager assessed whether it was a reportable cybersecurity incident under SD 01G Section II.C; no evidence of unauthorized access was found in the modem logs the OEM provided, and the decision and reasons were recorded in the incident register.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 191 |
| Other than satisfied | 62 |
| **Total** | **253** |

Other than satisfied statements by risk: 6 Very High, 19 High, 29 Moderate, and 8 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 20 | 6 | High | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 3 | 1 | Very High | POAM-003 |
| AT-3 | 7 | 2 | Low | POAM-015 |
| AU-2 | 4 | 2 | Moderate | POAM-005 |
| AU-6 | 2 | 1 | Moderate | POAM-005 |
| AU-11 | 0 | 1 | Moderate | POAM-005 |
| CA-2 | 10 | 1 | Moderate | POAM-016 |
| CM-3 | 7 | 3 | Moderate | POAM-006 |
| CM-6 | 4 | 2 | Moderate | POAM-006 |
| CM-8 | 3 | 3 | High | POAM-007 |
| CP-2 | 19 | 5 | High | POAM-008, POAM-009 |
| CP-4 | 3 | 2 | High | POAM-009 |
| CP-9 | 5 | 1 | High | POAM-009 |
| CP-10 | 0 | 2 | High | POAM-009 |
| IA-2 | 0 | 2 | High | POAM-004 |
| IA-2(1) | 0 | 1 | Moderate | POAM-004 |
| IA-5 | 8 | 2 | High | POAM-004 |
| IR-3 | 1 | 0 | n/a | n/a |
| IR-4 | 10 | 3 | High | POAM-008, POAM-010 |
| IR-6 | 2 | 0 | n/a | n/a |
| IR-8 | 14 | 3 | High | POAM-008 |
| MA-4 | 4 | 4 | Very High | POAM-003 |
| MP-3 | 0 | 2 | Moderate | POAM-011 |
| PE-3 | 11 | 1 | Low | POAM-017 |
| PS-4 | 4 | 1 | Moderate | POAM-001 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 8 | 1 | High | POAM-012 |
| SA-9 | 4 | 2 | Moderate | POAM-013 |
| SC-7 | 5 | 1 | Very High | POAM-003 |
| SI-2 | 8 | 2 | High | POAM-012 |
| SI-3 | 7 | 1 | Moderate | POAM-014 |
| SI-4 | 10 | 2 | High | POAM-014 |
| SR-6 | 0 | 1 | Moderate | POAM-013 |

**Fully satisfied (3 controls):** IR-3, IR-6, RA-3. The annual exercise met the directive's test of two plan objectives, both CISA reports were filed within 72 hours with the required content (the one late supplemental update found in P03 is tracked in POAM-020), and the risk assessment method and approvals are sound.

**Fully other than satisfied (7 controls):** AC-6, AU-11, CP-10, IA-2, IA-2(1), MP-3, SR-6.

**Themes:**
1. **The core is strong; the edges are not.** Segmentation at both DMZs, the remote access gateway with approvals and recordings, individual logins at the control centers, and MSSP escalation all worked. The failures cluster at Compressor Stations 2, 4, and 5, the field devices, and the OEM (AC-17, MA-4, SC-7, IA-2, IA-5, SI-4).
2. **Recovery and shutdown decisions are not proven** (CP-2, CP-4, CP-10, IR-4). BCC failover works, but a full SCADA rebuild, PLC logic restore, and live IT/OT isolation have not been demonstrated, and the plans do not say when to isolate, run manually, or shut down.
3. **Regulatory hygiene drifts without standards** (AU-11, CA-2, MP-3, SA-9). The intent is in policy, but the measurable rules (STD-02, STD-03, STD-10) were not issued.

**POA&M:** 31 controls had at least one Other than satisfied statement. They map to 17 POA&M items (POAM-001 to POAM-017), because related controls share an item. Three more items come from the gap analysis and the AI assessment (POAM-018 TSA plan amendments and milestones, POAM-019 AI governance, POAM-020 Cybersecurity Coordinator reachability and CISA supplemental reports). The total is 20 items: 1 Very High, 10 High, 7 Moderate, and 2 Low. See `poam.csv`.

**Use in the TSA annual report.** The GRC lead maps each tested statement to the Cybersecurity Implementation Plan measures it evidences, in the SSI workpapers, by 2026-10-31 (POAM-016). The annual report to TSA lists the methods used (examine, interview, test) and these results (SD 02G III.G.2.e).

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan, rules of engagement, and sample requests issued; OT test list approved by the Director of Gas Control |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | Site walkthroughs and technical tests (Compressor Station 4 and 2 M&R stations on 2026-08-12) |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M accepted by the COO and presented to the audit committee |
| 2026-10-31 | Results mapped to Cybersecurity Implementation Plan measures (POAM-016) |
| 2026-11-20 | Cybersecurity Assessment Plan update and annual report submitted to TSA |

Deliverables: this plan and summary; `assessment-results.csv` (253 rows); `poam.csv` (20 items).

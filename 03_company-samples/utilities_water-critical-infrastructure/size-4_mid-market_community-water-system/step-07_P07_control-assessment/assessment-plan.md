# Security Assessment Plan and Summary: Cris Santos Company | Water and Wastewater Systems | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed investor-owned water utility) |
| System assessed | Integrated Water Operations SCADA (IWOS, SYS-01 to SYS-06), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Water and Wastewater Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, and 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control. The Security Manager arranged access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (site visits 2026-08-11 to 2026-08-14) |
| Also serves | Evidence for the cyber element of the 3 RRA addenda (42 U.S.C. 300i-2(a)(1)(A)(ii)); annual internal IT and OT audit |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 247 determination statements.** Controls were selected because they:
- address the High risks in the risk register (P01), all of which sit in or next to the IWOS;
- test the cyber element of the RRAs and the ERP procedures (P03 G-004, G-013 to G-016, and benchmark rows G-021 to G-050);
- cover the engineered safeguards that the risk ratings depend on (SC-24);
- support inherited-control reliance and SOC 2 readiness for Utility Services (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-17, MA-4 | Unmanaged remote paths; R-001, R-002 (High); G-030, G-031 | Comprehensive | Comprehensive (every remote path into the IWOS) |
| AC-4, SC-7 | Tunnels, dual-homed historian, exposed modems; R-003, R-004, R-007 | Comprehensive | Comprehensive (all 4 major plants and 25 modems) |
| AC-2, IA-2, PS-4 | Shared logins and leavers; R-010, R-033; G-029 | Focused | Focused (samples of 25) |
| AC-6, IA-2(1), IA-5 | Privilege and credentials; R-011, R-013 | Focused | Focused (25 privileged accounts; 21 devices) |
| AT-3 | Operator training; G-034 | Basic | Focused (20 of 162) |
| AU-2, AU-6, SI-4 | OT monitoring and escalation; R-012, R-053 (High); G-039, G-042, G-044 | Focused | Comprehensive (all sites) |
| CA-3, SA-9, SR-6 | Integrator B and interconnections; R-013, R-014; G-023, G-024 | Focused | Comprehensive (14 OT vendors) |
| CM-2, CM-5, CM-6, CM-7, CM-8 | Baselines, PLC modes, hardening, inventory; R-009, R-015, R-018; G-025, G-037 | Focused | Focused (4 major plants and 3 of 8 small systems) |
| CP-2, CP-4, CP-9, CP-10 | Recovery and ERP procedures; R-008, R-019 (High); G-013 to G-016, G-036, G-048 | Comprehensive | Comprehensive (3 covered systems) |
| IR-4, IR-6, IR-8 | OT incident capability; R-026; G-045 | Focused | Focused |
| PE-3 | Remote site physical security; R-051 | Basic | Focused (4 major plants, the ROC, 3 small systems) |
| RA-3, RA-5, SI-2 | RRA quality, vulnerabilities, patching; R-016, R-017, R-025 | Focused | Focused |
| SC-24 | Engineered safeguards that the P01 ratings rely on | Comprehensive | Comprehensive (4 of 4 major plants) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items. Samples were chosen at random from populations extracted in the assessors' presence. OT samples were chosen to include every platform (Regional platform A, Lakes platform B, Ridge legacy platform, small-system controllers).

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 51 | 25 | AC-2 |
| New OT accounts (Regional) | 20 | 20 | AC-2 |
| Privileged accounts (gateway, firewalls, cloud, SCADA servers) | 38 | 25 for MFA test; all 38 for rights review | IA-2(1), AC-6 |
| OT devices for credential tests | 116 controllers plus 25 modems | 12 small-system devices and 9 Lakes and Ridge PLCs | IA-5 |
| Gateway sessions (April to June 2026) | 412 | 25 | AC-17, MA-4 |
| OT alerts escalated by the MSSP (2026) | 10 | 10 | AU-6, SI-4 |
| Operators and ROC staff | 162 | 20 | AT-3 |
| OT vendors with remote access | 14 | 14 | SA-9, SR-6 |
| Incidents (2025-2026) | 31 | 8 | IR-4 |
| PLCs for key switch checks | 41 | 35 (32 at the 4 major plants, 3 at small systems) | CM-5 |
| Public modem addresses | 25 | 25 (external exposure scan) | CM-6, SC-7, RA-5 |
| Staff for reporting interviews | 600 | 15 across 5 sites | IR-6 |
| Sites for walkthroughs | 4 major plants, the ROC, 8 small systems | All 4 major plants, the ROC, 3 small systems | PE-3, SC-24, CM-8 |

## 3. Methods and objects
- **Examine:**
  - POL-01 to POL-05 (2024 versions and the 2026 drafts) and the STD-01, STD-02, and STD-06 drafts
  - the SSP draft and the 3 RRAs and ERPs
  - firewall, tunnel, gateway, identity provider, and HMI user exports
  - backup logs, patch records, vulnerability reports, the OT inventory
  - vendor contracts, the interconnection register, MSSP escalation records
  - the 2025 Regional rebuild test report and drill records
- **Interview:**
  - COO, vCISO, IT Director, Security Manager, and the OT security analyst
  - Director of Water Operations, the SCADA and Controls Engineering Manager, the ROC Supervisor
  - the 4 Plant Managers and their Chief Operators
  - the Emergency Management and Resilience Manager and the Water Quality and Compliance Manager
  - the MSSP service lead and an Integrator B technician
  - 15 randomly selected staff
- **Test:**
  - external exposure scan of all 25 modem addresses (2026-08-10)
  - reachability tests from the Ridge and Lakes control networks toward the Regional control network
  - MFA sign-in tests on 25 privileged accounts
  - default-credential tests on 21 OT devices
  - PLC key switch checks on 35 PLCs
  - functional checks of hardwired stroke limits and analyzer alarms at 4 plants
  - a simulated OT alert at WTP-R2 to time MSSP escalation to the ROC
  - a restore of one Regional PLC program from offline media to the engineering simulator
  - passive network capture at WTP-L1

## 4. Rules of engagement
- **No test may affect treatment.** All OT tests were passive or read-only, except the credential tests and the stroke-limit and alarm checks, which ran with the Chief Operator present, with the affected feed in local control, and with a rollback plan. No active scanning on control networks. No logic was downloaded to any PLC; the restore test used the engineering simulator.
- **Stop-and-notify** for any critical exposure, the same day, to the IT Director and the Director of Water Operations. **Used twice:**
  - 2026-08-10 and 2026-08-12: the exposure scan found 3 small-system modems with web administration reachable from the internet, and the credential test confirmed default credentials. The company changed the credentials on 2026-08-13 as an interim step. The move to the private carrier network is due 2026-10-15 (P01 R-004 updated 2026-08-14; POAM-002).
  - 2026-08-12: Integrator B's remote desktop agent on the Ridge engineering workstation was found running with an outbound relay connection. The Director of Water Operations required an operator to be present for any agent session until removal (POAM-001).
- Evidence containing network details was kept in the firm's encrypted workpaper system and classified Restricted under POL-04.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 137 |
| Other than satisfied | 110 |
| **Total** | **247** |

Other than satisfied statements by risk: 59 High, 48 Moderate, 3 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 16 | 10 | Moderate | POAM-003 |
| AC-4 | 0 | 1 | High | POAM-002 |
| AC-6 | 0 | 1 | Moderate | POAM-005 |
| AC-17 | 2 | 2 | High | POAM-001 |
| AT-3 | 6 | 3 | Moderate | POAM-012 |
| AU-2 | 3 | 3 | Moderate | POAM-008 |
| AU-6 | 1 | 2 | High | POAM-008 |
| CA-3 | 5 | 3 | Moderate | POAM-014 |
| CM-2 | 2 | 3 | Moderate | POAM-006 |
| CM-5 | 4 | 2 | High | POAM-006 |
| CM-6 | 2 | 4 | High | POAM-006 |
| CM-7 | 4 | 2 | Moderate | POAM-006 |
| CM-8 | 2 | 4 | Moderate | POAM-007 |
| CP-2 | 15 | 9 | High | POAM-010 |
| CP-4 | 3 | 2 | High | POAM-010 |
| CP-9 | 4 | 2 | High | POAM-009 |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2 | 0 | 2 | Moderate | POAM-003 |
| IA-2(1) | 0 | 1 | High | POAM-004 |
| IA-5 | 4 | 6 | High | POAM-004 |
| IR-4 | 7 | 6 | Moderate | POAM-011 |
| IR-6 | 2 | 0 | n/a | n/a |
| IR-8 | 13 | 4 | Moderate | POAM-011 |
| MA-4 | 1 | 7 | High | POAM-001 |
| PE-3 | 9 | 3 | Low | POAM-015 |
| PS-4 | 3 | 2 | Moderate | POAM-003 |
| RA-3 | 7 | 1 | Moderate | POAM-016 |
| RA-5 | 6 | 3 | High | POAM-013 |
| SA-9 | 2 | 4 | High | POAM-014 |
| SC-7 | 2 | 4 | High | POAM-002 |
| SC-24 | 1 | 0 | n/a | n/a |
| SI-2 | 6 | 4 | Moderate | POAM-013 |
| SI-4 | 5 | 7 | High | POAM-008 |
| SR-6 | 0 | 1 | High | POAM-014 |

**Fully satisfied (2 controls):** SC-24 (the hardwired stroke limits and analyzer alarms worked at all 4 major plants without SCADA) and IR-6 (14 of 15 staff knew how and when to report). The SC-24 result supports the P01 decision to rate no risk Very High.

**Fully other than satisfied (6 controls):** AC-4, AC-6, CP-10, IA-2, IA-2(1), and SR-6.

**Themes:**
1. **Two standards inside one system.** Almost every finding is the same pattern: the control works at the Regional System and is missing at Lakes, Ridge, or the small systems. The Regional design (OT DMZ, gateway, named accounts, offline backups, passive monitoring) is the template; the acquired systems have not been brought up to it.
2. **Remote access and integrator control are the largest exposure** (AC-17, MA-4, AC-6, SA-9, SR-6). One integrator holds standing, unrecorded, password-only access to a covered system and the only copies of its configuration.
3. **Recovery and detection stop at the Regional fence** (CP-9, CP-10, SI-4, AU-6). The company cannot yet prove it could detect an attack at Lakes or Ridge, or rebuild their SCADA within the 24-hour RTO.

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 16 POA&M items (POAM-001 to POAM-016), because related controls share an item. Eight more come from the SSP, the gap analysis, the BIA, and the AI assessment (POAM-017 to POAM-024). The total is 24 items: 12 High, 11 Moderate, and 1 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan, rules of engagement, and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 | External exposure scan |
| 2026-08-11 to 2026-08-14 | Site visits, walkthroughs, and OT tests |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (247 rows); `poam.csv` (24 items).

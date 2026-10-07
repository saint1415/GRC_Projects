# Security Assessment Plan and Summary: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed diversified precision-agriculture crop farm with a central packinghouse and a Grower Services unit) |
| System assessed | Farm Management and Irrigation Control Platform (FMICP, CSC-FMICP-01), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Agriculture, Forestry, Fishing and Hunting |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); NIST SP 800-82 Rev. 3 for OT test constraints |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, and 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control. The Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (site walkthroughs 2026-08-10 to 2026-08-13; OT testing on 2026-08-12, outside irrigation run times and packinghouse operations) |
| Also satisfies | Annual internal IT audit; CSF 2.0 ID.IM-01 (benchmark, P03); evidence for the SOC 2 readiness assessment (P09) |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **33 controls, 265 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the CSF 2.0 High-priority subcategories with gaps in the gap analysis (P03), especially OT;
- support the binding record rules (Produce Safety, H-2A, WPS) and the SOC 2 readiness of Grower Services (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-2, PS-4 | Shared crew logins and late removal of seasonal accounts; R-015 (High), R-016; 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1) | Focused | Focused (samples of 25) |
| AC-6, IA-2(1) | Privileged access outside the cloud; R-009 (High) | Comprehensive | Comprehensive (all 38 privileged accounts; MFA test on 25) |
| AC-17, MA-4 | Vendor remote access to SCADA; R-002 (High), R-001 (Very High) | Comprehensive | Comprehensive (all remote paths) |
| IA-5 | Default credentials on OT devices; R-018 | Focused | Focused (controller and modem samples) |
| AT-2 | Training for field roles; R-038 | Basic | Focused (15 interviews) |
| AU-2, AU-6, SI-4 | OT logging and monitoring; record edit review; R-021 (High), R-044 | Focused | Focused |
| CA-3, SA-9, SR-6 | Interconnections and vendors; R-014, R-027; CSF GV.SC-05, GV.SC-07 | Focused | Focused (20 of 110 vendor files) |
| CM-2, CM-6, CM-7 | Baselines and hardening; R-039, R-019 | Focused | Focused (10 servers) |
| CM-3, SA-11 | OT and settlement change control; secure development; R-006, R-012, R-045 | Focused | Focused |
| CM-8 | OT inventory; R-020; gap 2 | Focused | Focused (12 pump stations) |
| CP-2, CP-4, CP-9, CP-10 | Contingency, freeze protection, and recovery; R-001 (Very High), R-004, R-007, R-008 | Comprehensive | Comprehensive |
| IR-4, IR-8 | Incident capability for OT and business impacts; R-038 | Focused | Focused (10 of 22 incidents) |
| PE-3 | Physical access to field OT; CSF PR.AA-06 | Basic | Focused (12 of 54 pump stations) |
| RA-3, RA-5, SI-2, SI-3 | Risk assessment, vulnerabilities, patching, malware; R-019, R-040 | Focused | Focused |
| SC-7 | Segmentation and the packinghouse controller rule; R-005, R-050 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control operating many times a year with moderate risk, and 5 to 12 items for weekly or monthly controls. Samples were drawn at random from populations extracted in the assessors' presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30), including 160 seasonal | 214 | 25 | AC-2, PS-4 |
| Transfers between farms or roles | 41 | 25 | AC-2 |
| New accounts | 388 H-2A arrivals plus about 60 staff | 25 | AC-2 |
| Privileged accounts (all administrative planes) | 38 | 25 for the MFA test; all 38 for the rights review | IA-2(1), AC-6 |
| Ripening room controllers / cold storage controllers / pivot modems | 12 / 1 / 46 | 3 / 1 / 10 (default-credential test) | IA-5 |
| Pump stations | 54 | 12 (Farms 1 and 2) | PE-3, CM-8, IA-5 |
| Endpoints for malware tests | 210 laptops and desktops; 20 line PCs | 5 laptops; 2 line PCs | SI-3 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| Vendor files | 110 | 20 | SA-9, CA-3 |
| Incidents (2025-07 to 2026-06) | 22 | 10 | IR-4 |
| Critical vulnerability findings (Q1-Q2 2026) | 50 | 50 | RA-5, SI-2 |
| Servers for configuration scan | 34 | 10 (including both SCADA servers) | CM-6 |
| IT changes / settlement service changes | 168 / 10 | 10 / 10 | CM-3 |
| SYS-01 tally edits (May 2026) | about 1,900 | 20 | AU-6 |
| Staff for training and reporting interviews | about 600 at peak | 15 (5 office, 5 crew leads, 5 Irrigation Technicians) | AT-2 |

## 3. Methods and objects
- **Examine:**
  - the 2024 policies and the 2026 drafts; the SSP draft; the BIA
  - identity provider, SYS-01, SCADA, ERP, and grower portal account exports
  - backup, patch, scan, EDR, and SIEM reports
  - the IT disaster recovery and incident response plans (2024) and the P08 runbook drafts
  - vendor contracts and SOC 2 reports; the contract register
  - change logs and the settlement service deployment history
  - OT inventory, PLC and HMI program inventory, and firewall rule exports
- **Interview:**
  - vCISO, Security Manager, both analysts, and the IT Director
  - Director of Irrigation and Water Resources, the Farm 2 Farm Manager, and 5 Irrigation Technicians
  - Packinghouse Manager and the refrigeration contractor's technician
  - Vice President of Grower Services, the Controller, and the development firm's lead
  - HR Director; the MSSP service lead; the SCADA integrator's project lead
  - 15 randomly selected staff
- **Test:**
  - MFA sign-in tests on 25 privileged accounts
  - default-credential tests on 3 ripening room controllers, the cold storage refrigeration controller, and 10 pivot modems (vendor-approved; Packinghouse Manager and Director of Irrigation present)
  - reachability test from the packinghouse office VLAN to the controller VLAN
  - passive network capture at the Farm 1 office and pump-station network
  - observation of an integrator support session started on request, to see whether it needed approval or raised an alert
  - test files on 5 laptops and 2 line PCs
  - a simulated impossible-travel sign-in to test MSSP escalation (2026-08-13)
  - restore of one farm data hub table from the backup account into the recovery network
  - benchmark configuration scans of 10 servers
  - trace of 20 tally edits in the SYS-01 audit trail

## 4. Rules of engagement
- **No testing that could disrupt irrigation, freeze protection, or packing.** OT tests ran on 2026-08-12 outside irrigation run times and packinghouse operations, with the control owner present. **No active scanning of PLCs, VFDs, or controllers** (SP 800-82 Rev. 3 section 6.1.3): network evidence came from passive capture and firewall exports. Credential tests used read-only sign-in, logged out immediately, and changed nothing.
- No personal data left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system.
- **Stop-and-notify rule:** any critical exposure is reported to the IT Director and the vCISO the same day. **Used once:** on 2026-08-12 the assessors reported default administrator credentials on the ripening room and refrigeration controllers, reachable from the packinghouse office VLAN. The company logged the finding as P01 R-050 on 2026-08-14 and set a fix date of 2026-10-15 (POAM-013, POAM-018).
- The 7 unexplained tally edits found in the AU-6 test were referred to the HR Director and the Farm Managers for review under the H-2A records process, not investigated by the assessors.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 134 |
| Other than satisfied | 131 |
| **Total** | **265** |

Other than satisfied statements by risk: 57 High, 72 Moderate, 2 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 17 | 9 | High | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 1 | 3 | High | POAM-003 |
| AT-2 | 8 | 2 | Moderate | POAM-004 |
| AU-2 | 1 | 5 | Moderate | POAM-020 |
| AU-6 | 2 | 1 | Moderate | POAM-005 |
| CA-3 | 1 | 7 | Moderate | POAM-016 |
| CM-2 | 2 | 3 | Moderate | POAM-006 |
| CM-3 | 4 | 6 | Moderate | POAM-007, POAM-017 |
| CM-6 | 2 | 4 | Moderate | POAM-006 |
| CM-7 | 3 | 3 | Moderate | POAM-006 |
| CM-8 | 2 | 4 | Moderate | POAM-008 |
| CP-2 | 10 | 14 | High | POAM-009, POAM-012 |
| CP-4 | 0 | 5 | High | POAM-011 |
| CP-9 | 2 | 4 | High | POAM-010 |
| CP-10 | 0 | 2 | High | POAM-011 |
| IA-2 | 1 | 1 | High | POAM-001 |
| IA-2(1) | 0 | 1 | High | POAM-002 |
| IA-5 | 7 | 3 | High | POAM-001, POAM-013 |
| IR-4 | 8 | 5 | Moderate | POAM-014 |
| IR-8 | 10 | 7 | Moderate | POAM-014 |
| MA-4 | 1 | 7 | High | POAM-003 |
| PE-3 | 8 | 4 | Moderate | POAM-015 |
| PS-4 | 2 | 3 | Moderate | POAM-001 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | Moderate | POAM-019 |
| SA-9 | 1 | 5 | Moderate | POAM-016 |
| SA-11 | 3 | 6 | Moderate | POAM-017 |
| SC-7 | 3 | 3 | High | POAM-018 |
| SI-2 | 7 | 3 | Moderate | POAM-019 |
| SI-3 | 6 | 2 | Low | POAM-019 |
| SI-4 | 8 | 4 | High | POAM-020 |
| SR-6 | 0 | 1 | Moderate | POAM-016 |

**Fully satisfied (1 control):** RA-3. The 2026 risk assessment follows SP 800-30 Rev. 1 and covers OT, Grower Services, and AI.

**Fully other than satisfied (5 controls):** AC-6, CP-4, CP-10, IA-2(1), and SR-6.

**Strengths confirmed by testing:** write-once cloud backups succeeded on 31 of 31 days and the test restore worked (CP-9); EDR quarantined test files on all 5 laptops within 5 minutes (SI-3); the MSSP escalated the simulated sign-in in 18 minutes against a 30-minute target (IR-4); 10 of 10 sampled IT changes were approved and documented (CM-3).

**Themes:**
1. **IT is protected and monitored; OT is not.** The OT findings repeat across families: vendor access (AC-17, MA-4), default credentials (IA-5), flat networks (SC-7), no logs or monitoring (AU-2, SI-4), no baselines or change control (CM-2, CM-3), and an incomplete inventory (CM-8).
2. **Recovery is unproven.** Cloud backups are strong, but SCADA and PLC recovery depends on the integrator, and nothing outside file services has been restore-tested (CP-4, CP-9, CP-10). Freeze protection has no written fallback (CP-2a.04).
3. **Records and settlements lack attribution and review.** Shared crew logins and unreviewed tally edits (AC-2, IA-2, AU-6), and settlement code changes without company approval (CM-3, SA-11), weaken the records that FDA, DOL, and the growers rely on.

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 20 POA&M items (POAM-001 to POAM-020), because related controls share an item. Four more items come from other deliverables: POAM-021 (unsupported HMIs, P02 and P01), POAM-022 (regulated records and retention, P03), POAM-023 (settlement processing integrity, P03 and P09), and POAM-024 (AI governance conditions, P10). The total is 24 items: 10 High and 14 Moderate. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan, rules of engagement, and sample requests issued; OT test window agreed with the Director of Irrigation and the Packinghouse Manager |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Site walkthroughs and technical tests (OT tests on 2026-08-12) |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (265 rows); `poam.csv` (24 items).

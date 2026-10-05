# Security Assessment Plan and Summary: Cris Santos Company | Dams | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (owner and operator of 4 FERC-licensed hydroelectric projects; NERC-registered GO and GOP) |
| System assessed | Hydro Control and Dam Monitoring System (HCDMS, SYS-01 to SYS-07), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Dams |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control. The OT Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-28 (site walkthroughs and tests 2026-08-10 to 2026-08-14) |
| Also satisfies | Annual internal IT audit; independent check behind Form 3 Q24b; input to the 2026 Annual Security Compliance Certification Letter |
| Results accepted | Chief Operating Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 240 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- test the Section 9 baseline and enhanced measures and the CIP-003-9 Attachment 1 sections where P03 found gaps;
- support the plan and schedule for Form 3 negative answers and the RMOS SOC 2 readiness work (P09).

| Control | Why selected (risk ID or requirement row) | Depth | Coverage |
|---|---|---|---|
| AC-17, AC-18, MA-4, IA-2(1) | Remote and vendor access; R-001 (Very High), R-012, R-041; G-058, G-092 | Comprehensive | Comprehensive (all remote paths at 5 sites) |
| AC-4, SC-7 | Segmentation and RMOS tunnels; R-002, R-004; G-056, G-086 | Comprehensive | Focused (60 of 1,140 rules; reachability tests) |
| AC-2, AC-3, IA-2, IA-5, PS-4 | Accounts and authenticators; R-006, R-028, R-045; G-059 | Focused | Focused (samples of 25) |
| AC-6 | Privileged access; R-044 | Focused | Comprehensive (all 29 plant hosts) |
| AT-3 | Role-based OT training; G-055 | Basic | Focused (20 interviews) |
| AU-2, AU-6, SI-4 | Monitoring; R-007; G-061 | Focused | Focused (all 5 sites) |
| CA-3, SA-9 | Interconnections and vendors; R-022 to R-024; G-048 | Focused | Comprehensive (14 vendors, 4 clients) |
| CM-3, CM-6, CM-8 | Change, configuration, inventory; R-040, R-041; G-042 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | Recovery; R-008, R-009; G-020, G-053 | Comprehensive | Comprehensive (47 controllers and HMIs) |
| IR-4, IR-6, IR-8 | Incident response, 12.10 link; R-015, R-016; G-074 | Focused | Basic |
| MP-7, PE-3 | Media and physical; G-062; CIP-003 Sec. 2 and 5 | Basic | Focused (all sites) |
| RA-5, SI-2, SA-22 | Vulnerabilities and legacy hosts; R-005; G-060 | Focused | Focused |
| SC-8 | ICCP protection; CIP-012-2 Part 1.1 | Basic | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control that operates many times a year with moderate risk; 5 to 13 items for weekly or monthly controls; whole populations where they are small or the risk is Very High. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls | Exceptions |
|---|---|---|---|---|
| SCADA domain leavers (2025-07-01 to 2026-06-30) | 61 | 25 | AC-2, PS-4 | 3 late |
| Jump host sessions (July 2026) | 212 | 25 | AC-17, MA-4 | 0 |
| Weekly vendor session reviews (2026 Q2) | 13 | 13 | AU-6 | 0 |
| Privileged jump host accounts | 15 | 15 (MFA test) | IA-2(1) | 0 |
| OT firewall rules (5 sites) | 1,140 | 60 | AC-4, SC-7 | 14 broader than documented need |
| OT changes (2026 Q2) | 88 | 20 | CM-3 | 4 OEM changes outside the board |
| Controllers and HMIs (backup completeness) | 47 | 47 | CP-9 | 28 incomplete |
| OT Windows hosts (configuration scan) | 45 | 8 | CM-6 | 4 at default settings |
| Field device credentials (gauge modems, panel modem, gate panel web interfaces) | 30 | 30 | IA-5 | 4 default passwords |
| High findings from the 2025 OT assessment | 14 | 14 | RA-5 | 6 open past 90 days |
| OT incident log entries (2025-2026) | 8 | 8 | IR-4 | 3 handled outside the process |
| ROC and plant staff (reporting awareness) | 270 | 20 | IR-6, AT-3 | 6 unaware |
| Keys in registers | 140 | 20 | PE-3 | 0 missing; 1 rekey overdue |
| Sites for walkthroughs | 5 | 5 (ROC and 4 projects) | PE-3, CM-8, MP-7, SC-7 | See results |

## 3. Methods and objects
- **Examine:**
  - SSP draft, OT contingency procedure, IR plan 2024, CIP-003 and CIP-012 plans
  - SCADA domain, HMI, and jump host exports; firewall rule exports from 5 sites
  - backup reports; vulnerability assessment report and tracker; change records
  - OT vendor and RMOS client contracts; BA/TOP operating agreement
  - Security Plans, EAPs, and the BWB Rapid Recovery sub-element
- **Interview:**
  - Vice President of Generation Operations, ROC Manager, 2 ROC shift supervisors, 4 Plant Managers
  - OT Security Manager and 2 OT security engineers; Manager of Controls Engineering
  - Chief Dam Safety Engineer; Corporate Security Manager; NERC Compliance Manager
  - IT Director; GRC Manager; HR Director; MSSP service lead
  - 20 randomly selected ROC and plant staff
- **Test:**
  - reachability test from a PNH engineering laptop toward BWB and CDS controllers (read-only, with controls engineering present)
  - test laptop connected to the CDS plant LAN for 3 hours to check detection
  - cellular signal survey at every gate and unit panel at the 4 projects
  - default credential checks on 30 field device interfaces
  - MFA tests on 15 privileged jump host accounts; sign-in tests on PNH and SGR HMIs
  - restore of one SCADA server image to the vendor test system
  - session disable test on a vendor jump host session (CIP-003 Section 6.2)

## 4. Rules of engagement
- **Safety first.** No active scanning of PLCs, governors, exciters, or gate controllers. Every test near controllers ran with the Plant Manager's approval, controls engineering present, and the affected gates and units in local control.
- No CEII or client data left company systems; workpapers stayed in the firm's encrypted system under a confidentiality agreement, and evidence containing CEII stayed in the restricted library.
- **Stop-and-notify rule: used once.** On 2026-08-12 the assessors found an undocumented cellular modem in the Sawgrass Run gate PLC panel, installed by the turbine controls OEM in 2023 for remote diagnostics, with a manufacturer default password. They told the OT Security Manager and the Vice President of Generation Operations the same day. The modem was disconnected on 2026-08-13, and the finding was logged in P01 (R-041) on 2026-08-14 and added to the facts as gap 13.
- No exploitation: findings were confirmed by observation and configuration review, not by using the access paths found.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 138 |
| Other than satisfied | 102 |
| **Total** | **240** |

Other than satisfied statements by risk: 6 Very High, 78 High, 17 Moderate, 1 Low.

| Control | Satisfied | Other than satisfied | Highest risk | POA&M |
|---|---|---|---|---|
| AC-2 | 18 | 8 | High | POAM-004 |
| AC-3 | 0 | 1 | High | POAM-004 |
| AC-4 | 0 | 1 | High | POAM-002 |
| AC-6 | 0 | 1 | Moderate | POAM-016 |
| AC-17 | 3 | 1 | Very High | POAM-001 |
| AC-18 | 3 | 1 | High | POAM-001 |
| AT-3 | 5 | 4 | Moderate | POAM-014 |
| AU-2 | 3 | 3 | High | POAM-005 |
| AU-6 | 2 | 1 | High | POAM-005 |
| CA-3 | 1 | 7 | High | POAM-009 |
| CM-3 | 7 | 3 | Moderate | POAM-013 |
| CM-6 | 2 | 4 | Moderate | POAM-013 |
| CM-8 | 2 | 4 | High | POAM-003 |
| CP-2 | 17 | 7 | High | POAM-007 |
| CP-4 | 2 | 3 | High | POAM-007 |
| CP-9 | 4 | 2 | High | POAM-007 |
| CP-10 | 0 | 2 | High | POAM-007 |
| IA-2 | 0 | 2 | High | POAM-004 |
| IA-2(1) | 0 | 1 | High | POAM-001 |
| IA-5 | 7 | 3 | High | POAM-004; POAM-012; POAM-016 |
| IR-4 | 7 | 6 | High | POAM-008 |
| IR-6 | 0 | 2 | High | POAM-008 |
| IR-8 | 12 | 5 | High | POAM-008 |
| MA-4 | 3 | 5 | Very High | POAM-001 |
| MP-7 | 1 | 1 | Moderate | POAM-015 |
| PE-3 | 11 | 1 | Low | POAM-017 |
| PS-4 | 3 | 2 | Moderate | POAM-004 |
| RA-5 | 6 | 3 | High | POAM-006 |
| SA-9 | 1 | 5 | High | POAM-009 |
| SA-22 | 1 | 1 | High | POAM-006 |
| SC-7 | 2 | 4 | High | POAM-002 |
| SC-8 | 1 | 0 | n/a | n/a |
| SI-2 | 7 | 3 | High | POAM-006 |
| SI-4 | 7 | 5 | High | POAM-005 |

**Fully satisfied (1 control):** SC-8 (ICCP, client tunnels, and microwave links are encrypted).

**Fully other than satisfied (7 controls):** AC-3, AC-4, AC-6, CP-10, IA-2, IA-2(1), IR-6.

**What works:** jump host sessions (all 25 sampled were approved, recorded, and reviewed), MFA on privileged jump host accounts, ROC SCADA role enforcement, the one-way cloud data path, physical security and key control, CIP-003 Sections 2, 5, and 6.1-6.2 evidence, and the BWB restore capability.

**Themes:**
1. **Paths around the front door.** The jump hosts work, but OEM VPNs, client tunnels, and a hidden modem go around them (AC-17, AC-18, MA-4, SC-7, AC-4).
2. **Program applied at the ROC and BWB, not yet at the other projects.** Monitoring, inventory, configuration, vulnerability management, training, and media controls stop at BWB (SI-4, CM-8, CM-6, RA-5, AT-3, MP-7).
3. **Recovery and incident response do not yet reach the dam safety side.** No proven recovery outside BWB and no link to the EAPs or 18 CFR 12.10 (CP-2, CP-10, IR-6, IR-8).

**POA&M:** 33 controls had at least one Other than satisfied statement. They map to 15 POA&M items, because related controls share an item. 9 more items come from the BIA, the gap analysis, and the AI and SOC 2 work (POAM-010, POAM-011, POAM-018, POAM-019, POAM-020, POAM-021, POAM-022, POAM-023, POAM-024). The total is 24 items: 1 Very High, 11 High, 10 Moderate, and 2 Low. See `poam.csv`. The Section 9 subset is the plan and schedule sent to the Regional Engineer on 2026-09-30.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | Site walkthroughs and technical tests (ROC 08-10, CDS 08-11, SGR 08-12, PNH 08-13, BWB 08-14) |
| 2026-08-17 to 2026-08-28 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |
| 2026-09-30 | Section 9 plan and schedule sent to the FERC Regional Engineer |

Deliverables: this plan and summary; `assessment-results.csv` (240 rows); `poam.csv` (24 items).

# Security Assessment Plan and Summary: Cris Santos Company | Government Services and Facilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed facilities support contractor operating government buildings) |
| System assessed | Integrated Facility Operations Platform (IFOP), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Government Services and Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 2 IT auditors) with an OT specialist subcontractor, reporting to the board audit committee. Neither firm designs or operates any assessed control. The Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (site tests 2026-08-10 to 2026-08-14, after hours where OT was touched) |
| Also satisfies | The state contract exhibit's annual independent assessment (SP 800-53 CA-2); the annual internal IT audit; the "equivalent independent assessment" County A and County B accept until a SOC 2 report exists |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 253 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the High and Very High gaps in the gap analysis (P03), including the FAR, CUI, and supply chain terms of the federal contract;
- support inherited-control reliance and SOC 2 readiness (P09).

| Control | Why selected (risk ID or requirement) | Depth | Coverage |
|---|---|---|---|
| AC-17, MA-4 | Subcontractor remote access; R-001 (Very High), R-010 | Comprehensive | Comprehensive (all 46 sites' remote paths; 4 site inspections) |
| IA-2, IA-2(1), IA-5 | Shared and default credentials; R-003, R-051 | Focused | Focused (all 61 privileged accounts; 60 controllers and 12 NVRs) |
| AC-2, AC-6, PS-4 | Access lifecycle in customer tenants; R-005, R-012; FAR 52.204-9(b) | Focused | Focused (samples of 25 and 15) |
| SC-7, CM-6, CM-8 | Segmentation, hardening, inventory; R-004, R-050, R-032 | Focused | Focused (5 sites tested) |
| SI-2, RA-5, SA-22 | Firmware, vulnerability management, unsupported components; R-015, R-016, R-047 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | Recovery and manual-mode operation; R-002, R-006, R-007, R-008, R-024, R-038 | Comprehensive | Comprehensive |
| AU-2, AU-6, SI-4 | OT monitoring; R-009 | Focused | Focused |
| IR-4, IR-6, IR-8 | Customer notice clocks; R-011 | Focused | Basic |
| SA-9, PS-7, SR-3 | Subcontractors; Section 889 screening; R-019, R-027, R-044; FAR 52.204-21(c), 52.204-25 | Focused | Comprehensive (all 7 OT subcontractors; all 9 FCI subcontracts) |
| CM-3, SI-7 | BAS change control and program integrity; R-017 | Focused | Focused |
| MP-4, AC-21 | CUI handling; R-025; 32 CFR 2002 | Basic | Focused |
| AT-3 | Role-based OT training; R-033 | Basic | Focused |
| PE-3 | Panel keys and ROC physical security | Basic | Focused |
| CA-3 | Customer interconnections; R-049, R-052 | Basic | Comprehensive (all 5 customer connections) |

GSA's own systems (SYS-10) and the school district's BAS server were not assessed. Their owners assess them.

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year at moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 15 items. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 41 | 15 | AC-2 |
| PIV holder departures | 31 | 25 | PS-4 |
| Privileged accounts (all admin planes) | 61 | 25 for MFA test; all 61 for rights review | IA-2(1), AC-6 |
| Field devices at County B and City sites | about 2,800 controllers; 21 NVRs | 60 controllers; 12 NVRs (default-credential test) | IA-5 |
| BAS program and door schedule changes (Q2 2026) | 390 | 25 | CM-3 |
| IT change tickets (Q2 2026) | 140 | 15 | CM-3 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Purchase orders for network, video, and OT equipment | about 450 | 25 | SR-3 |
| CUI drawing transfers (2026) | about 300 | 20 | MP-4, AC-21 |
| Incident records (2025-2026) | 37 | 10 | IR-4 |
| Critical vulnerability findings (Q1-Q2 2026) | 25 | 25 | RA-5, SI-2 |
| Laptops and cloud servers for patch status | 420 and 64 | 30 and 10 | SI-2 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6 |
| Sites for walkthroughs and technical tests | 46 | 5 (3 County B and City sites, 2 County A sites) plus 3 federal buildings for CUI | SC-7, CM-8, IA-5, MP-4 |

## 3. Methods and objects
- **Examine:**
  - POL-01 to POL-05, the standards index, the SSP, and the BIA
  - identity provider, cloud IAM, broker, tenant, and cluster account exports
  - edge firewall rules, VPN profiles, and route tables
  - CMMS asset lists and change tickets
  - backup, patch, scan, and EDR reports
  - contracts, subcontracts, and purchase records
  - the incident log, the 2025 tabletop report, and the P08 runbooks
- **Interview:**
  - vCISO, IT Director, Security Manager, OT Security Engineer
  - Director of Building Technology, Controls Engineering Manager, Security Systems Manager
  - VP Operations, ROC Manager, and the five program managers
  - Contracts Director, HR Director, General Counsel
  - the MSSP service lead
  - 15 randomly selected field staff and ROC operators
- **Test:**
  - connection tests from a technician laptop to confirm whether site networks are reachable without the broker
  - MFA sign-in tests on 25 sampled privileged accounts
  - read-only default-credential test on 60 controllers and 12 NVRs at 4 County B and City sites, after hours, with customer staff present
  - passive network discovery at 3 County A sites (listen-only)
  - traceroute from customer office network jacks to OT at 3 sites
  - inspection of 12 BAS panels at a City building
  - observed restore of the County B cluster into an isolated network
  - test download of a modified program to a bench controller in the company lab
  - simulated new-device connection at a sensor site to test detection

## 4. Rules of engagement
- No test could change a setpoint, schedule, door state, or program on a live customer system. Credential tests used read-only sessions, and customer facilities staff watched each one. The program integrity test used a bench controller in the company lab.
- No active vulnerability scans against field controllers. SP 800-82 Rev. 3 warns that active scanning can disrupt OT devices.
- Written customer approval was obtained before any test on a customer network.
- No cardholder data, face templates, or CUI left company systems. Screenshots were redacted, and evidence was kept in the firm's encrypted workpaper system.
- Stop-and-notify rule: any exposure needing action within 24 hours is reported the same day to the IT Director and the vCISO, and to the affected customer under its contract. **Used once:** on 2026-08-12 the OT specialist found a cellular modem in a City BAS panel that connected the OT network to an external carrier network. The City was notified the same day, the modem was powered off with City approval on 2026-08-13, and the company logged it as P01 R-050 on 2026-08-14 (removal and a sweep of all County B and City panels are due 2026-10-15, POAM-006).

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 133 |
| Other than satisfied | 120 |
| **Total** | **253** |

Other than satisfied statements by risk: 5 Very High, 44 High, 57 Moderate, 14 Low.

| Control | Satisfied | Other than satisfied | Highest risk | POA&M |
|---|---|---|---|---|
| AC-2 | 18 | 8 | High | POAM-003; POAM-004; POAM-005; POAM-011 |
| AC-6 | 0 | 1 | Moderate | POAM-005 |
| AC-17 | 2 | 2 | Very High | POAM-001 |
| AC-21 | 1 | 1 | Moderate | POAM-016 |
| AT-3 | 4 | 5 | Moderate | POAM-017 |
| AU-2 | 1 | 5 | High | POAM-011 |
| AU-6 | 1 | 2 | High | POAM-011 |
| CA-3 | 6 | 2 | Moderate | POAM-018 |
| CM-3 | 7 | 3 | Moderate | POAM-014 |
| CM-6 | 1 | 5 | High | POAM-015 |
| CM-8 | 2 | 4 | High | POAM-007 |
| CP-2 | 7 | 17 | High | POAM-009 |
| CP-4 | 3 | 2 | High | POAM-010 |
| CP-9 | 5 | 1 | Moderate | POAM-020 |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2 | 0 | 2 | High | POAM-003 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 6 | 4 | High | POAM-002 |
| IR-4 | 9 | 4 | Moderate | POAM-012 |
| IR-6 | 1 | 1 | Low | POAM-012 |
| IR-8 | 12 | 5 | Moderate | POAM-012 |
| MA-4 | 1 | 7 | Very High | POAM-001 |
| MP-4 | 3 | 2 | Moderate | POAM-016 |
| PE-3 | 9 | 3 | Low | POAM-019 |
| PS-4 | 3 | 2 | Moderate | POAM-004 |
| PS-7 | 2 | 3 | High | POAM-013 |
| RA-5 | 6 | 3 | High | POAM-008 |
| SA-9 | 3 | 3 | High | POAM-013 |
| SA-22 | 0 | 2 | High | POAM-008 |
| SC-7 | 3 | 3 | High | POAM-006; POAM-011 |
| SI-2 | 6 | 4 | High | POAM-008 |
| SI-4 | 7 | 5 | High | POAM-011 |
| SI-7 | 1 | 5 | Moderate | POAM-014 |
| SR-3 | 2 | 2 | High | POAM-013 |

**Fully satisfied (1 control):** IA-2(1). MFA was enforced on all 25 sampled privileged accounts, with phishing-resistant keys for cloud and broker administrators.

**Fully other than satisfied (4 controls):** AC-6, CP-10, IA-2, and SA-22.

**Largely satisfied:** IR-8 and IR-4 (the plan and runbooks exist; exercise and distribution are the gaps), CP-9 (all 30 sampled backup days succeeded; the program repository is the gap), CA-3 (the state agreement is sound; four agreements are missing), and AC-2 (identity provider lifecycle works; customer tenants are the gap).

**Themes:**
1. **The company protects its own IT well but not the edges it shares with others.** Subcontractor remote access, customer flat networks, and an unknown modem are the exposures (AC-17, MA-4, SC-7, SA-9).
2. **OT is under-instrumented.** Inventory, logging, and monitoring stop at 12 of 46 sites (CM-8, AU-2, SI-4).
3. **Recovery works on paper for IT, but not yet for the building platform.** The observed County B restore missed its RTO by 2 hours (CP-4, CP-10).

**New findings from testing (fed back to P01):**
- Cellular modem in a City BAS panel (SC-07c.); R-050 added 2026-08-14; POAM-006.
- Shared subcontractor administrator account in the County B tenant (IA-02[01]); R-051 added 2026-08-14; POAM-003.
- 41 devices on County A networks not in the CMMS (CM-08a.01); R-032 updated 2026-08-13; POAM-007.
- Default passwords on 14 of 60 controllers and 2 of 12 NVRs (IA-05e.); R-003 re-rated High 2026-08-13; POAM-002.
- County B cluster restore took 14 hours against a 12-hour RTO (CP-10[01]); POAM-010.

**POA&M:** 33 controls had at least one Other than satisfied statement. They map to 20 POA&M items (POAM-001 to POAM-020), because related controls share an item. Three more items come from other deliverables: POAM-021 AI governance (P10), POAM-022 elections warehouse cage remote unlock (P01 R-031), and POAM-023 standards issuance (P06). The total is 23 items: 1 Very High, 12 High, 9 Moderate, and 1 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued; customer test approvals requested |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | Site walkthroughs and technical tests |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee; SSP and POA&M to the state agency by 2026-10-31 |

Deliverables: this plan and summary; `assessment-results.csv` (253 rows); `poam.csv` (23 items).

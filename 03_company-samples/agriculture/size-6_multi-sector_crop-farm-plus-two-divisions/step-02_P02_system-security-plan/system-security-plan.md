# System Security Plan: Farm Management and Irrigation Control Platform (FMICP)

**Organization:** Cris Santos Company Holdings, Inc., Crop Farming division (focus division), inheriting group common controls from corporate shared services | **Tier:** Multi-Sector | **Vertical:** Agriculture, Forestry, Fishing and Hunting
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **OT guidance:** NIST SP 800-82 Rev. 3 (September 2023) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **FMICP**, the focus division's primary system, because it carries the group's top risks (P01 GR-01 and GR-02), it is where common control inheritance is weakest (scenario gap 2), and it feeds two other divisions (harvest lot data to Food Processing, payroll tally to group HR). Food Processing (SYS-D3) and Farm Supply (SYS-D4, SYS-D5) keep division SSPs that inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Farm Management and Irrigation Control Platform (**FMICP**), identifier CSCH-SYS-D1. It is SYS-D1 in `../00_company-facts.md`.

## 2. System Overview
The FMICP runs field, irrigation, harvest, and farm record work on about 240,000 farmed acres at 38 farm operations in 5 southeastern states. It supports:
- remote and scheduled control of about 1,150 center pivots, 410 well pumps, 6,800 drip-zone valves, and 96 fertigation injection systems;
- overhead freeze protection on about 4,200 acres of strawberries, run from ROC-1 in freeze season;
- piece-rate harvest tally and labor records for about 11,500 seasonal workers, including about 9,000 H-2A workers;
- Produce Safety records (21 CFR 112 Subpart O), pesticide application records, and harvest lot records sent to outside buyers and Food Processing;
- yield maps and the drone imagery used by the yield model (P10 AI-001).

About 2,600 named users (managers, agronomists, ROC staff, irrigation technicians, office staff) and about 3,400 harvest tablets use it, plus the irrigation integrator at the 14 farms acquired in 2024.

**Major components:**
- **FMIS tenant (vendor SaaS):** crop plans, field and pesticide application records, Produce Safety records, harvest tally, harvest lot records, yield maps, and the irrigation control module. The vendor's SOC 2 Type 2 report states an RTO of 8 hours and an RPO of 1 hour (reviewed in P09)
- **Regional irrigation operations centers ROC-1 to ROC-3:** SCADA servers, historians, and HMI workstations in an OT network at each center, staffed 24x7 in freeze season. ROC-1 serves the Florida farms, including all strawberries
- **Field OT at 38 farms:** pivot panels with cellular modems on a carrier private network, well pump drives, fertigation injection systems, drip-zone controllers, about 21,000 soil moisture probes, about 260 LoRaWAN gateways, 140 weather stations, and cooler temperature sensors at 22 farms. About 38,000 OT and IoT devices in total
- **Farm data hub (cloud provider A):** a historian that collects telemetry from ROC SCADA, syncs it to the FMIS, sends the nightly harvest lot file to Food Processing, and stages payroll tally exports for SYS-G4
- **Imagery store (cloud provider A):** drone orthomosaics for AI-001
- **Harvest tablets:** about 3,400 rugged tablets running the FMIS mobile app
- **Legacy farm operations directory:** an on-premises directory that predates SYS-G1. It authenticates the ROC SCADA servers and HMIs and the 2024 acquired farms' servers

Cloud components are described by service category and are vendor-agnostic (P04). OT components follow SP 800-82 Rev. 3.

## 3. Laws, Regulations, and Policies Affecting the System
Primary agricultural production has no binding federal cybersecurity rule, so the FMICP is measured against **NIST CSF 2.0** as a voluntary benchmark, with SP 800-82 Rev. 3 for OT (P03). Binding rules reach the records and data the system holds.

| ID | Requirement | Citation | How it applies to the FMICP |
|---|---|---|---|
| Benchmark | NIST Cybersecurity Framework 2.0 | NIST CSWP 29 (2024) | Voluntary benchmark for Crop Farming (P03 `gap-analysis.csv`) |
| Benchmark (OT) | Guide to Operational Technology Security | NIST SP 800-82 Rev. 3 | ROC SCADA and field OT; its Appendix F OT overlay tailors the baseline (section 6) |
| Binding | Produce Safety Rule, records | 21 CFR 112.161-112.167 | All 38 farms are covered farms (21 CFR 112.4(a)). Records kept in the FMIS must be created at the time of the activity, accurate, legible, indelible, and signed by the person who did the work (112.161(a)); kept 2 years (112.164(a)(1)); available within 24 hours if offsite (112.166(a)) |
| Binding | H-2A earnings records | 20 CFR 655.122(j)-(k) | Field tally and hours offered in the FMIS are part of each worker's earnings record; records kept safe and accessible (655.122(j)(2)) for 3 years after the certification (655.122(j)(4)) |
| Binding | Worker Protection Standard, application and hazard information | 40 CFR 170.311(b) | Pesticide application records in the FMIS feed the required display and must be retained 2 years after the restricted-entry interval expires (170.311(b)(6)) |
| Binding (state) | State data security and breach laws | Each state where affected individuals reside; Florida worked example Fla. Stat. 501.171 | Worker names with identifiers in tally and payroll exports; reasonable measures (501.171(2)) |
| Binding (group) | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 (N42-R07) | An FMICP incident may be material to the group (P08) |
| Contract | Buyer agreements | Contract terms | Notice within 24 hours of any event that could affect product safety, lot traceability, or committed volumes |
| Internal | Group policies POL-01 to POL-05 and the Crop Farming supplement | P06 | |

**Not applicable to the FMICP:**
- **N11-R01, the FSMA intentional adulteration rule (21 CFR Part 121):** it applies only to facilities required to register under FD&C Act section 415 (21 CFR 121.1), and farms do not register (21 CFR 1.226(b)). Each Crop Farming operation is a farm under 21 CFR 1.227. Part 121 does apply to the 11 Food Processing facilities (P03), which receive this system's harvest lot data.
- **Records access under 21 CFR Part 1, Subpart J** excludes farms (21 CFR 1.327(a)); Food Processing carries that duty for the lots it receives.
- **CIRCIA** (proposed 6 CFR Part 226): no final rule as of 2026-09-25; tracked only.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Crop Farming VP Irrigation and Field Technology (system owner) and the Group CISO on 2026-09-10, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions before the 2026-27 freeze season:** (1) integrator always-on remote access removed and replaced with group PAM sessions on request, by 2026-11-15 (POAM-001 milestone); (2) the farm data hub can no longer open connections into ROC SCADA, by 2026-11-30 (POAM-002 milestone); (3) the freeze-night manual procedure written and drilled at all ROC-1 farms, including the acquired farms, by 2026-11-15 (POAM-008 milestone).
- **Other conditions:** farm directory domain administrators brought under group PAM with MFA by 2026-12-31 (POAM-003); OT monitoring at all 38 farms by 2027-06-30 (POAM-006).
- **Reauthorization:** annually, or when the OT DMZ and ROC-1 standby are complete.

### 4.3 System Operational Status
Operational. **Major modifications planned:** OT DMZ and jump hosts (2026-12-31), segmentation of the 14 acquired farms (2027-03-31), warm standby SCADA for ROC-1 at ROC-2 (2027-06-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Crop Farming VP Irrigation and Field Technology | Accountable for the FMICP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Division risk acceptor | Crop Farming division president | Accepts Moderate risks |
| OT security | Crop Farming OT security manager | OT architecture, OT accounts, OT change control, OT monitoring with the SOC |
| Records owners | Crop Farming Director of Food Safety (Produce Safety, application, harvest lot records); Crop Farming labor compliance director (tally and H-2A records) | Record content, retention, and FDA and DOL requests |
| Division security and compliance lead | Crop Farming security and compliance lead | Division register, supplement, inheritance documentation |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group HR director (SYS-G4 and HR controls) | Operate inherited controls (`common-control-catalog.csv`) |
| External support | FMIS vendor; regional irrigation integrator (acquired farms) | Service operation; PLC and SCADA support |
| Independent assessor | Group internal audit with an independent OT assessment firm | Assesses common controls once and samples division controls (P07) |

**Where roles overlap:** at the 14 acquired farms the integrator designs, changes, and approves its own PLC changes (AC-5). Until POAM-011 closes, the ROC-2 engineering lead reviews every integrator change after the fact each week as a compensating control.

## 6. System Information Types and System Categorization
SP 800-60's catalog is built for federal missions and has no farm operations type, so information types below are author-defined following the SP 800-60 method; impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Irrigation and freeze protection control (schedules, setpoints, commands, PLC logic) | Low | **High** | Moderate | A malicious start can injure workers near pivots and pumps, and a disabled freeze start can destroy a large share of a strawberry crop worth about $310 million. Availability is Moderate only because crews can start systems by hand (P05 MTD 4 hours in freeze season) |
| Fertigation and chemigation control | Low | **High** | Low | A wrong injection rate can damage crops, contaminate water, or expose workers, and could affect produce that Food Processing and outside buyers receive. Stopping injection is safe (P05) |
| Harvest tally and labor records (H-2A earnings records) | Moderate | Moderate | Moderate | Names with piece-rate counts and hours offered for about 11,500 seasonal workers; errors lead to wage findings and payroll disputes |
| Produce Safety, pesticide application, and harvest lot records | Low | Moderate | Moderate | Records must be accurate and indelible (21 CFR 112.161(a)(3)) and traceable to lots shipped to buyers and Food Processing |
| Farm operational and yield data | Moderate | Moderate | Low | Commercially sensitive; yield estimates feed forward sales and financial reporting (P10) |
| Security information (OT accounts, directory, keys, network design) | Moderate | High | Moderate | Compromise of the farm operations directory gives control of every ROC |
| **FMICP category (high-water mark)** | **Moderate** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored with the **SP 800-82 Rev. 3 Appendix F OT overlay**. The plan documents **219 controls** in `control-implementation.csv`:
- 212 from the High baseline;
- 4 that the OT overlay adds (CP-12 safe mode, SC-41 port and I/O device access, SI-13 predictable failure prevention, SI-17 fail-safe procedures);
- 1 from the privacy baseline (PM-9) and 2 program management controls not in any baseline (PM-1, PM-2).

OT tailoring decisions (for example, HMIs that stay signed in and do not lock out operators, AC-2(5), AC-7, AC-11) are recorded with their compensating controls. Other High-baseline controls are fully inherited from the FMIS vendor or the cloud providers (evidenced by SOC 2 reports, P09) or tailored out in the group tailoring register (for example, IA-2(12), which concerns federal PIV credentials).

## 7. Authorization Boundary Description
- **Inside:** the FMIS tenant configuration and roles, ROC-1 to ROC-3 OT networks (SCADA servers, historians, HMIs, engineering workstations), field OT at 38 farms, the farm data hub and imagery store accounts in provider A, the harvest tablets, and the legacy farm operations directory.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC and OT monitoring, SYS-G3 landing zone and WAN, and SYS-G4 HR and payroll controls.
- **Outside, interconnected:** SYS-D2 (equipment telematics, GNSS, drones), SYS-D3 (Food Processing traceability, harvest lot file), SYS-G4 (payroll tally export), the FMIS vendor platform, the cellular carrier private network, and the integrator's own systems.

Diagrams are in P04 `cloud-architecture.md` (section 2.2, the FMICP boundary).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| FMIS vendor platform | Bidirectional | All FMIS records; irrigation commands from the FMIS module to ROC SCADA | Master agreement with security terms; SOC 2 Type 2 report (P09) |
| Irrigation integrator (acquired farms) | Inbound remote sessions | Full SCADA and PLC control | Time-and-materials agreement **without security terms** (POAM-012) |
| SYS-D3 Food Processing traceability | Outbound nightly file | Harvest lot records | Intercompany feed approval (2023) |
| SYS-G4 payroll | Outbound weekly | Payroll tally exports (staged on the farm data hub) | Group HR procedure |
| SYS-D2 equipment and drones | Inbound | As-applied maps, yield monitor data, drone orthomosaics | Dealer and drone software terms |
| Outside buyers | Outbound | Harvest lot and shipping records | Buyer agreements (24-hour notice term) |
| Carrier private network | Bidirectional | Pivot commands and status | Carrier contract |
| H-2A filing agent | Outbound (from SYS-G4, not the FMICP) | H-2A worker documents | Agent agreement; listed for completeness because tally feeds the earnings record |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| FMIS tenant and irrigation module | SaaS | FMIS vendor | Crop Farming VP Irrigation and Field Technology |
| ROC SCADA servers, historians, HMIs, engineering workstations | OT (on premises) | ROC-1, ROC-2, ROC-3 | Crop Farming OT security manager |
| Legacy farm operations directory (2 domain controllers per ROC) | On-premises directory | ROC-1 to ROC-3 | Crop Farming OT security manager |
| Pivot panels (about 1,150) with cellular modems | OT | 38 farms | Farm irrigation technicians |
| Well pump drives (about 410) and fertigation systems (96) | OT | 38 farms | Farm irrigation technicians |
| Drip-zone controllers (about 6,800), soil probes (about 21,000), LoRaWAN gateways (about 260), weather stations (140), cooler sensors (22 farms) | OT and IoT | 38 farms | Farm irrigation technicians; packing shed leads |
| Farm data hub (historian, integration jobs) | Cloud virtual machines and managed database (IaaS/PaaS) | Provider A | Crop Farming OT security manager |
| Imagery store | Object storage | Provider A | Crop Farming VP Agronomy |
| Harvest tablets (about 3,400) | Mobile endpoints | 38 farms | Crop Farming labor compliance director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (219 controls) and `common-control-catalog.csv` (118 group common controls).

| Status | Controls |
|---|---|
| Implemented | 86 |
| Partially implemented | 120 |
| Planned | 13 |
| Not applicable | 0 |
| **Total** | **219** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (SYS-G1 to SYS-G4, group functions, or the FMIS vendor) | 62 |
| Hybrid (group provides the mechanism; Crop Farming configures or operates part) | 56 |
| System-specific | 101 |

**The 120 partially implemented and 13 planned controls** show a division that inherits a mature corporate program for its IT but runs its OT largely on its own. They cluster in six places (examples; the CSV lists all):
- **Remote access and the boundary between the corporate cloud, ROCs, and acquired farms** (scenario gap 1): AC-4, AC-17, AC-17(1), AC-17(4), MA-4, AC-20, SC-7, SC-7(3), SC-7(5), SC-7(21), PL-8, IA-8, PS-6, PS-7, SA-4, SA-9.
- **Seasonal workforce identity** (gap 3): AC-2, AC-2(1), AC-2(3), AC-3, AC-6(7), AC-19, IA-2, IA-2(2), PS-4, AU-3.
- **Privileged and default credentials in OT:** AC-6, AC-6(5), IA-2(1), IA-5, AC-18, AC-18(1).
- **Inventory, vulnerability management, and monitoring of farm OT** (gap 2): CM-8, RA-5, SI-2, SI-3, SI-4, SI-4(4), AU-6, CA-2, CA-7, CA-8.
- **Integrity of control logic and setpoints:** CM-3, CM-4, CM-5, SI-7, SI-10, SC-24, CP-12, AC-5, SA-10, SA-11.
- **Recovery and fail-safe operation, including freeze nights:** CP-2, CP-3, CP-4, CP-6, CP-9, CP-9(1), CP-10, SI-17, SI-12.

The 13 planned controls are new capabilities with funded projects: AC-2(12), AC-6(3), AC-17(3), CM-3(2), CM-7(5), CP-7, IA-2(5), MA-3(2), SC-7(18), SI-6, SI-7(1), SR-8, SR-10.

### 10.2 Common control inheritance by division
`common-control-catalog.csv` lists 118 controls that corporate provides. Inheritance is **documented** for Food Processing (2025 matrix, including plant OT) and Farm Supply (PCI DSS responsibility matrix, 2026), and for this plan. For Crop Farming it is documented only for division IT: **96 of the 118 common controls have no documented inheritance for the Crop Farming OT estate** (scenario gap 2). In practice this means, for example, that the group SOC does not monitor 29 farms (SI-4), group vulnerability management does not scan farm OT (RA-5), and group PAM does not cover the farm operations directory (AC-6(5)), while division staff assumed all three were inherited. POAM-009 documents inheritance and the division's remaining responsibilities by 2026-12-31.

### 10.3 Control assessment status
Common controls were assessed once, and FMICP and division controls sampled, from 2026-07-01 to 2026-08-31 by group internal audit with the OT assessment firm. OT testing ran outside irrigation run windows. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Office, agronomy, and ROC staff** authenticate through SYS-G1 with MFA for the FMIS web console and cloud; **IT administrators** use phishing-resistant MFA and just-in-time PAM. This fits a High-integrity system.
- **Not acceptable, on the POA&M:** farm directory domain administrators without MFA or PAM (POAM-003); the integrator's shared account without MFA (POAM-001); shared crew logins on harvest tablets, which make tally and Produce Safety entries unattributable (POAM-005).
- **Accepted with compensation:** ROC HMIs use shift operator accounts that stay signed in, so alarms stay visible during freeze events. Compensation: badge-controlled control rooms, CCTV, and SCADA change logging under engineering accounts.
- **Crew leads** will use named accounts with a device PIN on managed tablets, which is proportionate for entering tally on a group-owned device.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud architecture and control map (P04), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness and FMIS vendor report review (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **FMICP:** Farm Management and Irrigation Control Platform
- **FMIS:** farm management information system (vendor SaaS)
- **HMI:** human-machine interface (SCADA operator workstation)
- **OT DMZ:** a network zone between OT and enterprise networks where all flows end, so no connection passes straight through
- **PAM:** privileged access management
- **PLC:** programmable logic controller
- **ROC:** regional irrigation operations center
- **SCADA:** supervisory control and data acquisition

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Crop Farming OT security manager |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Group CISO |

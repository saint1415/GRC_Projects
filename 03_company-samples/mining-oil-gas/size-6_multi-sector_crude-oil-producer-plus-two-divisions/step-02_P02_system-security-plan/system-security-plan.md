# System Security Plan: Field SCADA and Production Accounting System (FSPA)

**Organization:** Cris Santos Company Holdings, Inc., Crude Oil Production division (inherits common controls from corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Mining, Quarrying, and Oil and Gas Extraction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), with OT guidance from NIST SP 800-82 Rev. 3 | **Version:** 1.0, 2026-09-17

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the focus division's primary system, the **Field SCADA and Production Accounting System**, because it carries most of the group's revenue (about $38.9 million per day), its alarms support safety and SPCC duties, and it sits at both ends of the top group risks (P01 GR-01 and GR-02): its OT DMZ is where the shared historian connector and the shared jump servers land. It inherits most IT controls from corporate (SYS-G1 to SYS-G3), which is how every division system is built. The other divisions keep their own system plans that inherit from the same common control catalog (`common-control-catalog.csv`): the Power Generation CIP-003-9 low impact cyber security plans and the Crude Logistics pipeline SCADA plan.

## 1. System Name and Identifier
Field SCADA and Production Accounting System (**FSPA**), identifier CSCH-PRD-FSPA. It covers SYS-P1, SYS-P2, SYS-P4, and the company's configuration of SYS-P3 in `../00_company-facts.md` section 3.

## 2. System Overview
The FSPA monitors and controls about 16,800 operated wells, 410 central tank batteries, 95 associated gas compression stations, and 38 water injection plants in the Permian Basin and Florida, and turns field measurements into allocated volumes, state production reports, and royalty payments. It supports:
- **Field operations:** about 140 production controllers at the Permian Integrated Operations Center (IOC), the Backup Control Center (BCC) at the Mid-Continent Operations Center, and the Florida regional control room monitor and remotely start, stop, and change the speed of wells, pumps, and compressors (P05 BP-PD01).
- **Safety and environmental alarming:** H2S alarms and tank high-level alarms, including the SPCC high-level sensor option at about 250 batteries (40 CFR 112.9(c)(4)(iv); P05 BP-PD02).
- **Water handling:** injection and disposal of about 1.4 million barrels of produced water per day (BP-PD03).
- **Volumes and revenue:** field data capture on tablets, the volume integration service, and the hydrocarbon accounting and revenue distribution SaaS for about 190,000 royalty owners (BP-PD04, BP-PD05).

**Major components:**
- **SCADA servers and historians** (hot standby pairs at the IOC and BCC; a smaller server set at the Florida control room)
- **HMIs and engineering workstations** at the three control rooms
- **OT DMZ** at the IOC and BCC: historian broker, patch and antivirus relay, the landing point for PAM sessions
- **Field control devices:** about 38,000 RTUs, PLCs, rod pump controllers, ESP variable speed drives, and flow computers
- **Field communications:** private LTE (core at the IOC), licensed radio, and about 9,000 cellular modems
- **FSPA cloud workloads** in provider A: field data capture app back end, volume integration service, and the historian replica feed to SYS-G6
- **Hydrocarbon accounting SaaS configuration:** roles, interfaces, and owner payment settings (the service itself is the vendor's)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the FSPA |
|---|---|---|---|
| N21-BM | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary benchmark) | NIST CSWP 29; NIST SP 800-82 Rev. 3 | The Production division's primary benchmark (P03). Each control row names the SP 800-82 Rev. 3 section used |
| EPA SPCC | Oil production facility container rule | 40 CFR 112.9(c)(4)(iv) | About 250 batteries meet the overfill rule with high-level sensors that "generate and transmit an alarm signal to the computer", so FSPA alarming is part of SPCC compliance |
| EPA discharge notice | Notice of oil discharges | 40 CFR 110.6 | A discharge that may be harmful (40 CFR 110.3) must be reported to the National Response Center immediately; FSPA alarms are often the first sign |
| State breach laws | Each state where affected royalty owners and employees reside (Florida worked example: Fla. Stat. 501.171) | Fla. Stat. 501.171(2) to (6) | Royalty owner Social Security or taxpayer numbers and bank accounts in SYS-P3 and its exports |
| N48-49-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | An FSPA incident may be material to the group (P08) |
| N21-R03 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | Tracked only. Not in effect; if finalized as proposed the group would be covered because it exceeds the SBA size standard |
| Internal | Group policies POL-01 to POL-05 and the Production supplement | P06 | |

**Not applicable** (P03 section 1): PHMSA Part 195, because flow lines and production facility piping are excepted (195.1(b)(8)) and the FSPA control rooms are not pipeline control rooms (the Crude Logistics PCC is); USCG 33 CFR Part 101 Subpart F (no MTSA or OCS facilities); TSA pipeline Security Directives (no TSA notice); NERC CIP (no BES Cyber Systems in Production).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Production Vice President of Operations Technology (system owner) and the Group CISO on 2026-09-17, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-17, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks), with the Production division president.
- **Conditions:** (1) remove write rights from the SYS-G6 historian service account by 2026-10-31 and replace the connector by 2027-03-31 (POAM-001); (2) remove jump server routes from the corporate virtual desktop pool by 2026-11-15 and split the jump servers by division by 2026-12-31 (POAM-002); (3) no model or analytics service may write setpoints to field devices without Group AI council approval and a safety management of change review (POAM-021).
- **Reauthorization:** annually, or when the Mid-Continent legacy SCADA (SYS-P5) migrates into the boundary (due 2027-09-30).

### 4.3 System Operational Status
Operational. **Major modifications planned:** migration of SYS-P5 into SYS-P1 (2027-09-30) and replacement of licensed radio with private LTE (2027-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Production Vice President of Operations Technology | Accountable for the FSPA and this SSP; agrees to any risk decision affecting operations or safety |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Data owner, production and revenue data | Production Accounting Vice President | SYS-P3 configuration, owner data, volume integrity |
| OT security architecture | Group OT Security Director | OT DMZ standard, OT sensors, SOC OT desk |
| Process safety | Production HSE director | Safety review of any change that affects alarms, shutdowns, or setpoints |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples FSPA controls (P07) |
| Division compliance | Production security and compliance lead | Production register, supplement, and POA&M tracking |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1, which gives provisional impact levels for federal systems; the group adjusted them for its operations as the publication allows. Impact levels follow FIPS 199.

| Information type (SP 800-60 Vol. 2 Rev. 1) | Provisional (C, I, A) | Company rating (C, I, A) | Rationale |
|---|---|---|---|
| Energy Production (D.7.4): process data, setpoints, controller logic, alarms | Low, Low, Low | Low, **High**, **High** | Altered setpoints or suppressed H2S and tank alarms could cause injury or a release; about 520,000 barrels per day depend on it. Hardwired shutdowns limit but do not remove the worst case |
| Energy Supply (D.7.1): run tickets, allocated volumes, state production reports | Low, Moderate, Moderate | Low, **High**, Moderate | Wrong volumes misstate sales, royalties, and state reports across thousands of wells |
| Payments (C.3.2.5): royalty and partner distributions | Low, Moderate, Low | **High**, Moderate, Low | Aggregation: about 190,000 owners' taxpayer numbers and bank accounts in all 50 states; a disclosure would trigger notices in every state and an SEC materiality decision |
| Information security (keys, accounts, logs) | | High, High, Moderate | Compromise would open the OT DMZ and field devices |
| **FSPA category (high-water mark)** | | **High, High, High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored with the SP 800-82 Rev. 3 OT overlay (Appendix F). The plan documents **125 controls** in `control-implementation.csv`:
- 120 from the High baseline;
- 2 added for OT safety (CP-12 safe mode and SI-17 fail-safe procedures), because hardwired shutdowns and fail-safe field behavior are what cap the worst case;
- 3 program management controls not allocated to a baseline (PM-1, PM-2, PM-9).

Other High-baseline controls are either fully inherited from the cloud and SaaS providers (evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register. The OT overlay is applied where field equipment cannot support a control, for example lockout on controller console HMIs (AC-7, compensated by physical access control) and device-level authentication on legacy radio protocols (IA-3, compensated by network isolation).

CSF 2.0 subcategories in `control-implementation.csv` come from NIST's official CSF 2.0 to SP 800-53 crosswalk. For 13 controls that NIST does not map (for example AC-8, CP-12, PS-3, SI-17), the subcategory is an author mapping.

## 7. Authorization Boundary Description
- **Inside:** SYS-P1 (SCADA servers, historians, HMIs, and engineering workstations at the IOC, BCC, and Florida control room); SYS-P2 (field devices, private LTE core, radio network, cellular modems); the Production OT DMZs and IT/OT firewalls; the FSPA cloud workloads in provider A (SYS-P4 and the historian replica feed); and the company's configuration of SYS-P3.
- **Outside, inherited (common control providers):** SYS-G1 identity platform and PAM (including the shared OT support jump servers), SYS-G2 SOC, SIEM, EDR, and OT monitoring console, and the SYS-G3 landing zone, WAN, and backup vault.
- **Outside, interconnected:** SYS-G6 group data platform (historian replica and the connector into the OT DMZ); SYS-P5 Mid-Continent legacy SCADA (until migration); SYS-M2 and SYS-M3 (LACT data and run tickets from Crude Logistics); SYS-G4 ERP (work orders); the hydrocarbon accounting vendor's platform; carriers.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-G6 group data platform | Outbound historian replica; **inbound pull by one service account that can also write to the historian broker** | Process history | **None** (POAM-001, POAM-025) |
| SYS-G1 shared OT support jump servers | Inbound PAM sessions to the OT DMZ | Administrative sessions | Group OT access standard; **shared by three divisions** (POAM-002) |
| SYS-P5 Mid-Continent legacy SCADA | Bidirectional (historian and alarm forwarding to the IOC) | Process data and alarms | **None** (POAM-025); migration due 2027-09-30 |
| SYS-P3 hydrocarbon accounting SaaS | Outbound from the volume integration service | Daily allocated volumes, run tickets | SaaS agreement; vendor SOC 2 Type 2 |
| SYS-M2 and SYS-M3 (Crude Logistics) | Inbound | LACT custody volumes; electronic run tickets | Intercompany transportation and data agreement (2025) |
| SYS-G4 ERP | Bidirectional | Maintenance work orders | Internal |
| Third-party gas processor | Outbound (meter data from central facility outlets) | Gas volumes | Gas purchase contract |
| State oil and gas regulators | Outbound (through SYS-P3 reports) | Production reports | Filed by Production Accounting |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SCADA servers and historians | On-premises servers (hot standby) | IOC; BCC; Florida control room | Production Vice President of Operations Technology |
| HMIs and engineering workstations | Workstations (22 at the Florida control room on an unsupported OS, POAM-009) | Three control rooms | Production Vice President of Operations Technology |
| OT DMZ (historian broker, relays, PAM landing) | Servers and firewalls | IOC; BCC | Group OT Security Director |
| Field control devices (about 38,000) | RTUs, PLCs, rod pump controllers, VSDs, flow computers | Well pads, batteries, stations, plants | Production Vice President of Operations Technology |
| Private LTE core, radio network, cellular modems (about 9,000) | Communications | IOC; field | Production Vice President of Operations Technology |
| Field data capture back end and volume integration service | PaaS and containers | Provider A | Production Accounting Vice President |
| Field tablets (about 1,800) | Managed mobile devices | Field | Production Accounting Vice President |
| Hydrocarbon accounting configuration | SaaS tenant | Vendor | Production Accounting Vice President |

The full OT inventory is built from passive sensors and site surveys and is about 85% complete (POAM-005).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (125 controls) and `common-control-catalog.csv` (81 group common controls inherited by the FSPA, fully or as hybrids).

| Status | Controls |
|---|---|
| Implemented | 102 |
| Partially implemented | 21 |
| Planned | 2 |
| Not applicable | 0 |
| **Total** | **125** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, or group functions) | 60 |
| Hybrid (group or vendor provides the mechanism; the FSPA configures or operates part) | 23 |
| System-specific | 42 |

**The 21 partially implemented controls** cluster in four places:
- **The IT/OT seams** (scenario gap 1): AC-4, AC-6, AC-17, SC-7, CA-3.
- **Field device and OT hygiene:** AC-2, AC-18, IA-3, IA-5, CM-3, CM-7(5), CM-8, SA-22, RA-5, SI-2, SR-6.
- **Recovery of field devices:** CP-4, CP-9.
- **Monitoring and incident governance** (scenario gap 7): AU-6, IR-3, IR-6.

**The 2 planned controls** are CA-8 (an OT boundary penetration test in 2027-Q1, during a maintenance window) and SC-8(1) (cryptographic protection for the remaining licensed radio links, by 2027-12-31).

### 10.2 Common control inheritance by division
The common control catalog lists 81 controls provided by corporate. Inheritance is **documented for Production** and for **Power Generation** (2025 inheritance matrices; Power Generation maps them to its CIP-003-9 low impact plans) and for the FSPA (this plan). It is **not documented for Crude Logistics** (scenario gap 6). Until POAM-019 closes, Crude Logistics cannot show its shippers, its SOC 2 auditor (P09), or PHMSA and state inspectors which of its controls are met by group services, and P07 found CA-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and FSPA and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit, with OT tests at Permian field sites on 2026-08-13. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Business users** of SYS-P3 and SYS-P4 authenticate through SYS-G1 federated sign-in with MFA. **Administrators** of SCADA servers and the OT DMZ use phishing-resistant MFA and just-in-time PAM elevation through the jump servers.
- **Controllers** sign in to SCADA consoles with named local accounts tied to SYS-G1 identifiers, so control does not depend on SYS-G1 being available. The Florida control room still has 2 shared operator logins (POAM-008).
- **Field devices** authenticate to private LTE by SIM. Licensed radio and legacy protocols cannot authenticate devices; network isolation compensates (POAM-011).
- **Integrators and vendors** authenticate as named external identities in SYS-G1 before reaching PAM.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **BCC:** Backup Control Center (Mid-Continent Operations Center)
- **Common control:** a control provided once by corporate and inherited by several systems
- **FSPA:** Field SCADA and Production Accounting System
- **HMI:** human-machine interface
- **IOC:** Integrated Operations Center (Permian)
- **OT DMZ:** the buffer network between corporate IT and OT
- **PAM:** privileged access management
- **RTU, PLC:** remote terminal unit, programmable logic controller
- **SPCC:** Spill Prevention, Control, and Countermeasure (40 CFR Part 112)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Production Vice President of Operations Technology |
| 1.0 | 2026-09-17 | Approved with authorization conditions | Group CISO |

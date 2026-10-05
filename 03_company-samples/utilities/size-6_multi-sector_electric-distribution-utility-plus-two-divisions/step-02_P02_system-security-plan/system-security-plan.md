# System Security Plan: Distribution Operations Platform (DOP)

**Organization:** Cris Santos Company Holdings, Inc., Electric Utility division (Cris Santos Electric Company) | **Tier:** Multi-Sector | **Vertical:** Utilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the Electric Utility's **Distribution Operations Platform**, the registry's primary system ("Distribution SCADA and outage management system", which at this size is an advanced distribution management system). It is the system the BIA ranks highest after the TCC (P05 BP-EU02, BP-EU03), it carries two of the group's High risks (P01 GR-01, GR-02), and unlike the TCC it sits **outside NERC CIP scope**, so no external audit tests it. It inherits governance, personnel, monitoring, procurement, physical security, and remote access controls from corporate, which is why the group common control catalog (`common-control-catalog.csv`) is published with this plan. The TCC's medium impact BES Cyber Systems keep their own CIP program and evidence; Gas Production's field SCADA and Engineering Services' client project platform keep division plans that inherit from the same catalog.

## 1. System Name and Identifier
Distribution Operations Platform (**DOP**), identifier CSCH-EU-SYS-E1. SYS-E1 in `../00_company-facts.md`.

## 2. System Overview
The DOP monitors and controls the Electric Utility's distribution grid and runs outage restoration for about 2.4 million meters. From the Distribution Control Center (DCC) and the backup DCC, about 210 operators and supervisors switch 1,700 feeders and about 9,000 automated field devices, and dispatchers send crews during outages and storms.

**Major components:**
- **ADMS core:** distribution SCADA, distribution management applications (switching orders, fault location, isolation and restoration, volt/var control), and the outage management system (OMS), on primary and standby server clusters at the DCC and a warm standby cluster at the backup DCC
- **Operator consoles:** 64 consoles at the two DCCs, 22 of them on an operating system past vendor support
- **Front-end processors (8):** poll field devices by DNP3 over the field area network
- **Historian and OT DMZ:** historian replica, integration servers for AMI and CIS interfaces, SYS-G4 jump hosts, file transfer server
- **Field side:** gateways at the 446 distribution substations and the distribution side of the 74 transmission substations, field area network segments for distribution traffic, reclosers, switches, and capacitor and regulator controls
- **OMS mobile:** about 1,400 crew and troubleshooter tablets
- **OT domain:** a Windows domain for DOP users and hosts, separate from SYS-G1

No component runs in the public cloud. The outage map and analytics copies run on SYS-G3 outside this boundary (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the DOP |
|---|---|---|---|
| N22-R01 | NERC CIP Reliability Standards | 16 U.S.C. 824o; CIP-002-5.1a, CIP-003-9 | **Not a BES Cyber System.** The DOP monitors and controls distribution Facilities below 100 kV, and the DCC performs no RC, BA, TOP, or GOP function, so it is not a "Control Center" in the NERC Glossary. **But it reaches into CIP scope:** at the 74 transmission substations it polls gateways that are part of low impact BES Cyber Systems, so its traffic there must meet CIP-003-9 Attachment 1 Section 3.1, and vendor access to those substations through SYS-G4 must meet Section 6 (P03) |
| Secondary | NERC EOP-004-4; Form DOE-417 | EOP-004-4 R1-R2; Federal Energy Administration Act sec. 13(b) (Pub. L. 93-275) | A cyber event on the DOP that interrupts electrical system operations is a DOE-417 Emergency Alert (criterion 3, within 1 hour); one that could affect reliability is a Normal Report (criterion 11, within 6 hours). Loss of service to more than 50,000 customers for 1 hour or more is criterion 12 (P08) |
| Voluntary benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 | Group choice for OT outside CIP | The control baseline below and the P07 assessment |
| State | State breach notification laws (Fla. Stat. 501.171 worked example) | | OMS holds customer names, addresses, and phone numbers. These are not listed data elements on their own; the CIS (outside this boundary) holds the sensitive elements |
| SEC | Form 8-K Item 1.05; Reg S-K Item 106 | | A DOP incident with wide outages may be material to the group (P08) |
| Contracts | ADMS vendor contract (2019); intercompany services agreement with Engineering Services (2021) | | Neither has incident notice or security terms (POAM-011) |
| Internal | Group policies POL-01 to POL-05 and the Electric Utility supplement (P06) | | All components |

Not applicable: TSA pipeline directives (the Electric Utility operates no pipelines), NRC 10 CFR 73.54 (no reactors), SDWA section 1433 (no water system).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Electric Utility distribution operations director (system owner) and the Group CISO on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Electric Utility president and the Group CISO. High risks GR-01 and GR-02 are not accepted, because they can affect public and crew safety; they are under treatment with dated plans (P01), and the conditions below limit the exposure until treatment is complete.
- **Conditions:** (1) per-session approval by the DCC for every SYS-G4 session into the DOP by 2026-11-30, and no standing Engineering Services access by 2027-03-31 (POAM-001); (2) offline, immutable DOP backups and a full restore test at the backup DCC by 2026-12-31 (POAM-009); (3) no new interface between the DOP and the corporate network except through the OT DMZ (POAM-005).
- **Reauthorization:** annually, or when the DCC network sensors and firewall rebuild are complete.

### 4.3 System Operational Status
Operational. **Major modifications planned:** IT/OT firewall rebuild (due 2026-12-31), OT network sensors at both DCCs (due 2027-03-31), console replacement (due 2027-06-30), and hot standby at the backup DCC (due 2027-05-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Electric Utility distribution operations director | Accountable for the DOP and this SSP |
| Authorizing official equivalent | Electric Utility president with the Group CISO | Authorization decision; Moderate risk acceptance (division president) |
| System administrators | Electric Utility OT engineering manager and OT administrators | ADMS, OT domain, DMZ, backups |
| Operations lead | DCC shift supervisors | Operational incident command for DOP events |
| Compliance liaison | Electric Utility NERC compliance director | CIP-003-9 Sections 3.1 and 6 where the DOP touches low impact assets; DOE-417 and EOP-004 reporting |
| Common control providers | Group OT security director (SYS-G4), Group identity director (SYS-G1), Group SOC director (SYS-G2), group governance, HR, procurement, and physical security | Operate inherited controls (`common-control-catalog.csv`) |
| Supporting supplier (affiliate) | Engineering Services | Configuration changes, protection settings, and commissioning under the intercompany agreement; treated as a vendor |
| Independent assessor | Group internal audit | Assesses common controls once and samples DOP controls (P07) |

## 6. System Information Types and System Categorization
Information types follow NIST SP 800-60 Vol. 2 Rev. 1 where a close match exists and are defined by the group otherwise. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy supply: real-time distribution monitoring and control | Moderate | **High** | **High** | A false command can open feeders serving tens of thousands of customers or re-energize a line where crews work under a clearance. Loss of SCADA forces manual switching (P05 MTD 4 h) |
| Outage and restoration records (OMS) | Moderate | **High** | **High** | During storms, wrong or missing outage data misdirects crews and delays restoration for hundreds of thousands of customers |
| Customer contact and premise data (OMS) | Moderate | Moderate | Moderate | Names, addresses, and phone numbers for 2.4 million premises |
| Grid models, network diagrams, and security configuration | **High** | Moderate | Low | Useful to an attacker planning a grid attack; the group treats it as CEII-equivalent Restricted data (POL-04) |
| **DOP category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored with the OT guidance in SP 800-82 Rev. 3. The plan documents **137 controls** in `control-implementation.csv`:
- 135 from the High baseline;
- 2 program management controls not in any baseline (PM-1, PM-9), because the DOP relies on the group program.

Other High-baseline controls are recorded in the Electric Utility OT tailoring register as either covered by a documented base control or tailored out where they would harm safe operation (for example, account lock and session lock on operator consoles, compensated by physical access control to the operating floor, AC-7 and AC-11 notes).

## 7. Authorization Boundary Description
- **Inside:** the ADMS clusters at the DCC and backup DCC, 64 operator consoles, engineering workstations, the 8 front-end processors, the historian, the OT DMZ (historian replica, integration servers, SYS-G4 jump hosts for the DOP, file transfer server), the OT domain, distribution substation gateways, field area network segments for distribution traffic, distribution field devices, and OMS mobile tablets.
- **Outside, inherited (common control providers):** SYS-G4 gateway and policy engine, SYS-G1 (MFA for remote users), SYS-G2 (SOC, SIEM), group HR, procurement, physical security, and governance.
- **Outside, interconnected:** SYS-E2 (one-way data feed from the EMS), SYS-E3 low impact BES Cyber Systems at the 74 transmission substations (shared gateways), SYS-E4 AMI head-end, SYS-E5 CIS, SYS-G3 outage map, the corporate network.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-E2 EMS (TCC) | One-way inbound through a data diode | Transmission status at shared substations | Internal interconnection agreement (2023) |
| SYS-E3 low impact gateways at 74 transmission substations | Bidirectional (DNP3) | Distribution device status and commands | CIP-003-9 Section 3.1 access lists. **Rules allow any protocol from the 8 FEPs** (POAM-014) |
| SYS-E4 AMI head-end (vendor SaaS) | Inbound to OMS through the DMZ | Meter outage and restoration events | AMI contract; vendor SOC 2 Type 2 (P09) |
| SYS-E5 CIS (vendor SaaS) | Bidirectional through the DMZ | Customer and premise records; trouble calls | CIS contract; vendor SOC 2 Type 2 |
| SYS-G3 outage map | Outbound | Outage counts and estimated restoration times by area | Internal. **One interface bypasses the DMZ** (POAM-005) |
| SYS-G4 remote access | Inbound sessions to DMZ jump hosts | Vendor and engineer support | SYS-G4 policy. **Standing Engineering Services access; no per-session DCC approval** (POAM-001) |
| ADMS vendor | Remote support through SYS-G4; patches by file transfer | Support sessions, software updates | ADMS contract (2019). **No incident notice or vulnerability disclosure terms** (POAM-011) |
| Engineering Services | Remote sessions through SYS-G4; on-site laptops | Configuration changes, settings, commissioning | Intercompany agreement (2021). **No security schedule** (POAM-011) |

## 9. System Component Inventory
| Component | Type | Location | Owner |
|---|---|---|---|
| ADMS server clusters (primary, standby, warm standby) | OT servers | DCC; backup DCC | Electric Utility OT engineering manager |
| Operator consoles (64; 22 unsupported) | OT workstations | DCC; backup DCC | Electric Utility distribution operations director |
| Front-end processors (8) | OT servers | DCC; backup DCC | Electric Utility OT engineering manager |
| Historian and OT DMZ hosts | OT servers | DCC server room | Electric Utility OT engineering manager |
| IT/OT firewalls (2 pairs) | Network | DCC; backup DCC | Electric Utility OT engineering manager |
| Distribution substation gateways (446) | Field devices | Distribution substations | Electric Utility substation engineering manager |
| Field devices (about 9,000) | Reclosers, switches, capacitor and regulator controls | Feeders | Electric Utility substation engineering manager |
| Field area network (distribution segments) | Private LTE, fiber, legacy radio | Service territory | Electric Utility telecommunications manager |
| OMS mobile tablets (about 1,400) | Mobile endpoints | Crew vehicles | Electric Utility distribution operations director |

**Gap:** distribution substation gateways, radios, and some firmware versions are missing from the DOP inventory (CM-8, POAM-007).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (137 controls) and `common-control-catalog.csv` (85 group common controls).

| Status | Controls |
|---|---|
| Implemented | 78 |
| Partially implemented | 57 |
| Planned | 2 |
| Not applicable | 0 |
| **Total** | **137** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G4, or group functions) | 48 |
| Hybrid (group provides the mechanism; the DOP configures or operates part) | 30 |
| System-specific | 59 |

**The 57 partially implemented controls** cluster in five places:
- **Remote access and accounts** (scenario gap 1): AC-2, AC-2(1), AC-2(3), AC-2(12), AC-6, AC-6(5), AC-6(7), AC-17, AC-17(1), AC-17(4), MA-4, PS-7, IA-2(2), IA-3, IA-5.
- **Segmentation and boundary** (gap 2): AC-4, SC-7, SC-7(5), SC-7(21), SC-8, SC-8(1), CA-3, PL-8.
- **Monitoring and detection** (gap 2): AU-5(2), AU-6, AU-6(1), CA-7, SI-4, SI-4(2), SI-4(4), RA-5, IR-4(4).
- **Configuration, patching, and recovery:** CM-6, CM-7, CM-7(5), CM-8, SA-22, SI-2, SI-3, SI-7, MP-7, MA-3, CP-4, CP-6, CP-9, CP-9(1).
- **Supply chain, training, and response coordination** (gaps 4 and 9): SA-4, SA-9, SR-3, SR-6, SR-8, AT-2(3), AT-3, IR-3, IR-3(2), IR-6, IR-8.

The 2 planned controls are AU-6(3) and CM-8(3); both depend on the DCC network sensors (POAM-003, POAM-008).

### 10.2 Common control inheritance by division
The catalog lists 85 controls provided by corporate: the 78 the DOP inherits fully or in part, plus 7 that serve cloud and IT workloads only. Inheritance is **documented for the Electric Utility** (2025 inheritance matrix, which its CIP evidence also uses) and for the DOP (this plan). It is **not documented for Gas Production**, and only **partly documented for Engineering Services**, whose SOC 2 Type 1 system description names SYS-G1 to SYS-G3 but not SYS-G4, group HR, or procurement (scenario gap 7; POAM-017). P07 found CA-2 statements other than satisfied in both divisions for this reason.

### 10.3 Control assessment status
Group internal audit assessed the common controls once and sampled DOP controls from 2026-07-06 to 2026-08-28. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Remote users** (vendors, engineers, and administrators working off site) authenticate at the SYS-G4 gateway through SYS-G1 with MFA, then to the jump host with their OT domain account. This meets the High integrity need for the path itself. The weakness is **standing authorization**, not authentication (POAM-001).
- **Local administrators** use hardware tokens for privileged logons.
- **Operators** log on to consoles with a named account and password inside a badge-controlled operating floor. MFA for console logons is planned for 2027 (IA-2(2)). The group accepts this because the operating floor is physically restricted and staffed 24x7.
- **Field devices** authenticate to the private LTE network with certificates; DNP3 Secure Authentication covers about 40% of devices (IA-3).
- **No customers** access the DOP. They use the CIS portal and the outage map, which are outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); CIP-002 categorization record (2025-12-02); the Electric Utility low impact cyber security plan; the EOP-004-4 Operating Plan; DOP contingency plan (2026-04); group and division risk registers (P01); gap analyses and the regulation-by-division matrix (P03); cloud architecture and control map (P04); BIA (P05); group policies and division supplements (P06); assessment and POA&M (P07); incident response runbook and notification matrix (P08); SOC 2 readiness (P09); AI governance (P10).

## 13. Acronym List and Glossary
- **ADMS:** advanced distribution management system
- **BCSI:** BES Cyber System Information
- **BES:** Bulk Electric System
- **CEII:** Critical Energy/Electric Infrastructure Information (18 CFR 388.113)
- **Common control:** a control provided once by corporate and inherited by several systems
- **DCC:** Distribution Control Center
- **DMZ:** demilitarized zone, the buffer network between the corporate network and the DOP
- **DNP3:** Distributed Network Protocol, used to reach field devices
- **DOP:** Distribution Operations Platform
- **FEP:** front-end processor
- **OMS:** outage management system
- **TCC:** Transmission Control Center

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Electric Utility OT engineering manager |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Electric Utility distribution operations director; Group CISO |

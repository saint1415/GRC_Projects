# System Security Plan: Distribution Operations Platform (DOP)

**Organization:** Cris Santos Company, LLC (electric distribution utility) | **Tier:** Small | **Vertical:** Utilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Distribution Operations Platform (**DOP**), identifier CSC-SYS-001.

## 2. System Overview
The DOP monitors and controls the company's distribution grid and runs outage restoration. It serves about 72,000 meters from 22 substations. The 24x7 Distribution Control Center (DCC) at headquarters uses it to operate breakers, reclosers, and capacitor banks, and dispatchers use it to send crews during outages.

**Major components:**
- **SYS-01:** distribution SCADA (master station, 6 HMI consoles, historian, engineering workstation)
- **SYS-02:** outage management system (OMS) and GIS, run by the company in its cloud tenant (SYS-09)
- **SYS-03:** substation automation and field network (RTUs, gateways, reclosers, radio and cellular links)
- **SYS-04:** the low impact BES Cyber Systems: 115 kV line protection relays and gateways at Substation N and Substation E
- **SYS-11:** truck tablets running OMS mobile
- **SYS-12:** the OT DMZ (jump host, historian replica, OMS-SCADA integration server, file transfer server)

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the DOP |
|---|---|---|---|
| N22-R01 | NERC CIP Reliability Standards | 16 U.S.C. 824o; CIP-002-5.1a and CIP-003-9 (low impact) | Applies to SYS-04 only. The company is a registered Distribution Provider with low impact BES Cyber Systems at two substations (P03) |
| Secondary | NERC EOP-004-4 Event Reporting; Form DOE-417 | EOP-004-4 R1-R2; Federal Energy Administration Act sec. 13(b) (Pub. L. 93-275) | Event and incident reporting from the DCC (P08) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 | OMS customer contact data; the CIS is outside this boundary |
| Voluntary | NIST CSF 2.0 and SP 800-82 Rev. 3 (Guide to OT Security) | Benchmark | The SCADA, OMS, and field network outside CIP scope |
| Internal | Security policies POL-01 to POL-05; CIP low impact policy and cyber security plan | P06 | All components |

Not applicable:
- CIP-004 through CIP-014 and CIP-015 (future): these apply to high or medium impact BES Cyber Systems, Control Centers, or Transmission Owners. The company has none (P03).
- The distribution SCADA is not a BES Cyber System. A Distribution Provider is not one of the functions in the NERC "Control Center" definition, and DP systems outside CIP-003-9 section 4.2.1 are exempt under section 4.2.3.4.
- TSA pipeline directives, NRC 10 CFR 73.54, and SDWA 1433: the company has no pipelines, reactors, or water systems.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the President and CEO and the Vice President of Operations (system owner and CIP Senior Manager) on 2026-09-04.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The President and CEO accepted continued operation of the DOP on 2026-09-04, with the conditions in the P07 POA&M.
- The majority owner accepted the four High risks in P01 temporarily, with dated treatment plans.
### 4.3 System Operational Status
Operational. Major modifications planned: IT/OT firewall redesign (P01 R-002, due 2026-12-31), jump host rebuild with MFA and session control (R-001, due 2026-11-30), and HMI and historian upgrade (R-007, due 2027-03-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Vice President of Operations | Overall accountability for the DOP; CIP Senior Manager |
| Risk acceptor (authorizing official equivalent) | President and CEO; majority owner for High and Very High | Acceptance of residual risk |
| Information Security Lead | IT Manager | Security program for IT and OT; firewalls, identity, monitoring |
| System administrator | SCADA/OT Administrator | SCADA, OT domain, OT DMZ, backups |
| Operations lead | Manager of System Operations | DCC operation, operational incident command |
| Protection owner | Manager of Engineering and Protection | Relays, gateways at BES substations, substation physical access; CIP-002 R2.2 delegate |
| Compliance | NERC Compliance Coordinator | CIP and EOP-004 evidence, SERC submissions |
| Vendors | SCADA vendor; relay testing contractor; OMS software vendor | Support, patches, PRC-005 testing (external) |

## 6. System Information Types and System Categorization
Information types follow NIST SP 800-60 Vol. 2 Rev. 1 where a close match exists and are defined by the company otherwise. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy supply: real-time distribution monitoring and control | Moderate | **High** | **High** | A false or unauthorized command can open feeders serving thousands of customers or re-energize a line where crews work under a clearance. Loss of SCADA forces manual switching by crews (P05 MTD 4 h) |
| BES protection data: relay settings and access lists at Substation N and Substation E | Moderate | **High** | Moderate | Wrong settings can cause a misoperation of 115 kV line protection. CIP-011 information protection applies only to high and medium impact systems, but the company treats these files as Restricted (POL-04) |
| Outage and customer contact records (OMS) | Moderate | Moderate | Moderate | Names, addresses, and phone numbers; wrong data sends crews to the wrong place |
| Network diagrams and security configuration | Moderate | Moderate | Low | Useful to an attacker; not needed in real time |
| **DOP category (high-water mark)** | **Moderate** | **High** | **High** | |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored for a 250-person utility with the OT guidance and overlay in SP 800-82 Rev. 3. The plan documents 84 controls that carry the CIP-003-9 low impact requirements and the OT risks in P01 (see `control-implementation.csv`). Every other High-baseline control is treated as follows:
- **Inherited** from the cloud provider for the OMS workloads, as evidenced by its attestation reports (P04).
- **Tailored out**, as a recorded decision, where the control's purpose is federal-only or would harm safe operation. Two examples: PM-series program controls beyond PM-1, PM-2, and PM-9; and account and device lock on HMI operator consoles (AC-7 and AC-11 statements).

## 7. Authorization Boundary Description
The boundary contains company-managed OT components and the company's OMS and GIS workloads in the cloud tenant:
- **Inside:** the SCADA master (primary and standby), 6 HMIs, the historian, the engineering workstation, the OT DMZ (jump host, historian replica, integration server, file transfer server), RTUs and gateways at 22 substations, about 160 reclosers and capacitor controls, the 8 relays at Substation N and Substation E, field radios and cellular routers, the OMS and GIS workloads, and 110 truck tablets.
- **Outside (interconnected):** the corporate network and identity provider (SYS-07, SYS-10), the AMI head-end (SYS-05, vendor SaaS), the CIS (SYS-06, vendor SaaS), the cloud provider's infrastructure, the transmission owner's 115 kV facilities and its Energy Management System, and vendor networks that connect through the jump host.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Corporate network (SYS-10) | Bidirectional through the OT DMZ | Historian replica, OMS integration | Internal. **Legacy any rules bypass the DMZ (gap)** |
| AMI head-end (SYS-05) | Inbound to OMS | Meter outage and restoration events | AMI contract. **No security terms (gap)** |
| CIS (SYS-06) | Inbound to OMS | Customer and premise records, outage calls | CIS contract; vendor SOC 2 |
| Transmission owner | Voice and data per operating agreement | Switching coordination, 115 kV status | Interconnection and operating agreement |
| SCADA vendor | Inbound remote support through the jump host | Support sessions, patches | Support contract. **Shared standing account (gap)** |
| Relay testing contractor | Local laptop connections and remote sessions | Relay test files, settings | Service agreement. **No laptop or access requirements (gap)** |
| Weather data provider | Inbound to the analytics workspace | Forecasts (used by SYS-13, outside this boundary) | Subscription terms |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SCADA master (primary and standby servers) | OT server | DCC; backup DCC | SCADA/OT Administrator |
| HMI consoles (6), engineering workstation | OT workstation | DCC | Manager of System Operations |
| Historian | OT server (**unsupported OS, gap**) | DCC | SCADA/OT Administrator |
| Jump host, historian replica, integration server, file transfer server | OT DMZ servers | DCC server room | SCADA/OT Administrator |
| IT/OT firewall; substation routers | Network | DCC; 22 substations | IT Manager |
| RTUs and gateways (22 substations) | Field device | Substations | Manager of Engineering and Protection |
| 115 kV line protection relays (8) and gateways (2) | Low impact BES Cyber Systems | Substation N; Substation E | Manager of Engineering and Protection |
| Reclosers and capacitor controls (about 160) | Field device | Distribution feeders | Manager of Engineering and Protection |
| Licensed radios and private cellular routers | Field communications | 13 substations and feeder devices | Manager of Engineering and Protection |
| OMS and GIS | Cloud virtual machines and managed database | Cloud tenant | Manager of System Operations |
| Truck tablets (110) | Mobile endpoint | Crew trucks | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 84 controls:
- Implemented: 22
- Partially implemented: 51
- Planned: 11
- Not applicable: 0

Controls that carry a CIP-003-9 requirement cite it in the `regulatory_driver` column (for example, AC-17, MA-4, and SI-4 for Attachment 1 Section 6).

### 10.2 Control assessment status
Assessed 2026-08-10 to 2026-08-14. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Corporate and cloud users authenticate through the identity provider with a password and a second factor. Cloud administrators use phishing-resistant hardware keys. This fits the Moderate confidentiality of OMS data.

OT access is weaker than the High integrity rating requires. HMI operators use shared accounts, and vendor and engineer access to the jump host uses passwords without MFA. The company accepts this only until the dated fixes in POAM-001, POAM-002, and POAM-007. Target state: named OT accounts, and MFA on every remote path into the OT network.

Customers use the CIS vendor's portal, which is outside this boundary.

## 12. Referenced Artifacts
- Scenario facts (`../00_company-facts.md`)
- CIP-002 categorization record (2025-11-18), CIP low impact policy (2026-09-04), and the low impact cyber security plan
- EOP-004-4 event reporting Operating Plan
- BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10)

## 13. Acronym List and Glossary
- **BES:** Bulk Electric System
- **BES Cyber System:** one or more BES Cyber Assets grouped to perform reliability tasks (NERC Glossary)
- **DCC:** Distribution Control Center
- **DMZ:** demilitarized zone, a buffer network between the corporate and OT networks
- **DNP3:** Distributed Network Protocol, the SCADA protocol used to reach substations
- **DOP:** Distribution Operations Platform
- **DP:** Distribution Provider
- **HMI:** human-machine interface
- **OMS:** outage management system
- **OT:** operational technology
- **POA&M:** plan of action and milestones
- **RTU:** remote terminal unit

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial plan | IT Manager with the SCADA/OT Administrator |

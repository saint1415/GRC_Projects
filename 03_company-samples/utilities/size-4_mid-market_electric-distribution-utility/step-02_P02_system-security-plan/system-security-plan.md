# System Security Plan: Distribution Operations Platform (DOP)

**Organization:** Cris Santos Company, Inc. (investor-owned electric distribution utility, NERC-registered Distribution Provider) | **Tier:** Mid-Market | **Vertical:** Utilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Distribution Operations Platform (**DOP**), identifier CSC-DOP-01. The DOP is the company's major system: the registry's "distribution SCADA and outage management system", plus the substation and field network, the OT DMZ, the truck tablets, the ADMS FLISR pilot, and the low impact BES Cyber Systems at Substations N, E, L, and H.

## 2. System Overview
The DOP monitors and controls the company's distribution grid and runs outage restoration and switching. It serves about 265,000 meters from 74 substations (2025 peak 1,480 MW). The 24x7 Distribution Control Center (DCC) at headquarters, with the backup DCC at the West Operations Center, uses it to operate breakers, reclosers, and capacitor banks; dispatchers use it to send crews; shift supervisors use its switching and clearance module to protect crews working on de-energized lines. About 400 people use it: 28 system operators and dispatchers, 6 shift supervisors, the OT engineering team of 9, protection staff, about 330 field staff on 310 truck tablets, and 14 vendors with remote support paths.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Distribution SCADA: master station (primary at the DCC, hot standby at the backup DCC), 14 HMI consoles, historian, 2 engineering workstations; separate OT Windows domain | On-premises OT network |
| SYS-02 | Outage management system (OMS) and GIS, including the switching order and clearance module | Vendor software run by the company in the operations workloads account of SYS-09 (IaaS and managed database) |
| SYS-03 | Substation automation and field network: RTUs and gateways at 74 substations, about 1,900 field devices; company fiber to 40 substations, licensed radio and private LTE to 34 | On-premises and field |
| SYS-04 | Low impact BES Cyber Systems: 26 relays protecting 230 kV and 115 kV BES line terminals, and the access control gateway at each of Substations N, E, L, and H | Substations |
| SYS-11 | 310 rugged truck tablets (OMS mobile, switching orders, GIS maps) | Cellular to SYS-09 |
| SYS-12 | OT DMZ: 2 jump hosts, historian replica, OMS-SCADA integration server, file transfer server, patch staging server, OT sensor collector | On-premises at headquarters, replica at the West Operations Center |
| SYS-14 | ADMS FLISR pilot on 40 feeders | On-premises OT network |
| SYS-09 (part) | Operations workloads account of the cloud landing zone, with its share of the network hub, security and log archive, and backup accounts | Public cloud, vendor-agnostic (P04) |

The DOP interfaces with SYS-05 (AMI head-end), SYS-06 (CIS), and SYS-13 (security monitoring), which are outside the boundary (section 7).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the DOP |
|---|---|---|---|
| N22-R01 | NERC CIP Reliability Standards | 16 U.S.C. 824o; CIP-002-5.1a and CIP-003-9 (low impact) | Applies to SYS-04 only: the 26 relays at Substations N, E, L, and H are low impact BES Cyber Systems (criterion 3.6). The gateways carry the Attachment 1 Section 3.1 electronic access controls, and the jump hosts carry the Section 6 vendor remote access controls (P03) |
| N22-R01 (pending scope) | CIP-002-5.1a Attachment 1 criterion 2.10 | NERC CIP-002-5.1a | If the ADMS adaptive load-shedding module goes live as designed (2027-06), it would be a medium impact BES Cyber System, and CIP-004 to CIP-011 and CIP-013 would apply to it (gap 1; P03) |
| Secondary | NERC EOP-004-4 Event Reporting; Form DOE-417 | EOP-004-4 R1-R2; 15 U.S.C. 772(b) | Event and incident reporting from the DCC (P08) |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | OMS holds customer names, addresses, phone numbers, and premise locations; reasonable security measures (501.171(2)) and breach notice (P08) |
| Voluntary | NIST CSF 2.0 and SP 800-82 Rev. 3 (Guide to OT Security) | Benchmark | The SCADA, OMS, field network, and ADMS pilot, which CIP does not reach today |
| Contract | Transmission owner interconnection and operating agreements; SCADA and ADMS vendor contract | Contracts | Switching coordination, protection responsibilities, vendor support terms |
| Internal | Security policies POL-01 to POL-05 and supporting standards; CIP low impact policy (2026-02-26) and cyber security plan | P06 | Policy basis for every control |

Not applicable:
- **CIP-004 through CIP-011 and CIP-013** apply only to high or medium impact BES Cyber Systems. The company has none today (P03). See the pending scope row above.
- **The distribution SCADA is not a BES Cyber System.** A Distribution Provider is not one of the functions in the NERC "Control Center" definition, and DP systems outside Applicability section 4.2.1 are exempt (section 4.2.3.4).
- **CIP-012 and CIP-014** apply to other registered functions; **TSA pipeline directives, NRC 10 CFR 73.54, and SDWA 1433** do not apply (no pipelines, reactors, or water systems).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner and CIP Senior Manager) and the President and CEO on 2026-09-17, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the DOP accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** President and CEO for High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities). Very High risks are not accepted; R-001 runs under a 90-day CEO exception while its treatment is under way (P01).
- **Conditions:** (1) the SCADA shared administrator accounts are replaced by named, vaulted accounts by 2026-12-31 (POAM-001); (2) the 6 legacy IT/OT firewall rules are removed by 2026-11-30 (POAM-003); (3) no ADMS go-live decision is made before the board decision on the load-shedding design (2026-12-10); (4) the audit committee receives POA&M status each quarter; (5) re-decision by 2027-09-30 or after a major change.
### 4.3 System Operational Status
Operational. Major modifications planned:
- IT/OT firewall redesign and removal of the 6 legacy rules (due 2026-11-30)
- Privileged access management for OT and vaulting of SCADA administrator accounts (due 2026-12-31)
- Passive OT monitoring at the 20 largest substations and gateway log collection (due 2027-06-30)
- SCADA upgrade replacing the 2 unsupported HMIs and the historian (due 2027-06-30)
- ADMS full deployment (planned 2027-06; design under review, gap 1)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the DOP; CIP Senior Manager (CIP-003-9 R3); accepts Moderate risk |
| Authorizing official equivalent (High risk) | President and CEO | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk and POA&M reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Security lead | Information Security Manager, with 3 security analysts (one OT-focused) and a GRC analyst | Day-to-day security for IT and OT; MSSP oversight; vulnerability management; this SSP |
| IT operations | Director of Information Technology | Identity provider, cloud landing zone, corporate network, tablets |
| OT system administration | OT Engineering Manager and the OT engineering team | SCADA, OT domain, OT DMZ, OT backups, field network |
| Operations lead | Director of System Operations | DCC operation; operational incident commander for OT incidents; DOE-417 filing |
| Protection owner | Director of Engineering and Protection | Relays and gateways at Substations N, E, L, and H; substation physical access; CIP-002 R2.2 delegate |
| ADMS owner | ADMS Program Manager | FLISR pilot and ADMS project |
| Compliance | NERC Compliance Manager (reports to the General Counsel) | CIP, EOP-004, and DOE-417 evidence; SERC submissions |
| Independent assessment | Co-sourced internal audit firm with an OT specialist subcontractor | Annual IT audit; P07 assessment |
| Monitoring | MSSP | 24x7 monitoring of EDR, SIEM, and OT sensor alerts |
| Vendors | SCADA and ADMS vendor; relay testing contractor; carriers | Support, patches, PRC-005 testing, communications (external) |

## 6. System Information Types and System Categorization
Information types follow NIST SP 800-60 Vol. 2 Rev. 1 where a close match exists, and are defined by the company otherwise. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy supply: real-time distribution monitoring and control | Moderate | **High** | **High** | A false or unauthorized command can open feeders serving tens of thousands of customers or re-energize a line where crews work. Loss of SCADA forces manual switching by crews (P05 MTD 4 hours, 2 hours in a storm) |
| Switching orders and clearance records | Low | **High** | **High** | Wrong clearance status can energize a line under a clearance (P05 BP-04, RPO 15 minutes) |
| BES protection data: relay settings, gateway access lists at Substations N, E, L, and H | Moderate | **High** | Moderate | Wrong settings can cause a misoperation of 230 kV or 115 kV line protection. CIP-011 does not apply at low impact, but the company treats these files as Restricted (POL-04) |
| Outage and customer contact records (OMS) | Moderate | Moderate | Moderate | Names, addresses, phone numbers, premise locations; wrong data sends crews to the wrong place |
| Network diagrams, one-line diagrams, and security configuration | Moderate | Moderate | Low | Useful to an attacker; the company handles them as potential CEII and BES Cyber System Information (POL-04) |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed to investigate incidents and support CIP evidence |
| **DOP category (high-water mark)** | **Moderate** | **High** | **High** | |

**Why High and not Moderate.** The tier guidance for Mid-Market describes "a major system (Moderate impact)". The FIPS 199 analysis gives High for integrity and availability, because a control system failure can endanger crews and the public. The plan therefore uses the High baseline, tailored for OT. Confidentiality stays Moderate: the DOP holds limited customer data, and network information is sensitive but not catastrophic if disclosed.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the SCADA master (primary and hot standby), 14 HMIs, historian, 2 engineering workstations, and the OT Windows domain controllers;
- the OT DMZ at headquarters and its replica at the West Operations Center;
- RTUs, gateways, routers, radios, and private LTE equipment at 74 substations, and about 1,900 field devices;
- the 26 relays and 4 gateways at Substations N, E, L, and H;
- the ADMS FLISR pilot servers;
- the OMS and GIS workloads in the operations workloads account, with the DOP's share of the landing zone's network hub, log archive, and backup accounts;
- 310 truck tablets.

**Outside the boundary (interconnected):**
- the corporate network, identity provider, and productivity suite (SYS-07, SYS-08, SYS-10);
- the AMI head-end (SYS-05) and CIS (SYS-06), both vendor SaaS;
- the MSSP's SIEM platform (SYS-13);
- the cloud provider's infrastructure;
- Transmission Owners A and B and their energy management systems; the Balancing Authority and Reliability Coordinator;
- vendor networks that connect through the jump hosts.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Corporate network (SYS-10) | Bidirectional through the OT DMZ | Historian replica, file transfer, patch staging | Internal standard. **6 legacy rules bypass the DMZ (gap 4)** |
| Identity provider (SYS-07) | Inbound authentication | Jump host, OMS, tablet, and cloud console logons with MFA | Internal; identity vendor SOC 2 Type 2 |
| AMI head-end (SYS-05) | Inbound to OMS | Meter outage and restoration events | AMI contract; vendor SOC 2 Type 2. **No interconnection security terms (CA-3)** |
| CIS (SYS-06) | Inbound to OMS | Customer and premise records, outage calls | CIS contract; vendor SOC 2 Type 2 |
| MSSP (SYS-13) | Outbound logs and sensor alerts; inbound analyst queries | Security events | MSSP contract; SOC 2 Type 2 |
| Transmission Owners A and B | Voice and data under operating agreements | Switching coordination, 230 kV and 115 kV status | Interconnection and operating agreements |
| Balancing Authority and Reliability Coordinator | Voice; load data | Load-shedding directives, UFLS program data | Regional procedures |
| SCADA and ADMS vendor | Inbound remote support through the jump hosts | Support sessions, patches | Support contract with security terms. **Uses shared server administrator accounts (gap 5)** |
| Relay testing contractor | Local laptop connections at substations; remote sessions through the jump hosts only | Relay test files, settings | Service agreement. **Cellular modem at Substation H until 2026-08-20 (gap 2); no laptop review at L and H (gap 3)** |
| Carriers (fiber backhaul, licensed radio, private LTE, cellular for tablets) | Transport | Encrypted SCADA and tablet traffic | Carrier contracts. **No security terms** |
| Analytics account (SYS-15) | Outbound historian replica data | Feeder loads for the load-forecasting model (P10) | Internal |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SCADA master (primary and hot standby) | OT server | DCC; backup DCC | OT Engineering Manager |
| HMI consoles (10 at the DCC, 4 at the backup DCC); 2 HMIs on an **unsupported operating system** | OT workstation | DCC; backup DCC | Director of System Operations |
| Historian (**unsupported operating system**) | OT server | DCC | OT Engineering Manager |
| Engineering workstations (2) | OT workstation | DCC | OT Engineering Manager |
| OT domain controllers (2) | OT server | DCC; backup DCC | OT Engineering Manager |
| Jump hosts (2), historian replica, integration server, file transfer server, patch staging server, sensor collector | OT DMZ servers | Headquarters data room; replica at the West Operations Center | OT Engineering Manager |
| IT/OT firewall and OT DMZ firewall (with IDS signatures) | Network | Headquarters; West Operations Center | Information Security Manager |
| Passive OT network sensors (3) | Monitoring | DCC; backup DCC; OT DMZ | Information Security Manager |
| RTUs, gateways, and routers (74 substations) | Field device | Substations | Director of Engineering and Protection |
| BES line protection relays (26) and access control gateways (4) | Low impact BES Cyber Systems | Substations N, E, L, H | Director of Engineering and Protection |
| Reclosers, capacitor controls, line sensors, FLISR switches (about 1,900) | Field device | Distribution feeders | Director of Engineering and Protection |
| Licensed radios and private LTE routers | Field communications | 34 substations and feeder devices | OT Engineering Manager |
| ADMS FLISR servers | OT server | DCC | ADMS Program Manager |
| OMS and GIS | Virtual machines and managed database | Operations workloads account | Director of System Operations |
| Truck tablets (310) | Mobile endpoint | Crew trucks | Director of Information Technology |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The DOP uses the NIST SP 800-53B **High** baseline, tailored with the OT guidance and overlay in SP 800-82 Rev. 3:
- **Documented here: 116 controls** in `control-implementation.csv`. They cover every control that carries a CIP-003-9 low impact requirement, the OT risks in P01 (vendor access, privileged access, IT/OT boundary, monitoring, recovery, supply chain), and the program controls the DOP depends on.
- **Selected by tailoring (added):** PM-1, PM-2, and PM-9 (program level, not in a baseline), and CP-12 (safe mode, for a defined "manual operations" state).
- **OT tailoring (compensating controls):** AC-7 and AC-11 do not lock HMI operator consoles, so operators are never locked out during a grid event. The 24x7 staffed, badge-controlled DCC and named operator accounts compensate.
- **Inherited without separate statements:** physical and environmental controls of the cloud provider's data centers (for example PE-9 to PE-17 for the OMS workloads) and platform-level SC and SA controls, evidenced by the provider's attestation reports and reviewed each year (P04, P09).
- **Deferred:** other High-baseline controls with no CIP driver and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop the SCADA or OMS software). They are recorded as tailoring decisions and reviewed each year.

**Status of the 116 documented controls:**
| Status | Count |
|---|---|
| Implemented | 38 |
| Partially implemented | 74 |
| Planned | 4 |
| Not applicable | 0 |

**Inheritance of the 116 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 82 | Company (OT engineering, System Operations, Engineering and Protection, security team) |
| Hybrid | 23 | Identity provider vendor, cloud provider, MSSP |
| Common/Inherited | 11 | Corporate security program (for example AT-1, AT-2, PL-4, PM-1, PS-3, PS-4) and the cyber insurer's incident response panel with the MSSP (IR-7) |

The Partially implemented statements trace to the 15 known gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm and its OT specialist assessed 34 controls from 2026-08-10 to 2026-08-28, with substation testing on 2026-08-18 to 2026-08-20 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported each quarter to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce (IT and OMS).** Users authenticate through the identity provider with a password and push MFA with number matching. This fits the Moderate confidentiality of the OMS data.
- **Remote and vendor access to OT.** All vendor and engineer remote access goes through the jump hosts with named accounts, MFA, and per-session enablement by the DCC. Administrators and vendors move to phishing-resistant authenticators (FIDO2 security keys) by 2027-03-31 (P01 R-036).
- **OT local access.** HMI operators use named OT domain accounts with passwords inside the badge-controlled DCC; MFA is not used on HMIs so that operators can always reach the grid view. The 3 shared SCADA administrator accounts do not meet this plan's High integrity rating. The company accepts them only until POAM-001 (2026-12-31), with interim compensating steps: passwords changed after each vendor session and session recording on the jump hosts.
- **Customers.** Customers use the CIS vendor's portal, outside this boundary (P09).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); CIP-002 categorization record (2025-12-09), CIP low impact policy (2026-02-26), and cyber security plan; EOP-004-4 Operating Plan; risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **ADMS:** advanced distribution management system
- **BES:** Bulk Electric System
- **BES Cyber System:** one or more BES Cyber Assets grouped to perform reliability tasks (NERC Glossary)
- **CEII:** Critical Energy/Electric Infrastructure Information (18 CFR 388.113)
- **DCC:** Distribution Control Center
- **DMZ:** demilitarized zone, a buffer network between the corporate and OT networks
- **DNP3:** Distributed Network Protocol, the SCADA protocol used to reach substations
- **DOP:** Distribution Operations Platform
- **DP:** Distribution Provider
- **FLISR:** fault location, isolation, and service restoration
- **HMI:** human-machine interface
- **OMS:** outage management system
- **OT:** operational technology
- **POA&M:** plan of action and milestones
- **RTU:** remote terminal unit
- **UFLS:** underfrequency load shedding

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Information Security Manager with the OT Engineering Manager |
| 1.0 | 2026-09-17 | Updated with P07 results (Substation H modem, termination sample); approved by the Chief Operating Officer and the President and CEO | Information Security Manager |

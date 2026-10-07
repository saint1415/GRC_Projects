# System Security Plan: Field SCADA and Production Accounting System (FSPA)

**Organization:** Cris Santos Company, LLC (independent crude oil producer) | **Tier:** Small | **Vertical:** Mining, Quarrying, and Oil and Gas Extraction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Field SCADA and Production Accounting System (**FSPA**), identifier CSC-SYS-001.

## 2. System Overview
The FSPA lets the company watch and control its oil fields and turn what the fields produce into sales and royalty payments. It covers two Florida operating areas: 118 wells, 5 tank batteries, a water injection plant, and 2 compression stations. It is staffed around the clock from the Operations Control Center (OCC) at the Panhandle field office and used by about 110 people: Production Controllers, lease operators, automation technicians, engineers, and production accounting staff.

**Major components:**
- **SYS-01:** SCADA control center: primary and standby SCADA servers, historian, 6 HMIs, 2 engineering workstations
- **SYS-02:** field devices and communications: 96 RTUs and PLCs, 22 ESP drives, 40 electronic flow meters, a 900 MHz radio network, 46 cellular modems
- **SYS-04 (FSPA workloads):** a public-cloud tenant hosting the historian replica, the volume integration service, the field data capture app, and the backup vault
- **SYS-03:** the company's configuration of the production accounting SaaS
- **SYS-05:** the identity provider (for the cloud and SaaS parts)
- **SYS-08 (part):** the SCADA network segment and the IT/OT firewall
- **SYS-09 (part):** 70 rugged tablets used by lease operators
- **SYS-12:** the SCADA integrator's remote access path

**What the system does not do:** it does not perform safety functions. H2S detection, tank high-level shutdowns, and compressor emergency shutdowns are hardwired at each site and work without SCADA. This design choice limits how much harm a SCADA compromise can cause and is the basis for the Moderate integrity rating in section 6.

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Status for the FSPA |
|---|---|---|---|
| N21-BM | NIST CSF 2.0 with NIST SP 800-82 Rev. 3, including the SP 800-82 Rev. 3 OT overlay (Appendix F) | NIST CSWP 29; SP 800-82 Rev. 3 | Voluntary benchmark adopted by the company (P03) |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2)-(6) | Applies to royalty owner personal information in production accounting |
| Federal | Oil discharge notice | 40 CFR 110.6; 33 CFR 153.203 | Applies if a SCADA failure or attack leads to a discharge that reaches water; drives the P08 notification matrix |
| Internal | Security policies POL-01 to POL-05 | P06 | Approved 2026-08-31 |

**Not applicable** (see P03 section 1):
- N21-R01, the USCG Marine Transportation System cyber rule (33 CFR 101.605): no vessel, waterfront facility, or OCS facility.
- N21-R02, TSA Security Directive Pipeline-2021-02G: not a TSA-notified pipeline owner or operator.
- N21-R03, CIRCIA: proposed only; as proposed, the company is SBA-small and meets no sector criterion.
- PHMSA control room management (49 CFR 195.446): the OCC controls production facilities, not a pipeline (195.1(b)(8)).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the CFO and the VP Operations on 2026-08-31.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The CFO and the VP Operations accepted continued operation of the FSPA on 2026-08-31, with the conditions in the P07 POA&M.
- The majority owner accepted the three High risks listed in P01, with dated treatment plans.
- Condition of operation: the three internet-exposed modems must be moved to the private network by 2026-09-30 (POAM-013).
### 4.3 System Operational Status
Operational. Major modifications planned:
- OT DMZ and IT/OT firewall redesign (P01 R-001), due 2027-01-31.
- SCADA server and HMI operating system upgrade (R-005), due 2027-03-31.
- Standby SCADA server moved to the South Florida field office (R-014), due 2027-06-30.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | VP Operations | Business owner of field operations and SCADA; agrees to any risk acceptance affecting operations or safety |
| Risk acceptor (authorizing official equivalent) | CFO (up to Moderate); majority owner (High and Very High) | Acceptance of residual risk |
| Information Security Lead | IT Manager | Program owner day to day; corporate, cloud, and SaaS controls |
| OT security lead | SCADA and Automation Supervisor | SCADA servers, HMIs, field devices, integrator oversight |
| Data owner (production and royalty data) | Production Accounting Manager | Production accounting configuration, owner data, run ticket integrity |
| Operations support | SCADA integrator (contractor) | SCADA configuration and remote support |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1, which gives provisional impact levels for federal systems. The company adjusted them for its own operations as the publication allows. Impact levels follow FIPS 199.

| Information type (SP 800-60 Vol. 2 Rev. 1) | Provisional (C, I, A) | Company rating (C, I, A) | Rationale |
|---|---|---|---|
| Energy Production (D.7.4): process data, setpoints, controller logic | Low, Low, Low | Low, **Moderate**, **Moderate** | Changed setpoints or logic could cause equipment damage, a spill, or an injection permit violation; hardwired safety shutdowns keep the worst case below High. Loss of SCADA forces manual operations and, after 24 hours, shut-ins (P05) |
| Energy Supply (D.7.1): run tickets, custody transfer volumes, sales | Low, Moderate, Moderate | Low, Moderate, Moderate | Wrong volumes misstate sales and royalties; tank storage gives 72 hours before shut-in |
| Payments (C.3.2.5): royalty and partner distributions | Low, Moderate, Low | **Moderate**, Moderate, Low | Owner records include Social Security numbers covered by Fla. Stat. 501.171; SP 800-60 notes bank account details as a special factor |
| **FSPA category (high-water mark)** | | **Moderate, Moderate, Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored with the SP 800-82 Rev. 3 OT overlay (Appendix F). The overlay was applied where OT limits a control, for example device lock on OCC HMIs (AC-11), shared local accounts (IA-2), and unencrypted polling (SC-8). The plan documents the 68 controls that address the P01 risks and the benchmark gaps (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems (for example, PIV acceptance, IA-2(12), which the overlay itself limits to federal organizations).

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services:
- **Inside:** the OCC server room and HMIs, the SCADA network, all field controllers and communications equipment, the IT/OT firewall, the four FSPA workloads in the cloud tenant, the production accounting tenant configuration and user roles, the identity provider tenant (for FSPA users), the 70 rugged tablets, and the vendor remote access path.
- **Outside (external services, interconnected):** the production accounting vendor's platform, the cloud provider's infrastructure, the cellular carrier's network, the third-party gas gathering system and its sales meter data, the crude purchaser's systems, the SCADA integrator's own network, and the corporate network beyond the IT/OT firewall.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Corporate network (SYS-08) | Bidirectional through the IT/OT firewall | Historian reads, HMI remote desktop from IT (to be removed) | Internal; rules undocumented (**gap**) |
| Cloud tenant historian replica (SYS-04) | Outbound from the OCC historian over the VPN | Hourly process data | Internal |
| Production accounting SaaS (SYS-03) | Outbound from the volume integration service | Daily allocated volumes, run tickets | SaaS agreement; SOC 2 Type 2 |
| Gas gathering company | Inbound | Sales meter volumes (monthly statements) | Gas purchase contract; **no data security terms** |
| Crude purchaser | Bidirectional | Run tickets, sales statements | Crude purchase contract |
| SCADA integrator (SYS-12) | Inbound remote access | Full SCADA administration | Master services agreement; **no security terms, shared account, no MFA (gap)** |
| Cellular carrier | Transport | RTU polling for 46 sites | Carrier contract; 3 modems on the public network (**gap**) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SCADA primary and standby servers, historian | Servers (unsupported OS, **gap**) | OCC server room | SCADA and Automation Supervisor |
| HMIs (6), engineering workstations (2) | Workstations | OCC (4 HMIs, 2 EWS), South Florida field office (2 HMIs) | SCADA and Automation Supervisor |
| SCADA backup storage device | Network storage | OCC server room (same room, **gap**) | SCADA and Automation Supervisor |
| RTUs and PLCs (96), ESP drives (22), flow meters (40) | Field controllers | Well pads and facilities | SCADA and Automation Supervisor |
| Radio network (900 MHz) and cellular modems (46) | Communications | Field sites and towers | SCADA and Automation Supervisor |
| IT/OT firewall | Network | OCC | IT Manager |
| Historian replica, volume integration service, field data capture app, backup vault | Cloud VM, PaaS functions, PaaS web app and database, backup service | Cloud tenant | IT Manager |
| Production accounting tenant | SaaS | Production accounting vendor | Production Accounting Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Rugged tablets (70) | Mobile endpoints | Lease operators | IT Manager |
| Integrator remote access tool | Third-party software | Installed on the SCADA primary server (**gap**) | SCADA and Automation Supervisor |

The field controller list is not yet itemized by model and firmware (gap 1; POAM-006).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 68 controls:
- Implemented: 10
- Partially implemented: 41
- Planned: 17
- Not applicable: 0

By inheritance: 53 system-specific, 13 hybrid, 2 common or inherited.

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Corporate, cloud, and SaaS users** (including production accounting and the field data capture app) authenticate through the identity provider with a password and a second factor: a phone authenticator app, or a hardware key for the 4 IT administrators. This is appropriate for the Moderate categorization.
- **SCADA users** authenticate with local SCADA accounts. Today the OCC uses one shared operator login and the integrator uses one shared account without MFA. The target, consistent with the SP 800-82 Rev. 3 overlay discussion of IA-2: named accounts for engineers and administrators; for Production Controllers, either named accounts with fast user switching or a documented compensating control (badge-controlled OCC, shift sign-in log, SCADA event log review); and for all remote access, individual identification with MFA at the jump host before any shared account is used.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **DMZ:** demilitarized zone, a buffer network between IT and OT
- **ESP:** electric submersible pump
- **FSPA:** Field SCADA and Production Accounting System
- **H2S:** hydrogen sulfide
- **HMI:** human-machine interface
- **MDR:** managed detection and response
- **OCC:** Operations Control Center
- **OT:** operational technology
- **PLC / RTU:** programmable logic controller / remote terminal unit
- **POA&M:** plan of action and milestones
- **SCADA:** supervisory control and data acquisition

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager with the SCADA and Automation Supervisor |

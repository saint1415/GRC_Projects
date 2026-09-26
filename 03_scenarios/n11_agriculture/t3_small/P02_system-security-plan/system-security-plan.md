# System Security Plan: Farm Management and Irrigation Control Platform (FMICP)

**Organization:** Cris Santos Company, LLC (diversified precision-agriculture crop farm) | **Tier:** Small | **Vertical:** Agriculture, Forestry, Fishing and Hunting
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Farm Management and Irrigation Control Platform (**FMICP**), identifier CSC-SYS-001.

## 2. System Overview
The FMICP runs the farm's field, irrigation, harvest, and food safety record work across about 640 acres in two blocks (Home Block and North Block). It supports crop plans and application records, remote control of pumps, pivots, drip zones, and fertigation, freeze-protection irrigation for strawberries, piece-rate field tally for harvest crews (including 4 H-2A workers), packing and lot codes, cooler temperature alarms, and the Produce Safety records the farm must keep under 21 CFR Part 112. It serves 15 employees, the irrigation integrator, and the MSP.

**Major components:**
- **SYS-01:** a SaaS farm management and irrigation software platform (FMIS) with web and mobile apps, including the irrigation control module (farm-managed configuration of the vendor service)
- **SYS-02:** the identity provider for single sign-on and MFA
- **SYS-04:** a public-cloud tenant hosting the farm data hub (historian), drone imagery storage, and the backup vault
- **SYS-05:** the farm networks (headquarters, pump house, packing shed, pivot cellular links, LoRaWAN gateway)
- **SYS-06:** endpoints and rugged tablets used to run the farm
- **SYS-07:** irrigation, pump, and cold-room operational technology (OT): the pump-house PLC and SCADA HMI, pivot panels, valve controllers, sensors, and cooler alarms

The cloud tenant is described by service category and is vendor-agnostic (see P04). The OT portion follows NIST SP 800-82 Rev. 3.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Status for this system |
|---|---|---|---|
| Benchmark | NIST Cybersecurity Framework 2.0 | NIST CSWP 29 (2024) | Voluntary benchmark (P03). No binding federal cybersecurity rule applies |
| Benchmark (OT) | Guide to Operational Technology Security | NIST SP 800-82 Rev. 3 (2023) | Voluntary guidance for SYS-07 |
| Binding | Produce Safety Rule, records | 21 CFR 112.161-112.166 | Applies. Produce Safety records are kept in SYS-01 |
| Binding | H-2A earnings records | 20 CFR 655.122(j) | Applies. Field tally in SYS-01 is part of the earnings record |
| State | Florida Information Protection Act (data security, disposal, breach notice) | Fla. Stat. 501.171 | Applies to personal information in and around the system (worker records, operator geolocation in SYS-08) |
| Contract | PCI DSS through the acquirer agreement | Merchant agreement | Outside this boundary; card data never enters the FMICP |
| Internal | Security policies POL-01 to POL-05 | P06 | Approved 2026-08-31 |

Not applicable:
- **N11-R01**, the FSMA intentional adulteration rule (21 CFR Part 121): it applies only to facilities that must register under FD&C Act section 415 (21 CFR 121.1), and farms are exempt from registration (21 CFR 1.226(b)). It is used only as a voluntary checklist for the fertigation risk (P01 R-005).
- **CIRCIA** (proposed 6 CFR Part 226): not final, and as proposed it would not cover a farm under the SBA size standard.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the majority owner and General Manager on 2026-08-31.
### 4.2 System Authorization Decision
The farm is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The majority owner and General Manager accepted continued operation of the FMICP on 2026-08-31, with the conditions in the P07 POA&M. The two conditions that must be met before the 2026-27 freeze season: integrator remote access redesigned (POAM-002, due 2026-10-31) and the manual irrigation and freeze procedure written and drilled (POAM-004 milestone, 2026-11-15).
- The four High risks in P01 were accepted only with dated treatment plans.
### 4.3 System Operational Status
Operational. Major modifications planned: network segmentation of the pump house (R-022, due 2026-12-31) and backup redesign (R-003, due 2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Farm Manager | Business owner of field operations and the FMICP; accepts Moderate risks |
| Risk acceptor (authorizing official equivalent) | Majority owner and General Manager | Accepts High and Very High risks; approves this plan |
| Security lead | Operations and Technology Manager | Day-to-day security; administers SYS-01, SYS-02, SYS-04; manages the MSP and integrator |
| OT operator | Irrigation Technician | Operates SYS-07; approves PLC and HMI changes; runs manual operation |
| Records owner | Food Safety and Packing Lead | Produce Safety records in SYS-01 |
| Operations support | MSP; irrigation integrator | Office endpoints, firewall, backups (MSP); PLC and HMI support (integrator) |

## 6. System Information Types and System Categorization
SP 800-60's information type catalog is built for federal missions and has no farm operations type. Information types below are author-defined following the SP 800-60 method; impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Irrigation and fertigation control (schedules, setpoints, PLC program) | Low | Moderate | Moderate | Wrong commands can burn or drown a crop, exceed permit or label limits, or expose workers; manual operation and a standalone freeze alarm keep availability impact to Moderate (P05 MTD 12 h). On freeze nights availability would be High without the manual procedure, which is why POAM-004 is a condition of operation |
| Produce Safety and field records | Low | Moderate | Low | Records must be accurate and indelible (21 CFR 112.161(a)); a 72-hour outage is tolerable with paper forms (P05 BP-06) |
| Worker and harvest tally records (H-2A earnings records) | Moderate | Moderate | Low | Names with piece-rate counts; errors lead to wage disputes and program findings |
| Farm operational and yield data | Moderate | Low | Low | Commercially sensitive (yields, buyer volumes); little harm if briefly unavailable |
| **FMICP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 15-person farm, with the SP 800-82 Rev. 3 Appendix F OT overlay consulted for SYS-07. The plan documents the 77 controls that matter most for this system (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems or to organizations that develop software (for example, the SA-11 developer testing control).

## 7. Authorization Boundary Description
The boundary contains farm-managed components and the farm's configuration of vendor services:
- **Inside:** the SYS-01 tenant configuration and user roles, the identity provider tenant, the cloud tenant (3 workloads), the headquarters and pump-house networks, the pivot cellular modems and LoRaWAN gateway, 8 laptops, 3 desktops, 11 tablets and phones, the PLC, HMI, pivot panels, valve controllers, sensors, and cooler alarm sensors.
- **Outside (external services, interconnected):** the FMIS vendor's platform, the cloud provider's infrastructure, the equipment dealer's telematics portal (SYS-08), the agronomy analytics vendor (SYS-12), the cooler alarm service, the cellular carriers, and the integrator's own systems.
- **Outside and not interconnected:** accounting and payroll (SYS-10) and sales systems (SYS-11).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Irrigation integrator (remote support) | Inbound remote sessions to the HMI | Full HMI control; PLC programming | Time-and-materials agreement, **no security terms (gap)** |
| Equipment dealer telematics (SYS-08) | Inbound to SYS-01 | As-applied maps, yield monitor data | Dealer portal terms; **no access or retention terms (gap)** |
| Agronomy analytics vendor (SYS-12) | Outbound imagery; inbound yield estimates | Orthomosaics; block-level estimates | Click-through terms allowing secondary use (**gap**, P10) |
| Cooler alarm service | Outbound | Temperature readings and alarms | Service contract |
| Pivot panels (North Block) | Bidirectional over carrier private network | Start, stop, speed, and status | Carrier contract |
| MSP | Inbound management to office endpoints | Patches, configuration | MSP contract (patching and backup monitoring duties) |
| Wholesale distributor | Outbound (by email from SYS-01 reports) | Lot codes, temperature logs | Supplier agreement |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SYS-01 FMIS tenant (farm records, tally, irrigation module) | SaaS | FMIS vendor | Farm Manager |
| Identity provider tenant | SaaS | Productivity suite vendor | Operations and Technology Manager |
| Farm data hub | Cloud virtual machine | Cloud tenant | Operations and Technology Manager |
| Imagery storage | Cloud object storage | Cloud tenant | Equipment and Drone Specialist |
| Backup vault | Cloud backup service | Cloud tenant (same account and region, **gap**) | Operations and Technology Manager |
| Headquarters firewall, switches, 2 access points | Network | Headquarters | Operations and Technology Manager |
| LoRaWAN gateway | Network (IoT) | Pump house roof | Irrigation Technician |
| Laptops (8), desktops (3), tablets and phones (11) | Endpoint | Headquarters and field | Operations and Technology Manager |
| PLC with 3 VFD-driven well pumps and 2 fertigation injection pumps | OT | Pump house | Irrigation Technician |
| SCADA HMI workstation | OT | Pump house | Irrigation Technician |
| Center-pivot control panels (5) with cellular modems | OT | North Block | Irrigation Technician |
| Drip-zone valve controllers (24), soil moisture probes (96), flow meters (8), weather stations (2) | OT and IoT | Home Block and North Block | Irrigation Technician |
| Cooler temperature sensors (6) | IoT | Cooler | Food Safety and Packing Lead |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 77 controls:
- Implemented: 11
- Partially implemented: 42
- Planned: 24
- Not applicable: 0

Inheritance: 59 system-specific, 13 hybrid, 5 common or inherited from the FMIS vendor, identity provider, or cloud provider.

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07, with OT testing on 2026-08-05. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Office and management users authenticate through the identity provider with a password and a phone authenticator app; administrators use number matching. This is appropriate for access to a Moderate system that can change irrigation settings.

Two exceptions are not acceptable and are on the POA&M: the SYS-01 mobile app signs in with a password only (vendor MFA to be enabled, R-006), and the integrator's remote tool uses one shared account without MFA (POAM-002). Crew leads will use named accounts with a device PIN on managed tablets, which is proportionate for entering tally records on a farm-owned device.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 self-benchmark and FMIS vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **EDR:** endpoint detection and response
- **FMICP:** Farm Management and Irrigation Control Platform
- **FMIS:** farm management and irrigation software
- **HMI:** human-machine interface (the SCADA operator workstation)
- **LoRaWAN:** a low-power wide-area radio network for field sensors
- **MSP:** managed service provider
- **OT:** operational technology
- **PLC:** programmable logic controller
- **POA&M:** plan of action and milestones
- **RTK:** real-time kinematic (GNSS correction for guidance)
- **VFD:** variable-frequency drive

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Operations and Technology Manager |

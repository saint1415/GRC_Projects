# System Security Plan: Water Treatment SCADA System (WTSS)

**Organization:** Cris Santos Company, LLC (investor-owned community water system) | **Tier:** Small | **Vertical:** Water and Wastewater Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), with OT guidance from NIST SP 800-82 Rev. 3 | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Water Treatment SCADA System (**WTSS**), identifier CSC-OT-001.

## 2. System Overview
The WTSS monitors and controls drinking water production and delivery for 46,200 people. It runs the 14 wells, both treatment plants (WTP-1, 6.0 MGD; WTP-2, 2.5 MGD), chemical feed (sodium hypochlorite, sodium hydroxide, and corrosion inhibitor), 6 booster stations, and 4 storage tanks. Licensed operators supervise it 24 hours a day from the WTP-1 control room. WTP-2 is staffed on day shift and supervised remotely at night.

**Major components:**
- **SYS-01:** primary and standby SCADA/HMI servers, 4 operator HMI stations, 1 engineering workstation, and 1 process historian server
- **SYS-02:** 6 PLCs (4 at WTP-1, 2 at WTP-2) and 24 RTUs at wells, boosters, and tanks
- **SYS-03:** licensed radio telemetry to 18 sites and cellular modems at 6 sites
- **SYS-04:** remote access paths: the IT-managed VPN for on-call operators and the SCADA integrator's remote desktop agent
- **OT networks** at WTP-1 and WTP-2, joined to the business network by the IT/OT firewall

**Engineered safeguards outside the software.** Chemical feed pumps have hardwired stroke limits, and pH and chlorine analyzers have hardwired high/low alarms to the control room. Operators can run every process in manual (local) mode. SCADA cannot override these safeguards. They are documented as SC-24 (fail in known state) and are the reason no WTSS risk is rated Very High (P01).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-WATER-R01 | SDWA section 1433 risk and resilience assessment and emergency response plan. The WTSS is the main "electronic, computer, or other automated system" in the RRA, and its protection is part of the ERP's cybersecurity strategies | 42 U.S.C. 300i-2(a)(1)(A)(ii); (b)(1)-(4) |
| C-WATER-R02 | CIRCIA (proposed, not in effect). Tracked only. Would require reporting covered cyber incidents to CISA if finalized as proposed | 6 U.S.C. 681-681g; proposed 6 CFR Part 226 |
| Federal | SDWA public notification rule: a failure or significant interruption in key treatment processes can require a Tier 1 notice within 24 hours | 40 CFR 141.202 |
| Federal | Tampering with a public water system, including interfering with its operation with intent to harm persons, is a federal crime. Relevant to law enforcement referral after an attack | 42 U.S.C. 300i-1 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable: wastewater (POTW) requirements; federal contract clauses (no federal contracts).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the General Manager on 2026-08-31.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The General Manager accepted continued operation of the WTSS on 2026-08-31, with the conditions in the P07 POA&M. Operation continues because the plants cannot be shut down and because manual operation and the hardwired safeguards limit the worst outcomes.
- The majority owner accepted the five High risks in P01 temporarily, with treatment plans dated no later than 2027-03-31. Four of them (R-001, R-002, R-006, R-008) are due by 2026-10-31.
### 4.3 System Operational Status
Operational. Major modifications planned: remote access gateway (2026-10-31), OT DMZ and firewall redesign (2027-03-31), SCADA server and engineering workstation upgrade to a supported operating system (2027 capital plan).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Operations Manager | Accountable for WTSS operation and changes; RRA and ERP lead |
| Risk acceptor (authorizing official equivalent) | General Manager (up to Moderate); majority owner (High and Very High) | Risk acceptance per POL-01 |
| Security lead (IT and OT) | IT Manager | Security controls, firewall, remote access, logging, assessments |
| OT technical support | SCADA and Instrumentation Technicians (2) | PLCs, RTUs, HMIs, radios, backups of control logic |
| Shift supervision | Chief Plant Operators (2) | Approve vendor remote sessions (after 2026-10-31); lead manual operation |
| Contractor | SCADA system integrator | Programming and remote support under the company's rules |

## 6. System Information Types and System Categorization
SP 800-60 is written for federal mission areas and has no water treatment process type. The company defined its own information types and rated them with FIPS 199 definitions.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Process control and setpoints (PLC logic, chemical feed setpoints, commands) | Moderate | **High** | **High** | Unauthorized change to dosing or pumping could harm public health; loss of control forces manual operation of both plants (P05 BP-01 MTD 12 h) |
| Process and water quality data (historian, analyzer values, alarms) | Low | High | Moderate | Operators and compliance reporting rely on accurate values; manual sampling covers short outages |
| System configuration and network information (diagrams, IP plans, credentials) | Moderate | Moderate | Low | Disclosure helps an attacker plan an intrusion; also RRA and ERP content |
| **WTSS category (high-water mark)** | **Moderate** | **High** | **High** | |

**Baseline:** the NIST SP 800-53B High baseline, tailored with the **OT overlay in SP 800-82 Rev. 3, Appendix F**, and scaled for a 60-person utility. The plan documents the 64 controls that carry the RRA's automated-systems element and core OT hygiene (see `control-implementation.csv`). Every other High-baseline control is treated as follows:
- **Tailored with OT compensating controls** where the overlay allows it, and recorded in the implementation statement (for example AC-7 and AC-11 on operator HMIs that must stay available in a staffed control room).
- **Deferred** to the 2027 SCADA upgrade where the current platform cannot support the control (for example automated account management on the unsupported OS).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control exists for federal program management (PM family beyond the policy set).

## 7. Authorization Boundary Description
- **Inside:** SCADA servers, HMIs, engineering workstation, historian, PLCs, RTUs, radios and cellular modems, the OT network switches at both plants, the OT side of the IT/OT firewall, the VPN appliance, and the vendor remote access path (agent today, gateway after 2026-10-31).
- **Outside (interconnected):** the business network (SYS-11), the cloud tenant hosting the historian replica and anomaly detection model (SYS-05), the identity provider (SYS-06, used for VPN MFA after 2026-10-31), the integrator's own network, and the cellular carrier's network.

The diagram is in P04 `cloud-architecture.md`, which shows the OT boundary and its connections to the cloud tenant and SaaS services.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Business network (SYS-11) through IT/OT firewall | Outbound historian data; inbound VPN sessions | Process data; remote sessions | Internal firewall rule set (**too broad, gap**) |
| Cloud tenant historian replica (SYS-05) | Outbound only (planned one-way through OT DMZ) | Process and water quality data | Cloud provider terms |
| SCADA integrator | Inbound remote sessions | Engineering access to HMIs and PLCs | Service contract (**no security terms, gap**) |
| Cellular carrier private network | Bidirectional | Telemetry for 6 sites | Carrier contract |
| On-call operators (VPN) | Inbound | HMI sessions | POL-02; rules of behavior |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SCADA/HMI servers (primary and standby) | Server (unsupported OS, **gap**) | WTP-1 control room | Operations Manager |
| Operator HMI stations (4) | Workstation | WTP-1 (3), WTP-2 (1) | Operations Manager |
| Engineering workstation | Workstation | WTP-1 | SCADA and Instrumentation Technicians |
| Process historian | Server (dual-homed, **gap**) | WTP-1 | IT Manager |
| PLCs (6) with chemical feed control | Controller | WTP-1 (4), WTP-2 (2) | Operations Manager |
| RTUs (24) | Controller | 14 wells, 6 boosters, 4 tanks | SCADA and Instrumentation Technicians |
| Radios (18) and cellular modems (6) | Telemetry | Remote sites | SCADA and Instrumentation Technicians |
| IT/OT firewall and OT switches | Network | WTP-1, WTP-2 | IT Manager |
| VPN appliance | Network | Administration office | IT Manager |

A full inventory with firmware versions is being built (CM-8, due 2026-10-31).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 64 controls:
- Implemented: 11
- Partially implemented: 36
- Planned: 17
- Not applicable: 0

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Remote access to OT** (on-call operators and the integrator) must use MFA through the company's identity provider on the new gateway, with phishing-resistant authenticators for administrator and integrator accounts. Remote OT access can change treatment, so it needs the strongest assurance the company can support.
- **Operators in the control room** use named HMI accounts with passwords (after 2026-12-31). The badge-controlled room is a compensating control, and HMIs stay unlocked for alarm response, as the SP 800-82r3 OT overlay allows.
- **Device and service credentials** (PLCs, modems, historian service accounts) are stored in a password vault and changed from commissioning values.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register and RRA cyber addendum (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 self-benchmark (P09), AI assessment (P10), 2021 RRA and ERP, 2026 RRA review memo.

## 13. Acronym List and Glossary
- **DMZ:** demilitarized zone, a buffer network between IT and OT
- **ERP:** emergency response plan (SDWA section 1433(b))
- **HMI:** human-machine interface
- **MGD:** million gallons per day
- **OT:** operational technology
- **PLC:** programmable logic controller
- **RRA:** risk and resilience assessment (SDWA section 1433(a))
- **RTU:** remote terminal unit
- **SCADA:** supervisory control and data acquisition
- **WTSS:** Water Treatment SCADA System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager with the Operations Manager |

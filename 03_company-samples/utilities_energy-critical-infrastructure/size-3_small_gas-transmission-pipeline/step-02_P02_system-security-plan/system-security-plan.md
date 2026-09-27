# System Security Plan: Pipeline SCADA and Gas Control System (PSGCS)

**Organization:** Cris Santos Company, LLC (intrastate natural gas transmission pipeline operator) | **Tier:** Small | **Vertical:** Energy
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-24

## 1. System Name and Identifier
Pipeline SCADA and Gas Control System (**PSGCS**), identifier CSC-OT-001.

## 2. System Overview
The PSGCS lets 6 gas controllers monitor and control about 185 miles of intrastate natural gas transmission pipeline in Florida, 24 hours a day. Through it, controllers:
- watch pressures, flows, gas quality, and alarms;
- open and close 8 remote-control mainline valves;
- start, stop, and load the 2 compressor units at Compressor Station 1;
- manage deliveries to 14 delivery points serving 2 local distribution companies, a power plant, and 6 industrial plants.

It is the SCADA system that 49 CFR 192.631 regulates.

**Major components:**
- **SYS-01:** redundant SCADA host servers, 3 HMI consoles, historian, and an engineering workstation in the Gas Control Center (HQ)
- **SYS-02:** the backup SCADA host and backup control room at Compressor Station 1
- **SYS-03:** about 40 field RTUs and PLCs, plus flow computers and gas chromatographs
- **SYS-04:** licensed radio and carrier private cellular telecommunications
- **SYS-05:** the IT/OT DMZ: firewall pair, historian replica, patch staging server, and remote access jump host
- **SYS-12 (part):** badge access control at both control rooms

Business IT, the cloud tenant, and SaaS services are outside the boundary (section 7).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-ENERGY-R04 | PHMSA control room management | 49 CFR 192.631, adopted in Florida by Rule 25-12.005, F.A.C.; inspected by the FPSC |
| Related | Operations and maintenance manual; emergency plans | 49 CFR 192.605; 49 CFR 192.615 |
| Related | Incident reporting | 49 CFR 191.3, 191.5, 191.15; Rule 25-12.084, F.A.C. |
| Benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (OT overlay, Appendix F) | Voluntary; chosen in P03 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- **C-ENERGY-R02 and C-ENERGY-R03**, TSA SD Pipeline-2021-01G and 02G. TSA has not designated the pipeline as critical (P03 section 1.1). The SD measures are tracked as a readiness reference, and the `regulatory_driver` column of `control-implementation.csv` names the SD section each control would support.
- **C-ENERGY-R01**, NERC CIP. The company is not a NERC-registered entity.
- **C-ENERGY-R05**, CIRCIA. Proposed only (P03 section 1.2).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the President on 2026-09-24.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The President accepted continued operation of the PSGCS on 2026-09-24, with the conditions in the P07 POA&M.
- The majority owner accepted the High risks listed in P01 (R-001 to R-004, R-012), with dated treatment plans. The first milestone is named integrator accounts with MFA by 2026-11-30.
### 4.3 System Operational Status
Operational. Two major modifications are planned:
- a secure remote access redesign and OT monitoring sensor (P01 R-002, R-003, R-005), 2026 Q4 to 2027 Q1;
- a SCADA software and HMI operating system upgrade, 2027. This one requires the API RP 1165 review in 192.631(c)(1).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | VP Operations | Overall accountability for the PSGCS and the O&M and emergency procedures |
| Risk acceptor (authorizing official equivalent) | President (up to Moderate); majority owner (High and Very High) | Risk acceptance |
| Security program lead | IT Manager | Security program, policies, risk register, and assessments |
| System administrator and OT security | SCADA Engineer | SCADA hosts, HMIs, OT network, field device configuration, backups |
| Control room management lead | Gas Control Manager | 192.631 procedures, alarm management, controller training |
| Regulatory compliance | Pipeline Safety and Compliance Manager | FPSC and PHMSA records and reporting |
| External support | SCADA integrator (contractor) | SCADA software and display support through remote access |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199 and use the BIA (P05).

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy supply: pipeline control data and commands | Moderate | **High** | **High** | Wrong commands or false data could cause overpressure or hide a rupture, with potential loss of life. Loss of control beyond the 8-hour MTD forces curtailment to LDCs serving about 140,000 customers |
| SCADA configuration, network, and security information | Moderate | **High** | Moderate | Disclosure helps an attacker plan; unauthorized change affects every control function |
| Emergency response information | Low | Moderate | **High** | Public safety communication cannot stop (P05 BP-03) |
| Gas measurement data | Low | Moderate | Low | Flow computers keep 35 days locally (P05 BP-05) |
| **PSGCS category (high-water mark)** | **Moderate** | **High** | **High** | **High** |

**Baseline:** the NIST SP 800-53B High baseline, tailored with the SP 800-82 Rev. 3 OT overlay (Appendix F) for a 60-person operator. The plan documents 66 controls: the controls that protect SCADA integrity and availability, support 192.631, and would support the TSA SD measures on designation (see `control-implementation.csv`). Every other High-baseline control is treated in one of three ways:
- **Planned for the 2027 plan update**, after the monitoring and remote access projects. Examples: the rest of the AU, IR, and SR families.
- **Tailored out with a reason.** Examples:
  - Session termination on HMI consoles, because controllers must never lose the alarm display.
  - Account lockout on HMIs, compensated by the staffed, badge-controlled control room.
- **Not relevant to a non-federal operator.** Example: PM-series program controls beyond the program policy in POL-01.

## 7. Authorization Boundary Description
The boundary contains everything that can see or change the state of the pipeline:
- **Inside:**
  - the SCADA hosts, HMI consoles, historian, and engineering workstation at the Gas Control Center;
  - the backup SCADA host and backup control room at Compressor Station 1;
  - the field RTUs, PLCs, flow computers, and chromatographs at 23 sites (14 M&R stations, 8 valve sites, and the receipt interconnect), plus the compressor station control PLCs;
  - the radio network and cellular gateways;
  - the IT/OT firewall pair and the DMZ servers;
  - badge access at both control rooms.
- **Outside (interconnected):**
  - business IT and endpoints;
  - the identity provider and productivity suite;
  - the cloud tenant (measurement application and leak-detection analytics);
  - the telecom carrier's private network;
  - the SCADA integrator's systems.

Business IT connects only to the DMZ, never directly to OT. The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| DMZ historian replica to cloud analytics workload (SYS-09) | Outbound from DMZ | Pressure, flow, and valve data for the leak-detection model | Internal; model vendor contract (no security terms, gap) |
| DMZ historian replica to measurement application (SYS-09) | Outbound from DMZ | Hourly volumes and gas quality | Internal |
| SCADA integrator | Inbound remote sessions to the jump host | Support and display changes | Contract with **no security terms (gap)**; shared account without MFA (gap) |
| Telecom carrier | Bidirectional (transport) | SCADA polling and commands | Carrier service agreement; no incident notice term (gap) |
| Upstream interstate pipeline | None system-to-system | Operational calls by phone | Interconnect operating agreement |
| MSP | None into OT | MSP has no OT access by design | MSP contract |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SCADA host servers (2, redundant) | Server | Gas Control Center | SCADA Engineer |
| HMI consoles (3) and engineering workstation | Workstation | Gas Control Center | SCADA Engineer |
| Historian | Server | Gas Control Center | SCADA Engineer |
| Backup SCADA host and 2 HMI consoles | Server and workstations | Compressor Station 1 | SCADA Engineer |
| SCADA backup storage device | Network storage (inside OT, **gap**) | Gas Control Center | SCADA Engineer |
| IT/OT firewall pair | Network | Gas Control Center | SCADA Engineer |
| DMZ: historian replica, patch staging, jump host | Virtual servers | Gas Control Center | SCADA Engineer |
| Field RTUs and PLCs (about 40), flow computers, chromatographs | Field device | 23 field sites and Compressor Station 1 | Field Operations Manager |
| Compressor unit and station control PLCs | Field device | Compressor Station 1 | Field Operations Manager |
| Licensed radio network and cellular gateways | Telecommunications | Field; carrier private network | SCADA Engineer |
| Badge readers and CCTV at control rooms | Physical security | HQ and Compressor Station 1 | VP Operations |

The inventory is incomplete below the device level: firmware for about a third of field devices is unknown, and cellular gateways were missing (P03 G-040).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 66 controls:
- Implemented: 10
- Partially implemented: 46
- Planned: 10
- Not applicable: 0
- Inheritance: 61 system-specific, 5 hybrid (identity provider, telecom carrier, MSP)

The pattern reflects the P03 finding: the pipeline safety controls (backup control room, point verification, time sync, physical access, SCADA roles) are largely in place, and the cyber controls (accounts, remote access, monitoring, backups, patching) are partial.

### 10.2 Control assessment status
Assessed 2026-08-24 to 2026-08-28. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Controllers** authenticate to the SCADA application with individual passwords inside staffed, badge-controlled control rooms. MFA on HMI consoles was rejected: it could delay a controller in an emergency. The physical controls are the compensating measure. This is the approach SD 02G Section III.C.2 would require the company to document if designated.
- **Administrators and the SCADA integrator** reach OT remotely or through the engineering workstation. They must reach authenticator assurance level 2 (a password and a second factor) as described in NIST SP 800-63B. This is **not yet met**: the integrator account is shared and has no MFA. The target date is 2026-11-30 (POAM-002).
- **Business users** use the identity provider with MFA. They have no OT access.

## 12. Referenced Artifacts
- Scenario facts (`../00_company-facts.md`)
- Risk register (P01)
- Gap analysis (P03)
- Cloud and architecture map (P04)
- BIA (P05)
- Policies (P06)
- Assessment and POA&M (P07)
- Incident response runbook (P08)
- SOC 2 self-benchmark and MSP report review (P09)
- AI assessment for the leak-detection model (P10)
- Control room management manual, O&M manual (192.605), and emergency plan (192.615)

## 13. Acronym List and Glossary
- **AOC:** abnormal operating condition
- **DMZ:** demilitarized zone (network between business IT and OT)
- **FPSC:** Florida Public Service Commission
- **HMI:** human-machine interface (controller console)
- **LDC:** local distribution company
- **M&R:** meter and regulator station
- **MOC:** management of change
- **OT:** operational technology
- **P2P:** point-to-point verification
- **PLC / RTU:** programmable logic controller / remote terminal unit
- **SCADA:** supervisory control and data acquisition

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-24 | Initial plan | IT Manager with the SCADA Engineer |

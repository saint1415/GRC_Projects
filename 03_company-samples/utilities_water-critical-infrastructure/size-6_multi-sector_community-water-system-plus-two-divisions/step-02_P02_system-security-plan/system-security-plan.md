# System Security Plan: Regional System 1 Water Treatment SCADA (RS1-SCADA)

**Organization:** Cris Santos Company Holdings, Inc., Water Utility division (Regional System 1), inheriting corporate shared services | **Tier:** Multi-Sector | **Vertical:** Water and Wastewater Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose **RS1-SCADA**, the focus division's primary system, because it supervises treatment for about 640,000 people (the largest of the 58 water systems), it inherits most of its identity, monitoring, and remote access controls from corporate (SYS-G1 to SYS-G4), and it is where the group's top cross-division risk lands: the shared OT remote access gateway reaches it, and Construction commissioning engineers use that gateway (P01 GR-01). The 13 other regional SCADA systems keep shorter SSPs that inherit from the same common control catalog (`common-control-catalog.csv`). Construction's CUI enclave (SYS-C2) has its own NIST SP 800-171 system security plan (P03).

## 1. System Name and Identifier
Regional System 1 Water Treatment SCADA (**RS1-SCADA**), identifier CSCH-WU-SYS-W1-RS1. Part of SYS-W1 in `../00_company-facts.md` section 3.

## 2. System Overview
RS1-SCADA monitors and controls treatment, pumping, and storage for Regional System 1 (Florida): **WTP-A** (surface water, 120 MGD), **WTP-B** (groundwater lime softening, 60 MGD), and **WTP-C** (groundwater nanofiltration, 30 MGD), plus 61 wells, 24 storage tanks, and 41 booster stations. Licensed operators run it 24x7 from the regional operations center (ROC) at WTP-A, with a backup control room at WTP-B.

**Major components:**
- Redundant SCADA servers at the ROC and the backup control room
- 46 operator HMIs and 3 engineering workstations
- A process historian, replicated every minute to the group data platform (SYS-G3) through the OT DMZ
- About 150 PLCs (chemical feed, filters, membranes, pumps) and about 290 RTUs at remote sites
- Licensed radio telemetry with private cellular as a second path
- OT network: business network, OT DMZ, ROC zone, plant cell zones, and telemetry zone, separated by firewalls (zones and conduits per NIST SP 800-82 Rev. 3)

**Engineered safeguards that do not depend on SCADA:** hardwired stroke limits on chemical feed pumps, independent hardwired pH and residual analyzer alarms to the control rooms, and fail-safe design (feed pumps stop and filters hold on loss of control signal).

**Change in progress:** the WTP-A 40 MGD membrane expansion, built and commissioned by the Construction division under an intercompany contract (completion 2027-06-30). Thirty-four commissioning engineers use the group gateway (SYS-G4) and connect company laptops (SYS-C3) to the WTP-A maintenance segment.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to RS1-SCADA |
|---|---|---|---|
| C-WATER-R01 | SDWA section 1433 risk and resilience assessment and emergency response plan | 42 U.S.C. 300i-2 | RS-1 serves more than 100,000 people. Its RRA must assess the resilience of "electronic, computer, or other automated systems (including the security of such systems)" (300i-2(a)(1)(A)(ii)); its ERP must include cybersecurity strategies and procedures (300i-2(b)(1)-(2)). Five-year RRA review certified 2025-03-26; ERP certified 2025-09-22 |
| SDWA public notification | Tier 1 public notice for a waterborne emergency, including a failure or significant interruption in key treatment processes | 40 CFR 141.202(a) Table 1 item (7), (b) | A cyber-caused loss of treatment can require notice and primacy agency consultation within 24 hours (P08) |
| SDWA reporting | Report failure to comply with a drinking water regulation within 48 hours; public notice certification within 10 days | 40 CFR 141.31(b), (d)(1) | Monitoring data lost during an outage can be a violation (P05 BP-W04) |
| C-WATER-R02 | CIRCIA (proposed 6 CFR Part 226) | 6 U.S.C. 681-681g | **Not in effect.** Tracked only; the system would be in scope through the water-sector criterion if the rule is finalized as proposed |
| SEC | Cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | An RS1-SCADA incident may be material to the group (P08) |
| State utility commissions | Rate regulation and any commission incident or reliability rules | Each state's commission rules (generic) | Handled by Water Utility regulatory affairs; not analyzed here |
| Contracts | Intercompany construction contract for the WTP-A expansion; SCADA integrator contract; telemetry carrier | Contract terms | The intercompany contract has **no OT security terms** (POAM-019 tracks the contract fix with the supplier assessment) |
| Internal | Group POL-01 to POL-05, the Water Utility supplement, and the group OT security standard | P06 | |

Not applicable: the Water Utility holds no federal contracts (FAR and DFARS clauses do not reach RS1-SCADA), and it handles no PHI.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the RS-1 Director of Operations (system owner) and the Water Utility security and compliance lead on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Water Utility president and the Group CISO (High risks co-accepted by the Group Chief Risk Officer).
- **Conditions:** (1) revoke the commissioning exception and require per-session approval and recording review for all Construction sessions by 2026-10-31 (POAM-002); (2) no commissioning change to WTP-A PLCs or HMIs outside RS-1 management of change, effective immediately (POAM-008); (3) replace or isolate the 6 end-of-support HMIs at WTP-C by 2027-03-31 (POAM-011).
- **Reauthorization:** annually, and when the WTP-A expansion is placed in service.

### 4.3 System Operational Status
Operational. **Major modification under way:** WTP-A membrane expansion (commissioning through 2027-06-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | RS-1 Director of Operations | Accountable for RS1-SCADA and this SSP |
| Authorizing official equivalent | Water Utility president with the Group CISO | Authorization decision |
| Technical lead | RS-1 SCADA engineering lead | Configuration, backups, OT network, PLC and HMI security |
| Process safety and water quality | Water Utility VP of Water Quality and Compliance | Public notice decisions; analyzer and sampling program |
| Division security | Water Utility security and compliance lead | Division supplement; exceptions; division register |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group OT Security Director (SYS-G4 and the OT security standard), Group HR director | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07) |
| RRA and ERP program | Water Utility Emergency Management Director | Keeps the RS-1 RRA and ERP current with this plan |

**Overlaps and how they are compensated.** The RS-1 SCADA engineering lead both configures and monitors OT systems; independent review comes from the group SOC (SYS-G2) and group internal audit. The Water Utility security and compliance lead approved the 2025 commissioning exception and also owns the division register; the exception is now reviewed by the Group OT Security Director (POL-01 4.10).

## 6. System Information Types and System Categorization
NIST SP 800-60 is written for federal mission areas and has no water treatment process type. The group defined its own information types and rated them with FIPS 199 definitions.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Process control and setpoints (PLC logic, chemical feed setpoints, commands) | Moderate | **High** | **High** | An unauthorized change to dosing, filtration, or pumping could harm public health for about 640,000 people; loss of control forces manual operation (P05 BP-W01 MTD 8 h) |
| Process and water quality data (historian, analyzer values, alarms) | Low | High | Moderate | Operators and compliance reporting rely on accurate values; historian RPO is 1 hour (P05 BP-W03) |
| System configuration and network information (diagrams, credentials, RRA content) | Moderate | Moderate | Low | Disclosure helps an attacker plan an intrusion |
| **RS1-SCADA category (high-water mark)** | **Moderate** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored with the OT overlay in NIST SP 800-82 Rev. 3, Appendix F. The plan documents **203 controls** in `control-implementation.csv`:
- 201 from the High baseline;
- PM-1 and PM-9, program management controls outside the security baselines (PM-9 is in the privacy baseline), added because the group risk strategy governs this system.

Other High-baseline controls are tailored out with reasons in the group tailoring register (PL-11). Examples: AC-10 (concurrent session limits would block shift handover on operator HMIs), and controls for capabilities the system does not have (public-facing content, mobile code in the HMI runtime). OT-specific tailoring is recorded in the implementation statements, for example AC-7 and AC-11 on operator HMIs in staffed control rooms, where a lockout could block an emergency action.

## 7. Authorization Boundary Description
- **Inside:** SCADA servers, HMIs, engineering workstations, historian, PLCs, RTUs, radios and cellular modems, the OT network devices and firewalls at the ROC, the three plants, and remote sites, the OT DMZ, and the WTP-A maintenance segment.
- **Outside, inherited (common control providers):** SYS-G1 identity platform (federation of the RS-1 OT directory for MFA), SYS-G2 SOC and OT monitoring sensors, SYS-G3 (historian replica, key management), and SYS-G4 OT remote access gateway.
- **Outside, interconnected:** the Water Utility business network, SYS-W3 LIMS (compliance data), the SCADA integrator, the telemetry carrier, and Construction commissioning laptops (SYS-C3) on the maintenance segment.

The diagram is in P04 `cloud-architecture.md` (the RS1-SCADA subgraph).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-G3 data platform (historian replica, AI-001) | Outbound through the OT DMZ every minute | Process and water quality data | Internal interconnection record (CA-3) |
| SYS-G4 OT remote access gateway | Inbound sessions | Operator, integrator, and commissioning sessions | Group OT security standard; per-session approval (**waived for commissioning**, POAM-002) |
| SYS-G2 SOC and OT sensors | Outbound (logs and network metadata) | Events and alerts | Group logging standard |
| SYS-C3 Construction commissioning laptops | Bidirectional on the WTP-A maintenance segment | PLC and HMI projects, test data | **No interconnection agreement**; intercompany contract has no security terms (POAM-019) |
| SCADA integrator | Inbound through SYS-G4 only | Support sessions | Integrator contract with security terms (2024) |
| SYS-W3 LIMS | Outbound (manual and scheduled exports) | Compliance results | Internal |

## 9. System Component Inventory
| Component | Type | Location | Owner |
|---|---|---|---|
| SCADA servers (primary and standby pairs) | Server | ROC (WTP-A); backup control room (WTP-B) | RS-1 SCADA engineering lead |
| Operator HMIs (46; 6 at WTP-C on an end-of-support OS) | Workstation | ROC, plants | RS-1 SCADA engineering lead |
| Engineering workstations (3) | Workstation | ROC, WTP-B | RS-1 SCADA engineering lead |
| Process historian | Server | OT DMZ | RS-1 SCADA engineering lead |
| PLCs (about 150) and RTUs (about 290) | Controllers | Plants and remote sites | RS-1 SCADA engineering lead |
| Telemetry radios and cellular modems | Network | Remote sites | RS-1 SCADA engineering lead |
| OT firewalls and switches | Network | All zones | RS-1 SCADA engineering lead with the Group OT Security Director |

The full asset inventory is held in the OT asset system (CM-8); about 8% of devices (the WTP-A expansion equipment) are not yet recorded (POAM-009).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (203 controls) and `common-control-catalog.csv` (112 group common control rows).

| Status | Controls |
|---|---|
| Implemented | 174 |
| Partially implemented | 29 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **203** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1 to SYS-G4, group functions, or group HR) | 92 |
| Hybrid (group provides the mechanism; RS-1 configures or operates part) | 16 |
| System-specific | 95 |

**The 29 partially implemented controls** cluster in four places:
- **The commissioning path** (scenario gap 1): AC-2, AC-2(12), AC-6, AC-17, AC-20(1), CA-3, CM-3, CM-8, CM-8(1), MA-4, PS-7, RA-3(1), SA-4, SA-9, SR-6.
- **WTP-C coverage:** CA-7, CP-4, RA-5, SA-22, SI-2, SI-4, SI-4(4), AU-6.
- **Cross-division incident response** (gap 6): IR-3, IR-6, IR-8.
- **Field and people:** AT-3 (OT role training at 71%), IA-5 (12 RTUs with default device credentials), PE-3 (9 booster stations without intrusion alarms).

### 10.2 Common control inheritance by division
The common control catalog lists 112 rows: 108 controls RS1-SCADA inherits fully or in part, plus 4 cloud platform controls (CP-6, CP-9, SC-7, SC-28) that other workloads inherit while RS1-SCADA keeps its own system-specific version. Inheritance is **documented for the Water Utility** (2025 inheritance matrix) and for RS1-SCADA (this plan). It is **not documented for Construction or Environmental Services** (scenario gap 7; POAM-015). Construction's CUI enclave (SYS-C2) cannot inherit SYS-G1 controls at all, because it runs in a separate identity tenant; its controls are documented in its own NIST SP 800-171 plan.

### 10.3 Control assessment status
Common controls were assessed once, and RS1-SCADA and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit, with site visits to the ROC, WTP-A, WTP-C, 6 RS-1 remote sites, and 4 acquired systems. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Operators and engineers** sign in with named accounts in the RS-1 OT directory. Engineering, privileged, and remote access require MFA through SYS-G1 federation and the gateway; privileged accounts are checked out from group PAM.
- **Control room HMIs** keep a continuously staffed shift session with named operator sign-in and no lockout, because a lockout could block an emergency action; physical access to the control rooms is the compensating control (PE-3, PE-6).
- **Vendors and commissioning engineers** use named gateway accounts with MFA. Per-session approval is required for everyone except the commissioning team covered by the 2025 exception (POAM-002).
- **No customers** access RS1-SCADA.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud and OT architecture and control map (P04), group and division risk registers (P01), gap analyses and the regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10), RS-1 RRA (2025) and ERP (2025).

## 13. Acronym List and Glossary
- **DMZ:** demilitarized zone (a buffer network between business and OT networks)
- **ERP:** emergency response plan (SDWA section 1433(b))
- **HMI:** human-machine interface
- **MOC:** management of change
- **OT:** operational technology
- **PLC / RTU:** programmable logic controller / remote terminal unit
- **ROC:** regional operations center
- **RRA:** risk and resilience assessment (SDWA section 1433(a))
- **Zones and conduits:** network segments grouped by function and trust, connected only through defined, controlled paths (NIST SP 800-82 Rev. 3)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | RS-1 SCADA engineering lead |
| 1.0 | 2026-09-15 | Approved with authorization conditions | RS-1 Director of Operations |

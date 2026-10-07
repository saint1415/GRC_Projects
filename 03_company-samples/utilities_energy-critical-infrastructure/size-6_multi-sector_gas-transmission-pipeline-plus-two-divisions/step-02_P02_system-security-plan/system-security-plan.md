# System Security Plan: Pipeline SCADA and Gas Control System (PSGCS)

**Organization:** Cris Santos Company Holdings, Inc., Gas Transmission division (inherits common controls from corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Energy
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), with OT guidance from NIST SP 800-82 Rev. 3 | **Version:** 1.0, 2026-09-22

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the focus division's primary system, the **Pipeline SCADA and Gas Control System**, because it operates the 7,400-mile interstate system that TSA has designated as critical, it is the core of the Critical Cyber Systems in the TSA implementation plan, and it sits at the center of the top group risks (P01 GR-01 and GR-02): the business services it depends on and the shared remote access path into it are both corporate. It inherits most IT controls from corporate (SYS-G1 to SYS-G3). The other divisions keep their own system plans that inherit from the same common control catalog (`common-control-catalog.csv`): the Gathering and Production field SCADA plan and the Integrity Data Platform plan that supports its SOC 2 report.

## 1. System Name and Identifier
Pipeline SCADA and Gas Control System (**PSGCS**), identifier CSCH-GT-PSGCS. It covers SYS-T1, SYS-T2, SYS-T3, and SYS-T6 in `../00_company-facts.md` section 3.

## 2. System Overview
The PSGCS monitors and controls the Gas Transmission system: about 7,400 miles of pipeline, 41 compressor stations, about 640 meter and regulator stations, and about 410 remote-control valve sites in six states. It supports:
- **Gas control:** about 90 controllers at the primary Gas Control Center (Florida) and the Backup Gas Control Center (Louisiana) monitor pressures, flows, and line pack, start and stop compressors, and operate remote-control valves (P05 BP-T01).
- **Compressor stations:** station control PLCs, unit control panels, and station HMIs (BP-T02). Station emergency shutdown is hardwired and does not depend on the PSGCS.
- **Emergency response:** rupture identification and remote valve closure under the emergency plan (49 CFR 192.615; BP-T03).
- **Data for the business:** flow computer data passes through the central OT DMZ to gas measurement (SYS-T4), which feeds nominations and scheduling (SYS-T5). Historian data is replicated one way to the group data platform (SYS-G6).
- **Advisory analytics:** the leak-detection anomaly model scores data on a server in the central DMZ (BP-T06; P10).

**Major components:**
- **SCADA hosts and historians** (redundant at the primary center; hot standby at the backup center), with computational pipeline monitoring
- **Controller consoles and engineering workstations** at both gas control centers
- **OT DMZs:** one central and two regional (historian brokers, patch and antivirus relays, PAM session landing, leak-detection scoring server)
- **Station and field control:** station PLCs, unit control panels, and station HMIs at 41 stations; about 2,300 RTUs, PLCs, and flow computers
- **Communications:** private microwave and MPLS network with satellite backup at every station
- **Physical access control and video** at both centers and all stations (SYS-T6)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the PSGCS |
|---|---|---|---|
| C-ENERGY-R03 | TSA Security Directive Pipeline-2021-02G | SD Pipeline-2021-02G (effective 2026-05-03 through 2027-05-02), issued under 49 U.S.C. 114 | **Applies.** TSA notified the division that its pipeline system is critical. The PSGCS components are Critical Cyber Systems in the TSA-approved implementation plan, which sets the measures TSA inspects against (Sections II.B and III.A to III.E). The incident response plan (III.F) and assessment plan (III.G) cover it |
| C-ENERGY-R02 | TSA Security Directive Pipeline-2021-01G | SD Pipeline-2021-01G (effective 2026-01-16 through 2027-01-15) | **Applies.** Cybersecurity Coordinator and alternates available 24/7 (II.B); report cybersecurity incidents to CISA as soon as practicable and no later than 72 hours after identification (II.C) |
| C-ENERGY-R04 | PHMSA control room management | 49 CFR 192.631 | **Applies in full.** Controllers monitor and control the pipeline through SCADA from control rooms, and the system has compressor stations, so the reduced-procedure exception in 192.631(a)(1)(ii) does not apply |
| PHMSA 192.605, 192.615 | O&M manual and emergency plans | 49 CFR 192.605; 192.615 | The 192.631 procedures must be integrated with them (192.631(a)(2)); emergency shutdown capability (192.615(a)(6)) |
| PHMSA 191.5 | Incident notice | 49 CFR 191.5 | Telephonic notice no later than 1 hour after confirmed discovery of an incident, including events significant in the operator's judgment (191.3) |
| SSI 1520 | Sensitive Security Information | 49 CFR Part 1520; SD 02G Section IV.B | Plans, reports, and assessment results required by the directive are SSI and must be stored and transmitted under Part 1520 |
| FERC 260.9 | Service interruption reports | 18 CFR 260.9 | Serious interruptions of service and damage that reduces throughput are reported to FERC at the earliest feasible time (P08) |
| CEII | Critical energy infrastructure information | 18 CFR 388.113 | System flow diagrams filed with FERC (Form 567) are submitted with CEII treatment requested |
| N55-R01, N55-R02 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A PSGCS incident may be material to the group (P08) |
| C-ENERGY-R05 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | Tracked only. Not in effect |
| Internal | Group policies POL-01 to POL-05 and the Transmission supplement | P06 | |

**Not applicable:** NERC CIP (no Bulk Electric System assets or NERC registration); 49 CFR 195.446 (no hazardous liquid pipelines); USCG 33 CFR Part 101 Subpart F (no MTSA facilities).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Vice President of Gas Control (system owner) and the Group CISO on 2026-09-22, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. TSA does not authorize systems either; it approves the implementation plan and inspects against it. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-22, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks), with the Gas Transmission president.
- **Conditions:** (1) notify TSA of the station panel password schedule slip and file an amendment request by 2026-10-30 (POAM-008); (2) complete the architecture design review by 2026-12-15 (POAM-009); (3) move SYS-T4 measurement servers off the corporate directory into a dedicated enclave by 2027-06-30, with an interim block on directory administrator logons to those servers by 2026-10-31 (POAM-007); (4) no change to leak-detection model thresholds without control room management of change (POAM-010, POAM-026).
- **Reauthorization:** annually, aligned with the TSA assessment plan cycle.

### 4.3 System Operational Status
Operational. **Major modifications planned:** measurement enclave (2027-06-30); OT sensors at the remaining 5 stations (2027-03-31); replacement of 14 unsupported station HMIs (2027-09-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Vice President of Gas Control | Accountable for the PSGCS and this SSP; agrees to any risk decision affecting pipeline safety |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| TSA Cybersecurity Coordinator | Director of Pipeline Cybersecurity (primary); Group OT Security Director and the SOC OT desk manager (alternates) | TSA and CISA point of contact 24/7 (SD 01G II.B); owner of the TSA implementation and assessment plans |
| Control room management | Director of Gas Control | 192.631 procedures, alarm management, controller training |
| Technical owner | SCADA Engineering Manager | Configuration, change control, point-to-point verification |
| Pipeline safety | Pipeline Safety Compliance Director | Emergency plan integration; PHMSA notices |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group network and cloud platform director (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit; an outside firm for the TSA architecture design review | Assess common and PSGCS controls (P07) |

## 6. System Information Types and System Categorization
The group consulted the energy information types in NIST SP 800-60 Vol. 2 Rev. 1 and set its own ratings, as the publication allows for non-federal use. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Pipeline operations data: pressures, flows, setpoints, alarms, station logic | Moderate | **High** | **High** | Altered setpoints or suppressed alarms could cause an overpressure or a missed rupture; firm supply to 46 local distribution companies and 58 power plants depends on it. Hardwired station shutdowns limit but do not remove the worst case |
| Measurement and custody data passed to SYS-T4 | Low | **High** | Moderate | Wrong volumes misstate deliveries and imbalances for about 340 shippers |
| Security information: TSA plan content, zone diagrams, firewall rules (SSI and CEII) | **High** | Moderate | Low | Disclosure would help an attacker plan an attack on critical infrastructure; SSI and CEII handling rules apply |
| Information security (keys, accounts, logs) | High | High | Moderate | Compromise would open the OT DMZs |
| **PSGCS category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored with the SP 800-82 Rev. 3 OT overlay. The plan documents **133 controls** in `control-implementation.csv`:
- 128 from the High baseline;
- 2 added for OT safety (CP-12 safe mode and SI-17 fail-safe procedures), because hardwired station shutdowns and the manual operation plan are what cap the worst case;
- 3 program management controls not allocated to a baseline (PM-1, PM-2, PM-9).

Other High-baseline controls are either fully inherited from cloud and SaaS providers (evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register. The OT overlay is applied where operations cannot support a control as written, for example console lockout and session lock (AC-7, AC-11, compensated by a staffed, badge-controlled control room) and device authentication on legacy serial protocols (IA-3, compensated by network isolation).

CSF 2.0 subcategories in `control-implementation.csv` come from NIST's official CSF 2.0 to SP 800-53 crosswalk. For 16 controls that NIST does not map (AC-8, AC-11, AU-8, CA-6, CP-3, CP-12, IR-2, MA-4, MA-5, MP-2, MP-6, MP-7, PL-4, PS-3, PS-4, SI-17), the subcategory is an author mapping.

## 7. Authorization Boundary Description
- **Inside:** SYS-T1 (SCADA hosts, historians, consoles, and engineering workstations at both gas control centers); SYS-T2 (station and field control devices and the private microwave and MPLS network); SYS-T3 (central and regional OT DMZs, including the leak-detection scoring server); SYS-T6 (physical access control and video at centers and stations).
- **Outside, inherited (common control providers):** SYS-G1 identity platform, PAM, and the OT remote access gateway; SYS-G2 SOC, SIEM, SOAR, EDR, and OT monitoring console; SYS-G3 network, data centers, and backup vault.
- **Outside, interconnected:** SYS-T4 gas measurement (receives flow computer data through the central DMZ); SYS-T5 nominations (receives volumes from SYS-T4, not from SCADA); SYS-G6 group data platform (historian replica); SYS-E1 Integrity Data Platform (integrity records, through SYS-G6 exports); SCADA and station control vendors through the gateway.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-T4 gas measurement | Outbound flow computer data through the central DMZ broker | Measured volumes and gas quality | Zone model in the TSA implementation plan. **Gap:** the measurement servers are corporate-directory members (POAM-007) |
| SYS-G6 group data platform | Outbound one-way historian replica | Process history | Group OT data standard |
| SYS-E1 Integrity Data Platform | Outbound exports from SYS-G6 (pressure history for integrity analyses) | Process history extracts | Intercompany service agreement (2024). **Gap:** the IDP also holds Transmission SSI without SSI controls (POAM-019) |
| SYS-G1 OT remote access gateway | Inbound PAM sessions to the DMZ landing servers | Administrative and vendor sessions | Group OT access standard; **shared by three divisions** (POAM-001) |
| Gathering and Production interconnects | Measurement data at 6 receipt points | Volumes and gas quality | Interconnect operating agreements |
| Interconnected pipelines and customers | Telemetry at about 30 interconnects | Pressures and flows | Interconnect operating agreements |
| TSA and CISA | Outbound | Plans, assessment reports, incident reports (SSI) | SD 01G and 02G |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SCADA hosts, historians, computational pipeline monitoring | On-premises servers (redundant; hot standby) | Primary and backup gas control centers | SCADA Engineering Manager |
| Controller consoles and engineering workstations | Workstations | Both gas control centers | SCADA Engineering Manager |
| OT DMZs (central and two regional) | Servers and firewalls | Primary center; two regional hubs | Group OT Security Director |
| Station control systems | PLCs, unit control panels, station HMIs (14 HMIs on an unsupported OS, POAM-012) | 41 compressor stations | Vice President of Gas Control |
| Field devices (about 2,300) | RTUs, PLCs, flow computers | Meter, regulator, valve, and interconnect sites | Vice President of Gas Control |
| Private microwave and MPLS network, satellite backup | Communications | System-wide | Group network and cloud platform director (operation); SCADA Engineering Manager (OT use) |
| Physical access control and video | On-premises | Centers and stations | Vice President of Gas Control |

The OT inventory is built from passive sensors at 36 of 41 stations and quarterly manual surveys at the other 5 (POAM-003).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (133 controls) and `common-control-catalog.csv` (90 group common controls inherited by the PSGCS, fully or as hybrids).

| Status | Controls |
|---|---|
| Implemented | 116 |
| Partially implemented | 17 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **133** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, or group functions) | 47 |
| Hybrid (group provides the mechanism; the division configures or operates part) | 44 |
| System-specific | 42 |

**The 17 partially implemented controls** cluster in four places:
- **Business services that ride on corporate IT** (scenario gap 1): SC-7, CP-2, CP-4.
- **TSA implementation plan schedule and assessment** (gap 5): IA-5, AC-2, CA-2, SI-2, SA-22.
- **Shared access paths and data held elsewhere** (gaps 2 and 3): AC-17, SA-9.
- **Control room records, monitoring, and incident governance** (gaps 6 and 8): CM-3, AT-3, AU-6, AU-11, SI-4, IR-3, IR-6.

### 10.2 Common control inheritance by division
The common control catalog lists 90 controls provided by corporate. Inheritance is **documented for Gas Transmission** (an inheritance annex to the TSA implementation plan, because TSA inspects the measures whoever operates them) and for **Integrity Services** (its SOC 2 system description carves in the group services). It is **not documented for Gathering and Production** (scenario gap 7). Until POAM-017 closes, Gathering cannot show which of its field SCADA controls are met by group services, and P07 found CA-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and PSGCS and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit, with OT tests at Compressor Station 27 on 2026-08-12. See P07 `assessment-results.csv` and `poam.csv`. Separately, the TSA assessment plan schedules 96 measures for 2026-2027; the P07 results are recorded as evidence for 21 of them.

## 11. Digital Identity Acceptance Statement
- **Business and gateway users** authenticate through SYS-G1 federated sign-in with MFA. **Administrators** of SCADA servers and the OT DMZs use phishing-resistant MFA and just-in-time PAM elevation through the gateway.
- **Controllers** sign in to consoles with named local SCADA accounts tied to SYS-G1 identifiers, so control does not depend on SYS-G1. MFA is not used on control room consoles; the TSA plan documents the compensating controls the directive allows for control room workstations under Part 192: a staffed room with badge and PIN entry, video, and console allowlisting (SD 02G III.C.2).
- **Compressor unit control panels** at 11 stations still use shared local accounts (POAM-008).
- **Vendors and Integrity Services engineers** authenticate as named identities in SYS-G1 before reaching PAM.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10). The TSA implementation plan, assessment plan, and incident response plan are SSI and are referenced by section number only.

## 13. Acronym List and Glossary
- **CEII:** critical energy infrastructure information (18 CFR 388.113)
- **Common control:** a control provided once by corporate and inherited by several systems
- **Critical Cyber System:** an IT or OT system or data whose compromise could result in operational disruption, including business services (SD 02G Section VII)
- **ESD:** emergency shutdown
- **HMI:** human-machine interface
- **OT DMZ:** the buffer network between corporate IT and OT
- **PAM:** privileged access management
- **PSGCS:** Pipeline SCADA and Gas Control System
- **RTU, PLC:** remote terminal unit, programmable logic controller
- **SSI:** Sensitive Security Information (49 CFR Part 1520)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Vice President of Gas Control |
| 1.0 | 2026-09-22 | Approved with authorization conditions | Group CISO |

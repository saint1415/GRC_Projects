# System Security Plan: Water Treatment SCADA System (WTSS)

**Organization:** Cris Santos Company, LLC (privately held community water system, 2,850 population served) | **Tier:** Micro | **Vertical:** Water and Wastewater Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), with OT guidance from NIST SP 800-82 Rev. 3 | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Water Treatment SCADA System (**WTSS**), identifier CSC-OT-001.

## 2. System Overview
The WTSS monitors and controls drinking water production and delivery for 2,850 people. It runs 3 wells, the aerator, sodium hypochlorite disinfection, 3 high-service pumps, the 300,000-gallon ground tank, and the 150,000-gallon elevated tank. Operators supervise it from the plant control room on weekday day shift. At other times the on-call operator receives alarms by phone and can view and operate the HMI remotely.

The company is a 7-person business with no IT staff. The SCADA integrator built and supports the control system, an MSP runs the office IT that shares the plant network, and a remote monitoring vendor delivers alarms and trend history from its cloud service. This plan says, for each control, what the company does itself and what it relies on a contractor or vendor for.

**Major components:**
- **SYS-01:** the SCADA HMI computer in the control room (HMI, local historian, alarms, and the PLC programming software)
- **SYS-02:** the plant PLC and RTUs at Well 3 and the elevated tank
- **SYS-03:** cellular modems at Well 3 and the elevated tank
- **SYS-04:** the remote desktop tool on SYS-01, relayed by the tool vendor's cloud service
- **SYS-12:** the standalone cellular alarm dialer
- **Plant network segment:** the switch shared with the office (part of SYS-09)
- **SYS-05 functions:** the edge gateway that sends PLC values to the remote monitoring service, and the alarm call-out and mobile app

**Engineered safeguards outside the software.** The hypochlorite pump's mechanical stroke setting caps its output at about 2.5 times the normal rate. The chlorine analyzer's own high and low relays call the on-call phone through the alarm dialer. Every well, pump, and the chemical feed has a hand-off-auto switch. SCADA cannot override any of these. They are documented as SC-24 (fail in known state) and are the main reason no WTSS risk is rated Very High (P01).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| Federal | SDWA public notification rule: a failure or significant interruption in key water treatment processes is a waterborne emergency that requires a Tier 1 notice and primacy agency consultation within 24 hours | 40 CFR 141.202(a) Table 1 item (7); 141.202(b) |
| Federal | Ground Water Rule compliance monitoring: the company monitors the residual disinfectant continuously, so it must record the lowest residual each day, grab-sample every 4 hours if the analyzer fails, and resume continuous monitoring within 14 days. The WTSS holds that record | 40 CFR 141.403(b)(3)(i)(A)-(B) |
| Federal | Reporting a failure to comply with a drinking water regulation within 48 hours; record retention | 40 CFR 141.31(b); 141.33 |
| Federal | Tampering with a public water system, including interfering with its operation with the intention of harming persons, is a federal crime. Relevant to a law enforcement referral after an attack | 42 U.S.C. 300i-1 |
| C-WATER-R01 | SDWA section 1433 RRA and ERP. **Does not apply** (2,850 persons served; the threshold is more than 3,300). Used as a readiness reference because a new subdivision may take the system past 3,300 by about 2029 | 42 U.S.C. 300i-2 |
| C-WATER-R02 | CIRCIA (proposed, not in effect). Tracked only. As proposed, the company would not be covered: it is SBA-small and serves fewer than 3,300 people | 6 U.S.C. 681-681g; proposed 6 CFR Part 226 |
| State | Florida Information Protection Act, for customer data that reaches the WTSS only if an attacker moves from the plant network to office systems | Fla. Stat. 501.171 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable: wastewater (POTW) requirements; federal contract clauses (no federal contracts).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner and General Manager on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner and General Manager accepted continued operation of the WTSS, because the plant cannot be shut down and because hand operation and the engineered safeguards limit the worst outcomes. The conditions are the P07 POA&M dates and the treatment plans for the 4 High risks in P01, 3 of which (R-001, R-004, R-006) are due by 2026-10-31.

### 4.3 System Operational Status
Operational. Planned changes: remote access rebuilt with named accounts, MFA, and per-session approval (2026-09-30); separate OT network (2026-11-30); HMI computer patch plan with the integrator (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operator | Accountable for WTSS operation, changes, HMI and PLC credentials, and the integrator's work |
| Risk acceptor (authorizing official equivalent) | Owner and General Manager | Accepts Moderate and higher risk; approves this plan, policies, and spending |
| Security and compliance coordinator | Office Manager | Maintains this plan, the risk register, policies, and the incident log; manages the MSP |
| Operators | 2 Operators | Hand operation, on-call alarm response, daily checks |
| Contractor | SCADA integrator | PLC and HMI programming and remote support, under the company's rules (POL-02 B.7) |
| Contractor | MSP | Office firewall, Wi-Fi, office computers; separate OT network work under a contract addendum (2026-11-30) |
| Vendor | Remote monitoring vendor | Cloud alarm and trend service (SOC 2 report reviewed in P09) |
| Independent assessor | OT security consultant | Control assessment (P07) |

**Overlapping roles.** In a 7-person company the Chief Operator both runs the SCADA system and decides its security, and the Owner both approves spending and accepts the risk. The compensating checks are the independent consultant's assessment (P07), the Office Manager's monthly POA&M review with the Owner, and the remote monitoring vendor's SOC 2 report (P09).

## 6. System Information Types and System Categorization
NIST SP 800-60 is written for federal mission areas and has no water treatment process type. The company defined its own information types and rated them with FIPS 199 definitions.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Process control and setpoints (PLC program, chlorine pump pacing, pump commands) | Moderate | **High** | **High** | An unauthorized change to chlorine feed or pumping could harm public health; loss of control forces hand operation (P05 BP-01 MTD 12 h) |
| Process and compliance data (chlorine residual record, tank levels, alarms) | Low | **High** | Moderate | The daily lowest residual is compliance data under 40 CFR 141.403(b)(3); grab sampling covers short outages (P05 BP-04) |
| System configuration and network information (drawings, addresses, passwords) | Moderate | Moderate | Low | Disclosure helps an attacker plan an intrusion |
| **WTSS category (high-water mark)** | **Moderate** | **High** | **High** | |

**Baseline:** the NIST SP 800-53B High baseline, tailored with the **OT overlay in SP 800-82 Rev. 3, Appendix F**, and scaled for a 7-person water system. The plan documents 38 controls that carry core OT hygiene and the binding drinking water duties (see `control-implementation.csv`). All other High-baseline controls are handled one of three ways:
- **Inherited or provided** by a vendor or contractor (for example the remote desktop tool vendor's session encryption, the SaaS vendors' platform controls), recorded as Hybrid where the company still has a part to play.
- **Tailored with OT compensating controls** where the overlay allows it (for example AC-11 session lock on the HMI, which must stay visible in a staffed control room).
- **Tailored out for this tier**, where the control assumes dedicated IT staff or federal program management (for example separate development environments or a configuration control board). These are tailoring decisions, not gaps.

## 7. Authorization Boundary Description
- **Inside:** the HMI computer, the plant PLC, both RTUs, both cellular modems, the alarm dialer, the plant network switch and the office firewall's role in protecting it, the remote desktop tool installed on SYS-01, and the SYS-05 edge gateway.
- **Outside (interconnected):** the office computers on the same network (SYS-09; a gap until the OT network is separated), the remote desktop tool vendor's relay, the remote monitoring vendor's cloud service, the cellular carrier, the integrator's laptop and network, and the MSP's remote management platform.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Remote desktop tool relay (SYS-04) | Inbound remote sessions | Full control of the HMI computer | Tool vendor's standard terms; integrator time-and-materials contract (**no security terms, gap**) |
| Remote monitoring service (SYS-05) | Outbound process values; inbound alarm acknowledgements | Process and compliance data | Vendor subscription terms (**no security terms, gap**); setpoint write-back turned off |
| Cellular carrier | Bidirectional | Well 3 and tank telemetry | Carrier business data plan (public addresses, **gap**) |
| Office network (SYS-09) | Shared switch | All traffic (**flat network, gap**) | MSP contract (excludes plant control systems) |
| Primacy agency | Outbound | Monthly operating reports, notices | State rules |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| SCADA HMI computer (SYS-01) | Workstation (updates not applied since May 2024, **gap**) | Plant control room | Chief Operator |
| Plant PLC (SYS-02) | Controller (no program password; key switch in remote-program, **gap**) | Plant control panel | Chief Operator |
| RTUs (SYS-02) | Controller | Well 3; elevated tank | Chief Operator |
| Cellular modems (SYS-03) | Telemetry | Well 3; elevated tank | Chief Operator |
| Remote desktop tool (SYS-04) | Software and vendor relay | On SYS-01; tool vendor's cloud | Chief Operator |
| Edge gateway (SYS-05) | Network appliance | Plant control panel | Chief Operator |
| Alarm dialer (SYS-12) | Standalone cellular dialer | Plant building | Chief Operator |
| Network switch and office firewall (SYS-09) | Network | Plant building | Office Manager (MSP operates) |

A full inventory with firmware versions and network addresses is due 2026-10-31 (CM-8).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 38 controls:
- Implemented: 6
- Partially implemented: 21
- Planned: 11
- Not applicable: 0

By responsibility: 27 system-specific (the company), 11 hybrid (the company with the MSP or a vendor), 0 fully inherited.

### 10.2 Controls provided by contractors and vendors
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| MSP | Office firewall (SC-7, CM-7), office patching and antivirus (SI-2, SI-3), office backup (CP-9) | Monthly MSP report; P07 evidence requests | Extend the contract to the OT network separation; approve firewall changes; get MFA on the MSP-held firewall login |
| Remote monitoring vendor | Alarm call-out and trend history (SI-4, CP-9), platform security | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Its complementary user entity controls: named users, MFA, gateway settings with write-back off, user review |
| Remote desktop tool vendor | Session encryption and relay (AC-17), connection history (AU-2) | Vendor documentation | Everything else: accounts, MFA, approval, log review |
| SCADA integrator | PLC and HMI expertise; the only rebuild capability today (CP-10) | None | Security terms; company-held backups; approved and watched sessions |

**Provided does not mean done.** The MSP contract excludes plant control systems, so the HMI computer gets no patching or malware protection from anyone (SI-2, SI-3). Fixing that is a contract decision for the Owner, not a technical one.

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent OT security consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Remote access to the HMI** can change treatment, so it needs the strongest assurance the company can support: named accounts and MFA for every operator and integrator technician, with the integrator's sessions approved by the Chief Operator each time (target 2026-09-30).
- **Operators in the control room** will use named HMI accounts with passwords (target 2026-12-31). The locked, alarmed building is a compensating control, and the HMI stays unlocked for alarm response, as the SP 800-82 Rev. 3 OT overlay allows.
- **Device credentials** (PLC, modems, gateway) are changed from defaults and kept in a password manager that only the Owner, Office Manager, and Chief Operator can open, not in a shared spreadsheet (POL-02 B.9).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor report review (P09), AI assessment (P10), 2023 emergency plan, 2018 integrator as-builts, 2025 sanitary survey report.

## 13. Acronym List and Glossary
- **HMI:** human-machine interface
- **MFA:** multi-factor authentication
- **MGD:** million gallons per day
- **MSP:** managed service provider
- **OT:** operational technology
- **PLC:** programmable logic controller
- **RTU:** remote terminal unit
- **SCADA:** supervisory control and data acquisition
- **WTSS:** Water Treatment SCADA System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office Manager with the Chief Operator |

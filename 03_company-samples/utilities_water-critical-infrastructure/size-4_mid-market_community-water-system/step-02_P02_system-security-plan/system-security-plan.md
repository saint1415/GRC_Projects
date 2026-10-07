# System Security Plan: Integrated Water Operations SCADA (IWOS)

**Organization:** Cris Santos Company, Inc. (PE-backed investor-owned water utility) | **Tier:** Mid-Market | **Vertical:** Water and Wastewater Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), with OT guidance from NIST SP 800-82 Rev. 3 | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Integrated Water Operations SCADA (**IWOS**), identifier CSC-OT-IWOS-01. The IWOS is the company's major system. It comprises SYS-01 to SYS-06 in `../00_company-facts.md`.

## 2. System Overview
The IWOS monitors and controls drinking water production and delivery for 273,900 people in 11 community water systems, and gives the Regional Operations Center (ROC) read-only monitoring of 3 municipal clients' plants. Licensed operators supervise it 24 hours a day from the ROC. The Regional System plants (WTP-R1 and WTP-R2) and WTP-L1 are staffed around the clock, WTP-G1 is staffed 16 hours a day, and WTP-G2 and the 8 small systems are monitored remotely and visited by roving operators.

**Major components:**
| ID | Component | Hosting |
|---|---|---|
| SYS-01 | Regional SCADA (platform A, 2021): redundant servers at the ROC, standby server at WTP-R2, 14 HMI stations, 2 engineering workstations, historian, alarm notification server | On-premises |
| SYS-02 | 41 PLCs (including all chemical feed control) and 75 RTUs at wells, boosters, and tanks | Plants and remote sites |
| SYS-03 | Licensed radio, plant-to-plant fiber, and 25 cellular modems on a private carrier network | Radio and carrier networks |
| SYS-04 | OT remote access: the Regional gateway (MFA, approval, recording), the Lakes and Ridge site-to-site VPNs, the Lakes on-call VPN, and Integrator B's remote desktop agent at Ridge | On-premises appliances; vendor cloud relay for the agent |
| SYS-05 | Lakes SCADA (platform B, 2016) and Ridge SCADA (legacy platform, 2014; unsupported operating system) | On-premises |
| SYS-06 | OT networks: segmented Regional control networks and OT DMZ; flat control networks at WTP-L1 and WTP-G1; passive monitoring sensors at WTP-R1 and WTP-R2 | On-premises |

**Engineered safeguards outside the software.** Chemical feed pumps at every plant have hardwired stroke limits, and chlorine and pH analyzers have hardwired high/low alarms. Operators can run every process in manual (local) mode. SCADA cannot override these safeguards. They are documented as SC-24 (fail in known state) and are the main reason no IWOS risk is rated Very High in P01.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the IWOS |
|---|---|---|---|
| C-WATER-R01 | SDWA section 1433 risk and resilience assessment and emergency response plan, for the Regional, Lakes, and Ridge Systems (each certified separately by PWSID) | 42 U.S.C. 300i-2(a)(1)(A)(ii)-(iii), (vi); (b)(1)-(4); (c) | The IWOS is the main "electronic, computer, or other automated system" in all 3 RRAs. Its protection and recovery are part of each ERP's cybersecurity strategies and procedures |
| C-WATER-R02 | CIRCIA (proposed, not in effect) | 6 U.S.C. 681-681g; proposed 6 CFR Part 226 | Tracked only. If finalized as proposed, covered cyber incidents would be reported to CISA within 72 hours |
| Federal | SDWA public notification rule | 40 CFR 141.201, 141.202, 141.205 | A failure or significant interruption in key treatment processes can require a Tier 1 notice within 24 hours; the wholesale city (a consecutive system) must be notified |
| Federal | Ground Water Rule compliance monitoring and reporting | 40 CFR 141.403(b)(3); 141.405(a)(1) | Continuous residual monitoring depends on IWOS analyzers; failures require grab samples every 4 hours, and a residual below the state minimum not restored within 4 hours must be reported by the end of the next business day |
| Federal | Tampering with a public water system | 42 U.S.C. 300i-1 | Unauthorized control actions are a federal crime; drives law enforcement referral (P08) |
| Contract | Utility Services agreements with 3 municipal clients | Contract | ROC alarm acknowledgment within 15 minutes; incident notice within 24 hours; SOC 2 Type 2 from 2027 (P09) |
| Internal | POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable: wastewater (POTW) requirements; federal contract clauses; HIPAA; SEC disclosure rules (privately held); EPA Risk Management Program (no listed substance above threshold). Customer data in the CIS (Fla. Stat. 501.171) is outside this boundary and covered in P03 and P08.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07), and presented to the audit committee the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the IWOS accepted with conditions, 2026-09-15. The plants cannot be shut down, and manual operation plus the hardwired safeguards limit the worst outcomes.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones, starting with removal of the Ridge remote desktop agent and MFA on the Lakes VPN by 2026-10-31; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (including any new acquisition).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Ridge and Lakes remote access moved to the gateway (2026-10-31)
- Site-to-site VPN rules restricted to named flows, and Ridge SCADA isolated behind a dedicated firewall (2026-12-31)
- OT DMZ and segmentation at WTP-L1 and WTP-G1, and passive monitoring at both (2027-06-30)
- Ridge SCADA replacement on a supported platform (2027 capital plan)
- Alternate ROC position at WTP-R2 (2027-06-30)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the IWOS; accepts Moderate risk; signs the EPA certifications |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber and resilience reporting |
| Program strategy | vCISO (part-time contractor) | Strategy, audit committee reporting, SSP review |
| Security officer | IT Director | Day-to-day program owner; IT/OT boundary, remote access, identity |
| Security operations and GRC | Security Manager, 2 security analysts (one OT), GRC analyst | Monitoring, vulnerability management, MSSP liaison, POA&M |
| Operations owner | Director of Water Operations | Day-to-day SCADA operations at all plants and the ROC |
| OT engineering | SCADA and Controls Engineering Manager and 18 staff | PLC and HMI configuration, OT backups, change control, integrator oversight |
| Control room | ROC Supervisor | Approves vendor sessions at Regional; first response to OT alarms |
| RRA and ERP lead | Emergency Management and Resilience Manager | RRAs and ERPs for the 3 covered systems; LEPC coordination |
| Independent assessment | Co-sourced internal audit firm | Annual IT and OT audit; P07 assessment |
| Monitoring | MSSP | 24x7 IT monitoring; receives Regional OT sensor alerts |
| Contractors | Integrator A (Regional); Integrator B (Lakes and Ridge) | Programming and support under the company's rules |

**Where roles overlap.** The SCADA and Controls Engineering Manager both configures OT systems and owns their backups and change control; the Security Manager's OT analyst reviews changes monthly, and the co-sourced internal audit firm tests them yearly. The vCISO sets strategy and reports to the audit committee but does not operate controls.

## 6. System Information Types and System Categorization
SP 800-60 is written for federal mission areas and has no water treatment process type. The company defined its own information types and rated them with FIPS 199 definitions.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Process control and setpoints (PLC logic, chemical feed setpoints, commands) | Moderate | **High** | **High** | An unauthorized change to dosing or pumping could harm public health; loss of control forces manual operation of up to 11 systems (P05 BP-01 MTD 8 h) |
| Process and water quality data (historian, analyzer values, alarms) | Low | High | Moderate | Operators and compliance reporting rely on accurate values; continuous residual monitoring is a Ground Water Rule requirement |
| System configuration and network information (diagrams, IP plans, credentials, RRA content) | Moderate | Moderate | Low | Disclosure helps an attacker plan an intrusion |
| Client monitoring data (read-only views of 3 municipal plants) | Moderate | Moderate | High | Contract alarm response within 15 minutes (P05 BP-09 MTD 4 h) |
| **IWOS category (high-water mark)** | **Moderate** | **High** | **High** | |

**Why High, when the tier guide expects a Moderate system.** The Mid-Market tier guide expects a major system of Moderate impact. The IWOS is rated High for integrity and availability because the potential impact of an unauthorized chemical feed change is harm to people, which FIPS 199 places at High regardless of company size. The hardwired safeguards reduce the likelihood of harm (P01), but categorization is based on potential impact before controls.

## 7. Authorization Boundary Description
**Inside the boundary:**
- SCADA servers, HMIs, engineering workstations, and historians at Regional, Lakes, and Ridge;
- 41 PLCs and 75 RTUs, including small-system well controllers;
- radios, fiber, and 25 cellular modems;
- OT switches and the OT side of the IT/OT firewall at every plant;
- the OT DMZ (historian replica, patch server, remote access gateway);
- the site-to-site VPN endpoints and the Lakes on-call VPN appliance;
- the vendor remote access path at Ridge (agent today, gateway after 2026-10-31);
- passive OT monitoring sensors.

**Outside the boundary (external services, interconnected):**
- the business network and endpoints (SYS-15);
- the cloud landing zone with the historian replica and analytics (SYS-07);
- the identity provider (SYS-08), used for gateway MFA;
- the MSSP and SIEM (SYS-16);
- Integrator A's and Integrator B's own networks;
- the cellular carrier network;
- the 3 municipal clients' SCADA systems (read-only links).

The diagram is in P04 `cloud-architecture.md`, which shows the OT zones, the OT DMZ, and their connections to the cloud and SaaS.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Business network (SYS-15) through the IT/OT firewall | Outbound historian data to the DMZ; inbound gateway sessions | Process data; remote sessions | Firewall rule set (Regional deny-by-default) |
| Cloud historian replica and analytics (SYS-07) | Outbound only from the OT DMZ | Process and water quality data | Cloud provider terms; interconnection record |
| Lakes and Ridge plants to the ROC (site-to-site VPNs) | Bidirectional | SCADA client views, alarms | **No written terms; any-to-any rules (gap, CA-3 and SC-7)** |
| Integrator A | Inbound sessions through the gateway | Engineering access to Regional HMIs and PLCs | 2025 contract with security terms |
| Integrator B | Inbound through its own agent (Ridge) and the Lakes VPN | Engineering access | **Inherited contracts with no security terms (gap, PS-7 and SA-9)** |
| 13 other OT vendors | Inbound through the gateway on request | Device support | Vendor access agreement (12 of 13 signed) |
| Municipal clients 1-3 | Inbound read-only views to the ROC | Alarms and process values | Utility Services agreements |
| Cellular carrier private network | Bidirectional | Telemetry for 25 sites | Carrier contract |
| MSSP | Outbound sensor alerts and gateway logs | Security events | MSSP contract (SOC 2 Type 2) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Regional SCADA servers (2) and standby server | Server (supported OS) | ROC; WTP-R2 | Director of Water Operations |
| Regional HMIs (14) and engineering workstations (2) | Workstation | ROC 6, WTP-R1 4, WTP-R2 4 | Director of Water Operations |
| Regional historian and alarm notification server | Server | ROC | SCADA and Controls Engineering Manager |
| Lakes SCADA servers (2), HMIs (3), engineering workstation, historian (dual-homed, **gap**) | Server and workstation | WTP-L1 | Plant Manager (Lakes) |
| Ridge SCADA server, HMIs (2), engineering workstation (unsupported OS, **gap**) | Server and workstation | WTP-G1 | Plant Manager (Ridge) |
| PLCs (41) and RTUs (75) | Controller | Plants, wells, boosters, tanks | SCADA and Controls Engineering Manager |
| Radios, fiber, cellular modems (25) | Telemetry | Remote sites | SCADA and Controls Engineering Manager |
| IT/OT firewalls, OT switches, OT DMZ servers, remote access gateway | Network | WTP-R1, WTP-R2, WTP-L1, WTP-G1 | IT Director |
| Site-to-site VPN endpoints and Lakes on-call VPN appliance | Network | WTP-L1, WTP-G1, ROC | IT Director |
| Passive OT monitoring sensors (2) | Security sensor | WTP-R1, WTP-R2 | Security Manager |

The Regional inventory is complete. Inventories for Lakes, Ridge, and small systems are being built from passive discovery and site surveys (CM-8, due 2026-12-31).

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The IWOS uses the NIST SP 800-53B **High** baseline (370 controls and enhancements), tailored with the **OT overlay in SP 800-82 Rev. 3, Appendix F** and scaled for a 600-person utility:
- **Documented here: 111 controls** in `control-implementation.csv` (108 from the High baseline and 3 tailored in). They cover the controls that carry the RRA's automated-systems element and the risks in P01: remote and vendor access, segmentation, identity, OT backups and recovery, monitoring, configuration, and the engineered safeguards.
- **Selected by tailoring (added):** PM-1, PM-2, and PM-9. They are not in any SP 800-53B baseline but are needed for program governance and the risk appetite.
- **Tailored with OT compensating controls** where the overlay allows it, and recorded in the statement: for example AC-7 and AC-11 on operator HMIs that must stay available in a staffed control room.
- **Inherited without separate statements:** physical and environmental controls for the cloud provider's data centers and the SIEM platform, evidenced by their SOC 2 reports (P09 `vendor-soc2-review.csv`).
- **Deferred:** the remaining High-baseline controls with no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop software), and controls the Ridge platform cannot support until it is replaced in 2027. Each is recorded as a tailoring decision and reviewed yearly.

**CSF 2.0 mapping.** Most `csf2_subcategories` values come from NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`); enhancements inherit their base control's mapping. Thirteen controls with no official mapping (AC-8, AC-11, AU-8, CA-6, CP-3, IR-2, MA-4, MP-6, MP-7, PL-4, PS-3, PS-4, PS-5) and the tailored-in PM controls and SC-24 use an author mapping.

**Status of the 111 documented controls:**
| Status | Count |
|---|---|
| Implemented | 34 |
| Partially implemented | 75 |
| Planned | 2 |
| Not applicable | 0 |

**Inheritance of the 111 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 71 | Company (OT engineering, ROC, IT) |
| Hybrid | 19 | Identity provider (gateway MFA), MSSP (monitoring and logging), cloud provider (OT backups and replica) |
| Common/Inherited | 21 | Enterprise security program common controls (policies, training, HR screening, media sanitization, badge reviews) |

**Why so many Partially implemented.** Most Partially implemented statements say the same thing: the control works at the Regional System and is missing at Lakes, Ridge, or the small systems. That is the scale gap in `../00_company-facts.md` section 4 (gaps 1 to 7). The two Planned controls are IR-3 (first OT tabletop, 2026-11-17) and CP-7 (alternate ROC position).

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Remote access to OT** (on-call operators, engineers, and vendors) must use MFA through the identity provider on the gateway, with phishing-resistant authenticators for administrator and integrator accounts by 2027-03-31. Remote OT access can change treatment, so it needs the strongest assurance the company can support.
- **Operators in control rooms** use named HMI accounts with passwords (Regional now; Lakes and Ridge by 2026-12-31). Badge-controlled rooms are the compensating control, and HMIs stay unlocked for alarm response, as the SP 800-82 Rev. 3 OT overlay allows.
- **Device and service credentials** (PLCs, modems, historian service accounts) are vaulted and changed from commissioning values (Regional done; others by 2027-03-31).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register and RRA cyber addendum (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness (P09); AI governance assessment (P10); the 3 RRAs and ERPs on file.

## 13. Acronym List and Glossary
- **DMZ:** demilitarized zone, a buffer network between IT and OT
- **ERP:** emergency response plan (SDWA section 1433(b))
- **HMI:** human-machine interface
- **IWOS:** Integrated Water Operations SCADA
- **MGD:** million gallons per day
- **OT:** operational technology
- **PLC:** programmable logic controller
- **PWSID:** public water system identification number
- **ROC:** Regional Operations Center
- **RRA:** risk and resilience assessment (SDWA section 1433(a))
- **RTU:** remote terminal unit
- **SCADA:** supervisory control and data acquisition

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Security Manager with the SCADA and Controls Engineering Manager |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | IT Director (security officer) |

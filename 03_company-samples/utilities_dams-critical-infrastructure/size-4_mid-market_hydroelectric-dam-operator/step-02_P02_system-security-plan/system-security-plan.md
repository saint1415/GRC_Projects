# System Security Plan: Hydro Control and Dam Monitoring System (HCDMS)

**Organization:** Cris Santos Company, Inc. (owner and operator of 4 FERC-licensed hydroelectric projects; NERC-registered Generator Owner and Generator Operator) | **Tier:** Mid-Market | **Vertical:** Dams
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17
**Handling:** CEII and "Privileged - Security Sensitive Material". Keep in the restricted library (POL-04)

## 1. System Name and Identifier
Hydro Control and Dam Monitoring System (**HCDMS**), identifier CSC-HCDMS-01. It comprises SYS-01 to SYS-07 in `../00_company-facts.md` at the Remote Operations Center (ROC), the backup ROC, and the 4 projects. The registry default name ("Hydro plant control and dam monitoring system") was kept in substance and widened because, at this size, one central control system spans 4 projects and 6 RMOS client projects.

This SSP is also the **Cyber/SCADA Security Plan** that each Group 1 and Group 2 Security Plan references (Rev. 3A 3.3.1 and 3.3.2), and it records how the CIP-003-9 low impact cyber security plan applies inside the HCDMS.

## 2. System Overview
The HCDMS supervises and controls 12 generating units (300 MW) and 20 spillway gates at Blackwater Bend (BWB), Cedar Shoals (CDS), Pine Hollow (PNH), and Sawgrass Run (SGR); acquires data from 410 dam safety instruments and 9 upstream gauges; activates 23 downstream sirens; and monitors 6 client projects (operating units and gates at 4 of them) under RMOS contracts. It supports BIA processes BP-01 to BP-05, BP-08, and BP-18 (P05).

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | ROC SCADA: redundant servers (primary ROC, standby at the backup ROC), 16 operator consoles, 3 engineering workstations, OT historian, ICCP server | On-premises OT |
| SYS-02 | Plant control: 12 unit PLCs, 12 digital governors, 12 excitation systems, plant HMIs | On-premises OT at 4 powerhouses |
| SYS-03 | Spillway gate control: gate PLCs, 20 local gate panels, hoists, standby generators | On-premises OT at 4 spillways |
| SYS-04 | Dam safety instrumentation and early warning: automated data acquisition for 410 instruments, 9 cellular river gauges, 23 sirens | On-premises OT plus field devices |
| SYS-05 | OT WAN (private fiber and licensed microwave), site OT firewalls, OT DMZ (historian replica, jump hosts, patch server), OT backup server | On-premises OT |
| SYS-06 | Remote access: OT jump hosts with MFA; RMOS client site-to-site tunnels; 2 OEM direct VPNs (being removed) | OT DMZ and site firewalls |
| SYS-07 | OT security monitoring: passive sensors and log collection at the ROC and BWB, alerting to the MSSP | On-premises sensors; SaaS SIEM (SYS-13) |

The HCDMS relies on corporate services that sit outside the boundary: the identity provider (SYS-09) supplies MFA to the jump hosts, the SIEM (SYS-13) receives OT alerts, and the cloud OT data and analytics account (SYS-11, SYS-14) receives historian data one way.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the HCDMS |
|---|---|---|---|
| C-DAMS-R01 | FERC Security Program for Hydropower Projects | Rev. 3A, sections 3 to 9 and Form 3 | Primary driver. Section 9 applies at the Critical level (section 6 below): baseline and enhanced measures (Tables 9.3a and 9.3b), Form 3 Questions 5-33, plan and schedule for negative answers |
| C-DAMS-R02 | FERC dam safety incident reporting | 18 CFR 12.10; 12.3(b)(4) | A cyber event that affects gates or units, or any security incident, is a condition affecting project safety; detection and logging must support the report |
| C-DAMS-R03 | NERC CIP (low impact) | CIP-002-5.1a; CIP-003-9 R1 Part 1.2, R2 and Attachment 1; CIP-012-2 | BWB, CDS, and the ROC contain low impact BES Cyber Systems. CIP-003-9 Attachment 1 Sections 1 to 6 apply to those assets; CIP-012-2 applies to the ICCP data exchange with the BA/TOP Control Center |
| C-DAMS-R03 | NERC EOP-004-4 | R1, R2, Attachment 1 | Event reports for damage or physical threats at BWB and CDS within 24 hours of recognition or by the end of the next business day |
| Regulation | CEII | 18 CFR 388.113(c)(2) | HCDMS design details, network diagrams, and this SSP are handled as CEII |
| Contract | BA/TOP operating agreement; PPA; RMOS client contracts | Contracts | ICCP availability; RMOS operating orders; planned SOC 2 Type 2 (P09) |
| Internal | POL-01 to POL-05 and standards STD-01 to STD-12 | P06 | Policy basis for every control |

**Not applicable to the HCDMS:** NERC CIP-004 to CIP-011, CIP-013, and CIP-015 (they apply to high and medium impact BES Cyber Systems; the company has none, CIP-002-5.1a Attachment 1); CIP-014 (Transmission Owners only); SEC cyber disclosure (privately held). CIRCIA is a proposed rule only and is tracked in P03.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (authorizing official equivalent and CIP Senior Manager) on 2026-09-17, after the control assessment (P07).
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no authorization to operate. The internal equivalent:
- **Decision:** continued operation of the HCDMS accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Operating Officer for Moderate risks; Chief Executive Officer for High risks (P01 acceptance authorities).
- **Conditions:** the interim controls in P07 stay in place until their POA&M items close (OEM direct VPNs disabled except during approved sessions; the SGR modem removed; RMOS client tunnels restricted to client-specific SCADA objects); quarterly POA&M status to the audit committee; re-decision by 2027-09-30 or after a major change.
### 4.3 System Operational Status
Operational. Major modifications planned:
- OT zone architecture: per-site zones and a separate RMOS zone at the ROC (2027-03-31)
- OT monitoring at CDS, PNH, and SGR (2027-06-30)
- Replacement of 9 unsupported OT hosts at PNH and SGR (2027-09-30)
- ROC SCADA cyber recovery capability and an isolated recovery environment at the backup ROC (2027-06-30)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Vice President of Generation Operations | Accountable for the HCDMS; owns the ROC, the 4 plants, and controls engineering |
| Authorizing official equivalent; CIP Senior Manager | Chief Operating Officer | Accepts Moderate risk; approves this SSP, the CIP-003 plan, and CIP-002 identifications |
| High-risk acceptance | Chief Executive Officer | Temporary acceptance of High risks with a dated plan |
| Oversight | Board audit committee | Quarterly cyber risk reporting from the vCISO |
| Program strategy | vCISO (part-time contractor) | Program strategy, risk register, board reporting |
| OT cyber lead | OT Security Manager and 3 OT security engineers | Section 9 measures, CIP-003 implementation, jump hosts, OT monitoring, OT vulnerability management |
| Control system engineering | Manager of Controls Engineering | SCADA, PLC, governor, historian; OT change management; OT backups |
| Operations | ROC Manager; 6 ROC shift supervisors; 4 Plant Managers | Daily operation; incident commander on shift for OT incidents |
| Dam safety | Chief Dam Safety Engineer | EAPs, instrumentation, 18 CFR 12.10 reports; signs the annual certification letter |
| FERC security contact | Corporate Security Manager | Rev. 3A 3.2 primary contact; Security Plans; physical security |
| NERC compliance | NERC Compliance Manager (reports to the General Counsel) | CIP-002, CIP-003, CIP-012, EOP-004 evidence |
| IT security | IT Director | Identity provider, corporate network, cloud landing zone |
| Independent assessment | Co-sourced internal audit firm | P07 assessment; reports to the audit committee |
| Monitoring | MSSP | 24x7 SIEM and OT sensor alert monitoring |

**Overlap and compensation.** The OT Security Manager reports to the system owner, so OT security partly checks its own work. Compensating controls: the co-sourced internal audit firm assesses the HCDMS independently (P07), the NERC Compliance Manager reports to the General Counsel, and the vCISO reports directly to the audit committee.

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199. Integrity and availability were raised above the provisional levels because of the downstream safety consequence.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy production (unit control, generation data, ICCP data) | Moderate | High | Moderate | Wrong governor or unit commands can damage units; loss of the BES plants costs about $301,600 a day (P05) but has local workarounds |
| Water resource management and flood control (gate commands, reservoir levels) | Moderate | High | High | An unauthorized gate opening at BWB could send a surge toward a city of about 38,000 within 2 to 9 miles; loss of gate control during a flood could overtop a dam |
| Disaster monitoring and emergency response (instrumentation, trigger points, sirens) | Moderate | High | High | False or missing readings could hide a developing failure mode; sirens must work when an EAP is activated |
| Customer operations data (RMOS client control and instrument data) | Moderate | High | High | The ROC operates client gates and units under written orders; misoperation affects client downstream populations |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for investigations and 12.10 reports |
| **HCDMS category (high-water mark)** | **Moderate** | **High** | **High** | |

**Confidentiality stays Moderate.** Design details and network diagrams are CEII and are protected (POL-04), but disclosure alone does not operate a gate. The tier guide expects a Moderate-impact major system at this size; the safety consequence makes the High baseline the honest starting point.

**FERC Section 9 designation (re-determined 2026-07-14 to 2026-07-16).** Form 3 Questions 1-4 are Yes for BWB, CDS, and PNH (remote data acquisition, remote generation control, remote control of water retention features, and interconnection with other dams through the ROC). Under Table 9.1c, gate control at BWB, CDS, and PNH exceeds the population thresholds (more than 60 people within 3 miles of each dam), so it is **Critical**. BWB generation alone (180 MW) would be Operational on capacity, and CDS, PNH, and SGR generation Non-critical (Table 9.1c notes 2 and 3). The ROC SCADA is one cyber system with all 4 projects, so the whole HCDMS is treated as Critical, following FERC FAQ Question 1 (the consequence for a shared system comes from the higher asset). Sawgrass Run (Group 3) is interconnected and is held to the same level (Rev. 3A 9.1.1.2 note).

**NERC CIP-002-5.1a categorization (approved by the CIP Senior Manager 2026-02-10).** Assets containing low impact BES Cyber Systems: the ROC (Control Center, criterion 3.1), the backup ROC, BWB, and CDS (generation resources, criterion 3.3). No medium or high impact BES Cyber Systems: aggregate BES generation of 264 MW is below the 1,500 MW lines in criteria 2.1 and 2.11, no Planning Coordinator or Transmission Planner designation exists under criterion 2.3, and neither plant is a Blackstart Resource. PNH and SGR are not BES (69 kV).

## 7. Authorization Boundary Description
**Inside the boundary:**
- SYS-01 to SYS-07 at the ROC, the backup ROC (CDS powerhouse), and the 4 projects;
- the OT DMZ, including the historian replica, jump hosts, and patch server;
- the site ends of the RMOS client tunnels and the ICCP server;
- control rooms, powerhouses, gate houses, and instrument houses that house these components.

**Outside the boundary (interconnected):**
- the corporate network, identity provider, productivity suite, and SIEM (SYS-08, SYS-09, SYS-10, SYS-13);
- the cloud landing zone, including the OT data and analytics account and the RMOS client portal (SYS-11, SYS-14, SYS-15);
- the BA/TOP control center (ICCP);
- the 6 RMOS client sites;
- OEM and SCADA vendor networks.

The diagram is in P04 `cloud-architecture.md`. The planned design (POAM-002) splits the OT WAN into per-site zones and moves RMOS client tunnels into a separate zone that can reach only client objects in SCADA.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| BA/TOP control center (ICCP) | Bidirectional | Real-time MW, status, dispatch | Operating agreement; CIP-012-2 plan (Parts 1.2 and 1.3 missing, gap 11) |
| Electric cooperative (PNH, SGR offtaker) | Outbound | Hourly output; schedules by portal | PPA |
| RMOS client sites (6) | Bidirectional (site-to-site tunnels) | Client telemetry, alarms, gate and unit commands at 4 sites | RMOS contract and operating orders; **no security schedule (gap 9)** |
| Cloud OT data and analytics account (SYS-14) | Outbound only, from the DMZ historian replica | Instrument and operations data | Internal; one-way push |
| RMOS client portal (SYS-15) | Outbound from SYS-14 | Dashboards and reports | RMOS contract |
| SIEM (MSSP) | Outbound | OT alerts and logs (ROC and BWB) | MSSP contract; SOC 2 Type 2 |
| SCADA platform vendor | Inbound through jump hosts | Remote support | Contract with security terms |
| Governor and excitation OEM (BWB, CDS) | Inbound through jump hosts | Remote support | Contract with security terms |
| Governor OEM (PNH); turbine controls OEM (SGR) | Inbound **direct VPN** to plant OT firewalls | Remote support | **No security terms; bypasses jump hosts (gap 3)** |
| Identity provider (SYS-09) | Inbound | MFA for jump host sign-in | Internal |

## 9. System Component Inventory
| Component | Type | Location | Owner |
|---|---|---|---|
| SCADA servers (2), ICCP server, historian | Servers | ROC; standby at backup ROC | Manager of Controls Engineering |
| Operator consoles (12 ROC, 4 backup ROC) and engineering workstations (3) | Workstations | ROC; backup ROC | ROC Manager |
| Unit PLCs (12), governors (12), exciters (12), plant HMIs | Controllers and HMIs | 4 powerhouses | Plant Managers |
| Gate PLCs and 20 local gate panels; hoists; standby generators | Controllers | 4 spillways | Plant Managers |
| Data acquisition units for 410 instruments; 9 river gauges with cellular modems; 23 sirens | Field devices | Dams, river basin, downstream communities | Chief Dam Safety Engineer |
| OT firewalls (5), OT WAN routers, microwave radios | Network | ROC and 4 projects | OT Security Manager |
| OT DMZ: historian replica, jump hosts (2), patch server; OT backup server | Servers | ROC | OT Security Manager |
| Passive OT sensors (2) | Monitoring | ROC; BWB | OT Security Manager |
| Windows-based OT hosts at PNH and SGR (29, of which 9 unsupported) | Workstations and servers | PNH; SGR | Manager of Controls Engineering |

The full OT asset inventory (612 assets at the ROC and BWB recorded; CDS, PNH, and SGR in progress) is kept in the restricted library (Rev. 3A 9.2).

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The HCDMS starts from the NIST SP 800-53B **High** baseline (370 controls and enhancements in the repository catalog), informed by the SP 800-82 Rev. 3 OT overlay, and tailored as follows:
- **Documented here: 138 controls** in `control-implementation.csv`. They cover every FERC Section 9 baseline and enhanced measure, every CIP-003-9 Attachment 1 section (20 controls cite CIP-003-9), CIP-012-2, and the High-baseline controls that address the High and Very High risks in P01 (remote access, segmentation, recovery, monitoring, vulnerability management).
- **Selected by tailoring (added):** PM-9 (risk management strategy), which is not in any baseline but is needed for Form 3 Question 29.
- **Compensating controls for legacy devices:** PLCs, governors, exciters, and gate panels cannot enforce modern authentication or logging. They are protected by physical access control (PE-3), segmentation (SC-7), monitoring (SI-4), and fail-safe design (SC-24), as SP 800-82 Rev. 3 and Rev. 3A 9.1.1.4 recommend.
- **Inherited without separate statements:** physical and environmental protection of cloud and SaaS data centers, and platform-level controls of the identity provider, SIEM, and cloud provider, evidenced by their SOC 2 Type 2 reports (P09 Part B).
- **Not documented in this version:** High-baseline controls that assume general-purpose IT the HCDMS does not use (for example mobile code and some session authenticity controls), and program-level controls covered by POL-01. They are recorded as tailoring decisions in the OT asset inventory and reviewed each year.

**Status of the 138 documented controls:**
| Status | Count |
|---|---|
| Implemented | 44 |
| Partially implemented | 87 |
| Planned | 7 |
| Not applicable | 0 |

**Inheritance:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 96 | Company (OT controls are rarely inheritable) |
| Hybrid | 25 | MSSP (SIEM, EDR, monitoring), identity provider (MFA), cloud provider (backup copies, keys), SCADA platform vendor (test system) |
| Common/Inherited | 17 | Corporate programs: HR screening and training, Corporate Security physical protection, internal audit |

**By family:**
| Family | Controls documented |
|---|---|
| AC | 26 |
| AT | 4 |
| AU | 9 |
| CA | 8 |
| CM | 14 |
| CP | 12 |
| IA | 9 |
| IR | 7 |
| MA | 4 |
| MP | 3 |
| PE | 5 |
| PL | 3 |
| PM | 1 |
| PS | 4 |
| RA | 5 |
| SA | 4 |
| SC | 12 |
| SI | 6 |
| SR | 2 |

CSF 2.0 subcategories in the CSV come from the NIST CSF 2.0 to SP 800-53 crosswalk in `00_universal-framework/crosswalks/` where it maps the control; the rest are author mappings. The Partially implemented statements trace to the 13 gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-28 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). The Section 9 subset of the POA&M is the plan and schedule sent to the Regional Engineer on 2026-09-30 (Rev. 3A 9.1.1.3).

## 11. Digital Identity Acceptance Statement
- **ROC and plant operators.** Operators sign in to SCADA consoles with unique accounts and passwords inside card-access control rooms. MFA is not used at local consoles because a second factor could delay a safety action; physical access control compensates. Shared accounts at PNH and SGR will be replaced by named accounts by 2026-12-31 (POAM-004).
- **Remote users and vendors.** All remote access goes through the jump hosts with MFA from the identity provider and session recording. A break-glass MFA path that does not depend on the corporate identity provider is planned (P05 finding 5). The 2 OEM direct VPNs are disabled except during approved, escorted sessions from 2026-09-15 and will be removed by 2026-11-30.
- **RMOS client users.** Clients sign in to the portal as guests with MFA; they have no access to SCADA.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness (P09); AI governance assessment (P10); FERC Security Plans, Vulnerability Assessment, and Security Assessments (restricted library); CIP-003 low impact cyber security plan; CIP-012 plan.

## 13. Acronym List and Glossary
- **BA/TOP:** Balancing Authority and Transmission Operator
- **BES:** Bulk Electric System
- **CEII:** Critical energy infrastructure information
- **EAP:** Emergency Action Plan (18 CFR Part 12, Subpart C)
- **GO/GOP:** Generator Owner and Generator Operator (NERC registration)
- **HCDMS:** Hydro Control and Dam Monitoring System
- **ICCP:** Inter-Control Center Communications Protocol
- **OEM:** original equipment manufacturer
- **RMOS:** Remote Monitoring and Operations Services
- **ROC:** Remote Operations Center
- **Section 9:** Computer Security and SCADA section of the FERC Security Program Rev. 3A

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, the Section 9 re-determination, and the gap analysis | OT Security Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Operating Officer | OT Security Manager with the vCISO |

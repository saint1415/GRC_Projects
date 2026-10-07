# System Security Plan: Hydro Plant Control and Dam Monitoring System (HPCDMS)

**Organization:** Cris Santos Company Holdings, Inc. (Hydro division, with common controls from corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Dams
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10
**Handling:** Contains BES Cyber System Information and security-sensitive material. Mark "Privileged - Security Sensitive Material" (FERC Security Program Rev. 3A, 3.4.3.4 and 8.0) and handle as BCSI under CIP-011-3 and as CEII under POL-04.

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Hydro division's control system**, because it carries the group's highest consequences (uncontrolled release of water, loss of 10,140 MW of remotely operated generation), it is the system FERC and NERC inspect, and the top group risk (P01 GR-01) runs through it. The divisions' other systems (the DSMS, the Federal Projects Enclave, the project platform) inherit from the same **common control catalog** (`common-control-catalog.csv`), and each keeps its own plan: the FPE has its own SSP for CMMC (owned by the Federal Programs Compliance Director), and the DSMS has a SOC 2 system description in progress (P09).

## 1. System Name and Identifier
Hydro Plant Control and Dam Monitoring System (**HPCDMS**), identifier CSCH-HYD-OT-01. Made up of SYS-H1 to SYS-H5 in `../00_company-facts.md` section 3, at the 41 HOC-operated developments.

## 2. System Overview
The HPCDMS lets Hydro operate 41 hydroelectric developments (10,140 MW, 32 gated dams) from two Hydro Operations Centers and protect the people who live below them. It supports:
- **Generation:** unit dispatch, automatic generation control response, and real-time data exchange with 3 Balancing Authorities and Transmission Operators.
- **Water control:** spillway gate commands, reservoir level management, and flood passage under each license and EAP.
- **Dam safety:** automated instrument reading, threshold alarms, and EAP warning sirens.

About 640 people have access: HOC operators and supervisors, plant operators, controls and OT security engineers, dam safety technicians, and 26 vendors through the Intermediate Systems.

**Major components:**
- **SYS-H1 fleet SCADA** at HOC-A (north Georgia) and HOC-B (eastern Tennessee): redundant SCADA servers, operator consoles, AGC interface, ICCP servers, historian. Medium impact BES Cyber Systems inside Electronic Security Perimeters (CIP-002-5.1a Attachment 1 criterion 2.11).
- **SYS-H2 plant control:** unit PLCs, governors, exciters, and plant HMIs. Low impact BES Cyber Systems at the 36 HOC-operated BES plants (criterion 3.3).
- **SYS-H3 spillway gate control:** gate PLCs, local gate panels, hoists, standby generators. Not BES Cyber Systems; Critical under FERC Section 9 at the Group 1 and 17 Group 2 dams.
- **SYS-H4 dam safety instrumentation and early warning:** data acquisition, gauges, sirens.
- **SYS-H5 OT network and identity:** OT WAN (licensed microwave plus leased circuits), plant gateway firewalls, HOC ESP firewalls, OT DMZs, 2 Intermediate System clusters, the OT identity domain and OT PAM, one-way diodes at 24 plants.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the HPCDMS |
|---|---|---|---|
| C-DAMS-R01 | FERC Security Program for Hydropower Projects, Rev. 3A | FERC D2SI program applied under 18 CFR Part 12 and license conditions | Security Plans for the 29 Group 1 and 2 dams must include cyber/SCADA measures or a separate Cyber/SCADA Security Plan (3.3.1, 3.3.2). Section 9 baseline and enhanced measures apply because the HOC SCADA and gate control are Critical cyber assets (Table 9.1c). Where an asset falls under both FERC D2SI and NERC CIP, it must meet NERC CIP to satisfy D2SI (9.4). This SSP is the basis of the fleet Cyber/SCADA Security Plan |
| C-DAMS-R02 | FERC dam safety incident reporting | 18 CFR 12.10 | A security incident (physical and/or cyber) or gate misoperation is a reportable condition (12.3(b)(4)); initial report as soon as practicable, preferably within 72 hours |
| C-DAMS-R03 | NERC CIP Reliability Standards | 16 U.S.C. 824o; 18 CFR Part 40; CIP-002-5.1a to CIP-013-2 | Medium impact requirements (CIP-004 to CIP-011, CIP-013) for SYS-H1 at both HOCs; CIP-003-9 Attachment 1 for the low impact plants; CIP-012-2 for the ICCP links |
| NERC EOP-004-4; DOE-417 | Event reporting | EOP-004-4 R2; Form DOE-417 | Physical threats and damage to Facilities within 24 hours or by the end of the next business day; DOE-417 cyber criteria when the Balancing Authority does not file |
| Part 12 | Owner's Dam Safety Program; EAPs; gate testing | 18 CFR 12.20 to 12.25, 12.54, 12.60 to 12.65 | EAP siren activation runs on SYS-H4; annual gate and standby power tests (12.54) include the HPCDMS gate control path |
| SEC | Form 8-K Item 1.05; Reg S-K Item 106 | SEC Release 33-11216 | A compromise of the HPCDMS may be a material incident for the group (P08) |
| Contracts | ICCP and interconnection agreements; OEM service contracts | CIP-012-2 R1 Part 1.5; CIP-013-2 | Responsibilities with the 3 Balancing Authorities; vendor security terms |
| Internal | Group POL-01 to POL-05 and the Hydro supplement | P06 | |

Not applicable: CIP-014-3 (Transmission Owners and Transmission Operators only); high impact CIP requirements (no high impact BES Cyber Systems); FAR and DFARS clauses (Hydro holds no federal contracts). CIRCIA reporting is not in effect (final rule not published).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Senior Vice President, Hydro Operations (system owner and CIP Senior Manager) and the Group CISO on 2026-09-10, after the board safety, risk, and reliability committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Senior Vice President, Hydro Operations with the Group Chief Risk Officer (High risk acceptance authority).
- **Conditions:** (1) no Constructors commissioning kit or other non-Hydro device connects to any HPCDMS network except through an approved, escorted, logged session (in force from 2026-07-16; permanent design by 2026-12-31, POAM-001); (2) replace the two-way DSMS replication at 17 plants with one-way transfer by 2027-03-31 (POAM-005); (3) bring OT monitoring to all 41 HOC-operated plants by 2027-06-30 (POAM-006).
- **Reauthorization:** annually, or when the conditions close.

### 4.3 System Operational Status
Operational. **Major modifications planned:** plant HMI and gate workstation replacement (2027), OT sensor rollout to all HOC-operated plants (2027), and the one-way DSMS data path (2027).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner; CIP Senior Manager | Senior Vice President, Hydro Operations | Accountable for the HPCDMS and this SSP; approves CIP-002 identifications and CIP policies |
| Authorizing official equivalent | Senior Vice President, Hydro Operations with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Dam safety owner | Vice President, Dam Safety (Chief Dam Safety Engineer) | EAP and instrumentation functions; 18 CFR 12.10 reports |
| FERC primary security contact | Director, Hydro Security | Security Plans, Vulnerability and Security Assessments, certification letters |
| OT security lead | Director, OT Security | Section 9 and CIP technical controls; OT identity domain; maintains this plan |
| Compliance (second line) | NERC Compliance Director (reports to the Chief Compliance Officer) | CIP evidence, SERC correspondence, CIP-008 and EOP-004 reporting |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group HR director, Chief Procurement Officer | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit with a co-sourced OT specialist firm | Assesses common controls once and the HPCDMS controls (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy supply (generation control and real-time data) | Moderate | **High** | **High** | Manipulated setpoints or loss of control of 10,140 MW would have a severe effect on grid obligations and equipment |
| Water resource management (gate control, reservoir levels) | Moderate | **High** | **High** | An unauthorized gate opening could endanger people downstream (a city of about 52,000 below DEV-02) |
| Emergency response (dam safety instrumentation, EAP sirens) | Low | **High** | **High** | False or missing readings delay EAP action |
| Information security (OT credentials, firewall rules, BCSI) | **Moderate** | High | Moderate | Disclosure would help an attacker; BCSI and CEII rules apply |
| **HPCDMS category (high-water mark)** | **Moderate** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored for OT. The plan documents **163 controls** in `control-implementation.csv`, all from the High baseline. Controls left out are either fully provided by the Hydro physical security program and corporate without a system-level duty (for example PE-13 fire protection, PE-14 environmental controls), not applicable to an isolated OT system with no external users (for example IA-8(1), SC-21), or not technically feasible on legacy controllers, with compensating controls recorded in the Hydro tailoring register. The tailoring follows NIST SP 800-82 Rev. 3, Appendix F (the OT overlay).

## 7. Authorization Boundary Description
- **Inside:** SYS-H1 at HOC-A and HOC-B; SYS-H2, SYS-H3, and SYS-H4 at the 41 HOC-operated developments; SYS-H5 (OT WAN, plant gateway firewalls, HOC ESP firewalls, OT DMZs, Intermediate Systems, OT identity domain and OT PAM, diodes).
- **Outside, inherited (common control providers):** group governance, training, HR, procurement, internal audit; SYS-G2 SOC (alert triage, case handling, SIEM retention); SYS-G1 only for HR event signals and high-risk user alerts (no OT sign-in uses SYS-G1); Hydro physical security (SYS-H7).
- **Outside, interconnected:** the DSMS (SYS-E1, Engineering), the scheduling platform (SYS-H6), the 3 Balancing Authority and Transmission Operator control centers (ICCP), and Constructors commissioning connections (SYS-C3) during rehabilitation projects.
- **Outside, not connected:** the 13 locally operated developments (separate plant systems, monitored read-only through the OT DMZ).

The diagram is in P04 `cloud-architecture.md` (section 2.2, the OT-to-cloud boundary).

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement or control |
|---|---|---|---|
| 3 Balancing Authority and Transmission Operator control centers | Two-way (ICCP) | Real-time generation data, dispatch and AGC signals | ICCP agreements; CIP-012-2 plan (encryption on all links) |
| SYS-E1 DSMS (Engineering) | Outbound from the OT DMZ | Instrument and reservoir data for 68 dams | **Diodes at 24 plants; two-way historian replication at 17 plants (gap 3; POAM-005).** No intercompany agreement yet (POAM-005) |
| SYS-H6 scheduling platform | Outbound from the OT DMZ | Unit availability and output | One-way transfer service in the DMZ |
| SYS-G2 SOC | Outbound | Logs and OT sensor alerts | Common control catalog |
| Constructors commissioning kits (SYS-C3) | Two-way during commissioning | PLC programming and test data | **No agreement or design until 2026-07-16; interim rule now; permanent design due 2026-12-31 (POAM-001)** |
| OEM and integrator remote support (26 vendors) | Two-way through the Intermediate Systems | Diagnostics and maintenance | Vendor accounts in OT PAM; on-demand sessions; CIP-005-7 Parts 2.4 and 2.5 |

## 9. System Component Inventory
| Component | Type | Location | Owner |
|---|---|---|---|
| Fleet SCADA servers, consoles, AGC, ICCP, historian (SYS-H1) | On-premises OT | HOC-A and HOC-B | Senior Vice President, Hydro Operations |
| Unit PLCs, governors, exciters, plant HMIs (SYS-H2) | On-premises OT | 41 powerhouses | Plant managers |
| Gate PLCs, local panels, hoists, standby generators (SYS-H3) | On-premises OT | 32 gated dams | Plant managers |
| Data acquisition, gauges, sirens (SYS-H4) | OT and field devices | 68 instrumented dams (including some at locally operated developments, read through the DMZ) | Chief Dam Safety Engineer |
| OT WAN, firewalls, DMZs, Intermediate Systems, OT identity and PAM, diodes (SYS-H5) | On-premises | HOCs and plants | Director, OT Security |

The cyber asset inventory with Section 9 criticality lists every device (CM-8). Transient devices and commissioning kits are not yet in it (POAM-004).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (163 controls) and `common-control-catalog.csv` (107 common controls: 102 from corporate providers and 5 from the Hydro physical security program for all Hydro sites).

| Status | Controls |
|---|---|
| Implemented | 126 |
| Partially implemented | 34 |
| Planned | 3 |
| Not applicable | 0 |
| **Total** | **163** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from corporate or the Hydro physical security program) | 37 |
| Hybrid (a corporate or division mechanism, operated in part by the HPCDMS team) | 29 |
| System-specific | 97 |

Most controls are system-specific because the HPCDMS deliberately does not use corporate identity, networks, or hosting. What it inherits is governance, training, HR and personnel risk assessments, procurement, internal audit, the SOC's monitoring and case handling, and physical security.

**The 34 partially implemented controls** cluster in six places:
- **Construction and vendor connectivity** (gap 1): AC-2(12), AC-17, AC-17(1), AC-20, AT-3, CM-3, IA-5, MA-4, PS-7, SI-3.
- **The DSMS path and interconnections** (gap 3): AC-4, CA-3, PL-2, SA-9, SC-7.
- **Plant-level monitoring and vulnerability assessment** (gap 2): AU-6, CA-7, RA-5, SI-4, SI-4(4).
- **Legacy systems and recovery** (gap 4): CM-2, CM-8, CP-4, CP-9, CP-10, MP-7, SA-22, SI-2.
- **Supply chain** (gap 9): SA-4, SR-3, SR-6.
- **Cross-division incident response** (gap 8): IR-3, IR-4, IR-6.

The 3 planned controls are application allow-listing on plant HMIs (CM-7(5)), automated real-time analysis at all plants (SI-4(2)), and PLC logic integrity checks (SI-7(1)).

### 10.2 Common control inheritance by division
The common control catalog lists 107 controls. Inheritance is **documented for Hydro** (2025 inheritance matrix and this SSP). For **Constructors** it is documented only inside the FPE SSP, not for the project platform (SYS-C1) or jobsite technology (SYS-C3). For **Engineering** it is not documented; the DSMS SOC 2 system description in progress (P09) will be the first record (scenario gap 7; POAM-016). 16 common controls were assessed once for all divisions in P07.

### 10.3 Mapping to NERC CIP and FERC Section 9
Every row in `control-implementation.csv` names the CIP requirement or FERC program item it supports in `regulatory_driver`. Where a control serves both (for example AC-17 for CIP-005-7 R2 and Form 3 Q12), the CIP evidence is used for the FERC inspection, as Rev. 3A 9.4 allows, to avoid duplicate effort.

### 10.4 Control assessment status
Common controls were assessed once, and HPCDMS and division controls sampled, from 2026-07-01 to 2026-08-31 by group internal audit with the co-sourced OT firm. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **HOC and plant users** authenticate to the OT identity domain with unique accounts. Privileged access uses OT PAM with hardware tokens (replay resistant). Interactive Remote Access uses MFA at the Intermediate Systems (CIP-005-7 Part 2.3).
- **Vendors** use named vendor accounts in OT PAM, approved per session.
- **No corporate identity** is trusted by the OT domain, so a compromise of SYS-G1 does not give access to the HPCDMS.
- **Weak points:** 6 plant HMIs still have generic local accounts (inventoried and managed under CIP-007-6 Part 5.2), and the DEV-05 commissioning router had a default password (POAM-003).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud and OT boundary mapping (P04), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), DSMS SOC 2 readiness (P09), AI governance (P10). The fleet Cyber/SCADA Security Plan and the CIP-008 and CIP-009 plans reference this SSP.

## 13. Acronym List and Glossary
- **BCSI:** BES Cyber System Information
- **BES:** Bulk Electric System
- **DSMS:** Dam Safety Monitoring Service (Engineering)
- **EACMS:** Electronic Access Control or Monitoring Systems
- **ESP:** Electronic Security Perimeter
- **HOC:** Hydro Operations Center
- **ICCP:** Inter-Control Center Communications Protocol
- **Intermediate System:** the jump host cluster through which all Interactive Remote Access passes (CIP-005-7 Part 2.1)
- **PSP:** Physical Security Perimeter
- **Section 9:** Computer Security and SCADA section of the FERC Security Program

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Director, OT Security |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Senior Vice President, Hydro Operations |

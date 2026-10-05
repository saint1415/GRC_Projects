# System Security Plan: Pipeline SCADA and Gas Control System (PSGCS)

**Organization:** Cris Santos Company, LLC (small intrastate natural gas transmission pipeline operator) | **Tier:** Micro | **Vertical:** Energy
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Pipeline SCADA and Gas Control System (**PSGCS**), identifier CSC-OT-001.

## 2. System Overview
The PSGCS lets the company's 3 qualified controllers monitor and control about 26 miles of intrastate natural gas transmission line in Florida, 24 hours a day. Through it, controllers:
- watch pressures, flows, and alarms at 7 field sites;
- open and close 3 remote-control mainline valves (RCVs) and the receipt flow control valve;
- see hourly volumes from 4 flow computers;
- receive alarm callouts by phone after hours.

The company owns no SCADA servers. The SCADA host, historian, alarm callout, and web client run as a **hosted service** operated by the SCADA vendor. The company owns the field devices and the gas control desk, and the MSP manages the desk workstations and laptops. This plan therefore says, for each control, what the company does itself, what the SCADA vendor or the MSP does for it, and what it inherits. It is the SCADA system that 49 CFR 192.631 regulates.

**Major components:**
- **SYS-01:** the company's tenant on the hosted SCADA service (vendor SaaS), including the leak-detection anomaly module on trial (assessed separately in P10)
- **SYS-02:** 2 gas control desk workstations in the office (primary and backup)
- **SYS-03:** 7 RTUs, 4 flow computers, 3 RCV actuators, and the receipt flow control valve at 7 field sites
- **SYS-04:** 7 cellular gateways on a carrier private network, tunneled to the SCADA vendor
- **SCADA access from 3 controller laptops** (part of SYS-05), used for on-call duty

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-ENERGY-R04 | PHMSA control room management, reduced scope | 49 CFR 192.631(a)(1)(ii): transmission without a compressor station, so only paragraphs (d), (i), and (j) bind, plus integration under (a)(2). Adopted in Florida by Rule 25-12.005, F.A.C.; inspected by the FPSC |
| Related | Operations and maintenance manual, including abnormal operation for transmission lines; emergency plans | 49 CFR 192.605; 49 CFR 192.615 |
| Related | Incident reporting | 49 CFR 191.3, 191.5, 191.15; Rule 25-12.084, F.A.C. |
| Benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 | Voluntary; chosen in P03 |
| State | Florida Information Protection Act (employee personal information on the office side) | Fla. Stat. 501.171 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable:
- **C-ENERGY-R02 and C-ENERGY-R03**, TSA SD Pipeline-2021-01G and 02G. TSA has not designated the pipeline (P03 section 1.1). The `regulatory_driver` column of `control-implementation.csv` still names the SD section each control would support, as a readiness reference.
- **C-ENERGY-R01**, NERC CIP. The company is not a NERC-registered entity.
- **C-ENERGY-R05**, CIRCIA. Proposed only (P03 section 1.2).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-09-15.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-09-15 the Owner accepted continued operation of the PSGCS, on the condition that the four High risks in P01 (R-001, R-002, R-003, R-005) are treated on their dated plans. The first milestones are named SCADA accounts with MFA by 2026-10-31 and a clean spare SCADA laptop by 2026-10-31.

### 4.3 System Operational Status
Operational. Planned changes, all by 2026-12-31: SCADA MFA and named accounts (P01 R-002), a separate network segment and dedicated workstations for the gas control desk (R-001), second-carrier SIMs at 2 sites (R-008), and EDR on all computers (R-001).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner (General Manager) | Overall accountability; accepts Moderate and higher risk; approves this plan, policies, and spending |
| SCADA owner and administrator | Operations Manager | SCADA accounts, displays, alarm set-points, field device configuration; also a controller (see the overlap note below) |
| Security program coordinator | Office Manager | Maintains this plan, the risk register, and policies; MSP and vendor liaison |
| Controllers | Operations Manager and 2 Pipeline Technicians | Monitor and control the pipeline; on-call rotation |
| Office IT operations | MSP | Gas control desk workstations, laptops, office network, antivirus, patching |
| SCADA platform operations | Hosted SCADA vendor | SCADA host, historian, callout, web client, platform security and backups |
| Independent assessor | OT security consultant | Annual control assessment (P07) |

**Overlap and compensation.** At this size the Operations Manager both operates SCADA and administers it (AC-5). The Owner reviews the SCADA user list and the vendor's audit summary each month, and an independent consultant assesses the controls each year.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199 and use the BIA (P05).

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy supply: pipeline control data and commands | Moderate | **High** | **High** | A false reading or an unauthorized valve command could hide a rupture or cut supply to a municipal system serving about 9,000 homes and businesses. Loss of control beyond the 8-hour MTD forces curtailment (P05 BP-01) |
| SCADA configuration, account, and network information | Moderate | **High** | Moderate | Disclosure helps an attacker; an unauthorized change affects every control function |
| Emergency response information | Low | Moderate | **High** | Public safety communication cannot stop (P05 BP-02) |
| Gas measurement data | Low | Moderate | Low | Flow computers keep 35 days locally (P05 BP-04) |
| **PSGCS category (high-water mark)** | **Moderate** | **High** | **High** | **High** |

**Baseline:** the NIST SP 800-53B High baseline, tailored for a 7-person operator with a hosted SCADA service. The plan documents 46 controls: those that protect SCADA integrity and availability, support the binding pipeline rules, and would support the TSA SD measures if the pipeline were designated (see `control-implementation.csv`). Every other High-baseline control is handled one of three ways:
- **Inherited** from the SCADA vendor (data center, platform, and application controls), with its SOC 2 Type 2 report as the main evidence (P09).
- **Tailored out with a reason.** Examples:
  - Session termination on the gas control desk, because a controller must never lose the alarm display.
  - Separate development and test environments, because the company builds no software.
- **Not relevant to a non-federal operator.** Example: PM-series program controls beyond the program rules in POL-02 Part A.

## 7. Authorization Boundary Description
The boundary contains everything that can see or change the state of the pipeline:
- **Inside:** the company's SCADA tenant configuration, users, and roles (SYS-01); the 2 gas control desk workstations (SYS-02); the field devices at 7 sites (SYS-03); the 7 cellular gateways (SYS-04); and SCADA access from the 3 controller laptops.
- **Outside (interconnected):**
  - the SCADA vendor's own platform and data centers (inherited, evidenced by its SOC 2 report);
  - the carrier private network;
  - the office network and the rest of business IT (SYS-05 to SYS-09), which today share a flat network with the gas control desk;
  - the MSP's RMM tool (SYS-10), which has an agent on the gas control desk;
  - the upstream interstate pipeline's portal (SYS-11).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Field gateways to the SCADA vendor (carrier private network) | Bidirectional | Telemetry and commands | Carrier agreement; SCADA contract (**no security or incident notice terms, gap**) |
| SCADA vendor support staff | Inbound to the tenant | Support and platform changes | SCADA contract (**no approval or notice of support sessions, gap**) |
| Controller laptops and gas control desk to SCADA web client | Bidirectional over the internet | Displays, alarms, commands | Internal; password only (**gap**) |
| MSP RMM tool to gas control desk | Inbound administrative access | Device management | MSP contract (**no security terms, gap**) |
| Leak-detection module to on-call phones | Outbound alerts | Advisory anomaly alerts | Vendor trial terms (P10) |
| Upstream interstate pipeline | None system-to-system | Operational calls by phone | Interconnect operating agreement |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| SCADA tenant (SYS-01) | SaaS | Hosted SCADA vendor | Operations Manager |
| Gas control desk workstations (2) (SYS-02) | Workstation | Office | Operations Manager (MSP operates) |
| RTUs (7), flow computers (4), RCV actuators (3), receipt flow control valve (SYS-03) | Field device | 7 field sites | Operations Manager |
| Cellular gateways (7) and SIM cards (SYS-04) | Telecommunications | Field sites; carrier private network | Operations Manager |
| Controller laptops (3) used for SCADA (part of SYS-05) | Endpoint | Controllers' homes and trucks | Office Manager (MSP operates) |
| Spare clean SCADA laptop (planned) | Endpoint | Office safe, off the network | Operations Manager |

Firmware versions for the field devices and gateways are not yet recorded (CM-8 gap; P03 G-026).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 46 controls:
- Implemented: 9
- Partially implemented: 30
- Planned: 7
- Not applicable: 0

By responsibility: 18 system-specific (the company), 25 hybrid (the company with the SCADA vendor, the MSP, or the carrier), 3 common/inherited (fully provided by a vendor).

### 10.2 Inherited and provider-supported controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Hosted SCADA vendor | Platform security, data center redundancy, tenant backups (CP-9), failover (CP-10), role enforcement (AC-3), lockout (AC-7), audit logging and retention (AU-2, AU-11), encrypted telemetry tunnels (SC-8) | SOC 2 Type 2 report reviewed 2026-09-04 (P09) | Complementary user entity controls: named accounts and removal, MFA settings, role assignment, review of the audit log, approval of changes. **All are open gaps today** |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), screen lock (AC-11), suite backup (CP-9) | Monthly MSP report; P07 evidence requests | Approve exceptions; review reports; keep the RMM agent off the gas control desk once it is rebuilt (P04 finding 3) |
| Cellular carrier | Private network for telemetry; no public addresses (SC-7) | Carrier APN settings | Confirm the private-network setting whenever a SIM is replaced (P07 finding) |
| Productivity suite vendor | Platform security, encryption, lockout, logging | Vendor documentation | Account management, MFA settings, log review |

**Inherited does not mean done.** The SCADA vendor's controls protect the pipeline only if the company runs its side: named accounts, MFA, removal on the last day, and log review. Those are the weakest controls in this plan.

### 10.3 Control assessment status
Assessed 2026-08-17 to 2026-08-19 by an independent OT security consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Controllers** will sign in to the SCADA web client with a named account, a password, and a second factor from the vendor's authenticator app (authenticator assurance level 2 as described in NIST SP 800-63B). This is **not yet met**: the gas control desk uses a shared login and no SCADA login uses MFA (target 2026-10-31; POAM-002).
- **Emergency access.** So that MFA can never lock out a controller during an emergency, the Owner keeps a sealed break-glass credential for one controller account in the office safe. Any use is logged and the password is changed afterwards.
- **Business users** use the productivity suite and accounting SaaS with MFA. They have no SCADA access.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and SCADA vendor report review (P09), AI assessment (P10), O&M manual and emergency plan (company documents).

## 13. Acronym List and Glossary
- **CRM:** control room management (49 CFR 192.631)
- **EDR:** endpoint detection and response
- **FPSC:** Florida Public Service Commission
- **M&R:** meter and regulator station
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **PSGCS:** Pipeline SCADA and Gas Control System
- **RCV:** remote-control valve
- **RMM:** remote monitoring and management
- **RTU:** remote terminal unit
- **SCADA:** supervisory control and data acquisition

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-15 | Initial plan | Office Manager with the Operations Manager |

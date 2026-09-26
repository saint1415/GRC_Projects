# System Security Plan: Plant Production and Cold-Chain Monitoring System (PPCM)

**Organization:** Cris Santos Company, LLC (meat processing plant with a smoked seafood room) | **Tier:** Small | **Vertical:** Food and Agriculture
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), with OT guidance from NIST SP 800-82 Rev. 3 | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Plant Production and Cold-Chain Monitoring System (**PPCM**), identifier CSC-SYS-001.

## 2. System Overview
The PPCM runs and records every step that makes the plant's food safe: formulation and cure dosing, cooking and smoking, chilling, packaging and lot coding, and cold storage. It produces the electronic records that FSIS and FDA review (HACCP, seafood HACCP, and food defense monitoring). It serves about 190 production, maintenance, warehouse, and QA staff across two production shifts and a sanitation shift.

**Major components:**
- **SYS-01:** process control network (PLCs, 12 HMIs, dosing skid, seafood brine tank, CIP manifolds, five smokehouse controllers, packaging, metal detectors)
- **SYS-02:** SCADA server, process historian, and engineering workstation
- **SYS-03:** ammonia refrigeration control system (vendor-maintained)
- **SYS-04:** cold-chain monitoring (64 wireless sensors, gateway, vendor SaaS dashboard)
- **SYS-05:** recipe, batch, and lot-coding system (MES)
- **SYS-06:** public-cloud tenant (food safety records application, historian replica, traceability database, backup vault)
- **SYS-14:** OT remote access paths (integrator VPN, refrigeration contractor modem)

The cloud tenant is described by service category and is vendor-agnostic (see P04). OT zones follow the SP 800-82 Rev. 3 layered model: field devices and controllers (levels 0-1), HMIs and supervisory control (level 2), SCADA, historian, and MES (level 3), and the business network (level 4). Today levels 3 and 4 are not separated by an OT DMZ (see section 7).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it touches the PPCM |
|---|---|---|---|
| C-FOOD-AG-R01 | FSMA Intentional Adulteration rule | 21 CFR Part 121 | The dosing skid, brine tank, CIP valves, and recipe system are paths to adulterate the seafood product; mitigation strategies, monitoring, and records live in the PPCM |
| FSIS | HACCP systems | 9 CFR Part 417 | CCP monitoring by the historian and cold-chain sensors; computer records need integrity controls (417.5(d)) |
| FSIS | Recalls | 9 CFR Part 418 | 24-hour notification if adulterated product entered commerce (418.2); traceability database |
| FDA | Seafood HACCP | 21 CFR Part 123 | Seafood CCP records in the same records application (123.9(f)) |
| FDA | Reportable Food Registry | 21 U.S.C. 350f | 24-hour report for reportable seafood (P08) |
| Benchmark | NIST CSF 2.0 and SP 800-82 Rev. 3 | Voluntary | OT control expectations used to tailor the baseline |
| Internal | Security policies POL-01 to POL-05 | P06 | Apply to IT and OT |

Not applicable:
- CIRCIA (C-FOOD-AG-R02): proposed only; the company is below the proposed size criterion.
- USCG MTS cyber rule (C-FOOD-AG-R03): the plant is not an MTSA facility.
- OSHA PSM (29 CFR 1910.119) and EPA RMP (40 CFR Part 68) apply to the ammonia system as process safety rules. They are managed by the Maintenance and Refrigeration Manager's PSM program and are outside this plan, except that the refrigeration controller is inside the boundary.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the General Manager on 2026-09-04.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The General Manager accepted continued operation of the PPCM on 2026-09-04, with the conditions in the P07 POA&M.
- The majority owner approved the treatment plans for the High and Very High risks in P01 on 2026-09-04 and accepted none of them.
- Condition: the integrator VPN and refrigeration modem are disabled except during approved, supervised sessions until the remote access gateway is live (2026-10-31).
### 4.3 System Operational Status
Operational. Major modifications planned: OT DMZ and firewall rebuild (due 2027-03-31) and named HMI and recipe-system accounts (due 2026-12-31). Both require a food defense reanalysis check under 21 CFR 121.157(c) before they go live.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | General Manager | Overall accountability; risk acceptance up to Moderate; signs the food defense plan |
| Risk acceptor (authorizing official equivalent) | Majority owner | Acceptance of High and Very High risks |
| Security lead | IT Manager | IT and OT security, identity, cloud tenant, network |
| OT system owner | Controls Engineer | PLCs, HMIs, SCADA, historian, MES |
| Food safety and food defense owner | FSQA Manager | HACCP records, food defense plan, product holds and notifications |
| Refrigeration owner | Maintenance and Refrigeration Manager | Refrigeration controls, generator, PSM program |
| External support | Controls integrator; refrigeration contractor; cold-chain monitoring vendor | Remote maintenance and SaaS service |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and adapted for OT. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Process control data (setpoints, formulations, PLC logic, cure and brine dosing) | Moderate | **High** | Moderate | A changed cure level, cook cycle, or CIP valve state can produce adulterated food that reaches consumers; that is a severe adverse effect on individuals. Formulations are trade secrets. Local controllers keep running if supervisory systems fail |
| CCP monitoring and food safety records (HACCP, seafood HACCP, food defense) | Low | **High** | Moderate | Product cannot ship without complete, trustworthy records (9 CFR 417.5(c)); falsified records could hide a deviation. Paper workaround covers up to 24 hours (P05) |
| Cold-chain monitoring data | Low | Moderate | **Moderate** | Loss of monitoring for more than 2 hours forces product evaluation (P05 BP-01 MTD 2 h); manual log is the workaround |
| Food defense plan and vulnerability assessment | **Moderate** | Moderate | Low | Disclosure gives an attacker a map of vulnerable steps |
| Traceability and lot data | Low | Moderate | Moderate | Needed within 24 hours for FSIS recall notice (9 CFR 418.2) |
| **PPCM category (high-water mark)** | **Moderate** | **High** | **Moderate** | Overall: **High** |

**Baseline:** the NIST SP 800-53B High baseline, tailored with the SP 800-82 Rev. 3 OT overlay for a 250-person plant. The plan documents 61 controls that address the food defense, HACCP record, and OT risks in P01 and P03 (see `control-implementation.csv`). Every other High-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, where their SOC 2 reports support it (P09).
- **Tailored out** with a recorded reason, where the control assumes federal systems or capabilities disproportionate to this plant (for example PM-series program controls beyond PM-2, and AC-7 lockout on HMIs, where operator lockout during an upset is itself a safety risk).
- **Compensated** in OT where the IT form of a control would disrupt the process, following SP 800-82 Rev. 3 (for example, application allowlisting instead of agent-based scanning on HMIs).

## 7. Authorization Boundary Description
- **Inside:** SYS-01 to SYS-06 and SYS-14: PLCs, HMIs, dosing skid, brine tank and CIP controls, smokehouse controllers, packaging controls, SCADA, historian, engineering workstation, MES, the refrigeration controller, the cold-chain sensors and gateway, the company's configuration of the cold-chain SaaS, the cloud tenant (four workloads), and the remote access paths.
- **Outside (interconnected):** ERP (SYS-07), WMS (SYS-08), identity provider (SYS-09), corporate network and endpoints (SYS-11), AI vision inspection (SYS-13), the cold-chain vendor's platform, and the cloud provider's infrastructure.
- **Boundary weaknesses:** the MES server is dual-homed on the corporate and control networks, and the cold-chain gateway sits on the corporate Wi-Fi. Both cross the boundary without a controlled interface and are scheduled for correction (POAM-001).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| ERP (SYS-07) | Bidirectional (MES to ERP) | Production orders, consumption, lots | SaaS contract |
| WMS (SYS-08) | Inbound to MES | Lot and pallet data for labels | SaaS contract |
| Cloud tenant (SYS-06) | Outbound (historian replica every 15 minutes; records) | CCP data, food safety records, traceability | Cloud provider agreement |
| Cold-chain SaaS (SYS-04) | Outbound from gateway; alerts outbound by SMS | Temperatures, alarms | SaaS contract (no security terms; gap) |
| Controls integrator (SYS-14) | Inbound remote access | SCADA and PLC sessions | Service contract (no interconnection or security terms; gap) |
| Refrigeration contractor (SYS-14) | Inbound remote access (cellular modem) | Refrigeration controller sessions | Service contract (no security terms; gap) |
| AI vision inspection (SYS-13) | Inbound lot data; outbound reject counts | Lot codes, inspection results | Vendor contract (see P10) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| PLCs (about 30), dosing skid, CIP manifolds, smokehouse controllers (5), packaging controls, metal detectors | OT field and control devices | Lines 1-4 | Controls Engineer |
| HMIs (12, two on an unsupported OS) | OT supervisory | Production floor | Controls Engineer |
| SCADA server, historian, engineering workstation | OT level 3 servers | Plant server room | Controls Engineer |
| Recipe, batch, and lot-coding server (MES) | OT level 3 server (dual-homed, gap) | Plant server room | Controls Engineer |
| Refrigeration controller and cellular modem | OT controller | Engine room | Maintenance and Refrigeration Manager |
| Cold-chain sensors (64) and gateway | IoT | Coolers, freezer, seafood room, trailers | Warehouse and Logistics Manager |
| Cold-chain dashboard and alerting | SaaS | Cold-chain monitoring vendor | Warehouse and Logistics Manager |
| Records application, historian replica, traceability database | Cloud PaaS database and application service | Cloud tenant | IT Manager (FSQA Manager owns the data) |
| Backup vault | Cloud backup service | Cloud tenant (same account, gap) | IT Manager |
| Network storage device (OT backups) | On-premises storage | Plant server room (gap) | Controls Engineer |
| Corporate-to-OT firewall | Network | Plant server room | IT Manager |

The OT component counts above are from interviews and a walkthrough. A formal OT asset inventory does not exist yet (CM-8, POAM-015).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 61 controls:
- Implemented: 13
- Partially implemented: 32
- Planned: 16
- Not applicable: 0

### 10.2 Control assessment status
Assessed 2026-08-10 to 2026-08-15. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Business and cloud users authenticate through the identity provider with a password and a second factor (a phone authenticator app, or a hardware key for the two cloud administrators). That is appropriate for the Moderate confidentiality of the business data.

**OT access does not meet this statement today.** HMIs, SCADA, the recipe system, and the records application administrator use shared accounts, and OT remote access has no MFA. Because PPCM integrity is High, the target state is:
- named accounts on HMIs with fast badge or PIN sign-in, so operators are not slowed during an upset;
- MFA for all engineering, recipe-approval, and remote access;
- a second approver for formulation changes.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 self-benchmark and vendor review (P09), AI assessment (P10), the 2023 food defense plan, and the HACCP plans.

## 13. Acronym List and Glossary
- **CCP:** critical control point (9 CFR 417.1)
- **CIP:** clean-in-place
- **DMZ:** demilitarized zone (a buffer network between business and control networks)
- **HMI:** human-machine interface
- **MES:** manufacturing execution system (here, the recipe, batch, and lot-coding system)
- **OT:** operational technology
- **PLC:** programmable logic controller
- **PPCM:** Plant Production and Cold-Chain Monitoring System
- **SCADA:** supervisory control and data acquisition

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial plan | IT Manager with the Controls Engineer |

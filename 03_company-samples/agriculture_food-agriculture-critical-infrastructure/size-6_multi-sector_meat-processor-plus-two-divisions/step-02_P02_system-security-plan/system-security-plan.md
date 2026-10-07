# System Security Plan: Plant Production and Cold-Chain Monitoring System (PPCM)

**Organization:** Cris Santos Company Holdings, Inc. (Meat Processing division, six plants, inheriting corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Food and Agriculture
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), with OT guidance from NIST SP 800-82 Rev. 3 | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the focus division's primary system, the **PPCM**, because it is where a cyber event becomes a food safety event: it runs and records every step that makes the six plants' food safe, and it carries the group's food defense risk (P01 GR-09). It also shows inheritance clearly: most of its controls come from corporate (SYS-G1, SYS-G2, SYS-G3, SYS-G5) and from the shared cold-chain platform (SYS-G6). The group common control catalog (`common-control-catalog.csv`, 82 controls) is the same catalog Food Distribution and Grocery Retail inherit from.

## 1. System Name and Identifier
Plant Production and Cold-Chain Monitoring System (**PPCM**), identifier CSCH-MP-SYS-001. It covers SYS-M1 to SYS-M5 and the plant tier of SYS-G6 in `../00_company-facts.md` section 3.

## 2. System Overview
The PPCM runs and records formulation and cure dosing, cooking and smoking, chilling, packaging and lot coding, and cold storage at six plants. It produces the electronic CCP records that FSIS inspection program personnel review at every plant, and at Plant 6 the food defense monitoring records required by 21 CFR Part 121. About 9,500 production, maintenance, FSQA, and warehouse staff use it across two production shifts and a sanitation shift.

**Major components:**
- **SYS-M1:** process control networks: about 2,100 OT devices (PLCs, dosing skids, smokehouse and oven controllers, CIP manifolds, slicers, packaging lines, metal detectors, checkweighers) and 310 HMIs
- **SYS-M2:** SCADA servers, process historians, and engineering workstations at each plant
- **SYS-M3:** plant MES (recipe, batch, lot coding) and the central recipe master library hosted on SYS-G3
- **SYS-M4:** ammonia refrigeration control systems (five plants above the PSM threshold)
- **SYS-M5:** food safety records application on SYS-G3 (electronic HACCP and Sanitation SOP records, food defense monitoring, pre-shipment review)
- **SYS-G6 (plant tier):** cold-chain sensors and gateways in plant coolers, freezers, and docks, with alert routing through the group alert integration server

OT zones follow the SP 800-82 Rev. 3 layered model (levels 0 to 3 in the plant, level 3.5 OT DMZ, level 4 business network). Plants 1, 3, 4, and 6 are built to the group OT reference architecture. Plants 2 and 5 (acquired 2024) are not: their OT servers are joined to the corporate directory domain and their networks are flat (section 7).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the PPCM |
|---|---|---|---|
| C-FOOD-AG-R01 | FSMA Intentional Adulteration rule | 21 CFR Part 121 | Applies to **Plant 6** only, the one FDA-registered plant (its plant-based line makes FDA-regulated food). Dosing, CIP, and recipe-system paths are points where an attacker could adulterate food; mitigation strategies, monitoring, and records live in the PPCM |
| FSIS | HACCP systems | 9 CFR Part 417 | All six plants. CCP monitoring by historians and cold-chain sensors; computer records need integrity controls for electronic data and signatures (417.5(d)) |
| FSIS | Recalls | 9 CFR Part 418 | 24-hour notice to the FSIS District Office if adulterated or misbranded product entered commerce (418.2) |
| FDA | Reportable Food Registry | 21 U.S.C. 350f(d) | 24-hour report for a reportable food from Plant 6 (P08) |
| Benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 | Voluntary | OT control expectations used to tailor the baseline |
| C-FOOD-AG-R02 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | **Not in effect.** As proposed, the group would exceed the SBA size standard for NAICS 311612 and would be covered. Tracked only |
| SEC | Cybersecurity incident disclosure | Form 8-K Item 1.05 | A PPCM incident may be material to the group (P08) |
| Internal | Group policies POL-01 to POL-05 and the Meat Processing supplement | P06 | Apply to IT and OT |

Not applicable: USCG MTS cyber rule (C-FOOD-AG-R03), because no plant is an MTSA-regulated facility. OSHA PSM (29 CFR 1910.119) and EPA RMP (40 CFR Part 68) apply to the ammonia systems as process safety rules managed by plant PSM programs; they are context here, but the refrigeration controllers are inside the boundary.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Meat Processing division president (system owner) and the Group CISO on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks), with the Group Chief Food Safety and Quality Officer concurring.
- **Conditions:** (1) the Plants 2 and 5 integrator VPN and the Plant 5 refrigeration modem are disabled except during approved, supervised sessions until SYS-G5 is live there (POAM-002, due 2026-12-31); (2) default OT passwords found in P07 are changed at all plants by 2026-09-30 (P01 MT-030); (3) no OT change at Plant 6 goes live without a food defense reanalysis check under 21 CFR 121.157(c) (POAM-007); (4) the Plants 2 and 5 OT domain migration and DMZ are completed by 2027-03-31 (POAM-001).
- **Reauthorization:** annually, or when Plants 2 and 5 reach the reference architecture.

### 4.3 System Operational Status
Operational. **Major modifications planned:** OT DMZ and OT domain migration at Plants 2 and 5 (due 2027-03-31); named HMI sign-in with badge and PIN, phased by plant (due 2027-06-30). Both require HACCP reassessment checks (9 CFR 417.4(a)(3)) and, at Plant 6, a food defense reanalysis check.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Meat Processing division president | Accountable for the PPCM; accepts Moderate risks |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Food safety owner | Division VP FSQA, with plant FSQA managers | HACCP records, product holds, FSIS notices |
| Food defense owner (Plant 6) | Plant 6 FSQA manager (qualified individual, 21 CFR 121.4(c)); Plant 6 plant manager signs the plan (121.310) | Vulnerability assessment, mitigation strategies, reanalysis |
| OT system owner | Division controls engineering manager | PLCs, HMIs, SCADA, historians, MES, recipe library |
| Division security lead | Meat Processing security and compliance lead | Division register, supplement, and inheritance matrix |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group infrastructure director (SYS-G3), Group OT security director (SYS-G5), Group cold-chain services manager (SYS-G6) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and the PPCM's own controls (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and adapted for OT. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Process control data (setpoints, formulations, PLC logic, cure and brine dosing) | Moderate | **High** | Moderate | A changed cure level, cook cycle, or CIP valve state can produce adulterated food that reaches consumers in many states: a severe adverse effect. Formulations are trade secrets. Local controllers keep running if supervisory systems fail |
| CCP monitoring and food safety records (HACCP, Plant 6 food defense) | Low | **High** | Moderate | Product cannot ship without complete, trustworthy records (9 CFR 417.5(c)); falsified records could hide a deviation. Paper workaround covers up to 24 hours (P05 BP-M05) |
| Cold-chain monitoring data (plant tier) | Low | Moderate | **High** | Loss of monitoring for more than 2 hours forces product evaluation at every affected plant (P05 BP-M01, MTD 2 hours), and the shared alert path serves all divisions |
| Plant 6 food defense plan and vulnerability assessment | **Moderate** | Moderate | Low | Disclosure gives an attacker a map of vulnerable steps |
| Traceability and lot data | Low | Moderate | Moderate | Needed within hours for an FSIS recall notice (9 CFR 418.2) |
| **PPCM category (high-water mark)** | **Moderate** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored with the SP 800-82 Rev. 3 OT overlay. The plan documents **104 controls** in `control-implementation.csv`:
- 100 from the High baseline;
- 1 from the privacy baseline (PM-9, the group risk management strategy that sets acceptance authority);
- 3 program management controls not in any baseline (PM-1, PM-2, PM-16; PM-16 brings sector threat information to plants).

Other High-baseline controls are inherited from the cloud providers and SaaS vendors (evidenced by their SOC 2 reports, P09), or tailored out with a reason in the group tailoring register (for example, AC-7 lockout on HMIs, where operator lockout during an upset is itself a safety risk, and controls that assume federal systems). Where the IT form of a control would disrupt the process, SP 800-82 Rev. 3 compensating forms are used (for example, application allowlisting instead of agent-based scanning on HMIs).

## 7. Authorization Boundary Description
- **Inside:** SYS-M1 to SYS-M5 at all six plants (PLCs, HMIs, dosing skids, CIP controls, smokehouse controllers, packaging controls, SCADA, historians, engineering workstations, MES, refrigeration controllers), the recipe master library and SYS-M5 accounts in provider A, and the plant tier of SYS-G6 (sensors, gateways, and the plants' configuration in the vendor SaaS).
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SIEM, and EDR, SYS-G3 cloud landing zone and colocation network, SYS-G5 OT remote access gateway and OT monitoring, and the SYS-G6 platform core (vendor SaaS and the alert integration server).
- **Outside, interconnected:** SYS-G4 ERP (production orders, consumption), SYS-D1 WMS (lot and pallet data for shipments to DCs), and SYS-M6 AI vision inspection (lot data in, reject counts out).
- **Boundary weaknesses:** at Plants 2 and 5 the OT servers are members of the corporate directory domain and the networks are flat, so the boundary is administrative, not technical (POAM-001). Cold-chain gateways at Plants 2 and 5 sit on the business network.

The diagrams are in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-G4 ERP | Bidirectional | Production orders, consumption, lots | Internal interconnection record |
| SYS-D1 WMS (Food Distribution) | Outbound | Lot and pallet data for shipments to DCs | Internal interconnection record (division to division) |
| SYS-G6 cold-chain platform core | Outbound readings; inbound alerts | Temperatures, alarms | Group service; vendor SaaS contract (security terms added 2025; SOC 2 review lapsed, POAM-006) |
| Recipe master library (SYS-G3) | Outbound releases to plant MES | Signed formulation releases | Internal |
| SYS-G5 gateway | Inbound remote sessions (Plants 1, 3, 4, 6) | Engineering and vendor sessions | Group OT remote access standard |
| Controls integrator (Plants 2 and 5) | Inbound shared VPN | SCADA and PLC sessions | Legacy contract with **no security terms** (POAM-015) |
| Refrigeration contractor (Plant 5) | Inbound cellular modem | Refrigeration controller sessions | Service contract with **no security terms** (POAM-015) |
| SYS-M6 AI vision inspection | Inbound lot data; outbound reject counts | Lot codes, inspection results | Vendor contract (P10) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| PLCs, dosing skids, CIP manifolds, smokehouse and oven controllers, packaging controls, metal detectors (about 2,100 devices) | OT field and control devices | Six plants | Division controls engineering manager |
| HMIs (310; 24 on an unsupported OS at Plants 2 and 5) | OT supervisory | Production floors | Plant controls engineers |
| SCADA servers, historians, engineering workstations | OT level 3 | Plant server rooms | Plant controls engineers |
| Plant MES servers | OT level 3 | Plant server rooms | Plant controls engineers |
| Recipe master library | PaaS application and database | Provider A (replica in provider B) | Division controls engineering manager |
| Refrigeration controllers | OT controllers | Engine rooms (five plants above threshold; Plant 4 low-charge) | Plant refrigeration managers |
| Cold-chain sensors and gateways (plant tier, about 4,300 sensors) | IoT | Coolers, freezers, docks | Division VP FSQA |
| SYS-M5 food safety records application | PaaS application and database | Provider A (immutable backups in provider B) | Division VP FSQA |
| OT DMZ and plant firewalls | Network | Plants 1, 3, 4, 6 (not Plants 2 and 5) | Group OT security director |

Plants 1, 3, 4, and 6 inventories come from passive OT monitoring (CM-8). Plants 2 and 5 inventories are 2024 spreadsheets (POAM-008).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (104 controls) and `common-control-catalog.csv` (82 group common controls).

| Status | Controls |
|---|---|
| Implemented | 48 |
| Partially implemented | 53 |
| Planned | 3 |
| Not applicable | 0 |
| **Total** | **104** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, SYS-G5, group governance, or group HR) | 51 |
| Hybrid (a group provider supplies the mechanism; the division configures or operates part) | 31 |
| System-specific | 22 |

**Why so many partially implemented controls.** Most of the 53 are partial for one reason: the control works at Plants 1, 3, 4, and 6 but not yet at the two acquired plants. The rest cluster in three places:
- **Plants 2 and 5 below the reference architecture** (scenario gap 1): AC-4, AC-17, AC-17(1), MA-4, MA-5, SC-7, SC-7(5), CM-2, CM-7, CM-8, CP-9, CP-10, SI-2, SI-3, SI-4, RA-5, MP-7, SA-22, PL-8, AU-12, AC-6(9).
- **Shared operator logins and record integrity** (scenario gap 4): AC-2, AC-3, AC-5, AC-6, AC-11, AU-3, AU-9, IA-2, IA-2(2), IA-5, CM-5, SI-7.
- **Food defense change control, the shared cold-chain platform, suppliers, and cross-division incident handling** (gaps 2, 3, 6, and 9): CM-3, CM-4, CA-7, CA-3, CP-2, CP-4, CP-7, SA-4, SA-9, PS-7, SR-3, AU-6, AT-2, AT-3, IR-2, IR-3, IR-4, IR-6, IR-8, AC-18.

The 3 planned controls are AU-10 (electronic signatures in SYS-M5), RA-9 (criticality analysis of components that act on food), and SR-6 (annual OT and cold-chain supplier reviews).

### 10.2 Common control inheritance by division
The common control catalog lists 82 controls provided by corporate. Inheritance is **documented for Meat Processing** (2025 inheritance matrix; SYS-G5 coverage limited to Plants 1, 3, 4, and 6), for **Grocery Retail** (the PCI DSS responsibility matrix in the 2025 ROC), and for the **PPCM** (this plan). It is **not documented for Food Distribution** (scenario gap 7). Until POAM-017 closes, Food Distribution cannot show its 3PL customers or the service auditor (P09) which controls it inherits, and P07 found CA-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and PPCM and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit, with OT testing at Plants 2, 5, and 6 during weekend sanitation windows. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **IT and engineering users** authenticate through SYS-G1 with MFA; **administrators and OT engineers** use phishing-resistant authenticators and just-in-time PAM elevation. Vendors use named external accounts with MFA on SYS-G5. This fits a High-integrity system with remote engineering access.
- **Operators on HMIs** use shared logins today, which does not meet this statement because PPCM integrity is High. The target is named sign-in with badge and PIN (fast enough not to slow an operator during an upset) at all 310 HMIs by 2027-06-30 (POAM-003), and named MES accounts with two-person formulation approval at Plants 2 and 5 by 2026-12-31.
- **Service accounts** that touch OT must be managed in PAM; 34 privileged directory service accounts are not yet (POAM-012).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud architecture and control map (P04), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness and vendor review (P09), AI governance (P10), the Plant 6 food defense plan (2024), and each plant's HACCP plans.

## 13. Acronym List and Glossary
- **CCP:** critical control point (9 CFR 417.1)
- **CIP:** clean-in-place
- **Common control:** a control provided once by corporate and inherited by several systems
- **DMZ:** demilitarized zone (a buffer network between business and control networks)
- **HMI:** human-machine interface
- **MES:** manufacturing execution system (recipe, batch, and lot coding)
- **OT:** operational technology
- **PAM:** privileged access management
- **PSM:** process safety management (29 CFR 1910.119)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Meat Processing security and compliance lead |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |

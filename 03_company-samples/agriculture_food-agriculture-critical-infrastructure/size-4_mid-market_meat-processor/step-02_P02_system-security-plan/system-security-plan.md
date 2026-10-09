# System Security Plan: Plant Production and Cold-Chain Monitoring System (PPCM)

**Organization:** Cris Santos Company, Inc. (PE-backed meat processor with two USDA-inspected plants) | **Tier:** Mid-Market | **Vertical:** Food and Agriculture
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), with OT guidance from NIST SP 800-82 Rev. 3 | **Version:** 1.0, 2026-09-15
**Sources:** the intake [evidence register](../step-00_P00_intake/evidence-register.csv) (configuration exports, OT inventories and documents, EV-001 to EV-059), the plant walkthroughs in P03 fieldwork (EV-062, EV-063), and the P07 test results (EV-AC-2 to EV-SR-6). The `evidence` column in `control-implementation.csv` names the source of each statement.

## 1. System Name and Identifier
Plant Production and Cold-Chain Monitoring System (**PPCM**), identifier CSC-PPCM-01. The PPCM is the company's major system. It comprises SYS-01 to SYS-07, SYS-14, and SYS-15 in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv).

## 2. System Overview
The PPCM runs and records every step that makes the company's food safe at both plants: formulation and cure dosing, cooking, smoking, and chilling, grinding and blending, packaging, foreign material inspection, lot coding and labeling, and cold storage. It also supervises the two ammonia refrigeration systems. It produces the electronic CCP, Sanitation SOP, and Listeria records that FSIS reviews. It serves about 700 production, maintenance, warehouse, sanitation, and FSQA workers across two production shifts and a sanitation shift at each plant (P05 BP-01 to BP-09, BP-13).

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Plant 1 process control network: about 180 PLCs and 64 HMIs (smokehouses, spiral ovens, chillers, brine injectors, dosing skid, CIP, slicers, packaging, metal detectors, x-ray units) | On premises, Purdue levels 0-2 |
| SYS-02 | Plant 2 process control network: about 60 PLCs and 22 HMIs (grinders, blenders with fat analyzers, cutting, tray packaging, metal detectors) | On premises, levels 0-2 (flat with the Plant 2 office) |
| SYS-03 | SCADA servers, historians, and engineering workstations at both plants | On premises, level 3 |
| SYS-04 | Ammonia refrigeration controllers (one per plant) | On premises; vendor-maintained |
| SYS-05 | Cold-chain monitoring: about 260 sensors, gateways, and the vendor dashboard | Sensors and gateways on premises; vendor SaaS |
| SYS-06 | Plant 1 MES (recipe, batch, lot coding, labels) and the Plant 2 label and lot-code server | On premises, level 3 |
| SYS-07 | Cloud landing zone (4 accounts): records application, historian replicas, traceability database, backups | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-14 | OT remote access: Plant 1 gateway; Plant 2 integrator VPN and refrigeration modem | Internet-facing |
| SYS-15 | Plant 1 passive OT network monitoring sensor | On premises |

OT zones follow the SP 800-82 Rev. 3 layered model: field devices and controllers (levels 0-1), HMIs and supervisory control (level 2), SCADA, historians, and MES (level 3), an OT DMZ, and the business network (level 4). Plant 1 has this structure. Plant 2 does not (section 7).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it touches the PPCM |
|---|---|---|---|
| FSIS | Sanitation SOPs | 9 CFR 416.11-416.17 | Daily Sanitation SOP records may be kept on computers with integrity controls (416.16(b)); CIP controls sit in SYS-01 |
| FSIS | HACCP systems | 9 CFR Part 417 | CCP monitoring by historians and cold-chain sensors; entries at the time of the event, signed or initialed (417.5(b)); computer records need integrity controls for data and signatures (417.5(d)) |
| FSIS | Recalls | 9 CFR Part 418 | 24-hour notice if adulterated or misbranded product entered commerce (418.2); the traceability database supports it |
| FSIS | Listeria monocytogenes control (Plant 1) | 9 CFR 430.4 | Food contact surface testing results and hold-and-test records in the records application; verification results available to FSIS (430.4(c)(7)) |
| OSHA | Process safety management (ammonia) | 29 CFR 1910.119 | Refrigeration controls, alarms, and interlocks are mechanical integrity equipment ((j)(1)(v)); changes to them need management of change ((l)) |
| EPA | Risk management program, Program 3 (ammonia) | 40 CFR Part 68 | Same equipment under 68.73 and 68.75; emergency response program (68.95) |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2), (8) | Reasonable measures for employee personal information held in shared systems; disposal |
| Contract | Largest customer supply agreement; GFSI-benchmarked certification | Contract | Food defense plan; 24-hour event notice; SOC 2 Type 2 for the customer portal and EDI (P09, outside this boundary) |
| Benchmark | NIST CSF 2.0 and SP 800-82 Rev. 3 | Voluntary | OT control expectations used to tailor the baseline |
| Benchmark | FSMA Intentional Adulteration rule structure (C-FOOD-AG-R01) | 21 CFR Part 121 (voluntary here) | Vulnerability assessment and mitigation strategy method for the voluntary food defense plans |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Apply to IT and OT |

Not applicable:
- **21 CFR Part 121 as a legal requirement.** Both plants are regulated exclusively by USDA and are exempt from FDA registration (21 CFR 1.226(g)), so Part 121 does not bind them (121.1). It is used here only as a benchmark.
- **CIRCIA (C-FOOD-AG-R02):** proposed only; not in effect.
- **USCG MTS cyber rule (C-FOOD-AG-R03):** neither plant is an MTSA facility.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the PPCM accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:**
  1. The Plant 2 integrator VPN and refrigeration modem stay disabled except during approved, supervised sessions until Plant 2 moves onto the remote access gateway (due 2026-10-31; POAM-004).
  2. The High and Very High POA&M items in P07 meet their milestones, and the audit committee receives POA&M status each quarter.
  3. Re-decision by 2027-09-30, or after a major change (for example, the Plant 2 network rebuild or another acquisition).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Plant 2 segmentation and OT DMZ, modeled on Plant 1 (due 2027-03-31)
- Named HMI and MES accounts at both plants, with two-person approval for setpoint and recipe changes (due 2027-03-31)
- OT monitoring sent to the MSSP from both plants (due 2027-01-31)
- Immutable OT backups and a Plant 2 PLC repository (due 2026-12-31)

Each modification is an OT change. It needs a food safety review (HACCP reassessment trigger, 9 CFR 417.4(a)(3)) and a PSM management of change review where it touches the refrigeration systems (29 CFR 1910.119(l)) before it goes live.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the PPCM; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Security lead | Security Manager | Day-to-day security for IT and OT; incident commander; MSSP liaison |
| OT security | OT security engineer | OT monitoring, OT vulnerability management, remote access gateway |
| IT control owner | IT Director | Identity provider, landing zone, networks, IT/OT boundary firewalls, endpoints |
| OT system owner | Controls Engineering Manager | PLCs, HMIs, SCADA, historians, MES, engineering workstations; manages the controls integrators |
| Food safety owner | Vice President of Food Safety and Quality Assurance | CCP record integrity, product holds, FSIS notifications, voluntary food defense plans |
| Responsible establishment officials | Plant Manager, Plant 1; Plant Manager, Plant 2 | Sign HACCP plans and Sanitation SOPs; line restart decisions |
| Process safety owner | Director of Engineering and Maintenance | Refrigeration controllers, PSM and RMP programs; manages the refrigeration contractors |
| Cold chain | Director of Supply Chain and Logistics | Cold-chain monitoring service and alert routing |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring of IT; OT onboarding planned |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1, adapted for OT. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Process control data (setpoints, formulations, PLC logic, cure and brine dosing, blend targets) | Moderate | **High** | Moderate | A changed cure level, cook cycle, chill target, or CIP valve state can produce adulterated food that reaches consumers in many states: a severe adverse effect on individuals. Formulations are trade secrets. Local controllers keep running if supervisory systems fail |
| Refrigeration control and ammonia alarm data | Low | **High** | **High** | Manipulated alarms or controller logic could contribute to an ammonia release affecting workers and neighbors; BIA MTD for BP-13 is 1 hour |
| CCP monitoring and food safety records (HACCP, Sanitation SOP, Listeria) | Low | **High** | Moderate | Product cannot ship without complete, trustworthy records (9 CFR 417.5(c)); falsified records could hide a deviation. Paper workaround covers up to 24 hours (P05 BP-09) |
| Cold-chain monitoring data | Low | Moderate | Moderate | Loss of monitoring for more than 2 hours forces product evaluation (P05 BP-01, BP-06 MTD 2 hours); manual log is the workaround |
| Food defense plans and vulnerability assessments | **Moderate** | Moderate | Low | Disclosure gives an attacker a map of vulnerable steps |
| Traceability and lot data | Low | Moderate | Moderate | Needed within hours for the FSIS 24-hour notice (9 CFR 418.2) |
| **PPCM category (high-water mark)** | **Moderate** | **High** | **High** | Overall: **High** |

**Why High and not Moderate.** The tier guide expects a Moderate system at this size. The PPCM is categorized on its own information types, not on company size: integrity of process control data and availability of the ammonia alarm view both reach High. The baseline is therefore the **NIST SP 800-53B High baseline**, tailored with the SP 800-82 Rev. 3 OT overlay.

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv). OT device counts come from the Plant 1 passive sensor export (EV-011) and the Plant 2 integrator and maintenance records (EV-012); the network layout comes from the diagrams and firewall exports (EV-014) and the remote access records (EV-016, EV-017).

**Inside the boundary:**
- PLCs, HMIs, smokehouse and oven controllers, injectors, the dosing skid, CIP controls, blenders and fat analyzers, packaging controls, metal detectors, and x-ray units at both plants;
- SCADA servers, historians, engineering workstations, the Plant 1 MES, and the Plant 2 label server;
- both refrigeration controllers and their remote access paths;
- the cold-chain sensors and gateways, and the company's configuration of the cold-chain SaaS;
- the 4 cloud accounts and the PPCM workloads in them (records application, historian replicas, traceability database, backups);
- the Plant 1 remote access gateway and the passive OT sensor.

**Outside the boundary (interconnected):**
- ERP (SYS-08), WMS (SYS-09), identity provider (SYS-10), corporate networks and endpoints (SYS-11), and the MSSP's SIEM (SYS-12);
- the AI vision system on Plant 1 Lines 5-7 (SYS-16, AI-001);
- the customer traceability portal and EDI gateway, which share the workloads account but are a separate system (the SOC 2 system in P09);
- the cold-chain vendor's platform and the cloud provider's infrastructure.

**Boundary weaknesses:**
- At Plant 2, the office network, OT, and cold-chain gateways share one flat network.
- The Plant 2 integrator VPN and the refrigeration modem cross the boundary without a controlled interface.

Both are scheduled for correction (POAM-016 and POAM-004). The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| ERP (SYS-08) | Bidirectional through the Plant 1 OT DMZ broker; direct from Plant 2 | Production orders, consumption, lots | SaaS contract with security terms |
| WMS (SYS-09) | Inbound to the MES and Plant 2 label server | Lot and pallet data for labels | SaaS contract with security terms |
| Cloud landing zone (SYS-07) | Outbound (historian replicas every 15 minutes; records) | CCP data, food safety records, traceability | Cloud provider agreement |
| Cold-chain SaaS (SYS-05) | Outbound from gateways; alerts by app, phone, and SMS | Temperatures, alarms | SaaS contract (no security terms; gap) |
| Plant 1 controls integrator (SYS-14) | Inbound through the gateway | SCADA, MES, and PLC sessions | Service contract (no security terms; gap) |
| Plant 2 controls integrator (SYS-14) | Inbound shared VPN | SCADA, blender, and PLC sessions | Service contract inherited from the prior owner (no security terms; gap) |
| Refrigeration contractors (SYS-04, SYS-14) | Inbound (gateway at Plant 1; cellular modem at Plant 2) | Controller sessions | Service contracts (no security terms; gap) |
| AI vision system (SYS-16) | Inbound lot data; outbound reject counts and images to the vendor cloud | Lot codes, inspection results, product images | Vendor contract (see P10) |
| MSSP (SYS-12) | Inbound logs from IT boundary devices | Security logs | MSSP contract; SOC 2 Type 2 |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| PLCs (about 180), smokehouse and oven controllers, injectors, dosing skid, CIP, packaging, metal detectors, x-ray units | OT field and control devices | Plant 1 Lines 1-9 | Controls Engineering Manager |
| HMIs (64, 6 on an unsupported OS) | OT supervisory | Plant 1 floor | Controls Engineering Manager |
| PLCs (about 60), grinders, blenders, fat analyzers, packaging, metal detectors | OT field and control devices | Plant 2 lines | Controls Engineering Manager |
| HMIs (22, 3 on an unsupported OS) | OT supervisory | Plant 2 floor | Controls Engineering Manager |
| SCADA servers, historians, engineering workstations (2 unsupported) | OT level 3 | Plant 1 OT server room; Plant 2 server closet | Controls Engineering Manager |
| MES (Plant 1) and label server (Plant 2) | OT level 3 | Plant 1 OT server room; Plant 2 server closet | Controls Engineering Manager |
| OT backup server | On-premises storage (not immutable; gap) | Plant 1 OT server room | Controls Engineering Manager |
| Refrigeration controllers; Plant 2 cellular modem | OT controllers | Both engine rooms | Director of Engineering and Maintenance |
| Cold-chain sensors (about 260) and gateways | IoT | Coolers, freezers, trailers | Director of Supply Chain and Logistics |
| Cold-chain dashboard and alerting | SaaS | Cold-chain monitoring vendor | Director of Supply Chain and Logistics |
| OT DMZ and boundary firewalls (Plant 1); Plant 2 perimeter firewall | Network | Both plants | IT Director |
| Remote access gateway | Network appliance | Plant 1 OT DMZ | OT security engineer |
| Passive OT sensor | Network monitoring | Plant 1 | OT security engineer |
| Records application, historian replicas, traceability database | Cloud PaaS application and database services | Workloads account | IT Director (VP FSQA owns the data) |
| Backup vault | Cloud backup service with write-once retention | Backup account (second region) | IT Director |

The OT counts above come from the Plant 1 passive sensor export (EV-011), the Plant 2 integrator and maintenance records (EV-012), the unsupported component list (EV-013), and the walkthroughs (EV-062, EV-063). A complete OT inventory does not exist yet at Plant 2 (CM-8, POAM-008).

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The PPCM uses the NIST SP 800-53B **High** baseline (370 controls and enhancements), tailored as follows:
- **Documented here: 115 controls** in `control-implementation.csv`. They cover every control that addresses a risk in P01 or a requirement in P03 (record integrity, process control changes, OT remote access, segmentation, monitoring, recovery, suppliers), plus the program controls the audit committee reporting depends on.
- **Selected by tailoring (added):** PM-2 and PM-9, which are not in the High baseline but anchor the security lead role and the risk appetite.
- **Compensated in OT** where the IT form of a control would disrupt the process, following SP 800-82 Rev. 3: no account lockout on HMIs (AC-7), unencrypted industrial protocols protected by segmentation (SC-8), and application allowlisting instead of agent-based EDR on OT hosts (CM-7(5), SI-3).
- **Inherited without separate statements:** the physical and environmental controls of the cloud and SaaS data centers (for example PE-9 to PE-17 for those sites) and platform-level SA and SC controls, inherited from the cloud provider, the identity provider, and the MSSP and evidenced by their SOC 2 Type 2 reports (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other High-baseline controls with no P01 risk at Moderate or above and no P03 requirement (for example SA-11 developer testing and SA-15 development process, because the company does not develop software). They are recorded as tailoring decisions and reviewed each year.

**CSF 2.0 column.** Subcategories come from NIST's CSF 2.0 to SP 800-53 Rev. 5 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`) where NIST maps the control. For 13 controls NIST gives no mapping (AC-11, AU-8, CA-6, CP-3, IR-2, MA-4, MA-5, MP-6, MP-7, PL-4, PS-3, PS-4, PS-5); their subcategories are an author mapping.

**Status of the 115 documented controls:**
| Status | Count |
|---|---|
| Implemented | 25 |
| Partially implemented | 83 |
| Planned | 7 |
| Not applicable | 0 |

**Inheritance of the 115 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 81 | Company |
| Hybrid | 30 | Identity provider vendor (11), cloud provider (10), MSSP (8), cold-chain, ERP, and WMS vendors (1) |
| Common/Inherited | 4 | Identity provider vendor (AC-2(1), IA-2(2), IA-2(8)); cyber insurer panel and MSSP (IR-7) |

The Partially implemented statements trace to the intake observations cited in the `evidence` column of `control-implementation.csv` (for example EV-007, EV-017, EV-022 and EV-025) and to the P07 findings. The pattern is consistent: the IT and cloud layers are close to complete, Plant 1 OT is partly built, and Plant 2 OT has almost nothing.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 32 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce (business and cloud).** Users authenticate through the identity provider with a password and push MFA with number matching, under conditional access. Cloud administrators use phishing-resistant security keys. That fits the Moderate confidentiality of business data.
- **OT does not meet this statement today.** HMIs, SCADA, the MES, and the Plant 2 directory use shared accounts, and Plant 2 OT remote access has no MFA. Because PPCM integrity is High, the target state is:
  - named accounts on HMIs with fast badge or PIN sign-in, so operators are not slowed during an upset;
  - MFA for all engineering, recipe-approval, and remote access;
  - a second approver for setpoint, recipe, and blend changes.
- **Records signatures.** Electronic CCP and Sanitation SOP record entries must be attributable to the employee who made them (9 CFR 417.5(b), 416.16(a)). Typed initials under a shared login do not meet that. Named accounts with an authenticated sign-off are the target (POAM-017).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); HACCP plans, Sanitation SOPs, and the PSM and RMP program documents for both plants.

## 13. Acronym List and Glossary
- **CCP:** critical control point (9 CFR 417.1)
- **CIP:** clean-in-place
- **DMZ:** demilitarized zone (a buffer network between business and control networks)
- **EDR:** endpoint detection and response
- **FSQA:** food safety and quality assurance
- **HMI:** human-machine interface
- **MES:** manufacturing execution system (here, the recipe, batch, lot-coding, and labeling system)
- **MSSP:** managed security service provider
- **OT:** operational technology
- **PLC:** programmable logic controller
- **PPCM:** Plant Production and Cold-Chain Monitoring System
- **PSM, RMP:** OSHA process safety management; EPA risk management program
- **SCADA:** supervisory control and data acquisition

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-24 | Draft from the risk assessment and gap analysis | Security Manager with the Controls Engineering Manager |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | Security Manager |

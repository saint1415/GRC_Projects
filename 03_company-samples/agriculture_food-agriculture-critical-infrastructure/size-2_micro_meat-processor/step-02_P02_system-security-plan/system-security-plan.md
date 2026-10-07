# System Security Plan: Plant Production and Cold-Chain Monitoring System (PPCM)

**Organization:** Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) | **Tier:** Micro | **Vertical:** Food and Agriculture
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), with OT guidance from NIST SP 800-82 Rev. 3 | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Plant Production and Cold-Chain Monitoring System (**PPCM**), identifier CSC-SYS-001.

## 2. System Overview
The PPCM runs and records the steps that make the plant's products safe: formulation and stuffing, cooking and smoking, chilling, packaging and labeling, and cold storage. It also holds the electronic Sanitation SOP and HACCP records that FSIS inspection program personnel review. It serves all 7 employees on one production shift.

The company owns little IT. The office side is SaaS run by vendors, with an MSP for the computers, firewall, and backup. The plant side is three machine controllers supported remotely by their manufacturers. Nobody had looked at the two sides together before this plan. This plan says, for each control, what the company does itself, what the MSP or a vendor does for it, and what it inherits.

**Major components:**
- **SYS-01:** smokehouse controller (cook and smoke cycles; core-probe log; manufacturer cloud connection)
- **SYS-02:** Line 1 stuffer and linker HMI; Line 2 packager PLC, HMI, and label printer-applicator
- **SYS-03:** labeling PC (label templates, lot codes, smokehouse vendor software)
- **SYS-04:** cold-chain monitoring service (8 sensors, 1 product probe, gateway, SaaS dashboard)
- **SYS-05:** food safety records app (SaaS on 2 floor tablets)
- **SYS-06:** productivity suite (email, HACCP plans, SSOPs, formulations)
- **SYS-07:** accounting, order, and invoicing service (lot numbers on invoices)
- **SYS-08:** office network and endpoints (MSP-managed firewall, one flat network, Wi-Fi)
- **SYS-09:** cloud backup (operated by the MSP)
- **SYS-13:** remote access paths (smokehouse portal, packaging vendor remote desktop, MSP agent)

**OT in plain terms.** SP 800-82 Rev. 3 describes OT in layers from field devices to the business network. In this plant the layers collapse: the smokehouse controller, the line HMIs, the labeling PC, and the office desktop sit on the same network. Separating them is the main design change in this plan (section 7).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it touches the PPCM |
|---|---|---|---|
| FSIS | Sanitation SOPs | 9 CFR 416.11-416.16 | Daily SSOP records in the records app; computer records need integrity controls (416.16(b)) |
| FSIS | HACCP systems | 9 CFR Part 417 | Cooking and chilling CCPs are monitored by SYS-01 and SYS-04 and recorded in SYS-05; computer records need integrity controls for data and signatures (417.5(d)) |
| FSIS | Recalls | 9 CFR Part 418 | 24-hour notice if adulterated or misbranded product entered commerce (418.2); lot numbers on invoices support the recall procedure (418.3) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 | Employee personal information in the suite and payroll service |
| Benchmark | NIST CSF 2.0 and SP 800-82 Rev. 3 | Voluntary | Used to tailor the baseline for IT and OT controls no rule requires |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | Apply to IT and plant equipment |

Not applicable:
- FSMA Intentional Adulteration rule (C-FOOD-AG-R01): the plant is regulated exclusively by USDA and does not register with FDA (21 CFR 1.226(g); 121.1).
- CIRCIA (C-FOOD-AG-R02): proposed only, and the company is far below the proposed size criterion. Tracked in P03.
- USCG MTS cyber rule (C-FOOD-AG-R03): the plant is not an MTSA facility.
- OSHA PSM and EPA RMP: the plant uses no anhydrous ammonia.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the owner accepted continued operation of the PPCM on three conditions:
- The POA&M items in P07 are completed by their dates.
- The High risks in P01 are treated by their due dates; none is accepted.
- **Until the remote access change is live (2026-10-31), the smokehouse portal connection and the packaging vendor's remote desktop tool stay disabled except during sessions the Production Supervisor turns on and watches.** Both were set this way on 2026-08-12.

### 4.3 System Operational Status
Operational. Planned changes: a separate plant network (2026-11-30), named logins for the records app and labeling PC (2026-10-31), a cellular backup for the cold-chain gateway (2026-10-31), and replacement of the stuffer HMI (2027 budget). Each change to a machine that affects a CCP or a label also goes through the HACCP reassessment decision in POL-02 B.10.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner and General Manager | Overall accountability; accepts Moderate risks and approves treatment plans for High risks; approves this plan, policies, and spending |
| Security and compliance lead | Office Manager | Day-to-day security; maintains this plan, the risk register, and the vendor and account lists; MSP liaison |
| Food safety owner | Production Supervisor (HACCP-trained) | CCP records, cycles, formulations, label approvals, product holds |
| Plant equipment owner | Maintenance and Sanitation Technician | Machine settings and baselines; vendor maintenance sessions |
| IT operations | MSP | Office computers and labeling PC, firewall, Wi-Fi, suite administration, backup. Plant machines excluded by contract |
| Equipment and SaaS vendors | Smokehouse manufacturer, packaging machine vendor, cold-chain vendor, records app vendor | Remote support and SaaS operation |
| Independent assessor | Independent consultant | Annual control assessment (P07) |

**Overlapping roles.** The Office Manager both runs and checks most controls, and the Production Supervisor both produces and reviews many CCP records. The compensating checks are the owner's monthly review of the POA&M, the owner as second reviewer of CCP records when the Production Supervisor made them (417.5(c)), and the independent assessor each year.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and adapted for OT. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Process settings (smokehouse cycles, formulations, label templates) | Moderate | **High** | Moderate | A changed cook cycle, cure level, or allergen statement can produce unsafe or misbranded food that reaches consumers, a severe adverse effect on individuals. Formulations are trade secrets. Controllers keep running locally if the network fails |
| CCP and SSOP records | Low | **High** | Moderate | Product cannot ship without complete, trustworthy records (9 CFR 417.5(c)); altered records could hide a deviation. Paper forms cover up to 24 hours (P05 BP-05) |
| Cold-chain monitoring data | Low | Moderate | **Moderate** | Loss of monitoring for more than 2 hours puts inventory at risk (P05 BP-02); the manual log is the workaround |
| Orders, invoices, and lot data | Low | Moderate | Moderate | Needed to trace product within hours for a recall (9 CFR 418.2-418.3) |
| Employee personal information | Moderate | Low | Low | Payroll and HR data; Florida breach notice if disclosed |
| **PPCM category (high-water mark)** | **Moderate** | **High** | **Moderate** | Overall: **High** |

**Baseline.** The integrity rating makes this a High system, as in the Small sample. The NIST SP 800-53B High baseline is used as the reference catalog, tailored for a 7-person plant. The plan documents **43 controls** that carry the FSIS record duties and the risks in P01 (see `control-implementation.csv`). Every other High-baseline control is handled one of three ways:
- **Inherited** from the SaaS vendors (platform, physical, and application controls), with the cold-chain vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** with a recorded reason, where the control assumes staff or systems far beyond this plant (for example separate development environments, configuration control boards, and most PM-series program controls). PM-2 is kept, by tailoring, because a named security lead matters at any size.
- **Compensated** on plant equipment where the IT form of a control is not possible, following SP 800-82 Rev. 3 (for example, network separation and supervised vendor sessions instead of antivirus on the stuffer HMI).

## 7. Authorization Boundary Description
- **Inside:** SYS-01 to SYS-09 and SYS-13: the smokehouse controller, line controls and label printer, labeling PC, cold-chain sensors, probe, and gateway with the company's configuration of the cold-chain service, the company's records app, suite, and accounting tenants, the firewall, network, and endpoints, the company's backup subscription, and the remote access paths.
- **Outside (external services, interconnected):** the vendors' own platforms and data centers, the smokehouse manufacturer's cloud portal, the packaging vendor's remote support service, the MSP's remote management platform, the payroll service (SYS-10), the card terminal (SYS-11, on its own cellular link), and the AI camera pilot (SYS-12), which is assessed separately in P10 and enters this boundary only when the P10 conditions are met.

**Network today and planned.** Today one flat network carries everything except guest Wi-Fi. By 2026-11-30 the MSP will create a plant network (VLAN) for SYS-01, SYS-02, SYS-03, SYS-04 gateway, and SYS-12, with firewall rules that allow only: the label data path from the labeling PC to the label printer; outbound connections to the cold-chain service and smokehouse portal; and vendor sessions when enabled. The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Smokehouse manufacturer cloud portal (SYS-13) | Bidirectional | Cycle settings, cook logs, remote service | Equipment purchase terms only; **no security terms (gap)** |
| Packaging vendor remote desktop (SYS-13) | Inbound | Remote support of the labeling PC and packager | Commissioning agreement; **no security terms (gap)** |
| Cold-chain monitoring service (SYS-04) | Outbound readings; inbound alerts | Temperatures, alerts | SaaS terms; SOC 2 Type 2 reviewed (P09) |
| Food safety records app (SYS-05) | Bidirectional | SSOP and HACCP records | SaaS terms; no SOC 2 requested yet |
| Accounting service (SYS-07) | Bidirectional | Orders, invoices, lot numbers | SaaS terms |
| Payroll service (SYS-10) | Outbound | Employee personal information | Service agreement |
| AI camera vendor cloud (SYS-12) | Outbound images; inbound model updates | Pack images, label text, lot codes | **No data-use terms (gap; P10)** |
| MSP remote management platform | Inbound administrative access | Office computers and labeling PC | MSP service contract |
| Regional grocery chain | Outbound | Security questionnaire answers (no product data) | Supplier agreement |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Smokehouse controller and remote service module (SYS-01) | Machine controller | Smokehouse | Maintenance and Sanitation Technician |
| Stuffer and linker HMI (SYS-02) | Machine controller (unsupported OS) | Raw processing room | Maintenance and Sanitation Technician |
| Packager PLC, HMI, and label printer-applicator (SYS-02) | Machine controller | Packaging room | Maintenance and Sanitation Technician |
| Labeling PC (SYS-03) | Endpoint (PC) | Production office | Production Supervisor (MSP operates) |
| Cold-chain sensors, product probe, and gateway (SYS-04) | IoT devices; SaaS | Coolers, freezer, blast chill, rooms, truck; office network | Production Supervisor |
| Floor tablets (2) and records app tenant (SYS-05) | Tablets; SaaS | Raw room and packaging room | Production Supervisor |
| Productivity suite tenant (SYS-06) | SaaS | Productivity suite vendor | Office Manager |
| Accounting tenant (SYS-07) | SaaS | Accounting service vendor | Office Manager |
| Firewall, switch, staff and guest Wi-Fi; office desktop; owner laptop; 2 company phones (SYS-08) | Network and endpoints | Office network closet; office | Office Manager (MSP operates) |
| Backup subscription (SYS-09) | SaaS | Backup vendor (MSP subcontractor) | Office Manager (MSP operates) |

The inventory above is the first one the company has had. POL-04 4.4 makes the Office Manager keep it current (CM-8).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 43 controls:
- Implemented: 6
- Partially implemented: 22
- Planned: 15
- Not applicable: 0

By responsibility: 24 system-specific (the company), 18 hybrid (the company with a vendor or the MSP), 1 common/inherited (fully provided by SaaS vendors).

### 10.2 Inherited, MSP-provided, and vendor-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Cold-chain monitoring vendor | Sensor data collection, storage, alerting platform, encryption in transit (SC-8), 2-year history (AU-11) | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Complementary user entity controls: user accounts, alert recipients and escalation, gateway network and power, reviewing offline events |
| Food safety records app vendor | Platform security, edit history, retention | Vendor documentation only | Named accounts; administrator control; records integrity procedure (AU-9) |
| Productivity suite vendor | Platform security, encryption, MFA service, audit logging | Vendor documentation | Account management, MFA settings, folder permissions, log review |
| Accounting service vendor | Platform security, MFA, encryption | Vendor documentation | Account management |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), backup operation (CP-9), screen lock (AC-11) on the office computers and labeling PC | Monthly MSP report; P07 evidence requests | Direct and check the work; approve exceptions; annual MSP review (P01 R-012). **Plant machines are not covered by the MSP** |
| Smokehouse manufacturer and packaging vendor | Remote maintenance and firmware for their machines | None | Enable sessions only on request; supervise; log (MA-4, AC-17) |

**Inherited does not mean done.** The cold-chain vendor's report assumes the customer manages alert recipients and keeps the gateway connected. Both are open gaps at the plant (P01 R-004).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Office users sign in to the productivity suite and accounting service with a password and a phone authenticator app. Floor users today share a records app login and a labeling PC login, which does not meet the attribution FSIS expects for record entries (9 CFR 417.5(b)). By 2026-10-31 each floor user will have a named records app account with a short PIN on the shared tablets, and the labeling PC will require a named login. That level is accepted for the plant floor because the tablets stay inside the plant and the records app keeps an edit history. Administrator and vendor remote access require MFA (POL-02 B.3).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and cold-chain vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **CCP:** critical control point (9 CFR 417.1)
- **FSIS:** USDA Food Safety and Inspection Service
- **HACCP:** Hazard Analysis and Critical Control Point
- **HMI:** human-machine interface (operator touchscreen)
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **OT:** operational technology
- **PLC:** programmable logic controller
- **POA&M:** plan of action and milestones
- **PPCM:** Plant Production and Cold-Chain Monitoring System
- **SSOP:** Sanitation standard operating procedure (9 CFR 416.11)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office Manager (security and compliance lead) |

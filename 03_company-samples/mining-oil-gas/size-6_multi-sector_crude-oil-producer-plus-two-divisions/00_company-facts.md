# Scenario facts: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Regulatory facts were checked against eCFR (point in time 2026-09-23), the NERC standards documents (CIP-002-5.1a, CIP-003-9, EOP-004-4), the Form DOE-417 instructions (OMB 1901-0288), TSA Security Directive Pipeline-2021-01G and 02G, and the Federal Register between 2026-09-26 and 2026-10-04.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; diversified upstream energy group) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate operating subsidiary |
| Division 1: Crude Oil Production (NAICS 211120), **focus of this scenario** | Independent crude oil producer and operator. Onshore only, in three operating areas: **Permian Basin** (West Texas and southeast New Mexico; about 74% of production), **Mid-Continent** (Oklahoma; about 22%, including fields acquired from another operator on 2025-09-30), and **Florida** (Panhandle mature waterfloods; about 4%). Field SCADA at every well pad and facility. About 26,000 employees, including its own well servicing, roustabout, and water handling crews |
| Division 2: Power Generation (NAICS 221112, sector 22 Utilities) | Owns and operates three natural gas-fired plants: **Plant P1** (combined cycle, 640 MW, West Texas), **Plant P2** (simple-cycle peaker, 300 MW, West Texas), and **Plant P3** (simple cycle, 240 MW, southeast New Mexico), 1,180 MW in total. Registered with NERC as a **Generator Owner and Generator Operator**. All output is sold in wholesale markets (organized market sales and bilateral contracts); none is dedicated to end-use customers. About 2,200 employees |
| Division 3: Crude Logistics (NAICS 486110 and 484220, sector 48-49 Transportation and Warehousing) | Crude trucking and pipeline gathering. About 2,300 miles of crude oil gathering lines in the Permian and Mid-Continent, a 140-mile, 16-inch intrastate **crude trunk line** from the Permian Central Terminal to a third-party market hub, and about 1,150 crude tank trucks. Carries the Production division's crude and that of about 85 third-party shippers and producers. About 9,800 employees |
| Corporate shared services | Identity, network, security operations, OT security engineering, cloud and data platform, ERP, HR, finance, legal, and internal audit. About 7,000 employees |
| Location | Headquartered in Florida. Operations in Texas, New Mexico, Oklahoma, and Florida. Royalty owners live in all 50 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| SBA size status | Not small. The SBA standard for NAICS 211120 is 1,250 employees (13 CFR 121.201) |
| Why these three businesses | The producer monetizes its associated gas (the Power Generation division buys residue gas made from it) and moves its own crude (the Crude Logistics division) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks; receives the High risk list quarterly |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3) |
| Group OT Security Director | Reports to the Group CISO. OT security architecture, OT DMZ standard, OT monitoring sensors, and the OT desk of the group SOC for all three divisions |
| Group Chief Risk Officer | Group risk register and enterprise risk management (ERM) roll-up; chairs the Group AI council |
| Group General Counsel | Notification matrix, intercompany agreements, regulator notices, privilege |
| Division security and compliance leads (3) | Division registers, division supplements, division-specific regulators |
| Production: Vice President of Operations Technology | Business owner of the field SCADA platform; OT technical owner for the division |
| Production: Production Accounting Vice President | System owner of hydrocarbon accounting and revenue distribution |
| Power Generation: CIP Senior Manager | The division's Vice President of Generation, named as CIP Senior Manager (CIP-003-9 R3) |
| Power Generation: NERC Compliance Manager | CIP-002, CIP-003, and EOP-004 evidence; Regional Entity liaison |
| Crude Logistics: Pipeline Control Center Manager | Control room management program (49 CFR 195.446) and the 18 pipeline controllers |
| Crude Logistics: Pipeline Compliance Manager | PHMSA program for the trunk line and gathering lines (Part 195 Subpart B reports, 195.11, 195.15) |
| Crude Logistics: Fleet Safety Director | Senior official for the hazardous materials transportation security plan (49 CFR 172.802(b)(1)) |
| Group internal audit | Reports to the board audit committee. Assesses common controls once and samples division controls |
| Disclosure committee | SEC materiality of cybersecurity incidents |
| Group AI council | Approves High-tier AI use cases |

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (SSO, MFA, PAM, identity governance) and the shared OT support jump servers | Corporate | All divisions federate to it. Five jump servers are shared by the OT support staff of all three divisions (gap 1) |
| SYS-G2 | Group SOC, SIEM, EDR (24x7), and the OT monitoring console | Corporate | EDR on all IT servers and workstations. Passive OT monitoring sensors at the Permian IOC, the Pipeline Control Center, and the Generation Control Center |
| SYS-G3 | Group cloud platform (providers A and B, vendor-agnostic), landing zones, WAN, and immutable backup vault | Corporate | Provider A primary; provider B for disaster recovery and the backup vault |
| SYS-G4 | Group ERP (finance, supply chain, maintenance work orders), HR and payroll (SaaS) | Corporate | |
| SYS-G5 | Productivity suite (email, files, chat) | Corporate | |
| SYS-G6 | Group data platform (historian replicas from all three divisions, engineering analytics, machine learning workspace) | Corporate | Pulls data from historian brokers in each division's OT DMZ (gap 1). Hosts the predictive maintenance model (P10) |
| SYS-P1 | Enterprise field SCADA platform: SCADA servers, historians, HMIs, and engineering workstations at the Permian Integrated Operations Center (IOC), the Backup Control Center (BCC) at the Mid-Continent Operations Center, and the Florida regional control room | Production | 24x7. About 140 production controllers |
| SYS-P2 | Field control devices and communications: about 38,000 RTUs, PLCs, rod pump controllers, ESP variable speed drives, and flow computers; private LTE and licensed radio networks; about 9,000 cellular modems | Production | Safety shutdowns at central facilities and compressor stations are independent of SCADA |
| SYS-P3 | Hydrocarbon accounting and revenue distribution (vendor SaaS) | Production | About 190,000 royalty owners (names, Social Security or taxpayer numbers, bank accounts) and about 2,600 non-operating working interest owners |
| SYS-P4 | Field data capture app (tablets) and the volume integration service | Production | Runs in provider A |
| SYS-P5 | Legacy SCADA at the Mid-Continent fields acquired 2025-09-30 | Production | On-premises servers at two field offices; flat network; always-on integrator remote access; not in the group SIEM (gap 2). Migration to SYS-P1 due 2027-09-30 |
| SYS-P6 | Seismic and reservoir data platform | Production | Trade secret data |
| SYS-E1 | Plant control systems at P1, P2, and P3: distributed control systems (DCS), turbine control systems, and plant historians | Power Generation | **Low impact BES Cyber Systems** (CIP-002-5.1a Attachment 1, criterion 3.3) |
| SYS-E2 | Generation Control Center (GCC): dispatch, unit commitment interface to the market operators and Balancing Authorities, and plant monitoring | Power Generation | A NERC Control Center (Generator Operator for generation at two or more locations); **low impact** (criterion 3.1). Backup GCC function in the P1 control room |
| SYS-E3 | Market bidding and settlement systems | Power Generation | SaaS plus division servers in provider A |
| SYS-M1 | Pipeline SCADA and the Pipeline Control Center (PCC), with computational leak detection | Crude Logistics | Trunk line and gathering systems. Backup PCC at the Mid-Continent Operations Center |
| SYS-M2 | Measurement: about 140 lease automatic custody transfer (LACT) units and truck unloading stations with flow computers, and the measurement data system | Crude Logistics | Custody transfer for third-party shippers |
| SYS-M3 | Shipper services platform: shipper portal (nominations, run tickets, measurement and allocation statements), truck dispatch, and the electronic run ticket app | Crude Logistics | Built by the division on provider A. In scope for SOC 2 (P09) |
| SYS-M4 | Fleet telematics, electronic logging devices (ELDs), and driver-facing cameras with AI event scoring | Crude Logistics | Vendor SaaS |

**SSP system (P02):** the *Field SCADA and Production Accounting System (FSPA)*: the enterprise field SCADA platform (SYS-P1), the field devices and communications connected to it (SYS-P2), the Production division's OT DMZs and IT/OT boundary, the FSPA cloud workloads (SYS-P4 and the historian replica feed to SYS-G6), and the company's configuration of hydrocarbon accounting (SYS-P3). It inherits common controls from SYS-G1 to SYS-G3. The Mid-Continent legacy SCADA (SYS-P5) is an interconnected system outside the boundary until migration.

**Registry defaults kept.** The primary system (field SCADA and production accounting), the P08 incident (ransomware spreading from business IT toward field SCADA), and the P10 use case (predictive maintenance model for well equipment) all fit this business. At this size the P08 incident starts in a shared service so that it reaches all three divisions' OT boundaries, and P10 covers the group AI program with the predictive maintenance model as the priority use case.

## 4. Current security posture: varies by division
**In place today:**
- Group policies aligned to CSF 2.0 and a common control catalog (2025)
- 24x7 group SOC with EDR on all IT servers and workstations; an OT desk in the SOC since 2025
- MFA for all workforce on SSO applications; phishing-resistant MFA and just-in-time PAM for IT administrators
- Immutable backups of cloud workloads in the provider B vault
- OT DMZs and passive OT monitoring at the Permian IOC, the PCC, and the GCC
- Power Generation: a NERC CIP low impact program (CIP-002-5.1a categorization, CIP-003 policy and plans) audited by its Regional Entities without findings in 2024
- Crude Logistics: written control room management procedures (195.446) and a hazardous materials transportation security plan (172.802)
- Hardwired safety shutdowns independent of SCADA at central facilities, compressor stations, pump stations, and plants
- SEC Reg S-K Item 106 disclosure in the annual report

**Gaps:**
1. **Shared services cross the IT/OT seams.** The group data platform (SYS-G6) pulls historian data from all three divisions' OT DMZs with one service account that can also write to the historian brokers. Five shared OT support jump servers (SYS-G1) can reach the OT DMZs of all three divisions and are reachable from the corporate virtual desktop pool.
2. **Mid-Continent acquired fields.** Legacy SCADA (SYS-P5) on a flat network, always-on integrator remote access with a shared account, unsupported operating systems on HMIs, and no logs in the group SIEM. Migration due 2027-09-30.
3. **Power Generation: CIP-003-9 vendor remote access.** Attachment 1 Section 6 has been in force since 2026-04-01. Plant P3's turbine vendor still has a standing remote access path with no method to detect malicious communications, and transient cyber asset reviews of OEM laptops are not recorded. Possible noncompliance (self-report decision in P03).
4. **Crude Logistics: control room management.** The backup SCADA test at the backup PCC is overdue (last 2025-04-22), point-to-point verification records are incomplete after the 2026-03 SCADA expansion, and controller training does not cover loss or manipulation of SCADA as an abnormal operating condition.
5. **Crude Logistics: hazmat security plan and fleet systems.** The security plan's risk assessment does not cover cyber threats to dispatch, run tickets, and telematics (en route security), and in-depth security training covers only physical threats. Driver-facing camera AI scores feed driver discipline without review.
6. **Common control inheritance** is documented for Production and Power Generation, not for Crude Logistics.
7. **Shared incident notification.** One incident can trigger E-ISAC and EOP-004 reports, PHMSA and EPA notices, an SEC materiality decision, state breach notices in many states, and shipper and market notices. The single notification matrix has not been exercised.
8. **AI governance.** The predictive maintenance model (P10) began automatically reducing rod pump speeds at 640 Permian wells in 2026-06 without a safety review or AI council approval (the Group AI Standard was adopted 2026-07-01, after the change).
9. **Division supplement drift.** The Crude Logistics supplement was last aligned to group policy in 2023.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Regulation (P03) | Production: **NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary benchmark)**, plus EPA oil discharge notice (40 CFR 110.6) and the SPCC high-level alarm option (40 CFR 112.9(c)(4)(iv)). Power Generation: **NERC CIP-002-5.1a and CIP-003-9** (low impact), with EOP-004-4. Crude Logistics: **PHMSA 49 CFR Part 195** (control room management, 195.446; Subpart B reporting; 195.11 and 195.15 for gathering lines) and **hazmat transportation security plans** (49 CFR 172.800 to 172.804, 172.704). Group: SEC Reg S-K Item 106 and Form 8-K Item 1.05, state breach laws. Applicability screens: USCG Subpart F (N21-R01), TSA pipeline Security Directives (N21-R02), CIRCIA (N21-R03, proposed) |
| Regulatory driver labels | `N21-BM (...)` is the P03 voluntary benchmark, with the SP 800-82 Rev. 3 section or CSF 2.0 subcategory in parentheses (a scenario label, not a row in `requirements.csv`). `N22-R01 (CIP-003-9 ...)` marks NERC CIP. `PHMSA 195.xx` and `HMR 172.xxx` mark the Crude Logistics rules. `N48-49-R08` marks SEC disclosure. `N21-R03 (proposed)` marks CIRCIA items tracked but not required |
| P08 | Ransomware that starts with a phished corporate user, spreads through the group data platform connector and the shared OT jump servers toward field SCADA, encrypts the Mid-Continent legacy SCADA HMIs, forces precautionary isolation of the PCC and GCC, and steals royalty owner data: a multi-regulator notification matrix with NERC, PHMSA, EPA, SEC, and state duties |
| P09 | SOC 2 scoped per division: the Crude Logistics shipper services platform is in scope for a first report; Production and Power Generation are out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the rules that bear on them, with the predictive maintenance model as the priority use case |
| Cloud | Shared corporate platform (providers A and B) plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-04-01 | CIP-003-9 effective (vendor electronic remote access for low impact assets) |
| 2026-05-04 to 2026-07-31 | Group and division BIAs, risk analyses, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples. OT tests at Plant P2 during a planned outage on 2026-08-11 and at Permian field sites on 2026-08-13 |
| 2026-08-31 to 2026-09-04 | SOC 2 readiness self-assessment (P09) and Group AI council review (P10, 2026-09-02) |
| 2026-09-17 | Results to the board risk committee; deliverables approved |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Safety and environmental risks rated High must be treated, not accepted |
| Revenue split (fictional) | Crude Oil Production about $14.2 billion (about $38.9 million per day); Power Generation about $2.1 billion (about $5.8 million per day); Crude Logistics about $1.7 billion from third parties (about $4.7 million per day), plus about $0.9 billion of intercompany revenue eliminated in consolidation |
| Production scale | About 16,800 operated wells (11,200 producing, 4,300 water injection, 600 saltwater disposal, 700 shut-in), 410 central tank batteries, 95 associated gas compression stations, and 38 water injection plants. About 520,000 barrels of oil per day gross operated plus associated gas. Associated gas is sold at central facility outlets to a third-party gas processor; the Power Generation division buys residue gas from that processor under a netback contract |
| Tank batteries and SPCC | About 250 of the 410 central tank batteries use the high-level sensor option of 40 CFR 112.9(c)(4)(iv): high-level alarms are transmitted to the field SCADA |
| Power Generation details | Largest single plant 640 MW; the GCC dispatches 1,180 MW in total. Both are below the 1,500 MW bright lines of CIP-002-5.1a criteria 2.1 and 2.11, and no planner has designated a plant under criterion 2.3, so all four assets (P1, P2, P3, and the GCC) contain low impact BES Cyber Systems only. Turbine OEM remote monitoring and tuning service at all three plants |
| Crude Logistics details | Gathering lines are all 8 5/8 inch nominal outside diameter or smaller, in rural areas. 120 miles are regulated rural gathering lines (195.11(a)); about 2,180 miles are reporting-regulated-only (195.15). The trunk line is regulated under Part 195 as an intrastate pipeline (not a gathering line, because it is larger than 8 5/8 inch). 4 pump stations; breakout tanks at the Central Terminal. 18 pipeline controllers. TSA has not notified the division that any of its pipelines is critical |
| Trucking | About 1,150 cargo tank motor vehicles (about 8,400 gallons each) and about 3,900 drivers. Most crude hauled is classed UN1267 Packing Group I or II, so a security plan is required (172.800(b)(6), large bulk quantity of Class 3) |
| Shippers | About 85 third-party shippers and producers. About 120 shipper and customer security questionnaires were answered in 2025; the three largest shippers asked for a SOC 2 Type 2 report by the end of 2027 |
| Royalty owners | About 190,000 royalty owners in all 50 states (about 21,000 in Florida). Owner decks and payment files are exported from SYS-P3 to a finance file share each month |
| Cloud | Provider A hosts the corporate landing zone, SYS-G6, SYS-P4, SYS-M3, and the SYS-E3 servers. Provider B hosts disaster recovery replicas and the immutable backup vault. SYS-P1, SYS-E1, SYS-E2, and SYS-M1 are on premises at their control centers and plants |
| Cyber insurance | Group cyber insurance tower with a breach hotline and a panel of forensic firms and breach counsel |
| Out of scope by fact | No offshore, Outer Continental Shelf, or MTSA-regulated facilities. No federal contracts. No payment card acceptance. No operations, employees, or consumers in California or Colorado. No EAR-controlled technology identified. No Sensitive Security Information held |
| P07 new finding | Default vendor passwords on 2 cellular modem web interfaces and 1 rod pump controller at Permian well pads, reachable from the field LTE management network (found 2026-08-13; changed 2026-09-15) |
| AI (P10) | The predictive maintenance model's automatic speed reduction was switched back to advisory mode on 2026-09-03. Inventory also lists production optimization recommendations, seismic interpretation assistance, turbine anomaly detection (OEM), computational leak detection with machine learning, driver-facing camera AI, route and load optimization, an enterprise generative AI assistant piloted with 3,000 users, and a SOC triage assistant |
| CIP-012-2 | The GCC is a Generator Operator Control Center that sends real-time data to Balancing Authority and market operator Control Centers, so CIP-012-2 (enforceable 2026-07-01) applies. The plan covers Parts 1.1 to 1.4; responsibilities with the other entities (Part 1.5) are agreed only by email |
| Self-report decision (P03) | On 2026-09-17 the CIP Senior Manager, with the Group General Counsel, decided to self-report the Plant P3 vendor access gap (CIP-003-9 Attachment 1 Section 6.3) and the unrecorded transient cyber asset reviews (Section 5.2) to the Regional Entity with a mitigation plan |
| Additional roles | Production HSE director (process safety and EPA notices); Production field services director; Mid-Continent operations manager; Crude Logistics measurement manager, commercial director, and trucking operations director; group identity, SOC, cloud platform, and data platform directors |
| Field scale (P02) | About 1,800 field tablets; about 2,900 wells in the Mid-Continent fields on SYS-P5 |
| Shipper services (P09) | About 300 Crude Logistics staff work in commercial, dispatch, and measurement roles on SYS-M3 |
| P08 exercise scenario | The stolen exports cover about 168,000 royalty owners in all 50 states (about 19,000 in Florida). Counts are illustrative |
| Other P07 findings | 12 of 40 sampled field logic changes recorded after the fact; 41 field devices missing from the inventory in 3 Permian areas; a SYS-P5 HMI test restore failed; the jump servers were reachable from a corporate virtual desktop |

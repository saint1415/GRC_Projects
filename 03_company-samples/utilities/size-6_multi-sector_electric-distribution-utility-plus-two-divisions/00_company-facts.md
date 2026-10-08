# Scenario facts: Cris Santos Company | Utilities | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; utility holding company) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary |
| Division 1: Electric Utility (NAICS 221122), **focus of this scenario** | Cris Santos Electric Company, a regulated electric distribution utility in Florida. About 2.4 million customer meters (2.1 million residential, 300,000 commercial and industrial). Owns no generation and buys its energy under wholesale purchase agreements. Owns 115 kV and 230 kV transmission (about 2,600 circuit miles) and 12 kV to 34.5 kV distribution (about 41,000 circuit miles). 2025 summer peak load 10,400 MW. About 11,500 employees |
| Division 2: Gas Production (NAICS 211130, sector 21 Mining, Quarrying, and Oil and Gas Extraction) | Cris Santos Energy Resources, LLC. Onshore natural gas production in two basins in two other Gulf Coast states: about 2,100 operated wells and 38 field compressor stations, about 1.2 billion cubic feet per day of gross operated production. Sells gas under firm contracts to 14 gas-fired generating plants owned by third parties. About 3,900 employees |
| Division 3: Engineering Services (NAICS 541330, sector 54 Professional, Scientific, and Technical Services) | Cris Santos Engineering, Inc. Transmission, distribution, substation, protection and control, and SCADA/EMS engineering, plus NERC CIP consulting, for about 300 unaffiliated utilities nationwide and for the Electric Utility. About 24,600 employees in 60 offices in 22 states |
| Corporate shared services | Identity, network, security operations, OT security services, cloud and data platform, HR, finance, legal, procurement, internal audit. About 5,000 employees |
| Location | Headquartered in Florida. The Electric Utility serves Florida only; Gas Production operates in two other states; Engineering Services works nationwide. **State law is handled generically**, with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional): Electric Utility about $8.4 billion, Gas Production about $3.8 billion, Engineering Services about $5.8 billion (external revenue only) |
| SEC status | Common stock listed on a U.S. exchange. Form 8-K Item 1.05 and Regulation S-K Item 106 apply to the holding company |

### 1.1 Electric Utility grid and NERC facts
| Item | Fact |
|---|---|
| NERC registration | Registered on the NERC Compliance Registry as **Distribution Provider (DP), Transmission Owner (TO), and Transmission Operator (TOP)**. Not a Balancing Authority, Reliability Coordinator, Generator Owner, or Generator Operator. An unaffiliated Balancing Authority and the area Reliability Coordinator operate around it |
| Regional Entity | SERC Reliability Corporation (the former FRCC Regional Entity was dissolved in 2019 and its Florida registered entities were transferred to SERC; FERC Docket RR19-4) |
| Control centers | **Transmission Control Center (TCC)** and **backup TCC**, from which TOP functions are performed. **Distribution Control Center (DCC)** and **backup DCC** in separate buildings, from which distribution operators run the distribution system. The DCCs perform no TOP function |
| Transmission substations | 74 substations at 115 kV and 230 kV. Highest voltage 230 kV. No 230 kV station connects to more than four other 230 kV stations (highest aggregate weighted value 2,800 under CIP-002-5.1a criterion 2.5). No Facility is identified by the RC, PC, or TP as critical to an IROL, and none serves Nuclear Plant Interface Requirements |
| Load shedding | Feeder underfrequency load shedding relays act independently at each substation (no common control system), under the regional UFLS program |
| Generation interconnections | Third-party plants connect to the TO's system. The largest is 1,240 MW. No Generator Owner has notified the company of a plant meeting CIP-002-5.1a criterion 2.1 or 2.3 |
| CIP-002 result (approved 2025-12-02) | **Medium impact:** BES Cyber Systems at the TCC and backup TCC (Attachment 1 criterion 2.12; TOP Control Center not rated high because no asset meets criteria 2.2, 2.4, 2.5, 2.7, 2.8, 2.9, or 2.10). **Low impact:** the 74 transmission substations (criterion 3.2). No high impact BES Cyber Systems |
| Not in CIP scope | The DCCs and the distribution SCADA, DMS, and OMS (a DP function; the NERC Glossary "Control Center" lists only RC, BA, TOP, and GOP functions), the AMI, and the 446 distribution substations. These are held to the group's voluntary benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) |
| CIP-014 | Not applicable: no Transmission station or substation meets CIP-014-3 Applicability 4.1.1 (no 500 kV; no 200 kV to 499 kV station above the 3000 aggregate weighted value; none identified for IROLs or Nuclear Plant Interface Requirements) |
| Last SERC compliance audit | 2024-05 (CIP and O&P). Three potential noncompliances (CIP-007-6 R2 patch evaluations late, CIP-004-7 R4 Part 4.2 quarterly verification missed once, CIP-010-4 R1 Part 1.3 baseline update late) were mitigated and closed in 2025 |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and operational risk oversight; accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC disclosure controls |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G4) |
| Group Chief Risk Officer | Group risk register and ERM roll-up; co-accepts High risks |
| Group General Counsel | Contracts, notification matrix, regulatory filings coordination |
| Group Chief Privacy Officer | Personal information of customers, royalty owners, and workforce; breach determinations under state law |
| Group OT security director | Runs SYS-G4 (OT secure remote access) and the group OT security standard; reports to the Group CISO |
| Group identity director, Group SOC director, Group cloud platform director | Common control providers for SYS-G1, SYS-G2, SYS-G3 |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators |
| Electric Utility senior vice president of transmission and distribution operations | **CIP Senior Manager** (identified by name in the CIP-003-9 R3 record; this sample uses the title only) |
| Electric Utility NERC compliance director | CIP and O&P compliance program, SERC submissions, self-reports |
| Electric Utility system operations director | Runs the TCC and backup TCC (TOP); owns SYS-E2 |
| Electric Utility distribution operations director | Runs the DCC and backup DCC; **system owner of the Distribution Operations Platform** (P02) |
| Electric Utility manager of power supply and load forecasting | Business owner of the load-forecasting model (P10) |
| Gas Production vice president of operations; SCADA and automation manager | Field operations and field SCADA (SYS-N1) |
| Engineering Services contracts director; federal programs manager | Client contracts and flow-down terms; federal contracts (FAR) |
| Group internal audit | Independent assessor; assesses common controls once and samples division controls (P07). Reports to the board audit committee |
| Disclosure committee | SEC materiality decisions for cybersecurity incidents |

**Where roles overlap and how it is compensated.** Engineering Services is both a division of the group and a vendor to the Electric Utility. Its engineers who support Electric Utility projects are treated as vendor personnel under the Electric Utility's CIP-013-2 plan and CIP-004-7 access program, not as Electric Utility staff. Group internal audit does not assess controls it helped design; the 2026 OT remote access design review was done by an outside firm for that reason.

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (SSO, MFA, PAM, identity governance) | Corporate | IT identities for all divisions. Not used inside the CIP Electronic Security Perimeters |
| SYS-G2 | Group SOC, SIEM, and EDR, with an OT monitoring console | Corporate | 24x7. OT network sensors at the TCC and backup TCC since 2024 |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic) and data platform | Corporate | Provider A: corporate landing zone, data platform, load-forecasting workload, outage map. Provider B: Engineering Services client project platform, backup vault |
| SYS-G4 | Group OT secure remote access platform | Corporate (Group OT security director) | Central access gateway and policy engine (hosted in provider A) with MFA and session recording, plus one jump host cluster per OT environment: the DOP OT DMZ, the 74 transmission substations (vendor access for CIP-003-9 Attachment 1 Section 6), and the Gas Production POC. The TCC uses its own CIP-005 Intermediate System, not SYS-G4 |
| SYS-G5 | Group ERP, HR, and financial reporting | Corporate | SEC reporting and payroll |
| SYS-E1 | Distribution Operations Platform (ADMS: distribution SCADA, distribution management applications, and OMS) | Electric Utility | DCC and backup DCC. See section 3.1 |
| SYS-E2 | Transmission EMS/SCADA at the TCC and backup TCC | Electric Utility | Medium impact BES Cyber Systems with their EACMS (firewalls, Intermediate System, log collectors) and PACS |
| SYS-E3 | Substation automation, protection, and field area network | Electric Utility | 74 transmission substations (low impact BES Cyber Systems, with gateways enforcing CIP-003-9 Section 3.1 access controls) and 446 distribution substations. Private LTE and fiber |
| SYS-E4 | Advanced metering infrastructure (AMI) head-end, 2.4 million meters | Electric Utility (vendor SaaS) | Remote connect and disconnect; outage events to the OMS. The AMI vendor provides a SOC 2 Type 2 report (P09) |
| SYS-E5 | Customer information system (CIS), billing, portal, IVR | Electric Utility (vendor SaaS) | Customer names, addresses, Social Security numbers for credit and deposit decisions, and bank account numbers for automatic payment. Card payments go through the processor's hosted page |
| SYS-E6 | Electric load-forecasting model | Electric Utility (built in-house on SYS-G3) | Day-ahead and 7-day hourly forecasts (P10) |
| SYS-N1 | Gas field SCADA and the Production Operations Center (POC) | Gas Production | RTUs and flow computers at well pads and compressor stations; licensed radio and cellular. Separate OT domain |
| SYS-N2 | Production accounting, royalty, and land systems | Gas Production (vendor SaaS) | About 48,000 royalty owners with names, Social Security or taxpayer numbers, and bank account numbers |
| SYS-S1 | Engineering client project platform | Engineering Services (on SYS-G3 provider B) | Document management and collaboration for about 4,800 active projects. Holds client CEII and BES Cyber System Information (BCSI) |
| SYS-S2 | Engineering design environment and field commissioning laptops | Engineering Services | CAD/CAE workstations, protection settings tools, about 900 commissioning laptops that connect to client substations, and a generative AI design assistant pilot |

**SSP system (P02):** the *Distribution Operations Platform (DOP)*: SYS-E1 (ADMS servers, operator consoles, front-end processors, historian, and OMS at the DCC and backup DCC), its OT DMZ, the distribution substation gateways and field area network segments that carry distribution SCADA traffic, the OMS mobile clients, and its interfaces to SYS-E2, SYS-E3, SYS-E4, SYS-E5, and SYS-G4. It inherits common controls from SYS-G1 to SYS-G4 and group functions.

### 3.1 Distribution Operations Platform detail
| Item | Fact |
|---|---|
| Scale | 1,700 feeders; about 9,000 automated field devices (reclosers, switches, capacitor and regulator controls) through 446 distribution substations and the distribution side of the 74 transmission substations |
| Components | Primary and standby ADMS server clusters at the DCC; a warm standby cluster at the backup DCC; 64 operator consoles; 8 front-end processors; historian; OMS servers; OT DMZ (historian replica, integration servers, SYS-G4 jump hosts, file transfer); OT Windows domain separate from SYS-G1 |
| Shared field devices | At the 74 transmission substations, the distribution SCADA polls the same substation gateways that serve the EMS. Those gateways are part of the low impact BES Cyber Systems |
| Users | About 210 distribution operators and supervisors, 60 OT engineers and administrators, 1,400 OMS mobile users (crews and troubleshooters) |
| Why it matters | It switches load for 2.4 million meters, restores outages, and runs storm restoration. A wrong or malicious command can de-energize feeders or endanger crews |

## 4. Current security posture: mixed by division
**In place today:**
- Group policies aligned to NIST CSF 2.0 (v2026, approved 2026-03-18) and a common control catalog (2025)
- A 24x7 group SOC; EDR on IT endpoints and servers; OT network sensors at the TCC and backup TCC (CIP-005-7 Part 1.5)
- PAM and quarterly access certification for IT systems (SYS-G1)
- Immutable cloud backups in provider B
- A NERC CIP compliance program for the Electric Utility: CIP Senior Manager designated (CIP-003-9 R3), medium impact program for the TCC, low impact plan for the 74 transmission substations, CIP-013-2 supply chain plan (last approved 2025-11-20)
- An EOP-004-4 event reporting Operating Plan (reviewed 2026-03) and Form DOE-417 procedures at the TCC
- SEC Item 106 disclosure in the 2025 annual report; a disclosure committee with a cybersecurity charter
- Engineering Services SOC 2 Type 1 report for the client project platform as of 2026-03-31
- A Group AI Standard and Group AI council (2026-03)
- Storm restoration plans exercised every May; manual switching procedures for every feeder

**Gaps found in the 2026 assessments:**
1. **Shared OT remote access.** SYS-G4 serves the DOP, the 74 transmission substations, and the Gas Production POC. It holds 1,140 accounts, including 610 Engineering Services staff and 19 vendors; 230 Engineering Services accounts have standing access to all three environments. CIP-003-9 Attachment 1 Section 6 (effective 2026-04-01) is only partly implemented: the method to detect known or suspected malicious communications for vendor remote access (6.3) is in place at 31 of 74 substations.
2. **DOP segmentation and monitoring.** The DOP sits outside CIP scope but polls the shared gateways at the 74 transmission substations. The IT/OT firewall at the DCC holds 37 broad rules; the DCC networks have no OT monitoring sensors; 22 operator consoles run an operating system past vendor support.
3. **CIP-012-2 (effective 2026-07-01).** The plan for data between the TCC, the backup TCC, the RC, and neighboring TOPs covers confidentiality and integrity (Part 1.1) but not loss of availability or link recovery (Parts 1.2 and 1.3).
4. **Contract flow-down at Engineering Services.** 37 client contracts require notice of vendor-identified incidents within 24 to 72 hours, notice when access should be revoked, and disclosure of vulnerabilities (clients' CIP-013-2 Part 1.2 terms). There is no register of these terms and no process that routes group SOC findings to client notices.
5. **Client CEII and BCSI at Engineering Services.** Project platform permissions are inherited by project-wide groups. 2 of 25 sampled projects had client BCSI in personal cloud storage. The generative AI design assistant pilot was used with client documents before approval.
6. **Gas Production drift.** The division's 2023 security standards conflict with 2026 group policy. Field SCADA uses shared accounts; 120 well pad cellular modems have public IP addresses; there is no OT monitoring.
7. **Common control inheritance** is documented for the Electric Utility (2025 matrix, used as CIP evidence) but not for Gas Production or Engineering Services.
8. **Load-forecasting model.** The model replaced in 2025 was not independently validated and has no drift monitoring, although it drives day-ahead purchases, peak-day operating plans, and storm staffing.
9. **Cross-division incident notification.** An OT incident could trigger CIP-008-6 and DOE-417 reports, EOP-004 reports, client contract notices from Engineering Services, state breach notices, and an SEC materiality decision at once. The single notification matrix has not been exercised.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P01 | Group register plus three division registers (Electric Utility, Gas Production, Engineering Services), rolled up to group ERM |
| P02 | SSP for the DOP (the registry's primary system, "Distribution SCADA and outage management system", at this size an ADMS). A division system that inherits group common controls; common control catalog for all divisions |
| P03 | Electric Utility: NERC CIP (CIP-002 to CIP-014 at medium and low impact), with NERC EOP-004-4 and Form DOE-417 as secondary. Gas Production: NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary benchmark) plus applicability screens. Engineering Services: client contract flow-down of NERC CIP terms, FAR 52.204-21, and CEII handling. Group-wide: SEC, state breach laws, OFAC. Regulation-by-division matrix |
| P08 | Intrusion into distribution control systems (OT) that spans divisions: a phished Engineering Services account on SYS-G4 reaches the DOP, issues feeder commands, probes a transmission substation gateway and the TCC EACMS, and attempts to reach the Gas Production POC |
| P09 | Scoping per division: Engineering Services client project platform in scope (SOC 2 Type 2 readiness); Electric Utility and Gas Production out of scope with reasons, plus a review of the AMI vendor's SOC 2 Type 2 report |
| P10 | Group AI program with division use cases; focus use case: the electric load-forecasting model (registry default) |
| Cloud | Shared corporate platform with two providers plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses and gap analyses (TCC and substation walkthroughs 2026-06-16 to 2026-06-18; Gas field visits 2026-06-23 to 2026-06-25) |
| 2026-07-06 to 2026-08-28 | Common control assessment by group internal audit, plus division samples |
| 2026-09-15 | Results to the board risk committee; deliverables approved |
| 2026-09-30 | Planned self-reports to SERC of potential CIP noncompliances (P03) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. High risks to public or crew safety may not be accepted; they must be treated |
| Intercompany services | Engineering Services performs about $400 million a year of design, protection settings, and commissioning work for the Electric Utility under an intercompany services agreement (2021) that has no security schedule. About 180 of its engineers hold CIP-004-7 authorized electronic or unescorted physical access to the TCC |
| Holding company and affiliate rules | Background fact, not scored in P03. The group is a holding company of a public utility. It notified FERC of that status (FERC-65, 18 CFR 366.4(a)), and FERC may access the books and records of the holding company and its affiliates that bear on the utility's jurisdictional rates (18 CFR 366.2). The utility serves Florida only, so the group filed for the single-state waiver of the accounting and reporting rules (18 CFR 366.3(c)(1); FERC-65B under 366.4(c)); FERC's access to the books and records still applies. Because the utility owns jurisdictional transmission, it may not buy non-power goods or services from a non-utility affiliate at a price above market (18 CFR 35.44(b)(2)). Under the Florida PSC rule, the utility charges its regulated operations the lesser of fully allocated cost or market price for what it buys from an affiliate, keeps a cost allocation manual, and reports affiliate transactions each year (Fla. Admin. Code R. 25-6.1351(3)(c), (5), (6)). Engineering Services' work for the Electric Utility (row above) is the main affiliate transaction, so its pricing and records follow these rules |
| Fuel and power dependency | Two of the 14 plants that buy gas from Gas Production supply about 30% of the Electric Utility's purchased power under contracts with their third-party owner |
| Federal contracts | Engineering Services holds federal civilian agency contracts (about $160 million a year) that include FAR 52.204-21, 52.204-25, and 52.204-23. No DoD contracts and no contract that designates CUI |
| Workforce data | HR data for 45,000 employees in 23 states (SYS-G5) |
| Cyber insurance | Group cyber insurance tower with an incident response panel that includes an OT-capable firm |

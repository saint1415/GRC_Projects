# Scenario facts: Cris Santos Company | Critical Manufacturing | Multi-Sector

All 10 deliverables in this folder use the facts below. The company, its plants, its utility, its clients, and its suppliers are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Regulatory text was checked on 2026-10-05 against eCFR (version date 2026-09-23), the Federal Register API, the NERC standard PDFs and standards pages, the OMB-approved Form DOE-417, and the NIST CSRC publication pages.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; holding company for three operating divisions) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary |
| Division 1: Transformer Manufacturing (NAICS 335311), **focus of this scenario** | Cris Santos Transformer Company, LLC. Designs, builds, tests, and services liquid-filled and dry-type transformers for the electric grid: distribution transformers (about 290,000 units a year), power transformers from 10 MVA to 500 MVA and up to 500 kV class (about 1,200 units a year), and voltage regulators. Ships its own transformer monitoring unit (TMU) with every power transformer and sells a Fleet Monitoring Service (FMS) to utilities. About 24,000 employees |
| Division 2: Electric Utility (NAICS 221122, sector 22 Utilities) | Cris Santos Electric, LLC. A regulated electric transmission and distribution utility in Florida with about 1.4 million customer meters. Owns no generation and buys energy under wholesale contracts. Owns 115 kV and 230 kV transmission (about 1,900 circuit miles) and 12 kV to 34.5 kV distribution. 2025 summer peak load 6,300 MW. About 9,000 employees |
| Division 3: Grid Engineering Services (NAICS 541330, sector 54 Professional, Scientific, and Technical Services) | Cris Santos Grid Engineering, Inc. Transmission, distribution, substation, and protection and control design; SCADA integration; field commissioning; and NERC CIP consulting for about 260 unaffiliated utilities and for the Electric Utility. About 7,000 employees in 40 offices in 18 states |
| Corporate shared services | Identity, network, security operations, OT security standards, cloud and data platform, the group ERP, HR, finance, legal, procurement, and internal audit. About 5,000 employees |
| Location | Headquartered in Florida. Manufacturing has 8 plants in 6 states; the Electric Utility serves Florida only; Grid Engineering works nationwide. **State law is handled generically** ("the law of each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional): Transformer Manufacturing about $9.6 billion (about $26.3 million per calendar day), Electric Utility about $6.0 billion, Grid Engineering about $2.4 billion (external revenue only) |
| SBA size status | Not small. The SBA size standard for NAICS 335311 is 800 employees (13 CFR 121.201) |
| SEC status | Common stock listed on a U.S. exchange; not a smaller reporting company. Form 8-K Item 1.05 and Regulation S-K Item 106 (17 CFR 229.106) apply to the holding company |

### 1.1 Transformer Manufacturing detail (focus division)
| Item | Fact |
|---|---|
| Plants | **P1** Florida (HQ campus; three-phase pad-mounted distribution), **P2** Florida (large power transformers and the extra-high-voltage test laboratory), **P3** Georgia (single-phase distribution), **P4** Tennessee (medium power transformers), **P5** Texas (substation and generator step-up units), **P6** North Carolina (core steel slitting, windings, and tanks for the other plants), **P7** Ohio (dry-type and specialty transformers), **P8** South Carolina (distribution transformers and voltage regulators; **acquired 2025-09 as AQ-25**). Also 12 service and repair centers and 3 spare transformer yards |
| Customers | About 700 electric utilities (investor-owned, municipal, cooperative, and federal power customers), renewable and storage developers, data centers, and industry. Large power transformer backlog about 30 months; distribution backlog about 24 weeks. Utilities place storm-restoration orders each hurricane season, and the division reserves production slots and spare units for them |
| Utility contract security terms | **140 utilities** that operate medium or high impact BES Cyber Systems have added a **Supplier Cyber Security Addendum** to their purchase agreements. The addenda cover TMUs and their firmware, the TMU configuration software, field service access to utility sites and systems, and FMS subscriptions. Their terms follow the six topics in NERC CIP-013-2 Requirement R1 Part 1.2. **95 addenda require incident notice within 48 hours and 45 within 24 hours** of confirming a cyber incident related to the products or services supplied; all require notice within 1 business day when a company representative's access should no longer be granted, disclosure of known vulnerabilities in supplied firmware and software within 30 days, hashes or signatures for firmware, software, and patches, and only utility-controlled, MFA-protected, per-session remote access. **These deadlines are contract terms, not NERC requirements** |
| NERC status of the division | **Not a NERC-registered entity.** CIP-013-2 applies to the Responsible Entities in its section 4.1, not to their suppliers. It reaches the division through customer contracts, including the affiliated Electric Utility's procurement |
| Transformer monitoring unit (TMU) | The division's own product (dissolved gas, temperature, bushing, and load monitoring). Electronics are built by a contract manufacturer; the division's Grid Products group (about 110 engineers) writes 7 firmware lines and the configuration software. At customer sites the TMU is under utility control |
| Fleet Monitoring Service (FMS) | A SaaS service line on Cloud provider B, run by about 60 engineers and data scientists: about 70 utility subscribers and 18,000 monitored transformers. Utilities push TMU data from their own data platforms (utility-initiated, one-way, mutually authenticated TLS). The FMS has no connection into utility networks or to TMUs. It includes the transformer asset-health analytics (AI-003). Subscribers began asking for a SOC 2 Type 2 report in 2026 |
| Federal contracts | **14 civilian federal contracts** (no DoD), about $210 million of backlog: transformers for federal power marketing and water agencies and federal facilities, built to agency specifications (not COTS). All 14 include FAR 52.204-21, 52.204-23, and 52.204-25; the 9 awarded since 2024 also include 52.204-30. Federal contract information (FCI): agency specifications and drawings, delivery schedules, test reports, and correspondence. No DFARS clauses and no CUI |
| DoD work | None. A **bid review gate** stops any bid whose terms would flow down DFARS 252.204-7012 or a CMMC level until the group executive risk committee approves a compliance plan |
| Exports | About 8% of revenue: transformers to utilities in Canada, Mexico, and the Caribbean. Products and technology classified **EAR99** (2025 review by the Director of Trade Compliance). Export orders are screened against U.S. government restricted-party lists in the ERP before release. Export records must be kept 5 years (15 CFR 762.6(a)) |

### 1.2 Electric Utility detail
| Item | Fact |
|---|---|
| Federal contracts | None (no FAR clauses apply to the Electric Utility) |
| NERC registration | Registered as **Distribution Provider (DP), Transmission Owner (TO), and Transmission Operator (TOP)**. Not a Balancing Authority, Reliability Coordinator, Generator Owner, or Generator Operator. Regional Entity: SERC Reliability Corporation |
| Control centers | Transmission Control Center (**TCC**) and **backup TCC** (TOP functions). Distribution Control Center (**DCC**) and backup DCC (distribution operations only; no TOP function) |
| Substations | 58 transmission substations at 115 kV and 230 kV (no 500 kV; no station above the CIP-002-5.1a criterion 2.5 weighted-value threshold; none identified for IROLs) and 310 distribution substations. Feeder underfrequency load shedding relays act independently at each substation |
| CIP-002 result (approved 2025-11-18) | **Medium impact:** BES Cyber Systems at the TCC and backup TCC (Attachment 1 criterion 2.12). **Low impact:** the 58 transmission substations (criterion 3.2). No high impact BES Cyber Systems |
| Not in CIP scope | The DCCs, distribution SCADA and outage management, AMI, the customer information system, and the 310 distribution substations. These are held to the group's voluntary benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) |
| Last SERC compliance audit | 2024-10. Two potential noncompliances (CIP-007-6 R2 patch evaluation late; CIP-010-4 R1 Part 1.3 baseline update late) were mitigated and closed in 2025 |
| Transformer supply from the affiliate | Buys about 35% of its distribution transformers and all of its large power transformer spares from Transformer Manufacturing under a 2019 intercompany supply agreement. TMUs report from 41 of its 58 transmission substations |

### 1.3 Grid Engineering detail
| Item | Fact |
|---|---|
| Clients | About 260 unaffiliated utilities nationwide plus the Electric Utility (about $310 million a year of intercompany design, protection settings, and commissioning work under a 2020 intercompany services agreement) |
| Client contract security terms | **41 client contracts** flow down NERC CIP terms: CIP-004-7 (training and personnel risk assessments), CIP-011-3 (BES Cyber System Information handling), CIP-013-2 Part 1.2 (vendor incident notice in 24 to 72 hours, access revocation, vulnerability disclosure, remote access coordination), and Transient Cyber Asset rules for commissioning laptops |
| Federal contracts | Federal civilian agency contracts (about $95 million a year) that include FAR 52.204-21, 52.204-23, and 52.204-25. No DoD contracts and no contract that designates CUI |
| Delivery detail | About 1,100 engineers work on CIP-related client projects; about 700 commissioning laptops across 40 offices; 12 software tools delivered to clients in 2026; 23 subcontractors on federal projects; 14 CEII requests to FERC in 2026, each with the client's written authorization; 31 client contracts commit to 12-month log retention. About 1,400 closed project folders (2016 to 2023) remain on legacy group file servers |
| Assurance | SOC 2 Type 2 report (Security and Confidentiality) for the client project platform, 12 months ending 2026-06-30 |
| Access to the affiliate utility | About 140 Grid Engineering engineers hold CIP-004-7 authorized electronic or unescorted physical access to the TCC |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and operational risk oversight (Reg S-K Item 106(c)(1)); accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC disclosure controls |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3); co-accepts High risks |
| Group Chief Risk Officer | Group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group General Counsel | Contracts, intercompany agreements, notification matrix, regulatory filings coordination; chairs the disclosure committee |
| Group Chief Privacy Officer | Employee, customer, and other personal information; breach determinations under state law |
| Group OT security director | Group OT security standard, OT monitoring service, and OT incident support for plants and the utility; reports to the Group CISO |
| Group identity director; Group SOC director; Group cloud platform director | Common control providers for SYS-G1, SYS-G2, SYS-G3 |
| Group ERP platform director | **System owner of the GEPS** (P02); reports to the Group CIO |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators; accept Low risks |
| Division presidents (3) | Accept Moderate risks for their divisions |
| Manufacturing: VP manufacturing operations | Business owner of the GEPS production scheduling module; owns the 8 plants and the plant managers |
| Manufacturing: Director of OT engineering | Division OT lead: plant OT standards, OEM remote access, controller backups |
| Manufacturing: Chief product security officer | Leads the TMU product security incident response team (PSIRT); firmware signing; vulnerability disclosure to utilities |
| Manufacturing: VP supply chain and demand planning; Director of reliability engineering | Business owners of AI-001 (demand forecasting) and AI-002 (predictive maintenance) |
| Manufacturing: Director of trade compliance; Director of federal contracts; FMS general manager | EAR; FAR clauses; the FMS service line |
| Electric Utility: senior vice president of transmission and distribution operations | **CIP Senior Manager** (CIP-003-9 R3) |
| Electric Utility: NERC compliance director; system operations director; distribution operations director; manager of load forecasting | CIP and O&P compliance and SERC submissions; the TCC; the DCC; business owner of AI-004 |
| Grid Engineering: chief operating officer; contracts director; federal programs manager; project platform director | Delivery; client contract terms; FAR clauses; SYS-S1 |
| Group internal audit | Independent assessor; assesses common controls once and samples division controls (P07). Reports to the board audit committee |
| Disclosure committee | SEC materiality decisions for cybersecurity incidents |
| Group AI council | Approves High-tier AI use cases and the approved-tools list (P10) |

**Where roles overlap and how it is compensated.** Transformer Manufacturing and Grid Engineering are both divisions of the group and vendors to the Electric Utility. The Electric Utility treats them as vendors under its CIP-013-2 supply chain plan and its CIP-004-7 access program, not as its own staff. The Group OT security director wrote the group OT standard, so the P07 OT tests at P8 were co-sourced with an outside OT assessment firm and group internal audit signed the results.

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (SSO, MFA, PAM, identity governance) | Corporate | IT identities for all divisions. Not used inside the Electric Utility's CIP Electronic Security Perimeters |
| SYS-G2 | Group SOC, SIEM, and EDR, with an OT monitoring console | Corporate | 24x7. Passive OT network sensors at plants P1 to P7 and at the TCC and backup TCC |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic) and data platform | Corporate | Provider A: corporate landing zone, the GEPS, data platform and AI workloads. Provider B: FMS, Grid Engineering client project platform, immutable backup vault, GEPS disaster recovery |
| SYS-G4 | **Group ERP and Production Scheduling Platform (GEPS)** | Corporate (Group ERP platform director) | One shared ERP instance with a company code per division: finance, procurement, inventory, and order management for all three divisions; Manufacturing configure-to-order, bills of materials, routings, export screening, and the advanced planning and scheduling (APS) module; Electric Utility storm stock and materials; Grid Engineering project accounting. Includes the **integration hub** that sends work orders to the 8 plant MES and exchanges EDI with customers and suppliers |
| SYS-G5 | Group HR, payroll, and applicant tracking (SaaS) | Corporate | HR data for 45,000 employees |
| SYS-G6 | Productivity suite and group file services | Corporate | Email, chat, and file shares for all divisions, plus legacy on-premises file servers in the group data center |
| SYS-M1 | Plant MES (one standard product at P1 to P7; a legacy MES at P8) | Manufacturing | MES application servers in each plant's OT DMZ at P1 to P7. **The P8 legacy MES server is dual-homed on the office and plant networks** |
| SYS-M2 | Plant control systems (OT) | Manufacturing | About 4,100 OT assets: PLCs, CNC core cutting lines, winding machines, vapor-phase drying ovens, vacuum oil processing, robotic welding, paint lines, crane controls, and about 650 HMIs and engineering workstations. P1 to P7 are zoned behind OT DMZs with a central OEM remote access gateway. **P8 has a flat network and 4 always-on OEM cellular routers** |
| SYS-M3 | PLM and design vault | Manufacturing | Designs, electromagnetic calculations, winding specifications, customer drawings |
| SYS-M4 | Test systems and Test Data Management System (TDMS) | Manufacturing | Routine test stations at every plant; high-voltage labs at P2, P4, P5. Certified test reports |
| SYS-M5 | TMU firmware build and signing pipeline | Manufacturing (Grid Products) | Code repositories (SaaS), build servers in the group data center, customer download portal. **The firmware signing key sits in a software keystore on a build server, not in a hardware security module** |
| SYS-M6 | Fleet Monitoring Service (FMS) | Manufacturing | Cloud provider B; see section 1.1 |
| SYS-M7 | Plant historians and the manufacturing analytics workspace | Manufacturing | One historian per plant with a read-only replica in each OT DMZ (P1 to P7). Feeds AI-002 on the group data platform. At P8 a vendor connector sends historian tags directly to the internet |
| SYS-U1 | Transmission EMS/SCADA at the TCC and backup TCC | Electric Utility | Medium impact BES Cyber Systems with their EACMS and PACS |
| SYS-U2 | Distribution ADMS and outage management at the DCC | Electric Utility | Outside CIP scope; polls gateways at the 58 transmission substations that are part of low impact BES Cyber Systems |
| SYS-U3 | Substation automation and field network | Electric Utility | 58 transmission substations (low impact) and 310 distribution substations |
| SYS-U4 | AMI head end (vendor SaaS) and customer information system (vendor SaaS) | Electric Utility | 1.4 million meters; customer names, addresses, Social Security numbers for credit decisions, and bank account numbers |
| SYS-U5 | Work and asset management (EAM) and the load-forecasting model | Electric Utility | EAM on Cloud provider A; AI-004 on the group data platform |
| SYS-S1 | Client project platform | Grid Engineering (on Cloud provider B) | Document management for about 3,900 active projects. Holds client CEII and BES Cyber System Information (BCSI) and the Electric Utility's TCC design documents |
| SYS-S2 | Design environment and commissioning laptops | Grid Engineering | CAD and protection settings tools; about 700 commissioning laptops used as Transient Cyber Assets at client substations; the generative AI design assistant pilot (AI-006) |

**SSP system (P02):** the *Group ERP and Production Scheduling Platform (GEPS)*: the shared corporate ERP instance (SYS-G4) with its finance, procurement, inventory, order management, bills of materials, export screening, and APS production scheduling modules for all three divisions, the integration hub that links it to the 8 plant MES and to EDI, its database and application tiers in Cloud provider A, and its disaster recovery copy and backups in Cloud provider B; it inherits common controls from SYS-G1 to SYS-G3, and the plant MES and OT (SYS-M1, SYS-M2), PLM, TDMS, FMS, utility systems, and the client project platform are interconnected systems outside the boundary.

## 4. Current security posture: a defined group program, mixed by division
**In place today:**
- Group policies aligned to NIST CSF 2.0 (v2026, approved 2026-03-24) and a common control catalog (2025)
- 24x7 group SOC with SIEM and EDR on IT endpoints and servers; passive OT network sensors at P1 to P7 and at the TCC
- PAM and quarterly access certification for IT systems (SYS-G1); phishing-resistant MFA for administrators
- Immutable backups in Cloud provider B with a separate backup identity
- OT DMZs, deny-by-default IT/OT firewalls, and a central OEM remote access gateway at P1 to P7 (plant OT program, 2023 to 2025)
- A NERC CIP compliance program at the Electric Utility: CIP Senior Manager designated, medium impact program for the TCC, low impact plan for the 58 transmission substations, CIP-013-2 supply chain plan (approved 2025-11-20)
- An EOP-004-4 event reporting Operating Plan and Form DOE-417 procedures at the TCC
- A TMU product security incident response team (PSIRT) and a register of the 140 utility addenda (Manufacturing)
- Grid Engineering SOC 2 Type 2 report for the client project platform (Security and Confidentiality)
- SEC Item 106 disclosure in the 2025 annual report; a disclosure committee with a cybersecurity charter
- A Group AI Standard and Group AI council (2026-03)
- A group cyber insurance tower with an incident response panel that includes an OT-capable firm

**Missing or weak, found in the 2026 assessments:**
1. **GEPS reach into the plants.** The integration hub uses 6 service accounts with standing access to all 8 plant MES. The P8 legacy MES is dual-homed. GEPS disaster recovery has been tested only for the finance modules; a full restore of APS and the integration hub has never been tested, so the 24-hour production scheduling recovery time is unproven.
2. **The acquired plant (P8).** Flat OT network, 4 always-on OEM cellular routers with shared logins, 19 HMIs on operating systems past vendor support, a legacy directory domain with a two-way trust to the corporate domain, and no OT monitoring.
3. **TMU product security.** The firmware signing key is in a software keystore on a build server. The 30-day vulnerability disclosure term in the utility addenda was missed twice in 2026. SBOMs exist for 3 of 7 firmware lines.
4. **Affiliate relationships.** The 2019 intercompany supply agreement and the 2020 intercompany services agreement have no security schedules. Electric Utility TCC design documents (BCSI) sit on Grid Engineering's project platform outside the utility's CIP-011-3 program (2 of 20 sampled projects).
5. **Electric Utility CIP gaps.** CIP-003-9 Attachment 1 Section 6 (vendor electronic remote access for low impact, effective 2026-04-01): the detection method for known or suspected malicious communications is in place at 22 of 58 transmission substations. CIP-012-2 (effective 2026-07-01): the plan does not yet cover availability and recovery (Parts 1.2 and 1.3).
6. **Grid Engineering contract duties and inheritance.** No register of the CIP flow-down terms in 41 client contracts and no route from group SOC findings to client notices. Common control inheritance is documented for Manufacturing and the Electric Utility but not for Grid Engineering, and its 2023 standards conflict with group policy.
7. **Cross-division incident notification.** A production-stopping ransomware incident could trigger utility addenda notices (24 and 48 hours), Grid Engineering client notices, Electric Utility CIP-008-6 and DOE-417 reports, FAR reports, state breach notices, and an SEC materiality decision at once. The group notification matrix was drafted in 2026-06 and has never been exercised.
8. **AI governance lag.** The demand forecasting (AI-001) and predictive maintenance (AI-002) models went live before the Group AI Standard without independent validation. The forecast feeds the allocation of storm-reserve production slots, including slots for the affiliated Electric Utility, with no documented allocation rule. The P8 predictive maintenance connector opened an outbound internet path from the plant historian.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P01 | Group register plus three division registers (Transformer Manufacturing, Electric Utility, Grid Engineering), rolled up to group ERM |
| P02 | SSP for the GEPS, a shared corporate system (the registry's primary system, "ERP and production scheduling system", at this size a group ERP instance serving all three divisions). Common control catalog for all divisions |
| P03 | Manufacturing: NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary benchmark) plus the binding contract and FAR duties. Electric Utility: NERC CIP at medium and low impact, with EOP-004-4 and Form DOE-417. Grid Engineering: client contract flow-down of NERC CIP terms, CEII handling, and FAR 52.204-21. Group-wide: SEC, state breach laws, OFAC. Regulation-by-division matrix |
| P06 | Group policies POL-01 to POL-05 revised to v2026.1 (approved 2026-09-15, effective 2026-10-01) with division supplements; the Grid Engineering 2023 standards are replaced by a supplement. A customer security terms register (utility addenda, client CIP terms, FAR clauses, SOC 2 commitments) is required by POL-01 4.8 |
| P07 | 18 common controls assessed once, the GEPS, and samples of all three divisions by group internal audit; P8 OT tests co-sourced with an outside OT assessment firm |
| P08 | Ransomware disrupting production of grid equipment (registry default) that spans divisions: it encrypts GEPS application servers, the integration hub, group file servers, the P8 MES and HMIs, and the TMU firmware build servers, takes data from Grid Engineering and HR file shares, and probes the Electric Utility's TCC access point |
| P09 | Scoping per division: Manufacturing FMS in scope (first SOC 2 Type 2 readiness); Grid Engineering client project platform in scope (existing Type 2); Electric Utility out of scope with reasons |
| P10 | Group AI program with division use cases; focus use case: demand forecasting and predictive maintenance (registry default; AI-001 and AI-002). Kept because at this size both are live models that went into production before the Group AI Standard and the forecast steers storm-reserve allocation, including to the affiliated utility. Other inventory entries: AI-003 FMS asset-health analytics, AI-004 load forecasting, AI-005 enterprise generative AI assistant (pilot, 3,000 users), AI-006 Grid Engineering design assistant (pilot, 120 engineers), AI-007 weld and paint vision inspection (P4, P5 pilot), AI-008 coding assistant for TMU firmware (110 developers), AI-009 invoice matching in the GEPS. A storm allocation committee (VP supply chain, VP manufacturing operations, counsel) approves storm-reserve allocations |
| Cloud | Shared corporate platform with two providers plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses and gap analyses (plant walkthroughs at P2, P5, and P8 on 2026-06-09 to 2026-06-12; TCC walkthrough 2026-06-17) |
| 2026-07-06 to 2026-08-28 | Common control assessment by group internal audit, plus division samples (P8 OT tests in the maintenance window on 2026-08-22) |
| 2026-08-27 | Group AI council assessment of the AI portfolio |
| 2026-09-15 | Results to the board risk committee; deliverables approved |
| 2026-09-30 | Electric Utility self-reports to SERC of potential CIP noncompliances (P03) |

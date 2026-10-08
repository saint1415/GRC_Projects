# Scenario facts: Cris Santos Company | Transportation and Warehousing | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Regulatory facts were checked against eCFR (point in time 2026-09-23), the U.S. Code (govinfo and uscode.house.gov) and the Federal Register between 2026-09-26 and 2026-10-04.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; port logistics group) |
| Structure | A holding company with three divisions and corporate shared services |
| Division 1: Marine Terminals (NAICS 488320), **focus of this scenario** | Operates 9 container, breakbulk and ro-ro terminals at 5 U.S. ports in 4 states under long-term leases from port authorities, including its own stevedoring. About 23,000 employees: about 9,000 permanent staff and about 14,000 registered longshore workers dispatched per shift through union hiring halls under collective bargaining agreements. Every terminal is a facility regulated under 33 CFR Part 105 |
| Division 2: Freight Trading (NAICS 423510, sector 42 Wholesale Trade) | Merchant wholesale trading of imported and exported steel products, lumber and other construction commodities, with 38 distribution yards and service centers. About 13,500 employees. Sells to the Department of Defense (supply contracts that carry Federal Contract Information) |
| Division 3: Port Real Estate (NAICS 531120, sector 53 Real Estate) | Owns and leases 46 port-area warehouses and distribution centers (about 21 million square feet) and 3 truck staging and container depot yards to about 180 commercial tenants. About 3,000 employees |
| Corporate shared services | Identity, network, security operations, cloud platform, B2B integration hub, ERP, HR, finance, legal and internal audit. About 5,500 employees |
| Location | Headquartered in Florida. Operations in Florida, Georgia, Louisiana and Texas. **State law handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| SBA size status | Not small (the SBA standard for NAICS 488320 is $47.0 million in average annual receipts; 13 CFR 121.201) |
| Related-party dealings | The Freight Trading division imports about 30% of its tonnage through group terminals and leases 9 Port Real Estate warehouses. Terminals must treat it like any other cargo owner (see gap 1) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks; receives the High risk list quarterly |
| Group CISO; Group Chief Risk Officer; Group General Counsel | Group standards, group risk register (ERM roll-up), notification matrix and intercompany agreements |
| Division security and compliance leads (3) | Division registers, division supplements, division-specific regulators |
| Marine Terminals Division Cybersecurity Officer (CySO) | Designated in writing on 2026-03-02 as CySO for all 9 facilities (33 CFR 101.625(b)); reports to the division president with a dotted line to the Group CISO |
| Terminal alternate CySOs (one per terminal) | Terminal IT and OT leads; designated for terminals T1 to T6 only (gap 3) |
| Facility Security Officers (FSOs), one per terminal | Facility Security Plans (FSPs), TWIC access control, MTSA drills, exercises and reporting |
| Freight Trading federal contracts compliance manager | CMMC Level 1 self-assessment, SPRS entries, FAR and DFARS clause compliance |
| Port Real Estate director of building technology | Building management, access control and CCTV systems at 46 warehouses |
| Group internal audit | Reports to the board audit committee. Assesses common controls once and samples division controls |
| Disclosure committee | SEC materiality of cybersecurity incidents |
| Group AI council | Approves High-tier AI use cases (chaired by the Group Chief Risk Officer) |

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (SSO, MFA, PAM, identity governance) | Corporate | All divisions federate to it |
| SYS-G2 | Group SOC, SIEM and EDR (24x7) | Corporate | EDR on all IT servers and workstations, including the Gulf terminals |
| SYS-G3 | Group cloud platform (providers A and B, vendor-agnostic), landing zones, WAN and immutable backup vault | Corporate | Provider A primary; provider B for disaster recovery and the backup vault |
| SYS-G4 | Group B2B integration hub (managed file transfer, EDI translation, partner APIs) | Corporate | Carriers, customs data exchange, port community systems, trading suppliers and customers, tenant rent files from banks |
| SYS-G5 | Group ERP, treasury, HR and payroll (SaaS) | Corporate | Includes longshore payroll and SEC reporting |
| SYS-G6 | Productivity suite (email, files, chat) | Corporate | |
| SYS-T1 | Standard terminal operating system (TOS): vessel, yard and gate modules, equipment dispatch, billing, EDI adapters. One multi-terminal instance | Marine Terminals | Commercial TOS software run by the division in the group cloud (provider A). Serves T1 to T6 |
| SYS-T1L | Legacy TOS at the 3 Gulf terminals (T7 to T9) | Marine Terminals | On-premises servers at each terminal; migration to SYS-T1 due 2027-06-30 |
| SYS-T2 | Gate automation: OCR portals, TWIC readers tied to the physical access control system (PACS), driver kiosks, gate servers | Marine Terminals | At every terminal |
| SYS-T3 | Crane, automated stacking crane (ASC) and yard equipment OT: PLCs, HMIs, the T5 equipment control system, vehicle-mounted terminals (VMTs) | Marine Terminals | 64 ship-to-shore cranes, 210 rubber-tired gantries, 48 ASCs at T5, about 900 yard tractors |
| SYS-T4 | Terminal site networks and OT zones | Marine Terminals | Segmented at T1 to T6; flat at T7 to T9 (gap 2) |
| SYS-T5 | Berth and yard optimization service (AI, vendor SaaS) | Marine Terminals | Advisory at 5 terminals; automatic ASC job sequencing at T5 since 2026-03 (gap 8) |
| SYS-T6 | Terminal customer portal and truck appointment system | Marine Terminals | Built by the division on provider A; used by carriers, cargo owners and about 4,200 trucking companies |
| SYS-F1 | Freight Trading ERP extension and commodity trading and risk management (CTRM) platform | Freight Trading | SaaS |
| SYS-F2 | Distribution yard management system, scales and shipping documents | Freight Trading | 38 yards |
| SYS-F3 | Federal sales workspace (Federal Contract Information scope) | Freight Trading | A restricted area of SYS-G6 and SYS-F1 used for DoD orders |
| SYS-R1 | Property management, lease administration and tenant portal | Port Real Estate | SaaS |
| SYS-R2 | Building systems: building management (BMS), access control and CCTV at 46 warehouses and 3 yards | Port Real Estate | Run by 5 systems integrators with remote access (gap 5) |

**Terminals:** T1 and T2 (Florida port 1), T3 and T4 (Florida port 2), T5 (semi-automated) and T6 (Georgia port), T7 (Louisiana port), T8 and T9 (Texas port). T7 to T9 were acquired in 2024 ("the Gulf terminals"). Together the terminals handle about 5.6 million container moves and 9 million tons of breakbulk a year, about 55 vessel calls a week and about 14,000 truck gate transactions a day.

**SSP system (P02):** the *Terminal Operations Platform (TOP)*: the standard TOS (SYS-T1) with its EDI adapters, gate automation (SYS-T2) and operations endpoints at terminals T1 to T6, and the TOS equipment interface to SYS-T3, inheriting common controls from SYS-G1 to SYS-G4.

**Registry defaults kept:** the primary system (TOS and gate automation), the P08 incident (ransomware disrupting the TOS) and the P10 use case (container and berth scheduling optimization) all fit this business. At this size the P08 incident is set to start in a shared service so that it spans all three divisions, and P10 covers the group AI program with the scheduling optimization service as the priority use case.

## 4. Current security posture: defined program, gaps at the seams
**In place today:**
- Group policies aligned to CSF 2.0 and a common control catalog (2025)
- 24x7 group SOC with EDR on all IT servers and workstations
- MFA for all workforce on SSO applications; phishing-resistant MFA and just-in-time PAM for administrators
- Quarterly access certification for systems federated to SYS-G1
- Immutable backups of cloud workloads in the provider B vault; quarterly restore tests of the standard TOS since 2025
- Coast Guard-approved FSPs and an FSO at all 9 terminals; TWIC-based access control
- A Subpart F program office (since 2025-07) and a Division CySO designated in writing for all 9 facilities (2026-03-02)
- Cybersecurity training completed by 96% of permanent staff by 2026-01-12
- CTPAT partner status for the terminal division (marine port authority and terminal operator) and the trading division (importer)
- CMMC Level 1 (Self) status affirmed in SPRS for the federal sales workspace (2025-11-03)
- SEC Reg S-K Item 106 disclosure in the annual report

**Gaps:**
1. **Commercial data segregation and affiliate preference in the TOS.** 212 Freight Trading users hold a "group logistics" TOS role that shows cargo, vessel and appointment data for every customer at T1 to T6, including competing importers. At T3 and T5, appointment rules give the trading division's truckers reserved slots with no documented operational reason. Terminal services agreements require confidentiality of customer cargo data, and a marine terminal operator may not give "any undue or unreasonable preference or advantage" to any person (46 U.S.C. 41106(2)).
2. **Gulf terminals (T7 to T9).** Legacy TOS on premises, flat IT and OT networks, always-on crane vendor remote access, and local logs only (network and TOS logs are not in the group SIEM). Migration to SYS-T1 and the standard OT zone design is due 2027-06-30.
3. **Subpart F program behind at three terminals and for longshore labor.** Alternate CySOs designated for T1 to T6 only. Draft Cybersecurity Plans exist for T1 to T6; none for T7 to T9. Longshore workers who use OT and VMTs: 58% trained by the 2026-01-12 deadline. OT-specific training exists only at T5.
4. **Trading division federal work.** The 2026 scoping review found FCI on yard shipping documents in SYS-F2, outside the Level 1 assessment scope. On 2026-06-18 a DoD prime contractor emailed fabrication drawings marked CUI to a sales engineer for a quote. The division has no environment that meets NIST SP 800-171 and no written procedure for CUI or for DFARS 252.204-7012 incident reporting.
5. **Port Real Estate building systems and payments.** BMS, access control and CCTV at 46 warehouses are run by 5 integrators; 31 sites have internet-exposed remote access; none is monitored by the group SOC. The division supplement was last aligned in 2023. In 2026-03 a business email compromise attempt to redirect a $2.4 million property closing wire was stopped by a callback.
6. **Common control inheritance.** Documented for Marine Terminals and Freight Trading, not for Port Real Estate.
7. **Shared incident notification.** An incident in a shared service may trigger Coast Guard reports for several terminals, SEC disclosure, DoD reporting, state breach notices, carrier and tenant notices. The single notification matrix has not been exercised.
8. **AI governance.** Since 2026-03 the optimization service (SYS-T5) sequences ASC yard jobs automatically at T5 without a safety case or AI council approval (the Group AI Standard was adopted on 2026-06-15, after the change). The trading legal team uses a generative AI contract review tool with counterparties' confidential terms.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Regulation (P03) | Marine Terminals: USCG cyber rule, 33 CFR Part 101 Subpart F, with 33 CFR 6.16-1 and 101.305. Freight Trading: FAR 52.204-21, CMMC Level 1 (32 CFR Part 170) and DFARS 252.204-7012. Port Real Estate: FTC Safeguards Rule elements used as a voluntary benchmark (the rule does not apply; see P03). Group: SEC Reg S-K Item 106 and Form 8-K Item 1.05, Shipping Act 46 U.S.C. 41106, state breach laws |
| P08 | Ransomware that starts in the group B2B integration hub (SYS-G4), disrupts the TOS at all 9 terminals, and steals data from all three divisions: a multi-regulator notification matrix with Coast Guard, SEC, DoD and state duties |
| P09 | SOC 2 scoped per division: the terminal customer data services (SYS-T6 and partner EDI) are in scope for a first report; Freight Trading and Port Real Estate are out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the rules that bear on them (Subpart F, Shipping Act, OSHA marine terminal standards, FTC Act) |
| Cloud | Shared corporate platform (providers A and B) plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2025-07-16 | Subpart F effective (90 FR 6298) |
| 2026-01-12 | Subpart F training deadline (101.650(d)(4)). Met for permanent staff; missed for longshore labor |
| 2026-05-04 to 2026-07-31 | Group and division BIAs, risk analyses and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples. OT tests at T5 on the night of 2026-08-12, with no vessel at berth |
| 2026-08-31 to 2026-09-04 | SOC 2 readiness self-assessment (P09) and AI council review (P10) |
| 2026-09-15 | Results to the board risk committee; deliverables approved |
| 2027-07-16 | Cybersecurity Assessments and Cybersecurity Plans for all 9 terminals due (101.650(e)(1); 101.655) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Safety risks (crane, ASC and hazardous cargo) rated High must be treated, not accepted |
| Revenue split (fictional) | Marine Terminals about $3.4 billion; Freight Trading about $13.6 billion; Port Real Estate about $1.0 billion |
| Cloud | Provider A hosts the corporate landing zone, SYS-T1, SYS-T6, SYS-G4 and the AI service connector. Provider B hosts the disaster recovery replica of SYS-T1 and the immutable backup vault. SYS-T1L runs on servers at each Gulf terminal |
| Federal contracts | Freight Trading holds DoD supply contracts worth about $140 million a year. They include FAR 52.204-21, FAR 52.204-25 and DFARS 252.204-7012. No contract identifies covered defense information to date |
| Container freight station | One Port Real Estate warehouse sits inside the T3 secure area and is covered by the T3 FSP. Its access control readers report to the T3 PACS |
| Personal information | Employee and longshore worker records (SYS-G5); truck driver names and license numbers in gate transactions (SYS-T2); TWIC reader records; tenant contacts and guarantor data of sole-proprietor tenants (SYS-R1) |
| Cyber insurance | Group cyber insurance tower with a breach hotline and a panel of forensic firms and breach counsel |
| Terminals T1 to T6 (SSP scope) | About 6,200 permanent staff and about 9,500 registered longshore workers use the Terminal Operations Platform; about 10,000 of the 14,000 daily gate transactions are at T1 to T6. Longshore workers are dispatched by 5 hiring halls, one per port, and sign in to VMTs with individual operator IDs (TWIC tap plus PIN) |
| Subpart F program details | Critical IT and OT systems designated by the CySO for T1 to T6 in 2026-05. One Cybersecurity Plan per terminal; target submission 2027-04-30. A third-party penetration test of the TOS, the customer portal interface and the T2 gate was done in 2026-04 (OT out of scope). 3 of 11 OT KEVs at T1 to T6 were past the 30-day target at fieldwork. The group runs a public vulnerability disclosure page (since 2025) and shares threat information through a maritime information sharing organization and each port's Area Maritime Security Committee |
| Integration hub (SYS-G4) | 14 TOS EDI adapter service accounts with static passwords; 2 carriers still send by plain FTP; 11 partner credentials shared across divisions; one hub service account can write to every division's inbound folders. Full rebuild never tested |
| P07 new finding | Default vendor passwords on 2 OCR portal controllers at the T5 gate and 4 ASC maintenance HMIs at T5, plus open USB ports on those HMIs (found 2026-08-12; passwords changed 2026-09-22) |
| AI (P10) | SYS-T5 returned to advisory mode at T5 on 2026-09-25. Inventory also lists gate OCR, crane predictive maintenance, the trading legal AI tool (suspended for counterparty documents from 2026-09-04), commodity forecasting, building energy optimization, CCTV intrusion analytics, an enterprise generative AI assistant piloted with 1,500 users, and a SOC triage assistant |
| Freight Trading federal work | The CUI-marked drawings received 2026-06-18 were quarantined on 2026-08-04; the division president decides by 2026-10-31 whether to build a CUI enclave or decline CUI work. 12 yards use a shared login on scale PCs; 9 scale PCs were disposed of locally in 2026 without sanitization records |
| Out of scope by fact | No operations, employees or consumers in California or Colorado. Port Real Estate tenants pay rent by ACH; occasional card payments go through the processor's hosted page. Port Real Estate leases are commercial operating leases (no consumer financial products) |
| SOC 2 (P09) | About 140 carrier and cargo owner security questionnaires were answered in 2025. Target: Type 1 report as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30, for the terminal customer data services |

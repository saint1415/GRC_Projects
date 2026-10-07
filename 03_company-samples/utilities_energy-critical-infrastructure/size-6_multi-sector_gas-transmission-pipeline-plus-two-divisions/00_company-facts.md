# Scenario facts: Cris Santos Company | Energy | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Regulatory facts were checked against the eCFR (point in time 2026-09-23), the TSA-published texts of Security Directive Pipeline-2021-01G (effective 2026-01-16 through 2027-01-15) and Pipeline-2021-02G (effective 2026-05-03 through 2027-05-02), and the Federal Register, between 2026-09-26 and 2026-10-05.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; diversified midstream energy group) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate operating subsidiary |
| Division 1: Gas Transmission (NAICS 486210), **focus of this scenario** | Interstate natural gas transmission pipeline company regulated by FERC under the Natural Gas Act. About 7,400 miles of transmission pipeline (16 to 42 inches) in Texas, Louisiana, Mississippi, Alabama, Georgia, and Florida; 41 compressor stations; about 640 meter and regulator stations; about 410 remote-control valve sites. Design capacity about 4.6 billion cubic feet per day for about 340 shippers, including 46 local distribution companies and 58 gas-fired power plants. **TSA has notified the division that its pipeline system is critical**, so Security Directives Pipeline-2021-01G and -02G apply. About 9,500 employees |
| Division 2: Gathering and Production (NAICS 211130, sector 21 Mining, Quarrying, and Oil and Gas Extraction) | Natural gas producer and gathering operator in the Haynesville (northwest Louisiana and East Texas) and Arkoma (eastern Oklahoma) basins. About 5,600 operated wells and about 3,300 miles of onshore gathering lines with 58 field compressor stations. Delivers about 40% of its gas into the Gas Transmission system and the rest to third-party pipelines. About 22,000 employees, including its own field crews |
| Division 3: Integrity Services (NAICS 541330, sector 54 Professional, Scientific, and Technical Services) | Pipeline engineering and integrity services: in-line inspection (ILI) data analysis, integrity engineering, records verification, and the **Integrity Data Platform**, a multi-tenant service that clients use as their integrity management records system. A 120-person OT Assessment Practice performs OT architecture reviews and testing for pipeline operators. About 160 external clients in 34 states plus the Gas Transmission division. About 8,500 employees |
| Corporate shared services | Identity, network, security operations, OT security engineering, cloud and data platform, ERP, HR, finance, legal, and internal audit. About 5,000 employees |
| Location | Headquartered in Florida (corporate offices and the primary Gas Control Center). Operations in Texas, Louisiana, Mississippi, Alabama, Georgia, Florida, and Oklahoma; Integrity Services clients in 34 states; royalty owners in all 50 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| SBA size status | Not small. SBA standards (13 CFR 121.201): NAICS 486210, $41.5 million in average annual receipts; NAICS 211130, 1,250 employees; NAICS 541330, $25.5 million |
| Why these three businesses | A midstream group with upstream and services affiliates: Gathering and Production feeds the transmission system, and Integrity Services grew out of the transmission integrity program and now sells the same services to other operators |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks; receives the High risk list quarterly |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3) |
| Group OT Security Director | Reports to the Group CISO. OT security architecture, the OT remote access gateway, OT monitoring sensors, and the OT desk of the group SOC for all three divisions. Alternate TSA Cybersecurity Coordinator for Gas Transmission |
| Group Chief Risk Officer | Group risk register and enterprise risk management (ERM) roll-up; chairs the Group AI council |
| Group General Counsel | Notification matrix, intercompany and client agreements, regulator notices, privilege; leads the group privacy office |
| Division security and compliance leads (3) | Division registers, division supplements, division-specific regulators |
| Gas Transmission: Director of Pipeline Cybersecurity | The division security and compliance lead. **Primary TSA Cybersecurity Coordinator** (U.S. citizen, SD 01G Section II.B); owns the TSA Cybersecurity Implementation Plan and Cybersecurity Assessment Plan |
| Gas Transmission: Vice President of Gas Control | System owner of the Pipeline SCADA and Gas Control System; owns the control room management program (49 CFR 192.631) at both gas control centers |
| Gas Transmission: Director of Gas Control | Control room management procedures, alarm management plan, controller training; supervises about 90 gas controllers |
| Gas Transmission: SCADA Engineering Manager | SCADA hosts, HMIs, station control system standards, point-to-point verification |
| Gas Transmission: Pipeline Safety Compliance Director | PHMSA program; incident notices under 49 CFR Part 191; emergency plans (192.615) |
| Gas Transmission: Vice President of Commercial Operations | Nominations, scheduling, capacity release, measurement, and FERC tariff operations; FERC service interruption reports (18 CFR 260.9) |
| Gathering and Production: Vice President of Field Operations Technology | Business owner of the field SCADA platform; OT technical owner for the division |
| Gathering and Production: Gathering Compliance Manager | Gathering line determinations (192.8), Type B and Type C requirements (192.9), Part 191 reports |
| Gathering and Production: Revenue Accounting Vice President | System owner of hydrocarbon accounting and revenue distribution |
| Integrity Services: Chief Technology Officer | System owner of the Integrity Data Platform |
| Integrity Services: Client Security Officer | The division security and compliance lead. Client security commitments, Sensitive Security Information (SSI) handling program, SOC 2 program |
| Integrity Services: OT Assessment Practice Leader | Client OT assessments, assessment toolkits, engagement data handling |
| Group internal audit | Reports to the board audit committee. Assesses common controls once and samples division controls |
| Disclosure committee | SEC materiality of cybersecurity incidents |
| Group AI council | Approves High-tier AI use cases |

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (corporate directory, SSO, MFA, PAM, identity governance) and the **OT remote access gateway** | Corporate | All divisions federate to it. One OT remote access gateway cluster serves OT support staff of all three divisions and Integrity Services engineers (gap 3) |
| SYS-G2 | Group SOC, SIEM, EDR (24x7), security orchestration (SOAR), and the OT monitoring console | Corporate | Passive OT monitoring sensors at both gas control centers, 36 of 41 compressor stations, and the Haynesville Operations Center |
| SYS-G3 | Group cloud platform (providers A and B, vendor-agnostic), landing zones, wide-area network, two group data centers, and the immutable backup vault | Corporate | Provider A primary; provider B for disaster recovery and the backup vault. Group data centers in Florida and Louisiana |
| SYS-G4 | Group ERP (finance, supply chain, work management), HR and payroll (SaaS) | Corporate | |
| SYS-G5 | Productivity suite (email, files, chat) and corporate file shares | Corporate | |
| SYS-G6 | Group data and analytics platform (historian replicas, engineering analytics, machine learning workspace) | Corporate | Receives one-way historian replicas from each division's OT DMZ. Trains the leak-detection anomaly model (P10) |
| SYS-T1 | Pipeline SCADA: redundant SCADA hosts, HMIs, historians, and engineering workstations at the **primary Gas Control Center** (Florida) and the **Backup Gas Control Center** (Louisiana), with computational pipeline monitoring | Gas Transmission | 24x7. About 90 gas controllers |
| SYS-T2 | Station and field control: station control PLCs, unit control panels, and station HMIs at 41 compressor stations; about 2,300 RTUs, PLCs, and flow computers at meter, regulator, valve, and interconnect sites; private microwave and MPLS network with satellite backup | Gas Transmission | Station emergency shutdown systems are hardwired and independent of SCADA |
| SYS-T3 | Transmission OT DMZs (one central, two regional): historian brokers, patch and antivirus relays, PAM session landing, and the leak-detection scoring server | Gas Transmission | Built to the TSA implementation plan zone model (2023) |
| SYS-T4 | Gas measurement and accounting system (measurement data validation, custody transfer volumes, gas quality, imbalances) | Gas Transmission | On premises in the Florida group data center, with a replica in Louisiana. Servers are joined to the corporate directory and receive flow computer data through the central OT DMZ (gap 1) |
| SYS-T5 | Nominations, scheduling, capacity release, and customer informational postings platform (NAESB WGQ electronic communications, 18 CFR 284.12) | Gas Transmission | Built by the division on provider A. Depends on SYS-T4 for measured volumes |
| SYS-T6 | Physical access control and video at the gas control centers and compressor stations | Gas Transmission | Counted as OT under the SD definition of Operational Technology system |
| SYS-P1 | Field SCADA platform at the **Haynesville Operations Center** (Louisiana) with a backup control room at the Arkoma field office (Oklahoma) | Gathering and Production | 24x7. About 60 field controllers |
| SYS-P2 | Field control devices and communications: about 11,000 RTUs, PLCs, wellhead and compressor controllers, and flow computers; private LTE, licensed radio, and about 4,800 cellular gateways | Gathering and Production | Safety shutdowns at compressor and treating stations are independent of SCADA |
| SYS-P3 | Hydrocarbon accounting and revenue distribution (vendor SaaS) | Gathering and Production | About 140,000 royalty owners (names, Social Security or taxpayer numbers, bank accounts) |
| SYS-P4 | Legacy field SCADA at the Arkoma assets acquired 2025-06-30 | Gathering and Production | On-premises servers at two field offices; flat network; always-on vendor remote access with a shared account; not in the group SIEM (gap 4). Migration to SYS-P1 due 2027-06-30 |
| SYS-E1 | Integrity Data Platform (IDP): ILI results, alignment sheets and GIS, risk models, MAOP and material records, dig and repair records | Integrity Services | Multi-tenant service on provider A with a warm standby in provider B. In scope for SOC 2 (P09) |
| SYS-E2 | ILI data intake and analysis environment (secure transfer from ILI tool vendors; analysis workstations) | Integrity Services | Hosts the ILI anomaly classification model (P10) |
| SYS-E3 | OT Assessment Practice toolkits (assessment laptops, passive capture appliances) and the engagement evidence store | Integrity Services | Holds client network captures, firewall rules, and diagrams during and after engagements (gap 2) |
| SYS-E4 | Engineering project and document management (client deliverables, drawings, CEII and SSI received from clients) | Integrity Services | On corporate file shares and the productivity suite |

**SSP system (P02):** the *Pipeline SCADA and Gas Control System (PSGCS)*: the Gas Transmission division's SCADA (SYS-T1), station and field control and communications (SYS-T2), the transmission OT DMZs (SYS-T3), and the physical access control at the gas control centers and compressor stations (SYS-T6), with interfaces to gas measurement (SYS-T4), nominations (SYS-T5), the group data platform (SYS-G6), and the Integrity Data Platform (SYS-E1). It inherits common controls from SYS-G1 to SYS-G3.

**Registry defaults kept, with scale adjustments.** The primary system (pipeline SCADA and gas control), the P08 incident (ransomware on business IT forcing a precautionary pipeline shutdown), and the P10 use case (pipeline leak-detection anomaly model) all fit this business. At this size: the P08 incident starts in corporate shared services and reaches all three divisions, and the precautionary shutdown is of one transmission segment (6 compressor stations) rather than the whole system, because a full shutdown of a 7,400-mile interstate system would cut firm supply to local distribution companies and power plants beyond what line pack can cover, creating its own public safety risk. P10 covers the group AI program, with the leak-detection anomaly model as the priority use case.

## 4. Current security posture: varies by division
**In place today:**
- Group policies aligned to CSF 2.0 and a common control catalog (2025)
- 24x7 group SOC with EDR on all IT servers and workstations, security orchestration playbooks, and an OT desk with passive OT monitoring
- MFA for all workforce on SSO applications; phishing-resistant MFA and just-in-time PAM for IT administrators
- Immutable backups of cloud workloads in the provider B vault; offline SCADA backups at both gas control centers
- Gas Transmission: a TSA-approved Cybersecurity Implementation Plan (approved 2023-01-27, last amended 2025-04-14); Cybersecurity Coordinator and alternates registered with TSA; a Cybersecurity Assessment Plan approved by TSA on 2026-02-17; an annual Cybersecurity Incident Response Plan exercise (last 2026-04-22)
- Gas Transmission: written control room management procedures (192.631) at both gas control centers; backup SCADA failover tested 2026-04-08
- Integrity Services: a SOC 2 Type 1 report on the Integrity Data Platform as of 2025-12-31 (Security, Availability, Confidentiality)
- Hardwired emergency shutdown systems at compressor stations and treating facilities, independent of SCADA
- SEC Reg S-K Item 106 disclosure in the annual report

**Gaps:**
1. **Business-critical functions ride on corporate IT.** Gas measurement (SYS-T4) servers are joined to the corporate directory and sit in the corporate data center, and nominations (SYS-T5) depends on them for measured volumes. Both are listed as Critical Cyber Systems in the TSA implementation plan, but the manual fallback for scheduling and custody measurement has only been exercised for 8 hours (2025), and the contingency plan assumes 24 hours of business IT outage at most. A long corporate IT outage could force a precautionary shutdown even with SCADA healthy.
2. **Client and SSI data in Integrity Services.** The Integrity Data Platform and engineering file shares hold SSI from the Gas Transmission division and from 9 TSA-designated clients (implementation plan excerpts, assessment results, architecture review reports) without SSI marking or need-to-know restrictions (49 CFR 1520.9). OT assessment toolkits keep client network captures after engagements close.
3. **Shared OT access paths.** The single OT remote access gateway (SYS-G1) gives OT support staff of all three divisions and Integrity Services engineers a path toward both the Transmission and the Gathering OT DMZs; separation is by gateway policy only. Integrity engineers also hold standing read access to the Transmission historian replica on SYS-G6.
4. **Arkoma acquired fields.** Legacy SCADA (SYS-P4) on a flat network, always-on vendor remote access with a shared account, unsupported operating systems on HMIs, and no logs in the group SIEM. Migration due 2027-06-30.
5. **TSA plan schedule slippage.** Password reset mitigations for compressor unit control panels (SD 02G Section III.C.1.b) are past the plan schedule at 11 of 41 stations, and no amendment request was filed with TSA. The cybersecurity architecture design review last completed on 2024-05-20, so the two-year interval (Section III.G.2.b) lapsed on 2026-05-20.
6. **Control room management records.** Point-to-point verification records are incomplete after the 2026-03 station control upgrades at 3 compressor stations (192.631(c)(2)); controller training does not cover cyber-caused abnormal operating conditions; leak-detection model threshold changes bypass control room change management (192.631(f)).
7. **Common control inheritance** is documented for Gas Transmission (part of the TSA implementation plan) and Integrity Services (SOC 2 system description), not for Gathering and Production.
8. **Shared incident notification.** One incident can trigger a CISA report under the TSA directive, PHMSA and FERC notices, an SEC materiality decision, state breach notices in many states, SSI disclosure reports, and client notices. The single notification matrix has not been exercised across divisions.
9. **AI governance.** The leak-detection anomaly model has shown advisory alerts on controller consoles since 2026-03 without documented validation or control room change management, and Integrity Services uses an ILI anomaly classification model in client deliverables. The Group AI Standard was adopted 2026-07-01, after both went live.
10. **Division supplement drift.** The Gathering and Production supplement was last aligned to group policy in 2023.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Regulation (P03) | Gas Transmission: **TSA SD Pipeline-2021-02G** (primary, applies), with SD Pipeline-2021-01G, the SCADA-relevant duties of 49 CFR 192.631, and FERC reporting (18 CFR 260.9). Gathering and Production: **NIST CSF 2.0 with NIST SP 800-82 Rev. 3** (voluntary benchmark, the vertical primary for NAICS 21) plus PHMSA gathering rules (192.8, 192.9, Part 191). Integrity Services: the FTC Safeguards Rule screened out (not a financial institution); binding duties come from SSI rules (49 CFR Part 1520), its role under clients' TSA directives (SD 02G Section II.A.3 and II.A.4), CEII handling, FTC Act Section 5, and client contracts. Group: SEC Reg S-K Item 106 and Form 8-K Item 1.05, state breach laws, and applicability screens |
| Regulatory driver labels | `C-ENERGY-R02` to `C-ENERGY-R05` with the section in parentheses for the energy rules. `N21-BM (...)` is the Gathering and Production voluntary benchmark (a scenario label, not a row in a requirements file). `PHMSA 191.x` and `PHMSA 192.x` mark pipeline safety duties outside 192.631; `FERC 260.9` and `FERC 284.12` mark FERC duties. `SSI 1520.x` marks 49 CFR Part 1520. `N54-R01` marks the screened-out Safeguards Rule. `N55-R01` (Reg S-K Item 106) and `N55-R02` (Form 8-K Item 1.05) mark SEC disclosure. `State breach` marks state breach laws (Florida worked example: Fla. Stat. 501.171) |
| P08 | Ransomware that starts in corporate shared services, encrypts the corporate directory, file shares, and the gas measurement servers, reaches the regional OT DMZ through the shared remote access gateway, steals royalty owner files and Integrity Services client files, and leads to a precautionary controlled shutdown of the transmission Eastern segment: a multi-regulator notification matrix with TSA and CISA, PHMSA, FERC, SEC, state, SSI, and client duties |
| P09 | SOC 2 scoped per division: the Integrity Data Platform is in scope (first Type 2 period 2026-01-01 to 2026-12-31); Gas Transmission and Gathering and Production are out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the rules that bear on them, with the leak-detection anomaly model as the priority use case |
| Cloud | Shared corporate platform (providers A and B) plus division workloads, vendor-agnostic. SCADA and field control stay on premises |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-02-17 | TSA approved the 2026-2027 Cybersecurity Assessment Plan (next plan and annual report due to TSA by 2027-02-17) |
| 2026-05-04 to 2026-07-31 | Group and division BIAs, risk analyses, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples. OT tests at Compressor Station 27 during a planned outage on 2026-08-12 and at Arkoma field sites on 2026-08-19 |
| 2026-08-31 to 2026-09-04 | SOC 2 readiness self-assessment (P09) and Group AI council review (P10, 2026-09-03) |
| 2026-09-22 | Results to the board risk committee; deliverables approved |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Pipeline safety and environmental risks rated High must be treated, not accepted |
| Revenue split (fictional) | Gas Transmission about $6.1 billion (about $16.7 million per day); Gathering and Production about $10.4 billion (about $28.5 million per day); Integrity Services about $1.5 billion from external clients (about $4.1 million per day), plus about $0.2 billion of intercompany work eliminated in consolidation |
| TSA designation and plans | TSA notified Gas Transmission in 2021 that its pipeline system is critical under both SD series. The TSA implementation plan lists 14 Critical Cyber Systems, including SYS-T4 and SYS-T5 as business services whose compromise could cause operational disruption. The 2026-2027 assessment plan schedules 96 plan measures; 21 (22%) had been assessed by 2026-08-28 |
| Architecture design review | Performed by an outside firm, not the Integrity Services OT Assessment Practice, to keep the reviewer independent of the group. The 2024 review completed 2024-05-20; the 2026 review is contracted to start 2026-10-05 |
| Gas control | Primary Gas Control Center at the Florida headquarters campus; Backup Gas Control Center in Louisiana, 640 miles away. Both are within hurricane-exposed regions. About 90 controllers on 12-hour shifts. Controllers sign in to consoles with named local SCADA accounts tied to SYS-G1 identities, so control does not depend on SYS-G1 |
| Gathering lines (192.8) | About 85 miles of Type B lines (Class 3 locations near two towns), about 640 miles of Type C lines (8.625 inches or larger in Class 1 locations), and about 2,575 miles of Type R lines. No Type A lines. 192.631 does not apply to the Haynesville Operations Center because 192.9(d) and (e) do not list it for Type B or Type C lines |
| Royalty owners | About 140,000 in all 50 states (about 8,000 in Florida). Owner payment files are exported from SYS-P3 to a finance file share each month |
| Integrity Services clients | About 160 external pipeline operators. 9 have told the division that TSA designated them; for those clients the OT Assessment Practice acts as an **authorized representative** for architecture design reviews or testing under SD 02G Section II.A.4. 28 clients require a SOC 2 Type 2 report on the IDP by 2027-03-31. The standard client security exhibit requires notice of a security incident affecting client data within 72 hours of confirmation |
| IDP scale | Integrity records for about 96,000 miles of client pipelines plus the Gas Transmission system. About 3,900 client users |
| Cloud | Provider A hosts the corporate landing zone, SYS-G6, SYS-T5, and SYS-E1. Provider B hosts disaster recovery replicas, the IDP warm standby, and the immutable backup vault. SYS-T1, SYS-T2, SYS-T3, SYS-T6, SYS-P1, SYS-P2, and SYS-P4 are on premises; SYS-T4 is in the Florida group data center |
| Cyber insurance | Group cyber insurance tower with a breach hotline and a panel of forensic firms and breach counsel |
| CEII | Gas Transmission files annual system flow diagrams with FERC (Form 567, 18 CFR 260.8) and requests CEII treatment for them under 18 CFR 388.113(d)(1) |
| Out of scope by fact | No liquefied natural gas facilities, underground storage fields, offshore, or MTSA-regulated facilities. No hazardous liquid pipelines. No NERC-registered functions or Bulk Electric System assets. No federal contracts. No payment card acceptance. State comprehensive consumer privacy laws are tracked by the group privacy office and are not analyzed in this sample |
| P07 new finding | Default administrator passwords on 3 cellular gateways and 2 wellhead controllers at Arkoma sites (found 2026-08-19; changed 2026-09-10; a full sweep is in progress) |
| Additional role titles | Group identity director, Group SOC director (the SOC OT desk manager reports to this role), Group network and cloud platform director, Group data platform director, Group HR director (SYS-G1 to SYS-G6 and HR operators); Gathering and Production security and compliance lead; Vice President of Gas Marketing (Gathering and Production); Vice President of Integrity Engineering (Integrity Services) |
| TSA and PHMSA history (P03) | Last TSA inspection of Gas Transmission 2025-10, no findings. Last PHMSA control room management inspection 2025-06. The station panel mitigation schedule was replaced by an internal schedule in 2026-03 without an amendment request; 7 station technicians left in 2025 and 2026 without panel password changes at the 11 lagging stations. Corporate shared services is treated in the implementation plan inheritance annex like a managed security service provider (SD 02G II.A.3) |
| Integrity Services (P03, P09) | Marketing material claims client SSI is handled under 49 CFR Part 1520 (to be corrected by 2026-10-15). About 1,100 staff can reach shares that hold SSI. MFA is optional for about 3,600 of 3,900 IDP client users. The 2026-02 IDP failover took 5.5 hours against a 4-hour objective. About 300 IDP platform staff. CEII received from about 40 clients |
| P07 tests | SOC detected a scripted connection at Compressor Station 27 in 6 minutes (2026-08-12). 2 of 6 assessment toolkits were reissued holding earlier clients' captures. 46 of 412 OT gateway accounts unused for 90 days |
| P08 scenario (exercise) | The Eastern segment has 6 compressor stations, 2 of them among the 5 stations without OT sensors. The attacker took royalty owner files (about 140,000 owners) and Integrity Services shares holding SSI of Gas Transmission and 4 designated clients; 31 clients' files affected |
| AI (P10) | The leak-detection anomaly model was moved from console display to a separate advisory screen on 2026-09-08 pending validation. The inventory also lists the ILI anomaly classification model, compressor predictive maintenance, production forecasting, proposed automated compressor and choke setpoint optimization, aerial methane detection, a SOC triage assistant, an integrity report drafting assistant, and an enterprise generative AI assistant piloted with 3,000 users. The ILI model has been in client deliverables since 2025-11 and was validated against 1,480 field-verified digs (58 of 61 immediate repair conditions classified as immediate). The report drafting assistant is piloted with 40 engineers |

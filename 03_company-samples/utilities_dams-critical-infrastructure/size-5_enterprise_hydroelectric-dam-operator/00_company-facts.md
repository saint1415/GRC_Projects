# Scenario facts: Cris Santos Company | Dams | Enterprise

All 10 deliverables in this folder use the facts below. The company, its hydroelectric projects, rivers, plants, and downstream communities are fictitious and do not describe any real dam. This scenario is independent of the other sizes. Where a fact comes from a regulation, a NERC Reliability Standard, or a FERC program document, the citation is given. Regulatory text was checked against eCFR (version date 2026-09-23), the FERC Security Program for Hydropower Projects Revision 3A PDF and FERC's Revision 3/3A change notice and FAQ on ferc.gov, the NERC Bulk Electric System Definition Reference Document (version 3, April 30, 2026), and the text of the NERC CIP-002 to CIP-015 and EOP-004-4 standards retrieved from nerc.com in 2026-09.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded hydroelectric generation company; SEC registrant, not a smaller reporting company) |
| Business | Owner and operator of a fleet of FERC-licensed hydroelectric projects (NAICS 221111, Hydroelectric Power Generation, primary). Two smaller service lines sell to other dam owners: contract remote operations and maintenance (SL-1) and a dam safety monitoring data service (SL-2) |
| Headquarters and footprint | Headquartered in Florida (corporate offices and Data Center 1). Projects in Georgia, Alabama, North Carolina, South Carolina, Tennessee, and Virginia. **State law is handled generically:** breach notices follow the law of each state where affected individuals reside, with Florida as the worked example |
| The fleet | **31 FERC licenses** covering **46 hydroelectric developments** (44 conventional and 2 pumped storage) with **63 dams** (main dams, saddle dikes, and reregulating dams), **151 generating units**, and **8,640 MW** of installed capacity. Gated spillways at 41 dams |
| Largest plants (fictional names) | DEV-01 Laurel Ridge Pumped Storage Station (North Carolina, 1,320 MW, 4 units); DEV-03 Blackwater Bend Pumped Storage Station (South Carolina, 780 MW); DEV-02 Tallow Creek Dam and Powerhouse (Georgia, 640 MW); DEV-04 Hollins Shoals Dam (Alabama, 420 MW; a city of about 38,000 lies 6 to 14 miles downstream). No single plant reaches 1,500 MW |
| Hazard potential (18 CFR 12.3(b)(13)) | 38 dams High, 14 Significant, 11 Low. Every licensed development with a High or Significant hazard dam is covered by the fleet Owner's Dam Safety Program (18 CFR 12.60) |
| FERC Security Groups | **Group 1: 4 dams** (DEV-01 upper dam, DEV-02, DEV-03 upper dam, DEV-04). **Group 2: 19 dams** (including PD-04 and PD-06). **Group 3: 40 dams.** Group criteria are not public (Security Program Rev. 3A, 3.3.1 to 3.3.3); assignments come from FERC D2SI letters and inspections |
| Operations model | The primary **Hydro Operations Center (HOC-A, north Georgia)** and the backup **HOC-B (western North Carolina, about 160 miles away)** remotely operate **35 developments (8,210 MW)** around the clock: unit dispatch, gate operations, and reservoir management. Two small legacy developments (18 MW) are run by local operators. The 9 Piedmont developments are run locally with after-hours remote access (gap 1) |
| Piedmont portfolio (acquisition) | **PD-01 to PD-09**, 9 developments (412 MW, 11 dams) in North Carolina and South Carolina, acquired from a private owner on 2025-10-01. PD-02 (96 MW), PD-04 Cane Mill Dam (112 MW), and PD-06 (84 MW) are BES generating plants; the other 6 are not BES. PD-04 and PD-06 are Security Group 2 dams; the other PD dams are Group 3. Integration onto the HOC and the enterprise OT network is due 2027-03-31 |
| NERC registration | **Generator Owner (GO) and Generator Operator (GOP)** on the NERC Compliance Registry. Regional Entity: SERC Reliability Corporation. Plants sit in the Balancing Authority Areas of two unaffiliated utilities, which also act as Transmission Operators. The company is not a Transmission Owner (its generator interconnection facilities are owned as GO) |
| BES status (NERC BES definition, Inclusion I2) | **34 developments are BES generating plants** (units over 20 MVA or plants over 75 MVA, connected at 100 kV or above), including PD-02, PD-04, and PD-06. **6 of them are Blackstart Resources** in the Transmission Operators' restoration plans. 12 developments are not BES |
| CIP impact rating (CIP-002-5.1a, last approved 2026-03-18) | **Medium impact with External Routable Connectivity:** the BES Cyber Systems at HOC-A and HOC-B, which perform Generator Operator obligations for more than 1,500 MW in the Eastern Interconnection (Attachment 1 criterion 2.11). **No high impact:** no plant reaches 1,500 MW (criterion 2.1), and no Planning Coordinator or Transmission Planner designation exists (2.3, 2.6), so criterion 1.4 is not met. **Low impact:** the 34 BES plants (criterion 3.3; the 6 Blackstart Resources also under 3.4). PD-02, PD-04, and PD-06 were added to the low impact list on 2026-01-15 |
| Not in CIP scope | Spillway gate controls and dam safety instrumentation are not BES Cyber Systems (they do not perform a BES reliability task), except where gate functions run inside the HOC fleet SCADA, which is inside the HOC Electronic Security Perimeter. They are protected under the FERC Security Program Section 9 and the company's OT security standard (STD-01.8) |
| CIP-014-3 | Does not apply: it reaches Transmission Owners and Transmission Operators only |
| CIP-012-2 | Applies: the company is a GOP that operates Control Centers. Real-time data moves between HOC-A and HOC-B and from both to the two Balancing Authorities and Transmission Operators over ICCP |
| Workforce | **12,000 employees:** 4,300 generation operations (HOC operators, plant operators, mechanics, electricians, I&C technicians); 3,600 Hydro Services (contract operations, field maintenance, engineering); 820 dam safety and civil engineering; 1,450 lands, recreation, and environmental (including about 900 seasonal); 380 corporate security (including security officers at Group 1 and 2 dams); 610 IT and OT technology (including the SOC and the OT security team); 840 corporate functions |
| Revenue | About **$4.8 billion** a year (fictional): energy and capacity sales $3.12B; ancillary services and pumped storage capacity $0.41B; renewable energy credits $0.12B; Hydro Services $0.86B (SL-1 contract operations $0.31B; field and engineering services $0.55B); SL-2 dam safety monitoring $0.09B; recreation, lands, and leases $0.20B. Generation is 76% of receipts, so NAICS 221111 is the primary industry. The SBA standard for NAICS 221111 is 750 employees (13 CFR 121.201), so the company is not small |
| Offtakers and market | Long-term power purchase and capacity agreements with 4 load-serving utilities (about 70% of energy), bilateral wholesale sales for the rest, and ancillary services (regulation, reserves, blackstart) under agreements with the two Balancing Authorities. Schedules and dispatch instructions arrive by ICCP and the scheduling platform |
| Federal contracts | None. Hydro Services works only for non-federal dam owners. FAR 52.204-21, 52.204-23, 52.204-25, and 52.204-30 do not apply |
| Sensitive data | CEII (18 CFR 388.113(c)(2)): inundation maps, design drawings, spillway and unit control details. Security documents marked "Privileged - Security Sensitive Material" (Security Program Rev. 3A 3.4.3.4 and 8.0): Vulnerability Assessments, Security Assessments, Security Plans, certification letters. BES Cyber System Information (BCSI, CIP-011-3) for the HOCs and low impact plants. Client CEII and instrument data held by SL-1 and SL-2. Employee personal information (12,000 employees) and recreation customer contact data (card payments use the reservation vendor's hosted page, so no card data is stored). No PCII has been submitted |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; medium and low impact NERC CIP programs, including CIP-012 and CIP-013; Group 1 Vulnerability Assessments and Rapid Recovery; two service lines offered to external clients (SOC 2); growth by acquisition |
| Not in scope | CIP-014 (not a TO); NRC, TSA, and SDWA regimes (no reactors, pipelines, or water systems); HIPAA (no such data); FAR clauses (no federal contracts). CIRCIA reporting is not in effect (final rule not published as of 2026-09-25) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board: audit committee; safety, risk, and reliability committee | Audit committee: Internal Audit, SOX, disclosure controls. Safety, risk, and reliability committee: dam safety, cyber and physical security, NERC compliance, risk appetite (Item 106 governance) |
| Chief Executive Officer; Chief Financial Officer | Jointly accept Very High risks; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer | Business owner for generation and dam operations; authorizing official (equivalent) for the Hydro Fleet Control and Dam Monitoring System (P02) |
| Senior Vice President, Hydro Operations | **CIP Senior Manager** (CIP-003-9 R3; identified by name in the record, title only here) |
| Vice President, Dam Safety (Chief Dam Safety Engineer) | Licensed professional engineer designated under 18 CFR 12.62(a); owns the Owner's Dam Safety Program, the 46 EAPs, instrumentation, and 18 CFR 12.10 reports; business owner of AI-001 |
| Chief Information Security Officer (CISO) | Program owner for IT and OT security; reports to the CIO with a direct line to the safety, risk, and reliability committee |
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Compliance Officer | Second-line compliance, including the NERC compliance program and FERC dam security compliance |
| General Counsel | Chairs the disclosure committee; privilege; regulator correspondence |
| Chief Audit Executive | Heads Internal Audit (in-house, with a co-sourced OT specialist firm); reports functionally to the audit committee; leads the P07 assessment |
| Vice President, Corporate Security | **FERC primary security contact** for the fleet (Security Program Rev. 3A, 3.2), with each plant manager as alternate contact for that project; physical security, security officers, PACS |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |
| GRC team (10), NERC compliance team (9), Security Operations Center (24x7, in-house, IT and OT), OT security team (22), Internal Audit | Three lines model |
| Senior Vice President, Hydro Operations organization: Director, Hydro Operations Center; Director, Hydro Control Systems Engineering; plant managers | HOC operations and local control; SCADA, PLC, and gate logic, baselines, backups, and OT change control (HFCDMS system administrator) |
| CISO organization: Director of Security Operations; Director, OT Security; Director, OT Network Engineering; Director of Network Engineering | SOC; OT security team, OT identity domain, OT PAM, Intermediate Systems; OT WAN and firewalls; corporate network |
| Director, NERC Compliance (under the Chief Compliance Officer) | NERC compliance team; CIP evidence; CIP-008, EOP-004, and DOE-417 reporting |
| CIO organization: Director of Identity and Access Management; Director of Cloud Platform Engineering | Enterprise identity platform; cloud landing zones (P04) |
| Director of Third-Party Risk Management | Vendor tiering, SOC report reviews, CIP-013-2 plan |
| Vice President, Integration Management Office | Piedmont integration (owner of the PD gaps until integration) |
| Vice President, Hydro Services; Vice President, Dam Safety Monitoring Services | SL-1 and SL-2 service line owners (P09) |
| Chief Human Resources Officer; Vice President, Facilities; Vice President, Lands and Recreation; Vice President, Corporate Communications; Vice President, Investor Relations | Personnel and training; facilities; recreation; public and investor communications |
| AI council (chaired by the Chief Risk Officer) | AI intake, tiering, and review (P10) |

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Fleet SCADA and generation control: SCADA servers, operator consoles, automatic generation control interface, ICCP servers, historian | On-premises at HOC-A and HOC-B | **Medium impact BES Cyber Systems** inside Electronic Security Perimeters. Also issues gate commands for the 35 HOC-operated developments |
| SYS-02 | Plant control systems: unit PLCs, digital governors, excitation systems, plant HMIs at 46 developments | On-premises OT at each plant | Low impact BES Cyber Systems at 34 BES plants. 64 plant HMIs run an operating system past vendor support |
| SYS-03 | Spillway and gate control: gate PLCs, local gate panels, hoists, standby generators at 41 gated dams | On-premises OT at each dam | Kept in a separate dam safety zone at each plant; not BES Cyber Systems. 9 gate control workstations run an unsupported operating system |
| SYS-04 | Dam safety instrumentation and early warning: automated data acquisition at 52 dams (about 3,900 instruments), 87 river and rain gauges, 126 EAP warning sirens at 18 dams | On-premises OT plus field devices | Sirens are activated from the HOC or locally. Readings flow one-way to SYS-12 |
| SYS-05 | OT wide-area network and OT DMZs: licensed microwave backbone, leased circuits from 2 carriers, plant gateway firewalls, HOC ESP firewalls, Intermediate Systems for Interactive Remote Access, OT PAM, OT file transfer, one-way data diodes at 21 plants | On-premises | All vendor and engineer remote access to OT is meant to pass through the Intermediate Systems. 19 plants depend on one carrier with no diverse path |
| SYS-06 | Piedmont legacy OT (PD-01 to PD-09): local SCADA and HMIs at each plant, legacy VPN concentrator, always-on vendor connections | On-premises at the PD plants | **Not yet integrated.** Shared operator accounts, password-only VPN, no OT monitoring (gap 1) |
| SYS-07 | Identity: enterprise identity platform (SSO, MFA, PAM, identity governance); separate OT identity domain with OT PAM | SaaS and on-premises | The OT domain does not trust the corporate domain |
| SYS-08 | Multi-cloud estate: Cloud provider A and Cloud provider B (vendor-agnostic) plus colocation Data Center 1 (Florida) and Data Center 2 (Georgia) | IaaS, PaaS | Cloud A: scheduling and trading platform, data platform, corporate workloads. Cloud B: SL-2 platform, AI and analytics platform, SL-1 client portal |
| SYS-09 | Enterprise network and endpoints: WAN to 14 offices and the administrative networks at 46 plants; about 13,500 endpoints | On-premises | EDR on all corporate endpoints |
| SYS-10 | ERP, payroll, and enterprise asset management (work orders, spare parts, maintenance history) | DC-1 and DC-2 | SOX IT general controls tested annually |
| SYS-11 | Energy scheduling, trading, and settlement platform | Cloud provider A | Day-ahead and real-time schedules to the Balancing Authorities; offtaker settlements |
| SYS-12 | Dam Safety Monitoring Service platform (DSMS) | Cloud provider B | Company-built. Collects and analyzes instrument data for the company's 52 instrumented dams and **138 client dams of 46 SL-2 clients**; includes the AI anomaly detection model (AI-001) |
| SYS-13 | Contract Operations platform (SL-1): Contract Operations Center (COC) in Georgia, separate from the HOCs; monitoring and operating consoles; client portal | COC on-premises; portal on Cloud provider B | Monitors and, on the owner's instruction, operates **27 non-BES plants of 11 clients** through client-owned VPN endpoints |
| SYS-14 | Security operations: SIEM, EDR, passive OT network sensors, vulnerability management | SaaS and on-premises | OT sensors cover HOC-A, HOC-B, the COC, and **11 of 35** HOC-operated plants |
| SYS-15 | Physical security systems: PACS for the HOCs (CIP-006 scope), cameras and intrusion detection at Group 1 and 2 dams, security dispatch | On-premises | Monitored 24x7 by the security dispatch desk at HOC-A |
| SYS-16 | Third parties with system or data access | Various | About 1,100 vendors; 240 with system or data access; 58 with remote access paths into OT (21 into CIP-scope systems, all through Intermediate Systems). One OEM services 60% of governors and exciters |
| SYS-17 | AI and analytics portfolio (11 use cases) | Cloud provider B and vendor SaaS | Governed by the AI council formed in 2025 (P10) |
| SYS-18 | Recreation reservations and public website | Vendor SaaS | 26 campgrounds and 140 boat ramps and day-use areas; vendor-hosted payment page |

**HOC-operated scope (used in P02):** the 35 HOC-operated developments have 125 of the 151 units, 48 of the 63 dams (4 Group 1, 17 Group 2, 27 Group 3), 36 of the 41 gated dams, automated instrumentation at 44 of the 52 instrumented dams, and 112 of the 126 sirens (at 16 of the 18 siren dams). 31 of them are BES plants. The Piedmont developments hold 22 units, 11 dams (PD-04 and PD-06 in Group 2), 4 gated dams, 6 instrumented dams, and 14 sirens at PD-04 and PD-06; the 2 legacy local developments hold 4 units and 4 Group 3 dams.

**SSP system (P02):** the *Hydro Fleet Control and Dam Monitoring System (HFCDMS)*: the fleet SCADA at HOC-A and HOC-B (SYS-01), the plant control systems (SYS-02), spillway and gate control (SYS-03), and dam safety instrumentation and early warning (SYS-04) at the 35 HOC-operated developments, and the OT WAN, DMZs, and Intermediate Systems that connect them (SYS-05), with interfaces to the DSMS (SYS-12), the scheduling platform (SYS-11), security operations (SYS-14), and the Balancing Authority and Transmission Operator control centers.

## 4. Current security posture: mature, with targeted gaps

**In place today:**
- A security program aligned to NIST CSF 2.0 for IT and OT, with NIST SP 800-82 Rev. 3 as the OT benchmark
- Medium and low impact CIP programs since 2016; CIP Senior Manager designated with documented delegations; last SERC compliance audit 2025-03 (2 findings, both mitigated by 2025-09)
- FERC Security Program documents for all 23 Group 1 and 2 dams: Vulnerability Assessments for the 4 Group 1 dams, Security Assessments for Group 2, Security Plans with a fleet Cyber/SCADA Security Plan for the HOC, and Annual Security Compliance Certification Letters every year
- An Owner's Dam Safety Program with a Chief Dam Safety Engineer; 46 EAPs tested annually; Part 12D independent consultant inspections on schedule; independent external audit of the ODSP in 2023 (18 CFR 12.65)
- Annual enterprise risk analysis tied to ERM (NIST IR 8286 Rev. 1); a policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 in-house SOC for IT and OT, with passive OT monitoring at both HOCs and the COC
- Privileged access management for IT and for the OT domain; Intermediate Systems with MFA for all Interactive Remote Access into the HOC ESPs
- Quarterly CIP access verification (CIP-004-7 R4.2) and quarterly access certification for other critical systems
- Immutable backups for cloud and data center workloads; offline SCADA backups at both HOCs
- Annual disaster recovery tests for tier-1 systems; annual HOC failover exercise; annual EAP functional exercises rotated across the fleet
- A tiered third-party risk program and a CIP-013 supply chain cyber security risk management plan
- SOC 2 Type 2 report for SL-1 contract operations every year since 2024
- Reg S-K Item 106 disclosure in the annual report on Form 10-K

**Targeted gaps found in the 2026 assessments:**
1. **Piedmont integration.** The 9 PD developments still use a password-only VPN, shared operator accounts, and always-on vendor connections, with no OT monitoring. At the 3 BES plants (PD-02, PD-04, PD-06) this means the CIP-003-9 Attachment 1 Section 3 and Section 6 controls (Section 6 in effect since 2026-04-01) are not in place: a potential noncompliance.
2. **Section 9 enhanced measures below the HOC.** Gate control at Group 1 and 2 dams is part of a Critical cyber system, but OT network monitoring covers only 11 of 35 HOC-operated plants, and 13 of 35 plants have not had an OT vulnerability assessment in the last 12 months.
3. **Legacy OT.** 64 plant HMIs and 9 gate control workstations run an unsupported operating system; PLC logic backups at 14 plants are more than 12 months old.
4. **Recovery.** The 2026-05-16 HOC failover took 3.4 hours against a 2-hour RTO; 19 plants depend on one telecom carrier.
5. **Third-party concentration.** One OEM provides remote service for 60% of governors and exciters; its 2025 contract renewal skipped the CIP-013 procurement terms.
6. **Group 1 documents.** The DEV-04 Vulnerability Assessment reprint (due 2026-03) is late, and the DEV-03 Security Plan exercise (5-year interval, last 2020-10) is overdue.
7. **Information handling.** HOC network diagrams (BCSI) were found in a project folder shared with an engineering contractor; PD inundation maps (CEII) sit in general file shares.
8. **Service lines.** SL-2 has no SOC 2 report; alert thresholds and model changes in the DSMS lack formal change control.
9. **Materiality.** The disclosure committee has 3 new members since 2026 and has never exercised an OT or dam safety scenario.
10. **AI.** 11 AI use cases; 7 have completed AI council review.
11. **Undocumented vendor paths (found by Internal Audit in 2026-08).** Three instrumentation vendors reached dataloggers at 5 dams over cellular modems that bypass the Intermediate Systems; the modems were disabled except during approved sessions on 2026-09-02.
12. **Two more potential CIP issues at the HOC level.** A contractor kept unescorted physical access to the HOC-B PSP for 31 hours after termination (CIP-004-7 R5.1), and the BCSI in item 7 was outside an authorized repository (CIP-011-3 R1.2). Both were self-reported with the Piedmont issues on 2026-09-30.
13. **Statement to FERC.** The 2025 certification letter reported PD-04 and PD-06 contact verification as complete when it was not; the correction goes to the Regional Engineer in 2026-10.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 | The HFCDMS (High impact by FIPS 199 model: integrity and availability High), inheriting common controls from the enterprise platform and the CIP program |
| P03 | Primary: FERC Security Program for Hydropower Projects, Revision 3A, for a fleet with Group 1, 2, and 3 dams. Also: 18 CFR Part 12; NERC CIP-002 to CIP-013 for a medium and low impact GO/GOP; EOP-004-4; SEC Item 1.05 and Item 106; state breach laws (Florida worked example) |
| P08 | Unauthorized access to spillway and turbine control systems, with the worked example at PD-04 through a vendor's always-on connection, including NERC CIP and FERC reporting, and an **SEC materiality assessment and 8-K Item 1.05** step |
| P09 | SOC 2 Type 2 readiness across two service lines offered to external clients: SL-1 contract remote operations and SL-2 dam safety monitoring |
| P10 | Enterprise AI portfolio (11 use cases) with the AI council operating model; full assessment of AI-001 dam-safety sensor anomaly detection |
| Cloud | Multi-cloud (vendor-agnostic) with common controls. OT is never hosted in the cloud; only one-way data leaves OT |
| Registry defaults | Kept: primary system (expanded to the fleet), incident type, and AI use case all fit the business at this size |

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2025-03-10 to 2025-03-21 | SERC CIP compliance audit (2 findings, mitigated by 2025-09) |
| 2025-10-01 | Piedmont portfolio acquisition closes |
| 2025-12-15 | 2025 Annual Security Compliance Certification Letters filed for 23 Group 1 and 2 dams |
| 2026-01-15 | PD-02, PD-04, and PD-06 added to the CIP-002 low impact list |
| 2026-02-24 | CIP-008-6 plan tabletop (HOC scenario) |
| 2026-04-01 | CIP-003-9 takes effect (low impact vendor electronic remote access, Attachment 1 Section 6) |
| 2026-05-16 | Annual HOC failover exercise (HOC-A to HOC-B): 3.4 hours against a 2-hour RTO |
| 2026-06-01 to 2026-07-31 | Enterprise BIA, risk analysis, and regulatory gap analysis; Section 9 determinations refreshed 2026-07-08 |
| 2026-07-14 to 2026-07-17 | Site walkthroughs at HOC-A, HOC-B, DEV-04, PD-04, and PD-06 |
| 2026-07-13 to 2026-08-28 | Control assessment by Internal Audit with the co-sourced OT specialist firm |
| 2026-08-14 | BIA approved |
| 2026-08-21 | Gap analysis approved |
| 2026-08-31 | Internal Audit reports the cellular datalogger paths to the CISO and the Vice President, Dam Safety |
| 2026-09-02 | Cellular datalogger modems disabled except during approved sessions |
| 2026-09-04 | Internal Audit report issued |
| 2026-09-08 | Executive risk committee approves the risk register and treatments |
| 2026-09-10 | Board safety, risk, and reliability committee and audit committee review; policies approved (effective 2026-10-01) |
| 2026-09-14 | SSP approved; conditional authorization by the COO |
| 2026-09-18 | Piedmont vendor connections disabled outside approved windows (interim) |
| 2026-09-30 | Self-reports to SERC (PD CIP-003-9 Sections 3.1 and 6; CIP-004-7 R5.1; CIP-011-3 R1.2); plan and schedule letters for PD-04 and PD-06 to the FERC Regional Engineer |
| 2026-11-18 | Disclosure committee tabletop with an OT and dam safety scenario |
| 2026-12-31 | 2026 Annual Security Compliance Certification Letters due (Security Program Rev. 3A, 8.0) |

# Scenario facts: Cris Santos Company | Government Services and Facilities | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Contract terms described here are fictional scenario choices unless a regulation is cited.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three operating divisions and corporate shared services. Each division is a separate wholly owned subsidiary that signs its own customer contracts |
| Division 1: Government Facilities Support (NAICS 561210), **focus of this scenario** | Operates and maintains government buildings: building engineering, HVAC and building automation, and electronic security (access control and video) support for federal, state, county, municipal, and education customers. About 13,000 employees |
| Division 2: Construction and Renovation (NAICS 236220, sector 23 Construction) | Builds and renovates public buildings (courthouses, office buildings, schools, and military facilities), mostly as design-builder or general contractor. About 6,500 employees and about 1,900 active subcontractors |
| Division 3: Janitorial and Security Services (NAICS 561720 and 561612, sector 56 Administrative and Support Services) | Custodial services and contract security officers at government and commercial buildings, remote video and alarm monitoring, and electronic security installation. About 23,500 employees, most of them hourly |
| Corporate shared services | Identity, network, security operations, cloud platform, the Integrated Building Operations Platform (section 3), HR, finance, legal, internal audit. About 2,000 employees |
| Location | Headquartered in Florida. Operations in 11 states and the District of Columbia. **State law handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional). Not small under the SBA standard for NAICS 561210 ($47.0 million; 13 CFR 121.201) |
| Sector context | Government Services and Facilities sector (co-Sector Risk Management Agencies: DHS and GSA, NSM-22). The group is a contractor to government facility owners, not a government entity |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23, 52.204-25 and DFARS 252.204-7019 and -7020) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. New DoD awards under DFARS Part 240 (DoD Class Deviation 2026-O0025, Revision 3) carry 252.240-7997 for DoD-led Medium and High NIST SP 800-171 assessments instead of 252.204-7019 and -7020. Sources: SRC-FAR-RFO-PART40 and SRC-DFARS-DEV-2026-O0025 |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks |
| Group CISO | Owns group security policy, the common control catalog, and the group SOC; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and the roll-up to enterprise risk management; co-accepts High risks; chairs the Group AI council |
| Group General Counsel | Contracts, notification decisions, public records questions |
| Group building technology director | System owner of the Integrated Building Operations Platform (SSP system) |
| Division presidents (3) | Accept Moderate risks for their divisions |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators and customer security terms |
| Construction CUI program manager | DFARS 252.204-7012 and CMMC program for the Construction division |
| Group internal audit | Assesses common controls once and samples division controls; reports to the board audit committee |
| Disclosure committee | SEC materiality of cybersecurity incidents |

## 3. Systems
| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate |
| SYS-G2 | Group SOC, SIEM, and EDR (24x7) | Corporate |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic) and corporate wide-area network | Corporate |
| SYS-G4 | Group ERP, human capital management, and payroll (SaaS) | Corporate |
| SYS-G5 | Integrated Building Operations Platform (IBOP): building automation supervision, physical access control administration, video and alarm monitoring, OT remote access, and site OT edge gateways for customer buildings | Corporate (Group Building Technology Services) |
| SYS-F1 | Computerized maintenance management system (CMMS) for all Facilities Support sites | Facilities Support |
| SYS-F2 | Agency-furnished access at federal buildings (agency building systems reached only through agency virtual desktops with PIV cards). **The agencies' systems, outside the group's boundary** | Facilities Support (use only) |
| SYS-C1 | Construction project management, document control, and BIM collaboration (commercial SaaS) | Construction |
| SYS-C2 | Construction CUI enclave (government community cloud tenant for DoD project data) | Construction |
| SYS-C3 | Jobsite technology: jobsite networks, temporary access control and cameras, equipment telematics | Construction |
| SYS-J1 | Workforce management: applicant tracking with AI screening, background screening portal, scheduling, time and attendance | Janitorial and Security |
| SYS-J2 | Security operations apps: guard tour and incident reporting app on rugged phones; body-worn cameras | Janitorial and Security |
| SYS-J3 | Electronic security installation records (customer system designs, as-built drawings, panel credentials) | Janitorial and Security |

**SSP system (P02):** the *Integrated Building Operations Platform (IBOP)*: a shared corporate system (SYS-G5) used by all three divisions, covering the cloud-hosted building automation supervision and access control administration services, the video and alarm monitoring module, the OT remote access service, the two Remote Operations Centers, and the company-managed site OT edge gateways, and inheriting common controls from SYS-G1 to SYS-G3.

The registry default primary system ("physical access control and building automation system") fits this size as the IBOP: at a multi-sector group the access control and building automation layers are run once as a shared platform rather than per contract. The registry incident (intrusion into building access control and automation systems) and AI use case (facial recognition for facility access) are used as given, extended to show their effect on all three divisions.

## 4. Current security posture: a defined group program, with gaps in scale and in the newer divisions
**In place today:**
- Group policies aligned to CSF 2.0, with the SP 800-53 Rev. 5 Moderate baseline as the group control set
- A common control catalog maintained by the Group CISO
- 24x7 group SOC with SIEM and EDR on all corporate and IBOP servers and workstations
- Privileged access management with phishing-resistant MFA for administrators of corporate and IBOP cloud systems
- Quarterly access certification for corporate systems and the Facilities Support division
- Immutable backups in a second cloud provider
- A PAM-brokered OT remote access service with session recording (deployed 2024) at most IBOP sites
- Building recovery (manual operation) procedures at every federal building and most state, local, and education sites
- A SOC 2 Type 1 report for the Facilities Support managed building technology service
- E-Verify enrollment across the group (FAR 52.222-54; Fla. Stat. 448.095)
- CMMC Level 1 self-assessment affirmed in SPRS for the Construction division's FCI systems
- SEC Reg S-K Item 106 disclosure in the annual report; a disclosure committee charter that covers cybersecurity

**Gaps:**
1. **Legacy OT remote access.** 37 IBOP sites that came with a 2024 regional acquisition still use vendor remote-support tools and integrator VPNs outside the PAM jump service. 22 integrator accounts have no MFA.
2. **Cross-tenant access control administration.** 41 group administrators hold a global administrator role across every customer's access control tenant, with no per-customer, just-in-time elevation.
3. **OT inventory and segmentation.** The reconciled OT asset inventory covers 231 of 296 IBOP sites. 19 county and school sites have building automation and door controllers on flat customer networks.
4. **OT logging.** IBOP edge gateway and access control administrator logs reach the group SIEM from 61% of sites. Supervisory server logs are kept 30 days locally.
5. **CUI in the Construction division.** DoD controlled building drawings sit in the commercial project collaboration SaaS (SYS-C1, not FedRAMP Moderate equivalent) and in the IBOP commissioning workspace. Enclave migration (SYS-C2) is 40% complete. The SP 800-171 Basic Assessment score in SPRS is 71 of 110, below the score needed for a conditional CMMC Level 2 status.
6. **Section 889 and FASCSA screening.** The group screening process covers Facilities Support and Construction purchasing, but not the electronic security installation business that the Janitorial and Security division acquired in 2023. Its own central monitoring station uses 4 network video recorders bought in 2019 whose manufacturer is unconfirmed.
7. **Workforce screening data.** Background check reports sit in the applicant tracking system with access for about 310 recruiters and branch managers, with no disposal schedule. Badges and keys at customer sites are returned or disabled about 4 days after a separation, at a 58% annual turnover rate.
8. **Division supplement drift.** The Janitorial and Security division still uses its 2022 pre-acquisition policy set. The Construction supplement has no CUI handling standard aligned to SP 800-171.
9. **Common control inheritance** is documented for the IBOP and Facilities Support, but not for the Construction CMMC system security plan or the Janitorial and Security division.
10. **Multi-party incident notification.** An IBOP incident can trigger notices under hundreds of customer contracts, an immediate report to GSA, a 72-hour DoD report, Florida third-party agent notices, and an SEC materiality decision. The group notification matrix has never been exercised across divisions, and contract notice terms are inventoried for 71% of contracts.
11. **AI governance.** The Group AI Standard was adopted in March 2026, after face verification at 3 county sites and video analytics in the monitoring center went live. The applicant screening tool has had no bias audit, and an estimating tool sends CUI drawings to an unauthorized cloud AI service.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Focus division and IBOP: NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline (binding by contract for state customers; benchmark elsewhere) plus FAR clauses. Construction: DFARS 252.204-7012, NIST SP 800-171 Rev. 2, and CMMC (32 CFR Part 170). Janitorial and Security: NIST CSF 2.0 as benchmark plus FCRA, the Disposal Rule, E-Verify, and FAR clauses. Regulation-by-division matrix |
| P08 | Intrusion into IBOP building access control and automation through a legacy remote-support tool, spanning all three divisions: customer contract notices, GSA, DoD, Florida third-party agent duties, and SEC materiality |
| P09 | SOC 2 scoped per division: Facilities Support managed building technology service (Type 2 readiness); Janitorial and Security remote monitoring service (first readiness); Construction and janitorial and guard services out of scope, with reasons |
| P10 | Group AI governance program: group standards, division use cases (face verification, video analytics, building automation optimization, applicant screening, estimating), and regulator-specific rules |
| Cloud | Shared corporate platform plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses and gap analyses (customer site walkthroughs 2026-06-08 to 2026-06-19) |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-09-15 | Results to the board risk committee; deliverables approved |

## 7. Facts added while building the deliverables (Phase 5)
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Legal entities | Cris Santos Facility Services, LLC (Facilities Support); Cris Santos Builders, LLC (Construction); Cris Santos Protective and Building Services, LLC (Janitorial and Security). Each signs its own customer contracts and makes its own FAR representations. Corporate shared services sit in the parent and serve the divisions under intercompany service agreements |
| Revenue split (fictional) | Facilities Support about $5.6 billion; Construction about $9.6 billion; Janitorial and Security about $2.8 billion. Total about $18.0 billion |
| Workforce split | Facilities Support 13,000; Construction 6,500; Janitorial and Security 23,500 (about 8,500 security officers, 13,600 custodial staff, 1,400 monitoring, installation, and branch staff); corporate 2,000. 410 Facilities Support staff hold agency-issued PIV cards for federal buildings |
| States | Florida (headquarters), Georgia, Alabama, South Carolina, North Carolina, Tennessee, Virginia, Maryland, Texas, Colorado, Arizona, and the District of Columbia. No operations in New York City |
| Facilities Support customers | 410 customer sites: 46 federal buildings (mostly GSA Public Buildings Service operations and maintenance contracts), 128 state agency facilities in 7 states, 164 county and municipal facilities, and 72 education facilities (school districts and 2 state universities). One state agency facility is a state revenue department office building where federal tax information (FTI) is processed; several county buildings house sheriff's offices and courts |
| IBOP scale | Hosts building automation supervision for 296 state, local, and education sites (about 41,000 BACnet controllers) and access control administration for 188 sites (about 9,800 doors and 212,000 cardholders, including about 38,000 students at one state university). Federal building automation stays on agency networks (SYS-F2). 2 Remote Operations Centers (ROC-1 in Florida, ROC-2 in Texas), staffed 24x7; ROC-2 also houses the Janitorial and Security central monitoring station. About 2,400 workforce users and about 180 integrator and subcontractor accounts. Company-managed OT edge gateways at all 296 sites. PAM jump service in use at 259 sites (37 acquired sites are the exception, gap 1) |
| IBOP commissioning workspace | Construction commissioning engineers stage building automation and access control programming and drawings in an IBOP workspace before turnover. It holds controlled drawings from 4 active DoD projects (CUI, covered defense information), which makes it a covered contractor information system under DFARS 252.204-7012 |
| Integrity rating decision | The IBOP integrity impact was rated Moderate, not High: life-safety functions (fire alarm, smoke control, egress door release) are hardwired and outside the platform; door and BACnet controllers enforce schedules locally; and customers keep security staff on site |
| Federal contract clauses | Facilities Support and Janitorial and Security federal contracts include FAR 52.204-21, -23, -25 (with 52.204-24/-26 representations), -30, 52.204-9, and 52.222-54. GSA building contracts incorporate the GSA Building Technologies Technical Reference Guide (BTTRG) v3.0 (May 2024). The Janitorial and Security division provides protective security officers at 22 federal buildings under contracts with the Federal Protective Service (DHS). Construction federal contracts include the same FAR clauses; its 6 active DoD contracts also include DFARS 252.204-7012, 252.204-7019, and 252.204-7020, and new DoD solicitations include 252.204-7021 (CMMC) |
| Construction CUI | 6 active DoD construction contracts (4 in the commissioning phase). CUI drawings live in SYS-C1 (commercial SaaS), the IBOP commissioning workspace, jobsite plan rooms (paper), and SYS-C2 (enclave, 40% migrated). SPRS Basic Assessment (self-assessment) of 71 of 110 posted 2025-11-14 for the Construction system security plan. 3 DoD bids planned after 2026-11-10 were expected to require CMMC Level 2 (C3PAO). The DoD (Department of War) CIO memorandum of 2026-07-13 suspended CMMC Phase 2, so during the suspension their requiring activities may require Level 1 (Self) or Level 2 (Self) instead, and SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies (DoD Class Deviation 2026-O0025, Revision 3, DFARS 240.371-5). The division keeps its C3PAO assessment as a voluntary choice. 7012 flow-down appeared in 9 of 24 sampled subcontracts that receive CUI |
| State and local contract terms | State agency contracts include a cybersecurity exhibit requiring NIST SP 800-53 Rev. 5 Moderate controls for contractor-managed systems that hold agency data (Florida worked example: Fla. Stat. 282.318(4)(h)), incident notice within 24 hours, and an annual independent assessment. County and municipal contracts require compliance with the customer's cybersecurity standards (Florida worked example: Fla. Stat. 282.3185(4)) and notice within 24 hours (12 hours under 9 county contracts). The state university contract designates the company a school official under 34 CFR 99.31(a)(1)(i)(B) for cardholder records, which the university treats as education records. One state customer's 2027 renewal requires GovRAMP verification of the IBOP by 2027-07-01. Public records clauses apply under Fla. Stat. 119.0701 |
| Contract notice inventory | Of about 1,450 active customer contracts across the group, 71% have their incident notice terms recorded in the contract management system. Commercial remote monitoring contracts require notice within 72 hours |
| Janitorial and Security details | Custodial services at about 1,100 sites; security officers at 260 sites (including courthouses, 22 federal buildings, and the state revenue department building); remote video and alarm monitoring for 640 sites (government and commercial); electronic security installation and service for about 900 customers. About 70,000 job applications a year. 6,200 rugged phones run the guard tour app; 900 body-worn cameras. Customer contracts at the revenue department building and at buildings housing criminal justice agencies require fingerprint-based checks and awareness training for staff with unescorted access |
| Section 889 inventory | The 2023 installation business acquisition brought records for about 1,310 cameras and 36 NVRs at commercial customer sites whose manufacturer is unconfirmed, plus 4 NVRs (2019) at the central monitoring station. No equipment of unconfirmed manufacturer is installed at a federal site under a federal contract (confirmed 2026-08-14) |
| AI inventory | AI-001 face verification at 3 county sites (1,150 enrolled employees, since 2026-01); AI-002 1:N face identification in public lobbies (requested by a county and a commercial monitoring customer; not approved); AI-003 video analytics in the monitoring center (640 sites); AI-004 building automation fault detection and HVAC optimization (advisory at 120 sites; closed-loop setpoint pilot at 6 county sites); AI-005 applicant screening and interview scheduling in Janitorial and Security hiring; AI-006 construction estimating and quantity takeoff assistant; AI-007 generative drafting of security officer incident reports; AI-008 enterprise generative AI assistant (pilot, 3,000 users); AI-009 meeting transcription for internal meetings. A Group AI council and Group AI Standard were established in 2026-03 |
| SOC 2 | Facilities Support managed building technology service: SOC 2 Type 1 as of 2025-12-31 (Security, Availability, Confidentiality); first Type 2 period 2026-01-01 to 2026-12-31. Janitorial and Security remote monitoring service: no report; 34 commercial customers and 2 county customers asked for one in 2026 |
| Cloud | Provider A (primary) hosts the corporate landing zone, the IBOP cloud services, SYS-G4 integrations, and division workloads. Provider B hosts the IBOP disaster recovery replica and the immutable backup vault. The access control and video management services in the IBOP are vendor SaaS tenants administered by the group. SYS-C2 is a government community cloud tenant from a third provider |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Life-safety and physical-security risks rated High at a customer building may not be accepted |
| Not in scope by fact | No group system processes FTI or criminal justice information; staff only work in buildings where they are stored (customer physical controls apply). No election systems (VVSG 2.0). No company system operates on behalf of a federal agency (FedRAMP and FISMA authorizations belong to the agencies). The group does not pay ransoms on behalf of public customers |
| P07 assessment details | Assessment plan approved 2026-06-30 by the Group CISO and the board audit committee chair. Samples: 75 joiner-mover-leaver events and 40 terminations across divisions; 25 Janitorial and Security separations at customer sites (keys recovered late for 11); 31 agency PIV card returns (7 late); 40 hire files and 25 reassignments to posts with fingerprint-check terms (3 started before the check was complete); 48 federated applications; 12 sites tested (4 acquired); 3 integrator-installed cellular modems found at acquired sites; OT sensors missing at 115 of 296 sites; 26 adjudicators need consumer report access; 17 of 22 sampled derivative shop drawings unmarked; visitors not always escorted at 3 of 6 DoD jobsites; 30 sampled installation purchases, none screened. The OT detection test used the controls engineering training lab at ROC-1. Critical exposure stop-and-notify on 2026-07-21 (an internet-reachable remote-support tool with a default password at an acquired school site, disabled within 24 hours) |
| POA&M estimates | Budgets and resource figures in the POA&M (for example the $1.4M remote access program and the $1.1M CMMC program) are fictional estimates |
| P08 contract and exercise details | The state university contract and the county monitoring contracts carry 24-hour incident notice terms. Two per-tenant break-glass administrator accounts are kept in PAM for emergency access control administration. A printed incident binder is kept at ROC-1, ROC-2, and each division command center. The P08 runbook scenario (64,000 cardholders, 6 county buildings, 37 masked doors, 2 DoD projects) is an exercise scenario, not a real event |
| P09 details | About 220 of the Janitorial and Security monitoring, installation, and branch staff work in the central monitoring station. The 2025 Type 1 description listed the 37 acquired sites as "in transition to the jump service"; management will describe the 2026 exception rather than carve the sites out. Customer data deletion at contract end is manual; no deletion certificates were issued for 2 contracts that ended in 2026. Target for the monitoring service: Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| P10 details | The Group AI council: Group Chief Risk Officer (chair), Group CISO, Group General Counsel, Group HR director, Group building technology director, and one delegate per division; it met on the priority use cases on 2026-08-27. AI-001 runs at employee entrances of 3 county government centers, all in Florida; signed consent exists at 2 of the 3 sites; template retention was indefinite until 2026-08 (64 departed employees' templates deleted). AI-002 decline letters sent 2026-09-10. The estimating service CUI uploads were found on 2026-07-14 during the P03 data mapping and reported to DoD through DIBNet on 2026-07-16; labeled CUI uploads to AI services are blocked since 2026-09-01. Officer attestation for AI-007 drafts was added in 2026-09. Monitoring metrics in P10 section 4 (for example AI-001 FNMR 1.9% over 61,400 attempts; AI-005 impact ratios from about 18,200 applications in 2026 Q2) are scenario results |

# Scenario facts: Cris Santos Company | Commercial Facilities | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; a taxable corporation that has not elected REIT status, so it operates its hotels and construction business directly. Tax structure is outside this sample) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary; corporate shared services sit in the parent |
| Division 1: Commercial Property (NAICS 531120), **focus of this scenario** | Cris Santos Properties, LLC. Owns and operates 142 office and retail properties (96 office buildings and campuses, 46 retail centers), about 48 million rentable square feet, about 2,600 commercial tenants, and about 236,000 active tenant badge holders. Also manages 34 buildings (about 11 million square feet) owned by 9 institutional investors under property management agreements. About 6,500 employees (property management, leasing, engineering, security operations). Guard services are contracted |
| Division 2: Construction and Tenant Build-Out (NAICS 236220, sector 23 Construction) | Cris Santos Builders, LLC. Commercial general contracting, construction management, and tenant improvement (build-out) work, about 22% of it in group properties. About 900 active projects. 118 federal awards (civilian and Department of Defense). Includes the **Building Technology Integration (BTI) unit** (about 650 employees), which installs building automation, access control, and video systems for clients and is the **integrator for the group's own buildings and hotels** under an intercompany services agreement. About 12,000 employees, including about 7,400 craft workers |
| Division 3: Hotels (NAICS 721110, sector 72 Accommodation and Food Services) | Cris Santos Hospitality, LLC. Owns and operates 88 full-service and select-service hotels (about 29,000 rooms) in 11 states under two group-owned brands. No franchisor: the group designs and runs its own hotel systems and its own PCI DSS program. About 23,000 employees |
| Corporate shared services | Identity, security operations, network and cloud platform, the Remote Building Operations Center, finance (ERP, accounts payable, treasury), HR, legal, and internal audit. About 3,500 employees |
| Location | Headquartered in Florida. Owned properties in 9 states, hotels in 11 states (including 2 hotels in California), and construction projects in 14 states. No operations in Colorado, Illinois, or New York. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional): Construction about $10.9 billion, Commercial Property about $3.7 billion, Hotels about $3.4 billion, after intercompany eliminations |
| Why this combination | Build, own, and operate. Construction builds out tenant space and installs building systems; Commercial Property owns and runs office and retail buildings; Hotels runs lodging on the same building-operations platform. All three depend on one group building automation and access control platform |
| Sector context | Commercial Facilities critical infrastructure sector (Real Estate, Retail, and Lodging subsectors). Sector Risk Management Agency: CISA. No mandatory federal cybersecurity rule applies to commercial facilities; the CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0, December 2025) are voluntary. Construction is not a CISA sector; its binding cyber rules come through federal contracts |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and enterprise risk oversight; accepts Very High risks; approves POL-01 and POL-03 |
| Board audit committee | Oversees group internal audit; receives P07 results |
| Disclosure committee | SEC materiality of cybersecurity incidents (Form 8-K Item 1.05); Reg S-K Item 106 disclosure |
| Group CISO | Group security program and policies; common controls (SYS-G1 to SYS-G3); co-accepts High risks |
| Group Chief Risk Officer | Group risk register and enterprise risk management roll-up; co-accepts High risks |
| Group Chief Privacy Officer | Data classification, biometric and video data rules, state privacy laws |
| Group General Counsel | Notification matrix, intercompany agreements, tenant and owner contract terms |
| Group OT security lead (reports to the Group CISO) | OT security standard (NIST SP 800-82 Rev. 3), OT segmentation and monitoring program |
| Group building technology director | System owner of the BAACS (SYS-G5); runs the Remote Building Operations Center (RBOC) |
| Division presidents (3) | Accept Moderate risks for their divisions. The Construction division president is the CMMC Affirming Official for Cris Santos Builders, LLC |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators and customers; accept Low risks |
| Commercial Property director of security operations | Lobby security, badge issuance, video surveillance operations, guard contractor |
| Commercial Property regional chief engineers (6) | Building automation operation, manual plant operation, engineering staff |
| Commercial Property controller | PCI DSS (SAQ P2PE) for the division's card acceptance |
| Construction director of federal contracts compliance | FAR and DFARS clause compliance, CMMC scoping, SPRS entries |
| BTI unit general manager | Integrator services for group and client buildings; Section 889 product screening |
| Hotels payment security lead | Hotels PCI DSS program and the annual Report on Compliance |
| Group internal audit | Reports to the board audit committee. Assesses common controls once and samples division controls. Independent of the teams it assesses |

## 3. Systems
| ID | System | Owner | Holds |
|---|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate | Identities |
| SYS-G2 | Group SOC: SIEM, EDR, email security, 24x7 monitoring, passive OT network monitoring sensors (partly deployed) | Corporate | Security logs |
| SYS-G3 | Group cloud platform (landing zone on provider A; disaster recovery and backup vault on provider B) and the group WAN connecting every property, hotel, and office | Corporate | All corporate and division cloud workloads |
| SYS-G4 | Group ERP and treasury (accounting, accounts payable, payroll interface, bank connectivity) | Corporate finance | Financial data; employee and vendor bank details |
| SYS-G5 | **Group Building Automation and Access Control System (BAACS)**: central BAS supervisor and historian, site supervisory controllers and BAS field controllers, enterprise access control and video platform, RBOC workstations, integrator remote access path | Corporate (Group building technology director) | Badge holder data (names, employers, badge photos, credential numbers, access history); video; face templates for the verification pilot; building operational data and drawings |
| SYS-D1 | Property management and lease accounting platform (vendor SaaS): leases, tenant billing, ACH rent, work orders, owner reporting for managed buildings | Commercial Property | Tenant contacts and bank details; investor owners' financial data |
| SYS-D2 | Tenant experience app and visitor management (vendor SaaS): mobile credentials, visitor registration, lobby kiosks that scan government IDs | Commercial Property | Visitor names, photos, and ID numbers |
| SYS-D3 | Construction project delivery platform (project management SaaS, BIM/CAD collaboration, field tablets) | Construction | Federal contract information (FCI); client drawings |
| SYS-D4 | Construction CUI enclave: a FedRAMP Moderate authorized government-community cloud environment for DoD work | Construction | Controlled unclassified information (CUI) for 9 DoD contracts |
| SYS-D5 | BTI integrator tools: remote access tool, configuration repository, and credential vault for group and client building systems | Construction (BTI unit) | Building system configurations, controller programs, drawings, and credentials |
| SYS-D6 | Hotels property management system (cloud PMS), central reservation system, booking engine, loyalty and guest CRM | Hotels | Guest PII, stay history, loyalty profiles, tokenized cards |
| SYS-D7 | Hotels payment environment (cardholder data environment): front desk payment terminals, restaurant and bar POS, payment gateway integration | Hotels | Card data |
| SYS-D8 | Hotels guest room electronic lock systems, guest Wi-Fi, and in-room entertainment | Hotels | Key encoding data; guest device identifiers |

**SSP system (P02):** the *Group Building Automation and Access Control System (BAACS)*: the shared corporate building systems platform (SYS-G5) that runs HVAC, lighting, and metering control and physical access control and video at 142 owned properties, 88 hotels, and 34 managed buildings, operated from the Remote Building Operations Center, serviced by the Construction division's BTI unit, and inheriting common controls from SYS-G1 to SYS-G3.

**Why the registry defaults were kept.** The registry's primary system (building automation and access control), incident (ransomware on building automation systems), and AI use case (video analytics for building access) all fit this group. At this size the system is a shared corporate platform used by all three divisions, so the SSP covers the group platform rather than one property's systems, and the incident and AI work are widened to the group program.

## 4. Current security posture: a defined program, mature in corporate IT, with OT and cross-division gaps
**In place today:**
- Group policies aligned to NIST CSF 2.0, with division supplements
- A common control catalog maintained by the Group CISO's office
- 24x7 group SOC with EDR on all managed IT endpoints and servers
- MFA for all workforce users; phishing-resistant MFA and just-in-time privileged access for administrators
- Immutable backups of corporate and cloud workloads in a separate cloud provider
- An OT security standard based on NIST SP 800-82 Rev. 3 (adopted 2025), applied to all new buildings and renovations
- A central BAS supervisor in the group cloud and an enterprise access control and video platform whose vendor provides a SOC 2 Type 2 report
- Commercial Property card acceptance only through validated PCI-listed P2PE terminals (annual SAQ P2PE)
- Hotels: annual PCI DSS Report on Compliance (2025 report signed by the QSA with a compliant result)
- Construction: CMMC Level 1 (Self) for the project delivery platform and Level 2 (Self) for the CUI enclave, both affirmed in SPRS
- Reg S-K Item 106 disclosure in the 2025 annual report
- Cyber insurance with a breach response panel

**Gaps:**
1. **OT segmentation and remote access.** BAACS network segmentation to the OT standard is complete at 61 of 142 owned properties and 19 of 88 hotels. At the rest, site supervisors, door controllers, and video recorders share networks with building IT. The BTI unit's central remote access gateway (named accounts, MFA, approval, recording) carries most integrator sessions, but legacy always-on vendor remote-support tools remain on site supervisors at 47 sites, with shared accounts.
2. **OT visibility.** The OT asset inventory is about 74% complete. Passive OT monitoring sensors are deployed at 38 sites. Site supervisor and door controller logs are not sent to the group SIEM.
3. **BAS recovery at scale.** The central BAS supervisor is backed up immutably. Site supervisor configurations and field controller programs for about 40% of sites exist only in the BTI configuration repository (SYS-D5), outside group backup. A multi-site restore has never been tested, and manual operating procedures exist at only some properties and hotels.
4. **Intercompany integrator risk.** The BTI unit is the integrator for the group's own buildings under a 2021 intercompany services agreement with no security terms. BTI tools (SYS-D5) are run by the Construction division to its own standard, not the group OT standard, and BTI technicians hold standing credentials to group sites.
5. **Hotels PCI scope.** 14 hotels acquired in 2025 still run a legacy on-premises PMS that displays full card numbers, and the 2025 segmentation tests failed at 6 hotels. The QSA noted both as risks to the 2026 assessment.
6. **AI and biometrics.** The access control and video vendor enabled tailgating detection at 23 office properties, and a face verification pilot runs at the turnstiles of 2 office towers. A BAS optimization service writes setpoints automatically at 41 buildings. The Group AI Standard (adopted 2026-03) has not yet been applied to vendor-enabled features.
7. **Cross-division incident notification.** A BAACS incident could trigger SEC disclosure, state breach notices, tenant lease notices, managed-property owner notices, DoD reporting if CUI is involved, and acquirer notices. The group notification matrix has not been exercised across divisions.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | One shared corporate system (the BAACS, SYS-G5) with a group common control catalog |
| P03 | Focus division (Commercial Property): CISA CPG 2.0, all 34 goals, tailored for OT with NIST SP 800-82 Rev. 3, plus PCI DSS v4.0.1 SAQ P2PE and the legal baseline. Construction: FAR 52.204-21, CMMC (32 CFR Part 170), FAR 52.204-25, DFARS 252.204-7012. Hotels: PCI DSS v4.0.1 (Report on Compliance) plus FTC rules. Group-wide: SEC, CCPA/CPRA, state breach laws, CIRCIA (pending), OFAC. Regulation-by-division matrix |
| P08 | Ransomware on building automation systems, entering through a legacy integrator remote-support tool and spanning all three divisions: a multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 scoped per division: Commercial Property's third-party property management and remote building operations service line is in scope; Construction and Hotels are out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the rules that apply to each (video analytics and face verification for building access is the priority use case) |
| Cloud | Shared corporate platform (provider A primary, provider B for recovery) plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses and gap analyses (site walkthroughs at 12 properties, 6 hotels, and 4 jobsites, 2026-06-08 to 2026-06-26) |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-09-15 | Results to the board risk committee; deliverables approved |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Life-safety risks rated High may not be accepted |

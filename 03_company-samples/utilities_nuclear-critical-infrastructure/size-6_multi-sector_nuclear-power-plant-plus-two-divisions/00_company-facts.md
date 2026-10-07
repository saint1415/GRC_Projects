# Scenario facts: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; holding company with three operating divisions) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary |
| Division 1: Nuclear Generation (NAICS 221113), **focus of this scenario** | Owns and operates 3 nuclear generating stations with 5 pressurized water reactor units, about 5,700 MW net. Each unit holds a 10 CFR Part 50 operating license. Each station has an independent spent fuel storage installation (ISFSI) under the Part 72 general license. Sells power at wholesale and under long-term contracts. Registered with NERC as a Generator Owner and Generator Operator. About 5,400 employees, plus about 2,500 contractors on site during each refueling outage |
| Division 2: Nuclear Engineering and Radiation Services (NAICS 541330, sector 54 Professional, Scientific, and Technical Services) | Design and modification engineering, cyber security and physical security engineering for reactor licensees (the group's own stations and 14 external utilities), outage health physics and craft staffing, an NVLAP-accredited personnel dosimetry service, and engineering under U.S. Department of Energy (DOE) contracts. About 16,800 employees |
| Division 3: Radioactive Waste Management (NAICS 562211, sector 56 Administrative and Support and Waste Management and Remediation Services) | Two low-level radioactive waste (LLRW) processing facilities (one in Florida, one in another southeastern Agreement State), a hazmat transport fleet, decommissioning and radwaste services at reactor sites, and an environmental remediation contract at a DOE site. About 17,800 employees |
| Corporate shared services | Identity, network, security operations, cloud platform, finance, HR, legal, internal audit. About 5,000 employees |
| Location | Headquartered in Florida. Station A is in Florida; Stations B and C are in two other southeastern states. Engineering, dosimetry, and field services work in about 30 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| SBA status | Not small. SBA standard for NAICS 221113 is 1,150 employees (13 CFR 121.201); every division also exceeds its own standard |

### Regulatory driver IDs used in this sample
The vertical's `requirements.csv` lists C-NUCLEAR-R01 to R05. The other two divisions use the IDs in `02_industry-rules/professional-services/requirements.csv` (N54-) and `02_industry-rules/admin-support-services/requirements.csv` (N56-). For binding rules that neither file lists, this sample adds **scenario-level driver IDs (C-NUCLEAR-S01 to S12)**. They are defined here and nowhere else. Each was read on the eCFR (version date 2026-09-23) or the cited primary source.

| ID | Requirement | Citation | Applies to |
|---|---|---|---|
| C-NUCLEAR-R01 | NRC cyber security rule for power reactors | 10 CFR 73.54, with RG 5.71 Rev. 1 (February 2023) | Nuclear Generation (all 5 units). **Primary regulation in P03** |
| C-NUCLEAR-R02 | Part 53 cybersecurity rule | 10 CFR 73.110 | Not applicable (no Part 53 license) |
| C-NUCLEAR-R03 | NRC cyber security event notifications | 10 CFR 73.77 | Nuclear Generation |
| C-NUCLEAR-R04 | NERC CIP Reliability Standards | 16 U.S.C. 824o; 18 CFR Part 40; CIP-002-5.1a, CIP-003-9, CIP-004 to CIP-014 | Nuclear Generation, for systems outside the NRC cyber security plans (section 7) |
| C-NUCLEAR-R05 | CIRCIA (proposed only) | Proposed 6 CFR Part 226 | Not in effect |
| C-NUCLEAR-S01 | Protection of Safeguards Information (SGI) | 10 CFR 73.21, 73.22 | Nuclear Generation (licensee); Engineering and Radiation Services (a person who receives SGI related to power reactors, 73.21(a)(1)) |
| C-NUCLEAR-S02 | Access authorization program, including people who can act by electronic means | 10 CFR 73.56 | Nuclear Generation (licensee program); Engineering and Radiation Services (contractor/vendor program accepted by licensees, 73.56(a)(4)) |
| C-NUCLEAR-S03 | Safety/security interface and security program reviews | 10 CFR 73.58; 73.55(m) | Nuclear Generation |
| C-NUCLEAR-S04 | Maintenance Rule | 10 CFR 50.65 | Nuclear Generation (P10) |
| C-NUCLEAR-S05 | Immediate notifications and the Emergency Response Data System | 10 CFR 50.72(a) | Nuclear Generation |
| C-NUCLEAR-S06 | Physical protection of category 1 and 2 quantities, including security-related information | 10 CFR Part 37, applied through Agreement State license conditions (Florida: standard license condition, ADAMS ML23178A117) | Radioactive Waste Management (Florida facility sealed source vault) |
| C-NUCLEAR-S07 | RCRA permitted facility operating record and records retention | 40 CFR 264.73, 264.74, through EPA-authorized state programs | Radioactive Waste Management (mixed waste) |
| C-NUCLEAR-S08 | Personnel dosimetry processing and individual monitoring records | 10 CFR 20.1501(d) (NVLAP-accredited processor); 20.2106 (customer licensees' records) | Engineering and Radiation Services (dosimetry service) |
| C-NUCLEAR-S09 | Assistance to foreign atomic energy activities | 10 CFR Part 810 (DOE), scope in 810.2 | Engineering and Radiation Services |
| C-NUCLEAR-S10 | SEC cybersecurity disclosure | Form 8-K Item 1.05; Regulation S-K Item 106 | Group |
| C-NUCLEAR-S11 | State breach notification | Each state where affected residents live; Fla. Stat. 501.171 as the worked example | All divisions |
| C-NUCLEAR-S12 | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 | Voluntary benchmark | Radioactive Waste Management OT and security systems |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks |
| Board audit committee | Oversees group internal audit |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3) |
| Group Chief Risk Officer | Group risk register and ERM roll-up; co-accepts High risks with the Group CISO |
| Group General Counsel | Notification matrix, contracts, legal privilege during incidents |
| Disclosure committee | SEC materiality decisions |
| Group internal audit | Assesses common controls once; samples division controls (P07); independent of the teams it assesses |
| Chief Nuclear Officer (Nuclear Generation president) | Accepts Moderate risks for Nuclear Generation; executive owner of the three NRC cyber security plans |
| Site vice presidents (3) and plant managers (3) | Station operation; receive 73.55(m) program review reports |
| Fleet cyber security program manager | Owns the three cyber security plans (CSPs) and the fleet cyber security team (CST) described in RG 5.71 |
| Fleet security director | Physical protection program, SGI program for Nuclear Generation, 73.77 and 73.1200 reporting procedures |
| Fleet IT director | Plant business networks and endpoints; **system owner of the P02 system** |
| Work management director | Business owner of the fleet work management system |
| Nuclear Generation security and compliance lead | Division register, division supplement, NERC CIP compliance coordination |
| CIP Senior Manager | Named under CIP-003 for the division's NERC CIP program |
| Nuclear Oversight (fleet quality assurance) manager | Performs the independent 24-month security program reviews that include cyber (73.55(m)(1)(iii)) |
| Maintenance Rule coordinator (each station) | Owns 50.65 monitoring; business co-owner of the predictive maintenance pilot (P10) |
| Engineering and Radiation Services president | Accepts Moderate risks for the division |
| Engineering and Radiation Services security and compliance lead | Division register and supplement; FAR clause compliance for DOE work |
| SGI program manager (Engineering and Radiation Services) | Need-to-know determinations, SGI access list, stand-alone SGI systems |
| Contractor/vendor access authorization program manager | The division's 73.56 contractor/vendor program for outage workers |
| Dosimetry laboratory director | NVLAP accreditation; business owner of the dosimetry service |
| Export control officer | Part 810 and Part 110 determinations |
| Radioactive Waste Management president | Accepts Moderate risks for the division |
| Radioactive Waste Management security and compliance lead | Division register and supplement |
| Radiation Safety Officers (one per facility license) and Part 37 reviewing officials | Part 37 programs and access authorization at the Florida vault |
| Transportation security manager | DOT hazmat security plan (49 CFR 172.800-172.804) |

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate | Federates every division's business systems |
| SYS-G2 | Group SOC, SIEM, and EDR | Corporate | 24x7. Does **not** monitor CDAs; each station's CST monitors CDAs inside the CSP boundary |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic), wide-area network, and remote access service | Corporate | Provider A primary, provider B for disaster recovery and the backup vault |
| SYS-G4 | ERP, HR, and payroll (SaaS) | Corporate | |
| SYS-N1 | Plant business networks at Stations A, B, and C (site LANs, Wi-Fi, about 6,200 endpoints, file and print services, and each site's business DMZ with the plant data replica servers that receive one-way data from Level 3) | Nuclear Generation | In the P02 boundary |
| SYS-N2 | Fleet work management system (enterprise asset management with work orders, clearance and tagging, outage scheduling, and the interface to the corrective action program) | Nuclear Generation | Hosted on the group cloud platform (provider A). About 7,300 active users. In the P02 boundary |
| SYS-N3 | Corrective action program (CAP) system | Nuclear Generation | SaaS; interconnected |
| SYS-N4 | CDA networks at each station (defensive Levels 3 and 4): safety-related and important-to-safety I&C, plant process computers, balance-of-plant DCS, radiation monitoring, emergency preparedness systems including ERDS links | Nuclear Generation | Protected under each station's NRC-approved CSP; about 4,800 CDAs fleet-wide; outside the P02 boundary |
| SYS-N5 | Security systems (PACS, alarm stations, security communications) | Nuclear Generation | CDAs on an isolated security network; outside the P02 boundary |
| SYS-N6 | Portable media and mobile device (PMMD) scanning kiosks (9, three per station) and the kiosk update server | Nuclear Generation | Kiosks are CSP security controls for moving data to higher levels (RG 5.71 B.1.19). The update server sits on the plant business network |
| SYS-N7 | Fleet operations center (Generator Operator dispatch and telemetry for all 5 units) | Nuclear Generation | NERC CIP medium impact BES Cyber System (section 7) |
| SYS-N8 | SGI stand-alone systems (Nuclear Generation security organization) | Nuclear Generation | 73.22(g) stand-alone computers |
| SYS-N9 | Predictive maintenance analytics service | Nuclear Generation | Vendor SaaS analytics fed from the plant data replica (P10) |
| SYS-E1 | Engineering document management and collaboration (CAD, calculations, project shares) | Engineering and Radiation Services | Holds client engineering data, Part 810 controlled technology, and outage project files |
| SYS-E2 | SGI stand-alone systems at 4 engineering offices | Engineering and Radiation Services | 73.22(g) |
| SYS-E3 | Dosimetry laboratory information system and customer portal | Engineering and Radiation Services | About 2,100 customer licensees and 310,000 monitored individuals; about 5,800 customer portal users |
| SYS-E4 | Federal projects enclave (DOE contract work holding Federal Contract Information) | Engineering and Radiation Services | |
| SYS-W1 | Waste tracking, manifest, and customer portal | Radioactive Waste Management | Vendor SaaS configured by the division; e-Manifest interface |
| SYS-W2 | Processing facility OT at both facilities (PLCs, HMIs, historians) | Radioactive Waste Management | |
| SYS-W3 | Florida facility vault security systems (intrusion detection, PACS, video) | Radioactive Waste Management | Part 37 category 2 vault |
| SYS-W4 | Transport fleet telematics and shipment tracking | Radioactive Waste Management | About 120 tractors |

**SSP system (P02):** the *Plant Business Network and Work Management System (PBN-WMS)*: the plant business networks at the three stations (SYS-N1, including each site's business DMZ and the plant data replica servers) and the fleet work management system (SYS-N2), inheriting common controls from SYS-G1 to SYS-G3; all CDAs, the security network, and the PMMD kiosks are outside the boundary.

## 4. Current security posture: varies by division
Nuclear Generation has a mature, NRC-inspected program for its CDAs and a defined program elsewhere. The two service divisions are partially compliant. Most gaps sit where the divisions share people, identities, and information.

**In place today:**
- Group policies aligned to NIST CSF 2.0 and a common control catalog
- 24x7 group SOC with EDR on all business endpoints and servers
- PAM with just-in-time elevation; quarterly access certification for group systems
- Immutable backups in a separate provider account
- NRC-approved cyber security plans at all 3 stations (NEI 08-09 based), fully implemented; one-way deterministic devices between Level 3 and the plant business networks; a CST at each station
- 24-month security program reviews by Nuclear Oversight that include the cyber security program (73.55(m)); no open NRC cyber security inspection findings
- Access authorization programs under 73.56 (licensee program in Nuclear Generation; contractor/vendor program in Engineering and Radiation Services)
- SGI programs with stand-alone systems in Nuclear Generation and Engineering and Radiation Services
- NERC CIP program for the fleet operations center (medium impact) and low impact assets
- Part 37 program and DOT security plan in Radioactive Waste Management
- NVLAP accreditation for the dosimetry laboratory
- SEC Regulation S-K Item 106 disclosure in the annual report

**Gaps (found in the 2026 assessments):**
1. **Cross-division access to the station business networks.** About 1,900 Engineering and Radiation Services and Radioactive Waste Management staff hold standing plant business network and work management accounts through SYS-G1. During outages they connect division-managed laptops to the station networks with no station device check. Accounts are removed a median of 46 days after the outage assignment ends.
2. **CDA-related information in the work management system.** CDA work packages (CDA identifiers, firmware versions, network details) are readable by all about 7,300 work management users. There is no "cyber security sensitive" label, and screening of attachments for SGI is manual.
3. **PMMD kiosk update path.** The 9 kiosks receive signature and software updates from a server on the plant business network. Integrity checking of update packages is not documented, and 2 of the 3 kiosks at Station B run an operating system past end of support.
4. **SGI handling in Engineering and Radiation Services.** Need-to-know determinations are not documented for 31 contractor engineers; the SGI access list has not been reconciled since 2025-Q3; one office used a networked scanner to copy SGI documents.
5. **Contractor/vendor access authorization files.** Personal information for about 2,900 outage workers sits in engineering project shares readable by project teams (73.56(m)).
6. **Dosimetry customer portal.** Customer administrator accounts sign in with a password only. Three large customers have asked for a SOC 2 report.
7. **Waste facility security systems and OT.** At the Florida facility the vault PACS and intrusion detection still share the facility business network with no alternate path (37.49(c)); the other facility's security network was separated in 2025. Vendor remote access to processing PLCs at the Florida facility has no MFA.
8. **Cross-division notification.** Nuclear Generation has 73.77 procedures, but the group matrix does not show that notifying the FBI starts a 4-hour NRC clock (73.77(a)(2)(iii)), and does not cover CIP-008, Agreement State Part 37 reports, client and dosimetry customer contract notices, or SEC timing together. It has never been exercised across divisions.
9. **Common control inheritance and policy drift.** Inheritance is documented for Nuclear Generation and Engineering and Radiation Services, not for Radioactive Waste Management; that division's supplement was last aligned in 2024.
10. **AI governance.** A predictive maintenance pilot in Nuclear Generation covers balance-of-plant equipment, some of it in Maintenance Rule scope because its failure could cause a reactor trip (50.65(b)(2)(iii)). Model alerts create work requests automatically. The pilot was not reviewed under the Maintenance Rule program or the 73.58 safety/security interface process. Engineering staff also use a generative AI assistant without quality assurance program rules.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 regulation | Nuclear Generation: 10 CFR 73.54 with RG 5.71 Rev. 1, plus 73.77, SGI, 73.56, 73.58, and NERC CIP for the fleet operations center. Engineering and Radiation Services: SGI (73.21-73.22), 73.56 contractor/vendor duties, FAR 52.204-21, dosimetry records. Radioactive Waste Management: Part 37 by license condition, DOT security plans, RCRA records, CSF 2.0 OT benchmark. Group: SEC, state breach law, CIRCIA status |
| P08 incident | Cyber attack on the Station A business network with an attempted pivot to digital assets (through the PMMD kiosk update path), entering through a phished Engineering and Radiation Services engineer and touching all three divisions |
| P09 SOC 2 | Scoped per division: the dosimetry service (Engineering and Radiation Services) and the waste customer portal (Radioactive Waste Management) are in scope; Nuclear Generation is out of scope, with reasons |
| P10 AI | Group AI governance program; priority use case: predictive maintenance for non-safety plant equipment (Nuclear Generation) |
| Cloud | Shared corporate platform plus division workloads, vendor-agnostic. No CDA and no SGI is hosted in the cloud |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division BIAs, risk analyses, and gap analyses (Station A walkthrough 2026-06-16) |
| 2026-06-29 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-09-17 | Results to the board risk committee; deliverables approved |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Stations | Station A (Florida): 2 units, about 2,300 MW. Station B: 2 units, about 2,250 MW. Station C: 1 unit, about 1,150 MW. All in one Interconnection. Refueling outages every 18 months per unit, about 3 a year fleet-wide |
| Cyber security plans | Each station's CSP was approved by license amendment and fully implemented in 2017. Each defines defensive Levels 0 to 4 per the RG 5.71 defensive architecture: CDAs at Levels 3 and 4, one-way data flow from Level 4 to Level 3 and from Level 3 to Level 2, and the plant business network at Level 2 and below. CSP deficiencies are entered in the station CAP within 24 hours (73.77(b)(1)) |
| NRC-NERC boundary | Per CIP-002-5.1a section 4.2.3.3, systems regulated under a 73.54 CSP are exempt from CIP-002. Since the Commission's 2010 balance-of-plant decision (SRM-COMWCO-10-0001, cited in RG 5.71 Rev. 1), balance-of-plant digital assets with a nexus to radiological health and safety are in the CSPs. The division's NERC CIP scope is the fleet operations center (medium impact under CIP-002-5.1a Attachment 1 criterion 2.11: Generator Operator control center for more than 1,500 MW in one Interconnection) and low impact BES Cyber Systems at each station's generator interconnection that the boundary analysis left outside the CSPs |
| DOE-417 | Not required: the DOE-417 instructions exclude commercial power reactors regulated by the NRC and subject to the 10 CFR Part 73 event notification rules from "Generating Entities," and no division is a Balancing Authority, Reliability Coordinator, or electric utility |
| Work management system | Fleet-wide since 2022; about 7,300 active users (5,100 Nuclear Generation, 1,450 Engineering and Radiation Services, 450 Radioactive Waste Management, 300 corporate and vendor). About 410,000 work orders a year. Clearance and tagging has a paper fallback |
| Plant data replica | Each station has replica servers in its business DMZ that receive plant process data one way from Level 3. Engineering, the Maintenance Rule program, and the predictive maintenance service read from the replicas |
| Cross-division staff | Engineering and Radiation Services supplies about 900 engineers and technicians to the group's own stations each year; Radioactive Waste Management supplies radwaste and decommissioning crews. Both work under Nuclear Generation's access authorization and CSP rules while on site |
| Engineering and Radiation Services | 14 external utility clients and the group's own stations. SGI stand-alone systems at 4 offices; about 260 SGI-authorized staff. DOE contracts include FAR 52.204-21; no DoD contracts (DFARS 252.204-7012 and CMMC not applicable). No PHI (not a HIPAA business associate) |
| Dosimetry service | NVLAP-accredited processor (10 CFR 20.1501(d)). Customers are licensees that keep dose records under 20.2106; the division processes and hosts them. Records include names, dates of birth, and an identification number (Social Security number for about 61% of individuals). Customer contracts require incident notice within 72 hours of confirmation |
| Radioactive Waste Management | Florida facility: Florida Department of Health specific license with the Part 37 standard license condition; category 2 sealed source vault. Second facility: Agreement State license, no category 1 or 2 quantity. Both handle mixed waste under EPA-authorized RCRA programs. DOE remediation contract includes FAR 52.204-21. Background checks for drivers use consumer reports (FCRA) |
| Cloud | Provider A hosts the landing zone, the work management system, the CAP integration, the dosimetry system, and division workloads. Provider B hosts disaster recovery replicas and the immutable backup vault. The waste tracking system is vendor SaaS. No CDA, no SGI, and no Part 37 security plan is in either cloud |
| Revenue split (fictional) | Nuclear Generation about $3.6 billion; Engineering and Radiation Services about $6.2 billion; Radioactive Waste Management about $8.2 billion. Total about $18.0 billion |
| Out of scope by fact | No Part 53 license (73.110 not applicable); no DoD contracts; no PHI; no payment card data stored (customer card payments go to the bank's hosted payment page); no New York operations |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president (Chief Nuclear Officer for Nuclear Generation). High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. A risk that is a deficiency in a station CSP or could affect nuclear safety cannot be accepted outside the station CAP; it must be entered there and corrected |
| Additional role titles (P01 to P10) | Fleet engineering director (owns predictive maintenance pilot outcomes); CAP manager (Nuclear Generation); group identity, SOC, and cloud platform directors (operate SYS-G1 to SYS-G3); Radioactive Waste Management OT lead; Radioactive Waste Management processing director; Engineering and Radiation Services chief engineer; Engineering and Radiation Services outage staffing director; DOE programs director; DOE remediation program manager |
| Radioactive Waste Management history | The division was brought into the group structure in 2023; its security lead reported to operations until 2025, which is why its supplement had no review date (P06) |
| Waste customer assurance | Several waste generator customers asked for assurance about the customer portal at 2026 contract renewals (P09) |
| Assessment fieldwork detail | P07 station fieldwork: Station A 2026-07-13 to 2026-07-17; Station B 2026-08-03 to 2026-08-07. The printer finding was reported on 2026-08-05 and passwords were changed by 2026-09-04 |
| AI use cases | 9 registered use cases across the group (P10 inventory); the predictive maintenance pilot runs at Stations A and B, and automatic work request creation was disabled on 2026-09-15 |

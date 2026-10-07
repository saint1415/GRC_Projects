# Scenario facts: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given and was checked against the primary source (eCFR version date 2026-09-23 unless stated). This scenario is independent of the other sizes.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant, not a smaller reporting company; its wholly owned nuclear operating subsidiary holds the NRC operating licenses) |
| Business | Nuclear electric generation (NAICS 221113). Owns and operates a fleet of four nuclear generating stations with seven units and sells the output under long-term power purchase agreements (PPAs) with regional utilities and in bilateral wholesale sales. Also sells two services to outside companies: remote monitoring and diagnostics of plant equipment (SL-1) and personnel dosimetry processing (SL-2) |
| Location | Headquartered in Florida (corporate campus with the fleet support center and data center DC-1). Stations in four states: **Station 1** (Florida, 2 pressurized water reactor units, about 2,350 MW net), **Station 2** (Georgia, 2 boiling water reactor units, about 2,200 MW), **Station 3** (South Carolina, 2 pressurized water reactor units, about 2,300 MW), **Station 4** (Alabama, 1 pressurized water reactor unit, about 1,180 MW; acquired 2025-07-01). Fleet capacity about 8,030 MW net. Colocation data center DC-2 is in Georgia. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 7,750 at the stations (including about 900 nuclear security officers) and about 4,250 in fleet support (engineering, nuclear fuel, training, IT, supply chain, the monitoring and diagnostics center, the dosimetry laboratory, and corporate functions). Each refueling outage adds 1,200 to 1,500 supplemental contractor workers for about 30 days; the fleet ran 5 outages in 2025 and has 4 planned in 2026 |
| Revenue | $4.8 billion a year (fictional), about $13.2 million per calendar day. At full power one unit earns about $1.9 million of revenue per day on average |
| Ownership and governance | Public shareholders. Board committees: audit committee, risk committee, and nuclear safety oversight committee. Not SBA-small (SBA standard for NAICS 221113 is 1,150 employees, 13 CFR 121.201) |
| NRC status | Power reactor licensee for seven units (10 CFR Part 50 operating licenses). Subject to **10 CFR 73.54** (cyber security program under an NRC-approved cyber security plan based on the NEI 08-09 template, with RG 5.71 Rev. 1 as NRC guidance), **10 CFR 73.77** (cyber security event notifications), **10 CFR 73.21 and 73.22** (Safeguards Information), **10 CFR 73.55** (physical protection, including 73.55(m) program reviews), **10 CFR 73.56** (access authorization), **10 CFR Part 26** (fitness for duty), **10 CFR 50.72 and 50.73** (event reporting), and **10 CFR 50.65** (Maintenance Rule). Cyber security is inspected under NRC inspection procedure 71130.10 in the Reactor Oversight Process |
| NERC status | Registered Generator Owner and Generator Operator. The fleet **Generation Dispatch Center** (primary at headquarters, backup at Station 2) performs Generator Operator functions for all stations; because Stations 1 to 3 each exceed 1,500 MW, its BES Cyber Systems are **high impact** (CIP-002-5.1a Attachment 1, criterion 1.4). Systems regulated by the NRC under 73.54 are exempt from CIP (CIP-002-5.1a section 4.2.3.3). The company-owned switchyard interface devices at each station (remote terminal units and digital fault recorders outside the 73.54 scope) are **low impact** (criterion 3.3) |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; NERC CIP for the Generation Dispatch Center; two external service lines with SOC 2 commitments; an acquired station still on legacy systems |
| Not in scope | **10 CFR 73.110** (Part 53 plants; the company holds Part 50 licenses and has not elected it); **HIPAA** (the dosimetry laboratory processes occupational dose records that client employers keep as employment records; PHI excludes employment records held by a covered entity in its role as employer, 45 CFR 160.103, and the lab performs no covered function); **CIRCIA** (proposed only; final rule not published as of 2026-09-25) |

### Regulatory driver IDs used in this sample
The vertical's `requirements.csv` provides C-NUCLEAR-R01 to R05. This sample adds **scenario-level driver IDs (C-NUCLEAR-S01 to S10)** for other binding rules that touch information security. They are defined here and nowhere else.

| ID | Requirement | Citation | Status for this company |
|---|---|---|---|
| C-NUCLEAR-R01 | NRC cyber security rule for power reactors | 10 CFR 73.54 (RG 5.71 Rev. 1 guidance; NEI 08-09 based plan) | **Applies (primary regulation in P03)** |
| C-NUCLEAR-R02 | Part 53 cyber rule | 10 CFR 73.110 | Not applicable (Part 50 licensee; not elected) |
| C-NUCLEAR-R03 | NRC cyber security event notifications | 10 CFR 73.77 | Applies |
| C-NUCLEAR-R04 | NERC CIP Reliability Standards | 16 U.S.C. 824o; 18 CFR Part 40; CIP-002-5.1a, CIP-003-9, CIP-004-7, CIP-005-7, CIP-006-6, CIP-007-6, CIP-008-6, CIP-009-6, CIP-010-4, CIP-011-3, CIP-012-2, CIP-013-2, CIP-014-3 | Applies to the Generation Dispatch Center (high impact) and station switchyard interface devices (low impact) |
| C-NUCLEAR-R05 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | Not in effect. As proposed, the company would be covered (above the SBA size standard, and it owns commercial nuclear power reactors) |
| C-NUCLEAR-S01 | Protection of Safeguards Information | 10 CFR 73.21, 73.22 | Applies |
| C-NUCLEAR-S02 | Protection of access authorization and fitness-for-duty information | 10 CFR 73.56(m); 10 CFR 26.37 | Applies |
| C-NUCLEAR-S03 | Physical protection program reviews and physical security event notifications | 10 CFR 73.55(m); 10 CFR 73.1200 | Applies |
| C-NUCLEAR-S04 | Reactor event notifications and licensee event reports | 10 CFR 50.72; 10 CFR 50.73 | Applies |
| C-NUCLEAR-S05 | Maintenance Rule | 10 CFR 50.65 | Applies (context for P10) |
| C-NUCLEAR-S06 | SEC cybersecurity disclosure | Form 8-K Item 1.05; 17 CFR 229.106 | Applies |
| C-NUCLEAR-S07 | State breach notification and data security | Each state where affected individuals reside; Fla. Stat. 501.171 worked example | Applies |
| C-NUCLEAR-S08 | Dosimetry processing and dose records | 10 CFR 20.1501(d) (NVLAP accreditation); 10 CFR 20.2106 (records of individual monitoring results) | Applies (SL-2 and the fleet's own dose records) |
| C-NUCLEAR-S09 | Export control of nuclear technology | 10 CFR Part 810 (scope in 810.2); 10 CFR Part 110 | Applies to technology transfer, including access by foreign nationals |
| C-NUCLEAR-S10 | Technical Specification surveillance requirements | 10 CFR 50.36(c)(3) | Applies (context: surveillance schedules and clearance records in the WMS must stay accurate) |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board risk committee; audit committee; nuclear safety oversight committee | Cyber risk oversight (Item 106 disclosure); Internal Audit and SOX; nuclear safety and security performance |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk jointly; take part in materiality determinations with the disclosure committee |
| Chief Nuclear Officer (CNO) | Accountable for safe and secure operation of the fleet; executive owner of the 73.54 cyber security program; authorizing official equivalent for the SSP system (P02) |
| Site Vice Presidents (4) | Senior licensee official at each station; accept site-level risk up to Moderate |
| Chief Information Security Officer (CISO) | Enterprise cybersecurity program owner (business IT and governance of OT security standards); chairs the policy governance committee |
| Director, Nuclear Cyber Security | Fleet owner of the cyber security plan (CSP) and program under 73.54; reports to the CNO with a dotted line to the CISO. Each station has a Site Cyber Security Program Manager and a cyber security team that maintains critical digital assets (CDAs) |
| Director, Nuclear Security | Physical protection program (73.55), Safeguards Information program (73.21-73.22), access authorization (73.56), and fitness for duty (Part 26) |
| Director, Security Operations | Runs the 24x7 Security Operations Center (SOC) for business IT, with a managed security service provider (MSSP) for overflow |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee |
| Director, Nuclear Oversight | Independent nuclear quality assurance oversight; performs the 73.55(m) security program reviews, including the cyber security program; independent of station line management |
| General Counsel | Chairs the disclosure committee; legal holds; outside counsel |
| Chief Compliance Officer | Privacy and breach determinations for personal information; regulatory compliance program (second line with the GRC team) |
| Chief Information Officer (CIO) | Business IT operations; owns the enterprise platform (common control provider) |
| GRC team (10), Internal Audit IT audit group (6), Nuclear Oversight security auditors (4) | Three lines model; see section 2.1 of the build guide |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems

| ID | System | Notes |
|---|---|---|
| SYS-01 | Plant business networks (one per station) and the corporate network | Station LANs, Wi-Fi, outage trailers, print servers, and about 17,500 endpoints fleet-wide. One-way data transfer devices (data diodes) carry plant data outward from the CDA networks to a plant data historian replica on each business network. Station 4 is still on the prior owner's directory and a flat network |
| SYS-02 | Fleet work management system (WMS) | Commercial enterprise asset management software, customer-managed on Cloud provider A, with a WMS edge server at each of Stations 1 to 3. Work orders, work packages, clearance and tagging, Technical Specification surveillance scheduling, outage schedules. About 9,500 named users (plus up to 1,500 outage contractors per outage) |
| SYS-03 | Identity platform | Single sign-on, MFA, privileged access management (PAM), identity governance. Station 4 identities are not yet federated |
| SYS-04 | Multi-cloud estate and data centers | Two public cloud providers (vendor-agnostic: Cloud provider A and Cloud provider B) in US regions only, plus DC-1 (Florida) and DC-2 (Georgia colocation) |
| SYS-05 | Critical digital assets (CDAs) at the four stations | About 8,400 CDAs supporting safety, security, emergency preparedness, and support functions (73.54(a)(1)); governed by the CSP, outside the SSP boundary |
| SYS-06 | Physical security systems | Access control, alarm stations, intrusion detection, cameras; CDAs under the CSP |
| SYS-07 | Emergency preparedness systems | Emergency Response Data System link, offsite notification systems, emergency facility systems; CDAs or supporting systems under the CSP |
| SYS-08 | Generation Dispatch Center (GDC) | NERC CIP high impact BES Cyber Systems, inter-control-center links to host Balancing Authorities and Transmission Operators |
| SYS-09 | ERP, HR, payroll, and supply chain | SaaS ERP (SOX-relevant); supply chain including safety-related procurement |
| SYS-10 | Access authorization and fitness-for-duty systems | Personnel access data (73.56) and FFD records (Part 26); exchange with a shared industry personnel access database |
| SYS-11 | Safeguards Information systems | Stand-alone SGI workstations in locked containers (73.22(g)); never networked |
| SYS-12 | Monitoring and diagnostics (M&D) platform | Fleet M&D center analytics on Cloud provider B; supports AI-001 and the SL-1 service |
| SYS-13 | Dosimetry laboratory system | Dosimeter readers and the dose record database in DC-1; client portal on Cloud provider B; supports SL-2 |
| SYS-14 | Vendors | About 2,900 suppliers; about 410 with network or data access; 38 rated tier 1 |
| SYS-15 | AI portfolio | 12 use cases, governed by the AI governance committee formed in 2025 |
| SYS-16 | Productivity suite | SaaS email, files, and chat |

**SSP system (P02):** the *Fleet Work Management System and Plant Business Networks (WMS-PBN)*: the fleet work management system (SYS-02) with its Cloud provider A workload account and station edge servers, and the four plant business networks (SYS-01), up to the business side of the one-way data transfer devices.

## 4. Current security posture: mature, with residual gaps

**In place today:**
- Cyber security plans implemented at all four stations, with NRC cyber security inspections under IP 71130.10 at each station since 2022
- A defensive architecture in which CDA networks send data out only through one-way data transfer devices; no remote access to CDAs
- Portable media and mobile device kiosks at every protected area entry; controlled maintenance and test equipment
- Safeguards Information program with stand-alone SGI computers
- Access authorization and fitness-for-duty programs
- A 24x7 SOC with an MSSP for overflow; EDR on business endpoints at Stations 1 to 3 and corporate
- PAM and quarterly access certification for business systems
- Immutable backups in separate cloud accounts and DC-2
- Annual disaster recovery tests for tier-1 business systems
- NERC CIP program for the Generation Dispatch Center, audited by the Regional Entity in 2025
- Nuclear Oversight reviews of the security program, including cyber, at least every 24 months (73.55(m))
- SOC 2 Type 2 report for SL-1 (Security, Availability, Confidentiality) for 2025
- SEC Item 106 disclosure in the annual report

**Residual gaps found in the 2026 assessments:**
1. **Station 4 integration.** Station 4 is still on the prior owner's directory, a flat business network, a legacy VPN for vendors, and the prior owner's work management system under a transition services agreement that ends 2027-06-30. Its business-network logs are not in the SIEM.
2. **Outage contractor access.** During refueling outages, up to 1,500 contractors receive WMS and business-network accounts. Removal after the outage is manual and late at two stations.
3. **Predictive maintenance sensor gateways.** Wireless sensor gateways with their own cellular links were installed on non-safety equipment at Station 4 in 2026 without a documented 73.54(b)(1) analysis or design change cyber review.
4. **Notification coordination.** The SOC's reports to the FBI and CISA are not linked to the stations' 73.77(a)(2)(iii) 4-hour clock, and cyber program deficiencies are not always entered in the corrective action program within 24 hours (73.77(b)(1)).
5. **Disclosure readiness.** The SEC materiality playbook has never been exercised on a plant scenario that also triggers NRC notifications, which the NRC publishes as event notification reports.
6. **Third parties.** One work management software vendor, two major outage contractors, and an M&D analytics vendor without a SOC report are single points of failure or assurance gaps.
7. **AI.** 12 AI use cases, but only 8 have completed committee review. Predictive maintenance models are tested only fleet-wide, not by station or equipment class.
8. **Service lines.** SL-2 dosimetry has no SOC 2 report yet, and its dose record restore has never been tested.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 | WMS-PBN (registry default "Plant business network and work management system (non-safety)") |
| P03 | Primary: 10 CFR 73.54 with RG 5.71 Rev. 1 controls as implemented in the NRC-approved CSP. Also: 73.77, SGI, access authorization and FFD information, 73.55(m), 50.72 and 50.73, NERC CIP, SEC, state breach laws, dosimetry records, Part 810, CIRCIA status |
| P08 | Cyber attack on the Station 2 plant business network during a refueling outage, with an attempted pivot toward CDAs (registry default), including the 73.77 decision points, the SEC materiality assessment and 8-K Item 1.05 step, and multi-state breach notification for contractor personal data |
| P09 | SOC 2 Type 2 readiness across two service lines: SL-1 monitoring and diagnostics, SL-2 dosimetry processing |
| P10 | Enterprise AI portfolio (12 use cases) with a full assessment of AI-001, predictive maintenance for non-safety plant equipment (registry default) |
| Cloud | Multi-cloud (vendor-agnostic), US regions only, with common controls. SGI and CDA data are never placed in the cloud |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (station walkthroughs 2026-06-15 to 2026-06-26; evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment of WMS-PBN (Internal Audit, third line) |
| 2026-09-10 | Results to the board risk committee and the nuclear safety oversight committee |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1 to 6.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Vice President, Fleet Work Management | WMS business owner (system owner in P02) |
| WMS Application Manager | Day-to-day WMS administration, configuration, and interfaces |
| Plant Managers (4) | Station operations; approve station procedures and downtime plans |
| Director of Cloud Platform Engineering | Cloud landing zones in both clouds (common control provider) |
| Director of Identity and Access Management | Identity platform (SYS-03) |
| Director of Network Engineering | Corporate and plant business networks, SD-WAN, firewalls (common control provider) |
| Director of Endpoint Engineering | Workstations, EDR, endpoint baselines (common control provider) |
| Director of Third-Party Risk Management | Vendor tiering, SOC report reviews, supply chain risk (in the GRC team) |
| Vice President, Generation Dispatch and Energy Marketing | NERC CIP Senior Manager; GDC and PPA scheduling |
| Director, NERC Compliance | NERC CIP program |
| Vice President, Monitoring and Diagnostics Services | SL-1 service line owner; AI-001 business owner |
| Director, Dosimetry Laboratory | SL-2 service line owner; NVLAP accreditation |
| Director, Emergency Preparedness | Emergency plans, offsite notification, ERDS |
| Radiation Protection Managers (4) | Station radiation protection and dose records |
| Vice President, Outage Management | Fleet refueling outage program and outage contractors |
| Vice President, Integration Management | Station 4 integration |
| Vice President, Supply Chain | Procurement, including safety-related procurement |
| Export Compliance Officer | Part 810 and Part 110 technology controls |
| Chief Human Resources Officer | Workforce onboarding, terminations, training records |
| Vice President, Facilities | Corporate campus and data center physical security |
| Vice President, Corporate Communications; Vice President, Investor Relations | Media and investor communications; Investor Relations sits on the disclosure committee |
| Controller | SOX program owner |
| Senior Vice President, Nuclear Engineering | Chairs the AI governance committee |
| Maintenance Rule Coordinators (4) | 50.65 monitoring at each station; reviewers for AI-001 |
| Corrective Action Program Manager (fleet) | Corrective action program (CAP), including 73.77(b) entries |

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Nuclear Officer, Chief Compliance Officer, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel.

**Work management volumes.** About 410,000 work orders and 95,000 clearance tags a year fleet-wide. About 260 Technical Specification surveillance tests are scheduled through the WMS each week across the fleet.

**Service lines (P09).** SL-1 monitoring and diagnostics: the fleet M&D center monitors about 9,600 non-safety equipment points for the company's seven units and for 6 external generation owners (14 plants, including 2 nuclear plants owned by others). Clients send data outbound from their plants; the company never connects to client control systems. SL-2 dosimetry: an NVLAP-accredited dosimetry processor (20.1501(d)) that processes about 46,000 dosimeters a quarter, about 70% for about 140 external licensees (hospitals, universities, industrial radiography firms, and other nuclear plants).

**Station 4 legacy systems.** The prior owner's directory, work management system, and vendor VPN remain in service under a transition services agreement that ends 2027-06-30. WMS migration is planned for 2027-05, after Station 4's spring 2027 refueling outage.

**Policy set (P06).** Five policies, 20 standards, and 11 procedures in one hierarchy (`policy-hierarchy.md`), with 52 policy statements. The CIP Senior Manager also approves POL-01 to POL-05 as the CIP-003-9 R1 cyber security policies. Current exceptions include EXC-2026-031 (Station 4 identity), EXC-2026-033 (Station 4 SIEM and EDR), EXC-2026-036 (edge server patching during outage freezes), and EXC-2026-038 (Station 4 vendor VPN).

**Internal Audit team for P07.** An IT audit manager and four IT auditors from the six-person IT audit group. Default administrator passwords on 3 Station 4 sensor gateways were found during testing and reported 2026-08-06.

**Incident response (P08).** The technical tabletop on 2026-04-22 did not include the disclosure committee or the SOC-to-station notification step. The P08 worked example (fictional, 2027-03) uses a Station 2 refueling outage of Unit 2 and an outage contractor roster of 1,350 people in 23 states (230 Florida residents).

**SOC 2 (P09).** SL-1 has 6 client agreements. SL-2 uses client worker Social Security numbers as identifiers for about 40 older clients and about 30 older client agreements predate the standard security terms.

**AI portfolio (P10).** 12 use cases: AI-001 predictive maintenance (High); AI-002 enterprise generative AI assistant; AI-003 SOC alert triage; AI-004 condition report screening (High, pilot); AI-005 outage schedule optimization (pilot); AI-006 dosimetry reading anomaly flagging; AI-007 energy price and load forecasting; AI-008 generative AI drafting assistant for work packages; AI-009 spare parts forecasting; AI-010 engineering document search; AI-011 resume screening (High, suspended); AI-012 employee help desk agent. AI-005, AI-009, AI-011, and AI-012 lack committee review. AI governance committee chaired by the Senior Vice President, Nuclear Engineering. The registry default AI use case (predictive maintenance for non-safety plant equipment) is kept as AI-001 and tiered High at this size because its scope includes balance-of-plant equipment in Maintenance Rule scope under 10 CFR 50.65(b)(2)(iii).

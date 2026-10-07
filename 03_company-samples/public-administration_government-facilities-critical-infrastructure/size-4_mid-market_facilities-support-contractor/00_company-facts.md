# Scenario facts: Cris Santos Company | Government Services and Facilities | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Contract terms described here are fictional scenario choices unless a regulation is cited.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held corporation; private equity-backed since 2024; board with an audit committee) |
| Business | Integrated facilities support contractor (NAICS 561210, Facilities Support Services). The company operates and maintains government buildings: building engineering and trades, HVAC and building automation (BAS), electronic security support (access control and video), energy management, and 24x7 remote monitoring from its Remote Operations Center (ROC) |
| Location | Florida only. Headquarters and the primary ROC are in a leased office building in central Florida. A backup ROC sits in the north Florida regional office, about 200 miles away. Three regional offices (north, central, south) dispatch field staff. All customer sites are in Florida |
| Customers and contracts | **Federal (CT-F):** operations and maintenance (O&M) of 5 GSA-controlled federal office buildings in 3 Florida metro areas (about 1.9 million sq ft), GSA Public Buildings Service contract. **State (CT-S):** a state agency's office portfolio of 9 buildings at 6 sites (about 1.4 million sq ft), including the building that houses the agency's primary data center. **County A (CT-C1):** the county government center (2 towers), the county Emergency Operations Center (EOC), the Supervisor of Elections operations warehouse, and 16 county service buildings (19 sites). **County B (CT-C2):** the county government complex and 8 service centers (9 sites). **City (CT-M):** city hall and 11 municipal buildings (12 sites). **School district (CT-K):** HVAC and BAS energy management for 62 schools, with no access control or video work |
| Revenue | About $100.0 million a year (fictional): CT-F $36.0 million, CT-S $22.0 million, CT-C1 $19.5 million, CT-C2 $8.5 million, CT-M $7.0 million, CT-K $7.0 million. Above the SBA size standard of $47.0 million for NAICS 561210 (13 CFR 121.201), so not SBA-small |
| Workforce | 600 employees: 22 executive and administration; 38 finance, contracts, HR, and procurement; 18 IT and security; 30 operations management (VP Operations, 5 program managers, 24 site managers and supervisors); 60 building technology (Director of Building Technology, Controls Engineering Manager, Security Systems Manager, 36 BAS controls technicians and engineers, 21 security systems technicians); 24 ROC staff (ROC Manager, 23 operators across 24x7 shifts); 408 building engineers, technicians, and trades. 152 staff are assigned to the federal buildings and hold GSA-issued PIV cards |
| Who owns the building systems | **The customers.** All field equipment (BACnet controllers, door controllers, readers, cameras, NVRs) is government-owned. At the federal buildings the BAS runs on GSA servers on the GSA Building Systems Network (BSN), which GSA authorizes (FISMA Moderate ATO, per the GSA Building Technologies Technical Reference Guide (BTTRG) v3.0, May 2024). At the state, county, and city sites the company runs the supervisory and administration layer on its own platform (section 3). The school district hosts its own BAS server on its network; the company reaches it through the company's remote access broker |
| Data the company holds | For CT-S, CT-C1, CT-C2, and CT-M: cardholder records for about 41,000 government employees and contractors (name, employer or department, badge photo, credential number, door schedule, access history); 1,150 face templates at the County A government center (P10); building drawings, security system layouts, and door schedules. For CT-F: work orders and GSA building drawings marked **CUI** (Physical Security category, GSA Order PBS 3490.3 CHGE 1). For the company itself: records on 600 employees and about 2,400 job applicants a year. No FTI, CJI, voting systems, or education records (Not in scope, below) |
| Federal contract clauses (CT-F) | FAR 52.204-21 (Basic Safeguarding of Covered Contractor Information Systems, NOV 2021); FAR 52.204-23 (Kaspersky, DEC 2023); FAR 52.204-25 (Section 889 telecom and video surveillance, NOV 2021) with representations under 52.204-24/-26; FAR 52.204-30 (FASCSA orders, DEC 2023); FAR 52.204-9 (PIV of contractor personnel, JAN 2011), including the (d) flow-down to subcontractors with routine access to federal facilities, and GSAR 552.204-9. The statement of work incorporates the BTTRG, GSA IT Security Policy (CIO 2100.1), and CUI handling under 32 CFR Part 2002 and GSA Order PBS 3490.3 |
| State contract terms (CT-S) | Cybersecurity exhibit (Fla. Stat. 282.318(4)(h) requires state agency IT service contracts to meet state and federal standards, including NIST CSF, and to assign privacy and security duties). The exhibit requires **NIST SP 800-53 Rev. 5 Moderate** controls for contractor-managed systems that store or process agency data, background screening, incident notice to the agency within 24 hours, an annual independent assessment, and, from the renewal term that began 2026-07-01, a **SOC 2 Type 2 report** by the end of the second renewal year (2028-06-30) |
| County A contract terms (CT-C1) | Security addendum: compliance with the county's cybersecurity standards (adopted under Fla. Stat. 282.3185(4), NIST CSF-based); notice to the county **within 6 hours** of discovering suspected ransomware and within 24 hours for other incidents (set so the county can meet its own 12-hour and 48-hour state reports); fingerprint-based background checks; public records clause under Fla. Stat. 119.0701; an annual SOC 2 report or equivalent independent assessment. **Supervisor of Elections annex** for the elections operations warehouse: two-person access to the voting equipment cage, no remote unlock of cage doors, and an export of the cage access log after each election |
| County B, City, and School district terms | **CT-C2 and CT-M:** security addenda modeled on County A (county or city cybersecurity standards under Fla. Stat. 282.3185(4); 24-hour incident notice; background checks; Fla. Stat. 119.0701 public records clause). **CT-K:** 48-hour incident notice; no access to student information systems; the district provides the VPN endpoint the company's broker connects to |
| Sector context | Government Services and Facilities sector (co-Sector Risk Management Agencies: DHS and GSA, NSM-22). Election infrastructure is a subset of this sector; the company's only election-related work is access control at the elections warehouse. The company is a contractor to government facility owners, not a government entity |
| Not in scope | IRS Pub. 1075 (C-GOVERNMENT-R02): no FTI; the state contract states the company has no access to FTI areas or systems. CJIS Security Policy (C-GOVERNMENT-R03): both county contracts exclude the sheriff's offices, jails, and the 911 center (a separate sheriff-run building, not the EOC). VVSG 2.0 (R04): the company touches no voting system; it only maintains doors and cameras at the elections warehouse. FERPA (R05): the school district work is HVAC and BAS only and the company receives no education records. SLCGP (R07): a grant condition for governments. CIRCIA (R06): proposed rule only (tracked in P03 because the company now exceeds its SBA size standard). FedRAMP: the company operates no system for a federal agency. GovRAMP (R08): no contract requires it today (watch item for the 2028 state rebid). Colorado SB26-189: the company does business only in Florida |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: breach notice and reasonable security (Fla. Stat. 501.171), contractor public records duties and the security plan exemption (Fla. Stat. 119.0701 and 119.071(3)), the customers' own incident reporting duties that the contracts flow down (Fla. Stat. 282.318 and 282.3185), and the ransom payment ban for state agencies, counties, and municipalities (Fla. Stat. 282.3186). Cardholders or employees who live in another state are handled under the law of each state where affected individuals reside |
| Added at this size | A SOC 2 Type 2 commitment to the state (P09); five customer notice clocks to coordinate (P08); a 24x7 ROC with a backup ROC; a multi-account cloud landing zone (P04); an AI portfolio of 6 use cases (P10) |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting; oversight of the internal audit plan |
| Chief Executive Officer | Accepts High risk; approves the risk appetite, POL-01, and the security budget |
| Chief Operating Officer (COO) | Executive sponsor of the security program; system owner of the IFOP (the SSP system); accepts Moderate risk; approves POL-02 to POL-05 |
| Chief Financial Officer | Cyber insurance; ERP and payroll data owner |
| General Counsel | Breach determinations and customer, regulator, and contract notices; public records requests; privilege for incident investigations |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting; owns POL-01; chairs the AI review group |
| IT Director | Designated **Information Security Officer**; owns IT operations, the cloud landing zone, and contingency planning for IT |
| Security Manager, 2 security analysts, and 1 GRC analyst | Security operations, MSSP oversight, vulnerability management, risk register, SSP, and POA&M |
| OT Security Engineer (hired 2026-05) | OT network monitoring, OT hardening standards, remote access broker policy for OT |
| Director of Building Technology | Owns the BAS and access control platforms; manages the Controls Engineering Manager and the Security Systems Manager |
| Controls Engineering Manager | BAS supervisory platform, controller program repository, BAS programming standards, 36 controls technicians and engineers |
| Security Systems Manager | Access control and video platform administration for CT-S, CT-C1, CT-C2, and CT-M; integrator oversight; 21 security systems technicians |
| VP Operations | Field operations, emergency and hurricane operations, and the ROC; operations lead in incidents |
| Program managers (Federal; State; County A; County B; City and Schools) | Customer liaison per contract; customer incident notices; manual-mode (building recovery) procedures at their sites |
| ROC Manager | 24x7 ROC staffing, alarm handling procedures, ROC failover to the backup ROC |
| Contracts Director | FAR and customer contract compliance; subcontract flow-downs; Section 889 and FASCSA screening; CUI program lead |
| HR Director | Onboarding, terminations, background checks, PIV sponsorship coordination with GSA, training records, applicant tracking (AI-006) |
| Internal audit (co-sourced firm) | Independent annual IT audit; performed the P07 assessment with an OT specialist subcontractor |
| Managed security service provider (MSSP) | 24x7 managed detection and response (MDR) and SIEM monitoring |
| OT subcontractors and integrators (7) | Install and service door controllers, readers, cameras, NVRs, and specialty BAS equipment; several have remote access |

## 3. Systems

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | BAS supervisory platform: 8 supervisory server clusters and trend historians (one per customer and region) for about 9,800 customer-owned BACnet controllers at CT-S, CT-C1, CT-C2, and CT-M | Company cloud landing zone, OT workloads account (SYS-04), plus on-site OT networks | Operational data; building drawings | Field controllers keep running their last programs and schedules if the supervisory layer is lost. Company-licensed software |
| SYS-02 | Access control and video platform: cloud-hosted access control and video management tenants for CT-S, CT-C1, CT-C2, and CT-M, administered by the company; about 1,040 customer-owned door controllers, 4,300 readers, 5,100 cameras, and 58 NVRs | Vendor SaaS plus on-site OT | Yes: about 41,000 cardholder records and access history; video; face templates (SYS-13) | Door controllers cache credentials and keep working for up to 72 hours without the cloud service. Vendor has a SOC 2 Type 2 report |
| SYS-03 | Privileged remote access broker: per-session approval, credential injection from a vault, and session recording | Company cloud landing zone (shared services account) | Credentials; session recordings | Deployed 2025. The intended single path to customer OT networks. Not yet used by all subcontractors (gap 1) |
| SYS-04 | Cloud landing zone: 5 accounts (management and identity, security and logging, shared network services, OT workloads, backup) | Public cloud provider (vendor-agnostic) | Yes (drawings, CUI library, controller program repository, backups) | Hosts SYS-01 and SYS-03, file storage, the controller program repository, and the backup vault |
| SYS-05 | Site OT edge: 46 company-managed edge firewalls and VPN gateways (one per state, county, and city site); 38 engineering workstations; passive OT network monitoring sensors at 12 sites | On-premises at customer sites | In transit | 9 engineering workstations run an unsupported OS required by legacy BAS tools |
| SYS-06 | Identity provider (single sign-on, MFA, conditional access) | SaaS | Identities only | All workforce and subcontractor accounts; phishing-resistant keys for cloud and broker administrators |
| SYS-07 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | |
| SYS-08 | Computerized maintenance management system (CMMS) | Vendor SaaS | Federal contract information (FCI) for CT-F; site data for all contracts | Work orders, asset lists, preventive maintenance, change tickets for BAS programs and door schedules |
| SYS-09 | Endpoints | Company-owned | Yes (cached) | 420 laptops, 380 rugged tablets, 40 ROC workstations (30 at the primary ROC, 10 at the backup ROC), 520 managed phones |
| SYS-10 | GSA-furnished access (CT-F) | GSA | CUI and GSA building data | GSA BAS applications on the BSN, reached only through a GSA-provided virtual desktop with a PIV card; 12 GSA-furnished laptops. **GSA's system under GSA's ATO; outside the company's boundary** |
| SYS-11 | ERP (finance, procurement, project accounting) and HR, payroll, and applicant tracking suite | Vendor SaaS (two vendors) | Yes: employee SSNs, bank details, background check results, applicant records | The HR suite includes the candidate ranking feature (AI-006) |
| SYS-12 | SIEM and managed detection and response (MSSP) | SaaS | Security logs | Receives identity provider, cloud, EDR, broker, and IT firewall logs. BAS supervisory servers, access control audit trails, and OT sensors do not feed it (gap 5) |
| SYS-13 | Face verification module | Feature of the SYS-02 vendor platform plus 6 face-capable readers | Yes: face templates (treated as biometric data) | County A government center, 2 employee entrances, 1,150 enrolled county employees (P10) |
| SYS-14 | Primary and backup ROC | On-premises (HQ and north regional office) | Alarm data in transit | Video wall, alarm consoles, out-of-band phones; the backup ROC can take over in 2 hours |
| SYS-15 | Video analytics module | Feature of the SYS-02 vendor platform | Video metadata | After-hours intrusion and loitering detection at 4 CT-S sites since 2026-02 (AI-003) |

**SSP system (P02):** the *Integrated Facility Operations Platform (IFOP)*: SYS-01, SYS-02 (the company-administered tenants and configuration), SYS-03, SYS-04, SYS-05, SYS-13, SYS-14, SYS-15, the ROC workstations and technician devices in SYS-09, and their interfaces to SYS-06, SYS-08, SYS-12, and the subcontractors' remote access.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- A security program led by a vCISO since 2024, with an IT Director as Information Security Officer, a Security Manager, 2 security analysts, a GRC analyst, and an OT Security Engineer
- Policies adopted in 2024 (refreshed in this cycle, P06)
- MFA for all users through the identity provider; phishing-resistant keys for cloud and broker administrators
- EDR on all company laptops, ROC workstations, and cloud servers, with 24x7 MSSP monitoring
- A privileged remote access broker with session recording (2025) used by company staff at all 46 sites
- A 5-account cloud landing zone with daily backups to a separate backup account (30-day write-once retention, separate administrator credentials)
- Annual risk assessment (first done July 2025) and an annual independent assessment for the state contract (2025)
- Monthly authenticated vulnerability scanning of IT and cloud systems
- OT segmentation (dedicated VLANs, deny-by-default edge rules) at 29 of 46 sites; passive OT monitoring sensors at 12 sites
- Building recovery (manual operation) procedures for the 5 federal buildings (BTTRG requirement, exercised with GSA in March 2026) and for the 6 state sites (written 2025, tested April 2026)
- Supplier screening against FAR 52.204-25 and 52.204-23 for company purchases since 2024, and a quarterly SAM.gov check for FASCSA orders
- A CUI library with named access for GSA drawings; CUI training for federal site staff
- Fingerprint-based background checks for all staff before assignment; 152 PIV holders under GSA's HSPD-12 process
- Cyber insurance with a breach hotline and panel firms

**Missing or weak, found in the 2026 assessments:**
1. Remote access coverage is incomplete. 4 of 7 OT subcontractors still use their own remote-support tools at 11 sites (County B and City), outside the broker. 14 technicians still hold legacy VPN profiles that route straight to site edge firewalls.
2. OT segmentation is missing at 17 of 46 sites (8 County B service centers and 9 City buildings): BAS and door controllers share the customer's general building network.
3. The OT asset inventory is not reconciled. Passive monitoring covers 12 of 46 sites; the CMMS asset list is reconciled to the network only at the state sites.
4. Field device credentials: the device credential vault covers 31 of 46 sites. Default and shared passwords remain on field devices elsewhere (P07 testing).
5. OT logs are not monitored. BAS supervisory servers, access control administrator audit trails, and OT sensor alerts do not reach the SIEM, and there are no OT detection use cases.
6. Recovery is unproven. Backups are isolated, but only one BAS supervisory cluster restore has been tested; the controller program repository holds current backups for about 55% of controllers; there are no manual-mode procedures for County A, County B, the City, or the school district.
7. Subcontractor security: 3 of 7 OT subcontractors have signed the security addendum. FAR 52.204-21 is flowed down in 5 of the 9 subcontracts that receive FCI. No annual subcontractor reviews.
8. Access lifecycle across customer tenants: administrator and cardholder-admin accounts in the 4 access control tenants are removed manually and reviewed only twice a year.
9. OT vulnerability and firmware management: no OT patch program; 14 of 46 edge firewalls are 2 or more firmware releases behind; 9 engineering workstations run an unsupported OS.
10. Change control for BAS programs and door schedules: changes are ticketed in the CMMS, but many lack approval, and controller programs are not integrity-checked before download.
11. AI adopted without governance: face verification at County A grew from a pilot to 2 entrances with 1,150 enrolled; video analytics went live at state sites; the HR suite's candidate ranking feature was switched on. None had a security, privacy, or bias review.
12. Supporting standards are thin: no OT hardening, logging, or third-party standards.
13. The 2024 incident response plan is IT-centric. It has no OT playbook, does not integrate the 5 customer notice clocks, and has never been exercised with a customer.
14. CUI handling: the CUI library exists, but some CUI drawings still move by email outside it (P03 sample).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | NIST SP 800-53 Rev. 5 (Release 5.2.0) **Moderate** baseline (177 base controls), **binding by contract** for the state scope and used as the **benchmark** for the rest of the IFOP, tailored for OT with NIST SP 800-82 Rev. 3. Also analyzed, as all applicable rules for the primary business line: FAR 52.204-21 and the FAR supply chain and PIV clauses (CT-F); the CUI requirements of 32 CFR Part 2002 that GSA flows down; and the Florida duties that reach a contractor (Fla. Stat. 501.171 and 119.0701) |
| P08 incidents | **Two incident types:** (1) intrusion into building access control and automation systems through a subcontractor's remote-support tool at a County B site; (2) ransomware with data theft in the corporate and cloud environment, affecting the ROC. Both integrated with crisis management and legal |
| P09 SOC 2 | The company is a service organization for its state, county, and city customers. Readiness for a **SOC 2 Type 2** examination (Security, Availability, Confidentiality) to meet the state contract commitment and the county requests; plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio of 6: AI-001 face verification (1:1) at County A; AI-002 face identification (1:N) of the public (County A request, not approved); AI-003 video analytics at state sites; AI-004 BAS fault detection analytics; AI-005 enterprise generative AI assistant; AI-006 candidate ranking in the HR suite |
| Cloud | Multi-account landing zone, vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents in a table for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | Risk assessment and gap analysis fieldwork (site walkthroughs at 8 sites 2026-07-14 to 2026-07-23) |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (site tests 2026-08-10 to 2026-08-14) |
| 2026-09-15 | Results to the board audit committee; deliverables approved by the Chief Operating Officer and, for High risks, the Chief Executive Officer |

## 7. Facts added during the Phase 5 build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Terminology | "Integrated Facility Operations Platform (IFOP)" is the SSP system in P02, identifier CSC-IFOP-01 |
| Registry defaults | The registry defaults fit this business and were kept: primary system "Physical access control and building automation system" (the IFOP), P08 incident "Intrusion into building access control and automation systems" (runbook 1), and P10 use case "Facial recognition for facility access" (AI-001 and AI-002). A second incident type (ransomware) and four more AI use cases were added because the Mid-Market tier calls for two incident types and an AI portfolio |
| Site counts | IFOP sites with a company edge firewall: CT-S 6, CT-C1 19, CT-C2 9, CT-M 12 (46 in total). Segmented today: CT-S 6, CT-C1 19, CT-C2 1 (the government complex), CT-M 3 (29 sites). Flat: 8 County B service centers and 9 City buildings (17 sites). Passive OT sensors: the 6 state sites and 6 County A sites (government center, EOC, elections warehouse, and 3 large service buildings) |
| Controller counts | About 9,800 BACnet controllers on the IFOP: CT-S 2,900; CT-C1 4,100; CT-C2 1,300; CT-M 1,500. The school district's BAS has about 7,400 controllers on the district's own server |
| Revenue per day | About $400,000 per business day over about 250 business days; about $8.3 million invoiced per month. CT-F is about $144,000 per business day |
| Critical facilities | The County A EOC (activated for hurricanes and major events) and the CT-S data center building depend on BAS cooling and power monitoring. Both have local operator workstations and an on-site engineer during EOC activations and around the clock at the data center building |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics, including an OT-capable responder. Notice goes through the carrier hotline before incident vendors are engaged |
| MSSP | 24x7 MDR; contract requires a call to the Security Manager within 30 minutes of a high-severity alert |
| Backups | Daily backups of the OT workloads and shared services accounts to the backup account in a second region, 30-day write-once retention, separate administrator credentials. One restore of a supervisory cluster (CT-S) was tested on 2026-04-22 and took 11 hours |
| Workforce activity | 96 terminations and 41 transfers in the 12 months to 2026-06-30. The June 2026 phishing simulation click rate was 6.9% |
| Subcontractors | 7 OT subcontractors and integrators: 3 use the broker and signed the security addendum (SUB-1 to SUB-3); 4 use their own remote-support tools (SUB-4 to SUB-7). 9 subcontracts receive FCI (mechanical, electrical, and specialty trades at the federal buildings) |
| Additional role titles | Program managers: Federal Program Manager, State Program Manager, County A Program Manager, County B Program Manager, City and Schools Program Manager. Also the ROC Manager, the County A facilities director, the County A emergency management director, and the Supervisor of Elections operations manager (customer roles) |

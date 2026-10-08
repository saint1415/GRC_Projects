# Scenario facts: Cris Santos Company | Government Services and Facilities | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Contract terms described here are fictional scenario choices unless a regulation is cited.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; Cris Santos is majority owner and CEO) |
| Business | Facilities support contractor (NAICS 561210, Facilities Support Services). The company operates and maintains government buildings under three contracts: building engineering, HVAC and building automation, and electronic security (access control and video) support |
| Location | Florida. Headquarters and the **Remote Operations Center (ROC)** are in a leased office suite. All customer sites are in the same Florida metro area |
| Customers and contracts | **Federal (CT-F):** operations and maintenance (O&M) of one GSA-controlled multi-tenant federal office building (about 420,000 sq ft), GSA Public Buildings Service contract. **State (CT-S):** a state agency regional office complex (3 buildings, about 300,000 sq ft). **County (CT-C):** the county government center (administration tower and annex) and 4 county service centers |
| Revenue | $28.2 million a year (fictional): CT-F $11.4 million, CT-S $7.6 million, CT-C $9.2 million. Under the SBA standard of $47.0 million for NAICS 561210 (13 CFR 121.201), so SBA-small |
| Workforce | 60 employees: 5 executive and administration, 4 finance and HR, 2 IT, 4 operations management (Director of Operations and 3 Site Managers), 7 controls and security systems (Controls Engineering Manager, 4 BAS controls technicians, 2 security systems technicians), 4 ROC operators, 34 building engineers and technicians. 16 staff are assigned to the federal building and hold GSA-issued PIV cards |
| Who owns the building systems | **The customers.** All field equipment (BACnet controllers, door controllers, readers, cameras, NVRs) is government-owned. At the federal building the building automation system (BAS) runs on GSA servers on the GSA Building Systems Network (BSN), which GSA authorizes (FISMA Moderate ATO, per the GSA Building Technologies Technical Reference Guide v3.0, May 2024). At the state and county sites the company runs the supervisory and administration layer on its own platform (section 3) |
| Data the company holds | For CT-S and CT-C: cardholder records for about 5,000 government employees and contractors (name, employer or department, badge photo, credential number, door schedule, access history); 140 face templates in the county face verification pilot (P10); building drawings, security system layouts, and door schedules. For CT-F: work orders and GSA building drawings marked **CUI** (Physical Security category, GSA Order PBS 3490.3 CHGE 1). No FTI, CJI, election systems, or education records (section 1, Not in scope) |
| Federal contract clauses (CT-F) | FAR 52.204-21 (Basic Safeguarding of Covered Contractor Information Systems, NOV 2021); FAR 52.204-23 (Kaspersky, DEC 2023); FAR 52.204-25 (Section 889 telecom and video surveillance, NOV 2021) with representations under 52.204-24/-26; FAR 52.204-30 (FASCSA orders, DEC 2023); FAR 52.204-9 and GSAR 552.204-9 (PIV of contractor personnel). The statement of work incorporates the BTTRG, GSA IT Security Policy (CIO 2100.1), and CUI handling under 32 CFR Part 2002 and GSA Order PBS 3490.3 |
| State contract terms (CT-S) | Cybersecurity exhibit (Fla. Stat. 282.318(4)(h) requires state agency IT service contracts to meet NIST CSF and to assign privacy and security duties). The exhibit requires **NIST SP 800-53 Rev. 5 Moderate** controls for contractor-managed systems that store or process agency data, background screening, incident notice to the agency within 24 hours, and an annual independent assessment |
| County contract terms (CT-C) | Security addendum: compliance with the county's cybersecurity standards (adopted under Fla. Stat. 282.3185(4), NIST CSF-based); incident notice to the county within 24 hours of discovery; fingerprint-based background checks; public records clause under Fla. Stat. 119.0701; the county IT audit asks for a SOC 2 report or an equivalent readiness assessment |
| Sector context | Government Services and Facilities sector (co-Sector Risk Management Agencies: DHS and GSA, NSM-22). The company is a contractor to government facility owners, not a government entity |
| Not in scope | IRS Pub. 1075 (C-GOVERNMENT-R02): no FTI; the state contract states the company has no access to FTI areas or systems. CJIS Security Policy (C-GOVERNMENT-R03): the county contract excludes the sheriff's office and jail, which another contractor serves. VVSG 2.0 (R04): no election systems. FERPA (R05): no education facilities. SLCGP (R07): a grant condition for governments, not contractors. CIRCIA (R06): proposed rule only. FedRAMP: the company is not a cloud service provider to federal agencies; it uses no company system on behalf of GSA. Colorado SB26-189: the company does business only in Florida |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: breach notice and reasonable security (Fla. Stat. 501.171), public records duties of contractors and exemptions for security plans (Fla. Stat. 119.0701 and 119.071(3)), and the customers' own incident reporting duties that the contracts flow down (Fla. Stat. 282.318 and 282.3185) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Majority owner (Cris Santos, CEO) | Approves the security budget; accepts High and Very High risks |
| Chief Operating Officer (COO) | Executive owner of the security program; accepts Moderate risks; signs policies; system owner of the FOTP (SSP system) |
| IT Manager | Information Security Officer (part-time duties alongside IT operations); maintains the risk register, SSP, and POA&M |
| IT/OT Systems Administrator | Cloud tenant, identity provider, endpoints, ROC workstations, site edge gateways |
| Controls Engineering Manager | Owns the BAS supervisory platform, BAS programming standards, and the 4 BAS controls technicians |
| Security Systems Supervisor | Senior security systems technician; administers the access control and video platform for CT-S and CT-C; manages the access control and video integrator (subcontractor) |
| Director of Operations | Owns field operations, the ROC, and after-hours response |
| Site Managers (Federal, State, County) | Customer liaison at each contract; site-level incident notice to the customer; building recovery (manual operation) procedures |
| Contracts Manager | FAR and customer contract compliance, clause flow-down to subcontractors, Section 889 and FASCSA checks, CUI program lead |
| HR Manager | Onboarding, terminations, background checks, PIV sponsorship coordination with GSA, training records |
| Controller | Finance, cyber insurance policy, payroll data owner |
| ROC operators (4) | Monitor BAS and access control alarms 06:00-22:00 on weekdays; on-call technician after hours |
| Access control and video integrator (subcontractor) | Installs and services door controllers, readers, cameras, and NVRs at CT-S and CT-C; has remote access |
| Mechanical and electrical subcontractors | Specialty repairs; receive drawings and work orders |

## 3. Systems

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | BAS supervisory platform: multi-site supervisory server and trend historian (virtual machines) for CT-S and CT-C, about 1,150 customer-owned BACnet field controllers | Company cloud tenant (SYS-04) plus on-site OT networks | Operational data; building drawings | Field controllers keep running their last programs and schedules if the supervisory server is lost. Company-licensed software |
| SYS-02 | Access control and video platform: cloud-hosted access control and video management tenants for CT-S and CT-C, administered by the company; 118 customer-owned door controllers, about 520 readers, about 610 cameras, 9 NVRs | Vendor SaaS plus on-site OT | Yes: cardholder records and access history; video; 140 face templates (pilot) | Door controllers cache credentials and keep working for up to 72 hours without the cloud service. Vendor has a SOC 2 Type 2 report |
| SYS-03 | Remote access gateway (jump host with session recording) | Company cloud tenant | Credentials | Intended single path to site OT networks. Bypassed in practice (see gaps) |
| SYS-04 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes (drawings, controller program backups) | Hosts SYS-01 and SYS-03, file storage for drawings (including GSA CUI drawings), controller program backups, and the backup vault |
| SYS-05 | Site OT edge: company-managed edge firewalls and VPN gateways at the state complex and county sites; 5 on-site engineering workstations | On-premises at customer sites | In transit | The only company equipment on customer networks. Two county workstations run an unsupported OS required by a legacy BAS tool |
| SYS-06 | Identity provider (single sign-on and MFA) | SaaS | Identities only | Protects SYS-04, SYS-07, SYS-08, and the SYS-02 administrator portals |
| SYS-07 | Productivity suite (email, files, chat) | SaaS | Yes (incidental, including CUI drawings emailed to subcontractors) | |
| SYS-08 | Computerized maintenance management system (CMMS) | Vendor SaaS | Federal contract information (FCI) for CT-F; site data | Work orders, asset lists, preventive maintenance for all three contracts |
| SYS-09 | Endpoints | Company-owned | Yes (cached) | 48 laptops, 30 rugged tablets, 6 ROC workstations |
| SYS-10 | GSA-furnished access (CT-F) | GSA | CUI and GSA building data | GSA BAS applications on the BSN, reached only through GSA-provided virtual desktop with a PIV card; 2 GSA-furnished laptops. **GSA's system under GSA's ATO; outside the company's boundary** |
| SYS-11 | HR and payroll | Vendor SaaS | Yes: employee SSNs, bank details, background check results | |
| SYS-12 | Face verification module (pilot) | Feature of the SYS-02 vendor platform plus 2 face-capable readers | Yes: face templates (biometric data) | Pilot at the county government center employee entrance since June 2026 (P10) |

**SSP system (P02):** the *Facility Operations Technology Platform (FOTP)*: SYS-01, SYS-02 (the company-administered tenants and configuration), SYS-03, SYS-04, SYS-05, the ROC workstations and technician laptops in SYS-09, and their interfaces to SYS-06, SYS-08, SYS-12, and the integrator's remote access.

## 4. Current security posture: partially compliant

**In place today:**
- MFA through the identity provider for email, the CMMS, the cloud console, and the access control platform administrator portals
- Endpoint detection and response (EDR) on company laptops and ROC workstations, monitored by the IT Manager during business hours
- Automatic OS patching on company endpoints
- Company-managed edge firewalls and site-to-site VPNs at the state and county sites; no inbound services from the internet
- An access control and video platform vendor with a SOC 2 Type 2 report
- Daily backups of the cloud tenant VMs and file storage, stored in the same cloud account and region
- HSPD-12 process for federal site staff: 16 PIV cards, GSA annual IT security training completed, BSN access only through GSA virtual desktop
- Building recovery (manual operation) procedures for the federal building BAS, written and exercised with GSA in March 2026 as the BTTRG requires; none for the state or county sites
- Fingerprint-based background checks for all staff before assignment
- Cyber insurance with a breach hotline
- A jump host with session recording (SYS-03), deployed in 2025

**Missing or weak, found in the 2026 assessments:**
1. OT remote access bypasses the jump host. BAS technicians connect from laptops to site OT networks over the site VPN with a shared "roc-tech" account on the supervisory server. The integrator uses an always-on remote-support tool on a county engineering workstation with no MFA and no session approval.
2. Shared and default credentials: one shared administrator account on the BAS supervisory server. P07 testing found manufacturer default passwords on 9 BACnet controllers at a county service center and on 1 NVR.
3. No reconciled OT asset inventory. P07 testing found 23 BACnet devices at the county government center that are not in the CMMS asset list.
4. Weak OT segmentation at the 4 county service centers: BAS and door controllers share the county's general building network, and the edge firewall allows any traffic from the county network.
5. No Section 889 or FASCSA process. No supplier screening against FAR 52.204-25 and no quarterly SAM check for FASCSA orders (52.204-30(c)(1)). The headquarters NVR and 4 cameras (bought through a reseller in 2019) have an unconfirmed manufacturer; verification is open.
6. Slow deprovisioning. Company accounts are disabled about 3 business days after departure. P07 found 3 departed technicians still active in the access control administrator portal and 1 PIV card not returned to GSA (FAR 52.204-9(b)).
7. No central log collection or review for the jump host, access control administrator actions, the BAS supervisory server, or edge firewalls. Default retention only.
8. BAS supervisory databases are backed up in the same cloud account as production, not immutable. Controller program backups sit on technicians' laptops. No restore has been tested.
9. No written incident response plan. The customer notice terms (county and state 24 hours, GSA immediate report) are not mapped to a procedure.
10. CUI handling: GSA CUI drawings are stored in the general file share and were emailed unencrypted to a mechanical subcontractor. No CUI training or marking procedure.
11. Subcontractor contracts have no security requirements and do not flow down FAR 52.204-21, 52.204-25, or the customer incident notice terms.
12. Two county engineering workstations run an unsupported OS (a legacy BAS tool requires it). Edge firewall firmware is 3 releases behind.
13. Training is an annual generic video. There is no role-based OT, CUI, or privileged-user training and no phishing exercises.
14. The access control vendor enabled a face verification pilot at the county government center employee entrance (140 enrolled county employees) in June 2026 at the county's request, with no AI assessment and no approved-tools list.
15. No vulnerability scanning of the cloud tenant, the site edge, or OT networks.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | NIST SP 800-53 Rev. 5 (Release 5.2.0) **Moderate** baseline (177 base controls), **binding by contract** for the state contract scope and used as the **benchmark** for the rest of the FOTP, tailored for OT with NIST SP 800-82 Rev. 3. Secondary: FAR 52.204-21 (15 requirements) plus the FAR supply chain clauses 52.204-23, -25, and -30 for the federal contract |
| P08 incident | Intrusion into building access control and automation systems through the integrator's remote-support tool at a county site |
| P09 SOC 2 | The company is a service organization for its county and state customers (it operates their building systems and holds their cardholder data). (a) SOC 2 readiness self-assessment for Security, Availability, and Confidentiality, answering the county IT audit; (b) review of the access control and video platform vendor's SOC 2 Type 2 report |
| P10 AI | Facial recognition for facility access: AI-001 face verification (1:1) pilot at the county government center; AI-002 1:N face identification in public lobbies (county request, not approved) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork (site walkthroughs 2026-07-15 to 2026-07-17) |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork |
| 2026-08-31 | Deliverables approved by the Chief Operating Officer (majority owner for High risks) |

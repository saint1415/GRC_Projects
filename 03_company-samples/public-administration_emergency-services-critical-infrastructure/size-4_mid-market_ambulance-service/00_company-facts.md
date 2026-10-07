# Scenario facts: Cris Santos Company | Emergency Services | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given. This scenario is independent of the other sizes.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (a licensed private ambulance service; privately held; private equity-backed; board with an audit committee) |
| Business | Private ambulance (EMS) provider (NAICS 621910 Ambulance Services): basic life support (BLS), advanced life support (ALS), and critical care transport (CCT) ground ambulance service. It is the exclusive 911 ambulance provider for County A, the 911 provider for 2 of 5 response zones in County B, and an interfacility transport provider for hospitals and nursing facilities in Counties A, B, and C. A second, smaller line of business provides EMS billing services to 4 municipal fire-rescue departments |
| Location | Florida only. **Headquarters** in County A (administration, the revenue cycle and billing services office, the primary communications center, the fleet maintenance shop, and central supply). **13 stations**: Stations 1-9 in County A and Stations 10-13 in County B. The **backup communications center** is at Station 10, about 25 miles from headquarters. That makes 14 network sites |
| Population served | County A has about 520,000 residents. The 2 County B zones have about 210,000 residents. About 730,000 people are in the company's 911 service areas |
| Workforce | 600 employees: 420 field clinicians (230 EMTs, 170 paramedics, 20 critical care nurses and paramedics); 52 communications center staff (44 telecommunicators certified in emergency medical dispatch, 8 supervisors); 48 revenue cycle and billing services staff; 30 fleet, supply, and facilities staff; 50 management, administration, IT, security, compliance, HR, and training staff |
| Volume | About 118,000 911 responses a year (about 85,000 result in transport) and about 65,000 interfacility and non-emergency transports. About 150,000 transports in total, or about 410 a day |
| Fleet | 92 ambulances (54 BLS, 32 ALS, 6 CCT), with 50 to 62 staffed at peak; 14 supervisor and support vehicles |
| Revenue | About $100 million a year (fictional): about $97 million from ambulance services and about $3 million in billing services fees. Not SBA-small: the SBA standard for NAICS 621910 is $22.5 million in average annual receipts (13 CFR 121.201) |
| Payers | Medicare Part B (ambulance supplier), Florida Medicaid, commercial plans, and facility contracts. Medicaid is federal financial assistance, so Section 1557 of the Affordable Care Act applies (45 CFR Part 92) |
| Licenses and county authority | State EMS license for BLS and ALS transport (Fla. Stat. 401.25; Chapter 64J-1, F.A.C.). A certificate of public convenience and necessity from each county in which it operates, Counties A, B, and C (Fla. Stat. 401.25(2)(d)). An exclusive 911 ambulance service agreement with County A and a zone agreement with County B (contracts; terms in section 7). An employed Medical Director (physician), as Fla. Stat. 401.265(1) requires, with 2 associate medical directors |
| HIPAA status | **Covered entity.** A health care provider that transmits claims electronically in HIPAA standard transactions (45 CFR 160.103). With 600 employees it is far above the Medicare "small supplier" exception from electronic claims (fewer than 10 FTEs; 42 CFR 424.32(d)(1)(viii)(B) and (d)(3)(ii)). **Also a business associate** of its 4 billing services clients: the 45 CFR 160.103 definition of business associate includes a person that performs billing on behalf of a covered entity, and paragraph (2) of that definition states that a covered entity may be a business associate of another covered entity |
| County 911 relationship | The County A public safety answering point (PSAP), run by the county sheriff's office, answers 911 calls, sends EMS incidents to the company's CAD over a CAD-to-CAD interface, and transfers medical callers to the company's telecommunicators for emergency medical dispatch. The County B consolidated communications center sends incidents in the company's 2 zones over a second CAD-to-CAD interface and does not transfer callers. The company has **no access** to state or national criminal justice databases or to law enforcement records systems |
| Not in scope | FBI CJIS Security Policy and 28 CFR Parts 20 and 23: the company does not access criminal justice information (see P03; a County A proposal is tracked as a trigger). FCC EAS rules: not an EAS participant. 42 CFR Part 2: not a federally assisted substance use disorder program. Group health plan requirements (45 CFR 164.314(b)): the employee health plan is fully insured and the company receives only summary health and enrollment information (confirmed in P03). Payment cards: patients and client patients pay through the billing platform's hosted payment page, outside company systems (noted, not assessed). Federal contracts: none, so the FAR reporting clauses do not apply |
| State law approach | The company operates only in Florida. Florida law is cited only where a Florida duty is unavoidable: EMS records (Fla. Stat. 401.30; Rule 64J-1.014, F.A.C.), call recording (Fla. Stat. 934.03), and breach notification (Fla. Stat. 501.171). Patients from other states are handled under "each state where affected individuals reside" |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting; receives P01, P07, and P09 results |
| Chief Executive Officer (CEO) | Accepts High risk; approves the risk appetite and the security budget |
| Chief Operating Officer (COO) | Executive sponsor of the security program and system owner of the Dispatch and Patient Care Platform; accepts Moderate risk; signs POL-02 to POL-05 |
| Chief Financial Officer (CFO) | Owns the revenue cycle and billing services lines; cyber insurance |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting; owns POL-01 |
| Director of IT | HIPAA **Security Officer** (45 CFR 164.308(a)(2)); runs IT and the cloud landing zone |
| Security Manager plus 2 security analysts | Security operations, vulnerability management, MSSP oversight, GRC (one analyst is the GRC analyst) |
| Compliance and Privacy Officer | HIPAA **Privacy Officer**; breach determinations; BAAs, including the BAAs where the company is the business associate |
| Medical Director (employed physician) | Clinical oversight of dispatch and patient care protocols; chairs the clinical side of AI review; reviews manual-mode calls after outages |
| Director of Communications | Runs both communications centers; owns manual (paper and radio) dispatch procedures and the backup center |
| Director of Field Operations | Field crews, stations, fleet mobile systems, station alerting |
| Director of Clinical Services | ePCR quality review, clinical training, state data reporting |
| Director of Revenue Cycle | Company billing, the clearinghouse relationship, and billing services delivery to the 4 clients |
| Director of Government Contracts | County agreements, county reporting, and county notices |
| HR Director | Onboarding, terminations, certification tracking, workforce clearance |
| Internal audit (co-sourced firm) | Annual IT audit; performed the P07 assessment |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring; first containment. A business associate |

## 3. Systems

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Computer-aided dispatch (CAD): call entry and emergency medical dispatch, unit recommendation, unit status, AVL map, system status management (unit posting) module, CAD-to-CAD interfaces to both counties | Vendor-licensed software run in the company's dispatch production account (SYS-06): 2 application servers (active and standby), a managed database, an AVL gateway | Yes | Mission-critical for both communications centers. Console users sign in with named accounts federated to the identity provider (since 2025). The CAD mobile client on MDCs uses per-vehicle accounts (see gaps) |
| SYS-02 | Electronic patient care reporting (ePCR) with hospital record delivery and state data export | Vendor SaaS | Yes | System of record for patient care. Business associate with a SOC 2 Type 2 report. Tablets work offline and sync. Includes the narrative drafting feature (AI-002) |
| SYS-03 | Billing and revenue cycle platform with clearinghouse | Vendor SaaS | Yes | Business associate (and, for client data, the company's subcontractor). One workspace for the company and one for each of the 4 billing services clients. Includes the coding assistance module (AI-003) |
| SYS-04 | Identity provider (single sign-on, MFA, conditional access) | SaaS | No (identities only) | Protects CAD console sign-in, ePCR, billing, email, and the cloud consoles. ePCR and scheduling accounts are not provisioned from it (see gaps) |
| SYS-05 | Productivity suite (email, files, chat) and cloud fax | SaaS | Yes | Physician certification statements (PCS) and facility face sheets arrive by cloud fax |
| SYS-06 | Cloud landing zone: 5 accounts (identity and security, shared services, dispatch production, data and reporting, backup) | Public cloud (vendor-agnostic) | Yes | Dispatch production holds SYS-01, the integration engine (CAD-to-CAD, CAD-to-ePCR, ePCR-to-billing), and the call recording archive. Data and reporting holds the reporting database and the posting model (AI-004). Backup is in a second region |
| SYS-07 | Communications centers | On-premises | Yes (in use) | Primary center at headquarters (18 positions) and backup center at Station 10 (6 positions). County P25 radio console positions, UPS, and standby generators at both |
| SYS-08 | Hosted phone system with call recording | Vendor SaaS | Yes | Transferred 911 callers (County A), request lines, and facility lines. Business associate. Recordings copied nightly to the call recording archive |
| SYS-09 | Fleet mobile systems | In vehicles | Yes | 106 cellular routers with GPS (92 ambulances, 14 support vehicles), 92 mobile data computers (MDCs), 210 rugged ePCR tablets, 92 cardiac monitors that send 12-lead ECGs to hospitals through the monitor vendor's cloud relay (business associate) |
| SYS-10 | Networks | On-premises | Yes (in transit) | 14 sites on SD-WAN. Two ISPs at headquarters and at Station 10; one ISP plus cellular backup at the other stations. Station alerting controllers (receive dispatch alerts, sound tones, open bay doors) at every station |
| SYS-11 | Endpoints | On-premises and in vehicles | Yes (cached) | 340 workstations and laptops (including 24 communications center consoles), 210 rugged tablets, 92 MDCs. Device management and full-disk encryption on all |
| SYS-12 | SIEM operated by the MSSP | SaaS | Yes (log fragments) | Receives identity provider, EDR, firewall, SD-WAN, and cloud control-plane logs. CAD application, integration engine, and ePCR audit logs are not sent to it (see gaps) |
| SYS-13 | Workforce systems: scheduling, timekeeping, and credential tracking; HR and payroll; fleet maintenance | SaaS | No PHI (workforce data only) | Scheduling accounts are managed locally, outside the identity provider |
| SYS-14 | AI tools | Vendors and the data and reporting account | Varies | AI-001 call triage (CAD vendor module), AI-002 ePCR narrative drafting, AI-003 billing coding assistance, AI-004 demand forecasting and unit posting recommendations, AI-005 enterprise generative AI assistant (pilot). See P10 |

External systems the company connects to but does not operate: the County A and County B CAD systems and the county P25 radio systems (county-operated), hospital systems that receive ePCR records and 12-lead ECGs, and the state EMS data system (EMSTARS).

**SSP system (P02):** the *Dispatch and Patient Care Platform (DPCP)*: SYS-01, SYS-02, SYS-04, SYS-06, SYS-07, SYS-08, SYS-09, SYS-10, SYS-11, and SYS-12, with their interfaces to SYS-03, the AI tools AI-001 and AI-004, the two county CAD systems, receiving hospitals, and the state EMS data system.

## 4. Current security posture: partially compliant, with tooling

**In place today:**
- MFA through the identity provider for all workforce sign-ins to email, ePCR, billing, the cloud consoles, and CAD consoles (push with number matching)
- EDR on all managed endpoints and cloud virtual machines, monitored 24x7 by the MSSP (communications center consoles run it in detect-only mode; see gaps)
- SIEM operated by the MSSP
- Annual security risk analysis (last done July 2025)
- Security policies adopted in 2023
- Quarterly authenticated vulnerability scanning
- CAD database backups copied to the backup account with 30-day write-once retention; 14-day point-in-time restore on the CAD database
- Backup communications center at Station 10, with an annual relocation drill (last held 2025-11, a facility-loss scenario)
- County P25 radios in every vehicle and at both communications centers; UPS and standby generators at headquarters and Station 10; two ISPs at both communications centers
- BAAs with the ePCR vendor, the billing platform vendor, the CAD vendor, the hosted phone vendor, the MSSP, the cardiac monitor relay vendor, and the cloud provider
- Full-disk encryption and device management on laptops, tablets, and MDCs
- Annual HIPAA and security training and quarterly phishing simulations
- Background checks, driving record checks, and state certification checks at hire
- Annual internal IT audit by a co-sourced firm
- Cyber insurance

**Missing or weak, found in the 2026 assessments:**
1. CAD recovery is unproven. Only a CAD database restore has been tested (October 2025). The CAD application servers, integration engine, and AVL gateway have never been rebuilt in a test. The integration engine and the call recording archive are not covered by write-once backups. Both communications centers depend on the same cloud CAD, so the backup center protects against losing a building, not against losing CAD.
2. Communications center consoles run EDR in detect-only mode and are patched quarterly because of CAD client compatibility. They were last patched in May 2026.
3. MDCs sign in to CAD with per-vehicle shared accounts and no MFA. The CAD mobile client is not federated with the identity provider.
4. Access reviews are annual (last completed January 2026). Field staff turnover is high. ePCR and scheduling accounts are not provisioned from the identity provider, and some stay active after departures.
5. Station networks are flat at 9 of 13 stations: crew Wi-Fi, station alerting controllers, and workstations share one segment. Central management covers 71 of 106 vehicle routers.
6. CAD application, integration engine, and ePCR audit logs do not reach the SIEM. ePCR access is reviewed only after a complaint, and CAD queries are never reviewed.
7. Third parties: the CAD-to-CAD links with both counties have no written interconnection security terms. 6 of 58 vendors with PHI access have no BAA on file. Vendor reviews happen only at onboarding.
8. Billing services: the company has no SOC 2 report, and 2 of the 4 clients require a SOC 2 Type 2 report at renewal. Client separation in the billing platform relies on vendor workspace settings that the company has never reviewed.
9. No AI governance. AI-001 to AI-004 were enabled by business owners or arrived as vendor features without a security, privacy, or compliance review.
10. The incident response plan (2023) does not cover a CAD outage that affects both communications centers. The last exercise with the counties was in 2024, and manual dispatch has never been drilled for a ransomware scenario.
11. Policies exist, but supporting standards (configuration, logging, vendor, fleet devices, AI) are thin.
12. PCS and facility paperwork received before 2025 sit in the cloud fax archive and a shared mailbox with 2-year automatic deletion, short of Medicare's 7-year documentation rule (42 CFR 424.516(f)). Since January 2025, PCS documents are attached to the billing record.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incidents | **Two incident types:** (1) ransomware encrypts the CAD servers and the communications center consoles, forcing manual dispatch at both centers, with possible PHI theft (the registry scenario: computer-aided dispatch outage from ransomware); (2) a breach at the billing platform vendor that exposes company PHI and the PHI of the 4 billing services clients, where the company is both a covered entity and a business associate. Both runbooks integrate crisis management and legal |
| P09 SOC 2 | Readiness for a SOC 2 Type 2 examination of the **billing services** the company provides to municipal fire-rescue departments (Security, Availability, Processing Integrity, Confidentiality); plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio: AI-001 call triage (the registry use case), AI-002 ePCR narrative drafting, AI-003 billing coding assistance, AI-004 demand forecasting and unit posting, AI-005 enterprise generative AI assistant |
| Cloud | Multi-account landing zone, vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only in an equivalents table |
| Registry defaults | Kept as given. The primary system is the CAD and ePCR platform (named the DPCP); the P08 incident is the CAD ransomware outage; the P10 portfolio includes AI-assisted call triage. At this size a second incident type and a portfolio of AI uses are added, as the Mid-Market tier requires |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | Security risk analysis, BIA interviews, and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (station alerting finding on 2026-08-12) |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness assessment, vendor SOC 2 reviews, and AI portfolio assessment |
| 2026-09-16 | Deliverables approved (COO for Moderate and below; CEO for High and Very High) and presented to the board audit committee |

## 7. Facts added during the Phase 5 build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Revenue split | About $56 million from 911 transports (about $153,000 a day), about $41 million from interfacility transports (about $112,000 a day, about 42% of revenue), and about $3 million in billing services fees (about $8,200 a day). Company collections are about $1.87 million a week (about $373,000 per business day) from about 600 claims per business day |
| Billing services | 4 municipal fire-rescue departments, each a HIPAA covered entity. About 70,000 client transports and about $52 million of client collections a year (about $1.0 million a week; about 270 client claims per business day). 18 of the 48 revenue cycle staff work on billing services; the revenue cycle has 14 certified coders. Client agreements set claim submission within 5 business days of a completed ePCR, with service credits after 5 business days of delay. Client BAAs require breach and security incident notice to the client within 10 business days of discovery, plus quarterly summaries of unsuccessful attempts. Two clients require a SOC 2 Type 2 report at renewal (2027 and 2028); both accepted a Type 1 report by 2027-03-31 as an interim step. No client BAA delegates patient notices to the company |
| County A agreement (contract) | Exclusive 911 ambulance provider. 90th percentile response-time standards measured monthly; liquidated damages of $10,000 for each month that compliance falls below 90%. Written communications center continuity plan reviewed by the county EMS office each year. Notice to the County A PSAP of any dispatch system outage longer than 15 minutes. Notice of security incidents affecting county data within 24 hours. Annual joint exercise. Unit-hour and fleet readiness reporting. In May 2026 County A proposed sharing law enforcement premise hazard and officer-safety flags through CAD-to-CAD (on hold) |
| County B zone agreement (contract) | Monthly response-time report for the 2 company zones; notice of security incidents within 72 hours; annual joint exercise. The last joint exercise with either county was in 2024 |
| Volumes | About 320 County A and about 90 County B 911 responses a day; about 178 interfacility trips a day; about 180 request-line calls a day; about 120 PCS documents a day; about 25 12-lead ECG transmissions a day; about 1,400 crew shifts a week; payroll of about $1.6 million every 2 weeks. CAD holds about 450,000 patients from 3 years of incidents. Records go to 14 receiving hospitals; delivery problems persist at 2 |
| Recovery facts | CAD database: 14-day point-in-time restore and 30-day write-once copies in the backup account; restore tested once in October 2025; a P07 test restore on 2026-08-12 took 38 minutes. CAD moved to the cloud landing zone in 2024; console sign-in was federated to the identity provider in 2025. The backup center is about 25 miles from headquarters; its last relocation drill was in November 2025. Plan: 6 pre-imaged spare console laptops at each center and a warm CAD standby in the backup region by 2027-06-30 |
| Vendor recovery and notice terms | ePCR vendor: RTO 4 hours, RPO 15 minutes; 72-hour security incident notice; BAA 30 days for breaches. Billing platform vendor: RTO 24 hours, RPO 4 hours; BAA 30 days for breaches; client data covered by a 2024 BAA addendum; AI coding model excluded from its SOC 2 Processing Integrity testing. CAD vendor: reinstall support within 8 business hours; BAA 60 days; its SOC 2 report covers support operations only. Hosted phone vendor: failover within 15 minutes; BAA 30 days. MSSP: call within 30 minutes on high severity; BAA 10 days. The patient statement mail vendor and the cloud fax BAAs cover company patients only |
| Cyber insurance and lenders | $10 million aggregate limit, $250,000 retention; the carrier's panel supplies breach counsel and forensics; the policy requires notice through the carrier hotline before incident vendors are engaged. The credit agreement requires notice to the lender agent within 2 business days of a severity 1 incident |
| Workforce activity | 128 departures and 41 transfers between field and communications roles in the 12 months to 2026-06-30; 186 new ePCR accounts in that period. Last access review January 2026. Annual training completion 94% (36 field staff overdue at P07). June 2026 phishing click rate 6.9%. POL-05 acknowledgment rate 95% |
| Privileged access | 31 privileged accounts across the cloud, the identity provider, and CAD; 11 communications supervisors hold CAD administrator rights; 4 engineers hold standing cloud administrator roles. The identity provider has 2 break-glass accounts (tested June 2026); CAD and the cloud organization have none |
| Devices and networks | 642 managed endpoints (340 workstations and laptops, 210 tablets, 92 MDCs), all with full-disk encryption. 18 cloud and on-premises servers. 71 of 106 routers are centrally managed; 40 routers have a second carrier SIM. 13 station alerting controllers, reachable from crew Wi-Fi at the 9 flat stations; 4 had the manufacturer default password until 2026-08-14; the station alerting vendor keeps a persistent internet connection to them |
| Vendors | 58 vendors with PHI access; 52 BAAs on file; 9 Tier 1 and 21 Tier 2 under the P09 tiering; about 700 vendors in accounts payable. Tier 1 reviews not yet done: the cardiac monitor relay vendor and the SD-WAN provider |
| Compliance history | The July 2025 risk analysis produced 15 actions, 6 still open at the 2026 analysis. 29 security incidents logged in 2025-2026; 5 privacy incident files; 2 breaches under 500 individuals notified 38 and 44 days after discovery; the 2025 HHS log was submitted on 2026-02-18. The benefits broker confirmed the fully insured plan arrangement on 2026-07-15 |
| AI tools | AI-001: shadow period 2026-02-01 to 2026-04-30, advisory mode (upgrade prompts only) at the primary center since 2026-05-01, limited to English-language calls from 2026-09-16; the order form allows 30-day audio retention and does not exclude training. AI-002: pilot with 60 paramedics since March 2026. AI-003: in use since November 2025; about 35% of claims were coded straight through, about 52,000 claims through 2026-09-16 for the company and 2 of the 4 clients. AI-004: in use since January 2026, retrained monthly by analysts. AI-005: pilot with 40 administrative staff since August 2026 under an enterprise agreement with a BAA and a no-training term |
| FY2027 security plan | Approved by the CEO 2026-09-16: $1.02 million one-time and $380,000 a year (details in P01 section 4) |
| Additional role titles | Controller; Fleet and Supply Manager; associate medical directors (2); communications supervisors (8); 2 named communications staff to hold a new CAD configuration role |
| Terminology | "Dispatch and Patient Care Platform (DPCP)" is the SSP system in P02, identifier CSC-DPCP-01. The P09 SOC 2 system is "EMS billing services" |

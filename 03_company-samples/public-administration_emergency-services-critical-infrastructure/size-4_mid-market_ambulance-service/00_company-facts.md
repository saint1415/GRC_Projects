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
| HIPAA status | **Covered entity.** A health care provider that transmits claims electronically in HIPAA standard transactions (45 CFR 160.103). With 600 employees it is far above the Medicare "small supplier" exception (fewer than 10 FTEs) in 42 CFR 424.32(d)(1). **Also a business associate** of its 4 billing services clients: the 45 CFR 160.103 definition of business associate includes a person that performs billing on behalf of a covered entity, and paragraph (2) of that definition states that a covered entity may be a business associate of another covered entity |
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

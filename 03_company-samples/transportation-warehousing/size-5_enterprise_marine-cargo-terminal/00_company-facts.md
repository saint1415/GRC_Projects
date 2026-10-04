# Scenario facts: Cris Santos Company | Transportation and Warehousing | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given. Regulatory facts were checked against eCFR (point in time 2026-09-23) and the Federal Register on 2026-10-04.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; not a smaller reporting company) |
| Business | Multi-port marine cargo terminal operator (NAICS 488320 Marine Cargo Handling). Operates 8 container, ro-ro and multipurpose terminals at 6 U.S. ports under long-term concessions and leases from port authorities (landlord ports). Also sells two technology services to outside customers (SL-1 and SL-2 below) |
| Location | Headquartered in Florida, with the enterprise planning center and the security operations center at headquarters. Terminals in Florida, Georgia, South Carolina, and Texas. **State law is handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Terminals | 8 terminals (T-01 to T-08), listed below. Each is a separate MTSA facility with its own Facility Security Plan (FSP) and Facility Security Officer (FSO) |
| Volume | About 8.8 million container moves a year, about 4.1 million tons of breakbulk and project cargo, and about 640,000 vehicles (ro-ro). About 85 vessel calls a week and about 22,000 truck gate transactions a day across all terminals |
| Workforce | 12,000 employees: about 1,850 corporate and shared services (including about 640 in IT, digital services and security); about 6,500 terminal operations (planners, clerks, superintendents, equipment operators); about 2,250 maintenance and engineering; about 1,400 security (FSOs, supervisors and officers) |
| Contract labor | Longshore labor for vessel and yard work is ordered per shift through the hiring hall at each port: about 2,500 to 4,500 workers on a typical day across the 6 ports. They are not employees, but they use OT (crane, RTG and straddle carrier cabs) and vehicle-mounted terminals (VMTs) |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day. Terminal services about $4.67 billion; SL-1 about $38 million; SL-2 about $96 million |
| Customers | About 25 ocean carriers (about 40 vessel services); about 4,100 registered trucking companies (about 38,000 registered drivers); about 900 cargo owners, customs brokers and forwarders on SL-1; 4 SL-2 client terminals |
| MTSA status | **All 8 terminals are facilities regulated under 33 CFR Part 105.** Each receives foreign cargo vessels greater than 100 gross register tons (33 CFR 105.105(a)(4)); the container terminals also receive vessels subject to SOLAS chapter XI (105.105(a)(3)). Each has a Coast Guard-approved FSP, an FSO, TWIC-based access control to secure areas, and a Facility Security Assessment (FSA) that must consider measures to protect computer systems and networks (105.305(c)(1)(v)). The 6 ports sit in 5 Coast Guard Captain of the Port (COTP) zones |
| Cyber rule status | **33 CFR Part 101, Subpart F applies to all 8 facilities** (101.605(a)). No size threshold. Rule effective 2025-07-16 (90 FR 6298, 2025-01-17). The company will submit **one Cybersecurity Plan covering T-01 to T-07**, which have similar operations on the enterprise platform, with facility-specific annexes as 101.630(d)(2) requires, and a **separate Plan for T-08** until it migrates to the enterprise platform. One person is the Cybersecurity Officer (CySO) for all 8 facilities (101.625(b)) |
| MARSEC Directives | T-03, T-04 and T-07 operate ship-to-shore (STS) cranes manufactured by People's Republic of China (PRC) companies, so MARSEC Directives 105-4 (notice of availability 89 FR 13726, 2024-02-23) and 105-5 (notice 89 FR 91413, 2024-11-19) apply to those cranes. Their content is SSI. The FSOs and the CySO hold them; these deliverables record status only |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; CTPAT partner since 2019 (marine port authority and terminal operator category); growth by acquisition (T-08, closed 2025-11-03); a semi-automated container yard at T-01; two service lines sold to outside customers |
| Not in scope | TSA Security Directives (not a rail, pipeline or aviation operator). CMMC and FAR clauses (no federal or DoD contracts; military cargo moves through the terminals under ocean carriers' contracts, not the company's). Payment cards: carriers, truckers and cargo owners pay through a hosted payment page run by a payment service provider; card data never reaches company systems (noted, not assessed) |
| State law approach | Breach notification for employee, truck driver and longshore worker personal information follows each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example. The Subpart F federalism clause (101.610) makes Subpart F preempt conflicting state or local law for Part 105 facilities |

**Terminals**

| ID | Terminal | State | Type | Volume | Notes |
|---|---|---|---|---|---|
| T-01 | Port A container terminal | Florida | Container, semi-automated yard | About 2.4 million moves; 14 STS cranes; 30 automated stacking cranes (ASCs) in 15 yard blocks; on-dock rail | Equipment control system for the automated yard; automation vendor remote access (gap 3) |
| T-02 | Port A ro-ro and multipurpose terminal | Florida | Ro-ro, breakbulk | About 300,000 vehicles; 2 mobile harbor cranes | |
| T-03 | Port B container terminal | Florida | Container | About 1.3 million moves; 8 STS cranes | PRC-manufactured STS cranes (MARSEC Directives 105-4 and 105-5) |
| T-04 | Port C container terminal | Georgia | Container | About 2.0 million moves; 12 STS cranes; on-dock rail | PRC-manufactured STS cranes |
| T-05 | Port C breakbulk and ro-ro terminal | Georgia | Breakbulk, ro-ro, project cargo | About 340,000 vehicles; 2.2 million tons; 3 mobile harbor cranes | |
| T-06 | Port D container terminal | South Carolina | Container | About 1.1 million moves; 7 STS cranes | |
| T-07 | Port E container terminal | Texas | Container | About 1.4 million moves; 9 STS cranes; 600 reefer plugs | PRC-manufactured STS cranes; gate, RTG and reefer systems share a VLAN (gap 2) |
| T-08 | Port F multipurpose terminal (acquired 2025-11-03) | Texas | Container and breakbulk | About 0.6 million moves; 1.9 million tons; 4 STS cranes | Legacy systems (gap 1); about 520 employees |

**Service lines sold to outside customers**
| ID | Service line | Customers | Assurance today |
|---|---|---|---|
| SL-1 | Cargo Visibility and Appointment Platform (CVAP): container availability, holds, vessel schedules, truck appointments, and APIs for all 8 terminals | Trucking companies, cargo owners, customs brokers, forwarders and carriers. Free to truckers; subscription for API users | SOC 2 Type 2 (Security, Availability) since the 2025 period |
| SL-2 | Hosted terminal technology services: the company runs TOS and gate environments on its enterprise platform for 4 client terminals (C-01 to C-04) at other U.S. ports | 3 independent terminal operators and 1 port authority-operated public terminal. Each client is the MTSA facility operator with its own FSP and Cybersecurity Plan, and relies on the company for systems it has delegated (101.615) | None. Clients have asked for a SOC 2 Type 2 report with Processing Integrity by 2027 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board (audit committee; risk committee) | Cyber oversight (Item 106 governance). The risk committee receives quarterly cyber risk reporting; the audit committee oversees Internal Audit, SOX and disclosure controls |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee; approve any ransom decision with the General Counsel |
| Chief Operating Officer (COO) | Business owner for terminal operations; authorizing official for the SSP system (P02); chairs the crisis management team |
| Chief Information Security Officer (CISO) | Program owner; chairs the policy governance committee |
| Director of Maritime Cybersecurity | **Cybersecurity Officer (CySO) for all 8 facilities**, designated in writing 2025-10-01 (101.620(b)(3); 101.625(b)); reports to the CISO. Reachable 24x7 through the SOC |
| Terminal OT Security Leads (one per terminal) | **Alternate CySOs** for their terminal (T-08 alternate designated 2026-02-16) |
| Vice President, Maritime Security | Company-level security lead; oversees the 8 FSOs, MTSA reporting, TWIC and drills |
| Facility Security Officers (one per terminal) | FSO under 33 CFR 105.205; FSP, TWIC access control, CCTV, MTSA drills and exercises, MTSA reports |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment and the independent Cybersecurity Plan audits (101.630(f)(4)) |
| General Counsel | Chairs the disclosure committee |
| GRC team (10), Security Operations Center (24x7, in-house), Internal Audit (in-house, with co-sourced OT specialists) | Three lines model |
| Disclosure committee | 8-K materiality decisions (section 7 lists members) |

## 3. Systems

| ID | System | Hosting | Critical IT or OT? (101.615) | Notes |
|---|---|---|---|---|
| SYS-01 | Enterprise terminal operating system (TOS) platform: vessel and yard planning, equipment dispatch, gate module, billing interface. Commercial TOS software, customer-managed | Cloud provider A, one production environment per terminal: 7 company terminals (T-01 to T-07) and 4 SL-2 client terminals (11 environments) | Critical IT | System of record for every container, its location, holds and hazardous cargo class. One platform serves 11 terminals (gap 6) |
| SYS-02 | Gate automation at T-01 to T-07: OCR portals, TWIC readers tied to the physical access control system (PACS), driver kiosks, gate transaction servers | On premises at each terminal gate complex | Critical IT | T-07 gate servers share a VLAN with OT (gap 2) |
| SYS-03 | OT: STS cranes (54) and mobile harbor cranes, RTGs, straddle carriers, the T-01 automated stacking crane yard and its equipment control system, programmable logic controllers (PLCs), human-machine interfaces (HMIs), reefer monitoring, about 1,900 VMTs on yard tractors and straddle carriers | On premises, in OT zones at each terminal | Critical OT | About 4,430 OT devices estimated; 88% inventoried (gap 4) |
| SYS-04 | EDI and integration hub: B2B gateway (AS2, SFTP), API gateway, links to carriers, port community systems at the 6 ports, a customs data exchange service that delivers release and hold status from U.S. Customs and Border Protection, and rail partners | Cloud provider A | Critical IT | Port community systems and the customs data exchange have no security terms (gap 9) |
| SYS-05 | Identity platform: single sign-on (SSO), MFA, privileged access management (PAM), identity governance | SaaS identity service plus PAM in Cloud provider A | Critical IT | T-08 still on its own directory (gap 1) |
| SYS-06 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers (DC-1 Florida, DC-2 Georgia) | Cloud provider A: TOS platform, EDI hub, PAM. Cloud provider B: SL-1 platform, data and analytics, AI and machine-learning platform. DC-1 and DC-2: network core, central PACS and video servers, offline backup vault copies | Critical IT (Cloud A, DC-1, DC-2) | |
| SYS-07 | Enterprise and terminal networks: SD-WAN, terminal LANs, OT zones behind internal firewalls, private LTE and Wi-Fi for equipment, vendor access gateway | On premises and carriers | Critical IT | OT zones complete at T-01 to T-06 (gap 2) |
| SYS-08 | Endpoints: about 11,000 workstations, laptops, rugged tablets and VMTs | All sites | Critical IT (operations endpoints) | EDR on all endpoints except about 40% at T-08 (gap 1) |
| SYS-09 | Physical security systems: PACS and TWIC readers, about 4,200 CCTV cameras, video management | Terminals, with central servers in DC-1 | Critical IT (supports the FSPs) | Owned by the Vice President, Maritime Security |
| SYS-10 | ERP, finance, payroll and HR, and longshore labor ordering and timekeeping | SaaS | No (SOX-relevant) | SOX IT general controls tested annually |
| SYS-11 | SL-1 Cargo Visibility and Appointment Platform (CVAP) | Cloud provider B, managed containers, second-region standby | Critical IT (the appointment system feeds every gate) | SOC 2 Type 2 since the 2025 period |
| SYS-12 | Third parties: about 1,300 vendors, 210 of them tier 1 or 2 (network, OT or data access), including the TOS software vendor, 4 crane and automation OEMs, the OCR vendor, the customs data exchange service and the port community systems | External | Mixed | Tiered third-party risk program; Subpart F notification clauses missing at 31% of tier-1 IT and OT vendors (gap 9) |
| SYS-13 | T-08 legacy estate: on-premises legacy TOS and gate system, own directory, flat IT and OT network | On premises at T-08 | Critical IT and OT | Migration to SYS-01 and the enterprise network due 2027-06-30 |
| SYS-14 | AI portfolio (12 use cases) | Mostly Cloud provider B and vendor SaaS | See P10 | Governed by an AI governance committee formed in 2025 |

**SSP system (P02):** the *Enterprise Terminal Operating and Gate Platform (ETOP)*: the SYS-01 TOS platform (all 11 terminal environments in Cloud provider A), SYS-02 gate automation at T-01 to T-07, and the TOS-related channels of the SYS-04 integration hub, with interfaces to SYS-03 (OT), SYS-09 (PACS) and SYS-11, inheriting common controls from the enterprise platform.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A mature program aligned to CSF 2.0, with a policy hierarchy of policies, standards, procedures and exceptions
- Annual enterprise risk analysis tied to ERM (NIST IR 8286)
- A CySO designated in writing for all 8 facilities (2025-10-01), with an alternate at each terminal and a 24x7 contact through the SOC
- Subpart F training: 96% of employees trained by the 2026-01-12 deadline, 100% by 2026-03-13 (101.650(d)(4))
- 24x7 SOC with EDR, SIEM and cloud threat detection; PAM; quarterly access certification
- IT/OT segmentation with OT zones at T-01 to T-06, and passive OT network monitoring at T-01 to T-05
- An enterprise vendor access gateway (session approval, MFA, recording) used by 2 of 4 crane and automation OEMs
- Immutable backups in separate cloud accounts with an offline copy in DC-2; annual DR tests for tier-1 systems
- A tiered third-party risk program
- Annual SOC 2 Type 2 for SL-1
- SEC Item 106 disclosure in the 10-K; a disclosure committee and materiality playbook
- CTPAT partner (since 2019); quarterly MTSA drills and annual exercises at every terminal, with cyber scenarios added in 2026

**Targeted gaps:**
1. **T-08 integration.** T-08 (acquired 2025-11-03) runs a legacy on-premises TOS and gate system and its own directory with no MFA for TOS users, has a flat IT and OT network, has EDR on about 60% of endpoints, sends no logs to the SIEM, and has a crane OEM modem that is always on. Migration to the enterprise platform is due 2027-06-30.
2. **OT segmentation and monitoring incomplete.** OT zones are complete at T-01 to T-06. At T-07, gate servers, RTG controllers and reefer monitoring share one VLAN; T-08 is flat. OT network monitoring covers T-01 to T-05 only (101.650(h)).
3. **OEM remote access.** The automation vendor for the T-01 automated yard and one STS crane OEM (cranes at T-03, T-07 and T-08) use their own remote tools with persistent tunnels, outside the vendor access gateway; sessions are not recorded (101.650(e)(3)(v), (f)(3)).
4. **OT accounts and passwords.** The OT inventory is 88% complete (about 3,900 of an estimated 4,430 devices). About 340 PLCs and HMIs cannot enforce password strength, lockout or MFA, and their compensating controls are not documented (101.650(a)(2)-(4)). RTG HMIs at 4 terminals use shared operator accounts (101.650(a)(6)).
5. **OT KEVs.** IT Known Exploited Vulnerabilities (KEVs) are remediated within the 14-day target 96% of the time, but 37 KEVs on OT components were open beyond 30 days without documented compensating controls at fieldwork (101.650(e)(3)(i)).
6. **TOS platform concentration and recovery.** One TOS platform runs 11 terminal environments in Cloud provider A. The 2026-05-16 DR test restored 3 environments in 7.5 hours against a 4-hour RTO; cross-region failover has not been tested for the other 8 environments.
7. **Longshore and contractor training.** Training or supervised-access arrangements for longshore workers who use OT are in place at the hiring halls of 4 of 6 ports (101.650(d)(1)(v), (d)(3)). OT-specific training is complete for 69% of maintenance contractors.
8. **SL-2 client obligations.** The 4 client terminals rely on the company's platform for critical IT they have delegated (101.615). The agreements promise incident notice "within 24 hours", which does not support the clients' immediate reporting under 33 CFR 6.16-1 or the "without delay" vendor notice in 101.650(f)(2). SL-2 has no SOC 2 report.
9. **Port partner and vendor terms.** The port community systems at the 6 ports and the customs data exchange service have no contractual security or notification terms, and 31% of tier-1 IT and OT vendors lack the Subpart F notification clause (101.650(f)(2)).
10. **Materiality and Coast Guard reporting alignment.** The materiality playbook was last exercised in 2025-10, before the T-08 acquisition and before 3 disclosure committee members joined. It has no criteria for a multi-terminal outage or an OT safety event, and does not sequence immediate 6.16-1 reports in several COTP zones with public disclosure.
11. **Logging gaps.** T-07 OT and gate logs and all T-08 logs are not in the SIEM; OT logs are kept locally for 30 days (101.650(c)(1)).
12. **AI.** 12 AI use cases, 8 reviewed by the AI governance committee. AI-001 (container and berth scheduling optimization) is in production at T-01, T-03 and T-04 and piloting at T-06 and T-07; appointment-slot fairness has not been tested, and the independent constraint check runs only at T-01.
13. **Cybersecurity Plan progress.** The Cybersecurity Assessment network analysis is complete for T-01 to T-05; the Plan for T-01 to T-07 is about 60% drafted. Target submission is 2027-04-30, ahead of the 2027-07-16 deadline (101.655).

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| Regulation (P03) | Primary: USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101 Subpart F, for all 8 facilities. Also analyzed: maritime cyber incident reporting (33 CFR 6.16-1) and MTSA reporting (101.305); the FSA computer-systems duty (105.305(c)(1)(v)); MARSEC Directives 105-4 and 105-5 (status only, SSI); SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach notification laws (generic, Florida worked example); CTPAT (voluntary partner) |
| P08 incident | Ransomware disrupting the TOS platform at several terminals and the SL-2 client environments, including an **SEC materiality assessment and 8-K Item 1.05** step, Coast Guard, FBI and CISA reports in each affected COTP zone under 6.16-1, SL-2 client notification, and a multi-state breach-notification workflow for driver and employee personal information |
| P09 | SOC 2 Type 2 readiness across two service lines, all five categories considered: SL-1 (Security, Availability, Confidentiality, Processing Integrity added; Privacy out of scope with reasons) and SL-2 (Security, Availability, Confidentiality, Processing Integrity) |
| P10 | Enterprise AI portfolio (12 use cases) under the AI governance committee, with a full assessment of AI-001 container and berth scheduling optimization |
| Cloud | Multi-cloud (vendor-agnostic) with common controls; colocation data centers; OT edge at each terminal |

**Registry defaults kept.** The primary system (TOS and gate automation), the incident (ransomware disrupting the TOS) and the AI use case (container and berth scheduling optimization) fit an enterprise terminal operator and were kept. At this size the TOS is one platform serving many terminals and outside clients, so the SSP covers the platform, the incident spans several terminals and COTP zones, and the AI use case is built in-house and assessed inside a 12-use-case portfolio.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2025-07-16 | Subpart F effective (90 FR 6298) |
| 2025-10-01 | CySO designated in writing for all 8 facilities |
| 2025-11-03 | T-08 acquisition closed |
| 2026-01-12 | Subpart F training deadline for all personnel and key personnel (101.650(d)(4)). 96% of employees met it |
| 2026-06-01 to 2026-07-31 | Enterprise BIA, risk analysis and gap analysis (evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line). OT tests at night with no vessel at berth |
| 2026-08-19 | AI governance committee portfolio review |
| 2026-09-08 | Executive risk committee approval |
| 2026-09-10 | Results to the risk committee and the audit committee of the board |
| 2027-04-30 | Target submission of both Cybersecurity Plans to the COTPs |
| 2027-07-16 | Deadline for the first Cybersecurity Assessment (101.650(e)(1)) and Cybersecurity Plan submission (101.655) |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| Controller | SOX program owner; member of the disclosure committee |
| Vice President, Terminal Technology | System owner of ETOP (P02) and owner of SL-2 |
| Vice President, Digital Services | Owner of SL-1 (CVAP) |
| Vice President, Integration Management Office | Integration of T-08 |
| Vice President, Labor Relations | Hiring hall arrangements and collective bargaining agreements |
| Vice President, Corporate Communications | Media, customer and port partner communications during incidents |
| Vice President, Investor Relations | Investor communications; member of the disclosure committee |
| Vice President, Data and Analytics | Chairs the AI governance committee; owns the data science team |
| Chief Commercial Officer | Carrier and customer contracts |
| Chief People Officer | Workforce onboarding, terminations and training records |
| Terminal General Managers (8) | Business owners at each terminal |
| Director of Enterprise Planning | Enterprise vessel and yard planning center; business owner of AI-001 |
| Director of Security Operations | Runs the SOC; incident commander for security incidents |
| Director of Identity and Access Management | Identity platform (SYS-05) |
| Director of Cloud Platform Engineering | Cloud landing zones in both clouds (common control provider) |
| Director of Network Engineering | Enterprise network, SD-WAN, terminal LANs (common control provider) |
| Director of OT Engineering | Cranes, automation and controllers; OEM relationships; OT zones |
| Director of Endpoint Engineering | Workstations, VMTs, EDR and endpoint baselines (common control provider) |
| Director of Third-Party Risk Management | Vendor tiering, contract clauses, SOC report reviews (in the GRC team) |
| TOS Platform Manager | Day-to-day TOS platform administration (reports to the Vice President, Terminal Technology) |
| Disclosure committee members | General Counsel (chair), CFO, Controller, CISO, Chief Risk Officer, COO, Vice President, Investor Relations; advised by outside securities counsel. Three members joined in 2026 |

**SL-2 clients.** C-01 to C-04: three independent terminal operators (Gulf coast and Atlantic coast ports) and one port authority-operated public terminal. Together about 1.6 million container moves a year. Each has its own TOS environment on ETOP, its own users (about 1,150 client user accounts in total), and its own FSP, FSO, CySO and Cybersecurity Plan.

**Personal information held.** About 12,000 employee records (SYS-10); about 38,000 registered truck driver profiles with name, phone, driver license number and state, and TWIC status (SYS-11 and the gate module); gate and PACS records with TWIC card identifiers (FASC-N) for drivers and longshore workers (SYS-09), which the FSO must keep for 2 years and protect from unauthorized access or disclosure (33 CFR 105.225(a), (b)(9), (c)). Card data is not held.

**Recovery figures.** Revenue of about $4.8 billion a year is about $13.2 million per calendar day. The BIA (P05) scales its dollar thresholds to this figure.

**Cybersecurity Plan approach.** One Plan for T-01 to T-07 (similar operations on ETOP; 101.630(d)(2)) with an annex for each terminal, and one Plan for T-08. Both are SSI (101.630(b)) and kept by the CySO. The annual Plan audits will be performed by Internal Audit, whose staff have no cybersecurity duties at the terminals (101.630(f)(4)).

# Scenario facts: Cris Santos Company | Transportation and Warehousing | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given. Regulatory facts were checked against eCFR (point in time 2026-09-23), the Federal Register and the Florida Statutes (2026) between 2026-09-26 and 2026-10-04.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held corporation; private equity-backed; board with an audit committee) |
| Business | Marine cargo terminal operator (NAICS 488320 Marine Cargo Handling). Operates two terminals at two Florida ports under long-term leases from the port authorities (landlord ports), plus an off-dock empty container and chassis depot |
| Terminal 1 (T1) | Container terminal, about 180 acres. 3 container berths, 7 ship-to-shore (STS) cranes, 24 rubber-tired gantry cranes (RTGs), 8 reach stackers, 90 yard tractors with vehicle-mounted terminals (VMTs), 1,200 reefer plugs with a remote reefer monitoring system, and a 12-lane truck gate with OCR portals and driver kiosks. The headquarters office is in the T1 administration building |
| Terminal 2 (T2) | Multipurpose terminal (breakbulk, project cargo and roll-on/roll-off vehicles), about 95 acres, at a second Florida port. 2 berths, 2 mobile harbor cranes, 40 yard tractors with VMTs, vehicle storage for about 9,000 units, and a 4-lane truck gate with OCR portals. **Acquired in 2024**; moved onto the company TOS in 2025, but its network and OT were not yet integrated |
| Depot | Off-dock empty container and chassis depot about 5 miles from T1, with a 2-lane gate. It receives no vessels and has no Facility Security Plan (company reading of 33 CFR 105.105(a); to be confirmed with the Captain of the Port). It connects to the TOS over the company network |
| Volume | T1: about 620,000 container moves a year, about 14 vessel calls a week from 9 carrier services, about 3,000 truck gate transactions a day. T2: about 900,000 tons of breakbulk and project cargo and 160,000 vehicle units a year, about 6 vessel calls a week, about 600 truck transactions a day. Depot: about 400 truck transactions a day |
| Location | Florida only: T1, T2, the depot and the headquarters office |
| Workforce | 600 employees: 44 executive, finance, HR, legal and procurement; 46 commercial, customer service and billing; 248 operations (planners, shift superintendents, gate and yard clerks, checkers); 150 maintenance and engineering (mechanics, crane electricians, controls technicians); 88 port security (security officers and supervisors at both terminals and the depot); 24 IT and cybersecurity |
| Contract labor | Longshore labor for vessel and yard work (crane, RTG and yard tractor operators, lashers) is ordered per shift through the local hiring halls: about 400 to 700 workers a day across both terminals. They are not employees, but they use OT (crane and RTG cabs) and VMTs |
| Revenue | About $100.0 million a year (fictional): T1 about $76 million, T2 about $18 million, depot and other services about $6 million. Not SBA-small (standard $47.0 million for NAICS 488320; 13 CFR 121.201) |
| Customers | 9 container carrier services at T1 (3 of them under one carrier alliance agreement); 7 breakbulk, project cargo and vehicle logistics customers at T2; about 1,200 registered trucking companies; importers and exporters indirectly |
| MTSA status | **Both terminals are facilities regulated under 33 CFR Part 105.** Each receives foreign cargo vessels greater than 100 gross register tons (33 CFR 105.105(a)(4)) and has its own Coast Guard-approved Facility Security Plan (FSP) and Facility Security Officer (FSO). The two ports are in different Captain of the Port (COTP) zones, so one person cannot be FSO for both (105.205(a)(2)). Secure areas are controlled with TWIC cards and TWIC readers |
| Cyber rule status | **33 CFR Part 101, Subpart F applies to both terminals** (101.605(a)). No size threshold. Rule effective 2025-07-16 (90 FR 6298, 2025-01-17). The company plans **one Cybersecurity Plan covering both terminals**, with terminal-specific sections, as 101.630(d)(2) allows for facilities of similar operations, and **one CySO for both** (101.625(b)) |
| Not in scope | TSA Security Directives (not a rail, pipeline or aviation operator). CMMC and FAR clauses (no federal or DoD contracts). SEC disclosure rules (privately held). CTPAT is voluntary; the company is not a partner (the PE sponsor asked for a decision in 2027). Payment cards: customers pay through a hosted payment page run by a payment service provider; card data never reaches company systems (noted, not assessed) |
| State law approach | Florida only. Florida law is cited where a Florida duty applies (Fla. Stat. 501.171 for employee and truck driver personal information). The Subpart F federalism clause (101.610) makes Subpart F preempt conflicting state or local law for Part 105 facilities |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting; receives P01, P07 and P09 results |
| Chief Executive Officer | Accepts High risk; approves the risk appetite and the security budget |
| Chief Operating Officer | Executive sponsor of the security program; TOGP system owner; accepts Moderate risk; approves the Cybersecurity Plan for submission |
| Chief Financial Officer | Cyber insurance, ERP, payment service provider and vendor contract terms |
| General Counsel | Legal counsel; breach determinations under Fla. Stat. 501.171; SSI legal questions; contract notice terms |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting; P10 AI review chair with the Chief Operating Officer |
| Director of IT and Cybersecurity | **Cybersecurity Officer (CySO)** for both terminals, designated in writing 2026-03-02 (101.620(b)(3)); owns the SSP |
| Security Manager plus 2 security analysts (one OT-focused) and 1 GRC analyst | Security operations, vulnerability management, MSSP liaison, GRC. The Security Manager is the **alternate CySO** |
| Director of Port Security | **FSO for T1** (33 CFR 105.205); owns CCTV and PACS at both terminals and the depot |
| T2 Security Lead | **FSO for T2**; alternate FSO for T1 is the T1 security supervisor on duty |
| Vice President, Terminal Operations | Owns vessel, yard and gate operations at both terminals and the TOS business processes; T1 and T2 General Managers report to this role |
| Director of Planning | Leads vessel and yard planners; business owner of the scheduling optimization service (AI-001) |
| Director of Maintenance and Engineering | Owns cranes, yard equipment and their controllers (OT) and the crane vendor relationships |
| OT network engineer | Runs the T1 OT zone firewall and passive OT monitoring sensors; reports to the Director of IT and Cybersecurity |
| Director of Commercial and Customer Service | Carrier and trucking relationships; customer portal business owner |
| HR Director | Onboarding, terminations, training records |
| Internal audit (co-sourced firm) | Annual IT audit; performed the P07 assessment. Has no regularly assigned cybersecurity duties, so it can perform the annual Cybersecurity Plan audit (101.630(f)(4)) |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring for IT systems |
| TOS vendor | Licenses the TOS software; remote support under a support contract |
| Crane and equipment vendors (OEM service) | T1 STS and RTG controllers through the company's privileged remote access service; T2 mobile harbor cranes through the OEM's always-on cellular appliance (gap 2) |

## 3. Systems

| ID | System | Hosting | Critical IT or OT? (101.615) | Notes |
|---|---|---|---|---|
| SYS-01 | Terminal operating system (TOS): vessel and yard planning, equipment control, gate, breakbulk and vehicle module, billing, EDI engine. One instance serves T1, T2 and the depot | Commercial TOS software run by the company in the workloads account of the cloud landing zone (SYS-10); TOS gate servers on premises at each gate | Critical IT | System of record for every container and vehicle, its location, holds and hazardous cargo class |
| SYS-02 | Gate automation: OCR portals, TWIC readers tied to the physical access control system, driver kiosks, gate transaction servers (T1 12 lanes, T2 4 lanes, depot 2 lanes) | On premises | Critical IT | T2 OCR servers run an operating system past end of vendor support (gap 11) |
| SYS-03 | Crane and yard equipment OT: STS and RTG PLCs, drives and HMIs; crane management system server; mobile harbor crane controllers at T2; reefer monitoring gateways and server (1,200 plugs, T1); VMTs on 130 yard tractors | On premises | Critical OT | T1 OT sits in an OT zone behind an industrial firewall (2025) with passive OT monitoring. T2 OT shares a flat network with the gate (gap 1) |
| SYS-04 | EDI and integration: EDI with 16 carrier services and customers, trucking companies, the two port community systems, and a customs data exchange service that delivers release and hold status from U.S. Customs and Border Protection | EDI gateway and integration services in SYS-10 | Critical IT | 2 carrier services still use plain FTP (gap 12) |
| SYS-05 | Identity provider (single sign-on, MFA, conditional access) | SaaS | Critical IT | MFA for all identity provider users and the staff VPN since 2025. Not covered: TOS gate module local accounts, OT engineering and HMI accounts (gap 3) |
| SYS-06 | Productivity suite (email, files, chat) | SaaS | No | MFA enforced |
| SYS-07 | Networks: SD-WAN linking T1, T2, the depot and the cloud; internet firewalls; T1 OT zone firewall; T2 flat gate-and-yard network; VMT Wi-Fi at both terminals; staff VPN | On premises plus managed SD-WAN | Critical IT | Segmentation at T1 only (gap 1) |
| SYS-08 | Endpoints: 520 workstations and laptops, 140 rugged tablets, 130 VMTs | Company-managed | Critical IT (operations endpoints) | EDR on all Windows endpoints and servers. VMTs run a vendor-locked operating system without EDR |
| SYS-09 | Security systems: CCTV (420 IP cameras, 2 video management servers, perimeter video analytics at T1) and PACS with TWIC readers at both terminals | On premises | Critical IT (supports the FSPs) | Owned by the Director of Port Security |
| SYS-10 | Cloud landing zone: 4 accounts (identity and security, shared services, workloads, backup) plus a warm standby TOS database replica in a second region | Public cloud (vendor-agnostic) | Critical IT | Workloads: TOS application and database, EDI gateway, integration services, customer portal (SYS-14) |
| SYS-11 | ERP (finance, billing, procurement) and HR and payroll | SaaS | No | Employee personal information |
| SYS-12 | Berth and yard scheduling optimization service (AI-001) | Vendor SaaS integrated with the TOS by API | Not yet designated (see P10) | In production at T1 since 2026-03; advisory mode only (gap 14) |
| SYS-13 | Security monitoring: SIEM operated by the MSSP; passive OT network monitoring sensors at T1 | SaaS plus on-premises sensors | Critical IT | T2 sources and T1 OT alerts not in the MSSP workflow (gap 9) |
| SYS-14 | Customer portal and truck appointment system: container availability, appointments, invoices, links to the hosted payment page; about 1,200 trucking companies and cargo owners | Company-built web application in the workloads account | Critical IT | Built and maintained by the TOS application team with a development contractor |
| SYS-15 | Third-party IT and OT vendors and service providers (about 110; 27 with remote or network access) | Various | n/a | Contract notice terms missing for 14 of the 27 (gap 8) |

**SSP system (P02):** the *Terminal Operations and Gate Platform (TOGP)*: SYS-01, SYS-02, SYS-04, SYS-05, SYS-07, SYS-08 (operations endpoints), SYS-10, SYS-13 and SYS-14, with interfaces to SYS-03 (OT), SYS-09 (security systems), SYS-11 and SYS-12. Moderate baseline with tailoring.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- Coast Guard-approved FSPs, designated FSOs, TWIC-based access control and CCTV at both terminals; quarterly MTSA drills and an annual exercise (33 CFR 105.220). The 2025 T1 exercise included a cyber tabletop; T2 has had no cyber scenario
- CySO (Director of IT and Cybersecurity) and alternate CySO (Security Manager) designated in writing on 2026-03-02, with a 24x7 contact rota
- MFA for all identity provider users, the staff VPN and cloud administrators
- EDR on all Windows endpoints and servers with 24x7 MSSP monitoring; SIEM with identity provider, cloud, firewall, EDR, customer portal and T1 TOS gate server logs, kept 1 year
- T1 IT/OT segmentation: an OT zone behind an industrial firewall (2025), with passive OT network monitoring
- A 4-account cloud landing zone; daily TOS database backups to the backup account with 35-day write-once retention; a warm standby TOS database replica in a second region
- Monthly authenticated vulnerability scans of IT systems and a weekly Known Exploited Vulnerabilities (KEV) review
- A privileged remote access service with MFA and session recording, used today by the T1 crane OEM only
- Security policies adopted in 2024; an annual risk assessment (last July 2025)
- Subpart F training for employees: 548 of 590 employees with system access completed it by 2026-01-12; annual phishing simulations
- Annual co-sourced internal IT audit
- Cyber insurance with a breach hotline

**Missing or weak, found in the 2026 assessments:**
1. Terminal 2 has no IT/OT segmentation. Mobile harbor crane controllers, VMT Wi-Fi and the gate servers share one flat network, and IT-OT connections at T2 are not logged or monitored (101.650(h)).
2. Third-party remote access is not uniformly controlled. The T2 mobile harbor crane OEM uses an always-on cellular appliance with a shared account; the OCR vendor and the reefer monitoring vendor use their own remote support tools. Of 27 vendors with remote or network access, only the T1 crane OEM goes through the privileged remote access service (101.650(e)(3)(v), (f)(3)).
3. OT and privileged account security: shared engineering and HMI accounts on cranes at both terminals, no documented compensating controls where MFA is not feasible, TOS gate module local accounts outside the identity provider, and standing domain administrator accounts (privileged access management covers the cloud only) (101.650(a)(4)-(7)).
4. The asset inventory and network map are incomplete. IT is inventoried; OT is about 55% inventoried (T1 from passive monitoring, T2 not at all). There is no consolidated network map or OT device configuration documentation (101.650(b)(3)-(4)).
5. Recovery is unproven at scale. The 2026-04-22 TOS database restore test took 6.5 hours against a 4-hour RTO; there has been no full failover test to the second region; T2 gate server images are not backed up; T2 PLC programs are held only by the OEM (101.650(g)(4)).
6. The Cyber Incident Response Plan predates Subpart F. The 2024 plan is IT-focused, has no OT procedures, and the 33 CFR 6.16-1 reporting step has never been exercised. Only 1 cyber drill has been held in 2026; 101.635(b) calls for at least 2 each calendar year (101.650(g)(2)).
7. Training is incomplete. 42 employees completed Subpart F training after the 2026-01-12 deadline; longshore labor and vendor technicians who use OT and VMTs are not trained and there is no supervision rule; OT-specific training has been given only to T1 maintenance staff (101.650(d)).
8. Supply chain terms are thin. 14 of 27 vendors with access have no vulnerability or incident notification clause; vendors are reviewed only at onboarding; SOC 2 reports are on file for 4 vendors (101.650(f)(1)-(2)).
9. Logging gaps. T2 gate servers and the TOS application audit log do not feed the SIEM, and T1 OT monitoring alerts go to an analyst queue outside the MSSP workflow (101.650(c)(1), (h)(2)).
10. There is no approved list of hardware, firmware and software for OT and gate systems, and executable code is not disabled by default on critical IT and OT systems (101.650(b)(1)-(2)).
11. Unsupported components and scanning scope. T2 OCR servers and 2 T2 crane HMIs run end-of-support operating systems; vulnerability scanning covers IT only, not OT (101.650(e)(3)(i), (vi)).
12. Encryption gaps. Two carrier services still send EDI by plain FTP; OT protocols are unencrypted with no documented feasibility review (101.650(c)(2)).
13. USB and unused ports are open on T2 HMIs and gate servers; T1 uses port blockers (101.650(i)(2)).
14. There is no AI governance. The scheduling optimization service moved from pilot to production at T1 in 2026-03 without an AI policy, and two other AI tools were adopted by departments without a security review (P10).
15. The 2024 policies lack supporting standards for OT security, vendor remote access, logging and configuration, and there is no channel to receive publicly reported vulnerabilities (101.650(e)(3)(ii)).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| Regulation (P03) | All applicable rules for the terminal business: USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101 Subpart F (primary); maritime cyber incident and MTSA reporting (33 CFR 6.16-1; 101.305); the cyber-relevant duties in 33 CFR Part 105 (FSA, FSP, drills, records, audits); SSI protection (49 CFR 1520.9); Florida data security, disposal and breach notice (Fla. Stat. 501.171) |
| P08 incidents | **Two incident types:** (1) ransomware disrupting the TOS (registry default), with OT at risk on the flat T2 network; (2) unauthorized access to crane controllers through vendor remote access (an OT safety incident). Both are integrated with crisis management and legal |
| P09 SOC 2 | Readiness for a SOC 2 Type 2 examination of the customer portal and EDI services, requested by the carrier alliance customer (Security, Availability, Processing Integrity, Confidentiality); plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio: AI-001 berth and yard scheduling optimization (registry default), AI-002 gate OCR, AI-003 crane predictive maintenance analytics, AI-004 perimeter video analytics, AI-005 enterprise generative AI assistant |
| Cloud | Multi-account landing zone, vendor-agnostic, with a second region for the TOS database standby |

The registry defaults (TOS and gate automation; ransomware disrupting the TOS; container and berth scheduling optimization) fit this business and are kept. At this size the portfolio adds four more AI tools, and the second runbook covers the OT vendor-access risk that the T2 acquisition introduced.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2025-07-16 | Subpart F effective (90 FR 6298) |
| 2026-01-12 | Subpart F training deadline for all personnel and key personnel (101.650(d)(4)). Met for 548 of 590 employees; missed for 42 employees, longshore labor and vendor technicians |
| 2026-03-02 | CySO and alternate CySO designated in writing |
| 2026-07-06 to 2026-07-31 | Risk assessment and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (OT tests at T2 on the night of 2026-08-12 and at T1 on the night of 2026-08-13, with no vessel at berth) |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness assessment, vendor SOC 2 reviews and AI portfolio assessment |
| 2026-09-15 | Results to the audit committee; deliverables approved by the Chief Operating Officer (Moderate and below) and the Chief Executive Officer (High and above) |
| 2027-07-16 | Deadline for the first Cybersecurity Assessment (101.650(e)(1)) and submission of the Cybersecurity Plan (101.655). The company targets submission by 2027-05-28 |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Revenue per day | The terminals work about 363 days a year: about $209,000 a day at T1, $50,000 at T2 and $16,500 at the depot (about $275,000 a day in total) |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires notice through the carrier hotline before incident vendors are engaged |
| MSSP | 24x7 monitoring of IT sources; contract requires a call to the Security Manager within 30 minutes of a high-severity alert. The MSSP does not monitor OT |
| Backups and recovery | Daily TOS database backups to the backup account (35-day write-once retention, separate administrator credentials) and a continuous warm standby replica in a second region. T1 gate server images weekly; T1 PLC programs and HMI settings held offline in the Maintenance and Engineering safe since 2025. 2026-04-22 restore test: TOS database restored in 6.5 hours |
| Workforce activity | 74 terminations and 41 internal transfers in the 12 months to 2026-06-30. Access reviews are semiannual (last completed 2026-02). June 2026 phishing simulation click rate: 6.1% |
| Carrier alliance | The carrier alliance agreement at T1 (3 services, about 45% of T1 revenue) renews on 2027-12-31. The alliance's vendor risk program asked for a SOC 2 Type 2 report on the customer portal and EDI services before renewal |
| Vendors with access | The 27 vendors with remote or network access include the TOS vendor, the T1 crane OEM, the T2 mobile harbor crane OEM, the OCR vendor, the reefer monitoring vendor, the CCTV integrator, the SD-WAN provider, the MSSP, the development contractor and the scheduling optimization vendor |
| Terminology | "Terminal Operations and Gate Platform (TOGP)" is the SSP system in P02, identifier CSC-TOGP-01 |
| Additional role titles | T1 General Manager; T2 General Manager; Depot Manager; Controller; Procurement Manager; TOS Application Manager; T1 security supervisor on duty |
| Assessment populations (P03, P07) | 38 privileged accounts across the directory, identity provider, cloud, TOS, OT engineering workstations and gate server local administrators; about 310 network-connected OT and gate devices; 22 TOS and gate servers; 31 security tickets (2025-07 to 2026-06); 96 new hires and 74 terminations in the year to 2026-06-30; 48 T1 crane OEM remote sessions in 2026-Q2; 46 customs hold overrides (2026-04 to 2026-06); 34 portal releases in 2026 H1 |
| 2026 cyber drill | One cyber drill held on 2026-05-20 at T1 (phishing to VPN scenario); the second is scheduled for 2026-11-18 with a T2 mobile harbor crane scenario |
| FY2027 security plan | Approved by the CEO on 2026-09-15: $1.275 million one-time and $335,000 a year (itemized in P01 section 4) |
| Carrier alliance terms | Incident notice to the alliance within 24 hours of confirming an incident that affects the portal, EDI services or the alliance's T1 vessel operations. The alliance accepted the SOC 2 plan (Type 1 as of 2027-03-31, Type 2 period 2027-04-01 to 2027-09-30) on 2026-09-10 |
| Vendor tiers (P09) | 12 Tier 1 vendors (the cloud provider, identity provider, remote access service vendor, MSSP, TOS vendor, SD-WAN provider, both crane OEMs, OCR vendor, reefer monitoring vendor, CCTV integrator and scheduling optimization vendor) and 18 Tier 2 vendors with access. 5 vendors hold personal information for the company (HR and payroll SaaS, TOS vendor, identity provider, cloud provider, development contractor) |
| AI tools (P10) | AI-003 crane predictive maintenance analytics adopted by Maintenance and Engineering in 2026-01 (pilot on 7 STS cranes and 8 RTGs at T1); AI-004 perimeter video analytics added with the 2025 CCTV upgrade (46 cameras at T1; no facial recognition); AI-005 enterprise generative AI assistant licensed for 120 office users in 2026-06. First AI review group meeting 2026-10-06 |
| Other details | Cloud root credentials are sealed in the T1 FSO safe. T2 has 26 security staff. The T1 gate server room generator covers 48 hours. Longshore labor are employed through the hiring halls, which report their injuries under OSHA rules; the company reports for its own employees |

# Scenario facts: Cris Santos Company | Transportation and Warehousing | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, the citation is given. Regulatory facts were checked against eCFR (point in time 2026-09-23) and the Federal Register on 2026-09-26.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; Cris Santos is majority owner) |
| Business | Marine cargo terminal operator (NAICS 488320 Marine Cargo Handling). Operates a container and breakbulk terminal at a Florida port under a long-term lease from the port authority (a landlord port) |
| Terminal | About 70 acres. Berth 1 (container) and Berth 2 (multipurpose and breakbulk). 2 ship-to-shore (STS) container cranes, 1 mobile harbor crane, 6 rubber-tired gantry cranes (RTGs), 5 reach stackers, 30 yard tractors with vehicle-mounted terminals (VMTs), 300 reefer plugs. An office building and a 3-lane truck gate complex with a gate server room |
| Volume | About 160,000 container moves and 350,000 tons of breakbulk (steel, lumber, project cargo) a year. About 5 vessel calls a week from 6 regional ocean carrier services (Caribbean and Central America). About 800 truck gate transactions a day |
| Location | Florida, one terminal. No other sites |
| Workforce | 60 employees: 10 management, finance, HR and customer service; 24 operations (Operations Manager, 4 vessel and yard planners, 3 shift superintendents, 16 gate and yard clerks); 14 maintenance (Maintenance Manager, 13 mechanics and crane electricians); 10 security (Security and Safety Manager, 9 security officers); 2 IT (IT Manager, IT technician) |
| Contract labor | Longshore labor for vessel and yard work (crane, RTG and yard tractor operators, lashers) is ordered per shift through the local hiring hall: about 80 to 150 workers on a vessel day. They are not employees, but they use OT (crane and RTG cabs) and VMTs |
| Revenue | $28.2 million a year (fictional). Under the SBA standard of $47.0 million for NAICS 488320 (13 CFR 121.201), so SBA-small |
| Customers | 6 ocean carrier services under terminal services agreements; about 350 registered trucking companies; importers and exporters indirectly |
| MTSA status | **Facility regulated under 33 CFR Part 105.** The terminal receives foreign cargo vessels greater than 100 gross register tons (33 CFR 105.105(a)(4)). It has a Coast Guard-approved Facility Security Plan (FSP) and a Facility Security Officer (FSO). Secure areas are controlled with TWIC cards and TWIC readers |
| Cyber rule status | **33 CFR Part 101, Subpart F applies** (101.605(a): owners and operators of facilities required to have a security plan under Part 105). No size threshold. Rule effective 2025-07-16 (90 FR 6298, 2025-01-17) |
| Not in scope | TSA Security Directives (the company is not a rail, pipeline or aviation operator). CMMC and FAR clauses (no federal or DoD contracts). SEC disclosure rules (private company). CTPAT is voluntary and the company is not a partner today (considered for 2027). Payment cards: truckers and cargo owners pay demurrage and fees through a hosted payment page run by a payment service provider; card data never reaches company systems (noted, not assessed) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification for employee and truck driver personal information, Fla. Stat. 501.171). The Subpart F federalism clause (101.610) makes Subpart F preempt conflicting state or local law for Part 105 facilities |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Majority owner (Cris Santos) | Accepts High and Very High risks; approves the security budget |
| General Manager | Executive owner of the security program; accepts Moderate risk; signs policies; approves the Cybersecurity Plan for submission |
| IT Manager | Runs IT with a managed service provider. **Proposed Cybersecurity Officer (CySO)**, not yet designated in writing (gap 1) |
| Security and Safety Manager | **Facility Security Officer (FSO)** under 33 CFR 105.205; owns the FSP, TWIC access control, CCTV, MTSA drills and exercises. Proposed alternate CySO |
| Operations Manager | Owns vessel, yard and gate operations and the terminal operating system (TOS) business processes |
| Vessel and Yard Planning Lead | Leads 3 planners; business owner of the scheduling optimization pilot (P10) |
| Maintenance Manager | Owns cranes and yard equipment, their controllers (OT) and the crane vendor relationship |
| Finance and Administration Manager | Billing, contracts, insurance, HR oversight; vendor contract terms |
| HR Specialist | Onboarding, terminations, training records |
| Managed service provider (MSP) | Help desk, office endpoint patching, firewall administration, backup monitoring |
| TOS vendor | Licenses the TOS software; remote support; hosts the truck appointment and customer portal (SaaS) |
| Crane and equipment vendor (OEM service) | Remote diagnostics of STS and RTG controllers through an always-on remote access appliance (gap 3) |

## 3. Systems

| ID | System | Hosting | Critical IT or OT? (101.615) | Notes |
|---|---|---|---|---|
| SYS-01 | Terminal operating system (TOS): vessel planning, yard planning, equipment dispatch, gate module, billing, EDI engine | Commercial TOS software run by the company in its cloud tenant (SYS-10), plus TOS gate servers on premises | Critical IT | System of record for every container and its location, status, holds and hazardous cargo class |
| SYS-02 | Gate automation: optical character recognition (OCR) portals for container, chassis and license plate numbers; TWIC card readers tied to the physical access control system (PACS); driver kiosks; gate transaction server | On premises (gate server room) | Critical IT | Runs on the same flat network segment as SYS-03 (gap 2). OCR servers run an operating system that reaches end of vendor support in 2026-12 |
| SYS-03 | Crane and yard equipment controllers (OT): STS and RTG programmable logic controllers (PLCs), drive systems, human-machine interfaces (HMIs) in crane electrical houses and cabs; VMTs on 30 yard tractors | On premises | Critical OT | Crane vendor remote access is always on (gap 3). Default passwords found on 2 RTG HMIs (gap 8) |
| SYS-04 | EDI and data exchange: EDI links with ocean carriers (bay plans, load and discharge lists, container status), trucking companies (appointments), the port authority's port community system (vessel schedules, gate status), and a customs data exchange service that delivers release and hold status from U.S. Customs and Border Protection | EDI gateway in SYS-10; partner systems external | Critical IT | One carrier still uses unencrypted FTP (gap 15) |
| SYS-05 | Identity provider (single sign-on and MFA) | SaaS | Critical IT | MFA enforced for email and the TOS administrator group only (gap 4). The staff remote-access VPN authenticates with a password only |
| SYS-06 | Productivity suite (email, files, chat) | SaaS | No | MFA enforced |
| SYS-07 | Terminal networks: internet firewall, office LAN, the gate and yard network (one flat segment for gate servers, OCR, TWIC readers, VMT Wi-Fi, crane and RTG controllers), site-to-site VPN to SYS-10, staff remote-access VPN | On premises | Critical IT | Office LAN and the gate and yard network are separate VLANs, but routing between them is not filtered |
| SYS-08 | Endpoints: 62 office and operations workstations and laptops, 12 rugged tablets for checkers, 30 VMTs | On premises | Critical IT (operations endpoints) | MSP-managed antivirus on Windows endpoints; no endpoint detection and response (EDR) |
| SYS-09 | CCTV (110 IP cameras, video management server) and PACS server | On premises | Critical IT (supports the FSP) | Owned by the FSO; 30-day video retention |
| SYS-10 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Critical IT | Hosts TOS application servers, the TOS database (managed database service), the EDI gateway, the integration server for the port community system and customs data exchange, and database snapshots in the same account (gap 13) |
| SYS-11 | Finance, payroll and HR | SaaS | No | Employee personal information |
| SYS-12 | Berth and yard scheduling optimization service (AI) | Vendor SaaS integrated with the TOS by API | Not yet designated (see P10) | Pilot in advisory mode since 2026-05 (see P10) |

**SSP system (P02):** the *Terminal Operations and Gate Platform (TOGP)*: SYS-01, SYS-02, SYS-04, SYS-05, SYS-10, the gate and yard segment of SYS-07, and the operations endpoints in SYS-08, with interfaces to SYS-03 (OT), SYS-09 (PACS) and SYS-12.

## 4. Current security posture: partially compliant

**In place today:**
- A Coast Guard-approved FSP, a designated FSO, TWIC-based access control to secure areas, CCTV, and quarterly MTSA security drills and an annual exercise (33 CFR 105.220). None of the drills or exercises has included a cyber scenario
- MFA for email and for the TOS administrator group (which also covers cloud console administrators)
- Unique named user IDs in the TOS for planners, supervisors and office staff
- An internet firewall managed by the MSP; site-to-site VPN to the cloud tenant
- TOS database snapshots with 7-day point-in-time restore (same cloud account); a weekly TOS database export to a storage device in the office server closet
- MSP-managed antivirus and monthly patching on office Windows endpoints
- Secure EDI protocols (AS2 or SFTP) with 5 of 6 carrier services, the port community system and the customs data exchange service
- A general security awareness module (online) completed by 22 of 60 employees in 2026-02
- A partial hardware inventory (office and gate IT; no OT)
- Cyber insurance with a breach hotline

**Missing or weak, found in the 2026 assessments:**
1. No Cybersecurity Officer designated in writing (101.620(b)(3)). The IT Manager is the proposed CySO; no alternate, no 24x7 contact arrangement. The Coast Guard's final rule preamble places the designation within the 24-month implementation period (by 2027-07-16), but the CySO must drive the Assessment and the Plan, so the company treats it as urgent.
2. OT (crane and RTG controllers, VMT Wi-Fi) sits on the same flat network as the TOS gate servers, OCR and TWIC readers. No IT/OT segmentation, and IT-OT connections are not logged or monitored (101.650(h)).
3. Crane vendor remote access is always on through a vendor-installed appliance with a cellular modem, a shared vendor account, no MFA and no session logging (101.650(a)(4), (e)(3)(v), (f)(3)).
4. MFA only on email and the TOS administrator group. The staff remote-access VPN, TOS standard users, gate server local administrator accounts and OT HMIs have none (101.650(a)(4)).
5. Incident response is informal. No written Cyber Incident Response Plan (101.650(g)(2)) and no documented procedure for reporting to the FBI, CISA and the Captain of the Port (33 CFR 6.16-1).
6. Cybersecurity training has not been delivered to all personnel. The 2026-01-12 deadline in 101.650(d)(4) was missed: 22 of 60 employees completed a generic module; no OT-specific or key personnel training; no training for longshore labor who use OT and VMTs.
7. No Cybersecurity Assessment and no Cybersecurity Plan yet (both due 2027-07-16; 101.650(e)(1), 101.655). This P01 to P10 work is the starting point.
8. Manufacturer default passwords on 2 RTG HMIs and on the web interface of the 3 OCR camera controllers (found in P07 testing, 2026-08-12) (101.650(a)(2)).
9. No approved list of hardware, firmware and software; office users can install software; no application allowlisting on critical systems (101.650(b)(1)-(2)).
10. The inventory covers office and gate IT only. There is no network map and no OT device configuration documentation (101.650(b)(3)-(4)).
11. TOS, gate server and firewall logs are kept locally with default retention (7 to 30 days) and can be deleted by local administrators. No central log collection (101.650(c)(1)).
12. No vulnerability scanning. Known Exploited Vulnerabilities (KEVs) are not tracked. OCR servers run an operating system that reaches end of support in 2026-12 (101.650(e)(3)(i), (vi)).
13. TOS database snapshots share the production cloud account; the weekly export sits on a domain-joined storage device on the office LAN; gate server configurations are not backed up; PLC programs are held only by the crane vendor. No restore test has ever been performed (101.650(g)(4)).
14. No cybersecurity criteria in procurement; the crane vendor and OCR vendor contracts have no vulnerability or incident notification clause (101.650(f)(1)-(2)).
15. One carrier service still sends bay plans and container status messages by unencrypted FTP (101.650(c)(2)).
16. Departing employees' accounts are disabled about 5 business days after the last day. Four gate booth workstations use shared "gate clerk" logins (101.650(a)(6)-(7)).
17. USB ports are open on OT HMIs and gate servers; crane technicians connect their own laptops (101.650(i)(2)).
18. No channel to receive publicly reported vulnerabilities (101.650(e)(3)(ii)).
19. The AI scheduling pilot started without a security review or an AI policy (P10).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| Regulation (P03) | Primary: USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101 Subpart F (101.600-101.670). Secondary: maritime cyber incident reporting, 33 CFR 6.16-1, with the related MTSA reporting duties in 33 CFR 101.305 |
| P08 incident | Ransomware disrupting the TOS. Initial access through a password-only VPN account; gate servers and TOS servers encrypted; OT at risk on the flat network. USCG, FBI and CISA reporting under 33 CFR 6.16-1, and communications with port partners (port authority, carriers, trucking companies, port community system, customs data exchange) |
| P09 SOC 2 | A Security plus Availability readiness check used to answer ocean carrier customer security questionnaires. SOC 2 is not typical for a terminal operator (see P09); plus a review of the TOS vendor's SOC 2 Type 2 report for its hosted portal and remote support |
| P10 AI | AI-001: container and berth scheduling optimization (operational AI; yard safety considerations). Inventory also lists the gate OCR (AI-002) and public generative AI chatbots (AI-003) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2025-07-16 | Subpart F effective (90 FR 6298) |
| 2026-01-12 | Subpart F training deadline for all personnel and key personnel (101.650(d)(4)). **Missed** |
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis fieldwork |
| 2026-08-10 to 2026-08-14 | Control assessment fieldwork (OT tests on the night of 2026-08-12, with no vessel at berth) |
| 2026-08-26 to 2026-08-28 | TOS vendor SOC 2 report review (P09 Part B), AI risk assessment of the scheduling pilot (P10) and SOC 2 readiness self-assessment (P09) |
| 2026-09-04 | Deliverables approved by the General Manager (Moderate and below) and the majority owner (High) |
| 2027-07-16 | Deadline for the CySO designation (per the rule preamble), the first Cybersecurity Assessment (101.650(e)(1)) and submission of the Cybersecurity Plan to the Captain of the Port (101.655) |

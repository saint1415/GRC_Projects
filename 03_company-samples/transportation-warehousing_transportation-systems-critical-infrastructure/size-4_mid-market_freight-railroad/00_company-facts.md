# Scenario facts: Cris Santos Company | Transportation Systems | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given. Regulatory facts were checked against eCFR (point in time 2026-09-23), the Federal Register, and the TSA-published directive texts (SD 1580-21-01E and SD 1580/82-2022-01E) on 2026-10-05.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed; board with an audit committee) |
| Business | Regional freight railroad (NAICS 482112 Short Line Railroads). A **Class II** carrier under the Surface Transportation Board revenue classes (49 CFR part 1201, General Instructions 1-1). TSA quoted the STB thresholds in its 2024 surface cyber NPRM as revenue between $42.4 million and $943.9 million for Class II (89 FR 88488, footnote 123). The Chief Financial Officer confirms the class each year against STB's published threshold |
| Network | 512 route miles of company-owned track in north and central Florida. **Jacksonville Subdivision** (96 miles, centralized traffic control (CTC)) from Jacksonville Terminal Yard to Central Yard; 24 of its miles, the terminal yard, and the interchange tracks lie inside the Jacksonville high threat urban area (HTUA) in Appendix A to 49 CFR part 1580. **Central Subdivision** (188 miles, CTC) from Central Yard to Southern Yard. **5 branch lines** (228 miles) in non-signaled territory under track warrant control. Plus **52 miles of trackage rights** over a Class I railroad's PTC-equipped main line from Southern Yard to a Class I junction |
| Interchange | With 2 Class I railroads at Jacksonville Terminal Yard (inside the HTUA) and with the trackage-rights Class I at the far end of the 52-mile segment. No Class I or passenger train operates on company track |
| Facilities | Headquarters campus at Central Yard: offices, primary network operations center (NOC, the dispatch center), HQ data center, locomotive shop. Backup NOC and second server room at Jacksonville Terminal Yard. Southern Yard and 2 smaller yards; car repair shop; 2 transload terminals. 38 radio tower sites; 150 wayside signal locations (64 CTC control points and 86 intermediate signals); 22 hot bearing and dragging equipment detectors; 312 public highway-rail grade crossings with active warning devices (118 with cellular remote health monitors); 2 wayside machine vision portals (see P10) |
| Equipment | 118 locomotives (52 road, 66 yard and local). **46 road locomotives carry onboard positive train control (PTC) apparatus** for the trackage-rights run. 28 hi-rail trucks; 3 camera-equipped hi-rail inspection vehicles (P10) |
| Traffic | About 214,000 carloads a year from 310 shippers: aggregates, forest products, chemicals, fertilizer, propane (Division 2.1), ethanol, and about **5,200 tank cars a year of chlorine and anhydrous ammonia** (materials poisonous by inhalation, PIH), most of them interchanged at Jacksonville Terminal Yard. About 26 trains a day across the network |
| Shared services | Since 2025-07 the company dispatches 2 affiliated Class III short lines owned by the same private equity sponsor (140 route miles, track warrant control) and runs their car management in its TMS. A third, unaffiliated short line signed a services agreement on 2026-06-12 to start 2027-01-01; it requires a SOC 2 Type 2 report on the service (P09) |
| Location | Florida only. Headquarters in north-central Florida |
| Workforce | 850 employees: 330 train and engine service; 190 track and bridge maintenance of way; 70 signal and communications; 95 locomotive and car mechanical; 48 network operations (36 train dispatchers including 4 chief dispatchers, 12 car management and customer service); 12 safety, security, and hazmat; 35 IT and cybersecurity (including a 7-person cybersecurity team); 70 executive, finance, HR, legal, sales, and administration |
| Revenue | About $214 million a year (fictional): carload freight $196 million, demurrage and accessorial $14 million, contract dispatching and car management services $4 million. SBA-small by employees (SBA standard for NAICS 482112 is 1,500 employees, 13 CFR 121.201), so the Mid-Market size is set by the tier rule (500-999 employees) |
| TSA status | A freight railroad carrier under 49 CFR 1580.1(a)(1), so **49 CFR 1570.201 (Security Coordinator) and 1570.203 (reporting significant security concerns, including "Cyber Attack" in Appendix A to part 1570) apply**. It transports rail security-sensitive materials (RSSM: PIH tank cars, 1580.3) **in an HTUA**, so it is an owner/operator in **49 CFR 1580.101(b)**: **part 1580 subpart B applies** (TSA-approved security training program, 1580.113 and 1580.115; records, 1570.121), and **part 1580 subpart C applies** (location and shipping information within 30 minutes of a TSA request, 1580.203(d); chain of custody, including attended carrier-to-carrier transfers inside the HTUA, 1580.205(c)) |
| TSA cyber directives | **Covered.** SD 1580-21-01E (effective 2026-01-16 to 2027-01-15) and SD 1580/82-2022-01E (effective 2026-05-03 to 2027-05-02) both apply to "each freight railroad carrier identified in 49 CFR 1580.101." Covered since the first directives in 2021-12 and 2022-10. Cybersecurity Implementation Plan (CIP) approved by TSA 2023-03-14; Cybersecurity Assessment Plan (CAP) first approved 2023-06-02, most recent approval 2025-06-20; annual CAP report submitted 2026-06-18 |
| FRA status | Subject to FRA safety rules, including accident/incident reporting (49 CFR part 225). **Not required to install PTC on its own track**: 49 CFR 236.1005(b)(1) places that duty on Class I railroads and railroads that provide or host intercity or commuter passenger service. **A tenant railroad on the Class I's PTC line** (236.1003): the 52-mile trackage-rights movement exceeds 20 miles, so the exception for unequipped Class II and III trains in 236.1006(b)(4)(iii)(A) is not available, and each controlling locomotive on that segment must carry an operative onboard PTC apparatus (236.1006(a) and (b)(4)(iii)(B)). Signal apparatus housings must be secured against unauthorized entry (236.3) |
| Hazmat security | Transports PIH and large bulk Division 2.1, so it must have a hazmat transportation security plan (49 CFR 172.800 and 172.802). Plan reviewed 2026-03 |
| Not in scope | Passenger service (none hosted or operated). SEC disclosure (private company). FAR clauses and CMMC (no federal contracts). Payment cards (customers pay by invoice, EDI, and ACH). CIRCIA and the TSA surface cyber NPRM are proposed only and are tracked, not treated as obligations |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification for employee and customer-contact personal information, Fla. Stat. 501.171). TSA and FRA rules preempt state law on the same subject under 49 U.S.C. 20106 (49 CFR 1580.5) |

**Regulatory driver IDs used in this folder.** The vertical's `requirements.csv` lists C-TRANSPORTATION-R01 to R07. **R01 (TSA rail cyber directives) applies to this company** and is cited with the directive section, for example `C-TRANSPORTATION-R01 (SD 1580/82-2022-01E III.C.2)` or `C-TRANSPORTATION-R01 (SD 1580-21-01E II.C)`. R06 (TSA surface cyber NPRM) and R07 (CIRCIA) are proposed rules, tracked only. R02 to R05 (pipeline, aviation, maritime) do not apply to a railroad. The other binding rules are not in the registry, so this sample adds **scenario-level driver IDs**, defined here and nowhere else.

| ID | Requirement | Citation | Status for this company |
|---|---|---|---|
| C-TRANSPORTATION-S01 | TSA Security Coordinator, applicability determinations, and reporting of significant security concerns | 49 CFR 1570.105, 1570.201, 1570.203 and Appendix A to part 1570 | Applies (1580.1(a)(1) freight railroad) |
| C-TRANSPORTATION-S02 | TSA RSSM operations: location and shipping information, chain of custody | 49 CFR part 1580 subpart C (1580.201, 1580.203, 1580.205) | Applies (carries PIH tank cars, including in the Jacksonville HTUA) |
| C-TRANSPORTATION-S03 | Protection of Sensitive Security Information (SSI) | 49 CFR part 1520 (1520.5(b), 1520.7, 1520.9); 1570.121(c) | Applies (covered person; CIP, CAP, and incident reports are SSI under the directives) |
| C-TRANSPORTATION-S04 | FRA positive train control, tenant duties | 49 CFR part 236 subpart I (236.1006, 236.1029, 236.1033) | Applies to the 46 equipped locomotives, the tenant back office, and the trackage-rights run |
| C-TRANSPORTATION-S05 | FRA accident/incident reporting | 49 CFR part 225 (225.9, 225.11, 225.19) | Applies |
| C-TRANSPORTATION-S06 | Hazmat transportation security plan, rail car security inspection, and hazmat incident notice | 49 CFR 172.800, 172.802; 174.9; 171.15 | Applies |
| C-TRANSPORTATION-S07 | Florida breach notification | Fla. Stat. 501.171 | Applies to employee and customer-contact personal information |
| C-TRANSPORTATION-S08 | TSA security training program for security-sensitive employees | 49 CFR 1580.113, 1580.115; 1570.109, 1570.111, 1570.121 | Applies (1580.101(b)) |
| C-TRANSPORTATION-S09 | FRA inspection and recordkeeping duties touched by company systems | 49 CFR 213.7, 213.233 (track); 215.13 (freight cars); 229.21 (locomotive daily inspection); 228.11 (hours of duty records) | Applies; relevant to P05 and P10 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting; receives the TSA CAP annual report summary |
| Private equity sponsor operating partner | Informed of Severity 1 incidents; approves capital plan |
| Chief Executive Officer | Accepts High risk; approves the risk appetite and security budget; signs POL-01 |
| Chief Operating Officer | Executive sponsor of the security program; accepts Moderate risk; **system owner of the SSP system (P02)** |
| Chief Financial Officer | Insurance, contracts with vendors, STB class confirmation, fraud controls |
| General Counsel | Breach and notification decisions with outside counsel; SSI disclosure questions; contracts |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting; owns POL-01 |
| Director of Information Technology | Runs IT and the HQ data center; **alternate TSA Cybersecurity Coordinator** (SD 1580-21-01E II.B) |
| Cybersecurity Manager | Leads the 7-person cybersecurity team (2 security engineers, 1 OT security engineer, 2 GRC analysts, 1 identity administrator); **primary TSA Cybersecurity Coordinator** (U.S. citizen); owns the CIP and CAP; incident commander |
| Director of Safety, Security, and Hazmat | **Primary TSA Security Coordinator** (1570.201); hazmat security plan; FRA part 225 reporting; TSA security training program (1580.113) |
| Director of Network Operations | Owns the NOC, dispatching, and manual dispatch procedures; business owner of the CAD/CTC office system |
| Chief Dispatcher (on duty, 4 positions) | **Alternate TSA Security Coordinator** through the 24/7 NOC; answers TSA RSSM location requests (1580.203(f)) |
| PTC Program Manager | Tenant PTC compliance on the trackage-rights segment; tenant back office server; coordination with the host Class I |
| Chief Engineer | Track, bridges, signals and communications; designates qualified track inspectors (49 CFR 213.7); business owner of AI-001 (P10) |
| Director of Signals and Communications | CTC field equipment, code line, radio network, tower sites, detectors, crossing monitors |
| Chief Mechanical Officer | Locomotives and cars; onboard PTC hardware installation and seals; business owner of AI-002 (P10) |
| Director of Customer Service and Car Management | TMS, waybills, EDI, RSSM car data, shipper portal; business owner of the shared car management service |
| HR Director | Onboarding, terminations, training records (5-year TSA training records, 1570.121); business owner of AI-003 (P10) |
| Co-sourced internal audit firm | Independent annual IT audit; performs the P07 assessment, which also counts toward the TSA CAP annual assessments |
| Managed security service provider (MSSP) | 24x7 security operations center: SIEM and EDR monitoring for IT systems. OT monitoring is not in its contract today (gap 10) |

## 3. Systems

| ID | System | Hosting | Critical Cyber System (CIP)? | Notes |
|---|---|---|---|---|
| SYS-01 | Computer-aided dispatch and CTC office system (CAD/CTC): CTC route and signal requests to field control points, track warrants for dark territory, train sheets, work authority (track and time), bulletins and speed restrictions; also dispatches the 2 affiliated short lines | On premises: primary server cluster in the HQ data center; hot standby at the backup NOC with real-time replication; 16 consoles at the primary NOC and 6 at the backup NOC | Yes | System of record for movement authority. Standby replicates in real time, so corruption replicates too (gap 6). Servers 14 months behind vendor-certified patches (gap 4) |
| SYS-02 | PTC tenant systems: onboard PTC apparatus on 46 locomotives; company-operated tenant PTC back office server (BOS) pair (primary at HQ, standby at the backup NOC); 3 PTC administration workstations; message exchange with the host Class I's PTC system through the industry interoperable messaging network | Onboard (OT); on premises | Yes | The host Class I owns and certifies the PTC system on its line (236.1003). Onboard units in locked, sealed housings. The PTC vendor supports the BOS under a managed-service agreement through the PAM jump host |
| SYS-03 | CTC field network (OT): 150 wayside signal locations with communication controllers (non-vital) that pass dispatcher requests to vital field logic; code line over IP radio, microwave, and 2 leased circuits | Wayside (OT) | Yes | Vital interlocking logic is in the field and enforces signal safety independently of the office system. Field zone segmentation milestone missed (gap 1). Shared maintainer accounts (gap 2) |
| SYS-04 | Voice radio and wayside monitoring: radio-over-IP gateways and dispatcher consoles; 38 tower sites with microwave backhaul; 22 wayside detectors; 118 crossing remote health monitors (cellular) | Wayside (OT) and on premises | Yes (radio); detectors and monitors: yes | Detector and crossing warning logic is standalone; the network carries alarms and voice. Radio and detector vendors use always-on remote access (gap 3) |
| SYS-05 | Identity: on-premises directory and cloud identity provider (SSO, MFA, conditional access) | On premises and SaaS | Yes | MFA for all remote access, email, cloud, TMS, and the PAM jump hosts. CAD/CTC consoles use directory logins without MFA, with compensating controls documented in the CIP |
| SYS-06 | Transportation management system (TMS): car management, waybills, train consists, interchange EDI, RSSM car location data, shipper portal, demurrage and invoicing; also serves the 2 affiliates | Vendor SaaS | Yes | Supplies consists for PTC initialization and the RSSM location data TSA can request within 30 minutes. Vendor SOC 2 Type 2 reviewed (P09) |
| SYS-07 | Crew management and hours-of-service application (crew calling, hours of duty records under 49 CFR 228.11) | Company cloud (operations workloads account) | Yes | Vendor software on company-managed virtual machines and a managed database |
| SYS-08 | Cloud landing zone: 5 accounts (identity and security; shared services; operations workloads; corporate workloads; backup and recovery) | Public cloud provider (vendor-agnostic) | Partly (operations workloads and backup accounts) | Hosts SYS-07, the data warehouse, file services, the AI image store and inference service (P10), and the backup vault for SYS-01, SYS-02, and SYS-07 (P04) |
| SYS-09 | Corporate and operations networks and endpoints: SD-WAN to 9 sites; HQ and backup NOC dispatch zones behind the IT/OT boundary firewalls; 520 office workstations and laptops; 28 operations workstations (22 dispatch consoles, 3 PTC administration, 3 CTC maintenance); 60 shop and yard PCs; 410 rugged crew tablets | On premises and mobile | Operations zones, consoles, and tablets: yes | EDR on all Windows endpoints and servers, including dispatch consoles (vendor-certified agent since 2025) |
| SYS-10 | Security tooling: SIEM and EDR (MSSP-operated), PAM jump hosts with session recording, passive OT network monitoring sensors (HQ data center, primary and backup NOC only), vulnerability scanner, email security, DNS filtering | SaaS and on premises | Supports | Field OT, CAD/CTC application, and BOS logs are not in the SIEM (gap 7) |
| SYS-11 | ERP: finance, payroll, HR | SaaS | No | Employee personal information, including engineer and conductor certification and medical records |
| SYS-12 | Productivity suite (email, files, chat) | SaaS | No | MFA enforced |
| SYS-13 | AI tools: AI-001 track and equipment defect detection (3 hi-rail camera vehicles, 2 wayside portals); AI-002 locomotive predictive maintenance analytics; AI-003 applicant screening in the HR applicant tracking system; AI-004 enterprise generative AI assistant; AI-005 shipper portal chatbot | Vendors and company cloud | AI-001 image store in SYS-08 | Adopted by departments without a security review (gap 12). See P10 |
| SYS-14 | Physical security: CCTV at yards and the HQ campus; badge access at HQ, both NOCs, and the data centers; locks on 38 tower shelters and 150 signal housings | On premises and wayside | Supports | Owned by the Director of Safety, Security, and Hazmat |

**SSP system (P02):** the *Train Dispatch and PTC Operations Platform (TDPO)*: SYS-01, SYS-02, SYS-03, the radio and dispatch-zone components of SYS-04 and SYS-09, the directory and identity provider services of SYS-05 that serve them, and the SYS-08 operations workloads and backup accounts that support them (SYS-07 crew management and the backup vault), with interfaces to SYS-06 (TMS), the host Class I's PTC system, and the 2 Class I interchange partners. Moderate baseline with tailoring.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- TSA-approved Cybersecurity Implementation Plan (2023-03-14) and Cybersecurity Assessment Plan (most recent approval 2025-06-20); annual CAP report submitted 2026-06-18
- Primary and alternate Cybersecurity Coordinators and Security Coordinators designated and reported to TSA; reachable 24/7 through the NOC
- Cybersecurity Incident Response Plan (2022, updated 2025-04); annual exercise (2025-10 tabletop tested 2 objectives)
- TSA-approved security training program (subpart B), training records kept 5 years
- MFA for all remote access, email, cloud consoles, the TMS, and the PAM jump hosts; privileged access management for IT server and cloud administrators
- IT/OT boundary firewalls at the HQ data center and both NOCs (deny by default); CAD and PTC vendors reach OT only through the PAM jump host with MFA and session recording
- EDR on all Windows endpoints and servers, including dispatch consoles; MSSP 24x7 monitoring of IT logs
- Passive OT network monitoring at the HQ data center and both NOCs (2025)
- Write-once backups in a separate cloud backup account (35-day retention) for SYS-01, SYS-02, SYS-07, and file services
- Annual external and internal penetration test of IT (since 2024); first cybersecurity architecture design review completed 2024-02
- Security policies adopted 2023; annual training and quarterly phishing simulations
- RSSM location procedure (tested quarterly with TSA-style drills), chain-of-custody records, hazmat security plan

**Missing or weak, found in the 2026 assessments:**
1. Field OT zones are not segmented. The CTC code line, radio network, detectors, and crossing monitors share one flat backhaul across 38 tower sites. The CIP milestone for field zones (2025-12-31) was missed. OT monitoring covers only the HQ data center and the 2 NOCs.
2. Shared maintainer accounts on CTC field communication controllers (3 per vendor platform) were last changed in 2023, so departed maintainers still know them (SD 1580/82-2022-01E III.C.4.b). Default vendor passwords remain on some detector modems and crossing monitors.
3. The radio system vendor and the detector vendor keep always-on remote access (site-to-site VPN and cellular modems) outside the PAM jump host.
4. OT patching lags. CAD/CTC servers are 14 months behind vendor-certified patches. Two field communication controller firmware versions have entries in the CISA Known Exploited Vulnerabilities catalog, with no documented mitigations or timeline (SD III.E.2.b and III.E.3).
5. The assessment program is behind. The second architecture design review was due by 2026-02 (SD III.F.2.b) and is rescheduled for 2026-11. The 2025-26 CAP annual report showed 29% of CIP measures assessed, below the one-third minimum (SD III.F.2.d).
6. Recovery of the TDPO is unproven. CAD/CTC and BOS restores from the backup account have never been tested end to end. Manual dispatch has been drilled in track warrant territory only, not CTC territory. Incident response exercises have never tested IT/OT isolation (SD 1580-21-01E II.D.1.c).
7. CAD/CTC application, BOS, and field device logs do not reach the SIEM; local retention is about 30 days.
8. The OT asset inventory is about 70% complete (tower sites, crossing monitors, and detector modems lack firmware data). Field network diagrams date from 2022.
9. CAD/CTC, BOS, and TMS application roles are reviewed annually (IT accounts quarterly). Two shared dispatcher logins remain at the backup NOC. Crew tablet accounts of departing employees are disabled up to 5 days late.
10. OT vendors (radio, detector, crossing monitor, CTC field equipment) have no security or incident notice terms. The MSSP contract excludes OT.
11. SSI controls are inconsistent: copies of CIP and CAP documents were found outside the restricted SSI library, and SSI marking is not applied to the CAP annual report drafts (49 CFR 1520.9).
12. Four AI tools were adopted by departments without a security, legal, or safety review, and there is no AI use standard (P10).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | The named primary regulation **applies**: TSA SD 1580/82-2022-01E, analyzed requirement by requirement, together with SD 1580-21-01E, the TSA rules in 49 CFR parts 1570, 1580, and 1520, and the FRA tenant PTC duties in 49 CFR 236 subpart I |
| P08 incidents | **Two incident types:** (1) ransomware on the dispatch and train control back-office systems (registry default, kept); (2) ransomware or extended outage at the TMS SaaS vendor, which threatens PTC consists, interchange, and the 30-minute RSSM location duty. Both integrated with crisis management and legal |
| P09 SOC 2 | Readiness for a SOC 2 Type 2 examination on the **shared dispatch and car management service** provided to the affiliated and contracted short lines (Security, Availability, Processing Integrity), plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio: AI-001 track and equipment defect detection (registry default, kept as the anchor case), AI-002 locomotive predictive maintenance, AI-003 applicant screening, AI-004 enterprise generative AI assistant, AI-005 shipper portal chatbot |
| Cloud | Multi-account landing zone, vendor-agnostic. AWS, Azure, and Google Cloud names appear only in the P04 equivalents table |

**Why the registry defaults were kept.** The primary system (train dispatching and PTC back office), the ransomware incident, and the defect detection use case all fit a Class II railroad at this size. At this size the company runs its own PTC back office and a CTC office system, so they are a larger and more central system than at the Small size.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (applicability confirmed 2026-07-08) |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (primary NOC and HQ data center walkthrough 2026-08-11; backup NOC and Jacksonville Terminal Yard 2026-08-12; tower site, control point, and detector visit 2026-08-13) |
| 2026-09-15 | Deliverables approved by the Chief Operating Officer; High risks, risk appetite, and budget approved by the Chief Executive Officer; results presented to the board audit committee |

## 7. Facts added while building P01 to P10 (2026-10-05)

| Fact | Used in |
|---|---|
| 365 operating days a year: about $537,000 carload freight revenue per day, $586,000 total revenue per day | P05, P01 |
| 17 business processes, BP-01 to BP-17, across 9 business units | P05, P01, P08 |
| Cyber insurance: $15 million aggregate limit, $500,000 retention; the policy requires notice through the carrier hotline before incident vendors are engaged | P01, P08 |
| FY2027 security plan approved by the CEO on 2026-09-15: $1.48 million one-time and $510,000 a year | P01, P07 |
| 96 terminations and 41 transfers in the 12 months to 2026-06-30; 64 privileged accounts across IT, cloud, CAD/CTC, and BOS; June 2026 phishing simulation click rate 5.1% | P02, P07 |
| CAD/CTC application keeps train sheets, warrants, and the dispatcher log 3 years; CAD/CTC and BOS server backups kept 35 days write-once | P02, P04 |
| TSA TSOC telephone number 1-866-655-7023 for the voluntary early notice recommended by IC Surface-2025-01 (as published in the TSA notice at FR Doc. 2026-17894, 2026-09-01); company target is to call TSOC within 12 hours of discovery. CISA Central reporting at www.cisa.gov/report or (844) 729-2472 (SD 1580-21-01E II.C.3) | P08 |
| TMS vendor SOC 2 Type 2: Security, Availability, and Processing Integrity, 12 months ending 2026-03-31, unqualified, 2 exceptions | P09 |
| The shared service supports the 2 affiliates (140 route miles) and, from 2027-01-01, the contracted short line (about 90 route miles) | P05, P09 |
| Shared service agreements require notice to each client railroad within 24 hours of confirming a security incident that affects the service. The contracted short line's agreement requires a SOC 2 Type 2 report covering at least 6 months by 2027-12-31; the company plans a Type 1 as of 2027-03-31 and a Type 2 observation period from 2027-04-01 to 2027-09-30 | P08, P09 |
| Security policies POL-01 to POL-05 approved 2026-09-15 and effective 2026-10-01; 11 supporting standards (STD-01 to STD-11), 6 new in draft and 5 existing needing updates | P06, P02 |
| Vendor tiers (STD-03): 8 Tier 1 vendors (TMS, MSSP, cloud provider, identity provider, PTC vendor, CAD/CTC vendor, radio vendor, detector vendor). SOC 2 reports had been reviewed for 3 of them at P07 fieldwork | P07, P09 |
| P07 populations: 74 new CAD/CTC, BOS, and TMS accounts; 11 shared accounts (9 field maintainer, 2 dispatcher); 212 PAM vendor sessions; 140 changes to CAD/CTC, BOS, and field controllers in 2026 H1; 46 critical and high vulnerability findings in Q1-Q2 2026; 140 detector modems and crossing monitors. Two stop-and-notify findings on 2026-08-13 (an unlisted detector vendor cellular router at a hub tower; default passwords on 4 of 20 field devices) | P07 |
| AI facts: AI-001 in production on the hi-rail vehicles since 2025-06 and the portals since 2026-01, used by 14 qualified track inspectors; AI-002 since 2024-11 on 52 road locomotives; AI-003 ranking turned on by vendor default in 2026-02, about 2,400 applicants ranked, preliminary top-tier selection-rate ratio of 0.74 (women to men, conductor trainee postings), ranking switched off 2026-09-01; AI-004 for 120 users since 2026-05; AI-005 since 2026-04 | P10, P01 |

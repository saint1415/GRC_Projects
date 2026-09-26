# Scenario facts: Cris Santos Company | Transportation Systems | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, the citation is given. Regulatory facts were checked against eCFR (point in time 2026-09-23), the Federal Register, and the TSA-published directive texts on 2026-09-26.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; Cris Santos is majority owner) |
| Business | Short line freight railroad (NAICS 482112 Short Line Railroads). A Class III carrier under the Surface Transportation Board revenue classes (49 CFR part 1201, General Instructions 1-1) |
| Network | 186 route miles of company-owned track in north-central Florida: the North Subdivision (112 miles) and the South Subdivision (74 miles), both non-signaled ("dark") territory run under track warrant control from one dispatch center. Plus **26 miles of trackage rights** over a Class I railroad's main line to reach the Class I's interchange yard. The Class I does not operate on company track |
| Facilities | Headquarters and dispatch center at Central Yard (also the locomotive and car shop); North Yard office; South Yard office with a transload terminal; 7 radio tower sites; 3 wayside hot bearing and dragging equipment detectors; 41 public highway-rail grade crossings with active warning devices (standalone crossing circuits; 14 have cellular remote health monitors) |
| Equipment | 22 locomotives. **8 road locomotives carry onboard positive train control (PTC) apparatus** for the trackage-rights run. 2 hi-rail inspection trucks. 1 camera-equipped hi-rail inspection vehicle (see P10) |
| Traffic | About 38,000 carloads a year from 45 shippers: forest products (pulpwood, woodpulp, lumber), crushed stone, fertilizer, feed grain, propane (Division 2.1), and about 600 tank cars a year of chlorine and anhydrous ammonia (materials poisonous by inhalation, PIH). 2 to 3 interchange trains a day, 6 days a week |
| Location | Florida only. The whole route, including the trackage-rights segment and the interchange yard, lies outside every Florida high threat urban area (HTUA) listed in Appendix A to 49 CFR part 1580 (Fort Lauderdale, Jacksonville, Miami, Orlando, and Tampa areas, each with its 10-mile buffer). Map check by the Manager of Safety and Security on 2026-07-15 |
| Workforce | 250 employees: 92 train and engine service; 58 track and bridge maintenance of way; 14 signal and communications; 30 locomotive and car mechanical; 12 dispatch and car management (6 train dispatchers, 1 chief dispatcher, 5 car management and customer service clerks); 10 transload terminal; 4 safety and security; 5 IT; 25 executive, finance, HR, sales, and administration |
| Revenue | $36.4 million a year (fictional). SBA-small: the SBA standard for NAICS 482112 is 1,500 employees (13 CFR 121.201). Below the Class III revenue ceiling that TSA quoted from STB data in the 2024 surface cyber NPRM ($42.4 million; 89 FR 88488, footnote 123). The Director of Finance confirms the class each year against STB's published threshold |
| Customers | 45 shippers and receivers on line; the Class I connection for all interchange traffic; the transload terminal's truck customers |
| TSA status | A freight railroad carrier that "operates rolling equipment on track that is part of the general railroad system of transportation" (49 CFR 1580.1(a)(1)). So **49 CFR 1570.201 (Security Coordinator) and 1570.203 (reporting significant security concerns, including "Cyber Attack" in Appendix A to part 1570) apply**. Because it carries rail security-sensitive materials (PIH tank cars), **part 1580 subpart C applies** (1580.201): location and shipping information to TSA within 30 minutes of a request (1580.203(d)) and chain of custody (1580.205(b) and (d)). **Part 1580 subpart B does not apply** (1580.101: not Class I, no RSSM in an HTUA, not a host to a covered railroad) |
| TSA cyber directives | **Not covered.** SD 1580-21-01E and SD 1580/82-2022-01E apply to railroads in 1580.101 and railroads TSA designates by notice. TSA has never notified the company (confirmed 2026-07-15 by the President and General Manager and the Manager of Safety and Security; no TSA letter in the correspondence file). Details in P03 |
| FRA status | Subject to FRA safety rules, including accident/incident reporting (49 CFR part 225, which applies to all railroads on the general system, 225.3). **Not required to install PTC on its own track**: 49 CFR 236.1005(b)(1) places that duty on Class I railroads and railroads that provide or host intercity or commuter passenger service. **A tenant railroad on the Class I's PTC line** (236.1003): the trackage-rights run exceeds 20 miles, so the exception for unequipped Class II and III trains in 236.1006(b)(4)(iii)(A) is not available, and since 2024-01-01 each controlling locomotive on that segment must carry an operative onboard PTC apparatus (236.1006(a) and (b)(4)(iii)(B)) |
| Hazmat security | Transports PIH in any quantity and large bulk Division 2.1, so it must have a hazmat transportation security plan (49 CFR 172.800(b)(3) and (5); components in 172.802). The plan exists (reviewed 2026-02) |
| Not in scope | Passenger service (none). SEC disclosure (private company). CMMC and FAR clauses (no federal contracts). Payment cards (customers pay by invoice and ACH only). CIRCIA and the TSA surface cyber NPRM are proposed only and are tracked, not treated as obligations |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification for employee personal information, Fla. Stat. 501.171). TSA and FRA rules preempt state law on the same subject under 49 U.S.C. 20106 (49 CFR 1580.5), so the samples otherwise stay federal |

**Regulatory driver IDs used in this folder.** The vertical's `requirements.csv` lists C-TRANSPORTATION-R01 to R07. Of these, R01 (TSA rail cyber directives) does not apply and is used only for readiness rows; R06 (TSA surface cyber NPRM) and R07 (CIRCIA) are proposed rules, tracked only; R02 to R05 (pipeline, aviation, maritime) do not apply to a railroad. The binding rules that do apply are not in the registry, so this sample adds **scenario-level driver IDs**. They are defined here and nowhere else.

| ID | Requirement | Citation | Status for this company |
|---|---|---|---|
| C-TRANSPORTATION-S01 | TSA Security Coordinator and reporting of significant security concerns | 49 CFR 1570.201; 1570.203 and Appendix A to part 1570; 1570.105 | Applies (1580.1(a)(1) freight railroad) |
| C-TRANSPORTATION-S02 | TSA rail security-sensitive materials (RSSM) operations | 49 CFR part 1580 subpart C (1580.201, 1580.203, 1580.205) | Applies (carries PIH tank cars) |
| C-TRANSPORTATION-S03 | Protection of Sensitive Security Information (SSI) | 49 CFR part 1520 (1520.7(n), 1520.9) | Applies (covered person as a surface owner/operator subject to subchapter D) |
| C-TRANSPORTATION-S04 | FRA positive train control, tenant duties | 49 CFR part 236 subpart I (236.1006, 236.1029, 236.1033) | Applies to the 8 equipped locomotives and the trackage-rights run only |
| C-TRANSPORTATION-S05 | FRA accident/incident reporting | 49 CFR part 225 (225.9, 225.11, 225.19) | Applies |
| C-TRANSPORTATION-S06 | Hazmat transportation security plan and rail car security inspection | 49 CFR 172.800, 172.802; 174.9 | Applies |
| C-TRANSPORTATION-S07 | Florida breach notification | Fla. Stat. 501.171 | Applies to employee personal information |
| C-TRANSPORTATION-S08 | FRA track and freight car inspection duties | 49 CFR 213.7, 213.233; 215.13 | Applies (track owner and operating railroad); relevant to the AI pilot in P10 |
| C-TRANSPORTATION-BM | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 | Voluntary benchmark | Chosen because no binding cyber control rule applies |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Majority owner (Cris Santos) | Accepts High and Very High risks; approves the security budget |
| President and General Manager | Executive owner of the security program; accepts Moderate risk; signs policies |
| Vice President of Operations | Owns dispatch, train operations, and tenant PTC compliance on the Class I segment; business owner of the SSP system (P02) |
| Chief Engineer | Owns track, bridges, signals and communications; designates qualified track inspectors (49 CFR 213.7); business owner of the AI pilot (P10) |
| Manager of Safety and Security | **Primary TSA Security Coordinator** (1570.201); owns the hazmat security plan, FRA part 225 reporting, and TSA contacts |
| Chief Dispatcher | **Alternate TSA Security Coordinator**; runs the 24-hour dispatch center, which also answers TSA location requests (1580.203(f)) |
| IT Manager | Runs IT and security day to day with a managed service provider (MSP); leads this assessment. **Proposed Cybersecurity Lead**, not yet designated in writing (gap 14) |
| Signal and Communications Supervisor | Radio network, tower sites, wayside detectors, crossing monitors, and onboard PTC apparatus maintenance with the Chief Mechanical Officer |
| Chief Mechanical Officer | Locomotives and cars; onboard PTC hardware installation and seals |
| Car Management and Customer Service Manager | Transportation management system (TMS), waybills, car location data, interchange reporting |
| Director of Finance and Administration | Contracts, insurance, vendor terms, HR oversight |
| HR Manager | Onboarding, terminations, training records |
| MSP | Help desk, office endpoint patching, firewall administration, backup monitoring |
| Dispatch system vendor | Licenses and supports the computer-aided dispatch system; remote support through an always-on appliance (gap 4) |
| PTC back office vendor | Hosts the PTC back office service for the 8 equipped locomotives (SaaS); SOC 2 Type 2 reviewed in P09 |

## 3. Systems

| ID | System | Hosting | Operations-critical? | Notes |
|---|---|---|---|---|
| SYS-01 | Computer-aided dispatch system (CAD): track warrant issuance and conflict checking, train sheets, maintenance-of-way work authority (track and time), speed restrictions and bulletins, crew radio log | On premises: primary and standby servers in the HQ server room, 6 dispatch consoles plus the chief dispatcher desk | Yes | System of record for movement authority on company track. Standby server is in the same room (gap 5). OS 2 years behind because the vendor certifies patches slowly (gap 9) |
| SYS-02 | PTC tenant components: onboard PTC apparatus on 8 locomotives; the PTC administration workstation at HQ (loads locomotive and crew data, pulls onboard logs, reviews initialization failures); the vendor-hosted PTC back office service that manages the company's onboard units and exchanges messages with the Class I's PTC system through the industry interoperable messaging network | Onboard (OT); on premises (workstation); vendor SaaS (back office) | Yes | The Class I owns and certifies the PTC system on its line (PTC railroad and host, 236.1003). The company keeps its onboard units operative and its back office data current. Onboard units are in locked, sealed housings |
| SYS-03 | Transportation management system (TMS): car management, waybills, train consists, interchange reporting by EDI, hazmat car location data, demurrage and invoicing | Vendor SaaS | Yes | Supplies the train consist used for PTC initialization and the hazmat car location data TSA can request within 30 minutes. MFA enforced |
| SYS-04 | Operations network and radio: dispatch VLAN, IP radio gateway and consoles, 7 tower sites with microwave and cellular backhaul, 3 wayside detectors, 14 crossing remote health monitors (cellular) | On premises and wayside (OT) | Yes | Crossing warning circuits and detector logic are standalone; the network carries only alarms and radio voice. Detector modems use default credentials (gap 9, found in P07) |
| SYS-05 | Identity provider (single sign-on and MFA) | SaaS | Yes | Protects SYS-03, SYS-06, SYS-09, and the PTC back office portal. MFA not required for the staff remote-access VPN or server administrators (gap 6) |
| SYS-06 | Productivity suite (email, files, chat) | SaaS | No | MFA enforced. The shared file area holds the hazmat security plan and TSA-marked SSI (gap 12) |
| SYS-07 | Corporate network: HQ firewall, office LAN, dispatch VLAN, site-to-site VPN to SYS-09, VPN links to North and South Yard offices, staff remote-access VPN, dispatch vendor remote-access appliance | On premises | Yes | Routing between the office LAN and the dispatch VLAN is not filtered (gap 3) |
| SYS-08 | Endpoints: 95 office workstations and laptops, 8 operations workstations (6 dispatch consoles, chief dispatcher, PTC administration workstation), 15 shop and yard office PCs, 64 rugged crew tablets (electronic bulletins, train lists, hours-of-service entry) | On premises and mobile | Operations workstations and tablets: yes | MSP-managed signature antivirus; no endpoint detection and response (EDR) (gap 7). 2 dispatch consoles use a shared Windows login (gap 6) |
| SYS-09 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts the crew management and hours-of-service application (VM plus managed database), the file server replacement, the backup vault for SYS-01 (same account, not immutable, never restore-tested: gap 5), and the AI pilot image store and inference service (P10) |
| SYS-10 | Finance, payroll, and HR | SaaS | No | Employee personal information, including engineer and conductor certification and medical records |
| SYS-11 | Track and equipment defect detection (computer vision) pilot | Vendor model run in SYS-09; camera rig on a hi-rail vehicle; one wayside camera portal on the North Subdivision | Not yet (pilot) | Pilot since 2026-03 on the North Subdivision (see P10) |
| SYS-12 | Physical security: CCTV at Central Yard and South Yard, badge access at HQ and the dispatch center | On premises | No | Owned by the Manager of Safety and Security |

**SSP system (P02):** the *Train Dispatch and PTC Operations Platform (TDPO)*: SYS-01, SYS-02, the dispatch VLAN and radio components of SYS-04, SYS-05, the operations workstations in SYS-08, and the SYS-09 components that support them (backup vault), with interfaces to SYS-03 (TMS) and to the Class I's dispatch and PTC systems.

## 4. Current security posture: partially compliant

**In place today:**
- Primary and alternate TSA Security Coordinators designated and reported to TSA (1570.201); reachable 24/7 through the dispatch center
- A monitored 24/7 telephone number for TSA location requests, with a tested procedure to pull hazmat car locations from the TMS within 30 minutes (1580.203)
- Chain-of-custody procedure and records for PIH cars received from shippers and handed to the Class I (1580.205(b) and (d)), kept 60 days
- Hazmat transportation security plan (172.800), reviewed 2026-02
- FRA accident/incident reporting process run by the Manager of Safety and Security (part 225)
- MFA for email, the TMS, the cloud console, and the PTC back office portal
- Onboard PTC units in locked, sealed housings; PTC back office vendor holds a SOC 2 Type 2 report
- Daily backups of the dispatch servers to the cloud tenant
- HQ firewall; site-to-site VPN to the cloud tenant; no inbound services exposed except the two remote-access VPNs
- Badge access at HQ and the dispatch center; CCTV at the two main yards
- Annual security awareness training for office staff
- Background checks at hire

**Missing or weak, found in the 2026 assessments:**
1. Cyber attacks are not treated as TSA-reportable events. There is no procedure to call the Transportation Security Operations Center (TSOC) within 24 hours (1570.203, Appendix A "Cyber Attack"). A 2025 mailbox compromise in finance was not reported.
2. No written cybersecurity incident response plan. The manual dispatch fallback (paper track warrants by radio) is a 2019 procedure that has never been exercised.
3. The dispatch VLAN is not filtered from the office LAN. Office workstations can reach the dispatch servers.
4. The dispatch system vendor has always-on remote access through a VPN appliance, using one shared vendor account.
5. Dispatch server backups sit in the same cloud account as production, are not immutable, and have never been restore-tested. The standby CAD server is in the same room as the primary.
6. No MFA on the staff remote-access VPN or on server administrator accounts. Two dispatch consoles use a shared Windows login.
7. No EDR, no central logging, and no log review. Dispatch server logs overwrite after about 14 days.
8. No inventory of operations and OT assets (radio gateway, tower equipment, detectors, crossing monitors, PTC workstation, onboard units). The network diagram dates from 2021.
9. Patching gaps: dispatch servers 2 years behind; radio gateway firmware not updated since installation. Default credentials on the 3 wayside detector modems (found during P07 testing).
10. No adopted security policies. IT practices are informal.
11. No security terms in the dispatch vendor and MSP contracts. The PTC back office vendor's SOC 2 report had never been reviewed before 2026.
12. TSA-marked SSI and the hazmat security plan sit in a shared file area open to all office staff (49 CFR 1520.9(a)).
13. Accounts of departing employees (crew tablets, TMS) are disabled 3 to 6 days late. No periodic access review.
14. No one is designated in writing to lead cybersecurity. No cyber training for dispatchers or crews, and no phishing exercises.
15. The AI defect detection pilot started without an AI use policy or an approved-tools list (see P10).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | The named primary regulation (TSA SD 1580/82-2022-01E) **does not apply**. P03 analyzes the binding TSA rules that do apply (49 CFR 1570.201, 1570.203, part 1580 subpart C, and SSI protection in 1520.9), the FRA tenant PTC duties in 49 CFR 236 subpart I, and NIST CSF 2.0 with SP 800-82 Rev. 3 as the voluntary cyber benchmark. The SD rows are kept as a readiness reference |
| P08 incident | Ransomware on the dispatch and train control back-office systems, entering through the dispatch vendor's remote-access account |
| P09 SOC 2 | The railroad is not a service organization for its customers. (a) Security-only self-benchmark against the Common Criteria; (b) review of the PTC back office vendor's SOC 2 Type 2 report |
| P10 AI | Track and equipment defect detection (computer vision) pilot |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork (applicability confirmed 2026-07-15) |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (dispatch center and Central Yard walkthrough 2026-08-05; tower site and detector visit 2026-08-06) |
| 2026-08-31 | Deliverables approved by the President and General Manager; High risks and budget approved by the majority owner |

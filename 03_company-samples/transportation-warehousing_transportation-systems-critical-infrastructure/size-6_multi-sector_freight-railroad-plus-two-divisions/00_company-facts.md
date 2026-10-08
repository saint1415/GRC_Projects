# Scenario facts: Cris Santos Company | Transportation Systems | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given. Regulatory text was read on eCFR (point in time 2026-09-23; 12 CFR 225.28 and 16 CFR 314.2 read on 2026-10-05), in the Federal Register, in the U.S. Code (15 U.S.C. 44 and 45 on govinfo.gov), and in the TSA-published directive texts (SD 1580-21-01E dated 2026-01-09 and SD 1580/82-2022-01E dated 2026-05-01, both not marked SSI) between 2026-09-26 and 2026-10-05.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant, not a smaller reporting company; owns its operating companies through wholly owned subsidiaries) |
| Structure | A holding company with three divisions and corporate shared services. Each railroad, terminal company, and property company is a separate subsidiary |
| Division 1: Freight Railroad (NAICS 482112), **focus of this scenario** | **72 short line and regional freight railroads: 68 Class III and 4 Class II** under the Surface Transportation Board revenue classes (49 CFR part 1201, General Instructions 1-1). No subsidiary is a Class I railroad. The railroads are geographically separate lines that each interchange with one or more Class I railroads. About 10,200 route miles in 26 states. About 17,500 employees. Revenue about $4.9 billion. Also sells a **contract dispatching and car management service (CDS)** to 11 unaffiliated short lines |
| Division 2: Transload and Wholesale (NAICS 424690, sector 42 Wholesale Trade) | Merchant wholesaler of bulk industrial products (plastics resins, industrial chemicals, lumber and building products, dry fertilizer, road salt, and aggregates) that moves most of its volume through **58 rail-to-truck transload terminals** in 19 states, 41 of them on group railroads. About 9,600 business customers. Private truck fleet of about 2,300 tractors. About 21,000 employees. Revenue about $12.2 billion |
| Division 3: Railside Industrial Real Estate (NAICS 531120, sector 53 Real Estate) | Owns and manages about 4,300 acres of rail-served industrial land and **152 buildings** (warehouses, cross-docks, transload sheds; about 33 million square feet) in 14 states, leased to about 640 commercial tenants. Also runs the **right-of-way licensing program** for crossings and occupancies of group railroad property (about 6,100 active licenses for utility crossings, fiber, and signage). About 1,700 employees. Revenue about $0.9 billion |
| Corporate shared services | Identity, security operations, cloud and network, the group integration platform, ERP (finance, procurement, HR, payroll), legal, and internal audit. About 4,800 employees |
| Why this combination | Short line holding company with transload and property arms: the terminals and industrial parks generate carloads for the railroads, and the railroads make the land valuable |
| Location | Headquarters, the primary Network Operations Center (NOC), and data center DC-1 in Jacksonville, Florida. Backup NOC and colocation data center DC-2 outside Florida. Operations in 28 states, none in California. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | **45,000 employees; about $18.0 billion revenue** (fictional). The Freight Railroad division earns most of the group's operating income and value added, so the group reports NAICS 482112 as its primary industry. Not SBA-small (SBA standard for NAICS 482112 is 1,500 employees, 13 CFR 121.201) |
| Traffic | About 1.7 million carloads a year on the railroads. About 36,000 tank car moves a year of rail security-sensitive materials (RSSM), mostly chlorine and anhydrous ammonia (materials poisonous by inhalation, PIH), on 27 railroads. The Transload and Wholesale division handles no PIH and no other RSSM category (division standard) |
| TSA status (all 72 railroads) | Each is a freight railroad carrier that "operates rolling equipment on track that is part of the general railroad system of transportation" (49 CFR 1580.1(a)(1)). So **49 CFR 1570.201 (Security Coordinator) and 1570.203 (reporting significant security concerns within 24 hours, including "Cyber Attack" in Appendix A to part 1570) apply to all 72**, and each is a covered person for Sensitive Security Information (SSI) under 49 CFR 1520.7(n). **Part 1580 subpart C applies to the 27 railroads that carry RSSM** (1580.201); none is Class I, so the answer to a TSA location request is due within 30 minutes (1580.203(d)) |
| TSA status (Covered Railroads) | **14 railroads meet 49 CFR 1580.101** and so need a TSA-approved security training program (1580.113, 1580.115): **CR-01 to CR-10** transport RSSM in a high threat urban area (HTUA) (1580.101(b)); **CR-11 to CR-14** serve as host railroads to passenger operations described in 1582.101 (1580.101(c)): CR-11 and CR-12 host Amtrak (1582.101(a)); CR-13 and CR-14 host a commuter railroad identified in Appendix A to part 1582 (1582.101(b)). Florida worked example: CR-01 and CR-02 carry PIH inside the Jacksonville and Tampa HTUAs (Appendix A to part 1580) |
| TSA cyber directives | **Apply to the 14 Covered Railroads.** SD 1580-21-01E (effective 2026-01-16 to 2027-01-15) and SD 1580/82-2022-01E (effective 2026-05-03 to 2027-05-02) apply to "each freight railroad carrier identified in 49 CFR 1580.101." The 14 share one NOC, one dispatch and PTC platform, and the corporate network, so the division keeps **one Cybersecurity Implementation Plan (CIP)** naming all 14 and their shared Critical Cyber Systems. **TSA approved it on 2023-07-26**; Cybersecurity Assessment Plan (CAP) last approved 2025-11-14. The other 58 railroads are not covered, but division policy applies the same controls to every railroad on the shared platform |
| FRA status | All 72 are subject to FRA accident/incident reporting (49 CFR part 225) and, as track owners, the track safety standards (part 213). **PTC host duty on 4 railroads:** 49 CFR 236.1005(b)(1) requires "each railroad providing or hosting intercity or commuter passenger service" to install and operate a certified PTC system on main lines used for regularly provided passenger service, so CR-11 to CR-14 operate an FRA-certified PTC system on **238 route miles** (204 wayside interface units). **PTC tenant duty on 24 railroads:** their trains run more than 20 miles on Class I PTC lines, so the exception for unequipped Class II and III trains in 236.1006(b)(4)(iii)(A) is not available and each controlling locomotive there must carry an operative onboard PTC apparatus (236.1006(a)). About 1,520 locomotives, 330 with onboard PTC apparatus |
| Hazmat security | The railroads transport PIH, and the Transload and Wholesale division offers and transports large bulk quantities of Class 3 Packing Group II materials (ethanol and methanol by cargo tank), so both divisions must have a hazmat transportation security plan (49 CFR 172.800(b)(5) and (b)(6); components in 172.802). One plan per division |
| Federal contracts | The Transload and Wholesale division holds **7 supply contracts with federal civilian agencies** (road salt, aggregates, lumber) that include FAR 52.204-21, 52.204-23, and 52.204-25. Its order and invoicing records for those contracts are Federal Contract Information (FCI). No Department of Defense contracts and no Controlled Unclassified Information (CUI), so DFARS 252.204-7012 and CMMC do not apply (recheck when a DoD contract is bid) |
| SEC and financial reporting | Form 8-K Item 1.05 (material cybersecurity incidents, within 4 business days after the materiality determination); Regulation S-K Item 106 (17 CFR 229.106) annual disclosure in the Form 10-K; SOX Section 404 IT general controls over the ERP |
| State law approach | **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida (Fla. Stat. 501.171) as the worked example. Personal information held: about 45,000 current and 118,000 former employees (including engineer and conductor certification and medical records and commercial driver records), about 210 individual guarantors of tenant leases, and business contacts. TSA and FRA rules preempt state law on the same subject under 49 U.S.C. 20106 (49 CFR 1580.5) |
| FTC Act Section 5 | Applies to the Transload and Wholesale and Real Estate divisions and to corporate. The Act exempts "common carriers subject to the Acts to regulate commerce" (15 U.S.C. 45(a)(2)), and those Acts include subtitle IV of title 49 (15 U.S.C. 44), the rail carrier subtitle, so the railroads' common carrier activity is outside it. The group does not rely on the exemption: group policy applies the same security program everywhere |
| Not in scope | Passenger operations (the group hosts passenger trains but runs none and holds no passenger data). Maritime, pipeline, and aviation rules (no MTSA facility, pipeline, or airport). DFARS 252.204-7012 and CMMC (no DoD contracts). The FTC Safeguards Rule (16 CFR part 314): the Real Estate division's customers are businesses, not "consumers" (individuals obtaining a financial product for personal, family, or household purposes, 314.2), and its leases are operating leases, not the nonoperating, full-payout leases that 12 CFR 225.28(b)(3) treats as a financial activity. CCPA (no operations or sales in California). Payment cards (customers and tenants pay by invoice, ACH, and wire). HIPAA (the employee health plan is a separate covered entity outside these deliverables). CIRCIA and the TSA surface cyber NPRM are proposed only and are tracked, not treated as obligations |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

**Regulatory driver IDs used in this folder.** The vertical's `requirements.csv` lists C-TRANSPORTATION-R01 to R07. **R01 (TSA rail cyber directives) applies** to the 14 Covered Railroads and is the primary regulation in P03, cited with the directive section, for example `C-TRANSPORTATION-R01 (SD 1580/82-2022-01E III.C.4)`. R06 (TSA surface cyber NPRM) and R07 (CIRCIA) are proposed rules, tracked only. R02 to R05 (pipeline, aviation, maritime) do not apply. Division 2 and 3 obligations use the registry IDs of their own industries (N42 Wholesale Trade, N53 Real Estate). The other binding rules are not in the registry, so this sample adds **scenario-level driver IDs**, defined here and nowhere else. S01 to S08 keep the meanings used in the Small sample of this vertical.

| ID | Requirement | Citation | Status for this company |
|---|---|---|---|
| C-TRANSPORTATION-R01 | TSA rail cybersecurity directives | SD 1580-21-01E; SD 1580/82-2022-01E | Applies to CR-01 to CR-14 |
| C-TRANSPORTATION-S01 | TSA Security Coordinator, applicability determinations, and reporting of significant security concerns | 49 CFR 1570.105, 1570.201, 1570.203 and Appendix A to part 1570 | Applies to all 72 railroads |
| C-TRANSPORTATION-S02 | TSA RSSM operations | 49 CFR part 1580 subpart C (1580.201, 1580.203, 1580.205) | Applies to the 27 railroads that carry RSSM |
| C-TRANSPORTATION-S03 | Protection of SSI | 49 CFR part 1520 (1520.5, 1520.7(n), 1520.9) | Applies to the railroads and to every group employee or contractor who handles their SSI |
| C-TRANSPORTATION-S04 | FRA positive train control | 49 CFR part 236 subpart I (236.1005, 236.1006, 236.1023, 236.1029, 236.1033) | Host duties on CR-11 to CR-14; tenant duties on 24 railroads |
| C-TRANSPORTATION-S05 | FRA accident/incident reporting | 49 CFR part 225 | Applies to all 72 railroads |
| C-TRANSPORTATION-S06 | Hazmat transportation security plan, rail car security inspection, and immediate hazmat incident notice | 49 CFR 172.800, 172.802; 174.9; 171.15 | Applies to the railroads and to the Transload and Wholesale division |
| C-TRANSPORTATION-S07 | State breach notification (Florida worked example) | Each state where affected individuals reside; Fla. Stat. 501.171 | Applies to every division |
| C-TRANSPORTATION-S08 | FRA inspection and recordkeeping duties touched by group systems | 49 CFR 213.7, 213.233 (track); 215.13 (freight cars); 229.21 (locomotive daily inspection); 228.11 (hours of duty records) | Applies; relevant to P05 and P10 |
| C-TRANSPORTATION-S09 | TSA security training program | 49 CFR 1580.113, 1580.115; 1570.109, 1570.111 | Applies to CR-01 to CR-14 |
| C-TRANSPORTATION-S10 | SEC cybersecurity disclosure | Form 8-K Item 1.05; 17 CFR 229.106 | Applies to the group (same rule as N42-R07 and N53-R05) |
| N42-R01, N53-R02 | FTC Act Section 5 | 15 U.S.C. 45(a) | Applies to Divisions 2 and 3 and corporate |
| N42-R04 | FAR basic safeguarding of covered contractor information systems | 48 CFR 52.204-21 | Applies to the Division 2 systems that process FCI |
| N42-R05 | FAR covered telecommunications prohibition and reporting | 48 CFR 52.204-25 (with 52.204-23 for Kaspersky covered articles) | Applies to Division 2's federal contracts |
| N42-R06 | CTPAT | CBP voluntary program | Not joined; considered in P03 |
| N53-R01 | FTC Safeguards Rule | 16 CFR part 314 | Not applicable (no consumer customers); used as a reference for Division 3 controls |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors: audit committee; safety, security, and risk committee | Cyber risk oversight (Item 106 governance). The safety, security, and risk committee receives the group risk profile quarterly and accepts Very High risks; the audit committee oversees group internal audit, SOX, and disclosure controls |
| Chief Executive Officer; Chief Financial Officer | Members of the disclosure committee; approve the security budget |
| Group CISO | Owns the group security program and group policies; operates common controls through SYS-G1 to SYS-G5; **primary TSA Cybersecurity Coordinator** for CR-01 to CR-14 (SD 1580-21-01E II.B; U.S. citizen) |
| Group Chief Risk Officer | Owns the group risk register and the enterprise risk management (ERM) roll-up (NIST IR 8286 Rev. 1); co-accepts High risks with the Group CISO |
| Group General Counsel | Chairs the disclosure committee; owns the group notification matrix, intercompany agreements, and legal holds |
| Group CIO | Runs corporate IT; common control provider for SYS-G3 to SYS-G5 |
| Chief Audit Executive | Heads group internal audit (third line, reports functionally to the audit committee); leads the P07 assessment with co-sourced OT specialists |
| President, Freight Railroad; President, Transload and Wholesale; President, Real Estate | Division business owners; accept Moderate risks for their divisions |
| Division security and compliance leads (3) | Vice President, Rail Cybersecurity (Freight Railroad); Director, Security and Compliance (Transload and Wholesale); Manager, Security and Compliance (Real Estate). Maintain division registers and supplements; accept Low risks |
| Chief Operating Officer, Freight Railroad | Business owner of dispatching and PTC; authorizing official for the SSP system (P02) |
| Vice President, Rail Security | **Primary TSA Security Coordinator** for all 72 railroads (1570.201, appointed at the corporate level); owns the railroad hazmat security plan and the TSA security training program |
| Director, Network Operations Center | **Alternate TSA Security Coordinator** (reachable 24/7 through the NOC); runs dispatching, crew calling, and the 24/7 TSA location request line; system owner of the SSP system (P02) |
| Director, Rail OT Security | Owns OT security for dispatch, PTC, CTC, and wayside systems; **alternate TSA Cybersecurity Coordinator** |
| Group SOC Director | Runs the 24x7 group security operations center (SOC); **alternate TSA Cybersecurity Coordinator** |
| Chief Safety Officer, Freight Railroad | FRA compliance and part 225 reporting oversight; business owner of the AI defect detection program (P10) |
| Hazmat compliance managers (Railroad; Transload and Wholesale) | Each division's hazmat security plan (172.800) and 171.15 notices |
| Federal contracts compliance manager (Transload and Wholesale) | FAR clause compliance for the 7 federal contracts |
| Director, Facilities Technology (Real Estate) | Building automation, access control, and CCTV across the 152 buildings |
| Disclosure committee | Group General Counsel (chair), CEO, CFO, Controller, Group CISO, Group Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. Decides SEC materiality |

**Overlap and independence.** At this size roles are separated into three lines. The Group CISO's organization and the division security teams design and run controls; the Group Chief Risk Officer's GRC team (second line) runs the risk method and the gap analyses; group internal audit (third line) assesses controls and neither designs nor operates them. Two deliberate overlaps: (1) the Group CISO is both the program owner and the primary TSA Cybersecurity Coordinator, so TSA-facing reports are reviewed by the Group General Counsel before submission; (2) the Real Estate division is too small for its own security staff beyond one manager, so its controls are run by corporate under an intercompany service agreement and its lead reports dotted-line to the Group CISO.

## 3. Systems

| ID | System | Owner | Hosting | Notes |
|---|---|---|---|---|
| SYS-G1 | Group identity platform: single sign-on, MFA, privileged access management (PAM), identity governance; plus a separate rail OT directory | Corporate | SaaS identity provider; on-premises directories | A one-way trust from the rail OT directory to the corporate directory has never been reviewed (gap 4) |
| SYS-G2 | Group SOC, SIEM, and endpoint detection and response (EDR) | Corporate | SaaS SIEM data lake; in-house SOC with a managed security service provider (MSSP) for overnight tier 1 triage | EDR on 96% of IT endpoints; not at 21 acquired terminals (gap 5) |
| SYS-G3 | Group cloud platform (provider A and provider B, vendor-agnostic), data centers DC-1 and DC-2, and the enterprise network (SD-WAN to about 600 sites) | Corporate | Cloud and data centers | Common landing zone with guardrails, keys, central logging, immutable backups |
| SYS-G4 | Group ERP: finance, procurement, accounts payable, HR, payroll | Corporate | SaaS | SOX-relevant; holds employee personal information for all divisions |
| SYS-G5 | Group integration platform: EDI and API hub, managed file transfer | Corporate | Cloud provider A | Connects the rail TMS, the terminal operating system, the ERP, the property system, and customers. Carries car orders and car location data between the railroads and the terminals, so it is a dependency of the rail Critical Cyber Systems not described in the CIP (gap 1) |
| SYS-R1 | Centralized computer-aided dispatch and CTC office system (CAD): track warrants and track and time authority with conflict checking, CTC dispatcher displays, train sheets, bulletins and speed restrictions | Freight Railroad | On premises: primary cluster in DC-1, hot standby in DC-2; 156 dispatch consoles at the primary and backup NOCs | Dispatches all 72 railroads and the 11 CDS customers |
| SYS-R2 | PTC back office: office segment of the PTC system for the 4 host railroads (CR-11 to CR-14), back office for the 330 company locomotives with onboard PTC apparatus, interoperable messaging with Class I and passenger operators' back offices, PTC key management | Freight Railroad | On premises: DC-1 primary, DC-2 standby | Back office servers 8 months behind on operating system patches (gap 2) |
| SYS-R3 | CTC and wayside OT: CTC code servers and field code units, wayside interface units, crossing remote monitoring, wayside detectors, machine vision portals, radio and microwave network | Freight Railroad | On premises, wayside, and towers | OT asset inventory 86% complete (gap 3) |
| SYS-R4 | Rail transportation management system (TMS): car management, waybills, interchange EDI, RSSM car location data, demurrage | Freight Railroad | Cloud provider A (PaaS) | Supplies train consists for PTC initialization and the RSSM data for 30-minute TSA requests; core of the CDS service |
| SYS-R5 | Crew management, calling, and hours-of-service records (49 CFR 228.11) | Freight Railroad | Cloud provider A | Employee personal information |
| SYS-W1 | Terminal operating system (TOS): rail car and truck scheduling, inventory, bills of lading, hazmat shipping papers for truck loads | Transload and Wholesale | Cloud provider A | Exchanges car orders and car placement data with SYS-R4 through SYS-G5 |
| SYS-W2 | Terminal OT at 58 terminals: loading rack controllers, truck scales, tank level and valve controls, conveyors, gate kiosks | Transload and Wholesale | On premises at terminals | 21 terminals acquired in 2024 and 2025 still run flat networks with vendor remote access (gap 5) |
| SYS-W3 | Wholesale commerce: order management and pricing on the group ERP, customer portal, EDI with customers and suppliers, the federal contracts workspace (FCI) | Transload and Wholesale | SaaS and cloud provider A | Payment fraud losses in 2025 (gap 6) |
| SYS-W4 | Fleet dispatch, telematics, and electronic logging devices | Transload and Wholesale | SaaS | Driver personal information |
| SYS-E1 | Property management and lease administration with a tenant portal | Real Estate | SaaS | Tenant contacts and guarantor personal financial information |
| SYS-E2 | Building OT at 152 buildings: building automation (BAS), access control, CCTV, fire alarm monitoring | Real Estate | On premises; vendor-managed | Shared vendor logins; 9 BAS controllers reachable from the internet (gap 7, found in P07) |
| SYS-E3 | Right-of-way licensing and engineering document portal | Real Estate | SaaS | Shares track charts and bridge drawings with licensees |
| SYS-G6 | Group AI portfolio (11 use cases) | Corporate and divisions | Mostly cloud provider B and vendor services | Governed by the Group AI council formed 2026-02 |

**SSP system (P02):** the *Train Dispatching and PTC Back Office Platform (TDPB)*: the Freight Railroad division's SYS-R1 (CAD), SYS-R2 (PTC back office), the CTC office code servers from SYS-R3, the NOC operations network zone and industrial DMZ, and the 156 dispatch consoles at the primary and backup NOCs, inheriting group common controls from SYS-G1 to SYS-G3, with interfaces to SYS-R4 (TMS), SYS-R5 (crew system), SYS-G5 (integration platform), Class I and passenger operators' dispatch and PTC systems, and the CDS customers.

## 4. Current security posture: varies by division

**In place today:**
- A group security program aligned to NIST CSF 2.0, with NIST SP 800-82 Rev. 3 for OT; group policies with a Freight Railroad supplement
- TSA-approved CIP since 2023-07-26 for CR-01 to CR-14; CAP approved every year; cybersecurity architecture design reviews by an independent firm in 2024-05 and 2026-05
- Annual group and division risk analyses rolled up to ERM (NIST IR 8286 Rev. 1)
- 24x7 group SOC with SIEM and EDR on 96% of IT endpoints
- PAM and MFA for all remote and privileged access to rail systems; IT/OT segmentation through an industrial DMZ for the railroads
- Immutable backups in separate accounts; annual disaster recovery (DR) tests for tier-1 systems
- Tiered third-party risk program
- SEC Item 106 disclosure in the Form 10-K; disclosure committee in place
- Group AI Standard and Group AI council (2026-02)

**Maturity by division.** Freight Railroad: defined program, driven by the TSA directives, with gaps in scale. Transload and Wholesale: developing; corporate controls reach its offices but not 21 acquired terminals. Real Estate: basic; building systems are run by vendors.

**Gaps:**
1. **Shared integration platform.** SYS-G5 carries car orders and car location data between the rail TMS and the terminal operating system and connects to the ERP and customers. It is a dependency of the rail Critical Cyber Systems, but it is not described in the CIP's interdependency list (SD 1580/82-2022-01E III.B.1.a) and has no CIP amendment (VI.B.2). Its managed file transfer component also holds HR export files for all divisions.
2. **PTC back office patching and recovery.** PTC back office servers are 8 months behind on operating system patches because the PTC vendor certifies patches slowly, and no compensating measures are documented (III.E.3). In the 2026-04-18 DR test the PTC back office took 7.5 hours to fail over to DC-2 against a 4-hour recovery time objective (RTO).
3. **OT asset inventory.** 86% complete for rail wayside and field equipment; terminal OT and building OT inventories do not exist in a central form.
4. **Access in OT.** A one-way trust from the rail OT directory to the corporate directory has never been reviewed (III.C.5). CTC code servers use 3 shared administrator accounts (III.C.4).
5. **Acquired terminals.** 21 transload terminals acquired in 2024 and 2025 run flat networks, local accounts, vendor-managed loading rack controllers with always-on remote access, and no EDR.
6. **Payment fraud.** The Transload and Wholesale division lost $2.3 million in 2025 to two vendor bank-account change frauds. Call-back verification is policy but not enforced in the ERP workflow for 3 of 7 accounts payable teams. Real Estate had one rent-redirection attempt in 2026.
7. **Building OT.** Building systems at the 152 buildings are vendor-managed with shared logins and no inventory; 9 BAS controllers were found reachable from the internet during P07 testing.
8. **Multi-regulator notification.** An incident in a shared service could trigger TSA and CISA reports for 14 railroads, TSOC reports for others, SEC disclosure, state breach notices for employees of all divisions, customer and tenant contract notices, and FAR reports. The division playbooks are separate and the group notification matrix has not been exercised.
9. **Division supplements.** Only the Freight Railroad division has a policy supplement (aligned to the CIP). Transload and Wholesale and Real Estate have none, so terminal and building OT have no written standards.
10. **Common control inheritance.** Inheritance from corporate is documented for the railroads (in the CIP) but not for Transload and Wholesale or Real Estate.
11. **AI.** 11 AI use cases; 5 have completed council review. The defect detection models (AI-001) were validated on Class I main line data, not on short line track; a wholesale pricing model and a lease abstraction tool went live before the AI Standard existed.
12. **SSI handling.** The CIP, the CAP report, and the railroad hazmat security plan were found in a corporate file share readable by 340 users across all divisions (49 CFR 1520.9(a)).

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 | Train Dispatching and PTC Back Office Platform (TDPB), a Freight Railroad division system that inherits group common controls; a common control catalog for all divisions. The registry default fits this size unchanged |
| P03 | The named primary regulation (TSA SD 1580/82-2022-01E) **applies** to CR-01 to CR-14 and is analyzed requirement by requirement, with SD 1580-21-01E and the other binding rail rules. Division tables for Transload and Wholesale and Real Estate, a group table, and a regulation-by-division matrix |
| P08 | Ransomware on the dispatch and train control back-office systems, entering through the shared integration platform and touching all three divisions: TSA/CISA reports, the SEC materiality step, and state breach notices |
| P09 | SOC 2 scoped per division: the Freight Railroad division's contract dispatching and car management service (CDS) is in scope (first report); Transload and Wholesale terminal inventory services are routed to SOC 1; Real Estate is out of scope |
| P10 | Group AI governance program (11 use cases) with a full assessment of AI-001, track and equipment defect detection (computer vision). The registry default fits this size unchanged |
| Cloud | Shared corporate platform (provider A and provider B, vendor-agnostic) plus division workloads; AWS, Azure, and Google Cloud names appear only in the P04 equivalents table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses and gap analyses (applicability confirmed 2026-05-08) |
| 2026-07-06 to 2026-08-28 | Common control assessment by group internal audit, plus division samples (NOC walkthrough 2026-07-15; DC-2 and backup NOC 2026-07-22; CR-13 PTC wayside visit 2026-07-29; two terminals 2026-08-05 and 2026-08-06; two buildings 2026-08-12) |
| 2026-09-04 | Assessment report issued |
| 2026-09-10 | Results to the board safety, security, and risk committee and the audit committee; group register, High treatments, and policies approved |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Revenue per day | Freight Railroad about $13.4 million; Transload and Wholesale about $33 million in sales (low margin); Real Estate about $2.5 million | P05 |
| Business processes | 27 processes: BP-G01 to BP-G07 (group), BP-R01 to BP-R10 (railroad), BP-W01 to BP-W06 (terminals and wholesale), BP-E01 to BP-E04 (real estate) | P05, P01, P08 |
| Rail scale details | 1,480 CTC route miles on 12 railroads; manual CTC dispatch exercised at 7 of the 12; about 9,000 train and engine employees; 980 remotely monitored crossings; 560 wayside detectors; 8 machine vision portals; 24 camera-equipped hi-rail vehicles; about 210 radio tower sites | P05, P01, P07, P10 |
| TDPB users | About 640 users on 156 consoles; 6 consoles are the CDS dispatch desk | P02, P09 |
| Integration platform change | Terminals began sending car placement data through SYS-G5 into the TMS interface server on 2025-09-15; no CIP amendment request was filed, so the 50-day window (SD 1580/82-2022-01E VI.D) passed in 2025-11. 14 partner credentials on SYS-G5 are older than 1 year; HR export files are never purged | P02, P03, P07, P08 |
| DR test 2026-04-18 | CAD failed over to DC-2 in 1.4 hours (RTO 2 hours); PTC back office 7.5 hours (RTO 4 hours) because the standby was not at the production patch and configuration level | P02, P05, P07 |
| OT access and logging | 3 shared administrator accounts on CTC code servers; 2 administrators who knew the passwords left in 2026. SIEM collects 58% of rail OT log sources; CTC code servers and the PTC back office keep 30 days of local logs | P02, P03, P07 |
| CIP milestones | OT log forwarding for CTC and PTC servers was due 2026-06-30 and was missed; CAP annual report and update due 2026-11-14 | P03 |
| SSI exposure | The CIP, a CAP report, the CIRP, and the railroad hazmat security plan were readable by 340 users in a corporate share; access log review in progress | P03, P07 |
| Acquired terminals | 21 terminals acquired in 2024 and 2025; 6 of them use local internet service; 23 hazmat terminals give the loading rack vendor always-on remote access; rack configurations are backed up at 37 of 58 terminals; terminal network equipment budget of $1.9 million approved 2026-09-10 | P03, P05, P07 |
| Federal contracts | FCI in a workspace limited to 23 users; 2 contract haulers on older agreements without the FAR 52.204-21 flow-down; the contracts office shares a building with a tenant | P03, P04 |
| Building OT | 5 building OT vendors, 2 with SOC 2 reports; building networks at 64 sites on SYS-G3 and 88 vendor-managed; 11 temperature-controlled warehouses; 9 BAS controllers reachable from the internet, 7 fixed on 2026-08-20 | P03, P05, P07 |
| Third parties | 17 of about 160 tier-1 vendor reviews overdue; PTC vendor certifies operating system patches about 6 months after release | P01, P07 |
| TSA contacts | TSOC telephone 1-866-655-7023; IC Surface-2025-01 recommends notice to the TSOC no more than 12 hours after discovery of a significant cybersecurity incident (TSA information collection notice, FR Doc. 2026-17894, 2026-09-01). CISA Central: www.cisa.gov/report or (844) 729-2472 (SD 1580-21-01E II.C.3) | P03, P08 |
| CDS service | 11 unaffiliated short lines (2 with CTC); agreements commit to 99.9% availability, 4-hour recovery, and incident notice within 24 hours; 2 customers asked for a SOC 2 Type 2 report by the end of 2027 | P02, P05, P09 |
| Terminal inventory services | Customer-owned product stored at 14 terminals; 3 large customers asked for a SOC report on inventory controls | P09 |
| State footprint for AI laws | The group has employees in Colorado and Illinois (railroads and terminals) | P10 |
| AI | 11 use cases (AI-001 to AI-011); Group AI Standard and council adopted 2026-02; AI-001 runs on 9 railroads; a 2026-06 field comparison on 2 short lines found 71% recall for broken joint bars against 93% in the vendor report | P01, P10 |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board safety, security, and risk committee. Very High: the board committee only | P01, P06 |

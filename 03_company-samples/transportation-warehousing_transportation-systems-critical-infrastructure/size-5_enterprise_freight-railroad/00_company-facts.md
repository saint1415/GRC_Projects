# Scenario facts: Cris Santos Company | Transportation Systems | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given. Regulatory text was read on eCFR (point in time 2026-09-23), in the Federal Register, and in the TSA-published directive texts (SD 1580-21-01E dated 2026-01-09; SD 1580/82-2022-01E dated 2026-05-01, both not marked SSI) between 2026-09-26 and 2026-10-05.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded holding company and SEC registrant, not a smaller reporting company; it owns its railroads through wholly owned subsidiaries) |
| Business | Short line and regional freight railroad holding company (NAICS 482112 Short Line Railroads). It owns **64 freight railroads: 60 Class III and 4 Class II** under the Surface Transportation Board revenue classes (49 CFR part 1201, General Instructions 1-1). No subsidiary is a Class I railroad. The railroads are geographically separate lines that each interchange with one or more Class I railroads; they are not operated as "a single, integrated rail system," so each is classified on its own revenue (1-1(b)(1)). The Controller confirms each railroad's class every year |
| Rail services | A second segment sells (a) industrial switching at 38 customer plants and 12 transload terminals, and (b) two railroad technology services to **unaffiliated** railroads: **SL-1 hosted PTC back office service** (27 short lines, 310 of their locomotives) and **SL-2 dispatch and car management platform** (18 short lines and industrial railroads) |
| Network | About 11,400 route miles in **27 states** (not California). 1,620 miles are signaled and run by centralized traffic control (CTC) on 11 railroads (the 4 Class II railroads and 7 Class III railroads); the rest is non-signaled ("dark") territory under track warrant control. 2,950 public grade crossings with active warning devices, 1,140 of them remotely monitored; 640 wayside detectors; 9 machine vision car inspection portals |
| Facilities | Headquarters and the primary Network Operations Center (NOC) in Jacksonville, Florida, with company-owned data center DC-1 on the same campus. A backup NOC and colocation data center DC-2 in Texas. About 290 field sites (yards, shops, crew offices, regional offices) in 5 operating regions: Southeast, Gulf, Central, Northeast, and West |
| Equipment | About 1,180 locomotives, 236 of them carrying onboard positive train control (PTC) apparatus; 410 hi-rail and track inspection vehicles (24 with camera kits for AI-001) |
| Traffic | About 1.9 million carloads a year: chemicals and plastics, agricultural products, minerals and aggregates, forest products, metals, energy products, and intermodal. About 41,000 tank car moves a year of rail security-sensitive materials (RSSM), mostly chlorine and anhydrous ammonia (materials poisonous by inhalation, PIH), on 31 railroads |
| Workforce | **12,000 employees**: 6,900 train, engine, and yard service; 1,800 engineering (track, bridge, signal); 1,100 mechanical; 520 network operations (310 train dispatchers, crew callers, car management); 620 information technology and technology services (95 in the CISO organization); 1,060 corporate, sales, and rail services |
| Revenue | About **$4.8 billion** a year (fictional): rail operations about $4.2 billion, rail services about $0.6 billion. About $13.2 million per calendar day. Not SBA-small: the SBA standard for NAICS 482112 is 1,500 employees (13 CFR 121.201) |
| Growth by acquisition | 6 railroads acquired in 2025-2026 (AQ-01 to AQ-06; details in section 7) |
| TSA status (all 64 railroads) | Each is a freight railroad carrier that "operates rolling equipment on track that is part of the general railroad system of transportation" (49 CFR 1580.1(a)(1)). So **49 CFR 1570.201 (Security Coordinator) and 1570.203 (reporting significant security concerns within 24 hours, including "Cyber Attack" in Appendix A to part 1570) apply to all 64**, and each is a covered person for Sensitive Security Information (SSI) under 49 CFR 1520.7(n). **Part 1580 subpart C (RSSM location and chain of custody) applies to the 31 railroads that carry RSSM** (1580.201(1)); they are not Class I, so the TSA location answer is due within 30 minutes (1580.203(d)) |
| TSA status (Covered Railroads) | **10 railroads meet 49 CFR 1580.101** and so must have a TSA-approved security training program (1580.113, 1580.115): **CR-01 to CR-06 and CR-10** transport RSSM in a high threat urban area (HTUA) (1580.101(b)); **CR-07 to CR-09** serve as host railroads to passenger operations described in 1582.101 (1580.101(c)): CR-07 and CR-08 host Amtrak, CR-09 hosts a commuter railroad listed in Appendix A to part 1582. Florida worked example: CR-01 and CR-02 carry PIH inside the Jacksonville and Tampa HTUAs (Appendix A to part 1580). CR-10 is acquired railroad AQ-05 (section 7) |
| TSA cyber directives | **Apply to the 10 Covered Railroads.** SD 1580-21-01E (effective 2026-01-16 to 2027-01-15) and SD 1580/82-2022-01E (effective 2026-05-03 to 2027-05-02) apply to "each freight railroad carrier identified in 49 CFR 1580.101." Each Covered Railroad is an Owner/Operator. Because CR-01 to CR-09 share one NOC, one dispatch and PTC platform, and one corporate network, the company prepared one Cybersecurity Implementation Plan (CIP) naming the 9 railroads and their shared Critical Cyber Systems; **TSA approved it on 2023-08-15**. CR-10 still operates under the CIP its prior owner had approved, and the request to amend for the change in ownership was filed late (gap 1). The other 54 railroads are not covered, but enterprise policy applies the same controls to every railroad on the shared platform |
| FRA status | All 64 are subject to FRA accident/incident reporting (49 CFR part 225, 225.3) and the track safety standards as track owners (part 213). **PTC host duty on 3 railroads:** 49 CFR 236.1005(b)(1) requires "each railroad providing or hosting intercity or commuter passenger service" to install and operate PTC on main lines used for regularly provided passenger service, so CR-07, CR-08, and CR-09 operate an FRA-certified PTC system on **212 route miles** (186 wayside interface units). **PTC tenant duty on 22 railroads:** their trains run more than 20 miles on Class I PTC lines, so the exception for unequipped Class II and III trains in 236.1006(b)(4)(iii)(A) does not apply and each controlling locomotive there must carry an operative onboard PTC apparatus (236.1006(a)) |
| Hazmat security | Transports PIH, so a hazmat transportation security plan is required (49 CFR 172.800(b); components in 172.802). One corporate plan with a security annex per railroad, owned by the Assistant Vice President, Rail Security |
| SEC and financial reporting | Form 8-K Item 1.05 (material cybersecurity incidents, within 4 business days after the materiality determination); Regulation S-K Item 106 (17 CFR 229.106) annual disclosure in the Form 10-K; SOX Section 404 IT general controls over the ERP and revenue systems (tested by the SOX program) |
| State law approach | Operates in 27 states. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida (Fla. Stat. 501.171) as the worked example. Personal information held: about 12,000 current and 31,000 former employees, including engineer and conductor certification and medical records; business contacts of customers. State AI and employment laws are tracked for AI-007 (Colorado SB26-189, effective 2027-01-01; Illinois Public Act 103-0804, effective 2026-01-01). TSA and FRA rules preempt state law on the same subject under 49 U.S.C. 20106 (49 CFR 1580.5) |
| Not in scope | Passenger operations (the company hosts passenger trains but runs none and holds no passenger data). Maritime rules (no vessel or facility requiring a security plan under 33 CFR parts 104 to 106; the two port switching railroads work inside port facilities whose owners hold the facility plans). Pipeline and aviation directives. FAR clauses (no federal contracts; recheck if one is signed). Payment cards (customers pay by invoice and ACH). HIPAA (the employee health plan is a separate covered entity outside these deliverables). CIRCIA and the TSA surface cyber NPRM are proposed only and are tracked, not treated as obligations |

**Regulatory driver IDs used in this folder.** The vertical's `requirements.csv` lists C-TRANSPORTATION-R01 to R07. **R01 (TSA rail cyber directives) applies** to the 10 Covered Railroads and is the primary regulation in P03. R06 (TSA surface cyber NPRM) and R07 (CIRCIA) are proposed rules, tracked only. R02 to R05 (pipeline, aviation, maritime) do not apply. The other binding rules are not in the registry, so this sample adds **scenario-level driver IDs**, defined here and nowhere else. S01 to S08 keep the meanings used in the Small sample of this vertical.

| ID | Requirement | Citation | Status for this company |
|---|---|---|---|
| C-TRANSPORTATION-R01 | TSA rail cybersecurity directives | SD 1580-21-01E; SD 1580/82-2022-01E | Applies to CR-01 to CR-10 |
| C-TRANSPORTATION-S01 | TSA Security Coordinator and reporting of significant security concerns | 49 CFR 1570.201; 1570.203 and Appendix A to part 1570; 1570.105 | Applies to all 64 railroads |
| C-TRANSPORTATION-S02 | TSA RSSM operations | 49 CFR part 1580 subpart C (1580.201, 1580.203, 1580.205) | Applies to the 31 railroads that carry RSSM |
| C-TRANSPORTATION-S03 | Protection of SSI | 49 CFR part 1520 (1520.7(n), 1520.9) | Applies |
| C-TRANSPORTATION-S04 | FRA positive train control | 49 CFR part 236 subpart I (236.1005, 236.1006, 236.1009, 236.1021, 236.1023, 236.1029, 236.1033, 236.1037) | Host duties on CR-07 to CR-09; tenant duties on 22 railroads |
| C-TRANSPORTATION-S05 | FRA accident/incident reporting | 49 CFR part 225 (225.9, 225.11) | Applies |
| C-TRANSPORTATION-S06 | Hazmat transportation security plan, security training, and rail car security inspection | 49 CFR 172.800, 172.802; 172.704(a)(4)-(5); 174.9 | Applies |
| C-TRANSPORTATION-S07 | State breach notification (Florida worked example) | Each state where affected individuals reside; Fla. Stat. 501.171 | Applies |
| C-TRANSPORTATION-S08 | FRA track and freight car inspection duties | 49 CFR 213.7, 213.233; 215.13 | Applies; relevant to the AI portfolio in P10 |
| C-TRANSPORTATION-S09 | TSA security training program | 49 CFR 1580.113, 1580.115; 1570.109, 1570.111 | Applies to CR-01 to CR-10 |
| C-TRANSPORTATION-S10 | SEC cybersecurity disclosure | Form 8-K Item 1.05; 17 CFR 229.106 | Applies (SEC registrant) |
| C-TRANSPORTATION-S11 | State automated decision and AI-in-employment laws | Colorado SB26-189; Illinois Public Act 103-0804 | Applies to AI-007 in the states where it is used |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors: audit committee; safety, security, and risk committee | Cyber risk oversight (Item 106 governance); the audit committee oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk jointly; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer | Business owner of rail operations; authorizing official for the SSP system (P02) |
| Chief Information Security Officer (CISO) | Program owner; **primary TSA Cybersecurity Coordinator** (SD 1580-21-01E Sec. II.B; U.S. citizen) |
| Chief Information Officer (CIO) | IT and technology operations; common control provider for the enterprise platform |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Safety Officer | FRA compliance, part 225 reporting oversight; chairs the AI governance committee |
| General Counsel | Chairs the disclosure committee; legal holds; outside counsel |
| Chief Audit Executive | Heads Internal Audit (third line), reports functionally to the audit committee; leads the P07 assessment |
| Assistant Vice President, Rail Security | **Primary TSA Security Coordinator** for all 64 railroads (1570.201, appointed at the corporate level); owns the hazmat security plan and the TSA security training program |
| Director, Network Operations Center | **Alternate TSA Security Coordinator** (reachable 24/7 through the NOC); runs dispatch, crew calling, and the 24/7 TSA location request line |
| Director of Security Operations | Runs the 24x7 security operations center (SOC); **alternate Cybersecurity Coordinator** |
| Director of OT Security | Owns operational technology (OT) security for dispatch, PTC, CTC, and wayside; **alternate Cybersecurity Coordinator** |
| GRC team (11), SOC (in-house, with a managed security service provider (MSSP) for overnight tier 1 triage), Internal Audit (in-house, co-sourced OT specialists) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

**Overlap and independence.** At this size roles are separated. The CISO organization designs and runs controls; the GRC team (second line, reporting to the Chief Risk Officer) runs the risk method and the gap analysis; Internal Audit (third line) assesses controls and does not design or operate them. The one deliberate overlap is that the CISO is both the program owner and the primary Cybersecurity Coordinator; the TSA-facing reports are reviewed by the General Counsel before submission.

## 3. Systems

| ID | System | Hosting | Operations-critical? | Notes |
|---|---|---|---|---|
| SYS-01 | Centralized computer-aided dispatch system (CAD): track warrants and track and time authority with conflict checking, CTC dispatcher displays, train sheets, bulletins and speed restrictions | On premises: primary cluster in DC-1, hot standby in DC-2; 148 dispatch consoles at the primary and backup NOCs | Yes | Dispatches 61 of the 64 railroads (all except AQ-04 to AQ-06) |
| SYS-02 | PTC back office system: office segment of the PTC system for the 3 host railroads (CR-07 to CR-09), back office for the 236 company locomotives with onboard PTC apparatus, interoperable messaging with Class I and passenger operators' back offices, PTC key management | On premises: DC-1 primary, DC-2 standby | Yes | Also hosts SL-1 tenants (27 unaffiliated short lines) in logically separate tenants |
| SYS-03 | CTC and wayside OT: CTC code servers and field code units, wayside interface units on PTC territory, crossing remote monitoring, wayside detectors, machine vision portals, radio and microwave network | On premises, wayside, and towers | Yes | OT asset inventory 88% complete (gap 3) |
| SYS-04 | Transportation management system (TMS): car management, waybills, interchange EDI with Class I railroads, RSSM car location data, demurrage and billing inputs | Cloud provider A (PaaS) | Yes | Supplies train consists for PTC initialization and the RSSM data for 30-minute TSA requests; also the core of SL-2 |
| SYS-05 | Crew management, calling, and hours-of-service recordkeeping | Cloud provider A (IaaS and PaaS); calling telephony from a hosted provider | Yes | Employee personal information |
| SYS-06 | Identity platform: single sign-on, MFA, privileged access management (PAM), identity governance; separate OT directory | SaaS identity provider plus on-premises directories | Yes | A legacy two-way trust between the corporate and OT directories has never been reviewed (gap 4) |
| SYS-07 | Multi-cloud estate (Cloud provider A and Cloud provider B, vendor-agnostic) plus DC-1 and DC-2 | Cloud and data centers | Yes | Cloud A: TMS, crew system, customer portal, SL-2. Cloud B: data platform, AI services, SIEM data lake |
| SYS-08 | Enterprise and operations networks: SD-WAN to about 290 sites, NOC operations zone, industrial demilitarized zone (DMZ) between IT and OT, field networks | On premises and carrier services | Yes | AQ-04 to AQ-06 on flat networks with site VPNs (gap 1) |
| SYS-09 | Endpoints and onboard systems: about 8,600 office endpoints, 4,200 rugged crew tablets, 1,100 operations workstations; locomotive telematics and onboard PTC apparatus | On premises and mobile | Operations workstations and onboard: yes | EDR on 97% of endpoints (not at AQ-04 to AQ-06) |
| SYS-10 | ERP, revenue accounting, payroll, and HR | SaaS | No (SOX-relevant) | SOX IT general controls tested annually |
| SYS-11 | Third parties: about 1,100 vendors, 140 of them tier-1 | Various | Some | Tiered third-party risk program |
| SYS-12 | AI portfolio (13 use cases) | Mostly Cloud B and vendor services | AI-001 and AI-002 support safety inspections | Governed by an AI governance committee formed in 2025 |
| SYS-13 | Physical security: badge access and CCTV at the NOCs, data centers, yards, and shops | On premises | No | Railroad police and rail security department |

**SSP system (P02):** the *Train Dispatching and PTC Back Office Platform (TDPB)*: SYS-01 (CAD), SYS-02 (PTC back office), the CTC office code servers from SYS-03, the NOC operations network zone and industrial DMZ components from SYS-08, and the 148 dispatch consoles at the primary and backup NOCs, inheriting enterprise common controls, with interfaces to SYS-04 (TMS), SYS-05 (crew system), Class I and passenger operators' dispatch and PTC systems, and the SL-1 tenants.

## 4. Current security posture: defined program with targeted gaps

**In place today:**
- A security program aligned to NIST CSF 2.0 and NIST SP 800-82 Rev. 3, with a policy hierarchy of policies, standards, procedures, and exceptions
- TSA-approved Cybersecurity Implementation Plan since 2023-08-15 for CR-01 to CR-09; Cybersecurity Assessment Plan updated and approved every year (latest approval 2025-12-05); cybersecurity architecture design reviews by an independent firm in 2024-06 and 2026-05
- Annual risk analysis tied to ERM (NIST IR 8286)
- 24x7 SOC with SIEM and endpoint detection and response (EDR) on 97% of endpoints
- PAM for administrators and vendor remote access to the CAD and PTC systems; MFA for all remote and privileged access
- IT/OT segmentation through an industrial DMZ for the 61 integrated railroads
- Immutable backups in separate accounts; annual disaster recovery (DR) tests for tier-1 systems
- Tiered third-party risk program; SOC 2 Type 2 report for SL-1 every year since 2024
- SEC Item 106 disclosure in the Form 10-K; disclosure committee in place
- AI governance committee formed in 2025

**Targeted gaps:**
1. **Acquisition integration.** 3 of 6 acquired railroads (AQ-04 to AQ-06) still run their own legacy dispatch systems on flat networks, with local identity directories and no EDR. AQ-05 (now CR-10) carries RSSM in an HTUA; the request to amend its CIP for the change in ownership was filed 118 days after closing, against the 50-day limit in SD 1580/82-2022-01E Sec. VI.D.
2. **PTC back office patching and recovery.** PTC back office servers are 7 months behind on operating system patches because the PTC vendor certifies patches slowly, and no compensating measures are documented (SD 1580/82-2022-01E Sec. III.E.3). In the 2026-04-25 DR test, the PTC back office took 9.5 hours to fail over to DC-2 against a 4-hour recovery time objective (RTO).
3. **OT asset inventory.** 88% complete for wayside and field equipment; crossing monitors installed by a vendor at 2 regions are missing.
4. **Access in OT.** A two-way trust between the corporate and OT directories has never been reviewed (Sec. III.C.5). The CTC code servers use 3 shared administrator accounts. A crossing monitor vendor reaches its devices through its own cellular modems, outside PAM.
5. **OT logging.** The SIEM collects 61% of OT log sources; CTC code servers and the PTC back office keep local logs for 30 days only.
6. **Manual operations.** The manual dispatch fallback for CTC territory has been exercised at 2 of the 11 signaled railroads. The TSA 30-minute RSSM location procedure has no tested fallback if the TMS is down.
7. **Disclosure.** The materiality playbook has not been exercised with the disclosure committee since 3 new members joined in 2026-03, and the TSA/CISA reporting steps and the SEC steps sit in separate playbooks.
8. **Third parties.** SOC report reviews are overdue for 14 of 140 tier-1 vendors; the hosted crew calling telephony provider is a single point of failure with an untested fallback.
9. **AI.** 13 AI use cases; 8 have completed committee review. The two safety inspection models (AI-001, AI-002) were validated on vendor data from Class I main lines, not on short line track and equipment.
10. **Service lines.** SL-2 has no SOC 2 report yet, and two SL-2 customers have asked for one by 2027.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 system | Train Dispatching and PTC Back Office Platform (TDPB). The registry default fits this size unchanged |
| P03 regulation | The named primary regulation (TSA SD 1580/82-2022-01E) **applies** to CR-01 to CR-10 and is analyzed requirement by requirement, together with SD 1580-21-01E and every other binding rule in section 1 |
| P08 incident | Ransomware on the dispatch and train control back-office systems, with the TSA/CISA reports and the SEC materiality step |
| P09 SOC 2 | Type 2 readiness for two service lines sold to unaffiliated railroads: SL-1 hosted PTC back office (fourth report) and SL-2 dispatch and car management platform (first report) |
| P10 AI | Enterprise AI portfolio (13 use cases) with a full assessment of AI-001, track and equipment defect detection (computer vision). The registry default fits this size unchanged |
| Cloud | Multi-cloud (vendor-agnostic) with common controls; AWS, Azure, and Google Cloud equivalents appear only in the P04 equivalents table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis fieldwork (applicability confirmed 2026-06-05; evidence sampling finished 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment fieldwork by Internal Audit (NOC walkthrough 2026-07-22; DC-2 and backup NOC 2026-07-29; CR-07 wayside and PTC field visit 2026-08-05) |
| 2026-09-04 | Assessment report issued |
| 2026-09-08 | Executive risk committee approves the risk register, treatments, and policies |
| 2026-09-10 | Results to the board safety, security, and risk committee and the audit committee |

## 7. Facts added while building P01 to P10

| Fact | Used in |
|---|---|
| Revenue per calendar day about $13.2 million (rail operations about $11.5 million) | P05, P08 |
| Acquired railroads: AQ-01 to AQ-03 (2025) fully integrated onto SYS-01 and the identity platform. AQ-04 (closed 2025-11-03), AQ-05 (closed 2026-04-01; becomes CR-10), and AQ-06 (closed 2026-06-15) still run legacy dispatch systems, local directories, and flat networks; together about 610 employees and 21 field sites. CAD migration targets: AQ-04 2026-12-15, AQ-05 2027-02-28, AQ-06 2027-05-31 | P01, P03, P05, P07 |
| CR-10 CIP amendment request (change in ownership) filed with TSA on 2026-07-28 | P03, P07 |
| 17 business processes, BP-01 to BP-17 | P05, P01, P08 |
| 2026-04-25 DR test: CAD failed over to DC-2 in 1.6 hours (RTO 2 hours); PTC back office 9.5 hours (RTO 4 hours) | P02, P05, P07 |
| TSA TSOC telephone 1-866-655-7023, as published for IC Surface-2025-01 in the TSA notice at FR Doc. 2026-17894 (2026-09-01); IC Surface-2025-01 recommends notice to TSOC within 12 hours of discovering a significant cybersecurity incident. CISA Central: www.cisa.gov/report or (844) 729-2472 (SD 1580-21-01E Sec. II.C.3) | P08 |
| Disclosure committee: General Counsel (chair), CFO, Controller, CISO, Chief Risk Officer, Chief Safety Officer, and Vice President, Investor Relations, advised by outside securities counsel | P08 |
| SL-1 SOC 2 Type 2 reports since 2024 (Security, Availability, Confidentiality); 2025 report unqualified with one exception (late removal of a vendor engineer's access) | P09 |
| 2026 Q4 to 2027 Q2 treatment budget of about $7.4 million approved by the executive risk committee on 2026-09-08 | P01, P07 |

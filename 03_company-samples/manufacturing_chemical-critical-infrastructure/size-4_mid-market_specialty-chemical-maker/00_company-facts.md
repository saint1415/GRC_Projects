# Scenario facts: Cris Santos Company | Chemical | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or NIST publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23) and the Federal Register API on 2026-10-05. CFATS status relies on the vertical registry check of 2026-09-25 (CISA CFATS page and U.S. Code), plus a Federal Register search on 2026-10-05 that found no reauthorization document.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed; board with an audit committee) |
| Business | Formulates, blends, packages, and delivers specialty chemical products: aqua ammonia and diluted hydrogen peroxide grades, water treatment blends, pulp and paper process chemicals, and food plant sanitation and industrial cleaning products. Also toll blending, private-label packaging, and bulk resale of sulfuric acid and caustic soda from its marine terminal. Primary industry NAICS 325998, All Other Miscellaneous Chemical Product and Preparation Manufacturing |
| Locations | Florida only, 4 sites: the **Port plant** (38 acres at a Florida deepwater port: marine terminal with one barge dock, bulk tank farm, the **Ammonia Unit**, the **Peroxide Unit**, **Blend Hall 1** with 12 DCS-controlled blend reactors, packaging, 6 truck loading bays, a rail spur, the quality control laboratory, and the central control room); the **Inland plant** (20 acres in central Florida: PLC-controlled blending and packaging of cleaning, sanitation, and water treatment blends); the **Distribution center** (north Florida warehouse and the home base of the tank truck fleet); and **Corporate headquarters** (leased offices in the Port plant's metro area) |
| Workforce | 850 employees: Port plant 430 (150 operators on 4 shifts, 70 packaging, 30 terminal and tank farm, 55 maintenance and instrument and electrical (I&E), 25 laboratory, 18 EHS and security, 20 engineering, 40 logistics, 22 plant administration); Inland plant 190; Distribution center and fleet 95 (including 48 drivers); Corporate 135 (including a 22-person IT team and a 4-person information security team). About 6% of employees live in Georgia or Alabama |
| Revenue | About $410 million a year (fictional), about $1.64 million per shipping day over 250 shipping days. The SBA size standard for NAICS 325998 is 650 employees (13 CFR 121.201), so the company is **not** SBA-small |
| Customers | About 2,400 business customers in the Southeast, including 160 water utilities. The **Tank Telemetry and Replenishment Service (TTRS)** monitors 420 customer tanks and creates replenishment orders automatically. Two large water utilities and a pulp and paper group require a SOC 2 Type 2 report on TTRS from 2027 (P09) |
| Regulated inventory | See the threshold math below. Maximum intended inventories are the limits in the process safety information (40 CFR 68.65(c)(1)(iii); 29 CFR 1910.119(d)(2)(i)(C)) and are enforced by tank level alarms and trips |
| EPA RMP status | Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (EPA-RMP). **Port plant: covered, Program 3.** The anhydrous and aqua ammonia storage and dilution process (the Ammonia Unit) holds more than the threshold quantity. Program 1 is not available because the worst-case release endpoint reaches public receptors (40 CFR 68.10(j)(2)). The process is Program 3 because it is subject to OSHA PSM (68.10(l)(2)); NAICS 325998 is not in the 68.10(l)(1) list. The Port plant is a **responding stationary source** (68.90(a)) with a 24-person emergency response team. RMP five-year update submitted 2024-06-20; compliance audit 2025-04-15; Ammonia Unit HAZOP revalidated 2023-05-18 (EV-034, EV-035, EV-038). **Inland plant: not covered** (no regulated substance above its threshold) |
| OSHA PSM status | Determined in the intake obligations register (OSHA-PSM). **Port plant: two covered processes** (29 CFR 1910.119(a)(1)(i)): the Ammonia Unit (anhydrous ammonia) and the Peroxide Unit (70% hydrogen peroxide). Peroxide Unit HAZOP revalidated 2022-10-12 (EV-035). **Inland plant: not covered** |
| MTSA status | Determined in the intake obligations register (C-CHEMICAL-R02, USCG-6.16-1). **Port plant: regulated facility under 33 CFR Part 105.** The barge dock transfers sulfuric acid and caustic soda solution in bulk from tank barges of up to 10,000 barrels. Both are hazardous materials under 33 CFR 154.105 (listed in Table 1 to 46 CFR Part 153, see 46 CFR 153.40(c)), so the terminal is subject to 33 CFR Part 154 (154.100(a)) and therefore to Part 105 (105.105(a)(1)). The Coast Guard-approved Facility Security Plan (FSP) covers the whole Port plant property. The **USCG cybersecurity rule (33 CFR Part 101 Subpart F) applies** (101.605(a)): training was due 2026-01-12 (101.650(d)(4)); the Cybersecurity Assessment and the Cybersecurity Plan are due no later than 2027-07-16 (101.650(e)(1); 101.655) |
| DOT hazmat security plan | **Required**, determined in the intake obligations register (DOT-HMSP) (49 CFR 172.800(b)(10)): the company offers 50% hydrogen peroxide (Division 5.1, Packing Group II, UN2014) in cargo tanks larger than 3,000 liters and carries it in its own fleet. Security plan written 2019, last revised 2021 (EV-040) |
| CFATS status | Determined in the intake obligations register (C-CHEMICAL-R01). The Port plant holds 70% and 50% hydrogen peroxide, a CFATS chemical of interest for theft and diversion at a minimum concentration of 35% with a screening threshold quantity of 400 lb (72 FR 65396, Nov. 20, 2007). The company filed a Top-Screen in 2008, was tiered, and operated under an approved Site Security Plan until the statutory authority expired on **July 28, 2023**. CFATS has **not been reauthorized**, and CISA states it cannot enforce CFATS. RBPS 8 is used as a **voluntary benchmark** (P03). Legacy records: EV-041 |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): CIRCIA: proposed rule only, not in effect (as proposed, the company would be covered because it exceeds the SBA size standard and owns an MTSA facility). SEC cybersecurity disclosure rules: privately held. Federal contracts: none, so FAR 52.204-21, -23, -25 do not apply. EAR: all customers are in the United States and the company holds no controlled technology. HIPAA: the employee health plan is fully insured (EV-057) |
| Regulatory driver IDs | **C-CHEMICAL-R01** (CFATS RBPS 8, voluntary benchmark), **C-CHEMICAL-R02** (USCG MTSA cybersecurity rule, **binding** at the Port plant), **C-CHEMICAL-R03** (CIRCIA, proposed). EPA RMP (40 CFR Part 68), OSHA PSM (29 CFR 1910.119), the DOT hazmat security plan (49 CFR 172.800-172.804 and 172.704), CERCLA and EPCRA release reporting (40 CFR 302.6; 355.40-355.43), and the OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) are cited directly because the vertical registry has no ID for them |
| State law approach | Florida law is the worked example: breach notice for employee personal information (Fla. Stat. 501.171). For employees who live in other states, the law of each state where affected individuals reside applies |
| Why the registry defaults were kept | Primary system: the Port plant DCS and batch management system (the system the BIA ranks highest). Incident: intrusion into process control systems (P08 runbook 1), plus ransomware on corporate IT as the second incident type required at this size. AI use case: the process-optimization model (AI-001), as one of 5 use cases in the portfolio required at this size |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

### Regulated inventory and threshold math (Port plant)

| Chemical | Storage | Maximum intended inventory | EPA RMP (40 CFR 68.130) | OSHA PSM (29 CFR 1910.119 App. A) | Other |
|---|---|---|---|---|---|
| Anhydrous ammonia | One 30,000 water-gallon pressure vessel, filled to 85% at most; received by rail tank car | 25,500 gal x 5.15 lb/gal = **131,325 lb** | "Ammonia (anhydrous)", TQ 10,000 lb: **covered** | "Ammonia, Anhydrous", TQ 10,000 lb: **covered** | CERCLA RQ 100 lb; EPCRA extremely hazardous substance (RQ 100 lb) |
| Aqua ammonia, 29% (product of the Ammonia Unit) | Two 20,000-gal tanks, level limit 18,000 gal each, piped to the dilution skid | 36,000 gal x 7.50 lb/gal = 270,000 lb of solution; x 0.29 = **78,300 lb of ammonia** | "Ammonia (conc 20% or greater)", TQ 20,000 lb: **covered**. Interconnected with the anhydrous storage, so it is part of the same process. The partial-pressure exclusion in 68.115(b)(1) is not available (vapor pressure far above 10 mm Hg) | Listed only above 44%: not listed by itself, but inside the covered process because it is interconnected | The 19% product tanks are below the 20% listing |
| Hydrogen peroxide, 70% (feed to the Peroxide Unit) | Two 8,000-gal tanks, combined level limit 14,000 gal | 14,000 gal x 10.7 lb/gal = 149,800 lb of solution; x 0.70 = **104,860 lb of hydrogen peroxide** | Not listed | "Hydrogen Peroxide (52% by weight or greater)", TQ 7,500 lb: **covered** | EPCRA extremely hazardous substance at concentrations above 52% (RQ 1,000 lb); CFATS chemical of interest (legacy) |
| Hydrogen peroxide, 50% (product) | Two 10,000-gal tanks | About 190,000 lb of solution | Not listed | Below 52%, but interconnected with the 70% tanks through the dilution skid, so inside the covered process | Shipped in cargo tanks: DOT security plan trigger (172.800(b)(10)) |
| Sulfuric acid, 93% (barge receipt) | Two 250,000-gal tanks | About 7.6 million lb | Not listed (only oleum is) | Not listed (only oleum is) | CERCLA RQ 1,000 lb; EPCRA extremely hazardous substance |
| Caustic soda solution, 50% (barge receipt) | Two 300,000-gal tanks | About 7.6 million lb | Not listed | Not listed | CERCLA RQ 1,000 lb |
| Sodium hypochlorite, 12.5% | Three 15,000-gal tanks | About 450,000 lb | Not listed | Not listed | CERCLA RQ 100 lb |
| Flammable liquids (flash point below 100 F) | Drums and totes in the flammables warehouse | Capped at **8,000 lb** in one location | Not listed | Below the 10,000 lb flammable liquid threshold in (a)(1)(ii) while the cap holds | Cap enforced through MOC |

**Limits the company must keep** (enforced by management of change, POL-01 4.11): the 85% fill limit on the anhydrous ammonia vessel and the level limits above are the maximum intended inventories in the process safety information; the flammable liquids cap stays at 8,000 lb in one location; and the Inland plant buys only aqua ammonia below 20% and hydrogen peroxide below 35%, which keeps it outside RMP and the legacy CFATS chemical-of-interest list.

## 2. People (role titles only)

| Role | Security, process safety, and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber and process safety risk reporting; receives P01 and P07 results |
| Chief Executive Officer (CEO) | Accepts High risks; approves the risk appetite and the security budget |
| Chief Operating Officer (COO) | Executive sponsor of the security program; accepts Moderate risks; chairs the crisis management team |
| Chief Financial Officer (CFO) | Cyber insurance, ERP business owner, PE sponsor and lender reporting |
| General Counsel | Legal privilege, regulator and law enforcement contact, breach determinations with outside counsel |
| Virtual CISO (vCISO, part-time contractor) | Program strategy, risk appetite, board reporting |
| Information Security Manager | Runs the security program day to day; designated **Cybersecurity Officer (CySO)** for the Port plant in writing on 2025-10-01 (33 CFR 101.620(b)(3); EV-028) |
| OT Security Engineer | OT security architecture and monitoring; designated **alternate CySO** |
| Security Analyst and GRC Analyst | Vulnerability management and MSSP liaison (Security Analyst); risk register, POA&M, policies, and vendor reviews (GRC Analyst) |
| IT Director | Infrastructure, identity provider, cloud landing zone, backups, endpoints; 22-person IT team |
| VP EHS and Process Safety | Corporate owner of RMP, PSM, EPCRA, and DOT hazmat compliance; senior management official for the DOT security plan (172.802(b)(1)) |
| Port Plant Manager | System owner of the Port plant process control system; RMP qualified person with overall responsibility (40 CFR 68.15(b)); process incident commander |
| Process Safety Manager (Port plant) | PHA, MOC, mechanical integrity, incident investigation, compliance audits |
| Facility Security Officer (Port plant) | MTSA FSO under the FSP (33 CFR 105.205); physical security, TWIC access, guard force; former CFATS facility security officer |
| Controls Engineering Manager | Owns the DCS, batch management system, SIS, and OT networks at both plants; leads 3 controls engineers at the Port plant and 1 at the Inland plant |
| Inland Plant Manager | Owner of the Inland plant batch control system |
| Terminal Manager | Marine terminal and tank farm; person in charge of barge transfers |
| Director of Technical Services | Formulations, master recipes, recipe release workflow |
| Quality Director | LIMS, certificates of analysis, batch release |
| Director of Customer Solutions | Business owner of TTRS and its SOC 2 report |
| Director of Data and Analytics | Leads 2 data scientists; owner of AI-001 and AI-004 models |
| Distribution and Fleet Manager | Distribution center, 30 cargo tank trucks, hazmat shipping |
| HR Director | Onboarding, transfers, terminations, background checks, TWIC sponsorship |
| Co-sourced internal audit firm | Annual IT audit; performs the P07 assessment with an OT specialist subcontractor; independent of control operation |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring for IT; OT is not in its contract today (EV-022) |
| DCS integrator and SIS vendor (contracted) | Remote support through the OT remote access gateway; on-site turnaround work |
| Inland plant controls integrator (contracted) | PLC and SCADA support for the Inland plant |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Distributed control system (DCS), Port plant | On premises, central control room | Setpoints, alarm limits, process data | 4 redundant controller pairs (tank farm and terminal, Ammonia Unit, Peroxide Unit, Blend Hall 1), redundant server pair, 8 operator stations, 2 engineering workstations (EWS). One major release behind the vendor's current release (EV-016) |
| SYS-02 | Batch management system, Port plant | On premises (DCS server pair) | About 600 master recipes (trade secrets) | Receives production orders from the ERP through the order relay in the OT DMZ |
| SYS-03 | Safety instrumented systems (SIS), Port plant | On premises, separate SIS network | Safety logic | Two safety controllers (Ammonia Unit; Peroxide Unit and tank farm high-level trips) with a dedicated SIS engineering workstation. Proof-tested yearly (last 2025-11-04; EV-036) |
| SYS-04 | Terminal and loading automation, Port plant | On premises | Transfer and load records | Dock transfer PLC with emergency shutdown, radar tank gauging system and its server, and 6 truck loading bays with driver card readers |
| SYS-05 | Process historian, Port plant | On premises, OT DMZ | 5 years of process data | Built in 2023 with a replica in the OT DMZ. The replica feeds the cloud data platform (one-way) |
| SYS-06 | OT networks and IT/OT firewalls, Port plant | On premises | n/a | Control, supervisory, SIS, and OT DMZ zones behind a firewall pair (2023 redesign; EV-013, EV-014) |
| SYS-07 | OT remote access gateway, Port plant | On premises, OT DMZ | Session recordings | Named accounts, MFA, per-session approval, recording (2024). Used by the DCS integrator, the SIS vendor, and the tank gauging vendor (EV-009) |
| SYS-08 | Inland plant batch control system | On premises | Inland recipes | 14 PLCs and a SCADA server with 4 HMIs. Separated from the office network only by a VLAN access list. The Inland integrator uses an always-on remote desktop tool (EV-015) |
| SYS-09 | Enterprise resource planning (ERP) | Vendor SaaS | Orders, inventory (including hydrogen peroxide), bills of materials, hazmat shipping papers, customer data | Vendor SOC 2 Type 2 report on file (EV-046) |
| SYS-10 | Laboratory information management system (LIMS) | Cloud workloads account (SYS-11) | QC results, certificates of analysis | Serves both plants |
| SYS-11 | Cloud landing zone: 5 accounts (security, shared services, business workloads, TTRS, backup) | Public cloud provider (vendor-agnostic) | Formulations, historian copy, TTRS data | Hosts LIMS, the order interface, file services, the data platform, AI-001 and AI-004 model services, and TTRS |
| SYS-12 | Tank Telemetry and Replenishment Service (TTRS) | TTRS account (SYS-11) plus 420 cellular gateways on customer tanks | Customer tank levels, delivery addresses, customer contacts | Customer portal, telemetry ingestion, replenishment engine that creates orders in the ERP, and AI-004 forecasting |
| SYS-13 | Identity provider (SSO and MFA) and the on-premises directory | SaaS and on premises | Identities | MFA for all IT users; privileged access vault for directory and cloud administrators. OT systems use separate local accounts (EV-001, EV-003) |
| SYS-14 | Productivity suite (email, files, chat) | SaaS | Internal documents | Includes the enterprise generative AI assistant (AI-002) |
| SYS-15 | Endpoints | On premises and remote | Incidental | 640 office laptops and desktops with EDR; 74 OT workstations (52 Port, 22 Inland). Port DCS stations have application allowlisting; Inland HMIs have none. 9 OT workstations run an end-of-support operating system (EV-010, EV-011) |
| SYS-16 | SIEM and MSSP monitoring | SaaS | Security logs | IT, cloud, identity, and IT/OT firewall logs. A passive OT monitoring sensor at the Port plant (2025) alerts the OT Security Engineer by email during business hours only (EV-012, EV-022) |
| SYS-17 | Physical security systems | On premises | Video, badge and TWIC reader records | Badge and TWIC readers, 160 cameras, video management server on the business network (EV-050) |
| SYS-18 | HR and payroll | Vendor SaaS | Employee PII | Background check results and payroll data for 850 employees and former employees |
| SYS-19 | Fleet and transportation management | Vendor SaaS | Routes, telematics | 30 cargo tank trucks with telematics; dispatch for the Distribution center |
| SYS-20 | AI tools | Mixed | See P10 | AI-001 process optimization, AI-002 generative AI assistant, AI-003 predictive maintenance, AI-004 TTRS demand forecasting and replenishment, AI-005 SDS drafting assistant (EV-056) |

**SSP system (P02):** the *Process Control and Batch Management System (PCBMS)*: the Port plant DCS (SYS-01), batch management system (SYS-02), SIS (SYS-03), terminal and loading automation (SYS-04), historian (SYS-05), OT networks and IT/OT firewalls (SYS-06), the OT remote access gateway (SYS-07), and the 52 Port plant OT workstations in SYS-15, with common controls inherited from the identity provider (SYS-13), the SIEM and MSSP (SYS-16), and the cloud shared services account (SYS-11).

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the USCG cybersecurity rule, the RMP and PSM elements that depend on the control system, the DOT security plan, and the RBPS 8 benchmark** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 SSP | Process Control and Batch Management System (PCBMS) at the Port plant, categorized High (integrity and availability) under FIPS 199. The tier default is a Moderate system; the PCBMS is High because a manipulated setpoint or SIS can cause a toxic release that reaches the public |
| P03 regulations | All rules for the primary business line: USCG cybersecurity rule (33 CFR Part 101 Subpart F, binding); EPA RMP Program 3 and OSHA PSM elements that depend on the control system (binding); DOT hazmat security plan (binding); CFATS RBPS 8 (voluntary benchmark, the registry's primary regulation) |
| P04 cloud | 5-account landing zone plus SaaS. Vendor-agnostic; AWS, Azure, and Google Cloud names only in an equivalents table |
| P05 BIA | 18 business processes across the Port plant, Inland plant, Distribution center, TTRS, and corporate functions, with dollar impact |
| P07 assessment | 32 controls on the PCBMS, plus sampled corporate controls the PCBMS inherits; OT testing on 2026-08-19 during a planned Blend Hall 1 outage |
| P08 incidents | Two runbooks: (1) intrusion into the Port plant process control systems; (2) ransomware with data theft on corporate IT and the cloud that disrupts shipping and TTRS. Both integrated with crisis management, legal, and MTSA reporting |
| P09 SOC 2 | The company is a service organization for TTRS. Readiness for a SOC 2 Type 2 examination (Security, Availability, Confidentiality, Processing Integrity), plus a vendor SOC 2 review program |
| P10 AI | Portfolio of 5 use cases: AI-001 process-optimization model, AI-002 enterprise generative AI assistant, AI-003 predictive maintenance, AI-004 TTRS demand forecasting and automatic replenishment, AI-005 SDS drafting assistant |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-15 to 2026-07-02 | Intake: evidence requests, exports, document reviews (FSP sections on site), inventories, obligations register |
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (Port plant walkthrough 2026-07-14, Inland plant 2026-07-16, Distribution center 2026-07-21) |
| 2026-08-03 to 2026-08-07 | Policies (POL-01 to POL-05) and the P08 runbooks drafted from the gap analysis |
| 2026-08-10 to 2026-08-28 | Control assessment by the co-sourced internal audit firm (OT testing 2026-08-19 during a planned Blend Hall 1 outage): operating tests of controls already in place; design review of the draft policies and runbooks |
| 2026-09-04 | SOC 2 readiness assessment completed |
| 2026-09-11 | AI risk assessment completed |
| 2026-09-22 | Results to the audit committee; deliverables approved by the COO (Moderate and below) and the CEO (High) |
| 2026-10-01 | 2026 policies take effect |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies and standards introduced, after at least one quarter of operation |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Additional role titles | VP Sales and Customer Service (order management, BP-15); Maintenance Manager (Port plant); Procurement Manager; Shift Supervisors (4 crews at the Port plant); Logistics Manager (Port plant); Director of Corporate Communications; Controller; 3 regulatory specialists (SDS authoring) in technical services; a 5-person TTRS engineering team under the Director of Customer Solutions; 4 cloud engineers in the IT team |
| Terminology | "Process Control and Batch Management System (PCBMS)" is the SSP system in P02, identifier CSC-PCBMS-01 |
| Port OT workstations (52) | 8 operator stations, 2 DCS EWS, 1 SIS EWS, 12 Blend Hall 1 local HMIs, 5 packaging line HMIs, 3 terminal HMIs, 6 loading bay terminals, 9 historian clients, 2 recipe workstations, 2 operator training stations, 2 I&E maintenance laptops (EV-011) |
| End-of-support workstations (9) | 5 at the Port plant (4 packaging line HMIs and the dock HMI) and the 4 Inland SCADA HMIs (EV-011) |
| OT inventory and access data | The OT sensor found 412 Port OT assets; 340 reconciled into the register by 2026-08-01. 214 IT/OT firewall rules. 186 DCS user accounts. 41 gateway and OT administrator accounts. 312 gateway sessions from 2026-05 to 2026-07. 40 contractors with OT access (EV-012, EV-069, EV-014, EV-006, EV-009, EV-031; the session count is the P07 population in EV-AC-17) |
| Workforce activity | 96 terminations and 41 internal transfers in the 12 months to 2026-06-30. USCG training: 371 of 430 Port employees by 2026-01-12; 412 of 430 by 2026-08-31 (EV-004, EV-030, EV-070) |
| Actions after P07 | Tank gauging server password changed 2026-08-20 (EV-IA-5) (web interface restriction due 2026-10-15); integrator gateway accounts narrowed to their zones 2026-09-15; gateway session approvals recorded in the gateway from 2026-10-01 |
| Backups | Nightly online exports of DCS, batch, and SIS configurations to the OT backup server in the OT DMZ; weekly offline copies in the Port plant fire safe; a monthly second copy to the Inland plant safe (about 90 miles away). LIMS was restore-tested in the cloud in 2026-04 (6 hours) (EV-021, EV-020) |
| Process safety program dates | RMP and PSM compliance audit 2025-04-15 (2 of 14 findings open); annual coordination with county fire rescue and the LEPC (2026-03); last notification exercise 2025-11-06; joint cyber and process tabletop set for 2026-11-17 (also the RMP tabletop due before 2026-12-21); Peroxide Unit HAZOP revalidation due 2027-10 (EV-038, EV-039, EV-035) |
| Community notification | Shelter-in-place and evacuation messages are launched from a SaaS community notification service (web console); a phone launch path is being added (EV-039) |
| Vendors | 11 key cloud and SaaS vendors: cloud provider, ERP, identity provider, MSSP, productivity suite, HR and payroll, fleet management, TTRS gateway maker's device service, cellular carrier, community notification service, AI-005 vendor. SOC 2 reports reviewed for the first 3. OT service providers: DCS integrator, SIS vendor, tank gauging vendor, Inland integrator (EV-044, EV-046, EV-058) |
| Contract terms | TTRS master services agreement: 99.5% monthly availability, replenishment orders within 4 hours, security incident notice within 72 hours (missing from 40 older agreements). HR and payroll vendor: breach notice within 72 hours. MSSP: call within 30 minutes on high severity (EV-045) |
| FY2027 security plan | $1.5 million one-time and $610,000 a year, approved by the CEO 2026-09-22. The DCS upgrade and replacement of the 9 end-of-support workstations are in the 2027 turnaround capital plan ($1.4 million, turnaround 2027-10) |
| SOC 2 timeline | Type 1 report as of 2027-03-31; Type 2 observation period 2027-04-01 to 2027-09-30; report expected by 2027-11-30; examined by a CPA firm independent of the co-sourced internal audit firm |
| AI dates | AI-004 in production since 2025-06; AI-003 since 2025-10; AI-002 since 2026-01; AI-001 since 2026-03 (4 reactors and the dilution skid); AI-005 pilot since 2026-05 (EV-056) |
| Employees by state | About 800 of 850 employees live in Florida; the rest live in Georgia or Alabama (EV-004) |

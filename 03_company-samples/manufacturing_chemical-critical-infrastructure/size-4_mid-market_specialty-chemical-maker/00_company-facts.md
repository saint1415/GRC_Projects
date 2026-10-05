# Scenario facts: Cris Santos Company | Chemical | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or NIST publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23) and the Federal Register API on 2026-10-05. CFATS status relies on the vertical registry check of 2026-09-25 (CISA CFATS page and U.S. Code), plus a Federal Register search on 2026-10-05 that found no reauthorization document.

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
| EPA RMP status | **Port plant: covered, Program 3.** The anhydrous and aqua ammonia storage and dilution process (the Ammonia Unit) holds more than the threshold quantity. Program 1 is not available because the worst-case release endpoint reaches public receptors (40 CFR 68.10(j)(2)). The process is Program 3 because it is subject to OSHA PSM (68.10(l)(2)); NAICS 325998 is not in the 68.10(l)(1) list. The Port plant is a **responding stationary source** (68.90(a)) with a 24-person emergency response team. RMP five-year update submitted 2024-06-20; compliance audit 2025-04-15; Ammonia Unit HAZOP revalidated 2023-05-18. **Inland plant: not covered** (no regulated substance above its threshold) |
| OSHA PSM status | **Port plant: two covered processes** (29 CFR 1910.119(a)(1)(i)): the Ammonia Unit (anhydrous ammonia) and the Peroxide Unit (70% hydrogen peroxide). Peroxide Unit HAZOP revalidated 2022-10-12. **Inland plant: not covered** |
| MTSA status | **Port plant: regulated facility under 33 CFR Part 105.** The barge dock transfers sulfuric acid and caustic soda solution in bulk from tank barges of up to 10,000 barrels. Both are hazardous materials under 33 CFR 154.105 (listed in Table 1 to 46 CFR Part 153, see 46 CFR 153.40(c)), so the terminal is subject to 33 CFR Part 154 (154.100(a)) and therefore to Part 105 (105.105(a)(1)). The Coast Guard-approved Facility Security Plan (FSP) covers the whole Port plant property. The **USCG cybersecurity rule (33 CFR Part 101 Subpart F) applies** (101.605(a)): training was due 2026-01-12 (101.650(d)(4)); the Cybersecurity Assessment and the Cybersecurity Plan are due no later than 2027-07-16 (101.650(e)(1); 101.655) |
| DOT hazmat security plan | **Required** (49 CFR 172.800(b)(10)): the company offers 50% hydrogen peroxide (Division 5.1, Packing Group II, UN2014) in cargo tanks larger than 3,000 liters and carries it in its own fleet. Security plan written 2019, last revised 2021 |
| CFATS status | The Port plant holds 70% and 50% hydrogen peroxide, a CFATS chemical of interest for theft and diversion at a minimum concentration of 35% with a screening threshold quantity of 400 lb (72 FR 65396, Nov. 20, 2007). The company filed a Top-Screen in 2008, was tiered, and operated under an approved Site Security Plan until the statutory authority expired on **July 28, 2023**. CFATS has **not been reauthorized**, and CISA states it cannot enforce CFATS. RBPS 8 is used as a **voluntary benchmark** (P03) |
| Not in scope | CIRCIA: proposed rule only, not in effect (as proposed, the company would be covered because it exceeds the SBA size standard and owns an MTSA facility). SEC cybersecurity disclosure rules: privately held. Federal contracts: none, so FAR 52.204-21, -23, -25 do not apply. EAR: all customers are in the United States and the company holds no controlled technology. HIPAA: the employee health plan is fully insured |
| Regulatory driver IDs | **C-CHEMICAL-R01** (CFATS RBPS 8, voluntary benchmark), **C-CHEMICAL-R02** (USCG MTSA cybersecurity rule, **binding** at the Port plant), **C-CHEMICAL-R03** (CIRCIA, proposed). EPA RMP (40 CFR Part 68), OSHA PSM (29 CFR 1910.119), the DOT hazmat security plan (49 CFR 172.800-172.804 and 172.704), CERCLA and EPCRA release reporting (40 CFR 302.6; 355.40-355.43), and the OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) are cited directly because the vertical registry has no ID for them |
| State law approach | Florida law is the worked example: breach notice for employee personal information (Fla. Stat. 501.171). For employees who live in other states, the law of each state where affected individuals reside applies |
| Why the registry defaults were kept | Primary system: the Port plant DCS and batch management system (the system the BIA ranks highest). Incident: intrusion into process control systems (P08 runbook 1), plus ransomware on corporate IT as the second incident type required at this size. AI use case: the process-optimization model (AI-001), as one of 5 use cases in the portfolio required at this size |

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
| Information Security Manager | Runs the security program day to day; designated **Cybersecurity Officer (CySO)** for the Port plant in writing on 2025-10-01 (33 CFR 101.620(b)(3)) |
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
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring for IT; OT is not in its contract today |
| DCS integrator and SIS vendor (contracted) | Remote support through the OT remote access gateway; on-site turnaround work |
| Inland plant controls integrator (contracted) | PLC and SCADA support for the Inland plant |

## 3. Systems

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Distributed control system (DCS), Port plant | On premises, central control room | Setpoints, alarm limits, process data | 4 redundant controller pairs (tank farm and terminal, Ammonia Unit, Peroxide Unit, Blend Hall 1), redundant server pair, 8 operator stations, 2 engineering workstations (EWS). One major release behind the vendor's current release |
| SYS-02 | Batch management system, Port plant | On premises (DCS server pair) | About 600 master recipes (trade secrets) | Receives production orders from the ERP through the order relay in the OT DMZ |
| SYS-03 | Safety instrumented systems (SIS), Port plant | On premises, separate SIS network | Safety logic | Two safety controllers (Ammonia Unit; Peroxide Unit and tank farm high-level trips) with a dedicated SIS engineering workstation. Proof-tested yearly (last 2025-11-04) |
| SYS-04 | Terminal and loading automation, Port plant | On premises | Transfer and load records | Dock transfer PLC with emergency shutdown, radar tank gauging system and its server, and 6 truck loading bays with driver card readers |
| SYS-05 | Process historian, Port plant | On premises, OT DMZ | 5 years of process data | Built in 2023 with a replica in the OT DMZ. The replica feeds the cloud data platform (one-way) |
| SYS-06 | OT networks and IT/OT firewalls, Port plant | On premises | n/a | Control, supervisory, SIS, and OT DMZ zones behind a firewall pair (2023 redesign) |
| SYS-07 | OT remote access gateway, Port plant | On premises, OT DMZ | Session recordings | Named accounts, MFA, per-session approval, recording (2024). Used by the DCS integrator, the SIS vendor, and the tank gauging vendor |
| SYS-08 | Inland plant batch control system | On premises | Inland recipes | 14 PLCs and a SCADA server with 4 HMIs. Separated from the office network only by a VLAN access list. The Inland integrator uses an always-on remote desktop tool |
| SYS-09 | Enterprise resource planning (ERP) | Vendor SaaS | Orders, inventory (including hydrogen peroxide), bills of materials, hazmat shipping papers, customer data | Vendor SOC 2 Type 2 report on file |
| SYS-10 | Laboratory information management system (LIMS) | Cloud workloads account (SYS-11) | QC results, certificates of analysis | Serves both plants |
| SYS-11 | Cloud landing zone: 5 accounts (security, shared services, business workloads, TTRS, backup) | Public cloud provider (vendor-agnostic) | Formulations, historian copy, TTRS data | Hosts LIMS, the order interface, file services, the data platform, AI-001 and AI-004 model services, and TTRS |
| SYS-12 | Tank Telemetry and Replenishment Service (TTRS) | TTRS account (SYS-11) plus 420 cellular gateways on customer tanks | Customer tank levels, delivery addresses, customer contacts | Customer portal, telemetry ingestion, replenishment engine that creates orders in the ERP, and AI-004 forecasting |
| SYS-13 | Identity provider (SSO and MFA) and the on-premises directory | SaaS and on premises | Identities | MFA for all IT users; privileged access vault for directory and cloud administrators. OT systems use separate local accounts |
| SYS-14 | Productivity suite (email, files, chat) | SaaS | Internal documents | Includes the enterprise generative AI assistant (AI-002) |
| SYS-15 | Endpoints | On premises and remote | Incidental | 640 office laptops and desktops with EDR; 74 OT workstations (52 Port, 22 Inland). Port DCS stations have application allowlisting; Inland HMIs have none. 9 OT workstations run an end-of-support operating system |
| SYS-16 | SIEM and MSSP monitoring | SaaS | Security logs | IT, cloud, identity, and IT/OT firewall logs. A passive OT monitoring sensor at the Port plant (2025) alerts the OT Security Engineer by email during business hours only |
| SYS-17 | Physical security systems | On premises | Video, badge and TWIC reader records | Badge and TWIC readers, 160 cameras, video management server on the business network |
| SYS-18 | HR and payroll | Vendor SaaS | Employee PII | Background check results and payroll data for 850 employees and former employees |
| SYS-19 | Fleet and transportation management | Vendor SaaS | Routes, telematics | 30 cargo tank trucks with telematics; dispatch for the Distribution center |
| SYS-20 | AI tools | Mixed | See P10 | AI-001 process optimization, AI-002 generative AI assistant, AI-003 predictive maintenance, AI-004 TTRS demand forecasting and replenishment, AI-005 SDS drafting assistant |

**SSP system (P02):** the *Process Control and Batch Management System (PCBMS)*: the Port plant DCS (SYS-01), batch management system (SYS-02), SIS (SYS-03), terminal and loading automation (SYS-04), historian (SYS-05), OT networks and IT/OT firewalls (SYS-06), the OT remote access gateway (SYS-07), and the 52 Port plant OT workstations in SYS-15, with common controls inherited from the identity provider (SYS-13), the SIEM and MSSP (SYS-16), and the cloud shared services account (SYS-11).

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- A security program led by the vCISO since 2023, with policies adopted in 2024 and quarterly reporting to the audit committee
- An OT DMZ and IT/OT firewall pair at the Port plant (2023), with the historian replica in the DMZ
- The OT remote access gateway at the Port plant with named accounts, MFA, approval, and recording (2024)
- Named DCS engineering accounts at the Port plant (2024)
- MFA for all IT users through the identity provider; a privileged access vault for directory and cloud administrators
- EDR on all office endpoints with 24x7 MSSP monitoring; SIEM
- Application allowlisting on Port plant DCS operator stations and engineering workstations (2024)
- A passive OT monitoring sensor at the Port plant (2025)
- Weekly offline copies of DCS, batch, and SIS configurations kept in the Port plant fire safe (2024)
- MOC covering DCS and SIS logic, setpoint, and alarm changes at the Port plant (2024); a two-approval recipe release workflow
- Mature RMP Program 3 and PSM programs: HAZOPs, operating procedures, mechanical integrity including SIS proof tests, compliance audits, a responding emergency response team, annual notification exercises
- An approved MTSA Facility Security Plan, an FSO, TWIC access control, and annual FSP audits; a CySO designated in writing (2025-10-01)
- A DOT hazmat security plan and hazmat training program
- Immutable cloud backups in a separate backup account
- An annual external penetration test of internet-facing IT (last 2026-03)
- An annual co-sourced internal IT audit
- Background checks at hire; TWIC for unescorted access at the Port plant
- Cyber insurance ($15 million limit, $500,000 retention)

**Missing or weak, found in the 2026 assessments:**
1. USCG cybersecurity rule readiness is behind. The Cybersecurity Plan draft is about 30% complete and the Cybersecurity Assessment has not started (both due 2027-07-16). Only 371 of 430 Port plant employees, and no tracked contractors, completed the required training by 2026-01-12.
2. Operators share one account per console position at both plants. Inland plant PLCs and HMIs use shared and default-style passwords.
3. The Inland plant network is nearly flat: the SCADA server is reachable from the office VLAN, and the Inland integrator has always-on remote desktop access without MFA.
4. OT monitoring is partial. The Port plant sensor is watched only in business hours, IT/OT conduit logs are collected but not reviewed, and the Inland plant has no OT monitoring.
5. OT recovery is unproven. Offline copies exist at the Port plant, but only one operator station has ever been restored, the SIS program is not routinely compared with the approved copy, and Inland PLC programs live only on one engineer's laptop.
6. OT patching happens only at the annual turnaround. OT assets are not tracked against CISA's Known Exploited Vulnerabilities (KEV) catalog, the DCS is one major release behind, and 9 OT workstations run an end-of-support operating system.
7. Third-party risk: about 260 vendors, 52 with system or data access. Reviews happen only at onboarding, OT vendor contracts do not require vulnerability or incident notice, and SOC 2 reports have been reviewed for only 3 of 11 key SaaS vendors.
8. Access governance: access reviews are annual. OT accounts and loading rack driver cards sit outside the identity provider and are removed by hand.
9. The incident response plan (2024) is IT-focused. The OT runbook is a draft, cyber reporting under 33 CFR 6.16-1 is not in the FSP procedures, and there has never been a joint cyber and process emergency exercise.
10. Sensitive security information (the FSP and Facility Security Assessment), legacy CVI, and formulations sit in file shares open to 65 users. There is no data loss prevention.
11. TTRS: 37% of the 420 cellular gateways run outdated firmware with one shared credential per gateway model, the replenishment engine has no formal change management, and the 99.5% availability commitment is not measured.
12. There is no AI governance beyond the acceptable use policy. AI-001 and AI-004 went live without a risk assessment, and staff use public AI tools.
13. The DOT hazmat security plan was last revised in 2021, missed its 2025 annual review, and does not address cyber risks to shipping papers, driver cards, or telematics.
14. Supporting standards are missing for OT security, configuration, logging, and vendors.
15. The radar tank gauging server at the Port plant still had the vendor default administrator password, with its web interface reachable from the supervisory network (found during P07 testing on 2026-08-19).

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
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (Port plant walkthrough 2026-07-14, Inland plant 2026-07-16, Distribution center 2026-07-21) |
| 2026-08-10 to 2026-08-28 | Control assessment by the co-sourced internal audit firm (OT testing 2026-08-19 during a planned Blend Hall 1 outage) |
| 2026-09-04 | SOC 2 readiness assessment completed |
| 2026-09-11 | AI risk assessment completed |
| 2026-09-22 | Results to the audit committee; deliverables approved by the COO (Moderate and below) and the CEO (High) |

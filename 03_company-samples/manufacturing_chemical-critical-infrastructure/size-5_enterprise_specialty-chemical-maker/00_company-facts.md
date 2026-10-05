# Scenario facts: Cris Santos Company | Chemical | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or NIST publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23) and the Federal Register API on 2026-10-05; CFATS status relies on the CISA CFATS page and uscode.house.gov as read on 2026-09-26 for the Small sample, plus a Federal Register search on 2026-10-05 that found no CFATS documents in 2026.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; specialty chemical formulator and packager) |
| Business | Formulates, blends, packages, and ships specialty chemicals: water treatment chemicals for municipal and industrial customers, process and cleaning chemicals, lubricant and fuel additive packages, and coatings additives. Also runs toll manufacturing and contract formulation for other companies, and a tank telemetry and vendor-managed inventory (VMI) service. Primary industry NAICS 325998, All Other Miscellaneous Chemical Product and Preparation Manufacturing |
| Location | Headquartered in Florida. 14 manufacturing plants (PL-01 to PL-14), 9 distribution centers, and 2 R&D centers in Florida, Georgia, Alabama, Louisiana, Texas, Tennessee, Ohio, and North Carolina. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Flagship site | **PL-01 Gulf Coast Complex (Florida)**: a 180-acre waterfront site with an anhydrous ammonia unit, a chlorine and sodium hypochlorite unit (the "Chlor Unit"), three DCS-controlled blend halls, an additives unit that blends lubricant additive packages with base oils, a tank farm of about 140 tanks, packaging lines, a 12-bay truck rack, a rail yard, a QC laboratory, and a **marine terminal with two barge docks** that receives petroleum base oils by tank barge. About 1,150 employees; about 19% of company production volume |
| Workforce | 12,000 employees: about 7,400 in plant operations and maintenance, 1,600 in supply chain, logistics, and distribution (including about 310 company tank truck drivers), 900 in R&D and technical service, 1,100 in sales and customer service, and 1,000 in corporate functions (including about 480 in IT and about 96 in the CISO organization) |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day. The SBA size standard for NAICS 325998 is 650 employees (13 CFR 121.201), so the company is not small |
| Customers | About 38,000 business customers in the United States and 40 other countries, including about 1,900 municipal water utilities. About 2,900 customers use the tank telemetry and VMI service (SL-1) and about 85 use toll manufacturing (SL-2) |
| Ownership and governance | Publicly traded; board with an audit committee and a risk committee. The risk committee oversees cybersecurity and process safety risk. Not a smaller reporting company |
| Growth by acquisition | Three plants acquired in 2025: PL-12 (Ohio, March 2025), PL-13 (Tennessee, July 2025), and PL-14 (North Carolina, November 2025). About 960 workforce members in total |
| Regulated inventory | See the tables below. Maximum intended inventories are the limits written into the RMP and PSM process safety information (40 CFR 68.65(c)(1)(iii); 29 CFR 1910.119(d)(2)(i)(C)) and enforced by tank level alarms and cylinder caps |
| CFATS status | Nine plants filed Top-Screens because they held 50% hydrogen peroxide, a CFATS chemical of interest for theft and diversion (minimum concentration 35%, screening threshold quantity 400 lb; 72 FR 65396, Nov. 20, 2007), and six were tiered, including PL-01. The statutory authority expired on **July 28, 2023** (6 U.S.C. 621-629 shown as omitted at uscode.house.gov), and CFATS has **not been reauthorized**. CISA states it cannot enforce CFATS. The company kept its Site Security Plan measures and uses RBPS 8 as a **voluntary enterprise benchmark** (P03) |
| USCG MTSA status | **Covered at PL-01 only.** The marine terminal can transfer oil (petroleum base oils) in bulk to or from tank barges with a capacity of 250 barrels or more, so 33 CFR Part 154 applies (154.100(a)). A facility subject to Part 154 must have a Facility Security Plan under 33 CFR Part 105 (105.105(a)(1)), and the cybersecurity rule in 33 CFR Part 101 Subpart F applies to every facility required to have a security plan under Part 105 (101.605(a)). Key dates: cybersecurity training by January 12, 2026 and annually (101.650(d)(4)); Cybersecurity Assessment and Cybersecurity Plan submission no later than July 16, 2027 (101.650(e)(1); 101.655). No other plant has a marine transfer |
| EPA RMP status | **Covered at 8 plants.** Program 3 at PL-01, PL-04 (Louisiana), and PL-05 (Texas), because those processes are also covered by OSHA PSM (40 CFR 68.10(l)(2)); NAICS 325998 is not in the 68.10(l)(1) list. Program 2 at PL-02, PL-03, PL-06, PL-07, and PL-09 (29% aqueous ammonia above the 20,000 lb threshold quantity; worst-case release reaches public receptors, so Program 1 is not available, 68.10(j)(2)). PL-01 is a **responding stationary source** with its own hazardous materials team (68.90(a); 68.95). The 2024 amendments add requirements with a May 10, 2027 compliance date (68.10(g)), including safer technology and alternatives analysis for NAICS 325 processes (68.67(c)(9)) |
| OSHA PSM status | **Covered processes at PL-01, PL-04, and PL-05** (29 CFR 1910.119(a)(1)(i)). Math below |
| DOT hazmat security plan | **Required.** The company offers large bulk quantities (more than 3,000 liters in one packaging) of Class 3 Packing Group II solvent blends and of 50% hydrogen peroxide (Division 5.1, Packing Group II) in cargo tanks and rail cars (49 CFR 172.800(b)(6) and (b)(10)). The enterprise security plan covers personnel security, unauthorized access, and en route security (172.802(a)), is reviewed annually (172.802(c)), and requires security awareness and in-depth security training (172.704(a)(4)-(5)). Senior official: Vice President, Global Logistics |
| SEC | Form 8-K Item 1.05 (material cybersecurity incidents, within 4 business days after the materiality determination) and Regulation S-K Item 106 (annual risk management, strategy, and governance disclosure in the 10-K) apply. SOX IT general controls cover the ERP and payroll |
| Not in scope | **CIRCIA:** proposed rule only (89 FR 23644, 2024-04-04); no final rule in the Federal Register as of 2026-10-05. As proposed, the company would be covered (above the SBA size standard, and PL-01 is an MTSA facility). **FAR clauses:** no federal prime contracts or subcontracts; government customers buy through distributors. **EAR:** exports are handled by the export compliance program; EAR-controlled technology is classified Restricted (POL-04) but export licensing is not analyzed here. **HIPAA:** the employee health plan is a separate covered entity handled by the benefits program |
| Regulatory driver IDs | **C-CHEMICAL-R01** (CFATS RBPS 8, voluntary benchmark), **C-CHEMICAL-R02** (USCG MTSA cybersecurity rule, binding at PL-01), **C-CHEMICAL-R03** (CIRCIA, proposed). EPA RMP (40 CFR Part 68), OSHA PSM (29 CFR 1910.119), DOT hazmat security plans (49 CFR 172.800-172.804), CERCLA and EPCRA release reporting (40 CFR 302.6; 355.40-355.43), SEC rules, and the OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) are cited directly because the vertical registry has no ID for them |

### Regulated inventory and threshold math (PL-01 Gulf Coast Complex)

| Chemical | Storage | Maximum intended inventory | EPA RMP (40 CFR 68.130) | OSHA PSM (29 CFR 1910.119 App. A) | CFATS App. A (legacy) |
|---|---|---|---|---|---|
| Anhydrous ammonia | One 18,000-gal (water capacity) pressure vessel, fill limit 85%, feeding the aqueous ammonia dilution system | 18,000 x 0.85 = 15,300 gal x 5.15 lb/gal = **78,795 lb** | "Ammonia (anhydrous)", TQ 10,000 lb: **covered** | "Ammonia, Anhydrous", TQ 10,000 lb: **covered** | Not used for the legacy tiering |
| Chlorine | Ton containers, inventory cap of 8 on site (2,000 lb each) | 8 x 2,000 = **16,000 lb** | "Chlorine", TQ 2,500 lb: **covered** | "Chlorine", TQ 1,500 lb: **covered** | Not used for the legacy tiering |
| Hydrogen peroxide, 50% | Two 4,000-gal tanks (combined level limit 7,000 gal) | 7,000 gal x 10.0 lb/gal = 70,000 lb of solution; 35,000 lb of hydrogen peroxide | Not listed | Listed only at 52% by weight or greater: **not covered** | Theft and diversion chemical of interest at 35% or more, STQ 400 lb: the basis of the legacy Top-Screen |
| Isopropyl alcohol, 99% (flash point below 100 F) | Two 30,000-gal atmospheric tanks | About 393,000 lb | Not listed | Above 10,000 lb, but excepted because it is stored in atmospheric tanks below its normal boiling point without chilling (1910.119(a)(1)(ii)(B)) | Not relevant |
| Petroleum base oils | Tank farm, received by barge | About 9.5 million lb | Not listed | Not listed (flash point above 100 F) | Not relevant; the reason the marine terminal is a Part 154 facility |

**Result for PL-01:** two PSM-covered processes (the ammonia unit and the Chlor Unit), both in RMP Program 3. PL-04 (anhydrous ammonia, about 41,000 lb) and PL-05 (chlorine ton containers, cap of 6, 12,000 lb) were assessed the same way and are also PSM and Program 3. The Program 2 plants hold 29% aqueous ammonia above the 20,000 lb TQ for "Ammonia (conc 20% or greater)", as in the Small sample's math. **Limit the company must keep:** hydrogen peroxide is bought below 52% at every plant (management of change, POL-01 4.13).

## 2. People (role titles only)

| Role | Security, process safety, and compliance duties |
|---|---|
| Board risk committee | Oversees cybersecurity and process safety risk; approves POL-01 and the risk appetite (Item 106 governance) |
| Board audit committee | Oversees Internal Audit, SOX, disclosure controls, and the RMP third-party audit reports when required (40 CFR 68.80(f)(3)) |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk jointly; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer (COO) | Executive owner of manufacturing; authorizing official equivalent for the P02 system |
| Chief Information Security Officer (CISO) | Program owner for IT and OT security; reports to the CEO with a dotted line to the board risk committee |
| Director of OT Security | Leads the OT Security Center of Excellence (12 staff); designs and runs the enterprise OT security services (common control provider); reports to the CISO |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line; reports functionally to the audit committee); leads the P07 assessment |
| GRC team (9, second line) | Risk method, policy governance, gap analysis, common control catalog |
| Security Operations Center (24x7) | In-house SOC for IT with OT monitoring analysts; an MSSP with an OT practice handles overflow |
| Disclosure committee | 8-K materiality decisions; the General Counsel chairs |

## 3. Systems

| ID | System | Notes |
|---|---|---|
| SYS-01 | PL-01 Gulf Coast Complex process control: DCS, batch management system, two safety instrumented systems (SIS), terminal automation and emergency shutdown, process historian, and the PL-01 OT network and OT DMZ | The P02 system. One DCS platform with 22 redundant controller pairs, 6 redundant server pairs, 38 operator stations, and 6 engineering workstations (EWS); about 1,900 master recipes and about 260 batches a day |
| SYS-02 | Process control at the other 13 plants | 3 DCS platforms and about 420 PLCs; SIS at 8 plants. OT DMZs at 10 of 14 plants (not at PL-12 to PL-14 and PL-08) |
| SYS-03 | Enterprise OT security services | Central remote access gateway (session approval, MFA, recording) at 11 of 14 plants; passive OT network monitoring at 9 of 14 plants; OT backup vault (offline and immutable copies); OT patch and media staging |
| SYS-04 | Identity platform (SSO, MFA, privileged access management, identity governance) | Covers IT, cloud, and the OT remote access gateway. Each plant's OT uses a separate OT directory or local accounts |
| SYS-05 | ERP (global SaaS) and plant manufacturing execution systems (MES) | SOX-relevant; order, inventory, and bill-of-materials records, including hydrogen peroxide inventory |
| SYS-06 | Laboratory information management system (LIMS) | Enterprise LIMS on Cloud provider A; certificates of analysis for every batch |
| SYS-07 | Multi-cloud estate plus 2 colocation data centers | Cloud provider A: ERP integration, LIMS, data platform, historian replicas, AI/ML platform. Cloud provider B: the SL-1 telemetry platform. Colocation DC-1 (Florida) and DC-2 (Ohio) |
| SYS-08 | Enterprise network | SD-WAN to 40 sites; IT/OT boundary firewalls at every plant |
| SYS-09 | Endpoints | About 14,500 IT endpoints (EDR on 98%); about 2,300 OT workstations and servers (EDR or application allowlisting on 61%) |
| SYS-10 | Tank telemetry and VMI platform (SL-1) | About 41,000 cellular tank sensors at about 6,800 customer sites; customer portal with about 9,500 user accounts; about 1,400 automatic replenishment orders a week into the ERP |
| SYS-11 | Transportation management system and fleet telematics | Hazmat shipments, about 220 company tank trucks, and contract carriers; supports the DOT security plan's en route measures |
| SYS-12 | Physical security systems | Badge access and video at 14 plants; TWIC readers at the PL-01 marine terminal (legacy CFATS and MTSA measures) |
| SYS-13 | Third parties | About 2,600 vendors; about 180 with OT or remote access, including 6 DCS and PLC integrators |
| SYS-14 | AI portfolio (12 use cases) | Governed by an AI governance committee formed in 2025 (P10) |
| SYS-15 | HR and payroll SaaS | Employee PII for 12,000 employees and former employees |
| SYS-16 | Productivity suite (email, files, chat) | SaaS |

**SSP system (P02):** the *Gulf Coast Complex Process Control and Batch Management System (GC-PCBMS)*: the PL-01 DCS and batch management system, the Ammonia Unit SIS and Chlor Unit SIS, the marine terminal automation and emergency shutdown system, the process historian, the PL-01 control and supervisory networks and OT DMZ, and the OT workstations at PL-01, inheriting common controls from the enterprise OT security services, identity platform, SOC, and cloud landing zone.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A mature IT security program aligned to CSF 2.0, with a CISO, a dedicated GRC team, and a three lines model
- An OT Security Center of Excellence formed in 2024, with enterprise OT standards based on NIST SP 800-82 Rev. 3
- Annual enterprise risk analysis tied to ERM (NIST IR 8286 Rev. 1)
- A policy hierarchy of policies, standards, procedures, and exceptions
- A 24x7 SOC with OT monitoring analysts
- PAM and quarterly access certification for IT
- Immutable IT backups and annual disaster recovery tests for tier-1 IT systems
- OT DMZs at 10 of 14 plants; the central OT remote access gateway at 11 of 14 plants; passive OT monitoring at 9 of 14 plants
- Independent SIS at all PSM and RMP Program 3 processes, proof-tested on schedule
- A corporate process safety management program: an electronic MOC system, PHAs, compliance audits, and a responding hazardous materials team at PL-01
- An approved MTSA Facility Security Plan at PL-01, and an enterprise DOT hazmat security plan
- Tiered third-party risk reviews
- An annual SOC 2 Type 2 report (Security and Availability) for the SL-1 telemetry platform since 2025
- SEC Item 106 disclosure in the 10-K

**Targeted gaps found in the 2026 assessments:**
1. **Acquired plants.** PL-12, PL-13, and PL-14 still run flat IT/OT networks, integrator remote access outside the central gateway, shared DCS and PLC accounts, and no OT monitoring. Their OT logs do not reach the SIEM.
2. **MTSA cybersecurity rule readiness at PL-01.** The Cybersecurity Plan and Cybersecurity Assessment are not done (due 2027-07-16). 94% of PL-01 personnel completed the cybersecurity training by the January 12, 2026 deadline; 212 contractor personnel did not and are escorted instead. The approved hardware and software list (101.650(b)(1)) and the network map (101.650(b)(4)) are incomplete.
3. **OT change control.** Control logic, alarm limit, and recipe changes at PL-01 are not always routed through the MOC system: 7 of 40 sampled DCS changes had no MOC record. Five other plants have the same pattern.
4. **Known exploited vulnerabilities in OT.** At PL-01, 37 KEV findings on OT assets were older than 30 days without documented compensating controls, which the MTSA rule requires "without delay" (101.650(e)(3)(i)).
5. **OT recovery.** Offline OT backups exist, but only 1 of 3 DCS areas at PL-01 has had a restore test, and comparison of the running SIS programs with the approved copies is manual and irregular.
6. **Disclosure readiness for OT incidents.** The materiality playbook covers data breaches only, the disclosure committee has no operations or process safety member, and it has never exercised an OT scenario.
7. **Third parties with OT access.** Two of 6 DCS and PLC integrators have no security clauses; third-party remote connections at the acquired plants are not monitored.
8. **AI.** 12 use cases, but only 8 have completed committee review. The AI-001 process-optimization model gives advisory setpoints at 6 plants, and a closed-loop pilot is proposed for PL-01.
9. **Service line assurance.** SL-2 toll manufacturing has no SOC 2 report; two large customers require one with Confidentiality and Processing Integrity by 2027.
10. **OT logging.** OT logs from 5 plants (PL-08 and PL-11 to PL-14) do not reach the SIEM.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 | Gulf Coast Complex Process Control and Batch Management System (GC-PCBMS), High baseline with OT tailoring and common control inheritance |
| P03 | All applicable regulations across the enterprise: USCG MTSA cybersecurity rule at PL-01 (binding); EPA RMP and OSHA PSM elements that depend on the control systems (binding); DOT hazmat security plans (binding); SEC Item 1.05 and Item 106 (binding); CERCLA and EPCRA release reporting (binding); state breach laws (binding); CFATS RBPS 8 as the voluntary enterprise benchmark (primary benchmark in the vertical registry); CIRCIA (proposed, tracked) |
| P04 | Multi-cloud (vendor-agnostic) with platform, landing zone, workload, and SaaS layers, plus the OT-to-cloud data paths |
| P05 | Enterprise-wide BIA with a dependency map and third parties |
| P07 | Internal Audit assessment of 42 controls on the GC-PCBMS and its inherited common controls, with statistical sampling |
| P08 | Intrusion into the PL-01 process control systems through a compromised integrator account on the remote access gateway, with alarm limit changes on the ammonia unit, then ransomware on the historian and OT workstations, including the **SEC materiality assessment and 8-K Item 1.05** step and the MTSA, release, and process safety reporting |
| P09 | SOC 2 Type 2 readiness across two service lines offered to external customers: SL-1 tank telemetry and VMI, and SL-2 toll manufacturing and contract formulation |
| P10 | Enterprise AI portfolio (12 use cases) with the AI governance committee; full assessment of AI-001 process-optimization model |
| Cloud | Multi-cloud (vendor-agnostic) with common controls |

**Why the registry defaults were kept.** The registry's primary system (process control and batch management), incident (intrusion into process control at a chemical facility), and AI use case (process-optimization model) all fit an enterprise chemical maker. At this size they are scoped to the flagship plant (PL-01) because it is the only plant where all the binding regulations meet: MTSA, PSM, RMP Program 3, and the DOT security plan.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-10 | Enterprise BIA interviews and workshops |
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment by Internal Audit (OT testing at PL-01 on 2026-08-11 to 2026-08-13 during a planned ammonia unit outage) |
| 2026-08-24 | SOC 2 readiness assessment completed |
| 2026-08-26 | AI governance committee portfolio review |
| 2026-09-08 | Executive risk committee approvals |
| 2026-09-10 | Results to the board risk committee and audit committee |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Plants.**
| Plant | State | Notes |
|---|---|---|
| PL-01 Gulf Coast Complex | Florida | Flagship; MTSA facility; PSM and RMP Program 3 (ammonia unit, Chlor Unit); SL-2 toll blending; about 1,150 employees |
| PL-02 | Georgia | Water treatment chemicals; RMP Program 2 |
| PL-03 | Alabama | Process chemicals; RMP Program 2; SL-2 toll blending |
| PL-04 | Louisiana | Anhydrous ammonia; PSM and RMP Program 3 |
| PL-05 | Texas | Chlorine and hypochlorite; PSM and RMP Program 3 |
| PL-06 | Texas | Additive packages; RMP Program 2; SL-2 toll blending |
| PL-07 | Georgia | Water treatment chemicals; RMP Program 2 |
| PL-08 | Florida | Packaging and repackaging only; no OT DMZ (small PLC estate) |
| PL-09 | Louisiana | Process chemicals; RMP Program 2; SL-2 toll blending |
| PL-10 | Alabama | Coatings additives |
| PL-11 | Ohio | Cleaning chemicals |
| PL-12 | Ohio | Acquired 2025-03; coatings additives |
| PL-13 | Tennessee | Acquired 2025-07; process chemicals |
| PL-14 | North Carolina | Acquired 2025-11; water treatment chemicals |

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Senior Vice President, Manufacturing | All 14 plants; plant managers report to this role |
| Vice President, Process Safety and EHS | Corporate PSM and RMP program; release reporting standards; PHA and MOC system owner |
| PL-01 Plant Manager | System owner of the GC-PCBMS; RMP qualified person for PL-01 (40 CFR 68.15(b)); incident commander for process emergencies at PL-01 |
| PL-01 Facility Security Officer (FSO) | MTSA Facility Security Plan (33 CFR Part 105) |
| PL-01 Cybersecurity Officer (CySO) | Designated in writing by name and title under 33 CFR 101.620(b)(3) (the name is kept in the SSI-protected Cybersecurity Plan). The CySO is the PL-01 OT Security Lead, who reports to the Director of OT Security; the Director of OT Security is the alternate |
| PL-01 Controls Engineering Manager | DCS, batch, SIS, and terminal automation engineering; approves control system changes |
| Director of Automation Engineering | Corporate DCS and PLC standards and the integrator contracts |
| Process Safety Manager, PL-01 | PHAs, MOC, incident investigations, and compliance audits at PL-01 |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| General Counsel | Chairs the disclosure committee |
| Controller (Chief Accounting Officer) | SOX program owner |
| Vice President, Global Logistics | Senior management official for the DOT hazmat security plan (49 CFR 172.802(b)(1)) |
| Vice President, Digital Services | SL-1 telemetry and VMI service line owner |
| Vice President, Toll Manufacturing | SL-2 service line owner |
| Chief Data and Analytics Officer | Chairs the AI governance committee |
| Director of Identity and Access Management | Identity platform (SYS-04) |
| Director of Cloud Platform Engineering | Cloud landing zones in both clouds (common control provider) |
| Director of Network Engineering | Enterprise network, SD-WAN, and IT/OT boundary firewalls (common control provider) |
| Director of Endpoint Engineering | IT endpoints and EDR (common control provider) |
| Director of Third-Party Risk Management | Vendor tiering, contract security clauses, SOC report reviews (in the GRC team) |
| Vice President, Integration Management Office | Integration of the acquired plants |
| Chief Human Resources Officer | Onboarding, terminations, background checks, training records |
| Vice President, Corporate Security | Physical security and personnel surety across plants; former CFATS program lead |
| Vice President, Investor Relations | Investor communications; member of the disclosure committee |
| Vice President, Corporate Communications | Media and community communications during incidents |

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. Adding the Senior Vice President, Manufacturing and the Vice President, Process Safety and EHS is a POA&M action (gap 6).

**PL-01 GC-PCBMS figures.** About 412 OT user accounts (about 310 operators, 26 shift supervisors, 22 controls engineers and I&E technicians, and the rest maintenance, lab, and integrator accounts). 64 PLCs (packaging, truck rack, and terminal). About 140 tanks with radar level gauging. The Ammonia Unit SIS and Chlor Unit SIS are separate safety logic solvers; the terminal emergency shutdown uses a safety PLC. Production orders come from the ERP through an order relay in the OT DMZ. Historian data is replicated one way to Cloud provider A for analytics and AI-001.

**Service lines offered to external customers (P09).** SL-1: tank telemetry and VMI on Cloud provider B, with an annual SOC 2 Type 2 report (Security and Availability) since 2025. SL-2: toll manufacturing and contract formulation at PL-01, PL-03, PL-06, and PL-09, where customer-owned formulations run in the plant batch systems and customers receive batch records and certificates of analysis through a customer portal. No SOC 2 report yet.

**Recording and monitoring.** Fleet telematics records vehicle location and driving events, not audio or video. No AI use case records conversations.

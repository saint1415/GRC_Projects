# Scenario facts: Cris Santos Company | Chemical | Enterprise

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or NIST publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23) and the Federal Register API on 2026-10-05; CFATS status relies on the CISA CFATS page and uscode.house.gov as read on 2026-09-26 for the Small sample, plus a Federal Register search on 2026-10-05 that found no CFATS documents in 2026.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; specialty chemical formulator and packager) |
| Business | Formulates, blends, packages, and ships specialty chemicals: water treatment chemicals for municipal and industrial customers, process and cleaning chemicals, lubricant and fuel additive packages, and coatings additives. Also runs toll manufacturing and contract formulation for other companies, and a tank telemetry and vendor-managed inventory (VMI) service. Primary industry NAICS 325998, All Other Miscellaneous Chemical Product and Preparation Manufacturing |
| Location | Headquartered in Florida. 14 manufacturing plants (PLT-01 to PLT-14), 9 distribution centers, and 2 R&D centers in Florida, Georgia, Alabama, Louisiana, Texas, Tennessee, Ohio, and North Carolina. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Flagship site | **PLT-01 Gulf Coast Complex (Florida)**: a 180-acre waterfront site with an anhydrous ammonia unit, a chlorine and sodium hypochlorite unit (the "Chlor Unit"), three DCS-controlled blend halls, an additives unit that blends lubricant additive packages with base oils, a tank farm of about 140 tanks, packaging lines, a 12-bay truck rack, a rail yard, a QC laboratory, and a **marine terminal with two barge docks** that receives petroleum base oils by tank barge. About 1,150 employees; about 19% of company production volume |
| Workforce | 12,000 employees: about 7,400 in plant operations and maintenance, 1,600 in supply chain, logistics, and distribution (including about 310 company tank truck drivers), 900 in R&D and technical service, 1,100 in sales and customer service, and 1,000 in corporate functions (including about 480 in IT and about 96 in the CISO organization) |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day. The SBA size standard for NAICS 325998 is 650 employees (13 CFR 121.201), so the company is not small |
| Customers | About 38,000 business customers in the United States and 40 other countries, including about 1,900 municipal water utilities. About 2,900 customers use the tank telemetry and VMI service (SL-1) and about 85 use toll manufacturing (SL-2) |
| Ownership and governance | Publicly traded; board with an audit committee and a risk committee. The risk committee oversees cybersecurity and process safety risk. Not a smaller reporting company |
| Growth by acquisition | Three plants acquired in 2025: PLT-12 (Ohio, March 2025), PLT-13 (Tennessee, July 2025), and PLT-14 (North Carolina, November 2025). About 960 workforce members in total |
| Regulated inventory | See the tables below, taken from the threshold worksheets in the process safety information (EV-028). Maximum intended inventories are the limits written into the RMP and PSM process safety information (40 CFR 68.65(c)(1)(iii); 29 CFR 1910.119(d)(2)(i)(C)) and enforced by tank level alarms and cylinder caps |
| CFATS status | Nine plants filed Top-Screens because they held 50% hydrogen peroxide, a CFATS chemical of interest for theft and diversion (minimum concentration 35%, screening threshold quantity 400 lb; 72 FR 65396, Nov. 20, 2007), and six were tiered, including PLT-01. The statutory authority expired on **July 28, 2023** (6 U.S.C. 621-629 shown as omitted at uscode.house.gov), and CFATS has **not been reauthorized**. CISA states it cannot enforce CFATS. The company kept its Site Security Plan measures and uses RBPS 8 as a **voluntary enterprise benchmark** (P03). Status determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-CHEMICAL-R01; EV-055, EV-057) |
| USCG MTSA status | **Covered at PLT-01 only.** The marine terminal can transfer oil (petroleum base oils) in bulk to or from tank barges with a capacity of 250 barrels or more, so 33 CFR Part 154 applies (154.100(a)). A facility subject to Part 154 must have a Facility Security Plan under 33 CFR Part 105 (105.105(a)(1)), and the cybersecurity rule in 33 CFR Part 101 Subpart F applies to every facility required to have a security plan under Part 105 (101.605(a)). Key dates: cybersecurity training by January 12, 2026 and annually (101.650(d)(4)); Cybersecurity Assessment and Cybersecurity Plan submission no later than July 16, 2027 (101.650(e)(1); 101.655). No other plant has a marine transfer. Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-CHEMICAL-R02; EV-029) |
| EPA RMP status | **Covered at 8 plants.** Program 3 at PLT-01, PLT-04 (Louisiana), and PLT-05 (Texas), because those processes are also covered by OSHA PSM (40 CFR 68.10(l)(2)); NAICS 325998 is not in the 68.10(l)(1) list. Program 2 at PLT-02, PLT-03, PLT-06, PLT-07, and PLT-09 (29% aqueous ammonia above the 20,000 lb threshold quantity; worst-case release reaches public receptors, so Program 1 is not available, 68.10(j)(2)). PLT-01 is a **responding stationary source** with its own hazardous materials team (68.90(a); 68.95). The 2024 amendments add requirements with a May 10, 2027 compliance date (68.10(g)), including safer technology and alternatives analysis for NAICS 325 processes (68.67(c)(9)). Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (EPA-RMP; EV-026, EV-028) |
| OSHA PSM status | **Covered processes at PLT-01, PLT-04, and PLT-05** (29 CFR 1910.119(a)(1)(i)). Math below. Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (OSHA-PSM; EV-028) |
| DOT hazmat security plan | **Required.** The company offers large bulk quantities (more than 3,000 liters in one packaging) of Class 3 Packing Group II solvent blends and of 50% hydrogen peroxide (Division 5.1, Packing Group II) in cargo tanks and rail cars (49 CFR 172.800(b)(6) and (b)(10)). The enterprise security plan covers personnel security, unauthorized access, and en route security (172.802(a)), is reviewed annually (172.802(c)), and requires security awareness and in-depth security training (172.704(a)(4)-(5)). Senior official: Vice President, Global Logistics. Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (DOT-HMSP; EV-056) |
| SEC | Form 8-K Item 1.05 (material cybersecurity incidents, within 4 business days after the materiality determination) and Regulation S-K Item 106 (annual risk management, strategy, and governance disclosure in the 10-K) apply. SOX IT general controls cover the ERP and payroll. Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (SEC-8K-1.05, SEC-SK-106, SOX-404; EV-039) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-CHEMICAL-R03, FAR-52.204, EAR, HIPAA; EV-044, EV-057, EV-058). **CIRCIA:** proposed rule only (89 FR 23644, 2024-04-04); no final rule in the Federal Register as of 2026-10-05. As proposed, the company would be covered (above the SBA size standard, and PLT-01 is an MTSA facility). **FAR clauses:** no federal prime contracts or subcontracts; government customers buy through distributors. **EAR:** exports are handled by the export compliance program; EAR-controlled technology is classified Restricted (POL-04) but export licensing is not analyzed here. **HIPAA:** the employee health plan is a separate covered entity handled by the benefits program |
| Regulatory driver IDs | **C-CHEMICAL-R01** (CFATS RBPS 8, voluntary benchmark), **C-CHEMICAL-R02** (USCG MTSA cybersecurity rule, binding at PLT-01), **C-CHEMICAL-R03** (CIRCIA, proposed). EPA RMP (40 CFR Part 68), OSHA PSM (29 CFR 1910.119), DOT hazmat security plans (49 CFR 172.800-172.804), CERCLA and EPCRA release reporting (40 CFR 302.6; 355.40-355.43), SEC rules, and the OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) are cited directly because the vertical registry has no ID for them |

### Regulated inventory and threshold math (PLT-01 Gulf Coast Complex)

| Chemical | Storage | Maximum intended inventory | EPA RMP (40 CFR 68.130) | OSHA PSM (29 CFR 1910.119 App. A) | CFATS App. A (legacy) |
|---|---|---|---|---|---|
| Anhydrous ammonia | One 18,000-gal (water capacity) pressure vessel, fill limit 85%, feeding the aqueous ammonia dilution system | 18,000 x 0.85 = 15,300 gal x 5.15 lb/gal = **78,795 lb** | "Ammonia (anhydrous)", TQ 10,000 lb: **covered** | "Ammonia, Anhydrous", TQ 10,000 lb: **covered** | Not used for the legacy tiering |
| Chlorine | Ton containers, inventory cap of 8 on site (2,000 lb each) | 8 x 2,000 = **16,000 lb** | "Chlorine", TQ 2,500 lb: **covered** | "Chlorine", TQ 1,500 lb: **covered** | Not used for the legacy tiering |
| Hydrogen peroxide, 50% | Two 4,000-gal tanks (combined level limit 7,000 gal) | 7,000 gal x 10.0 lb/gal = 70,000 lb of solution; 35,000 lb of hydrogen peroxide | Not listed | Listed only at 52% by weight or greater: **not covered** | Theft and diversion chemical of interest at 35% or more, STQ 400 lb: the basis of the legacy Top-Screen |
| Isopropyl alcohol, 99% (flash point below 100 F) | Two 30,000-gal atmospheric tanks | About 393,000 lb | Not listed | Above 10,000 lb, but excepted because it is stored in atmospheric tanks below its normal boiling point without chilling (1910.119(a)(1)(ii)(B)) | Not relevant |
| Petroleum base oils | Tank farm, received by barge | About 9.5 million lb | Not listed | Not listed (flash point above 100 F) | Not relevant; the reason the marine terminal is a Part 154 facility |

**Result for PLT-01:** two PSM-covered processes (the ammonia unit and the Chlor Unit), both in RMP Program 3. PLT-04 (anhydrous ammonia, about 41,000 lb) and PLT-05 (chlorine ton containers, cap of 6, 12,000 lb) were assessed the same way and are also PSM and Program 3. The Program 2 plants hold 29% aqueous ammonia above the 20,000 lb TQ for "Ammonia (conc 20% or greater)", as in the Small sample's math. **Limit the company must keep:** hydrogen peroxide is bought below 52% at every plant (management of change, POL-01 4.13).

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

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Notes |
|---|---|---|
| SYS-01 | PLT-01 Gulf Coast Complex process control: DCS, batch management system, two safety instrumented systems (SIS), terminal automation and emergency shutdown, process historian, and the PLT-01 OT network and OT DMZ | The P02 system. One DCS platform with 22 redundant controller pairs, 6 redundant server pairs, 38 operator stations, and 6 engineering workstations (EWS); about 1,900 master recipes and about 260 batches a day (EV-012, EV-052) |
| SYS-02 | Process control at the other 13 plants | 3 DCS platforms and about 420 PLCs; SIS at 8 plants. OT DMZs at 10 of 14 plants (not at PLT-12 to PLT-14 and PLT-08) (EV-012, EV-013) |
| SYS-03 | Enterprise OT security services | Central remote access gateway (session approval, MFA, recording) at 11 of 14 plants; passive OT network monitoring at 9 of 14 plants; OT backup vault (offline and immutable copies); OT patch and media staging (EV-007, EV-016, EV-019) |
| SYS-04 | Identity platform (SSO, MFA, privileged access management, identity governance) | Covers IT, cloud, and the OT remote access gateway. Each plant's OT uses a separate OT directory or local accounts (EV-001, EV-006) |
| SYS-05 | ERP (global SaaS) and plant manufacturing execution systems (MES) | SOX-relevant; order, inventory, and bill-of-materials records, including hydrogen peroxide inventory |
| SYS-06 | Laboratory information management system (LIMS) | Enterprise LIMS on Cloud provider A; certificates of analysis for every batch |
| SYS-07 | Multi-cloud estate plus 2 colocation data centers | Cloud provider A: ERP integration, LIMS, data platform, historian replicas, AI/ML platform. Cloud provider B: the SL-1 telemetry platform. Colocation DC-1 (Florida) and DC-2 (Ohio) |
| SYS-08 | Enterprise network | SD-WAN to 40 sites; IT/OT boundary firewalls at every plant |
| SYS-09 | Endpoints | About 14,500 IT endpoints (EDR on 98%); about 2,300 OT workstations and servers (EDR or application allowlisting on 61%) (EV-010, EV-011) |
| SYS-10 | Tank telemetry and VMI platform (SL-1) | About 41,000 cellular tank sensors at about 6,800 customer sites; customer portal with about 9,500 user accounts; about 1,400 automatic replenishment orders a week into the ERP (EV-069) |
| SYS-11 | Transportation management system and fleet telematics | Hazmat shipments, about 220 company tank trucks, and contract carriers; supports the DOT security plan's en route measures |
| SYS-12 | Physical security systems | Badge access and video at 14 plants; TWIC readers at the PLT-01 marine terminal (legacy CFATS and MTSA measures) |
| SYS-13 | Third parties | About 2,600 vendors; about 180 with OT or remote access, including 6 DCS and PLC integrators (EV-042) |
| SYS-14 | AI portfolio (12 use cases) | Governed by an AI governance committee formed in 2025 (P10; EV-074, EV-075, EV-096) |
| SYS-15 | HR and payroll SaaS | Employee PII for 12,000 employees and former employees |
| SYS-16 | Productivity suite (email, files, chat) | SaaS |

**SSP system (P02):** the *Gulf Coast Complex Process Control and Batch Management System (GC-PCBMS)*: the PLT-01 DCS and batch management system, the Ammonia Unit SIS and Chlor Unit SIS, the marine terminal automation and emergency shutdown system, the process historian, the PLT-01 control and supervisory networks and OT DMZ, and the OT workstations at PLT-01, inheriting common controls from the enterprise OT security services, identity platform, SOC, and cloud landing zone.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. At this size the sources are enterprise systems of record across IT, OT, and process safety (identity platform, OT directories and DCS configuration, the OT security services, SIEM, MOC and PSM records), prior Internal Audit and SOX workpapers, the FSO's MTSA records, regulator correspondence, and board and committee records.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv), reviewed by the General Counsel's office.
- **Gaps against the MTSA cybersecurity rule, RMP, PSM, and the other applicable rules** are judged in the gap analysis (P03), and **whether controls work** is tested by Internal Audit in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 | Gulf Coast Complex Process Control and Batch Management System (GC-PCBMS), High baseline with OT tailoring and common control inheritance |
| P03 | All applicable regulations across the enterprise: USCG MTSA cybersecurity rule at PLT-01 (binding); EPA RMP and OSHA PSM elements that depend on the control systems (binding); DOT hazmat security plans (binding); SEC Item 1.05 and Item 106 (binding); CERCLA and EPCRA release reporting (binding); state breach laws (binding); CFATS RBPS 8 as the voluntary enterprise benchmark (primary benchmark in the vertical registry); CIRCIA (proposed, tracked) |
| P04 | Multi-cloud (vendor-agnostic) with platform, landing zone, workload, and SaaS layers, plus the OT-to-cloud data paths |
| P05 | Enterprise-wide BIA with a dependency map and third parties |
| P07 | Internal Audit assessment of 42 controls on the GC-PCBMS and its inherited common controls, with statistical sampling |
| P08 | Intrusion into the PLT-01 process control systems through a compromised integrator account on the remote access gateway, with alarm limit changes on the ammonia unit, then ransomware on the historian and OT workstations, including the **SEC materiality assessment and 8-K Item 1.05** step and the MTSA, release, and process safety reporting |
| P09 | SOC 2 Type 2 readiness across two service lines offered to external customers: SL-1 tank telemetry and VMI, and SL-2 toll manufacturing and contract formulation |
| P10 | Enterprise AI portfolio (12 use cases) with the AI governance committee; full assessment of AI-001 process-optimization model |
| Cloud | Multi-cloud (vendor-agnostic) with common controls |

**Why the registry defaults were kept.** The registry's primary system (process control and batch management), incident (intrusion into process control at a chemical facility), and AI use case (process-optimization model) all fit an enterprise chemical maker. At this size they are scoped to the flagship plant (PLT-01) because it is the only plant where all the binding regulations meet: MTSA, PSM, RMP Program 3, and the DOT security plan.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-04-06 to 2026-04-30 | Intake: evidence requests, exports from systems of record, inventories, obligations register (reviewed by counsel) |
| 2026-05-04 to 2026-07-10 | Enterprise BIA interviews and workshops |
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (evidence sampling completed 2026-08-14) |
| 2026-06-22 to 2026-07-10 | 2026 annual revision of POL-01 to POL-05 drafted from the intake evidence and early risk and gap results |
| 2026-07-13 to 2026-08-28 | Control assessment by Internal Audit (OT testing at PLT-01 on 2026-08-11 to 2026-08-13 during a planned ammonia unit outage): operating tests of controls in force under the 2025 policy set; design review of the draft 2026 revisions |
| 2026-08-24 | SOC 2 readiness assessment completed |
| 2026-08-26 | AI governance committee portfolio review |
| 2026-09-08 | Executive risk committee approvals |
| 2026-09-10 | Results to the board risk committee and audit committee; 2026 revisions of POL-01 to POL-05 approved (effective 2026-10-01) |
| 2027-03 (planned) | Internal Audit follow-up: operating effectiveness of the controls the 2026 revisions and POA&M items introduced, after at least one quarter of operation |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Plants.**
| Plant | State | Notes |
|---|---|---|
| PLT-01 Gulf Coast Complex | Florida | Flagship; MTSA facility; PSM and RMP Program 3 (ammonia unit, Chlor Unit); SL-2 toll blending; about 1,150 employees |
| PLT-02 | Georgia | Water treatment chemicals; RMP Program 2 |
| PLT-03 | Alabama | Process chemicals; RMP Program 2; SL-2 toll blending |
| PLT-04 | Louisiana | Anhydrous ammonia; PSM and RMP Program 3 |
| PLT-05 | Texas | Chlorine and hypochlorite; PSM and RMP Program 3 |
| PLT-06 | Texas | Additive packages; RMP Program 2; SL-2 toll blending |
| PLT-07 | Georgia | Water treatment chemicals; RMP Program 2 |
| PLT-08 | Florida | Packaging and repackaging only; no OT DMZ (small PLC estate) |
| PLT-09 | Louisiana | Process chemicals; RMP Program 2; SL-2 toll blending |
| PLT-10 | Alabama | Coatings additives |
| PLT-11 | Ohio | Cleaning chemicals |
| PLT-12 | Ohio | Acquired 2025-03; coatings additives |
| PLT-13 | Tennessee | Acquired 2025-07; process chemicals |
| PLT-14 | North Carolina | Acquired 2025-11; water treatment chemicals |

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Senior Vice President, Manufacturing | All 14 plants; plant managers report to this role |
| Vice President, Process Safety and EHS | Corporate PSM and RMP program; release reporting standards; PHA and MOC system owner |
| PLT-01 Plant Manager | System owner of the GC-PCBMS; RMP qualified person for PLT-01 (40 CFR 68.15(b)); incident commander for process emergencies at PLT-01 |
| PLT-01 Facility Security Officer (FSO) | MTSA Facility Security Plan (33 CFR Part 105) |
| PLT-01 Cybersecurity Officer (CySO) | Designated in writing by name and title under 33 CFR 101.620(b)(3) (the name is kept in the SSI-protected Cybersecurity Plan). The CySO is the PLT-01 OT Security Lead, who reports to the Director of OT Security; the Director of OT Security is the alternate |
| PLT-01 Controls Engineering Manager | DCS, batch, SIS, and terminal automation engineering; approves control system changes |
| Director of Automation Engineering | Corporate DCS and PLC standards and the integrator contracts |
| Process Safety Manager, PLT-01 | PHAs, MOC, incident investigations, and compliance audits at PLT-01 |
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

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. Adding the Senior Vice President, Manufacturing and the Vice President, Process Safety and EHS is a POA&M action (POAM-004; EV-038, EV-IR-8).

**PLT-01 GC-PCBMS figures.** About 412 OT user accounts (about 310 operators, 26 shift supervisors, 22 controls engineers and I&E technicians, and the rest maintenance, lab, and integrator accounts). 64 PLCs (packaging, truck rack, and terminal). About 140 tanks with radar level gauging. The Ammonia Unit SIS and Chlor Unit SIS are separate safety logic solvers; the terminal emergency shutdown uses a safety PLC. Production orders come from the ERP through an order relay in the OT DMZ. Historian data is replicated one way to Cloud provider A for analytics and AI-001 (EV-006, EV-012, EV-066).

**Service lines offered to external customers (P09).** SL-1: tank telemetry and VMI on Cloud provider B, with an annual SOC 2 Type 2 report (Security and Availability) since 2025. SL-2: toll manufacturing and contract formulation at PLT-01, PLT-03, PLT-06, and PLT-09, where customer-owned formulations run in the plant batch systems and customers receive batch records and certificates of analysis through a customer portal. No SOC 2 report yet (EV-046, EV-047).

**Recording and monitoring.** Fleet telematics records vehicle location and driving events, not audio or video. No AI use case records conversations.

**Plant identifiers.** Plants are numbered PLT-01 to PLT-14. The "PLT-" prefix is used so plant IDs are never confused with NIST SP 800-53 PL-family control IDs (for example, PL-2 or PL-10).

**More roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Director of Security Operations | Runs the 24x7 SOC (common control provider CCP-04); incident commander for the cyber response (P08) |
| Vice President, Quality | Quality release, LIMS, and certificates of analysis (P05 BP-08; P10 AI-008) |
| Senior Vice President, Water Treatment Business | Supply to municipal water utilities (P05 BP-09) |
| Chief Procurement Officer | Procurement and inbound raw materials (P05 BP-12) |
| Senior Vice President, Commercial | Customer and technical service, SDS distribution (P05 BP-16) |
| Operations superintendent (PLT-01) | Backup incident commander for process safety on shift (P08) |

**Workforce by state.** About 4,600 of the 12,000 employees work in Florida (headquarters, PLT-01, PLT-08, and Florida distribution centers) (EV-005). This drives the Florida worked example in P08.

**Events after fieldwork (used in the deliverables).** The 3 shared integrator accounts on the remote access gateway were disabled on 2026-09-15 (POAM-005). AI-012, a closed-loop model inherited at PLT-13, was switched to advisory mode and AI-011 resume ranking was suspended on 2026-08-27 (P10).

**SL-2 contract term.** SL-2 toll agreements require notice to the customer within 72 hours of an incident affecting that customer's recipes (contract, P08).

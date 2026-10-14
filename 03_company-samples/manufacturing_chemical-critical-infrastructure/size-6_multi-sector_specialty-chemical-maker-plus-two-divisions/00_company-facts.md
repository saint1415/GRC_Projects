# Scenario facts: Cris Santos Company | Chemical | Multi-Sector

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Regulatory facts were checked against eCFR (point in time 2026-09-23), the Federal Register, and nist.gov between 2026-09-26 and 2026-10-05. Citations reused from the Chemical Small sample were re-checked for this size.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; diversified specialty chemicals group) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate operating subsidiary |
| Division 1: Specialty Chemicals (NAICS 325998), **focus of this scenario** | Formulates, manufactures, and packages specialty chemicals: water treatment chemicals (including sodium hypochlorite made from chlorine and caustic soda), cleaning and sanitation chemicals, and process chemicals, plus toll blending and private-label packaging. **16 plants in 8 states** (Florida, Georgia, Alabama, Louisiana, Texas, Tennessee, Ohio, and Pennsylvania). The flagship is **Plant C1** in Florida: an inland, rail-served, 120-acre site with chlorine rail unloading, two sodium hypochlorite reactor trains, a bulk tank farm, three blend halls, four packaging lines, a quality control laboratory, and a truck loading rack. About 24,000 employees |
| Division 2: Chemical Distribution (NAICS 424690, sector 42 Wholesale Trade) | Distributes the group's products and about 9,000 third-party chemical products to about 38,000 industrial, municipal, and food-processing customers in 30 states. **64 distribution branches** (warehouses with drum and tote repackaging) and **3 bulk liquid terminals**. **Terminal T1**, at a Florida deepwater port, receives chemical tankers and tank barges and is an **MTSA-regulated facility** under 33 CFR Part 105. Also runs a **managed inventory service** (tank telemetry and automatic replenishment) at about 2,600 customer sites. About 9,500 employees |
| Division 3: Hazmat Transport (NAICS 484230, sector 48-49 Transportation and Warehousing) | Motor carrier hauling bulk liquid and packaged hazardous materials for the group and about 1,400 third-party shippers in 48 states. About 1,900 tractors, 1,400 cargo tank trailers, 1,100 van and flatbed trailers, and 2,700 drivers, from 28 terminals with cargo tank wash racks. About 6,000 employees |
| Corporate shared services | Identity, network, security operations, OT security engineering, cloud and data platform, ERP, the 24x7 Group Emergency Response Center, process safety center of excellence, HR, finance, legal, and internal audit. About 5,500 employees |
| Location | Headquartered in Florida. Operations in 30 states; trucks run in 48. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| SBA size status | Not small. The SBA standard for NAICS 325998 is 650 employees (13 CFR 121.201) |
| Why these three businesses | The chemical maker distributes and transports its own products. About 30% of Specialty Chemicals volume is sold through Distribution, and about 55% of the two divisions' bulk outbound loads move on Hazmat Transport trucks |
| Regulated inventory | Plant C1 threshold math is in the table below. Maximum intended inventories are the limits in the Plant C1 process safety information (40 CFR 68.65(c)(1)(iii); EV-045) |
| CFATS status | Seven plants, including Plant C1, filed Top-Screens and were tiered before the statutory authority expired on **July 28, 2023**. CFATS has **not been reauthorized**: the vertical registry confirmed this on 2026-09-25, and a Federal Register search on 2026-10-05 found no CFATS document since June 2025. The group kept the physical measures of the legacy Site Security Plans and uses RBPS 8 as a **voluntary benchmark** (P03). Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-CHEMICAL-R01-SC; EV-044) |
| EPA RMP and OSHA PSM status | **Plant C1:** the chlorine process is covered by OSHA PSM and therefore by **RMP Program 3** (40 CFR 68.10(l)(2)). Plant C1 is a **responding stationary source** with its own trained hazardous materials team (68.95). RMP five-year update submitted 2024-06-20; last compliance audit 2025-05-14. **Four other plants** hold more than 20,000 lb of ammonia in 29% aqueous ammonia and run **RMP Program 2**. The other 11 plants, the branches, and the terminals hold no RMP-listed substance above its threshold quantity (annual inventory screen, 2026-03). Decided in the obligations register (RMP-P3, RMP-P2, RMP-OTHER, PSM; EV-043, EV-045, EV-046) |
| Not in scope | USCG Subpart F applies to Terminal T1 only (no other plant, branch, or terminal has a 33 CFR Part 105 security plan). CIRCIA: proposed rule only, not in effect. FAR safeguarding clauses: no federal contracts. FMCSA hazardous materials safety permit (49 CFR 385.403): Hazmat Transport does not haul explosives, radioactive material, poisonous-by-inhalation materials, or bulk methane, so no permit is needed (chlorine arrives at Plant C1 by rail only). TSA surface Security Directives: none apply to the group (they cover designated pipelines and railroads). No DEA List I chemicals are distributed. No payment cards are accepted (customers pay by ACH and check). Group trade compliance found no EAR-controlled technology in the systems in this sample (review 2026-03). Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (EV-036, EV-037, EV-071, EV-081) |
| Regulatory driver IDs | **C-CHEMICAL-R01** (CFATS RBPS 8, voluntary benchmark), **C-CHEMICAL-R02** (USCG Subpart F; applies to Terminal T1; the same rule is N48-49-R01 in the transportation registry), **C-CHEMICAL-R03** (CIRCIA, proposed), **N42-R07** (SEC disclosure). EPA RMP and EPCRA, CERCLA, the Hazardous Materials Regulations (HMR), FMCSA rules, and the OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) are cited directly, because the registries have no ID for them. The obligations register lists each one, for each division and the group |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

### Plant C1 regulated inventory and threshold math
| Chemical | Storage | Maximum intended inventory | EPA RMP (40 CFR 68.130) | OSHA PSM (29 CFR 1910.119 App. A) | CFATS App. A (legacy) |
|---|---|---|---|---|---|
| Chlorine (liquefied gas) | Up to 2 rail tank cars of 90 tons each, both connected to the unloading manifold (one unloading, one on standby), piped to two hypochlorite reactor trains | 2 x 180,000 lb = **360,000 lb** | Listed, TQ 2,500 lb. Transportation containers connected for unloading are part of the stationary source (68.3), so the process is covered with a large margin | Listed, TQ 1,500 lb: **covered**. This makes the process **RMP Program 3** (68.10(l)(2)) | Release-toxic chemical of interest with an STQ of 2,500 lb (72 FR 65396, Nov. 20, 2007, discussion at 65407): basis for the legacy Top-Screen and tier |
| Hydrogen peroxide, 50% | Two 20,000-gal tanks (combined level limit 34,000 gal) | 34,000 gal x 10.0 lb/gal = 340,000 lb of solution; **170,000 lb of hydrogen peroxide** | Not listed | Listed only at 52% by weight or greater: **not covered** | Theft and diversion chemical of interest at a minimum concentration of 35%, STQ 400 lb (72 FR 65396): far above |
| Sodium hydroxide, 50% | Three 30,000-gal tanks | About 1,150,000 lb | Not listed | Not listed | Not relevant |
| Sodium hypochlorite, 12.5% (product) | Ten 25,000-gal tanks | About 2,400,000 lb | Not listed | Not listed | Not relevant |

**Limits Plant C1 must keep** (management of change, POL-01 4.13): hydrogen peroxide is bought below 52%, and flammable liquids stay under 10,000 lb in any one process location, so neither becomes a second PSM-covered process.

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and process safety oversight; accepts Very High risks; receives the High risk list quarterly |
| Board audit committee | Oversees group internal audit |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3) |
| Group OT Security Director | Reports to the Group CISO. OT security standard, OT DMZ pattern, OT remote access gateway design, OT monitoring sensors, and the OT desk of the group SOC for all divisions |
| Group Chief Risk Officer | Group risk register and enterprise risk management (ERM) roll-up; chairs the Group AI council |
| Group General Counsel | Notification matrix, intercompany agreements, regulator notices, privilege |
| Group Process Safety Director | Process safety center of excellence: RMP and PSM standards, PHA and MOC methods, compliance audit program across plants |
| Group Emergency Response Center (ERC) manager | 24x7 emergency response telephone service on group shipping papers (49 CFR 172.604) and the group crisis line |
| Division security and compliance leads (3) | Division registers, division supplements, division-specific regulators |
| Specialty Chemicals: Vice President of Manufacturing Technology | Business owner of the plant control system standard for all 16 plants |
| Specialty Chemicals: Director of Process Control Engineering | Runs the central Process Control Engineering hub (SYS-C8) and its configuration repositories |
| Plant C1 Plant Manager | RMP qualified person with overall responsibility for the risk management program (40 CFR 68.15(b)); system owner of the PCBMS; incident commander for process emergencies |
| Plant C1 Process Safety Manager | PHA, MOC, pre-startup safety reviews, compliance audits, and the RMP update for Plant C1 |
| Plant C1 Controls Engineering Manager | DCS, SIS, PLCs, and the OT network at Plant C1; approves control system configuration changes |
| Specialty Chemicals EHS director | CERCLA and EPCRA release reporting; emergency response coordination |
| Specialty Chemicals Process Engineering Director | Business owner of AI-001, the process-optimization model (P10) |
| Distribution: Terminal T1 Terminal Manager | Terminal operations, marine transfers, and the terminal control systems |
| Distribution: Terminal T1 Facility Security Officer (FSO) | Facility Security Plan under 33 CFR 105.205 |
| Distribution: Cybersecurity Officer (CySO) for Terminal T1 | The Distribution OT security manager, designated in writing under 33 CFR 101.620(b)(3) in 2025 |
| Distribution: Transportation Security Coordinator | Senior management official for the Distribution hazmat transportation security plan (49 CFR 172.802(b)(1)) |
| Distribution: managed inventory service director | Business owner of the managed inventory service platform (SYS-D3) |
| Hazmat Transport: Vice President of Safety and Compliance | Senior management official for the carrier's security plan (49 CFR 172.802(b)(1)); FMCSA compliance |
| Hazmat Transport: Director of Fleet Technology | TMS, telematics, ELDs, and driver-facing cameras |
| Group internal audit | Reports to the board audit committee. Assesses common controls once and samples division controls |
| Disclosure committee | SEC materiality of cybersecurity incidents |
| Group AI council | Approves High-tier AI use cases |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in the [vendor register](step-00_P00_intake/vendor-register.csv).

| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (SSO, MFA, PAM, identity governance) and the **group OT remote access gateway** | Corporate | All divisions federate to SSO. The OT remote access gateway carries vendor, integrator, and central engineering sessions into the OT DMZs of all 16 plants and Terminal T1 (EV-015) |
| SYS-G2 | Group SOC, SIEM, EDR (24x7), and the OT monitoring console | Corporate | EDR on all IT servers and workstations. Passive OT monitoring sensors at the 9 plants on the OT standard and at Terminal T1 (EV-016, EV-018) |
| SYS-G3 | Group cloud platform (providers A and B, vendor-agnostic), landing zones, WAN, and immutable backup vault | Corporate | Provider A primary; provider B for disaster recovery and the backup vault |
| SYS-G4 | Group ERP (order-to-cash, procure-to-pay, inventory including chemical-of-interest tracking, maintenance work orders, and hazmat shipping paper data), HR and payroll (SaaS) | Corporate | Shipping papers for all three divisions are generated from ERP product data |
| SYS-G5 | Productivity suite (email, files, chat) | Corporate | |
| SYS-G6 | Group data platform (historian replicas, process analytics, machine learning workspace) | Corporate | Pulls historian data from plant OT DMZ brokers; trains AI-001 |
| SYS-G7 | Product stewardship and SDS authoring system (SaaS) and the Emergency Response Center console | Corporate | Product hazard data and SDS for about 11,000 products; feeds ERC responders and shipping papers |
| SYS-C1 | Plant C1 distributed control system (DCS) | Specialty Chemicals | Redundant controllers and server pairs, 14 operator stations, 3 engineering workstations (EWS). Controls chlorine unloading, both hypochlorite reactor trains, the tank farm, and the blend halls. One major release behind the vendor's current release (EV-055) |
| SYS-C2 | Plant C1 batch management and recipe system | Specialty Chemicals | Batch execution for about 2,300 master recipes (trade secrets), synchronized from the division recipe library in SYS-C8. Receives production orders from SYS-G4 |
| SYS-C3 | Plant C1 safety instrumented system (SIS) | Specialty Chemicals | Separate safety controllers: chlorine car emergency isolation, reactor high-temperature and feed-ratio trips, scrubber trips, hydrogen peroxide tank high-temperature trip. Separate SIS engineering workstation. Proof tests at each turnaround |
| SYS-C4 | Plant C1 rail unloading, tank farm, and loading rack PLCs; chlorine and toxic gas detection system | Specialty Chemicals | 46 PLCs; 38 chlorine detectors alarmed in the control room and at the ERC |
| SYS-C5 | Plant C1 process historian and OT DMZ | Specialty Chemicals | Historian replica broker in the OT DMZ feeds SYS-G6 and the AI-001 advisory interface |
| SYS-C6 | Control systems at the other 15 plants | Specialty Chemicals | 8 plants on the group OT standard; **7 legacy plants** (5 acquired in 2024) with flat networks, dual-homed historians, unsupported HMIs, and no OT monitoring (EV-066) |
| SYS-C7 | Laboratory information management system (LIMS) | Specialty Chemicals | SaaS; certificates of analysis for all plants |
| SYS-C8 | Central Process Control Engineering hub | Specialty Chemicals | Engineering workstations, configuration and recipe repositories, and DCS backup server at the division engineering center. Reaches every plant's EWS through the SYS-G1 OT remote access gateway |
| SYS-C9 | AI-001 process-optimization model service | Specialty Chemicals | Runs on provider A; reads the Plant C1 historian replica; writes recommended setpoints to the advisory interface in the Plant C1 OT DMZ (EV-068, EV-099) |
| SYS-D1 | Terminal T1 terminal automation | Distribution | Tank gauging, pump and valve PLCs, marine transfer controls, truck and rail loading racks, and the terminal management system |
| SYS-D2 | Warehouse management system and repackaging line PLCs | Distribution | 64 branches |
| SYS-D3 | Managed inventory service platform | Distribution | About 2,600 cellular tank telemetry gateways at customer sites, a telemetry service on provider A, and the customer portal (orders, SDS, certificates of analysis, inventory) |
| SYS-D4 | Terminal T1 physical access control (TWIC readers) and CCTV | Distribution | Reader records are SSI (33 CFR 105.225(c)) |
| SYS-T1 | Transportation management system (TMS) | Hazmat Transport | Dispatch, load planning, electronic shipping papers, and customer load tracking |
| SYS-T2 | Fleet telematics, electronic logging devices (ELDs), cargo tank sensors, and driver-facing cameras with AI event scoring | Hazmat Transport | Vendor SaaS |
| SYS-T3 | Driver qualification and drug and alcohol testing records | Hazmat Transport | Vendor SaaS; PII for about 2,700 drivers and 1,900 former drivers |
| SYS-T4 | Fleet maintenance and cargo tank inspection records | Hazmat Transport | Vendor SaaS |

**SSP system (P02):** the *Plant C1 Process Control and Batch Management System (PCBMS)*: the Plant C1 DCS (SYS-C1), batch management and recipe system (SYS-C2), SIS (SYS-C3), rail unloading, tank farm, and loading rack PLCs and the gas detection system (SYS-C4), the historian and OT DMZ (SYS-C5), and the Plant C1 OT network and OT workstations. It inherits common controls from SYS-G1 to SYS-G3 and interconnects with SYS-C8, SYS-C9, SYS-G4, and SYS-G6.

**Registry defaults kept.** The primary system (process control and batch management), the P08 incident (intrusion into process control systems at a chemical facility), and the P10 use case (process-optimization model) all fit this business. At this size the P08 intrusion starts in a shared service (the OT remote access gateway) so it reaches Plant C1 and Terminal T1, and P10 covers the group AI program with the process-optimization model as the priority use case.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Rows are grouped by division (Group, Specialty Chemicals, Distribution, Hazmat Transport). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** to each division and to the group is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps** against the RBPS 8 and OT benchmarks, EPA RMP, the USCG cyber rule, the hazmat transportation rules, and the group-wide rules are judged in the gap analyses (P03), which also number the ten group gaps cited across this sample, and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Regulation (P03) | Specialty Chemicals: **CFATS RBPS 8 (6 CFR 27.230(a)(8)) as a voluntary benchmark**, with the OT benchmark (CSF 2.0 with SP 800-82 Rev. 3), plus binding **EPA RMP Program 3** at Plant C1 (with OSHA PSM parallels), CERCLA and EPCRA release notices, and the HMR security plan as an offeror. Distribution: **USCG 33 CFR Part 101 Subpart F** at Terminal T1 (binding) and the HMR security plan as an offeror. Hazmat Transport: **HMR security plan and training** as a carrier (49 CFR 172.800 to 172.804, 172.704), HMR incident reports (171.15, 171.16), and FMCSA ELD and driver record rules. Group: SEC Reg S-K Item 106 and Form 8-K Item 1.05, state breach laws, applicability screens |
| Regulatory driver labels | `C-CHEMICAL-R01 (...)` marks the RBPS 8 voluntary benchmark; `OT-BM (...)` marks a CSF 2.0 or SP 800-82 Rev. 3 benchmark row; `RMP 68.xx` marks 40 CFR Part 68; `C-CHEMICAL-R02 (101.xxx)` marks USCG Subpart F; `HMR 17x.xxx` and `FMCSA 3xx.xx` mark DOT rules; `N42-R07` marks SEC disclosure; `C-CHEMICAL-R03 (proposed)` marks CIRCIA items tracked but not required |
| P08 | An intruder uses a stolen integrator credential on the group OT remote access gateway to reach the Plant C1 DCS engineering workstation, changes hypochlorite reactor alarm limits and a chlorine feed setpoint (the SIS trips the reactor safely), then probes the Terminal T1 tank gauging network and deploys ransomware on ERP-connected servers that stops order release and electronic shipping papers for Distribution and Hazmat Transport: a multi-regulator notification matrix with EPA, Coast Guard, DOT, SEC, and state duties |
| P09 | SOC 2 scoped per division: the Distribution managed inventory service is in scope for a first report; Specialty Chemicals and Hazmat Transport are out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the rules that bear on them, with the AI-001 process-optimization model as the priority use case |
| Cloud | Shared corporate platform (providers A and B) plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-03-30 to 2026-04-24 | Intake: evidence requests, exports, walk-throughs, inventories, obligations register, grouped by division |
| 2026-05-04 to 2026-07-31 | Group and division BIAs (BIA interviews in May), risk analyses (risk interviews in June), and gap analyses (gap analysis interviews from 2026-06-29) |
| 2026-06-01 to 2026-06-26 | Group policies v2026 drafted from the intake observations and the risks and gaps found so far (P06); the Specialty Chemicals supplement was aligned to the drafts on 2026-06-30 |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples. OT tests at Plant C1 on 2026-08-12 during a planned turnaround, at Terminal T1 on 2026-08-19, and at two Hazmat Transport terminals on 2026-08-25. Operating tests of controls in place under the 2025 group policies, the OT security standard, the incident response plan v2025 and division procedures; the draft notification matrix was reviewed for design only |
| 2026-08-31 to 2026-09-04 | SOC 2 readiness self-assessment (P09) and Group AI council review (P10, 2026-09-02) |
| 2026-09-17 | Results to the board risk committee; deliverables and group policies v2026 approved (policies effective 2026-10-01) |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the v2026 policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Process safety and public safety risks rated High must be treated, not accepted (ERM risk acceptance standard, EV-005) |
| Revenue split (fictional) | Specialty Chemicals about $11.4 billion (about $31.2 million per day); Distribution about $5.6 billion from third parties (about $15.3 million per day); Hazmat Transport about $1.0 billion from third parties (about $2.7 million per day), plus about $0.7 billion of intercompany revenue eliminated in consolidation (FY2025, EV-003) |
| Plant C1 scale | About 1,150 employees. About 900 tons a day of sodium hypochlorite and blended products; about 140 outbound truckloads a day. About 60% of sodium hypochlorite goes to drinking water and wastewater utilities in the Southeast, which typically hold 7 to 14 days of supply (EV-002, EV-054, EV-088) |
| Terminal T1 details | 42 tanks (about 38 million gallons) for caustic soda, sulfuric acid, glycols, and Class 3 solvents; 2 ship berths and 1 barge dock. It transfers hazardous materials in bulk to and from vessels of 250 barrels or more, so 33 CFR Part 154 applies and, through 33 CFR 105.105(a)(1), so do Part 105 and USCG Subpart F (101.605(a)). About 140 employees and about 60 regular contractor personnel (EV-071) |
| Hazmat security plans | Specialty Chemicals and Distribution offer large bulk quantities of 50% hydrogen peroxide (Division 5.1, PG II) and Class 3 PG II solvents (172.800(b)(6) and (b)(10)); Hazmat Transport transports them. Each division keeps its own plan with its own senior official (EV-069, EV-077, EV-082) |
| Hazmat Transport details | About 2,700 drivers; electronic shipping papers on driver tablets with paper printouts at every pickup; the Group ERC number is on all group shipping papers. 28 terminals; ELD support personnel at each terminal (EV-081, EV-086) |
| Managed inventory customers | About 2,600 customer sites, of which about 640 are drinking water or wastewater utilities. The 12 largest customers asked for a SOC 2 Type 2 report by the end of 2027 (EV-078, EV-079) |
| Cloud | Provider A hosts the corporate landing zone, SYS-G6, SYS-C9, SYS-D3, SYS-T1, and SYS-G4 integration services. Provider B hosts disaster recovery replicas and the immutable backup vault. SYS-C1 to SYS-C5, SYS-C8, SYS-D1, and SYS-D2 are on premises (EV-020) |
| Cyber insurance | Group cyber insurance tower with a breach hotline and a panel of forensic firms and breach counsel (EV-038) |
| P07 new finding | Default vendor passwords on 4 tank gauging interface units at Terminal T1, reachable from the terminal office network (found 2026-08-19; changed 2026-09-10) (P07; EV-D-IA5) |
| AI (P10) | AI-001 was switched back to advisory mode on 2026-09-03. Inventory also lists predictive maintenance for rotating equipment, a generative formulation assistant, an SDS authoring assistant, demand forecasting for the managed inventory service, route and load optimization, driver-facing camera AI, an enterprise generative AI assistant piloted with 3,000 users, and a SOC triage assistant (EV-030, EV-105) |
| P08 exercise scenario | Ransomware stole HR and driver qualification exports covering about 7,400 current and former drivers and employees in 41 states (about 1,900 in Florida). Counts are illustrative |
| Additional roles | Group identity, SOC, cloud platform, and data platform directors; Distribution warehouse operations director; Hazmat Transport dispatch director; Plant C1 shift superintendents |
| OT scale (P02, P07) | Plant C1 OT inventory: 412 devices; about 96 operators and shift superintendents; 3 integrator teams support Plant C1. The gateway serves 17 sites (16 plants and Terminal T1) and had 31 integrator team accounts at fieldwork. Terminal T1 OT inventory: 312 devices from 7 OT vendors (EV-055, EV-056, EV-015, EV-C-AC2, EV-074) |
| Shipping volumes (P05) | About 1,100 loaded group hazmat movements a day; Terminal T1 loads about 220 trucks and 15 railcars a day (EV-081, EV-070) |
| Plant C1 RMP records (P03) | Operating procedures certified 2026-03-15; LEPC and county coordination meeting 2026-03-11; field exercise evaluation report 2025-12-19; screening (2026-06) found no other NAICS 324 or 325 stationary source with a covered process within 1 mile; the RMP tabletop (due before 2026-12-21) is combined with the group cyber tabletop on 2026-12-08 (EV-050, EV-053, EV-100, EV-102) |
| Hazmat Transport geography (P03, P10) | Terminals and domiciled drivers include Illinois and Colorado; about 110 drivers live in California. TMS dispatch accounts at 4 terminals lacked MFA until 2026-03 (EV-002, EV-083) |
| Managed inventory service (P09) | About 160 Distribution staff run the service; the telemetry vendor portal has 11 named users. Target: SOC 2 Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 (EV-078) |
| AI-001 timeline (P10) | Automatic setpoint writes ran from 2026-06-08 to 2026-09-03 (about 14,200 writes, all inside the bounded ranges) (EV-099, EV-105) |
| Assessment details (P07) | Legacy plant passive tests 2026-07-21 and 2026-07-23; 2 KEVs on Terminal T1 management servers were open 47 days; owners were named for all 38 notification matrix rows on 2026-09-15 (EV-S-SC7, EV-C-RA5, EV-C-IR6; P08) |
| More roles | Group ERP director, group procurement director, group internal audit director, group HR director, group communications lead, group workplace technology director, group product stewardship director, group chief accounting officer; Specialty Chemicals quality director, reliability director, and Transportation Security Coordinator; Hazmat Transport finance director; Distribution security and compliance lead |

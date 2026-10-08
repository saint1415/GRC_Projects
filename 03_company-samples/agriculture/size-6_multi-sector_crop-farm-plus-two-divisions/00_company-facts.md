# Scenario facts: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Multi-Sector

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given and was read on the eCFR (current through 2026-09-23) or the Federal Register.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; holding company of three operating subsidiaries) |
| Structure | A holding company with three divisions, each a separate operating subsidiary, plus corporate shared services in the parent |
| Division 1: Crop Farming (NAICS 111998), **focus of this scenario** | Diversified precision-agriculture crop farming on about 240,000 farmed acres (owned and leased) at 38 farm operations in 5 southeastern states. Crops in rotation: strawberries, tomatoes, peppers, cucumbers, leafy greens, sweet corn, green beans, watermelons, peanuts, and cotton, with no single crop family a majority of crop value. Connected irrigation, fertigation, GNSS-guided equipment, imaging and spray drones, and an enterprise farm management platform. About 19,000 employees at seasonal peak |
| Division 2: Food Processing and Packing (NAICS 311411, 311991, 311911; sector 31-33 Manufacturing) | 11 FDA-registered food facilities: 4 fresh-cut produce plants, 2 frozen vegetable plants, 1 peanut processing plant (shelling, roasting, peanut butter), and 4 regional packinghouses. Buys about 40% of its produce and peanuts from Crop Farming and the rest from about 260 outside growers. Sells to retail grocery chains, foodservice distributors, and USDA commodity programs. About 17,000 employees |
| Division 3: Farm Supply Wholesale (NAICS 424910; sector 42 Wholesale Trade) | Seed, fertilizer, crop protection products, irrigation parts, and precision-ag hardware through 120 branches, 4 distribution centers, and 2 liquid fertilizer blending plants in 7 southeastern states. About 31,000 customer accounts, including Crop Farming. Operates the **Grower Agronomy Portal** (SYS-D5), a service offered to growers and to cooperatives that resell it. About 5,500 employees |
| Corporate shared services | Identity, security operations, cloud and network, ERP and HR, finance, legal, and internal audit. About 3,500 employees |
| Location | Headquartered in Florida. Operations in 7 southeastern states (Crop Farming in 5 of them). **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees at seasonal peak; about $18.0 billion revenue (fictional, consolidated, after intercompany eliminations) |
| Which rules apply | Decided for each division and the group in the intake [obligations register](step-00_P00_intake/obligations-register.csv): the FSMA food defense rule (N11-R01) binds the 11 Food Processing facilities and not the farms; Produce Safety, H-2A and Worker Protection Standard record rules bind Crop Farming; PCI DSS (contract) and FTC Act Section 5 (N42-R01) bind Farm Supply; SEC disclosure (N42-R07) binds the group |
| Not in scope | Decided in the same register: DFARS and CMMC (no DoD contracts), the FTC Safeguards Rule (grower credit is business credit), California privacy law (no California customers or operations), records access under 21 CFR Part 1 Subpart J at farms, and CIRCIA (proposed only) |
| Why these divisions | Vertical integration from field to packed product to farm inputs: Farm Supply sells inputs to Crop Farming and outside growers; Crop Farming sells produce and peanuts to Food Processing and outside buyers |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks |
| Group CISO; Group Chief Risk Officer | Group program, group standards, group risk register, common controls; co-accept High risks |
| Group Chief Privacy Officer; Group General Counsel | Personal information handling across divisions; contracts; notification matrix |
| Group VP Food Safety and Quality | Group food safety and food defense standards; coordinates FDA matters across Crop Farming and Food Processing |
| Division presidents (3) | Accept Moderate risks for their division |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators and customers |
| Crop Farming VP Irrigation and Field Technology | System owner of the FMICP (P02) |
| Crop Farming OT security manager; Food Processing plant OT security manager | Division OT security (SP 800-82 Rev. 3) |
| Crop Farming Director of Food Safety; Crop Farming labor compliance director | Produce Safety records; H-2A program records |
| Food Processing VP Food Safety and Quality | Food safety plans (21 CFR 117) and food defense plans (21 CFR 121) at the 11 facilities; preventive controls and food defense qualified individuals report to this role |
| Group internal audit | Assesses common controls once and samples division controls; co-sources an independent OT assessment firm |
| Disclosure committee | SEC materiality decisions |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in the [vendor register](step-00_P00_intake/vendor-register.csv).

| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, PAM, identity governance) | Corporate |
| SYS-G2 | Group SOC: SIEM, EDR, and passive OT network monitoring | Corporate |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic), group WAN and site networks, and the group data platform | Corporate |
| SYS-G4 | Group ERP (finance, order-to-cash, procure-to-pay) on cloud IaaS, and the HR and payroll SaaS | Corporate |
| SYS-D1 | Farm Management and Irrigation Control Platform (FMICP) | Crop Farming |
| SYS-D2 | Connected equipment, GNSS guidance, and drone fleet (equipment telematics portals, RTK base stations, drone fleet management, spray drones) | Crop Farming |
| SYS-D3 | Plant systems: manufacturing execution, plant OT (wash, sorting, blanching, freezing, roasting, and packaging lines; ammonia refrigeration controls), quality and food safety records, food defense plan repository, traceability, and warehouse management | Food Processing |
| SYS-D4 | Branch and distribution systems: branch ordering and point of sale (the card data environment), e-commerce ordering, distribution center warehouse management, blending plant controllers | Farm Supply |
| SYS-D5 | Grower Agronomy Portal (multi-tenant service for growers and reselling cooperatives) | Farm Supply |

**SSP system (P02):** the *Farm Management and Irrigation Control Platform (FMICP)*: SYS-D1, the Crop Farming division's enterprise farm management tenant (vendor SaaS) with its irrigation control module, the 3 regional irrigation operations centers and their SCADA, the field OT at 38 farms, the farm data hub and imagery store on the group cloud, and its interfaces to SYS-D2, SYS-D3 (harvest lot feed), and SYS-G4 (payroll tally feed); it inherits common controls from SYS-G1 to SYS-G4.

**FMICP components:**
- **FMIS tenant (vendor SaaS):** crop plans, field and pesticide application records, Produce Safety records, harvest tally and labor records (part of the H-2A earnings records), harvest lot records, yield maps, and the irrigation control module (schedules, setpoints, remote commands). The vendor's SOC 2 Type 2 report states an RTO of 8 hours and an RPO of 1 hour (EV-078)
- **Regional irrigation operations centers (ROC-1 to ROC-3):** SCADA servers and HMI workstations in an OT network at each center, staffed 24x7 during freeze season. ROC-1 serves the Florida farms, including all strawberries
- **Field OT at 38 farms:** about 1,150 center-pivot panels (cellular modems on a carrier private network), about 410 well pumps with variable-frequency drives, 96 fertigation injection systems, about 6,800 drip-zone valve controllers, overhead freeze protection on about 4,200 acres of strawberries, about 21,000 soil moisture probes, about 260 LoRaWAN gateways, 140 weather stations, and temperature monitoring for packing sheds and field coolers at 22 farms. About 38,000 OT and IoT devices in total (EV-043)
- **Farm data hub (provider A):** a historian that collects telemetry from the ROC SCADA through an OT DMZ, syncs to the FMIS, sends harvest lot files to Food Processing nightly, and sends payroll tally exports to SYS-G4
- **Imagery store (provider A):** drone orthomosaics for the yield model (P10 AI-001)
- **Harvest tablets:** about 3,400 rugged tablets running the FMIS mobile app

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Rows are grouped by division (Group, Crop Farming, Food Processing, Farm Supply). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** to each division and to the group is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps** against the CSF 2.0 benchmark, the farm record rules, the FDA food rules, PCI DSS and the group's disclosure and notice duties are judged in the gap analyses (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | The Crop Farming FMICP (focus division system), inheriting group common controls; plus the group common control catalog |
| P03 | Crop Farming: NIST CSF 2.0 (all 106 subcategories, with SP 800-82 Rev. 3 for OT) plus the binding farm record rules. Food Processing: FDA food defense (21 CFR 121, N11-R01), food safety records (21 CFR 117 Subpart F), records access (21 CFR Part 1 Subpart J), the Food Traceability Rule (pending enforcement), and USDA contract clauses. Farm Supply: PCI DSS (contract) and FTC Act Section 5 (N42-R01). Group: SEC (N42-R07) and state breach laws. A regulation-by-division matrix ties them together |
| P08 | Ransomware that enters through the irrigation integrator's remote access at an acquired farm, encrypts the ROC SCADA, the farm data hub, and ERP application servers, and steals payroll and H-2A files and Farm Supply grower credit files. One multi-regulator notification matrix across the three divisions and the SEC |
| P09 | SOC 2 scoped per division: the Grower Agronomy Portal is in scope as a true service organization; Crop Farming and Food Processing are out of scope, with reasons; review of the FMIS vendor's SOC 2 report |
| P10 | Group AI governance program, with the computer-vision crop yield prediction model (AI-001) as the priority use case |
| Cloud | Shared corporate platform on two providers plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-04-06 to 2026-04-28 | Intake: evidence requests, exports, walk-throughs, inventories, obligations register, grouped by division |
| 2026-05-01 to 2026-07-31 | BIA interviews (May), group and division risk analyses (June) and gap analyses (June and July) (off-season for Florida strawberries; no freeze risk) |
| 2026-06-01 to 2026-06-26 | Group policies v2026 drafted from the gaps found so far (P06); the Food Processing supplement was aligned to the drafts on 2026-06-30 |
| 2026-07-01 to 2026-08-31 | Common control assessment (group internal audit with the OT assessment firm) plus division samples: operating tests of controls already in place under the 2024 policies; design review only of the draft v2026 policies. OT testing ran outside irrigation run windows |
| 2026-09-10 | Results to the board risk committee; deliverables and group policies v2026 approved (policies effective 2026-10-01) |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the v2026 policies and the re-issued Crop Farming supplement introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Revenue split (fictional, external) | Food Processing about $10.6 billion; Farm Supply about $4.8 billion; Crop Farming about $2.6 billion external plus about $1.5 billion of intercompany sales to Food Processing (eliminated). Total about $18.0 billion, as in section 1 (EV-003) |
| Crop Farming scale | 24 legacy farms and 14 farms acquired in 2024 (the "2024 acquired farms"). About 7,500 year-round employees and about 11,500 seasonal workers at peak, of whom about 9,000 are H-2A workers (season about October to June). Strawberry crop value about $310 million a season. Each farm operation is a "farm" under 21 CFR 1.227 and a covered farm under the Produce Safety Rule (21 CFR 112.4(a)); farms do not register with FDA (21 CFR 1.226(b)). Applicability is recorded in the obligations register (N11-R01-CF, CF-R112) (EV-002, EV-034) |
| Crop Farming buyers | About 60% of crop value goes to outside buyers (retail chains, wholesale distributors, peanut shellers). Buyer agreements require notice within 24 hours of any event that could affect product safety, lot traceability, or committed volumes (EV-049) |
| Irrigation support | Legacy farms: the division's own OT team. 2024 acquired farms: a regional irrigation integrator under a time-and-materials agreement without security terms (EV-036) |
| H-2A records | Field tally and hours offered are kept in the FMIS. H-2A workers' passport numbers, visa data, and home-country addresses are kept in the HR and payroll SaaS (SYS-G4). An outside H-2A filing agent receives exports. The farm data hub stages payroll tally exports and, until this assessment, also held copies of H-2A onboarding exports (EV-025, EV-045, EV-083; P01 CF-009) |
| Food Processing facilities | The 4 packinghouses pack and cool produce from group farms and outside growers. Outside growers supply the majority of their volume, so they are not secondary activities farms under 21 CFR 1.227 and they register as food facilities. Group counsel's 2024 review applies 21 CFR Part 121 to all 11 facilities; the packinghouses' written vulnerability assessments found no actionable process steps (explained as 121.130(c) requires), and the 7 processing plants each have actionable process steps and mitigation strategies (EV-056, EV-057). Applicability is recorded in the obligations register (N11-R01-FP) |
| Food Processing OT | The 2 frozen vegetable plants use anhydrous ammonia refrigeration (about 48,000 lb and 61,000 lb), above the 10,000 lb threshold in 40 CFR 68.130 and 29 CFR 1910.119 Appendix A, so EPA RMP and OSHA PSM apply (obligations register FP-PSM). Refrigeration controls are supported remotely by the refrigeration contractor through group PAM (EV-061) |
| Food Processing federal contracts | Frozen vegetables and peanut butter are sold to USDA commodity programs under contracts whose files include FAR 52.204-21, 52.204-23, and 52.204-25. No DoD contracts and no covered defense information (EV-064, EV-031) |
| Food Processing customers | Retail and foodservice customer agreements require notice within 24 hours of an event that could affect product safety or supply, and annual third-party food safety certification audits (EV-065) |
| Farm Supply scale | 120 branches, 4 distribution centers, 2 liquid fertilizer blending plants. About 31,000 customer accounts; about 12,000 are individual growers whose trade credit applications include Social Security numbers and personal guarantees. Card payments at branch counters and on the e-commerce ordering site. The division does not store anhydrous ammonia or ammonium nitrate. No federal contracts. No customers or operations in California (EV-068, EV-031) |
| Grower Agronomy Portal (SYS-D5) | Multi-tenant service on cloud provider B: field boundaries, soil tests, yield maps, variable-rate prescriptions, application records, and grower contact data for about 8,200 grower accounts. 22 cooperatives and independent ag retailers resell it under their own brand to about 5,400 of those growers. The AI variable-rate prescription feature launched 2026-03-01. The portal terms (2025) commit to notify reselling cooperatives of a security incident affecting their growers' data within 72 hours, and to use grower data only to provide the service (EV-069, EV-070) |
| Cloud | Provider A (primary): corporate landing zone, group data platform, SYS-G4 ERP application and database servers (IaaS), the farm data hub and imagery store, the Food Processing traceability system, and Farm Supply e-commerce and order management. Provider B: Grower Agronomy Portal production, the disaster recovery replica, and the immutable backup vault. The FMIS and the HR and payroll system are vendor SaaS. ROC SCADA and plant MES and OT run on premises (EV-019) |
| Legacy farm directory | The ROC SCADA servers and HMIs at all 3 centers, and the 2024 acquired farms' servers, are joined to an on-premises "farm operations" directory that predates SYS-G1. Its domain administrators are not in group PAM (EV-038) |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Worker-safety and food-safety risks rated High must be treated, not accepted (EV-016) |
| Regulatory driver labels | N11-R01 applies to the 11 Food Processing facilities only, so `regulatory_driver` columns cite it there with the section (for example "N11-R01 (21 CFR 121.130(a))"). For Crop Farming, which has no binding cybersecurity rule, they cite the benchmark as "CSF 2.0 <subcategory> (benchmark)", the OT guide as "SP 800-82r3 <section>", and binding rules by their own citation (21 CFR 112, 20 CFR 655.122, 40 CFR 170.311, Fla. Stat. 501.171 as the worked example). Group and Farm Supply rows use the wholesale-trade IDs N42-R01 (FTC Act Section 5), N42-R04 and N42-R05 (FAR clauses in Food Processing USDA contracts), and N42-R07 (SEC disclosure) |
| Crop Farming identities (2026 fieldwork) | About 2,600 named FMIS and OT users plus about 3,400 harvest tablets. 11 farm operations directory domain administrators, none in group PAM or with MFA. About 1,140 seasonal FMIS accounts from the 2025-26 season still active in July 2026. Default credentials on 11 of 60 sampled pivot panel modems (18%) and 4 of 20 sampled LoRaWAN gateways. Entries keyed after the fact from paper at 9 farms where tablets lose signal (EV-039, EV-040, EV-085; P07 testing: EV-C-AC6(5), EV-C-AC2, EV-C-IA5) |
| Interim measure for CF-001 | Approved by the board risk committee on 2026-09-10: from 2026-09-14 the integrator remote tool at each acquired farm is switched off and turned on only for windows the ROC lead approves, until group PAM replaces it (POAM-001, due 2026-11-15) (EV-095) |
| Supplements and AI standard | The Crop Farming policy supplement v2023 lacked OT remote access, OT change, and seasonal account rules (EV-017); re-issued as v2026-09. Farm Supply supplement amended 2026-09 with a portal release gate. The Group AI Standard and the Group AI council were established in 2026-06. AI-001 is built in-house by the group data science team; the AI inventory lists 10 use cases (P10) |
| Food Processing details | 9 lines at 3 plants use shared HMI operator logins (EV-090, EV-P-CM5). The food defense plan repository was readable by 140 plant staff (to be restricted to 38) (EV-057). Plant MES runs in its own domain, with no trust to the Crop Farming farm operations directory; it still trusts the plant IT domain (EV-060; P01 FP-004). Food defense awareness training is given at hire to all line staff, including seasonal staff (EV-023) |
| Farm Supply details | The grower credit file share (provider A) was readable by 340 finance and branch manager accounts; about 45 credit staff need access (EV-092, EV-S-AC6). MFA is optional for cooperative administrators of the portal (EV-069). The FMIS vendor's 2025 contract renewal requires notice within 72 hours of confirming an incident affecting group data (EV-050) |

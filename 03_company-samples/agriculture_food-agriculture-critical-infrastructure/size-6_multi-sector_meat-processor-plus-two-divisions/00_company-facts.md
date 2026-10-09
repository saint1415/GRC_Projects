# Scenario facts: Cris Santos Company | Food and Agriculture | Multi-Sector

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or agency publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23), govinfo.gov, federalregister.gov, and fda.gov between 2026-09-26 and 2026-10-04.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; a holding company with three operating divisions) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a wholly owned operating subsidiary |
| Division 1: Meat Processing (NAICS 311612), **focus of this scenario** | Further processing of purchased beef and pork carcasses and primals at **six plants** (no slaughter): bacon, hams, smoked sausage, fresh sausage, deli meats, cooked meats for food service, and marinated and case-ready cuts, under the group's brands and as private label. About 14,000 employees. Every plant is an FSIS **official establishment** under a federal grant of inspection (Federal Meat Inspection Act), decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (FSIS-417-MP). Plants 2 and 5 were acquired in 2024 |
| Division 2: Food Distribution (NAICS 424410, sector 42 Wholesale Trade) | General-line grocery wholesale from **five distribution centers (DCs)** with ambient, refrigerated, and frozen storage; a private fleet of about 450 tractors and 900 refrigerated trailers. Supplies the group's own stores, about 2,800 independent grocers and food service customers, and runs a **third-party cold storage and logistics (3PL) service** for about 60 external food brands at DC-1 and DC-3. About 7,000 employees |
| Division 3: Grocery Retail (NAICS 445110, sector 44-45 Retail Trade) | **120 supermarkets** with in-store meat counters (cutting and grinding), deli, and bakery; online ordering with store pickup and delivery; a loyalty program with about 6.5 million members. Accepts payment cards in stores and online. No in-store pharmacies. About 21,000 employees |
| Corporate shared services | Identity, network, security operations, cloud and data platform, group ERP, OT security services, HR, finance, legal, and internal audit. About 3,000 employees |
| Location | Headquartered in Florida. The six plants, five DCs, and 120 stores are in **five southeastern states**. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional): Meat Processing about $7.0 billion (external sales; intercompany sales to Food Distribution are eliminated), Food Distribution about $5.0 billion, Grocery Retail about $6.0 billion |
| SBA size status | Not small. SBA standards (13 CFR 121.201): 1,000 employees for NAICS 311612; 250 employees for NAICS 424410; $40.0 million receipts for NAICS 445110. Each division exceeds its standard |
| Why these divisions | The processor also distributes and sells its own products: about 30% of Meat Processing volume moves through the group's DCs, and about 40% of the stores' fresh and deli meat comes from the group's plants. One supply chain, three regulators' views of it |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Security, food safety, and compliance duties |
|---|---|
| Board risk committee | Group cyber and food safety risk oversight; accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC disclosure controls |
| Group CISO | Group security program and group policies; operates common controls (SYS-G1 to SYS-G5); co-accepts High risks |
| Group Chief Risk Officer | Group risk register and enterprise risk management (ERM) roll-up; co-accepts High risks; chairs the Group AI council |
| Group Chief Food Safety and Quality Officer | Group food safety standards; final call on product holds, recalls, and regulator notifications that cross divisions |
| Group General Counsel | Contracts, the multi-regulator notification matrix, and approval of every external notice |
| Group Chief Privacy Officer | Consumer and employee personal information, loyalty program data, data classification |
| Group OT security director (reports to the Group CISO) | Group OT security standard; OT remote access gateway and OT monitoring service (SYS-G5) |
| Division security and compliance leads (3) | Division risk registers, division supplements, division regulators; accept Low risks |
| Division presidents (3) | Accept Moderate risks for their division |
| Meat Processing: Division VP Food Safety and Quality Assurance (FSQA) | Division HACCP, Sanitation SOP, recall, and food defense program |
| Meat Processing: plant managers (6) | "Responsible establishment official" who signs each plant's HACCP plans (9 CFR 417.2(d)). The Plant 6 plant manager is also the "owner, operator, or agent in charge" who signs and dates the FDA food defense plan (21 CFR 121.310) |
| Meat Processing: plant FSQA managers (6) | HACCP coordinators trained under 9 CFR 417.7. The Plant 6 FSQA manager is the **Food Defense Coordinator and qualified individual** for the vulnerability assessment and plan (21 CFR 121.4(c)) |
| Meat Processing: division controls engineering manager; plant controls engineers | PLCs, HMIs, SCADA, historians, MES, and the central recipe master library |
| Meat Processing: plant refrigeration managers | Ammonia refrigeration and process safety management (PSM) programs |
| Food Distribution: division food safety manager | Sanitary transportation procedures; preventive controls qualified individual for refrigerated storage (21 CFR 117.206); FSIS registration and records |
| Food Distribution: fleet director; DC general managers (5); 3PL services director | Fleet and trailer telematics; DC operations; 3PL customer commitments |
| Grocery Retail: payments security manager | PCI DSS program owner; acquirer and Qualified Security Assessor (QSA) contact |
| Grocery Retail: retail food safety director; digital commerce director | Store food safety (including grinding records); online ordering, mobile app, and loyalty program |
| Group internal audit (reports to the board audit committee) | Independent assessor. Assesses common controls once and samples division controls (P07). Designs and operates no controls |
| Disclosure committee | SEC materiality decisions for cybersecurity incidents |
| External parties | Two public cloud providers; group ERP SaaS vendor; cold-chain monitoring SaaS vendor; WMS and TMS SaaS vendors; controls integrators (Plants 2 and 5 use one under a legacy contract); refrigeration contractors; AI vision inspection vendor; payment processor and acquirer; QSA firm; e-commerce and loyalty platform vendors; forensic firm on retainer through the cyber insurer's panel |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in the [vendor register](step-00_P00_intake/vendor-register.csv). Where a note below describes the state of a system, it cites the intake evidence that shows it.

| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform: corporate directory (domain controllers in the group colocation data center and at each plant and DC), cloud single sign-on, MFA, privileged access management (PAM), identity governance | Corporate | All 45,000 workforce users. **OT servers at Plants 2 and 5 and the DC automation servers are joined to the corporate directory domain** (the other four plants run a separate OT domain) (EV-010) |
| SYS-G2 | Group SOC, SIEM, and EDR | Corporate | 24x7 SOC. EDR on all IT servers and endpoints and on OT Windows hosts at Plants 1, 3, 4, and 6 (EV-011) |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic) and data platform | Corporate | Provider A: corporate landing zone, group data platform, food safety records application, central recipe master library, 3PL customer portal. Provider B: e-commerce and loyalty platform, DR replicas, and the immutable backup vault |
| SYS-G4 | Group ERP (SaaS) | Corporate | Finance, procurement, order-to-cash, and production orders for all divisions |
| SYS-G5 | Group OT security services: OT remote access gateway with MFA and session recording, plus passive OT network monitoring | Corporate (Group OT security director) | Program started 2025. **Deployed at Plants 1, 3, 4, and 6 and at DC-1 and DC-3; not yet at Plants 2 and 5 or DC-2, DC-4, DC-5** (EV-023) |
| SYS-G6 | Group cold-chain monitoring platform: vendor SaaS with wireless sensors and gateways in plant coolers and freezers, DC rooms, refrigerated trailers (through trailer telematics), and store display cases and walk-in coolers | Corporate service; used by all three divisions | About 21,000 sensors. Alerts go to each site's on-call roles by SMS and app push through a **cold-chain alert integration server** in the colocation data center (EV-025) |
| SYS-M1 | Plant process control networks (PLCs, HMIs, brine and cure dosing skids, smokehouse and oven controllers, clean-in-place (CIP) manifolds, chilling, slicing, packaging, metal detectors, checkweighers) | Meat Processing | Six plants, about 2,100 OT devices and 310 HMIs. 24 HMIs at Plants 2 and 5 run an unsupported operating system (EV-045) |
| SYS-M2 | Plant SCADA servers, process historians, and engineering workstations | Meat Processing | Collect CCP data (cook, chill, cold storage temperatures). **Historian audit trails are disabled at Plants 2 and 5** (EV-047) |
| SYS-M3 | Plant MES (recipe, batch, lot coding) with the central recipe master library on SYS-G3 | Meat Processing | Named MES accounts with two-person formulation approval at Plants 1, 3, 4, and 6 since 2025; **shared operator logins remain at Plants 2 and 5**. HMIs at all six plants use shared operator logins (EV-046) |
| SYS-M4 | Ammonia refrigeration control systems | Meat Processing | Five plants hold more than 10,000 lb of anhydrous ammonia (threshold quantity in 29 CFR 1910.119 Appendix A and 40 CFR 68.130); Plant 4 uses a low-charge packaged system below the threshold. A refrigeration contractor keeps an always-on cellular modem on the Plant 5 controller (EV-051, EV-053) |
| SYS-M5 | Food safety records application (electronic HACCP and Sanitation SOP records, food defense monitoring records, pre-shipment review) | Meat Processing (hosted on SYS-G3) | Used by all six plants |
| SYS-M6 | AI vision inspection on packaging lines | Meat Processing | In production on 7 lines at Plants 1, 3, and 4 since 2025; pilot on 2 lines at Plant 6 since 2026-05. Edge inference servers on the control networks; vendor cloud for model training (EV-037, EV-058, EV-100) |
| SYS-D1 | Warehouse management system (WMS, SaaS) and DC automation (conveyors, sortation, and automated freezer storage at DC-1 and DC-3) | Food Distribution | DC automation servers are joined to the corporate directory domain (EV-010, EV-064) |
| SYS-D2 | Transportation management system (TMS, SaaS) and trailer telematics | Food Distribution | Telematics report reefer setpoints and temperatures to SYS-G6 |
| SYS-D3 | 3PL customer portal and EDI | Food Distribution (hosted on SYS-G3, provider A) | Inventory visibility, orders, and temperature history for about 60 external brands |
| SYS-R1 | Store point-of-sale (POS) and payment environment (the cardholder data environment, CDE) | Grocery Retail | 1,450 lanes and self-checkouts. A validated point-to-point encryption (P2PE) solution is live in 90 stores; **30 stores still run older terminals outside P2PE** (replacement due 2027-03-31) (EV-073) |
| SYS-R2 | E-commerce, mobile app, and loyalty platform | Grocery Retail (hosted on SYS-G3, provider B) | Online payment through the payment processor's hosted payment fields; about 6.5 million loyalty members (name, email, phone, address, purchase history) |
| SYS-R3 | Store systems: store servers, in-store networks and Wi-Fi, CCTV, scales, meat-counter grinding logs, and refrigerated case controllers connected to SYS-G6 | Grocery Retail | |

**SSP system (P02):** the *Plant Production and Cold-Chain Monitoring System (PPCM)*: the Meat Processing division's process control networks, SCADA and historians, MES, and ammonia refrigeration controls at all six plants (SYS-M1 to SYS-M4), the food safety records application (SYS-M5), and the plant tier of the group cold-chain monitoring platform (SYS-G6), inheriting common controls from SYS-G1, SYS-G2, SYS-G3, and SYS-G5.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Rows are grouped by division (Group, Meat Processing, Food Distribution, Grocery Retail). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** to each division and to the group is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps** against Part 121, the FSIS HACCP and recall rules, the FDA storage and transportation rules, PCI DSS, and the CSF 2.0 benchmark are judged in the gap analyses (P03), which also number the nine group gaps cited across this sample, and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 SSP | The PPCM (Meat Processing, all six plants), with a group common control catalog inherited by all three divisions |
| P03 regulation | Regulation-by-division matrix. Meat Processing: FSMA Intentional Adulteration rule, 21 CFR Part 121 (applies to Plant 6, the one FDA-registered plant) with FSIS HACCP and recall rules (9 CFR 417, 418) for electronic CCP records and an OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3, voluntary). Food Distribution: FDA refrigerated storage and sanitary transportation rules (21 CFR 117.206; 21 CFR 1.900-1.912), FSIS registration and records (9 CFR 320.1, 320.5), and the Food Traceability Rule (enforcement not before 2028-07-20). Grocery Retail: PCI DSS v4.0.1 (contractual) with FACTA receipt truncation and grinding records. Group: SEC disclosure and state breach laws |
| P04 cloud | Shared corporate cloud platform (providers A and B) plus division workloads; OT stays on premises behind SYS-G5. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| P05 BIA | Group and division BIAs in one workbook with cross-division dependencies |
| P07 assessment | Common controls assessed once by group internal audit; division samples (OT testing at Plants 2, 5, and 6 during weekend sanitation windows) |
| P08 incident | Ransomware through a shared service (the corporate directory) halting processing lines and cold-chain monitoring across divisions, with employee data theft |
| P09 SOC 2 | Scoped per division: the Food Distribution 3PL service is in scope as a true service organization; Meat Processing and Grocery Retail are not service organizations (Retail's assurance is its PCI DSS ROC); plus a group review of the cold-chain monitoring vendor's SOC 2 report |
| P10 AI | Group AI governance program; priority use case AI-001 AI vision inspection on processing lines (Meat Processing) |

**Registry defaults kept, and why.** The registry's primary system ("Plant production and cold-chain monitoring system"), incident ("Ransomware halting processing lines and cold-chain monitoring"), and AI use case ("AI quality inspection on processing lines") all fit the focus division at this size. Two adaptations: the system becomes a six-plant system that inherits group common controls, and the incident starts in a shared group service so that it spans all three divisions, which is what a Multi-Sector runbook must show.

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-03-30 to 2026-04-24 | Intake: evidence requests, exports, inventories, obligations register, grouped by division |
| 2026-05-04 to 2026-07-31 | Group and division BIAs (May), risk analyses (June), and gap analyses (from 2026-06-29; plant walkthroughs at all six plants; DC-1 and DC-3; 8 stores) |
| 2026-06-01 to 2026-06-26 | Group policies v2026 drafted from the gaps found so far (P06); the Grocery Retail supplement was aligned to the drafts in 2026-06 |
| 2026-07-06 to 2026-08-28 | Common control assessment by group internal audit plus division samples: operating tests of controls already in place under the 2025 group policies; design review only of the draft v2026 policies and the draft notification matrix (OT testing at Plants 2, 5, and 6 during weekend sanitation windows, 2026-08-08 to 2026-08-23) |
| 2026-08-31 | SOC 2 readiness (3PL service) and cold-chain vendor report review completed |
| 2026-09-02 | Group AI council risk assessment completed |
| 2026-09-15 | Results to the board risk committee; deliverables and group policies v2026 approved (policies effective 2026-10-01) |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the v2026 policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Plants | Plant 1 (Florida, flagship): bacon, hams, smoked sausage, deli meats; about 3,000 employees. Plant 2 (acquired 2024): fresh sausage and ground products; about 2,200. Plant 3: cooked meats for food service; about 2,600. Plant 4: marinated and case-ready cuts; about 2,400. Plant 5 (acquired 2024): smoked sausage and meat snack sticks; about 1,800. Plant 6: deli meats plus a **plant-based protein line** opened in 2024; about 2,000. Division staff are counted in their home plant. HACCP plans at each plant cover the 9 CFR 417.2(b)(1) categories the plant produces (EV-042, EV-002) |
| FDA status by site | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (FDA-REG-MP, FDA-REG-FD, FDA-REG-GR). **Plant 6 is a registered food facility** (FD&C Act section 415; 21 CFR 1.225) because its plant-based line makes FDA-regulated food, so the 21 CFR 1.226(g) exemption ("regulated exclusively, throughout the entire facility" by USDA) does not apply. Plants 1 to 5 are regulated exclusively by FSIS and are not registered. The **five DCs are registered** because they hold FDA-regulated food. Stores are retail food establishments, which do not register (21 CFR 1.226(c)) |
| Part 121 at the DCs | Decided in the obligations register (C-FOOD-AG-R01-FD). The DCs only hold food in packaged form and have no liquid storage tanks, so Part 121 does not apply to them (21 CFR 121.5(b)) |
| FSIS status of the DCs | Decided in the obligations register (FSIS-320-FD). Food Distribution is a wholesaler of meat products and is registered with FSIS under 9 CFR 320.5; it keeps the transaction records in 9 CFR 320.1(b)(1) |
| Ammonia | Plants 1, 2, 3, 5, and 6 each hold more than 10,000 lb of anhydrous ammonia (about 38,000, 22,000, 30,000, 14,000, and 26,000 lb). DC-1 and DC-3 freezers also use ammonia above the threshold. PSM (29 CFR 1910.119) and RMP (40 CFR Part 68) are managed by site PSM programs and are context only in this sample (EV-053; obligations register PSM-RMP) |
| Grocery Retail payments | The acquirer requires an annual ROC by a QSA (contractual). Online payments use the processor's hosted payment fields embedded in the checkout page. The co-branded credit card is issued by a partner bank; the division does not extend credit itself (EV-070, EV-074, EV-004) |
| Out of scope by fact | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv), from group legal's response (EV-004). No federal contracts or subcontracts (FAR and DFARS clauses do not apply); no MTSA-regulated facility (no USCG cyber rule); no business in California (CCPA does not apply); no in-store pharmacies; no child-directed online services; the company has never submitted Protected Critical Infrastructure Information to DHS |
| Cloud | Provider A (primary) hosts the corporate landing zone, the group data platform, SYS-M5, the recipe master library, and SYS-D3. Provider B hosts SYS-R2 and the DR replicas and immutable backup vault for provider A workloads. The group colocation data center hosts domain controllers, the SYS-G5 central gateway, SIEM collectors, and the cold-chain alert integration server (EV-016) |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. High risks that could put adulterated product into commerce must be treated, not accepted (group risk management strategy, EV-034) |
| Cold-chain vendor | The vendor's latest SOC 2 Type 2 report covers 2025-04-01 to 2026-03-31 (Security and Availability), carves out its cloud provider, and lists complementary user entity controls (EV-098) |
| 3PL service | About 60 external brands store refrigerated and frozen product at DC-1 and DC-3 and see inventory, orders, and temperature history in SYS-D3. 14 of them, including two national food manufacturers, asked for a SOC 2 report by the end of 2027 (EV-068) |
| AI use cases (P10 inventory) | Besides AI-001, the inventory lists predictive maintenance on refrigeration compressors (Meat Processing), demand forecasting and replenishment (Food Distribution), route optimization (Food Distribution), store loss-prevention camera analytics (pilot, Grocery Retail), personalized loyalty offers (Grocery Retail), a workforce scheduling optimizer (Grocery Retail), and an enterprise generative AI assistant piloted with 1,500 workforce users. A Group AI Standard and Group AI council were established in 2026. Sources: EV-037 and EV-100 |
| 3PL SOC 2 scope (P09) | Customers asked for Security, Availability, and Processing Integrity (temperature history and inventory records). The about 60 3PL agreements are on four contract versions. Target: Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30. Subservice organizations carved out: cloud providers A and B, the WMS vendor, and the cold-chain monitoring vendor (EV-068) |
| Cold-chain vendor report review (P09) | Reviewed 2026-08-31 by the Group cold-chain services manager with the group third-party risk team. Bridge letter through 2026-06-30. 2 exceptions (late removal of terminated vendor users; one skipped restore test); 6 complementary user entity controls, 4 operating (EV-098) |
| AI use case details (P10) | AI-001 lines: Plant 1 bacon, ham, and deli (3); Plant 3 cooked meats (2); Plant 4 case-ready (2); Plant 6 pilot on one deli line and one plant-based line. AI-002 runs at Plants 1, 3, and 6. AI-005 camera analytics: 12 stores since 2026-04, facial recognition disabled, video in the vendor cloud for 30 days. Use case owners added as roles: Food Distribution supply chain planning director, Grocery Retail asset protection director, Grocery Retail human resources director (EV-037, EV-058, EV-078, EV-100) |

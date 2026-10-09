# Scenario facts: Cris Santos Company | Food and Agriculture | Micro

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute or regulation, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23) and uscode.house.gov.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) |
| Business | Further processing of purchased pork and beef trimmings and primals (NAICS 311612, Meat Processed from Carcasses): fresh sausage, smoked sausage, smoked hams, and beef jerky and snack sticks. No slaughter. Meat and meat food products only; the plant makes no FDA-regulated food |
| Location | Florida. One small plant: a raw processing room with a grinder and a vacuum stuffer with automatic linker (**Line 1**); one programmable two-truck smokehouse for cooking and smoking; a blast chill cooler; a drying room for jerky; two coolers and one freezer; a packaging room with a thermoforming vacuum packaging machine and an inline label printer-applicator (**Line 2**); an office; and a small retail counter at the front. One refrigerated box truck for deliveries |
| Workforce | 7 employees: the owner (General Manager), 1 Office Manager, 1 Production Supervisor, 1 Maintenance and Sanitation Technician, and 3 production workers (one also drives the delivery truck; one also covers the retail counter) (EV-001) |
| Revenue | About $1.1 million a year (fictional), about $4,400 per production day (250 days). The SBA size standard for NAICS 311612 is 1,000 employees (13 CFR 121.201), so the company is SBA-small (EV-039) |
| Customers | About 40 wholesale accounts (independent grocers, butcher shops, and restaurants within about 150 miles, all in Florida), about 75% of sales, delivered by the company truck. The retail counter is about 25%. A 12-store regional grocery chain became a customer in May 2026. No online sales. No federal contracts or subcontracts (EV-040; EV-034) |
| USDA FSIS status | **Official establishment** under a federal grant of inspection (Federal Meat Inspection Act). FSIS inspection program personnel are assigned to the establishment. Three written HACCP plans (9 CFR Part 417) under the 417.2(b)(1) processing categories: raw product, ground (fresh sausage); fully cooked, not shelf stable (smoked sausage, smoked hams); heat treated, shelf stable (jerky, snack sticks). Written Sanitation SOPs (9 CFR 416.11-416.16) and a written recall procedure (9 CFR 418.3) (EV-026; EV-027; EV-029; EV-030) |
| FDA status | **Not registered** with FDA (EV-026), as decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (FDA-REG). Facilities "regulated exclusively, throughout the entire facility" by USDA under the FMIA do not register (21 CFR 1.226(g)). The FSMA Intentional Adulteration rule applies only to facilities required to register (21 CFR 121.1), so it does not apply. The company is also not a "responsible party" under the Reportable Food Registry, which is tied to registration (21 U.S.C. 350f(a)(1)). If the plant ever adds an FDA-regulated product, these answers change (see the Small sample, whose seafood room made it a registered facility) |
| CCPs that depend on systems | **Cooking** (fully cooked products and jerky): the smokehouse controller's product core-probe log, verified by a handheld thermometer reading entered on a floor tablet at the end of each cycle. **Chilling** (stabilization of fully cooked products): a wireless product probe in the blast chill cooler, logged by the cold-chain monitoring service. **Receiving and cold storage** (raw product, ground): cooler temperatures from the cold-chain service plus receiving checks on the tablet. Jerky water activity is tested per lot by an outside laboratory (EV-027; EV-008; EV-006) |
| Refrigeration | Packaged condensing units with a halocarbon refrigerant serve the coolers, freezer, and blast chill cooler. **No anhydrous ammonia.** The 10,000 lb ammonia threshold quantity in OSHA process safety management (29 CFR 1910.119, Appendix A) and EPA risk management program rules (40 CFR 68.130) is therefore not reached (EV-021; EV-037) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): the FSMA Intentional Adulteration rule (C-FOOD-AG-R01), CIRCIA (C-FOOD-AG-R02, proposed only), the USCG MTS cyber rule (C-FOOD-AG-R03), the Reportable Food Registry, OSHA PSM and EPA RMP, SEC rules, FAR 52.204-21 and 52.204-25, and PCII do not apply |
| Payment cards | The retail counter uses a standalone card terminal managed by the payment provider on its own cellular connection. No card numbers touch company systems. PCI DSS obligations are contractual through the acquirer and are not analyzed here (EV-023) |
| Regulatory driver IDs | The vertical registry IDs are used for their applicability decisions, recorded in the obligations register: C-FOOD-AG-R01 (not applicable), C-FOOD-AG-R02 (proposed, tracked), C-FOOD-AG-R03 (not applicable). The binding food safety rules are outside the registry and are cited directly after being read on eCFR: 9 CFR Part 416 (sanitation), Part 417 (HACCP), Part 418 (recalls). NIST CSF 2.0 and SP 800-82 Rev. 3 are the voluntary benchmark for IT and OT controls that no binding rule covers |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice for employee data, Fla. Stat. 501.171) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Security, food safety, and compliance duties |
|---|---|
| Owner and General Manager (Cris Santos) | Approves policies and spending; accepts Moderate risks and approves treatment plans for High risks. The "responsible establishment official" who signs the HACCP plans (9 CFR 417.2(d)) and the individual with overall authority on-site who signs the Sanitation SOPs (416.12(b)) |
| Office Manager | **Security and compliance lead** (designated in writing in 2026): MSP liaison, accounts, vendors, the risk register, policies, and the incident log. Also invoicing, purchasing, payroll, insurance, and customer service |
| Production Supervisor | HACCP coordinator, trained under 9 CFR 417.7; sets smokehouse cycles and formulations; signs the pre-shipment review (417.5(c)); decides product holds; owns the recall procedure with the owner |
| Maintenance and Sanitation Technician | Equipment upkeep and sanitation (pre-operational SSOP); point of contact for the refrigeration contractor and the smokehouse and packaging machine vendors |
| Production workers (3) | Run Lines 1 and 2 and the smokehouse; one drives the delivery truck; one covers the retail counter |
| Managed service provider (MSP) | IT support for the office computers, firewall, Wi-Fi, productivity suite administration, and backup. **The MSP contract excludes the plant equipment** |
| External parties | Smokehouse manufacturer (remote service), packaging machine vendor (also supplies the AI camera module), cold-chain monitoring SaaS vendor, food safety records app vendor, refrigeration contractor, payroll service, card terminal provider, cyber insurer |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in the [vendor register](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Smokehouse controller | On premises (plant network) | Programmable controller on the two-truck smokehouse. Stores cook and smoke cycles and logs core-probe and chamber temperatures (90 days on the device). Web interface on the plant network. A remote service module connects outbound to the manufacturer's cloud portal, **always on**, with one shared login and no MFA. Operators use one shared PIN (EV-008) |
| SYS-02 | Line 1 and Line 2 controls | On premises (plant network) | Vacuum stuffer and linker with a touchscreen HMI (**unsupported embedded operating system, installed 2016**); thermoforming packager (installed June 2026) with PLC, HMI, and an inline label printer-applicator. Recipes and settings live only on the machines (EV-010; EV-011) |
| SYS-03 | Labeling PC (production office) | On premises; MSP-managed | PC running label and lot-code software (templates, product and allergen statements) and the smokehouse vendor's desktop software for cycle uploads and cook-log exports. **One shared "production" login.** The packaging vendor installed an **unattended remote desktop tool** with a static password at commissioning (EV-009; EV-011) |
| SYS-04 | Cold-chain monitoring service | 8 wireless sensors and 1 wireless product probe, gateway on premises; vendor SaaS dashboard | Sensors in both coolers, the freezer, the blast chill cooler, the raw room, the packaging room, the drying room, and the truck. Alerts by text to the Production Supervisor only. **The gateway sits on the office network with no cellular backup** (EV-006; EV-017; EV-037) |
| SYS-05 | Food safety records app | Vendor SaaS on 2 floor tablets | SSOP pre-operational checks, HACCP monitoring, corrective actions, verification, and pre-shipment review. **One shared tablet login; "signatures" are typed initials.** The app's administrator account is the vendor-issued default, shared by the owner and the Office Manager (EV-005) |
| SYS-06 | Productivity suite (email, calendar, files) | SaaS | MFA on the four named mailboxes. A shared "plant" mailbox used by floor staff has no MFA. HACCP plans, SSOPs, the recall procedure, and formulations sit in a shared folder open to every suite account (EV-002; EV-003) |
| SYS-07 | Accounting, order, and invoicing service | SaaS | Orders, invoices with lot numbers (the traceability record for the recall procedure), customer list, purchasing. MFA on (EV-004) |
| SYS-08 | Office network and endpoints | On premises; MSP-managed | MSP-managed small-business firewall; **one flat network** for office computers, plant equipment, the cold-chain gateway, and staff Wi-Fi; separate guest Wi-Fi for retail customers. Endpoints: office desktop, owner laptop (encrypted), labeling PC (SYS-03), 2 floor tablets, 2 company phones (EV-013; EV-014; EV-017; EV-037) |
| SYS-09 | Cloud backup | SaaS, resold and operated by the MSP | Nightly backup of the office desktop, the labeling PC, and the productivity suite; 30 days of versions; one MSP administrator login without MFA. **Never restore-tested.** Smokehouse cycles, HMI settings, and packager recipes are not backed up (EV-018) |
| SYS-10 | Payroll service | SaaS | Employee personal information (Social Security numbers, bank accounts) (EV-001) |
| SYS-11 | Retail card terminal | Provider-managed, cellular | Outside the company network (EV-023) |
| SYS-12 | AI label and seal inspection camera (pilot) | Smart camera on Line 2 (plant network); vendor cloud for model updates | Checks each pack's seal and reads the label to confirm product name, allergen statement, and lot code match the job. Rejects go to a bin. Pilot since 2026-06-15 (see P10) (EV-011; EV-036) |
| SYS-13 | Remote access paths | Internet | Smokehouse manufacturer cloud portal (always on, shared login); packaging vendor unattended remote desktop on SYS-03; MSP remote management agent on the managed PCs (EV-008; EV-009; EV-020) |

**SSP system (P02):** the *Plant Production and Cold-Chain Monitoring System (PPCM)*: SYS-01 to SYS-09 and SYS-13, with interfaces to SYS-10 and the SYS-12 pilot.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). For a 7-person plant the systems of record are the vendor admin consoles (productivity suite, accounting service, records app, cold-chain dashboard), the payroll service, the smokehouse controller and its manufacturer's portal, the MSP's exports and monthly report, the food safety binder and FSIS establishment file, the contracts folder, the inspection and calibration records, the card statements, and a walk-through of the plant. Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the FSIS rules and the CSF 2.0 benchmark** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Scenario choice |
|---|---|
| P02 SSP | Plant Production and Cold-Chain Monitoring System (PPCM). The registry default system fits the business at this size |
| P03 regulation | **Changed from the registry default.** The registry names the FSMA Intentional Adulteration rule (21 CFR Part 121), but it does not reach a plant regulated exclusively by USDA (21 CFR 121.1 with 1.226(g)). P03 analyzes the binding rules instead: FSIS Sanitation SOPs (9 CFR 416.1-416.16, selected paragraphs), HACCP (9 CFR 417.2-417.7), and recalls (9 CFR 418.2-418.4), requirement by requirement with documentary evidence; plus applicability rows for the three registry IDs and a short NIST CSF 2.0 benchmark (with SP 800-82 Rev. 3) for IT and OT controls |
| P04 cloud | The SaaS services (productivity suite, records app, cold-chain service, accounting, payroll) plus one cloud workload, the MSP-operated cloud backup (SYS-09), and the vendor cloud connections into plant equipment. Vendor-agnostic |
| P05 BIA | 8 business processes (BP-01 to BP-08). Cold storage temperature control and monitoring: MTD 2 h, RTO 1 h |
| P07 assessment | 13 controls on the PPCM, assessed by an independent consultant; plant equipment checked after the production shift |
| P08 incident | Ransomware halting processing lines and cold-chain monitoring (registry default, scaled to a flat network: ransomware on the office and labeling PCs reaches the stuffer HMI, and isolating the network cuts the cold-chain gateway); the MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Availability readiness self-assessment, used to answer the regional grocery chain's supplier security questionnaire; plus a review of the cold-chain monitoring vendor's SOC 2 Type 2 report |
| P10 AI | AI-001 AI label and seal inspection camera on Line 2 (pilot). The registry default ("AI quality inspection on processing lines") is kept, scaled to one vendor smart camera on the packaging line. Also inventoried: AI-002 cold-chain anomaly alerts, AI-003 public generative AI chatbots |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-17 | Intake: evidence requests; exports from the vendor consoles (productivity suite, accounting service, records app, cold-chain dashboard), the payroll service and the MSP; the smokehouse controller and portal settings; the food safety binder, the FSIS establishment file and the contracts folder; a plant walk-through; inventories; obligations register |
| 2026-07-20 to 2026-07-31 | BIA interviews, risk assessment and gap analysis by the Office Manager with the MSP lead technician and the Production Supervisor (plant walkthrough 2026-07-22) |
| 2026-08-03 to 2026-08-07 | Policies drafted from the gaps; MSP evidence for the control assessment requested on 2026-08-03 |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant (plant equipment checked after the production shift on 2026-08-11): operating tests of controls already in place; design review of the draft policies |
| 2026-08-20 | SOC 2 readiness self-assessment and cold-chain vendor report review |
| 2026-08-25 | AI risk assessment |
| 2026-08-31 | Deliverables and policies approved by the owner |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6. Facts drawn from the company's records cite the evidence register ID they rest on.

| Topic | Added fact | Used in |
|---|---|---|
| Security lead designation | The owner designated the Office Manager as security and compliance lead in writing on 2026-07-20 (EV-050) | P02, P06, P09 |
| MSP contract | Covers the office desktop, owner laptop, labeling PC, firewall, Wi-Fi, suite administration, and backup, with a next-business-day response time, no recovery time commitment, and no incident notice term. Plant machines are excluded (EV-020) | P02, P05, P08 |
| Refrigeration contractor | Service agreement with a 4-hour emergency response (EV-021) | P05 |
| Inventory and sales | $25,000 to $40,000 of product and raw material in cold storage at any time; about $16,500 of wholesale deliveries a week; about $1,100 a day at the retail counter (EV-041; EV-040) | P05 |
| Accounts | The accounting service has three named users (owner, Office Manager, Production Supervisor), all with MFA. The cold-chain dashboard has two named accounts (owner, Production Supervisor) and one shared login used by the delivery driver; at intake it also listed the March 2026 leaver's login (EV-004; EV-006) | P04, P07 |
| Personal information held | Records of about 30 current and former employees (payroll exports and HR files); no consumer personal information (EV-001; EV-003; EV-035) | P08, P09 |
| Firewall logging | The firewall keeps 7 days of logs (EV-017) | P02, P07 |
| Cold-chain gateway | The gateway went offline 3 times between February and July 2026 (vendor dashboard history); nobody was alerted (EV-007) | P03, P05 |
| 2026 changes | March 2026: SSOP monitoring moved from paper to the records app (SSOP text updated, not re-signed) and a new smoked sausage cycle was added (fully cooked plan modified, not re-signed). June 2026: new packaging machine with the AI camera; the old packaging controller was removed with no disposal record. The smokehouse remote service module was installed in 2025 (EV-005; EV-027; EV-029; EV-010; EV-011) | P02, P03, P09 |
| HACCP training and validation | The owner and the Production Supervisor completed a qualifying HACCP course in 2019; initial validation files for all three plans date from 2019 (EV-031; EV-028) | P03 |
| Departure | A production worker left in March 2026. His suite account was disabled the same day; shared passwords and the smokehouse PIN were not changed until 2026-08-12, and his cold-chain dashboard login was removed the same day (EV-001; EV-002; EV-035; EV-AC-2) | P01, P07 |
| Vendor remote access change | On 2026-08-12 the smokehouse portal connection and the packaging vendor's remote desktop tool were set to off by default, enabled only for supervised sessions (EV-AC-17) | P01, P02, P04, P07 |
| P07 testing results | On 2026-08-11 the assessor found the manufacturer default administrator password on the smokehouse controller web interface (changed the same day), 17 networked devices against 3 in the MSP list, and 6 unrequested manufacturer portal sessions in July 2026 (EV-SC-7; EV-CM-8; EV-AC-17) | P01, P07, P09 |
| Invoice fraud attempt | In 2025 an email asked the Office Manager to change a meat supplier's bank details; she called the supplier and stopped it. It was never shared with staff (EV-035; EV-AT-2) | P01, P07 |
| Assessor | The P07 assessor is an independent consultant with food plant OT experience, not involved in the risk assessment, the gap analysis, or operating any control | P07, P09 |
| Grocery chain questionnaire | Received July 2026; response due 2026-09-30; small suppliers may answer with a self-assessment (EV-042) | P09 |
| AI camera pilot | Two model updates pushed by the vendor without notice (2026-07-09 and 2026-08-04); packaging film supplier changed on 2026-07-28 (EV-052) | P10 |

# Scenario facts: Cris Santos Company | Chemical | Micro

All 11 deliverables in this folder use the facts below. The company is fictitious and independent of the other sizes. Where a fact comes from a statute, regulation, or NIST publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23), the Federal Register API, and uscode.house.gov between 2026-09-26 and 2026-10-05.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (specialty chemical maker) |
| Business | Blends and packages specialty cleaning, degreasing, and water-treatment chemicals (boiler and cooling-tower treatment products) for business customers, plus small toll-blending and private-label jobs. Primary industry NAICS 325998, All Other Miscellaneous Chemical Product and Preparation Manufacturing |
| Location | Florida. One leased 12,000 sq ft unit in an inland light-industrial park: a **blend room** with two mix tanks run by the batch control system (**T-1**, 1,000 gal, stainless, jacketed and heated by a hot-water skid; **T-2**, 500 gal, unheated) and a portable mixer for small batches; a packaging area (pail and jug filler; drums and totes filled on a floor scale); a locked raw-material room; a flammables storage room; a QC bench; one loading dock; and three offices. No rail, dock, or waterfront |
| Workforce | 7 employees (see section 2). One shift, 7:00 to 15:30, Monday to Friday |
| Revenue | About $1.1 million a year (fictional), about $4,400 of shipments per production day (250 days) (EV-035). The SBA size standard for NAICS 325998 is 650 employees (13 CFR 121.201), so the company is SBA-small |
| Operations | About 85 active formulations and 180 packaged SKUs. About 4 batches a day (100 to 1,000 gal each). 2 to 4 outbound less-than-truckload (LTL) shipments a day plus customer pickups (EV-036). The company has no trucks of its own |
| Customers | About 140 business customers in Florida and neighboring states: commercial laundries, food plants, HVAC and boiler service contractors, and two regional distributors. The largest, a distributor that buys private-label products (about 22% of revenue), sent a supplier security and continuity questionnaire in June 2026, response due 2026-09-30 (EV-037; see P09). Customers pay by ACH or check (EV-035); the company handles no payment card data |
| Regulated inventory | See the table below. Maximum inventories are purchasing limits set by the Owner and checked at each order (purchasing records, EV-027) |
| CFATS status | The company holds 35% hydrogen peroxide in totes, a CFATS theft/diversion chemical of interest. It filed a Top-Screen in 2009 and was notified in 2010 that the facility was **not high risk** (never tiered; no Security Vulnerability Assessment or Site Security Plan was ever required) (EV-028). CFATS statutory authority **terminated on July 27, 2023** (U.S. Code note to 6 U.S.C. 621-629, text of laws in effect 2026-09-24; CISA describes the program as expired as of July 28, 2023) and has **not been reauthorized**: no CFATS document appears in the Federal Register in 2026 (search run 2026-10-05). The Top-Screen file is kept as legacy CVI (6 CFR 27.400(b)(8)). RBPS 8 is used as a **voluntary benchmark** (P03). Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-CHEMICAL-R01) |
| EPA RMP status | **Not covered**, determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (EPA-RMP). No regulated substance in 40 CFR 68.130 is held above its threshold quantity (math below) |
| OSHA PSM status | **Not covered** (29 CFR 1910.119(a)(1)), determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (OSHA-PSM). No chemical is at a listed concentration, and flammable liquids stay far below 10,000 lb (math below) |
| DOT hazmat status | **Offeror (shipper) of hazardous materials.** Outbound products include Class 8 corrosive cleaners (Packing Groups II and III) and a Class 3 isopropyl-alcohol degreaser (Packing Group II), all in non-bulk packagings (pails, jugs, 55-gal drums, and 275-gal IBC totes). Pallet shipments often exceed 1,001 lb aggregate gross weight of Table 2 materials, so placards are required (49 CFR 172.504(c), (e)) and the company holds an annual PHMSA hazmat registration (49 CFR 107.601(a)(6)). **No transportation security plan is required** (49 CFR 172.800(b)): no shipment is a "large bulk quantity" (more than 792 gal in a single packaging), and none of the any-quantity materials are shipped. Six hazmat employees receive the 172.704 training every three years, including security awareness training (172.704(a)(4)). A contracted 24-hour emergency response information (ERI) provider supplies the emergency response telephone number on shipping papers (172.604(b)(2)). Records: EV-023 to EV-026; applicability in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (DOT rows) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): USCG MTSA cybersecurity rule (C-CHEMICAL-R02; 33 CFR Part 101 Subpart F): applies only to facilities required to have a security plan under 33 CFR Part 105 (101.605(a)); the site has no marine transfer. CIRCIA (C-CHEMICAL-R03): proposed rule only, not in effect (no final rule in the Federal Register as of 2026-10-05); as proposed, the company is under the SBA size criterion and the CFATS sector criterion is moot. EAR: domestic customers only and no controlled technology. Federal contracts: none. SEC rules: privately held. HIPAA and PCI DSS: no health or card data |
| Regulatory driver IDs | **C-CHEMICAL-R01** (CFATS RBPS 8, voluntary benchmark), **C-CHEMICAL-R02** (USCG MTSA rule, not applicable), **C-CHEMICAL-R03** (CIRCIA, proposed). DOT Hazardous Materials Regulations (49 CFR 107.601, 172.201, 172.604, 172.704, 172.800), CERCLA and EPCRA release reporting (40 CFR 302.6, 355.30-355.43), and the OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) are cited directly because the vertical registry has no ID for them |
| State law approach | Florida law is cited only where unavoidable: breach notice for employee personal information (Fla. Stat. 501.171). The samples otherwise stay federal |

### Regulated inventory and threshold math

Densities are from supplier SDSs (rounded). Totes are 275-gal IBCs. Quantities and concentrations are from the purchasing records and supplier SDSs (EV-027).

| Chemical | Storage | Maximum inventory | EPA RMP (40 CFR 68.130) | OSHA PSM (29 CFR 1910.119 App. A and (a)(1)(ii)) | CFATS Appendix A (legacy) | CERCLA RQ (40 CFR 302.4) |
|---|---|---|---|---|---|---|
| Hydrogen peroxide, 35% | Locked raw-material room; one tote connected to the T-1 dosing pump | 2 totes: 2 x 275 gal x 9.4 lb/gal = **5,170 lb of solution**, 5,170 x 0.35 = **1,810 lb of hydrogen peroxide** | Not listed | Listed only at "52% by weight or greater", TQ 7,500 lb. 35% is below 52%: **not covered** | Theft/diversion-EXP/IEDP chemical, minimum concentration 35%, STQ 400 lb, counted only in transportation packagings (6 CFR 27.203(c); 27.204(b)(3); 72 FR 65396, Nov. 20, 2007). Both counting methods exceed 400 lb: this is why the 2009 Top-Screen was filed | Not listed |
| Sodium hydroxide, 50% | Raw-material room; one tote connected to a T-1 dosing pump | 2 totes: 2 x 275 x 12.7 = 6,985 lb of solution (3,493 lb NaOH) | Not listed | Not listed | Not listed | 1,000 lb (count the NaOH content, 302.6(b)(1)(i)): about 2,000 lb of solution (about 157 gal) |
| Sodium hypochlorite, 12.5% | Raw-material room, separated from acids | 2 totes: 2 x 275 x 10.0 = 5,500 lb of solution (688 lb NaOCl) | Not listed | Not listed | Not listed | 100 lb: about 800 lb of solution (about 80 gal) |
| Phosphoric acid, 75% | Raw-material room, acid side | 1 tote: 275 x 13.1 = 3,603 lb of solution (2,702 lb acid) | Not listed | Not listed | Not listed | 5,000 lb: a full tote is below the RQ |
| Isopropyl alcohol, 99% (flash point below 100 F) | Flammables room | 8 drums: 8 x 55 gal x 6.55 lb/gal = **2,882 lb** | Not listed | Flammable liquid rule needs 10,000 lb or more in one location: **not covered** | Not relevant | Not listed |
| Propane (forklift) | Exterior cage | 4 cylinders x 33 lb = 132 lb | Listed flammable, TQ 10,000 lb: far below | Not relevant | Not relevant | Not listed |

Surfactants, glycols, dyes, fragrances, and citric acid are not listed under any of these rules.

**Limits the company must keep** (POL-02 A.10): hydrogen peroxide is bought only below 52%, no more than 2 totes on site, and any new raw material is screened against the RMP, PSM, CFATS Appendix A, and DOT 172.800 lists before the first purchase. The Owner rejected a peracetic acid sanitizer in 2025 (EV-027) after learning that peracetic acid is an RMP-listed substance (TQ 10,000 lb).

## 2. People (role titles only)

| Role | Security, safety, and compliance duties |
|---|---|
| Owner and President | Accountable for the business; accepts Moderate and higher risks; approves policies and spending; owns the formulations (a chemist by training); signs customer questionnaires; holds the CFATS Top-Screen file |
| Operations Manager | **System owner** of the batch control system; production, process safety, and the emergency action plan; hazmat training coordinator and registration holder for DOT; incident commander for process emergencies; works with the control system integrator |
| Office Manager | **Security Coordinator** (designated in writing on 2026-08-31, EV-051): accounts, MSP liaison, vendor files, training records, incident log; also bookkeeping, orders, HR, and payroll |
| QC Technician | QC tests and certificates of analysis; drafts SDS updates in the SDS service for Owner approval |
| Blend Operators (2) | Run batches on the HMI; first responders to alarms (evacuate and call 911; the company does not perform hazmat response). One was hired on 2026-04-20 to replace an operator who left on 2026-03-13 (EV-001) |
| Warehouse and Shipping Lead | Receiving, packaging, shipping papers, placards, and loading |
| Managed service provider (MSP) | Office IT under contract: laptops and desktops, firewall and Wi-Fi, productivity suite administration, patching, antivirus, and the cloud backup. **Does not support the control system** |
| Control system integrator (contracted) | Built the batch control system in 2017; supports the PLC, HMI, and recipe software remotely through a cellular gateway and its cloud portal; turned on the portal's AI batch-optimization feature in May 2026 |
| 24-hour ERI provider (contracted) | Answers the emergency response telephone number on shipping papers; holds current SDSs for all shipped products |
| Independent assessor | OT-experienced security consultant engaged for P07 on a fixed fee (EV-038); did not take part in P01 or P03 and operates no control |

**Role overlap.** Seven people cannot separate duties fully. The Office Manager both runs and checks account controls, and the Operations Manager both changes recipes and approves batches. The compensations are: the Owner's monthly review of the account list and recipe change log (POL-02 A.2, B.5), the MSP's monthly report, the integrator's session log, and the independent assessment (P07).

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Batch control PLC and field devices | On premises, blend room control panel | Setpoints, alarm limits, interlock logic | One PLC controlling T-1 and T-2: load cells, 4 metering pumps drawing from connected totes (hydrogen peroxide, sodium hydroxide, and two surfactant blends), mixers, valves, the hot-water skid, and temperature probes. **Hardwired** emergency stop and a T-1 high-temperature switch that cuts the heater and dosing pumps independent of the PLC. Atmospheric vents on both tanks (EV-039) |
| SYS-02 | HMI and recipe PC | On premises, blend room | About 85 recipes (trade secrets); batch records | One industrial panel PC running the HMI and the batch recipe module. Operating system out of mainstream support; not patched since 2023; no antivirus; a remote desktop service is enabled for the integrator (EV-008). **One shared operator login** (EV-009) |
| SYS-03 | Integrator remote access gateway and cloud portal | Cellular gateway in the control panel; integrator's cloud portal (SaaS) | Process data stream; remote sessions | Always on (EV-010). **One shared portal login** used by integrator staff and the Operations Manager, with no MFA (EV-006). The portal also hosts the monitoring dashboard and the AI batch-optimization feature (SYS-12) |
| SYS-04 | Office network | On premises, MSP-managed | In transit | Small-business firewall and Wi-Fi. **The HMI PC is on the same flat network** as the office (used to print batch tickets and copy recipe exports) (EV-016, EV-047). Guest Wi-Fi exists |
| SYS-05 | Endpoints | MSP-managed | Formulations and employee data (cached) | 4 laptops (Owner, Operations Manager, Office Manager, QC Technician), 2 desktops (shipping, QC bench), and 1 warehouse tablet. Antivirus and monthly patching by the MSP; laptops encrypted, desktops not (EV-012 to EV-015, EV-039) |
| SYS-06 | Productivity suite (email, files, shared drive) | SaaS | Formulations folder; customer correspondence | MFA enforced for all users (EV-003) |
| SYS-07 | Cloud accounting and inventory service | SaaS | Orders, customers, lot records, hazmat shipping papers (bills of lading) | MFA enabled only for the Owner (EV-004). The vendor has a SOC 2 Type 2 report (EV-022; reviewed in P09) |
| SYS-08 | SDS and label authoring service | SaaS | SDSs and GHS labels for about 85 products | SDS updates are exported to the ERI provider by email (EV-005) |
| SYS-09 | Cloud backup service | SaaS, operated by the MSP | Copies of the productivity suite and shared drive | Daily, 30 days of versions; the HMI PC and PLC are **not** included (EV-017) |
| SYS-10 | Payroll service | SaaS | Employee PII for 7 employees | Outside the SSP boundary; vendor-run (EV-001) |
| SYS-11 | Building alarm and cloud video | On premises with cloud video service | Video | Keypad entry with a shared code, alarm panel with a cellular communicator, 4 cameras (EV-032) |
| SYS-12 | AI batch-optimization feature | Integrator's cloud portal (SYS-03) | Process data from T-1 | Pilot since 2026-05-11 (EV-006; see P10). Recommends heat-up and mixing settings for T-1; a write-back option exists in the portal and is switched off |

**SSP system (P02):** the *Blending and Business Platform (BBP)*: SYS-01 to SYS-09, the batch control system, its remote access path, the office network and endpoints, and the SaaS services the business runs on, with interfaces to the payroll service (SYS-10), the building systems (SYS-11), and the integrator's AI feature (SYS-12, assessed in P10).

**Why not a DCS.** The registry default primary system is a "process control (DCS) and batch management system." A 7-person blender does not run a DCS. Its equivalent is one PLC with an HMI and recipe module (SYS-01, SYS-02), supported remotely by an integrator. The same risks apply at a smaller scale: remote access, shared logins, and unverified recipes.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). For a 7-person blender the systems of record are the SaaS admin consoles, the payroll service, the integrator's portal and the HMI PC's own screens, the MSP's exports and reports, the contracts folder and the DOT files, and a site walk-through. Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the RBPS 8 benchmark and the binding DOT and release reporting duties** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 SSP | Blending and Business Platform (BBP), categorized Moderate under FIPS 199 (reasoning in the SSP section 6) |
| P03 regulation | Primary: CFATS RBPS 8, 6 CFR 27.230(a)(8), as a **voluntary benchmark** (authority lapsed; the company was never tiered), with CISA's RBPS 8 security measures. Secondary (binding): DOT Hazardous Materials Regulations offeror duties that depend on the company's systems and people (49 CFR 107.601, 172.201(e), 172.604, 172.704, 172.800). Applicability rows for EPA RMP and OSHA PSM |
| P04 cloud | SaaS services plus one cloud workload, the MSP-operated cloud backup. The integrator's cloud portal is mapped as SaaS. Vendor-agnostic |
| P05 BIA | 9 business functions (BP-01 to BP-09). BP-07 emergency notification has the shortest MTD (1 h) |
| P07 assessment | 13 controls on the BBP; on-site testing on 2026-08-11 with blending stopped for the day |
| P08 incident | Intrusion into the batch control system through the integrator's shared portal login: the attacker raises the hydrogen peroxide dose in a T-1 recipe and widens the high-temperature alarm, then runs ransomware on the HMI PC, which spreads toward the office over the flat network. MSP, integrator, and insurer are in the notification chain |
| P09 SOC 2 | The company is not a service organization. (a) Security plus Availability self-assessment to answer the private-label distributor's questionnaire; (b) review of the accounting and inventory vendor's SOC 2 Type 2 report |
| P10 AI | AI-001 integrator-provided AI batch-optimization feature (advisory recommendations for T-1; write-back off). Inventory also lists AI-002 (SDS service drafting assistant) and AI-003 (public chatbots, prohibited for formulations) |
| Cloud | Vendor-agnostic. Services are described by category |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-29 to 2026-07-10 | Intake: evidence requests; exports from the SaaS consoles, the payroll service, the integrator portal, the HMI PC and the MSP; the contracts folder and DOT files; a site walk-through; inventories; obligations register |
| 2026-07-13 to 2026-07-24 | BIA, risk assessment, and gap analysis fieldwork with the MSP and the integrator (site walkthrough 2026-07-15) |
| 2026-07-27 to 2026-08-07 | Policies drafted from the gaps |
| 2026-08-10 to 2026-08-12 | Control assessment by the independent consultant (on-site testing 2026-08-11, blending stopped): operating tests of controls already in place; design review of the draft policies |
| 2026-08-19 | SOC 2 readiness self-assessment and vendor report review |
| 2026-08-21 | AI risk assessment |
| 2026-08-31 | Deliverables and policies approved by the Owner |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |

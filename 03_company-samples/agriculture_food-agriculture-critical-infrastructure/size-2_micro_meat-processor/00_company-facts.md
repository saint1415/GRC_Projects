# Scenario facts: Cris Santos Company | Food and Agriculture | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute or regulation, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23) and uscode.house.gov.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) |
| Business | Further processing of purchased pork and beef trimmings and primals (NAICS 311612, Meat Processed from Carcasses): fresh sausage, smoked sausage, smoked hams, and beef jerky and snack sticks. No slaughter. Meat and meat food products only; the plant makes no FDA-regulated food |
| Location | Florida. One small plant: a raw processing room with a grinder and a vacuum stuffer with automatic linker (**Line 1**); one programmable two-truck smokehouse for cooking and smoking; a blast chill cooler; a drying room for jerky; two coolers and one freezer; a packaging room with a thermoforming vacuum packaging machine and an inline label printer-applicator (**Line 2**); an office; and a small retail counter at the front. One refrigerated box truck for deliveries |
| Workforce | 7 employees: the owner (General Manager), 1 Office Manager, 1 Production Supervisor, 1 Maintenance and Sanitation Technician, and 3 production workers (one also drives the delivery truck; one also covers the retail counter) |
| Revenue | About $1.1 million a year (fictional), about $4,400 per production day (250 days). The SBA size standard for NAICS 311612 is 1,000 employees (13 CFR 121.201), so the company is SBA-small |
| Customers | About 40 wholesale accounts (independent grocers, butcher shops, and restaurants within about 150 miles, all in Florida), about 75% of sales, delivered by the company truck. The retail counter is about 25%. A 12-store regional grocery chain became a customer in May 2026. No online sales. No federal contracts or subcontracts |
| USDA FSIS status | **Official establishment** under a federal grant of inspection (Federal Meat Inspection Act). FSIS inspection program personnel are assigned to the establishment. Three written HACCP plans (9 CFR Part 417) under the 417.2(b)(1) processing categories: raw product, ground (fresh sausage); fully cooked, not shelf stable (smoked sausage, smoked hams); heat treated, shelf stable (jerky, snack sticks). Written Sanitation SOPs (9 CFR 416.11-416.16) and a written recall procedure (9 CFR 418.3) |
| FDA status | **Not registered** with FDA. Facilities "regulated exclusively, throughout the entire facility" by USDA under the FMIA do not register (21 CFR 1.226(g)). The FSMA Intentional Adulteration rule applies only to facilities required to register (21 CFR 121.1), so it does not apply. The company is also not a "responsible party" under the Reportable Food Registry, which is tied to registration (21 U.S.C. 350f(a)(1)). If the plant ever adds an FDA-regulated product, these answers change (see the Small sample, whose seafood room made it a registered facility) |
| CCPs that depend on systems | **Cooking** (fully cooked products and jerky): the smokehouse controller's product core-probe log, verified by a handheld thermometer reading entered on a floor tablet at the end of each cycle. **Chilling** (stabilization of fully cooked products): a wireless product probe in the blast chill cooler, logged by the cold-chain monitoring service. **Receiving and cold storage** (raw product, ground): cooler temperatures from the cold-chain service plus receiving checks on the tablet. Jerky water activity is tested per lot by an outside laboratory |
| Refrigeration | Packaged condensing units with a halocarbon refrigerant serve the coolers, freezer, and blast chill cooler. **No anhydrous ammonia.** The 10,000 lb ammonia threshold quantity in OSHA process safety management (29 CFR 1910.119, Appendix A) and EPA risk management program rules (40 CFR 68.130) is therefore not reached |
| Not in scope | FSMA Intentional Adulteration rule (C-FOOD-AG-R01): not a registered facility (above); it would also be a very small business under 121.5(a). CIRCIA (C-FOOD-AG-R02): proposed only; as proposed, coverage turns on exceeding the SBA size standard (7 employees against 1,000). USCG MTS cyber rule (C-FOOD-AG-R03): no MTSA facility. SEC rules: privately held. FAR 52.204-21 and 52.204-25: no federal contracts. PCII: never submitted information to DHS |
| Payment cards | The retail counter uses a standalone card terminal managed by the payment provider on its own cellular connection. No card numbers touch company systems. PCI DSS obligations are contractual through the acquirer and are not analyzed here |
| Regulatory driver IDs | The vertical registry IDs are used for their applicability decisions: C-FOOD-AG-R01 (not applicable), C-FOOD-AG-R02 (proposed, tracked), C-FOOD-AG-R03 (not applicable). The binding food safety rules are outside the registry and are cited directly after being read on eCFR: 9 CFR Part 416 (sanitation), Part 417 (HACCP), Part 418 (recalls). NIST CSF 2.0 and SP 800-82 Rev. 3 are the voluntary benchmark for IT and OT controls that no binding rule covers |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice for employee data, Fla. Stat. 501.171) |

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
| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Smokehouse controller | On premises (plant network) | Programmable controller on the two-truck smokehouse. Stores cook and smoke cycles and logs core-probe and chamber temperatures (90 days on the device). Web interface on the plant network. A remote service module connects outbound to the manufacturer's cloud portal, **always on**, with one shared login and no MFA. Operators use one shared PIN |
| SYS-02 | Line 1 and Line 2 controls | On premises (plant network) | Vacuum stuffer and linker with a touchscreen HMI (**unsupported embedded operating system, installed 2016**); thermoforming packager (installed June 2026) with PLC, HMI, and an inline label printer-applicator. Recipes and settings live only on the machines |
| SYS-03 | Labeling PC (production office) | On premises; MSP-managed | Windows PC running label and lot-code software (templates, product and allergen statements) and the smokehouse vendor's desktop software for cycle uploads and cook-log exports. **One shared "production" login.** The packaging vendor installed an **unattended remote desktop tool** with a static password at commissioning |
| SYS-04 | Cold-chain monitoring service | 8 wireless sensors and 1 wireless product probe, gateway on premises; vendor SaaS dashboard | Sensors in both coolers, the freezer, the blast chill cooler, the raw room, the packaging room, the drying room, and the truck. Alerts by text to the Production Supervisor only. **The gateway sits on the office network with no cellular backup** |
| SYS-05 | Food safety records app | Vendor SaaS on 2 floor tablets | SSOP pre-operational checks, HACCP monitoring, corrective actions, verification, and pre-shipment review. **One shared tablet login; "signatures" are typed initials.** The app's administrator account is the vendor-issued default, shared by the owner and the Office Manager |
| SYS-06 | Productivity suite (email, calendar, files) | SaaS | MFA on the four named mailboxes. A shared "plant" mailbox used by floor staff has no MFA. HACCP plans, SSOPs, the recall procedure, and formulations sit in a shared folder open to every suite account |
| SYS-07 | Accounting, order, and invoicing service | SaaS | Orders, invoices with lot numbers (the traceability record for the recall procedure), customer list, purchasing. MFA on |
| SYS-08 | Office network and endpoints | On premises; MSP-managed | MSP-managed small-business firewall; **one flat network** for office computers, plant equipment, the cold-chain gateway, and staff Wi-Fi; separate guest Wi-Fi for retail customers. Endpoints: office desktop, owner laptop (encrypted), labeling PC (SYS-03), 2 floor tablets, 2 company phones |
| SYS-09 | Cloud backup | SaaS, resold and operated by the MSP | Nightly backup of the office desktop, the labeling PC, and the productivity suite; 30 days of versions; one MSP administrator login without MFA. **Never restore-tested.** Smokehouse cycles, HMI settings, and packager recipes are not backed up |
| SYS-10 | Payroll service | SaaS | Employee personal information (Social Security numbers, bank accounts) |
| SYS-11 | Retail card terminal | Provider-managed, cellular | Outside the company network |
| SYS-12 | AI label and seal inspection camera (pilot) | Smart camera on Line 2 (plant network); vendor cloud for model updates | Checks each pack's seal and reads the label to confirm product name, allergen statement, and lot code match the job. Rejects go to a bin. Pilot since 2026-06-15 (see P10) |
| SYS-13 | Remote access paths | Internet | Smokehouse manufacturer cloud portal (always on, shared login); packaging vendor unattended remote desktop on SYS-03; MSP remote management agent on the Windows PCs |

**SSP system (P02):** the *Plant Production and Cold-Chain Monitoring System (PPCM)*: SYS-01 to SYS-09 and SYS-13, with interfaces to SYS-10 and the SYS-12 pilot.

## 4. Current security posture: early, with basic hygiene
**In place today:**
- Three HACCP plans, Sanitation SOPs, and a written recall procedure under FSIS inspection; annual HACCP reassessment signed in January 2026; Production Supervisor HACCP-trained (9 CFR 417.7)
- Daily SSOP and HACCP monitoring records in the records app; handheld thermometer verification of each cook cycle
- Cold-chain alerting for every cooler, the freezer, the blast chill cooler, and the truck
- MSP patching and antivirus on the three Windows computers; MSP-managed firewall; nightly cloud backup
- MFA on the named productivity suite mailboxes and the accounting service
- Owner laptop encrypted; guest Wi-Fi separated from staff Wi-Fi
- Card terminal on the provider's own cellular connection
- Keyed exterior doors, an after-hours alarm, and a locked office
- A cyber insurance policy with a 24x7 breach hotline (bought 2025)

**Missing or weak, found in the 2026 assessments:**
1. No risk assessment had ever been done. No security policies. The Office Manager's security role was informal until 2026.
2. One flat network: plant equipment, the labeling PC, the cold-chain gateway, the AI camera, office computers, and staff Wi-Fi share it.
3. Always-on vendor remote access: the smokehouse cloud portal uses one shared login with no MFA; the packaging vendor's unattended remote desktop tool uses a static password. No approval, no logging review.
4. Shared logins on the labeling PC, the floor tablets, and the smokehouse controller PIN. Cook cycle, formulation, and label template changes are not attributable and need no second check.
5. Electronic HACCP and SSOP records have no documented integrity controls (9 CFR 417.5(d), 416.16(b)): typed initials under a shared login; cook-log exports are editable spreadsheets; the records app administrator is a shared vendor default account.
6. Backups have never been restore-tested; smokehouse cycles, HMI settings, and packager recipes are not backed up at all.
7. No incident response plan. Nothing links a cyber incident to product holds or the 24-hour FSIS notification (9 CFR 418.2).
8. Cold-chain alerts reach one person with no escalation; the gateway has no backup connection; there is no written manual temperature log procedure for monitoring outages.
9. The stuffer HMI runs an unsupported operating system that cannot be patched.
10. No security training. Staff have never been told how to spot phishing or whom to call.
11. The MSP contract excludes plant equipment, has no recovery time commitment or incident notice term, and MSP-held administrator logins (firewall, backup console) have no MFA.
12. No security review of any vendor; no SOC 2 report reviewed; no security terms in equipment vendor, cold-chain, records app, or AI camera contracts.
13. Formulations and HACCP plans sit in a shared folder open to every suite account, including the shared plant mailbox.
14. The AI camera pilot started 2026-06-15 without a validation protocol, a written relationship to the label check at the start of each run, or data-use terms.
15. Shared passwords were never changed after a production worker left in March 2026.

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
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis by the Office Manager with the MSP lead technician and the Production Supervisor (plant walkthrough 2026-07-22) |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant (plant equipment checked after the production shift on 2026-08-11) |
| 2026-08-20 | SOC 2 readiness self-assessment and cold-chain vendor report review |
| 2026-08-25 | AI risk assessment |
| 2026-08-31 | Deliverables approved by the owner |

# Scenario facts: Cris Santos Company | Chemical | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Regulatory text was read from eCFR (point-in-time 2026-09-23), the Federal Register, and the Florida Legislature's statutes site between 2026-09-25 and 2026-10-05.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C) |
| Business | Specialty chemical distributor (broker). Buys water treatment and sanitation chemicals from manufacturers and resells them to industrial customers. Every order is **drop-shipped**: a for-hire carrier picks it up at the manufacturer's plant or terminal and delivers it to the customer. The business takes title (merchant wholesaler, NAICS 424690) but never takes physical possession. It has no warehouse, tanks, trucks, or chemical inventory |
| Location | Florida. A home office in the owner's residence. No chemicals are ever at the home |
| Workforce | The owner only (0 employees). The owner started the business in 2022 after 15 years in sales at a regional chemical distributor |
| Customers | About 40 active business customers in Florida and south Georgia: cooling water treatment, food and beverage plant sanitation, commercial laundries, and pool service companies. About 75 orders a year |
| Suppliers | Five manufacturers and terminals: two hydrogen peroxide producers' terminals, one chlor-alkali producer (sodium hypochlorite and sodium hydroxide), one ferric chloride producer, and one specialty polymer formulator |
| Revenue | About $180,000 a year in receipts (fictional). SBA-small (standard 175 employees for NAICS 424690; 13 CFR 121.201) |
| Hazmat role | The business is an **offeror** under the Hazardous Materials Regulations (HMR) for its drop shipments (49 CFR 171.8; 171.1(b)). For each order the owner confirms the hazard class from the manufacturer's safety data sheet (SDS) against the Hazardous Materials Table, prepares the bill of lading (BOL) with the hazmat description, the emergency response telephone number, and the shipper's certification, books the carrier, and sends the supplier a pickup authorization. The supplier fills, marks, labels, placards, and loads. Both are offerors for the functions each performs (171.2(b)) |
| Hazmat registration | Registered with PHMSA (49 CFR 107.601(a)(4) and (a)(6): bulk loads of 3,500 gallons or more and placarded quantities). Current Certificate of Registration covers the registration year 2026-07-01 to 2027-06-30 (EV-010) |
| Hazmat security plan | **Required** (intake [obligations register](step-00_P00_intake/obligations-register.csv), HMR-172I). No plan was found at intake (EV-009). Bulk 50% hydrogen peroxide is a large bulk quantity of a Division 5.1 material in Packing Group II (172.800(b)(10)). The owner believed the suppliers' own security plans covered the drop shipments (EV-028). They cover the suppliers' functions, not the broker's (EV-034) |
| Emergency response information | Contract with a 24-hour emergency response information (ERI) provider under 49 CFR 172.604(b)(2). The BOL template shows the provider's number and the company's contract number (EV-012) |
| CFATS status | Not applicable, decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-CHEMICAL-R01). The business has no establishment that possesses chemicals (6 CFR 27.105 "chemical facility"), and CFATS authority lapsed on 2023-07-28 and has not been reauthorized (vertical registry, verified 2026-09-25; no CFATS document in the Federal Register in 2026 as of 2026-10-05). Hydrogen peroxide's former status as a CFATS theft and diversion chemical of interest is why diversion matters here. RBPS (a)(5), (a)(6), and (a)(8) are used as a **voluntary benchmark** in P03 |
| EPA RMP and OSHA PSM | Not applicable, decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (EPA-RMP, OSHA-PSM). No stationary source or process: 40 CFR 68.3 excludes transportation, including storage incident to transportation, from "stationary source", and 68.10(a) applies to owners or operators of stationary sources. OSHA PSM needs a process and employees |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): USCG MTSA cybersecurity rule (no MTSA facility; 33 CFR 101.605). CIRCIA (proposed only; as proposed the business is far below the SBA size criterion). DEA listed chemicals: the product line excludes List I and List II chemicals (21 CFR 1310.02 lists hydrochloric acid, sulfuric acid, and potassium permanganate; the owner declined to add the two acids in 2025). EAR: domestic sales only. Federal contracts: none. SEC: not applicable. HIPAA: not applicable |
| Regulatory driver IDs | **C-CHEMICAL-R01** (CFATS RBPS, voluntary benchmark), **C-CHEMICAL-R02** (USCG MTSA rule, not applicable), **C-CHEMICAL-R03** (CIRCIA, proposed). The binding rules for this business, the DOT HMR (49 CFR Parts 107, 171, 172) and Fla. Stat. 501.171, are cited directly because the vertical registry has no ID for them |
| State law approach | Florida law is cited only where unavoidable: Fla. Stat. 501.171 (driver identity data and customer records). The owner is a "covered entity" (501.171(1)(b) names a sole proprietorship). Drivers from other states are handled under "each state where affected individuals reside" |

### Products and hazmat thresholds
Hazmat descriptions verified against the 49 CFR 172.101 Hazardous Materials Table (eCFR 2026-09-23).

| Product | HMT entry | Packaging and volume | Security plan (172.800(b)) | Registration (107.601(a)) |
|---|---|---|---|---|
| Hydrogen peroxide, 50% | UN2014, Hydrogen peroxide, aqueous solutions with more than 40 percent but not more than 60 percent hydrogen peroxide, 5.1 (subsidiary 8), PG II | Cargo tank loads of about 4,000 gal (about 15,140 L, about 40,000 lb), about 6 a year to 2 customers; 275-gal totes (about 1,041 L), about 20 a year | **Yes.** A single cargo tank above 3,000 L is a "large bulk quantity" of Division 5.1 PG II ((b)(10)). Totes are bulk packagings but not large bulk | Yes: bulk packaging of 13,248 L or more ((a)(4)), and placarded quantities ((a)(6)) |
| Sodium hypochlorite, 12.5% | UN1791, Hypochlorite solutions, 8 | Totes and drums, about 30 totes a year | No (Class 8 is listed only for PG I in large bulk, (b)(16)) | Yes when placarded ((a)(6)) |
| Sodium hydroxide solution, 50% | UN1824, Sodium hydroxide solution, 8, PG II | Totes, about 15 a year | No | Yes when placarded |
| Ferric chloride solution | UN2582, Ferric chloride, solution, 8, PG III | Totes, about 10 a year (added in 2025) | No | Yes when placarded |
| Polymers and defoamers | Not regulated as hazmat | Totes and pails | No | No |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner | Every role: owner, security officer, privacy contact, risk acceptor, incident commander, hazmat employee, and the **senior management official responsible for the hazmat security plan** (172.802(b)(1)) |
| Outside accountant (CPA firm) | Quarterly bookkeeping review and taxes. Has its own user in the accounting SaaS |
| On-call IT technician (local computer shop, hourly) | Laptop and router help on request. No standing access. Used a remote-support tool once in 2025 |
| ERI provider | 24-hour emergency response telephone service for the company's shipments (172.604(b)(2)) |
| For-hire carriers (about 6 used) | Bulk cargo tank and less-than-truckload carriers. Their drivers pick up at the supplier's dock |
| Suppliers' shipping offices (5) | Load and release orders against the owner's pickup authorization; the shipping clerk checks the driver at the dock |
| Hazmat training provider | Online HMR course with test and certificate |
| Business attorney | General business matters. No breach counsel retained |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Email, calendar, and file storage suite (business plan) | SaaS | Pickup authorizations, BOLs, the order and shipment workbook, the SDS library, customer end-use statements, driver names with license numbers, the hazmat registration and training certificates | MFA available but off (EV-001). Password also used on one carrier portal (EV-005). No backup beyond the provider's deleted-item recovery (EV-001, EV-002) |
| SYS-02 | Accounting and invoicing SaaS | SaaS | Invoices, receivables and payables, customer and supplier bank details | Vendor enforces MFA. The accountant has a separate user (EV-003) |
| SYS-03 | Business bank online portal | Bank-hosted | Account access; ACH and wire payments to suppliers | One user; codes by text message; payees can be added online (EV-004) |
| SYS-04 | Supplier, carrier, and ERI provider portals (about 9 accounts) | SaaS | Order status, load bookings, tracking links, the ERI product list | Passwords saved in the browser (EV-005); most portals offer no MFA (EV-IA-2(2)) |
| SYS-05 | Laptop | Owner device | Cached email and files, downloads | Built-in disk encryption on (default at purchase in 2024). Owner works in an administrator account, and family members sometimes use it. Built-in antivirus; automatic updates (EV-006) |
| SYS-06 | Mobile phone | Personal device | Calls and texts with dispatchers and drivers; email app; bank codes; photos of signed BOLs | Passcode and device encryption on; find-my-device on (EV-007) |
| SYS-07 | Home network | ISP-provided router | Traffic for SYS-01 to SYS-05 | Router admin password never changed, by the owner's account. Shared with the household (EV-008) |
| SYS-08 | Generative AI assistant (paid individual plan) | Vendor SaaS | Prompts with customer names, prices, SDS text, and draft hazmat descriptions | Used since 2026-03 (EV-019, EV-024). The setting that lets the vendor use chats to improve its models was on until 2026-09-18 (EV-037). See P10 |

**SSP system (P02):** the *Brokerage Core SaaS Stack*: SYS-01 to SYS-08, the SaaS accounts, bank portal, partner portals, devices, home network, and AI assistant the owner uses to take orders, arrange hazmat shipments, keep shipping records, and bill.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person brokerage the sources are the SaaS admin consoles, the bank portal, the browser and device settings, the inbox and file storage, the order and shipment workbook, bank and card statements, the agreements folder, the PHMSA and training provider portals, the insurance agent's portal, and a walk through the home office.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the HMR, the CFATS benchmark and Fla. Stat. 501.171** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 SSP | Brokerage Core SaaS Stack (BCSS), short form, categorized Moderate |
| P03 regulation | **Primary (binding): DOT HMR hazmat transportation security plan and training** (49 CFR 172.800-172.804; 172.702-172.704), with the HMR registration, shipping paper, and emergency response information duties that run through the SaaS stack (107.601-107.620; 172.201; 172.204; 172.602; 172.604). **Benchmark (voluntary):** CFATS RBPS (a)(5), (a)(6), (a)(8), (a)(15)-(16) (C-CHEMICAL-R01). **State:** Fla. Stat. 501.171. The registry default (CFATS RBPS 8 as the primary benchmark) was changed because a broker with no facility could never be a CFATS facility, while the HMR binds it today |
| P08 incident | Takeover of the owner's email account, used to send a fraudulent pickup authorization that diverts a bulk hydrogen peroxide load and to send a customer false bank details. The registry default ("intrusion into process control systems at a chemical facility") was replaced because the business has no facility or process control systems |
| P09 SOC 2 | Security criteria only. Self-check to answer the largest customer's supplier security questionnaire and the hydrogen peroxide producers' product stewardship review, plus a review of the email suite provider's SOC 2 Type 2 report |
| P10 AI | The generative AI assistant (SYS-08). The registry default ("process-optimization model") was replaced because the business runs no process. The assistant's hazmat-description use is the safety-relevant case |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-08-31 to 2026-09-04 | Intake: the owner collects account and device settings, statements, agreements, certificates, the order workbook, inbox records and the home office walk-through; inventories; obligations register |
| 2026-09-08 to 2026-09-11 | Self-assessment with the on-call IT technician: BIA, risk assessment, gap analysis, and control assessment (account and device tests on 2026-09-10) |
| 2026-09-14 | Calls with the hydrogen peroxide producer's distribution security contact and the ERI provider |
| 2026-09-14 to 2026-10-02 | POL-01 and HSP-01 drafted from the gaps and the test results |
| 2026-09-18 | AI use assessment |
| 2026-09-25 to 2026-10-02 | Regulatory status checks (eCFR point-in-time 2026-09-23; Federal Register) |
| 2026-10-05 | Deliverables, POL-01 and HSP-01 adopted by the owner |
| 2027-02 (planned) | Follow-up check: operating effectiveness of the controls POL-01 and HSP-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Near miss | On 2026-06-17 an email from a lookalike of an existing customer's domain asked the owner to ship a hydrogen peroxide tote to a new address "for a second site". The owner did not ship only because the customer's buyer happened to call that day. It was not recorded or reported (EV-017) | P01, P03, P08, HSP-01 |
| AI near miss | In 2026-05 an AI-drafted BOL description for ferric chloride showed Packing Group II instead of III. The supplier's shipping clerk questioned it and the owner corrected it before pickup (EV-018) | P01, P03, P10 |
| ERI product list | Found on 2026-09-09 that ferric chloride was not on the ERI provider's product list. The provider confirmed the update on 2026-09-14. Four ferric chloride totes had shipped since 2025 with the provider lacking that product's information (EV-031, EV-035) | P03, P07 |
| Driver data | About 140 driver records (name and driver license number) sit in email from 2022 to 2026. Most drivers live in Florida or Georgia. Carriers send them so the owner can forward them to the supplier's shipping clerk (EV-016, EV-032) | P01, P03, P08 |
| AI setting | The owner turned off the AI assistant's model-improvement setting on 2026-09-18 during the P10 assessment (EV-037) | P10, P04 |
| Email suite assurance | The email and file suite provider publishes a SOC 2 Type 2 report on its trust portal for business-plan customers. The owner reviewed it on 2026-09-11 (EV-023) | P02, P09 |
| Payments | Suppliers are paid by wire or ACH from the bank portal. About half of the customers pay by ACH to the account number printed on the invoice (EV-019, EV-025) | P01, P05, P08 |
| Insurance | General and products liability only. No cyber policy (EV-019, EV-021) | P01, P08 |
| AI accuracy check | On 2026-09-18 the owner checked the 7 hazmat descriptions the AI assistant drafted from 2026-03 to 2026-08 against the 172.101 table (1 wrong: the ferric chloride packing group) and asked for the UN2014 description in 5 new chats (1 left out the subsidiary class 8) (EV-038) | P10 |
| AI chat history | The 2026-09-18 review of the chat history found customer names, prices, and SDS text, but no driver license numbers, pickup numbers, schedules, or bank details (EV-037) | P10 |
| AI decision | Adopted 2026-10-05: hazmat-description use (AI-002) prohibited; office drafting (AI-001) approved with conditions (no-training plan by 2026-10-31; MFA if the plan offers it by 2026-10-15) | P10 |

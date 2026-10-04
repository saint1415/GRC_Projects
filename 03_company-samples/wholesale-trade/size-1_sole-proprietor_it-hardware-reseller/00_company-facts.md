# Scenario facts: Cris Santos Company | Wholesale Trade | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was read from eCFR (current as of 2026-09-23) and the Florida Legislature's statute site.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C) |
| Business | IT hardware reseller (NAICS 423430): network switches, wireless access points, firewalls, optical transceivers, uninterruptible power supplies, and small-office peripherals and software licenses. Adds a staging service: firmware updates, asset labeling, and kitting before delivery |
| Location | Florida. A home office in the owner's residence and an attached garage with a staging bench and a locked steel stock cabinet. No warehouse. Most commercial orders are drop-shipped by the distributors |
| Workforce | The owner only (0 employees). Uses contracted help instead of staff |
| Revenue | About $180,000 a year in receipts (fictional), about $720 per business day over 250 days. Gross margin about 22% (about $40,000 a year). SBA-small (standard for NAICS 423430: 250 employees, 13 CFR 121.201) |
| Commercial customers | About 45 active small businesses in Florida (law, accounting, dental, and retail offices) and 3 local managed service providers. About 77% of receipts (about $139,000) |
| Federal (DoD) channel | One customer: a regional IT services integrator that is a DoD prime contractor (the "prime") refreshing network edge equipment at a DoD installation in Florida. The owner sells to it under a blanket purchase agreement (BPA) signed 2025-03, about 2 purchase orders a month, about $41,000 a year (23% of receipts). The owner buys switches, access points, and UPS units, updates firmware to the version the prime specifies, applies government asset tags (tag numbers supplied by the prime), records serial numbers against tags in a spreadsheet, kits by building, and delivers to the prime's staging warehouse |
| Clauses in the BPA | FAR 52.204-21, FAR 52.204-23, and FAR 52.204-25 (since 2025-03). The prime treats the orders as more than commercially available off-the-shelf (COTS) items because of the staging and labeling service, so it flowed down FAR 52.204-21 (see 52.204-21(c)). **No** DFARS 252.204-7012, no Controlled Unclassified Information (CUI), and no DFARS 252.246-7008 or FAR 52.246-26 |
| CMMC trigger | On 2026-06-15 the prime told the owner that its new DoD task order contains DFARS 252.204-7021 at CMMC Level 1 (Self). Before it places purchase orders under that task order, the prime must ensure the owner has a current CMMC Level 1 (Self) status and affirmation in the Supplier Performance Risk System (SPRS) (252.204-7021(d)(4) and (f)(2); 32 CFR 170.23(a)(1)). The prime set **2026-10-30** as the owner's deadline |
| Federal Contract Information (FCI) | The asset tag lists, serial-to-tag-to-building spreadsheets, and building delivery schedules the owner receives from or generates for the prime. They are "not intended for public release" and are generated for the Government under a contract (FAR 52.204-21(a)). Prices and invoice payment details alone are simple transactional information and are not FCI |
| Registrations | Unique Entity ID and CAGE code obtained through SAM registration in 2025-02 at the prime's request. No SPRS account yet. No GSA Schedule and no federal prime contract |
| Suppliers | 2 authorized distributors (about 90% of purchase spend). 1 online B2B marketplace (about 7%) and 2 independent brokers (about 3%) used for end-of-life optics, power supplies, and legacy switch modules. The owner is a registered entry-tier partner in 3 OEM partner programs, which give access to the OEMs' serial number and warranty lookup portals |
| Not in scope | NIST SP 800-171 Rev. 2, CMMC Level 2, and DFARS 252.204-7012 (no CUI and no clause; see P03). SEC disclosure rules (not a public company). CCPA/CPRA (no California business; far below every threshold). CTPAT (voluntary; not an importer of record). Trade Agreements Act (no GSA Schedule or federal prime contract; the owner answers the prime's country-of-origin questions from distributor data). Payment cards are taken only through the invoicing vendor's hosted payment page |
| State law approach | Florida law is cited only where unavoidable (Fla. Stat. 501.171: a "covered entity" expressly includes a sole proprietorship). Otherwise the samples stay federal |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner | Every role: owner, security and compliance lead, risk acceptor, incident lead, purchaser, staging technician, and the **CMMC Affirming Official** (32 CFR 170.22(a)(1)) |
| On-call IT consultant | Hourly help with the laptop, home network, and this self-assessment. No standing access; remote sessions only when the owner starts and watches them. Confidentiality agreement signed 2026-07-30 |
| Bookkeeper (contract) | Monthly reconciliation and year-end tax preparation through a named, read-only accountant user in the accounting SaaS |
| Prime's subcontracts manager | The prime's contact for purchase orders, delivery schedules, and any report the BPA requires (customer, not staff) |

## 3. Systems
| ID | System | Hosting | Holds FCI? | Notes |
|---|---|---|---|---|
| SYS-01 | Accounting, invoicing, and inventory SaaS (quotes, sales orders, purchase orders, stock and serial numbers, invoices with hosted payment links) | Vendor SaaS | Yes (DoD order notes and asset tag references) | The order management system of record. Vendor has a SOC 2 Type 2 report. MFA available but **off** |
| SYS-02 | Business email, calendar, and cloud file storage suite (small-business plan) | Vendor SaaS | Yes | MFA on, using SMS text codes. Files shared by "anyone with the link" |
| SYS-03 | Distributor reseller portals (2) and OEM partner portals (3) | Vendor SaaS | Limited (prime purchase order numbers on order lines) | Distributor A enforces MFA. **Distributor B offers no MFA** |
| SYS-04 | Online B2B marketplace buyer account and broker purchasing by email | Vendor SaaS; email | No | Paid by business credit card or wire transfer |
| SYS-05 | Business laptop | Owner device | Yes | Built-in full-disk encryption on; built-in antivirus; automatic updates. Owner signs in with a **local administrator account** every day. Also used with a console cable to stage devices |
| SYS-06 | Mobile phone | Personal device | Yes (business email) | Passcode; encrypted by default; receives SMS sign-in codes |
| SYS-07 | Home network | ISP-provided router and Wi-Fi in the residence | Yes (in transit) | Shared with household devices (TVs, game consoles, cameras) |
| SYS-08 | Garage staging bench and stock cabinet | Owner premises | Yes (printed asset tag sheets and labels) | Test switch, label printer, console cables; locked steel cabinet for stock and staged DoD equipment |
| SYS-09 | Business bank account and business credit card online | Bank SaaS | No | Bank-enforced MFA |
| SYS-10 | Consumer generative AI assistant (paid individual plan) | Vendor SaaS | **Yes (pasted sales history)** | Used for demand forecasting, reorder lists, and drafting emails. Chat history used for model training by default (setting on). See P10 |

**SSP system (P02):** the *Reseller Order Desk (ROD)*: SYS-01 to SYS-10, the owner's SaaS stack, devices, home network, and garage staging bench used to quote, buy, stage, deliver, and bill. SYS-01, SYS-02, SYS-03, SYS-05, SYS-06, SYS-07, and SYS-08 (and SYS-10 until FCI is removed from it) also form the CMMC Level 1 assessment scope for the FCI stream (32 CFR 170.19(b)).

## 4. Current security posture: informal (basic hygiene, big gaps)
**In place today:**
- Built-in full-disk encryption on the laptop; passcode and default encryption on the phone
- Built-in antivirus with real-time scanning and automatic updates; automatic operating system and browser updates on the laptop and phone
- MFA on distributor portal A, the bank, and email (SMS codes)
- About 90% of purchases from two authorized distributors; DoD orders bought from distributor A only (practice, not written)
- Registered OEM partner accounts with serial number lookup
- The accounting SaaS vendor's SOC 2 Type 2 report and vendor-run backups
- Unique named accounts in every service; the bookkeeper has an own read-only account
- A locked steel cabinet in the garage for stock and staged DoD equipment
- Asset tags applied and a serial-to-tag list kept for every DoD delivery

**Missing:**
1. No written security policy, risk assessment, or incident plan. The CMMC Level 1 self-assessment has never been done, and there is no status or affirmation in SPRS (prime deadline 2026-10-30).
2. MFA is off on the accounting and inventory SaaS (the owner's account is its administrator). Distributor portal B offers no MFA. The same password is reused across 4 services, with no password manager.
3. The owner uses a local administrator account for daily work on the laptop.
4. The home network is shared with household devices on one flat Wi-Fi network.
5. Marketplace and broker purchases (about 10% of spend) get no authenticity checks: no OEM serial validation, packaging or seal inspection, or firmware verification. There is no written sourcing rule or broker vetting.
6. No Section 889 screening. The owner relies on memory of brand names and does not check white-label or rebranded products. The substance of FAR 52.204-25 is not in the owner's own purchase orders for DoD-bound items.
7. Supplier wire instructions and bank-detail changes are accepted by email with no call-back. On 2026-05-19 the owner paid a $2,340 broker invoice to a fraudulent account after the broker's mailbox was compromised; nothing was recovered.
8. FCI and quotes are shared by "anyone with the link" file links that never expire, including 14 asset tag spreadsheets sent to the prime.
9. FCI was pasted into a consumer generative AI assistant with model training on (P10).
10. Admin passwords for about 30 customer network devices are kept in a spreadsheet in cloud storage.
11. No backup of the laptop or the cloud file storage beyond the provider's recycle bin.
12. No media sanitization method or record. The old phone was traded in at the carrier in 2026-02 with no recorded wipe, and 2 trade-in switches in stock still held customer configurations (found 2026-08-05).
13. Household members can enter the garage. The cabinet key hangs on the house key hook, and the garage keypad code (also known to a dog walker) has never been changed. No record of drivers or customers who enter the garage.
14. A photo of a staged DoD pallet showing asset tags and building delivery labels was posted on the business social media page in 2026-04 (removed 2026-08-04).
15. No security training beyond OEM partner sales training; no anti-counterfeit training.
16. Single point of failure: nobody else can reach the accounts, the stock, or the prime.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Primary: FAR 52.204-21 (15 basic safeguarding requirements) as assessed under CMMC Level 1 (Self) (32 CFR 170.15; DFARS 252.204-7021). Plus the CMMC Level 1 procedure duties and a supply chain clause check (FAR 52.204-25, FAR 52.204-23). The registry's primary regulation (NIST SP 800-171 Rev. 2 via CMMC Level 2 and DFARS 252.204-7012) is documented as not applicable at this size because the owner handles no CUI |
| P08 incident | Supplier compromise introducing counterfeit or tampered products: a marketplace seller or broker ships counterfeit or tampered network products, including a supplier mailbox used to redirect payment |
| P09 SOC 2 | Security criteria only. The owner's self-check, plus a review of the accounting and inventory SaaS vendor's SOC 2 Type 2 report. A self-attestation answers the prime's supplier questionnaire |
| P10 AI | One third-party tool: the consumer generative AI assistant, used for demand forecasting and reorder suggestions (AI-001) and drafting customer emails (AI-002) |
| Cloud | SaaS only. No IaaS or PaaS |
| Supply chain practice | NIST SP 800-161 Rev. 1 (upd1) as the benchmark (source SRC-800-161), scaled down to SP 800-53 SR-3, SR-5, and SR-11 |
| Registry defaults adapted | Primary system: a sole proprietor runs no ERP, warehouse management system, or reseller portal, so the "order management, warehouse, and reseller portal (ERP)" is the accounting and inventory SaaS plus the distributor portals. AI use case: no forecasting add-on and no automated reordering exist; the owner uses a general-purpose AI assistant for forecasts and places every order by hand |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-15 | Prime's notice: CMMC Level 1 (Self) status and affirmation required by 2026-10-30 |
| 2026-08-03 to 2026-08-07 | Self-assessment (BIA, system profile, risk, gaps) by the owner, with the on-call IT consultant on 2026-08-05 and 2026-08-06 (control tests on 2026-08-06) |
| 2026-08-31 | Deliverables adopted by the owner |
| 2026-10-15 | Target: all 15 FAR 52.204-21 requirements met |
| 2026-10-23 | Final CMMC Level 1 self-assessment with the IT consultant |
| 2026-10-30 | Level 1 (Self) results and affirmation entered in SPRS (prime deadline) |
| 2027-08 | Annual self-assessment and affirmation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Volumes | About 60 quotes, 40 orders, and 25 drop shipments a month. About 30 devices a month staged for the prime. About $12,000 of stock at cost in the cabinet | P05, P01 |
| Insurance | A business owner's policy with a data breach endorsement ($25,000 sublimit). Social engineering and funds transfer fraud are not covered (confirmed with the agent 2026-08-04) | P01, P08 |
| Counterfeit optics (P07 test) | On 2026-08-06 the owner checked 12 serial numbers from 2026 marketplace and broker purchases in the OEM partner portals. 10 were valid. 2 optical transceivers from a lot of 8 bought from one marketplace seller on 2026-06-10 returned "not found". The other 6 had been sold to 2 commercial customers. None went on a DoD order. The OEM confirmed on 2026-08-20 that the 2 serials are cloned (counterfeit). Worked example in P08 | P07, P01, P08 |
| Home router (P07 new finding) | On 2026-08-06 the ISP-provided router still had its default admin password, remote management from the internet on, and firmware about 2 years old. The owner changed the password and turned remote management off the same day | P07, P01, P03, P04 |
| BPA reporting terms | The BPA names the prime's subcontracts manager as the recipient of any FAR 52.204-25(d) or 52.204-23(c) report and of any notice of a suspected counterfeit or nonconforming item delivered on the prime's orders (within 2 business days, a BPA term). The prime reports to DoD through DIBNet | P03, P08 |
| AI assistant use | Used since 2026-01. In 2026-05 and 2026-07 the owner pasted 18 months of sales history (about 900 lines, including 52 DoD order lines with asset tag ranges and building names) to forecast demand. The assistant once suggested a marketplace seller for an end-of-life optic. Every order is still placed by hand | P10, P01, P03 |
| Accounting SaaS assurance | The vendor's SOC 2 Type 2 report (Security and Availability, 12 months ending 2026-03-31, unqualified) was reviewed on 2026-08-05. Stated RPO 24 hours, RTO 8 hours | P02, P05, P09 |
| Asset inventory | SYS-01 to SYS-10 plus 2 old laptops kept in a drawer (not wiped) | P02, P07 |

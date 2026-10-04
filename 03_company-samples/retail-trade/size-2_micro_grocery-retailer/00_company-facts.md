# Scenario facts: Cris Santos Company | Retail Trade | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the payment provider, the merchant agreement, the insurer, and other vendors are fictional.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (neighborhood grocery store with online ordering) |
| Business | Neighborhood grocery retailer (NAICS 445110): **one store** of about 4,500 square feet (produce, dairy, frozen, packaged groceries, and a small prepared-foods case stocked by a local supplier), plus **online ordering** for curbside pickup and local delivery within about 5 miles. The registry describes the business as "stores and online ordering"; at the Micro size the company runs one store |
| Location | Florida. One store, open 8:00 to 20:00 every day |
| Ownership and form | Limited liability company, privately held by its owner (sole member) |
| Workforce | 7 employees: the Owner (works full time as general manager), 1 Store Manager, 1 part-time Bookkeeper, 2 Cashiers, 1 Stock and Produce Clerk, 1 Order Picker and Delivery Driver |
| Revenue | About $1.1 million a year (fictional), about $3,000 per day. Online orders are about 9% of sales (about 1,700 orders a year, about 5 a day, average about $55). Under the SBA standard of $40.0 million for NAICS 445110 (13 CFR 121.201), so SBA-small |
| Card acceptance | About 31,000 card transactions a year: about 29,300 in the store on 2 countertop terminals, about 1,450 online at checkout, and about 250 on a mobile card reader for pay-on-delivery and curbside orders. The company does not take card numbers by phone, mail, or email |
| SNAP | The store is an FNS-authorized SNAP retailer (7 CFR 278.1; authorizations run for 5 years). About 4,000 SNAP EBT transactions a year, in the store only, on the same countertop terminals. Online orders cannot be paid with SNAP |
| Customers | About 2,400 loyalty members in the platform's customer directory (name, phone number, optional email, purchase history) and about 850 online store accounts (name, email, phone, delivery address, order history; passwords handled by the platform) |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 (PCI SSC) applies through the merchant agreement with the payment provider. It is a contractual standard, not law. In a compliance notice in the merchant dashboard dated 2026-06-10 (fictional), the provider asked for an annual self-assessment using **SAQ P2PE** for the store and **SAQ A** for the online store, with attestations due 2026-11-30. Visa sets merchant levels by total Visa transaction volume over 12 months, and acquirers must make sure their merchants validate at the right level (Visa Account Information Security Program page, checked 2026-10-04). The level thresholds were not verified, so these documents do not state the company's level |
| Scope reduction (why the cardholder data environment is small) | **In the store:** the 2 countertop terminals belong to the provider's **validated, PCI-listed P2PE solution**. Card data is encrypted inside the terminal and only the provider can decrypt it. The dashboard's virtual terminal (typing card numbers on a computer) is turned off. SAQ P2PE eligibility requires that all payment processing for the channel goes through the validated P2PE solution and that the merchant follows the P2PE Instruction Manual (SAQ P2PE v4.0.1, eligibility criteria). **The mobile card reader is not part of the P2PE solution** (see gap 1). **Online:** the online store is built and hosted on the provider's platform. Card fields on the checkout page are served by the provider inside a frame, and the company receives only tokens and truncated card numbers. Scripts that the company adds to its pages still run on the checkout page (see gap 2) |
| Not in scope | **Pharmacy and HIPAA:** the store has no pharmacy (Owner decision, confirmed), so it is not a HIPAA covered entity. **FTC Safeguards Rule and Red Flags Rule:** no store credit, house charge accounts, or deferred payment (no covered accounts). **CCPA:** the company does not do business in California and is far below the revenue threshold. **COPPA:** the online store is not directed to children; loyalty sign-up asks members to confirm they are 18 or older. **INFORM Consumers Act:** no third-party sellers. **SEC disclosure:** privately held. **Facial recognition:** the cameras only record. **SNAP program rules** are not analyzed; EBT cards are not payment-brand cards, so PCI DSS does not govern them, but they are read on the same P2PE terminals and benefit from the same terminal checks |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a), (n)) for customer data security, privacy statements, and pricing and offer claims; FACTA receipt truncation (15 U.S.C. 1681c(g)); Florida breach notification, reasonable security, and record disposal (Fla. Stat. 501.171(2), (3)-(6), (8)); Florida price gouging during a declared state of emergency (Fla. Stat. 501.160) for the AI markdown and offer feature (P10) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable. Other states are treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Owner | Sole member and general manager. Approves policies and spending; accepts Moderate and higher risks; signed the 2025 SAQs; decision maker in incidents; decides on the AI feature (P10) |
| Store Manager | Designated **Security and PCI Lead** in writing (2026-07-15). Manages platform and online store users, terminal checks, staff training, and the risk register; incident lead. Also operates most of the controls (overlap compensated by MSP evidence, the provider's assurance reports, and an independent assessor in P07) |
| Bookkeeper (part-time) | Merchant statements, the provider's compliance notices, vendor contracts, the cyber insurance policy, and the payroll service; backup incident contact |
| Cashiers (2) | Checkout and loyalty sign-up; first to notice a tampered terminal |
| Stock and Produce Clerk | Receiving, counts, and near-date markdowns (P10 user) |
| Order Picker and Delivery Driver | Picks online orders, delivers, and takes pay-on-delivery payments on the mobile reader |
| Managed service provider (MSP, external) | Local IT provider on a monthly plan: help desk, patching and antivirus on the office PC and Owner laptop, the store firewall and Wi-Fi, email administration, and the office PC cloud backup. 4-business-hour response; no recovery time commitment |
| Marketing freelancer (external) | Built the online store design in 2024; adds marketing scripts through the platform's custom code setting; holds an online store administrator login |
| Payment and commerce platform provider (external) | One provider supplies the POS software, the P2PE terminals and mobile reader, card processing, the online store, the loyalty directory, and the AI offers and markdown feature. A PCI DSS validated service provider |

## 3. Systems

| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Commerce platform: POS app, back office dashboard (items, prices, sales reports, customer directory and loyalty, employee logins and POS codes), and card processing | Vendor SaaS | About 2,400 loyalty members; truncated card numbers and tokens only | Dashboard administrators: Owner (MFA on) and Store Manager (no MFA). Staff use 4-digit POS codes; **the 2 Cashiers share one code** (see gaps). Provider supplies a service provider AOC and a SOC 2 Type 2 report in its trust portal |
| SYS-02 | Online store: catalog, customer accounts, ordering, pickup and delivery scheduling, provider-hosted checkout | Vendor SaaS (same provider) | About 850 online accounts; **no card numbers** | The custom code setting adds 4 third-party scripts to every page, including checkout (see gaps). Administrators: Owner, Store Manager, marketing freelancer (password only) |
| SYS-03 | Card terminals: 2 countertop terminals in the provider's PCI-listed P2PE solution, and 1 mobile Bluetooth card reader paired with the store smartphone | Provider devices | Card data encrypted in the countertop terminals; EBT on the countertop terminals | The mobile reader is **not** part of the P2PE solution. No device list or inspection records |
| SYS-04 | Productivity suite (email and files) | SaaS | Customer emails in the shared orders mailbox; a loyalty export spreadsheet (see gaps) | 4 mailboxes: Owner, Store Manager, Bookkeeper, and a shared orders mailbox. MFA on the Owner's mailbox only |
| SYS-05 | Endpoints | On-premises | Cached exports on the office PC | 1 office PC (back office), 1 Owner laptop (both MSP-managed), 2 POS tablets on counter stands (provider app in locked mode), 1 store smartphone (order alerts, mobile reader, delivery navigation; not managed) |
| SYS-06 | Store network | On-premises | Encrypted card data in transit only | MSP-managed small-business firewall with Wi-Fi. One staff Wi-Fi carries the terminals, tablets, office PC, store phone, cameras, and temperature sensors; customer guest Wi-Fi is separated (internet only) |
| SYS-07 | Accounting SaaS and outside payroll service | SaaS | Employee and supplier data | Daily sales summary synced from SYS-01 |
| SYS-08 | Refrigeration temperature monitoring | Wireless sensors with a vendor cloud app | No | 6 sensors; alerts to the Owner's and Store Manager's phones; on the staff Wi-Fi |
| SYS-09 | CCTV | On-premises recorder with a remote viewing app | Video | 8 cameras; no facial recognition; 21-day retention |
| SYS-10 | AI offers and markdown suggestions | Vendor SaaS feature inside SYS-01 | Loyalty purchase history; item sales, cost, and stock | Turned on by the Owner in April 2026 (P10) |
| SYS-11 | Cloud backup of the office PC | SaaS, resold and run by the MSP | Supplier spreadsheets, shelf-tag templates, the loyalty export (see gaps) | Nightly; 30 days of versions; never restore-tested |

**SSP system (P02):** the *Store Commerce Platform (SCP)*: SYS-01, SYS-02, SYS-03, and SYS-10, with the endpoints (SYS-05) and store network (SYS-06) that run and manage them, and interfaces to SYS-04, SYS-07, and SYS-11.

## 4. Current security posture: informal, with basic hygiene and big gaps

**In place today:**
- Validated P2PE countertop terminals for in-store card and EBT payments; the dashboard virtual terminal is turned off
- Provider-hosted card fields on the online checkout page; the company never receives card numbers online
- Receipts show only the last 4 digits of the card number and no expiration date (FACTA)
- MFA on the Owner's dashboard and email accounts
- MSP patching, antivirus, and firewall for the office PC and Owner laptop
- Guest Wi-Fi separated from the staff Wi-Fi
- Provider's service provider AOC and SOC 2 Type 2 report available in its trust portal (not reviewed until this engagement)
- Cyber liability coverage with a 24x7 breach hotline
- Nightly cloud backup of the office PC (SYS-11)

**Missing or weak, found in the 2026 assessments:**
1. The 2025 SAQs were completed online by the Owner in one sitting, with no scope review. **SAQ P2PE was attested even though the mobile card reader used for pay-on-delivery is not part of the P2PE solution**, and the SAQ A statement that the site is not susceptible to script attacks was attested without evidence. There is no written PCI DSS scope.
2. Four third-party scripts (a social media tracking pixel, a chat widget, a product review widget, and a coupon pop-up) run on every online store page, including checkout, through the custom code setting. Nobody keeps a list, approves changes, or watches the checkout page. The marketing freelancer can add or change scripts at any time.
3. The marketing freelancer's online store administrator login has full rights and no MFA. The Store Manager's dashboard and email logins have no MFA. The Bookkeeper's mailbox and the shared orders mailbox have no MFA.
4. The 2 Cashiers share one POS code. A former cashier's POS code (left 2026-03) was still active at fieldwork.
5. No list of terminals and no tamper inspections. Cashiers have never been shown what a tampered terminal looks like.
6. One flat staff Wi-Fi for terminals, tablets, the office PC, the store phone, cameras, and sensors. The Wi-Fi password has not changed since 2023 and is known to former employees.
7. No written security policies and no incident response plan. Nobody knew the merchant agreement's notice term: notify the provider within 24 hours of suspecting a card data compromise (fictional term).
8. No security training. Phishing has never been discussed with staff.
9. A full loyalty export (2,400 members) made for a 2025 email campaign still sits in the shared orders mailbox and on the office PC, and the marketing freelancer received a copy by email. No agreement with the freelancer covers data use or security.
10. The store smartphone is unmanaged, uses a 4-digit code shared by staff, and runs the mobile reader app and order alerts.
11. The CCTV recorder still uses its default administrator password and is reachable from the internet through a port opened for the remote viewing app.
12. The online store privacy notice is a 2024 template that says customer information is "never shared", while the freelancer and the AI feature use it.
13. The AI offers and markdown feature was turned on in April 2026 without a review of the provider's data use terms, customer disclosure, or fairness.
14. No list of service providers with their PCI DSS responsibilities, and nobody had read the provider's AOC.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 primary regulation | PCI DSS v4.0.1 (contractual standard), with FTC Act Section 5 as the secondary regulation and a one-row FACTA check |
| P08 incident | Payment card data compromise through e-commerce skimming: the chat widget's vendor is compromised and its script, loaded on the checkout page through the custom code setting, overlays a fake card form. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Availability. SOC 2 is **not** the company's assurance mechanism (PCI DSS validation is). The readiness check is an internal benchmark used to answer the cyber insurer's renewal application (due 2026-10-15), plus a review of the provider's SOC 2 report |
| P10 AI | **Adapted from the registry default "Dynamic pricing and personalized offers".** A store of this size does not run a dynamic pricing engine. It uses the commerce platform's built-in AI feature (SYS-10), which suggests personalized loyalty offers and markdown prices for near-date items. Staff approve each suggestion before it takes effect. The pricing and offer risks are the same in kind (FTC Section 5 claims and fairness, emergency pricing), at a smaller scale |
| Cloud | SaaS plus one cloud workload: the MSP-run cloud backup of the office PC (SYS-11). Vendor-agnostic |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-10 | Provider compliance notice: SAQ P2PE and SAQ A due 2026-11-30 |
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis fieldwork (Store Manager with the MSP technician) |
| 2026-08-10 to 2026-08-12 | Control assessment (independent consultant) |
| 2026-08-24 to 2026-08-26 | SOC 2 readiness self-assessment, provider report review, and AI assessment |
| 2026-08-31 | Deliverables approved by the Owner |
| 2026-10-15 | Cyber insurance renewal application due |
| 2026-11-30 | 2026 SAQs and attestations due to the provider |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Former cashier | Left on 2026-03-14. The personal POS code was found active on 2026-07-21 and disabled that day. The POS activity report showed no sign-ins after the last shift | P01, P03, P07 |
| Scripts | The coupon pop-up script came from a vendor the freelancer stopped using in 2025 and still loads from that vendor's server | P01, P03, P08 |
| Internet | One business internet line with no failover. The countertop terminals need the internet to authorize cards | P01, P05 |
| Cyber insurance | Cyber liability endorsement on the business owner's policy (fictional limit $250,000) with a 24x7 breach hotline and panel counsel and forensics; the policy requires prompt notice and use of panel vendors | P08, P09 |
| Finances and payroll | A cash reserve covers about 3 weeks of expenses; payroll runs biweekly through the outside payroll service | P01, P05 |
| Assessor | The P07 assessor is an independent security consultant (not a QSA) on a fixed fee, not involved in the risk or gap analysis and operating no control | P07 |
| Hurricane | The store closed for 2 days in 2024 for a hurricane; the Owner moved the laptop and the store phone home | P01, P05 |

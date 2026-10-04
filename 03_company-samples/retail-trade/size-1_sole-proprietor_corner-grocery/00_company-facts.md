# Scenario facts: Cris Santos Company | Retail Trade | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the processor, the merchant agreement, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C and does business under the store's trade name) |
| Business | Corner grocery (NAICS 445110): one neighborhood store of about 1,500 square feet selling produce, dairy, bread, a small meat and deli case, staples, and Caribbean and Latin American specialty foods. **Online ordering** for in-store pickup and local delivery (within about 2 miles, delivered by the owner), and **phone orders** from regular customers for delivery |
| Location | Florida. One leased storefront on the ground floor of a mixed-use building. Open Monday to Saturday, 8:00 to 19:00 (about 310 days a year); closed Sunday |
| Workforce | The owner only (0 employees). A family member helps at the register, unpaid, on Saturday afternoons and while the owner makes deliveries (about 8 hours a week). The family member is not an employee but follows the same rules (POL-01) |
| Revenue | About $180,000 a year (fictional), about $580 per open day. SBA-small (standard $40.0 million for NAICS 445110; 13 CFR 121.201) |
| Tender mix | About 12,500 sales a year. Cards are about 60% of sales: about 7,000 card transactions a year (about 6,300 in store on the terminal, about 360 online orders, and about 300 phone orders keyed into the terminal). SNAP EBT is about 20% of sales, on the same terminal. Cash is the rest |
| Customers | About 240 online store accounts (name, email, phone, delivery address, order history). About 45 regular phone-order customers, many of them older neighbors |
| PCI DSS status | **Merchant.** The merchant agreement with the payment processor (a merchant services provider acting for its acquiring bank) requires compliance with PCI DSS v4.0.1 and card brand rules. PCI DSS is a contractual standard, not law (N44-45-R01). The processor's PCI compliance portal (run by a compliance vendor) asks for an annual self-assessment. When the owner answered its screening questions in 2024, the portal assigned **SAQ B-IP** for the countertop terminal and **SAQ A** for the online store (fictional). The owner never completed either SAQ, and the processor has charged a **monthly PCI non-compliance fee of $29.95 since March 2024** (fictional). The owner's screening answers did not mention phone orders or the paper order pad. The processor has not stated a merchant level, and these documents do not state one |
| How card data flows | **In store:** a countertop terminal supplied by the processor reads chip, contactless, and PIN debit cards and sends them over the store's internet connection (wired to the router) to the processor. The terminal is not part of a PCI-listed P2PE solution. **Online:** the online store's checkout **redirects** the customer to the processor's hosted payment page. Card data goes from the customer's browser to the processor; the online store receives only an approval and the last four digits. The online store still controls where the "Pay now" button sends the customer. **Phone orders:** the owner writes the card number, expiration date, and security code on a paper order pad and keys them into the terminal when the order is packed |
| SNAP | Authorized SNAP retailer (7 CFR 278.1). EBT cards run on the processor's terminal. The online store does not accept SNAP; SNAP customers who order online pay at pickup. Under 7 CFR 278.2(b), SNAP benefits (which include EBT cards, 7 CFR 271.2) must be accepted for eligible foods at the same prices and on the same terms as cash purchases |
| Not in scope | **Pharmacy and HIPAA:** no pharmacy. **FTC Safeguards Rule and Red Flags Rule:** the store does not issue credit, keep customer tabs, or offer deferred payment (no covered accounts; it stopped keeping a paper tab book in 2023). **CCPA:** no California business and revenue far below the threshold. **COPPA:** the online store is not directed to children and its terms require account holders to be 18 or older. **INFORM Consumers Act:** no third-party sellers. **SEC:** not a public company. **Facial recognition:** the store's cameras do not use it |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a), (n)) for customer data security, the online privacy notice, and pricing claims (N44-45-R02); FACTA receipt truncation (15 U.S.C. 1681c(g), N44-45-R05); Florida Information Protection Act, Fla. Stat. 501.171, whose "covered entity" expressly includes a sole proprietorship (501.171(1)(b)): reasonable measures (2), breach notice (3)-(6), and disposal of customer records (8); Florida price gouging statute, Fla. Stat. 501.160, during a declared state of emergency (P10) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (data security, breach notice, disposal, price gouging). Customers from other states are treated generically ("each state where affected individuals reside") |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner | Every role: owner, security and privacy lead, PCI DSS contact, incident lead, and risk acceptor |
| Family member (unpaid helper) | Runs the register about 8 hours a week. Uses the owner's POS app PIN (see gaps). No access to email, the online store, or the merchant portal |
| Outside IT helper | Independent computer repair technician, paid by the hour. Set up the router in 2022. No standing access; works only in person or in sessions the owner starts |
| Payment processor | Countertop terminal, EBT processing, hosted payment page, merchant portal, and the PCI compliance portal. A PCI DSS validated service provider (its attestation of compliance was requested on 2026-08-11; see section 7) |
| Website builder vendor | Hosts the online store (catalog, customer accounts, ordering, pickup and delivery slots) |
| POS app vendor | Cloud point-of-sale and inventory app on the store tablet (barcode scanning, item and price file, sales totals). Not connected to the card terminal |
| Internet service provider | Business internet service and the ISP-supplied router with Wi-Fi |
| Wholesale grocery distributor | Online ordering portal; deliveries on Tuesday and Friday |
| Tax preparer | Read-only accountant access to the accounting SaaS at tax time |

## 3. Systems
| ID | System | Hosting | Card or personal data? | Notes |
|---|---|---|---|---|
| SYS-01 | Online store (catalog of about 350 items, customer accounts, ordering, pickup and delivery slots) | Website builder SaaS | About 240 customer accounts; **no card data** (checkout redirects to SYS-02) | One administrator account (the owner's), password only, password reused from the owner's email. Four add-ons installed by the owner (chat widget, analytics, reviews, promotional pop-up), never reviewed. A "custom code" setting lets the administrator add scripts to store pages |
| SYS-02 | Payment processor services: countertop terminal, EBT, hosted payment page, merchant portal, PCI compliance portal | Service provider; terminal on the counter | Card data (processor side and inside the terminal) | Terminal is a PCI PTS-approved device that the processor updates remotely; IP connection through the store router. Keyed entry is used for phone orders. Merchant portal shows truncated card numbers only and enforces MFA |
| SYS-03 | POS and inventory app on the store tablet, with a barcode scanner and receipt printer | Vendor SaaS | Sales totals; no card data | The owner keys each card sale total into the terminal. One login PIN shared by the owner and the family member. Vendor backs up the data |
| SYS-04 | Email and cloud file storage | Consumer SaaS (the owner's personal account) | Yes: online order notices, processor statements, supplier invoices, and a monthly export of online customers (spreadsheet) | No MFA. Business and personal mail mixed |
| SYS-05 | Laptop and smartphone | Owner devices (personal) | Yes: customer exports on the laptop; email, store admin app, and merchant portal app on the phone | Laptop shared with family, no full-disk encryption, owner uses an administrator account daily. Phone holds the merchant portal second factor and texts with phone-order customers |
| SYS-06 | Store network | ISP-supplied router with Wi-Fi | Card data in transit (terminal traffic, encrypted by the terminal and processor) | One flat network: the terminal (wired), tablet, laptop, cameras, and customers' phones (Wi-Fi password printed on a sign at the register). Router administrator password unchanged since 2022 |
| SYS-07 | Accounting SaaS | Vendor SaaS | Business financial data; no customer card data | MFA on. Bank feed connected |
| SYS-08 | Cloud security cameras (2) | Consumer cloud camera service | Video (14-day cloud retention) | No facial recognition. The camera over the register can see the terminal keypad |
| SYS-09 | Consumer generative AI chatbot (free personal plan) | Vendor app and website | Yes, since May 2026: customer names, emails, and order histories pasted into chats | Used weekly for price suggestions and personalized offer emails (P10) |
| SYS-10 | Paper phone-order pad | Drawer under the register | **Full card number, expiration date, and security code** with name and address | Kept until the order is delivered, then torn off and put in the regular trash |

**SSP system (P02):** the *Store Sales Platform*: the store's e-commerce and point-of-sale platform, SYS-01 to SYS-10.

## 4. Current security posture: early (few formal controls)
**In place today:**
- A PCI PTS-approved countertop terminal from the processor, updated remotely by the processor
- Online card payments only on the processor's hosted payment page (redirect); the online store never receives card numbers
- Receipts show only the last 4 digits and no expiration date (FACTA)
- MFA enforced on the processor's merchant portal; MFA on the accounting SaaS
- Automatic updates on the laptop, phone, and tablet; built-in antivirus on the laptop
- The website builder and POS app vendors back up their own data
- Store alarm; the tablet is locked in the back room at night

**Missing:**
1. No PCI DSS self-assessment has ever been completed. The processor has charged a monthly non-compliance fee since March 2024. There is no PCI scope description, and the portal's SAQ assignment was based on answers that left out phone orders.
2. Phone-order card numbers, expiration dates, and **security codes** are written on a paper pad, kept in an unlocked drawer, and thrown in the regular trash.
3. The online store administrator account has no MFA (available but off) and reuses the email password. Four add-ons and the custom code setting have never been reviewed.
4. One flat network: customers' phones, the card terminal, the tablet, the laptop, and the cameras share it. The router administrator password is unchanged.
5. The owner's POS app PIN is shared with the family member.
6. The terminal is never inspected for tampering, and its serial number is not recorded.
7. Email is a personal consumer account with no MFA. It receives customer data and can reset the online store password.
8. The laptop is shared with family, has no full-disk encryption, and the owner works from an administrator account.
9. No backup of the laptop's files or customer exports.
10. No incident plan. The owner does not know the merchant agreement's notice term (notify the processor within 24 hours of suspecting a card data compromise; fictional term).
11. No written policies and no security training; the family member has never been shown what a skimmer looks like.
12. A consumer generative AI chatbot has received customer data, and its price suggestions are applied without a written check.
13. The camera over the register can record PIN entry on the terminal keypad.
14. No cyber insurance. The business owner's policy has not been checked for data breach coverage.
15. Single-person dependency: the owner holds every credential, and the merchant portal's second factor is on the owner's one phone.
16. The online store's privacy notice is the website builder's default template. It says customer information is "never shared", which is not accurate (analytics add-on, AI chatbot).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 primary regulation | PCI DSS v4.0.1 (contractual standard), with FTC Act Section 5 rows, one FACTA row, and two Fla. Stat. 501.171 rows (reasonable measures and disposal) |
| P08 incident | Payment card data compromise through e-commerce skimming, **adapted to a redirect checkout**: an attacker takes over the online store administrator account and adds a script that shows a fake card form before sending the customer on to the real hosted payment page. The registry's default (a skimming script on a checkout page that hosts the payment form) does not fit, because this store's checkout redirects; the account takeover path is how a redirect merchant is skimmed |
| P09 SOC 2 | SOC 2 is not the store's assurance mechanism (PCI DSS validation is). (a) Security-criteria self-check as a structured checklist; (b) review of the website builder's SOC 2 report and the processor's PCI DSS attestation of compliance |
| P10 AI | **Adapted:** the registry use case "Dynamic pricing and personalized offers" is carried out with a consumer generative AI chatbot (SYS-09), because a corner grocery does not buy a pricing engine. The owner pastes sales and customer order data into the chatbot to get weekly price suggestions and personalized offer emails |
| Cloud | SaaS only. No IaaS or PaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-30 | Processor's portal reminder that the SAQs are overdue and the fee continues |
| 2026-08-10 to 2026-08-14 | Self-assessment (BIA, system profile, risk register, gap analysis, control tests) with the outside IT helper, after store hours; control tests on 2026-08-13 |
| 2026-08-24 | AI use review (P10) |
| 2026-09-04 | Deliverables adopted by the owner |
| 2026-11-30 | Target to complete both SAQs in the processor's portal and stop the non-compliance fee |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Paper pad count | On 2026-08-11 the order pad held 23 pages with card details from orders between 2026-06-22 and 2026-08-10. Pages from delivered orders had gone into the regular trash. The owner shredded the 23 pages with a borrowed cross-cut shredder on 2026-08-11 and now writes only the order on the pad (card details are keyed directly while the customer is on the phone) | P01, P03, P07 |
| Terminal default password | Control testing on 2026-08-13 found that the terminal's manager password (used for refunds and settings) was still the factory default printed in the quick-start guide. The owner changed it that day | P01, P03, P07 |
| Router | The router's administrator password was the default printed on the router label. The router supports a separate guest network, which was not turned on | P02, P04, P07 |
| Processor assurance | The owner requested the processor's PCI DSS attestation of compliance on 2026-08-11 and received it on 2026-08-12 (service provider AOC dated 2026-02; fictional) | P09 |
| Website builder assurance | The website builder publishes a SOC 2 Type 2 report (Security and Availability, 12 months ending 2026-03-31) in its trust portal after a click-through nondisclosure agreement. The owner downloaded and reviewed it on 2026-08-12 | P02, P09 |
| Add-on review | The four online store add-ons were reviewed on 2026-08-12. The promotional pop-up add-on had permission to add scripts to every page, including checkout; the owner removed it on 2026-08-12. The chat widget and reviews add-on are kept off the checkout pages | P01, P04, P07 |
| AI chatbot use | The owner used the chatbot from 2026-05-04. Four monthly customer exports (about 240 customers each) were pasted into chats. Model training on chats was on (the free plan's default) | P01, P10 |
| Weekly volumes | About 7 online orders and about 6 phone orders a week | P05, P08 |
| Cyber insurance | The business owner's policy was checked on 2026-08-14: it has no data breach or card compromise coverage | P01, P08 |

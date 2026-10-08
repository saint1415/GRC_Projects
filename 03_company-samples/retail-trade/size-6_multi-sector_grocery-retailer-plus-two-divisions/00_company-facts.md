# Scenario facts: Cris Santos Company | Retail Trade | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about acquirers, processors, contracts, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary under common ownership: Cris Santos Markets, LLC (Grocery Retail), Cris Santos Distribution, LLC (Grocery Wholesale), and Cris Santos Financial Services, LLC (Financial Services) |
| Division 1: Grocery Retail (NAICS 445110), **focus of this scenario** | 380 supermarkets in 6 southeastern states (Florida 214, Georgia 58, Alabama 31, South Carolina 29, North Carolina 27, Tennessee 21), plus online ordering on the website and mobile app with curbside pickup at 360 stores and home delivery. About 36,500 employees. About 9.6 million active loyalty members (members must be 18 or older). **No pharmacies** (a standing group decision) |
| Division 2: Grocery Wholesale (NAICS 424410, sector 42 Wholesale Trade) | 6 distribution centers (3 in Florida, 1 each in Georgia, Alabama, and North Carolina) that supply all 380 group stores and about 1,100 independent grocers in 8 southeastern states. Operates a fleet of about 420 tractors and 900 refrigerated trailers, and the **Retailer Services Portal** (ordering, item and price files, promotions, invoices, and payments) used by the independent grocers. About 4,800 employees |
| Division 3: Financial Services (NAICS 522210 Credit Card Issuing and 522291 Consumer Lending, sector 52 Finance and Insurance) | Issues the store-branded **Cris Santos Rewards Card**, a private-label revolving credit card usable only at group stores and online, directly to consumers (about 1.4 million open accounts, about 910,000 active). Also makes closed-end personal installment loans of $500 to $5,000 to existing cardholders (about 62,000 loans outstanding). Not a bank and takes no deposits. About 1,200 employees, most in cardholder service and collections |
| Lending licenses | Background fact, not scored in P03. Financial Services is not a bank, so it lends under state licenses. In Florida, granting revolving credit to buyers for purchases at the group's stores makes it a retail seller under the Retail Installment Sales Act, which needs a license (Fla. Stat. 520.31(16), 520.32(1)). Its personal installment loans of $25,000 or less need a consumer finance license if the rate is above 18 percent a year (Fla. Stat. 516.02(1), (2)(a)). It holds the equivalent licenses in each other state where it lends (handled generically) |
| Corporate shared services | Identity, network, cloud platform, two colocation data centers, security operations, digital front door, ERP and finance, HR, legal, and internal audit. About 2,500 employees |
| Location | Headquartered in Florida. All stores, distribution centers, and customers are in 8 southeastern states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example. The group has no stores, customers, employees, or sales in California or New York |
| Workforce / revenue | 45,000 employees; about $18.0 billion annual revenue (fictional): Grocery Retail about $15.6 billion, Grocery Wholesale about $1.8 billion from external customers (sales to group stores are eliminated), Financial Services about $0.6 billion in interest and fees (about $2.9 billion in receivables) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber, privacy, and AI risk oversight; accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC reporting |
| Group CISO; Group Chief Risk Officer; Group Chief Privacy Officer; Group General Counsel | Group standards, group risk register, common controls, notification matrix |
| Division presidents (3) | Accept Moderate risks for their division |
| Grocery Retail CISO | Division security and compliance lead; owns the PCI DSS program and the annual Report on Compliance (ROC) for the retail merchant |
| Grocery Wholesale security and compliance lead | Division register and supplement; distribution center operational technology (OT) security with the engineering director |
| Financial Services CISO | Division security and compliance lead and the **Qualified Individual** under the FTC Safeguards Rule (16 CFR 314.4(a)); reports to the Financial Services board of managers |
| Financial Services chief compliance officer | Reg Z, Reg B, Reg P, FCRA, Red Flags program, and state licensing (with outside counsel) |
| Group AI council | Approves High-tier AI use cases under the Group AI Standard (P10) |
| Group internal audit | Independent of the teams it assesses (reports to the board audit committee). Assesses common controls once and samples division controls (P07) |
| Disclosure committee | SEC materiality determinations (Form 8-K Item 1.05) |
| External assurance | PCI Qualified Security Assessor (QSA) firm for the retail ROC; SOC 2 service auditor (independent CPA firm) for the wholesale portal readiness (P09) |

## 3. Systems
| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (workforce single sign-on, MFA, privileged access management (PAM), identity governance) | Corporate |
| SYS-G2 | Group SOC, SIEM, and endpoint detection and response (EDR) | Corporate |
| SYS-G3 | Group cloud platform and data centers: landing zones in two public cloud providers (provider A and provider B, vendor-agnostic) and two group colocation data centers (primary and secondary) | Corporate |
| SYS-G4 | Group digital front door: content delivery network and web application firewall, the **tag management service** used by all three divisions' websites, and customer identity (sign-in for shoppers, cardholders, and wholesale customers) | Corporate (group digital) |
| SYS-G5 | Group ERP (finance, merchandising, procurement) and HR system | Corporate |
| SYS-D1 | **E-commerce and Point-of-Sale Platform (EPP)**: web storefront and mobile app back end, checkout and order management, the store point-of-sale (POS) estate, and the payment switch | Grocery Retail |
| SYS-D2 | Loyalty program, customer data platform (CDP), and the pricing and offers engine | Grocery Retail |
| SYS-D3 | Store infrastructure: store networks and Wi-Fi, refrigeration and building controls, CCTV, electronic shelf labels | Grocery Retail |
| SYS-D4 | Distribution systems: warehouse management (WMS), transportation management (TMS), EDI, and distribution center OT (conveyors, automated storage and retrieval, refrigeration controls) | Grocery Wholesale |
| SYS-D5 | Retailer Services Portal (B2B ordering, item and price files, promotions, invoices, card and ACH payments) | Grocery Wholesale |
| SYS-D6 | Card and lending platform: card processing platform from a third-party processor (accounts, authorizations, statements), the in-house credit decision engine, collections, and the cardholder portal and app | Financial Services |

**SSP system (P02):** the *E-commerce and Point-of-Sale Platform (EPP)*: the Grocery Retail division's web storefront and mobile app back end, checkout and order management, store POS estate, and payment switch (SYS-D1), which is the retail cardholder data environment and inherits group common controls from SYS-G1 to SYS-G4.

## 4. Current security posture: a mature retail program, uneven divisions, and gaps in what the group shares
**In place today:**
- Group policies aligned to NIST CSF 2.0, with division supplements, and a common control catalog
- PCI DSS validated every year by a QSA Report on Compliance for the retail merchant since 2015; the 2025 ROC and Attestation of Compliance were accepted by the acquirer in December 2025
- EMV chip PIN pads (PCI PTS-approved) at every lane, with card data encrypted at the PIN pad under the processor's encryption solution; processor tokens for card-on-file; hosted payment fields from the processor on web checkout
- 24x7 group SOC, SIEM, and EDR; quarterly external ASV scans and annual penetration tests of the retail CDE
- Single sign-on with MFA for all workforce users; PAM with just-in-time elevation for administrators
- Semi-annual access reviews for CDE systems and quarterly access certification for group applications
- Immutable backups in the second cloud provider; payment switch active in both data centers
- A written information security program, a Qualified Individual, and a Red Flags program at Financial Services
- Board risk committee oversight; SEC Reg S-K Item 106 disclosure in the annual report

**Missing or weak, found in the 2026 assessments:**
1. **Shared tag management.** The group tag management service (SYS-G4) lets marketing teams in all three divisions publish third-party scripts. The retail web checkout script inventory (PCI DSS 6.4.3) was completed in March 2026, but scripts can still be added through "all pages" containers. Payment page change and tamper detection (11.6.1) runs only on the retail web checkout, and its alerts go to a shared mailbox reviewed weekly. Neither control covers the wholesale portal invoice payment page or the cardholder portal bill payment page.
2. **Store card number on the retail checkout.** The Rewards Card number and its 3-digit card code are typed into a company-hosted field on the same checkout page, outside the processor's hosted payment fields. The store card is not a payment brand card, so PCI DSS does not reach it; it is Financial Services customer information under the Safeguards Rule, and no one owned its protection on the retail page.
3. **Acquired stores.** 46 stores acquired from a regional chain in 2025 still run a legacy POS version on flat store networks until migration (due 2027-06-30). Segmentation testing, POS back office MFA, and SIEM onboarding are incomplete there.
4. **Card data where it should not be.** Data discovery in July 2026 found about 31,000 full card numbers in settlement reconciliation exports from the acquired chain on a finance file share (SYS-G5).
5. **Store card data in marketing.** Rewards Card transaction data flows from Financial Services into the retail CDP and feeds personalized offers. About 41,000 cardholders who opted out of affiliate marketing are not suppressed in the CDP, and no one documented when the pre-existing business relationship exception (12 CFR 1022.21(c)(1)) applies.
6. **Distribution center OT.** Conveyor, automated storage, and refrigeration control networks at 4 of 6 distribution centers connect to the WMS with weak segmentation; two OT vendors have always-on remote access; there is no OT asset inventory at 2 distribution centers.
7. **Retailer Services Portal.** About 30% of independent grocer accounts share credentials among store staff and MFA is optional; 140 of the largest independent grocers asked for a SOC 2 Type 2 report by the end of 2027.
8. **Credit decision model.** The machine learning credit decision engine (line assignment and installment loan decisions) produces adverse action reason codes that were not validated against the model after its 2026 retraining; fairness testing is partial (Reg B, 12 CFR 1002.9(b)(2)).
9. **Common control inheritance.** The PCI responsibility matrix documents what the retail CDE inherits from corporate. Inheritance is not documented for the wholesale portal or the card and lending platform.
10. **Notification matrix.** The group incident notification matrix does not include the acquirer notice term, the FTC Safeguards Rule notice (16 CFR 314.4(j)), Reg Z card reissue and dispute handling, or wholesale customer contract notices, and it has never been exercised across divisions.
11. **Division supplement drift.** The Financial Services standards were last aligned to group policy in 2024. The 2025 Qualified Individual report to the Financial Services board did not cover service provider oversight of the card processing platform (16 CFR 314.4(i)(2)).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | Registry default kept: the E-commerce and Point-of-Sale Platform, the retail cardholder data environment and the system the BIA ranks highest |
| P03 | Each division's primary rule set: PCI DSS v4.0.1 for Grocery Retail (with FTC Act Section 5, FACTA, and SNAP checks); the FTC Safeguards Rule for Financial Services (with Red Flags, Reg P, Reg V, Reg B, FCRA, and Reg Z rows); for Grocery Wholesale, an applicability finding that the vertical's primary rule (NIST SP 800-171 through CMMC and DFARS) does not apply, plus FDA record availability, PCI DSS for portal payments, FTC Act Section 5, and a NIST CSF 2.0 benchmark. A regulation-by-division matrix ties them together |
| P08 | Registry default kept and widened: a payment card data compromise through e-commerce skimming, injected through a compromised third-party script in the group tag management service, that reaches the retail checkout (brand cards and Rewards Card numbers) and the wholesale portal payment page. It needs a multi-regulator notification matrix and an SEC materiality decision |
| P09 | SOC 2 scoped per division: the Retailer Services Portal is in scope (the wholesale division is a service organization for 1,100 independent grocers); Grocery Retail and Financial Services are out of scope, with reasons and the assurance each relies on instead (PCI ROC; FTC and CFPB rules and the card processor's SOC reports) |
| P10 | Registry default kept as the priority use case: dynamic pricing and personalized offers (SYS-D2), assessed inside a group AI governance program with division use cases (the High-tier credit decision model among them) |
| Cloud | Shared corporate platform (two providers, vendor-agnostic) plus two colocation data centers and division workloads |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-01 to 2026-07-31 | Group and division risk analyses; internal PCI DSS pre-assessment of the retail CDE; Safeguards Rule risk assessment at Financial Services |
| 2026-07-01 to 2026-08-31 | Common control assessment (group internal audit) plus division samples |
| 2026-08-17 to 2026-08-28 | Group AI council assessment of priority AI use cases |
| 2026-09-10 | Results to the board risk committee; deliverables approved |
| 2026-10-19 to 2026-11-20 | QSA fieldwork for the 2026 ROC (planned) |
| 2026-12-15 | 2026 ROC and AOC due to the acquirer (merchant agreement term) |
| 2026-12-31 | Qualified Individual's 2026 written report to the Financial Services board due (16 CFR 314.4(i)) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Card acceptance volume | About 330 million retail transactions a year; about 257 million are payment card transactions (credit, debit, and prepaid across all brands), of which well over 6 million are Visa transactions. Visa assigns Level 1 to merchants with more than 6 million Visa transactions a year across all channels and requires an annual ROC by a QSA (or an internal resource if signed by an officer) plus an AOC (Visa compliance validation page, checked 2026-10-04). The acquirer's letter of 2026-02-02 (fictional) confirms Level 1 and an annual ROC by a QSA |
| Online volume | Online orders are about 9% of retail sales: about 12.6 million orders a year (about 34,500 a day), 55% placed in the mobile app and 45% on the website |
| SNAP | Every store is an authorized SNAP retailer (7 CFR 278.1). EBT cards are read on the same PIN pads and routed by the payment switch to the state EBT processors. EBT cards are not payment brand cards, so PCI DSS does not by itself cover them; the group protects them the same way |
| Payment switch | Runs active-active in the two group colocation data centers. Routes brand card authorizations to the processor, Rewards Card authorizations to the card processing platform, and EBT to the state processors. The 46 acquired stores connect through a legacy store gateway |
| Merchant agreement terms (fictional) | Notify the acquirer within 24 hours of suspecting a compromise of card data; use a PCI Forensic Investigator (PFI) if the acquirer or a card brand requires one; ROC and AOC due each December 15 |
| Wholesale contracts (fictional) | Independent grocer supply agreements (2024 form) require notice within 72 hours after the division confirms a security incident affecting the customer's data or payment information |
| Wholesale payments | About 18% of independent grocers pay invoices by card on the portal (the processor's hosted payment fields, about 2,100 payments a month); the rest pay by ACH. The division has its own merchant account and validates by self-assessment |
| Financial Services platform | The card processing platform is a third-party SaaS that holds account, statement, and authorization data under a processing agreement; it provides a SOC 1 Type 2 report and a SOC 2 Type 2 report (Security and Availability). The credit decision engine, collections, and the cardholder portal and app run in Financial Services accounts in cloud provider A |
| Financial Services licensing | Holds the state consumer lending licenses that counsel determined are required in its 8 states (generic; not analyzed here). Funded by a warehouse credit facility; no deposits |
| Affiliate data sharing | Financial Services provides Rewards Card transaction and account data to the retail CDP under an intercompany data agreement (2023) for rewards fulfillment and marketing. The cardholder agreement and annual privacy notice give an affiliate marketing opt-out (about 41,000 opt-outs) |
| Store card at checkout | About 7% of online orders are paid with the Rewards Card |
| Acquisition | The 46 stores came from a regional chain acquired on 2025-04-01 |
| Other AI use cases (P10 inventory) | Besides the pricing and offers engine and the credit decision model: card and e-commerce fraud scoring, demand forecasting and replenishment, self-checkout loss prevention video analytics (no facial recognition), a generative AI customer service assistant, warehouse labor and slotting optimization, collections contact strategy, and an enterprise generative AI assistant piloted with 3,000 workforce users. A Group AI Standard and Group AI council were established in 2026 |
| Electronic shelf labels | Installed in 120 stores; the pricing engine can change shelf prices in those stores within approved bounds |
| Cloud | Provider A hosts the landing zone hub, the EPP storefront and order services, the CDP, the Retailer Services Portal, and Financial Services workloads. Provider B hosts the disaster recovery environments and the immutable backup vault. The payment switch, the store gateway, and the ERP run in the two group colocation data centers. The WMS runs on servers in each distribution center with a central instance in the primary data center |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only |
| Wholesale merchant agreement (fictional) | The Grocery Wholesale merchant account has the same 24-hour acquirer notice term as the retail merchant agreement (P08) |
| Pricing engine bounds | The pricing and offers engine may move shelf label prices within plus or minus 10% and online prices within plus or minus 15% of the base price, above item cost floors; infant formula, baby food, bottled water, and over-the-counter medicines stay at base price (P10) |
| Vendor assurance reports (P09) | The card processing platform's SOC 1 and SOC 2 Type 2 reports cover the 12 months ending 2026-06-30 and its contract requires incident notice within 48 hours (fictional term). The tag management vendor provides a SOC 2 Type 2 report (Security only) for the 12 months ending 2026-03-31, with a qualified opinion on one change management criterion |
| SOC 2 timeline for the portal (P09) | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30, issued by 2027-12-15 |
| Out of scope by fact | No pharmacies (HIPAA does not apply); no California or New York business (CCPA and NYDFS Part 500 do not apply); no federal or DoD contracts (CMMC, DFARS 252.204-7012, and FAR clauses do not apply); no third-party sellers on the website (INFORM Consumers Act does not apply); website and app not directed to children and loyalty members are 18 or older (COPPA does not apply); no facial recognition anywhere in the group |

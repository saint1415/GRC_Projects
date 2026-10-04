# Scenario facts: Cris Santos Company | Retail Trade | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the acquirer, the merchant agreement, suppliers, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed; board with an audit committee) |
| Business | Regional grocery retailer (NAICS 445110): **5 supermarkets** (Stores 1 to 5, each about 35,000 square feet, open 7:00 to 22:00 every day), **online ordering** through a website and a mobile app with curbside pickup at every store and home delivery by company drivers, deli and bakery **catering** orders, a **distribution center (DC)** of about 120,000 square feet that supplies the stores with company trucks, and a **support center** (headquarters) on the DC campus. No pharmacy |
| Location | Florida only. The 5 stores are in two neighboring counties; the DC and support center share one campus in the same region. Online delivery covers about a 12-mile radius around each store |
| Workforce | 600 employees: about 480 in the stores (including 70 e-commerce pickers and drivers), 65 in the DC and transportation, and 55 in the support center |
| Revenue | About $100 million a year (fictional): about $88 million in stores and about $12 million online (12%). Not SBA-small: the SBA standard for NAICS 445110 is $40.0 million in average annual receipts (13 CFR 121.201) |
| Card and EBT acceptance | About 2.1 million card transactions a year: about 1.95 million in the stores (EMV chip and contactless) and about 140,000 online. About 230,000 SNAP EBT transactions a year in the stores. Catering phone orders (about 3,000 a year) are keyed into the processor's virtual terminal. Orders placed through a third-party delivery marketplace (about 4% of online sales) are paid on the marketplace, which pays the company, so those cards never reach company systems |
| Customers | About 148,000 loyalty members (members must be 18 or older), about 52,000 online shopping accounts, and about 31,000 monthly active mobile app users |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 (PCI SSC) applies through the merchant agreement with the acquiring bank. It is a contractual standard, not law. In a letter dated 2026-05-15 (fictional), the acquirer confirmed the company's merchant level (Level 2 under the acquirer's program) and the **validation it requires**: an annual **SAQ D for Merchants**, prepared with a Qualified Security Assessor (QSA) firm and signed by the Chief Financial Officer, plus passing quarterly external scans by an Approved Scanning Vendor (ASV). The 2026 attestation of compliance (AOC) is due 2026-12-31. Card brand level thresholds are not restated in these documents because they were not verified from a card brand source |
| Why the CDE is large | **In store:** the 65 PIN pads are PCI-approved PTS devices and encrypt card data at the moment of reading with the processor's encryption service, but that service is **not a PCI-listed validated P2PE solution**. The acquirer and QSA therefore treat the 65 registers, the 5 store POS servers, the store POS networks, and the POS head-office application as part of the cardholder data environment (CDE). **Online:** the website and app checkouts use the processor's hosted payment fields (inline frames) and mobile software development kit (SDK); the e-commerce platform receives only tokens. The checkout pages that host the fields can still affect the payment, so PCI DSS v4.0.1 Requirements 6.4.3 and 11.6.1 apply. **Service desks:** 5 service-desk PCs (one per store) are used for the processor's virtual terminal |
| Not in scope | **Pharmacy and HIPAA:** no pharmacy (owners' decision), so not a HIPAA covered entity. **FTC Safeguards Rule and Red Flags Rule:** the company issues no store credit card, offers no deferred payment, and does not cash checks or sell money services (no covered accounts; not a financial institution under 16 CFR Part 314). **CCPA:** revenue exceeds the $26,625,000 threshold, but the company does not do business in California (Florida stores and delivery only). **Florida Digital Bill of Rights (Fla. Stat. 501.701 et seq.):** not a "controller" because that definition requires more than $1 billion in global gross annual revenue (501.702). **COPPA:** the website and app are not directed to children; loyalty members must be 18 or older. **INFORM Consumers Act:** the company does not operate an online marketplace; on the delivery marketplace it is a seller, and collecting seller information is the marketplace's duty (15 U.S.C. 45f). **SEC disclosure:** privately held. **Facial recognition:** not used (a vendor proposal was declined in P10) |
| Other applicable law and rules | FTC Act Section 5 (15 U.S.C. 45(a), (n)) for customer and loyalty data security, privacy statements, and pricing claims; FACTA receipt truncation (15 U.S.C. 1681c(g)); Florida Information Protection Act, Fla. Stat. 501.171 (reasonable security (2), breach notice (3)-(6), disposal (8)); Fla. Stat. 501.160 (price gouging during a declared state of emergency) for the pricing engine; SNAP retailer authorization at all 5 stores (7 CFR 278.1 and 278.2; no cybersecurity control requirements were identified in Part 278); Title VII of the Civil Rights Act for the hiring screening tool (P10) |
| State law approach | The company operates only in Florida, so Florida law is the worked example. Online customers and seasonal residents may live in other states, so breach notice is planned "for each state where affected individuals reside" (P08) |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Board audit committee | Quarterly cyber risk and PCI DSS status reporting |
| Chief Executive Officer | Accepts High risk; approves the risk appetite and security budget |
| Chief Operating Officer | Executive sponsor of the security program; system owner of the SSP system; accepts Moderate risk |
| Chief Financial Officer | Owns the merchant agreement and acquirer relationship; signs the PCI DSS AOC; owns cyber insurance |
| General Counsel | Legal lead for incidents and breach determinations; privacy program owner |
| Privacy and Compliance Manager | Privacy notices, data sharing reviews, vendor contract terms, breach decision log (reports to the General Counsel) |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting; AI governance co-lead |
| IT Director | Information security officer for the program; PCI DSS program owner; day-to-day control owner |
| Security Manager plus 2 security analysts | Security operations, vulnerability management, MSSP liaison, GRC (one analyst is the GRC analyst) |
| Director of E-commerce and Marketing | Business owner of the website, app, loyalty program, supplier offers and retail media service, and the pricing and offers engine (P10) |
| Director of Store Operations | Owns the 5 stores, front-end procedures, PIN pad inspections (with the 5 Store Managers) |
| Distribution Center Director | DC, transportation, warehouse management system |
| Director of Loss Prevention | CCTV, physical security, PIN pad tampering investigations |
| HR Director | Hiring, terminations, transfers, training records, applicant tracking system |
| Internal audit (co-sourced firm) | Annual IT audit; performed the P07 assessment |
| QSA firm (independent) | Prepares the annual PCI DSS assessment that supports the SAQ D; not the internal audit firm |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring |

## 3. Systems
| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | E-commerce platform: website storefront, mobile app back end, customer accounts, ordering, pickup and delivery scheduling | Vendor SaaS | Customer accounts (name, email, password hash, phone, addresses, order history, app location for curbside arrival); **no card numbers** (tokens only) | Checkout pages host the processor's payment fields. 23 third-party scripts load on checkout pages (see gaps). Vendor SOC 2 Type 2 and PCI DSS service provider AOC |
| SYS-02 | Payment processor and gateway services: in-store encryption service, hosted payment fields and mobile SDK, tokenization, virtual terminal, merchant portal | Service provider | Card data (processor side) | Third-party service provider (TPSP) with a PCI DSS AOC. The in-store encryption service is not a PCI-listed P2PE solution |
| SYS-03 | Store POS system: 65 registers (8 staffed lanes, 4 self-checkouts, and 1 service desk per store), 65 PIN pads, 5 store POS servers, and the POS head-office application | Registers and store servers on premises; head-office application in the company's cloud workloads account, managed by the POS vendor | Encrypted card data, truncated card numbers, loyalty lookups | In the CDE. Store servers run offline (store-and-forward) mode when the network or processor is down. POS vendor technicians use 3 shared support accounts (see gaps) |
| SYS-04 | Cloud landing zone: 4 accounts or subscriptions (identity and security, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Yes | Workloads: loyalty and customer data platform (CDP) database and loyalty API, integration platform (APIs and file transfers between the ERP, POS, e-commerce platform, and offers engine), POS head-office application, data warehouse, supplier offers reporting portal, file services |
| SYS-05 | ERP (merchandising, item and price file, purchasing, finance) and warehouse management system (WMS) | ERP vendor SaaS; WMS vendor SaaS with 120 RF handhelds at the DC | Employee, supplier, and financial data | ERP sends the nightly price file to the POS and e-commerce platform. EDI with about 300 suppliers |
| SYS-06 | Identity provider with single sign-on, MFA, and conditional access | SaaS | Identities only | All workforce cloud and SaaS access. Registers use POS-local sign-in (see gaps) |
| SYS-07 | Site networks: 6 sites (Stores 1 to 5 and the DC campus) on SD-WAN | On premises; managed SD-WAN service | Encrypted card data in transit | Each store has a POS VLAN (CDE), a corporate VLAN, guest Wi-Fi (internet only), and CCTV. IoT devices are on a separate VLAN at Stores 1 to 3 and the DC; at Stores 4 and 5 they share the corporate VLAN |
| SYS-08 | Endpoints: 210 support-center, store office, and DC PCs and laptops (including the 5 service-desk PCs), 220 handhelds for picking and inventory, 35 tablets | Company-managed | Yes (exports, email) | EDR on PCs, laptops, and the 5 store POS servers. Registers run the POS vendor's anti-malware, not the company EDR |
| SYS-09 | SIEM operated by the MSSP | SaaS | Security logs | Receives identity provider, cloud, firewall, EDR, and e-commerce admin logs. Registers, store POS servers, and the POS head-office application do not send logs (see gaps) |
| SYS-10 | Store and DC operational technology: refrigeration controllers (62) and case sensors (about 900), energy management, CCTV recorders, DC dock and cold-room controls | On premises with vendor cloud dashboards | No (CCTV video only) | Refrigeration contractor has always-on remote access (see gaps) |
| SYS-11 | Third parties: about 85 vendors with company data or system access, 14 of them PCI DSS-relevant TPSPs | Various | Various | Includes the marketing agency, delivery marketplace, POS vendor, refrigeration contractor, and payroll provider |
| SYS-12 | AI tools: pricing and personalized offers engine, demand forecasting, self-checkout computer vision, customer service chatbot, hiring screening module, generative AI assistant | Vendors | Various | 5 of 6 tools in use were adopted by departments without a security, privacy, or fairness review (see gaps and P10) |

**SSP system (P02):** the *E-commerce and Point-of-Sale Platform (EPP)*: SYS-01 to SYS-04 and SYS-06 to SYS-09, with interfaces to SYS-05, SYS-10, SYS-11, and SYS-12. Moderate baseline with tailoring.

**Registry defaults kept, and why.** The registry's primary system ("E-commerce and point-of-sale platform"), incident ("Payment card data compromise, e-commerce skimming"), and AI use case ("Dynamic pricing and personalized offers") all fit a 5-store grocer with online ordering. At this size the incident set adds a second type (ransomware across stores and the DC) and the AI scope widens to a portfolio, as the Mid-Market tier requires.

## 4. Current security posture: defined program with gaps in scale
**In place today:**
- A security program led by the vCISO and the IT Director, with a Security Manager and 2 analysts; policies adopted in 2024
- MFA through the identity provider for all workforce email, SaaS, and cloud access
- EDR on PCs, laptops, and store POS servers, monitored 24x7 by the MSSP through the SIEM
- PCI DSS validated each year since 2023 with an SAQ D prepared with a QSA firm; quarterly ASV scans passing
- EMV chip and contactless acceptance on PCI-approved PIN pads, with the processor's encryption at the PIN pad
- Hosted payment fields and tokenization online; no card numbers stored by the e-commerce platform
- POS VLANs separated from corporate networks at all 5 stores; guest Wi-Fi isolated
- Immutable backups of cloud workloads in a separate backup account (35-day write-once retention)
- Annual security training and quarterly phishing simulations
- Annual co-sourced internal IT audit and an annual external penetration test of the website (last done November 2025)

**Gaps:**
1. **PCI scope is larger than it needs to be, and the scope document is stale.** Because the in-store encryption is not a listed P2PE solution, 65 registers, 5 store servers, and the store POS networks are in the CDE. The 2025 scope document was not updated when the POS head-office application moved into the cloud workloads account in December 2025 (Requirement 12.5).
2. **Payment page scripts are not fully managed.** The checkout pages load 23 third-party scripts. 15 are in an inventory, none has a written justification or integrity check, and change and tamper detection covers the website checkout but not the in-app web checkout (Requirements 6.4.3 and 11.6.1). The marketing agency can publish tags through the tag manager.
3. **Privileged and vendor access.** Privileged access management covers cloud accounts only. POS vendor technicians use 3 shared support accounts with standing remote access to the store POS servers, and register local administrator passwords are identical across stores.
4. **Store IoT segmentation.** Refrigeration, energy management, and CCTV devices share the corporate VLAN at Stores 4 and 5. The refrigeration contractor has an always-on remote access tool.
5. **CDE logging and review.** Registers, store POS servers, and the POS head-office application do not send logs to the SIEM, and CDE audit logs are not reviewed daily (Requirement 10.4).
6. **Third-party service providers.** The TPSP list is incomplete (14 identified, a responsibility matrix for 6), AOCs are not tracked, 3 AOCs on file are expired, and the marketing agency and delivery partner contracts have no security terms (Requirement 12.8).
7. **Recovery is unproven for cloud workloads.** Store POS offline mode is tested each year, but the loyalty and CDP database, the integration platform, and the POS head-office application have never been restore-tested. The ERP vendor's stated RTO of 24 hours is longer than the BIA needs for pricing.
8. **Card data outside the payment systems.** Deli and bakery staff write catering phone orders, including full card numbers and security codes, on paper forms kept in binders. The virtual terminal runs on general-purpose service-desk PCs that are also used for email.
9. **Loyalty data sharing does not match the privacy notice.** Member-level loyalty exports are emailed weekly to the marketing agency, and a pilot shares hashed member emails with one consumer goods supplier, while the privacy notice says member data is not shared with third parties for their own marketing.
10. **No AI governance.** The pricing and offers engine, self-checkout computer vision, customer chatbot, and hiring screening module were adopted without security, privacy, or fairness review.
11. **PIN pad protection is uneven.** Weekly PIN pad inspections are recorded at Stores 1 to 3 only, and the device list was not reconciled with the processor's records; 2 PIN pads in use were missing from the list (Requirement 9.5.1).
12. **Supporting standards are thin.** There is no configuration standard for registers and store servers, and vulnerability management relies on the POS vendor's quarterly register patches (2 critical updates were applied about 90 days late).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | PCI DSS v4.0.1 (contractual standard) at requirement level with evidence sampling, plus every other rule that binds the primary business line: FTC Act Section 5, FACTA receipt truncation, and Florida's reasonable security and disposal duties (Fla. Stat. 501.171(2), (8)). Applicability of the other retail rules is decided in section 1 of the report |
| P08 | **Two incident types**, integrated with crisis management and legal: (1) payment card data compromise through e-commerce skimming (registry default), and (2) ransomware across store POS servers, the integration platform, and DC operations |
| P09 | Readiness for a SOC 2 **Type 2** examination of the **Supplier Offers and Retail Media service**, requested by national consumer goods suppliers (Security, Availability, Confidentiality, Processing Integrity); plus a vendor assurance review program (SOC 2 reports and PCI DSS AOCs) |
| P10 | AI use-case portfolio: AI-001 pricing and personalized offers engine (registry default), AI-002 demand forecasting and replenishment, AI-003 self-checkout computer vision, AI-004 customer service chatbot, AI-005 facial recognition for loss prevention (vendor proposal, not adopted), AI-006 hiring screening module, AI-007 generative AI assistant |
| Cloud | 4-account landing zone, vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-15 | Acquirer letter confirming merchant level and validation (SAQ D with QSA, quarterly ASV scans) |
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment (co-sourced internal audit firm) |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness assessment and AI governance assessment |
| 2026-09-15 | Results to the audit committee; deliverables approved |
| 2026-10-19 to 2026-11-20 | QSA fieldwork for the 2026 PCI DSS validation (planned) |
| 2026-12-31 | 2026 SAQ D and AOC due to the acquirer |

## 7. Facts added during the build (fictional; used across P01-P10)
| Topic | Added fact |
|---|---|
| Daily revenue | About $275,000 a day over 364 trading days: about $48,400 per store in store sales (about $242,000 across 5 stores) and about $33,000 online. Average store basket about $38; average online order about $85 (about 390 online orders a day) |
| Merchant agreement | Notify the acquirer within 24 hours of suspecting a compromise of card data (contract term, fictional) |
| Cyber insurance | $10 million aggregate limit, $250,000 retention. The policy requires notice through the carrier hotline before incident vendors are engaged; panel counsel and forensics |
| POS offline mode | Store POS servers can store and forward card approvals for up to 24 hours under a per-transaction floor limit set with the processor; SNAP EBT cannot be processed offline |
| Workforce activity | 268 terminations and 85 transfers in the 12 months to 2026-06-30; last access review completed in February 2026; June 2026 phishing simulation click rate 6.9% |
| Supplier offers and retail media | About 140 consumer goods suppliers fund digital coupons and sponsored placements; the company targets offers to members, reports redemptions, and bills suppliers about $3.1 million a year in offer reimbursements and media fees. Two national suppliers require a SOC 2 Type 2 report by 2027-12-31 (contract term, fictional) |
| Third parties | Marketing agency (tags and email campaigns), delivery marketplace, POS vendor, refrigeration contractor, payment processor, e-commerce platform vendor, ERP vendor, WMS vendor, MSSP, cloud provider, identity provider, payroll and HR SaaS provider, pricing and offers engine vendor |
| Terminology | "E-commerce and Point-of-Sale Platform (EPP)" is the SSP system in P02, identifier CSC-EPP-01 |
| Additional role titles | Store Managers (5); Director of Customer Service; Controller; Transportation Manager; Director of Merchandising; Director of Fresh Departments |

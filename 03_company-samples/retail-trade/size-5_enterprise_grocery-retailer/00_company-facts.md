# Scenario facts: Cris Santos Company | Retail Trade | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about the acquirer, the merchant agreement, the QSA, and vendors are fictional.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; regional supermarket chain) |
| Business | Grocery retailer (NAICS 445110): **112 supermarkets** under two banners, **online ordering** on the web and in mobile apps with curbside pickup and home delivery, and 2 distribution centers. **No pharmacy** in any store (Phase 3 decision, kept at this size and confirmed by the board) |
| Location | Headquartered in Florida. Stores in Florida (66), Georgia (20), Alabama (9), South Carolina (8), and Tennessee (9). **State law is handled generically:** apply the law of each state where affected individuals reside, with Florida as the worked example |
| Acquired banner (AB) | 14 stores (9 in Tennessee, 5 in Alabama) acquired on 2025-10-01 from a regional chain. Not yet converted to the company's POS, network, or identity platform (see section 4) |
| Workforce | 12,000 employees: about 10,350 in stores, 980 in distribution and transportation, and 670 at headquarters (about 290 in technology and digital, including a 46-person security organization) |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day. Online orders are about 9% of sales (about $430 million a year, about 3.6 million orders, about 9,900 a day) |
| Card and EBT acceptance | About 118 million customer transactions a year. About 84 million card transactions (credit, debit, prepaid), of which about 44 million are Visa, and about 3.4 million card-not-present online payments. About 7.2 million SNAP EBT transactions |
| Customers | About 3.1 million active loyalty members (about 240,000 in Tennessee), about 1.4 million online shopping accounts, and about 900,000 monthly active mobile app users. Loyalty and online accounts require age 18 or older |
| PCI DSS status | **Level 1 merchant** as designated by the acquirer (letter dated 2026-02-10, fictional). PCI DSS v4.0.1 applies through the merchant agreement; it is a contractual standard, not law (N44-45-R01). Validation is an annual **Report on Compliance (ROC) by a Qualified Security Assessor (QSA)** with an Attestation of Compliance (AOC). The 2025 ROC (core stores and e-commerce) was compliant with 3 compensating controls. The 2026 ROC is the first to include the acquired banner. The Visa Core Rules (April 2026 edition) say merchant levels are set out in Visa's Account Information Security Program Guide; this analysis does not restate the thresholds |
| Payment architecture | **Core stores (98):** PCI-approved PIN pads encrypt card data at the point of interaction with the processor's end-to-end encryption. The solution is **not a PCI-listed P2PE solution**, so the acquirer has not approved scope reduction: lanes, store controllers, the store payment network, and the payment switch stay in ROC scope. **Payment switch:** commercial payment switch software run by the company in two colocation sites, routing card authorizations to the primary processor and SNAP EBT transactions to each state's EBT processor. **Online:** the web checkout embeds the processor's hosted payment fields (inline frames); the mobile apps use the processor's SDK; saved cards are processor tokens. The company stores no full card numbers after authorization. **Acquired banner (14):** legacy POS and legacy PIN pads that do **not** encrypt at the PIN pad; card data is in clear text between the PIN pad and the store server, then sent over a legacy VPN to a legacy processor |
| SNAP EBT | Each store is an FNS-authorized retail food store (7 CFR 278.1). For the 98 core stores the company drives its own terminals through its payment switch, which makes it a **third party processor** under 7 CFR 274.3(d) in each state's EBT system. Online SNAP payment is not offered |
| Not in scope (applicability decided in P03) | **HIPAA:** no pharmacy. **FTC Safeguards Rule and Red Flags Rule:** the co-brand credit card is issued, underwritten, and serviced by a partner bank; the company extends no credit, cashes no checks, and offers no money transmission, so it has no covered accounts and is not a financial institution under 16 CFR Part 314. **CCPA:** no stores, delivery, or targeted marketing in California. **Florida Digital Bill of Rights:** the company exceeds $1 billion in revenue but meets none of the other controller criteria in Fla. Stat. 501.702. **COPPA:** sites and apps are not directed to children and accounts require age 18. **INFORM Consumers Act:** no third-party marketplace sellers. **Facial recognition:** not used anywhere (board decision, 2024) |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a), (n)); FACTA receipt truncation (15 U.S.C. 1681c(g)); **Tennessee Information Protection Act** (2023 Tenn. Pub. Acts ch. 408, effective 2025-07-01); SEC Form 8-K Item 1.05 and Regulation S-K Item 106; SOX internal control over financial reporting; state breach notification laws (Florida worked example, Fla. Stat. 501.171); Florida price gouging during declared emergencies (Fla. Stat. 501.160) |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board: audit committee; risk and technology committee | Risk and technology committee oversees cybersecurity (Item 106 disclosure); audit committee oversees Internal Audit and SOX |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk jointly; sign the PCI DSS AOC (CFO); the CFO is the authorizing official equivalent for the payments platform (P02) |
| Chief Information Security Officer (CISO) | Security program owner; reports to the CIO with a direct line to the risk and technology committee |
| Director of Security Operations | 24x7 SOC (in-house, with MSSP overflow), incident commander (P08) |
| Chief Privacy Officer | Privacy program; Tennessee Information Protection Act compliance; breach determinations with counsel |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Internal Audit (third line, in-house IT audit team of 6); reports to the audit committee; leads P07 |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Information Officer (CIO) | Technology operations; owns the enterprise platform (common control providers) |
| Chief Digital Officer | System owner of the Omnichannel Commerce and Payments Platform (P02); owns e-commerce and mobile apps |
| Vice President, Payments | Merchant agreements, acquirer and processor relationships, payment switch business owner, ROC sponsor |
| PCI Program Manager (GRC team) | Day-to-day PCI DSS program: scope, evidence, QSA coordination, TPSP list |
| GRC team (10, including the PCI Program Manager), SOC, Internal Audit | Three lines model: first line operates, GRC (second line) runs the methods, Internal Audit (third line) tests independently |
| QSA firm (external) | Independent PCI DSS assessor; 2026 ROC fieldwork 2026-10-19 to 2026-11-20 |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |
| AI governance committee | Formed 2025; chaired by the Chief Data and Analytics Officer |

## 3. Systems

| ID | System | Notes |
|---|---|---|
| SYS-01 | POS platform at the 98 core stores: about 2,650 lanes (including about 610 self-checkouts), 196 store controllers (2 per store), about 2,780 E2EE PIN pads | Commercial POS software, customer-managed; card data encrypted at the PIN pad |
| SYS-02 | Payment switch and tokenization interface | Commercial switch software, active-active in colocation sites COLO-1 (Florida) and COLO-2 (Georgia); routes cards to the primary processor (about 98% of card volume) and SNAP EBT to state EBT processors |
| SYS-03 | E-commerce platform: web storefront, iOS and Android apps, order management, pickup and delivery scheduling | Company-built on Cloud provider A managed containers; web checkout embeds the processor's hosted payment fields; 47 scripts load on payment pages (see gaps) |
| SYS-04 | Loyalty, CRM, and customer data platform (CDP) | Cloud provider B; 3.1 million members; feeds personalized offers (SYS-12) and retail media (SYS-13) |
| SYS-05 | Identity platform (SSO, MFA, privileged access management, identity governance) | The acquired banner still uses its own legacy directory |
| SYS-06 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation sites | Cloud A: commerce workloads. Cloud B: data, analytics, AI, retail media. COLO-1 and COLO-2: payment switch, network core, backup copies |
| SYS-07 | Store and enterprise network (SD-WAN, store segmentation, wireless) | Network access control (NAC) at 61 of 98 core stores; none at AB stores |
| SYS-08 | Store operational technology and IoT: refrigeration controllers, building management, electronic shelf labels (ESL) at 40 stores, CCTV | Refrigeration and ESL controllers share the store operations VLAN with back-office PCs at 37 core stores; CCTV has no facial recognition |
| SYS-09 | ERP (finance, merchandising, item and price file, procurement), warehouse management at 2 distribution centers, supplier collaboration portal (SL-2) | SOX-relevant; the price file feeds POS, ESL, and web |
| SYS-10 | Endpoints | About 7,400 PCs, laptops, and handhelds, plus about 3,100 POS devices (registers and store controllers) |
| SYS-11 | Third parties | About 1,100 vendors; 71 third-party service providers (TPSPs) with PCI DSS responsibilities; 3 last-mile delivery providers |
| SYS-12 | Pricing and personalized offers engine | Built on Cloud B by the data science team with a commercial optimization library; sets ESL markdowns, online prices, and weekly digital coupons (P10 AI-001) |
| SYS-13 | Retail media platform and data clean room (SL-1) | Cloud B; serves about 140 consumer packaged goods (CPG) brand clients |
| SYS-14 | Acquired banner legacy stack | Legacy POS and store servers at 14 stores, legacy directory, flat store networks, legacy processor link over VPN; not in the SIEM |
| SYS-15 | AI portfolio | 12 use cases (P10), governed by the AI governance committee |

**SSP system (P02):** the *Omnichannel Commerce and Payments Platform (OCPP)*: the POS platform at the 98 core stores (SYS-01), the payment switch and tokenization interface (SYS-02), and the e-commerce platform with web storefront, mobile apps, and order management (SYS-03), including the administrator endpoints that manage them, with interfaces to SYS-04, SYS-09, SYS-12, the primary processor, and state EBT processors. The 14 acquired-banner stores (SYS-14) are outside the boundary until they convert.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A mature program aligned to CSF 2.0, with three lines of defense and ERM integration (NIST IR 8286)
- Annual PCI DSS ROC by a QSA since 2015; the 2025 ROC was compliant with 3 compensating controls
- Encryption at the PIN pad at all core stores; tokenization for saved cards; hosted payment fields on the web checkout
- 24x7 SOC with SIEM; EDR on 97% of PCs and servers
- Privileged access management; quarterly access certification for the cardholder data environment (CDE)
- Immutable backups; annual disaster recovery tests for tier-1 systems; active-active payment switch
- Tiered third-party risk program with annual AOC collection
- Payment page script inventory and change detection on the main web checkout since 2025-03 (PCI DSS 6.4.3 and 11.6.1)
- SOX IT general controls tested annually
- SEC Item 106 disclosure in the 10-K

**Targeted gaps:**
1. **Acquired banner.** The 14 AB stores run legacy POS with no encryption at the PIN pad, flat store networks, a legacy directory, and no SIEM feed. Conversion is due in two waves (5 Alabama stores by 2026-12-15; 9 Tennessee stores by 2027-03-31).
2. **Payment page scripts.** Script controls cover the main web checkout but not the express checkout used on mobile browsers, and retail media sponsored-product tags still load through the tag manager on cart and express checkout pages. Fieldwork found 47 scripts on payment pages; 3 had no written justification.
3. **Service provider oversight.** Of 71 TPSPs, 9 had an expired or missing AOC, and 14 had no written split of PCI DSS responsibilities (12.8.4, 12.8.5).
4. **Store OT and IoT.** Refrigeration and ESL controllers share a VLAN with back-office PCs at 37 core stores; NAC covers 61 of 98 core stores; 2 refrigeration vendors use always-on remote access tools outside PAM.
5. **AI.** 12 use cases; 7 reviewed by the AI governance committee. Pricing and offer fairness has been tested only by store cluster, not by neighborhood income or delivery zone. Tennessee data protection assessments for targeted advertising (retail media) and profiling (personalized offers) are not complete.
6. **Materiality.** The disclosure committee has never exercised a payment card compromise, and the playbook does not link card brand and forensic investigation steps to the materiality timeline.
7. **Retail media and supplier data (SL-1, SL-2).** Clean room minimum audience thresholds are not enforced in 2 of 6 report templates. Neither service line has a SOC 2 report, and large clients now require a Type 2.
8. **Delivery concentration.** One last-mile delivery platform handles 62% of home deliveries; the fallback to the other two providers has never been tested at volume.
9. **Legacy credentials.** AB store servers share one local administrator account across all 14 stores.
10. **EBT failover.** The payment switch failover test met its RTO for cards, but SNAP EBT routing has never been tested in failover.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P03 | PCI DSS v4.0.1 at ROC depth (primary, contractual), plus FTC Act Section 5, FACTA, card brand rules (Visa Core Rules, contractual), SNAP EBT retailer and third party processor rules, SEC Item 1.05 and Item 106, the Tennessee Information Protection Act, and state breach and data security law (Florida worked example) |
| P08 | Payment card data compromise through e-commerce skimming, with acquirer and card brand steps, forensic investigation, an **SEC materiality assessment and 8-K Item 1.05** step, and a multi-state notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to external business clients: SL-1 retail media and data clean room (CPG brands) and SL-2 supplier collaboration portal (suppliers) |
| P10 | Enterprise AI portfolio (12 use cases) with the committee operating model, and a full assessment of AI-001 dynamic pricing and personalized offers |
| Cloud | Multi-cloud (vendor-agnostic) with common controls, plus colocation for the payment switch |
| Registry defaults | Primary system "E-commerce and point-of-sale platform" kept, named the OCPP. Incident "e-commerce skimming" kept. AI use case "dynamic pricing and personalized offers" kept as AI-001 within the portfolio |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-02-10 | Acquirer letter confirming Level 1 and ROC validation, with the acquired banner in 2026 scope |
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit) |
| 2026-09-10 | Results to the risk and technology committee of the board |
| 2026-10-19 to 2026-11-20 | QSA fieldwork for the 2026 ROC |
| 2026-12-15 | 2026 ROC and AOC due to the acquirer |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Sites and volumes.** 112 stores, 2 distribution centers (DIST-1 in Florida, DIST-2 in Georgia), 2 colocation sites (COLO-1 Florida, COLO-2 Georgia), and headquarters in Florida. Revenue of about $4.8 billion a year is about $13.2 million per calendar day. Average in-store basket about $37; average online order about $120.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Operating Officer (COO) | Store operations and supply chain; crisis management team chair |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| Controller | SOX program owner; disclosure committee member |
| Chief Marketing Officer | Loyalty program and customer communications; business owner of personalized offers |
| Chief Merchandising Officer | Prices and promotions; business owner of dynamic pricing and markdowns |
| Chief Data and Analytics Officer | CDP, data science, AI governance committee chair |
| Chief Human Resources Officer | Onboarding, terminations, training, and HR AI tools |
| Senior Vice President, Store Operations | Store processes, front end, PIN pad inspections, SNAP EBT procedures |
| Senior Vice President, Supply Chain | Distribution centers, transportation, replenishment |
| Vice President, Retail Media | SL-1 owner (retail media and data clean room) |
| Vice President, Supplier Collaboration | SL-2 owner (supplier collaboration portal) |
| Vice President, Integration Management Office | Conversion of the acquired banner |
| Vice President, Asset Protection | Loss prevention, physical security, CCTV |
| Vice President, Investor Relations | Investor communications; disclosure committee member |
| Vice President, Corporate Communications | Media and customer communications during incidents |
| Director of Store Technology | POS, store controllers, store networks at the store edge, store OT integration (common control provider) |
| Director of Identity and Access Management | Identity platform (SYS-05) |
| Director of Cloud Platform Engineering | Landing zones in both clouds (common control provider) |
| Director of Network Engineering | SD-WAN, colocation and data center networks, NAC (common control provider) |
| Director of Endpoint Engineering | PCs, handhelds, EDR, endpoint baselines (common control provider) |
| Director of Third-Party Risk Management | Vendor tiering, TPSP list and AOC tracking, SOC report reviews (in the GRC team) |
| Director of Facilities Engineering | Refrigeration controllers, building management, ESL infrastructure |
| Director of E-commerce Engineering | Web storefront, apps, order management, payment page script program |
| Payment Switch Manager | Day-to-day administration of the payment switch (reports to the Director of Store Technology) |
| Director of Data Science | Pricing and offers models (SYS-12), model monitoring |

**Acquired banner (AB).** 14 stores, about 1,350 employees (included in the 12,000), about 210 lanes and 236 legacy PIN pads. Through 2025 AB validated under its own merchant agreement with a legacy acquirer. Its loyalty members moved into the company's loyalty program in 2026-03. Conversion wave 1 (5 Alabama stores) is due 2026-12-15 and wave 2 (9 Tennessee stores) 2027-03-31. Identity federation of AB staff is due 2026-12-31.

**Merchant agreement term (fictional).** Notify the acquirer within 24 hours of suspecting a compromise of card data and follow the acquirer's and card brands' instructions, including engaging a PCI Forensic Investigator (PFI) on request. The Visa Core Rules require members to report suspected or confirmed compromises to Visa immediately; in the US region a merchant may report on the member's behalf (Visa Core Rules and Visa Product and Service Rules, April 2026 edition, ID# 0007999).

**Service lines offered to external business clients (P09).** SL-1: retail media network and data clean room for about 140 CPG brand clients (onsite sponsored products and display, offsite audiences, and closed-loop sales measurement returned as aggregated results). SL-2: supplier collaboration portal for about 1,400 suppliers (store-level sales and inventory, forecasts, purchase orders, invoice and deduction status). Neither has a SOC 2 report yet.

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, and Vice President, Investor Relations. The Vice President, Payments joins for card data incidents. Outside securities counsel advises.

**Tennessee Information Protection Act.** Verified on the Tennessee General Assembly site: HB1181 (113th General Assembly) became Public Chapter 408, effective 2025-07-01, in the form of House Amendment HA0348. The Act reaches businesses with more than $25,000,000 in revenue that control or process personal information of at least 175,000 Tennessee consumers in a calendar year (or 25,000 with more than 50% of revenue from selling personal information). With about 240,000 Tennessee loyalty members, the company is a controller under the Act. Section references in these deliverables use the bill's numbering (47-18-3201 et seq.); Legal confirms against the codified text.

**Mobile app location.** The app asks for precise location only when a pickup customer taps "I'm on my way" or "I'm here." Precise geolocation is sensitive data under the Tennessee Act.

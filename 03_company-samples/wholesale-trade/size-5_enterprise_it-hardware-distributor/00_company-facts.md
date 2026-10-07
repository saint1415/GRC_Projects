# Scenario facts: Cris Santos Company | Wholesale Trade | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; not a smaller reporting company) |
| Business | IT hardware and software wholesale distributor (NAICS 423430): networking, servers and storage, PCs and peripherals, video surveillance and collaboration equipment, software licenses and cloud subscriptions, and a private-label accessories line. Value-added services: configuration and integration, and IT asset disposition (ITAD). Sells through about 9,500 reseller and integrator accounts and directly to the Department of Defense (DoD) through the **Federal Solutions** business unit |
| Location | Headquartered in Florida. **FL-1** headquarters (offices and the Security Operations Center). Six distribution centers: **FL-2** (Florida; also the Federal Solutions Integration Center with the CUI configuration lab and the Product Authentication Lab), **GA-1** (Georgia), **TX-1** (Texas; also the Lifecycle Services center for ITAD), **OH-1** (Ohio), **NV-1** (Nevada), and **TX-2** (Texas; came with the AQ-1 acquisition). 15 sales offices in 11 states, including California and Virginia. Two colocation data centers: **COLO-1** (Georgia) and **COLO-2** (Texas). **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 5,900 distribution and logistics, 2,500 sales and account management, 950 services (configuration and ITAD), 780 IT, e-commerce engineering, and security, 620 purchasing and supplier management, and 1,250 corporate and administrative. Up to 1,500 temporary warehouse workers at peak through 4 staffing agencies |
| Revenue | About $4.8 billion a year (fictional): about $19.2 million per shipping day (250 shipping days) and $13.2 million per calendar day. Gross margin about 7.1% (about $1.36 million gross profit per shipping day). Commercial channel 89% (about $4.27 billion); Federal Solutions 11% (about $530 million: $190 million DoD prime contracts and $340 million subcontracts to DoD systems integrators). The SBA size standard for NAICS 423430 is 250 employees (13 CFR 121.201), so the company is not small |
| Customers | About 9,500 active reseller and integrator accounts in all 50 states (about 38,000 reseller platform users). DoD components buy directly from Federal Solutions under delivery orders and blanket purchase agreements |
| Suppliers | About 3,600 active suppliers: 240 OEM vendor programs (authorized distribution agreements), about 2,900 service and indirect suppliers, 58 approved independent brokers used by the **open-market sourcing desk** for end-of-life and allocated items (about 1.9% of product spend, about $85 million a year), 6 contract manufacturers for the private-label line, and about 140 carriers and third-party logistics (3PL) providers |
| Imports | Importer of record for the private-label line (about $310 million of purchases a year from contract manufacturers in Asia). **CTPAT** member (importer entity type) since 2019 |
| Federal Contract Information (FCI) | Every DoD order carries FCI (order details, delivery schedules, ship-to locations). DoD prime contracts and subcontracts include FAR 52.204-21, FAR 52.204-25, DFARS 252.204-7012, 252.204-7019 and 252.204-7020, and DFARS 252.246-7008 (prescribed at 48 CFR 246.870-3(b) when procuring electronic parts or end items containing them, including commercial products). Contracts awarded from 2025-11-10 also include DFARS 252.204-7021. FCI is processed in the Order-to-Cash and Fulfillment Platform (OCFP), the productivity suite, and corporate endpoints: the **enterprise FCI scope** |
| Controlled Unclassified Information (CUI) | Federal Solutions configuration and integration jobs use CUI-marked network drawings, IP addressing plans, device configuration baselines, and site survey reports for DoD installations. CUI is allowed only in the **Federal Solutions CUI Enclave (FSCE)** |
| CMMC status | **FSCE: Conditional Level 2 (C3PAO)**, CMMC Status Date 2026-05-14, score 104 out of 110 with 6 one-point requirements on the POA&M (32 CFR 170.21(a)(2)). The POA&M closeout certification assessment must be completed within 180 days, by **2026-11-10**, or the Conditional status expires (32 CFR 170.21(b); 170.17(a)(1)(ii)(B)). The closeout assessment is booked for 2026-10-20. Two DoD contracts awarded in 2026 required Level 2 (C3PAO), which DoD may require at its discretion during Phase 1 (32 CFR 170.3(e)(1)). **Enterprise FCI scope: Final Level 1 (Self)**, self-assessment documented and affirmed 2026-01-15, renewed annually (32 CFR 170.15(a)(1)). **Affirming Official:** President, Federal Solutions (32 CFR 170.22(a)(1)) |
| Public company duties | SEC Form 8-K Item 1.05 and Regulation S-K Item 106 (17 CFR 229.106); SOX internal control over financial reporting, including IT general controls over the ERP |
| Privacy | A CCPA "business" (Cal. Civ. Code 1798.140(d)): revenue above the threshold and business in California. Counsel's 2026-06 count: about 41,000 California consumers (reseller business contacts, end-user license registrants, and about 420 California employees). Below the cyber audit thresholds in Cal. Code Regs. tit. 11, 7120 (250,000 consumers or households; sensitive personal information of 50,000 consumers); rechecked each year. Automated decision-making technology (ADMT) rules apply to the resume screening tool for California applicants from 2027-01-01 (P10) |
| Payment cards | About 6% of revenue is paid by commercial card through a payment processor's hosted payment fields on the reseller platform. Card data does not touch company systems. PCI DSS is a contractual duty validated through the acquiring bank and is outside the scope of these deliverables |
| Not in scope | CIRCIA reporting (final rule not published; proposed only). Classified work: none. Export controls (EAR) for the small export volume are handled by the trade compliance program and are not analyzed here |
| State law approach | State breach laws are handled generically (each state where affected individuals reside), with Florida (Fla. Stat. 501.171) as the worked example. Personal information in scope: employees, reseller business contacts, and end-user license registrants |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors (audit committee; risk committee) | Cyber risk oversight (Item 106 governance). The risk committee receives quarterly cyber reporting |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer (COO) | Business owner for distribution operations; authorizing official equivalent for the OCFP (P02) |
| Chief Information Security Officer (CISO) | Program owner; chairs the policy governance committee; recommends system authorization |
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Audit Executive | Heads Internal Audit (third line); reports to the audit committee; leads the P07 assessment |
| Chief Supply Chain Officer | Supplier management, the open-market sourcing desk, the Product Authentication Lab, and the C-SCRM plan |
| President, Federal Solutions | **CMMC Affirming Official** (32 CFR 170.22); business owner of the FSCE |
| GRC team (9), Security Operations Center (24x7, in-house), Internal Audit (in-house, co-sourced for OT and CMMC specialists) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions (General Counsel chairs) |

## 3. Systems

| ID | System | Hosting | FCI / CUI | Notes |
|---|---|---|---|---|
| SYS-01 | ERP: order-to-cash, procure-to-pay, inventory, finance | Commercial ERP, customer-managed on Cloud provider A (IaaS) | FCI (all DoD orders). **CUI found** in 23 quote records (spill, section 4) | About 6,800 named users; 74 technical administrators through PAM. SOX IT general controls tested annually |
| SYS-02 | Warehouse management system (WMS) | Central instance on Cloud provider A; 2 edge servers at each distribution center | FCI (DoD ship-to data) | About 4,800 handheld and wearable scanners; about 6,100 WMS users including temporary workers |
| SYS-03 | Reseller commerce platform: B2B portal, quoting, cloud subscription marketplace, and order APIs | Company-built on Cloud provider B (managed containers) | FCI in federal integrator quotes; **CUI found** in 23 quote attachments (spill) | About 38,000 users at 9,500 accounts; about 430 reseller API integrations; card payments through a processor's hosted payment fields. Service line SL-1 (P09) |
| SYS-04 | EDI and B2B integration | EDI translator on Cloud provider A; two value-added network (VAN) providers | FCI in DoD EDI orders | About 1.1 million EDI documents a month; the primary VAN carries 72% |
| SYS-05 | Transportation management system (TMS) and carrier integrations | Vendor SaaS | FCI (DoD ship-to) | Parcel and LTL rating, labels, tracking |
| SYS-06 | Distribution-center OT: warehouse control systems, conveyors, sortation, automated storage | On-premises at FL-2, GA-1, TX-1, OH-1 | None | About 1,400 PLCs; 112 HMIs and engineering workstations on unsupported operating systems |
| SYS-07 | Identity platform: SSO, MFA, privileged access management (PAM), identity governance | SaaS plus on-premises directory | Identities | AQ-1 users still on a legacy directory |
| SYS-08 | Security operations platform: 24x7 SOC, SIEM, EDR, vulnerability management, threat intelligence | Cloud provider A and COLO-1 | Security data | Common control provider for monitoring and response |
| SYS-09 | Enterprise network: SD-WAN, distribution-center networks, OT segmentation; COLO-1 and COLO-2 | On-premises and carrier services | FCI and CUI in transit | AQ-1 connects through a legacy site-to-site VPN |
| SYS-10 | **Federal Solutions CUI Enclave (FSCE)**: collaboration suite, virtual desktops, CUI exchange gateway, and the configuration lab at FL-2 | Government-community cloud offering, FedRAMP authorized at Moderate; lab on-premises | **CUI** | About 190 enclave users; 26 lab workstations; its own CMMC SSP. Conditional Level 2 (C3PAO) |
| SYS-11 | Lifecycle services platform: configuration and imaging factory, ITAD asset tracking, and sanitization records | Cloud provider A plus factory networks at FL-2 and TX-1 | Customer data on devices being sanitized | Service line SL-2 (P09) |
| SYS-12 | Endpoints | All sites | FCI | About 14,500 laptops and desktops |
| SYS-13 | Third parties | Mixed | FCI for carriers and drop-ship partners | About 3,600 suppliers plus about 1,100 IT and service vendors (140 tier-1) |
| SYS-14 | AI portfolio (12 use cases) | Mixed | Some FCI (AI-001 order history) | Governed by the AI governance committee formed in 2025 (P10) |
| SYS-15 | AQ-1 legacy environment: legacy ERP, WMS, directory, and file server at TX-2 | On-premises at TX-2 | None (commercial orders only) | Cutover to SYS-01 and SYS-02 due 2027-03-31 |
| SYS-16 | Productivity suite (email, chat, file storage) | Vendor SaaS (commercial) | FCI | CUI prohibited by policy and blocked by DLP rules for CUI markings |

**SSP system (P02):** the *Order-to-Cash and Fulfillment Platform (OCFP)*: SYS-01 ERP, SYS-02 WMS, SYS-03 reseller commerce platform, and SYS-04 EDI and B2B integration, a high-value system categorized Moderate for confidentiality and integrity with availability treated as High, inheriting common controls from the enterprise platform.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A mature program aligned to CSF 2.0, with annual risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- A 24x7 in-house SOC; EDR on 97% of enterprise endpoints; PAM; quarterly access certification
- Immutable backups in separate accounts; annual disaster recovery tests for tier-1 systems
- A tiered third-party risk program and a C-SCRM plan aligned to NIST SP 800-161 Rev. 1
- Automated Section 889 screening on federal orders: manufacturer of record mandatory in the ERP item master since 2025-03, with a hard block on covered manufacturers
- A Product Authentication Lab at FL-2: 100% inspection of open-market receipts bound for federal orders
- Conditional Level 2 (C3PAO) for the FSCE; Final Level 1 (Self) for the enterprise FCI scope; three DoD-approved medium assurance certificates for DIBNet reporting
- A SOC 2 Type 2 report for the reseller commerce platform (SL-1) since 2024
- CTPAT membership; SEC Item 106 disclosure in the Form 10-K

**Targeted gaps:**
1. **Acquisition integration (AQ-1).** The regional distributor acquired on 2025-10-01 still runs a legacy ERP, WMS, and directory at TX-2. Its site-to-site VPN reaches the EDI translator and the ERP integration layer, EDR covers 61% of AQ-1 endpoints, and the legacy ERP sends no logs to the SIEM.
2. **CMMC closeout and a CUI spill.** 4 of the 6 FSCE POA&M items are still open ahead of the 2026-11-10 deadline. Separately, integrator customers uploaded CUI-marked network drawings to 23 quote requests on the reseller commerce platform, which copied them into the ERP (found 2026-07-08). The OCFP has no CMMC Level 2 status, so CUI there is outside DFARS 252.204-7021(d)(2).
3. **Open-market sourcing.** Commercial open-market receipts are inspected on a 10% sample; OEM serial validation is automated for only 31 of the 40 most-brokered OEMs; firmware hash checks are manual.
4. **Drop-ship screening.** About 22% of federal order lines are drop-shipped by OEMs and authorized distributors. Partner-proposed substitute part numbers are entered as free text and bypass the item-master Section 889 screen.
5. **Distribution-center OT.** OT segmentation is complete at 3 of 4 automated sites (OH-1 is not); 112 HMIs and engineering workstations run unsupported operating systems; OT vendors use always-on remote tools at OH-1 and TX-1.
6. **Reseller platform fraud.** In 2026 H1, 14 fraudulent orders worth $1.3 million were placed through compromised reseller accounts and shipped to freight forwarders. About 430 reseller API integrations use static API keys, 61% older than one year.
7. **EDI concentration.** The primary VAN carries 72% of EDI documents, and failover to the secondary VAN has never been tested end to end.
8. **Materiality.** The SEC materiality playbook (exercised 2025-11 for ransomware) has no product-integrity or supplier-compromise scenario and no guidance on when a supplier event is a "cybersecurity incident" under 17 CFR 229.106(a).
9. **AI.** 12 AI use cases, 8 reviewed by the AI governance committee. Automated reorder release (AI-001) has run since 2026-02 without formal drift monitoring, and the resume screening tool (AI-004) is not ready for the 2027-01-01 CCPA ADMT compliance date.
10. **Third parties and independence.** Staffing agencies and 3PL providers are outside third-party risk tiering. Two Internal Audit IT auditors are former ERP administrators (cooling-off period applies; see P07).

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 | The OCFP, with common control provider inheritance and availability supplements from the High baseline |
| P03 | Primary: NIST SP 800-171 Rev. 2 (110 requirements) for the FSCE under DFARS 252.204-7012 and CMMC Level 2. Also: FAR 52.204-21 (CMMC Level 1) for the enterprise FCI scope; FAR 52.204-25; DFARS 252.246-7008; DFARS 252.204-7012, -7019/-7020, and -7021 clause duties; SEC Item 1.05 and Item 106; CCPA/CPRA; CTPAT; FTC Act Section 5; state breach laws (Florida worked example) |
| P08 | Supplier compromise introducing tampered or counterfeit products into distribution, with an **SEC materiality assessment and Form 8-K Item 1.05** step and a "is this a cybersecurity incident?" decision |
| P09 | SOC 2 Type 2 readiness for two service lines: SL-1 reseller commerce platform (all five categories; Privacy added for 2027) and SL-2 lifecycle services (Security, Confidentiality, Processing Integrity; first report) |
| P10 | Enterprise AI portfolio (12 use cases) with the AI governance committee; full assessment of AI-001 demand forecasting and automated reordering |
| Cloud | Multi-cloud, vendor-agnostic: Cloud provider A, Cloud provider B, a government-community cloud offering for the FSCE, two colocation data centers, and SaaS |
| Supply chain practice | NIST SP 800-161 Rev. 1 (upd1) C-SCRM practices applied through SP 800-53 SR controls |

**Registry defaults kept.** The primary system (order management, warehouse, and reseller portal) is the OCFP. The P08 incident (supplier compromise introducing tampered or counterfeit products) is kept because product integrity is the distributor's largest enterprise risk after ransomware. The P10 use case (demand forecasting and automated reordering) is kept as the fully assessed use case within a 12-item portfolio.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line, with a co-sourced firm for OT) |
| 2026-09-10 | Results to the risk committee of the board |
| 2026-10-20 | C3PAO POA&M closeout certification assessment of the FSCE |
| 2026-11-10 | FSCE closeout deadline (180 days); CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2027-01-15 | Annual Level 1 (Self) self-assessment and affirmation due for the enterprise FCI scope |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Volumes.** About 41,000 order lines and 26,000 shipments per shipping day; about 180,000 active SKUs. Order channels: EDI 46%, reseller platform and APIs 31%, sales desk and email 23%. About 1,100 federal order lines a week.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Accounting Officer | SOX program owner; member of the disclosure committee |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| Chief Privacy Officer | Privacy program (CCPA/CPRA, state laws); breach determinations for personal information |
| Chief Human Resources Officer | Workforce onboarding, terminations, training records; owner of the resume screening tool (AI-004) |
| Chief Data and Analytics Officer | Chairs the AI governance committee |
| Vice President, Enterprise Applications | OCFP system owner (P02) |
| Vice President, Distribution Operations | WMS and distribution-center business owner; owner of the OT environment |
| Vice President, E-commerce | Reseller commerce platform and SL-1 service line owner |
| Vice President, Lifecycle Services | Configuration and ITAD; SL-2 service line owner |
| Vice President, Supply Chain Planning | Forecasting and replenishment; business owner of AI-001 |
| Vice President, Supplier Management | Supplier onboarding, the approved supplier list, the broker program |
| Vice President, Credit and Collections | Reseller credit limits; business owner of AI-003 |
| Vice President, Integration Management Office | Integration of AQ-1 |
| Vice President, Investor Relations; Vice President, Corporate Communications | Investor and media communications during incidents |
| Director, CMMC Program Office | FSCE SSP, scope, SPRS entries, C3PAO liaison, supplier CMMC verification |
| Director, Government Contracts | Flowdowns, Section 889 representations and reports, DIBNet reports, notices to primes and contracting officers |
| Director, Product Authentication Lab | Inspection, testing, and authentication of open-market and suspect product; GIDEP liaison |
| Director, Trade Compliance | CTPAT program; import compliance |
| Director, OT Engineering | Distribution-center OT security |
| Director of Security Operations | Runs the SOC; incident commander for security incidents |
| Director of Identity and Access Management | Identity platform (SYS-07) |
| Director of Cloud Platform Engineering; Director of Network Engineering; Director of Endpoint Engineering | Common control providers for cloud, network, and endpoints |
| Director of Third-Party Risk Management | Vendor tiering, SOC report reviews (in the GRC team) |
| ERP Platform Manager | Day-to-day ERP administration and change control (reports to the Vice President, Enterprise Applications) |

**AQ-1.** Regional distributor acquired 2025-10-01: the TX-2 distribution center, 2 sales offices, about 640 employees, and about $290 million of annual revenue (all commercial). Legacy ERP and WMS on servers at TX-2 with nightly local backups; own directory (not federated); site-to-site VPN to COLO-2. Cutover to SYS-01 and SYS-02 due 2027-03-31.

**CUI spill.** Between 2026-02 and 2026-07, integrator customers attached CUI-marked network drawings to 23 quote requests on SYS-03, which synchronized the files to 23 ERP quote records in SYS-01. A data loss prevention (DLP) pilot scan found them on 2026-07-08. The files were purged from both systems on 2026-07-21; copies in the immutable backups expire under the 35-day retention. The Director, Government Contracts notified the affected primes and contracting officers on 2026-07-22. No access by anyone outside the quoting teams was found.

**Recovery facts (P05).** The ERP and WMS central instances fail over to a second region of Cloud provider A; the 2026-05-09 tier-1 DR test recovered the ERP in 5.5 hours against a 4-hour RTO. WMS edge servers let each distribution center keep picking and shipping for up to 8 hours if the central WMS is down.

**Cyber insurance.** $100 million tower with a $5 million retention.

**Budget.** 2026 Q4 to 2027 Q2 security funding of $7.55 million approved by the executive risk committee on 2026-09-08: AQ-1 integration security $1.6 million; OT segmentation at OH-1 and HMI refresh $2.2 million; reseller API credential modernization and fraud analytics $1.1 million; Product Authentication Lab automation $0.9 million; drop-ship screening integration $0.6 million; CUI upload controls and FSCE closeout $0.45 million; EDI VAN failover $0.35 million; AI governance tooling and bias testing $0.3 million; outside counsel for the supply chain tabletop $0.05 million.

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Chief Accounting Officer, CISO, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. The Chief Supply Chain Officer joins for product-integrity events (added 2026-09).

**Service lines (P09).** SL-1: the reseller commerce platform, used by about 9,500 reseller accounts; SOC 2 Type 2 (Security, Availability, Confidentiality) since 2024. SL-2: lifecycle services (configuration, imaging, and ITAD sanitization) for about 1,200 enterprise customers at FL-2 and TX-1; about 310,000 devices processed a year; no SOC 2 report yet.

**More roles added during the build.**
| Role | Duties in the deliverables |
|---|---|
| Vice President, Corporate Security and Facilities | Physical security of sites, docks, and server rooms; colocation access lists (common control provider CCP-07 in P02) |
| Controller | Vendor master and payment controls; owner of segregation-of-duties fixes (P07 POAM-004) |

**Site footprint for state AI laws (P10).** No sites in Illinois or New York City, and no distribution center in California or Colorado. Remote inside sales staff are hired nationwide.

**Federal stream volumes (P03, P07).** About 5,700 drop-ship federal order lines with partner substitutions in 2026 H1; 38 drop-ship partner agreements; 9 subcontractors receive FCI or CUI; 2 field installation subcontractors receive CUI drawings.

**Reseller fraud and APIs (P01, P07).** 14 fraudulent orders ($1.3 million) in 2026 H1, 9 of them first reported by resellers; IP allow lists cover about 40% of API integrations.

**AI-001 facts (P10).** Auto-release since 2026-02 for authorized-source purchase orders up to $250,000 and within 20% of forecast; about 38% of purchase order lines released automatically from 2026-03 to 2026-08; an OEM price change in 2026-06 led to about $3.1 million of excess inventory over 2 weeks.

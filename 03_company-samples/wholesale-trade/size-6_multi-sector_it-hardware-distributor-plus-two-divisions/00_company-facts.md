# Scenario facts: Cris Santos Company | Wholesale Trade | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was read from eCFR (version date 2026-09-23), the U.S. Code (govinfo), and the CPPA's approved regulation text between 2026-09-25 and 2026-10-04.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a wholly owned operating subsidiary |
| Division 1: IT Distribution (NAICS 423430), **focus of this scenario** | Wholesale distribution of networking, wireless, video surveillance, servers, storage, end-user devices, and software licenses to about 19,000 reseller accounts nationwide. Two specialized units: **Federal Solutions** (sales to DoD and federal customers, directly and through prime contractors, plus 2 federal integration centers that stage and configure equipment for DoD installations) and **Lifecycle Services** (asset tagging, staging, and IT asset disposition (ITAD) with media sanitization for about 300 enterprise customers). About 14,500 employees |
| Division 2: Logistics and Warehousing (NAICS 493110, sector 48-49 Transportation and Warehousing) | Operates 9 distribution centers (DCs) in 7 states that fulfill orders for the two other divisions and provide third-party logistics (3PL) contract fulfillment for about 140 external client companies. Runs a private truck fleet (about 620 tractors) that moves only group freight; external client freight moves by third-party carriers booked through the division's transportation management system. Handles the group's direct imports (the group is importer of record; entries are filed by licensed third-party customs brokers). About 19,500 employees |
| Division 3: Online Retail (NAICS 449210, sector 44-45 Retail Trade) | Consumer e-commerce website and mobile app selling consumer electronics, accessories, and certified refurbished devices, plus an **online marketplace** for about 2,600 third-party sellers. A contact center takes phone orders and service calls. About 6,500 employees |
| Corporate shared services | Identity, security operations, cloud platform, group ERP, EDI and integration, network, HR, finance, legal, trade compliance, supply chain risk, and internal audit. About 4,500 employees |
| Location | Headquartered in Florida. DCs, integration centers, offices, and remote staff in several states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example. No DC or integration center is in California |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| Ownership | Public shareholders. As an SEC registrant the group files Form 8-K Item 1.05 for material cybersecurity incidents and makes the annual Regulation S-K Item 106 disclosure |
| SBA size status | Not small (SBA standard for NAICS 423430 is 250 employees, 13 CFR 121.201) |
| Federal business (Federal Solutions) | About $1.9 billion a year. About 70% is orders exclusively for commercially available off-the-shelf (COTS) products, which carry FAR 52.204-25 but no CMMC requirement (32 CFR 170.3(c)) and no FAR 52.204-21 in COTS subcontracts. About 30% is integration work under subcontracts with 6 DoD prime contractors (Primes A to F) that include DFARS 252.204-7012, 252.204-7019 and -7020, 252.246-7008, FAR 52.204-21, and FAR 52.204-25; awards made from 2025-11-10 also include DFARS 252.204-7021 |
| CUI handled | Prime-provided configuration documents for DoD installations (network drawings, IP addressing plans, device configuration templates, and installation schedules) marked as Controlled Unclassified Information (CUI). They are covered defense information under DFARS 252.204-7012(a) |
| CMMC requirement | Primes A to F have notified Federal Solutions that integration subcontracts and option periods awarded from Phase 2 (2026-11-10, 32 CFR 170.3(e)(2)) require a CMMC Status of **Level 2 (C3PAO)**, flowed down under 32 CFR 170.23(a)(3). The first affected option period (Prime B) starts **2027-04-01**. That requirement is suspended: the DoD (Department of War) CIO memorandum of 2026-07-13 suspended CMMC Phase 2, and under DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5), DoD includes clause 252.204-7021 until 2028-11-09 only when a program office requires a specific CMMC level. During the suspension requiring activities may require Level 1 (Self) or Level 2 (Self). Federal Solutions keeps preparing because it still owes SP 800-171 Rev. 2 under DFARS 252.204-7012, and keeps the 2027-01 C3PAO assessment as a customer-driven choice |
| Payment cards | Online Retail is classified by its acquiring bank as a Level 1 merchant and must deliver an annual PCI DSS Report on Compliance (ROC) signed by a Qualified Security Assessor (QSA). The IT Distribution reseller portal takes business card payments through a payment service provider's hosted payment page and files an annual self-assessment questionnaire with its acquirer. Logistics takes no card payments |
| Not in scope by fact | USCG maritime cybersecurity rule (no vessel or MTSA-regulated facility, 33 CFR parts 104 to 106); TSA security directives (no rail, pipeline, or aviation operations; not an indirect air carrier); FTC Safeguards Rule and Red Flags Rule (consumer financing is extended by third-party lenders at checkout; the group extends no consumer credit, counsel confirmed 2026-06); COPPA (no service directed to children and an age gate on accounts); FACTA receipt truncation (no printed point-of-sale receipts); classified work (none) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board audit and risk committee | Group cyber oversight; accepts Very High risks; receives internal audit results |
| Disclosure committee | SEC materiality of cybersecurity incidents (Form 8-K Item 1.05) |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3); co-accepts High risks |
| Group Chief Risk Officer | Group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group General Counsel | Contracts, notification matrix, SEC and customer notices |
| Group Chief Privacy Officer | Consumer and employee personal information, CCPA program, state breach laws |
| Group CMMC program director | CMMC assessment scope, SPRS submissions, C3PAO coordination; reports to the Group CISO |
| Group supply chain risk director | C-SCRM program (NIST SP 800-161 Rev. 1), approved supplier list, broker program, Section 889 screening list |
| Group trade compliance director | Importer-of-record program, customs broker oversight, CTPAT |
| Group SOC director | 24x7 SOC; incident commander for incidents in shared services |
| Group ERP and platforms director | System owner of the SSP system (OFP) |
| Division presidents (3) | Accept Moderate risks for their divisions. The IT Distribution president is the **CMMC Affirming Official** for the Federal Solutions CAGE code (32 CFR 170.22) |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators and customers; accept Low risks |
| Federal Solutions vice president | Flowdown clauses, Section 889 representations, reports to primes and contracting officers, DIBNet reporting |
| Integration center managers (2) | Day-to-day custodians of CUI at the federal integration centers |
| Lifecycle Services general manager | ITAD and media sanitization service owner |
| Logistics vice president of operations; DC general managers (9) | DC operations, receiving, physical security of DC buildings (including the integration centers inside DC-1 and DC-6) |
| Logistics OT engineering manager | DC automation (conveyors, sortation, automated storage) and its vendors |
| Online Retail PCI compliance manager | PCI DSS program, QSA and acquirer liaison |
| Online Retail marketplace director | Third-party seller onboarding, INFORM Consumers Act compliance, counterfeit listing takedowns |
| Group internal audit | Independent assessor: reports to the board audit and risk committee; assesses common controls once and samples division controls; neither designs nor operates controls |
| External assessors | QSA firm (PCI DSS ROC); CMMC Third-Party Assessment Organization (C3PAO) for the planned Level 2 assessment; SOC 1 service auditor for the 3PL service |

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform: single sign-on, MFA, privileged access management (PAM), identity governance. A separate government-community tenant serves Federal Fulfillment Enclave users | Corporate | Security Protection Asset for the CMMC scope |
| SYS-G2 | Group SOC (24x7, in-house), SIEM, and EDR | Corporate | Security Protection Asset |
| SYS-G3 | Group cloud platform: a commercial landing zone on provider A (WMS, TMS, retail platform, data platform) and a government-community landing zone on provider B (Federal Fulfillment Enclave; services FedRAMP authorized at Moderate or higher), plus the immutable backup vault in a separate provider B account | Corporate | Vendor-agnostic |
| SYS-G4 | Group ERP: order-to-cash, procure-to-pay, inventory, and finance for all three divisions (commercial SaaS) | Corporate | Holds Federal Contract Information (FCI) in DoD orders. **No CUI by policy** |
| SYS-G5 | EDI and integration hub: value-added network, B2B APIs, and the supplier portal (advance ship notices, catalog and price files, returns) | Corporate | About 1,150 trading partners |
| SYS-G6 | Group data and analytics platform (managed data warehouse and machine learning workspace) | Corporate | Trains AI-001 and Online Retail models |
| SYS-D1 | Reseller portal and quoting (B2B e-commerce, vendor SaaS) | IT Distribution | About 41,000 reseller users |
| SYS-D2 | **Federal Fulfillment Enclave (FFE)**: federal order management, the CUI document store, imaging and configuration servers, and the lab networks at the 2 federal integration centers | IT Distribution | CUI. Core of the CMMC Level 2 assessment scope |
| SYS-D3 | Lifecycle Services platform: asset tracking, chain of custody, and sanitization records for ITAD | IT Distribution | Customer asset data |
| SYS-D4 | Demand forecasting and automated reordering (models on SYS-G6; purchase orders released through SYS-G4) | IT Distribution | AI-001 (P10) |
| SYS-D5 | Warehouse management system (WMS), multi-client, with about 6,800 handheld scanners at 9 DCs | Logistics | Runs on provider A. FCI for DoD shipments |
| SYS-D6 | Transportation management system (TMS), fleet telematics, and electronic logging devices | Logistics | Vendor SaaS |
| SYS-D7 | DC automation operational technology (OT): conveyors, sortation, and automated storage and retrieval, with PLC networks at 9 DCs | Logistics | Vendor remote support |
| SYS-D8 | Online Retail storefront and mobile app (commerce platform on provider A; card entry through the payment service provider's hosted payment fields) | Online Retail | PCI DSS scope (payment pages) |
| SYS-D9 | Contact center platform (contact-center-as-a-service) with call recording, and agent desktops that key phone orders into the payment service provider's virtual terminal | Online Retail | PCI DSS scope (cardholder data environment) |
| SYS-D10 | Marketplace seller platform: seller onboarding, identity and bank verification, listings, payouts through a payment facilitator | Online Retail | INFORM Consumers Act data |

**SSP system (P02):** the *Order-to-Fulfillment Platform (OFP)*: the shared order management, warehouse, and reseller portal platform used by all three divisions (group ERP SYS-G4, EDI and integration hub SYS-G5, WMS SYS-D5, and reseller portal SYS-D1), plus the Federal Fulfillment Enclave (SYS-D2) that carries the DoD order stream and forms the core of the CMMC Level 2 assessment scope; it inherits common controls from SYS-G1 to SYS-G3.

## 4. Current security posture: a defined, mostly mature program with gaps that vary by division
**In place today:**
- Group policies aligned to CSF 2.0 (2026 versions) with division supplements, and a common control catalog
- 24x7 group SOC with EDR on managed endpoints and servers
- SSO with MFA for all workforce access to SaaS and cloud consoles; phishing-resistant keys for administrators; PAM with just-in-time elevation
- Quarterly access certification for the ERP and the FFE
- Immutable backups in a separate provider B account, with quarterly restore tests for the ERP integrations and the WMS
- The FFE in a government-community landing zone (since 2025), with CUI marking and a CUI user roster of about 420 people
- A NIST SP 800-171 Basic Assessment for the FFE posted in SPRS on 2025-04-11 (self-assessed score 104); a CMMC Level 1 (Self) affirmation for the FCI systems on 2026-01-15
- A group C-SCRM program based on NIST SP 800-161 Rev. 1: about 2,400 active suppliers, an approved supplier list, and an authorized-source rule for federal orders
- A Section 889 screening list in the ERP item master with a hard block on federal orders (since 2024)
- Online Retail: PCI DSS ROC for 2025 (compliant); quarterly external scans by an Approved Scanning Vendor
- Logistics: annual SOC 1 Type 2 report to 3PL clients (inventory and billing controls)
- CTPAT partner (importer entity) since 2019
- Reg S-K Item 106 disclosure; a disclosure committee charter that covers cybersecurity
- Annual group internal audit of common controls

**Gaps:**
1. **CMMC Level 2 readiness.** The 2025 Basic Assessment covered only the FFE servers. The integration center lab networks were not in it, and CUI was found outside the FFE: about 2,300 CUI-marked documents attached to sales orders in the commercial ERP and about 900 in the commercial collaboration tenant. The 104 score is not supported for the full CUI environment.
2. **Supply chain at scale.** About 180 independent brokers (about 3% of purchase spend) are used for hard-to-find items. About 1,900 of 310,000 active SKUs have no manufacturer of record. The Section 889 block applies to federal orders only, not to refurbished Lifecycle stock or Online Retail listings. DFARS 252.246-7008 flowdown to brokers is incomplete.
3. **Receiving authenticity checks.** Logistics receives for all divisions. OEM serial validation runs at 4 of 9 DCs; firmware verification runs only at the 2 integration centers.
4. **Online Retail payment data.** Contact center call recordings captured spoken card numbers and security codes on about 12% of phone orders sampled (pause-and-resume not enforced). The script inventory and change detection for payment pages cover 1 of 3 storefront brands.
5. **Marketplace sellers.** 46 high-volume sellers are past the 10-day verification window under the INFORM Consumers Act; seller bank data is visible to 210 support staff; counterfeit listing reports rose 40% in 2026.
6. **DC operational technology.** PLC networks at 5 of 9 DCs share a flat network with WMS handhelds. Three automation vendors keep persistent remote access tunnels. OT is not monitored by the SOC.
7. **WMS access.** Two DCs acquired in 2025 use shared handheld logins. MFA is not enforced for 3PL client users of the WMS web console.
8. **Common control inheritance** is documented for IT Distribution (FFE SSP draft) and Online Retail (PCI responsibility matrix), but not for Logistics (WMS, TMS, OT).
9. **Division supplement drift.** The Logistics supplement was last aligned to group policy in 2024 and conflicts with group rules on shared accounts and vendor remote access.
10. **Cross-division incident notification.** A product-integrity incident would trigger DoD and prime reports, contracting officer notices, customer notices in three divisions, possible state breach notices, and an SEC materiality decision. The group notification matrix has not been exercised. Only 2 people (both at Federal Solutions headquarters) hold DoD-approved medium assurance certificates for DIBNet.
11. **AI governance.** The Group AI Standard was adopted in 2026-05. AI-001 automatic release of purchase orders was enabled on 2026-02-02, before the standard, and Logistics and Online Retail use cases were not assessed.
12. **CCPA program.** The first CCPA cybersecurity audit report is due 2028-04-01, and no risk assessment has been started for sharing personal information for cross-context behavioral advertising.
13. **Lifecycle Services ITAD.** Sanitization verification sampling is not documented for 2 of 5 processing lines; enterprise customers ask for a SOC 2 report.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Primary: NIST SP 800-171 Rev. 2 (110 requirements) for the IT Distribution CUI environment, as required by DFARS 252.204-7012 and assessed under CMMC Level 2, plus clause duties (FAR 52.204-21, 52.204-25, DFARS 252.246-7008, 252.204-7012, -7019, -7020, -7021). Division tables: Online Retail (PCI DSS v4.0.1, INFORM Consumers Act, CCPA) and Logistics (FCI safeguarding for DoD shipments, CTPAT cybersecurity criteria, OT and 3PL contract duties). One regulation-by-division matrix |
| P08 | Supplier compromise introducing tampered products into distribution, spanning all three divisions: a compromised authorized distributor ships switches and consumer mesh routers with altered firmware; Logistics receives them, IT Distribution sells them to resellers and uses some in a DoD integration job, and Online Retail sells them to consumers. Multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 scoped per division: Logistics 3PL fulfillment (true service organization; Security and Availability) and IT Distribution Lifecycle Services ITAD (Security and Confidentiality) are in scope; Online Retail is out of scope (PCI DSS is its assurance); core distribution and Federal Solutions are out of scope (reasons in P09) |
| P10 | Group AI governance program. Priority use case: demand forecasting and automated reordering (AI-001, registry default kept), plus division use cases with their rules |
| Cloud | Shared corporate platform plus division workloads, vendor-agnostic: provider A (commercial) and provider B (government-community region for the FFE, and the backup vault) |
| Supply chain practice | NIST SP 800-161 Rev. 1 C-SCRM practices, applied through SP 800-53 SR controls |

**Registry defaults kept:** the primary system (order management, warehouse, and reseller portal) is kept and made a shared corporate platform because all three divisions run on the same ERP and WMS. The P08 incident and the P10 use case are kept, and the incident is extended across divisions.

## 6. Assessment calendar (fictional unless a regulation is cited)
| Date | Event |
|---|---|
| 2025-04-11 | NIST SP 800-171 Basic Assessment for the FFE posted in SPRS (score 104) |
| 2025-11-10 | CMMC Phase 1 begins (DFARS rule effective date, 90 FR 43560) |
| 2026-01-15 | CMMC Level 1 (Self) affirmation for the FCI systems |
| 2026-02-02 | AI-001 automatic release of purchase orders enabled |
| 2026-05-04 to 2026-07-31 | Group and division BIAs, risk analyses, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-09-15 | Results to the board audit and risk committee; deliverables approved |
| 2026-11-10 | Planned CMMC Phase 2 start (32 CFR 170.3(e)(2)), suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 |
| 2026-11-02 to 2026-11-20 | PCI DSS 2026 ROC fieldwork by the QSA (Online Retail) |
| 2027-01-11 to 2027-01-22 | Planned CMMC Level 2 (C3PAO) assessment of the CUI environment (customer-driven while CMMC Phase 2 is suspended) |
| 2027-04-01 | First prime option period that was to require Level 2 (C3PAO) (Prime B); requirement suspended with CMMC Phase 2 |
| 2028-04-01 | First CCPA cybersecurity audit report due (2026 revenue over $100 million; Cal. Code Regs. tit. 11, 7121) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Revenue split (fictional) | IT Distribution about $12.6 billion (about $34.5 million per day); Logistics about $1.4 billion external (3PL) revenue; Online Retail about $4.0 billion (about $11 million per day). Total about $18.0 billion |
| IT Distribution volumes | About 310,000 active SKUs; about 85,000 order lines per shipping day; about 1,100 integration jobs per year at 2 federal integration centers (IC-1 inside DC-1 in Florida, IC-2 inside DC-6); about 14,000 CUI documents in the FFE |
| Logistics volumes | About 210,000 outbound shipments per day across 9 DCs; DC-8 and DC-9 acquired 2025-06; about 140 3PL clients with about 1,900 client users in the WMS web console |
| Online Retail volumes | About 5.8 million active customer accounts (about 640,000 in California); about 25 million orders a year, about 6% by phone; 2,400 contact center agents; 2,600 marketplace sellers, of which about 780 are high-volume sellers under 15 U.S.C. 45f(f)(3) and about 310 have $20,000 or more in annual gross revenue on the marketplace (disclosure duty, 45f(b)(1)) |
| Employees in California | About 1,300 (sales staff and remote contact center agents). No DC or integration center in California |
| Cyber insurance | $150 million tower; $10 million retention; the primary carrier must be called before incident vendors are engaged |
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board audit and risk committee; temporary only, with a dated plan. Very High: board audit and risk committee only |
| Medium assurance certificates | Held by the Federal Solutions vice president and the Federal Solutions contracts director. Two more planned (IC-2 manager and the Group SOC director) by 2026-11-30 |
| SKU and supplier facts (P03, P07) | The item master lists 41 SKUs whose OEM of record is a covered manufacturer under FAR 52.204-25; all are blocked on federal orders, 12 are still sold commercially through Online Retail marketplace listings by third-party sellers and 3 appear in Lifecycle refurbished stock |

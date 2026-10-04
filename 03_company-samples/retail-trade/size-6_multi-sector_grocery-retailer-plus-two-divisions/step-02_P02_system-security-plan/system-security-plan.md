# System Security Plan: E-commerce and Point-of-Sale Platform (EPP)

**Organization:** Cris Santos Company Holdings, Inc. (Grocery Retail division, Cris Santos Markets, LLC, inheriting group common controls) | **Tier:** Multi-Sector | **Vertical:** Retail Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **E-commerce and Point-of-Sale Platform**, the focus division's primary system, because the BIA ranks in-store checkout and online ordering highest (P05 BP-RT01, BP-RT02), it is the retail cardholder data environment (CDE) validated each year by a QSA Report on Compliance, and it carries the group's top risk (P01 GR-01, payment page script compromise). It inherits most of its general controls from corporate (SYS-G1 to SYS-G4), so this plan also shows how group common controls are documented. The wholesale Retailer Services Portal (SYS-D5) and the Financial Services card and lending platform (SYS-D6) inherit from the same catalog but have no documented inheritance yet (scenario gap 9; POAM-018).

## 1. System Name and Identifier
E-commerce and Point-of-Sale Platform (**EPP**), identifier CSCH-SYS-D1-EPP. SYS-D1 in `../00_company-facts.md`.

## 2. System Overview
The EPP sells groceries to consumers in 380 stores and online. It supports:
- **In-store checkout** at about 4,900 lanes (including self-checkout) with EMV PIN pads, for about 330 million transactions a year, about 257 million of them by payment card;
- **SNAP EBT** acceptance on the same PIN pads (every store is an authorized SNAP retailer, 7 CFR 278.1);
- **Online ordering** on the website and mobile app (about 12.6 million orders a year) with curbside pickup and delivery;
- **Rewards Card** purchases in stores and online, authorized by Financial Services (SYS-D6) through the payment switch.

About 36,500 Grocery Retail workforce users have EPP roles (cashiers, store managers, digital and operations staff), plus about 140 administrators and 30 POS vendor technicians.

**Major components:**
- **Store POS estate:** lanes and self-checkout units, PCI PTS-approved PIN pads that encrypt card data under the processor's encryption solution (not a PCI-listed validated P2PE solution, so the store systems remain in PCI DSS scope), and one store controller per store
- **Store networks (CDE segments):** POS VLANs and store firewalls, managed centrally (other store infrastructure, SYS-D3, is outside the boundary)
- **Payment switch:** runs active-active in the two group colocation data centers; routes brand card, Rewards Card, and EBT authorizations; hardware security modules for key management
- **Legacy store gateway:** connects the 46 stores acquired in 2025 until their migration (due 2027-06-30)
- **Storefront and order services:** containers and managed databases in cloud provider A, warm standby in provider B; checkout uses the **processor's hosted payment fields** for brand cards (web) and the processor's mobile SDK (app); card-on-file uses processor tokens
- **Storefront administration console and release pipeline**

The plan describes services by category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the EPP |
|---|---|---|---|
| N44-45-R01 | PCI DSS v4.0.1 | PCI SSC, June 2024 (industry standard enforced through the merchant agreement, not law) | The EPP is the retail CDE. The acquirer confirmed Level 1 and an annual ROC by a QSA (letter of 2026-02-02, fictional). Visa assigns Level 1 to merchants with more than 6 million Visa transactions a year (Visa compliance validation page, checked 2026-10-04) |
| N44-45-R02 | FTC Act Section 5 | 15 U.S.C. 45(a), 45(n) | Security and privacy representations to online customers; reasonable security for customer accounts |
| N44-45-R03 | FTC Safeguards Rule (applies to Financial Services) | 16 CFR Part 314 | The Rewards Card number is Financial Services customer information handled on the EPP checkout "on behalf of" an affiliate (definition of customer information, 16 CFR 314.2). The EPP must protect it to the Financial Services program's standard (scenario gap 2) |
| N44-45-R05 | FACTA receipt truncation | 15 U.S.C. 1681c(g) | Lane and online receipts show no more than the last 5 digits and no expiration date |
| SNAP | Retailer authorization | 7 CFR 278.1 | Every store is an authorized SNAP retailer. EBT data is outside PCI DSS but protected the same way |
| N52-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | An EPP compromise may be material to the group (P08) |
| State law | Breach notification | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Card numbers with security codes and online credentials are personal information (P08) |
| Contracts | Merchant agreement; processor agreement; POS vendor and storefront vendor contracts | Fictional terms in `../00_company-facts.md` section 7 | 24-hour acquirer notice; ROC and AOC each December 15; TPSP responsibilities |
| Internal | Group policies POL-01 to POL-05 and the Grocery Retail supplement | P06 | |

Not applicable: HIPAA (no pharmacies), CCPA (no California business), COPPA (not directed to children), INFORM Consumers Act (no third-party sellers).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the Grocery Retail CIO (system owner) on 2026-09-10, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) no new script on any payment page without EPP change approval, and payment page alerts routed to the SOC, by 2026-11-30 (POAM-001, POAM-002); (2) the Rewards Card field moved into an isolated payment frame operated by Financial Services by 2027-03-31 (POAM-004); (3) the stray card numbers on the finance file share deleted and the share removed from the CDE path by 2026-10-31 (POAM-005); (4) the 46 acquired stores segmented, tested, and in the SIEM before the 2026 ROC fieldwork closes, or carved out of the ROC with the acquirer's agreement (POAM-006 to POAM-009).
- **Reauthorization:** annually with the ROC, or on completion of the acquired store migration.

### 4.3 System Operational Status
Operational. **Major modifications planned:** acquired store migration to the standard POS (2027-06-30); payment frame for the Rewards Card (2027-03-31); payment page script governance across divisions (2026-11-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Grocery Retail CIO | Accountable for the EPP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Division security and compliance lead | Grocery Retail CISO | PCI DSS program and ROC; responsible for information security for the merchant (PCI DSS 12.1.4) |
| Checkout page owner | Grocery Retail chief digital officer | Approves scripts and changes on checkout pages (6.4.3) |
| Rewards Card data owner | Financial Services CISO (Qualified Individual) | Sets the protection standard for Rewards Card data on the checkout (16 CFR 314.4) |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director and Group network director (SYS-G3), Group digital director (SYS-G4) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessors | Group internal audit; the QSA firm | P07 common control assessment; annual ROC |

## 6. System Information Types and System Categorization
The information types below are organization-defined, rated with the FIPS 199 method.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment card data (brand cards in transit, tokens, truncated numbers) | **High** | Moderate | **High** | Compromise of card data at this volume would bring acquirer, card brand, state, and SEC consequences. Card authorization must be available for stores to sell (P05 BP-RT01: MTD 2 hours) |
| Rewards Card and EBT data in transit | High | Moderate | High | Financial Services customer information and SNAP benefits; the same lanes and switch carry them |
| Customer accounts and orders (names, addresses, order history, online credentials) | Moderate | Moderate | Moderate | About 9.6 million loyalty members and online accounts; online ordering MTD 8 hours (BP-RT02) |
| Prices and item data | Low | **High** | Moderate | Price integrity at the register is a consumer protection matter; payment pages must not be altered |
| Information security (keys, configurations, logs) | High | High | Moderate | Compromise would expose every component |
| **EPP category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **124 controls** in `control-implementation.csv`:
- 121 from the High baseline;
- 3 program management controls not in any baseline (PM-1, PM-2, PM-9).

Other High-baseline controls are either fully inherited from the cloud and colocation providers (for example, most PE controls) or tailored out with a reason in the group tailoring register (for example, controls for systems the EPP does not include).

**CSF 2.0 references.** The `csf2_subcategories` column comes from the NIST CSF 2.0 to SP 800-53 Rev. 5 crosswalk in `00_universal-framework/crosswalks/`. Twelve controls have no entry there (AC-11, AC-21, AU-8, CA-6, IR-2, MA-4, MP-6, PL-4, PS-3, PS-4, PS-8, SC-18); for those, the subcategory is an **author mapping**.

## 7. Authorization Boundary Description
- **Inside:** store POS estate (lanes, self-checkout, PIN pads, store controllers, POS VLANs and store firewalls), the payment switch and its hardware security modules in both data centers, the legacy store gateway, storefront and order services in cloud provider A and the warm standby in provider B, the storefront administration console, and the release pipeline.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SIEM, and EDR, SYS-G3 landing zones and data center facilities, and SYS-G4 (content delivery, web application firewall, tag management, customer identity).
- **Outside, interconnected:** the payment processor (brand card authorization, hosted payment fields, tokens), the state EBT processors, SYS-D6 (Rewards Card authorization), SYS-D2 (loyalty lookups at the lanes; order data to the CDP), SYS-G5 ERP (sales, settlement, and price files), the delivery partner (orders without card data).

**PCI DSS scope versus SSP boundary.** The PCI scope document (12.5.2) covers the same components, plus connected-to systems (identity, SIEM, the PAM vaults, the jump hosts). The SSP boundary is narrower because those connected systems are documented in the common control catalog. The finance file share where stray card numbers were found (SYS-G5) is **not** in scope by design and is being cleaned (POAM-005).

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Payment processor | Outbound and inbound | Brand card authorization (encrypted at the PIN pad), hosted payment fields, tokens, settlement files | Processor agreement; processor AOC as a service provider (12.8.4) |
| State EBT processors | Outbound and inbound | EBT authorizations | SNAP retailer agreements; state processor terms |
| SYS-D6 card processing platform (Financial Services) | Outbound and inbound | Rewards Card authorizations; Rewards Card number and code from the online checkout | Intercompany service agreement (2023). **Gap:** no protection standard for the checkout field (POAM-004) |
| SYS-G4 tag management service | Inbound to customer browsers | Third-party scripts on storefront pages, including checkout | Group digital standard. **Gap:** "all pages" containers bypass EPP change approval (POAM-001) |
| SYS-D2 loyalty and CDP | Outbound | Loyalty IDs, baskets, order history (no card data) | Grocery Retail data standard |
| SYS-G5 ERP | Outbound and inbound | Sales and settlement summaries; nightly price files | Group data standard |
| Delivery partner | Outbound | Delivery orders (no card data) | Delivery partner agreement |
| POS vendor support | Inbound | Remote maintenance through PAM; through the vendor's own tool at the 46 acquired stores (POAM-007) | POS vendor contract |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Lanes, self-checkout, PIN pads (about 4,900 lanes) | Hardware and POS software | 380 stores | Grocery Retail store technology director |
| Store controllers (380) and POS VLANs | Servers and network | 380 stores | Grocery Retail store technology director |
| Payment switch and hardware security modules | Servers and HSMs | Two group colocation data centers | Grocery Retail payments director |
| Legacy store gateway | Server | Primary data center | Grocery Retail payments director |
| Storefront and order services | Containers and managed databases (PaaS) | Provider A; warm standby in provider B | Grocery Retail chief digital officer |
| Storefront administration console and release pipeline | SaaS tooling and pipeline | Provider A | Grocery Retail chief digital officer |
| Backups and DR replicas | Object storage and backup service | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (124 controls) and `common-control-catalog.csv` (106 group common controls offered to the EPP).

| Status | Controls |
|---|---|
| Implemented | 104 |
| Partially implemented | 20 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **124** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1 to SYS-G4 or group functions) | 67 |
| Hybrid (group provides the mechanism; the EPP configures or operates part) | 39 |
| System-specific | 18 |

**The 20 partially implemented controls** cluster in four places:
- **Payment pages and shared tag management** (scenario gaps 1 and 2): CM-3, CM-8, SC-18, SI-4, SI-7, SA-9, AC-4.
- **The 46 acquired stores** (gap 3): AC-17, AU-6, AU-12, CA-8, IA-2(1), SC-7, SI-2.
- **Account and data hygiene** (gap 4 and payment switch accounts): AC-2, IA-5, CM-12.
- **Cross-division incident response** (gap 10): IR-3, IR-6, IR-8.

### 10.2 Common control inheritance by division
The common control catalog lists the 106 controls corporate offers. Inheritance is **documented for the EPP** (the PCI responsibility matrix maps each PCI DSS requirement to the group provider, the EPP, or the processor). It is **not documented** for the Retailer Services Portal (SYS-D5), and only partly for the card and lending platform (SYS-D6), whose Safeguards program names SYS-G1 and SYS-G2 but not which safeguards they meet (scenario gap 9). Until POAM-018 closes, the Financial Services Qualified Individual cannot show which 16 CFR 314.4(c) safeguards group controls meet, and P07 found CA-2 determination statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and EPP and division controls sampled, from 2026-07-01 to 2026-08-31 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`. The QSA's 2026 ROC fieldwork is planned for 2026-10-19 to 2026-11-20.

## 11. Digital Identity Acceptance Statement
- **Workforce users** sign in through SYS-G1 with MFA. **Administrators** of CDE components use phishing-resistant authenticators and just-in-time PAM elevation (PCI DSS 8.4.1, 8.4.2). Store manager back office accounts at the 46 acquired stores are the exception until POAM-007 closes.
- **Cashiers** use unique operator IDs at the lanes; lanes do not give access to card data.
- **Application and system accounts** in the payment switch should be vaulted and rotated; 9 still use static passwords (POAM-010).
- **Customers** use the group customer identity service (SYS-G4) for online accounts. They never access CDE components; card data goes from the browser to the processor's hosted fields.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10), the 2025 ROC and AOC, the PCI scope document, and the PCI responsibility matrix.

## 13. Acronym List and Glossary
- **AOC:** Attestation of Compliance
- **ASV:** Approved Scanning Vendor
- **CDE:** cardholder data environment
- **EBT:** electronic benefit transfer (SNAP)
- **EPP:** E-commerce and Point-of-Sale Platform
- **Hosted payment fields:** payment inputs served by the processor inside frames on the merchant's page, so card data goes from the browser to the processor
- **PAM:** privileged access management
- **PIN pad:** the point-of-interaction device where customers insert or tap cards
- **QSA:** Qualified Security Assessor
- **ROC:** Report on Compliance
- **Tag management service:** the group service that loads third-party scripts onto web pages
- **TPSP:** third-party service provider

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Grocery Retail CIO |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Group CISO |

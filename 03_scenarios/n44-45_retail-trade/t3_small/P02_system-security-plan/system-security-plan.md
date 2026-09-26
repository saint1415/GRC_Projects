# System Security Plan: E-commerce and Loyalty Platform (ELP)

**Organization:** Cris Santos Company, LLC (independent grocery retailer) | **Tier:** Small | **Vertical:** Retail Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
E-commerce and Loyalty Platform (**ELP**), identifier CSC-SYS-001.

## 2. System Overview
The ELP runs the company's online store and its loyalty program. Customers browse, order, and pay online, then pick up at the curb or get local delivery. Shoppers in the store scan their loyalty number at the register. The pricing and offers engine sets online prices and personalized loyalty offers. The ELP serves about 9,500 online shopping accounts and about 21,000 loyalty members.

**Major components:**
- **SYS-01:** a SaaS e-commerce storefront. Its checkout page embeds the payment processor's card form
- **SYS-03:** the loyalty database and loyalty API
- **SYS-04:** the public-cloud tenant (PaaS and IaaS) that hosts SYS-03, its exports, and its backups
- **SYS-09:** the identity provider for single sign-on and MFA
- **SYS-12:** the pricing and personalized offers engine (vendor SaaS; see P10)
- **SYS-11 (administrator endpoints only):** 5 PCs and laptops used to manage the platform

**Card data is not stored, processed, or transmitted by the ELP.** Card numbers are typed into the processor's embedded form and go straight to the processor, which returns a token. The ELP is still security-relevant to card data, because anyone who can change the checkout page can capture what customers type (PCI DSS v4.0.1 Requirements 6.4.3 and 11.6.1; P03).

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N44-45-R01 | PCI DSS v4.0.1 (contractual standard, enforced through the merchant agreement; not law) | PCI SSC, June 2024. Validation by SAQ A for the online channel, as confirmed by the acquirer on 2026-06-15 |
| N44-45-R02 | FTC Act Section 5 | 15 U.S.C. 45(a) and 45(n): privacy and security representations, reasonable security, pricing claims |
| State | Florida breach notification | Fla. Stat. 501.171. Covers card numbers with security codes, and an email address with a password for an online account |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- FTC Safeguards Rule (N44-45-R03) and Red Flags Rule (N44-45-R04), because the company extends no credit.
- CCPA (N44-45-R06), because the company does not do business in California and is below the revenue threshold.
- COPPA (N44-45-R07), because the site is not directed to children and members must be 18 or older.
- INFORM Consumers Act (N44-45-R08), because the storefront has no third-party sellers.
- FACTA receipt truncation (N44-45-R05) applies to store receipts, which are outside this system (P03 row G-075).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the General Manager on 2026-09-04.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The General Manager accepted operation of the ELP on 2026-09-04, with the conditions in the P07 POA&M.
- The majority owner accepted the High risks listed in P01 (R-001, R-002, R-004) with dated treatment plans.
- **Condition:** the payment-page script controls (POAM-003 and POAM-004) must be in place before the 2026 SAQ A is signed (due 2026-11-30).
### 4.3 System Operational Status
Operational. Major modifications planned:
- payment page script management and monitoring (P01 R-001), due 2026-11-15;
- a separate-account backup copy for the loyalty database (P01 R-013), due 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | E-commerce and Marketing Manager | Business owner of the storefront, loyalty program, and pricing engine |
| Authorizing official equivalent | General Manager | Accepts operation and risks up to Moderate |
| Risk acceptor for High and Very High | Majority owner | Accepts High risks with dated treatment plans |
| Information Security Lead | IT Manager | Day-to-day security, identity provider, cloud tenant, PCI DSS contact |
| Vendor and contract owner | Controller | Merchant agreement, SAQs, service provider contracts |
| External support | Marketing contractor; storefront vendor; cloud provider; pricing engine vendor | Theme and tag changes (contractor); platform operation (vendors) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer and loyalty member records (contact details, purchase history, account credentials) | Moderate | Moderate | Low | Disclosure harms customers and can trigger breach duties (credentials) and FTC exposure; loyalty outages do not stop sales (P05 BP-06 MTD 72 h) |
| Online orders and the checkout page that hosts the payment form | Moderate | Moderate | Moderate | A changed checkout page can expose card data typed by customers; online ordering is about 12% of sales (P05 BP-02 MTD 24 h) |
| Prices and personalized offers | Low | Moderate | Low | Wrong or unfair prices harm customers and create FTC exposure; shelf prices can be used if the engine is paused |
| Workforce identities (administrator accounts) | Moderate | Moderate | Low | Administrator takeover leads to page tampering |
| **ELP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person grocer. The plan documents 67 controls (66 from the Moderate baseline plus PT-5 from the privacy baseline) that address the PCI DSS requirements in scope for the online channel (P03), FTC reasonable-security expectations, and core hygiene. See `control-implementation.csv`. Every other Moderate-baseline control is handled one of two ways:
- **Inherited** from the storefront vendor, cloud provider, and identity provider, as evidenced by their SOC 2 reports and PCI DSS AOCs (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems or to larger programs.

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services:
- **Inside:** the storefront configuration, theme code, installed apps, and scripts; the loyalty database, API, exports, and backups in the cloud tenant; the identity provider tenant; the pricing engine configuration; 5 administrator PCs and laptops.
- **Outside (external services, interconnected):**
  - the payment processor (embedded form, tokens, merchant portal);
  - the storefront vendor's platform;
  - the cloud provider's infrastructure;
  - the pricing engine vendor's platform;
  - the POS system (loyalty lookups only);
  - the back office and inventory system (nightly price file);
  - the productivity suite (email).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Payment processor (SYS-02) | Customer browser to processor; token back to storefront | Card data (processor side only); payment tokens | Merchant agreement; processor service provider AOC (2024, **update needed**) |
| POS system (SYS-05) | Bidirectional (loyalty API) | Member lookup by phone number, points, offers | POS vendor service contract |
| Back office and inventory (SYS-06) | Inbound nightly | Items and shelf prices | Vendor SaaS terms |
| Pricing engine (SYS-12) | Bidirectional | Purchase history, ZIP code, delivery zone out; prices and offers in | Vendor terms; **no data use clause (gap)** |
| Marketing contractor | Outbound email | Full loyalty exports | **No data use or security terms (gap)** |
| Productivity suite (SYS-10) | Outbound | Order and account emails to customers | Vendor SaaS terms |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Storefront tenant, theme, apps, checkout scripts | SaaS | Storefront vendor | E-commerce and Marketing Manager |
| Loyalty database | Managed database (PaaS) | Cloud tenant | IT Manager |
| Loyalty API | Application service (PaaS) | Cloud tenant | IT Manager |
| Export storage and backup vault | Object storage; cloud backup service | Cloud tenant (same account, **gap**) | IT Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Pricing and offers engine configuration | SaaS add-on | Pricing engine vendor | E-commerce and Marketing Manager |
| Administrator PCs and laptops (5) | Endpoint | Store office | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 67 controls:
- Implemented: 18
- Partially implemented: 35
- Planned: 14

By inheritance: 41 system-specific, 16 hybrid, 10 common/inherited from providers.

### 10.2 Control assessment status
Assessed 2026-08-10 to 2026-08-14. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Employees and administrators authenticate through the identity provider with a password and a second factor (an authenticator app with number matching). This is appropriate for administrative access given the Moderate categorization. Two local storefront administrator accounts do not use the identity provider and have no MFA; both are being removed (POAM-001 and POAM-006).

Customers sign in to online shopping accounts with an email address and password managed by the storefront vendor. Bot protection and login rate limits are being turned on (P01 R-011). Customer identity is governed by the vendor's platform, with the settings above under company control.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor reviews (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **CDE:** cardholder data environment
- **ELP:** E-commerce and Loyalty Platform
- **MFA:** multi-factor authentication
- **P2PE:** point-to-point encryption
- **POA&M:** plan of action and milestones
- **SAQ:** self-assessment questionnaire (PCI DSS)
- **TPSP:** third-party service provider

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial plan | IT Manager |

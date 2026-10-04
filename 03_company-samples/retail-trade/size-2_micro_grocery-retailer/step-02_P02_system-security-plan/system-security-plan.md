# System Security Plan: Store Commerce Platform (SCP)

**Organization:** Cris Santos Company, LLC (neighborhood grocery store with online ordering) | **Tier:** Micro | **Vertical:** Retail Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Store Commerce Platform (**SCP**), identifier CSC-SYS-001.

## 2. System Overview
The SCP supports every way the store sells: in-store checkout with card, SNAP EBT, and cash; online ordering with curbside pickup and local delivery; the loyalty program; and item pricing and markdowns. It serves 7 workforce members, about 2,400 loyalty members, and about 850 online shoppers, and handles about 31,000 card transactions a year.

The store owns almost no infrastructure. One payment and commerce platform provider supplies the POS app, the card terminals, card processing, the online store, the loyalty directory, and an AI offers and markdown feature. A managed service provider (MSP) runs the office computers, firewall, and Wi-Fi. This plan therefore says, for each control, what the store does itself, what the MSP does for it, and what it inherits from the provider.

**Major components:**
- **SYS-01:** commerce platform (vendor SaaS): POS app, back office dashboard, card processing, customer directory and loyalty
- **SYS-02:** online store (same provider): catalog, customer accounts, ordering, provider-hosted checkout
- **SYS-03:** 2 countertop card terminals in the provider's validated P2PE solution, and 1 mobile card reader that is **not** part of that solution
- **SYS-05 (in part):** the office PC and Owner laptop that administer the platform, 2 POS tablets, and the store phone
- **SYS-06 (in part):** the store firewall and Wi-Fi that carry terminal and tablet traffic (MSP-managed)
- **SYS-10:** AI offers and markdown suggestions (a feature inside SYS-01; assessed in P10)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N44-45-R01 | PCI DSS v4.0.1 (contractual, through the merchant agreement; not law) | PCI SSC, June 2024. Validation by SAQ P2PE (store) and SAQ A (online), due 2026-11-30 |
| N44-45-R02 | FTC Act Section 5 (unfair or deceptive practices: data security, privacy statements, pricing and offer claims) | 15 U.S.C. 45(a), 45(n) |
| N44-45-R05 | FACTA receipt truncation | 15 U.S.C. 1681c(g) |
| State | Florida Information Protection Act: reasonable measures, breach notice, record disposal | Fla. Stat. 501.171(2), (3)-(6), (8) |
| State | Price gouging during a declared state of emergency (relevant to AI markdown suggestions) | Fla. Stat. 501.160 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable:
- FTC Safeguards Rule and Red Flags Rule (N44-45-R03, R04): no store credit, house accounts, or deferred payment.
- CCPA (N44-45-R06): no California business; far below the revenue threshold.
- COPPA (N44-45-R07): the online store is not directed to children.
- INFORM Consumers Act (N44-45-R08): no third-party sellers.
- HIPAA: the store has no pharmacy.

The store is an FNS-authorized SNAP retailer (7 CFR 278.1). SNAP EBT is read on the same P2PE terminals; SNAP program rules are outside this plan.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-08-31.

### 4.2 System Authorization Decision
The store is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner accepted continued operation of the SCP, on the conditions that (1) the scripts are removed from the checkout page and MFA is on for every administrator login by 2026-10-15, (2) the mobile card reader is retired or replaced with a P2PE device before the 2026 SAQs are signed, and (3) the other POA&M items in P07 are completed by their dates.

### 4.3 System Operational Status
Operational. Planned changes: checkout script clean-up and payment page monitoring (P01 R-001), MFA for all administrators (R-002), retirement of the mobile reader (R-003), a separate network for terminals and tablets (R-006, R-007), and a cellular failover router (R-014), all due by 2026-11-30.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner | Overall accountability; accepts Moderate and higher risk; approves this plan, policies, and spending; signs the SAQs |
| Security and PCI Lead | Store Manager | Day-to-day security (designated in writing 2026-07-15); maintains this plan, the risk register, the terminal list, and user accounts |
| Vendor and contract contact | Bookkeeper | Merchant agreement, provider compliance notices, insurance, freelancer agreement |
| IT operations | MSP | Office PC and laptop, firewall, Wi-Fi, mailbox administration, office PC backup |
| Online store design | Marketing freelancer (external) | Design and marketing content, under the Store Manager's approval from 2026-09-30 |
| Independent assessor | Security consultant | Yearly control assessment (P07) |

**Where roles overlap.** The Store Manager both runs and checks most controls. This is normal at 7 people. It is compensated by the Owner's monthly review of the POA&M, MSP reports as outside evidence, the provider's AOC and SOC 2 report, and a yearly assessment by someone who operates no control (P07).

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer services (orders, loyalty profiles, online accounts) | Moderate | Moderate | Moderate | Disclosure harms customers and trust; wrong orders or prices harm customers; online orders tolerate a day (P05 MTD 24 h) |
| Payments and collections (card and EBT transactions, payouts) | Moderate | Moderate | Moderate | Card data is encrypted at capture, but skimming or a redirected payout causes direct loss; card payments are needed within 2 hours (P05 BP-01) |
| Inventory control (items, costs, prices, markdowns) | Low | Moderate | Low | Wrong prices or markdowns cause losses and claims issues; tolerates 48 hours |
| **SCP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person store. The plan documents 44 controls that carry the PCI DSS requirements in scope, the FTC reasonable security expectation, and basic hygiene (see `control-implementation.csv`); 2 of them (PM-2, PT-5) are added by tailoring. All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the provider (platform, application, physical, and card processing controls), with the provider's AOC and SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with in-house IT staff (for example, configuration change boards and separate development environments). These are tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the store controls or pays someone to control on its behalf:
- **Inside:** the store's platform account, users, roles, and settings (SYS-01), the online store's settings, design, and custom code (SYS-02), the 3 card devices (SYS-03), the AI feature settings (SYS-10), the office PC, laptop, POS tablets, and store phone (SYS-05), and the store firewall and Wi-Fi (SYS-06).
- **Outside (external services, interconnected):** the provider's own platform, data centers, P2PE decryption environment, and processing network; the productivity suite (SYS-04); the accounting SaaS and payroll service (SYS-07); the MSP's remote management platform and the office PC backup (SYS-11); the temperature sensors (SYS-08) and cameras (SYS-09), which share the staff Wi-Fi today but do not support the SCP.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Provider processing network (through SYS-01 and SYS-03) | Bidirectional | Encrypted card and EBT data out; authorizations, tokens, and settlement in | Merchant agreement; provider AOC |
| Payout bank account | Inbound | Daily settlement deposits | Merchant agreement |
| Accounting SaaS (SYS-07) | Outbound | Daily sales summary | Vendor terms |
| Productivity suite (SYS-04) | Inbound | Order alerts and customer emails | Vendor terms |
| Marketing freelancer | Bidirectional | Online store design; a 2025 loyalty export by email | **No written agreement (gap; SA-9)** |
| Third-party script vendors (4) | Outbound from customers' browsers | Page views and anything the scripts can read on the page | **None (gap; CM-7, SI-7)** |
| MSP remote management platform | Inbound administrative access | Office PC and laptop management | MSP service contract |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Platform account, dashboard, and POS app (SYS-01) | SaaS | Provider | Store Manager |
| Online store (SYS-02) | SaaS | Provider | Store Manager |
| Countertop P2PE terminals (2) and mobile reader (1) (SYS-03) | Payment devices | Checkout lanes; store phone | Store Manager |
| POS tablets (2) | Endpoint (provider app in locked mode) | Checkout lanes | Store Manager |
| Office PC and Owner laptop | Endpoint | Back office; laptop travels with the Owner | Store Manager (MSP operates) |
| Store phone | Endpoint (unmanaged) | Back office and delivery vehicle | Store Manager |
| Firewall with Wi-Fi (SYS-06) | Network | Back office | Store Manager (MSP operates) |
| AI offers and markdown feature (SYS-10) | SaaS feature | Provider | Owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 44 controls:
- Implemented: 10
- Partially implemented: 22
- Planned: 12
- Not applicable: 0

By responsibility: 22 system-specific (the store), 21 hybrid (the store with the provider, a SaaS vendor, or the MSP), 1 common/inherited (fully provided by SaaS vendors).

### 10.2 Inherited and MSP-provided controls
| Provider | What the store relies on | Evidence | What the store must still do |
|---|---|---|---|
| Payment and commerce platform provider | P2PE encryption and key management; card processing; platform security; checkout card fields; backups (CP-9); lockout (AC-7); activity logging (AU-2); role enforcement (AC-3) | Service provider AOC (2026) and SOC 2 Type 2 report, reviewed 2026-08-25 (P09) | Follow the P2PE Instruction Manual; inspect terminals; manage users and MFA; control the scripts the store adds to its pages; review the activity log |
| Productivity suite vendor | Platform security, encryption, lockout, sign-in logging | Vendor documentation | Account management, MFA, sharing settings |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), office PC backup (CP-9), screen lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: review reports monthly, approve exceptions, yearly MSP review |

**Inherited does not mean done.** The provider's AOC states that the merchant is responsible for scripts and code it adds to its own pages. That is exactly where the store's largest gap sits (CM-7, SI-7; P01 R-001).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Office users sign in to the platform dashboard and the productivity suite with a password, and MFA through an authenticator app is being turned on for every administrator by 2026-10-15 (POAM-005). Cashiers use personal 4-digit POS codes on locked POS tablets; these codes allow sales and loyalty lookups only, and each cashier will have their own code by 2026-09-30. Customers sign in to the online store under the provider's identity rules, which are outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and provider report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **EBT:** electronic benefit transfer (SNAP)
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **P2PE:** point-to-point encryption (a PCI SSC validated solution)
- **POA&M:** plan of action and milestones
- **SAQ:** self-assessment questionnaire (PCI DSS)
- **SCP:** Store Commerce Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Store Manager (Security and PCI Lead) |

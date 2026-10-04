# System Security Plan: E-commerce and Point-of-Sale Platform (EPP)

**Organization:** Cris Santos Company, Inc. (PE-backed regional grocery retailer: 5 supermarkets, online ordering, a distribution center) | **Tier:** Mid-Market | **Vertical:** Retail Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
E-commerce and Point-of-Sale Platform (**EPP**), identifier CSC-EPP-01. The EPP is the company's major system. It comprises SYS-01 to SYS-04 and SYS-06 to SYS-09 in `../00_company-facts.md`.

## 2. System Overview
The EPP supports every selling and payment process in the BIA (P05): in-store checkout and SNAP EBT at 5 stores, online ordering through the website and app, picking, pickup and delivery, loyalty and digital offers, catering payments, and the supplier offers service. It serves about 2.1 million card transactions a year, about 148,000 loyalty members, and about 52,000 online accounts. The ERP and WMS (SYS-05) and the store operational technology (SYS-10) connect to it but are separate systems with their own owners.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | E-commerce platform: website, app back end, customer accounts, order management. Checkout pages host the processor's payment fields | Vendor SaaS; vendor SOC 2 Type 2 and PCI DSS service provider AOC |
| SYS-02 | Payment processor services: in-store encryption service, hosted payment fields and mobile SDK, tokenization, virtual terminal, merchant portal | Service provider (TPSP) with a PCI DSS AOC |
| SYS-03 | Store POS system: 65 registers, 65 PIN pads, 5 store POS servers, and the POS head-office application | On premises at stores; head-office application in the company's workloads account, managed by the POS vendor |
| SYS-04 | Cloud landing zone: identity and security, shared services, workloads, and backup accounts; loyalty and CDP database, loyalty API, integration platform, POS head-office application, data warehouse, supplier reporting portal, file services | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-06 | Identity provider with single sign-on, MFA, and conditional access | SaaS |
| SYS-07 | Site networks at 6 sites (Stores 1 to 5 and the DC campus) on SD-WAN | On premises; managed SD-WAN service |
| SYS-08 | About 465 endpoints: 210 PCs and laptops (including 5 service-desk PCs), 220 handhelds, 35 tablets | Company-managed |
| SYS-09 | SIEM operated by the MSSP | SaaS |

**Card data in the EPP.** In the stores, card data is encrypted at the PIN pad by the processor's encryption service, which is not a PCI-listed P2PE solution. The acquirer and QSA therefore treat the registers, store POS servers, store POS VLANs, and the POS head-office application as the cardholder data environment (CDE). Online, the e-commerce platform receives only tokens, but the checkout pages that host the payment fields are in scope for PCI DSS v4.0.1 Requirements 6.4.3 and 11.6.1. The service-desk PCs that run the virtual terminal are in scope as well.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the EPP |
|---|---|---|---|
| N44-45-R01 | PCI DSS v4.0.1 (contractual standard, not law) | PCI SSC, June 2024; merchant agreement; acquirer letter 2026-05-15 (SAQ D with a QSA, quarterly ASV scans) | Primary control requirement for the CDE and checkout pages; mapped in `control-implementation.csv` and analyzed in P03 |
| N44-45-R02 | FTC Act Section 5 | 15 U.S.C. 45(a), (n) | Reasonable security for customer and loyalty data; privacy and pricing claims must be truthful (P03, P10) |
| N44-45-R05 | FACTA receipt truncation | 15 U.S.C. 1681c(g) | Register receipts and any manual receipts during outages |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Reasonable measures to protect personal information (501.171(2)), disposal (501.171(8)), and breach notice (P08) |
| Federal program | SNAP retailer authorization | 7 CFR 278.1, 278.2 | EBT acceptance at all 5 stores; no cybersecurity control requirements identified in Part 278 |
| Contract | Supplier offers agreements | Contract (fictional) | SOC 2 Type 2 report on the supplier offers service by 2027-12-31 (P09) |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable:
- **FTC Safeguards Rule (N44-45-R03) and Red Flags Rule (N44-45-R04):** the company issues no store credit, offers no deferred payment, and does not cash checks.
- **CCPA (N44-45-R06):** the company does not do business in California.
- **COPPA (N44-45-R07):** the website and app are not directed to children, and loyalty members must be 18 or older.
- **INFORM Consumers Act (N44-45-R08):** the company does not operate an online marketplace.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the EPP accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the POA&M items that the QSA must see closed before the 2026 SAQ D (POAM-002 vendor access, POAM-005 CDE logging, POAM-013 payment page scripts, POAM-019 catering card data) must meet their milestones before QSA fieldwork on 2026-10-19; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (for example a P2PE migration or a store acquisition).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Migration of in-store card acceptance to a PCI-listed validated P2PE solution at the 2027 terminal refresh, which would take registers, store servers, and store POS networks out of the CDE (due 2027-09-30)
- Brokered, named access for the POS vendor and the refrigeration contractor (due 2026-12-31)
- Onboarding of registers, store POS servers, and the POS head-office application to the SIEM (due 2026-11-30)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the EPP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| PCI DSS attestation signer | Chief Financial Officer | Owns the merchant agreement; signs the AOC |
| Oversight | Board audit committee | Quarterly cyber risk and PCI DSS reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Information security officer | IT Director | Day-to-day control owner; PCI DSS program owner |
| Security operations and GRC | Security Manager and 2 security analysts | Vulnerability management, SIEM liaison, GRC, TPSP tracking |
| Business owners | Director of E-commerce and Marketing; Director of Store Operations | Checkout page and tag changes; store procedures and PIN pad inspections |
| Privacy | General Counsel; Privacy and Compliance Manager | Privacy notice, data sharing, breach determinations, vendor terms |
| Independent assessment | Co-sourced internal audit firm; QSA firm | Annual IT audit (P07); annual PCI DSS assessment |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring |

**Overlap and compensation.** The IT Director runs the controls and owns PCI DSS compliance, so the company relies on two independent checks: the co-sourced internal audit firm (P07) and a separate QSA firm. Neither firm designs or operates controls.

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment transactions (encrypted card data, tokens, truncated card numbers, EBT authorizations) | Moderate | Moderate | Moderate | Card compromise brings acquirer action, breach notice, and fraud losses, which are serious but not catastrophic for the company; checkout can run in offline mode for up to 24 hours (P05 BP-01 MTD 4 hours for a full stop) |
| Customer and loyalty records (contact details, purchase history, account credentials, app location for curbside arrival) | Moderate | Moderate | Low | Disclosure for up to 148,000 members harms customers and creates FTC and breach notice exposure; loyalty outages do not stop sales (P05 BP-09 MTD 24 hours) |
| Prices, promotions, and offers | Low | Moderate | Moderate | Wrong prices cause overcharges and FTC exposure; prices can run on the last good file for a day (P05 BP-05) |
| Supplier campaign and redemption data | Moderate | Moderate | Low | Supplier sales data is confidential; billing depends on accurate redemptions (P05 BP-10 MTD 72 hours) |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for incident investigations and PCI DSS Requirement 10 |
| **EPP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Confidentiality was considered for High.** A compromise of the store POS environment could expose about 1.95 million card transactions a year. The team kept confidentiality at Moderate because card data is encrypted at the PIN pad and the company holds no decryption keys, so a compromise would most likely involve malware on registers or the checkout page rather than bulk stored card data. To compensate, the plan adds CA-8 (penetration testing) by tailoring and treats the store CDE controls as priority items (section 10.1).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the company's e-commerce platform configuration, checkout theme code, installed apps, and scripts;
- the company's configuration of the processor's services (merchant portal users, virtual terminal users, hosted field settings);
- 65 registers, 65 PIN pads, and 5 store POS servers;
- all 4 cloud accounts and their workloads, including the POS head-office application;
- the identity provider tenant;
- site networks at 6 sites;
- about 465 endpoints;
- the company's SIEM tenant and its use cases.

**Outside the boundary (external services, interconnected):**
- the processor's and EBT processor's platforms;
- the e-commerce platform vendor's infrastructure;
- the cloud provider's infrastructure;
- the MSSP's platform;
- the ERP and WMS (SYS-05), the refrigeration and building systems (SYS-10), and the AI vendors (SYS-12);
- the marketing agency, the delivery marketplace, and the other vendors in SYS-11.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Payment processor (cards, store encryption service, hosted fields, tokens) | Bidirectional (TLS) | Encrypted card data, authorizations, tokens, settlement files | Merchant agreement; processor AOC |
| EBT processor | Bidirectional (TLS, through the processor's network) | EBT authorizations | Processor agreement |
| E-commerce platform vendor | Bidirectional (APIs over TLS) | Orders, customer accounts, prices | SaaS agreement; vendor AOC and SOC 2 |
| ERP and WMS (SYS-05) | Bidirectional through the integration platform | Price file, orders, inventory | SaaS agreements |
| Pricing and offers engine vendor (AI-001) | Outbound purchase history and prices; inbound prices and offers | Loyalty purchase history, ZIP code, delivery zone | SaaS agreement; **data use terms missing (gap, P10)** |
| Marketing agency | Outbound weekly member-level exports by email; agency publishes checkout tags | Names, emails, phone numbers, purchase history | **No security or data use terms (gap 6, gap 9)** |
| Consumer goods supplier (data pilot) | Outbound hashed member emails | Hashed emails, segment labels | **Pilot agreement only; privacy notice conflict (gap 9)** |
| Delivery marketplace | Inbound orders | Order details (no card data) | Marketplace terms; **no security schedule (gap 6)** |
| MSSP | Inbound logs; remote response actions | Security logs | Contract; SOC 2 Type 2 |
| POS vendor | Remote maintenance of store servers and the head-office application | System access to the CDE | Service contract; **3 shared support accounts (gap 3)** |
| Suppliers (about 140) | Outbound through the reporting portal | Campaign and redemption reports | Supplier offers agreements (SOC 2 required, P09) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| E-commerce tenant, checkout theme, apps, tag manager | SaaS | E-commerce platform vendor | Director of E-commerce and Marketing |
| Merchant portal and virtual terminal | SaaS | Payment processor | Chief Financial Officer |
| Registers (65) and PIN pads (65) | POS hardware | Stores 1 to 5 | Director of Store Operations |
| Store POS servers (5) | Server (offline mode) | Store server closets | IT Director |
| POS head-office application | Virtual machines and managed database | Workloads account (POS vendor managed) | IT Director |
| Loyalty and CDP database, loyalty API | Managed database and application service | Workloads account | Director of E-commerce and Marketing |
| Integration platform | Integration service and virtual machines | Workloads account | IT Director |
| Data warehouse and supplier reporting portal | Managed database and web application | Workloads account | Chief Financial Officer (warehouse); Director of E-commerce and Marketing (portal) |
| File services | Managed file service | Workloads account | IT Director |
| Backup vault | Backup service with write-once retention | Backup account (second region) | IT Director |
| Network hub, cloud firewall, access broker, log pipeline | Network and management services | Shared services account | IT Director |
| Cloud federation, guardrails, posture service | Identity and policy services | Identity and security account | Security Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| SD-WAN edges, store firewalls, switches, Wi-Fi | Network | Stores 1 to 5 and the DC campus | IT Director |
| PCs and laptops (210), handhelds (220), tablets (35) | Endpoint | All sites | IT Director |
| SIEM tenant | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The EPP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 121 controls** in `control-implementation.csv`: 116 from the Moderate baseline, 4 added by tailoring, and 1 from the privacy baseline. They cover every control the author mapping links to a PCI DSS requirement in scope (P03), the controls behind FTC reasonable-security expectations, and the controls that address the risks in P01.
- **Selected by tailoring (added):** CA-8 (penetration testing, from the High baseline) for PCI DSS 11.4 and the store CDE; PM-1, PM-2, and PM-9 for program governance and PCI DSS 12.1 and 12.4. **PT-5** (privacy notice, privacy baseline) is added because the privacy notice is an FTC deception issue (gap 9).
- **Inherited without separate statements:** the remaining physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17) and platform-level SA and SC controls, inherited from the cloud provider, the e-commerce platform vendor, the identity vendor, the processor, and the MSSP. They are evidenced by SOC 2 reports and PCI DSS AOCs reviewed each year (P09 `vendor-assurance-review.csv`).
- **Deferred:** the other Moderate controls with no PCI DSS mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing for vendor products, and SA-15). The supplier reporting portal is the one company-built application; its secure development controls are tracked in P01 R-032.

**Status of the 121 documented controls:**
| Status | Count |
|---|---|
| Implemented | 50 |
| Partially implemented | 69 |
| Planned | 2 |
| Not applicable | 0 |

**Inheritance of the 121 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 77 | Company |
| Hybrid | 29 | Identity vendor, e-commerce platform vendor, cloud provider, processor, MSSP, POS vendor, SD-WAN provider |
| Common/Inherited | 15 | Identity vendor (for example AC-7, IA-2(1)), cloud provider (CP-6, SC-12), e-commerce platform vendor (AC-12, SC-5), MSSP (IR-7) |

The Partially implemented statements trace to the 12 known gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 36 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee. The QSA firm's PCI DSS assessment follows in October and November 2026.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users of cloud and SaaS services authenticate through the identity provider with a password and push MFA with number matching, under conditional access. This meets the company's authenticator standard for general users and PCI DSS 8.4 for access into the CDE from the corporate network once vendor and agency accounts move to it (POAM-002).
- **Store staff at registers.** Cashiers sign in to registers with an employee number and a 4-digit PIN. This is accepted only because registers sit on the isolated POS VLAN, sessions end after 15 minutes idle, and no administrative function is available to cashiers. Administrative access to registers and store servers must use MFA through the access broker (POL-02 4.7).
- **Administrators.** Administrators will move to phishing-resistant authenticators (FIDO2 security keys) by 2027-03-31 (P01 R-009).
- **Customers.** Customers use the e-commerce platform's accounts with bot protection and optional MFA. P01 R-022 tracks credential stuffing against customer accounts.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor assurance reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **ASV:** Approved Scanning Vendor
- **CDE:** cardholder data environment
- **CDP:** customer data platform
- **DC:** distribution center
- **EBT:** electronic benefits transfer (SNAP)
- **EDR:** endpoint detection and response
- **EPP:** E-commerce and Point-of-Sale Platform
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **P2PE:** point-to-point encryption (a PCI SSC validation program)
- **POA&M:** plan of action and milestones
- **QSA:** Qualified Security Assessor
- **SAQ:** self-assessment questionnaire
- **TPSP:** third-party service provider
- **WMS:** warehouse management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Security Manager |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | IT Director |

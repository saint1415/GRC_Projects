# System Security Plan (short form): Store Sales Platform

**Organization:** Cris Santos Company (corner grocery with online and phone ordering) | **Tier:** Sole Proprietorship | **Vertical:** Retail Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Store Sales Platform (**SSP-1**), identifier CSC-SYS-001. It is the store's e-commerce and point-of-sale platform.

## 2. System Overview
The Store Sales Platform is everything the store uses to sell: the countertop card and EBT terminal, the POS app on the tablet, the online store, phone orders, and the owner's email, laptop, and phone that run them. One person, the owner, runs it, with an unpaid family member at the register about 8 hours a week. Components are SYS-01 to SYS-10 in `../00_company-facts.md` section 3. There is no server and no IaaS. Most technical safeguards are **inherited from the payment processor and the SaaS vendors**. The owner is responsible for accounts and passwords, the store network, devices, paper, and vendor choices (P04).

**Card data in this system:** card data is read by the terminal and sent to the processor; online card data is entered only on the processor's hosted payment page after a redirect. The store keeps no electronic card data. Until 2026-08-11 it kept paper card data on the phone-order pad (SYS-10).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N44-45-R01 | PCI DSS v4.0.1 (contractual, through the merchant agreement) | PCI SSC, June 2024. SAQ B-IP (terminal) and SAQ A (online store) assigned by the processor's portal |
| N44-45-R02 | FTC Act Section 5 | 15 U.S.C. 45(a), 45(n) |
| N44-45-R05 | FACTA receipt truncation | 15 U.S.C. 1681c(g) |
| State | Data security, breach notice, disposal of customer records | Fla. Stat. 501.171(2), (3)-(6), (8) |
| Program rule | SNAP retailer authorization and equal treatment | 7 CFR 278.1; 278.2(b) |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: FTC Safeguards Rule and Red Flags Rule (N44-45-R03, R04; no store credit), CCPA (N44-45-R06), COPPA (N44-45-R07), INFORM Consumers Act (N44-45-R08). See P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-09-04.
### 4.2 System Authorization Decision
No formal authorization applies to a private store. Equivalent decision: the owner accepted continued operation on 2026-09-04, on condition that the High risks in P01 (R-001, R-002, R-004) are treated by their due dates and both SAQs are completed by 2026-11-30.
### 4.3 System Operational Status
Operational. Planned changes: guest Wi-Fi for customers (2026-09-30); separate network for the terminal (2026-12-31); business email account (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security and privacy lead, PCI DSS contact, risk acceptor | Owner | Every role (designated in POL-01) |
| Register helper | Family member (unpaid) | Rings sales; inspects the terminal at opening on Saturdays; no administrator access |
| Technical support | Outside IT helper | Router and laptop help on request; no standing access |
| Service providers | Payment processor; website builder, POS app, and accounting vendors; ISP | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Customer payment data (card data in the terminal, on the hosted page, and formerly on paper) | Moderate | Moderate | Moderate | Disclosure means card fraud and breach duties; tampering redirects payments; loss of the terminal stops most sales (P05 MTD 24 h) |
| Customer account and order data (online accounts, delivery addresses, order history) | Moderate | Low | Low | Personal information with an email and password is covered by Fla. Stat. 501.171; orders can wait (P05 MTD 72 h) |
| Business financial data | Low | Moderate | Low | Errors affect tax filings; deadlines are in weeks (P05 MTD 168 h) |
| **Category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 27 controls that carry the PCI DSS and reasonable-security safeguards for a one-person store (`control-implementation.csv`). Other Moderate controls are inherited from the processor and SaaS vendors (evidence: the processor's PCI DSS attestation and the website builder's SOC 2 report, P09) or tailored out because they assume staff, servers, or software development. AC-5, AU-9, CM-3, and CA-2(1) assume a second person but are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in the online store, merchant portal, POS app, email, and accounting SaaS; the terminal on the counter; the tablet, laptop, and phone; the router and store network; the cameras; the AI chatbot account; and the phone-order pad.
- **Outside (external services):** the processor's platform and hosted payment page, the website builder's platform, the POS app platform, the ISP network, the distributor's portal, and the AI chatbot vendor's service.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Payment processor | Card and EBT authorizations; online payments after redirect; deposits | Merchant agreement (PCI DSS clause; 24-hour compromise notice term) |
| Website builder vendor | Customer accounts and orders | Online terms of service |
| POS app vendor | Items, prices, sales totals | Online terms of service |
| Wholesale distributor | Purchase orders, invoices | Customer account terms |
| Tax preparer | Read-only books | Engagement letter |
| AI chatbot vendor | Customer names, emails, order histories (May to August 2026) | **Consumer terms only; training on chats was on (gap, P10)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Online store (SYS-01) | SaaS | Owner |
| Countertop terminal, hosted payment page, merchant portal (SYS-02) | Service provider; terminal on the counter | Processor (terminal is leased) |
| POS app and tablet (SYS-03) | SaaS and endpoint | Owner |
| Email and files (SYS-04) | Consumer SaaS | Owner |
| Laptop and phone (SYS-05) | Personal endpoints | Owner |
| Router and Wi-Fi (SYS-06) | Network device | ISP (leased) |
| Accounting SaaS (SYS-07) | SaaS | Owner |
| Cameras (SYS-08) | Consumer cloud service | Owner |
| AI chatbot (SYS-09) | Consumer app | Owner |
| Phone-order pad (SYS-10) | Paper | Owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 27 controls:
- Implemented: 6
- Partially implemented: 16
- Planned: 5

Inheritance: 2 fully inherited (SC-8, encryption in transit by the processor and vendors; AU-9, logs kept by the processor and vendors), 9 hybrid (a provider operates the mechanism and the owner configures or uses it), and 16 the owner's alone (AC-5, AC-11, AC-18, AT-2, AU-6, CA-2(1), CM-3, CM-8, CP-2, IA-5, IR-8, MP-4, MP-6, PE-3, RA-3, SA-9).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor list and annual AOC check (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); inventory with the terminal serial number (CM-8) |
| Protect | MFA on store admin and email (IA-2(1), gap); unique passwords and no defaults (IA-5); separate networks (SC-7, AC-18); no paper card data (MP-4, MP-6) |
| Detect | Monthly check of store, email, and refund activity (AU-6, planned); terminal inspection (POL-01 7.8) |
| Respond | Card data compromise runbook (IR-8) |
| Recover | Vendor backups (CP-9); backup terminal and cash-only procedure (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-08-10 to 2026-08-14 with the outside IT helper; tests on 2026-08-13. See P07.

## 11. Digital Identity Acceptance Statement
The merchant portal requires a password and a second factor on the owner's phone, which fits administrator access to payment functions at a Moderate categorization. The online store administrator account and the email account that can reset it use a password only until MFA is turned on (2026-09-15). Online customers sign in to the website builder's customer accounts with the vendor's identity controls, outside this boundary; they never enter card data in the online store.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **EBT:** electronic benefit transfer (SNAP)
- **MFA:** multi-factor authentication
- **PTS:** PCI PIN Transaction Security (device approval program)
- **SAQ:** self-assessment questionnaire (PCI DSS)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial short-form plan | Owner |

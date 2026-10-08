# System Security Plan (short form): Reseller Order Desk

**Organization:** Cris Santos Company (IT hardware reseller) | **Tier:** Sole Proprietorship | **Vertical:** Wholesale Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Reseller Order Desk (**ROD**), identifier CSC-SYS-001.

## 2. System Overview
The ROD is everything the business uses to quote, buy, stage, deliver, and bill network equipment for about 48 commercial customers and one DoD prime contractor. One person, the owner, uses and runs it. Components are SYS-01 to SYS-10 in `../00_company-facts.md` section 3: the accounting and inventory SaaS (the order management system), the email and file suite, distributor and OEM portals, the marketplace buyer account, a laptop, a phone, the home network, the garage staging bench and stock cabinet, the bank, and a consumer AI assistant. There is no server and no IaaS. Most technical safeguards are **inherited from the SaaS vendors**; the owner is responsible for identities, data locations, devices, the home network, the garage, and supplier choices (P04).

**CMMC Level 1 assessment scope.** The FCI stream (asset tag lists, serial-to-tag spreadsheets, building delivery schedules) touches SYS-01, SYS-02, SYS-03, SYS-05, SYS-06, SYS-07, and SYS-08. Under 32 CFR 170.19(b)(1) these are in scope for the Level 1 self-assessment. SYS-10 is in scope only until FCI is removed from it (P10). SYS-04 and SYS-09 hold no FCI and are out of scope (170.19(b)(2)(i)).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N42-R04 | FAR Basic Safeguarding of Covered Contractor Information Systems | 48 CFR 52.204-21 (in the prime's BPA) |
| N42-R02 | CMMC Program, Level 1 (Self) | 32 CFR 170.15, 170.19(b), 170.22; DFARS 252.204-7021 (prime's new task order) |
| N42-R05 | Section 889 prohibition and reporting | 48 CFR 52.204-25(b)(1), (d), (e) |
| Clause | Kaspersky prohibition and reporting | 48 CFR 52.204-23 (in the BPA) |
| N42-R01 | FTC Act Section 5 (reasonable security; truthful claims such as "new and genuine") | 15 U.S.C. 45(a) |
| State | Reasonable security and breach notification | Fla. Stat. 501.171(2) and (3)-(6) |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: DFARS 252.204-7012 and NIST SP 800-171 (N42-R03; no CUI and no clause), SEC rules (N42-R07), CCPA/CPRA (N42-R08), and CTPAT (N42-R06; voluntary, not an importer). See P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-004) are treated by their due dates and that all 15 FAR 52.204-21 requirements are met before the owner affirms CMMC Level 1 compliance in SPRS.
### 4.3 System Operational Status
Operational. Planned changes: business-only Wi-Fi network and password manager (2026-10-15); laptop and file backup (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, risk acceptor, CMMC Affirming Official | Owner | Every role (POL-01 section 3) |
| Technical support | On-call IT consultant (confidentiality agreement 2026-07-30) | Laptop and network help on request; no standing access |
| Bookkeeper | Contract bookkeeper | Read-only accountant user in SYS-01 |
| Service providers | Accounting SaaS vendor, email provider, distributors, bank | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Inventory control and goods acquisition (orders, stock, serial numbers, supplier choices) | Low | Moderate | Low | Altered orders or substituted stock can put counterfeit equipment in customer networks (P01 R-001); MTD 48 hours (P05) |
| Federal contract information (asset tag lists, delivery schedules) | Moderate | Moderate | Low | Not for public release; wrong tags or serials break the prime's records; MTD 72 hours |
| Financial management (invoices, payments, bank details) | Moderate | Moderate | Low | Payment redirection already cost $2,340 (P01 R-002); MTD 120 hours |
| **ROD category (high-water mark)** | **Moderate** | **Moderate** | **Low** | |

**Baseline:** SP 800-53B Moderate, tailored to 26 controls that carry the 15 FAR 52.204-21 requirements, the supply chain duties, and the top risks for a one-person business (`control-implementation.csv`). Other controls are inherited from the SaaS vendors (evidence: the accounting SaaS vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal system. AC-5, AU-9, CM-3, and CA-2(1) assume a second person but are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in SYS-01, SYS-02, SYS-03, and SYS-10; the laptop and phone; the home router and Wi-Fi as used for business; the garage staging bench and stock cabinet; and paper tag sheets.
- **Outside (external services):** the SaaS vendors' platforms, distributors, the marketplace and brokers, parcel carriers, the bank, the invoicing payment page provider, and the prime's systems.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Prime contractor | Purchase orders, asset tag lists, serial-to-tag spreadsheets, delivery schedules (FCI) | BPA with FAR 52.204-21, -23, -25; DFARS 252.204-7021 for the new task order |
| Distributors A and B | Orders, drop-ship addresses, pricing | Reseller agreements |
| Marketplace and brokers | Purchase orders, payment details | Marketplace terms; broker invoices (no written terms) |
| Accounting SaaS vendor | All order and financial records | Subscription terms; SOC 2 report |
| Bookkeeper | Read-only financial records | Engagement letter |
| Consumer AI assistant | Sales history, including DoD order lines (FCI) | **Consumer terms only; training on (gap, P10)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Accounting and inventory SaaS tenant (SYS-01) | SaaS | Owner |
| Email and file storage (SYS-02) | SaaS | Owner |
| Distributor and OEM portal accounts (SYS-03) | SaaS | Owner |
| Marketplace buyer account (SYS-04) | SaaS | Owner |
| Laptop (SYS-05); 2 old laptops awaiting wipe | Endpoints | Owner |
| Phone (SYS-06) | Personal endpoint | Owner |
| Home router and Wi-Fi (SYS-07) | Network (ISP-provided) | Owner; ISP supplies the device |
| Staging bench, test switch, label printer, stock cabinet (SYS-08) | Premises and equipment | Owner |
| Bank and card accounts (SYS-09) | SaaS | Owner |
| Consumer AI assistant (SYS-10) | SaaS | Owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 26 controls:
- Implemented: 7
- Partially implemented: 15
- Planned: 4

Inheritance: 2 fully inherited from the SaaS vendors (AC-3, AU-9), 11 hybrid (the vendor provides the mechanism, the owner configures or uses it correctly), and 13 the owner's alone (AC-5, AC-20, AC-22, AT-2, CA-2(1), IR-8, MP-6, PE-3, RA-3, SA-9, SR-3, SR-5, SR-11).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; supply chain rules (SR-3, SR-5); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); CMMC Level 1 scope (section 2) |
| Protect | MFA (IA-2(1), IA-2(2), gaps); disk encryption (SC-28); home network (SC-7, gap); garage and cabinet (PE-3) |
| Detect | Antivirus (SI-3); OEM serial checks on receipt (SR-11, planned) |
| Respond | Counterfeit and tampered product runbook (IR-8) |
| Recover | SaaS vendor backups (CP-9, inherited); laptop and file backup (planned) |

### 10.2 Control assessment status
Self-assessed 2026-08-03 to 2026-08-07 with the IT consultant (tests on 2026-08-06). See P07.

## 11. Digital Identity Acceptance Statement
The bank and distributor portal A require a password and a second factor. Email uses SMS codes, accepted only until the owner moves to an authenticator app (2026-09-15). The SYS-01 administrator account and distributor portal B use a password only; MFA for SYS-01 is turned on by 2026-09-15, and portal B is used only for price checks until it offers MFA. FAR 52.204-21(b)(1)(vi) requires authentication but not MFA; the owner adds MFA because account takeover is a top risk (P01 R-003, R-005).

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **BPA:** blanket purchase agreement
- **CAGE:** Commercial and Government Entity code
- **CMMC:** Cybersecurity Maturity Model Certification
- **FCI:** Federal Contract Information (FAR 52.204-21(a))
- **MFA:** multi-factor authentication
- **ROD:** Reseller Order Desk
- **SPRS:** Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner |

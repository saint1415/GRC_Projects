# System Security Plan (short form): Brokerage Core SaaS Stack

**Organization:** Cris Santos Company (specialty chemical distributor, broker) | **Tier:** Sole Proprietorship | **Vertical:** Chemical
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-10-05

## 1. System Name and Identifier
Brokerage Core SaaS Stack (**BCSS**), identifier CSC-SYS-001.

## 2. System Overview
The BCSS is everything the business uses to sell and ship chemicals it never touches: quotes and orders, customer and ship-to verification, bills of lading (BOLs) with hazmat descriptions, pickup authorizations to suppliers, carrier bookings, emergency response information, invoices, and supplier payments. One person, the owner, uses and runs it. Components are SYS-01 to SYS-08 in `../00_company-facts.md` section 3: an email and file suite, an accounting SaaS, the bank portal, about 9 supplier, carrier, and ERI provider portals, a laptop, a phone, the home network, and a generative AI assistant. There is no server and no IaaS. Most technical safeguards are **inherited from the SaaS vendors**. The owner is responsible for identities, data handling, devices, the home network, and vendor terms (P04).

**Why this system matters for chemical security.** A forged email from this stack can release a cargo tank of 50% hydrogen peroxide, an explosives precursor, to the wrong truck. In this business the "critical business system" that CFATS RBPS 8 talks about is the email account.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| DOT HMR (binding) | Hazmat transportation security plan; training; shipping papers; emergency response information; registration | 49 CFR 172.800-172.804; 172.702-172.704; 172.201; 172.204; 172.602; 172.604; 107.601-107.620 |
| C-CHEMICAL-R01 | CFATS risk-based performance standards (voluntary benchmark; authority lapsed; the business is not a chemical facility) | 6 CFR 27.230(a)(5), (a)(6), (a)(8), (a)(15)-(16) |
| C-CHEMICAL-R03 | CIRCIA (proposed, not in force). Tracked only | Proposed 6 CFR Part 226 |
| State | Data security, breach notice, disposal (driver identity data) | Fla. Stat. 501.171(2)-(6), (8) |
| Internal | Information Security Policy; Hazmat Transportation Security Plan | POL-01 and HSP-01 (P06) |

Not applicable: C-CHEMICAL-R02 (USCG MTSA rule; no MTSA facility), EPA RMP and OSHA PSM (no stationary source or process).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-10-05.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner accepted continued operation on 2026-10-05 on two conditions: no bulk hydrogen peroxide load is released until HSP-01 call-back verification is in use (in force from 2026-10-05), and the Very High and High risks in P01 (R-001, R-002, R-004) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: email MFA and password manager (2026-10-15); email and file backup (2026-11-30); new router and work network (2026-11-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security officer, risk acceptor, incident commander | Owner | Every role. Also the senior management official for HSP-01 (172.802(b)(1)) |
| Technical support | On-call IT technician | Laptop and router help on request; no standing access |
| Service providers | Email suite provider, accounting SaaS vendor, bank, portal vendors, ERI provider, AI assistant vendor | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Shipment release and hazmat shipping data (pickup authorizations, BOLs, ERI data) | Moderate | **Moderate** | Moderate | A forged or wrong record can release hazmat to the wrong party or mislead responders. Integrity is the main concern; outages beyond a day stop shipments (P05 MTD 24 h). Rated Moderate rather than High because suppliers check the driver at the dock and the ERI provider holds its own copy of emergency data |
| Financial transactions (invoices, payments, bank details) | Moderate | Moderate | Low | A changed bank detail can redirect a payment; suppliers allow 30-day terms (P05 MTD 120 h) |
| Personal identity data (driver names and license numbers) | Moderate | Low | Low | Breach notice duties under Fla. Stat. 501.171 |
| **BCSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 29 controls that carry the HMR, CFATS benchmark, and Florida duties for a one-person brokerage (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors (evidence: the email suite provider's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in each SaaS service and portal, the bank portal user, the laptop, the phone, the home network as used for work, the AI assistant account, and paper in the home office.
- **Outside (external services):** the SaaS platforms themselves, the bank, the ERI provider's call center, the suppliers' plants and shipping offices, the carriers and their drivers, and the AI vendor's models.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Suppliers' shipping offices | Purchase orders, BOLs, pickup authorizations (carrier, driver, truck, pickup number) | Distribution agreements; producers' product stewardship terms |
| Carriers | Load bookings, BOLs, tracking links, driver details | Carrier rate confirmations |
| ERI provider | Product list and SDS; caller details during an emergency | ERI service contract (172.604(b)(2)) |
| Customers | Quotes, invoices, end-use statements, delivery details | Customer terms; one customer's supplier security questionnaire (P09) |
| Bank and accounting SaaS | Payments and bank details | Bank and SaaS terms |
| AI assistant vendor | Prompts with customer, price, and SDS text | Click-through terms; model-improvement setting off since 2026-09-18 (P10) |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Email, calendar, and file suite (SYS-01) | SaaS | Owner |
| Accounting and invoicing SaaS (SYS-02) | SaaS | Owner |
| Bank portal (SYS-03) | Bank-hosted | Owner |
| Partner portals, about 9 (SYS-04) | SaaS | Owner |
| Laptop (SYS-05) | Endpoint | Owner |
| Mobile phone (SYS-06) | Endpoint | Owner |
| Home network and ISP router (SYS-07) | Network | Owner (ISP equipment) |
| Generative AI assistant (SYS-08) | SaaS | Owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 29 controls:
- Implemented: 6
- Partially implemented: 20
- Planned: 2
- Not applicable: 1 (PS-3, no employees)

Inheritance: 3 fully inherited from the SaaS providers (AU-2, AU-9, SI-8), 11 hybrid (the provider runs the mechanism and the owner configures or uses it), and 15 the owner's alone (AC-5, AC-6(2), AT-2, AT-3, AU-6, CA-2(1), CM-3, CP-2, IR-6, IR-8, MP-6, PS-3, RA-3, SA-9, SI-12).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01 and HSP-01; vendor terms (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); account list (AC-2) |
| Protect | MFA (IA-2(1), IA-2(2), gaps on email); HMR training (AT-3); disk encryption (SC-28) |
| Detect | Provider sign-in logs (AU-2, inherited); monthly review (AU-6, planned) |
| Respond | Email takeover and load diversion runbook (IR-8); notification matrix (IR-6) |
| Recover | Backups (CP-9, gap for email and files); supplier hold-release instruction (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-09-08 to 2026-09-11 with the on-call IT technician. See P07.

## 11. Digital Identity Acceptance Statement
Email is the account that can release a load, so it needs phishing-resistant or at least app-based MFA. Today it uses a password only; an authenticator app goes on by 2026-10-15, and a hardware security key is the target at the next review. The accounting SaaS enforces MFA. The bank uses text-message codes, which is weaker because of SIM-swap risk; the owner adds a carrier account PIN by 2026-10-31. Partner portals without MFA hold no payment authority and are protected by unique passwords.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01 and HSP-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **BCSS:** Brokerage Core SaaS Stack
- **BOL:** bill of lading (the shipping paper)
- **ERI provider:** emergency response information telephone service provider (49 CFR 172.604)
- **HMR:** Hazardous Materials Regulations, 49 CFR Parts 171-180
- **HSP-01:** the company's hazmat transportation security plan (49 CFR 172.800)
- **MFA:** multi-factor authentication
- **SDS:** safety data sheet

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-10-05 | Initial short-form plan | Owner |

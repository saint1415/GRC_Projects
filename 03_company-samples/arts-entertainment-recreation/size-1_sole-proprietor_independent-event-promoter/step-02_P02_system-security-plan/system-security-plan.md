# System Security Plan (short form): Ticketing and Venue Operations Platform

**Organization:** Cris Santos Company (independent event promoter with one leased room) | **Tier:** Sole Proprietorship | **Vertical:** Arts, Entertainment, and Recreation
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Ticketing and Venue Operations Platform (**TVOP**), identifier CSC-SYS-001.

## 2. System Overview
The TVOP is everything the owner uses to book, sell, market, and run about 60 public shows a year in the Room: the ticketing platform (SYS-01) with its integrated payment processor (SYS-02), the website (SYS-03), email and files (SYS-04), email marketing and social media (SYS-05), accounting (SYS-06), the laptop and phones (SYS-07), and the Room's Wi-Fi (SYS-08). Components are listed in `../00_company-facts.md` section 3. One person, the owner, runs it, with contractors who need limited access. There is no server and no IaaS. Card payments are entered only in the hosted checkout, so most card security is **inherited from the ticketing vendor and the processor**. The owner is responsible for identities, website content, data exports, devices, the Room's network, and vendor oversight (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N71-R04 | PCI DSS v4.0.1 (contractual, through the merchant agreement); validated with SAQ A | PCI SSC standard; P03 |
| N71-R05 | FTC Act Section 5; FTC Rule on Unfair or Deceptive Fees | 15 U.S.C. 45(a), 45(n); 16 CFR Part 464 |
| BOTS Act | Protects the owner as a ticket issuer (no compliance duty) | 15 U.S.C. 45c |
| ADA Title III | Accessible seating ticket rules on seated shows | 28 CFR 36.302(f) |
| State | Reasonable security, disposal, and breach notification | Fla. Stat. 501.171 |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: N71-R01 to R03 (no gaming), N71-R06 COPPA (general-audience site; buyers must be 18 or older).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a sole proprietorship. Equivalent decision: the owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-003) are treated by their due dates and that the 2026 SAQ A is signed only after the P03 eligibility actions are complete.
### 4.3 System Operational Status
Operational. Planned changes: payment links replace keyed phone orders (2026-09-01); MFA and named sub-users on SYS-01 and the website (2026-09-15); event pages cleared of non-essential scripts (2026-09-30); guest Wi-Fi network for crews (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security and privacy lead, PCI DSS contact, risk acceptor | Owner | Every role (POL-01 4.2) |
| Limited users | Marketing assistant; door contractor's staff | Event pages and posts; ticket scanning (named sub-users from 2026-09-15) |
| Technical support | On-call IT consultant (confidentiality agreement 2026-07-24) | Laptop, phone, and Wi-Fi help on request; no standing access |
| Service providers | Ticketing vendor, payment processor, website builder, productivity suite, email marketing, accounting SaaS | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Patron and order records (names, emails, phones, order history) | Moderate | Moderate | Moderate | Disclosure invites phishing of fans and FTC scrutiny; altered events or prices mislead buyers; an outage on show night stops doors (P05 MTD 2 h) |
| Payment flows (hosted checkout, payouts) | Moderate | Moderate | Moderate | A skimming script or payout change causes direct financial harm and card brand and breach duties; card data itself is held only by the vendors |
| Business records (contracts, settlements, books) | Low | Moderate | Low | Wrong payment instructions cause loss; deadlines are measured in days (P05 MTD 72 to 120 h) |
| **TVOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 28 controls that a one-person promoter can run and that carry the PCI DSS, FTC, and Florida duties (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors (evidence: AOCs and the ticketing vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or software development. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts, settings, users, and data in SYS-01 to SYS-06; the website's pages and scripts; the laptop, the owner's phone, and the two scanning phones; the Room's router and Wi-Fi.
- **Outside (external services):** the ticketing vendor's platform and checkout, the processor's payment fields and systems, the other SaaS platforms, the bar concessionaire's POS, the landlord's building network, and patrons' own devices.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Payment processor (through SYS-01) | Card payments, payouts, chargebacks | Merchant agreement (24-hour compromise notice term) |
| Email marketing service | Monthly patron export (name, email, ZIP) | Vendor terms; no export retention rule (gap) |
| Marketing assistant | Event pages, posts, exports | Verbal engagement; no confidentiality terms (gap) |
| Door and security contractor | Attendee list in the scanner app | Service agreement with no data terms (gap) |
| Outside bookkeeper | Books and settlement records | Engagement letter |
| Fans | Order emails; some sent card details by email or text | Website notice: never send card details (2026-08-31) |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Ticketing platform tenant (SYS-01) | SaaS | Owner |
| Processor merchant account and portal (SYS-02) | SaaS | Owner |
| Website (SYS-03) | SaaS | Owner |
| Email and files (SYS-04) | SaaS | Owner |
| Email marketing and social accounts (SYS-05) | SaaS | Owner |
| Accounting (SYS-06) | SaaS | Owner |
| Laptop, owner's phone, 2 scanning phones (SYS-07) | Endpoints | Owner |
| ISP router and Wi-Fi in the Room (SYS-08) | Network | Owner (internet line from the landlord) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 28 controls:
- Implemented: 10
- Partially implemented: 15
- Planned: 3

Inheritance: 3 fully inherited from the vendors (AC-3, AU-2, AU-9), 11 hybrid (the vendor provides the mechanism and the owner configures or uses it), and 14 the owner's alone (AC-11, AC-18, AT-2, AU-6, CA-2(1), CM-3, CP-2, IA-5, IR-8, PL-4, RA-3, SA-9, SC-7, SI-12).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor PCI DSS status and contractor terms (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05) |
| Protect | MFA (IA-2(1), gap on SYS-01 and the website); unique passwords (IA-5); named accounts (AC-2); approved scripts only (CM-7); export retention (SI-12) |
| Detect | SYS-01 activity log (AU-2, inherited); monthly review (AU-6, planned) |
| Respond | Account takeover and skimming runbook (IR-8) |
| Recover | Vendor backups (CP-9); offline door list and sealed recovery codes (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-27 to 2026-07-31 with the IT consultant. See P07.

## 11. Digital Identity Acceptance Statement
Email, the processor portal, and accounting require a password and an authenticator app on the owner's phone, which fits a Moderate categorization. The SYS-01 and website administrator logins use a password only until MFA is turned on (2026-09-15); until then they are the weakest point in the system (P01 R-001 and R-002). Patrons sign in to the vendor's ticketing accounts under the vendor's own identity controls, outside this boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **MFA:** multi-factor authentication
- **SAQ A:** PCI DSS self-assessment questionnaire for card-not-present merchants that fully outsource card data functions
- **TVOP:** Ticketing and Venue Operations Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner |

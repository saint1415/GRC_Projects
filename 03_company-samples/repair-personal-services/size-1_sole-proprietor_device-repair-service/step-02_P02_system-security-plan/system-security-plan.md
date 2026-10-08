# System Security Plan (short form): Service Ticketing and Point-of-Sale System

**Organization:** Cris Santos Company (electronics and device repair service) | **Tier:** Sole Proprietorship | **Vertical:** Other Services (except Public Administration)
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Service Ticketing and Point-of-Sale System (**STPS**), identifier CSC-STPS-001.

## 2. System Overview
The STPS is everything the shop uses to take in, repair, and return about 1,400 customer devices a year: the ticketing and POS platform (SYS-01, vendor SaaS), the P2PE card terminal and processor portal, the productivity suite, the accounting SaaS and bank portal, the owner laptop, the repair bench PC and transfer drives, the counter tablet, the owner phone, the shop Wi-Fi, two cloud security cameras, the website and booking form, and a consumer generative AI assistant (SYS-01 to SYS-12 in `../00_company-facts.md` section 3). One person, the owner-technician, uses and runs it; a fill-in technician uses it about 12 days a year. There is no server and no IaaS. Most application safeguards are **inherited from the SaaS vendors and the payment processor**; the owner is responsible for accounts, devices, the shop network, customer data on the bench, and vendor terms (P04).

What makes this system different from other small businesses: **it holds other people's devices and the keys to them.** Device passcodes, account passwords, and full copies of customers' phones pass through it every day.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N81-R01 | FTC Act Section 5 (unfair or deceptive practices) | 15 U.S.C. 45(a)(1) and 45(n) |
| N81-R02 | State breach notification laws; Florida as the worked example | Fla. Stat. 501.171 (2) security, (3)-(6) notice, (8) disposal; each state where affected customers reside |
| N81-R03 | PCI DSS v4.0.1 (contractual, through the merchant agreement) | PCI DSS v4.0.1 SAQ P2PE (October 2024) |
| N81-BM | Voluntary benchmark | NIST CSF 2.0; NIST SP 800-88 Rev. 2 for sanitization |
| Contract | Processor merchant agreement (fictional terms) | Annual SAQ P2PE; notice within 24 hours of a suspected card data compromise |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable at this size (P03 applicability screen): N81-R04 FTC Disposal Rule (no consumer reports are obtained), N81-R05 COPPA (no child-directed site), N81-R06 HIPAA (not a covered entity), the FTC Safeguards Rule (not a financial institution), and the Florida Digital Bill of Rights (revenue threshold).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-technician on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner-technician accepted continued operation on 2026-08-31, on condition that the two High risks in P01 (R-001 ticketing account takeover, R-002 customer data on the bench PC and drives) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: named fill-in account and MFA on SYS-01 (2026-09-15 to 2026-09-30); bench PC encryption and retention purge (2026-10-31); separate guest and bench Wi-Fi networks (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security and privacy lead, risk acceptor | Owner-technician | Every role; designated in writing in POL-01 4.2 |
| Occasional user | Fill-in technician (independent contractor) | Uses SYS-01 and the bench about 12 days a year. Agreement and named account planned |
| Assessment help | Independent security consultant | 8 hours in July 2026; no standing access |
| Service providers | Ticketing and POS vendor, payment processor, productivity suite provider, accounting SaaS, website builder | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Customer records and device access data (names, contacts, serials, passcodes, account passwords) | Moderate | Moderate | Low | Email-and-password pairs are personal information under Fla. Stat. 501.171(1)(g)1.b.; wrong custody records can release a device to the wrong person; a day without SYS-01 is workable on paper (P05) |
| Customer device content (transfer and recovery copies) | Moderate | Moderate | Moderate | Photos, messages, location history, and health data of named customers; a recovery copy may be the only copy (P05 BP-04 RPO 0) |
| Payment transactions | Low | Moderate | Moderate | Card data stays in the P2PE terminal; revenue depends on taking payment at release (P05 MTD 24 h) |
| **STPS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 28 controls that a one-person shop can run (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors and the processor (evidence: the ticketing vendor's SOC 2 report, P09, and the P2PE solution listing) or tailored out because they assume staff, servers, or software development. AC-5, AU-9, CM-3, and CA-2(1) assume a second person but are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's SYS-01 account and settings, the processor portal account, the productivity, accounting, bank, camera, website, and AI accounts, the laptop, bench PC, transfer drives, tablet, and phone, the shop router and Wi-Fi, the card terminal as a physical device, and paper intake forms and tags in the shop.
- **Outside (external services):** the SaaS platforms themselves, the P2PE solution (decryption and processing), the internet provider, parts suppliers, the recycler, and the fill-in technician's own devices.
- **Customer devices under repair** are not part of the system, but they connect to the bench PC and the shop Wi-Fi, so the boundary rules in P04 treat them as untrusted.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Direction | Data | Agreement |
|---|---|---|---|
| Ticketing and POS vendor | Both | Customer records, tickets, status texts | Vendor terms; SOC 2 report under NDA |
| Payment processor | Outbound (encrypted in the terminal) | Card transactions | Merchant agreement; P2PE solution |
| Fill-in technician | Both | Full SYS-01 access through the owner's login | **None (gap)** |
| Certified recycler | Outbound | Drop-off devices and scrap parts | Service contract **without data terms (gap)** |
| Generative AI assistant vendor | Outbound | Pasted ticket notes, logs, screen photos | **Consumer terms; training on (gap)** |
| Bookkeeper | Both | Invoices and payments | Engagement letter |
| Customers | Both | Status texts and emails, booking requests | Intake form and website privacy notice |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SYS-01 Ticketing and POS tenant | SaaS | Ticketing and POS vendor | Owner-technician |
| SYS-02 P2PE terminal and merchant portal | Payment device; provider portal | Shop counter; payment processor | Owner-technician |
| SYS-03 Productivity suite | SaaS (business plan) | Productivity suite provider | Owner-technician |
| SYS-04 Accounting SaaS and bank portal | SaaS | Providers | Owner-technician |
| SYS-05 Owner laptop | Endpoint | Shop and owner's home | Owner-technician |
| SYS-06 Bench PC and 2 transfer drives | Endpoint and removable media | Repair bench | Owner-technician |
| SYS-07 Counter tablet | Endpoint | Counter | Owner-technician |
| SYS-08 Owner phone | Mobile endpoint | Owner | Owner-technician |
| SYS-09 Router and Wi-Fi | Network | Shop (internet provider equipment) | Owner-technician |
| SYS-10 Cloud security cameras | IoT and SaaS | Shop; camera vendor cloud | Owner-technician |
| SYS-11 Website and booking form | SaaS | Website builder | Owner-technician |
| SYS-12 Generative AI assistant | SaaS (consumer plan) | AI vendor | Owner-technician |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 28 controls:
- Implemented: 7
- Partially implemented: 16
- Planned: 5

Inheritance: 3 fully inherited from the ticketing vendor (AC-3, AU-2, AU-9), 10 hybrid (a vendor operates the mechanism, the owner configures or uses it correctly), and 15 the owner's alone (AC-5, AC-11, AC-18, AT-2, AU-6, CA-2(1), CM-3, CP-2, IA-5, IR-6, IR-8, PE-3, RA-3, SA-9, SI-12).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor terms (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); retention rules (SI-12, planned) |
| Protect | MFA (IA-2(1), gap on SYS-01); bench PC encryption (SC-28, gap); P2PE (SC-8); sanitization (MP-6, gap); network separation (SC-7, gap) |
| Detect | SYS-01 activity logging (AU-2, inherited); monthly review (AU-6, planned) |
| Respond | Account takeover runbook (IR-8); incident reporting (IR-6) |
| Recover | Vendor backups (CP-9, inherited); device-return procedure (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-27 with the independent security consultant. See P07 (10 controls tested, 41 determination statements).

## 11. Digital Identity Acceptance Statement
Every account that can export customer records, change payment settings, or move money must use a unique account, a password manager passphrase, and MFA from the authenticator app on the owner's phone. Today that is true for the productivity suite, accounting SaaS, bank, and processor portal, but **not for SYS-01**, the account with the most customer data (MFA on by 2026-09-15). The fill-in technician will get a named SYS-01 account with MFA and no export rights. Customers do not sign in to anything; they receive status links that show one ticket only.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **MFA:** multi-factor authentication
- **P2PE:** point-to-point encryption (a PCI-listed solution that encrypts card data inside the terminal)
- **PIM:** P2PE Instruction Manual, the solution provider's instructions the merchant must follow
- **SAQ:** PCI DSS Self-Assessment Questionnaire
- **STPS:** Service Ticketing and Point-of-Sale System
- **Transfer drive:** an external drive used to hold customer data while it moves from one device to another

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-technician |

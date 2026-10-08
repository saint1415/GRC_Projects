# System Security Plan (short form): Shop Production and Cold-Chain Monitoring System

**Organization:** Cris Santos Company (custom-exempt meat processing shop) | **Tier:** Sole Proprietorship | **Vertical:** Food and Agriculture
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Shop Production and Cold-Chain Monitoring System (**SPCM**), identifier CSC-SYS-001.

## 2. System Overview
The SPCM is everything the shop uses to keep customers' carcasses and product cold, process them to each owner's cut sheet, cure and smoke them, label every package "Not for Sale", and keep the custom records the exemption requires. One person, the owner-operator, uses and runs it. Components are SYS-01 to SYS-10 in `../00_company-facts.md` section 3: a cold-chain monitoring service with five sensors and a gateway, a smokehouse controller with a cloud app, a shop laptop driving a scale and label printer, a consumer email and file account, the owner's phone, a booking form, accounting and payments, the shop Wi-Fi, and a public AI chatbot. There is no server, no processing-line network, and no IaaS. Most safeguards inside the services are **inherited from the vendors**; the owner is responsible for accounts, data, devices, the shop network, and vendor choices (P04).

Two components act on food, not just on data: the smokehouse controller runs cook programs, and the cold-chain service is the only real-time warning that a cooler is failing. That is why integrity and availability, not confidentiality, set the categorization in section 6.

## 3. Laws, Regulations, and Policies Affecting the System
| Requirement | Citation | How it touches the SPCM |
|---|---|---|
| FMIA custom exemption conditions | 9 CFR 303.1(a)(2)(i)-(iv), (b)(1)-(4) | Records, labels, ingredients, and product protection (rows below) |
| Custom records and transaction records | 9 CFR 303.1(b)(3); 320.1-320.3 | Custom records spreadsheet (SYS-05, SYS-03); kept 2 years after December 31 of the transaction year |
| FSIS access to records | 9 CFR 300.6(b)(2); 320.4 | Records must be producible at the shop during business hours |
| "Not for Sale" marking | 9 CFR 316.16; 317.16 | Label templates and printer (SYS-03, SYS-04) |
| Curing agents | 9 CFR 424.21(c) via 303.1(b)(1) | Cure sheet and chatbot calculations (SYS-03, SYS-10); locked cabinet |
| Product protection during storage | 9 CFR 416.4(d) via 303.1(a)(2)(i) | Cold-chain monitoring (SYS-01) |
| Florida data security, disposal, breach notice | Fla. Stat. 501.171(2)-(6), (8) | Custom records and booking data, treated as personal information (P03 open question) |
| Voluntary benchmark | NIST CSF 2.0 | P03 checklist |
| Internal | Information Security Policy POL-01 (P06) | All components |

Not applicable (P03 section 1): C-FOOD-AG-R01 (21 CFR Part 121; the shop is not required to register, 21 CFR 1.226(g)), C-FOOD-AG-R02 (CIRCIA, proposed only), C-FOOD-AG-R03 (USCG MTS rule), the Reportable Food Registry, and 9 CFR 417 and 418.2 (official establishments).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-operator on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private shop. Equivalent decision: the owner-operator accepted continued operation on 2026-08-31, on condition that the four High risks in P01 (R-001, R-002, R-003, R-010) are treated by their due dates, all before the 2026-10-15 busy season except the generator work.
### 4.3 System Operational Status
Operational. Planned changes: password manager and MFA (2026-09-15); business-grade file plan with version history and an encrypted backup drive (2026-10-15); guest and device networks on the router (2026-10-15).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, risk acceptor, incident lead | Owner-operator | Every role. Also the only person who answers cold-chain alerts |
| Technical support | On-call IT technician | Laptop, phone, and router help on request; no standing access |
| Refrigeration support | Refrigeration service contractor | Condensing units; no system access |
| Service providers | Cold-chain vendor, smokehouse manufacturer, booking form vendor, email and file provider, accounting vendor, card processor | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Production and process data (temperatures, alarm set points, cook programs, cure amounts) | Low | Moderate | Moderate | Disclosure harms no one; a changed set point, cook program, or cure amount can make product unsafe; loss of alerting beyond 4 hours risks the cooler (P05 MTD) |
| Customer and regulatory records (custom records, cut sheets, bookings) | Moderate | Moderate | Low | Names and addresses that may be personal information under Fla. Stat. 501.171; wrong records misdirect product or fail an FSIS review; a few days' outage is tolerable (P05 MTD 120 h) |
| **SPCM category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

Information types are named in plain terms; SP 800-60 has no food production type, so the ratings follow FIPS 199 definitions directly.

**Baseline:** SP 800-53B Moderate, tailored to 27 controls that a one-person shop can run (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS vendors (evidence: the cold-chain vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or software development. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in SYS-01, SYS-02, SYS-05, SYS-07, SYS-08, and SYS-10; the sensors, gateway, and smokehouse controller; the laptop, scale and label printer, and phone; the shop router and Wi-Fi; paper cut sheets and logs in the shop.
- **Outside (external services):** the vendors' platforms and their subservice providers, the mobile slaughter operator, the refrigeration contractor, the card processor, and the internet provider's network.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Mobile slaughter operator | Kill sheet photos by text (owner, species, carcass number, hot weight) | None (separate business; informal) |
| Cold-chain vendor | Temperature readings; alert contacts | Click-through terms; SOC 2 report reviewed |
| Smokehouse manufacturer | Cook programs; run status | Click-through app terms (**not read**) |
| Booking form vendor | Processing requests and cut sheets | Click-through terms |
| Card processor | Card payments (encrypted at the reader) | Merchant agreement |
| Tax preparer | Accounting exports by shared link | Engagement letter |
| Public AI chatbot vendor | Recipe and cure prompts; occasionally customer first names | Consumer terms that allow use of inputs to improve the service (**gap**, P10) |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Cold-chain sensors (5) and gateway; SYS-01 account | Connected devices; vendor SaaS | Owner-operator |
| Smokehouse controller; SYS-02 app account | Connected device; vendor cloud app | Owner-operator |
| Shop laptop (SYS-03) and scale and label printer (SYS-04) | Endpoint; peripheral | Owner-operator |
| Email and file account (SYS-05) | Consumer SaaS | Owner-operator |
| Phone (SYS-06) | Personal endpoint | Owner-operator |
| Booking form (SYS-07); accounting, banking, card reader (SYS-08) | SaaS; processor device | Owner-operator |
| Router and Wi-Fi (SYS-09) | Network device | Internet provider (device); owner (settings) |
| AI chatbot account (SYS-10) | Consumer SaaS | Owner-operator |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 27 controls:
- Implemented: 9
- Partially implemented: 14
- Planned: 4

Inheritance: 3 fully inherited from vendors (AC-3, AU-2, AU-9), 10 hybrid (the vendor provides the mechanism and the owner configures or uses it), and 14 the owner's alone (AC-6, AT-2, AU-6, CA-2(1), CM-3, CM-6, CP-2, IA-5, IR-6, IR-8, MP-6, PE-3, RA-3, SA-9).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor review (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05) |
| Protect | MFA (IA-2(1), gaps on SYS-01 and the booking form); unique passwords (IA-5, gap); device encryption (SC-28); defaults changed (CM-6) |
| Detect | Cold-chain alerts and vendor logs (AU-2, inherited); monthly log review (AU-6, planned); antivirus (SI-3) |
| Respond | Ransomware runbook with cold-chain steps (IR-8); notification matrix (IR-6) |
| Recover | Backups (CP-9, gap); manual temperature readings and printed cook programs (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-27 to 2026-07-31 with the on-call IT technician. See P07.

## 11. Digital Identity Acceptance Statement
Every SaaS account is an administrator account held by the owner, so each should require a second factor. Today email (text message) and accounting meet that. The cold-chain account and booking form admin use a password only until MFA is turned on (2026-09-15). The smokehouse app offers no MFA; compensating steps are a unique passphrase, remote program editing turned off, and a monthly check of the controller's program list. Customers do not sign in to any shop system.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **Custom exempt:** preparation of meat for the animal's owner under 9 CFR 303.1(a)(2), without inspection, marked "Not for Sale"
- **FSIS:** USDA Food Safety and Inspection Service
- **MFA:** multi-factor authentication
- **SPCM:** Shop Production and Cold-Chain Monitoring System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-operator |

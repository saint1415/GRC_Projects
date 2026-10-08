# System Security Plan (short form): Inn Business Systems Profile

**Organization:** Cris Santos Company (six-room bed-and-breakfast inn) | **Tier:** Sole Proprietorship | **Vertical:** Accommodation and Food Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Inn Business Systems Profile (**IBSP**), identifier CSC-SYS-001.

## 2. System Overview
The IBSP is everything the inn uses to sell rooms, take payments, let guests in, and keep the books for about 600 stays a year. One person, the owner-innkeeper, runs it; a relief innkeeper uses it on weekends. Components are SYS-01 to SYS-11 in `../00_company-facts.md` section 3: the innkeeping software (SaaS), the payment facilitator's services and mobile reader, two OTA portals, a consumer email and file account, an accounting SaaS, the website, the laptop, the phone, the inn's router, the smart door locks, and the innkeeping software's AI add-on. There is no server and no IaaS. Most technical safeguards are **inherited from the SaaS vendors**; the owner is responsible for accounts and passwords, card and guest data handling, the two devices, the router, and vendor choices (P04).

**Where card data flows today:** booking engine (vendor page; token only), OTA virtual cards (vendor vault; displayable), phone bookings (keyed on the laptop or written on a paper pad), card authorization forms (email), and card-present payments (P2PE reader). The first and last flows keep card data off the inn's systems; the other three put the laptop, the paper pad, and the email account in PCI DSS scope (P03).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N72-R01 | PCI DSS v4.0.1 (through the payment facilitator's sub-merchant agreement) | PCI SSC standard; contract, not law |
| N72-R02 | FTC Act Section 5; FTC Rule on Unfair or Deceptive Fees | 15 U.S.C. 45(a), (n); 16 CFR Part 464 |
| N72-R04 | Florida breach notice, reasonable security, and disposal; other states where guests live | Fla. Stat. 501.171; each state's statute |
| State | Guest register; emergency pricing | Fla. Stat. 509.101(2); Fla. Stat. 501.160 |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: FTC Disposal Rule (N72-R03; no consumer reports), Illinois BIPA (N72-R05; no Illinois operations and no biometrics), and CIRCIA (N72-R06; proposed only, and the inn is far below the SBA size standard).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-innkeeper on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-004) are treated by their due dates and that phone bookings stop being written on paper immediately.
### 4.3 System Operational Status
Operational. Planned changes: pay-by-link for phone bookings and a front desk role without card display (2026-10-31); separate guest Wi-Fi network (2026-09-30); move email and files to a business plan (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security and privacy lead, PCI contact, risk acceptor | Owner-innkeeper | Every role (POL-01 section 3) |
| Backup operator | Relief innkeeper (unpaid family member) | Check-ins and bookings on weekends; named account planned |
| Technical support | On-call IT consultant (confidentiality agreement since 2026-07-17) | Laptop, router, and lock help on request; no standing access |
| Service providers | Innkeeping software vendor, payment facilitator, OTAs, lock vendor | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Payment card data (card numbers, security codes on forms and the pad) | Moderate | Moderate | Low | Disclosure leads to fraud, card brand reporting, and breach notice; payments can wait 72 hours (P05 BP-03) |
| Guest records (identity, contact, stay history, ID photos, door codes) | Moderate | Moderate | Moderate | Names with ID numbers are personal information under Fla. Stat. 501.171(1)(g); wrong door codes or calendar data affect guest safety and bookings (P05 MTD 8 to 24 h) |
| Business administration (books, tax returns, contracts) | Low | Moderate | Low | Errors matter; deadlines are in days (P05 MTD 120 h) |
| **IBSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 28 controls that carry the PCI DSS and Florida duties for a one-person inn (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors (evidence: the innkeeping vendor's SOC 2 report and the AOCs, P09) or tailored out because they assume staff, servers, or software development. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in the innkeeping software, OTA portals, payment facilitator portal, email and files, accounting SaaS, website builder, and lock app; the laptop and phone; the mobile reader; the router; the door locks; paper records in the owner's office.
- **Outside (external services):** the vendors' platforms, the OTAs' systems, the card networks, and the internet service provider's network.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Payment facilitator | Card payments, payouts, chargebacks | Sub-merchant agreement; AOC on file |
| Innkeeping software vendor | Guest profiles, reservations, virtual cards, AI add-on data | Subscription terms; AOC and SOC 2 report on file |
| OTA-1 and OTA-2 | Reservations, guest messages, virtual cards | OTA partner terms |
| Smart lock vendor | Guest names, room assignments, codes | App terms. **Installer account found active (P07)** |
| Email and file provider | Guest correspondence, card forms, ID photos | Consumer terms. **Holds card data (gap)** |
| Bookkeeper | Payouts and books | Engagement letter |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Innkeeping software tenant (SYS-01) | SaaS | Owner-innkeeper |
| Payment facilitator account and mobile reader (SYS-02) | Service provider; P2PE device (serial number recorded 2026-07-23) | Owner-innkeeper |
| OTA-1 and OTA-2 portal accounts (SYS-03) | Third-party extranets | Owner-innkeeper |
| Email, files, and photo backup (SYS-04) | Consumer SaaS | Owner-innkeeper |
| Accounting SaaS (SYS-05) | SaaS | Owner-innkeeper |
| Website (SYS-06) | Website-builder SaaS | Owner-innkeeper |
| Laptop (SYS-07) | Endpoint | Owner-innkeeper |
| Mobile phone (SYS-08) | Personal endpoint | Owner-innkeeper |
| Router (SYS-09) | ISP-provided network device | Internet service provider; settings by the owner |
| Smart door locks, 7 keypads (SYS-10) | Cloud-managed devices | Owner-innkeeper |
| AI add-on (SYS-11) | SaaS feature | Owner-innkeeper |
| Paper reservation pad and binder | Paper records (to be destroyed) | Owner-innkeeper |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 28 controls:
- Implemented: 4
- Partially implemented: 21
- Planned: 3

Inheritance: 2 fully inherited from the vendors (AU-2, AU-9), 11 hybrid (a vendor operates the mechanism, the owner configures or uses it correctly), and 15 the owner's alone (AC-5, AC-11, AT-2, AU-6, CA-2(1), CM-3, CM-6, CM-8, CP-2, IA-5, IR-8, MP-6, RA-3, SA-9, SI-12).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor list and AOCs (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); component inventory (CM-8) |
| Protect | MFA (IA-2(1), gap); password manager (IA-5, gap); disk encryption (SC-28, gap); guest network separation (SC-7, gap); door codes (PE-3) |
| Detect | Innkeeping activity log (AU-2, inherited); monthly log review (AU-6, planned) |
| Respond | Reservation system compromise runbook (IR-8) |
| Recover | Innkeeping vendor backups (CP-9, inherited); relief innkeeper account and sealed recovery codes (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the IT consultant. See P07.

## 11. Digital Identity Acceptance Statement
The accounting SaaS and OTA-1 require a password and a second factor on the owner's phone. The innkeeping software, email, and OTA-2 use a password only until MFA is turned on (2026-09-15). For accounts that can display card numbers and send messages to guests, a password alone is not acceptable at a Moderate categorization. Guests use the booking engine and OTA sites under those vendors' identity controls, outside this boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **IBSP:** Inn Business Systems Profile
- **MFA:** multi-factor authentication
- **OTA:** online travel agency
- **P2PE:** point-to-point encryption (a PCI-listed solution that encrypts card data in the reader)
- **SAQ:** self-assessment questionnaire

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-innkeeper |

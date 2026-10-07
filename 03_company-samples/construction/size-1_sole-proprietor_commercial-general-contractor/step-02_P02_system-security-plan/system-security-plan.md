# System Security Plan (short form): Project Management and Payment Application System

**Organization:** Cris Santos Company (commercial and institutional building general contractor) | **Tier:** Sole Proprietorship | **Vertical:** Construction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Project Management and Payment Application System (**PMPAS**), identifier CSC-SYS-001.

## 2. System Overview
The PMPAS is everything the owner uses to run jobs and move money: drawings, RFIs, submittals, daily logs, pay apps, subcontractor invoices and lien waivers, payments, and the federal paperwork for FC-1. One person, the owner, uses and runs it. Components are SYS-01 to SYS-06 in `../00_company-facts.md` section 3: the project management and pay app SaaS, the accounting SaaS, the business email and file account, one laptop, one phone, and the home office network. The bank portal (SYS-07), the federal portals (SYS-08), and the AI bid assistant (SYS-09) are external services it connects to. There is no server and no IaaS. Most platform safeguards are **inherited from the SaaS vendors**; the owner is responsible for identities, data handling, devices, the home network, and vendor terms (P04).

The PMPAS is also the **proposed CMMC Level 1 assessment scope**: the systems that process, store, or transmit FCI (32 CFR 170.19(b)(1)). This plan is the scope document the owner will use for the Level 1 self-assessment.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N23-R01 | FAR 52.204-21 Basic Safeguarding of Covered Contractor Information Systems | 48 CFR 52.204-21 (NOV 2021). In FC-1 |
| N23-R02 | FAR 52.204-25 Section 889 prohibition | 48 CFR 52.204-25 (NOV 2021). In FC-1 |
| N23-R04 | CMMC Program (32 CFR Part 170) and DFARS 252.204-7021 | Level 1 (Self) required before award of the DoD subcontract (P03) |
| N23-R03 | DFARS 252.204-7012 | Not applicable: no DoD contract today and no covered defense information expected (P03 G-032) |
| Payment terms | FAR 52.232-27 and 52.232-33 | Pay subcontractors within 7 days of receipt; EFT to the SAM bank account |
| Payroll | FAR 52.222-8 | Weekly certified payrolls for FC-1 subcontractors |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 (W-9 forms with Social Security numbers; account credentials) |
| Internal | Information Security Policy | POL-01 (P06) |

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.
### 4.2 System Authorization Decision
No federal authorization applies to a contractor's own systems. Equivalent decision: the owner accepted continued operation on 2026-08-31, on the condition that the Very High and High risks in P01 (R-001, R-002, R-008, R-010) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: separate work network on the home router (2026-09-30); bookkeeper account in SYS-02 (2026-09-30); file sync with version history for the laptop work folder (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, risk acceptor, CMMC Affirming Official | Owner | Every role. Designated in writing in POL-01 |
| Technical support | On-call IT technician | Device and router help on request; no standing access |
| Bookkeeping | Outside bookkeeper | Monthly reconciliation in SYS-02 (separate account planned) |
| Service providers | Project management, accounting, email, bank, and AI vendors | Operate inherited controls |

Because one person designs, runs, and checks every control, independence is limited. POL-01 4.5 adds an outside check.

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Facilities, fleet, and equipment management (drawings, submittals, daily logs; FCI for FC-1) | Low | Moderate | Moderate | Small renovation drawings with no CUI; wrong drawings cause rework; jobsites need current drawings daily (P05 MTD 24 h) |
| Payments; collections and receivables (pay apps, vendor bank details) | Low | **Moderate** | Low | One altered bank detail can divert more than a month's billing, a serious loss for a business this size (P01 R-001); billing tolerates 120 hours down |
| Personal information of subcontractors (W-9 forms) | Moderate | Low | Low | Social Security numbers trigger Florida breach duties |
| **PMPAS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 23 controls (`control-implementation.csv`). The set covers every FAR 52.204-21 requirement (which the SP 800-171 R2 chain maps to these controls) plus the controls that stop payment fraud (MFA, call-back verification, log review). Other Moderate controls are inherited from the SaaS vendors (evidence: the project management vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or software development.

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in SYS-01, SYS-02, and SYS-03; the laptop; the phone; the home office network; paper plan sets and files in the home office and truck.
- **Outside (external services):** the SaaS vendors' platforms, the bank portal, the federal portals, the AI bid assistant, the bookkeeper's own devices, and subcontractors' systems.
- **Out of scope for CMMC Level 1:** family devices on the home network once they move to a separate guest network (32 CFR 170.19(b)(2)(i)).

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement or control |
|---|---|---|
| FC-1 subcontractors (6) | Drawings, RFIs, submittals, invoices, certified payrolls | Subcontract (**FAR 52.204-21 and 52.204-25 substance missing: gap**) |
| Private clients | Pay apps, remittance details | Contract; no remittance-change notice yet (gap) |
| VA paying office | Invoices; EFT to the SAM bank account | FC-1 contract; FAR 52.232-33 |
| Outside bookkeeper | Accounting records, bank feed, W-9s | Engagement letter (**no security terms: gap**) |
| AI bid assistant vendor | Drawings and specifications (FC-1 change-order drawings uploaded June 2026) | Individual terms of service (**allowed use for model improvement: gap; see P10**) |
| Personal cloud photo account | Jobsite photos, including FC-1 | None (**not approved for FCI: gap**) |

## 9. System Component Inventory
| Component | Type | Manufacturer checked against FAR 52.204-25 | Owner |
|---|---|---|---|
| SYS-01 project management and pay app tenant | SaaS | n/a | Owner |
| SYS-02 accounting tenant | SaaS | n/a | Owner |
| SYS-03 email and file tenant | SaaS | n/a | Owner |
| SYS-04 laptop (bought 2026-02) | Endpoint | Yes, 2026-07-16 | Owner |
| Old laptop (replaced 2026-02; to be wiped and kept as a spare) | Endpoint | Yes, 2026-07-16 | Owner |
| SYS-05 smartphone | Endpoint | Yes, 2026-07-16 | Owner |
| SYS-06 internet service provider gateway | Network | Yes, 2026-07-16 (provider equipment) | Internet provider |
| SYS-06 Wi-Fi router | Network | Yes, 2026-07-16 | Owner |
| Carrier-branded mobile hotspot | Network | **Covered manufacturer; removed from use 2026-07-16** | Owner (to be returned to the carrier) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 23 controls:
- Implemented: 3
- Partially implemented: 16
- Planned: 4

Inheritance: 9 hybrid (a vendor operates the mechanism and the owner configures or uses it correctly) and 14 the owner's alone. None is fully inherited, because even where a SaaS vendor runs the mechanism, the owner still decides who gets access and where data goes.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; owner holds every role; vendor terms reviewed (SA-9); Section 889 purchase check (SR-5) |
| Identify | Risk assessment (RA-3); BIA (P05); component inventory with manufacturers (CM-8) |
| Protect | Unique accounts (IA-2, gap); MFA (IA-2(1), gap on SYS-01 and SYS-02); disk encryption (SC-28); approved locations for FCI (AC-20, planned) |
| Detect | Monthly and pre-pay-app check of sign-ins and forwarding rules (AU-6, planned) |
| Respond | Business email compromise runbook with call-back and bank recall steps (IR-8) |
| Recover | Vendor backups (CP-9, hybrid); standby supervision agreement and sealed recovery codes (CP-2, planned) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-22 with the on-call IT technician. See P07. These results are **not** a CMMC self-assessment; that is scheduled for November 2026 against the NIST SP 800-171A (June 2018) objectives (P03 G-021).

## 11. Digital Identity Acceptance Statement
The bank and the government sign-in service enforce MFA. Email uses text-message codes, which do not resist phishing; a security key is planned by 2026-10-31 because the top risk is mailbox takeover (P01 R-001). SYS-01 and SYS-02 use passwords only until app-based MFA is turned on (2026-09-15). FAR 52.204-21(b)(1)(vi) requires authentication but not MFA; the stronger methods are a business decision.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **CMMC:** Cybersecurity Maturity Model Certification (32 CFR Part 170)
- **EFT:** electronic funds transfer
- **FCI:** Federal contract information (FAR 52.204-21(a))
- **MFA:** multi-factor authentication
- **PMPAS:** Project Management and Payment Application System
- **SAM / SPRS:** System for Award Management / Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan; proposed CMMC Level 1 scope | Owner |

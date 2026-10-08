# System Security Plan (short form): Advisory Practice Systems Profile

**Organization:** Cris Santos Company (state-registered investment adviser) | **Tier:** Sole Proprietorship | **Vertical:** Finance and Insurance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Advisory Practice Systems Profile (**APSP**), identifier CSC-SYS-001. This is the "core business SaaS stack" named in the scenario brief.

## 2. System Overview
The APSP is everything the adviser uses to manage about $19 million for about 70 client households: trading and money movement at the custodian, portfolio models and fee billing, client records, email and files, financial planning, e-signature, and bookkeeping. One person, the owner-adviser, uses and runs it. Components are SYS-01 to SYS-10 in `../00_company-facts.md` section 3. There is no server and no IaaS. Most technical safeguards are **inherited from the custodian and the SaaS vendors**; the owner is responsible for identities and MFA, where client data is kept, the devices and home network, and vendor contracts (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N52-R01 | Gramm-Leach-Bliley Act, section 501(b) safeguards duty | 15 U.S.C. 6801(b) |
| N52-R03 | FTC Safeguards Rule (primary; P03) | 16 CFR Part 314. Small-entity exceptions in 314.6 apply |
| State | Adviser registration; books and records and OFR examination | Fla. Stat. 517.12; 517.121 |
| State | Data security, disposal, breach notice; recording consent | Fla. Stat. 501.171; Fla. Stat. 934.03 |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable, with the reason in P03 section 1: SEC Regulation S-P and S-ID (N52-R05, N52-R06) apply only to SEC-registered advisers; the Interagency Guidelines (N52-R02) apply to banks; NYDFS Part 500 (N52-R04), NAIC Model #668 (N52-R07), and SEC public-company disclosure (N52-R08) do not reach this business.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-adviser on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private adviser. Equivalent decision: the owner-adviser accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-003) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: MFA on every SaaS account (2026-09-15); encrypted backup to a second cloud location (2026-10-31); separate business network (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, Qualified Individual (16 CFR 314.4(a)), risk acceptor | Owner-adviser | Every role, designated in writing in POL-01 4.2 |
| Technical support | On-call IT consultant (services agreement since 2026-07-10) | Laptop, router, and SaaS settings on request; no standing access |
| Service providers | Custodian, SaaS vendors, compliance consultant | Operate inherited controls; handle client data under contract |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Client financial and identity records (customer information under 16 CFR 314.2) | Moderate | Moderate | Low | Disclosure triggers Florida notice and possible identity theft; wrong data leads to wrong advice; a few days' outage harms no client (P05) |
| Trading and money movement instructions | Moderate | Moderate | Moderate | A forged or altered instruction moves client money (P05 BP-02); trading must resume within a trading day (BP-01 MTD 24 h) |
| Books and records | Low | Moderate | Low | Must be complete and producible to the OFR (Fla. Stat. 517.121) |
| **APSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 28 controls that carry the Safeguards Rule elements for a one-person adviser (`control-implementation.csv`). Other Moderate controls are either inherited from the custodian and SaaS vendors (evidence: the portfolio platform's SOC 2 report, P09) or tailored out because they assume staff, servers, or software development. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in SYS-01 to SYS-06, SYS-09, and SYS-10; the laptop, phone, and USB drive; the home network as used for business; paper client files in the locked cabinet.
- **Outside (external services):** the custodian's platform, each SaaS vendor's platform, the internet provider, the IT consultant's and compliance consultant's own systems, and clients' email accounts.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Qualified custodian | Trades, fee files, money movement requests, statements | Custodial and adviser service agreements |
| Portfolio platform vendor | Daily custodian data feed; models; fees | Subscription terms with security commitments; SOC 2 Type 2 |
| Clients | Statements, review letters, requests | Advisory agreement; privacy notice. **Money movement requests arrive by ordinary email (gap)** |
| Compliance consultant | Sample client files each year | Engagement letter with **no security terms (gap)**; files sent as email attachments |
| IT consultant | Remote sessions on the laptop | Services agreement with security terms (2026-07-10) |
| Generative AI assistant vendor | Pasted client statements and notes | **Consumer terms that allow model training (gap; use paused, P10)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Custodian advisor portal (SYS-01) | Custodian-hosted service | Owner-adviser (account) |
| Portfolio and billing platform (SYS-02) | SaaS | Owner-adviser |
| CRM (SYS-03) | SaaS | Owner-adviser |
| Email and file suite (SYS-04) | SaaS (business plan) | Owner-adviser |
| Financial planning software (SYS-05) | SaaS | Owner-adviser |
| E-signature (SYS-06) | SaaS | Owner-adviser |
| Laptop, phone, USB drive (SYS-07) | Endpoints and media | Owner-adviser |
| Home network (SYS-08) | Internet provider router | Owner-adviser |
| Generative AI assistant (SYS-09) | Consumer SaaS | Owner-adviser |
| Accounting SaaS (SYS-10) | SaaS | Owner-adviser |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 28 controls:
- Implemented: 8
- Partially implemented: 15
- Planned: 5

Inheritance: 2 fully inherited from the SaaS vendors (AU-2, AU-9), 10 hybrid (the vendor operates the mechanism, the owner configures or uses it correctly), and 16 the owner's alone.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; Qualified Individual designation; vendor contracts (SA-9) |
| Identify | Risk assessment (RA-3); BIA (P05); data locations (POL-01 Appendix A) |
| Protect | Custodian and planning MFA (IA-2(2)); MFA on the administrator accounts (IA-2(1), gap); callback rule (POL-01 7.6, trained under AT-2(3)); encryption (SC-28, USB gap) |
| Detect | SaaS logging (AU-2, inherited); monthly sign-in and forwarding-rule review (AU-6, planned) |
| Respond | Business email compromise runbook (IR-8); notification matrix (IR-6) |
| Recover | Custodian records of account; weekly backup (CP-9, gap); successor adviser arrangement (CP-2, gap) |

### 10.2 Control assessment status
Self-assessed 2026-07-13 to 2026-07-17 with the IT consultant. See P07.

## 11. Digital Identity Acceptance Statement
The custodian portal requires a password and an authenticator app on the owner's phone, which is appropriate for access that can move client money. The email suite, CRM, portfolio platform, e-signature, and accounting services use a password only until MFA is turned on (2026-09-15); 16 CFR 314.4(c)(5) requires MFA for any individual accessing any information system unless the Qualified Individual approves an equivalent control in writing, and no such approval is appropriate here. Clients use the custodian's own client site and its identity controls, outside this boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **APSP:** Advisory Practice Systems Profile
- **Customer information:** nonpublic personal information about a customer, in any form (16 CFR 314.2(d))
- **MFA:** multi-factor authentication
- **OFR:** Florida Office of Financial Regulation
- **Qualified Individual:** the person designated to oversee the information security program (16 CFR 314.4(a))

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-adviser |

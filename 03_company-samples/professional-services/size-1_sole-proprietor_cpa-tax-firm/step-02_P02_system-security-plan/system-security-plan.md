# System Security Plan (short form): Tax Practice Systems Profile

**Organization:** Cris Santos Company (CPA and tax preparation practice) | **Tier:** Sole Proprietorship | **Vertical:** Professional, Scientific, and Technical Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Tax Practice Systems Profile (**TPSP**), identifier CSC-SYS-001.

## 2. System Overview
The TPSP is everything the practice uses to prepare and file about 425 returns a year, keep the books for 12 small businesses, and answer IRS notices. One person, the CPA-owner, uses and runs it. Its core is the registry's primary system, the **tax preparation software and client document portal** (SYS-01 and SYS-02), both hosted by one tax software vendor. Around that core sit the business email and file suite (SYS-03), practice management and billing (SYS-04), the laptop and printer-scanner (SYS-05), the owner's phone (SYS-06), the home office network (SYS-07), a generative AI assistant (SYS-08; client data stopped 2026-07-27, see P10), and accounting SaaS (SYS-09). Components are listed in `../00_company-facts.md` section 3. There is no server and no IaaS. Most safeguards are **inherited from the SaaS vendors**; the owner is responsible for identities, where client data goes, devices, the home network, and vendor contracts (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N54-R01 | FTC Safeguards Rule (GLBA). The 314.6 exception applies (about 1,450 consumers) | 16 CFR Part 314 |
| N54-R02 | IRC 7216 limits on disclosure and use of tax return information | 26 U.S.C. 7216; 26 CFR 301.7216-1 to -3 |
| N54-R03 | IRS WISP expectation and e-file provider duties | IRS Pubs. 4557 (Rev. 6-2024), 5708 (Rev. 8-2024), 1345 (Rev. 12-2025); Form W-12 line 11 |
| State | Data security, breach notice, disposal | Fla. Stat. 501.171(2), (3)-(6), (8) |
| Practice | Due diligence of a practitioner before the IRS | 31 CFR 10.22 (Circular 230) |
| Internal | Information Security Policy (the firm's WISP with P01, P02, and P08) | POL-01 (P06) |

Not applicable: HIPAA as a business associate (N54-R06), FAR and DFARS with CMMC (N54-R04, N54-R05), ABA Model Rules (N54-R07), and CIRCIA (N54-R09, proposed only). The AICPA confidentiality rule (N54-R08) is noted, not assessed.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the CPA-owner on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private practice. Equivalent decision: the CPA-owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001 email takeover, R-009 single-person dependency) are treated by their due dates and that every High and Moderate treatment is done before the 2027 filing season (2027-01-15).
### 4.3 System Operational Status
Operational. Planned changes: scan-to-folder replaces scan-to-email and MFA goes on for email and practice management (2026-09-15); separate home office network (2026-10-31); backup service for the email and file suite (2026-11-30); portal-only exchange of returns and documents with required client MFA (2027-01-15).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, Qualified Individual (16 CFR 314.4(a)), e-file Responsible Official, risk acceptor | CPA-owner | Every role, designated in writing in POL-01 |
| Technical support | On-call IT consultant (services agreement and IRC 7216 notice since 2026-07-23) | Laptop, router, printer-scanner, and SaaS settings on request; no standing access |
| Service providers | Tax software vendor, email and file suite provider, practice management vendor, accounting SaaS vendor, AI assistant vendor | Operate inherited controls |

**Overlap.** The owner designs, operates, and checks every control. The compensating checks are the IT consultant's review during the self-assessment, the tax software vendor's SOC 2 report, and the outside review every second year required by POL-01 4.5.

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Client tax return information (SSNs, income, bank and brokerage accounts, prior returns) | Moderate | Moderate | Moderate | Theft enables refund fraud and identity theft and triggers IRS, FTC, and Florida duties; a wrong figure becomes a wrong return; loss beyond two filing-season days misses deadlines (P05 MTD 48 h) |
| Small-business bookkeeping and payroll data | Moderate | Moderate | Low | Employee pay data; clients can run payroll themselves for a cycle (P05 MTD 72 h) |
| Practice administration (billing) | Low | Low | Low | Fees can be billed late (P05 MTD 168 h) |
| **TPSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 26 controls that carry the Safeguards Rule elements for a one-person practice (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS vendors (evidence: the tax software vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program.

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in SYS-01 to SYS-04, SYS-08, and SYS-09; the laptop, printer-scanner, and phone; the home office's use of the home network and router; paper files in the home office.
- **Outside (external services):** the tax software vendor's platform and its hosting provider, the IRS and state e-file systems, the email suite, practice management, accounting, and AI assistant platforms, clients' own accounting and payroll services, the phone's personal photo backup service (to be emptied of client documents), and the internet provider.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Tax software vendor (also an Authorized IRS e-file Provider) | Returns and source documents; e-file transmission to the IRS and states | Vendor contract; permitted preparer-to-preparer disclosure (301.7216-2(d)(1)); SOC 2 report |
| IRS and state tax agencies | Returns, extensions, notice responses, transcripts | IRS e-file rules (Pub. 1345); powers of attorney |
| Clients | Source documents in; returns and Forms 8879 out | Engagement letters. **Plain email and text photos today (gap)** |
| Email and file suite provider | Attachments and client folders | Business terms with a data protection addendum |
| IT consultant | Remote sessions on the laptop | Services agreement and IRC 7216 notice since 2026-07-23 |
| AI assistant vendor | Uploaded client documents and notice text (stopped 2026-07-27) | **Individual plan terms; no IRC 7216 basis (gap, P10)** |
| Mortgage lenders (on client request) | Copies of returns | Signed IRC 7216 consent before release |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Tax software and client portal (SYS-01, SYS-02) | SaaS | CPA-owner (account) |
| Email and file suite (SYS-03) | SaaS, business plan | CPA-owner |
| Practice management and billing (SYS-04) | SaaS | CPA-owner |
| Laptop and printer-scanner (SYS-05) | Endpoints | CPA-owner |
| Mobile phone (SYS-06) | Personal endpoint | CPA-owner |
| Home network and router (SYS-07) | Shared home network | CPA-owner (router from the internet provider) |
| Generative AI assistant (SYS-08) | SaaS, individual plan | CPA-owner |
| Accounting SaaS (SYS-09) | SaaS | CPA-owner (own books); clients (their files) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 26 controls:
- Implemented: 8
- Partially implemented: 15
- Planned: 3

Inheritance: 1 fully inherited (AU-2, from the tax software vendor and the email suite), 10 hybrid (a vendor operates the mechanism and the owner configures or uses it correctly), and 15 the owner's alone.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01 as the written program; Qualified Individual designated; vendor contracts and IRC 7216 notice (SA-9) |
| Identify | Risk assessment (RA-3); BIA (P05); data locations list (CM-8) |
| Protect | Tax software MFA (IA-2(1)); email and practice management MFA (gap); laptop encryption (SC-28); portal-only exchange (SC-8, gap) |
| Detect | Vendor logging (AU-2, inherited); monthly log and forwarding-rule review (AU-6, planned) |
| Respond | Business email compromise runbook with IRS, FTC, and Florida clocks (IR-8, IR-6) |
| Recover | Tax software vendor backups (CP-9, inherited); suite backup (gap); continuation agreement (CP-2, gap) |

### 10.2 Control assessment status
Self-assessed 2026-07-27 to 2026-07-31 with the IT consultant (tests on 2026-07-29). See P07.

## 11. Digital Identity Acceptance Statement
The tax software requires a password and an authenticator app on the owner's phone, which fits a Moderate categorization and remote access to taxpayer data. The email suite and practice management SaaS use a password only until MFA goes on (2026-09-15); the email account is also the suite's administrator account, so it is the most exposed identity in the practice. Clients sign Forms 8879 through the portal's e-signature with identity verification provided by the vendor (Pub. 1345 sets the requirements; P03 G-047); portal MFA for clients becomes mandatory on 2027-01-15.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **EFIN / PTIN:** Electronic Filing Identification Number / Preparer Tax Identification Number
- **ERO:** Electronic Return Originator
- **MFA:** multi-factor authentication
- **TPSP:** Tax Practice Systems Profile
- **WISP:** written information security plan (the IRS term for the Safeguards Rule's written program)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | CPA-owner |

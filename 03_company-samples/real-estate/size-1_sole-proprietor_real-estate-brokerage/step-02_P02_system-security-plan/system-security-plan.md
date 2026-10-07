# System Security Plan (short form): Transaction Management and Closing Communications System

**Organization:** Cris Santos Company (residential real estate brokerage) | **Tier:** Sole Proprietorship | **Vertical:** Real Estate and Rental and Leasing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Transaction Management and Closing Communications System (**TMCC**), identifier CSC-SYS-001.

## 2. System Overview
The TMCC is everything the brokerage uses to take a client from first contact to a funded closing or a signed lease: contracts and deadlines, document exchange, e-signatures, email with clients, lenders, and title companies, the sales escrow account, and the devices the owner works on. One person, the broker-owner, runs it, with help from a freelance transaction coordinator. Components are SYS-01 to SYS-09 in `../00_company-facts.md` section 3: the transaction platform, email and files, e-signature, the MLS and showing apps, online banking, accounting, the laptop, the phone, and the home network. The tenant screening service (SYS-10) and the AI writing assistant (SYS-11) are external services that exchange data with it. There is no server and no IaaS. Most technical safeguards are **inherited from the SaaS vendors and the bank**; the owner is responsible for identities, data handling, devices, the home network, and how money instructions are confirmed (P04).

**The system's main job, from a security view, is to make sure that every instruction to move money is genuine.** The BIA (P05) and the risk register (P01) both rank closing funds first.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| State | Broker escrow duties | Fla. Stat. 475.25(1)(d)1. and (1)(k); Fla. Admin. Code ch. 61J2-14; r. 61J2-10.032; record retention Fla. Stat. 475.5015 |
| State | Reasonable measures, breach notice, disposal | Fla. Stat. 501.171(2)-(6), (8) |
| N53-R02 | FTC Act Section 5 | 15 U.S.C. 45(a), (n) |
| Federal | FCRA adverse action and disposal of consumer information (tenant screening) | 15 U.S.C. 1681m(a); 16 CFR 682.3 |
| N53-R01 | FTC Safeguards Rule, **benchmark only** (not a financial institution; P03 section 1) | 16 CFR 314.4 |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: the FinCEN residential real estate rule (vacated 2026-03-19, appeal pending; brokers are not in its reporting cascade), CCPA/CPRA (N53-R03), PCI DSS (N53-R04; no cards accepted), and SEC disclosure (N53-R05).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the broker-owner on 2026-09-15.
### 4.2 System Authorization Decision
No formal authorization applies to a private brokerage. Equivalent decision: the broker-owner accepted continued operation on 2026-09-15, on condition that the three High risks in P01 (R-001, R-002, R-004) are treated by their due dates, and that **no escrow disbursement is made on emailed instructions without a phone callback** from that date (POL-01 8.4).
### 4.3 System Operational Status
Operational. Planned changes: separate mailbox login for the coordinator and authenticator-app MFA on every account (2026-09-30); secure document sharing for wire instructions (2026-10-31); separate work network at home (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead (benchmark Qualified Individual), privacy contact, risk acceptor | Broker-owner | Every role (designated in writing in POL-01 4.2) |
| User | Freelance transaction coordinator | Prepares files and sends documents; bound by the engagement terms in POL-01 6.2 once signed |
| Limited user | Outside bookkeeper | Accounting login; prepares the escrow reconciliation; no banking access |
| Technical support | On-call IT technician (confidentiality agreement since 2026-08-14) | Laptop and network help on request; no standing access |
| Service providers | Platform, email, e-signature, accounting, and screening vendors; the bank | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Client identity and financial records (driver license images, bank statements, pre-approval letters, screening reports) | Moderate | Moderate | Low | Disclosure triggers Florida breach notice and identity theft risk; files can be rebuilt from clients and lenders |
| Payment instructions and escrow records | Moderate | **Moderate** | Moderate | Altered instructions send client money to criminals (integrity is the main concern); a closing cannot fund without a trusted channel (P05 MTD 24 h) |
| Transaction documents and deadlines | Low | Moderate | Moderate | Mostly shared with the other parties; a wrong or missed deadline harms the client (P05 MTD 24 h) |
| **TMCC category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

Integrity is rated Moderate rather than High because every wire also passes through a bank and a title company, and because the phone callback rule (POL-01 8.4) gives a second, independent check. If the owner ever handled closing disbursements as settlement agent, integrity would move to High.

**Baseline:** SP 800-53B Moderate, tailored to 24 controls that carry the binding duties and the benchmark elements for a one-person brokerage (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors and the bank (evidence: the platform vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or software development.

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in SYS-01 to SYS-06, the laptop and phone, the home office network as used for work, the escrow ledger spreadsheet, and paper files in the home office.
- **Outside (external services):** the vendors' platforms, the bank's systems, the MLS and lockbox provider, the tenant screening service (SYS-10), the AI writing assistant (SYS-11), the coordinator's own laptop, title companies, lenders, and clients' own email.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Title companies and closing attorneys | Contracts; closing documents; **wire instructions (inbound and outbound)** | None needed (independent parties); verification by phone callback (POL-01 8.4) |
| Buyers and sellers | Contracts, disclosures, escrow wire instructions | Engagement agreement; wire instructions move to secure document sharing |
| Freelance transaction coordinator | Full transaction files; the owner's mailbox | **No written security terms (gap)** |
| Outside bookkeeper | Bank statements, escrow ledger | Engagement letter, confidentiality only (gap: no breach notice term) |
| Escrow bank | Deposits, wires | Bank account agreement |
| Tenant screening service | Applicant data and consumer reports | Click-through terms; **never reviewed (gap)** |
| AI writing assistant | Listing details; some pasted client details | Consumer terms; **client data now prohibited (POL-01 9.5)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Transaction platform account (SYS-01) | SaaS | Broker-owner |
| Email and files (SYS-02) | SaaS | Broker-owner |
| E-signature (SYS-03) | SaaS | Broker-owner |
| MLS, showing, and lockbox apps (SYS-04) | Provider apps | MLS and local association |
| Online banking (SYS-05) | Bank-hosted | Broker-owner (bank operates) |
| Accounting (SYS-06) | SaaS | Broker-owner |
| Laptop (SYS-07) | Endpoint | Broker-owner |
| Mobile phone (SYS-08) | Personal endpoint | Broker-owner |
| Home office network (SYS-09) | ISP router | Broker-owner (ISP supplies equipment) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 24 controls:
- Implemented: 5
- Partially implemented: 14
- Planned: 5

Inheritance: 1 fully inherited from the email provider (SI-8), 10 hybrid (the vendor or bank operates the mechanism, the owner configures or uses it correctly), and 13 the owner's alone.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; service provider terms (SA-9, gap); owner holds every role |
| Identify | Risk assessment (RA-3); BIA (P05); retention schedule (SI-12, planned) |
| Protect | Separate identities (IA-2, gap); MFA (IA-2(1), IA-2(2), gaps); disk encryption (SC-28); training (AT-2(3), planned) |
| Detect | Weekly mailbox and sign-in review with provider alerts (AU-6, planned); spam filtering (SI-8, inherited) |
| Respond | Business email compromise runbook (IR-8); phone callback before any money moves (POL-01 8.4) |
| Recover | Vendor backups (CP-9, inherited); backup broker arrangement and sealed recovery codes (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-08-17 to 2026-08-21 with the IT technician. See P07.

## 11. Digital Identity Acceptance Statement
Email and online banking require a password and a text-message code; the transaction platform, e-signature, and accounting accounts use a password only. Text codes resist password guessing but not a fake sign-in page that relays the code, which is the usual first step in business email compromise. The owner accepts nothing less than an authenticator app (with number matching where offered) or a security key for email, the platform, and banking by 2026-09-30, and an authenticator app for all other accounts. Clients and title companies are outside this boundary; their identity is checked by calling a number taken from the contract file, never from an email.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **BEC:** business email compromise
- **DMARC:** Domain-based Message Authentication, Reporting, and Conformance (an email domain setting that tells receivers to reject forged mail)
- **MFA:** multi-factor authentication
- **MLS:** multiple listing service
- **TMCC:** Transaction Management and Closing Communications System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-15 | Initial short-form plan | Broker-owner |

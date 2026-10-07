# System Security Plan (short form): Agency Systems Profile

**Organization:** Cris Santos Company (independent insurance agency) | **Tier:** Sole Proprietorship | **Vertical:** Financial Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-14

## 1. System Name and Identifier
Agency Systems Profile (**ASP**), identifier CSC-ASP-001.

## 2. System Overview
The ASP is everything the agency uses to sell and service about 1,150 policies for about 640 client accounts: quoting, binding, policy service, claims help, invoicing agency-billed policies, and the premium trust account. One person, the owner-agent, uses and runs it. Components are SYS-01 to SYS-08 in `../00_company-facts.md` section 3: the agency management system (AMS, SaaS), a business email and file suite, insurer and partner portals, an e-signature service, accounting SaaS and online banking, a laptop, phone, and printer-scanner, the home office network, and a consumer generative AI chatbot (paused; see P10). There is no server and no IaaS. Most safeguards inside each service are **inherited from the SaaS vendors and insurers**; the owner is responsible for identities, data handling, devices, the home network, and vendor contracts (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| Source | Requirement | Citation |
|---|---|---|
| Florida statute | Reasonable measures to protect personal information; disposal; breach notice | Fla. Stat. 501.171(2), (3)-(6), (8) |
| Florida Insurance Code | Premium trust funds and premium records (3 years); policy records (5 years after expiration); privacy of nonpublic personal information | Fla. Stat. 626.561, 626.748, 626.9651; Rule 69O-128, F.A.C. |
| Contract | Insurer data security addenda (4 of 9 insurers): GLBA 501(b)-consistent safeguards, MFA, 72-hour incident notice, annual questionnaire | Carrier DSA |
| Benchmark | Elements of an information security program, used to judge "reasonable measures" and the addenda | 16 CFR 314.4 (benchmark only; the rule does not bind an insurance agency) |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: the FTC Safeguards Rule as law (15 U.S.C. 6805(a)(6)-(7); 16 CFR 314.1(b)), the vertical's bank, credit union, and SEC rules (C-FINANCIAL-R01 to R04), NYDFS Part 500 (C-FINANCIAL-R05; no New York license), and CIRCIA (C-FINANCIAL-R06; proposed only). Reasons are in P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-agent on 2026-09-14.
### 4.2 System Authorization Decision
No formal authorization applies to a private agency. Equivalent decision: the owner-agent accepted continued operation on 2026-09-14, on condition that the High risks in P01 (R-001, R-002, R-005) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: authenticator app or security key for email and banking (2026-09-30); separate agency network (2026-10-31); AMS client upload portal for documents (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, information security coordinator, privacy contact, risk acceptor | Owner-agent | Every role (designated in writing in POL-01) |
| Technical support | On-call IT consultant (security terms since 2026-07-27) | Laptop, router, printer-scanner, and SaaS settings on request; owner-started sessions only |
| Bookkeeping | Outsourced bookkeeper | Reconciliations; own accounting user; banking access to be moved to a sub-user |
| Service providers | AMS vendor, email suite vendor, insurers, e-signature vendor, rater vendor | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Insurance services (client applications, policies, claims notes, driver license and Social Security numbers) | Moderate | Moderate | Moderate | Disclosure triggers Florida notice and insurer notice duties; wrong data can leave a client uninsured; loss beyond one business day stops binding and claims help (P05 MTD 24 h) |
| Financial management (premium trust account, invoices, commissions) | Moderate | Moderate | Low | A changed bank detail redirects trust funds; remittances can wait days (P05 MTD 72 h) |
| **ASP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 24 controls that carry the agency's duties for a one-person business (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS vendors (evidence: the AMS vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or software development.

## 7. Authorization Boundary Description
- **Inside:** the owner's AMS, email, insurer portal, rater, e-signature, accounting, and banking accounts and settings; the laptop, phone, and printer-scanner; the retired laptop; the home office network; paper in the office and the garage.
- **Outside (external services):** the AMS vendor's platform, the email suite platform, insurer and partner platforms, the bank, the bookkeeper's own computer, and the AI chatbot vendor.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Insurers (9) | Applications, policy changes, claims reports | Agency agreements; data security addenda with 4 |
| Wholesale broker; premium finance company | Submissions; finance agreements | Broker agreement; finance company producer agreement (security terms not reviewed) |
| Clients | Applications, ID photos, invoices, bank draft forms | Plain email and text today (**gap**) |
| Bookkeeper | Bank statements, deposits, commission data | **Engagement letter without security or confidentiality terms (gap)** |
| AI chatbot vendor | Pasted declarations pages and applications | **Consumer terms; model training allowed (gap; paused)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| AMS tenant (SYS-01) | SaaS | Owner-agent |
| Email and file suite (SYS-02) | SaaS (business plan) | Owner-agent |
| Insurer and partner portal accounts (SYS-03) | Third-party hosted | Owner-agent |
| E-signature account (SYS-04) | SaaS | Owner-agent |
| Accounting SaaS and online banking (SYS-05) | SaaS; bank-hosted | Owner-agent |
| Laptop, phone, printer-scanner, retired laptop (SYS-06) | Endpoints | Owner-agent |
| Home office network (SYS-07) | Home network | Owner-agent |
| AI chatbot account (SYS-08) | Consumer app | Owner-agent |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 24 controls:
- Implemented: 7
- Partially implemented: 15
- Planned: 2

Inheritance: 2 fully inherited from the SaaS vendors (AC-3, AU-2), 10 hybrid (the vendor operates the mechanism, the owner configures or uses it correctly), and 12 the owner's alone (AC-11, AC-19, AT-2, AU-6, CP-2, IA-5, IR-8, MP-6, PE-3, RA-3, SA-9, SC-7).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor terms (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05) |
| Protect | MFA (IA-2(1), IA-2(2)); unique identities (IA-2, gap on banking); encrypted devices (SC-28); secure document exchange (SC-8, gap) |
| Detect | Vendor logging (AU-2, inherited); monthly mailbox and sign-in review (AU-6, planned); spam and phishing filtering (SI-8) |
| Respond | Business email compromise runbook (IR-8) |
| Recover | AMS vendor backups (CP-9, inherited); AMS export and email backup (CP-9, gap); emergency servicing arrangement (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-08-03 to 2026-08-07 with the IT consultant. See P07.

## 11. Digital Identity Acceptance Statement
The AMS requires a password and an authenticator app code, which is appropriate for remote access to client personal information at a Moderate categorization. Email and online banking use a text message code, which defeats password-only attacks but not phishing pages that relay codes or SIM swaps; both move to an authenticator app or security key by 2026-09-30. Two insurer portals and the rater use a password only until MFA is available or turned on. Clients use each insurer's own portal and identity controls, outside this boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **AMS:** agency management system
- **ASP:** Agency Systems Profile
- **Carrier DSA:** an insurer's data security addendum to its agency agreement
- **E&O:** errors and omissions insurance
- **MFA:** multi-factor authentication
- **Premium trust account:** the bank account that holds premiums as trust funds (Fla. Stat. 626.561)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-14 | Initial short-form plan | Owner-agent |

# System Security Plan (short form): Recruiting and Placement Systems Profile

**Organization:** Cris Santos Company (independent recruiter) | **Tier:** Sole Proprietorship | **Vertical:** Administrative and Support and Waste Management and Remediation Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Recruiting and Placement Systems Profile (**RPSP**), identifier CSC-SYS-001. This is the business's version of the registry's "payroll and applicant tracking system": the applicant tracking system plus the back-office partner portal that feeds the partner's payroll. The business runs no payroll of its own (`../00_company-facts.md` section 5).

## 2. System Overview
The RPSP is everything the owner uses to recruit, submit, and place candidates and to keep 11 contractors on assignment: the recruiting ATS/CRM with its AI match add-on (SYS-01), business email and files (SYS-02), the back-office partner portal (SYS-03), accounting (SYS-04), e-signature (SYS-05), the owner's sourcing accounts (SYS-09), and a consumer AI chatbot (SYS-10), reached from one laptop (SYS-06), a personal phone (SYS-07), and the home network (SYS-08). One person, the owner-recruiter, uses and runs it. There is no server and no IaaS. Platform safeguards are **inherited from the SaaS vendors**; the owner is responsible for identities, data handling, devices, and vendor terms (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Applies? |
|---|---|---|---|
| N56-BM | NIST CSF 2.0 (voluntary benchmark) | NIST CSWP 29 | Yes, voluntary (P03) |
| State | Florida Information Protection Act: reasonable measures, breach notice, disposal | Fla. Stat. 501.171(2)-(6), (8) | Yes. "Covered entity" includes a sole proprietorship (501.171(1)(b)) |
| N56-R01 | FTC/FACTA Disposal Rule | 16 CFR 682.3 | Yes. The owner possesses consumer information (2 client-forwarded background reports and the partner's clearance status) |
| Federal | Title VII employment agency practices and disparate impact; ADA selection criteria | 42 U.S.C. 2000e-2(b), (k); 42 U.S.C. 12112(b)(6) | Yes, for the AI match add-on (P10). An employment agency is covered regardless of its own headcount |
| N56-R02 | FCRA employment background checks | 15 U.S.C. 1681b(b) | No. The owner does not procure consumer reports |
| N56-R03 | Form I-9 | 8 CFR 274a.2 | No. Recruiter and referrer duties are limited to agricultural entities (274a.2(a)(1)) |
| Internal | Information Security Policy | POL-01 (P06) | Yes |

Not applicable: N56-R04 to N56-R09 (no PHI, telemarketing, payment cards, federal contracts, NYC jobs, or hazmat) and Fla. Stat. 448.095 (no employees). Reasons are in P03.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-recruiter on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner-recruiter accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-004) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: authenticator-app MFA on email and MFA on the ATS (2026-09-15); purge of SSNs and IDs from email and devices (2026-10-31); separate work network at home (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, privacy contact, risk acceptor | Owner-recruiter | Every role (designated in POL-01 4.2) |
| Technical support | On-call IT support technician (confidentiality agreement since 2026-07-17) | Laptop, phone, and router help on request; no standing access |
| Bookkeeping | Outside bookkeeper | Named account in the accounting SaaS only |
| Service providers | ATS vendor, email provider, back-office partner, accounting and e-signature vendors | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Staff recruitment and employment (candidate records, resumes, submittals) | Moderate | Moderate | Low | Home addresses, work history, and compensation; wrong data harms candidates; searches tolerate 2-3 days of outage (P05 MTD 48-72 h) |
| Personal identity and authentication (SSNs, dates of birth, ID images in start forms and email) | Moderate | Moderate | Low | Disclosure triggers Fla. Stat. 501.171 notice and identity theft risk |
| Contractor assignment data (start requests, pay and bill rates) | Moderate | Moderate | Moderate | A missed start request stops a contractor starting (P05 BP-01 MTD 24 h) |
| **RPSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 23 controls that a one-person, SaaS-only business can run (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors (evidence: the partner's SOC 2 report, P09; vendor security pages) or tailored out because they assume staff, servers, or software development.

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts, settings, and data in the ATS, email and files, partner portal, accounting, e-signature, sourcing, and chatbot services; the laptop and phone; the home network as used for work; paper in the home office.
- **Outside (external services):** the SaaS platforms themselves, the partner's payroll, I-9, E-Verify, and background check operations, the job boards and networking site, the internet provider, and the clients' systems.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Back-office partner (portal) | Start requests with SSN and date of birth; rates; timesheet status; margin statements | Back-office services agreement: confidentiality only, **no security or breach notice terms (gap)** |
| Clients | Candidate submittals (resume, summary, rate or salary) by email | Fee agreement with a confidentiality clause |
| ATS vendor and AI match add-on | Candidate records and resumes | Click-through terms; AI training opt-out **off (gap)** |
| Consumer AI chatbot | Pasted resumes (stopped 2026-07-21) | Consumer terms; **not approved for personal data (gap)** |
| Job boards and networking site | Job ads out; applications in | Subscription terms |
| Outside bookkeeper | Invoices and bank feed | Engagement letter with confidentiality |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Recruiting ATS/CRM with AI match add-on (SYS-01) | SaaS | Owner-recruiter |
| Email, calendar, and files (SYS-02) | SaaS (business plan) | Owner-recruiter |
| Back-office partner portal account (SYS-03) | Partner SaaS | Owner-recruiter (account); partner (platform) |
| Accounting SaaS (SYS-04) | SaaS | Owner-recruiter |
| E-signature (SYS-05) | SaaS | Owner-recruiter |
| Laptop (SYS-06) | Endpoint | Owner-recruiter |
| Smartphone (SYS-07) | Personal endpoint | Owner-recruiter |
| Home network and router (SYS-08) | Consumer network | Owner-recruiter (router supplied by the internet provider) |
| Sourcing accounts (SYS-09) | SaaS | Owner-recruiter |
| Consumer AI chatbot account (SYS-10) | Consumer SaaS | Owner-recruiter |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 23 controls:
- Implemented: 7
- Partially implemented: 13
- Planned: 3

Inheritance: 1 fully inherited from the SaaS vendors (AU-2), 9 hybrid (a vendor operates the mechanism, the owner configures or uses it correctly), and 13 the owner's alone.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor terms and the partner's SOC 2 review (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); data locations (SI-12, planned) |
| Protect | MFA (IA-2(1), partial); password manager (IA-5, planned); disk encryption (SC-28); device lock (AC-11) |
| Detect | SaaS sign-in and export logs (AU-2, inherited); monthly review (AU-6, planned) |
| Respond | Email and ATS takeover runbook (IR-8); notice duties (IR-6) |
| Recover | SaaS backups (CP-9, partial); continuity sheet and sealed recovery codes (CP-2, partial) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the IT support technician. See P07.

## 11. Digital Identity Acceptance Statement
Every account the owner holds is an administrator account over personal information, so each needs a second factor that resists phishing as far as the service allows. Today only the accounting SaaS meets that. Email uses SMS codes, which an adversary-in-the-middle page can relay; the partner portal's code goes to that same mailbox; the ATS has no second factor. Target by 2026-09-15: authenticator-app MFA with number matching on email, MFA on the ATS, and the partner portal code moved to the authenticator app if the partner supports it (otherwise protected by the stronger email MFA). Candidates and clients use no accounts in this boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and partner report review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **ATS:** applicant tracking system
- **Back-office partner:** the contract staffing firm that employs and pays the contractors the owner places (employer of record)
- **MFA:** multi-factor authentication
- **RPSP:** Recruiting and Placement Systems Profile
- **Start request:** the partner form that creates a new contractor (name, address, SSN, date of birth, rates, start date)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-recruiter |

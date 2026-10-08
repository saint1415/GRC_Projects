# System Security Plan (short form): Core Business SaaS Stack

**Organization:** Cris Santos Company (tutoring and educational support service) | **Tier:** Sole Proprietorship | **Vertical:** Educational Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-07-31

## 1. System Name and Identifier
Core Business SaaS Stack (**CBSS**), identifier CSC-SYS-001.

## 2. System Overview
The CBSS is everything the business uses to tutor about 55 active students and keep records on about 265 children: scheduling and billing, student folders, the student practice portal, online sessions, and the devices and home network used to reach them. One person, the owner-tutor, uses and runs it. Components are SYS-01 to SYS-09 in `../00_company-facts.md` section 3: an email and files suite, a client-management SaaS, a website-builder site with a members-only student portal, a video platform, a laptop, a personal phone, the home network, an accounting SaaS, and a consumer AI assistant (use narrowed in P10). There is no server and no IaaS. Most platform safeguards are **inherited from the SaaS vendors**; the owner is responsible for accounts, data handling, devices, the home network, and vendor terms (P04).

The portal makes the business an **operator of an online service directed to children** under the COPPA Rule (16 CFR 312.2), so the plan is also the written information security program that 16 CFR 312.8(b) requires, together with POL-01.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N61-R03 | COPPA Rule, as amended in 2025 (compliance date 2026-04-22) | 15 U.S.C. 6501-6506; 16 CFR Part 312 (notice 312.4, consent 312.5, parent review 312.6, security program 312.8, retention 312.10) |
| State | Data security, breach notice, and disposal | Fla. Stat. 501.171 (sections (2), (3)-(4), (8)) |
| State | Consent to record online sessions | Fla. Stat. 934.03(2)(d) |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable (reasons in P03 section 1): FERPA (N61-R01; no Department of Education funds, 34 CFR 99.1), GLBA Safeguards Rule (N61-R02; no Title IV participation), CIPA (N61-R04; no E-Rate), HIPAA (N61-R05; not a covered entity), and CIRCIA (N61-R06; proposed only).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-tutor on 2026-07-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner-tutor accepted continued operation on 2026-07-31, on condition that the free fixes for the four High risks in P01 (R-001 to R-004: MFA, disk encryption, a separate family account) are in place by 2026-08-14, before the fall term starts on 2026-08-17, that the children's privacy notice is posted by the same date, and that the independent backup for R-001 is in place by 2026-09-30.
### 4.3 System Operational Status
Operational. Planned changes: password manager and MFA on every account (2026-08-14); separate family device account (2026-08-14); first retention purge (2026-09-30); independent backup of student folders (2026-09-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, information security program coordinator (16 CFR 312.8(b)(1)), privacy contact for parents, risk acceptor, incident lead | Owner-tutor | Every role (designated in writing in POL-01 4.2) |
| Technical support | On-call IT technician (confidentiality and data-handling agreement signed 2026-07-08) | Laptop, router, and account help on request; remote support only in sessions the owner starts |
| Service providers | Email and files suite, client-management SaaS, website-builder, video platform, accounting SaaS vendors | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Children's personal information and student records (portal content, assessments, progress notes, IEP and 504 plans, evaluations) | Moderate | Moderate | Low | Disclosure harms children and triggers Florida notice for evaluations and portal passwords; wrong accommodations or scores mislead teaching; BIA MTD 120 to 168 h (BP-03, BP-05) |
| Scheduling and parent contact | Low | Moderate | Moderate | Contact data only; a wrong time or address for an in-home session matters; BIA MTD 24 h (BP-02) |
| Billing records | Low | Low | Low | No card numbers (processor-hosted page); BIA MTD 336 h (BP-04) |
| **CBSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 28 controls that carry the COPPA security program and Florida duties for a one-person business (`control-implementation.csv`). PT-4 and PT-5 come from the SP 800-53B privacy baseline because COPPA is mainly a notice and consent rule. Other Moderate controls are either inherited from the SaaS vendors (evidence: the client-management SaaS SOC 2 report, P09) or tailored out because they assume staff, servers, or software development. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's account settings and member lists in SYS-01 to SYS-04 and SYS-08, the AI assistant account (SYS-09), the laptop, the phone, the home router settings, and paper worksheets and notes at home.
- **Outside (external services):** the vendors' platforms, the payment processor's hosted page, the internet service provider's network, the library's network, the personal photo cloud linked to the phone (being removed from business use), and the tax preparer.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Parents | Intake forms, report cards, IEP and 504 plans, schedules, progress reports | Enrollment agreement (e-signed); **lacks COPPA direct notice content (gap)** |
| Students under 13 (portal) | Name, user name, work photos, reading audio, messages | Parent consent through the enrollment agreement; **not informed consent (gap)** |
| Client-management SaaS vendor | Student and parent profiles, session notes, invoices | Terms with a data processing addendum; SOC 2 Type 2 report |
| Website-builder vendor | Portal content collected from children | Standard terms only; **no written security assurances reviewed (gap, 312.8(c))** |
| Video platform vendor | Live sessions and cloud recordings | Standard terms only; **no written security assurances reviewed (gap)** |
| Consumer AI assistant vendor | Student first names, scores, accommodations in prompts | Consumer terms allow use for model improvement; **no parent consent and no assurances (gap; P10)** |
| Accounting SaaS and tax preparer | Parent names and payment totals | Standard terms; tax preparer engagement letter |
| On-call IT technician | Remote access to the laptop during owner-started sessions | Confidentiality and data-handling agreement, 2026-07-08 |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Email and files suite (SYS-01) | SaaS, paid business plan | Owner-tutor |
| Client-management SaaS (SYS-02) | SaaS | Owner-tutor |
| Website and student practice portal (SYS-03) | Website-builder SaaS | Owner-tutor |
| Video platform (SYS-04) | SaaS, paid plan | Owner-tutor |
| Laptop (SYS-05) | Endpoint | Owner-tutor |
| Mobile phone (SYS-06) | Personal endpoint | Owner-tutor |
| Home network (SYS-07) | Router from the internet service provider | Owner-tutor (household) |
| Accounting SaaS (SYS-08) | SaaS | Owner-tutor |
| Consumer AI assistant (SYS-09) | Consumer app | Owner-tutor |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 28 controls:
- Implemented: 5
- Partially implemented: 19
- Planned: 4

Inheritance: 2 fully inherited from the SaaS vendors (AC-3, AU-9), 10 hybrid (the vendor provides the mechanism and the owner configures or uses it), and 16 the owner's alone (AC-5, AC-11, AT-2, AU-6, CA-2(1), CM-3, CP-2, IA-5, IR-8, MP-6, PL-4, PT-4, PT-5, RA-3, SA-9, SI-12).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01 as the written security program (312.8(b)); vendor assurances (SA-9, gap); notice and consent (PT-4, PT-5) |
| Identify | Risk assessment (RA-3); BIA (P05); data retention schedule (SI-12, planned) |
| Protect | MFA (IA-2(1) and IA-2(2), gaps); laptop encryption (SC-28, gap); separate accounts (IA-2, PL-4) |
| Detect | Monthly sign-in history review (AU-6, planned); built-in antivirus (SI-3) |
| Respond | Ransomware runbook (IR-8) |
| Recover | Version history and independent backup (CP-9); emergency sheet and backup tutor (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-13 to 2026-07-17 with the IT technician; tests on 2026-07-16. See P07.

## 11. Digital Identity Acceptance Statement
The client-management SaaS requires a password and a second factor on the owner's phone, which is appropriate for administrator access to children's records at a Moderate categorization. The email suite, website-builder administrator, and video platform use a password only until MFA is turned on (2026-08-14). Students sign in to the portal with a user name and password; from 2026-08-14 parents set the password at account creation, and the owner no longer keeps a list of them. Parents use the client-management SaaS parent login, which the vendor runs.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **CBSS:** Core Business SaaS Stack
- **COPPA:** Children's Online Privacy Protection Act and the FTC's COPPA Rule, 16 CFR Part 312
- **IEP / 504 plan:** individualized education program / Section 504 accommodation plan, shared by parents
- **MFA:** multi-factor authentication
- **Operator:** a person who runs a commercial website or online service that collects personal information from children (16 CFR 312.2)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-07-31 | Initial short-form plan | Owner-tutor |

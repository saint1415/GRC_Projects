# System Security Plan: Tutoring Operations Platform (TOP)

**Organization:** Cris Santos Company, LLC (K-12 tutoring and learning center) | **Tier:** Micro | **Vertical:** Educational Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-28

## 1. System Name and Identifier
Tutoring Operations Platform (**TOP**), identifier CSC-SYS-001.

## 2. System Overview
The TOP supports every function of the company's single Florida learning center: scheduling and enrollment, in-person and online tutoring, the district after-school program, assessments and progress reports, student intake records, and billing. It serves 7 employees, 14 contractor tutors, and about 420 students a year, about 250 of them under 13.

The company owns almost no infrastructure. Most of the TOP is vendor SaaS, and a managed service provider (MSP) runs the company's devices, network, and backup. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** tutoring and learning platform (vendor SaaS): student portal, online classroom with recording, session notes, assessments, progress reports, messaging, AI progress insights module
- **SYS-02:** scheduling, enrollment, and billing platform (vendor SaaS) with parent portal and integrated card payments
- **SYS-03:** productivity suite (SaaS): email, shared drive, calendar, video meetings
- **SYS-04:** 7 laptops, 1 front-desk desktop, 10 student tablets (MSP-managed)
- **SYS-05:** center network: firewall, staff Wi-Fi, student and guest Wi-Fi, one internet line (MSP-managed)
- **SYS-06:** SaaS-to-SaaS backup of suite email and the shared drive (operated by the MSP)
- **SYS-08:** public website with inquiry form and online privacy notice (website builder SaaS)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N61-R03 | COPPA Rule (2025 amendments) | 15 U.S.C. 6501-6506; 16 CFR Part 312. Amended rule 90 FR 16918 (Apr. 22, 2025), effective June 23, 2025; compliance date April 22, 2026. Section 312.8(b) requires a written information security program; this SSP is part of it |
| N61-R01 | FERPA, through the district contract only | 34 CFR 99.31(a)(1)(i)(B) (contractor as school official, under the district's direct control) and 99.33(a) (no redisclosure; use only for the purpose of the disclosure). Applies to the 90 district program students' data |
| Contract | District data privacy agreement | 48-hour incident notice; deletion within 60 days after the contract ends; district audit right |
| State | Florida Information Protection Act | Fla. Stat. 501.171: reasonable measures (2), breach notice (3)-(6), disposal (8) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable:
- GLBA Safeguards Rule (N61-R02): the company is not a Title IV institution and offers no financing to families.
- FERPA as a regulated institution: the company receives no funds under a Department of Education program (34 CFR 99.1).
- CIPA (N61-R04): not an E-Rate recipient. HIPAA (N61-R05): not a covered entity.
- CIRCIA (N61-R06): proposed only, and the proposed criteria (education agencies with 1,000 or more students, Title IV institutions, or entities above the SBA size standard) would not reach the company.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-08-28.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-28 the Owner accepted continued operation of the TOP, on the condition that the POA&M items in P07 are completed by their dates, the three High risks in P01 are treated by 2026-12-31, and the AI progress insights module stays off until the P10 conditions are met.

### 4.3 System Operational Status
Operational. Planned changes by 2026-12-31: MFA enforcement in the tutoring platform and on all administrator logins (P01 R-003), backup upgrade and restore tests (R-010), Wi-Fi segmentation (R-014), retention purge (R-007), suite alerting and EDR (R-001, R-002).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner | Overall accountability; accepts Moderate risk; approves this plan, policies, and spending |
| Information Security Coordinator (16 CFR 312.8(b)(1)) and privacy contact | Center Director | Runs the written information security program; maintains this plan, the risk register, the vendor folder, and the inventory; answers parents' privacy requests |
| Platform administrator and AI-001 owner | Director of Tutoring | Platform accounts, roles, and settings; district program coordinator; P10 owner |
| Scheduling and consent records | Enrollment and Billing Coordinator | Family accounts, enrollment agreements, consent records |
| IT operations | MSP | Devices, patching, antivirus, firewall, Wi-Fi, suite administration, backup |
| Independent assessor | Independent security consultant | Annual control assessment (P07) |

**Overlapping roles.** The Center Director runs most controls and also coordinates the program that checks them. The independent consultant's annual assessment (P07) and the Owner's monthly review are the compensating checks.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Education and training delivery (student work, session notes and recordings, assessments, progress reports, children's personal information) | Moderate | Moderate | Low | Disclosure of children's information and evaluation reports harms families and triggers breach duties; wrong assessment results could misplace a student; sessions can be moved or made up within a day (P05 MTD 24 h) |
| Customer services (family accounts, schedules, consent records, invoices) | Moderate | Moderate | Low | Parent contact and child details; consent records must be accurate; billing tolerates days (P05 MTD 120 h) |
| Human resources management (staff and contractor files) | Moderate | Low | Low | Screening results and payroll details in the shared drive |
| **TOP category (high-water mark)** | **Moderate** | **Moderate** | **Low** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person company, plus two controls from the SP 800-53B privacy baseline (PT-4 Consent and PT-5 Privacy Notice) because COPPA's notice and consent rules are the company's main regulatory duty. The plan documents 44 controls (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the tutoring platform vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the company controls or pays someone to control on its behalf:
- **Inside:** the company's tutoring platform tenant, its settings and roles (SYS-01); the scheduling platform account (SYS-02); the suite tenant and shared drive (SYS-03); 18 company devices (SYS-04); the center network (SYS-05); the backup subscription (SYS-06); the website account (SYS-08).
- **Outside (external services, interconnected):** the vendors' own platforms and data centers; the payment processor reached through SYS-02; the district's systems; the MSP's remote management platform; and **contractor tutors' personal computers (SYS-07)**. SYS-07 is outside the boundary because the company does not own or manage it, but it handles children's information, so AC-20 and POL-02 B.9 set the rules for it.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| School district | Inbound roster; outbound attendance and progress reports | Names, grade, teacher, assessment scores, accommodation notes for about 90 students | District contract and data privacy agreement (school official designation) |
| Payment processor (through SYS-02) | Outbound | Card payments entered by parents in hosted fields | Scheduling platform terms; no card data held by the company |
| Parents (SYS-02 parent portal, SYS-01 messaging, SYS-03 email) | Bidirectional | Schedules, invoices, progress reports, messages, documents parents upload | Enrollment agreement |
| Contractor tutors' computers (SYS-07) | Bidirectional | Online sessions, session notes; district rosters by email (**to stop under POL-02 B.9**) | Contractor agreement (**no security terms; gap**) |
| MSP remote management platform | Inbound administrative access | Device management | MSP service contract (**no security terms; gap**) |
| Platform AI progress insights module (AI-001) | Internal to SYS-01; vendor may use de-identified data for model improvement | Practice exercise results, attendance, session counts | **Unsigned data processing addendum (gap; P10)** |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Tutoring platform tenant (SYS-01) | SaaS | Tutoring platform vendor | Director of Tutoring |
| Scheduling and billing account (SYS-02) | SaaS | Scheduling platform vendor | Enrollment and Billing Coordinator |
| Suite tenant and shared drive (SYS-03) | SaaS | Productivity suite vendor | Center Director |
| Laptops (7), front-desk desktop (1), student tablets (10) (SYS-04) | Endpoint | Learning center; laptops travel with staff | Center Director (MSP operates) |
| Firewall, staff Wi-Fi, student and guest Wi-Fi (SYS-05) | Network | Network closet | Center Director (MSP operates) |
| Suite backup subscription (SYS-06) | SaaS | Backup vendor (MSP subcontractor) | Center Director (MSP operates) |
| Website and privacy notice (SYS-08) | SaaS | Website builder vendor | Center Director |

A complete device and data inventory does not exist yet (CM-8, due 2026-10-31).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 44 controls:
- Implemented: 9
- Partially implemented: 23
- Planned: 12
- Not applicable: 0

By responsibility: 21 system-specific (the company), 19 hybrid (the company with a vendor or the MSP), 4 common/inherited (fully provided by a SaaS vendor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Tutoring platform vendor | Platform security, encryption (SC-8, SC-28), backups (CP-9), session timeout (AC-12), lockout (AC-7), logging (AU-2) | SOC 2 Type 2 report reviewed 2026-08-18 (P09) | Complementary user entity controls: account provisioning and removal, role assignment, MFA enforcement, review of user access and export logs, retention settings |
| Scheduling platform vendor | Application security, hosted payment fields, encryption in transit, backups | Standard terms and documentation only (no SOC 2 report) | Account management; MFA on the administrator login when offered; weekly schedule export |
| Productivity suite vendor | Platform security, encryption at rest and in transit, lockout, logging | Vendor documentation | Account management, MFA settings, sharing and forwarding settings, alert configuration, log review |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), backup operation (CP-9), device lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: approve exceptions, read reports monthly, annual MSP security review (P01 R-013) |
| Backup service (MSP subcontractor) | Storage of suite copies (CP-9) | None yet; restore test due 2026-09-30 | Confirm through the MSP who the subcontractor is and its security terms (312.8(c)) |

**Inherited does not mean done.** Three of the platform vendor's complementary user entity controls are open gaps at the company: account removal (AC-2, PS-4), MFA enforcement (IA-2(1)), and retention settings (SI-12).

### 10.3 Control assessment status
Assessed 2026-08-03 to 2026-08-05 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the suite with a password and a second factor (phone authenticator app). The same is required for the tutoring platform, the scheduling platform administrator, and every MSP-held administrator login by 2026-10-31 (POL-02 B.3). Children sign in to the student portal with a user name and password that the platform issues; younger children use a picture password on center tablets. Children's accounts give access only to their own work, so the company accepts single-factor sign-in for them. Parents use the scheduling platform's parent portal with its own sign-in, outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and platform vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **COPPA:** Children's Online Privacy Protection Act and the FTC's COPPA Rule (16 CFR Part 312)
- **DPA:** data privacy agreement (with the school district)
- **EDR:** endpoint detection and response
- **FERPA:** Family Educational Rights and Privacy Act (34 CFR Part 99)
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones
- **TOP:** Tutoring Operations Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-28 | Initial plan | Center Director (Information Security Coordinator) |

# System Security Plan: Student Information and Learning Platform (SILP)

**Organization:** Cris Santos Company, Inc. (PE-backed private, for-profit college) | **Tier:** Mid-Market | **Vertical:** Educational Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Student Information and Learning Platform (**SILP**), identifier CSC-SILP-01. The SILP is the college's major system. It comprises SYS-01, SYS-02, SYS-03, SYS-04, SYS-06, SYS-08, and SYS-14, plus the staff side of SYS-10 and SYS-11, in `../00_company-facts.md`.

## 2. System Overview
The SILP supports the college's core student business in the BIA (P05): registration and academic records, online and campus instruction, Title IV aid processing and disbursement, student accounts and credit balance refunds, and employer partner reporting. It serves 600 employees, about 7,800 current students, former students whose records the college retains, and Parent PLUS borrowers. It holds nearly all of the college's **customer information** under the FTC Safeguards Rule (16 CFR 314.2(d)), about 41,000 consumers, and most of its **education records** under FERPA.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Student information system (SIS) with the student self-service portal (registration, grades, transcripts, student accounts, refund direct-deposit setup) | Vendor SaaS; SOC 2 Type 2 |
| SYS-02 | Learning management system (LMS) with the proctoring (AI-005) and AI tutor (AI-004) integrations | Vendor SaaS; SOC 2 Type 2 |
| SYS-03 | Financial aid management system (FAMS) with the student aid portal | Vendor SaaS; SOC 2 Type 2 (Security only) |
| SYS-04 | Access to the Department of Education's student aid systems: SAIG mailbox on 3 workstations and 28 staff accounts for the Department's web-based systems | Department-operated; college workstations and accounts |
| SYS-06 | Identity provider with SSO, MFA, and conditional access | SaaS |
| SYS-08 | Cloud landing zone: security and identity, shared services, workloads (integration platform, data warehouse, employer partner portal, file services), and backup accounts | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-14 | SIEM operated by the MSSP | SaaS |
| SYS-10, SYS-11 (staff side) | Staff VLANs and firewalls at 3 campuses on SD-WAN; 780 staff and faculty endpoints | On-premises; college-managed |

The admissions CRM (SYS-05), email suite (SYS-07), ERP (SYS-09), campus safety systems (SYS-13), and the student-data vendors (SYS-15) connect to the SILP as external services (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the SILP |
|---|---|---|---|
| N61-R02 | FTC Safeguards Rule, applied to Title IV institutions through the PPA and enforced by FSA | 16 CFR Part 314 (elements in 314.4) | Primary control requirement; mapped in `control-implementation.csv` |
| N61-R01 | FERPA | 20 U.S.C. 1232g; 34 CFR Part 99 (99.31(a)(1)(ii) "reasonable methods"; 99.31(c) identity authentication; 99.32 recordkeeping) | Role design, portal authentication, disclosure records |
| Title IV | Administrative capability and separation of duties; fraud referral; record retention; third-party servicer contracts; SAIG Enrollment Agreement | 34 CFR 668.16(c), (g); 34 CFR 668.24; 34 CFR 668.25; SAIG Enrollment Agreement | Aid processing controls, servicer access, breach notice to FSA |
| Title IV | Credit balance refunds within 14 days | 34 CFR 668.164(h)(2) | Refund availability and fraud controls (IA-11) |
| HEA | Limits on use of FAFSA data and federal tax information | HEA section 483, as summarized in the FSA Handbook, Vol. 2, Ch. 7 | Data warehouse and AI-002 inputs (PT-3) |
| Clery Act | Emergency response and evacuation procedures | 34 CFR 668.46(g) | The emergency notification service depends on SILP identity and contact data |
| State | Breach notification in each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | State statutes | Notification (P08) |
| Contract | Employer partner agreements (2 require SOC 2 Type 2) | Contract | SOC 2 readiness (P09) |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable:
- **COPPA (N61-R03).** No online services directed to children under 13; the minimum age at admission is 17.
- **CIPA (N61-R04).** The college does not receive E-Rate discounts.
- **HIPAA Security Rule (N61-R05).** The college is not a covered entity. Counseling treatment records and student health records are excluded from protected health information (45 CFR 160.103).
- **CIRCIA (N61-R06).** Proposed only. The proposed rule would cover every Title IV institution regardless of size, so it is tracked in P03 and P08, not treated as a current obligation.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Information Officer (system owner) on 2026-09-17, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The college is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the SILP accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** President and Chief Executive Officer for High and Very High risks; Chief Information Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the audit committee receives POA&M status each quarter; the Qualified Individual's annual written report to the board (2026-10-22) covers this decision; re-decision by 2027-09-30 or after a major change.
### 4.3 System Operational Status
Operational. Major modifications planned:
- Step-up authentication for refund bank changes and student MFA by default (due 2026-11-30 and 2027-03-31)
- SIS, FAMS, and LMS audit logs into the SIEM (due 2027-01-31)
- Removal of ISIR-derived fields from the data warehouse (due 2026-11-30)
- IT disaster recovery plan and quarterly restore tests (from 2026-10-27)
- Campus 3 network segmentation (due 2027-03-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Information Officer | Accountable for the SILP; accepts Moderate risk; senior member directing and overseeing the Qualified Individual (16 CFR 314.4(a)(2)) |
| Authorizing official equivalent (High risk) | President and Chief Executive Officer | Accepts High risk; approves the risk appetite and budget |
| Oversight | Board of directors and its audit committee | Receives the Qualified Individual's written report (314.4(i)); quarterly cyber risk reporting |
| Qualified Individual | vCISO (part-time, consulting firm) | Oversees, implements, and enforces the program (314.4(a)); writes the annual board report |
| Security operations and GRC | Information Security Manager and 2 security analysts | Day-to-day control owner; vulnerability management; MSSP liaison; GRC |
| Data owner, education records | Registrar | FERPA compliance officer; SIS roles |
| Data owner, financial aid | Director of Financial Aid | FAMS, SAIG, and servicer oversight |
| Data owner, student accounts | Bursar | Refunds and payment plans |
| Data owner, online learning | Dean of Online Learning | LMS configuration and integrations |
| Compliance and privacy | Chief Compliance Officer | Title IV and FERPA compliance; breach determinations with counsel; vendor contracts |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP (service provider under 314.4(f)) | 24x7 EDR and SIEM monitoring |
| External operator | Financial aid third-party servicer (34 CFR 668.25) | Verification and default prevention within the FAMS |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Higher education (enrollment, grades, transcripts, academic activity) | Moderate | Moderate | Moderate | Disclosure for up to 7,800 current students is serious but not catastrophic to the college; wrong grades or enrollment status affect aid eligibility; registration runs on paper for about a day (P05 MTD 24 h) |
| Payments and student accounts (Title IV awards, disbursements, refunds, payment plans) | Moderate | Moderate | Moderate | SSNs, bank details, and tax data enable identity theft and refund fraud; wrong amounts cause Title IV liabilities; refunds have a 14-day deadline |
| Personal identity and authentication (staff and student identities) | Moderate | Moderate | Moderate | Account takeover is the main fraud path; identity loss stops online classes (P05 BP-02 MTD 12 h) |
| Human resources management (employee identities for provisioning) | Moderate | Low | Low | Account data; limited harm if briefly unavailable |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for breach investigations and the FTC discovery date |
| **SILP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Confidentiality was considered for High.** The SILP holds SSNs and financial data for about 41,000 consumers. The team kept Moderate because the harm, while serious for individuals, would not cause a severe or catastrophic loss of the college's mission capability, and the high-water mark already drives encryption, MFA, and monitoring. To compensate, the baseline adds the identity proofing and re-authentication controls in section 10.1.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the college's SIS, LMS, and FAMS tenant configurations, roles, and integrations;
- the identity provider tenant;
- all 4 cloud accounts and their workloads (integration platform, data warehouse, employer partner portal, file services, backups);
- the 3 SAIG workstations and the college's 28 Department system accounts;
- the staff VLANs, firewalls, and SD-WAN edges at 3 campuses;
- 780 staff and faculty endpoints;
- the college's SIEM tenant and its use cases.

**Outside the boundary (external services, interconnected):**
- the SIS, LMS, FAMS, and identity vendors' platforms;
- the cloud provider's infrastructure;
- the MSSP's platform;
- the Department of Education's systems;
- the admissions CRM, email suite, ERP, and emergency notification service;
- the third-party servicer, the bank, the payment plan vendor, and the proctoring and AI tutor vendors;
- lab computers (SYS-12) and campus safety devices (SYS-13) on their own VLANs at Campuses 1 and 2. At Campus 3 they share the staff network today, which is a boundary weakness (SC-7, AC-4).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Department of Education (SAIG and web systems) | Bidirectional | ISIRs in; origination, disbursement, and enrollment records out | PPA; SAIG Enrollment Agreement |
| Third-party servicer | Bidirectional (FAMS access; emailed spreadsheets) | Verification documents, awards, loan data | Servicer contract under 34 CFR 668.25. **No MFA or incident notice terms (gap)** |
| Bank | Outbound refund files; inbound returns | Refund payments, bank details | Bank agreement |
| Admissions CRM (SYS-05) | Inbound via integration platform | Admitted applicant records | Contract with FERPA school-official terms |
| ERP (SYS-09) | Inbound HR feed; outbound student billing summary | Employee identities; receivables | Contract |
| Employer partners (9) | Outbound via the partner portal and 4 file feeds | Enrollment, progress (with written consent), invoices | Partner agreements; **no interconnection terms for the 4 file feeds (gap, CA-3)** |
| Emergency notification service (SYS-13) | Outbound nightly | Names, phone numbers, emails | Contract; **no interconnection terms (gap)** |
| Proctoring vendor (AI-005) | Bidirectional (LTI) | Exam sessions, webcam video, flags | Contract with FERPA terms |
| AI tutor vendor (AI-004) | Bidirectional (LTI) | Student prompts and course content | **Card purchase; no FERPA terms (gap, P10)** |
| Website and portal assistant vendor (AI-003) | Bidirectional | Prospective and current student questions; SIS data for signed-in students | **Card purchase; no FERPA or security terms (gap, P10)** |
| MSSP | Inbound logs; remote response actions | Security logs | Contract; SOC 2 Type 2 |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SIS tenant and student portal | SaaS | SIS vendor | Registrar |
| LMS tenant and integrations | SaaS | LMS vendor | Dean of Online Learning |
| FAMS tenant and student aid portal | SaaS | FAMS vendor | Director of Financial Aid |
| SAIG workstations (3) | Endpoint | Campus 1 financial aid office | Director of Financial Aid |
| Identity provider tenant | SaaS | Identity vendor | Chief Information Officer |
| Integration platform (37 interfaces) | Virtual machines | Workloads account | Chief Information Officer |
| Data warehouse and AI-002 model | Managed database and analytics service | Workloads account | Director of Institutional Research |
| Employer partner portal | Containers behind a web application firewall | Workloads account | Director of Corporate Partnerships |
| File services | Managed file service | Workloads account | Chief Information Officer |
| Backup vault | Backup service with write-once retention | Backup account (second region) | Chief Information Officer |
| Network hub, cloud firewall, VPN, privileged access broker, log pipeline | Network and management services | Shared services account | Information Security Manager |
| Cloud identity federation, guardrails, posture management | Identity and policy services | Security and identity account | Information Security Manager |
| SD-WAN edges, campus firewalls, staff switches and Wi-Fi | Network | Campuses 1-3 | Chief Information Officer |
| Staff and faculty laptops and desktops (780) | Endpoint | Campuses and remote | Chief Information Officer |
| SIEM tenant | SaaS | MSSP | Information Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The SILP uses the NIST SP 800-53B **Moderate** baseline, tailored as follows:
- **Documented here: 115 controls** in `control-implementation.csv`. They cover every control that implements a Safeguards Rule element or a FERPA, Title IV, or Clery requirement in section 3, plus the Moderate controls that address the risks in P01 (portal account takeover, recovery, segmentation, vendor access, monitoring).
- **Selected by tailoring (added, 5):** PM-1, PM-2, and PM-9 (program plan, Qualified Individual, and board reporting under 314.3(a), 314.4(a), and 314.4(i)); CA-8 (annual penetration testing under 314.4(d)(2)(i)); and PT-3 (HEA limits on FAFSA data).
- **Emphasized by tailoring:** IA-11 (re-authentication for refund bank changes) and IA-12, IA-12(2), and IA-12(3) (identity proofing of online applicants), because account takeover and fraudulent applicants are the college's fraud paths (P01 R-005, R-006).
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17), and platform-level SA and SC controls. These are inherited from the SIS, LMS, FAMS, identity, and cloud providers and the MSSP, evidenced by their SOC 2 Type 2 reports, which are reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** other Moderate controls with no regulatory mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the college develops only integration scripts and the partner portal; the portal's development practices are covered under SA-4 and 314.4(c)(4)). They are recorded as tailoring decisions and reviewed yearly.

**Status of the 115 documented controls:**
| Status | Count |
|---|---|
| Implemented | 36 |
| Partially implemented | 70 |
| Planned | 9 |
| Not applicable | 0 |

**Inheritance of the 115 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 77 | College |
| Hybrid | 30 | SIS, LMS, FAMS, and identity vendors; cloud provider; MSSP |
| Common/Inherited | 8 | Identity vendor (AC-2(1), AC-7, IA-2(1), IA-2(8)); cloud provider (CP-6, SC-12, SC-13); MSSP (IR-7) |

The Partially implemented and Planned statements trace to the 12 gaps in `../00_company-facts.md` section 4 and to the P07 findings.

**CSF 2.0 mapping.** The `csf2_subcategories` column takes up to 3 subcategories from the NIST CSF 2.0 to SP 800-53 crosswalk in `00_universal-framework/crosswalks/`. Where the crosswalk has no entry for a control enhancement, the parent control's mapping is used (13 rows). Where it has no entry for a base control, the subcategories are an author mapping (13 rows: AC-11, AC-21, CA-6, CP-3, IR-2, MA-4, MP-6, PL-4, PS-3, PS-4, PS-5, PS-8, PT-3).

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 32 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Staff and faculty.** All authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. Given the Moderate categorization and remote access to customer information, this meets 16 CFR 314.4(c)(5) for these users.
- **Administrators.** Cloud administrators use separate privileged identities through the access broker. SaaS administrators will move to separate accounts and phishing-resistant authenticators (FIDO2 security keys) by 2027-03-31 (P01 R-009).
- **Students.** Students use SSO for the portal and LMS. MFA is optional today (54% enrolled), and refund bank changes need only a password. **This does not meet 314.4(c)(5)**, and the Qualified Individual has not approved equivalent controls in writing. The plan: step-up MFA for refund bank changes by 2026-11-30, then MFA by default for all students by 2027-03-31 (P01 R-005; POAM-001).
- **Third-party servicer and partners.** The servicer's 8 FAMS accounts and the employer partner portal users have no MFA (POAM-003, POAM-019).
- **Applicants.** Online applicants are identity-proofed by admissions staff, with document and liveness verification planned for the January 2027 start (IA-12(3); 34 CFR 668.16(g)).
- **Department systems.** Access to the Department's systems uses Department-issued credentials governed by the Department, outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); WISP (2023, updated 2025).

## 13. Acronym List and Glossary
- **FAMS:** financial aid management system
- **FERPA:** Family Educational Rights and Privacy Act
- **FSA:** Federal Student Aid, an office of the U.S. Department of Education
- **ISIR:** Institutional Student Information Record (FAFSA results sent to the college)
- **LMS:** learning management system
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **POA&M:** plan of action and milestones
- **PPA:** Program Participation Agreement
- **SAIG:** Student Aid Internet Gateway
- **SILP:** Student Information and Learning Platform
- **SIS:** student information system
- **WISP:** written information security program

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Information Security Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Information Officer | vCISO (Qualified Individual) |

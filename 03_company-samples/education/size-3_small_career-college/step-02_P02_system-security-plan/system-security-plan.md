# System Security Plan: Student Information and Financial Aid Platform (SIFAP)

**Organization:** Cris Santos Company, LLC (private career college) | **Tier:** Small | **Vertical:** Educational Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-21

## 1. System Name and Identifier
Student Information and Financial Aid Platform (**SIFAP**), identifier CSC-SYS-001.

## 2. System Overview
The SIFAP supports the college's core student business: enrollment and registration, academic records and transcripts, federal student aid (Title IV) processing, student accounts, and credit balance refunds. It serves 60 staff, about 900 current students, and former students whose records the college retains. It is where the college keeps nearly all of its **customer information** under the FTC Safeguards Rule (16 CFR 314.2(d)) and most of its **education records** under FERPA.

**Major components:**
- **SYS-01:** a SaaS student information system (SIS) with the student self-service portal
- **SYS-03:** a SaaS financial aid management system (FAMS) with the student-facing financial aid portal
- **SYS-04:** the college's access to the Department of Education's student aid systems: the SAIG mailbox on 2 dedicated workstations and staff accounts for the Department's web-based systems
- **SYS-06:** an identity provider for single sign-on and MFA
- **SYS-08:** a public-cloud tenant hosting the integration server, the reporting database, the financial aid and business office file server, and the backup vault
- **SYS-09 and SYS-10 (staff side):** the campus staff network, firewall and VPN, and 70 staff endpoints

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N61-R02 | FTC Safeguards Rule, applied to Title IV institutions through the Program Participation Agreement and enforced by FSA | 16 CFR Part 314 (elements in 314.4) |
| N61-R01 | FERPA | 20 U.S.C. 1232g; 34 CFR Part 99 (99.31(a)(1)(ii) "reasonable methods"; 99.32 recordkeeping) |
| Title IV | Administrative capability; record retention; SAIG Enrollment Agreement | 34 CFR 668.16(c); 34 CFR 668.24; SAIG Enrollment Agreement |
| HEA | Limits on use of FAFSA data and federal tax information | HEA section 483, as summarized in the FSA Handbook, Vol. 2, Ch. 7 |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- COPPA (N61-R03): no users under 13.
- CIPA (N61-R04): the college does not receive E-Rate discounts.
- HIPAA (N61-R05): the college is not a covered entity. Health records of students (immunizations for clinical placements) are education records under FERPA.
- CIRCIA (N61-R06): proposed only. The proposed rule would cover every Title IV institution regardless of size, so it is tracked in P03 and P08.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Campus President on 2026-08-21.
### 4.2 System Authorization Decision
The college is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The Campus President accepted operation of the SIFAP on 2026-08-21, with the conditions in the P07 POA&M.
- The Board chair approved the High-risk treatment plans in P01 on 2026-08-21.
### 4.3 System Operational Status
Operational. Major modifications planned: backup redesign (P01 R-019) due 2026-12-31, and removal of FAFSA and tax fields from the reporting database (R-022) due 2026-10-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Campus President | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Board chair (majority owner) | Acceptance of High and Very High risks |
| Qualified Individual | IT Director | Oversees and enforces the information security program (16 CFR 314.4(a)); reports to the Board in writing at least annually (314.4(i)) |
| Data owner, education records | Registrar | FERPA compliance; SIS roles |
| Data owner, financial aid | Director of Financial Aid | FAMS, SAIG, servicer oversight |
| Operations support | 2 IT technicians | Endpoint, network, and account administration |
| External operator | Financial aid servicer | Administers the student-facing aid portal within FAMS |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Higher education (enrollment, grades, transcripts) | Moderate | Moderate | Moderate | Disclosure harms students and is a FERPA issue; wrong grades or enrollment status affect aid eligibility; registration can run on paper for about a day (P05 MTD 24 h) |
| Payments and student accounts (Title IV awards, disbursements, refunds) | Moderate | Moderate | Moderate | SSNs and tax data enable identity theft; wrong amounts cause Title IV liabilities; credit balance refunds have a 14-day deadline (34 CFR 668.164(h)(2)) |
| Personal identity and authentication (staff and student identities) | Moderate | Moderate | Low | Account data; limited harm if briefly unavailable |
| **SIFAP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person college. The plan documents 62 controls that implement the Safeguards Rule elements and the FERPA access requirement (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems.

Four controls outside the Moderate baseline were added by tailoring because the Safeguards Rule calls for them: PM-2 (Qualified Individual), PM-9 (risk strategy and Board reporting), CA-8 (annual penetration testing, 314.4(d)(2)(i)), and PT-3 (HEA limits on FAFSA and tax data). The `csf2_subcategories` column is filled from the NIST CSF 2.0 to SP 800-53 crosswalk in `00_universal-framework/crosswalks/`; it is blank where that crosswalk lists no reference for the control.

## 7. Authorization Boundary Description
The boundary contains college-managed components and the college's configuration of vendor services:
- **Inside:** the SIS and FAMS tenant configurations and roles, the identity provider tenant, the cloud tenant (3 workloads and the backup vault), the 2 SAIG workstations and the college's Department system accounts, the campus firewall, VPN, and staff VLAN, and 70 staff endpoints.
- **Outside (external services, interconnected):** the SIS and FAMS vendors' platforms, the cloud provider's infrastructure, the Department of Education's systems, the LMS (SYS-02), the admissions CRM (SYS-05), the email suite (SYS-07), and the financial aid servicer (SYS-12). Lab computers (SYS-11) sit on a separate VLAN outside the boundary; the firewall between them is a boundary control (SC-7).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Department of Education (SAIG) | Bidirectional | ISIRs in; enrollment and disbursement records out | PPA; SAIG Enrollment Agreement |
| LMS (SYS-02) | Bidirectional via integration server | Rosters out; attendance and final grades in | Contract with FERPA school-official clause |
| Admissions CRM (SYS-05) | Inbound via integration server | Admitted applicant records | Contract |
| Financial aid servicer (SYS-12) | Bidirectional (FAMS access; emailed spreadsheets) | Verification documents, awards | Third-party servicer contract. **No MFA or incident notice terms (gap)** |
| Email suite (SYS-07) | Outbound from staff | Aid spreadsheets to the business office and servicer | **Unencrypted (gap)** |
| Bank (refund processing) | Outbound | Refund payment files | Bank agreement |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SIS tenant and student portal | SaaS | SIS vendor | Registrar |
| FAMS tenant and student aid portal | SaaS | FAMS vendor | Director of Financial Aid |
| SAIG workstations (2) | Endpoint | Financial aid office | Director of Financial Aid |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| Integration server | Cloud virtual machine | Cloud tenant | IT Director |
| Reporting database | Managed database service | Cloud tenant | Director of Institutional Effectiveness |
| File server | Cloud virtual machine and file storage | Cloud tenant | IT Director |
| Backup vault | Cloud backup service | Cloud tenant (same account and region, **gap**) | IT Director |
| Campus firewall, VPN, core switches | Network | Campus server closet | IT Director |
| Staff laptops and desktops (70) | Endpoint | Campus and remote | IT Director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 62 controls:
- Implemented: 14
- Partially implemented: 35
- Planned: 12
- Not applicable: 1 (SA-11: the college develops no applications that handle customer information)

Inheritance: 45 system-specific, 14 hybrid, 3 common/inherited.

### 10.2 Control assessment status
Assessed 2026-07-27 to 2026-07-31. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
All staff authenticate through the identity provider with a password and a second factor (a phone authenticator app with push approval; hardware keys are planned for IT and financial aid administrators). This is appropriate for remote and privileged access to customer information at the Moderate categorization, and it meets 16 CFR 314.4(c)(5) for staff.

Two exceptions do not meet it today and are tracked in the POA&M: the financial aid servicer's local FAMS accounts, and students, for whom MFA is optional. Access to the Department's systems uses Department-issued accounts governed by the Department, outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), risk register (P01), gap analysis (P03), cloud control map (P04), BIA (P05), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor reviews (P09), AI assessment (P10), written information security program (2023, superseded in part by P06).

## 13. Acronym List and Glossary
- **FAMS:** financial aid management system
- **FERPA:** Family Educational Rights and Privacy Act
- **FSA:** Federal Student Aid, an office of the U.S. Department of Education
- **ISIR:** Institutional Student Information Record (FAFSA results sent to the college)
- **MFA:** multi-factor authentication
- **PPA:** Program Participation Agreement
- **SAIG:** Student Aid Internet Gateway
- **SIFAP:** Student Information and Financial Aid Platform
- **SIS:** student information system
- **WISP:** written information security program

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-21 | Initial plan | IT Director |

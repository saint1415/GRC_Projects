# System Security Plan: Student Records and Learning Platform (SRLP)

**Organization:** Cris Santos Company Holdings, Inc., Higher Education division (Cris Santos College, LLC), with platform services from the Education Software division and common controls from corporate shared services | **Tier:** Multi-Sector | **Vertical:** Educational Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the college's **Student Records and Learning Platform**, the registry's primary system (SIS and LMS), because it holds the college's education records and most of its GLBA customer information, it is the college's most critical system (P05 BP-HE01 to BP-HE03), and it shows the group's inheritance model at its most complex: controls come from **three places**, corporate common controls (SYS-G1 to SYS-G3), the Education Software division's Campus Platform (SYS-E1), and the college itself. Education Software keeps its own platform security documentation (its SOC 2 system description, P09), and Student Health keeps a division SSP for the clinic EHR that inherits from the same common control catalog.

## 1. System Name and Identifier
Student Records and Learning Platform (**SRLP**), identifier CSCH-HE-SRLP. It covers SYS-H1 in `../00_company-facts.md` plus the college integration hub and student data warehouse on SYS-G3.

## 2. System Overview
The SRLP is the college's system of record for students and the place where teaching happens online. It supports:
- **Registration and academic records** for about 410,000 enrolled students a year and about 2.3 million current and former student records (SIS).
- **Online and hybrid instruction** for about 295,000 online students (LMS).
- **Student financials:** student ledgers, Title IV disbursements, and credit balance refunds. This module holds customer information under 16 CFR 314.2.
- **Institutional reporting and student success analytics** through the student data warehouse.

About 22,000 workforce users (faculty, advisors, registrar, financial aid, student accounts, admissions, institutional research) and about 410,000 students use it. 14 service accounts run the integrations.

**Major components:**
- **SIS and LMS tenants** on the Campus Platform (SYS-E1), a multi-tenant SaaS run by the Education Software division in cloud provider B. The college configures roles, settings, and integrations; Education Software operates the platform.
- **Student financials module** (part of the SIS tenant)
- **Integration hub** in provider A: managed integration services connecting the SIS to the financial aid management system (SYS-H2), the admissions CRM (SYS-H3), the proctoring service (SYS-H5), and the clinic EHR enrollment checks (SYS-S1)
- **Student data warehouse** in provider A: object storage and a managed analytical database on the group data platform
- **Key management:** customer-managed keys for the hub and warehouse

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the SRLP |
|---|---|---|---|
| N61-R02 | FTC Safeguards Rule, applied to Title IV institutions through the PPA and enforced by FSA | 16 CFR Part 314 | Student financials and aid data are customer information. The college holds it on about 1.4 million consumers, so every element of 314.4 applies (314.6 exception not available). This plan is part of the written information security program (314.3(a)) |
| N61-R01 | FERPA | 20 U.S.C. 1232g; 34 CFR Part 99 | Education records in the SIS, LMS, and warehouse. "Reasonable methods" so school officials reach only records in which they have a legitimate educational interest (99.31(a)(1)(ii)); disclosure records (99.32); conditions for outsourced school officials such as Education Software and Student Health (99.31(a)(1)(i)(B)) |
| Title IV | Program Participation Agreement; SAIG Enrollment Agreement; 34 CFR 668.16(c); HEA sec. 483 | Program rules | Immediate breach notice to FSA; administrative capability; FAFSA data used only for aid administration |
| N62-R01, N62-R02 | HIPAA Security and Privacy Rules (Student Health only) | 45 CFR Part 164 | The SRLP is not a HIPAA system. It must not receive PHI of Student Health's nonstudent patients. The 2025 clinic utilization extract did (scenario gap 2; section 8) |
| N61-R06 | CIRCIA (proposed, not in force) | Proposed 6 CFR Part 226 | Tracked only. The proposed rule would cover every Title IV institution |
| N51-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | An SRLP incident may be material to the group (P08) |
| State law | State breach notification laws | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Online students live in all 50 states |
| Internal | Group policies POL-01 to POL-05 and the Higher Education supplement | P06 | |

Not applicable: COPPA (the college enrolls no children under 13); CIPA (no E-Rate funds); DFARS 252.204-7012 (no CUI). HIPAA does not apply to the college as an entity: it performs no covered functions.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the college chief information officer (system owner) and the College CISO (Qualified Individual) on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The college is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the college president and the Group CISO.
- **Conditions:** (1) purge nonstudent and contract-college clinic data from the warehouse by 2026-10-31 and keep the clinic utilization extract off until a redesigned, minimum-necessary feed is approved by the registrar and the Student Health Privacy Officer (POAM-006); (2) redesign warehouse roles around legitimate educational interest by 2027-03-31 (POAM-005); (3) sign a revised intercompany service agreement with Education Software, with safeguards, 72-hour incident notice, and a right to assess, by 2026-12-31 (POAM-009).
- **Reauthorization:** annually, or when a condition is completed.

### 4.3 System Operational Status
Operational. **Major modifications planned:** warehouse role redesign and purpose tagging (P01 HE-002), and migration of the 6 legacy campuses onto the SIS tenant by 2027-06-30 (P01 HE-005).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | College chief information officer | Accountable for the SRLP and this plan |
| Authorizing official equivalent | College president with the Group CISO | Authorization decision |
| Qualified Individual (16 CFR 314.4(a)) | College CISO | Oversees the college's information security program; reports to the college board of trustees |
| Data owner, education records | University registrar (FERPA compliance officer) | Approves access and disclosures |
| Data owner, aid and student financial data | Executive director of financial aid; college chief financial officer | Approve access to aid and ledger data |
| Data owner, warehouse content | Director of institutional research | Approves warehouse data sets and roles, with the registrar |
| Platform provider | Education Software chief technology officer | Operates the Campus Platform controls the college inherits (10 controls) |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group CISO (governance), Group HR director | Operate the 98 corporate common controls in `common-control-catalog.csv` |
| Independent assessor | Group internal audit | Assessed common controls once and sampled SRLP controls (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Education records (enrollment, grades, transcripts, advising) | **High** | Moderate | Moderate | Provisional Moderate, raised to High for aggregation: disclosure of about 2.3 million student records would have a severe effect (breach notices in every state, FSA and accreditor attention, SEC materiality) |
| Student financial assistance and student accounts (customer information) | **High** | Moderate | Moderate | SSNs, bank details, and aid data on about 1.4 million consumers. Integrity matters for payment fraud (bank detail changes) but is protected by reconciliation (SI-7) |
| Online instruction (course content, submissions, grades in progress) | Moderate | Moderate | Moderate | P05 BP-HE01: 8-hour MTD for online students |
| Information security (keys, roles, logs) | High | High | Moderate | Compromise would expose every data set |
| **SRLP category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **125 controls** in `control-implementation.csv`:
- 120 from the High baseline;
- 3 from the privacy baseline (PM-9, PT-2, PT-3), added because purpose limits on warehouse data are the system's main privacy risk;
- 2 program management controls not in any baseline (PM-1, PM-2).

Other High-baseline controls are either fully inherited from the cloud providers or the Campus Platform (for example, most PE controls, evidenced by SOC 2 reports) or tailored out with a reason in the group tailoring register.

The `csf2_subcategories` column uses the official CSF 2.0 to SP 800-53 Rev. 5 reference (`00_universal-framework/crosswalks/`). It is left blank for 13 controls that the official reference does not map (for example AC-21, PS-4, PT-3).

## 7. Authorization Boundary Description
- **Inside:** the college's SIS and LMS tenants with student financials (configuration, roles, data); the integration hub and student data warehouse accounts in provider A; their disaster recovery replica and backups in provider B.
- **Outside, inherited:** SYS-G1 identity, SYS-G2 SOC, the SYS-G3 landing zone (network hub, log archive, guardrails, keys), and the Campus Platform's shared infrastructure (SYS-E1: application code, multi-tenant database, platform identity service, warm standby).
- **Outside, interconnected:** SYS-H2 financial aid management system and SAIG, SYS-H3 admissions CRM, SYS-H5 proctoring service, SYS-S1 clinic EHR (enrollment and immunization checks), the legacy SIS at 6 campuses (SYS-H4, nightly loads until retirement).

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-E1 Campus Platform (Education Software) | Hosting | All SIS, LMS, and student financials data | Intercompany service agreement (2021). **No safeguards, notice, or assessment terms** (scenario gap 3; POAM-009) |
| SYS-H2 FAMS and SAIG | Two-way, nightly and on demand | ISIR data, awards, disbursements | FAMS vendor contract with safeguards and 72-hour notice; SAIG Enrollment Agreement |
| SYS-H3 admissions CRM | Inbound | Admitted applicants, application data | CRM vendor contract |
| SYS-H5 proctoring service | Two-way | Rosters, exam sessions, integrity flags | Proctoring vendor contract; FERPA school-official terms |
| SYS-S1 clinic EHR (Student Health) | Two-way | Enrollment status (outbound); immunization compliance status (inbound) | Clinic services agreement 2024 (school-official terms). **Gap:** the 2025 utilization extract (visit dates, clinic, and diagnosis categories) also flowed inbound to the warehouse, including nonstudent patients and contract-college students. Suspended 2026-08-07 (POAM-006) |
| Legacy campus SIS (SYS-H4) | Inbound nightly | Registration and grades for 6 campuses | Internal; ends at retirement (2027-06-30) |
| Transcript clearinghouse, lenders, employers | Outbound | Transcripts and verifications with consent or under 99.31 | Clearinghouse contract; disclosure records under 99.32 |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SIS and LMS tenants with student financials | SaaS (intercompany) | SYS-E1, provider B | College chief information officer (configuration); Education Software (platform) |
| Platform identity service for students | SaaS (inherited) | SYS-E1 | Education Software |
| Integration hub | PaaS (managed integration and workflow) | Provider A | College chief information officer |
| Student data warehouse | Object storage and managed analytical database (PaaS) | Provider A, group data platform | Group data platform director (operation); director of institutional research (content) |
| Key management | PaaS (customer-managed keys) | Provider A | Group cloud platform director |
| DR replica and immutable backups | Object storage and backup service | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (125 controls) and `common-control-catalog.csv` (98 corporate common controls).

| Status | Controls |
|---|---|
| Implemented | 104 |
| Partially implemented | 21 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **125** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from corporate, the cloud providers, or the Campus Platform) | 80 |
| Hybrid (a provider supplies the mechanism; the college configures or operates part) | 28 |
| System-specific | 17 |

| Provider of inherited and hybrid controls | Controls |
|---|---|
| Group security governance office | 31 |
| SYS-G1 Group identity platform | 21 |
| SYS-G3 Group cloud platform | 18 |
| SYS-G2 Group SOC, SIEM, and EDR | 16 |
| SYS-E1 Campus Platform (Education Software) | 10 |
| Group HR with SYS-G1 | 7 |
| Cloud providers A and B | 3 |
| Group internal audit | 2 |
| **Total** | **108** |

**The 21 partially implemented controls** cluster in four places:
- **Warehouse purpose limits** (scenario gap 2): AC-3, AC-4, AC-6, AC-21, PT-2, PT-3, CM-8, SI-12, AT-3.
- **Cross-tenant support access** (gap 1): AC-2, AU-6.
- **Service provider oversight of the Campus Platform** (gap 3): SA-4, SA-9, CA-3, IR-6.
- **Monitoring, credentials, and testing coverage:** AC-2(12), SI-4(4), IA-5, CA-8, CP-4, IR-3.

### 10.2 Inheritance from three providers
1. **Corporate common controls.** The common control catalog lists 98 controls. Inheritance is **documented for Higher Education** (2025 inheritance matrix), for Education Software (its SOC 2 system description carves in the group services), and for the SRLP (this plan). It is **not documented for Student Health** (scenario gap 4; POAM-016).
2. **Campus Platform controls.** Ten controls are inherited from SYS-E1 (for example AU-3, CP-7, SC-28, SA-8, IA-8). The college relies on Education Software's SOC 2 Type 2 report as evidence. Until 2026-08 no one at the college had read that report, and the intercompany agreement gives the college no right to assess or to be told of incidents (POAM-009).
3. **College controls.** Seventeen controls are system-specific, mostly roles, data flows, and purpose limits that only the college can decide.

### 10.3 Control assessment status
Common controls were assessed once, and SRLP and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with MFA; **administrators** of the tenant, hub, and warehouse use phishing-resistant authenticators and just-in-time PAM elevation.
- **Students, applicants, and parent borrowers** authenticate through the platform identity service with MFA (required for students since 2025). Bank detail changes need a fresh MFA challenge and an out-of-band confirmation (SI-7).
- **Service accounts** should use workload identity. 14 integration accounts still use static secrets, 5 older than 1 year (POAM-002).
- **Education Software support engineers** reach the tenant through the support console with their SYS-G1 identity, but without a college approval or ticket link (POAM-001).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness and vendor reviews (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **FAMS:** financial aid management system
- **ISIR:** Institutional Student Information Record (FAFSA results sent to the college)
- **Legitimate educational interest:** the FERPA test a school official must meet to access a record (34 CFR 99.31(a)(1))
- **PPA:** Program Participation Agreement
- **Qualified Individual:** the person designated to oversee the GLBA information security program (16 CFR 314.4(a))
- **SAIG:** Student Aid Internet Gateway
- **SRLP:** Student Records and Learning Platform
- **Treatment records:** records on an eligible student made and used only for treatment (34 CFR 99.3); excluded from both "education records" and HIPAA PHI

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | College chief information officer |
| 1.0 | 2026-09-15 | Approved with authorization conditions | College CISO |

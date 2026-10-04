# Scenario facts: Cris Santos Company | Educational Services | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions, each a separate legal subsidiary, plus corporate shared services in the parent |
| Division 1: Higher Education (NAICS 611310), **focus of this scenario** | Cris Santos College, LLC: a private, for-profit, accredited multi-campus college. 22 campuses in 8 southeastern states plus online programs offered to students in all 50 states. About 410,000 enrolled students a year (about 115,000 on campus or hybrid, about 295,000 fully online), certificate to master's level. About 25,000 employees (faculty and staff). Participates in Title IV federal student aid under one Program Participation Agreement (PPA) and holds a Student Aid Internet Gateway (SAIG) Enrollment Agreement |
| Division 2: Education Software (NAICS 513210, sector 51 Information) | Cris Santos Learning Technologies, Inc.: multi-tenant SaaS sold to schools. The **Campus Platform** (student information system, learning management system, and student financials for colleges) serves about 900 colleges and universities, including Cris Santos College. The **District Platform** (K-12 student information system, learning management system, and family app) serves about 5,400 school districts. About 8,500 employees. Issues a SOC 2 Type 2 report each year |
| Division 3: Student Health (NAICS 621111, sector 62 Health Care and Social Assistance) | Cris Santos Student Health, LLC: 96 clinic sites. 22 student health and counseling clinics on Cris Santos College campuses, 58 clinics run under management contracts for 37 unaffiliated colleges and universities, and 16 community urgent care sites near campuses. About 6,500 employees. Bills health plans electronically, so it is a **HIPAA covered entity** (45 CFR 160.103). Acquired in 2024 |
| Corporate shared services | Identity, network, security operations, cloud and data platform, HR, finance, legal, internal audit. About 5,000 employees |
| Location | Headquartered in Florida. Campuses and clinics in 8 southeastern states; online students and software customers nationwide. **State law handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional). Not SBA-small (NAICS 611310 standard: $34.5 million; 13 CFR 121.201) |
| Title IV and GLBA | The college agreed in its PPA to comply with the FTC Safeguards Rule (16 CFR Part 314), enforced by Federal Student Aid (FSA Electronic Announcement GENERAL-23-09). It holds customer information on about **1.4 million consumers** (current and former aid recipients within the record retention period, plus parent borrowers), so the 16 CFR 314.6 exception for fewer than 5,000 consumers does not apply |
| FERPA | The college receives funds under Department of Education programs, so FERPA (34 CFR Part 99) applies to its education records, including records kept for it by Student Health and Education Software acting as school officials (34 CFR 99.31(a)(1)(i)(B)) |
| COPPA | The District Platform is used by children under 13 in about 4,100 districts, so Education Software is an **operator** under 16 CFR 312.2 (amended rule compliance date 2026-04-22) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board of directors; board risk committee | Group cyber and AI oversight; accepts Very High risks; receives the High-risk list each quarter |
| Board audit committee | Oversees group internal audit |
| Disclosure committee | SEC materiality decisions (Form 8-K Item 1.05) |
| Group CISO; Group Chief Risk Officer; Group Chief Privacy Officer; Group General Counsel | Group standards, group risk register, common controls, notification matrix |
| Group internal audit | Independent of the teams it assesses; assesses common controls once and samples division controls |
| College board of trustees | Governing body of Cris Santos College; receives the Qualified Individual's annual written report (16 CFR 314.4(i)) |
| College president; division presidents (Education Software, Student Health) | Accept Moderate risks for their divisions |
| College CISO | Higher Education security and compliance lead; **Qualified Individual** under 16 CFR 314.4(a), designated in writing in 2023 |
| University registrar | FERPA compliance officer; data owner for the student information system tenant |
| Executive director of financial aid | Owns the financial aid management system and SAIG access; FSA point of contact |
| Vice president of admissions; vice president of student success; director of institutional research | Own the admissions CRM, the student-success program, and the student data warehouse content |
| Education Software CISO | Education Software security and compliance lead; designated coordinator of the children's information security program (16 CFR 312.8(b)(1)) |
| Education Software chief product officer, chief technology officer, support director, privacy counsel | Product, platform, support access, customer commitments |
| Student Health security and compliance lead | Designated HIPAA Security Official of the covered entity |
| Student Health Privacy Officer; chief medical officer | HIPAA Privacy Official; clinical owner of the clinic EHR and AI tools |

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (workforce SSO, MFA, PAM, identity governance) | Corporate | Higher Education and Education Software fully federated. Student Health about 60% migrated (see SYS-S2) |
| SYS-G2 | Group SOC, SIEM, and EDR | Corporate | 24x7 |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic) and group data platform | Corporate | Hosts the college integration hub and the **student data warehouse** |
| SYS-H1 | College student information system (SIS) and learning management system (LMS) tenants, including student financials (student accounts, aid disbursement, refunds) | Higher Education | Runs as a dedicated tenant on SYS-E1 under a 2021 intercompany service agreement |
| SYS-H2 | Financial aid management system (FAMS) and access to Department of Education systems (SAIG mailbox, web systems) | Higher Education | FAMS is third-party vendor SaaS; SAIG transmissions run on 12 dedicated workstations at the central financial aid office |
| SYS-H3 | Admissions CRM and online application | Higher Education | Third-party vendor SaaS. Includes the AI applicant scoring feature in use since 2025 (P10) |
| SYS-H4 | Campus networks, labs, and the legacy SIS and file servers at 6 campuses acquired in 2023 | Higher Education | Legacy campuses migrate to SYS-H1 by 2027-06-30 |
| SYS-H5 | Online proctoring service | Higher Education | Third-party vendor SaaS with identity verification and AI flagging (P10) |
| SYS-E1 | Campus Platform (multi-tenant higher education SaaS) | Education Software | Cloud provider B. About 900 college customers, about 6.5 million student records |
| SYS-E2 | District Platform (multi-tenant K-12 SaaS and family app), including the AI tutoring assistant | Education Software | Cloud provider B. About 5,400 districts, about 22 million student users (about 8 million under 13) |
| SYS-E3 | Education Software support console and release pipeline | Education Software | The support console can read any customer tenant on SYS-E1 and SYS-E2 |
| SYS-S1 | Student Health clinic EHR and practice management system | Student Health | Vendor-hosted. Holds FERPA records of student patients and PHI of nonstudent patients |
| SYS-S2 | Student Health legacy identity domain and clinic file servers | Student Health | Inherited from the 2024 acquisition; migration to SYS-G1 and SYS-G3 in progress |

**SSP system (P02):** the *Student Records and Learning Platform (SRLP)*: Cris Santos College's SIS and LMS tenants with student financials (SYS-H1, hosted on SYS-E1), plus the college integration hub and student data warehouse on SYS-G3, with interfaces to SYS-H2, SYS-H3, SYS-H5, and SYS-S1. It inherits common controls from SYS-G1 to SYS-G3 and platform controls from SYS-E1.

## 4. Current security posture: defined group program, with gaps where divisions meet
**In place today:**
- Group policies aligned to CSF 2.0 and a common control catalog
- 24x7 group SOC with EDR on managed endpoints and servers
- PAM with just-in-time elevation for corporate, Higher Education, and Education Software administrators
- MFA for all workforce users federated to SYS-G1, and for all students on SYS-H1
- Quarterly access certification for federated systems
- Immutable backups in a separate cloud provider
- A Qualified Individual designated in writing (2023) and a written 314.4(i) report to the college board of trustees each year since 2024
- Annual Title IV compliance audit (no GLBA finding in the fiscal 2025 audit)
- Education Software SOC 2 Type 2 report (Security, Availability, Confidentiality) issued each year
- A COPPA children's information security program with a designated coordinator (312.8(b)), adopted before the 2026-04-22 compliance date
- SEC Reg S-K Item 106 disclosure in the annual report

**Gaps:**
1. **Support access across tenants.** Education Software support engineers hold standing read access to every customer tenant on SYS-E1 and SYS-E2, including the college's tenant, through the support console (SYS-E3). Access is not tied to a ticket or a time limit.
2. **Student data warehouse mixes divisions and purposes.** A clinic utilization extract added in 2025 sends Student Health visit data to the college's student data warehouse for the student-success model. It includes records of nonstudent patients (PHI) and of students of contracted colleges, and gives warehouse analysts access beyond any legitimate educational interest (34 CFR 99.31(a)(1)(ii); 45 CFR 164.502).
3. **Intercompany service provider oversight.** The college treats Education Software as an internal department. The 2021 intercompany service agreement has no safeguards, incident notice, or right-to-assess terms, and the college has never assessed the Campus Platform as a service provider (16 CFR 314.4(f)).
4. **Student Health integration.** Division standards still date from before the 2024 acquisition. About 40% of Student Health users sign in through the legacy identity domain (SYS-S2) without MFA for on-site clinical workstations, and common control inheritance is not documented for the division.
5. **College AI governance.** The admissions applicant scoring model has run since 2025 without bias testing, applicant notice, or a review against Colorado SB26-189 (effective 2027-01-01) for online applicants in Colorado.
6. **Education Software AI and COPPA.** The K-12 AI tutoring assistant launched as a pilot in 140 districts in January 2026 without a children's privacy review, a SOC 2 system description update, or district contract updates. Data from 212 former district customers is still retained past contract end, contrary to the written retention policy (312.10).
7. **Multi-regulator notification.** The notification matrix covers FSA, the FTC, HIPAA, customer contracts, state law, and the SEC, but it has never been exercised across divisions, and district contract notice terms vary.
8. **Legacy campuses.** The 6 campuses acquired in 2023 run a legacy SIS and file servers on flat networks with local administrator accounts. The 2026 penetration test covered the Campus Platform tenant but not these campuses (314.4(d)(2)).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | Ransomware with student record exposure spanning all three divisions: entry through a support engineer's session, data theft from the college's tenant and other Campus Platform customers, and encryption of the group data platform and Student Health clinic file servers |
| P09 | SOC 2 scoped per division: Education Software in scope (true service organization, both platforms); Higher Education and Student Health out of scope with reasons, plus a review of key vendors' SOC 2 reports for the college |
| P10 | Group AI governance program: group standards, division use cases, and the regulator-specific rules. Priority use cases: college admissions applicant scoring and student-success risk scoring (the registry default), the K-12 AI tutoring assistant, and clinic AI tools |
| Cloud | Shared corporate platform plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division BIAs and risk analyses |
| 2026-06-01 to 2026-07-31 | Regulatory gap analyses (evidence updated to 2026-08-28) |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-08-27 | Group AI council review |
| 2026-09-15 | Results to the board risk committee; deliverables approved |
| 2026-10-20 | Qualified Individual's annual written report to the college board of trustees (scheduled) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Registry defaults | The registry primary system (SIS and LMS) is kept as the SSP system, extended to the warehouse and integration hub because gap 2 sits there. The registry incident (ransomware with student record exposure) is kept and made to span divisions. The registry AI use case is split into two inventory entries (admissions scoring AI-001; student-success scoring AI-002) because they have different owners, tiers, and rules |
| FERPA and HIPAA for clinic records | Student Health runs the 22 campus clinics on behalf of the college and the 58 contract clinics on behalf of the contracting colleges. Records on those students are the institution's education records or treatment records under FERPA (34 CFR 99.3; 20 U.S.C. 1232g(a)(4)(B)(iv)) and are excluded from PHI (45 CFR 160.103). Records of nonstudent patients (employees, family members, community patients) and all patients at the 16 community urgent care sites are PHI. Source: HHS and ED Joint Guidance on FERPA and HIPAA (December 2019 update), questions 3 to 6 |
| HIPAA status | Student Health is a single covered entity (no hybrid designation needed: every component performs covered functions). The college and Education Software perform no covered functions and are not covered entities. Corporate shared services is a business associate of Student Health under an intercompany BAA signed 2024 |
| Student Health scale | About 310,000 student patients and about 190,000 nonstudent patients a year. Counseling services at the 22 campus clinics |
| Education Software scale | SOC 2 Type 2 period 2025-07-01 to 2026-06-30, report issued 2026-08-14. Standard contracts: 72-hour notice to customers of a security incident affecting their data. About 1,300 district contracts carry state-specific terms with shorter or different notice duties. No federal agency customers (FedRAMP not applicable) |
| AI tutoring assistant | Generative assistant for students in grades 3 to 12 in 140 pilot districts (about 410,000 student users, about 160,000 under 13). Uses a hosted large language model from a third-party model provider under a contract with zero-data-retention and no-training terms |
| Campus Platform and the college | The college tenant holds about 2.3 million student records (current and former). The student financials module holds customer information under 16 CFR 314.2 |
| Cloud | Provider A hosts the corporate landing zone, the group data platform (including the student data warehouse and college integration hub), and division corporate workloads. Provider B hosts SYS-E1 and SYS-E2 production, the group backup vault, and the data platform disaster recovery replica. SYS-S1 is vendor-hosted. SYS-H2, SYS-H3, and SYS-H5 are vendor SaaS |
| Out of scope by fact | No CUI or federal research contracts (DFARS 252.204-7012 does not apply). No E-Rate funding (CIPA does not apply). No 42 CFR Part 2 program. No students under 13 at the college. Tuition card payments use a hosted payment page and clinic copays use point-to-point encrypted terminals (PCI DSS noted only) |
| Revenue split (fictional) | Higher Education about $9.6 billion; Education Software about $5.8 billion; Student Health about $2.6 billion. Total about $18.0 billion |
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only |

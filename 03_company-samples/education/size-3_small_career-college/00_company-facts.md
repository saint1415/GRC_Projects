# Scenario facts: Cris Santos Company | Educational Services | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (operates a private, for-profit career college) |
| Business | Career college (NAICS 611310) offering certificate and associate degree programs in healthcare technician fields (medical assistant, pharmacy technician, patient care technician) and information technology (IT support, network and cybersecurity technician) |
| Location | Florida. One campus with classrooms, 5 computer and skills labs, and administrative offices. Online programs are offered only to Florida residents (a scenario choice that keeps state law to Florida) |
| Workforce | 60 employees: 24 faculty, 10 admissions representatives, 5 financial aid staff, 4 registrar and records staff, 6 student success advisors and career services staff, 3 IT staff, 8 administration and business office staff |
| Students | About 900 enrolled: about 600 in on-campus and hybrid healthcare programs, about 300 in online IT programs. Adult learners; no students under 13 |
| Revenue | $20.7 million a year in receipts (fictional). Under the SBA standard of $34.5 million for NAICS 611310, so SBA-small |
| Title IV | Participates in the federal student aid programs (Pell Grants and Direct Loans, including Parent PLUS). About 80% of students receive Title IV aid. Has a **Program Participation Agreement (PPA)** with the U.S. Department of Education and a **Student Aid Internet Gateway (SAIG) Enrollment Agreement**. Annual Title IV compliance audit by an independent auditor |
| Safeguards Rule status | Subject to the FTC Standards for Safeguarding Customer Information (16 CFR Part 314) through its PPA, enforced by Federal Student Aid (FSA Electronic Announcement GENERAL-23-09). The college maintains customer information on about **6,400 consumers** (current and former aid recipients within the record retention period, plus parent borrowers), so the 16 CFR 314.6 exception for fewer than 5,000 consumers **does not apply** |
| FERPA status | An institution that receives funds under a Department of Education program, so FERPA (34 CFR Part 99) applies to education records |
| Governance | Board of Managers (3 members) is the LLC's governing body; the majority owner (Cris Santos) chairs it |
| Not in scope | COPPA (no users under 13); CIPA (not an E-Rate recipient); HIPAA (the college is not a covered entity; student health records it holds, such as immunization records for clinical placements, are education records under FERPA); CUI or research data (none); payment cards (tuition card payments use a vendor-hosted payment page outside the systems below, noted only) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board of Managers (chaired by the majority owner) | Governing body for 16 CFR 314.4(i) reporting; the chair accepts High and Very High risks |
| Campus President | Executive owner of the program; accepts risk up to Moderate; signs policies |
| IT Director | **Qualified Individual** under 16 CFR 314.4(a), designated in writing in March 2024; leads 2 IT technicians |
| Director of Financial Aid | Owns the financial aid management system, SAIG access, and the servicer relationship; FSA point of contact |
| Registrar | FERPA compliance officer; data owner for the student information system |
| Director of Admissions | Owns the admissions CRM |
| Dean of Academic Affairs | Owns the learning management system; oversees program directors and faculty |
| Director of Student Success | Owns the early-alert program and advisor interventions (P10) |
| Director of Institutional Effectiveness | Owns the reporting database and configures the early-alert model |
| Business Office Manager | Student accounts, Title IV credit balance refunds, tuition payments |
| HR Manager | Onboarding, terminations, adjunct faculty contracts |
| Lab Coordinator | Lab computers in the 5 labs |
| Financial aid servicer (contracted third-party servicer) | Verification and packaging support; administers the student-facing financial aid portal within the financial aid management system |

## 3. Systems

| ID | System | Hosting | Holds customer information (16 CFR 314.2(d))? | Holds FERPA education records? | Notes |
|---|---|---|---|---|---|
| SYS-01 | Student information system (SIS): admissions records after enrollment, registration, grades, transcripts, student accounts ledger, student self-service portal | Vendor SaaS | Yes (student accounts, aid disbursements, SSNs) | Yes | System of record. Vendor provides a SOC 2 Type 2 report. Includes the vendor's student-success analytics module (AI-001) |
| SYS-02 | Learning management system (LMS): courses, assignments, grades in progress, attendance and activity records | Vendor SaaS | No (incidental only) | Yes | SSO for staff and students, but **adjunct faculty use local LMS accounts**. Vendor provides a SOC 2 Type 2 report |
| SYS-03 | Financial aid management system (FAMS) with the student-facing financial aid portal (document upload, award acceptance) | Vendor SaaS | Yes (ISIR data, tax and verification documents, awards) | Yes | Used by college staff (SSO with MFA) and by the contracted servicer (**local admin accounts without MFA**) |
| SYS-04 | Access to the Department of Education's student aid systems: the SAIG mailbox (ISIR downloads and data transmissions through Department-provided software on 2 dedicated financial aid workstations) and financial aid staff access to the Department's web-based systems (for example, NSLDS) with individually issued accounts | Department-operated; 2 college workstations | Yes | Yes | The Department's systems are outside the college boundary; the 2 workstations and the college's user accounts are inside it |
| SYS-05 | Admissions CRM: inquiries, applications, communications | Vendor SaaS | Limited (applicant financial information for aid estimates) | Only for admitted students | Includes the vendor's lead and applicant scoring feature (AI-002, not in use) |
| SYS-06 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | No | MFA required for all staff; **optional for students** |
| SYS-07 | Email and productivity suite (email, files, chat) | SaaS | Yes (incidental) | Yes (incidental) | Financial aid spreadsheets are emailed to the business office (see gaps) |
| SYS-08 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Yes | Three college-managed workloads: the integration server (nightly SIS, FAMS, LMS, and CRM data sync), the reporting database (copy of SIS and LMS data for reporting and the early-alert model), and the file server used by financial aid and the business office. Plus the backup vault |
| SYS-09 | Campus network | On-premises | In transit | In transit | Firewall with remote-access VPN, core switches, staff VLAN, lab VLAN, student and guest Wi-Fi |
| SYS-10 | Staff endpoints | On-premises and remote | Cached | Cached | 70 managed laptops and desktops, all with full-disk encryption and signature antivirus |
| SYS-11 | Lab computers | On-premises | No (by policy) | No | 150 PCs in 5 labs (3 IT labs, 2 healthcare skills labs). **One shared local administrator password on all 150**; IT students use a shared lab admin account for coursework |
| SYS-12 | Financial aid servicer | Vendor | Yes | Yes | Third-party servicer under contract; accesses SYS-03 |

**SSP system (P02):** the *Student Information and Financial Aid Platform (SIFAP)*: SYS-01, SYS-03, SYS-04, SYS-06, SYS-08, and the staff side of SYS-09 and SYS-10, with interfaces to SYS-02, SYS-05, and SYS-12.

## 4. Current security posture: partially compliant

**In place today:**
- A written information security program (WISP) adopted in 2023
- The IT Director designated in writing as the Qualified Individual (March 2024)
- A written risk assessment dated June 2024
- MFA for all staff through the identity provider (email, SIS, LMS, FAMS, CRM, cloud console, VPN)
- SIS, LMS, and FAMS contracts with confidentiality, security, and FERPA school-official clauses
- Vendor encryption at rest and in transit for the SaaS systems
- Full-disk encryption on all 70 staff endpoints
- Separate staff and lab VLANs; student and guest Wi-Fi isolated from staff systems
- Daily backups of the cloud tenant workloads (same account and region as production)
- Annual FERPA and security awareness training for staff
- Separation of duties between financial aid (awarding) and the business office (disbursing), as 34 CFR 668.16(c)(2) requires
- Annual Title IV compliance audit
- A cyber insurance policy with a breach hotline and a panel of breach counsel and forensic firms (used in P08)

**Missing or weak, found in the 2026 assessments:**
1. The Qualified Individual has never delivered a written report to the Board of Managers (16 CFR 314.4(i)).
2. The risk assessment is 2 years old (June 2024) and predates the online IT programs, the LMS migration, and the early-alert pilot (314.4(b)(2)).
3. The financial aid servicer's administrators of the student-facing financial aid portal sign in with local accounts and no MFA (314.4(c)(5)).
4. All 150 lab computers share one local administrator password, and IT students use a shared lab admin account (314.4(c)(1)).
5. Oversight of the SIS and LMS vendors is limited to contract terms. Their SOC 2 reports have never been requested or reviewed (314.4(f)(3)).
6. Financial aid staff export ISIR and award data to spreadsheets on the file server and email them to the business office and the servicer without encryption (314.4(c)(3)).
7. No penetration test has ever been performed. Vulnerability scans are run ad hoc, the last in 2025 (314.4(d)(2)).
8. No review of user activity logs in the SIS or FAMS, and no security monitoring (314.4(c)(8)).
9. The incident response plan is a two-page contact list. It does not address the seven elements of 314.4(h) or the FTC and FSA notices.
10. No retention and disposal schedule for customer information. Financial aid records are kept indefinitely (314.4(c)(6)).
11. No change management procedure for SIS, FAMS, or integration changes (314.4(c)(7)).
12. Cloud tenant backups share the production account and region and have never been restore-tested.
13. FERPA "reasonable methods": admissions representatives and all advisors can see every student's full SIS record, including financial aid holds (34 CFR 99.31(a)(1)(ii)); disclosures are logged inconsistently (99.32).
14. Students can change refund bank details in the SIS portal without MFA or out-of-band confirmation.
15. The early-alert model went into pilot without fairness testing, student notice, or a written human review rule (P10).
16. Eleven LMS accounts of former adjunct faculty were still active (found during P07 testing).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incident | Ransomware with exfiltration of student records, starting from a phishing email to a financial aid staff member |
| P09 SOC 2 | The college is not a service organization. (a) Security-only (CC1-CC9) readiness self-benchmark requested by the Board of Managers; (b) review of the SIS and LMS vendors' SOC 2 Type 2 reports |
| P10 AI | AI-001: student-success early-alert risk scoring (pilot in 2 programs since the May 2026 term). AI-002: admissions applicant scoring (feature available in the CRM, not approved) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

**Details added while completing P06 to P10:**
- The AI-001 pilot runs in the patient care technician (on campus) and IT support (online) programs, covering 214 students in the May 2026 term, with 2 pilot advisors. Its inputs include two ISIR-derived fields (Pell eligibility, first-generation status) and home ZIP code (P10).
- The financial aid servicer holds 6 local administrator accounts in the FAMS (P07, P08).
- The SIS vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31; the LMS vendor's covers the 12 months ending 2026-05-31. Both were reviewed on 2026-08-14 (P09).

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-17 | Risk assessment and gap analysis fieldwork |
| 2026-07-27 to 2026-07-31 | Control assessment fieldwork |
| 2026-08-21 | Deliverables approved by the Campus President; High-risk treatment plans approved by the Board chair |
| 2026-10-15 | First written Qualified Individual report to the Board of Managers (scheduled) |

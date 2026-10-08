# Scenario facts: Cris Santos Company | Educational Services | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed; board of directors with an audit committee; operates a private, for-profit college) |
| Business | Private, for-profit (proprietary) college (NAICS 611310), institutionally accredited. Certificate, associate, bachelor's, and master's programs in nursing and health sciences, business, information technology and cybersecurity, and criminal justice. Called "the college" in the deliverables |
| Location | Headquarters and Campus 1 in Florida (central administration, financial aid, registrar, student accounts, IT), Campus 2 and Campus 3 in Florida, and an online division. On-campus students live in Florida. Online students live in 41 states (about 55% in Florida) |
| Workforce | 600 employees: 150 full-time faculty, 120 adjunct faculty (part-time employees), and 330 staff (admissions 70, financial aid 28, registrar 14, student accounts 16, student success and advising 45, academic administration 40, online learning and instructional design 22, IT 26 including 3 security staff, campus safety 18, and HR, finance, legal, and other support 51) |
| Students | About 7,800 enrolled: 4,300 on-campus and hybrid (Campus 1 about 2,100, Campus 2 about 1,300, Campus 3 about 900) and 3,500 fully online. Adult learners; minimum age at admission is 17; no services directed to children |
| Revenue | About $100 million a year in receipts (fictional). Above the SBA size standard of $34.5 million for NAICS 611310 (13 CFR 121.201), so not SBA-small |
| Title IV | Participates in the federal student aid programs (Pell Grants and Direct Loans, including Parent PLUS). About 78% of students receive Title IV aid. Has a **Program Participation Agreement (PPA)** and a **Student Aid Internet Gateway (SAIG) Enrollment Agreement** with the U.S. Department of Education. Annual Title IV compliance audit by an independent auditor |
| Safeguards Rule status | Subject to the FTC Standards for Safeguarding Customer Information (16 CFR Part 314) through its PPA, enforced by Federal Student Aid (FSA Electronic Announcement GENERAL-23-09). Holds customer information on about **41,000 consumers** (current and former aid recipients within the record retention period, Parent PLUS borrowers, and tuition payment plan participants), so the 16 CFR 314.6 exception for fewer than 5,000 consumers **does not apply** |
| FERPA status | Receives funds under Department of Education programs, so FERPA (34 CFR Part 99) applies to education records |
| HIPAA status | **Not a covered entity.** The counseling and wellness center at Campus 1 (4 licensed counselors) does not bill for services. Its treatment records fall under the FERPA treatment records exclusion (34 CFR 99.3, "education records" (b)(4)), and HIPAA excludes both FERPA education records and those treatment records from protected health information (45 CFR 160.103, "protected health information" paragraph (2)(i)-(ii)). Nursing students' immunization and clinical clearance records are education records. Students on clinical rotations use hospital systems under the hospitals' own programs and the clinical affiliation agreements |
| Governance | Board of directors (7 members: 4 sponsor appointees, 2 independent directors, and the President and CEO). The audit committee (3 directors, chaired by an independent director) oversees cyber risk and internal audit |
| Not in scope | COPPA (no online services directed to children under 13); CIPA (not an E-Rate recipient); HIPAA (see above); CUI and export-controlled research (no sponsored research and no federal contracts, so the FAR reporting clauses do not apply); payment cards (tuition card payments use a vendor-hosted payment page and the payment plan vendor, noted only); no on-campus student housing (so the Clery missing student notification rule, 34 CFR 668.46(h), does not apply) |
| State law approach | Online students live in 41 states, so breach notification follows the law of each state where affected individuals reside. Florida (Fla. Stat. 501.171) is the worked example. The samples otherwise stay federal |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Board of directors | Governing body for 16 CFR 314.4(i): receives the Qualified Individual's written report at least annually; approves the risk appetite |
| Board audit committee | Quarterly cyber risk reporting; oversees the co-sourced internal audit |
| President and Chief Executive Officer | Accepts High risk; approves POL-01 and the security budget |
| Chief Information Officer (CIO) | Executive sponsor of the security program; SSP system owner; **senior member responsible for direction and oversight of the Qualified Individual (16 CFR 314.4(a)(2))**; accepts Moderate risk |
| Virtual CISO (vCISO, part-time, from a security consulting firm) | **Qualified Individual** under 16 CFR 314.4(a), designated in writing in January 2025; program strategy; written report to the board |
| Information Security Manager plus 2 security analysts (one is the GRC analyst) | Security operations, vulnerability management, MSSP liaison, GRC |
| Chief Compliance Officer | Title IV and FERPA compliance oversight; privacy; breach determinations with counsel |
| General Counsel | Legal advice; engages breach counsel through the cyber insurer |
| Chief Financial Officer | Student financial services (financial aid and student accounts) report to the CFO; cyber insurance |
| Provost and Chief Academic Officer | Academic owner of the LMS; faculty; AI in teaching (P10) |
| Vice President of Enrollment Management | Admissions and the admissions CRM; AI-001 owner |
| Vice President of Student Affairs | Student success, counseling and wellness, campus safety |
| Registrar | FERPA compliance officer; data owner for the student information system |
| Director of Financial Aid | Owns the financial aid management system, SAIG access (Primary Destination Point Administrator), and the third-party servicer relationship |
| Bursar | Student accounts, Title IV credit balance refunds, payment plans |
| Internal audit (co-sourced firm) | Annual IT audit; performs the P07 assessment |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring. A service provider under 16 CFR 314.4(f) |
| Financial aid third-party servicer (contracted) | Verification support and Direct Loan default prevention. A Title IV third-party servicer under 34 CFR 668.25 |

## 3. Systems
| ID | System | Hosting | Customer information (16 CFR 314.2(d))? | FERPA education records? | Notes |
|---|---|---|---|---|---|
| SYS-01 | Student information system (SIS): registration, grades, transcripts, student accounts ledger, refund direct-deposit setup, student self-service portal | Vendor SaaS | Yes | Yes | System of record. Vendor SOC 2 Type 2 |
| SYS-02 | Learning management system (LMS) for all modalities, with integrated tools (online proctoring AI-005, AI tutor AI-004) | Vendor SaaS | Incidental | Yes | Vendor SOC 2 Type 2. About 140 local accounts outside the identity provider (clinical preceptors, guest instructors, contractors) |
| SYS-03 | Financial aid management system (FAMS) with the student-facing financial aid portal | Vendor SaaS | Yes (ISIR data, verification documents, awards) | Yes | The third-party servicer's 8 accounts use local sign-in without MFA |
| SYS-04 | Access to the Department of Education's student aid systems: SAIG mailbox on 3 dedicated workstations at Campus 1, and 28 staff accounts for the Department's web-based systems | Department-operated; 3 college workstations | Yes | Yes | The Department's systems are outside the college boundary |
| SYS-05 | Admissions CRM: inquiries, applications, communications, applicant scoring (AI-001) | Vendor SaaS | Limited (aid estimates) | Only for admitted students | About 4,000 online inquiries a month |
| SYS-06 | Identity provider with single sign-on and MFA | SaaS | No | No | MFA required for staff and faculty; **optional for students (54% enrolled)** |
| SYS-07 | Email and productivity suite (staff and students) | SaaS | Incidental | Incidental | |
| SYS-08 | Cloud landing zone: 4 accounts (security and identity, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Yes | Yes | Workloads: integration platform, data warehouse (with the AI-002 model), employer partner portal, file services |
| SYS-09 | Finance and HR ERP (general ledger, accounts payable, payroll, HR) | Vendor SaaS | No | No | Employee data |
| SYS-10 | Campus networks at 3 campuses on SD-WAN | On-premises | In transit | In transit | Staff, lab, campus safety, and student and guest Wi-Fi VLANs at Campuses 1 and 2. **Campus 3 (opened 2024) is flat** |
| SYS-11 | Staff and faculty endpoints | Managed | Cached | Cached | 780 laptops and desktops with EDR and full-disk encryption |
| SYS-12 | Student lab and library computers | On-premises | No (by policy) | No | 950 computers (IT and cybersecurity labs, nursing simulation lab, libraries) |
| SYS-13 | Campus safety systems: door access control (64 controllers), CCTV (11 network video recorders), and a SaaS emergency notification service | On-premises and SaaS | No | Directory data | Emergency notification sign-in through SSO only; contact lists synced nightly from the SIS |
| SYS-14 | SIEM (MSSP-operated) | SaaS | Security logs | Security logs | Identity provider, email, firewall, cloud, and EDR logs. SIS, FAMS, and LMS logs are not collected |
| SYS-15 | About 90 third-party vendors with student data | Various | Some | Some | 68 contracts have FERPA school-official and security terms; the third-party servicer is one of them |
| SYS-16 | AI tools | Vendors and in-house | Some | Yes | AI-001 to AI-005 (section 5) |

**SSP system (P02):** the *Student Information and Learning Platform (SILP)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-06, SYS-08, and SYS-14, plus the staff side of SYS-10 and SYS-11, with interfaces to SYS-05, SYS-07, SYS-09, and SYS-13. Moderate baseline with tailoring.

## 4. Current security posture: a defined program with gaps in scale
**In place today:**
- A written information security program (WISP), adopted 2023 and updated 2025
- The vCISO designated in writing as Qualified Individual (January 2025), with the CIO as the senior overseer and a consulting contract that requires the firm to maintain its own security program (314.4(a)(1)-(3))
- An annual written risk assessment (last done July 2025)
- The first annual written Qualified Individual report to the board, delivered 2025-10-23
- MFA for all staff and faculty (SSO applications, VPN, cloud console)
- EDR on all managed staff endpoints and servers, monitored 24x7 by the MSSP, and a SIEM
- Quarterly authenticated vulnerability scans and an annual external penetration test (last November 2025)
- Immutable backups in a separate backup account
- Encryption at rest in the SaaS systems and the cloud; full-disk encryption on all staff endpoints
- Annual FERPA, Safeguards Rule, and security awareness training; quarterly phishing simulations
- Separation of duties between awarding aid and disbursing funds (34 CFR 668.16(c)(2))
- Annual Title IV compliance audit
- Emergency notification tested each year, as the Clery Act rule requires (34 CFR 668.46(g)(6))
- A cyber insurance policy with a breach hotline and panel counsel and forensic firms

**Missing or weak, found in the 2026 assessments:**
1. Student portal security: MFA is optional for students (54% enrolled), and refund direct-deposit changes in the SIS portal need only a password. Attackers took over 23 student accounts in the 2025-26 award year and diverted refunds.
2. Access management: access reviews are annual; about 140 local LMS accounts sit outside the identity provider; 46 data warehouse users see all student-level data; privileged access management covers only the cloud.
3. Third parties: 22 of about 90 vendors with student data lack FERPA school-official and security terms; SOC 2 reports are reviewed only at onboarding; the third-party servicer's 8 FAMS accounts have no MFA.
4. FAFSA-derived (ISIR) fields are copied into the data warehouse and used for the AI-002 model and enrollment marketing analytics, beyond the HEA use limits.
5. Recovery: there is no IT disaster recovery plan; the integration platform, data warehouse, and employer partner portal have never been restore-tested; the SIS vendor's stated recovery objectives do not meet the BIA.
6. Logging: SIS, FAMS, and LMS audit logs are not in the SIEM, and there is no routine review of user activity in the SIS or FAMS.
7. Campus 3 has a flat network (staff, lab, and campus safety devices together); 64 door controllers and 11 video recorders run unsupported firmware; the emergency notification console has no break-glass account.
8. Lab computers: 410 lab computers at Campuses 2 and 3 share one local administrator password, and the Campus 3 cybersecurity lab is not isolated.
9. AI governance: 5 AI tools were adopted by departments without a security, privacy, or bias review.
10. Policies (2023) have few supporting standards; there is no retention and disposal schedule for customer information; change management for the integration platform and SIS configuration is informal.
11. The 2023 incident response plan does not address the FTC notice (314.4(j)), the FSA notice, multi-state notification, or fraud referrals; the last tabletop was in 2024.
12. There is no documented process to refer suspected fraudulent applicants to the Department's Office of Inspector General (34 CFR 668.16(g)), and identity checks for online applicants are manual and inconsistent.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | **Two incident types:** (1) ransomware with student record exposure (registry default); (2) student identity fraud: account takeover with refund diversion and fraudulent online applicants. Integrated with crisis management and legal |
| P09 | Readiness for a SOC 2 Type 2 examination of the employer education services (Security, Availability, Confidentiality), requested by 2 hospital-system employer partners; plus a vendor SOC 2 review program |
| P10 | AI use-case portfolio: AI-001 admissions applicant scoring, AI-002 student-success early-alert scoring, AI-003 website and portal generative AI assistant, AI-004 LMS AI tutor (pilot), AI-005 online proctoring AI flags. The registry default ("AI admissions and student-success risk scoring") is covered by AI-001 and AI-002; a mid-market college runs several AI tools, so the portfolio adds the other three |
| Primary system | The registry default (SIS and LMS) is kept and widened into the SILP, because at this size the financial aid systems and the cloud landing zone share the same identity provider, integration platform, and data |
| Cloud | Multi-account landing zone, vendor-agnostic |
| Ownership | The README sets a private equity-backed, privately held corporation. A private nonprofit college cannot be owned that way, so the college is a proprietary (for-profit) institution. Title IV, the Safeguards Rule, and FERPA apply the same way. As a for-profit, the college is also within FTC Act Section 5 jurisdiction |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment (co-sourced internal audit) |
| 2026-09-17 | Results to the audit committee; deliverables approved by the CIO and the President and CEO |
| 2026-10-22 | Second annual written Qualified Individual report to the board (scheduled) |
| 2027-04-01 to 2027-09-30 | Planned SOC 2 Type 2 observation period (P09) |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Revenue split and terms | Online division about $38 million, Campus 1 about $30 million, Campus 2 about $19 million, Campus 3 about $13 million. About $400,000 of receipts per business day over about 250 business days. On-campus programs run 15-week semesters; online programs run 8-week terms with 6 starts a year |
| Title IV volume | About $64 million in Title IV funds disbursed per award year. About 9,000 Title IV credit balance refunds a year (about $14 million), concentrated in the first 3 weeks of each term |
| Refund fraud | In the 2025-26 award year, attackers used reused passwords to take over 23 student portal accounts, changed the refund bank details, and diverted $61,400 in credit balance refunds; $38,000 was recovered. The college repaid the affected students from its own funds |
| Applicant fraud | In fall 2025 admissions flagged 310 online applications as likely fraudulent (synthetic or stolen identities). 41 reached enrollment and 6 received a Pell disbursement before withdrawal. None was referred to the Office of Inspector General |
| Cyber insurance | $5 million aggregate limit, $150,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires notice through the carrier hotline before incident vendors are engaged |
| SaaS recovery commitments | SIS vendor SOC 2 system description: RTO 24 hours, RPO 4 hours. LMS vendor: RTO 6 hours, RPO 1 hour. FAMS vendor: Security-only SOC 2, no stated recovery objectives |
| Backups | Daily backups of the workloads account to the backup account in a second region, with 30-day write-once retention and separate administrator credentials |
| MSSP | 24x7 monitoring; the contract requires a call to the Information Security Manager within 30 minutes of a high-severity alert |
| Workforce activity | 142 terminations and 58 internal transfers in the 12 months to 2026-06-30; about 310 adjunct course assignments per term. The last access review was completed in February 2026. The June 2026 phishing simulation click rate was 9.4% |
| Employer partners | 9 employer partners sponsor about 640 students. They receive enrollment, progress (with student consent under 34 CFR 99.30), and invoices through the employer partner portal. Two hospital-system partners require a SOC 2 Type 2 report before their 2027-12-31 contract renewals |
| AI tools | AI-001 in production since 2025-09 for online inquiries; AI-002 built in-house by Institutional Research, in production for online students since 2026-01; AI-003 since 2026-03; AI-004 pilot in 40 general education course sections since 2026-05; AI-005 in use since 2023 (about 18,000 proctored exams a year) |
| Online students by state | About 1,925 online students live in Florida; the rest live in 40 other states, including about 240 in California and about 110 in Colorado (relevant to state AI and privacy laws in P10) |
| AI-003 signed-in mode | Suspended on 2026-07-22 after a gap analysis test showed it could return another student's account balance (P03, P10) |
| Campus safety | The last annual emergency notification test was 2026-02-11 (announced). The door access controllers and video recorders at Campus 3 share the staff network |
| Terminology | "Student Information and Learning Platform (SILP)" is the SSP system in P02, identifier CSC-SILP-01 |
| Additional role titles | Director of Institutional Research; Dean of Online Learning; Director of Student Success; Director of Campus Safety; Director of Corporate Partnerships; HR Director; Director of Marketing and Communications; Library Director; Campus Directors (Campuses 1-3); Director of Admissions Operations; Director of Counseling and Wellness |
| Other operating details | The SIS role catalog has 64 roles; 14 of the 90 student-data vendors are Tier 1 under the P09 tiering approach; the integration platform runs 37 scheduled interfaces |

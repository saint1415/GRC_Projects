# Scenario facts: Cris Santos Company | Educational Services | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed; board of directors with an audit committee; operates a private, for-profit college) |
| Business | Private, for-profit (proprietary) college (NAICS 611310), institutionally accredited. Certificate, associate, bachelor's, and master's programs in nursing and health sciences, business, information technology and cybersecurity, and criminal justice. Called "the college" in the deliverables |
| Location | Headquarters and Campus 1 in Florida (central administration, financial aid, registrar, student accounts, IT), Campus 2 and Campus 3 in Florida, and an online division. On-campus students live in Florida. Online students live in 41 states (about 55% in Florida) |
| Workforce | 600 employees: 150 full-time faculty, 120 adjunct faculty (part-time employees), and 330 staff (admissions 70, financial aid 28, registrar 14, student accounts 16, student success and advising 45, academic administration 40, online learning and instructional design 22, IT 26 including 3 security staff, campus safety 18, and HR, finance, legal, and other support 51) |
| Students | About 7,800 enrolled: 4,300 on-campus and hybrid (Campus 1 about 2,100, Campus 2 about 1,300, Campus 3 about 900) and 3,500 fully online (EV-055). Adult learners; minimum age at admission is 17; no services directed to children |
| Revenue | About $100 million a year in receipts (fictional; EV-053). Above the SBA size standard of $34.5 million for NAICS 611310 (13 CFR 121.201), so not SBA-small |
| Title IV | Participates in the federal student aid programs (Pell Grants and Direct Loans, including Parent PLUS). About 78% of students receive Title IV aid (EV-054). Has a **Program Participation Agreement (PPA)** and a **Student Aid Internet Gateway (SAIG) Enrollment Agreement** with the U.S. Department of Education (EV-048). Annual Title IV compliance audit by an independent auditor (EV-035) |
| Safeguards Rule status | Determined in the intake obligations register (N61-R02): subject to the FTC Standards for Safeguarding Customer Information (16 CFR Part 314) through its PPA, enforced by Federal Student Aid (FSA Electronic Announcement GENERAL-23-09). Holds customer information on about **41,000 consumers** (current and former aid recipients within the record retention period, Parent PLUS borrowers, and tuition payment plan participants; EV-056), so the 16 CFR 314.6 exception for fewer than 5,000 consumers **does not apply** |
| FERPA status | Determined in the intake obligations register (N61-R01): receives funds under Department of Education programs (EV-048), so FERPA (34 CFR Part 99) applies to education records |
| HIPAA status | **Not a covered entity**, determined in the intake obligations register (N61-R05). The counseling and wellness center at Campus 1 (4 licensed counselors) does not bill for services (EV-058). Its treatment records fall under the FERPA treatment records exclusion (34 CFR 99.3, "education records" (b)(4)), and HIPAA excludes both FERPA education records and those treatment records from protected health information (45 CFR 160.103, "protected health information" paragraph (2)(i)-(ii)). Nursing students' immunization and clinical clearance records are education records. Students on clinical rotations use hospital systems under the hospitals' own programs and the clinical affiliation agreements |
| Governance | Board of directors (7 members: 4 sponsor appointees, 2 independent directors, and the President and CEO). The audit committee (3 directors, chaired by an independent director) oversees cyber risk and internal audit |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): COPPA (no online services directed to children under 13); CIPA (not an E-Rate recipient); HIPAA (see above); CUI and export-controlled research (no sponsored research and no federal contracts, so the FAR reporting clauses do not apply); payment cards (tuition card payments use a vendor-hosted payment page and the payment plan vendor, noted only); no on-campus student housing (so the Clery missing student notification rule, 34 CFR 668.46(h), does not apply) (EV-055, EV-058, EV-059) |
| State law approach | Online students live in 41 states, so breach notification follows the law of each state where affected individuals reside. Florida (Fla. Stat. 501.171) is the worked example. The samples otherwise stay federal |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Board of directors | Governing body for 16 CFR 314.4(i): receives the Qualified Individual's written report at least annually; approves the risk appetite |
| Board audit committee | Quarterly cyber risk reporting; oversees the co-sourced internal audit |
| President and Chief Executive Officer | Accepts High risk; approves POL-01 and the security budget |
| Chief Information Officer (CIO) | Executive sponsor of the security program; SSP system owner; **senior member responsible for direction and oversight of the Qualified Individual (16 CFR 314.4(a)(2))**; accepts Moderate risk |
| Virtual CISO (vCISO, part-time, from a security consulting firm) | **Qualified Individual** under 16 CFR 314.4(a), designated in writing in January 2025 (EV-033); program strategy; written report to the board |
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
The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Customer information (16 CFR 314.2(d))? | FERPA education records? | Notes |
|---|---|---|---|---|---|
| SYS-01 | Student information system (SIS): registration, grades, transcripts, student accounts ledger, refund direct-deposit setup, student self-service portal | Vendor SaaS | Yes | Yes | System of record. Vendor SOC 2 Type 2 (EV-045) |
| SYS-02 | Learning management system (LMS) for all modalities, with integrated tools (online proctoring AI-005, AI tutor AI-004) | Vendor SaaS | Incidental | Yes | Vendor SOC 2 Type 2 (EV-045). About 140 local accounts outside the identity provider (clinical preceptors, guest instructors, contractors) (EV-009) |
| SYS-03 | Financial aid management system (FAMS) with the student-facing financial aid portal | Vendor SaaS | Yes (ISIR data, verification documents, awards) | Yes | The third-party servicer's 8 accounts use local sign-in without MFA (EV-010) |
| SYS-04 | Access to the Department of Education's student aid systems: SAIG mailbox on 3 dedicated workstations at Campus 1, and 28 staff accounts for the Department's web-based systems | Department-operated; 3 college workstations | Yes | Yes | The Department's systems are outside the college boundary (EV-013) |
| SYS-05 | Admissions CRM: inquiries, applications, communications, applicant scoring (AI-001) | Vendor SaaS | Limited (aid estimates) | Only for admitted students | About 4,000 online inquiries a month (EV-039) |
| SYS-06 | Identity provider with single sign-on and MFA | SaaS | No | No | MFA required for staff and faculty; **optional for students (54% enrolled)** (EV-001, EV-002) |
| SYS-07 | Email and productivity suite (staff and students) | SaaS | Incidental | Incidental | |
| SYS-08 | Cloud landing zone: 4 accounts (security and identity, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Yes | Yes | Workloads: integration platform, data warehouse (with the AI-002 model), employer partner portal, file services (EV-023) |
| SYS-09 | Finance and HR ERP (general ledger, accounts payable, payroll, HR) | Vendor SaaS | No | No | Employee data |
| SYS-10 | Campus networks at 3 campuses on SD-WAN | On-premises | In transit | In transit | Staff, lab, campus safety, and student and guest Wi-Fi VLANs at Campuses 1 and 2. **Campus 3 (opened 2024) is flat** (EV-016) |
| SYS-11 | Staff and faculty endpoints | Managed | Cached | Cached | 780 laptops and desktops with EDR and full-disk encryption (EV-014) |
| SYS-12 | Student lab and library computers | On-premises | No (by policy) | No | 950 computers (IT and cybersecurity labs, nursing simulation lab, libraries) (EV-015) |
| SYS-13 | Campus safety systems: door access control (64 controllers), CCTV (11 network video recorders), and a SaaS emergency notification service | On-premises and SaaS | No | Directory data | Emergency notification sign-in through SSO only; contact lists synced nightly from the SIS (EV-017, EV-018) |
| SYS-14 | SIEM (MSSP-operated) | SaaS | Security logs | Security logs | Identity provider, email, firewall, cloud, and EDR logs. SIS, FAMS, and LMS logs are not collected (EV-027) |
| SYS-15 | About 90 third-party vendors with student data | Various | Some | Some | 68 contracts have FERPA school-official and security terms; the third-party servicer is one of them (EV-043) |
| SYS-16 | AI tools | Vendors and in-house | Some | Yes | AI-001 to AI-005 (section 5; EV-057) |

**SSP system (P02):** the *Student Information and Learning Platform (SILP)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-06, SYS-08, and SYS-14, plus the staff side of SYS-10 and SYS-11, with interfaces to SYS-05, SYS-07, SYS-09, and SYS-13. Moderate baseline with tailoring.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the Safeguards Rule, FERPA, and the Title IV and Clery requirements** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-06-15 to 2026-07-02 | Intake: evidence requests, exports, walk-throughs at Campus 1 and Campus 3, inventories, obligations register |
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-07-27 to 2026-07-31 | 2026 policy revisions (POL-01 to POL-05), the standards index, and the P08 runbooks drafted from the gaps |
| 2026-08-03 to 2026-08-21 | Control assessment (co-sourced internal audit): operating tests of controls already in place; design review of the draft policies and runbooks |
| 2026-08-24 to 2026-09-11 | AI governance assessment (P10) |
| 2026-09-17 | Results to the audit committee; deliverables, policies, and runbooks approved by the CIO and the President and CEO |
| 2026-10-01 | 2026 policies take effect |
| 2026-10-22 | Second annual written Qualified Individual report to the board (scheduled) |
| 2027-03 (planned) | Follow-up assessment: operating effectiveness of the controls the 2026 policies and standards introduced, after at least one quarter of operation |
| 2027-04-01 to 2027-09-30 | Planned SOC 2 Type 2 observation period (P09) |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Revenue split and terms | Online division about $38 million, Campus 1 about $30 million, Campus 2 about $19 million, Campus 3 about $13 million. About $400,000 of receipts per business day over about 250 business days (EV-053). On-campus programs run 15-week semesters; online programs run 8-week terms with 6 starts a year (EV-055) |
| Title IV volume | About $64 million in Title IV funds disbursed per award year. About 9,000 Title IV credit balance refunds a year (about $14 million), concentrated in the first 3 weeks of each term (EV-054) |
| Refund fraud | In the 2025-26 award year, attackers used reused passwords to take over 23 student portal accounts, changed the refund bank details, and diverted $61,400 in credit balance refunds; $38,000 was recovered. The college repaid the affected students from its own funds (EV-038) |
| Applicant fraud | In fall 2025 admissions flagged 310 online applications as likely fraudulent (synthetic or stolen identities). 41 reached enrollment and 6 received a Pell disbursement before withdrawal. None was referred to the Office of Inspector General (EV-039) |
| Cyber insurance | $5 million aggregate limit, $150,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires notice through the carrier hotline before incident vendors are engaged (EV-047) |
| SaaS recovery commitments | SIS vendor SOC 2 system description: RTO 24 hours, RPO 4 hours. LMS vendor: RTO 6 hours, RPO 1 hour. FAMS vendor: Security-only SOC 2, no stated recovery objectives (EV-045) |
| Backups | Daily backups of the workloads account to the backup account in a second region, with 30-day write-once retention and separate administrator credentials (EV-026) |
| MSSP | 24x7 monitoring; the contract requires a call to the Information Security Manager within 30 minutes of a high-severity alert (EV-027) |
| Workforce activity | 142 terminations and 58 internal transfers in the 12 months to 2026-06-30; about 310 adjunct course assignments per term. The last access review was completed in February 2026. The June 2026 phishing simulation click rate was 9.4% (EV-003, EV-005, EV-040) |
| Employer partners | 9 employer partners sponsor about 640 students. They receive enrollment, progress (with student consent under 34 CFR 99.30), and invoices through the employer partner portal. Two hospital-system partners require a SOC 2 Type 2 report before their 2027-12-31 contract renewals (EV-049) |
| AI tools | AI-001 in production since 2025-09 for online inquiries; AI-002 built in-house by Institutional Research, in production for online students since 2026-01; AI-003 since 2026-03; AI-004 pilot in 40 general education course sections since 2026-05; AI-005 in use since 2023 (about 18,000 proctored exams a year) (EV-057) |
| Online students by state | About 1,925 online students live in Florida; the rest live in 40 other states, including about 240 in California and about 110 in Colorado (relevant to state AI and privacy laws in P10) (EV-055) |
| AI-003 signed-in mode | Suspended on 2026-07-22 after a gap analysis test showed it could return another student's account balance (P03, P10; EV-068) |
| Campus safety | The last annual emergency notification test was 2026-02-11 (announced). The door access controllers and video recorders at Campus 3 share the staff network (EV-016, EV-018, EV-050) |
| Terminology | "Student Information and Learning Platform (SILP)" is the SSP system in P02, identifier CSC-SILP-01 |
| Additional role titles | Director of Institutional Research; Dean of Online Learning; Director of Student Success; Director of Campus Safety; Director of Corporate Partnerships; HR Director; Director of Marketing and Communications; Library Director; Campus Directors (Campuses 1-3); Director of Admissions Operations; Director of Counseling and Wellness |
| Other operating details | The SIS role catalog has 64 roles; 14 of the 90 student-data vendors are Tier 1 under the P09 tiering approach; the integration platform runs 37 scheduled interfaces (EV-007, EV-024) |

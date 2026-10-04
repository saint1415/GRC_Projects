# Scenario facts: Cris Santos Company | Educational Services | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; operates a private, for-profit college) |
| Business | Publicly traded postsecondary education company (NAICS 611310). It owns and operates one accredited private, for-profit institution (called "the College" in these deliverables) offering certificate, associate, bachelor's, master's, and doctoral programs in nursing and health sciences, business, information technology, education, and criminal justice. Most students study online |
| Location | Headquartered in Florida. The College has one Title IV program participation agreement (one institution) with a main campus in Florida and 22 additional locations in Florida, Georgia, Texas, Arizona, North Carolina, and Ohio (23 campuses in total), plus an online division that enrolls students in all 50 states and DC. **State law is handled generically:** apply the law of each state where affected students reside, with Florida as the worked example |
| Workforce | 12,000 employees: 1,400 full-time faculty, 3,800 adjunct faculty (part-time employees on term contracts, mostly online), 2,100 enrollment advisors, 1,700 academic and student success advisors, 950 financial aid and student finance staff, 620 IT and security staff, and 1,430 campus operations, clinical placement, library, career services, and corporate staff |
| Students | About 285,000 enrolled: about 238,000 online and 47,000 at the 23 campuses. Adult learners (minimum age 17 at enrollment); no users under 13. About 3.4 million academic records of former students are kept permanently (transcripts) |
| Revenue | About $4.8 billion a year in receipts (fictional), about $13.2 million per calendar day. Not small under the SBA standard for NAICS 611310 ($34.5 million; 13 CFR 121.201) |
| Title IV | Participates in the federal student aid programs (Pell Grants and Direct Loans, including Parent PLUS). About 74% of students receive Title IV aid; about $3.2 billion of Title IV funds are disbursed each year. Has a **Program Participation Agreement (PPA)** and a **Student Aid Internet Gateway (SAIG) Enrollment Agreement** with the U.S. Department of Education. Annual Title IV compliance audit and audited financial statements by an independent auditor |
| Safeguards Rule status | Subject to the FTC Standards for Safeguarding Customer Information (16 CFR Part 314) through its PPA, enforced by Federal Student Aid (FSA Electronic Announcement GENERAL-23-09). The company maintains customer information on about **2.3 million consumers** (current students, former students within the record retention period, parent borrowers, and customers of institutional payment plans and a small institutional loan program), so the 16 CFR 314.6 exception for fewer than 5,000 consumers **does not apply** |
| FERPA status | An institution that receives funds under Department of Education programs, so FERPA (34 CFR Part 99) applies to education records. The company is also a school official for 14 partner institutions under the SL-2 service line (section 5) |
| HIPAA status | **Not a covered entity.** The College runs no health care component that bills electronically; nursing programs use simulation labs and external clinical sites. Student wellness counseling is provided by a contracted telehealth vendor; the College receives referral and utilization data, which are education records. PHI excludes health information in education records covered by FERPA (45 CFR 160.103). The employee group health plan is a separate covered entity handled by the benefits program and is outside these deliverables |
| SEC status | Publicly traded; not a smaller reporting company. Form 8-K Item 1.05 and Regulation S-K Item 106 apply. SOX IT general controls are tested annually for ERP, payroll, and the student billing and revenue systems |
| Not in scope | COPPA (no users under 13); CIPA (not an E-Rate recipient; E-Rate serves K-12 schools and libraries); CUI and federal contracts (none held; FAR clauses checked in P08); research data (no sponsored research). Payment cards: tuition card payments run through a payment processor's hosted pages under a separate PCI DSS program, noted only |
| Added at this size | SEC cybersecurity disclosure; SOX IT general controls; two service lines offered to other organizations (SL-1 and SL-2); multi-state operations; an enterprise AI portfolio with a governance committee |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Board of directors, with an audit committee and a risk and compliance committee ("board risk committee") | Cyber oversight (Item 106 disclosure). The board risk committee receives the **Qualified Individual's written report** (16 CFR 314.4(i)) and quarterly cyber reporting; the full board is briefed after it |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner and **Qualified Individual** under 16 CFR 314.4(a), designated in writing by the board risk committee in February 2024 |
| Director of Security Operations | Runs the 24x7 SOC (in-house, with managed security service provider overflow); incident commander |
| Chief Privacy Officer | Privacy program owner; FERPA compliance with the University Registrar; breach determinations |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment |
| Chief Compliance Officer | Regulatory compliance program, including Title IV compliance (second line with the GRC team) |
| General Counsel | Chairs the disclosure committee |
| GRC team (9), Security Operations Center, Internal Audit (in-house IT audit team) | Three lines model |
| Disclosure committee | Form 8-K Item 1.05 materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Student information system (SIS): commercial higher-education SIS, customer-managed on Cloud provider A. Modules: matriculated admissions records, registration, academic records and transcripts, degree audit, student financials (bursar), and financial aid (ISIR import, packaging, origination, disbursement) | System of record for about 285,000 active and 3.4 million former students. Holds customer information (SSNs, ISIR data, awards, bank details for refunds) and education records |
| SYS-02 | Learning management system (LMS): vendor SaaS, multi-tenant | The College's tenant (about 9,000 course sections per term) plus 14 partner institution tenants (SL-2). Contract RTO 24 hours |
| SYS-03 | Student portal and mobile app (company-built) | Cloud provider A managed containers. Registration, grades, account balance, aid offers, refund bank details |
| SYS-04 | Department of Education connections | Two SAIG transmission servers in Cloud provider A running Department-provided software; individually issued accounts for about 640 financial aid staff in the Department's web-based systems |
| SYS-05 | Identity platform: workforce SSO, MFA, privileged access management (PAM), identity governance; separate student identity tenant | MFA required for workforce. **Student MFA is optional** except for viewing aid offers |
| SYS-06 | Admissions CRM and enrollment marketing platform (SaaS) | About 1.6 million inquiries a year; includes the CRM vendor's inquiry and applicant scoring (AI-002) |
| SYS-07 | Data and analytics platform on Cloud provider B | Data lake, warehouse, and machine learning platform; hosts the company-built student-success risk model (AI-003). **Receives a nightly copy of ISIR-derived fields** (see gaps) |
| SYS-08 | Multi-cloud estate and colocation | Cloud provider A (SIS, portal, integration, SAIG servers), Cloud provider B (data platform, AI services), and one colocation data center in Florida hosting the legacy document imaging system, the contact-center telephony core, and an offline backup copy |
| SYS-09 | Enterprise network | SD-WAN for headquarters, 23 campuses, and 4 student support centers; campus Wi-Fi; network access control (NAC) at 18 of 28 sites |
| SYS-10 | Endpoints | About 15,500 workforce laptops and desktops; about 6,800 campus lab and classroom computers |
| SYS-11 | ERP, HR, and payroll (SaaS) | SOX-relevant; adjunct faculty contracts and pay |
| SYS-12 | Online proctoring and assessment platform (SaaS) | Webcam-proctored exams for online courses |
| SYS-13 | Campus safety systems | Physical access control at 23 campuses, a SaaS emergency notification service, CCTV |
| SYS-14 | Third parties | About 1,100 vendors; 260 handle student records or customer information. Includes a Title IV third-party servicer (verification support and default prevention), a tuition payment plan servicer, the LMS and CRM vendors, a contact-center overflow vendor, and the telehealth counseling vendor |
| SYS-15 | AI portfolio (16 use cases) | Governed by an AI governance committee formed in 2025 |

**SSP system (P02):** the *Student Records and Learning Platform (SRLP)*: SYS-01 (SIS, including the student financials and financial aid modules), the College's SYS-02 LMS tenant configuration, SYS-03, SYS-04, and the integration services that connect them, inheriting common controls from the identity platform, the Cloud provider A landing zone, security operations, the network, and endpoint engineering.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A mature program aligned to CSF 2.0 that serves as the written information security program (16 CFR 314.3(a))
- The CISO designated in writing as Qualified Individual; written reports to the board risk committee since 2024
- Annual enterprise risk assessment tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC with SIEM and endpoint detection and response (EDR)
- MFA for all workforce access; PAM for administrators; quarterly access certification for workforce accounts
- Immutable backups in separate accounts; annual disaster recovery tests for tier-1 systems
- Annual external penetration test and quarterly authenticated vulnerability scans
- Tiered third-party risk program
- Separation of duties between awarding aid and disbursing funds (34 CFR 668.16(c)(2))
- Annual SOC 2 Type 2 report for the SL-1 employer platform since 2024
- SEC Item 106 disclosure in the Form 10-K

**Targeted gaps:**
1. **Adjunct and partner identity lifecycle.** Adjunct accounts are disabled from a nightly HR contract feed that misses non-renewals between terms. Partner institutions administer their own faculty accounts in their LMS tenants with no attestation.
2. **Student account takeover and refund fraud.** Student MFA is optional, and refund bank details can be changed in the student portal with email confirmation only. 212 refund redirection cases (about $0.9 million) were confirmed in the 2025-26 award year. Synthetic-identity ("ghost student") applications target the online programs.
3. **Third-party oversight.** 37 of 260 vendors that handle student data have no current assurance review, and 19 legacy contracts lack Safeguards Rule (314.4(f)(2)) and FERPA direct-control terms.
4. **FAFSA-derived data in analytics.** ISIR-derived fields are copied nightly to the data platform (SYS-07) and used as model features and in marketing analytics, outside aid administration (HEA section 483 limits).
5. **AI.** 16 AI use cases, but only 10 have completed committee review. The admissions scoring feature (AI-002) runs in production with fairness testing done only by the vendor and no applicant notice.
6. **Materiality.** The materiality playbook does not cover Title IV consequences (FSA breach report, corrective action plan, administrative capability) and has not been exercised since the General Counsel and CFO changed in 2026.
7. **Legacy document imaging.** The colocation imaging system (about 14 million scanned aid verification and tax documents) runs an unsupported operating system with local accounts and sends no logs to the SIEM.
8. **FERPA reasonable methods at scale.** All 2,100 enrollment advisors can read the academic and account records of every student, not only their applicants (34 CFR 99.31(a)(1)(ii)).
9. **Recovery.** The SIS met its RPO but recovered in 11.5 hours against an 8-hour RTO in the 2026-04-25 DR test. The LMS contract RTO (24 hours) is longer than the BIA RTO for online instruction (8 hours).
10. **Retention.** SSNs and aid documents of former students are kept indefinitely; no secure disposal under 16 CFR 314.4(c)(6).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | The registry default system (SIS and LMS) fits this size. It is documented as one high-value system, the SRLP, because the SIS and the College's LMS tenant share identity, integration, and data |
| P08 | Ransomware with student record exposure (registry default, kept): ransomware with exfiltration of SIS extracts and scanned aid documents, including the **SEC materiality assessment and Form 8-K Item 1.05** step, the FSA breach report, the FTC notice, and a multi-state notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to other organizations. **SL-1 Workforce Education Services:** tuition-benefit programs for about 310 employer clients, with an employer portal for enrollment, progress (with student FERPA consent), and invoicing; SOC 2 Type 2 (Security, Availability, Confidentiality) since 2024. **SL-2 Online Program Services:** LMS tenant hosting, instructional design, 24x7 student technical support, and learning analytics for 14 partner institutions (about 41,000 partner students); first SOC 2 Type 2 requested |
| P10 | Enterprise AI portfolio (16 use cases) with the AI governance committee. The registry default use case is kept and split into the two inventory items it describes: AI-002 admissions inquiry and applicant scoring, and AI-003 student-success risk scoring, assessed together in full |
| Cloud | Multi-cloud (two public cloud providers, vendor-agnostic) with common controls; one colocation data center |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise BIA update, risk assessment, and gap analysis (GRC team, second line) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line) |
| 2026-09-10 | Results and the Qualified Individual's annual written report to the board risk committee |
| 2026-09-14 | SRLP SSP approved; conditional authorization decision |

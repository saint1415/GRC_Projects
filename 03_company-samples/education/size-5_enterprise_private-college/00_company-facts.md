# Scenario facts: Cris Santos Company | Educational Services | Enterprise

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

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
| Safeguards Rule status | Subject to the FTC Standards for Safeguarding Customer Information (16 CFR Part 314) through its PPA, enforced by Federal Student Aid (FSA Electronic Announcement GENERAL-23-09). The company maintains customer information on about **2.3 million consumers** (current students, former students within the record retention period, parent borrowers, and customers of institutional payment plans and a small institutional loan program), so the 16 CFR 314.6 exception for fewer than 5,000 consumers **does not apply**. Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (N61-R02; EV-056, EV-057) |
| FERPA status | An institution that receives funds under Department of Education programs, so FERPA (34 CFR Part 99) applies to education records. The company is also a school official for 14 partner institutions under the SL-2 service line (section 5). Determined in the intake obligations register (N61-R01; EV-056, EV-046) |
| HIPAA status | **Not a covered entity.** The College runs no health care component that bills electronically; nursing programs use simulation labs and external clinical sites. Student wellness counseling is provided by a contracted telehealth vendor; the College receives referral and utilization data, which are education records. PHI excludes health information in education records covered by FERPA (45 CFR 160.103). The employee group health plan is a separate covered entity handled by the benefits program and is outside these deliverables. Determined in the intake obligations register (N61-R05; EV-059, EV-061) |
| SEC status | Publicly traded; not a smaller reporting company. Form 8-K Item 1.05 and Regulation S-K Item 106 apply. SOX IT general controls are tested annually for ERP, payroll, and the student billing and revenue systems. Determined in the intake obligations register (SEC-8K-1.05, SEC-SK-106, SOX-404; EV-034, EV-031) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): COPPA (no users under 13); CIPA (not an E-Rate recipient; E-Rate serves K-12 schools and libraries); CUI and federal contracts (none held; FAR clauses checked in P08); research data (no sponsored research). Payment cards: tuition card payments run through a payment processor's hosted pages under a separate PCI DSS program, noted only |
| Added at this size | Rules decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): SEC cybersecurity disclosure; SOX IT general controls. Also: two service lines offered to other organizations (SL-1 and SL-2); multi-state operations; an enterprise AI portfolio with a governance committee |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Board of directors, with an audit committee and a risk and compliance committee ("board risk committee") | Cyber oversight (Item 106 disclosure). The board risk committee receives the **Qualified Individual's written report** (16 CFR 314.4(i)) and quarterly cyber reporting; the full board is briefed after it |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner and **Qualified Individual** under 16 CFR 314.4(a), designated in writing by the board risk committee in February 2024 (EV-028) |
| Director of Security Operations | Runs the 24x7 SOC (in-house, with managed security service provider overflow); incident commander |
| Chief Privacy Officer | Privacy program owner; FERPA compliance with the University Registrar; breach determinations |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment |
| Chief Compliance Officer | Regulatory compliance program, including Title IV compliance (second line with the GRC team) |
| General Counsel | Chairs the disclosure committee |
| GRC team (9), Security Operations Center, Internal Audit (in-house IT audit team) | Three lines model |
| Disclosure committee | Form 8-K Item 1.05 materiality decisions (General Counsel chairs) |

## 3. Systems
The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Notes |
|---|---|---|
| SYS-01 | Student information system (SIS): commercial higher-education SIS, customer-managed on Cloud provider A. Modules: matriculated admissions records, registration, academic records and transcripts, degree audit, student financials (bursar), and financial aid (ISIR import, packaging, origination, disbursement) | System of record for about 285,000 active and 3.4 million former students. Holds customer information (SSNs, ISIR data, awards, bank details for refunds) and education records |
| SYS-02 | Learning management system (LMS): vendor SaaS, multi-tenant | The College's tenant (about 9,000 course sections per term) plus 14 partner institution tenants (SL-2). Contract RTO 24 hours (EV-025) |
| SYS-03 | Student portal and mobile app (company-built) | Cloud provider A managed containers. Registration, grades, account balance, aid offers, refund bank details |
| SYS-04 | Department of Education connections | Two SAIG transmission servers in Cloud provider A running Department-provided software; individually issued accounts for about 640 financial aid staff in the Department's web-based systems |
| SYS-05 | Identity platform: workforce SSO, MFA, privileged access management (PAM), identity governance; separate student identity tenant | MFA required for workforce (EV-002). **Student MFA is optional** except for viewing aid offers (EV-007) |
| SYS-06 | Admissions CRM and enrollment marketing platform (SaaS) | About 1.6 million inquiries a year; includes the CRM vendor's inquiry and applicant scoring (AI-002) |
| SYS-07 | Data and analytics platform on Cloud provider B | Data lake, warehouse, and machine learning platform; hosts the company-built student-success risk model (AI-003). **Receives a nightly copy of ISIR-derived fields** (EV-065) |
| SYS-08 | Multi-cloud estate and colocation | Cloud provider A (SIS, portal, integration, SAIG servers), Cloud provider B (data platform, AI services), and one colocation data center in Florida hosting the legacy document imaging system, the contact-center telephony core, and an offline backup copy |
| SYS-09 | Enterprise network | SD-WAN for headquarters, 23 campuses, and 4 student support centers; campus Wi-Fi; network access control (NAC) at 18 of 28 sites (EV-015) |
| SYS-10 | Endpoints | About 15,500 workforce laptops and desktops; about 6,800 campus lab and classroom computers |
| SYS-11 | ERP, HR, and payroll (SaaS) | SOX-relevant; adjunct faculty contracts and pay |
| SYS-12 | Online proctoring and assessment platform (SaaS) | Webcam-proctored exams for online courses |
| SYS-13 | Campus safety systems | Physical access control at 23 campuses, a SaaS emergency notification service, CCTV |
| SYS-14 | Third parties | About 1,100 vendors; 260 handle student records or customer information (EV-041). Includes a Title IV third-party servicer (verification support and default prevention), a tuition payment plan servicer, the LMS and CRM vendors, a contact-center overflow vendor, and the telehealth counseling vendor |
| SYS-15 | AI portfolio (16 use cases) | Governed by an AI governance committee formed in 2025 |

**SSP system (P02):** the *Student Records and Learning Platform (SRLP)*: SYS-01 (SIS, including the student financials and financial aid modules), the College's SYS-02 LMS tenant configuration, SYS-03, SYS-04, and the integration services that connect them, inheriting common controls from the identity platform, the Cloud provider A landing zone, security operations, the network, and endpoint engineering.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. At this size the sources are enterprise systems of record across the College's administrative units, prior Internal Audit, SOX and Title IV compliance audit workpapers, regulator correspondence, and board and committee records.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv), reviewed by the General Counsel's office.
- **Gaps against the Safeguards Rule, FERPA, Title IV and the other applicable rules** are judged in the gap analysis (P03), and **whether controls work** is tested by Internal Audit in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | The registry default system (SIS and LMS) fits this size. It is documented as one high-value system, the SRLP, because the SIS and the College's LMS tenant share identity, integration, and data |
| P08 | Ransomware with student record exposure (registry default, kept): ransomware with exfiltration of SIS extracts and scanned aid documents, including the **SEC materiality assessment and Form 8-K Item 1.05** step, the FSA breach report, the FTC notice, and a multi-state notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to other organizations. **SL-1 Workforce Education Services:** tuition-benefit programs for about 310 employer clients, with an employer portal for enrollment, progress (with student FERPA consent), and invoicing; SOC 2 Type 2 (Security, Availability, Confidentiality) since 2024; Privacy is added for the 2027 period at employer clients' request. **SL-2 Online Program Services:** LMS tenant hosting, instructional design, 24x7 student technical support, and learning analytics for 14 partner institutions (about 41,000 partner students); first SOC 2 Type 2 requested |
| P10 | Enterprise AI portfolio (16 use cases) with the AI governance committee. The registry default use case is kept and split into the two inventory items it describes: AI-002 admissions inquiry and applicant scoring, and AI-003 student-success risk scoring, assessed together in full. The AI governance committee is chaired by the Provost and Chief Academic Officer and reports to the executive risk committee |
| Cloud | Multi-cloud (two public cloud providers, vendor-agnostic) with common controls; one colocation data center |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-05-29 | Intake: evidence requests, exports from systems of record, inventories, obligations register (reviewed by counsel) |
| 2026-06-01 to 2026-07-15 | Enterprise BIA update: interviews and dependency review |
| 2026-06-01 to 2026-07-31 | Enterprise risk assessment and gap analysis (GRC team, second line; gap analysis evidence sampling completed 2026-08-14) |
| 2026-06-22 to 2026-07-10 | 2026 annual revision of POL-01 to POL-05 and the policy hierarchy drafted from the intake evidence and early risk and gap results |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line): operating tests of controls in force under the 2025 policy set; design review of the draft 2026 revisions |
| 2026-09-10 | Results and the Qualified Individual's annual written report to the board risk committee; 2026 policy revisions approved (effective 2026-10-01) |
| 2026-09-14 | SRLP SSP approved; conditional authorization decision |
| 2027-03 (planned) | Internal Audit follow-up: operating effectiveness of the controls the 2026 revisions and POA&M items introduced, after at least one quarter of operation |

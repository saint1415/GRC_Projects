# Scenario facts: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded staffing and workforce solutions company; SEC registrant) |
| Business | Temporary help services (NAICS 561320) in four segments: **Commercial Staffing** (light industrial, warehouse, office and administrative; about 44% of revenue), **Professional Staffing** (IT, finance and accounting, and a Government Solutions unit that staffs federal and state agency contracts; about 28%), **Healthcare Staffing** (travel and per diem nurses and allied health clinicians placed at hospitals; about 16%), and **Workforce Solutions** (managed service provider programs on the firm's own vendor management platform, recruitment process outsourcing, and payrolling; about 12%) |
| Location | Headquartered in Florida. About 380 branch offices and 140 on-site offices at client facilities in 38 states and the District of Columbia. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | **12,000 internal employees** (recruiters, account managers, branch, payroll, associate service, and corporate staff). In addition, the firm is the W-2 employer of its **temporary associates**: about 78,000 on assignment in an average week, and about 310,000 different associates paid during 2025. Associates work under client supervision at client sites |
| Volumes | About 2.6 million applications a year; about 240,000 new associate hires a year (onboarding, Form I-9, E-Verify); about 190,000 employment background checks a year; about 9,500 active clients |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day. Associate gross payroll is about $3.4 billion a year, paid weekly (about $65 million per weekly payroll) |
| Size status | Not small. NAICS 561320 uses a receipts-based SBA standard of $34.0 million (13 CFR 121.201); the firm exceeds it by a wide margin |
| Employer status | Employer of record for associates: completes their Forms I-9, runs E-Verify, withholds taxes, and pays wages. For direct-hire referrals and recruitment process outsourcing the hiring client completes the Form I-9 |
| E-Verify | Enrolled under the E-Verify MOU for Employers and, because Government Solutions holds federal contracts with the FAR E-Verify clause (48 CFR 52.222-54), enrolled as a Federal contractor (MOU Art. II.B). Verifies all new hires in every state |
| HIPAA status | **Not a business associate** for clinician placements: travel and per diem clinicians work under the hospital's direct control, so they are part of the hospital's workforce (45 CFR 160.103, "workforce"), and the firm does not create, receive, maintain, or transmit PHI on a hospital's behalf. 37 hospital clients require business associate agreements by contract anyway; the firm treats those as contractual commitments (see section 7) |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; federal contracts with FAR 52.204-21 and 52.222-54; NYC Local Law 144 for NYC candidates; multi-state operations; growth by acquisition (2 staffing firms acquired in 2025-2026) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board (audit committee plus a risk and technology committee) | Cyber oversight (Item 106 disclosure); the risk and technology committee receives the risk register and assessment results |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner; reports to the Chief Information Officer with a direct line to the risk and technology committee |
| Chief Privacy Officer | Privacy program for candidates, associates, and internal staff; breach determinations with the General Counsel |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| General Counsel | Legal; chairs the disclosure committee; co-chairs the AI governance council |
| Senior Vice President, Payroll and Associate Services | Business owner of associate payroll, pay delivery, and the Associate Service Center |
| Vice President, Employment Compliance | Form I-9, E-Verify, FCRA background screening, and records retention compliance |
| GRC team (9), Security Operations Center (24x7, in-house plus MSSP overflow), Internal Audit (in-house) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Front-office platform: enterprise applicant tracking system (ATS) and client CRM (staffing-industry vendor SaaS) | Career sites, candidate profiles and resumes, job orders, recruiter workflow; about 2.6 million applications a year; AI ranking add-on (AI-001) |
| SYS-02 | Onboarding and electronic Form I-9 platform (vendor SaaS) | Tax and direct deposit forms, electronic Form I-9 with document images, background check ordering, E-Verify case data |
| SYS-03 | Staffing back-office payroll and billing engine (commercial staffing back-office software, customer-managed on Cloud provider A) | Weekly associate payroll (about $65 million), pay delivery files (ACH, paycard funding), client invoicing, tax files; SOX-relevant |
| SYS-04 | Time capture: associate mobile timekeeping app and client timesheet portal (vendor SaaS), client VMS time feeds, and badge and PIN time clocks at 140 on-site offices | Clock server for the time clocks runs in colocation DC-1 |
| SYS-05 | Identity platform (SSO, MFA, privileged access management, identity governance) | ACQ-1 identities are not yet federated |
| SYS-06 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers | Cloud A: payroll engine, integration platform, Workforce Management Platform. Cloud B: enterprise data platform and AI services. DC-1 and DC-2: legacy servers, I-9 scanned archive, backup copies |
| SYS-07 | Workforce Management Platform (WMP): the firm's own vendor management system for managed service provider clients (developed in-house, on Cloud A) | Service line SL-1; client hiring managers and about 2,300 supplier firms use it; SOC 2 Type 2 since 2024 |
| SYS-08 | Enterprise network and endpoints: SD-WAN to about 520 sites; about 14,500 laptops; about 1,150 lobby applicant kiosks | Kiosks at 46 legacy branches remain on the branch staff network |
| SYS-09 | Screening and verification services: two background screening providers (consumer reporting agencies), drug testing provider, E-Verify (DHS web system) | About 1,100 named E-Verify users, outside SSO |
| SYS-10 | ERP (finance, accounts receivable and payable, general ledger) and internal staff HCM and payroll (vendor SaaS) | SOX IT general controls tested annually |
| SYS-11 | About 1,400 third-party vendors (220 with associate or candidate personal information) | Tiered third-party risk program |
| SYS-12 | AI portfolio (11 use cases) | Governed by an AI governance council formed in 2025 |

**SSP system (P02):** the *Associate Lifecycle and Payroll Platform (ALPP)*: the firm's configuration and use of the front-office ATS (SYS-01) and the onboarding and Form I-9 platform (SYS-02), the customer-managed payroll and billing engine (SYS-03), the time capture services (SYS-04), and the ALPP integrations on the enterprise integration platform; a Moderate system that inherits common controls from the enterprise platform.

**Data flow in one line:** candidates apply on a career site or kiosk (SYS-01), the AI add-on ranks them (AI-001), recruiters select and offer, onboarding collects tax, bank, and Form I-9 data (SYS-02), a background check runs through a screening provider (SYS-09), the onboarding team creates the E-Verify case, the integration platform creates the associate in the payroll engine (SYS-03), associates record time in the app, on a time clock, or through a client VMS (SYS-04), and weekly payroll, pay files, and invoices run in SYS-03.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A defined program aligned to CSF 2.0 (current Tier 3, Repeatable)
- Annual risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC with an MSSP for overflow
- PAM for administrators
- Quarterly access certification for SOX and tier-1 applications
- Immutable backups in separate backup accounts
- Annual DR tests for tier-1 systems
- Tiered vendor reviews
- Annual SOC 2 Type 2 for the Workforce Management Platform (SL-1)
- SEC Item 106 disclosure in its 10-K
- Tokenization of SSNs and bank account numbers inside the payroll engine
- Electronic Form I-9 with E-Verify for all new hires; FCRA disclosures and adverse action letters run through the screening providers

**Targeted gaps:**
1. **Payroll diversion.** Associates change direct deposit accounts in the mobile app after an SMS one-time code. In 2025, 214 fraudulent bank changes diverted about $612,000 of pay, which the firm repaid. Out-of-band confirmation exists only for internal staff.
2. **Acquisition integration.** ACQ-1 (a travel nurse firm acquired in 2025) still runs its own identity directory, ATS and credentialing system, and outsourced payroll, with no SIEM feeds. Migration is due 2027-03-31.
3. **Data sprawl.** The enterprise data platform (Cloud B) holds full SSNs and bank account numbers for about 2.9 million current and former associates and candidates outside the payroll engine's tokenization. Applicant data and consumer reports have no enforced retention schedule.
4. **E-Verify and I-9 access.** About 1,100 E-Verify user accounts sit outside SSO; the 2026 quarterly review found 37 accounts of departed users. The scanned paper I-9 archive (about 1.4 million forms, 2009-2019) in DC-2 has no access audit trail.
5. **Third parties and client integrations.** 31 of 220 vendors with personal information lack a current assessment. About 400 client VMS integrations use shared service accounts and long-lived API keys.
6. **AI.** 11 AI use cases, but only 6 have completed council review. The NYC bias audit of the ranking tool covers NYC only; enterprise-wide bias monitoring relies on vendor data; Colorado deployer duties start 2027-01-01 and are not designed yet.
7. **Materiality.** The disclosure playbook has not been exercised since the CFO and General Counsel changed in 2026, and it has no method to estimate client contract and associate remediation costs for a PII breach.
8. **Legacy.** The time clock server in DC-1 runs an unsupported operating system, and 46 legacy branches still have kiosks on the staff network.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | **NIST CSF 2.0 (voluntary benchmark, all 106 subcategories)** plus every binding rule that applies across the enterprise: Form I-9 (8 CFR 274a.2, N56-R03), the E-Verify MOU and FAR 52.222-54, Fla. Stat. 448.095 (worked example of state E-Verify law), FCRA (N56-R02), the Disposal Rule (N56-R01), SEC Form 8-K Item 1.05 and Reg S-K Item 106, FAR 52.204-21 (N56-R07), NYC Local Law 144 (N56-R08), Colorado SB26-189 (effective 2027-01-01), and state breach and data security laws (Florida worked example). N56-R04, N56-R05, N56-R06, and N56-R09 are checked and recorded |
| Regulatory driver labels | `N56-BM (...)` means the P03 voluntary benchmark (NIST CSF 2.0), with the CSF 2.0 subcategory in parentheses; it is a scenario label, not a row in `requirements.csv`. `N56-R01` to `N56-R09` cite the vertical requirements with the specific section. `E-Verify MOU Art. II.x` cites the MOU paragraph (MOU for Employers, revision 06/01/13). `SEC 8-K 1.05` and `SEC S-K 106` cite 17 CFR 229.106 and Form 8-K Item 1.05. `Fla. Stat. 501.171(x)` and `Fla. Stat. 448.095(x)` cite the Florida worked examples |
| P08 | Payroll and HR system breach exposing worker PII, including an **SEC materiality assessment and 8-K Item 1.05** step, and a multi-state breach-notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to clients: SL-1, the Workforce Management Platform (existing SOC 2 Type 2 for Security, Availability, Confidentiality), and SL-2, payrolling and employer-of-record services (no SOC 2 yet); all five categories assessed |
| P10 | Enterprise AI portfolio (11 use cases), with the council operating model; focus use case AI-001, AI resume screening and candidate ranking |
| Cloud | Multi-cloud (vendor-agnostic) with common controls |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, with second-line GRC support) |
| 2026-09-10 | Results to the risk and technology committee of the board |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Registry defaults kept.** The registry's primary system (payroll and applicant tracking system), incident (payroll and HR system breach exposing worker PII), and AI use case (AI resume screening and candidate ranking) all fit a staffing firm at this size and were kept. At this size the "payroll and applicant tracking system" is a platform of several components (SYS-01 to SYS-04), so P02 documents it as one system, the ALPP.

**States with large operations.** The 38 states include Florida (headquarters and worked example), California, Illinois, New York (including 9 branches in New York City), Colorado, Connecticut, Texas, and Georgia. In 2025 the firm had about 41,000 associates and about 330,000 applicants in California, so it holds sensitive personal information (SSNs) of more than 50,000 California consumers. These facts drive the state AI and privacy rows in P03 and P10.

**Cyber insurance.** A $50 million cyber insurance tower (P01 R-064; P08 section 6).

**Sites and volumes.** About 520 sites: 380 branch offices and 140 on-site offices at client facilities, in 38 states and the District of Columbia. Florida has 61 branches and about 9,800 associates on assignment in an average week. About 46,000 timesheets and 3,900 client invoices a business day at the weekly peak. About $13.2 million of revenue per calendar day (about $18.5 million per business day).

**Segments and acquired firms.**
| Unit | Facts |
|---|---|
| Commercial Staffing | About 52,000 associates on assignment a week; most on-site offices and kiosks |
| Professional Staffing | About 11,000 consultants a week, including **Government Solutions** (about 1,900 associates on 34 federal contracts with FAR 52.204-21 and 52.222-54, and 21 state agency contracts) |
| Healthcare Staffing | About 9,000 clinicians a week, including 6,500 at **ACQ-1** |
| Workforce Solutions | SL-1 Workforce Management Platform (about 60 managed service provider clients, about 2,300 supplier firms); SL-2 payrolling and employer-of-record (about 340 clients, about 6,000 client-sourced workers a week); recruitment process outsourcing (RPO) for about 25 clients, in the clients' own ATSs |
| ACQ-1 | Travel nurse firm acquired 2025-06; about 900 internal staff; legacy directory, ATS and credentialing system, and outsourced payroll provider until migration on 2027-03-31 |
| ACQ-2 | IT staffing firm acquired 2026-02; about 400 internal staff; identities federated 2026-05; moves onto SYS-01 to SYS-03 by 2026-12-31 |

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Operating Officer (COO) | Business owner for branch and on-site operations; authorizing official for the ALPP (P02) |
| Chief Audit Executive | Heads Internal Audit; reports to the audit committee; leads the P07 assessment |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| Chief Data Officer | Enterprise data platform (Cloud B); co-chairs the AI governance council |
| Chief Human Resources Officer | Internal staff onboarding, terminations, training records |
| Controller | SOX program owner for financial reporting controls |
| Treasurer | Bank relationships, ACH origination, and paycard program funding |
| Segment presidents (Commercial, Professional, Healthcare, Workforce Solutions) | Own segment processes; accept segment risks up to High with the CRO |
| Vice President, Talent Acquisition Technology | System owner of SYS-01 and the AI ranking add-on |
| Vice President, Payroll Technology | System owner of SYS-03 and the ALPP integrations |
| Vice President, Government Solutions | Federal and state agency contracts; FAR clause compliance |
| Vice President, Integration Management Office | ACQ-1 and ACQ-2 integration |
| Vice President, Associate Service Center | Contact center for associates (pay questions, bank changes, W-2s) |
| Vice President, Product, Workforce Management Platform | SL-1 owner and WMP product and engineering |
| Vice President, Payrolling Services | SL-2 owner |
| Director of Security Operations | SOC, SIEM, EDR, vulnerability management, incident response |
| Director of Identity and Access Management | Identity platform (SYS-05) |
| Director of Cloud Platform Engineering | Landing zones in both clouds (common control provider) |
| Director of Network and Endpoint Engineering | SD-WAN, branch networks, kiosks, laptops, time clocks (common control provider) |
| Director of Third-Party Risk Management | Vendor tiering, contract security terms, SOC report reviews (in the GRC team) |
| Director of Employment Eligibility Compliance | I-9 and E-Verify program, E-Verify program administrators (reports to the Vice President, Employment Compliance) |
| Payroll Engine Application Manager | Day-to-day administration of SYS-03 (reports to the Vice President, Payroll Technology) |
| Vice President, Investor Relations; Vice President, Corporate Communications | Disclosure committee member; media and associate communications |
| Vice President, Facilities | Physical security of branches, corporate offices, and colocation contracts |

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. The CFO and General Counsel joined in 2026.

**Healthcare Staffing and HIPAA.** 37 hospital clients required business associate agreements in their staffing contracts. Because placed clinicians are the hospital's workforce, the firm treats those agreements as contractual commitments (confidentiality, incident notice to the client) and not as a determination that it is a business associate. Clinicians' credentialing files (licenses, immunization and drug test results) are the firm's own employment records. The firm's employee group health plans are separate covered entities administered by third-party administrators and are outside the scope of these deliverables.

**Pay delivery.** About 86% of associates are paid by direct deposit, 12% by paycard through a bank paycard program manager, and 2% by check. The firm originates ACH through two banks. The firm does not accept payment cards from anyone (clients pay by ACH or wire), so PCI DSS does not apply.

**Recruiting texts.** Recruiters send job alerts and shift reminders by automated text message to candidates and associates who opt in through SYS-01. The firm does not telemarket goods or services.

**Biometric time clocks.** The time clocks support a face-match feature; it is disabled at every site pending legal review of state biometric laws (not analyzed here).

**Operational facts used in the deliverables.**
| Topic | Fact | Used in |
|---|---|---|
| Payroll rhythm | Associates are paid every Friday. Approved time is due Monday 12:00; payroll runs Monday 06:00 to Thursday 12:00 (Eastern); ACH files must reach the banks by Thursday 14:00. Three payroll centers (about 420 staff), one of them in Florida | P05; P08 section 3 |
| Pay delivery | Bank A carries 80% of ACH files and Bank B 20%; Bank B passed a full-volume test on 2025-11-14. About 9,400 associates a week are paid by paycard | P05; P08 |
| Associate Service Center | Two centers, about 380 agents, about 21,000 calls and chats a day; caller verification today uses knowledge questions | P05; P07; P08 |
| ALPP users and volumes | About 9,800 workforce users; about 310,000 associate self-service accounts active in 2025; about 21,000 client approvers; about 140 integration routes and 900 interface jobs a day; 6 payroll engine servers | P02; P07 |
| Disaster recovery | The 2026-05-16 tier-1 DR test recovered the payroll engine in 9.5 hours against an 8-hour RTO; the WMP met its 4-hour RTO | P02; P05; P07 |
| Client integrations | About 400 client VMS integrations; 63 API keys older than 2 years | P02; P04; P07 |
| Data platform | 41 analytics users can query clear-text SSNs and bank numbers in the nightly extract | P01; P04; P07 |
| Records past retention | About 1.9 million applications and 410,000 consumer reports past the retention schedule; about 410,000 scanned Forms I-9 from 2009-2012 lack a searchable index; about 38,000 ACQ-1 Forms I-9 sit in ACQ-1's legacy system | P03; P07 |
| Internal Audit | IT audit manager and four IT auditors under the Chief Audit Executive | P07 |
| Workforce Management Platform | SOC 2 Type 2 (Security, Availability, Confidentiality) issued every year since 2024; the 2025 report had no exceptions | P09 |
| AI-001 | In production since 2024-09 in sort-only mode (auto-advance and automatic rejection never enabled); independent NYC bias audit completed 2026-02-09; NYC applicants are those for jobs at 9 NYC branches | P03; P10 |
| Treatment funding | About $4.9 million of security treatment funded for 2026 Q4 to 2027 Q2 | P01 section 7 |
| Disclosure playbook | Version 2, with a PII breach cost model due 2026-10-31 (POAM-013) | P07; P08 section 6 |

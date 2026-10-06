# Scenario facts: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or a contract, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (temporary staffing firm, doing business as a staffing agency) |
| Business | Temporary help services (NAICS 561320) in one Central Florida metro area. Places temporary associates with small and mid-size client businesses in two lines: **Light Industrial** (warehouse, distribution, packaging, and event setup; about 60% of associate hours) and **Office Support** (reception, data entry, customer service, and bookkeeping assistants; about 40%). A small **direct-hire** service refers candidates to clients for permanent jobs for a fee (about 8% of receipts) |
| Location | Florida. One office suite in Central Florida with a small applicant lobby and an interview room. All clients and worksites are in the same metro area. The firm does not recruit for remote jobs or for worksites in other states |
| Workforce | **7 internal staff employees** (section 2). In addition, the firm is the W-2 employer of its **temporary associates**: about 22 on assignment in an average week (14 to 38; the peak is November and December), and 96 different associates paid during 2025. Associates work under client supervision at client sites |
| Volumes | About 2,600 applications a year through the applicant tracking system (ATS), which holds about 9,800 candidate records collected since 2019; about 120 new associate hires a year (Form I-9 and E-Verify); about 90 employment background checks a year (required by most Light Industrial clients); about 30 active client accounts; about 10 direct-hire placements a year |
| Revenue | About $1.1 million a year in receipts (fictional): about $1.01 million of temporary help billings and about $90,000 of direct-hire fees. Associate gross payroll is about $700,000 a year, paid weekly every Friday (about $13,500 a week; up to $24,000 in peak weeks) |
| Size status | SBA-small. NAICS 561320 uses a receipts-based standard of $34.0 million (13 CFR 121.201). The size tier counts the 7 internal staff in permanent positions; temporary associates are counted separately, as the firm's other samples do |
| Clients | Small warehouses, regional distributors, event venues, and professional offices. Client supervisors approve associate time in the payroll service's approver portal. Clients pay invoices by ACH or check. The largest client, a regional distributor (about 22% of receipts), sent a vendor security questionnaire in June 2026; the response is due 2026-09-30 |
| Employer status | The firm is the **employer of record** for associates: it completes their Forms I-9, runs E-Verify, withholds taxes, pays wages, and carries workers' compensation. For direct-hire referrals the hiring client completes the Form I-9. The firm is not a "recruiter or referrer for a fee" for Form I-9 purposes, because 8 CFR 274a.2(a)(1) limits that term to agricultural associations, agricultural employers, and farm labor contractors |
| E-Verify | Enrolled directly as an employer on 2024-03-04 because two Light Industrial clients require it in their contracts. Fla. Stat. 448.095(2)(b)2. requires E-Verify of private employers with 25 or more employees, and 448.095(1)(b) defines "employee" as an individual filling a permanent position. The firm has 7 permanent staff; whether temporary associates count is not settled. It does not change practice: the E-Verify MOU requires the firm to verify all new employees and not selectively (MOU Art. II.A.11) |
| Form I-9 practice | Paper Form I-9 completed in person at the office. Originals and document photocopies are kept in a locked cabinet in the locked records room. Since 2024-03 the Onboarding and Payroll Coordinator also scans each completed Form I-9 with its document copies into the shared drive (SYS-03). Because those document images are electronic, 8 CFR 274a.2(b)(3) makes them subject to the electronic retention standards in 274a.2(e) to (i) |
| Employment law status | An employer of its associates and an **employment agency** under Title VII (42 U.S.C. 2000e(c)) when it refers candidates to clients |
| Not in scope | HIPAA (N56-R04): the firm places no clinical staff and performs no services for covered entities involving PHI. Its small-group health plan for internal staff is fully insured through a carrier; plan duties were not analyzed. Payment cards (N56-R06): none. Federal contracts (N56-R07): none. Telemarketing (N56-R05): the firm does not telemarket; recruiters text candidates who opted in through the ATS, and TCPA consent details were not analyzed. NYC Local Law 144 (N56-R08): no NYC candidates or jobs. Hazmat (N56-R09): none. SEC rules: private company |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: the Florida Information Protection Act (Fla. Stat. 501.171) and Florida's employment eligibility statute (Fla. Stat. 448.095). Other states' breach laws are treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Owner (President) | Accepts Moderate, High, and Very High risks; approves policies and spending; signs client contracts; decision authority for the AI tool (P10) |
| Operations Manager | **Security and Privacy Lead** (designated in writing 2026-07-01); approves payroll each week; E-Verify program administrator; Form I-9 and FCRA compliance; breach notice decisions with counsel; works with the MSP on the productivity suite |
| Onboarding and Payroll Coordinator | Completes Form I-9 Section 2, creates E-Verify cases, orders background checks, sends FCRA notices; enters weekly payroll; handles associate bank-change requests |
| Senior Recruiter | ATS administrator (users, settings, the AI match feature); Office Support desk and direct-hire placements |
| Recruiters (2) | Light Industrial desk: sourcing, screening, scheduling, and associate call-outs |
| Account Manager | Client sales and job orders; client questionnaires and contract terms |
| Managed service provider (MSP, contractor) | Help desk, laptop patching and antivirus, firewall and Wi-Fi, productivity suite administration on request, and administration of the suite backup (SYS-08) |
| Outside CPA firm (contractor) | Quarterly tax review and year-end close; read-only access to the accounting SaaS |

Headcount (7): Owner 1; Operations Manager 1; Onboarding and Payroll Coordinator 1; Senior Recruiter 1; Recruiters 2; Account Manager 1.

## 3. Systems
| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Staffing ATS: career site, applicant records and resumes, job orders, client contacts, onboarding packet e-forms (W-4, direct deposit form, emergency contact, policy acknowledgments), background check ordering through SYS-06 | Vendor SaaS (ATS for small staffing firms) | Yes: SSNs and dates of birth in onboarding packets; bank account numbers on direct deposit forms; resumes | System of record for candidates and job orders. 7 named users. MFA by authenticator app enforced for all users |
| SYS-02 | Payroll and timekeeping service: weekly payroll for associates and staff, tax filings, W-2s, direct deposit, associate self-service portal (pay stubs, W-2s, bank changes), mobile clock-in, client approver portal | Vendor SaaS (payroll service for small employers) | Yes: SSNs, dates of birth, addresses, bank accounts, pay and tax data | 3 administrator users (Owner, Operations Manager, Coordinator). MFA by **SMS one-time code**. Associates change their own bank account in self-service with a password only |
| SYS-03 | Productivity suite: email, calendar, chat, shared drive | SaaS (business plan) | Yes: the shared "Onboarding" folder holds Form I-9 scans with document images (since 2024-03), consumer report PDFs (since 2019), and onboarding packet exports with SSNs | MFA by push approval for all users since 2025-06 (a cyber insurance requirement). All 7 staff can open the whole shared drive. Sign-in and file activity logs kept 90 days (plan default) |
| SYS-04 | Endpoints: 8 laptops (7 staff, 1 interview-room laptop), 1 applicant tablet in the lobby, 1 multifunction printer and scanner; 7 personal smartphones used for work | MSP-managed laptops; personal phones unmanaged | Yes (cached email and downloads; candidate ID photos in text messages on phones) | Laptops have full-disk encryption and MSP antivirus. Phones carry email, the ATS app, and MFA apps |
| SYS-05 | Office network: small-business firewall, staff Wi-Fi, guest Wi-Fi, one business internet line | On-premises, MSP-managed | In transit | Applicant tablet and visitors on guest Wi-Fi |
| SYS-06 | Background screening provider (consumer reporting agency) portal, integrated with SYS-01 | Vendor SaaS | Yes: consumer reports | Provider hosts the electronic FCRA disclosure and authorization and mails the pre-adverse and adverse action letters the firm triggers |
| SYS-07 | E-Verify (DHS web system) | Federal government | Yes: case data | Named user accounts; outside every firm sign-in system |
| SYS-08 | Cloud backup of the productivity suite (SaaS-to-SaaS backup) | SaaS, operated by the MSP | Yes (copies of SYS-03) | Daily, 30-day retention. **Never restore-tested.** One MSP administrator login with a password only |
| SYS-09 | AI match and ranking feature of the ATS | Vendor SaaS (ATS vendor's AI subprocessor) | Yes: resumes and application answers | Turned on 2026-03-16 with a "smart filter" that hides applicants scoring under 50 from the default view (see P10) |
| SYS-10 | Accounting SaaS: client invoices, receivables, bank feed | SaaS | Business financial data; client contacts | Owner, Operations Manager, and the outside CPA (read-only). MFA enforced by the vendor. Outside the SSP boundary |

**SSP system (P02):** the *Payroll and Applicant Tracking System (PATS)*: the firm's accounts, settings, and data in SYS-01, SYS-02, SYS-03, and SYS-08; the interfaces to SYS-06, SYS-07, and SYS-09; and the SYS-04 endpoints and SYS-05 office network used to operate them.

**Data flow in one line:** candidates apply on the career site or the lobby tablet (SYS-01), the AI feature scores them (SYS-09), recruiters screen and place, onboarding collects tax and bank forms in the ATS packet (SYS-01), a background check runs through the screening provider (SYS-06), the Coordinator completes the paper Form I-9, scans it to the shared drive (SYS-03), and creates the E-Verify case (SYS-07), the Coordinator keys the new hire into payroll (SYS-02), associates clock in on the payroll app, clients approve time in the approver portal, and weekly payroll runs in SYS-02.

## 4. Current security posture: early to partial
**In place today:**
- MFA on email (push approval) and on the ATS (authenticator app); vendor-enforced MFA on the accounting SaaS
- MSP patching, antivirus, and firewall; full-disk encryption on laptops
- Guest Wi-Fi separated from staff Wi-Fi; the applicant tablet runs the career site in kiosk mode on guest Wi-Fi
- Paper Forms I-9 in a locked cabinet in a locked records room
- E-Verify for all new hires since 2024-03-04, with case numbers written on the Form I-9
- FCRA disclosure and authorization collected electronically through the screening provider; pre-adverse and adverse action letters sent by the provider with a 5-business-day wait between them
- Locked shred bin with a monthly shredding service that issues certificates of destruction
- Daily cloud backup of the productivity suite (SYS-08)
- Cyber insurance (the policy requires MFA on email and remote access)
- New-hire handbook acknowledgment (one page on computer use)

**Missing:**
1. No risk assessment and no written security policies; the handbook has one page on computer use.
2. No incident response plan or breach notice procedure. Nobody knew the Florida 30-day clocks or the E-Verify MOU's immediate breach notice to DHS.
3. The payroll service uses SMS one-time codes. Bank-account changes made by associates in self-service, or by staff on request by phone, email, or text, get no call-back and send no alert to the firm.
4. The shared "Onboarding" folder holds Form I-9 scans and document images, consumer report PDFs, and onboarding exports with SSNs. All 7 staff can open it. There is no retention schedule, and paper Forms I-9 have never been purged.
5. Terminations are handled "when remembered". A former recruiter's ATS and email accounts stayed active for 2 months after she left.
6. The suite backup has never been restore-tested, its MSP administrator login has no MFA, and there is no export of ATS or payroll data.
7. No log review in any system; suite logs age out after 90 days.
8. Training is the handbook acknowledgment only: no phishing awareness and no payroll diversion training for the Coordinator.
9. Personal phones carry email, the ATS app, and texts with candidates, including photos of identity documents; no mobile management and no remote wipe.
10. No vendor security review. The payroll vendor's SOC 2 report was never requested, the ATS AI feature terms were accepted by click-through, and the MSP contract has no security terms or recovery commitment.
11. The AI match feature was turned on with a filter that hides low scorers, without review, bias testing, applicant notice, or an accommodation path.
12. No inventory of devices or of where SSNs, Form I-9 images, and consumer reports are kept.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Registry defaults | Kept as given. **Primary system:** "Payroll and applicant tracking system" fits as is: the ATS and the payroll service are the firm's two core systems (the PATS). **P08:** "Payroll and HR system breach exposing worker PII" fits a firm that runs its own weekly payroll. **P10:** "AI resume screening and candidate ranking" fits the ATS AI match feature |
| P03 benchmark | **NIST CSF 2.0 (voluntary benchmark)**, all 106 subcategories (label `N56-BM`). No sector cybersecurity rule applies to a temporary staffing firm. The binding rules that govern the records in the PATS are assessed as secondary rows: Form I-9 (8 CFR 274a.2, N56-R03), the E-Verify MOU, Fla. Stat. 448.095, FCRA employment screening (15 U.S.C. 1681b(b), N56-R02), the FACTA Disposal Rule (16 CFR 682.3, N56-R01), and Fla. Stat. 501.171. N56-R04 to N56-R09 are recorded as Not applicable rows with reasons |
| Regulatory driver labels | `N56-BM (...)` means the P03 voluntary benchmark (NIST CSF 2.0) with the CSF 2.0 subcategory in parentheses. It is a scenario label, not a row in `requirements.csv`. `N56-R01` to `N56-R03` cite the vertical requirements with the specific section. `E-Verify MOU Art. II.A.x` cites the MOU for Employers posted on e-verify.gov (revision date 06/01/13). `Fla. Stat. 501.171(x)` and `Fla. Stat. 448.095(x)` cite the Florida duties. `Title VII 703(b)` is 42 U.S.C. 2000e-2(b) and `Title VII 703(k)` is 42 U.S.C. 2000e-2(k) |
| P08 incident | Payroll and HR system breach exposing worker PII: an adversary-in-the-middle phishing page that imitates the payroll service captures the Onboarding and Payroll Coordinator's password and SMS code; the attacker downloads the employee census report (names, SSNs, dates of birth, addresses, bank accounts) and changes direct deposit accounts for several associates before Friday payroll. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | The firm is **not** a SOC 2 service organization: it supplies labor and runs no system that processes client data for clients. P09 is (a) a readiness self-assessment against **Security plus Confidentiality**, used to answer the largest client's questionnaire, and (b) a review of the payroll vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| P10 AI | AI-001: the ATS AI match and ranking feature (SYS-09). AI-002: the ATS's generative AI writer for job ads and candidate messages. AI-003: staff use of public chatbots |
| Cloud | SaaS plus one cloud workload: the SaaS-to-SaaS backup of the productivity suite (SYS-08), operated by the MSP. Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis with the MSP lead technician (office walkthrough 2026-07-22) |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant (on site 2026-08-11) |
| 2026-08-31 | Deliverables approved by the Owner |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Firm history | Founded in 2017. The ATS has been in use since 2019 and the current payroll service since 2023-01. The employee handbook is the 2023 edition. The screening services agreement (with the FCRA end-user certification) dates from 2021 | P02, P03, P08 |
| Departures and stale accounts | Three staff left in 2025-2026: an Account Manager (2025), the previous Coordinator (2025-12-12), and a recruiter (2026-05-15). The recruiter's ATS and email accounts were found active on 2026-07-21 during the risk assessment and disabled that day; ATS and suite sign-in logs showed no use after her last day. P07 found the previous Coordinator's E-Verify account still active on 2026-08-11 (last sign-in 2025-12-10; deactivated that day) and her screening portal account still listed (removed 2026-08-12). The staff Wi-Fi password was changed on 2026-05-15; the replacement recruiter, hired in 2026-06, received a laptop the MSP reimaged | P01, P02, P03, P07 |
| Records search (2026-07-22) | The Onboarding folder held 214 Form I-9 scan packets (2024-03 to 2026-07), 412 consumer report PDFs (2019 to 2026), and 38 onboarding exports with SSNs. Mailboxes held 63 messages with SSNs or identity document images. Text threads on 3 recruiters' phones held candidate ID photos. The records room holds about 610 paper Forms I-9 (2017 to 2026), filed by hire year with no index | P01, P03, P07, P09 |
| Payroll operations | Payroll is due in the payroll service by Wednesday 5 p.m. for Friday direct deposit. The payroll vendor can freeze bank-account changes and hold or recall pending deposits on request. The census report covers about 318 current and former associates and staff paid since 2023-01 (about 301 with Florida addresses and about 17 in 6 other states); it was downloaded 6 times in 2026 with no record of why. Payroll notification settings were changed in 2025 with no record | P03, P05, P07, P08 |
| Payroll vendor SOC 2 report | Requested 2026-08-03; received under a nondisclosure agreement 2026-08-14; reviewed 2026-08-20 by the Operations Manager with the independent consultant. Type 2, 12 months ending 2026-03-31, Security, Availability, and Confidentiality, unqualified, one exception (bank-change call-backs not documented in 2 of 40 samples). States RTO 8 hours and RPO 1 hour | P02, P05, P09 |
| ATS vendor | Its trust page claims a SOC 2 Type 2 report; requested 2026-08-03, not received by 2026-08-31. Its terms delete customer data 30 days after a subscription ends. The AI feature's click-through terms allow use of customer data to improve models unless an opt-out is set (off by default; turned on 2026-08-28) | P03, P04, P05, P10 |
| AI feature history | Turned on by the Senior Recruiter on 2026-03-16 after an ATS upgrade, with a smart filter hiding scores under 50 on Light Industrial job orders. From 2026-03-16 to 2026-07-24, 560 applicants applied to those orders and 196 were hidden; 325 answered the voluntary self-identification form. Filter turned off 2026-07-24. Feature-weight sheet provided 2026-08-19; employment-gap feature turned off and keyword list replaced on 2026-08-28. One of the two Recruiters is bilingual in English and Spanish | P01, P03, P10 |
| Compliance samples | Form I-9 sample of 20 (2025-2026): one Section 2 and one E-Verify case completed on the fourth business day during the Coordinator's leave. Background checks: 20 orders sampled, all with authorization; in 2 of the 4 adverse decisions in 2026 a recruiter told the candidate by phone and filled the assignment before the pre-adverse letter | P01, P03 |
| Credentials and devices | E-Verify passwords were written in a notebook in the Coordinator's desk. The firewall and the backup console each use one MSP administrator account shared by its technicians. The interview-room laptop was exempt from screen lock. Two laptops were retired in 2025 and the previous copier was returned at lease end in 2024, all with no wipe record; the current scanner keeps scan images on an internal disk. The Senior Recruiter kept Light Industrial onboarding access after moving to the Office Support desk | P02, P03, P04, P07 |
| Office | Keyed suite entry with an after-hours monitored alarm; locked records room; keys held by the Owner and the Operations Manager; surge protectors and a small battery unit on the network gear | P02, P03 |
| MSP contract | Covers help desk, laptop patching, antivirus, firewall, Wi-Fi, suite administration on request, and backup administration, with a 4-business-hour response time; no recovery commitment, no security terms, and no incident notice clause. The MSP's technician list was requested 2026-08-03 and not received by fieldwork end | P02, P04, P05, P07 |
| Continuity resources | A bench of about 40 ready associates; a line of credit that covers about 3 weeks of payroll; a printed assignment roster every Friday | P05 |
| Cyber insurance | The policy has a 24x7 breach hotline and panel vendors (breach counsel, forensics) and requires prompt notice and use of panel vendors | P08 |
| Client contracts | The largest client's agreement requires notice of a security incident affecting client information "promptly", with no fixed number of hours. Its questionnaire arrived in June 2026 and is due 2026-09-30 | P08, P09 |
| Assessor | The P07 assessor is an independent security consultant, not involved in the risk assessment or gap analysis and operating no control | P07 |
| Budget | Q4 2026 treatments approved 2026-08-31: about $1,900 one-time and $2,900 a year; the 2026 assessment and policy work cost about $2,800 | P01 |
| Form I-9 scans decision | On 2026-08-31 the Owner decided that paper is the only Form I-9 record: each paper file is checked as complete, then its scan is deleted, and scanning stops (target 2026-12-31) | P03, P06, P07 |

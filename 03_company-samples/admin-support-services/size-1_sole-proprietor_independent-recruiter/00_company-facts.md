# Scenario facts: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-recruiter files Schedule C) |
| Business | Independent recruiter for IT support, accounting, and data analyst roles. Two lines of work: **contract staffing** (about 65% of receipts), in which the owner recruits contractors who are placed with client companies and employed and paid by a contract staffing back-office partner, and **direct-hire placement** (about 35%), in which the owner refers candidates to clients for permanent jobs for a contingency fee. Primary NAICS 561320 (Temporary Help Services), because contract staffing is the larger line; the direct-hire line alone would be NAICS 561311 |
| Location | Florida. Home office in the owner's residence in Central Florida. Candidates are met by video call or in public places; client meetings are at client offices |
| Workforce | The owner-recruiter only (0 employees). Contractors on assignment are W-2 employees of the back-office partner, not of the business |
| Volumes | About 3,400 candidate records in the applicant tracking system (ATS), built up since 2019, with about 1,200 added each year; about 40 job orders a year; 11 contractors on assignment at 6 client companies (about 24 different contractors paid through the partner in 2025); about 5 direct-hire placements a year |
| Revenue | About $180,000 a year in receipts (fictional): about $117,000 from the recruiter's share of contract gross margin, paid monthly by the partner, and about $63,000 from direct-hire fees (average fee about $12,500, 20% of first-year salary). SBA-small (NAICS 561320 standard $34.0 million in average annual receipts; 13 CFR 121.201) |
| Clients | About 15 active client companies, all Florida employers with 50 to 500 employees (so each is an "employer" under Title VII, 42 U.S.C. 2000e(b)). Clients receive candidate submittals by email and approve contractor timesheets in the partner's portal |
| Employer status | **Not an employer** of the contractors or of direct-hire candidates. The back-office partner is the employer of record for contractors: it completes their Forms I-9, runs E-Verify, orders background checks, withholds taxes, and pays wages. Clients complete Forms I-9 for direct hires |
| Form I-9 | No I-9 duty. Under 8 CFR 274a.2(a)(1), references to recruiters and referrers for a fee are limited to agricultural associations, agricultural employers, and farm labor contractors. The business is none of these |
| Background checks | The owner does **not** procure consumer reports. The partner orders them for contractors under its own FCRA certification and shows the owner only a "cleared to start" or "not cleared" status in its portal. Clients order their own for direct hires. However, two clients emailed full background check reports to the owner (2025-11 and 2026-03), and both are still in the mailbox |
| Employment law status | An **employment agency** under Title VII (42 U.S.C. 2000e(c): "any person regularly undertaking with or without compensation to procure employees for an employer") and therefore a covered entity under the ADA (42 U.S.C. 12111(2), (7)). The EEOC states that a recruitment company that regularly refers employees to employers "is covered no matter how many employees it has" (eeoc.gov, Coverage of Employment Agencies, read 2026-10-06) |
| Not in scope | HIPAA (N56-R04): no clinical placements and no work for covered entities involving PHI. TCPA and Telemarketing Sales Rule (N56-R05): the owner texts candidates one at a time from the phone and does not telemarket; TCPA consent details were not analyzed. Payment cards (N56-R06): none; the partner pays by ACH and direct-hire clients pay invoices by ACH or check. Federal contracts (N56-R07): none. NYC Local Law 144 (N56-R08): no NYC jobs or candidates for NYC jobs. Hazmat (N56-R09): none. Florida E-Verify statute (Fla. Stat. 448.095): no employees. SEC rules: not a public company |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: the Florida Information Protection Act (Fla. Stat. 501.171), whose "covered entity" definition names a sole proprietorship (501.171(1)(b)). Other states' breach laws are treated generically ("each state where affected individuals reside") |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-recruiter | Every role: owner, security lead, privacy contact, risk acceptor, system administrator for every account |
| Contract staffing back-office partner | Employer of record for contractors: payroll, Forms I-9, E-Verify, background checks, benefits, workers' compensation, client invoicing for contract hours. Operates the partner portal (SYS-03). Back-office services agreement has a general confidentiality clause but **no security requirements and no breach notice clause** |
| Outside bookkeeper (contractor) | About 3 hours a month in the accounting SaaS (SYS-04) with a named user account. No access to the ATS, email, or partner portal |
| On-call IT support technician (local IT shop) | Hourly help with the laptop, phone, and home router. No standing access; remote sessions only through a one-time session code the owner starts. Signed a confidentiality agreement on 2026-07-17 |

## 3. Systems
| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Recruiting ATS/CRM for independent recruiters: candidate records, resumes, notes, job orders, client contacts, submittal history, email sync add-on, and the **AI match add-on** (resume parsing, 0-100 match score, ranking, optional automatic rejection) | Vendor SaaS | Yes: about 3,400 candidate records (names, home addresses, phone numbers, resumes, compensation notes); some attachments include ID images | System of record. Own password; **MFA available but not turned on**; the password was reused from an old job board account |
| SYS-02 | Business email, calendar, and file storage (productivity suite, business plan) | SaaS | Yes: resumes and submittals; about 70 messages with contractor start forms holding full SSNs and dates of birth (2019-2025); candidate-sent ID images; 2 client-forwarded background check reports | MFA by SMS text code. File version history kept 30 days (plan default) |
| SYS-03 | Back-office partner portal | Partner SaaS | Yes: contractor names, addresses, dates of birth, SSNs (entered by the owner at start, masked after submission), pay and bill rates, timesheet status, monthly margin statements | One recruiter login: password plus a one-time code sent to the owner's email |
| SYS-04 | Accounting SaaS (direct-hire invoices, bank feed, partner margin deposits) | SaaS | Business financial data; client billing contacts | Owner and outside bookkeeper accounts. MFA enforced by the vendor |
| SYS-05 | E-signature service (client fee agreements; candidate consent-to-represent forms) | SaaS | Names, contact details, signed agreements | Signs in through the email account (inherits SYS-02 MFA) |
| SYS-06 | Laptop (business-owned) | Owner device | Yes: cached email; a downloads folder with start forms and resumes | Full-disk encryption on (operating system default); automatic updates; built-in antivirus; locks after 5 minutes |
| SYS-07 | Smartphone (personal, used for business) | Personal device | Yes: email and ATS apps, texts with candidates, photos of candidate ID documents in the camera roll | Passcode and biometric unlock; device locator on; remote erase never tested |
| SYS-08 | Home office network | Consumer router from the internet provider | Yes (in transit) | Router admin password never changed from the default; family phones, game console, and smart-home devices share the one network |
| SYS-09 | Sourcing services: professional networking recruiter subscription and two job boards | SaaS | Public candidate profiles and applications that flow into SYS-01 | Outside the boundary except the owner's accounts |
| SYS-10 | General-purpose AI chatbot (free consumer account) | SaaS | Yes, when resumes are pasted in | Used since 2025-11 for job ads and outreach messages; resumes pasted in for summaries (see P10) |

**SSP system (P02):** the *Recruiting and Placement Systems Profile (RPSP)*: the owner's accounts, settings, and data in SYS-01 to SYS-05, SYS-09, and SYS-10, and the SYS-06 to SYS-08 devices and network used to reach them.

**Data flow in one line:** candidates apply through job boards or are sourced on the networking site (SYS-09) and land in the ATS (SYS-01), where the AI match add-on scores them; the owner screens by phone, submits candidates to clients by email (SYS-02), and for contract roles enters a start request with the contractor's SSN and date of birth in the partner portal (SYS-03); the partner onboards, screens, and pays the contractor; the partner pays the owner's margin share monthly and direct-hire fees are invoiced from the accounting SaaS (SYS-04).

## 4. Current security posture: early (few formal controls)
**In place today:**
- Business-plan email with MFA (SMS text codes)
- Full-disk encryption, automatic updates, built-in antivirus, and a 5-minute lock on the laptop
- Passcode and biometric unlock on the phone
- Vendor-enforced MFA on the accounting SaaS
- The SaaS vendors' own backups; 30-day file version history in the productivity suite
- Cross-cut shredder in the home office for paper
- The back-office partner runs I-9, E-Verify, background checks, and payroll under its own programs

**Missing:**
1. No written security policy and no risk assessment before 2026.
2. No MFA on the ATS, and its password is reused; passwords are saved in the browser, not a password manager.
3. Email MFA uses SMS codes, which an adversary-in-the-middle phishing page can capture; sign-in alerts are not reviewed.
4. Full SSNs, dates of birth, and ID images sit in the mailbox, the laptop downloads folder, and the phone camera roll, with no retention schedule.
5. Two client-forwarded background check reports are kept with no disposal procedure (16 CFR 682.3).
6. Candidate records are kept indefinitely (since 2019).
7. The back-office partner agreement has no security or breach notice terms, and the partner's payroll desk accepts contractor bank-change requests forwarded from the owner's email without a call-back.
8. The home router still uses its default admin password, and family and smart-home devices share the network.
9. The phone holds candidate ID photos; remote erase has never been tested.
10. The ATS AI match add-on was turned on with automatic rejection for two job orders without any review, candidate notice, or accommodation path; resumes were pasted into a consumer AI chatbot.
11. No incident plan, contact list, or knowledge of the Florida 30-day notice clock.
12. No independent export of ATS data; the ATS vendor deletes data 30 days after a subscription ends.
13. No security training.
14. Single-person dependency: only the owner holds the credentials and the client and candidate relationships.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Registry defaults adapted | **Primary system:** the registry default "Payroll and applicant tracking system" is adapted to the ATS plus the back-office partner portal, because a recruiter with no employees runs no payroll; payroll is the partner's system and the owner only feeds it. **P08 incident:** "Payroll and HR system breach exposing worker PII" is adapted to a takeover of the owner's email and ATS that exposes contractor and candidate PII and is used to try to divert a contractor's pay through the partner. **P10:** the registry default (AI resume screening and candidate ranking) fits as is: the ATS AI match add-on |
| P03 benchmark | **NIST CSF 2.0 (voluntary benchmark)**, all 106 subcategories (label `N56-BM`). No sector cybersecurity rule applies. Binding rules that touch the owner's data are assessed as secondary rows: Fla. Stat. 501.171 and the FACTA Disposal Rule (16 CFR 682.3, N56-R01). FCRA 1681b(b) (N56-R02), Form I-9 (N56-R03), Fla. Stat. 448.095, and N56-R04 to N56-R09 are recorded as Not applicable rows with reasons |
| Regulatory driver labels | `N56-BM (...)` means the P03 voluntary benchmark (NIST CSF 2.0) with the CSF 2.0 subcategory in parentheses. It is a scenario label, not a row in `requirements.csv`. `N56-R01` cites the Disposal Rule. `Fla. Stat. 501.171(x)` cites the Florida duties. `Title VII 703(b)` is 42 U.S.C. 2000e-2(b) and `Title VII 703(k)` is 42 U.S.C. 2000e-2(k) |
| P08 incident | Adversary-in-the-middle phishing captures the owner's email password and SMS code; the attacker searches the mailbox for SSNs and IDs, resets the ATS password through email and exports the candidate list, and sends the partner a forwarded "direct deposit change" for a contractor before a pay date |
| P09 SOC 2 | The business is not a SOC 2 service organization: it refers people, and it runs no system that processes client data for clients. P09 is (a) the owner's Security-only self-check and (b) a review of the back-office partner's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| P10 AI | AI-001: the ATS AI match add-on (score, ranking, and automatic rejection). AI-002: the consumer AI chatbot used for job ads, outreach, and resume summaries |
| Cloud | SaaS only. No IaaS or PaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call IT support technician (after the confidentiality agreement was signed on 2026-07-17); tests on 2026-07-23 |
| 2026-08-31 | Deliverables adopted by the owner-recruiter |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Mailbox search results | On 2026-07-23 the owner and the IT technician searched the mailbox and the laptop for SSNs and ID images. Found: 71 messages with full SSNs and dates of birth for 58 contractors (start forms 2019-2025), ID images from 19 candidates (23 images), and the 2 background check reports. In all, 77 people have an SSN or a government ID number in the mailbox; 66 live in Florida and 11 in 6 other states. 34 of the start forms were also in the laptop downloads folder. The phone camera roll held 9 photos of candidate IDs | P01, P03, P05, P07, P08 |
| Start forms by email | Until the partner opened its portal in 2025-03, the partner required start forms by email. Since then the owner has used the portal, but sent 4 start forms by email in 2025-2026 when the portal was slow | P02, P03, P04 |
| Partner bank-change practice | In a call on 2026-07-22 the partner's payroll desk confirmed it accepts a contractor's bank-change form forwarded from the owner's email address without calling the contractor. Contractors can also change their own bank account in the partner's employee self-service, which uses MFA | P01, P04, P08 |
| Partner assurance | The partner provided its SOC 2 Type 2 report (Security and Confidentiality categories, 12 months ending 2026-03-31) under a nondisclosure agreement on 2026-07-22. The owner reviewed it with the IT technician on 2026-07-23 | P02, P09 |
| ATS vendor terms | The ATS vendor states on its trust page that it holds a SOC 2 Type 2 report; the owner has not requested it. Its terms delete customer data 30 days after the subscription ends, and its AI match add-on terms allow use of customer data to improve the models unless the customer turns on an opt-out setting (off by default) | P01, P04, P10 |
| AI match add-on history | Turned on 2026-02-02. Automatic rejection ("auto-disposition") below a score of 40 was turned on for two job orders (a staff accountant and a help desk analyst) from 2026-04-06 to 2026-06-26: 412 applicants, of whom 236 received an automatic rejection email with no human review. Automatic rejection was turned off on 2026-07-21 during the self-assessment. Scores are now a sort aid only | P01, P03, P10 |
| Chatbot use | Since 2025-11 the owner has used a free consumer AI chatbot for job ads and outreach, and pasted about 30 resumes into it to draft client summaries. The account's chat history and model-training setting were on. The owner stopped pasting resumes on 2026-07-21 | P01, P10 |
| Cyber insurance | No standalone cyber insurance. Whether the professional liability (errors and omissions) policy includes a cyber endorsement is unconfirmed (owner action in P08) | P01, P08 |
| Client contracts | Fee agreements with clients include a confidentiality clause covering client information and require notice of a security incident affecting client information "promptly"; no fixed number of hours | P08 |
| Router default password | The router admin password was confirmed as the factory default during the 2026-07-23 test (found under IA-5) and changed the same day | P07 |
| Partner SOC 2 details | Type 2, unqualified opinion. Carved-out subservice organizations: the cloud hosting provider, the background screening vendor, and the payroll tax filing provider. One exception: 2 of 25 sampled terminated partner employees kept portal access for more than 5 business days (remediated). Portal MFA options are email or authenticator-app codes; the system description states a 99.5% monthly availability target and no recovery time. Bridge letter requested 2026-07-23 | P09 |
| AI match add-on features | The vendor's public help documentation names skills, job titles, years of experience, education, location, and employment gaps as scoring inputs. The owner requested the full feature list with weights on 2026-07-24. The owner does not collect demographic data, so group outcomes cannot be measured | P10 |
| Account inventory | The owner built the first account list on 2026-07-22. It found recruiter accounts on two job boards unused since 2021 and still open with old applications. The bookkeeper's accounting account was set up by the owner after a video call. Browser-saved passwords sync to the owner's personal browser account, with no primary password | P02, P03, P07 |
| Devices and home office | Laptop about 3 years old, phone about 2 years old. The previous phone was traded in during 2024 after a factory reset that was not recorded. Paper (current fee agreements) is kept in a locked drawer; a surge protector is in use. Home office walkthrough held 2026-07-21 | P02, P03, P07 |
| ATS logging | The ATS keeps an activity log of sign-ins, exports, and downloads; the email service records sign-ins and mailbox rule changes. Neither had been reviewed | P02, P04, P07 |
| Public presence | The business has a one-page website and a profile on the professional networking site | P03 |
| Security budget | About $300 a year approved on 2026-08-31 (password manager and training), plus up to about $150 once for a router that supports a separate work network | P01, P03 |

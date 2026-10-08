# Scenario facts: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (temporary staffing firm, doing business as a staffing agency) |
| Business | Temporary help services (NAICS 561320). Places temporary associates with client businesses in two divisions: **Light Industrial** (warehouse, distribution, packaging, light assembly; about 75% of hours) and **Office and Administrative** (clerical, customer service, data entry; about 25%). A small **Direct Hire** desk (about 3% of revenue) refers candidates to clients for permanent jobs for a fee |
| Location | Florida only. Headquarters and **Branch 1** in Central Florida; **Branches 2, 3, and 4** in other Florida metro areas. All job orders and all client worksites are in Florida. The firm does not recruit for remote jobs or for worksites in other states |
| Workforce | **60 internal staff employees** (section 2). In addition, the firm is the W-2 employer of its **temporary associates**: about 450 on assignment in an average week, and about 2,100 different associates paid during 2025. Associates work under client supervision at client sites |
| Volumes | About 16,000 applications a year through the applicant tracking system (ATS); about 2,000 new associate hires a year (onboarding, Form I-9, E-Verify); about 1,500 employment background checks a year (required by most Light Industrial clients); about 180 active client accounts |
| Revenue | $20.4 million a year in receipts (fictional). Associate gross payroll is about $14 million a year, paid weekly (about $270,000 per weekly payroll) |
| Size status | SBA-small. NAICS 561320 uses a receipts-based standard of $34.0 million (13 CFR 121.201), so the size tier does not depend on associate headcount. "60 employees" in the tier profile means internal staff |
| Clients | Third-party logistics warehouses, regional distributors, light manufacturers, and office employers. Clients approve associate timesheets in the client portal and pay invoices by ACH or check. Two large warehouse clients sent security questionnaires in 2026 that ask about SOC 2 |
| Employer status | The firm is the employer of record for associates: it completes their Forms I-9, runs E-Verify, withholds taxes, and pays wages. For Direct Hire referrals the firm is a referrer for a fee (8 CFR 274a.2), but it does not complete Forms I-9 for those candidates (the hiring client does) |
| E-Verify | Enrolled directly as an employer (not through an employer agent) in 2023 to meet Fla. Stat. 448.095(2)(b)2. (private employers with 25 or more employees). The firm verifies **all** new hires, internal staff and associates, as the E-Verify MOU requires (Art. II.A.11) |
| Not in scope | HIPAA (N56-R04): the firm does not place clinical staff or perform services for covered entities involving PHI. Its group health plan for eligible associates is fully insured through a carrier and broker; group health plan duties were not analyzed. Payment cards (N56-R06): the firm does not accept cards. Federal contracts (N56-R07): none. Telemarketing (N56-R05): the firm does not telemarket; recruiting text messages go only to candidates who opted in through the ATS, and TCPA details were not analyzed. NYC Local Law 144 (N56-R08): no NYC candidates or jobs. Hazmat (N56-R09): no transport of hazardous materials. SEC rules: private company |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: the Florida Information Protection Act (Fla. Stat. 501.171) and Florida's E-Verify statute (Fla. Stat. 448.095). State AI employment laws in other states were checked and do not reach the firm while it stays Florida-only (see P10) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| President (majority owner, Cris Santos) | Accepts High and Very High risks; approves the security budget; signs client contracts |
| Chief Operating Officer (COO) | Executive sponsor of the security program; accepts Moderate risks; approves policies; business owner of the P10 AI tool decision |
| Controller | Owns payroll, billing, and cash; cyber insurance; approves payroll bank changes over the threshold |
| IT Manager | Part-time Information Security Lead (designated in writing 2026-07-01); runs IT with one IT Support Specialist and a managed IT provider for after-hours support and branch network gear |
| HR and Compliance Manager | Owns Form I-9, E-Verify, background check (FCRA), and records retention compliance; privacy contact for associates and candidates; breach notice decisions with counsel |
| Payroll Manager | Runs the weekly associate payroll and internal payroll; supervises 3 Payroll Specialists and 2 Billing Specialists |
| Director of Recruiting | Owns the ATS recruiting workflow and the recruiters' use of the AI screening tool |
| Recruiting Operations Coordinator | ATS and AI screening tool administrator (configuration, job board feeds, reports) |
| Branch Managers (4) | Branch facilities, lobby kiosks, local access, and branch downtime procedures |
| Onboarding and Compliance Specialists (6) | Complete Form I-9 Section 2, create E-Verify cases, order background checks, send FCRA notices |
| Safety Coordinator | Client site safety visits and workers' compensation; keeps client site access badges issued to associates |
| Managed IT provider (contractor) | After-hours monitoring of the endpoint security console, branch firewall and Wi-Fi changes |

Headcount (60): President 1; COO 1; Controller 1; Director of Recruiting 1; Branch Managers 4; Recruiters 22; Account Managers 7; Onboarding and Compliance Specialists 6; Payroll Manager 1; Payroll Specialists 3; Billing Specialists 2; Accounting staff 2; HR and Compliance Manager 1; IT Manager 1; IT Support Specialist 1; Recruiting Operations Coordinator 1; Safety Coordinator 1; Branch Office Administrators 4.

## 3. Systems

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Staffing ATS and onboarding platform: career site, candidate profiles and resumes, job orders, onboarding forms (W-4, direct deposit, electronic Form I-9 module with document images), background check ordering, client portal for timesheet approval | Vendor SaaS (staffing-industry ATS; SOC 2 Type 2 report requested, not yet received) | Yes: SSNs, I-9 identity document images, E-Verify case numbers, consumer reports (PDF copies), bank account numbers entered at onboarding | System of record for candidates and associates. Uses SSO through SYS-03 |
| SYS-02 | Payroll and billing platform: associate and internal payroll, tax filings, W-2s, direct deposit and pay card funding, client invoicing | Vendor SaaS (payroll service provider; SOC 2 Type 2 report on file) | Yes: SSNs, bank accounts, pay and tax data | Uses its own login with SMS one-time codes, **not** SSO (see gaps). Originates ACH through the vendor's bank |
| SYS-03 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Push-notification MFA. Protects SYS-01, SYS-04 console, SYS-05, SYS-06 admin, SYS-09 |
| SYS-04 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts four firm-managed workloads: the **integration service** (container service; syncs new hires and pay rates from SYS-01 to SYS-02 and imports approved time from SYS-06), the **reporting database** (managed database; nightly copy of ATS and payroll data, including full SSNs), the **document archive** (object storage; scanned paper Forms I-9 from 2014-2022 and exported consumer reports), and the **backup vault** |
| SYS-05 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | Recruiters sometimes receive I-9 document photos and resumes by email |
| SYS-06 | Mobile timekeeping app for associates (clock-in with GPS geofence) | Vendor SaaS | Yes: geolocation at clock-in (personal information under Fla. Stat. 501.171(1)(g)1.a.(VII)) | Biometric face-match feature is available but **disabled** |
| SYS-07 | Background screening provider (consumer reporting agency) portal and ATS integration | Vendor SaaS | Yes: consumer reports | Provider also sends the pre-adverse and adverse action letters the firm triggers |
| SYS-08 | E-Verify (DHS web system) | Federal government | Yes: case data | 6 named user accounts; outside SSO (see gaps) |
| SYS-09 | AI resume screening and candidate matching add-on to SYS-01 | Vendor SaaS (third-party AI vendor integrated into the ATS) | Yes: resumes, application answers, work history | In production since 2026-03-02 in "rank and auto-advance" mode (see P10) |
| SYS-10 | Office networks (HQ/Branch 1 and Branches 2-4) | On-premises | Yes (in transit) | Firewall at each office; staff Wi-Fi and guest Wi-Fi; lobby applicant kiosks on the staff network (see gaps) |
| SYS-11 | Endpoints | On-premises and mobile | Yes (cached) | 62 laptops, 8 lobby applicant kiosk PCs, 4 multifunction scanners, 34 company smartphones (recruiters and managers) |

**SSP system (P02):** the *Associate Payroll and Applicant Tracking Platform (APATP)*: the firm's configuration and use of SYS-01, SYS-02, SYS-03, and SYS-06; the SYS-04 workloads (integration service, reporting database, document archive, backup vault); the interfaces to SYS-07, SYS-08, and SYS-09; and the SYS-10 networks and SYS-11 endpoints used to operate them.

**Data flow in one line:** candidates apply on the career site or a lobby kiosk (SYS-01), the AI add-on scores them (SYS-09), recruiters select and offer, onboarding collects tax, bank, and Form I-9 data (SYS-01), a background check runs through the CRA integration (SYS-07), an Onboarding Specialist creates the E-Verify case (SYS-08), the integration service creates the associate in payroll (SYS-02), associates clock in on the app (SYS-06), clients approve time in the client portal (SYS-01), and weekly payroll and invoices run in SYS-02.

## 4. Current security posture: partially compliant

**In place today:**
- SSO with push MFA for email, the ATS, the cloud console, and the timekeeping admin portal
- Endpoint detection and response (EDR) on laptops, monitored by the managed IT provider (alerts reviewed next business day)
- Automatic OS and browser patching on laptops
- Full-disk encryption on laptops
- Electronic Form I-9 completed in the ATS onboarding module since 2022, with electronic signatures and a per-record change history
- E-Verify used for all new hires since 2023, with case numbers recorded in the I-9 module
- FCRA pre-adverse and adverse action letters sent through the screening provider, with a 5-business-day wait between them
- Locked shred bins at every branch and a shredding vendor that issues certificates of destruction
- Annual security awareness video for internal staff
- The payroll platform vendor's SOC 2 Type 2 report on file (never formally reviewed)
- Daily snapshots of the reporting database and document archive (same account and region)
- Cyber insurance (the policy requires MFA on email and remote access)

**Missing or weak, found in the 2026 assessments:**
1. The payroll platform (SYS-02) is not on SSO and uses SMS one-time codes. Payroll bank-account changes by associates and by staff have no out-of-band confirmation and no alert.
2. No security policy set. The employee handbook has one page on computer use. No documented risk assessment before 2026.
3. No review of audit logs in the payroll platform, the ATS, or the identity provider. Identity provider logs are kept 30 days.
4. No written incident response plan or breach notification procedure. The firm does not know its Florida 30-day clock or its E-Verify MOU breach notice duty.
5. No BIA, contingency plan, or manual payroll procedure. Cloud snapshots share the production account and region and have never been restore-tested.
6. The reporting database holds full SSNs and bank account numbers for about 31,000 current and former associates that reports do not need, and all 22 recruiters can query it.
7. ATS roles are too broad: every recruiter can open I-9 document images and consumer report PDFs for all branches. Consumer reports and I-9 images are kept indefinitely with no retention schedule.
8. Electronic I-9 program gaps: no written description of the electronic I-9 system and indexing (8 CFR 274a.2(e)(5)), no periodic inspection and quality checks ((e)(1)(iii)), and the scanned 2014-2022 I-9 archive in object storage has no access audit trail ((g)(1)(iv)).
9. E-Verify accounts are outside SSO and are not on the termination checklist.
10. The FCRA background check disclosure form includes a liability release and state notices, so it is not a document that "consists solely of the disclosure" (15 U.S.C. 1681b(b)(2)(A)(i)).
11. Lobby applicant kiosks sit on the staff network with a shared local account, and one retired kiosk PC was discarded in 2025 without wiping.
12. Vendor management is informal: no security review or contract terms for the AI screening vendor, the timekeeping app vendor, or the screening provider; the ATS vendor's SOC 2 report has not been obtained.
13. Training is an annual video only. There are no phishing exercises, and payroll staff have no training on payroll diversion and bank-change fraud.
14. The AI screening add-on went live in "rank and auto-advance" mode without bias testing, candidate notice, or an approved-tools list for AI.
15. Two E-Verify user accounts belonging to Onboarding Specialists who left in 2025 were still active, and one of them had been used after the person's departure date by a colleague who knew the password (found during P07 testing).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 benchmark | **NIST CSF 2.0 (voluntary benchmark).** No sector cybersecurity rule applies to a temporary staffing firm. The binding rules that touch the data are assessed as secondary rows: Form I-9 retention and electronic I-9 standards (8 CFR 274a.2, N56-R03), the E-Verify MOU, FCRA employment screening (15 U.S.C. 1681b(b), N56-R02), the FACTA Disposal Rule (16 CFR 682.3, N56-R01), Fla. Stat. 501.171, and Fla. Stat. 448.095. The other vertical requirements (N56-R04 to N56-R09) do not apply and are recorded as Not applicable rows |
| Regulatory driver labels | `N56-BM (...)` means the P03 voluntary benchmark (NIST CSF 2.0), with the CSF 2.0 subcategory in parentheses. It is a scenario label, not a row in `requirements.csv`. `N56-R01` to `N56-R03` cite the vertical requirements with the specific section. `E-Verify MOU Art. II.A.x` cites the MOU paragraph (numbering from the MOU for Employers posted on e-verify.gov, revision 06/01/13). `Fla. Stat. 501.171(x)` and `Fla. Stat. 448.095(x)` cite the Florida duties. `Title VII 703(k)` is 42 U.S.C. 2000e-2(k) |
| P08 incident | Payroll and HR system breach exposing worker PII: an adversary-in-the-middle phishing page captures a Payroll Specialist's password and SMS code for the payroll platform (SYS-02); the attacker exports the associate register (names, SSNs, addresses, bank accounts) and changes direct deposit accounts for associates before a weekly payroll |
| P09 SOC 2 | The firm is **not** a SOC 2 service organization for its clients: it supplies labor, and it does not operate a system that stores or processes client data on the clients' behalf. P09 is (a) a Security-only self-benchmark against the Trust Services Criteria, used to answer the two warehouse clients' questionnaires, and (b) a review of the payroll platform vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| P10 AI | AI resume screening and candidate ranking add-on to the ATS (SYS-09), in production since 2026-03-02. Second inventory entry: generative AI drafting of job ads and candidate messages in the ATS. Third: staff use of public chatbots |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork (HQ walkthrough 2026-07-15; Branch 3 walkthrough 2026-07-16) |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (branch testing 2026-08-05) |
| 2026-08-31 | Deliverables approved by the COO, with High risks accepted by the President |

# Scenario facts: Cris Santos Company | Professional, Scientific, and Technical Services | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or IRS publication, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a licensed CPA firm operating as a limited liability company) |
| Business | CPA and tax preparation firm (NAICS 541211). Individual and small-business income tax preparation and planning (about 70% of receipts), monthly bookkeeping and payroll processing for small-business clients (about 20%), and IRS notice and examination representation (about 10%). The firm performs no attest engagements (no audits, reviews, or compilations) |
| Location | Florida. One office suite in a professional office building |
| Workforce | 7 employees: the Owner CPA (managing member), 1 Senior Tax Accountant (CPA), 1 Tax Accountant (enrolled agent), 1 Tax Preparer, 1 Bookkeeper, 1 Client Services Coordinator, and 1 Office Manager. One seasonal data-entry assistant works from January to mid-April as a temporary employee and is not counted in the 7 |
| Clients | About 880 individual income tax returns (Form 1040 series) a year, covering about 1,400 individual consumers (spouses on joint returns counted separately); about 170 business returns (S corporations, partnerships, LLCs, and a few trusts); 38 monthly bookkeeping and payroll clients, with payroll run for about 420 of their employees. About 6% of individual clients live outside Florida for part or all of the year |
| Customer information held | Records on about 3,300 consumers: current individual clients plus former clients whose folders are still in cloud storage. Folders go back to 2016 because no disposal schedule exists (see gap 8). Payroll employees of business clients are not the firm's consumers (16 CFR 314.2(b)(1)); even if all 420 were counted, the total would be about 3,700 |
| Revenue | About $1.1 million a year (fictional), about $4,400 per business day on average. About 60% of receipts are billed from February to April, about $10,500 per business day in that season. Under the SBA standard of $26.5 million for NAICS 541211, so SBA-small |
| GLBA status | **Financial institution under the FTC Safeguards Rule.** 16 CFR 314.2(h)(2)(viii) names "an accountant or other tax preparation service that is in the business of completing income tax returns." Individuals who become clients for tax preparation have a customer relationship (314.2(e)(2)(i)(H)). The firm maintains customer information on fewer than 5,000 consumers, so the **314.6 exception applies**: 314.4(b)(1), (d)(2), (h), and (i) do not apply. Every other element applies, including the written program (314.3(a)) and FTC notice of notification events involving 500 or more consumers (314.4(j)) |
| IRS status | Tax return preparer under IRC 7216 (26 CFR 301.7216-1(b)(2)); every employee who helps prepare returns, including the Client Services Coordinator and the seasonal assistant, is a tax return preparer for section 7216. Four PTIN holders (Owner CPA, Senior Tax Accountant, Tax Accountant, Tax Preparer). Authorized IRS e-file Provider acting as an Electronic Return Originator (ERO) with one EFIN; the Owner CPA is the e-file Responsible Official. Returns are transmitted through the tax software vendor, itself an Authorized IRS e-file Provider |
| Not in scope | HIPAA: the firm has no health care bookkeeping clients and declines engagements that would require it to receive PHI, so it is not a business associate. FAR 52.204-21, DFARS 252.204-7012, and CMMC: no federal contracts or subcontracts. ABA Model Rules: not a law firm. SEC and PCAOB: no attest clients. SOC examinations: the firm does not perform them. CIRCIA: proposed rule only. Payment cards: client payments run through the practice management vendor's hosted payment page |
| Professional standards | The AICPA Code of Professional Conduct confidentiality rule applies to the CPAs as a professional standard adopted through state licensing. It is noted but not assessed, because its text was not verified from the source for this sample. Circular 230 (31 CFR Part 10) applies to the CPAs and the enrolled agent who practice before the IRS |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, data security, and disposal in Fla. Stat. 501.171). Clients who live in other states are handled generically ("each state where affected individuals reside") |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Owner CPA (managing member) | Senior person responsible for the program; accepts Moderate risks and approves treatment plans for High risks; approves policies and spending; IRS e-file Responsible Official; decides breach notifications with counsel; decision authority for AI use |
| Office Manager | **Qualified Individual** under 16 CFR 314.4(a), designated in writing by the Owner CPA on 2026-07-06. Runs the program day to day with the MSP; keeps the risk register, vendor list, and incident log; onboarding and terminations; billing and vendor contracts |
| Senior Tax Accountant (CPA) | Reviews returns; backup tax software administrator; business owner of the generative AI assistant (AI-001) |
| Tax Accountant (enrolled agent) | IRS notice responses and representation; main AI-001 user |
| Tax Preparer | Prepares individual returns |
| Bookkeeper | Client bookkeeping and payroll processing; accountant user in clients' accounting platforms and in the payroll platform |
| Client Services Coordinator | Reception, document intake and scanning, client portal administration, e-file acknowledgments, and Form 8879 files |
| Managed service provider (MSP) | Help desk, patching, antivirus, firewall and Wi-Fi, productivity suite administration on request, and backup administration. A service provider under 314.4(f) and a contractor under 26 CFR 301.7216-2(d)(2) |

## 3. Systems

| ID | System | Hosting | Holds customer information? | Notes |
|---|---|---|---|---|
| SYS-01 | Professional tax preparation and e-file software | Vendor-hosted (SaaS) | Yes | System of record for returns. Vendor enforces MFA. Vendor transmits returns to the IRS and states. Vendor has a SOC 2 Type 2 report (reviewed in P09). Offers an AI document extraction feature that the firm has **not** turned on |
| SYS-02 | Client document portal with e-signature | Vendor SaaS (separate vendor) | Yes | Clients upload documents, sign Forms 8879 and engagement letters, and download returns. Client MFA is optional; about 30% of individual clients use it |
| SYS-03 | Productivity suite (email, calendar, cloud file storage) | SaaS, business plan | Yes | Client folders (scans, workpapers, prior returns since 2016) live in shared cloud storage and sync to the desktops. Clients routinely email source documents |
| SYS-04 | Client accounting and payroll platforms | Vendor SaaS | Yes | Accountant user access to bookkeeping clients' cloud accounting files, and the payroll platform under the firm's accountant account (employee SSNs and bank accounts) |
| SYS-05 | Practice management, time and billing | Vendor SaaS | Yes (client list, engagement letters, invoices) | Includes the vendor-hosted payment page |
| SYS-06 | Endpoints | On-premises and remote | Yes (cached) | 4 desktops, 4 laptops, 1 leased multifunction printer-scanner (MFP), and 7 staff-owned phones with the productivity suite app |
| SYS-07 | Office network | On-premises, MSP-managed | Yes (in transit) | Small-business firewall, staff Wi-Fi, separate guest Wi-Fi for clients, one internet line |
| SYS-08 | Cloud backup of the productivity suite (SaaS-to-SaaS) | SaaS, operated by the MSP | Yes | Daily backup of mailboxes and cloud storage with 1 year of retention |
| SYS-09 | Generative AI assistant (business plan, 3 seats) | Vendor SaaS | Yes, in use | Subscribed 2026-03-02 by the Owner CPA. Used to draft client letters and IRS notice responses and to summarize uploaded documents (P10, AI-001) |

**SSP system (P02):** the *Client Tax Platform (CTP)*: SYS-01, SYS-02, SYS-03, SYS-06, SYS-07, and SYS-08, with their interfaces to the IRS and state e-file systems through the tax software vendor.

## 4. Current security posture: early to partial

**In place today:**
- MFA on the tax software (enforced by the vendor) and on the productivity suite (push approval without number matching); MFA on portal staff accounts
- Unique user accounts in the tax software and the productivity suite; a PTIN for every preparer
- Full-disk encryption on the 4 laptops; provider encryption at rest in SYS-01, SYS-02, and SYS-03
- MSP monthly patching, antivirus with automatic updates, and a managed firewall; guest Wi-Fi separated from staff devices
- Daily SaaS-to-SaaS backup of the productivity suite (SYS-08) with 1 year of retention
- Engagement letters for every client, and an IRC 7216 consent form used for the one routine third-party disclosure (release of returns to a client's lender on request)
- A locked shred bin emptied by a shredding vendor that provides certificates of destruction
- A cyber insurance policy (bought 2025) with a breach hotline and panel vendors
- A written information security plan (WISP) filled in from the IRS Pub. 5708 template in 2024
- A Qualified Individual designated in writing (2026-07-06)

**Missing or weak, found in the 2026 assessments:**
1. The 2024 WISP was filled in once from the Pub. 5708 template and never updated, followed, or shared with staff. No risk assessment had ever been done.
2. No incident response plan or data theft procedure. Nobody knew about the next-business-day IRS report (IRS Pub. 1345) or the 30-day FTC notice (314.4(j)).
3. Email is exposed to business email compromise: push MFA without number matching, automatic forwarding to external addresses allowed, no alerts on new inbox rules or risky sign-ins, and firm email on staff-owned phones without device controls.
4. Returns and source documents are emailed to clients as plain attachments on request. Client portal MFA is optional.
5. The 4 desktops are unencrypted, and the leased MFP keeps scanned images on its internal drive.
6. Access removal happens "when remembered". The 2026 seasonal assistant's tax software and email accounts stayed active for about 12 weeks after the assistant's last day. There are no access reviews, and the Owner CPA and Office Manager use global administrator rights on their everyday productivity suite accounts.
7. No service provider inventory or oversight. The MSP contract has no security terms, and MSP technicians were never given the written IRC 6713 and 7216 notice (26 CFR 301.7216-2(d)(2)).
8. No data retention and disposal schedule. Client folders go back to 2016, including former clients (314.4(c)(6)).
9. The suite backup (SYS-08) has never had a full restore test, and the MSP-held backup administrator account has no MFA.
10. No log review or alerting, and no weekly check of returns filed per PTIN and EFIN.
11. No call-back verification when a client asks by email to change a refund direct deposit account, or when someone asks the Bookkeeper to change a payroll employee's bank account.
12. Training was a single video in 2024. There is no annual training, no phishing exercise, and the seasonal assistant was never trained.
13. Three staff have used the generative AI assistant (SYS-09) since March 2026 with client notices and some source documents uploaded. There was no IRC 7216 analysis and no approved-tools rule, and one staff member used a free personal chatbot once.
14. No asset inventory and no change procedure. The MSP changes firewall and suite settings without approval or a record (314.4(c)(2), (c)(7)).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulations | Primary: FTC Safeguards Rule, 16 CFR Part 314, with the 314.6 exception applied. Secondary: IRC 7216 and 26 CFR 301.7216-1 to -3, with the IRS e-file provider duties in Pub. 1345 and the WISP expectations in Pubs. 4557 and 5708 |
| P08 incident | Business email compromise of the Tax Accountant's mailbox, leading to theft of client tax documents and an attempted refund diversion. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Confidentiality. The firm is not a SOC 2 service organization. The readiness check answers a vendor security questionnaire from its largest bookkeeping and payroll client; Part B reviews the tax software vendor's SOC 2 Type 2 report |
| P10 AI | Generative AI for tax and document preparation: AI-001, the business-plan generative AI assistant used to draft client letters and IRS notice responses. **Adapted from the registry default:** at this size the firm does not use the tax software's AI extraction feature (it is turned off), so the assessed use case is the general-purpose assistant the firm actually uses |
| Cloud | SaaS plus one cloud workload: the SaaS-to-SaaS backup operated by the MSP (SYS-08). Vendor-agnostic |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-17 | Risk assessment and gap analysis (Office Manager as Qualified Individual, with the MSP lead technician) |
| 2026-08-03 to 2026-08-05 | Control assessment by an independent consultant (on site 2026-08-04) |
| 2026-08-31 | Deliverables approved by the Owner CPA |

## 7. Facts added while building the deliverables
These facts were added in Phase 5 because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Endpoints | SYS-06 is 4 desktops (reception and scanning station, Office Manager, Bookkeeper, seasonal station) and 4 laptops (Owner CPA, Senior Tax Accountant, Tax Accountant, Tax Preparer). The 4 desktops sync the client folders from SYS-03. Staff phones are staff-owned; 7 have the suite email app | P01, P02, P04, P07 |
| Seasonal assistant account | The 2026 seasonal assistant's last day was 2026-04-17. The assistant's tax software and email accounts were found active on 2026-07-08 during the risk assessment and disabled that day. Sign-in logs showed no use after 2026-04-17 | P01, P03, P07 |
| Backup vendor | The SYS-08 subscription is held by the MSP and resold to the firm, so the backup vendor is the MSP's subcontractor. It is administered with one shared MSP administrator account. Single-file restores have been done on request; no full restore has ever been tested | P01, P04, P05, P07 |
| MSP contract | Covers help desk, patching, antivirus, firewall, Wi-Fi, suite administration on request, and backup administration, with a 4-business-hour response time, no recovery time commitment, and no security or breach notice terms | P01, P05, P07 |
| Internet | One business internet line; no failover | P01, P05 |
| Cyber insurance | The policy (since 2025) has a 24x7 breach hotline and panel vendors (breach counsel, forensics). It requires prompt notice and use of panel vendors, and the application stated that MFA is used for email | P08 |
| Finances | A cash reserve covers about 45 days of expenses. The firm's own payroll runs biweekly through an outside payroll service | P01, P05 |
| Office security | Keyed suite entry with an after-hours alarm; keys held by the Owner CPA and the Office Manager; a locked network closet; paper source documents kept in locked cabinets during the season | P02, P03 |
| MFP lease | The MFP is leased; the lease ends 2027-03-31. The lessor's return process does not include drive wiping unless requested | P01, P03 |
| Questionnaire | The firm's largest bookkeeping and payroll client, a property management company with about 140 employees on payroll, sent a vendor security questionnaire in June 2026 covering security and confidentiality, because the client's own lender and insurer ask how its payroll provider protects employee data. The response is due 2026-09-30 | P09 |
| Assessor | The P07 assessor is an independent IT security consultant engaged for a fixed fee, not involved in the risk assessment or gap analysis and operating no control. The assessor signed the written IRC 6713 and 7216 notice before reviewing any system | P07 |
| MFP scan-to-email (P07 finding) | P07 testing on 2026-08-04 found that the MFP sends scans to email through a suite mailbox ("scanner") that signs in with an app password over legacy authentication, so it is excluded from MFA, and that the MFP's administration page still had the default password. The administration password was changed on 2026-08-05 | P01, P04, P07 |
| AI assistant use | AI-001 has 3 seats (Owner CPA, Senior Tax Accountant, Tax Accountant). Interviews found that IRS notices for about 40 clients and Forms W-2 for 3 clients were uploaded from March to July 2026. The vendor's business terms exclude training on inputs by default, keep inputs up to 30 days for abuse monitoring with possible human review, and do not commit to U.S.-only processing. The Tax Preparer pasted one client letter, with the client's name, into a free personal chatbot in April 2026 | P01, P03, P10 |
| Consumer count | The Office Manager counted consumers from the tax software client list and the cloud storage folders on 2026-07-08: about 1,400 current individual clients and about 1,900 former clients, about 3,300 in total | P03 |
| Past events | One misdirected email with a client's return in 2025 was handled informally with no record. Two desktops were replaced in 2024 with no disposal record | P03, P09 |
| Email sample | The P03 review of 15 emails with returns sent in the 2026 season found 6 sent as plain attachments | P02, P03, P07 |
| External forwarding | At the Office Manager's request, the MSP blocked automatic forwarding to external addresses for every mailbox on 2026-07-20 | P01, P08 |
| Risk register review | The Owner CPA reviewed the draft risk register on 2026-07-24, before approval on 2026-08-31 | P07 |
| MSP evidence | The MSP security questionnaire and evidence request were sent on 2026-07-27. The technician list, MFA evidence for the remote management platform, and the backup subcontractor's terms had not arrived by the end of P07 fieldwork | P04, P07 |
| P07 account findings | The seasonal assistant's portal staff account was still active on 2026-08-04 (removed that day; no sign-in after 2026-04-17). The assistant had started work 3 days before signing the confidentiality agreement | P07, P09 |
| Qualified Individual training | The Office Manager completed an online FTC Safeguards Rule course in June 2026, before the designation | P03 |
| Lender releases | 12 returns were released to clients' lenders in 2026, all with the IRC 7216 consent signed first. The consent template comes from a 2018 practice guide | P03, P09 |
| Tax software SOC 2 review | Reviewed 2026-08-12 by the Office Manager and the Senior Tax Accountant: Type 2, period ending 2026-03-31, unmodified opinion, one remediated exception; RTO 4 h and RPO 1 h; U.S. data centers; MFA enforced for all customer users | P02, P05, P09 |
| Other device facts | The staff Wi-Fi password has not changed since 2021. MFP firmware has never been updated and is outside the MSP's scope. The portal has 5 staff accounts | P02, P04 |
| Languages | The Client Services Coordinator and the Tax Accountant are bilingual in Spanish and English; many of the firm's Florida clients prefer Spanish | P10 |
| AI review sample | On 2026-08-20 the Senior Tax Accountant and the Office Manager reviewed 24 AI-001 drafts from June and July (16 English, 8 Spanish) and 30 prompts. A May 2026 letter gave a client a 60-day response period when the IRS notice said 30; it was corrected by phone the next day. MFA was on for 2 of the 3 seats | P10 |
| Payroll engagement letters | Engagement letters for bookkeeping and payroll clients require the firm to tell the client without unreasonable delay about a breach affecting the client's data | P08 |
| Security budget | The Owner CPA approved about $6,900 one-time and $2,930 a year for 2026 Q4 treatments | P01 |

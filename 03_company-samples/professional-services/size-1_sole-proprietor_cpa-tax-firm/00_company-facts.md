# Scenario facts: Cris Santos Company | Professional, Scientific, and Technical Services | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or IRS publication, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the CPA-owner files Schedule C and is the firm's only preparer) |
| Business | CPA and tax preparation practice (NAICS 541211). Individual income tax returns and tax planning (about 70% of receipts), business entity returns plus monthly bookkeeping and payroll for small-business clients (about 20%), and IRS and state notice representation (about 10%). **No attest work** (no audits, reviews, or compilations), so no peer review and no AICPA attest independence questions |
| Location | Florida. A home office in the owner's house: a separate room with a locked file cabinet. Clients drop off paper documents by appointment or mail them |
| Workforce | The CPA-owner only (0 employees). Uses contracted services instead of staff. In the 2025 filing season a retired CPA worked as an independent contract preparer from 2025-02-03 to 2025-04-15; nobody was engaged for 2026 |
| Clients | About 380 individual income tax returns (Form 1040 series) a year, covering about 600 individual consumers (spouses on joint returns counted separately); about 45 business, trust, and estate returns; 12 small businesses with monthly bookkeeping and payroll. About 30 client households are part-year Florida residents whose other home is in another state |
| Customer information held | Records on about 1,450 consumers: current clients plus former clients whose files are still kept. Electronic files go back to 2014 and paper source documents to 2019, because no disposal schedule exists (gap 7) |
| Revenue | About $180,000 a year (fictional). About 60% is earned from February to April: about $1,700 per business day in filing season and about $400 per business day in the rest of the year. SBA-small (standard $26.5 million for NAICS 541211; 13 CFR 121.201) |
| GLBA status | **Financial institution under the FTC Safeguards Rule.** 16 CFR 314.2(h)(2)(viii) names "an accountant or other tax preparation service that is in the business of completing income tax returns", and 314.1(b) lists "tax preparation firms". An individual who "becomes your client for the purpose of obtaining tax preparation" services has a customer relationship (314.2(e)(2)(i)(H)). **The 314.6 exception applies**: customer information on about 1,450 consumers is fewer than 5,000, so 314.4(b)(1), (d)(2), (h), and (i) do not apply |
| IRS status | Tax return preparer under IRC 7216 (26 CFR 301.7216-1(b)(2)); holds a PTIN, renewed each year on Form W-12. Authorized IRS e-file Provider acting as an Electronic Return Originator (ERO) with one EFIN; the owner is the Responsible Official. Returns are transmitted through the tax software vendor, which is itself an Authorized IRS e-file Provider and software developer. The owner practices before the IRS as a CPA under Circular 230 (31 CFR Part 10) |
| Contrast worth noting | If customer information reached 5,000 consumers (about 3.4 times today's count), the four 314.6 exceptions would end and the written risk assessment, penetration testing and vulnerability scans, written incident response plan, and annual report to a senior officer would all become mandatory. The test is the number of consumers, not headcount or revenue |
| Not in scope | HIPAA as a business associate (N54-R06): no engagement requires PHI from a covered entity, and the engagement letter process declines such work. FAR 52.204-21, DFARS 252.204-7012, and CMMC (N54-R04, N54-R05): no federal contracts or subcontracts. ABA Model Rules (N54-R07): not a law firm. SEC and PCAOB: no public company clients. SOC examinations: the firm performs none. CIRCIA (N54-R09): proposed only. Payment cards: clients pay by check or through the practice management vendor's hosted payment page; card data never touches the firm's systems |
| Professional standards | The AICPA Code of Professional Conduct confidentiality rule (N54-R08) is noted but not assessed, because its text was not verified from the source |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: data security, breach notice, and disposal (Fla. Stat. 501.171(2), (3)-(6), (8)). Clients who live in other states are handled generically ("each state where affected individuals reside") |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| CPA-owner | Every role: owner, only preparer and signer, **Qualified Individual** under 16 CFR 314.4(a) (not designated in writing before 2026-08-31), e-file Responsible Official, risk acceptor, incident lead, and owner of every AI use |
| On-call IT consultant | Hourly help with the laptop, router, printer-scanner, and SaaS settings. Connects by a remote-support tool only when the owner starts a session. **A services agreement with confidentiality and security terms, and the written IRC 6713 and 7216 notice required by 26 CFR 301.7216-2(d)(2), were signed on 2026-07-23. Before that date the consultant had remote access to the laptop since 2023 with neither** |
| Tax software vendor | Hosts the tax preparation and e-file software and the client portal add-on; transmits returns to the IRS and states. Provides a SOC 2 Type 2 report. A tax return preparer in its own right under 301.7216-1(b)(2)(i)(B) |
| Outside breach counsel | Not yet engaged. The professional liability carrier's breach hotline refers counsel (see section 7) |
| Former contract preparer (2025 season only) | A retired CPA paid per return in the 2025 season under a short written agreement with a confidentiality clause. A tax return preparer under 301.7216-1(b)(2)(i)(C) while engaged |

## 3. Systems
| ID | System | Hosting | Holds customer information? | Notes |
|---|---|---|---|---|
| SYS-01 | Professional tax preparation and e-file software | Vendor-hosted SaaS | Yes | System of record for returns. **The vendor enforces MFA** (authenticator app on the owner's phone). Includes an AI document extraction feature that is **not turned on** |
| SYS-02 | Client document portal with e-signature (an add-on module from the tax software vendor) | Vendor SaaS | Yes | Clients upload documents, sign Forms 8879 and engagement letters, and download returns. About 35% of individual clients use it. **Client MFA is optional** |
| SYS-03 | Business email, calendar, and file storage suite | SaaS (business plan) | Yes (attachments; client folders by year back to 2014) | **MFA off**: it was turned on in 2024 and turned off the next day because the printer-scanner's scan-to-email stopped working. The email password is also used for SYS-04. File version history is kept 30 days; no other backup |
| SYS-04 | Practice management, time and billing, with a vendor-hosted payment page | Vendor SaaS | Yes (client list, engagement letters, invoices) | **MFA available but off** |
| SYS-05 | Laptop and multifunction printer-scanner | Owner devices | Yes (downloads; scans) | Laptop full-disk encryption on (set up by the IT consultant in 2023). The printer-scanner stores the email password for scan-to-email |
| SYS-06 | Mobile phone | Personal device | Yes (texts, photos, email app) | Holds the SYS-01 authenticator. Clients text photos of documents; the camera roll syncs to a **personal photo backup account** |
| SYS-07 | Home office network | Internet provider's router in the home | Yes (in transit) | **One network shared with family devices and smart-home devices**; router admin password is the default printed on the label |
| SYS-08 | Generative AI assistant (individual paid plan, web and phone app) | Vendor SaaS | Yes (uploaded client documents and pasted notice text) | Used since 2026-02 to summarize brokerage statements and K-1s and draft IRS notice responses. **The setting that lets the vendor use chats to improve its models was on until 2026-07-27**; see P10 |
| SYS-09 | Accounting SaaS | Vendor SaaS | Limited (the firm's own books) plus accountant-user access to 12 bookkeeping clients' own accounting files | Those client platforms enforce MFA for accountant users. Client payroll is run in the clients' own payroll services |

**SSP system (P02):** the *Tax Practice Systems Profile*: SYS-01 to SYS-09 as one boundary, built around the tax preparation software and client document portal (SYS-01 and SYS-02) and including the email, files, devices, home network, and SaaS tools used to reach them.

## 4. Current security posture: informal (basic hygiene, big gaps)
**In place today:**
- MFA on the tax software (enforced by the vendor) and on the accountant logins to clients' accounting files (enforced by those platforms)
- Full-disk encryption on the laptop; passcode on the phone
- Automatic operating system updates and built-in antivirus on the laptop and phone
- A business-plan email and file suite (not a consumer account) whose terms include a data protection addendum
- A signed engagement letter for every client each year, and an IRC 7216 consent form for the one routine third-party disclosure (release of a return to a client's mortgage lender on request)
- PTIN renewed and EFIN application current; e-file acknowledgments checked daily in filing season
- A cross-cut shredder and a locked file cabinet in the home office
- A professional liability policy with a data breach expense endorsement (section 7)

**Missing:**
1. No written information security program. The owner downloaded the IRS Pub. 5708 WISP template in 2024 but never completed it, while answering "Yes" each year to the Form W-12 question that preparers are required by law to keep a written information security plan. No written designation of the Qualified Individual (314.3(a); 314.4(a)).
2. No risk assessment ever performed (314.4(b)).
3. No MFA on the email and file suite or the practice management SaaS, and the same password is used on both (314.4(c)(5)).
4. Clients send documents as plain email attachments and as text-message photos; completed returns are emailed as attachments on request; client portal MFA is optional (314.4(c)(3)).
5. Customer information is spread across email, cloud folders, laptop downloads, the phone's camera roll and personal photo backup, the AI assistant's chat history, and paper, with no inventory of where it is (314.4(c)(2)).
6. No review of email sign-in history, forwarding rules, or tax software activity (314.4(c)(8)).
7. No retention or disposal schedule: electronic files back to 2014 and paper back to 2019; IRS authorizations (Forms 2848 and 8821) for former clients never withdrawn (314.4(c)(6); IRS Pub. 4557).
8. Service providers not overseen: no vendor list, no review of their safeguards, and the IT consultant had no written terms or IRC 7216 notice until 2026-07-23 (314.4(f); 301.7216-2(d)(2)).
9. No incident response plan or contact list. The owner did not know the IRS e-file next-business-day reporting rule (Pub. 1345) or Florida's 30-day notice clock (Fla. Stat. 501.171(4)).
10. No call-back rule: requests from clients by email to change the refund direct deposit account or mailing address are acted on without a phone call to a known number.
11. The home network is shared with family and smart-home devices, and the router still has its default admin password.
12. Client documents and notice text were put into a general-purpose generative AI assistant with no IRC 7216 analysis, and with the model-improvement setting on (P10).
13. No security training beyond continuing professional education on ethics; nothing on phishing or business email compromise (314.4(e)).
14. Single-person dependency: no written arrangement with another CPA to finish returns or file extensions if the owner is incapacitated in filing season, and the tax software's second factor is on one phone with no recovery codes stored.
15. The email and file suite has no backup beyond 30 days of version history, and local laptop files are not backed up.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 regulations | Primary: FTC Safeguards Rule, 16 CFR Part 314 (N54-R01), with the 314.6 exceptions applied. Also checked: IRC 7216 and 26 CFR 301.7216-1 to -3 (N54-R02), the IRS e-file and PTIN duties and Pub. 4557 guidance (N54-R03), and the Florida duties in Fla. Stat. 501.171 |
| P08 incident | Business email compromise of the owner's mailbox (no MFA) leading to theft of client tax documents from email and cloud folders, and fraudulent returns filed with stolen client data. The registry default fits this firm as it is |
| P09 SOC 2 | The firm is not a service organization and would not obtain a SOC 2 report. Security criteria only: (A) the owner's self-check, used to answer bookkeeping clients' security questions, and (B) a review of the tax software vendor's SOC 2 Type 2 report |
| P10 AI | The registry default "Generative AI for tax and document preparation" is kept and narrowed to the one third-party tool the owner actually uses: the general-purpose generative AI assistant (SYS-08). The tax software's AI extraction feature is listed in the inventory as not turned on |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-23 | IT consultant signs a services agreement with confidentiality and security terms and receives the written IRC 6713 and 7216 notice |
| 2026-07-27 to 2026-07-31 | Self-assessment with the IT consultant: BIA 2026-07-27; vendor SOC 2 review 2026-07-28; control tests 2026-07-29; gap analysis 2026-07-30; risk register 2026-07-31 |
| 2026-08-24 | AI use assessment completed |
| 2026-08-31 | Deliverables adopted by the CPA-owner |
| 2026-10-15 | Extension deadline for individual returns; most remediation is scheduled around it and finished before the 2027 filing season (target 2027-01-15) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Refund diversion near miss | On 2026-02-09 an email from a client's real address asked to change the refund direct deposit account on her return. The wording seemed odd, so the owner phoned her on the number on file; her mailbox had been taken over. No change was made. The call was the owner's own idea, not a rule | P01, P03, P08 |
| Phishing near miss | On 2026-03-09 the owner opened a "new client documents" link to a look-alike sign-in page for the email suite, typed the email address, recognized the page, and closed it without entering the password. Nothing was reported and MFA was not turned on | P01, P08 |
| Former contract preparer account | The 2025 contract preparer's user account in the tax software was still active (last sign-in 2025-04-14). Found in the P07 account test on 2026-07-29 and disabled that day; no sign-in after 2025-04-14 appears in the vendor's audit log | P01, P07, P09 |
| Mailbox rules check | On 2026-07-29 the owner and the IT consultant checked the mailbox for forwarding rules, delegates, and connected apps: none unknown. The suite keeps sign-in history for 30 days, so nothing earlier than 2026-06-29 could be reviewed | P07, P08 |
| Scan-to-email | The printer-scanner sends scans to the owner's mailbox using the mailbox password over a basic sign-in method. This is why MFA was turned off in 2024. The IT consultant confirmed on 2026-07-29 that the device can instead scan to a folder on the laptop, which removes the conflict | P02, P04, P07 |
| Tax software vendor assurance | The tax software vendor provided its SOC 2 Type 2 report (Security and Availability; the client portal module is in scope; the AI extraction feature is not) under a nondisclosure agreement. The owner reviewed it with the IT consultant on 2026-07-28 | P02, P04, P09 |
| Insurance | No standalone cyber policy. The professional liability policy has a data breach expense endorsement with a $25,000 sublimit; confirmed with the agent on 2026-07-30. It requires notice to the carrier's breach hotline before hiring outside vendors, and the hotline refers breach counsel | P01, P08 |
| AI assistant use | From 2026-02-02 to 2026-07-24 the owner uploaded documents (brokerage composite 1099s, K-1s, and three prior-year returns from new clients) or pasted IRS notice text for about 70 clients, about 95 individual consumers counting spouses. Full SSNs appeared on the three prior-year returns and on 9 K-1s; the other documents showed masked numbers. On 2026-07-27 the owner stopped putting client information into the tool, turned off the model-improvement setting, and deleted those chats | P01, P03, P10 |
| AI output errors | Reviewing the chat history on 2026-07-27 found two errors, both caught before anything was filed or sent: a draft notice response cited a Code subsection that does not exist, and a summary of a composite 1099 left out the wash sale loss disallowed amount (found when the owner reconciled to the form totals) | P01, P10 |
| IRS authorizations | IRS powers of attorney and tax information authorizations are still on file for about 40 former clients | P03, P06 |
| Transmission counts | The P07 test on 2026-07-29 counted 37 returns emailed to clients as plain attachments in the 2026 season and 212 photos of client documents in the phone's camera roll (counted, not opened) | P07, P01 |
| Contract preparer account set-up | The 2025 contract preparer's tax software account was created after a phone call, with no written approval, and had the preparer role (not administrator) | P07, P09 |
| Mailbox contents | The owner's mailbox and synced client folders hold documents on more than 500 consumers, so a full mailbox compromise could reach the FTC 500-consumer threshold | P03, P08 |
| Consent records | Nine lender releases in 2026 were each made after the client signed the IRC 7216 consent in the portal; the portal stores signed Forms 8879 back to 2019; five signed Forms 8879 were checked for the e-signature identity record | P03 |
| Tax software vendor SOC 2 details | 12-month period ending 2026-03-31; unqualified opinion; one exception (2 of 40 sampled departing vendor staff kept access 3 days against a 1-day standard; remediated); RTO 4 hours and RPO 1 hour in the system description; customer incident notice promised with no number of days; bridge letter requested 2026-07-28 | P02, P04, P05, P09 |
| Device and remote access settings | Laptop locks after 5 minutes idle and the phone after 1 minute. The IT consultant's remote-support tool has no unattended access; whether the consultant's own tool account uses MFA is not yet confirmed (due 2026-09-30) | P01, P02, P07 |
| Accountant access | The 12 bookkeeping clients each invited the owner as an accountant user to their own accounting files | P07 |
| Budget figures (fictional) | Password manager about $40 a year; backup service for the suite about $60 a year; security course about $150; IT consultant about $120 an hour; attorney time for the sealed envelope about $300 | P01, P07 |
| Tabletop figures | The P08 worked example (dates in February 2027; about 640 consumers, about 590 Floridians) is a hypothetical exercise script, not an event that happened | P08 |

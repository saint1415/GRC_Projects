# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (CPA and tax preparation practice) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | CPA-owner (Qualified Individual) |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, before each PTIN renewal, and after a new system, a new vendor, any helper or contract preparer, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-7, RA-2, RA-3, CA-2, CA-7, SA-4, SA-9, AC-2, AC-11, AC-17, AU-6, CM-3, CM-8, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, AT-3, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-06, GV.SC-07, ID.AM-01, ID.AM-07, ID.AM-08, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.IR-01, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Regulatory basis | FTC Safeguards Rule, 16 CFR 314.3 and 314.4 (N54-R01); IRC 7216 and 26 CFR 301.7216 (N54-R02); IRS Pubs. 1345, 4557, 5708 (N54-R03); Fla. Stat. 501.171 |

## 1. Purpose
Protect the security, confidentiality, and integrity of client tax return information and other customer information, and meet the FTC Safeguards Rule and IRC 7216 in a way that one person can actually run. **This policy, with the risk register (P01), the system profile (P02), and the incident runbook (P08), is the firm's written information security program (16 CFR 314.3(a)), the "WISP" that IRS Pubs. 4557 and 5708 and Form W-12 refer to.** Each rule below is written so it can be checked (P07).

## 2. Scope
All client and firm information in any form (electronic, paper, spoken), on every system in the Tax Practice Systems Profile (SYS-01 to SYS-09), on paper in the home office, and at every service provider that handles it. It applies to the CPA-owner and to any future employee, helper, or contract preparer. Contractors are bound through their agreements.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Qualified Individual (16 CFR 314.4(a)) and program owner | CPA-owner | Runs this policy; decides incident and notice questions with counsel; keeps records |
| e-file Responsible Official | CPA-owner | IRS e-file duties, including the security incident report (Pub. 1345) |
| Risk acceptor | CPA-owner | Accepts or treats every risk (4.4) |
| On-call IT consultant | Contractor (services agreement and IRC 7216 notice since 2026-07-23) | Technical help on request; no standing access |
| Service providers | Tax software vendor, email and file suite, practice management, accounting SaaS, AI assistant vendor | Operate their safeguards under contract |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The firm must maintain a written information security program made up of this policy, P01, P02, and P08, listed in Appendix A. (PM-1; GV.PO-01; 314.3(a))
4.2 The CPA-owner is designated in writing, by this policy, as the Qualified Individual responsible for overseeing, implementing, and enforcing the program. (PM-2; GV.RR-02; 314.4(a))
4.3 A risk assessment must be done every July and after any material change, using NIST SP 800-30 Rev. 1, and kept in writing even though 314.6 does not require the written form. Every risk must have a treatment and a due date. (RA-3; PM-9; 314.4(b), (b)(2))
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every July (P07). At least every second year the evaluation must include review by someone outside the practice, such as the IT consultant or another CPA's IT adviser. (CA-2; 314.4(d)(1), (g))
4.6 This policy must be reviewed every July and before each PTIN renewal. (PL-1; GV.PO-02; Form W-12 line 11)
4.7 Each July the owner must count the consumers whose information the firm keeps. If the count nears 5,000, the owner must plan for the 314.4(b)(1), (d)(2), (h), and (i) duties that the 314.6 exception no longer covers. (PM-9; 314.6)

## 5. Sanctions and exceptions
5.1 Any future employee, helper, or contract preparer must sign an agreement that binds them to this policy and to IRC 7216, and a breach must lead to retraining, ending the engagement, or both, in proportion to intent and harm. Each case must be documented. (PL-4; PS-7)
5.2 A service provider that breaks its contract or this policy must be dealt with under its contract, up to ending it. (SA-9)
5.3 The owner must record any personal departure from this policy as an exception under 5.4.
5.4 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Service providers and contractors
6.1 **No terms, no client data.** No service provider may receive, store, or process client information until a contract requires it to protect that information. (SA-9; GV.SC-05; 314.4(f)(2))
6.2 The owner must keep a vendor list showing each provider, the client data it handles, and the contract date. (SA-9; ID.AM-01; 314.4(f)(1))
6.3 Before any new application, SaaS service, or new feature of an existing one (including AI features) is used with client data, the owner must complete the one-page pre-adoption checklist: data handled, where it is processed, training or secondary use, MFA, contract terms, and the IRC 7216 basis. (SA-4; GV.SC-06; 314.4(c)(4))
6.4 The tax software vendor's SOC 2 report must be reviewed every July, and the owner must operate the customer controls that report lists. Other providers are reviewed every July against the vendor list. (SA-9; GV.SC-07; 314.4(f)(3))
6.5 Every individual at a contractor who may see tax return information while maintaining or repairing equipment or software used for tax preparation must first sign the written notice of IRC sections 6713 and 7216. (PS-7; 301.7216-2(d)(2))
6.6 Remote support sessions must be started and watched by the owner. Unattended remote access must be off, and the contractor's remote-support account must use MFA. (AC-17)

## 7. Access control
7.1 Every person must have their own named account. Credentials must never be shared. (IA-2; AC-2; PR.AA-01; 314.4(c)(1)(i))
7.2 MFA must be on for every system that offers it: the tax software, client portal (for the owner and for every client), email and file suite, practice management, accounting SaaS, and the AI assistant. Any exception needs the Qualified Individual's written approval of an equivalent control. (IA-2(1); IA-2(2); PR.AA-03; 314.4(c)(5))
7.3 Passwords must be unique passphrases of at least 14 characters, kept in a password manager. Passwords must not be saved in the web browser or stored in devices such as the printer-scanner. (IA-5)
7.4 Any account for a helper or contract preparer must be approved in writing, limited to what the work needs, and disabled on the last day of the engagement. The owner must review the tax software users every quarter, and remove accountant access to a client's accounting file when that engagement ends. (AC-2; PR.AA-05; 314.4(c)(1)(i)-(ii))
7.5 The laptop must lock after 5 minutes idle and the phone after 1 minute. (AC-11)
7.6 **Emergency access.** Tax software and email recovery codes, the laptop recovery key, and a one-page access sheet must be kept in a sealed envelope held by the owner's attorney, for use under the continuation agreement (11.2). (AC-2; CP-2)
7.7 On the first business day of each month, and every Monday from February to April, the owner must review the mailbox sign-in history, forwarding rules, delegates, and connected apps, and the tax software activity log, and record the review in the security log. Every Monday in filing season the owner must also compare the returns filed under the firm's EFIN and the owner's PTIN with the firm's own count (IRS Pub. 4557). (AU-6; DE.AE-02; 314.4(c)(8))
7.8 **Change log.** Any change to a security setting (MFA, sharing, forwarding, device encryption, router) must be written in the security log with the date and reason, and must not weaken a rule in this policy unless an exception is approved under 5.4. (CM-3; 314.4(c)(7))

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Tax return information, SSNs, bank and brokerage account numbers, client source documents, Forms 8879, credentials | Approved locations only (8.2); encrypted; disclosed only as IRC 7216 permits (8.10) |
| **Confidential** | Engagement letters, invoices, the firm's own tax and bank records, this policy set | Encrypted storage; owner only |
| **Public** | Office hours, website, published rates | No restriction |

8.2 Restricted data may be kept only in the tax software and portal, the business email and file suite, the laptop's encrypted disk (working copies only), and the locked cabinet. It must not be kept in a personal account, a phone's camera roll or photo backup, or any tool not on the vendor list. (AC-3; CM-8; 314.4(c)(2))
8.3 Every device that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01; 314.4(c)(3))
8.4 Returns, source documents, and Forms 8879 must be exchanged through the client portal. They must not be sent as plain email attachments or by text message. If a client sends documents by email or text, the owner moves them to the client's folder and deletes them from the phone the same day, and reminds the client to use the portal. (SC-8; PR.DS-02; 314.4(c)(3))
8.5 **Call-back rule.** Any request to change a client's refund bank account, mailing address, or email address must be confirmed by phone, on the number already on file, before the return is changed or filed. The same applies to any request to change where the firm sends money or documents. (IA-2; 314.3(b)(3))
8.6 Paper with Restricted data must stay in the locked home office or locked cabinet and must never be left in a vehicle. (PE-3)
8.7 The email and file suite must be backed up by an encrypted backup service that keeps at least one year of versions. Client files must be kept in the suite, not only on the laptop. (CP-9; PR.DS-11; 314.3(b)(2))
8.8 Paper must be cross-cut shredded. Old laptops, phones, and the printer-scanner must be wiped (encrypted, then reset to factory settings) before reuse or disposal, or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))
8.9 **Retention.** The owner must keep a written retention schedule that gives the business or legal reason for each period, keeps Forms 8878 and 8879 for at least three years from the return due date or the IRS received date, whichever is later (Pub. 1345), and disposes of other customer information when its period ends. The schedule is reviewed every July. IRS authorizations for former clients must be withdrawn. (SI-12; ID.AM-08; 314.4(c)(6)(i)-(ii))
8.10 **IRC 7216.** Tax return information may be disclosed or used only for preparing the client's return, as 26 CFR 301.7216-2 permits, or with the client's prior written consent under 301.7216-3. Consent must be signed before the disclosure, must not be a condition of service, and the client gets a copy. SSNs of Form 1040 series filers must never be sent to anyone outside the United States. (PL-4; 26 U.S.C. 7216)

## 9. Acceptable use and training
9.1 The practice laptop and printer-scanner are for practice work only. Family members must not use them. (PL-4)
9.2 Devices must never be left in a vehicle or unattended outside the home office. (PL-4)
9.3 Automatic updates and the built-in antivirus must stay on. Software and apps must come only from the official app stores or the vendor's site, and new ones that touch client data go through 6.3 first. (SI-2; SI-3)
9.4 The router admin password must be changed from the default and the firmware kept current. Family and smart-home devices must use the guest network, separate from the laptop and printer-scanner. (SC-7; PR.IR-01)
9.5 **AI tools.** A generative AI tool may be used only after the pre-adoption checklist (6.3) and the P10 assessment, and only on its approved terms. No client name, SSN, account number, address, employer, or document may be entered unless P10 records an IRC 7216 basis confirmed by counsel. Every AI output that reaches a client or the IRS must be checked by the owner: every citation against the primary source, and every figure against the source document. (PL-4; SA-9; 301.7216-3(a)(1); 31 CFR 10.22)
9.6 The owner must complete a security course with phishing and business email compromise modules every year before filing season, and read the IRS Security Summit and tax professional security alerts. Any future helper must be trained before getting access. (AT-2; AT-3; PR.AT-01; 314.4(e)(1), (e)(3))

## 10. Incident response
10.1 The firm must keep the incident runbook (P08) with a printed contact list in the home office and a copy away from it. (IR-8; RS.MA-01)
10.2 Every suspected incident (phishing click, unknown sign-in, odd forwarding rule, lost device, misdirected email, e-file reject for a duplicate SSN, vendor notice) must be written in the incident log the same day, with the time it was discovered and, later, the time it was confirmed. (IR-5; IR-6; RS.MA-02; 314.4(j)(2))
10.3 A confirmed incident involving taxpayer information must be reported to the IRS through the local Stakeholder Liaison as soon as possible and no later than the next business day after confirmation. (IR-6; RS.CO-02; Pub. 1345)
10.4 Notices to the FTC, affected clients, the Florida Department of Legal Affairs, other states, and consumer reporting agencies must meet the deadlines in the P08 notification matrix, confirmed by counsel. (IR-6; RS.CO-02; 314.4(j); Fla. Stat. 501.171(3)-(5))
10.5 No extortion or ransom payment may be made without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year before filing season and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3; RC.RP-01)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep a written practice continuation agreement with another CPA who can file extensions and contact clients if the owner is incapacitated, with counsel's advice on how client information may be shared under IRC 7216. (CP-2)
11.3 When a hurricane watch is issued in filing season, the owner must take the laptop, phone, and paper files in progress and be ready to work from another location or file extensions. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.7. Exceptions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. WISP index, devices, and data locations (314.3(a); 314.4(c)(2))
**WISP parts:** this policy; P01 risk register; P02 system profile; P08 runbook and notification matrix; the vendor list (6.2); the retention schedule (8.9); the security log (7.7, 7.8) and incident log (10.2).

| Item | Restricted data held | Protection required |
|---|---|---|
| Tax software and client portal (SYS-01, SYS-02) | Returns, source documents, Forms 8879, consents | 7.2; 7.4; vendor SOC 2 review (6.4) |
| Email and file suite (SYS-03) | Client folders and correspondence | 7.2; 8.4; 8.7 |
| Practice management (SYS-04) | Client list, engagement letters, invoices | 7.2 |
| Laptop (SYS-05) | Working copies and downloads | 8.3; 7.5; 9.3 |
| Printer-scanner (SYS-05) | Scans in progress | Scan-to-folder; no stored password (7.3) |
| Phone (SYS-06) | Authenticator; client texts until moved | 8.3; 8.4; 7.5 |
| Accounting SaaS (SYS-09) | Clients' books and payroll data | 7.2; 7.4 |
| AI assistant (SYS-08) | None permitted (9.5) | 6.3; 9.5 |
| Locked cabinet | Paper source documents | 8.6; 8.8; 8.9 |

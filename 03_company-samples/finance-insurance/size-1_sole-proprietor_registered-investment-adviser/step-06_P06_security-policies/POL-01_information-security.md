# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (state-registered investment adviser) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-adviser |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new system, a new vendor, a hire, a move to SEC registration, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, CM-3, SA-4, SA-9, AC-2, AC-17, AC-19, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, AT-2(3), IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.SC-06, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Legal basis | FTC Safeguards Rule, 16 CFR 314.3 and 314.4 (N52-R03); GLBA section 501(b) (N52-R01); Fla. Stat. 501.171 and 517.121 |

## 1. Purpose
Protect the security, confidentiality, and integrity of client information and client money, and meet the FTC Safeguards Rule in a way one person can actually run. This policy, together with the risk register (P01), the system profile (P02), and the incident runbook (P08), is the adviser's **written information security program** under 16 CFR 314.3(a). Each rule below is written so it can be checked (P07).

## 2. Scope
All business information in any form (electronic, paper, spoken), including customer information (16 CFR 314.2(d)), on every system in the Advisory Practice Systems Profile (SYS-01 to SYS-10), on paper in the home office, and at every service provider that handles it. It applies to the owner-adviser and to any future employee or contractor. Service providers are bound through their contracts.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Qualified Individual (16 CFR 314.4(a)) | Owner-adviser | Oversees, implements, and enforces this program; decides breach questions; keeps records |
| Risk acceptor | Owner-adviser | Accepts or treats every risk (section 4.4) |
| On-call IT consultant | Contractor under a services agreement with security terms | Technical help on request; no standing access; annual assessment support |
| Service providers | Custodian, SaaS vendors, compliance consultant | Operate their safeguards; report incidents under their contracts |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The adviser must maintain a written information security program made up of this policy, P01, P02, and P08. (PM-1; GV.PO-01; 314.3(a))
4.2 The owner-adviser is designated in writing, by this policy, as the **Qualified Individual**. (PM-2; GV.RR-02; 314.4(a))
4.3 A risk assessment must be completed every July and after any material change (new system or vendor, a hire, SEC registration, an incident), using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9; 314.4(b); 314.4(b)(2))
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Key controls must be tested every July (P07). At least every second year, the test must include review by someone outside the business, such as the IT consultant. (CA-2; 314.4(d)(1))
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02; 314.4(g))
4.7 Security-relevant setting changes and every new tool must be written in the security log with the date and reason. (CM-3; 314.4(c)(7))

## 5. Sanctions and exceptions
5.1 **Sanctions.** Any future employee or contractor who breaks this policy must be dealt with in proportion to intent and harm: retraining, written warning, loss of access, or termination of employment or contract. Each action must be documented. (PS-8; GV.RR-04)
5.2 A service provider that breaks its contract or this policy must be dealt with under its contract, up to ending it. (SA-9)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. The owner must record any personal departure from this policy the same way. An exception to MFA (7.2) or encryption (8.3) must be approved in writing by the Qualified Individual with the compensating control named, as 314.4(c)(3) and (c)(5) require. (PL-1)

## 6. Service providers
6.1 No service provider may receive customer information until a written contract requires it to implement and maintain safeguards for it. (SA-9; GV.SC-05; 314.4(f)(2))
6.2 Before adopting any new tool that will hold customer information, the owner must check and record: MFA available, encryption at rest and in transit, contract terms (security, confidentiality, no model training, incident notice), and an assurance report or security questionnaire. (SA-4; GV.SC-06; 314.4(c)(4); 314.4(f)(1))
6.3 The owner must keep a vendor list (Appendix A) and review each vendor every July, including the SOC 2 report of the portfolio platform and any report the custodian provides, and must operate the customer controls those reports list. (SA-9; GV.SC-07; 314.4(f)(3))
6.4 Remote support sessions must be started and watched by the owner. Unattended remote access must be off. (AC-17)
6.5 Service provider contracts must require notice to the adviser of any security event affecting customer information as soon as possible. New and renewed contracts must include it. (SA-9; 314.4(j)(2))

## 7. Access control and money movement
7.1 Every person must have their own account. Credentials must never be shared. (IA-2; AC-2; PR.AA-01; 314.4(c)(1)(i))
7.2 MFA must be on for every service that holds customer information or can move money, including email, the custodian portal, the CRM, the portfolio platform, e-signature, financial planning, and accounting. An authenticator app or hardware key is preferred over text messages. (IA-2(1); IA-2(2); PR.AA-03; 314.4(c)(5))
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager. (IA-5; 314.4(c)(1)(i))
7.4 Business devices are for the owner's business use only. Family members must not use them. (AC-2; PL-4)
7.5 The laptop must lock after 5 minutes idle and the phone after 1 minute. (AC-2; 314.4(c)(1)(i))
7.6 **Callback rule.** Before submitting any request to move money, change bank instructions, or change a client's address, email, or phone, the owner must call the client at the phone number already on file in the CRM (never a number in the request) and confirm the details. The call must be recorded in the CRM with the date and time. A request that cannot be confirmed must not be submitted. The same rule applies to any request that appears to come from the custodian. (AT-2(3); PR.AA-05; 314.3(b)(3))
7.7 **Emergency access.** Recovery codes for the custodian portal, email, and CRM, and a one-page emergency access sheet, must be kept in a sealed envelope held by the owner's attorney. A hardware security key must be registered as a second MFA method and kept in the home safe. (AC-2; CP-2)
7.8 On the first business day of each month, the owner must review email sign-in history, mailbox forwarding and inbox rules, connected third-party apps, and new or changed money movement beneficiaries, and note the review in the security log. (AU-6; DE.AE-02; 314.4(c)(8))

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer information: SSNs, account numbers, ID images, statements, tax returns, credentials | Approved systems only (8.2); encrypted; minimum necessary |
| **Confidential** | Business contracts, fee records, this policy set | Encrypted storage; owner only |
| **Public** | Form ADV Part 2 brochure, website | No restriction |

8.2 Restricted data may be kept only in the systems listed as approved in Appendix A. It must not be kept in a personal account, a phone photo roll, or a consumer app, and must never be entered into a consumer AI tool. (AC-3; SA-9; 314.4(c)(2))
8.3 Every device or drive that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01; 314.4(c)(3))
8.4 Restricted data must be shared outside the approved systems only through the custodian's or e-signature vendor's secure channel or an expiring secure link, never as an ordinary email attachment. (SC-8; PR.DS-02; 314.4(c)(3))
8.5 Email and files must be backed up to an encrypted second cloud location with at least 1 year of retention. The USB copy must be encrypted, connected only during the copy, and kept in the home safe. (CP-9; PR.DS-11; Fla. Stat. 517.121)
8.6 Books and records must be kept for the periods Florida requires, with the records index in Appendix A. (SI-12; Fla. Stat. 517.121(1))
8.7 Paper with Restricted data must be cross-cut shredded. Old devices and drives must be wiped (encrypted, then reset) or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; ID.AM-08; 314.4(c)(6)(i); Fla. Stat. 501.171(8))
8.8 Records on former clients must be deleted two years after the relationship ends unless a law, including Florida's books and records rule, or a legitimate business need requires keeping them. The schedule is reviewed and applied every January. (SI-12; 314.4(c)(6))
8.9 Security documentation (this policy, risk assessments, test results, incident records, vendor reviews) must be kept for at least 5 years. (SI-12)

## 9. Acceptable use and training
9.1 Business work must use the business devices, over the separate business network or the phone hotspot. (SC-7; PL-4)
9.2 Automatic updates and the built-in antivirus must stay on. Software must come only from official app stores or the vendor's site. (SI-2; SI-3)
9.3 Devices must never be left in a vehicle or unattended outside the home office. (PL-4)
9.4 **AI tools.** An AI tool may receive client information only after a written P10 assessment, a business plan whose terms bar model training, and the owner's written approval. Account numbers and SSNs must never be entered. Every figure in an AI-assisted client document must be checked against the custodian statement before it is sent. Recording a client call requires every party's prior consent (Fla. Stat. 934.03). (PL-4; SA-9)
9.5 The owner must complete a security awareness course every year that covers business email compromise and payment fraud, and read monthly security reminders. Any future employee must be trained before getting access. (AT-2; AT-2(3); PR.AT-01; 314.4(e)(1), (e)(3)-(4))

## 10. Incident response
10.1 The adviser must keep an incident runbook (P08) with a printed contact list in the home office and in the owner's bag. (IR-8; RS.MA-01)
10.2 Every suspected incident (phishing click, unknown sign-in, strange forwarding rule, disputed money movement, lost device, vendor notice) must be written in the incident log the same day, with the date and time it was discovered. (IR-5; IR-6; RS.MA-02; 314.4(j)(2))
10.3 A suspected fraudulent money movement must be reported to the custodian's fraud line immediately, before anything else. (IR-4)
10.4 Notices to affected individuals, the Florida Department of Legal Affairs, other states, and the FTC must meet the deadlines in the P08 notification matrix, confirmed by counsel. (IR-6; RS.CO-02; 314.4(j); Fla. Stat. 501.171)
10.5 No ransom or extortion payment may be made without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-8; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep a written arrangement with another Florida-registered adviser to serve clients if the owner is incapacitated, and must tell clients how to reach the custodian directly. (CP-2)
11.3 A printed client contact list must be kept in the locked file cabinet for callbacks when systems are down. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control test (P07) and the monthly review in 7.8. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Data locations, vendors, and records index (314.4(c)(2); 517.121)
| System | Restricted data held | Approved for Restricted data? | Protection required | Contract with safeguards |
|---|---|---|---|---|
| Custodian advisor portal (SYS-01) | Records of account; statements | Yes | 7.2 | Custodial and adviser agreements |
| Portfolio and billing platform (SYS-02) | Holdings, fees, performance | Yes | 7.2 | Terms with security commitments; SOC 2 |
| CRM (SYS-03) | Client identity, contact, onboarding files, callback log | Yes | 7.2 | Standard terms; review due 2026-10-31 |
| Email and file suite (SYS-04) | Correspondence; documents; records | Yes | 7.2; 8.4; 8.5 | Data protection addendum |
| Financial planning software (SYS-05) | Planning data | Yes | 7.2 | Standard terms; review due 2026-10-31 |
| E-signature (SYS-06) | Signed agreements and forms | Yes | 7.2; 7.6 | Standard terms; review due 2026-10-31 |
| Laptop and phone (SYS-07) | Synced files; MFA app | Yes | 7.5; 8.3 | Owner device |
| Encrypted USB drive (SYS-07) | Backup copy | Yes, once encrypted | 8.3; 8.5 | Owner device |
| Generative AI assistant (SYS-09) | None allowed | **No** | 9.4 | Consumer terms |
| Accounting SaaS (SYS-10) | Client names and fees | Yes (Confidential) | 7.2 | Standard terms |
| Locked file cabinet | Signed paper forms; printed contact list | Yes | 8.7 | Not applicable |

**Records index.** Advisory agreements (SYS-06 and SYS-04); client profiles and onboarding (SYS-03); trade and fee records (SYS-01 and SYS-02); client correspondence (SYS-04); Form ADV and compliance files (SYS-04). The list and periods are confirmed against Rule 69W-600, F.A.C., by the compliance consultant (P03 G-039).

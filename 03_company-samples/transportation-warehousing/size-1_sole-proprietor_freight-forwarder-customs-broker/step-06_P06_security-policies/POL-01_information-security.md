# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight forwarder and customs broker) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner (licensed customs broker) |
| Effective date | 2026-09-15 (adopted 2026-09-14) |
| Review cycle | Every August with the risk assessment, and after a new system, a new vendor, a first employee, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, SA-9, AC-2, AC-3, AC-11, AC-17, AC-19, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, AT-2(3), IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-11, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Rules it answers | 19 CFR 111.3, 111.21, 111.23 to 111.26, 111.28, 111.29, 111.39(b); 19 CFR 163.5; 46 CFR 515.33; Fla. Stat. 501.171(2), (3)-(4), (8) |

## 1. Purpose
Protect client records, client money, and the broker license by keeping the business's information confidential, correct, and available, in a way one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All business information in any form (electronic, paper, spoken), including customs records, powers of attorney (POAs), importer of record numbers, export information, and payment details, on every system in the Core Brokerage SaaS Stack (SYS-01 to SYS-10), in the home office, and at every vendor that handles it. It applies to the owner and to any future employee. Contractors are bound through their engagement terms.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security officer, recordkeeping contact (111.21(d)), CBP point of contact (111.3(b)) | Owner | Runs this policy; decides breach questions; keeps records |
| Risk acceptor | Owner | Accepts or treats every risk (section 4.4) |
| Contract bookkeeper | Contractor | Monthly reconciliation through a named, limited account |
| On-call IT consultant | Contractor | Technical help on request; no standing access |
| Vendors | Customs software vendor, email and file suite provider, accounting SaaS provider, bank | Operate their safeguards under their terms |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01; Fla. Stat. 501.171(2))
4.2 The owner is designated in writing, by this policy, as the security officer, the person responsible for brokerage-wide recordkeeping, and CBP's point of contact. (PM-2; GV.RR-02; 111.21(d); 111.3(b))
4.3 A risk assessment must be completed every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every August (P07). At least every second year, the evaluation must include review by someone outside the business, such as the IT consultant or another broker's security adviser. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Contractors, workforce, and exceptions
5.1 Every contractor who can see client records must have written confidentiality terms, and must be named in the client authorization in 6.1. (SA-9; 111.24)
5.2 Before any future employee gets access, the owner must train the employee, submit the employee information CBP requires within 30 days (111.28(b)), and store that information as Restricted data. Breaking this policy leads to retraining, warning, or termination, documented and kept 5 years. (PS-8; GV.RR-04)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Vendors and client authorization
6.1 **Client records go only where the client has agreed in writing.** Client records may be shared only with the client, its surety, DHS or other accredited U.S. officers, on subpoena or court order, or with a service provider named in the client's written authorization. (SA-9; GV.SC-05; 111.24)
6.2 The owner must keep a vendor list showing each vendor, the client records it handles, where it stores them, and its terms. (SA-9; GV.SC-05)
6.3 The customs software vendor's SOC 2 report must be reviewed every year, and the owner must operate the customer controls that report lists. (SA-9; GV.SC-07)
6.4 Remote support sessions must be started and watched by the owner. Unattended remote access must be off. (AC-17)
6.5 Broker records, including electronic records, must be stored within the customs territory of the United States. The storage region of each service that holds records must be confirmed and recorded. (SA-9; 111.23(a))

## 7. Access control
7.1 Every person must have their own account. Credentials must never be shared. Only the owner may use the customs software and the CBP portals. (IA-2; AC-2; PR.AA-01; 111.33; 111.37)
7.2 MFA must be on for every service that offers it, using the authenticator app where available. App passwords and legacy sign-in methods that skip MFA must be off. (IA-2(1); IA-2(2); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager. Default passwords on any device (router, printer) must be changed before use. A password must be changed at once when compromise is suspected or when anyone who knew it leaves. (IA-5)
7.4 The bookkeeper must use a named account with the least role that allows reconciliation. The owner must review the user list of every service each quarter. (AC-2; PR.AA-05)
7.5 The laptop must lock after 5 minutes idle and the phone after 1 minute. (AC-11)
7.6 **Emergency access.** Recovery codes for the customs software, email, and bank, and a one-page emergency sheet naming the backup broker and a records custodian, must be kept in a sealed envelope held by the owner's attorney. (AC-2; CP-2; 111.30(e))
7.7 On the first business day of each month, the owner must review sign-in history for email, the customs software, and the bank, check email forwarding rules, check the eCBP point of contact details, and note the review in the security log. (AU-6; DE.AE-02)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Client records, POAs, importer of record numbers (including Social Security numbers), payment details, credentials | Approved systems only (8.2); encrypted; shared only under 6.1 |
| **Confidential** | Business contracts, tax and bank records, this policy set | Encrypted storage; owner and bookkeeper only |
| **Public** | Website, published rates | No restriction |

8.2 Restricted data may be kept only in: the customs software, the business email and file suite, the accounting SaaS, and online banking. It must not be kept in a consumer app, a personal account, or a phone camera roll. (AC-3; SA-9)
8.3 Every device that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01)
8.4 **Scanned records.** Paper originals must be kept until 30 days after the alternative storage notice has been sent to CBP Regulatory Audit (163.5(b)(1)). Scans must follow the written scanning and retrieval procedure and the naming rule: client code, entry or booking number, document type, date. (SI-12; 163.5(b)(2)(i)-(ii); 111.25(a))
8.5 Documents and advice received or given through the phone or a messaging app must be saved to the shipment file the same day and then deleted from the chat and the camera roll. (AC-19; SI-12; 111.21(a); 111.39(c); 46 CFR 515.33(b))
8.6 **Payment changes.** Before paying a new payee or using changed bank details, the owner must call the carrier, agent, or client on a number already on file (never one in the request) and record the call in the payee change log. Clients must be told in writing that the business never changes its own bank details by email. (AT-2(3); 111.29(a))
8.7 The records archive must have a backup in a separate account that the laptop cannot change, kept with versions for at least 90 days, and restored as a test every quarter. (CP-9; PR.DS-11; 163.5(b)(2)(vi); 111.25(b))
8.8 Paper with Restricted data must be cross-cut shredded. Old devices must be encrypted and reset before reuse, or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))
8.9 **Retention.** Customs records must be kept at least 5 years after the date of entry; POAs until revoked, and revoked POAs for 5 years after revocation or after the client stops being active, whichever is later; export records 5 years from export; FMC shipment files 5 years. Purges happen once a year with a record, and stop at once if DHS or another agency asks for, or may ask for, the records. Security documentation is kept 5 years. (SI-12; 111.23(b); 111.26; 15 CFR 30.10(a); 46 CFR 515.33)

## 9. Acceptable use and training
9.1 The work laptop is for business. Household members must not use it. (PL-4)
9.2 Customs business must be done from within the customs territory of the United States. The laptop must not be left in a vehicle or unattended outside the home. (PL-4; 111.3(a))
9.3 Automatic updates and the built-in antivirus must stay on. Software must come only from official app stores or the vendor's site. (SI-2; SI-3)
9.4 Business devices must use the business Wi-Fi network, not the household network, once it is set up. (SC-7)
9.5 **AI tools.** An AI tool may receive client records only after a written assessment (P10), business terms that bar training on business data, and client authorization under 6.1. AI and document capture output is a research lead or a draft: the owner must check every classification against the tariff schedule and CBP rulings and record the basis in the shipment file before filing or advising. (PL-4; SA-9; 111.28(a); 111.39(b))
9.6 The owner must complete a small-business security course every year, including payment fraud and phishing, in addition to continuing broker education. Any future employee must be trained before getting access. (AT-2; AT-2(3); PR.AT-01; 111.102(b))

## 10. Incident response
10.1 The business must keep an incident runbook (P08) with a printed contact list in the home office and in the car. (IR-8; RS.MA-01)
10.2 Every suspected incident (phishing click, strange sign-in, payment request that fails the call-back, lost phone, ransomware note, vendor notice) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 Any known breach of electronic or physical customs records must be reported to the CBP Security Operations Center electronically within 72 hours of discovery, with known compromised importer identification numbers, followed by an updated list within 10 business days. (IR-6; RS.CO-02; 111.21(b))
10.4 Notices to individuals, the Florida Department of Legal Affairs, other states, and clients must meet the deadlines in the P08 notification matrix, confirmed by counsel. (IR-6; Fla. Stat. 501.171(3)-(4))
10.5 No ransom may be paid without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep a written coverage agreement with a backup licensed broker for urgent entries and CBP holds when the owner is unavailable, and offer clients a standby POA with that broker. (CP-2; 111.3(b))
11.3 A wiped spare laptop must be kept ready, and the next week's arrivals list printed each Friday. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.7. Section 5 covers contractors and any future workforce.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices and data locations
| Item | Restricted data held | Protection required |
|---|---|---|
| Customs software | Entries, POAs, importer of record numbers | 7.1; 7.2; 6.3 |
| Email and file suite | Correspondence; scanned records archive | 7.2; 6.5; 8.7 |
| Accounting SaaS | Client ledgers, bank details | 7.2; 7.4 |
| Online banking | Payees, payments | 7.2; 8.6 |
| Laptop (2024) and spare (2019, after wipe) | Synced archive, downloads | 8.3; 7.5; 9.3; 8.8 |
| Phone | Second factors; chats until filed | 8.3; 8.5; 7.5 |
| Locked cabinet | Paper POAs and originals | Locked; 8.4; 8.8 |

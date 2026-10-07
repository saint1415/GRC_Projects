# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (sole proprietorship) and its wholly owned LLCs: CSC Self Storage, LLC; CSC Rentals, LLC; CSC Laundry, LLC |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-manager, for the sole proprietorship and, as sole member and manager, for each LLC |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after buying or selling a business, a new system or vendor, a new employee at any LLC, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-4, PS-7, PS-8, RA-2, RA-3, CA-2, CM-8, SA-4, SA-9, AC-2, AC-3, AC-6, AC-11, AC-17, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, AT-3, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-02, GV.RM-05, GV.SC-04, GV.SC-05, GV.SC-06, GV.SC-10, ID.AM-07, ID.AM-08, ID.RA-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02, PR.DS-01, PR.DS-11, PR.IR-01, DE.CM-03, RS.MA-04, RS.CO-02, RC.RP-01 |
| Binding rules served | Fla. Stat. 501.171(2), (3)-(6), (8); for Rentals, 15 U.S.C. 1681b(f), 1681m(a), 16 CFR 682.3, and 42 U.S.C. 3604 |

## 1. Purpose
Protect the information of the tenants, applicants, customers, and employees of three small businesses, and the money in their four bank accounts, in a way one person can run. Each rule is written so it can be checked (P07). The LLCs are separate legal entities; this policy keeps their data separate too, while one back office serves all of them.

## 2. Scope
All information of the sole proprietorship and each LLC in any form (electronic or paper), on every system in the Shared Back-Office Platform (SYS-01 to SYS-04, SYS-08, SYS-10), in each LLC's own system (SYS-05 to SYS-07), on the site devices (SYS-09), and at every vendor and contractor that handles it. It applies to the owner, to every LLC employee (the Storage manager and the Laundry attendants), and to any future employee of any entity. Contractors (the bookkeeper, the IT technician) are bound through their written terms.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead, risk acceptor, administrator of every system | Owner-manager | Runs this policy for every entity; decides breach questions; keeps records |
| Successor manager | Named in each LLC operating agreement | Uses the sealed access sheet (7.8) only if the owner is incapacitated |
| Storage manager; Laundry attendants | LLC employees | Follow sections 7, 9, and 10.2 at their site |
| Bookkeeper; IT technician | Contractors | Follow their written terms (6.1) and section 9.4 |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The owner must maintain a security program for all four entities documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 This policy designates the owner-manager in writing as the security lead for the sole proprietorship and each LLC. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July using NIST SP 800-30 Rev. 1, and again before any of these changes: buying or selling a business, adding a system or vendor that holds Restricted data, turning on a new AI feature, or hiring at any entity. Every risk must have a treatment and a due date. (RA-3; PM-9; ID.RA-07)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-02)
4.5 Security controls must be evaluated every July (P07). At least every second year the evaluation must include review by someone outside the business, such as the IT technician under written terms. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Sanctions and exceptions
5.1 **Sanctions.** An LLC employee who breaks this policy is dealt with in proportion to intent and harm: retraining, written warning, or ending employment, decided by the owner as manager of that LLC. Each sanction is documented. (PS-8)
5.2 A contractor or vendor that breaks its written terms is dealt with under its contract, up to ending it. (SA-9)
5.3 The owner must record any personal departure from this policy as an exception under 5.4.
5.4 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Vendors and contractors
6.1 **No written terms, no Restricted data.** A contractor may handle Restricted data only under written confidentiality and security terms that require breach notice to the owner within 10 days (mirroring Fla. Stat. 501.171(6)(a)). The bookkeeper signs these terms by 2026-10-31. (SA-9; GV.SC-05)
6.2 The owner must keep a vendor list (Appendix A) showing each vendor and contractor, the entities it serves, the data it holds, its criticality, and its security notice contact. A security contact phone number is registered with each vendor, not only the owner's mailbox. (SA-9; GV.SC-04)
6.3 Before buying any new tool that will hold Restricted data, the owner must check: MFA available, where data is stored, breach notice terms, how to export and delete data, and a SOC 2 report if offered. (SA-4; GV.SC-06)
6.4 When a vendor or contractor relationship ends, the owner must export what must be kept, delete or confirm deletion of the rest, and close the account, and record it. (SA-9; GV.SC-10)
6.5 The accounting service's SOC 2 report must be reviewed every year, and the owner must operate the customer controls it lists (P09). (SA-9; GV.SC-07)
6.6 Remote support sessions must be started and watched by the owner. Unattended remote access must be off. (AC-17)

## 7. Access control
7.1 Every person must have their own account and PIN. Credentials and PINs must never be shared. Shared mailboxes are reached through each person's own account, never through a shared password. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every system that offers it, using an authenticator app, not text-message codes. The owner's email and banking access must also use a hardware security key, with a second key in the sealed envelope (7.8). (IA-2(1); IA-2(2); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, kept in a password manager. Default passwords on any device (routers, gate controller) must be changed before or at installation. (IA-5)
7.4 **Hire and departure checklist.** The owner creates an LLC employee's accounts only after hire paperwork is complete, and on the employee's last day removes every account, PIN, key, and gate code the person held. Accounts in every system are reviewed every quarter. (AC-2; PS-4; PS-7; GV.RR-04)
7.5 **Least privilege.** Each person gets only the role the work needs. The bookkeeper's role allows reconciliation and reports but not payee or bank changes. The owner uses a separate administrator account only for administration, not for daily email. (AC-6; PR.AA-05)
7.6 Laptops and desktops must lock after 5 minutes idle; phones and tablets after 1 minute. (AC-11)
7.7 On the first business day of each month the owner must review the suite sign-in log and mailbox forwarding rules, the storage system user list and after-hours gate entries, the accounting service's payee change history, and the month's bank payment alerts, and note the review in the security log. (AU-6; DE.CM-03)
7.8 **Emergency access.** A one-page access sheet for each entity, recovery codes, and a spare hardware key must be kept in a sealed envelope held by the business attorney, released to the successor manager under the LLC operating agreements. (AC-2; CP-2)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | SSNs, driver license numbers, screening reports, bank details, passwords and recovery codes | Approved locations only (8.2); encrypted; never in AI prompts; minimum necessary |
| **Confidential** | Leases, tenant ledgers, contracts, books, management agreements, this policy set | Own entity's folder; owner and the person who needs it |
| **Public** | Rates, hours, listings, website text | No restriction |

8.2 Restricted data may be kept only in: the LLC system it belongs to (SYS-05, SYS-06, SYS-07), the payroll service, the accounting service, and one restricted folder per entity in the suite that the AI assistant cannot read. Each LLC's Restricted data stays in that LLC's system or folder. (AC-3; PR.DS-01)
8.3 Every computer that can hold Restricted data must use full-disk encryption and an individual sign-in. (SC-28; PR.DS-01)
8.4 Restricted data may be sent only through the system it belongs to or an encrypted suite link, never as an ordinary email attachment or text message. (SC-8)
8.5 Rental applications and screening reports stay in the property management platform. They must not be downloaded except to answer a dispute, and any download is deleted within 30 days. (SI-12; 16 CFR 682.3)
8.6 Suite mail and files must be backed up by a backup service, and each LLC system and the accounting service must be exported monthly. A restore is tested every year. (CP-9; PR.DS-11)
8.7 **Retention and disposal.** Declined and withdrawn rental applications and their screening reports are deleted 2 years after the decision (the period for a Fair Housing Act civil action, 42 U.S.C. 3613(a)(1)(A)); applications of tenants who sign a lease are kept in the platform for the lease term plus 2 years. Driver license scans are not kept once the number is in the storage system. Former Storage tenant records are deleted 3 years after move-out. New-hire forms are kept only in the payroll service. Paper is cross-cut shredded; devices are wiped (encrypted, then reset) or destroyed with a certificate before disposal. Each deletion or disposal is recorded. (MP-6; SI-12; ID.AM-08; Fla. Stat. 501.171(8); 16 CFR 682.3)
8.8 Security documentation (this policy, risk assessments, assessments, incident records, vendor terms, written no-harm determinations) must be kept for at least 5 years. (SI-12; Fla. Stat. 501.171(4)(c))

## 9. Acceptable use, payments, and training
9.1 Business devices are for business work. Family members must not use them. (PL-4)
9.2 Automatic updates and built-in antivirus must stay on. Software comes only from official app stores or the vendor's site. LLC staff use standard (non-administrator) accounts. (SI-2; SI-3)
9.3 Customer Wi-Fi at any site must be on a guest network separate from business devices. (SC-7; PR.IR-01)
9.4 **Payment changes.** No new payee or changed bank details are entered or paid until the owner has called the payee at a phone number already on file (never one in the request). Only the owner changes payees. Urgency is a warning sign, not a reason to skip the call. (AC-6; AT-3; PR.AT-02)
9.5 **AI tools.** Only the approved AI assistant (SYS-10) may be used for business work, and only after the P10 assessment. Restricted data must never be pasted into a prompt or left where the assistant can read it. AI must not be used to rank, select, screen, or decide about any applicant, tenant, customer, or employee, or to write rental listings without the owner reading every word against 42 U.S.C. 3604(c). (PL-4; SA-9; Fla. Stat. 501.171(2))
9.6 **Tenant selection.** Rentals uses written selection criteria applied the same way to every applicant, and sends the platform's adverse action notice whenever a screening report contributed to a decline or a changed term. (PL-4; 15 U.S.C. 1681m(a); 42 U.S.C. 3604)
9.7 The owner completes a security awareness course every year. LLC staff get a 30-minute briefing at hire and every year. The owner and the bookkeeper are briefed on payment fraud every year. (AT-2; AT-3; PR.AT-01; PR.AT-02)

## 10. Incident response
10.1 The business must keep an incident runbook (P08) with a printed contact list at the home office and in the owner's car, and a short "call the owner" notice at each site. (IR-8; RS.MA-01)
10.2 Anyone who suspects an incident (strange email, lost device, unknown sign-in alert, a payment request that seems off) must tell the owner by phone the same day. The owner writes it in the incident log with the time of discovery. (IR-5; IR-6; GV.RM-05; RS.MA-04)
10.3 For every incident the owner must record **which entity's data was involved**. Each LLC is a separate covered entity under Fla. Stat. 501.171, and the sole proprietorship, as each LLC's third-party agent, records the date it told that LLC (same day; the statute allows no more than 10 days). (IR-6; RS.CO-02)
10.4 Notices to individuals and to the Department of Legal Affairs must meet the deadlines in the P08 notification matrix, confirmed by breach counsel, for each affected LLC separately. A decision not to notify must be a written no-harm determination made after consulting law enforcement, kept for 5 years, and sent to the Department within 30 days (501.171(4)(c)). (IR-6; RS.CO-02)
10.5 No ransom or extortion payment may be made without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities: owner identity and email first. (CP-2; RC.RP-01)
11.2 The Storage manager has written authority to run Storage day to day for up to two weeks if the owner is unavailable, using a limited account. (CP-2)
11.3 Paper move-in forms, paper wash-and-fold tickets, and a coin-only sign are kept at the sites for system outages. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.7. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P09 SOC 2 self-check; P10 AI use assessment. Pointer files POL-02 to POL-05 show where each topic lives in this policy.

## Appendix A. Inventory: systems, devices, data locations, and vendors (CM-8; ID.AM-01; ID.AM-02; ID.AM-07; GV.SC-04)
| Item | Entity | Restricted data | Vendor criticality | Protection required |
|---|---|---|---|---|
| Productivity suite and AI assistant (SYS-01, SYS-10) | All four | Restricted folders only | Critical | 7.2, 7.5, 8.2, 8.6, 9.5 |
| Accounting service (SYS-02) | All four | Bank details | Critical | 7.2, 7.5, 6.5 |
| Online banking (SYS-03) | All four | Credentials | Critical | 7.2, 9.4 |
| Payroll service (SYS-04) | Storage, Laundry | Employee SSNs and bank accounts | High | 7.2, 7.4 |
| Storage management system (SYS-05) | Storage | Driver license numbers; gate codes | Critical for Storage | 7.1, 7.2, 7.4, 8.6 |
| Property management platform (SYS-06) | Rentals | Applications; screening reports | High for Rentals | 7.2, 8.5, 8.7, 9.6 |
| Laundry POS and payments (SYS-07) | Laundry | None held by the owner (vendor holds app accounts) | Critical for Laundry | 7.1, 9.3 |
| Owner laptop and phone (SYS-08) | All four | Cached mail and files | | 7.6, 8.3, 9.2 |
| Storage desktop; gate controller (SYS-09) | Storage | Cached tenant records | | 7.1, 7.3, 7.6, 8.3 |
| Laundry POS tablet; laundromat router (SYS-09) | Laundry | None | | 7.1, 9.3 |
| Outside bookkeeper | All four | Books; payroll hours | High | 6.1, 7.5 |
| On-call IT technician | All four | None at rest | Moderate | 6.1, 6.6 |
| Paper move-in forms | Storage | Driver license numbers | | Locked office; 8.7 |

# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (unarmed private security patrol, licensed Class "B" agency) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every August with the risk assessment, and after a new system, a new client type, a hire, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, SA-9, AC-2, AC-3, AC-11, AC-19, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, PE-3, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Florida law and contracts | Fla. Stat. 501.171(2)-(6), (8); Fla. Stat. 493.6118(1)(e), (n), (y); 493.6119(4); 493.6121(2); 493.6110; Fla. Stat. 934.03; client patrol agreements |

## 1. Purpose
Protect what clients entrust to the business (keys, codes, post orders, and reports), the personal information of people the owner meets on patrol, and the business's own records, in a way that one person working nights can actually follow. Each rule below is written so it can be checked (P07).

## 2. Scope
All business information in any form (electronic, paper, keys and cards, video, spoken), on every system in the Patrol Business SaaS Stack (SYS-01 to SYS-07), in the patrol vehicle, at the home office, and at every vendor that handles it. It applies to the owner and to any future employee. Vendors and the backup patrol agency are bound through their contracts.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Information security lead, records custodian, incident commander | Owner | Runs this policy; decides breach and client-notice questions; keeps records |
| Risk acceptor | Owner | Accepts or treats every risk (section 4.4) |
| On-call IT technician | Contractor under a confidentiality agreement | Technical help on request; no standing access |
| Backup patrol agency | Licensed Class "B" agency | Covers patrols only under a written agreement (11.2) |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01; Fla. Stat. 501.171(2))
4.2 The owner is designated in writing, by this policy, as the information security lead and records custodian. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every August (P07). At least every second year, the evaluation must include review by someone outside the business, such as the IT technician or another licensed agency owner under a confidentiality agreement. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Conduct, sanctions, and exceptions
5.1 Any future employee who breaks this policy must be sanctioned in proportion to intent and harm: retraining, written warning, or termination, documented and kept 5 years. Hiring and termination are reported to the department within 15 calendar days (Fla. Stat. 493.6112(2)). (PS-8)
5.2 A vendor or contractor that breaks its contract or this policy is dealt with under its contract, up to ending it. (SA-9)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. The owner records any personal departure from this policy the same way. (PL-1)

## 6. Client keys, codes, and client information
6.1 Client access information (alarm and gate codes, keys, access cards, keyholder lists, post orders) and reports are **Restricted**. They may be used only to provide that client's services and released only to that client, to law enforcement or fire rescue in an emergency at the client's site, or as the law requires. (PE-3; Fla. Stat. 493.6118(1)(e); client agreements)
6.2 Codes may be kept only in the password manager vault and in the patrol app post orders. They must not be kept in spreadsheets, notes, email, or text messages. Clients are asked to give new codes by phone call or through the patrol app, not by text. Any code received by text is moved to the vault and the message deleted the same shift. (PE-3; SC-28; SC-8)
6.3 One sealed paper copy of all codes and of the account recovery codes is kept in the locked safe at the home office. It is replaced, resealed, and dated after each change. (PE-3; CP-2)
6.4 Keys and cards carry coded tags, never site names; the code key is in the vault. When not on the owner's person, keys stay in the bolted vehicle lockbox or the home safe. Every key received or returned is signed in the key log, and keys are counted against the log on the first Monday of each month. (PE-3; PR.AA-06)
6.5 A lost key or a code that may be exposed must be reported to the client within 2 hours, with a recommendation to rekey or change the code (client agreements). At contract end, keys are returned within 7 days and the client's codes and portal accounts are deleted within 5 days; both are recorded in the key log. (PE-3; AC-2)
6.6 The owner keeps a vendor list showing each vendor, the data it holds, and its security contact. The patrol app vendor's SOC 2 report is reviewed every year, and the owner runs the customer controls it lists. No new service may hold Restricted data until its terms (including AI and data-use terms) are read and recorded. (SA-9; GV.SC-05; GV.SC-07; Fla. Stat. 501.171(6))

## 7. Access control
7.1 Every person has their own account. Credentials are never shared. The laptop has a business account for the owner and a separate account for family use. (IA-2; AC-2; PR.AA-01)
7.2 App-based MFA must be on for the patrol app admin account, email, and the accounting SaaS. MFA is required for client portal users from 2026-10-31. Text-message codes are not used where an app option exists. (IA-2(1); IA-2(2); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, stored in the password manager, and changed at once if a breach check flags them. Default device passwords are changed before use. (IA-5)
7.4 Client portal accounts are created only on a client's written request, removed the same day a client reports a departure, and reviewed every quarter with each client. (AC-2; PR.AA-05)
7.5 The phone uses a passcode of at least 6 digits, locks after 30 seconds, and hides message previews on the lock screen. The laptop locks after 5 minutes idle. (AC-11; AC-19)
7.6 **Emergency access.** Account recovery codes are kept in the sealed copy in the safe (6.3). (AC-2; CP-2)
7.7 On the first Monday of each month, the owner reviews the patrol app sign-in log and the email sign-in history, and notes the review in the security log. (AU-6; DE.AE-02)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Codes, keys, post orders, incident and daily reports, personal information (ID numbers, injury notes), body-camera video, credentials | Approved locations only (8.2); encrypted; shared only under 6.1 |
| **Confidential** | Contracts, invoices, tax and bank records, this policy set | Encrypted storage; owner only |
| **Public** | Website, license number in advertising | No restriction |

8.2 Restricted data may be kept only in the patrol app, the password manager vault, the business file area that has a versioned backup, the home safe, and the patrol vehicle lockbox. (AC-3; SC-28)
8.3 Every device that can hold Restricted data must use encryption. Body-camera clips are copied to the business file area after each shift, and the camera card is cleared each week. (SC-28; PR.DS-01)
8.4 Codes and personal information must not be sent by ordinary text message or in an email body. Use the patrol app or an expiring link to a named person. (SC-8; PR.DS-02)
8.5 Reports state only what the owner observed. Changes after a report is submitted are made only as a dated addendum, never by overwriting. (AU-2; Fla. Stat. 493.6119(4))
8.6 **Body camera.** The owner announces that the camera is recording at the start of every contact, and follows counsel's advice on when audio may be recorded (Fla. Stat. 934.03). Clips are shared only with the client, its insurer, or law enforcement on request, by links that expire within 30 days, and each share is logged. (SC-8; SI-12)
8.7 Paper with Restricted data is cross-cut shredded. Old phones, laptops, and camera cards are wiped (encrypted, then reset) before reuse or trade-in, or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))
8.8 **Retention.** Reports, daily activity reports, the key log, contracts, and post orders are kept at least 2 years from creation (Fla. Stat. 493.6121(2)) and deleted after 3 years unless a client contract, a claim, or a legal hold needs them longer. Video is kept 90 days unless tied to an incident or a request, then kept with that incident record. Any written no-harm determination under 501.171(4)(c) is kept at least 5 years. Security records (this policy, risk assessments, assessments, incident records) are kept 5 years. Each December the owner exports 2 years of patrol app reports to the backup and purges what has expired. (SI-12; ID.AM-08)

## 9. Acceptable use, AI, and training
9.1 Business devices and the business laptop account are for business work. Software is installed on the business account only by the owner, from official stores or the vendor's site. (PL-4)
9.2 The phone stays on the owner's person on duty. The laptop stays at the home office. (PL-4)
9.3 Automatic updates and the built-in antivirus must stay on. (SI-2; SI-3)
9.4 GPS tracking is limited to the owner's own phone during shifts. No tracking device or application is placed on anyone else's vehicle or device (Fla. Stat. 493.6118(1)(y)). (PL-4)
9.5 **AI tools.** An AI tool may process Restricted data only after a written assessment (P10) and the owner's written approval, with training on customer data turned off. Voice notes must not include ID numbers, codes, or medical details beyond what the report needs. The owner sets the priority on every report and reads every AI draft in full before submitting. Fire, water, intrusion, injury, and police events are reported to the client by phone call at once, whatever any tool suggests. (PL-4; SA-9; Fla. Stat. 493.6119(4))
9.6 **Criminal justice information.** The owner must never request, accept, or store criminal history, warrant, or intelligence information from a law enforcement contact. If any is received, it is deleted and the sender is told. (PL-4; C-EMERGENCY-R01)
9.7 The owner completes a small-business security course every year and reads monthly security reminders. Any future employee is trained before getting access. (AT-2; PR.AT-01)

## 10. Incident response
10.1 The business keeps an incident runbook (P08) with a printed contact list in the home safe and the vehicle. (IR-8; RS.MA-01)
10.2 Every suspected incident (lost phone, key, or card; phishing click; code sent to the wrong person; vendor notice) is written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 Clients are told within 2 hours of a lost key or exposed code, and within 24 hours of any other security incident affecting their information (client agreements). (IR-6; RS.CO-02)
10.4 For any incident involving personal information, the owner and counsel decide whether there was a breach under Fla. Stat. 501.171 and send notices within the deadlines in the P08 notification matrix. (IR-6)
10.5 No ransom may be paid without legal counsel's advice and an OFAC sanctions check. (IR-4)
10.6 If a client makes a claim against the liability insurance, the department is notified (Fla. Stat. 493.6110(1)). (IR-6)
10.7 The runbook is walked through every year and after any real incident. Lessons learned are recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities: phone and patrol app, then codes and keys, then reports, then records, then the laptop. (CP-2; RC.RP-01)
11.2 The owner keeps a written coverage agreement with a licensed backup patrol agency, with confidentiality terms, and checks its license each year (Fla. Stat. 493.6118(1)(n)). A one-page emergency sheet in the safe tells a trusted family member how to reach the backup agency and clients. (CP-2)
11.3 A spare phone with the patrol app installed is kept charged at home, and blank paper patrol log forms are kept in the vehicle. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07), the monthly review in 7.7, and the monthly key count in 6.4. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Where Restricted data may live
| Item | Restricted data held | Protection required |
|---|---|---|
| Patrol app (SYS-01) | Reports, post orders with codes, GPS, photos | 7.2, 7.4, 7.7 |
| Password manager vault | Codes, credentials | 7.2, 7.3 |
| Business file area with versioned backup (replacing the consumer drive) | Contracts, video clips, report exports | 7.2, 8.3, 8.8 |
| Laptop (SYS-04) | Synced files | 7.1, 7.5, 8.3, 9.1 |
| Phone (SYS-05) | Patrol app, MFA codes | 7.5, 8.4, 9.2 |
| Body camera (SYS-06) | Video until copied off | 8.3, 8.6 |
| Home safe | Sealed code and recovery copy, emergency sheet, spare keys | 6.3, 11.2 |
| Vehicle lockbox | Client keys and cards | 6.4 |

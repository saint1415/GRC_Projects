# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (custom-exempt meat processing shop) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-operator |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new system or vendor, a hire, a change to the custom exemption status, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PL-1, PL-4, PM-1, PM-9, RA-2, RA-3, CA-2, SA-9, AC-2, AC-6, AC-17, AU-6, IA-2, IA-2(1), IA-5, CM-6, SC-7, SC-28, SI-2, SI-3, SI-7, SI-12, MP-6, PE-3, CP-2, CP-9, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-02, GV.SC-04, GV.SC-05, GV.SC-08, GV.SC-10, ID.AM-07, ID.AM-08, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-10, PR.DS-11, PR.PS-01, PR.IR-01, PR.IR-03, DE.CM-02, DE.CM-03, ID.IM-02, RS.MA-01, RS.CO-02, RC.RP-01 |
| Binding rules supported | 9 CFR 303.1(a)(2)-(b), 316.16, 317.16, 320.1-320.3, 300.6(b)(2), 424.21(c); Fla. Stat. 501.171(2)-(6), (8) |

## 1. Purpose
Keep customers' meat safe and correctly handled, keep the records the custom exemption requires, and protect the personal information the shop holds, in a way one person can actually run. The shop's mission is to return every customer's meat safe, correctly cut, and labeled. Each rule below is written so it can be checked (P07).

## 2. Scope
All shop information and systems: SYS-01 to SYS-10 in the Shop Production and Cold-Chain Monitoring System (P02), paper cut sheets, logs, and records in the shop, and every vendor that holds shop data. It applies to the owner-operator and to anyone the owner later hires or authorizes, including the second alert contact.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead, risk acceptor, incident lead | Owner-operator | Runs this policy; accepts or treats every risk; keeps records |
| Responsible person for curing agents | Owner-operator | Custody and use of nitrite cure (424.21(c)) |
| Second alert contact (planned) | Neighboring custom processor, under a written reciprocal agreement | Receives cold-chain alerts with a view-only role; calls the owner and, if unreachable, the refrigeration contractor |
| On-call IT technician | Contractor | Technical help on request; no standing access |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.4 adds an outside check. If the shop ever hires, a security step (account setup, this policy, training) is part of hiring.

## 4. Governance and risk
4.1 The shop maintains a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 A risk assessment is completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk is recorded with a treatment and a due date. (RA-3; PM-9)
4.3 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan. A risk that could put unsafe product in a customer's home is never accepted at High. (PM-9; GV.RM-02)
4.4 Security controls are evaluated every July (P07), with the IT technician reviewing the evidence at least every second year. (CA-2)
4.5 This workbook of requirements (P03) is the shop's register of legal and contractual duties and is reviewed every July. Before accepting wild game, selling any product, or adding a retail counter, the owner reruns P03. (PM-1; GV.OC-03)
4.6 This policy is reviewed at least every year and after major changes or incidents. Exceptions are written, risk-rated under 4.3, recorded in P01, and expire within 12 months. (PL-1; GV.PO-02)

## 5. Accounts and access
5.1 Every account is the owner's own. Passwords are never shared with the slaughter operator, contractors, or family. (IA-2; AC-2; PR.AA-01)
5.2 MFA must be on for every account that offers it: email, cold-chain, booking form, accounting, and banking. Authenticator app preferred over text message. (IA-2(1); PR.AA-03; Fla. Stat. 501.171(2))
5.3 Every account has a unique passphrase of at least 14 characters, stored in a password manager. The browser must not store passwords. (IA-5; PR.AA-01)
5.4 Factory default passwords and PINs are changed before a device is used (router, smokehouse panel, gateway, printer). (IA-5; CM-6)
5.5 Daily work on the laptop uses a standard user account. The administrator account is used only to install approved software. (AC-6; PR.AA-05)
5.6 The second alert contact gets a view-only role in the cold-chain service and nothing else. Any vendor support access is turned on only for a session the owner requested and turned off afterwards. (AC-2; AC-17)
5.7 Remote program editing in the smokehouse app stays off. Cook programs are changed only at the controller panel by the owner. (AC-17; PR.AA-05)
5.8 On the first Monday of each month (every Monday from October to December), the owner reviews the cold-chain activity log, the email sign-in history, the router's connected-device list, and the smokehouse program list against the printed binder, and notes the review in the shop log. (AU-6; DE.CM-03; SI-7)
5.9 **Emergency access.** A sealed envelope with the cold-chain recovery codes, the refrigeration contractor's number, and a one-page cooler emergency sheet is held by a trusted family member. (CP-2; AC-2)

## 6. Vendors
6.1 The owner keeps a vendor list showing each vendor, the data or device it handles, how critical it is (from P05), and the security contact registered with it. (SA-9; GV.SC-04)
6.2 A shop security contact address is registered with every vendor that holds shop data, so breach notices are not lost in personal mail (Fla. Stat. 501.171(6)). (IR-6; GV.SC-08)
6.3 Before a new vendor, device, or AI tool, or at renewal, the owner checks that it offers MFA, gives notice of breaches, lets the shop export its data, and does not claim rights to use shop data for other purposes. The cold-chain vendor's SOC 2 report is reviewed every year (P09). (SA-9; GV.SC-05)
6.4 When a service is dropped, the owner exports the data, deletes it from the vendor, and closes the account. (SA-9; GV.SC-10)

## 7. Data handling
7.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Custom records, cut sheets and booking submissions (names, addresses, phones), cook programs, the cure sheet, passwords and recovery codes | Approved locations only (Appendix A); encrypted; never entered in an AI tool except recipes without customer details (9.5) |
| **Internal** | Invoices, tax records, vendor contracts, this policy set | Business file plan; owner only |
| **Public** | Prices, hours, the booking page | No restriction |

7.2 Restricted data is kept only in the locations in Appendix A. It is not kept in a personal account once the business file plan is in place (2026-10-15), and not in the phone's photo roll after it has been entered. (AC-3; PR.DS-01)
7.3 Every laptop and phone uses full-disk or device encryption. (SC-28; PR.DS-01; Fla. Stat. 501.171(2))
7.4 Paper cut sheets and logs are kept in a locked file box when not in use. (PE-3; 9 CFR 320.2(a))
7.5 **Backups.** The custom records, label templates, cure sheet, and cook programs are kept in the business file plan with version history, and exported on the first Monday of each month to an encrypted drive kept in the house. A test restore is done each quarter. Cook programs and a monthly records summary are also printed and kept in the shop binder. (CP-9; PR.DS-11; 9 CFR 303.1(b)(3), 320.3(a))
7.6 **Retention and disposal.** Custom records and Part 320 records are kept for 2 years after December 31 of the year of the transaction (9 CFR 320.3(a)), and longer only if FSIS asks in writing. After that, paper is cross-cut shredded and electronic copies are deleted from the file plan and the backup drive. Old devices are wiped (encrypted, then factory reset) before reuse or recycling. Each disposal is noted in the shop log. (SI-12; MP-6; ID.AM-08; Fla. Stat. 501.171(8))
7.7 Records must be producible at the shop during business hours (9 CFR 300.6(b)(2), 320.4), from the laptop, the phone, or the printed summary.

## 8. Devices and network
8.1 Automatic updates and the built-in antivirus stay on. Software comes only from official stores or the vendor's site. Router, gateway, and smokehouse firmware is checked each quarter and updated from the maker's site or app. (SI-2; SI-3; PR.PS-02)
8.2 Customers use a separate guest network. The cold-chain gateway and the smokehouse controller use their own network, apart from the laptop. (SC-7; PR.IR-01)
8.3 Required device settings are listed in Appendix A and checked in the monthly review. (CM-6; PR.PS-01)

## 9. Acceptable use and training
9.1 Shop devices are for shop work. Family members do not use the laptop. (PL-4)
9.2 Devices are never left in the truck or unattended outside the locked shop or the house. (PL-4)
9.3 Payment changes or new bank details received by email or text are confirmed by phone with a known number before any payment. (PL-4; PR.AT-01)
9.4 The owner completes a free small-business security course every year and reads monthly security reminders. Anyone hired or authorized later is trained before access. (AT-2; PR.AT-01)
9.5 **AI tools.** No customer names, addresses, or phone numbers are entered into any AI tool. **Cure and brine amounts are never taken from an AI tool.** They come only from the cure supplier's printed chart or the locked cure sheet checked against it, within the limits in 9 CFR 424.21(c), and the check is written on the batch sheet. Any new AI use needs a P10 assessment first. (SA-9; SI-7; PR.DS-10)

## 10. Incident response
10.1 The shop keeps the incident runbook (P08) and a printed contact list in the shop and in the house. (IR-8; RS.MA-01)
10.2 Every suspected incident (unknown sign-in, silenced or missing alert, changed program, phishing click, lost phone, vendor breach notice) is written in the incident log the same day, with the time it was discovered. (IR-5; IR-6)
10.3 **Product first.** If an incident could have affected temperatures, a cook program, or a cure amount, the owner holds the affected product and checks it before anything else (P08 section 3). Product whose safety cannot be shown is not released to the owner as food without talking to the owner of the animal.
10.4 Notices follow the P08 notification matrix, with counsel confirming any Fla. Stat. 501.171 notice. (IR-6; RS.CO-02)
10.5 No ransom is paid without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook is walked through every year before the busy season and after any real incident, and lessons are recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. Cold storage comes first. (CP-2; RC.RP-01)
11.2 **When alerts are down** (gateway offline notice, internet or power outage, lost phone), the owner reads the dial thermometers every hour while awake and at least every 4 hours overnight, writes each reading on the paper log, and calls the second alert contact to cover any gap. (CP-2; DE.CM-02; PR.IR-03)
11.3 **Storm procedure.** When a hurricane watch covers the county, no new carcasses are accepted for 72 hours before forecast landfall, the freezer is kept full and closed, the slaughter operator is told, and emergency cooler space is confirmed. (CP-2; PR.IR-02)
11.4 The gateway and router run on a battery backup, and the vendor's "gateway offline" notice stays on. (CP-2; PR.IR-03)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 5.8. A broken rule is recorded as an exception under 4.6 and fixed, or the risk is re-rated in P01.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Data locations and required settings
| Item | Restricted data held | Required settings |
|---|---|---|
| Cold-chain service (SYS-01) | Temperature history; alert contacts | MFA; unique passphrase; second contact (view-only); offline notice on; set points 38 F cooler, 10 F freezer |
| Smokehouse controller and app (SYS-02) | Cook programs | Unique passphrase; panel PIN changed; remote editing off; programs printed in the binder |
| Laptop (SYS-03) | Synced records; label templates; cure sheet | Encryption; standard user for daily work; no saved browser passwords; antivirus on |
| Business file plan (replacing the consumer account, SYS-05) | Custom records; cut sheets | MFA; version history on; monthly export to the encrypted drive |
| Phone (SYS-06) | Kill sheet photos until entered; alerts | Passcode; encryption; find-and-wipe on; photos deleted after entry |
| Booking form (SYS-07) | Requests and cut sheets | MFA; unique passphrase |
| Router (SYS-09) | None (traffic) | Admin password changed; guest network; device network; current firmware |
| Paper box in the shop | Cut sheets; logs | Locked; shredded after the retention period |

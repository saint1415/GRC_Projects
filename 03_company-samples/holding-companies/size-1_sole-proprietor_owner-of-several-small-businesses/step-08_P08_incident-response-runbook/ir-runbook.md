# Incident Response Runbook: Takeover of the Shared Back-Office Email Account

| Field | Value |
|---|---|
| Organization | Cris Santos Company (sole proprietorship) and its LLCs: Storage, Rentals, Laundry |
| Tier / Vertical | Sole Proprietorship / Management of Companies and Enterprises |
| Incident type | Compromise of shared services affecting all three LLCs: an attacker takes over the owner's email account (SYS-01), which is the administrator and recovery address for every system, then tries to redirect a payment and downloads the Rentals application folder |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner-manager, 2026-08-31, for the sole proprietorship and each LLC |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-09-30 (POAM-009) |

Keep a printed copy at the home office and in the car. Assume the attacker can read the owner's email: **use the phone, the bank's phone line, and this paper copy. Do not send incident details by email until step 3 of the first hour is done.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Bank fraud line | Freeze new payees and outgoing payments on all four accounts; recall any payment already sent | Hour 0 |
| Outside bookkeeper | Stop: no payee changes or payments from any email request until the owner calls back | Hour 0 |
| On-call IT technician | Help lock out the attacker, check the laptop, preserve logs | Hour 0-1 |
| Breach counsel (privacy attorney referred by the business attorney) | Privilege; which LLC must notify whom; notice letters; any extortion demand | Hours 1-4 |
| Each LLC's general liability carrier | Ask whether any coverage applies **before** hiring outside firms (no cyber policy today) | Hours 1-4 |
| Vendor support: storage system, property management, laundry platform, accounting, payroll | Confirm no password resets or new users; pull access logs for the owner's accounts | Hours 1-8 |
| Storage manager; Laundry attendants | Ignore any email "from the owner" about payments, codes, or passwords until told otherwise by phone | Hours 1-2 |
| FBI Internet Crime Complaint Center | Report the payment fraud attempt; supports the bank's recall | Day 1 |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: the bookkeeper or a vendor asks about an email the owner did not send; a sign-in alert for a place or device the owner does not recognize; a password reset notice the owner did not request from any LLC system; forwarding rules or sent items the owner did not create; a tenant, applicant, or employee reports a strange message from a business address. **Write down the date and time, and which LLC's systems and data might be involved.** Florida's 30-day notice clock runs from determination of the breach or reason to believe a breach occurred (Fla. Stat. 501.171(4)(a)), separately for each LLC.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Call the bank fraud line: hold new payees and outgoing payments on all four accounts; ask about any payment in the last 7 days | Hold confirmed; reference number written down |
| 2. Call the bookkeeper: no payee changes or payments on email instructions | Bookkeeper confirms |
| 3. From the phone (not the laptop), change the email password, sign out all sessions, delete forwarding and inbox rules, remove unknown MFA methods, and switch MFA to the authenticator app | Only the owner's phone is signed in |
| 4. Change the passwords of the storage system, property management platform, laundry platform, accounting, and payroll, in that order, and turn on MFA wherever it is off | Each system checked for new users and password resets |
| 5. Start the paper incident log: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What did the attacker read or take?** Export the suite sign-in log, mailbox audit log, and file activity for the past 30 days **today**, before they roll over. Look for the "Rentals - applications" folder, the Storage license scans, the new-hire forms, and any file shared by link.
2. **Which LLC is affected?** Sort every exposed file and system by entity. This decides who must notify (section 6). Count people per LLC and note who lives outside Florida.
3. **Did the attacker reach an LLC system?** Ask each vendor for the owner's account activity. If the storage system was opened, the Storage count may pass 500 (about 610 tenant records).
4. **Payment trail.** In the accounting service, check payee and bank-detail changes in all four company files. Compare every payment in the last 7 days with the bank.
5. **Laptop.** The IT technician checks the laptop for malware and saved-password theft. If anything is found, use the phone and a clean device until the laptop is reinstalled.
6. **Preserve evidence.** Keep the exported logs, the phishing email, and the attacker's messages in a folder the owner controls, with a note of who saved what and when. Nothing is deleted until counsel agrees.

## 5. Hours 8-24: keep the LLCs running and prepare notices (RS.CO, RC.RP)
- **Operations:** Storage continues on the gate's stored codes and paper move-in forms; Laundry continues normally (its platform is separate); Rentals tenants pay as usual through the portal. Payroll is paid on schedule only from the last confirmed pay register, by a payment the owner releases after calling the bank.
- **Tell staff and the bookkeeper what changed,** by phone: new passwords, no payment or code changes by email, and whom to call.
- **Agent-to-LLC record:** for each affected LLC, the owner writes the date the sole proprietorship (as third-party agent) told that LLC (Fla. Stat. 501.171(6)(a): no later than 10 days; POL-01: same day).
- **Breach assessment with counsel:** for each LLC, was personal information (SSN, driver license number, bank account with access code, or a user name with password) accessed? Downloaded applications and screening reports are presumed accessed. A decision **not** to notify needs a written no-harm determination after consulting law enforcement, kept 5 years and sent to the Department within 30 days (501.171(4)(c)).
- **Rentals extra:** applicants' screening reports are consumer reports. Counsel advises whether anything beyond the Florida notice is needed; the reports stay subject to proper disposal afterward (16 CFR 682.3).
- **Extortion:** if the attacker demands payment for the files, nothing is paid without counsel's advice and an OFAC sanctions check.

## 6. Notice deadlines and who sends them (from `notification-matrix.csv`)
| LLC (covered entity) | Data most likely exposed | People | Florida notices |
|---|---|---|---|
| CSC Rentals, LLC | Applications with SSNs, screening reports, license copies | Up to 47 applicants | Individuals within 30 days of determination; Department not required (under 500) |
| CSC Self Storage, LLC | License scans in files; tenant records if the storage system was opened | About 230 (files) or about 610 (system) | Individuals within 30 days; **Department within 30 days if 500 or more** |
| CSC Self Storage, LLC and CSC Laundry, LLC | New-hire forms with SSNs | Up to 8 current and former employees | Individuals within 30 days |

**Plan to the shortest clock.** The Department notice has no extension; the individual notice may get 15 more days only with good cause given to the Department in writing within the 30 days. People outside Florida are notified under their own state's law. If more than 1,000 people had to be notified by one LLC at once, the consumer reporting agencies would also be told; no LLC can reach that today.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner identity and email, a clean device, banking and payment hold, the storage system and gate, bookkeeping and payroll, the laundry platform, then the property management platform. Release the bank hold only after every payee changed in the last 30 days has been confirmed by phone. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-008), P07, and this runbook, and keep all incident records for at least 5 years (POL-01 8.8).

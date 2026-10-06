# Incident Response Runbook: Business email compromise and taxpayer data theft

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Tier / Vertical | Micro / Professional, Scientific, and Technical Services |
| Incident type | Business email compromise (BEC) of a staff mailbox, theft of client tax documents from the mailbox and the client folders it can reach, and an attempted refund diversion through requests sent from the hijacked account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy. A written incident response plan is not required at this size (16 CFR 314.6 exempts 314.4(h)); the firm adopts this one because of IRS Pub. 1345 and its top risk (P01 R-001) |
| Runbook owner | Office Manager (Qualified Individual) |
| Approved | 2026-08-31 by the Owner CPA |
| Last tested | Not yet. First tabletop with the MSP due 2026-12-15, before the filing season (POAM-007) |

## 0. Roles and notification chain (Govern)
The firm has 7 people and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics. The Office Manager runs the incident and keeps the log; the Owner CPA makes the decisions and talks to the IRS.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Owner CPA | Cell phone (numbers on the printed contact card) |
| Decision maker (money, notices, closing the office) | Owner CPA | Senior Tax Accountant | Cell phone |
| IRS and state tax agency reporting | Owner CPA (e-file Responsible Official) | Senior Tax Accountant | Local IRS Stakeholder Liaison number on the contact card |
| Technical response | MSP incident line (emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel | Insurer panel counsel | n/a | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm | n/a | Engaged by breach counsel |
| Client call-backs and held returns | Client Services Coordinator (individual returns); Bookkeeper (payroll clients) | Senior Tax Accountant | In person |
| Law enforcement | FBI local field office | Local police | Numbers in the binder |

**Notification chain in the first hour:** staff member → Office Manager → MSP incident line and Owner CPA (at the same time) → insurer breach hotline (Owner CPA) → breach counsel and forensics (through the insurer). The tax software vendor is called if any preparer account may have been used.

**Out-of-band first.** Assume the attacker can read the compromised mailbox and may reach others. Coordinate by phone and text on personal phones, using the printed contact card. Never discuss the response by email until the MSP confirms the suite is clean.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the front desk and at the Owner CPA's and Office Manager's homes: this runbook, the notification matrix, the contact card, the Stakeholder Liaison number, and the client call-back script
- [ ] Suite sign-in and mailbox audit logs kept one year (AU-11). **Gap until POAM-005 closes:** logs expire in under a year, so export them on day 0
- [ ] Number matching on and legacy authentication blocked for every account, including the MFP (IA-2(2)). **Gap until POAM-002 closes**
- [ ] Alerts on new inbox rules, external forwarding, and risky sign-ins to the Office Manager and MSP (SI-4). **Gap until POAM-005 closes**
- [ ] Automatic forwarding to external addresses blocked (done 2026-07-20)
- [ ] Call-back rule in use for refund, payroll, and vendor bank changes (POL-02 C.3)
- [ ] Weekly check of returns filed per EFIN and PTIN in season (IRS Pub. 4557; P03 G-056)
- [ ] Two sealed break-glass administrator accounts tested (POL-02 B.4)
- [ ] Insurer hotline and policy number checked at each renewal

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A client asks about an email "from the firm" requesting documents, payment, or new bank details | Client call, front desk | Log the time. Call the Office Manager. Do not reply to the email thread |
| A request to change a refund bank account, payroll employee bank account, or client email arrives by email or portal message | Preparer, Bookkeeper | Freeze the change (POL-03 4.9). Call the client on the number on file. Report |
| A staff member gets an MFA prompt they did not start, or typed a password and code into a page that looked like a firm or IRS sign-in | Staff report | Report at once. MSP revokes sessions and resets the password and MFA method |
| New inbox rule that moves, deletes, or forwards mail; new connected app | Suite alert (after POAM-005), MSP | Office Manager opens the incident |
| Sign-in from an unusual country or hosting network | Suite alert (after POAM-005) | MSP revokes sessions; open the incident |
| E-file reject for a duplicate SSN, or an IRS letter about a return the client did not file | Client Services Coordinator, client | Open the incident; check for data theft |
| Returns filed per EFIN or PTIN exceed the firm's own count | Weekly EFIN and PTIN check | Owner CPA calls the Stakeholder Liaison and opens the incident |

**Declare a BEC incident when** an unauthorized sign-in to any firm mailbox is confirmed, a malicious rule or forwarding is found, or clients report requests sent from a firm address that staff did not send.

**Record three dates in the incident log. Each one starts a different clock:**
| Date | Definition | Clock it starts |
|---|---|---|
| Discovery | First day the event is known to any employee, officer, or other agent, other than the attacker (16 CFR 314.4(j)(2)) | FTC notice, if 500 or more consumers: no later than 30 days after discovery |
| Confirmation | The incident is confirmed as an event that can result in unauthorized disclosure, misuse, modification, or destruction of taxpayer information (IRS Pub. 1345) | IRS report: no later than the next business day |
| Determination | The firm determines a breach occurred, or has reason to believe one occurred (Fla. Stat. 501.171) | Florida individual notices (and the Department notice if 500 or more Floridians): no later than 30 days |

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke all sessions and tokens for the affected account; reset the password; remove and re-register MFA after verifying the user in person | MSP with the Office Manager | Attacker sessions ended |
| 2. Export mailbox audit, sign-in, and message trace logs for the longest period available **before any cleanup** | MSP | Logs saved to the evidence folder |
| 3. Record, then remove, malicious inbox rules, forwarding, delegates, and connected app consents | MSP | Mailbox matches baseline |
| 4. Block the attacker's sign-in sources and sending domains | MSP | Blocks in place |
| 5. Freeze every refund bank account, address, and email change entered in the tax software in the last 30 days, and every payroll bank change in the payroll platform; hold e-file transmission of affected returns | Senior Tax Accountant; Client Services Coordinator; Bookkeeper | Hold list created |
| 6. Call the cyber insurer's breach hotline; engage counsel and forensics through the insurer | Owner CPA | Claim number issued |
| 7. Open the incident log: timeline, actions, who, when; record the discovery date | Office Manager | Log open |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Initial access.** How was the account taken: a phishing page that captured the password and code, an approved push, the MFP's legacy-authentication mailbox (P07 finding), or a reused password? Did other staff get the same message?
2. **Scope of access.** From the audit logs, list every message, attachment, and client folder file the attacker opened, downloaded, or synced. If item-level records are missing, **assume every message in the mailbox and every folder the account could open was accessed** (16 CFR 314.2(m) presumes acquisition from access unless reliable evidence shows otherwise). Because every employee can open every client folder today (POAM-004), a compromised account can reach all of them.
3. **Messages the attacker sent.** Search sent and deleted items and the message trace for messages to clients, payroll clients, vendors, and staff. List every recipient asked for documents, payments, or bank changes.
4. **Refund and payroll diversion check.** In the tax software and payroll platform audit logs, list every bank account change in the period. Call each client on the number on file. Classify each return or payroll run as held, transmitted, or not affected.
5. **Data inventory and count.** Build one list of affected people from the stolen documents (Forms W-2 and 1099, prior returns, identity documents, bank letters, payroll registers). For each person record: data elements (SSN, account numbers, driver license, email and password), whether the person is an individual tax client (an FTC "consumer"), and state of residence.
   - **FTC count:** individual clients only (314.2(b), (e)). Business entities and payroll employees are not counted.
   - **Florida count:** every Florida resident whose personal information was accessed, including spouses, dependents, and payroll employees named in the documents, and the mailbox user, whose email and password count as personal information.
6. **Preserve evidence.** Keep the exported logs with chain of custody and the attacker's messages with full headers. Forensics images the user's computer if malware is suspected.

## 5. Containment and eradication (RS.MI)
1. Confirm no other mailbox shows the same sign-in sources, rules, or app consents. Reset any that does.
2. Change the MFP "scanner" mailbox password, or disable it if POAM-002 is not yet closed.
3. Scan the user's computer with antivirus, or with EDR once it is deployed under P01 R-005; reimage it if forensics finds malware or token theft tools.
4. Warn clients and payroll clients who received attacker messages: phone first, then a portal message. Tell them the firm never asks for bank changes by email.
5. Keep every held return and payroll change on hold until the client confirms bank details by phone on the number on file, and the Stakeholder Liaison's guidance on that client is received.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each notice before it goes out. The Owner CPA decides breach status with counsel (POL-03).

| When | Action | Owner |
|---|---|---|
| Hour 1 | Insurer notified; counsel and forensics engaged | Owner CPA |
| As soon as confirmed, and **no later than the next business day** | Report to the local IRS Stakeholder Liaison: the Pub. 1345 security incident report and the data theft report. Ask for guidance on held and transmitted returns | Owner CPA |
| Same day as the IRS report | Notify the tax agencies of the states where affected clients file (Florida has no personal income tax, so this means other states' agencies) | Owner CPA |
| Day 0 to 2 | Report to the FBI local field office; file a local police report | Office Manager |
| Day 0 to 2 | Staff briefing: what happened, the call-back rule, and no discussion outside the firm | Office Manager |
| Within 30 days after determination | Florida individual notices by mail or email; Department of Legal Affairs notice if 500 or more Floridians; consumer reporting agencies if more than 1,000 | Owner CPA with counsel |
| No later than 30 days after discovery | FTC notice on the ftc.gov form if 500 or more consumers. The 314.6 exception does not remove this duty | Owner CPA with counsel |
| Per each state's law | Notices to residents of other states and their regulators (about 6% of individual clients live outside Florida for part or all of the year) | Counsel |
| Within 1 week | Call each payroll client whose employees' data was taken, as the engagement letter requires | Bookkeeper with the Owner CPA |

**The Florida notice cannot be replaced by the FTC notice.** The deemed-compliance path in 501.171(4)(g) needs a federal regulator's rule on notice to individuals. The FTC rule requires notice only to the FTC.

**What to tell clients.** The letter covers the Florida content (date range, information involved, how to contact the firm) and the IRS-recommended advice: watch for IRS letters, file Form 14039 only if the IRS sends a notice or an e-filed return is rejected for a duplicate SSN, and get an IRS Identity Protection PIN.

**Worked example (tabletop script for 2026-12-15).**
| Date | Event | Clock effect |
|---|---|---|
| Tue 2027-02-16 | The Tax Accountant enters a password and MFA code on a fake IRS e-Services page, then thinks nothing of it | Counsel decides whether this is "known to" an employee under 314.4(j)(2). The plan assumes it could be |
| Thu 2027-02-18 | A client calls about an email from the firm asking to change the refund account. Incident declared | Discovery recorded no later than today |
| Fri 2027-02-19 | Forensics confirms the attacker downloaded 310 attachments and opened client folders, and sent 12 bank-change requests | Confirmation. IRS report due by **Mon 2027-02-22**; made the same afternoon |
| Tue 2027-02-23 | Counsel and the Owner CPA determine a breach: about 240 individual clients (FTC consumers), 300 Florida residents including spouses and payroll employees, and 14 residents of other states | Florida notices due by **Thu 2027-03-25**. No Department notice (fewer than 500 Floridians); no consumer reporting agency notice (not more than 1,000); no FTC notice (fewer than 500 consumers). Counsel records the counts and the reasoning, and the firm re-checks if forensics finds more |

**Small numbers do not mean small duties.** At this size most incidents fall below the 500-consumer FTC line and the 500-person Florida Department line, but the IRS next-business-day report and the Florida individual notices apply to every affected client, however few.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6):
1. Internet and office network: firewall login checked and credentials changed
2. Clean computers for the preparers: the affected computer checked or rebuilt by the MSP
3. Suite sign-in and email: the cleaned mailbox, or a new one for the user if forensics cannot clear the old one; forwarding and rules checked on every mailbox
4. Tax software: confirm no preparer account was used by the attacker; release held returns only after call-back confirmation and Stakeholder Liaison guidance
5. Payroll platform: confirm no changed bank details; release held payroll changes after call-backs
6. Client portal: move every targeted client to portal-only delivery
7. Client folders: restore from SYS-08 only if the attacker changed or deleted files

**Validate before closing:** no sign-ins from attacker sources for 14 days, all users on number matching, legacy authentication blocked, and all held returns and payroll changes resolved. In season, file extensions early for any client whose return cannot be released in time (BP-01 workaround).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and counsel; written summary within 30 days (POL-03 4.13).
- Update the risk register (P01, especially R-001, R-002, R-003, R-020, R-024), the POA&M (P07), training content (AT-2), and this runbook.
- Discuss the event at the next monthly program review (POL-02 A.10).
- Keep all incident records for at least 5 years (POL-02 A.8), which also covers the 5-year retention for any Florida no-harm determination (501.171(4)(c)).

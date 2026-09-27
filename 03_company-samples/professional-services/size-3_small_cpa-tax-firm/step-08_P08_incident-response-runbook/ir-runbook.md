# Incident Response Runbook: Business email compromise and taxpayer data theft

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Tier / Vertical | Small / Professional, Scientific, and Technical Services |
| Incident type | Business email compromise (BEC) of a staff mailbox, theft of client tax documents from the mailbox, and an attempted refund diversion through requests sent from the hijacked account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy. With POL-03, this runbook is part of the written incident response plan required by 16 CFR 314.4(h) (N54-R01) |
| Runbook owner | IT Manager (Qualified Individual) |
| Approved | 2026-08-31 by the Firm Administrator |
| Last tested | Not yet. First tabletop exercise due 2026-12-15, before the filing season (POAM-016, POAM-017) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | Firm Administrator | Incident line (cell), then the out-of-band group chat on personal phones |
| Technical response | MSP incident team | Forensic firm from the cyber insurer's panel | MSP 24x7 line |
| Breach and notification decisions | Risk and Quality Partner | Managing Partner | Cell |
| IRS and state tax agency reporting | Tax Partner (e-file Responsible Official) | Client Services Supervisor | Cell; local IRS Stakeholder Liaison number in the incident binder |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Through the insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Client and staff communications | Firm Administrator | Managing Partner (external statements) | Cell |
| Law enforcement | FBI local field office | Local police | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read email in the compromised mailbox and may have access to others. Coordinate by phone and the printed contact list. Never discuss the response by email until the IT Manager confirms the tenant is clean.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at both offices: this runbook, the notification matrix, contacts, the Stakeholder Liaison number, and the client call-back script
- [ ] Mailbox audit and sign-in logs retained for at least one year in a log workspace (AU-11, AU-6). **Gap until POAM-004 closes:** identity and mailbox logs keep only 30 to 90 days, so export them on day 0
- [ ] Legacy authentication blocked and number matching on for all users (IA-2(2)). **Gap until POAM-002 closes**
- [ ] 24x7 alerting on new inbox rules, external forwarding, and anomalous sign-ins (SI-4). **Gap until POAM-005 closes**
- [ ] Call-back verification procedure for any change to a refund bank account, address, or email (POL-05 4.4; P01 R-002)
- [ ] Weekly check of returns filed per PTIN and EFIN totals during filing season (IRS Pub. 4557; P03 G-056)
- [ ] Two break-glass administrator accounts sealed and tested (POL-02 4.7)
- [ ] Incident line and reporting rules briefed to all staff, including seasonal preparers (POL-03 4.2; POAM-017)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A client asks about an email "from the firm" requesting documents, payment, or new bank details | Client call, reception | Log the time. Call the incident line. Do not reply to the email thread |
| A client or preparer receives a request to change the direct deposit account on a return by email or portal message | Preparer, Client Services Supervisor | Freeze the change (POL-03 4.7). Call the client on the number on file. Report to the incident line |
| A staff member receives or approved an MFA prompt they did not start | Staff report | Report immediately. IT revokes sessions and resets the password and MFA method |
| New inbox rule that moves, deletes, or forwards mail; new external forwarding | Log workspace alert (after POAM-004), MSP | IT Manager opens the incident |
| Sign-in from an unusual country or hosting network, or impossible travel | Identity provider alert (after POAM-005) | Revoke sessions; open the incident |
| E-file reject for a duplicate SSN, or an IRS notice about a return the client did not file | E-file coordinator, client | Open the incident; check for data theft |
| Returns filed per EFIN or PTIN exceed the firm's own count | Weekly EFIN and PTIN check | Tax Partner calls the Stakeholder Liaison and opens the incident |
| Bulk download of attachments or DMS files | Log workspace alert (after POAM-004) | Open the incident |

**Declare a BEC incident when** an unauthorized sign-in to any firm mailbox is confirmed, or a malicious rule or forwarding is found, or clients report requests sent from a firm address that staff did not send.

**Record three dates in the incident log. Each one starts a different clock:**
| Date | Definition | Clock it starts |
|---|---|---|
| Discovery | First day the event is known to any employee, officer, or other agent other than the attacker (16 CFR 314.4(j)(2)) | FTC notice: no later than 30 days after discovery |
| Confirmation | The incident is confirmed as an event that can result in unauthorized disclosure, misuse, modification, or destruction of taxpayer information | IRS report: no later than the next business day (Pub. 1345) |
| Determination | The firm determines a breach occurred, or has reason to believe one occurred (Fla. Stat. 501.171) | Florida individual and Department notices: no later than 30 days |

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke all sessions and refresh tokens for the affected account; reset the password; remove and re-register MFA after verifying the user in person | IT Manager | Attacker sessions ended; user re-enrolled |
| 2. Export mailbox audit, sign-in, and message trace logs for the last 90 days **before any cleanup** | IT Manager with the MSP | Logs saved to the evidence folder with hash values |
| 3. Record, then remove, malicious inbox rules, forwarding, delegates, and connected third-party app consents | IT Manager | Mailbox configuration matches baseline |
| 4. Block the attacker's sign-in sources and sending domains; block external auto-forwarding tenant-wide if not already blocked | IT Manager | Blocks in place |
| 5. Freeze every refund bank account, address, and email change entered in the tax software in the last 30 days, and hold e-file transmission of the affected returns | Tax Partner; e-file coordinator | Hold list created; no affected return transmitted |
| 6. Call the cyber insurer's breach hotline; engage counsel and forensics through the insurer | Managing Partner | Claim number issued |
| 7. Start the incident log: timeline, actions, who, when; record the discovery date | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Initial access.** Identify how the account was taken: phishing link, MFA push approved by mistake, legacy protocol (the path found in P07 testing), or a reused password. Check whether other accounts received the same phishing message.
2. **Scope of access.** From the audit logs, list every message and attachment the attacker opened, downloaded, or synced, and every file reached in the productivity suite. If item-level access records are missing, **assume every message in the mailbox was accessed** (16 CFR 314.2(m) presumes acquisition from access unless reliable evidence shows otherwise).
3. **Messages sent by the attacker.** Search sent items, deleted items, and message trace for messages to clients, vendors, and staff. List each recipient who was asked for documents, payments, or bank changes.
4. **Refund diversion check.** In the tax software audit log, list every bank account change in the period. For each, compare with the prior-year return and call the client on the number on file. Classify each return as held, transmitted and accepted, or not affected.
5. **Data inventory and count.** Build one list of affected people from the extracted attachments (Forms W-2 and 1099, prior returns, identity documents, bank letters). Record for each person: name, data elements (SSN, account numbers, driver license), whether they are an individual tax client (an FTC "consumer" with a customer relationship), and state of residence.
   - **FTC count:** individual consumers only (314.2(b), (e)). Business entities are not counted; their owners are counted only if they are individual clients.
   - **Florida count:** every Florida resident whose personal information was accessed (501.171(1)(g)), including spouses, dependents, and employees named on business clients' documents, and the mailbox user's own credential if it was taken.
6. **Preserve evidence.** Forensics images the affected laptop if malware is suspected, keeps the exported logs with chain of custody, and preserves the attacker's messages with full headers.
7. **Encryption check.** Attachments sent through the portal or with enforced encryption are still "unencrypted" for the FTC rule if the attacker had the key or the mailbox that opens them (314.2(m)). Plain attachments are always unencrypted.

## 5. Containment and eradication (RS.MI)
1. Confirm no other mailbox shows the same sign-in sources, rules, or app consents. Reset any account that does.
2. Rotate the credentials of any shared or service mailbox the user could reach (see POAM-011).
3. Scan the user's laptop with EDR; reimage it if forensics finds malware or a persistent token theft tool.
4. Send an out-of-band warning to clients who received messages from the attacker: phone first, then a portal message. Tell them the firm never asks for bank changes by email.
5. Keep every held return on hold until the client confirms bank details by phone on the number on file, and the Stakeholder Liaison's guidance on that client is received.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each notice before it goes out. The Risk and Quality Partner decides breach status (POL-03 4.5).

| When | Action | Owner |
|---|---|---|
| Day 0 | Insurer notified; counsel and forensics engaged | Managing Partner |
| As soon as confirmed, and **no later than the next business day** | Report to the local IRS Stakeholder Liaison: the Pub. 1345 security incident report and the data theft report. Ask for guidance on held and transmitted returns | Tax Partner |
| Same day as the IRS report | Notify the state tax agencies where affected clients file (Federation of Tax Administrators contact list) | Tax Partner |
| Day 0 to 2 | Report to the FBI local field office; file a local police report | IT Manager |
| Day 0 to 5 | Staff briefing: what happened, the call-back rule, and no discussion outside the firm | Firm Administrator |
| Within 30 days after determination | Florida individual notices, by mail or email; Department of Legal Affairs notice if 500 or more Floridians; consumer reporting agencies if more than 1,000 | Risk and Quality Partner with counsel |
| No later than 30 days after discovery | FTC notice on the ftc.gov form if 500 or more consumers | Risk and Quality Partner with counsel |
| Per each state's law | Notices to residents of other states and their regulators (about 9% of individual clients live outside Florida for part or all of the year) | Counsel |

**The Florida notice cannot be replaced by the FTC notice.** The deemed-compliance path in 501.171(4)(g) needs a federal regulator's rule on notice to individuals. The FTC rule requires notice only to the FTC.

**What to tell clients.** The letter covers the Florida content (date range, information involved, how to contact the firm) and the IRS-recommended advice: watch for IRS letters, file Form 14039 only if the IRS sends a notice or an e-filed return is rejected for a duplicate SSN, and get an IRS Identity Protection PIN.

**Worked example (tabletop script).**
| Date | Event | Clock effect |
|---|---|---|
| Fri 2027-02-05 | A tax manager approves an MFA push they did not start and mentions it to a colleague, but no one reports it | Counsel decides whether this is "known to" an employee under 314.4(j)(2). The plan assumes it could be, so the FTC target is **Fri 2027-03-05** |
| Tue 2027-02-09 | A client calls about an email "from the firm" asking to change her refund account. Incident declared | Discovery recorded no later than today. FTC outer limit Thu 2027-03-11 |
| Wed 2027-02-10 | Forensics confirms the attacker downloaded 1,140 attachments and sent 38 bank-change requests | Confirmation. IRS report due by **Thu 2027-02-11**; made the same afternoon |
| Fri 2027-02-12 | Counsel and the Risk and Quality Partner determine a breach: about 620 individual clients (FTC consumers) and 910 Florida residents, plus 84 residents of other states | Florida notices due by Sun 2027-03-14, so sent by **Fri 2027-03-12**. Department notice required (500 or more Floridians); consumer reporting agencies not required (not more than 1,000) |

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6):
1. SYS-05 identity provider and administrator access (break-glass accounts if needed)
2. SYS-01 tax software access, after confirming no preparer account was used by the attacker
3. SYS-01 e-file queue: release held returns only after call-back confirmation and Stakeholder Liaison guidance
4. SYS-06 email: the cleaned mailbox, or a new mailbox for the user if forensics cannot clear the old one
5. SYS-02 client portal and SYS-03 DMS: confirm no portal or DMS access from the attacker's sources
6. SYS-02 e-signature and return delivery; move clients who were targeted to portal-only delivery
7. SYS-07 practice management and billing: check for changed payment details (P01 R-025)

**Validate before closing:** no sign-ins from attacker sources for 14 days, all affected users on number matching, and all held returns resolved. Tell staff and affected clients when normal service resumes (RC.CO). During filing season, file extensions early for any client whose return cannot be released in time (BP-01 workaround).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 4.10 requires documentation within 30 days of closing).
- Update the risk register (P01, especially R-001, R-002, R-003, R-024, R-033), the POA&M (P07), training content (AT-2), and this runbook.
- Include the event in the Qualified Individual's next written report to the Partner Group (314.4(i)).
- Keep all incident records for at least 5 years (POL-01 4.13), which also covers the 5-year retention for any Florida no-harm determination (501.171(4)(c)).

# Incident Response Runbook: Business Email Compromise and Taxpayer Data Theft

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm, with its attest affiliate) |
| Tier / Vertical | Mid-Market / Professional, Scientific, and Technical Services |
| Incident type | Business email compromise (BEC) of a partner's or tax manager's mailbox by session token theft, theft of client tax documents from the mailbox and shared files, and attempted refund and CAS payment diversion through messages sent from the hijacked account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy. With POL-03 and `ir-runbook-ransomware.md`, this runbook is the written incident response plan required by 16 CFR 314.4(h) (N54-R01) |
| Companion documents | `ir-runbook-ransomware.md` (ransomware with data extortion, and the tax software vendor outage variant); `notification-matrix.csv`; BIA (P05); risk register (P01 R-001, R-002, R-003, R-020, R-023) |
| Runbook owner | Director of Information Security (incident commander) |
| Approved | 2026-09-22 by the Chief Operating Officer |
| Last tested | Not yet. BEC tabletop with outside counsel and the IRS Stakeholder Liaison step scheduled for 2026-11-19 (POAM-014) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, business, and legal decisions each have a clear owner (314.4(h)(3)).

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. Chief Executive Officer, Chief Financial Officer, General Counsel, Director of Information Security, National Tax Practice Leader, CAS Practice Leader, Director of Marketing and Communications, Chief People Officer, outside breach counsel | Client communications, refund and payment holds across the practice, external statements, resources, and reporting to the board and the private equity sponsor |
| **Incident response team (IRT)** | Incident commander: Director of Information Security. Security engineers, Chief Information Officer's identity and messaging administrators, MSSP, panel forensic firm (through counsel) | Containment, investigation, eradication, recovery |
| **Legal and notification cell** | General Counsel (lead), Privacy Officer (decision log), outside breach counsel, Director of Tax Operations (IRS), CAS Practice Leader (CAS clients), Attest Firm Quality and Independence Partner (health care clients) | Breach determinations, the three dates, every external notice |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Information Security | Security engineer (named deputy) | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Breach and notification decisions | General Counsel with the Privacy Officer | Outside breach counsel | Out-of-band group |
| IRS and state tax agency reporting | Director of Tax Operations (Responsible Official for all 6 EFINs) | National Tax Practice Leader | Stakeholder Liaison number in the incident binder |
| CAS payments and client notices | CAS Practice Leader | Chief Financial Officer | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | Company's outside general counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($15 million limit, $500,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Board and sponsor | CEO informs the audit committee chair and the sponsor's operating partner | Chief Operating Officer | Phone |
| Law enforcement | FBI field office or IC3 | Local police | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read the compromised mailbox and may hold tokens for other services. Coordinate by phone and the out-of-band group. Do not discuss the response by email or chat until the incident commander confirms the tenant is clean.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel." Keep facts (timeline, logs) separate from legal conclusions.

## 1. Preparation checks (Identify / Protect)
- [x] MFA with number matching for all staff; legacy authentication and external auto-forwarding blocked tenant-wide
- [ ] Phishing-resistant security keys for partners, administrators, finance, and CAS payroll staff; compliant devices required for mail. **Gap until POAM-012 and POAM-003 close (2027-01-15)**
- [ ] Inbox-rule, forwarding, token-reuse, and impossible-travel alerts active all year, never suppressed in season. **Restored with tuning by 2026-10-15; season plan due under POAM-007**
- [ ] Tax software, portal, DMS, and CAS activity in the SIEM with bulk-download alerts. **Gap until POAM-006 closes (2027-01-15)**
- [x] Call-back rule for refund bank, address, and email changes (POL-05 4.4). [ ] Tax software workflow flag that blocks e-file release after a bank change until the call-back is logged (P01 R-002, due 2026-12-15)
- [ ] CAS second approver and 10-day hold on first payments to a changed account (POAM-024, due 2026-12-31)
- [x] Weekly EFIN and PTIN returns-filed checks in season for all 6 EFINs (IRS Pub. 4557)
- [ ] Break-glass accounts for the identity provider and productivity suite (POL-02 4.10; P01 R-007, due 2026-12-31)
- [x] Incident binder at every office: this runbook, the ransomware runbook, the notification matrix, the call tree, the Stakeholder Liaison number, and the client call-back script
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-22
- [ ] Contract register lists each BAA's and CAS agreement's notice term (G-084; due 2026-12-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| New inbox rule that moves, deletes, or forwards mail; mailbox delegate added; app consent granted | SIEM alert; MSSP | MSSP calls the incident commander within 30 minutes; IRT opens the incident |
| Sign-in token reused from a new device, hosting network, or country; impossible travel | Identity provider alert; MSSP | Revoke sessions; open the incident |
| A staff member reports an MFA prompt or a sign-in page they did not expect | Staff report | Report immediately; IT revokes sessions and checks for token reuse |
| A client asks about an email "from the Company" requesting documents, payment, or new bank details | Client call; reception | Log the time; call the security line; do not reply to the thread |
| A request to change a refund direct deposit account, or a CAS payee or employee bank account | Preparer; CAS staff | Freeze the change (POL-03 4.7); call back on the number on file; report |
| Bulk download of attachments or DMS files | SIEM (after POAM-006) | Open the incident |
| E-file reject for a duplicate SSN, or an IRS notice about a return the client did not file | E-file team; client | Open the incident; check for data theft |
| Returns filed per EFIN or PTIN exceed the Company's own count | Weekly EFIN and PTIN check | Director of Tax Operations calls the Stakeholder Liaison and opens the incident |

**Severity 1 (declare immediately, CMT within 2 hours):** confirmed unauthorized access to any mailbox or file store holding client data, any diverted refund or client payment, or any confirmed data theft.

**Record three dates in the incident log (POL-03 4.3). Each one starts a different clock:**
| Date | Definition | Clocks it starts |
|---|---|---|
| Discovery | First day the event is known to any employee, officer, or other agent other than the attacker (16 CFR 314.4(j)(2); 45 CFR 164.410(a)(2)) | FTC notice: no later than 30 days. Business associate notice: no later than 60 days, or the shorter BAA term |
| Confirmation | The incident is confirmed as an event that can result in unauthorized disclosure, misuse, modification, or destruction of taxpayer information | IRS report: no later than the next business day (Pub. 1345) |
| Determination | The Company determines a breach occurred, or has reason to believe one occurred (Fla. Stat. 501.171) | Florida individual and Department notices: no later than 30 days. Notice to CAS clients as their third-party agent: no later than 10 days (501.171(6)(a)) |

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Revoke all sessions and refresh tokens for the account; reset the password; remove the MFA methods and registered devices; re-enroll the user in person with a security key | Identity administrator | Attacker sessions ended; user re-enrolled |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log with the discovery date | Incident commander | Log open |
| 0-1 h | Export mailbox audit, sign-in, token, app consent, and message trace logs, and file access logs for the user's files, **before any cleanup** | Security engineers with the MSSP | Logs saved to the evidence store with hash values |
| 0-1 h | Call the cyber insurer's hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Financial Officer | Claim number; counsel on the call |
| 0-2 h | Record, then remove, malicious inbox rules, forwarding, delegates, and app consents; block the attacker's sign-in sources and sending domains | Identity and messaging administrators | Mailbox matches baseline |
| 0-2 h | **Refund hold:** freeze every refund bank, address, and email change entered in the tax software in the last 30 days for clients in the user's mailbox or engagement teams; hold e-file release of those returns | Director of Tax Operations | Hold list created; no affected return transmitted |
| 0-2 h | **Payment hold:** freeze every CAS payee and employee bank change in the last 30 days and every pending payment to a changed account; call the banks to recall any payment already released | CAS Practice Leader | Hold list; recall requests logged with times |
| 1-2 h | Convene the CMT; first situation report (scope, client impact, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | CEO informs the audit committee chair and the sponsor's operating partner | Chief Executive Officer | Notice given |
| 2-4 h | Staff briefing by phone and text: what happened, the call-back rule, no discussion outside the Company, report anything unusual | Director of Marketing and Communications with HR | Briefing sent |

## 4. Analysis (RS.AN)
1. **Initial access.** Confirm the path: an adversary-in-the-middle page that relayed the user's password and MFA approval and captured the session token (the path number matching does not stop), a help desk reset (P01 R-050), or a password reused elsewhere. Search for the same phishing message in every mailbox and quarantine copies.
2. **Token and device scope.** List every token, registered device, and app consent tied to the user since the first suspicious sign-in. Check whether the attacker reached the portal staff console, the DMS, the tax software, or the CAS services with the same identity.
3. **Data accessed.** From audit logs, list every message, attachment, and file the attacker opened, downloaded, or synced. If item-level records are missing, **assume every item in the mailbox and the user's file shares was accessed** (unauthorized access is presumed to be acquisition unless reliable evidence shows otherwise, 16 CFR 314.2(m)).
4. **Messages sent by the attacker.** Search sent and deleted items and the message trace for messages to clients, CAS clients' vendors and employees, and staff. List each recipient asked for documents, payments, or bank changes.
5. **Refund diversion check.** In the tax software audit log, list every bank change in the period. Compare with the prior-year return and call each client on the number on file. Classify each return as held, transmitted and accepted, or not affected.
6. **CAS payment check.** List every payee and employee bank change and every payment in the CAS services for the period. Confirm each by call-back. For any payment to a fraudulent account, record the amount, bank, time, and recall status for the FBI report and the CAS client.
7. **Affected-individual list.** Build one list from the extracted items (Forms W-2 and 1099, prior returns, identity documents, bank letters, payroll registers, PHI samples). For each person record: name, data elements, whether they are an individual tax client (an FTC "consumer"), state of residence, whether the data was PHI held for a covered entity client, and whether it was held for a CAS client as its third-party agent.
   - **FTC count:** individual consumers only. Business entities are not counted.
   - **State counts:** every resident whose personal information was accessed, by state, including spouses, dependents, and client employees.
   - **Covered entity clients:** the individuals whose PHI each health care client must assess under its own breach rules.
   - **CAS clients:** the employees and payees whose data the Company held as each CAS client's agent.
8. **Encryption.** Customer information is treated as unencrypted for the FTC rule if the encryption key was accessed by an unauthorized person (314.2(m)). Data the attacker could open with the user's identity is therefore unencrypted for this purpose, and plain attachments always are.
9. **IRC 7216.** The attacker's access is not a "disclosure" by the Company, but any mistaken disclosure during the response would be. Do not send client data to vendors, banks, or agencies beyond what the matrix requires.
10. **Preserve evidence.** Forensics images the user's laptop if malware or a token-theft tool is suspected and keeps exported logs with chain of custody.

## 5. Containment and eradication (RS.MI)
1. Confirm no other account shows the same sign-in sources, tokens, rules, or consents. Treat any match as part of this incident.
2. Issue the user (and any other affected high-risk user) a security key now, even before the POAM-012 rollout.
3. Require compliant devices for the affected users' mail access immediately (the tenant setting can be scoped to a group).
4. Reimage the user's laptop if forensics finds malware or a browser token-theft tool.
5. Send an out-of-band warning to every client, CAS client, vendor, and employee who received a message from the attacker: phone first, then a portal message. Say the Company never asks for bank changes by email.
6. Keep every held return and payment on hold until the owner confirms the bank details by call-back and, for returns, the Stakeholder Liaison's guidance is received.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice before it goes out. The Privacy Officer keeps the **decision log** (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Discovery, confirmation, and determination dates (section 2) | General Counsel with the Privacy Officer | Decision log |
| D2 | Is this an FTC notification event (500 or more consumers, unencrypted customer information)? | General Counsel with counsel | Decision log with the consumer count |
| D3 | Breach under each state's law, by state of residence; Florida thresholds (500 for the Department; more than 1,000 for consumer reporting agencies) | Counsel | Affected-individual list by state |
| D4 | Breach of unsecured PHI for any covered entity client, and each BAA's notice term | Privacy Officer with the Attest Firm Quality and Independence Partner | BAA register |
| D5 | Data held for CAS clients as their third-party agent; each CAS agreement's notice term | CAS Practice Leader with counsel | CAS client list |
| D6 | Has law enforcement asked for a delay in writing? | Counsel | Copy of the request |
| D7 | Reimbursement of diverted refunds or client payments, and penalty relief requests | Chief Financial Officer with the General Counsel | CMT minutes |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | Chief Financial Officer |
| As soon as confirmed, and **no later than the next business day** | Report to the local IRS Stakeholder Liaison: the Pub. 1345 security incident report and the data theft report. Ask for guidance on held and transmitted returns | Director of Tax Operations |
| Same day as the IRS report | Notify the state tax agencies where affected clients file (Federation of Tax Administrators list) | Director of Tax Operations |
| Day 0-2 | Report to the FBI (IC3 or field office) with payment recall details; local police report | Director of Information Security through counsel |
| Per each BAA (5 to 10 business days in 11 BAAs) and no later than 60 days after discovery | Notice to each affected covered entity client with the affected-individual list (45 CFR 164.410) | Privacy Officer |
| Per each CAS agreement (72 hours in the current template) and no later than 10 days after determination | Notice to each affected CAS client as its third-party agent (Fla. Stat. 501.171(6)(a)) | CAS Practice Leader |
| Within 30 days after determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 | Privacy Officer with counsel |
| No later than 30 days after discovery | FTC notice on the ftc.gov form if 500 or more consumers | Privacy Officer with counsel |
| Per each state's law | Notices to residents of other states and their regulators (about 19% of individual clients) | Counsel |

**The Florida notice cannot be replaced by the FTC notice.** The deemed-compliance path in 501.171(4)(g) needs a federal regulator's rule on notice to individuals, and the FTC rule requires notice only to the FTC.

**What to tell clients.** The letter covers the state content (date range, information involved, how to contact the Company) and the IRS-recommended advice: watch for IRS letters, file Form 14039 only if the IRS sends a notice or an e-filed return is rejected for a duplicate SSN, and get an IRS Identity Protection PIN.

**Worked example (tabletop script for 2026-11-19).**
| Date | Event | Clock effect |
|---|---|---|
| Mon 2027-02-08, 23:10 | The MSSP sees a new inbox rule and token reuse from a hosting network on a tax partner's mailbox and calls the incident commander at 23:35 | Discovery recorded as 2027-02-08 (counsel confirms the MSSP's knowledge counts as the Company's). FTC outer limit **Wed 2027-03-10**. Business associate outer limit Fri 2027-04-09 |
| Tue 2027-02-09 | Forensics confirms the attacker downloaded about 2,300 attachments and synced the partner's file share, and sent 64 bank-change requests to clients and 3 payee-change requests to CAS clients' vendors | Confirmation. IRS report due by **Wed 2027-02-10**; made the same afternoon |
| Wed 2027-02-10 | A CAS bookkeeper released one $86,400 bill payment to a changed account before the hold reached the team | Bank recall and FBI report the same day |
| Mon 2027-02-15 | Counsel and the Privacy Officer determine a breach: about 1,480 individual clients (FTC consumers), 2,050 Florida residents (with spouses, dependents, and client employees), and 390 residents of 14 other states. The share held PHI samples of 212 patients from one hospital audit client and payroll registers of 2 CAS clients (140 employees) | Florida notices due by **Wed 2027-03-17**; Department notice and consumer reporting agency notice both required. Hospital BAA term: 5 business days after discovery, so notice due **Mon 2027-02-15**; sent that day. CAS agreements: 72 hours after determination, so **Thu 2027-02-18** (Florida outer limit Thu 2027-02-25) |
| Fri 2027-03-05 | FTC notice filed (before the Wed 2027-03-10 outer limit) | Done |
| Fri 2027-03-12 | Florida individual and Department notices sent (before Wed 2027-03-17); consumer reporting agencies notified | Done |

In this example the FTC clock, which runs from discovery, ends a week before the Florida clock, which runs from determination. The BAA term ends first of all. The incident team therefore works to the earliest date, not the familiar one.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7):
1. SYS-05 identity provider and administrator access (break-glass accounts if needed)
2. SYS-08 CAS payroll and bill pay: confirm no unauthorized changes before the next payroll cutoff
3. SYS-01 tax software access, after confirming no preparer account was used by the attacker
4. SYS-01 e-file queue: release held returns only after call-back confirmation and Stakeholder Liaison guidance
5. SYS-06 email: the cleaned mailbox, or a new one if forensics cannot clear the old
6. SYS-12 monitoring: confirm every alert that should have fired now fires
7. SYS-02 portal and SYS-03 DMS: confirm no access from the attacker's sources; move targeted clients to portal-only delivery

**Validate before closing:** no sign-ins or token use from attacker sources for 14 days; affected users on security keys; all held returns and payments resolved. Tell staff and affected clients when normal service resumes (RC.CO). During filing season, file extensions early for any client whose return cannot be released in time.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days of closing (POL-03 4.11).
- Update the risk register (P01: R-001, R-002, R-003, R-020, R-023), the POA&M (P07), training content (AT-2), and this runbook.
- Include the event in the Qualified Individual's next written report to the board (314.4(i)).
- Keep all incident records, the decision log, and notices for at least 6 years (POL-01 4.13), which also covers the 5-year retention of any Florida no-harm determination (501.171(4)(c)).

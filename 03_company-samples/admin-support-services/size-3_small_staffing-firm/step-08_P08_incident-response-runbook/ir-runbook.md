# Incident Response Runbook: Payroll and HR System Breach Exposing Worker PII

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm) |
| Tier / Vertical | Small / Administrative and Support and Waste Management and Remediation Services |
| Incident type | Payroll and HR system breach exposing worker PII: account takeover of the payroll platform (SYS-02) through an adversary-in-the-middle phishing page, export of the associate register (names, SSNs, addresses, bank accounts), and fraudulent direct deposit changes before payroll |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (Information Security Lead) |
| Approved | 2026-08-31 by the COO |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-014) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | COO | Incident line (cell), then the out-of-band group chat on personal phones |
| Payroll containment and pay continuity | Payroll Manager | Controller | Cell; payroll vendor's fraud and support line |
| Breach determination and notices | HR and Compliance Manager, with outside counsel | COO | Cell |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Forensics | Forensic firm (insurer panel) | Managed IT provider | Via counsel |
| Vendors | Payroll vendor security team; ATS vendor support | Account managers | Numbers in the vendor inventory |
| Communications | COO | Outside PR (via counsel) | Cell |
| Law enforcement | FBI IC3 and local field office | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker may be reading email. Coordinate by phone and the printed contact list in the incident binder at HQ.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at HQ: this runbook, contacts, the notification matrix, notice templates (English and Spanish)
- [ ] Payroll platform behind SSO with number-matching MFA; SMS codes disabled (POAM-002). **Gap until it closes**
- [ ] Alerts on payroll exports and bank-account changes routed to the IT Manager and Payroll Manager (POAM-008, POAM-019). **Gap until they close**
- [ ] Call-back verification and one-payroll hold on new bank accounts (POL-02 4.6; POAM-022)
- [ ] Payroll vendor fraud contact and procedure for stopping or recalling direct deposits confirmed in writing
- [ ] Report from payroll of each associate's residence state, runnable in under 1 hour (needed for notice planning)
- [ ] Break-glass accounts sealed and tested (POL-02 4.8)
- [ ] Log retention of at least 1 year for the identity provider and payroll audit reports (POAM-008)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Several associates report on payday that their pay did not arrive, or that their bank account changed without their request | Branch calls, recruiter texts | Call the incident line. Payroll Manager pulls the bank-change report for the last 14 days |
| Payroll staff member reports entering a password and code on a page reached from an email or text | Staff report | Reset the password, revoke sessions, review payroll sign-ins and exports; escalate if any export or change occurred |
| Payroll platform alert: bulk export of the employee register, or many bank changes in one session | Payroll alert (once POAM-019 closes) | IT Manager opens the incident immediately |
| Sign-in to the payroll platform from a new location or device during off-hours | Payroll vendor notice or sign-in report | Verify with the user by phone; if not them, declare |
| Vendor tells the firm of a breach at its end | Payroll or ATS vendor (Fla. Stat. 501.171(6)) | Declare; request the information needed for notice |
| Extortion email claiming to hold associate data | Email | Declare; preserve the message; do not reply |

**Declare a payroll data breach incident when** any unauthorized bank-account change, export, or report download containing SSNs is confirmed, or a vendor reports a breach of firm data.
**Record the time of determination.** Florida's 30-day notice clocks run from the determination of the breach or reason to believe a breach occurred (Fla. Stat. 501.171(3)(a), (4)(a)). Write down who decided what, and when.

## 3. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Freeze all bank-account changes in the payroll platform (vendor-side freeze if the firm cannot trust its admin accounts) | Payroll Manager with the payroll vendor | Freeze confirmed in writing by the vendor |
| 2. Disable the compromised user, reset all payroll platform passwords, revoke sessions, and remove any unknown MFA devices or phone numbers | IT Manager with the payroll vendor | No active sessions remain |
| 3. List every bank change and export in the last 30 days (earlier if logs allow) and have the Payroll Specialists confirm each change by call-back to the phone number on file | Payroll Manager | Fraudulent changes identified |
| 4. Stop or recall pending direct deposits to fraudulent accounts through the payroll vendor and its bank; ask the receiving banks to freeze funds | Controller with the payroll vendor | Recall requests logged |
| 5. Call the cyber insurer's breach hotline. Engage counsel and forensics through the insurer | COO | Claim number issued |
| 6. Report the payroll diversion to FBI IC3 | IT Manager | IC3 report number recorded |
| 7. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

**Pay the associates.** Diverted pay is still owed. The Payroll Manager runs an off-cycle payment to the verified accounts (or issues pay cards) for every associate whose pay was diverted, within 1 business day. This is a business decision the COO has pre-approved; it does not wait for fund recovery.

## 4. Analysis (RS.AN)
1. **Scope:** which payroll accounts were used, which reports or exports ran, and whether the attacker also reached email, the ATS (I-9 module, consumer reports), or the reporting database. Check identity provider sign-ins, payroll audit reports, ATS admin history, and cloud database logs.
2. **Initial access:** identify the phishing message, the fake page, and how the SMS code was captured.
3. **Preserve evidence:** export payroll audit reports and identity provider logs before they roll over (identity provider logs are kept only 30 days today; POAM-008). Keep the phishing message. Maintain chain of custody through the forensic firm.
4. **Data involved:** list the exported fields. **SSN with name is personal information under Fla. Stat. 501.171(1)(g)1.a.(I).** A financial account number counts only with a code or password that permits account access (1.a.(III)), so bank numbers alone may not trigger Florida notice; counsel confirms, and other states may differ.
5. **Who is affected and where they live:** run the residence-state report for every person in the export (current and former associates). This drives which state laws apply.
6. **E-Verify data:** if the ATS I-9 module or any E-Verify account was touched, the DHS notice duty in MOU Art. II.A.16 applies **immediately**.

## 5. Containment and eradication (RS.MI)
1. Block the phishing domains and sender addresses in email; search and purge the same message from all mailboxes.
2. Move the payroll platform to SSO with number-matching MFA as an emergency change (POAM-002), or, until then, require vendor-side call-back for every admin sign-in.
3. Rotate the integration service's payroll and ATS API credentials.
4. Check for persistence: new payroll users, changed notification emails, report schedules sending data outside the firm, mail forwarding rules.
5. Keep the bank-change freeze until every change since the compromise date has been verified by call-back.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Day 0 | Insurer notified; counsel engaged; IC3 report | COO / IT Manager |
| Day 0 (immediately, if E-Verify data involved) | Notice to DHS E-Verify (phone or E-Verify@dhs.gov, subject "Privacy Incident - Password") | HR and Compliance Manager |
| Day 0-2 | Associate and staff briefing: pay will be made whole; do not change bank details by email or text; how to verify a call from the firm | COO |
| Day 0-3 | IRS notice to dataloss@irs.gov, subject "W2 Data Loss", with contact details only (IRS guidance) | Controller |
| Per contract (72 hours for the two largest clients) | Client notices, only if client data was involved | COO |
| As soon as known | Breach determination under Fla. Stat. 501.171 and other states' laws, documented | HR and Compliance Manager and counsel |
| Within 30 days of determination | Florida individual notices by mail or email (English and Spanish templates); Department of Legal Affairs notice if 500 or more Floridians. Individual notices may get 15 more days only if good cause for delay is given to the department in writing within the 30 days (501.171(3)(a)) | HR and Compliance Manager and counsel |
| Without unreasonable delay | Nationwide consumer reporting agencies if more than 1,000 people are notified at once | HR and Compliance Manager |
| Per each state's law | Notices to residents of other states and their regulators | Counsel |

**Plan to the 30-day clock.** It runs from determination, not from when the investigation ends. The residence-state report and the templates must be ready before an incident. If law enforcement asks for a delay in writing, notices are held for the period requested (501.171(4)(b)).

**Credit monitoring and identity protection** for affected people is a firm decision taken with counsel and the insurer; it is not stated as a Florida requirement here.

**Extortion:** any payment requires the President, counsel, the insurer, and an OFAC sanctions check (POL-03 4.6). Paying does not remove notice duties.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Identity provider and payroll platform access for the payroll team, with SSO and MFA in place
2. Verified bank data for every associate (call-back list complete), then lift the bank-change freeze
3. Weekly payroll run on schedule (BP-01, MTD 48 h), with the Controller reviewing every bank change since the incident
4. Client dispatch and time capture (normally unaffected in this scenario)
5. Reporting database access only after SSNs and bank numbers are removed (POAM-005)

**Validate before closing recovery:** no unknown users or report schedules in payroll, all diverted associates paid, and the next weekly payroll run reconciled. Tell associates and clients when normal operations resume (RC.CO-03).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-005, R-017), the POA&M (P07), and this runbook.
- Keep the Florida no-harm determination (if any) for at least 5 years (501.171(4)(c)) and all incident records for at least 6 years (POL-01 4.10).

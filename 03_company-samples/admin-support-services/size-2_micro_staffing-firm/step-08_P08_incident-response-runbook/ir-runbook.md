# Incident Response Runbook: Payroll and HR System Breach Exposing Worker PII

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm) |
| Tier / Vertical | Micro / Administrative and Support and Waste Management and Remediation Services |
| Incident type | Takeover of a payroll administrator account through an adversary-in-the-middle (AiTM) phishing page; export of the employee census report (names, SSNs, dates of birth, addresses, bank accounts, pay); fraudulent direct deposit changes before Friday payroll |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Operations Manager (Security and Privacy Lead) |
| Approved | 2026-08-31 by the Owner |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POAM-008) |

## 0. Roles and notification chain (Govern)
The firm has 7 staff and no IT staff. The MSP does the technical work on laptops and the suite; the payroll vendor does the payroll-side containment; the cyber insurer supplies breach counsel and forensics. The Operations Manager runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Operations Manager | Owner | Cell phone (printed contact card) |
| Decision maker (money, notices, extortion, client messages) | Owner | Operations Manager | Cell phone |
| Payroll containment | Onboarding and Payroll Coordinator with the payroll vendor's fraud or support line | Operations Manager | Vendor phone number on the contact card (not from email) |
| Technical response | MSP incident line (emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel | Insurer panel counsel | n/a | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm | n/a | Engaged by breach counsel, as counsel advises |
| The firm's bank | Business banking fraud line | Relationship manager | Number on the contact card |
| Law enforcement | FBI IC3 online; local FBI field office | n/a | Numbers in the binder |

**Notification chain in the first hour:** staff member or associate call → Operations Manager → payroll vendor (Coordinator) and Owner at the same time → MSP incident line → insurer breach hotline (Owner) → breach counsel and forensics (through the insurer).

**Out-of-band first.** Assume the victim's email and phone number may be watched. Coordinate by phone call, not email or text, using the printed contact card, and never use contact details from a suspicious message.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the locked records room and at the Operations Manager's and Owner's homes: this runbook, contact card, notification matrix, notice templates (English and Spanish), and the breach determination form
- [ ] Payroll administrators on authenticator-app MFA, not SMS (IA-2(1)). **Gap until POAM-004 closes**
- [ ] Payroll alerts on bank-account changes and report exports sent to the Operations Manager and the Owner (SI-4). **Gap until POAM-006 closes**
- [ ] Call-back rule for bank changes and check of the first payroll after any change (POL-02 B.4)
- [ ] Residence-state report saved in the payroll service (counts of current and former workers by state)
- [ ] Payroll vendor's fraud contact and its process for freezing bank changes and recalling deposits written on the contact card
- [ ] Insurer hotline and policy number checked at each renewal; MSP contract includes incident notice terms (R-013)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| An associate says their pay went elsewhere, or they got a "bank account changed" email they did not expect | Associate call or text to a recruiter | Recruiter calls the Operations Manager at once. Do not change anything in the associate's record yet |
| Payroll alert: bank-account change, census or tax report export | Payroll alert (once POAM-006 closes) | Operations Manager checks who made it within 30 minutes |
| A staff member typed a password into a page reached from an email or text, or got an MFA code they did not ask for | Staff report (POL-03 4.2) | Reset the password from a clean device; Operations Manager reviews payroll and suite activity |
| Payroll vendor reports unusual sign-ins or a breach on its side | Vendor (Fla. Stat. 501.171(6)(a)) | Declare; ask for the information needed for notices |
| Email or call from someone claiming to hold worker data | Extortion message | Do not reply. Save it. Declare |

**Declare a payroll data breach incident** when any of these is confirmed: a bank-account change the worker did not request; a sign-in to a payroll administrator account by someone other than its owner; a census, tax, or W-2 report exported by someone not authorized; or a vendor's notice of a breach involving firm data (POL-03 4.4).

**Write down the determination time.** Florida's 30-day clocks run from the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(3)(a), (4)(a)). Record who decided what, and when.

## 3. First hour (RS.MA, RS.MI)
Payroll is due in the payroll service by **Wednesday 5 p.m.** for Friday direct deposit (P05 BP-02). Containment must finish before that cutoff if at all possible.

| Step | Who | Done when |
|---|---|---|
| 1. Call the payroll vendor (number from the contact card): freeze all bank-account changes for the firm's account; hold or recall any pending deposits to changed accounts; ask for the audit log of sign-ins, exports, and bank changes for the last 30 days | Coordinator with the vendor | Vendor confirms the freeze in writing |
| 2. From a clean laptop, reset the passwords of all 3 payroll administrators, sign out all sessions, and remove any MFA phone number or device the firm did not add | Operations Manager | Sessions revoked; MFA list clean |
| 3. Call the MSP incident line: reset the affected staff member's suite password, revoke sessions, check for forwarding rules and new app consents, and scan their laptop | Operations Manager; MSP | MSP confirms |
| 4. Call the insurer's breach hotline and give the claim details | Owner | Claim number issued; counsel assigned |
| 5. Call the firm's bank fraud line if any deposit has already been sent to a changed account | Owner | Recall request logged |
| 6. Open the incident log: timeline, actions, who, when | Operations Manager | Log started |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the payroll vendor and the MSP supplying logs.
1. **Initial access.** Find the phishing message, the fake page, and the account used. Search all mailboxes for the same message and remove it (MSP).
2. **What the attacker did in payroll.** From the vendor's audit log: sign-ins (time, location, device), reports exported (which report, which fields, how many people), bank changes (which workers, old and new account), and any change to administrator users, MFA, or notification settings.
3. **Preserve evidence.** Export the payroll audit log, the suite sign-in and file logs (they age out after 90 days until POAM-006 closes), and the phishing email with headers. Keep a chain-of-custody record.
4. **Other systems.** Did the attacker reach the suite, the ATS, the Onboarding folder, or E-Verify? Check sign-in logs for the same IP addresses and devices. **If any E-Verify data or credentials were reachable, the DHS notice is due immediately (MOU Art. II.A.16).**
5. **Whose data, and where they live.** Build the affected list from the export: in the expected scenario, the census report covers about 318 current and former associates and staff since 2023-01, of whom about 301 have Florida addresses and about 17 live in 6 other states. Run the residence-state report.
6. **Data elements.** A name with an SSN is personal information under Fla. Stat. 501.171(1)(g)1.a.(I). A bank account number counts only with a code or password that permits access to the account (1.a.(III)), so the SSNs, not the bank numbers, drive Florida notice; counsel confirms, and other states may differ.

## 5. Containment and eradication (RS.MI)
1. Keep the bank-change freeze until every change since the earliest attacker sign-in has been confirmed by a call-back to the phone number on file before the compromise.
2. Restore each fraudulently changed bank account to the verified one, and record the call-back.
3. Remove anything the attacker added: payroll users, MFA devices or phone numbers, notification changes, suite forwarding rules, app consents.
4. Move the 3 payroll administrators to authenticator-app MFA before the freeze is lifted, if POAM-004 has not already done it.
5. Block the phishing domains and sender addresses in the suite (MSP).
6. Confirm with forensics that no other account was taken over before declaring containment complete.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice before it goes out. The Operations Manager records the breach determination; for a census export with SSNs, plan on notification, because a no-harm determination (501.171(4)(c)) is not credible when SSNs and bank details were taken.

| When | Action | Owner |
|---|---|---|
| Hour 1 | Payroll vendor freeze; insurer notified; counsel and forensics assigned; MSP engaged | Coordinator; Owner; Operations Manager |
| Immediately, if E-Verify data or credentials are involved | DHS E-Verify by phone (888-464-4218) or E-Verify@dhs.gov, subject "Privacy Incident - Password" | Operations Manager |
| Day 0-1 | FBI IC3 report (supports recovery of diverted deposits and any law enforcement delay request) | Owner |
| Day 0-1 | Affected associates called: pay will be made whole on Friday; the firm never asks for bank changes by email or text; how to confirm a call is really from the firm | Operations Manager with the recruiters |
| Day 0-3 | IRS notice to dataloss@irs.gov, subject "W2 Data Loss", contact details only (IRS guidance); statealert@taxadmin.org for state tax agencies | Operations Manager |
| As soon as scope is known | Breach determination documented; affected list by state; credit monitoring offer decided with counsel and the insurer | Operations Manager with counsel |
| Within 30 days of determination | Florida notices to each affected Florida resident by mail or email (English and Spanish templates). Individual notices may get 15 more days only if good cause for delay is given to the Department of Legal Affairs in writing within the 30 days (501.171(3)(a)). Department notice only if 500 or more Floridians are affected (not expected for the census report) | Operations Manager and counsel |
| Per each state's law | Notices to residents of other states and to any regulator those states require | Counsel |
| If a client's information was involved | Client notice under its contract | Account Manager with the Owner |

**Plan to the 30-day clock.** It runs from determination, not from the end of the investigation. If law enforcement asks in writing for a delay, notices are held for the period requested (501.171(4)(b)).

**Inbound notices.** If the breach happened at the payroll vendor (for example, an attack on its platform rather than on the firm's accounts), the vendor must notify the firm no later than 10 days after its determination and give the information needed for notice (501.171(6)(a)). The firm still sends the notices; the vendor may send them on the firm's behalf, but a failure by the vendor counts against the firm (501.171(6)(b)).

**Extortion:** only the Owner decides, with breach counsel and the insurer and after an OFAC sanctions check (POL-03 4.11). Paying does not remove any notice duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05), with payroll first in this incident:
1. **Payroll on time (BP-02).** Submit Friday's payroll only after every bank change is verified. Pay any associate whose deposit was diverted by an off-cycle payment or printed check approved by the Owner, on the normal payday.
2. **Time capture and approvals (BP-04).** Confirm client approver accounts were not changed.
3. **Orders and onboarding (BP-01, BP-03).** Staff resume work on clean laptops with reset passwords.
4. **Lift the freeze** only after the call-back list is complete and the vendor confirms no unauthorized administrator remains.

**Before closing:** the Owner reviews every bank change since the incident for the next 4 payroll cycles. Tell associates and staff when payroll is back to normal (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, the payroll vendor if involved, and counsel. Written summary within 30 days (POL-03 4.13).
- Update the risk register (P01 R-001, R-002, R-003, R-016), the POA&M (P07), and this runbook.
- Keep the incident log, breach determination, notices, and forensic report for at least 5 years (POL-02 A.7; 501.171(4)(c) sets 5 years for any no-harm determination).

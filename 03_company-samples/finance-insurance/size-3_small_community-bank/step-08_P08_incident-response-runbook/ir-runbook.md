# Incident Response Runbook: Business Email Compromise and Fraudulent Wire Transfer

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (community commercial bank; subsidiary of Cris Santos Company, a bank holding company) |
| Tier / Vertical | Small / Finance and Insurance |
| Incident type | Business email compromise (BEC): a business customer's email account is taken over and used to send a fraudulent wire request, sometimes combined with use of the customer's stolen online banking password |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; POL-02 4.8 (wire callback) |
| Regulatory basis | 12 CFR 30 App. B III.C.1.g and Supplement A (N52-R02); 12 CFR Part 53; 12 CFR 225.302; 12 CFR 21.11 |
| Runbook owner | IT Manager (Information Security Officer) |
| Approved | 2026-08-31 by the President and CEO |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-016) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Information Security Officer (IT Manager) | Chief Operating Officer | Incident line (cell), then the out-of-band group chat on bank-issued phones |
| Wire recall and account holds | Deposit Operations Manager | Senior wire-room approver | Wire room direct line |
| Online banking containment | Treasury Management Officer | Deposit Operations Manager | Cell |
| Fraud, SAR, and law enforcement | BSA/AML Officer | Compliance Officer | Cell |
| Customer notice and state breach law | Compliance Officer (Privacy Officer) | Outside counsel | Cell |
| Notification incident decision and OCC and Federal Reserve notice | President and CEO with the ISO | Chief Operating Officer | Cell; OCC and Federal Reserve contacts in the incident binder |
| Technical response | MSSP 24x7 team | Forensic firm through the cyber insurer's panel | MSSP hotline |
| Providers | Digital banking provider and payments service provider support desks | Account managers | Numbers in the incident binder |
| Legal counsel | Outside bank counsel | n/a | Cell |
| Insurance | Financial institution bond and cyber policy carriers | n/a | Claim lines in the incident binder (held by the CFO) |
| Communications | President and CEO | Outside communications firm (through counsel) | Cell |

**Out-of-band first.** If a bank mailbox may be involved, assume email is compromised. Coordinate by phone and the printed contact list in the incident binder (main office and Branch 4).

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at the main office and Branch 4: this runbook, the contact list, OCC and Federal Reserve contacts, wire recall request forms, and the notification matrix
- [ ] Callback enforced as a required field in the wire platform, with monthly callback sampling (POL-02 4.8). **Gap until POAM-007 closes**
- [ ] MFA required for business online banking users and out-of-band confirmation of new beneficiaries (POL-02 4.4). **Gap until POAM-002 closes**
- [ ] Alerts on new beneficiaries and limit changes routed to Treasury Management and the MSSP (SI-4). **Gap until POAM-006 closes**
- [ ] Designated 12 CFR 53.4 contacts sent to the core processor, digital banking provider, and card processor (POAM-009, due 2026-09-30)
- [ ] Admin console, wire platform, and identity provider logs kept at least 1 year in the central log archive (AU-11). **Gap until POAM-004 closes**
- [ ] Branch and wire-room staff trained on BEC red flags and the 15-minute reporting rule (POL-05 4.4; POL-03 4.2)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Customer reports a wire they did not request, or asks where a wire went | Customer call to branch or treasury management | Call the incident line and the Deposit Operations Manager **within 15 minutes**. Start the wire recall at once (section 3, step 1) |
| Callback reaches the customer, who denies sending the request | Branch or wire room | Do not send. Report within 15 minutes. Tell the customer their email may be compromised |
| Email request with changed beneficiary instructions, urgency, or a look-alike domain | Branch staff, wire room | Hold the request; callback to the number on file; report if the customer denies it |
| New beneficiary added, or limit raised, by a password-only business user | Daily new-beneficiary report; provider fraud alert | Treasury Management calls the customer at the number on file before any wire to that beneficiary |
| Beneficiary bank reports a suspicious incoming wire from the bank | Beneficiary bank fraud desk | Deposit Operations opens the incident |
| Online banking login from a new device or foreign location followed by beneficiary changes | Provider fraud scoring | Suspend the user; call the customer |

**Declare a BEC incident when** a wire or ACH payment was sent, or was about to be sent, on instructions the customer did not give, or a customer's email or online banking credentials are confirmed to be in an attacker's hands.
**Record two times:** when the bank first learned of the fraud (starts the SAR clock under 12 CFR 21.11(d)), and, separately, when the bank determines whether it is a notification incident (starts the 36-hour clock under 12 CFR 53.3, only if it is one).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Call the beneficiary bank's wire or fraud department, request a recall and a freeze, and follow up in writing. Send the recall through the payment system messaging where available | Deposit Operations Manager | Recall request acknowledged; reference number logged |
| 2. Report to the FBI through IC3 with the wire details (amount, date, beneficiary bank and account) | BSA/AML Officer | IC3 complaint number logged |
| 3. Suspend the customer's online banking users; cancel pending wires and ACH files; block the fraudulent beneficiary templates | Treasury Management Officer | Users suspended; pending items cancelled |
| 4. Call the customer at the phone number on file (never a number from the email). Tell them to secure their email account and that the bank will not act on emailed instructions until further notice | Relationship officer with Treasury Management | Customer informed; call logged |
| 5. Check other customers: search the wire platform for the same beneficiary account, the same email domain, or the same IP address in online banking logs | Deposit Operations and the ISO | Search results logged |
| 6. Open the incident register entry, linked to the BSA case number, and start the timeline | ISO and BSA/AML Officer | Entry open |
| 7. Notify the bond and cyber insurance carriers | Chief Financial Officer | Claim numbers issued |

## 4. Analysis (RS.AN)
1. **How the request arrived.** Branch, email, phone, or online banking. Get the original email with full headers from the branch mailbox, and export the online banking and wire platform audit trails for the customer's users (sign-ins, device, IP, beneficiary changes, limit changes).
2. **Was the callback done?** Check the callback field and the branch's notes. If it was skipped, record the branch, the staff member, and the reason. This drives the funds-transfer liability analysis (Fla. Stat. 670.202) and the training response.
3. **Bank-side compromise?** Confirm that no bank mailbox, admin console account, or wire-room account was used. Check identity provider sign-in logs and mailbox forwarding rules for the branch staff involved. Default identity provider retention is only 30 days (POAM-004), so export logs now.
4. **Customer information accessed.** List what the attacker saw in online banking (balances, account numbers, statements, wire history). A user name and password that allow access to an account are sensitive customer information under Supplement A, and a user name with a password is personal information under Fla. Stat. 501.171.
5. **Scale.** One customer or many? Many customers, the same attacker infrastructure across accounts, or any bank-side compromise changes the notification incident decision (section 6).
6. **Preserve evidence.** Keep emails, audit exports, the recall correspondence, and call recordings with a chain-of-custody log. Evidence also supports the SAR (retain supporting documents 5 years, 12 CFR 21.11(g)).

## 5. Containment and eradication (RS.MI)
1. Keep the customer's online banking users suspended until the customer confirms its email is clean and new credentials are issued in branch or by an out-of-band call. Require MFA before re-enabling, even before the bank-wide deadline.
2. Delete fraudulent beneficiary templates and reset the customer's limits to the agreed levels.
3. Flag the customer's profile so that email wire requests are refused until the customer and the Treasury Management Officer agree new instructions.
4. If a bank mailbox or account was involved: reset credentials, revoke sessions and tokens in the identity provider, remove forwarding rules, and have the MSSP check for persistence.
5. Block the attacker's email domains and IP addresses at the email gateway, and give the IP addresses to the digital banking provider.
6. Send a same-day alert to all branch and wire-room staff: the red flags seen, and a reminder that every emailed request needs a callback to the number on file.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each notice before it goes out.

**Notification incident determination (12 CFR 53.2(b)(7)).** The ISO and the President and CEO answer, and record with the date and time:
- Has the incident materially disrupted or degraded, or is it reasonably likely to, the bank's ability to serve a material portion of its customers? (For example: the wire platform or online banking is unavailable or untrustworthy for many customers.)
- Has it affected a business line whose failure would cause material loss of revenue, profit, or franchise value? (For example: wire or treasury management services must be suspended.)
- Is a bank-side system (bank mailboxes, the admin console, the wire room) compromised?

A fraud against one customer through the customer's own email is usually **not** a notification incident. The determination, and the reasons, are recorded either way. If the answer is yes, the OCC must receive notice within 36 hours of the determination, and the Federal Reserve too if the holding company is affected (12 CFR 225.302).

| When | Action | Owner |
|---|---|---|
| Hour 0 | Wire recall request; IC3 report; insurers notified | Deposit Operations Manager; BSA/AML Officer; CFO |
| Hour 0 to 4 | Notification incident determination recorded | ISO and President and CEO |
| Immediately, if the fraud is ongoing | Telephone notice to law enforcement and the OCC (12 CFR 21.11(d)) | BSA/AML Officer |
| As soon as possible | OCC notice of unauthorized access to sensitive customer information (Supplement A II.A.1.b) | President and CEO |
| Within 36 hours of a "yes" determination | OCC notice (12 CFR 53.3); Federal Reserve notice if the holding company is affected (12 CFR 225.302) | President and CEO |
| As soon as possible after misuse is confirmed | Written customer notice with the Supplement A III.B content (the business customer, and any individual whose credentials were used) | Compliance Officer |
| Within 30 days of determination | Florida individual notice, or reliance on the Supplement A notice under the deemed-compliance path (Fla. Stat. 501.171(4)) | Compliance Officer and counsel |
| Within 30 calendar days of initial detection | SAR filed (up to 60 days only if no suspect is identified) | BSA/AML Officer |
| Promptly after filing | Audit and Risk Committee told of the SAR (12 CFR 21.11(h)) | BSA/AML Officer |

**Plan to the shorter clock.** The 36-hour clock, when it applies, runs from the determination, so make the determination early and write it down. The SAR clock runs from initial detection, not from the end of the investigation.

**Customer liability.** If the branch skipped the callback that the funds transfer agreement makes the security procedure, the payment order may not be effective as the customer's order (Fla. Stat. 670.202), and the bank would have to refund it with interest (670.204). Counsel decides. Do not tell the customer the loss is theirs before counsel has reviewed it.

**Staff and customer communications.** Staff do not discuss the case outside the bank, and never mention a SAR (12 CFR 21.11(k)). Customer-facing statements come from the President and CEO.

## 7. Recovery (RC.RP, RC.CO)
A BEC incident rarely takes systems down. Recovery means restoring safe service to the affected customer and confirming that payment services are trustworthy. If a bank system was compromised, restore in BIA priority order (P05):
1. Identity provider and administrator access (break-glass accounts if needed)
2. Branch networks and circuits to the core processor
3. Core banking access (branch services)
4. Wire platform and payments workstations (alternate wire procedure at Branch 4 if needed)
5. Phones and email (callbacks depend on phones)
6. Online and mobile banking
7. Card and ATM services, then lending and reporting systems

**For the affected customer:** new credentials issued out of band, MFA enrolled, beneficiaries and limits reviewed with the customer, and a written note of the agreed security procedure. Record the amount recovered through the recall and any refund decision.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing the case (POL-03 4.11 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-009, R-026), the POA&M (P07), and this runbook.
- Add the case, with names removed, to the next BEC training session (POL-05 4.4).
- Report the incident and management's response in the annual board report (12 CFR 30 App. B III.F).
- Retain incident records for at least five years (POL-01 4.13).

## 9. Worked example (tabletop script)
| Time | Event | Clock or decision |
|---|---|---|
| Day -1, 16:40 | Attacker signs in to the customer's online banking with a stolen password (no MFA) and views balances and recent wires | Not yet known to the bank |
| Day 0, 09:55 | Branch 3 receives an email from the customer's real address asking for a $148,500 wire to a new beneficiary for "equipment" | Red flags: new beneficiary, urgency |
| Day 0, 10:20 | The universal banker skips the callback ("known customer") and sends the request to the wire room | Security procedure not followed |
| Day 0, 11:05 | Wire keyed and approved (maker-checker) and sent | |
| Day 1, 09:30 | Customer calls about the wire; branch reports within 15 minutes | **Initial detection: SAR clock starts** |
| Day 1, 09:45 | Recall request to the beneficiary bank; IC3 report; users suspended | |
| Day 1, 12:00 | ISO and CEO determine: not a notification incident (one customer; no bank system compromised; services normal). Determination recorded | 36-hour clock does not start |
| Day 1, 15:00 | OCC told of unauthorized access to sensitive customer information (Supplement A) | |
| Day 3 | Customer notice sent; counsel reviews the refund question | Florida 30-day clock tracked from Day 1 |
| By Day 31 | SAR filed; Audit and Risk Committee told | 12 CFR 21.11(d), (h) |

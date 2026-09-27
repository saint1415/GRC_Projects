# Incident Response Runbook: Business Email Compromise and Fraudulent Wire Transfer

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (regional commercial bank), subsidiary of Cris Santos Company, Inc. (bank holding company) |
| Tier / Vertical | Mid-Market / Finance and Insurance |
| Incident type | Business email compromise (BEC): a business customer's email is taken over; the attacker first has the customer's phone number on file changed by an emailed request, then sends a wire request, so the wire callback reaches the attacker. Variants: real-time phishing of a business online banking user (relayed one-time code), and a compromised relationship manager mailbox |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy; POL-02 4.6 (contact-change verification) and 4.11 (wire callback); STD-04 |
| Regulatory basis | 12 CFR 30 App. B III.C.1.g and Supplement A (N52-R02); 12 CFR Part 53; 12 CFR 225.302; 12 CFR 21.11; 12 CFR 41.90; state breach laws (Florida as the worked example) |
| Companion documents | `ir-runbook-core-outage.md` (core processor cyber incident and outage); `notification-matrix.csv`; BIA (P05 BP-01, BP-08, BP-15) |
| Runbook owner | Information Security Officer (incident commander), with the Director of Payments Operations (fraud lead) |
| Approved | 2026-09-18 by the Chief Operating Officer |
| Last tested | Not yet. Executive tabletop with General Counsel scheduled 2026-11-30 (POAM-012) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so fraud, technical, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. President and CEO, CRO, CFO, General Counsel, ISO, Chief Compliance Officer, BSA/AML Officer, Director of Marketing and Communications | Convened for severity 1 (see section 2): customer and media statements, refunds and customer relief, resources, escalation to the board |
| **Fraud and incident response team** | Incident commander: ISO. Fraud lead: Director of Payments Operations. Treasury Management Director, BSA/AML Officer, Retail Banking Director or Contact Center Director, MSSP | Recall, containment, investigation, scoping, evidence |
| **Legal and regulatory** | General Counsel (lead), Chief Compliance Officer, BSA/AML Officer; outside counsel through the cyber insurer panel when notices or claims are likely | Notification incident determination (with the CEO and the ISO), customer and state notices, SAR, funds-transfer liability |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Information Security Officer | IT Risk and Compliance Manager | Incident line; out-of-band group on bank-issued phones |
| Fraud lead (recalls and holds) | Director of Payments Operations | Senior wire room supervisor | Wire room direct line |
| Online banking containment | Treasury Management Director | Director of Payments Operations | Cell |
| Contact-change reversal | Retail Banking Director (branches); Contact Center Director (phone) | Director of Deposit Operations | Cell |
| Fraud, SAR, and law enforcement | BSA/AML Officer | Chief Compliance Officer | Cell |
| Customer and state notices | Chief Compliance Officer | General Counsel | Cell |
| Notification incident decision; OCC and Federal Reserve notices | President and CEO with the ISO and General Counsel | Chief Operating Officer | Cell; OCC and Federal Reserve contacts in the incident binder |
| Legal counsel | General Counsel | Outside bank counsel; insurer panel breach counsel | Cell |
| Technical response | MSSP 24x7 team | Insurer panel forensic firm (engaged by counsel) | MSSP hotline |
| Insurance | CFO (financial institution bond and cyber policy) | Controller | Claim lines in the incident binder |
| Communications | Director of Marketing and Communications | Outside communications firm (through counsel) | Cell |

**Out-of-band first.** If a bank mailbox may be involved, assume email is compromised. Coordinate by phone and the printed contact list in the incident binder (headquarters and Georgia regional office).

**Legal privilege protocol.** When notices, refunds, or claims are likely, General Counsel engages outside counsel, and outside counsel engages any forensic firm. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate about fault in email or chat, and never tell a customer who bears the loss before counsel has reviewed it.

## 1. Preparation checks (Identify / Protect)
- [x] Maker-checker on every outgoing wire and a required callback field in the payments hub (self-approval of a wire was blocked in P07 testing)
- [x] Workforce MFA with number matching; EDR with 24x7 MSSP (P07 IA-2(1), SI-3 satisfied)
- [ ] Out-of-band verification and customer alerts for every contact-information change (POL-02 4.6). **Gap until POAM-011 closes (2026-12-31)**; interim rule since 2026-10-15: contact changes only in branch with identification or by callback to the prior number
- [ ] Out-of-band confirmation of new online banking beneficiaries; phishing-resistant business MFA (POL-02 4.5). **Gap until POAM-010 closes**; daily new-beneficiary review in place since 2026-10-01
- [ ] Payments hub, portal, and core security events in the SIEM with change-anomaly use cases (STD-02). **Gap until POAM-005 closes**
- [ ] Role-based fraud training for branch, contact center, and relationship manager staff (POL-05 4.4). **Gap until POAM-004 closes**
- [x] Incident binder at headquarters and the Georgia regional office: this runbook, contact lists, OCC and Federal Reserve contacts, recall request forms, and the notification matrix
- [x] Cyber insurer panel counsel and forensics confirmed; bond claim procedure on file (CFO)

## 2. Detection, severity, and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Customer reports a wire it did not request, or asks where a wire went | Customer call to a branch, relationship manager, or the contact center | Call the incident line and the fraud lead **within 15 minutes**. Start the recall at once (section 3, step 1) |
| Customer reports it did not change its phone number or email | Customer; alert letter returned | Treat as a BEC precursor: freeze wire requests for that customer; report within 15 minutes |
| Callback reaches someone who does not match the customer's known contacts, or the number on file changed recently | Wire room; branch | Do not send. Verify through the prior number or a relationship manager who knows the customer; report |
| New beneficiary added, or limit raised, followed by a wire within 24 hours | Daily new-beneficiary report; provider fraud scoring (AI-003) | Treasury management calls the customer at a verified number before release |
| Beneficiary bank reports a suspicious incoming wire from the bank | Beneficiary bank fraud desk | Fraud lead opens the incident |
| Mailbox rule forwarding external mail, or sign-in from a new country, on a relationship manager account | Identity provider and email alerts (MSSP) | MSSP contains the account; ISO opens the incident; treat as the relationship manager mailbox variant |

**Severity levels:**
- **Severity 3:** attempted fraud stopped before any payment; one customer.
- **Severity 2:** a fraudulent payment sent, or credentials of one customer confirmed compromised. Fraud and incident response team engaged; COO and General Counsel informed.
- **Severity 1:** loss above $250,000 not recalled within 24 hours, more than one customer affected by the same attacker, or any bank-side compromise (bank mailbox, admin console, payments hub, core). Convene the CMT within 2 hours (POL-03 4.4) and start the notification incident determination (section 6).

**Record three times in the incident register:** (1) when the bank first learned of facts that may require a SAR (starts the SAR clock under 12 CFR 21.11(d)); (2) when a breach of personal information was determined or reasonably believed (starts state clocks, for example Fla. Stat. 501.171); and (3) when the bank determines whether it is a notification incident (starts the 36-hour clock under 12 CFR 53.3 and 225.302, only if it is one).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Call the beneficiary bank's wire or fraud department, request a recall and a freeze, and follow up in writing; send a recall message through the payment system where available | Fraud lead | Recall acknowledged; reference number logged |
| 2. Report to the FBI through IC3 with the wire details (amount, date, beneficiary bank and account) | BSA/AML Officer | IC3 complaint number logged |
| 3. Suspend the customer's online banking users; cancel pending wires and ACH files; block fraudulent beneficiary templates | Treasury Management Director | Users suspended; pending items cancelled |
| 4. **Reverse the contact-information change** and restore the prior phone number and email from the core audit history; flag the account so no maintenance is accepted except in branch with identification | Retail Banking Director or Contact Center Director | Contact data restored; flag set |
| 5. Call the customer at the **prior, verified** phone number (never a number from the email or the changed record). Tell them to secure their email and that the bank will not act on emailed instructions until further notice | Relationship manager with treasury management | Customer informed; call logged |
| 6. Check for other victims: search the payments hub for the same beneficiary account, the same email domain, the same caller number, or the same IP address in online banking logs; search contact changes in the last 30 days made from the same channel or number | Fraud lead and ISO (MSSP assists) | Search results logged |
| 7. Open the incident register entry linked to the BSA case number; start the timeline | ISO and BSA/AML Officer | Entry open |
| 8. Notify the bond carrier (fraud loss) and, if any bank system may be involved, the cyber insurer through its hotline before engaging vendors | CFO | Claim numbers issued |

## 4. Analysis (RS.AN)
1. **How the change and the request arrived.** Get the original emails with full headers, the call recordings, and the core audit record of the contact change (who made it, from which channel, with what verification). Export online banking and payments hub audit trails for the customer's users. Payments hub logs are kept only 90 days (POAM-005), so export them now.
2. **Was the security procedure followed?** Check the callback field, the number called, and whether that number had changed. The funds transfer agreement makes the callback part of the agreed security procedure; whether the bank followed it drives the liability analysis under UCC Article 4A (Fla. Stat. 670.202 and 670.204 govern the agreement). Record the facts; counsel draws conclusions.
3. **Bank-side compromise?** Confirm that no bank mailbox, admin console account, payments hub account, or core account was used. Check identity provider sign-in logs and mailbox rules for the staff involved. If any bank system is involved, raise to severity 1.
4. **Customer information accessed.** List what the attacker saw or changed (balances, account numbers, statements, wire history, contact data). A user name and password that permit access to an account are **sensitive customer information** under Supplement A, and a user name or email with a password is personal information under Fla. Stat. 501.171.
5. **Scale.** One customer or many? The same attacker infrastructure across customers, or a pattern of contact changes, changes the notification incident decision and may require notices in more than one state.
6. **Preserve evidence.** Keep emails, call recordings, audit exports, and recall correspondence with a chain-of-custody log. Evidence also supports the SAR (supporting documents kept 5 years, 12 CFR 21.11(g)).

## 5. Containment and eradication (RS.MI)
1. Keep the customer's online banking users suspended until the customer confirms its email is clean and new credentials are issued in branch or by a verified out-of-band call. Enroll app-based push or a passkey before re-enabling (POL-02 4.5), even before the bank-wide deadline.
2. Delete fraudulent beneficiary templates and reset limits to the agreed levels.
3. Keep the maintenance flag: contact changes only in branch with identification for 90 days.
4. If a bank mailbox or account was involved: reset credentials, revoke sessions and tokens in the identity provider, remove forwarding rules, and have the MSSP hunt for persistence.
5. Block the attacker's email domains, caller numbers where possible, and IP addresses; give the IP addresses to the digital banking provider.
6. Send a same-day alert to branch, contact center, relationship manager, and wire room staff: the red flags seen, and a reminder that contact changes and payment requests must be verified through contact details already on file.

## 6. Reporting, legal, and communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel confirms each notice before it goes out.

**Notification incident determination (12 CFR 53.2(b)(7)).** The CEO, the ISO, and General Counsel answer the questions below, and record the answers, the decision, the date and time, and the reasons:
- Has the incident materially disrupted or degraded, or is it reasonably likely to, the bank's ability to deliver banking products and services to a material portion of its customers? (For example: the payments hub, online banking, or the core is unavailable or untrustworthy for many customers.)
- Has it affected a business line whose failure would cause material loss of revenue, profit, or franchise value? (For example: wires, treasury management, or correspondent services must be suspended.)
- Is a bank-side system (bank mailboxes, admin console, payments hub, core security module) compromised in a way that could lead to either of the above?

A fraud against one customer through the customer's own email is usually **not** a notification incident. A pattern across many customers, or a bank-side compromise, may be. Re-run the determination whenever the scope changes. If the answer is yes, the OCC must receive notice within 36 hours of the determination, and the Federal Reserve must receive the holding company's notice within the same period (12 CFR 225.302). The two companies share one determination record, but each notice is sent.

| When | Action | Owner |
|---|---|---|
| Hour 0 | Recall request; IC3 report; bond carrier notified | Fraud lead; BSA/AML Officer; CFO |
| Hour 0 to 4 | Notification incident determination recorded (and again at each scope change) | CEO, ISO, General Counsel |
| Immediately, if the fraud is ongoing | Telephone notice to law enforcement and the OCC (12 CFR 21.11(d)) | BSA/AML Officer |
| As soon as possible | OCC notice of unauthorized access to sensitive customer information (Supplement A II.A.1.b) | General Counsel for the CEO |
| Within 36 hours of a "yes" determination | OCC notice (12 CFR 53.3); Federal Reserve notice for the holding company (12 CFR 225.302) | President and CEO |
| As soon as possible after misuse is confirmed | Written customer notice with the Supplement A III.B content, to the business customer and to any individual whose credentials were used | Chief Compliance Officer |
| Per each state's law | State notices for affected individuals (Florida: no later than 30 days after determination; a notice under the primary federal regulator's rules is deemed compliant if a copy goes to the Department of Legal Affairs on time) | Chief Compliance Officer and General Counsel |
| Within 30 calendar days of initial detection | SAR filed (up to 60 days only if no suspect is identified) | BSA/AML Officer |
| Promptly after filing | Board Risk Committee told of the SAR (12 CFR 21.11(h)) | BSA/AML Officer |

**Plan to the shortest clock.** The 36-hour clock, when it applies, runs from the determination, so make the determination early and write it down. The SAR clock runs from initial detection, not from the end of the investigation.

**Customer relief and liability.** General Counsel decides whether the payment order was effective as the customer's order under the funds transfer agreement and UCC Article 4A. If the bank did not follow the agreed security procedure (for example, the callback went to a number changed without verification), a refund with interest may be owed (Fla. Stat. 670.204). The CMT approves any refund or goodwill payment.

**Staff and customer communications.** Staff never mention a SAR (12 CFR 21.11(k)). Customer-facing statements come from the CEO or the Director of Marketing and Communications, reviewed by General Counsel. If more than one customer is affected, prepare a holding statement for relationship managers.

## 7. Recovery (RC.RP, RC.CO)
A BEC incident rarely takes systems down. Recovery means restoring safe service to the affected customer and confirming that payment services are trustworthy. If a bank system was compromised, restore in BIA priority order (P05):
1. Identity provider and administrator access (break-glass accounts if needed)
2. Operations networks and circuits to the core processor
3. Payments hub and correspondent portal (secondary wire room if needed)
4. Core banking access for branches
5. Phones and the contact center (callbacks depend on phones)
6. Online and mobile banking
7. Item processing, cards, lending, and reporting systems

**For the affected customer:** new credentials issued out of band, phishing-resistant MFA enrolled, beneficiaries and limits reviewed with the customer, contact data re-verified, and a written note of the agreed security procedure. Record the amount recovered through the recall and any refund decision.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing the case (POL-03 4.14 requires documentation within 30 days).
- Update the risk register (P01 R-001, R-002, R-013, R-028, R-041), the POA&M (P07), the Red Flags program (POAM-018), and this runbook.
- Add the case, with names removed, to the next role-based fraud training (POL-05 4.4).
- Report the incident and management's response in the annual board report (12 CFR 30 App. B III.F).
- Retain incident records for at least five years (POL-01 4.14).

## 9. Worked example (tabletop script)
| Time | Event | Clock or decision |
|---|---|---|
| Day -9, 14:10 | An email "from" a construction company's controller asks relationship manager staff to update the company's phone number "after a carrier change". A branch processes it without verification (gap 2) | Red flag missed; no customer alert sent |
| Day 0, 10:05 | Email from the controller's real (compromised) address asks for a $486,000 wire to a new beneficiary for "steel delivery", marked urgent | Red flags: new beneficiary, urgency |
| Day 0, 10:40 | Wire room calls back the number on file, which is now the attacker's; the "controller" confirms. Wire keyed and approved (maker-checker) and sent at 11:15 | Security procedure followed on its face, defeated upstream |
| Day 1, 09:20 | The real controller calls about an unknown wire; branch reports within 15 minutes | **Initial detection: SAR clock starts** |
| Day 1, 09:35 | Recall request; IC3 report; online banking suspended; phone number restored from the core audit history; bond carrier notified | Severity 2 |
| Day 1, 11:30 | Search finds 2 other business customers whose phone numbers were changed by email in the last 30 days from the same sender domain; no wires yet | **Raised to severity 1; CMT convened at 13:00** |
| Day 1, 14:00 | CEO, ISO, and General Counsel determine: not a notification incident (3 customers of 11,500 business customers; no bank system compromised; services normal). Determination recorded with reasons | 36-hour clock does not start; re-check if more customers are found |
| Day 1, 16:00 | OCC told of unauthorized access to sensitive customer information (Supplement A) | |
| Day 2 | Beneficiary bank freezes $301,000 | Recovery partial |
| Day 3 | Customer notices sent to the 3 companies and to the controller as an individual; General Counsel reviews the refund question because the callback reached a number changed without verification | Florida 30-day clock tracked from the breach determination on Day 1 |
| By Day 31 | SAR filed; Board Risk Committee told | 12 CFR 21.11(d), (h) |

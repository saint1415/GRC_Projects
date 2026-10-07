# Incident Response Runbook: Business Email Compromise Redirecting Progress Payments

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Tier / Vertical | Small / Construction |
| Incident type | Business email compromise (BEC) that redirects progress payments |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; POL-01 4.7 payment instruction changes |
| Runbook owner | IT Manager (incident commander); CFO (payment response lead) |
| Approved | 2026-08-31 by the CFO |
| Last tested | Not yet. First tabletop due 2026-11-30 (POAM-004) |

## Scenario this runbook is built for
Three variants share one playbook. They can happen together.

| Variant | What happens | Money at risk |
|---|---|---|
| **A. Outbound: owner pays the attacker** | An adversary-in-the-middle phishing page captures a Project Manager's password and session, bypassing push MFA. The attacker reads the mailbox for weeks and adds an inbox rule that hides replies from the owner's accounts payable. Just before pay app week, the attacker sends the owner "updated remittance instructions" from the real mailbox, on forged company letterhead. It may also use a lookalike domain. | One monthly pay app, typically $300,000 to $1.2 million |
| **B. Inbound: the company pays the attacker** | A spoofed or compromised subcontractor mailbox asks accounts payable to change the subcontractor's bank account "before Friday's run". | One subcontractor payment, typically $50,000 to $400,000 |
| **C. Federal: SAM EFT change** | The attacker gets into the SAM Entity Administrator account and changes the company's EFT information, so a federal progress payment goes elsewhere. Under FAR 52.232-33(e)(2), the loss may fall on the company. | One federal progress payment |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | CFO | IT incident line (cell) |
| Payment response lead | CFO | Accounting Manager | Cell |
| Bank recall | Accounting Manager | CFO | Bank fraud desk number on the printed card (never from email) |
| Technical response | MSP on-call | Forensic firm (insurer panel) | MSP on-call line |
| Owner and subcontractor contact | Project Manager for the job (a different PM if the PM's own mailbox is compromised) | VP Operations | Phone numbers from the contract file, not from email |
| Federal contacts | Contracts Administrator | CFO | Contracting Officer numbers in the contract file |
| Legal counsel | Outside breach and government contracts counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Law enforcement | FBI IC3 (www.ic3.gov) and field office | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker is reading company email. Coordinate by phone and text on company phones. Never discuss the response in email threads the attacker may see.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at the main office: this runbook, verified phone numbers for owners' AP, bank fraud desk, and top 30 subcontractors, and the notification matrix
- [ ] Call-back rule and second approver in place for bank changes (POL-01 4.7). **Gap until POAM-007 closes**
- [ ] Dual approval for all ACH batches (POL-02 4.3). **Gap until POAM-007 closes**
- [ ] Phishing-resistant MFA for Project Managers, accounting, and executives (POL-02 4.4). **Gap until POAM-002 closes**
- [ ] Mailbox auditing and alerts on new forwarding and inbox rules (POAM-005)
- [ ] Standing letter to every owner: "We will never change our bank details by email. Call us at the number in your contract before paying to any new account." Also printed on every pay app cover sheet
- [ ] Lookalike domains registered and monitored (P01 R-004)
- [ ] Insurer social engineering claim requirements known (proof of call-back is often required)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Owner or subcontractor asks about a bank change the company did not make | Phone call, owner AP | Declare immediately. Ask the caller not to pay any new account |
| Expected owner payment not received within 2 business days of its due date | Accounting Manager cash report | Call the owner's AP at the number on file and confirm where they sent it |
| Subcontractor says "we never received payment" | Subcontractor call | Check the vendor master change log; declare if bank details changed recently |
| Alert: new inbox rule, external forwarding, or risky sign-in | Identity provider and mailbox alerts (once POAM-005 closes) | IT Manager reviews within 1 hour; declare if unexplained |
| Staff report an unexpected MFA prompt or a login page after clicking a link | Staff report (POL-03 4.2) | Revoke sessions and reset the password now; review the mailbox for rules |
| SAM notice of a registration change the company did not make | SAM email to the Entity Administrator | Declare (variant C) |

**Declare a BEC incident when** a payment instruction is shown to be false, a mailbox shows unexplained rules or sign-ins, or money is missing.
**Record two times:**
- the time the incident was first known to any employee;
- later, the time the company determines, or has reason to believe, that personal information was accessed. Florida's 30-day clock runs from that determination (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Call the bank to request a recall** of any payment that may have been diverted (IC3: "time is of the essence"). For variant A, ask the owner to call *its* bank at once | Accounting Manager (variant B); Project Manager and CFO with the owner (variant A) | Recall request reference number recorded |
| 2. Freeze all bank-detail changes in the ERP vendor master and hold unreleased ACH batches | Accounting Manager | Freeze confirmed |
| 3. Revoke all sessions for the affected account; reset the password; remove attacker MFA methods; disable the account if still in doubt | IT Manager | Sign-in log shows no new sessions |
| 4. Export evidence before it rolls off: identity provider sign-ins, mailbox audit log, inbox rules, sent items, ERP vendor-master change log (POL-03 4.8) | IT Manager with the MSP | Exports saved to the incident folder with hashes |
| 5. Call the cyber insurer's breach hotline; engage panel counsel | CFO | Claim number issued |
| 6. Phone every owner with a pay app in the last 60 days and every subcontractor paid in the last 30 days. Use numbers on file. Tell them to pay nothing to new details | Project Managers (VP Operations assigns) | Call log complete |
| 7. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Initial access.** Find the phishing message or credential source. Check for an adversary-in-the-middle sign-in: a new session from an unfamiliar location shortly after a successful MFA approval.
2. **Persistence.** Look for:
   - inbox and forwarding rules
   - OAuth app consents
   - new MFA methods
   - mailbox delegates
   - the same actor's sign-ins to other accounts (SYS-01, SYS-02, SAM)
3. **Scope of the mailbox.** List what the attacker could read. **This drives the notification decisions:**
   - certified payroll files or HR documents with Social Security numbers (Florida personal information);
   - the account holder's own email address and password (also Florida personal information, 501.171(1)(g)1.b.);
   - federal drawings and pay apps (FCI; no notice duty under FAR 52.204-21, but record it for the CMMC scope);
   - anything marked CUI or covered defense information (would trigger DFARS 252.204-7012(c) 72-hour reporting; none expected, P03 G-033);
   - client facility security details (contractual notice to the client).
4. **Money trail.** For each payment: amount, date, receiving bank and account, recall status, and IC3 complaint number.
5. **Other victims.** Did the attacker email other owners or subcontractors from the mailbox? Use sent items and message trace.

## 5. Containment and eradication (RS.MI)
1. Remove malicious rules, forwarding, OAuth grants, and delegates. Re-register MFA with a security key.
2. Block the attacker's sign-in sources and the lookalike domains at the mail gateway.
3. Reset credentials for any system the user reached with single sign-on. If variant C is suspected, also reset the SAM Entity Administrator account and review SAM EFT data against the bank.
4. Check the other payment-role mailboxes (Project Managers, accounting, executives) for the same rules or sign-in patterns.
5. Keep the vendor-master freeze until every bank change from the last 90 days is re-verified by call-back.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Bank recall request; owner told to call its bank (variant A) | Accounting Manager; CFO |
| Day 0 | Insurer notified; counsel engaged | CFO |
| Day 0-1 | IC3 complaint filed "as soon as possible, regardless of the amount" (IC3 PSA I-091124-PSA) | IT Manager |
| Day 0-1 | Variant C: correct SAM; tell the Contracting Officer and paying office (FAR 52.232-33) | Contracts Administrator |
| Day 0-2 | Written notice to affected owners and subcontractors confirming the real bank details and the call-back rule | CFO |
| Within 72 hours of discovery | Only if covered defense information was affected: DoD report at dibnet.dod.mil (DFARS 252.204-7012(c)). Not expected today | Contracts Administrator |
| Within 7 days of receiving the Government's payment | Variant B on a federal job: pay the real subcontractor even though the first payment was diverted (FAR 52.232-27(c)) | CFO |
| As soon as known | Written personal information determination (POL-03 4.5) | CFO with counsel |
| Within 30 days of that determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 (Fla. Stat. 501.171(3)-(5)). Other states per their laws | CFO and counsel |

**Plan to the shorter clock.** If certified payroll files were in the mailbox, a 30-day Florida clock starts at determination. Do not wait for the funds recovery to finish before making the personal information determination.

**Paying twice.** In variant A, the owner may still owe the company. In variant B, the subcontractor must still be paid. Counsel decides who bears the loss. The company does not stop paying real subcontractors while that is argued, because that invites liens and, on federal jobs, interest penalties.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). For BEC, "restored" means "verified":
1. Identity provider: the affected account is re-secured with phishing-resistant MFA; break-glass accounts confirmed
2. Out-of-band contact list re-verified
3. Email: mailbox cleaned; alerts in place
4. ERP vendor master: every bank change in the last 90 days re-verified by call-back and second approval before the freeze is lifted
5. Bank portal: dual approval confirmed on ACH and wires
6. SAM: EFT information matches the bank; Entity Administrator on a security key
7. Pay app cycle resumes with a remittance confirmation call to each owner for the next two cycles

**Tell people when it is safe (RC.CO):** send a confirmation to owners and subcontractors, and brief staff on what to watch for.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-003, R-004), the POA&M (P07), training content (POAM-003), and this runbook.
- If the company holds a CMMC status by then, confirm that every Level 1 requirement is still met before the next award or affirmation (notification matrix, "CMMC status currency").
- Retain all incident documentation for 6 years (POL-01 4.12). Keep a written Florida no-harm determination for at least 5 years if one is made (501.171(4)(c)).

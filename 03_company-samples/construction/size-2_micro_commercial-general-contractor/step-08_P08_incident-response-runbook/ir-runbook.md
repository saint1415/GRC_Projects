# Incident Response Runbook: Business Email Compromise Redirecting Progress Payments

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Tier / Vertical | Micro / Construction |
| Incident type | Business email compromise (BEC) that redirects progress payments |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; POL-02 A.6 payment instruction changes |
| Runbook owner | Office Manager (incident lead); Owner and President (decision maker) |
| Approved | 2026-08-31 by the Owner and President |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (P02 CP-4) |

## Scenario this runbook is built for
Three variants share one playbook. They can happen together.

| Variant | What happens | Money at risk |
|---|---|---|
| **A. Outbound: an owner pays the attacker** | A phishing email sends the Project Manager to a fake sign-in page that relays the push MFA approval and steals the session. The attacker reads the mailbox for weeks and adds an inbox rule that hides replies from the medical office owner's accounts payable. Just before pay app week, the attacker emails the owner "updated remittance instructions" from the real mailbox, with a forged letter on company letterhead. | One pay app, up to $78,000 |
| **B. Inbound: the company pays the attacker** | A spoofed or compromised supplier mailbox asks the Office Manager to change the supplier's bank account "before Friday's run". This is how the May 2026 near miss began. | One supplier or subcontractor payment, typically $5,000 to $25,000 |
| **C. Federal: SAM EFT change** | The attacker gets into the Owner's government sign-in and changes the company's EFT information in SAM, so the FC-1 progress payment goes elsewhere. Under FAR 52.232-33(e)(2), the loss may fall on the company. | One FC-1 progress payment, up to about $40,000 |

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics. The Office Manager runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Owner and President | Company cell (printed contact card) |
| Decision maker (money, notices, outside firms) | Owner and President | Office Manager | Company cell |
| Bank recall | Office Manager | Owner | Bank fraud desk number on the printed card (never from email) |
| Technical response | MSP after-hours emergency line (billed hourly) | MSP lead technician's cell | Phone only |
| Owner and subcontractor calls | Project Manager and Estimator (the Owner if the Project Manager's mailbox is the compromised one) | Owner | Numbers from the contract file, not from email |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel counsel; forensic firm engaged by counsel | n/a | Assigned on the first hotline call |
| Federal contacts | Owner (FC-1 Contracting Officer and paying office) | Office Manager | Numbers in the FC-1 contract file |
| Law enforcement | FBI IC3 (www.ic3.gov) and the FBI field office | n/a | Numbers in the binder |

**Notification chain in the first hour:** staff member → Office Manager → bank fraud desk and the Owner (at the same time) → MSP emergency line → insurer breach hotline (Owner) → breach counsel and forensics (through the insurer) → affected owner or supplier by phone (Project Manager or Owner).

**Out-of-band first.** Assume the attacker is reading company email. Coordinate by phone and text on company phones. Never discuss the response in email threads the attacker may see.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the office and in the Owner's truck: this runbook, the contact card with verified numbers (owners' accounts payable, bank fraud desk, MSP, insurer, top 10 subcontractors and suppliers), and the notification matrix
- [ ] Call-back, Owner approval, log, and 5-day hold for bank changes (POL-02 A.6). **Gap until POAM-002 closes**
- [ ] Security keys for the Owner, Office Manager, and Project Manager; MFA on the bids mailbox and SYS-01 (POL-02 B.3). **Gap until POAM-007 closes**
- [ ] Alerts on new forwarding and inbox rules and risky sign-ins (POAM-005)
- [ ] DMARC at reject and two look-alike domains registered (POAM-016)
- [ ] Standing letter to every owner: "We will never change our bank details by email. Call us at the number in your contract before paying to any new account." Also printed on every pay app, which no longer shows bank details on the cover page
- [ ] The insurer's social engineering condition is understood: coverage needs a recorded call-back to a known number (P01 R-016)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| An owner or subcontractor asks about a bank change the company did not make | Phone call | Declare at once. Ask the caller not to pay any new account |
| An expected owner payment is not received within 2 business days of its due date | Office Manager's cash check | Call the owner's accounts payable at the number on file and confirm where they sent it |
| A supplier says "we never received payment" | Supplier call | Check the call-back log and SYS-02 change log; declare if bank details changed recently |
| Alert: new inbox rule, external forwarding, or risky sign-in | Suite alert to the Office Manager and MSP (once POAM-005 closes) | MSP reviews within 1 business hour; declare if unexplained |
| A staff member reports an unexpected MFA prompt or a sign-in page after clicking a link | Staff report (POL-03 4.2) | MSP revokes sessions and resets the password now; check the mailbox for rules |
| SAM notice of a registration change the company did not make | SAM email to the Owner | Declare (variant C) |

**Declare a BEC incident when** a payment instruction is shown to be false, a mailbox shows unexplained rules or sign-ins, or money is missing.

**Record two times:**
- the time the incident was first known to any employee;
- later, the time the company determines, or has reason to believe, that personal information was accessed. Florida's 30-day clock for individual notice runs from that determination (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Call the bank fraud desk to request a recall** of any payment that may have been diverted (IC3: "time is of the essence"). For variant A, ask the owner to call *its* bank at once | Office Manager (variant B); Owner with the owner's accounts payable (variant A) | Recall reference number recorded |
| 2. Freeze all bank-detail changes in SYS-02 and hold any unreleased ACH batch | Office Manager; Owner (does not release) | Freeze confirmed |
| 3. Revoke all sessions for the affected account, reset the password, remove attacker MFA methods; disable the account if in doubt | MSP | Sign-in log shows no new sessions |
| 4. Export evidence before it rolls off: suite sign-ins, mailbox audit log, inbox rules, sent items, SYS-01 activity, SYS-02 vendor-change log (POL-03 4.8) | MSP with the Office Manager | Exports saved to the incident folder |
| 5. Call the cyber insurer's breach hotline; engage panel counsel; keep the call-back log for the claim | Owner | Claim number issued |
| 6. Phone every owner with a pay app in the last 60 days and every subcontractor and supplier paid in the last 30 days, using numbers on file. Tell them to pay nothing to new details | Project Manager (or Owner) | Call log complete |
| 7. Start the incident log: timeline, actions, who, and when | Office Manager | Log open |

## 4. Analysis (RS.AN)
1. **Initial access.** The MSP finds the phishing message or credential source and checks for a relayed sign-in: a new session from an unfamiliar location right after a successful MFA approval.
2. **Persistence.** Look for inbox and forwarding rules, app consents, new MFA methods, mailbox delegates, and the same actor's sign-ins to SYS-01, SYS-02, the bids mailbox, and SAM.
3. **What the attacker could read.** List it. **This drives the notification decisions:**
   - certified payrolls and HR documents with Social Security numbers (Florida personal information). Subcontractors email full payrolls to the Office Manager (P01 R-017), so a compromised Office Manager mailbox likely holds about 40 workers' records;
   - the account holder's own email address and password (also Florida personal information, 501.171(1)(g)1.b.);
   - FC-1 drawings and pay apps (FCI; FAR 52.204-21 has no incident notice duty, but record it for the CMMC scope and tell counsel);
   - anything marked CUI or covered defense information (would trigger DFARS 252.204-7012(c) 72-hour reporting; none expected, P03 G-033);
   - owners' security system drawings (contractual notice to that owner).
4. **Money trail.** For each payment: amount, date, receiving bank and account, recall status, and IC3 complaint number.
5. **Other victims.** Did the attacker email other owners, subcontractors, or the FC-1 Contracting Officer from the mailbox? Use sent items and message trace.

## 5. Containment and eradication (RS.MI)
1. Remove malicious rules, forwarding, app consents, and delegates. Re-register MFA with a security key.
2. Block the attacker's sign-in sources and any look-alike domains at the mail filter.
3. Reset credentials for every system the user reached. If variant C is suspected, reset the Owner's government sign-in and compare SAM EFT data with the bank.
4. Check the other mailboxes (Owner, Office Manager, Project Manager, bids mailbox) for the same rules or sign-in patterns.
5. Keep the SYS-02 freeze until every bank change from the last 90 days is re-verified by call-back and approved by the Owner.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Bank recall request; owner told to call its bank (variant A) | Office Manager; Owner |
| Day 0 | Insurer notified; counsel engaged; MSP engaged | Owner |
| Day 0-1 | IC3 complaint filed "as soon as possible, regardless of the amount" (IC3 PSA I-091124-PSA) | Office Manager |
| Day 0-1 | Variant C: correct SAM; tell the FC-1 Contracting Officer and paying office (FAR 52.232-33) | Owner |
| Day 0-2 | Written notice to affected owners and subcontractors confirming the real bank details and the call-back rule | Owner |
| Within 7 days of receiving the Government's payment | Variant B on FC-1: pay the real subcontractor even though the first payment was diverted (FAR 52.232-27(c)(1)) | Office Manager; Owner releases |
| Within 72 hours of discovery | Only if covered defense information were affected: DoD report at dibnet.dod.mil (DFARS 252.204-7012(c)). Not expected | Owner |
| As soon as known | Written personal information determination with its date (POL-03 4.5) | Office Manager with counsel |
| Within 30 days of that determination | Florida individual notices (501.171(4)); Department of Legal Affairs only if 500 or more Floridians (501.171(3)); consumer reporting agencies only if more than 1,000 (501.171(5)). Workers who live in other states: each state's law | Owner and counsel |

**Plan to the shorter clock.** If certified payrolls were in the mailbox, Florida's 30-day clock starts at determination. Do not wait for the funds recovery to finish before making the personal information determination. At about 40 affected workers, the Department and consumer reporting agency thresholds are not reached, but individual notices are still due.

**Paying twice.** In variant A, the owner may still owe the company. In variant B, the supplier or subcontractor must still be paid. Counsel decides who bears the loss. The company does not stop paying real subcontractors while that is argued, because that invites liens and, on FC-1, interest penalties. The Owner tells the surety if the loss affects the ability to pay subcontractors.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). For BEC, "restored" means "verified":
1. Company phones and the printed contact card: numbers re-verified
2. Email: the affected account re-secured with a security key; mailbox cleaned; alerts in place
3. SYS-01: sessions revoked; pay app packages checked for altered remittance pages
4. SYS-02: every bank change in the last 90 days re-verified by call-back and Owner approval before the freeze is lifted
5. Bank portal: Owner release confirmed; no pending batches with unverified accounts
6. SAM: EFT information matches the bank; the Owner's government sign-in on a security key
7. Pay app cycle resumes with a remittance confirmation call to each owner for the next two cycles

**Tell people when it is safe (RC.CO):** send a confirmation to owners and subcontractors, and brief all 7 employees, including the Carpenters, on what to watch for.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 4.10 requires the write-up within 30 days), with the MSP and the insurer's notes.
- Update the risk register (P01, especially R-001, R-002, R-003, R-016), the POA&M (P07), the training content (POAM-006), and this runbook.
- If the company holds a CMMC status by then, confirm that every Level 1 requirement is still met before the next award or annual affirmation (notification matrix, "CMMC status currency").
- Keep all incident records for 6 years (POL-04 4.9). Keep a written Florida no-harm determination for at least 5 years if one is made (501.171(4)(c)).

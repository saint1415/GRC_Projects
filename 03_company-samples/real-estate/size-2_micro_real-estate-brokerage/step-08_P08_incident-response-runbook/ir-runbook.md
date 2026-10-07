# Incident Response Runbook: Business Email Compromise Targeting Closing Funds

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management) |
| Tier / Vertical | Micro / Real Estate and Rental and Leasing |
| Incident type | Business email compromise (BEC) targeting closing funds. **Variant A:** a contractor agent's mailbox is taken over and a buyer is sent altered closing wire instructions that appear to come from the title company. **Variant B:** a spoofed owner email changes a property owner's payout bank account and diverts a monthly distribution from the property management escrow account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy. Also the brokerage's voluntary version of the benchmark incident response plan element (16 CFR 314.4(h)) |
| Goals | Stop and recover the money first; secure the mailbox or channel; keep closings moving on a verified channel; meet every notice deadline; fix the weakness that allowed it |
| Runbook owner | Office Manager (security and compliance lead) |
| Approved | 2026-09-14 by the Broker-owner |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (P01 R-015) |

## 0. Roles and notification chain (Govern)
The brokerage has 7 employees and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics. The Office Manager runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Broker-owner | Cell phone (numbers on the printed contact card) |
| Decision maker (money, insurer, Commission notice, outside statements) | Broker-owner | Office Manager | Cell phone |
| Escrow bank fraud desk and relationship manager | Called by the Broker-owner or Office Manager | Branch in person | Numbers on the contact card (recorded 2026-08) |
| Client contact (variant A) | Transaction Coordinator on the file | Senior Transaction Coordinator | Phone only, to numbers from the contract file |
| Owner contact (variant B) | Property Manager | Office Manager | Phone only, to the number in the owner file |
| Title company on the file | Transaction Coordinator | Broker-owner | Phone number from the contract or the title company's published website |
| Technical response | MSP 24x7 emergency line | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Policy card in the binder |
| Breach counsel and forensics | Insurer panel firms | n/a | Assigned on the first hotline call |
| Law enforcement | FBI IC3 (www.ic3.gov); FBI field office | Local police (for the report some banks ask for) | Numbers in the binder |

**Notification chain in the first hour:** whoever learns of it → Office Manager (phone) → at the same time, the bank (if money moved), the MSP emergency line, and the Broker-owner → insurer hotline (Broker-owner) → counsel and forensics (through the insurer). The title company is called at once in variant A.

**Out-of-band first.** Assume the affected mailbox, and maybe others, is being read by the attacker. Do not discuss the incident by email. Use phones and the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the office and at the Office Manager's and Broker-owner's homes: this runbook, the contact card (bank fraud desk, insurer hotline, MSP, title companies used most often), the notification matrix, and the incident log template (section 8)
- [ ] MFA on every mailbox, including all 22 agents, and legacy protocols blocked. **Gap until POAM-003 closes (2026-10-31)**
- [ ] Named administrator accounts with MFA; shared administrator disabled. **Gap until POAM-002 closes (2026-09-30)**
- [ ] Alerts on new forwarding rules and risky sign-ins; external forwarding blocked. **Gap until POAM-004 closes**
- [ ] Payment instruction verification rule in use (POL-03 4.9); callback record in every file
- [ ] Buyers told in the contract packet and again a week before closing: the brokerage never sends wire instructions by email; call the title company at the number in your contract before sending money
- [ ] Owners told that payout bank changes are accepted only through the owner portal or on a signed form, followed by a call

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A buyer asks about "new" or "updated" wire instructions | Client call or email | Tell them **not to send money**. Give them the title company's number from the contract. Call the Office Manager |
| A buyer says funds were sent but the title company has not received them | Title company or buyer | **Declare at once (variant A).** Go to section 3 |
| An owner says a distribution did not arrive, or a payout change request arrives by email | Owner or Property Manager | Declare if money went out (variant B); otherwise hold the change and verify by phone |
| Unexpected inbox rules, forwarding, or sent messages the agent did not write | Agent, MSP alert | Declare; start mailbox containment (section 5) |
| An agent or employee typed a password into a suspicious page or approved an unexpected MFA prompt | Self-report | MSP resets the password and signs out all sessions; check sign-ins and rules; declare if anything unusual |
| A deposit verification request comes back with "no deposit received" | Transaction Coordinator (r. 61J2-14.008(2)(b)) | Treat as a possible diverted deposit; call the buyer and title company |
| Email from a look-alike of the brokerage's or a title company's domain | Staff or client | Declare if anyone acted on it; otherwise log it and block the domain |

**Declare a BEC incident when** a payment instruction may have been altered, any money may have gone to the wrong account, or a brokerage mailbox shows signs of takeover.

**Write down two dates.** The time the first person learned of it, and later the date the brokerage determines a breach occurred or has reason to believe one did. Florida's 30-day clocks run from that determination (Fla. Stat. 501.171(3)(a), (4)(a)). The FTC 30-day rule for financial institutions (16 CFR 314.4(j)) does **not** apply to this brokerage (P03 1.1).

## 3. First hour: stop the money (RS.MI)
Once the receiving bank accepts a payment order, it can be cancelled only if that bank agrees (Fla. Stat. 670.211(3)), and fraudsters often move funds within hours.

**Variant A: buyer wired closing funds on altered instructions**
| Step | Who | Done when |
|---|---|---|
| 1. Call the buyer (number from the contract file). Tell them to call **their own bank's** fraud or wire department now, ask for a recall of the wire, and get a reference number. Call back within 15 minutes | Transaction Coordinator on the file | Buyer gives the bank reference number |
| 2. Call the title company at its known number: report the fraud, give the fraudulent account details, and ask it to hold the closing and alert its bank | Transaction Coordinator | Title company contact name logged |
| 3. Ask the buyer to file an IC3 complaint the same day with full banking details; file the brokerage's own complaint too | Office Manager | IC3 complaint IDs logged |
| 4. Freeze the agent's files: no instruction changes on any of that agent's open transactions; call every buyer and seller on them, using contract-file numbers, to warn them | Broker-owner with the Transaction Coordinators | All parties reached |
| 5. Contain the mailbox (section 5, steps 1-3) | MSP with the Office Manager | Sessions revoked; rules removed |
| 6. Call the insurer hotline | Broker-owner | Claim number logged |

**Variant B: owner distribution diverted from the property management escrow account**
| Step | Who | Done when |
|---|---|---|
| 1. Call the escrow bank's fraud desk: request a recall of the ACH entry and ask the bank to contact the receiving bank | Broker-owner or Office Manager | Bank reference number logged |
| 2. Hold every pending payout change and the next distribution batch until each owner's bank details are confirmed by phone | Property Manager; Bookkeeper | Hold recorded in SYS-05 |
| 3. Call the owner at the number in the owner file; restore the correct bank details only after the call | Property Manager | Owner confirmation logged |
| 4. File an IC3 complaint; call the insurer hotline | Office Manager; Broker-owner | IC3 ID and claim number logged |
| 5. Record the escrow impact for the monthly reconciliation (r. 61J2-14.012(3)). Other owners' funds must not cover the shortfall; the Broker-owner decides how the brokerage pays the owner | Bookkeeper; Broker-owner | Decision recorded |

In both variants, start the incident log (section 8) in the first hour.

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Channel.** Was a brokerage mailbox taken over, or was the email spoofed from a look-alike domain? Check message headers, the sender domain's registration date, and the mailbox's sign-in log.
2. **Mailbox activity** (if taken over): sign-ins by location and app, inbox and forwarding rules, messages sent, deleted, or read, and app consents. **Export the logs today**; the default retention is shorter than one year (POAM-005).
3. **Other targets.** Search all 29 mailboxes for the same sender, domain, subject lines, and account numbers. The same agent's other files and the same title company's other closings are the next targets.
4. **Data exposed.** List the people whose information was in the mailbox or its forwarded copies, which data elements (driver license or passport images, bank statements, the agent's own password), and each person's state of residence. This list drives section 6.
5. **Preserve evidence.** Keep the fraudulent emails with full headers, the wire or ACH records, and the log exports, with a chain-of-custody record for forensics and law enforcement.

## 5. Containment and eradication (RS.MI)
1. Reset the affected account's password, sign out all sessions and tokens, and require MFA before it is used again.
2. Remove every inbox and forwarding rule the user did not create; remove unknown app consents and mobile device partnerships.
3. Block legacy sign-in for the account (for every account once POAM-003 closes).
4. Block the fraudulent sender addresses and look-alike domains; report look-alike domains to the registrar.
5. Check the other mailboxes that received the same phishing message; reset any that show the same signs.
6. If the shared administrator or an MSP login may have been used, change it at once and have forensics review administrator activity (P01 R-006, R-013).
7. Confirm with the MSP or forensics that no persistence remains before closing containment.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel confirms every notice before it goes out.

**Notice determination** (Office Manager with counsel, recorded in the log):
1. Was personal information of Florida residents accessed (Fla. Stat. 501.171(1)(g))? Driver license images and passport copies in an agent's mailbox usually make the answer yes. If yes, notify within 30 days of the determination, or document a no-harm determination after consulting law enforcement (501.171(4)(c)) and send it to the Department within 30 days.
2. How many Floridians? 500 or more: notice to the Department of Legal Affairs within 30 days. More than 1,000: also the consumer reporting agencies.
3. Where do the others live? About 25% of buyers live outside Florida; counsel applies each state's law.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Bank recall requests; title company or owner called; MSP engaged | Transaction Coordinator or Property Manager; Office Manager |
| Day 0 | IC3 complaints; insurer hotline; counsel and forensics assigned; E&O carrier told if a client may claim | Office Manager; Broker-owner |
| Day 0-1 | Call every party on the affected agent's open files: no wire instructions will ever come by email; call the title company before sending money | Transaction Coordinators |
| Day 0-2 | Briefing for employees and agents by phone or at the office: what happened, what to watch for, do not discuss outside the brokerage | Broker-owner |
| Within 15 business days | If a missing deposit leads to conflicting demands or good-faith doubt about escrowed funds: written notice to the Florida Real Estate Commission; settlement procedure within 30 business days (r. 61J2-10.032(1)) | Broker-owner |
| Within 30 days of determination | Florida individual notices; Department notice if 500 or more Floridians; or the no-harm determination to the Department | Office Manager and counsel |
| Per each state's law | Other states' notices | Counsel |

**Inbound notices.** If the breach happened at a vendor (for example the property management platform), the vendor must tell the brokerage within 10 days of its determination (501.171(6)(a)); the brokerage still sends the notices to individuals and the Department.

## 7. Recovery (RC.RP, RC.CO)
1. Resume closings only on the verified channel: documents and instructions through the transaction platform's client document sharing, confirmed by a call the buyer makes to the title company's number in the contract.
2. Re-verify by phone every pending payment instruction on the affected agent's files and every owner payout change in the last 30 days.
3. If a closing cannot fund on time, tell the title company and lender at once so they can reschedule (P05 BP-01, MTD 24 h).
4. Restore any mail the attacker deleted from the vendor's retention or, for employees, from SYS-09. Agent mailboxes have no independent backup until POAM-006 closes.
5. Tell affected clients, owners, and agents when the channel is safe again (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days, with the MSP and counsel; written summary within 30 days (POL-03 4.11).
- Update the risk register (P01, especially R-001, R-002, R-003, R-025), the POA&M (P07), training, and this runbook.
- Record the funds outcome: amount recalled, amount lost, insurance recovery under the social engineering endorsement.
- Keep all incident records at least 5 years (a Florida no-harm determination must be kept at least 5 years, 501.171(4)(c)).
- **First log entry:** the May 2026 near miss (a look-alike title company email that the buyer questioned) was recorded on 2026-09-14 as the first lessons-learned record.

**Incident log template**
| Field | Entry |
|---|---|
| Incident ID and variant | |
| Date and time first known, and by whom | |
| Florida determination date | |
| Transactions, clients, owners, and amounts involved | |
| Bank recall and IC3 reference numbers | |
| Accounts and mailboxes affected; containment time | |
| Data exposed; Florida and other-state counts | |
| Notice decisions, dates, and counsel sign-off | |
| Commission notice (if an escrow dispute) | |
| Funds outcome and insurance claim | |
| Lessons learned and POA&M items opened | |

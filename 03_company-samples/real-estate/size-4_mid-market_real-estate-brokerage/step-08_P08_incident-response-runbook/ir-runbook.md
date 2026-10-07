# Incident Response Runbook: Business Email Compromise Targeting Closing Funds

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC (PE-backed residential real estate brokerage with property management and title and closing services) |
| Tier / Vertical | Mid-Market / Real Estate and Rental and Leasing |
| Incident type | Business email compromise (BEC) that diverts, or tries to divert, client money: buyer cash-to-close and earnest money wires, title trust disbursements and payoffs, sales escrow refunds, owner distributions, and agent commission payouts |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy (4.1 to 4.12); POL-04 4.3 to 4.5 (payment instructions and payee changes); STD-05 Payment instruction and payee verification standard |
| Companion documents | `ir-runbook-ransomware.md` (ransomware with data theft at Title and Closing); `notification-matrix.csv`; BIA (P05 BP-01, BP-02, BP-03, BP-05, BP-11, BP-12); risk register (P01 R-001 to R-003, R-019, R-021, R-022, R-052) |
| Written incident response plan | This runbook and the ransomware runbook together are the written plan Title and Closing must keep under 16 CFR 314.4(h) (N53-R01). The goals (314.4(h)(1)) are in section 1 |
| Runbook owner | Security Manager (Qualified Individual) as incident commander; President, Title and Closing as funds response lead |
| Approved | 2026-09-29 by the Chief Operating Officer and the President of Title and Closing |
| Last tested | Not yet. Funds recovery tabletop with the banks' fraud desks, breach counsel, and the insurer scheduled 2026-11-18 (POAM-009) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so that the money, the technology, and the legal decisions each have a clear owner (314.4(h)(3)).

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, President of Title and Closing, Broker of Record, General Counsel, vCISO, Security Manager, Director of Marketing (communications), HR Director; breach counsel when engaged | Client communications, restoring escrow or trust shortages from operating funds, closing delays, statements, claims |
| **Funds response team (FRT)** | Lead: President, Title and Closing. Title Escrow Accounting Manager, Controller (sales escrow and property management escrow), CFO (bank relationships), the closer or property manager on the affected file | Bank recalls, payment holds, re-verification of every pending payment on the file, contact with the buyer's or seller's bank |
| **Incident response team (IRT)** | Incident commander: Security Manager (Qualified Individual). IT Director, security analysts, MSSP, forensic firm (engaged through counsel) | Mailbox and account containment, investigation, scope of data accessed, eradication |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager (Qualified Individual) | IT Director | Out-of-band group on personal phones; printed call tree |
| Funds response lead | President, Title and Closing | Title Escrow Accounting Manager | Out-of-band group |
| Sales escrow and property management funds | Controller | Chief Financial Officer | Out-of-band group |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Notification decisions and decision log | General Counsel | Breach counsel (insurer panel) | Out-of-band group |
| Escrow disputes and agent supervision | Broker of Record | Regional managing broker | Out-of-band group |
| Banks (2 title trust banks; 1 escrow and operating bank) | Wire room and fraud desk numbers on the laminated bank card in each closing room | Relationship managers | Verified quarterly; last verified 2026-09-15 |
| Cyber insurer | Carrier breach hotline ($10 million limit, $250,000 retention, $1 million funds transfer fraud sublimit) | Broker | Policy card in the incident binder |
| Title insurance underwriter | Agency claims contact | Underwriter agency manager | Agency agreement |
| Monitoring | MSSP 24x7 operations center (calls within 30 minutes of a high-severity alert) | n/a | MSSP hotline |
| Communications | Director of Marketing | Outside crisis PR through counsel | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner; President of Title and Closing informs its board of managers | COO | Phone |
| Law enforcement | FBI field office and IC3 (www.ic3.gov) | Local police for the victim's report | Numbers in the binder |

**Out-of-band first.** Assume the attacker can read the compromised mailbox and may read others. Responders use the pre-arranged messaging group on personal phones and the printed call tree (POL-03 4.7). Never tell a client by email that their wire instructions were changed; call them at the number in the contract file.

**Legal privilege protocol.** General Counsel engages breach counsel through the insurer, and breach counsel engages forensics. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs, bank records) separate from legal conclusions.

## 1. Goals and preparation checks (Identify / Protect)
**Goals (314.4(h)(1)):** (1) recover diverted money while recall is still possible; (2) stop every other pending payment that could follow the same path; (3) contain the compromised accounts; (4) determine whether customer or personal information was acquired and meet every notice deadline; (5) close the weakness that let it happen.

- [x] Wire instructions to buyers and sellers are delivered only through the Closing Communications Portal (since 2023)
- [x] Callback to a verified number and dual approval for every outgoing title trust wire to a new payee (40 of 40 sampled in P07)
- [x] Positive pay on all escrow and trust accounts
- [x] Phishing-resistant security keys for the 46 wire release staff and all administrators (P07 IA-2(1) fully satisfied)
- [x] Bank fraud desk and wire room numbers verified 2026-09-15 and printed on bank cards in each closing room
- [x] Alerts on new mailbox forwarding rules (since 2026-05)
- [ ] MFA for every contractor agent. **Gap until POAM-001 closes (2026-11-15)**
- [ ] Two-person rule and callback for edits to existing payees, sales escrow refunds, owner payout changes, and agent payout changes. **Gap until POAM-002 closes (2026-11-30)**
- [ ] External auto-forwarding blocked tenant-wide (2026-10-31) and SaaS payee change alerts in the SIEM (2027-01-31). **Gap until POAM-005 closes**
- [ ] Every payee change attempt logged in the incident log, not a spreadsheet (POAM-009)
- [ ] Consumer counting worksheet for the FTC 500-consumer threshold (POAM-020)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A buyer, seller, lender, or agent reports changed wire instructions, or a buyer says they already wired money that Title and Closing has not received | Phone call; closer; positive pay or incoming wire report | Funds response lead calls the client at the number in the contract file; if a wire left the buyer's bank, start section 3 at once |
| A payoff letter or payee bank change arrives by email, or differs from the lender portal or the file | Payoff processor; SYS-02 payee change | Do not use it; verify through the lender portal or the lender's published number (POL-04 4.5); report it to the incident line |
| A property owner or agent changes a payout bank account, or asks to by email | SYS-10 owner portal; SYS-13; accounting staff | Hold the next payment; callback to the number on file (STD-05); report it |
| A sales escrow refund request comes from an agent or party by email | Escrow accounting | Callback to the party at the number in the contract file before release; second approver |
| Forwarding rule, inbox rule that hides messages, or impossible-travel sign-in on any mailbox | MSSP alert; SIEM | MSSP revokes sessions and calls the incident commander within 30 minutes |
| A client receives email from a look-alike domain | Client report; email gateway | Block the domain; warn every party on affected files by phone; takedown request |
| Earnest money not confirmed by the title company or attorney within 10 business days | Transaction coordinator (r. 61J2-14.008(2)(b)) | Call the buyer and the holder; treat an unconfirmed deposit as possible diversion |

**Severity 1 (declare immediately, POL-03 4.2):** any wire sent to an account not verified for the payee, any change to a payee's bank details that cannot be verified, or any compromised mailbox that held closing documents or wire information.
**Severity 2:** a stopped attempt with no money sent and no evidence of account compromise. It is still logged as a security event (314.4(h)(6)).

**Record two dates in the incident log** (POL-03 4.3):
- **Discovery** (FTC clock): the first day the event is known to any employee, officer, or other agent of Title and Closing, other than the person committing it (16 CFR 314.4(j)(2)). A contractor agent who saw the suspicious email counts, so ask when the agent first noticed it.
- **Determination** (Florida clock): the date the company determines a breach occurred or has reason to believe it did (Fla. Stat. 501.171(4)(a)).

## 3. First hour: follow the money (RS.MA, RS.MI)
Recall is most likely to work in the first hours, before the receiving bank lets the money move on. After the receiving bank accepts the payment order, cancellation needs that bank's agreement (Fla. Stat. 670.211(3)). The FBI advises contacting the sending bank immediately to request a recall and filing an IC3 complaint as soon as possible, whatever the amount (IC3 PSA I-091124-PSA).

| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | **Variant A (buyer's own wire):** the closer calls the buyer at the contract-file number and tells them to call their bank's fraud line now and ask for a recall; the closer stays on the phone. **Variant B (title trust disbursement):** the funds response lead calls the sending bank's wire room for a recall and hold, with the wire reference. **Variant C (sales escrow refund, owner payout, agent payout):** the Controller does the same with the escrow bank | Funds response lead; Controller | Recall request made; bank reference number logged |
| 0-30 min | Hold every other pending payment on the affected file and every payment to the affected payee or account until re-verified under STD-05 (POL-03 4.4) | Title Escrow Accounting Manager; Controller | Holds placed in SYS-02, SYS-10, SYS-13, and bank platforms |
| 0-30 min | Declare Severity 1; open the out-of-band channel; start the incident log with discovery time | Incident commander | Log open |
| 0-60 min | Contain the mailbox: revoke all sessions; reset the password; enforce MFA (security key for staff); remove forwarding and inbox rules and unknown connected apps; block the sender and look-alike domains | Security analysts with the MSSP | Account secured; rules exported for evidence before deletion |
| 0-60 min | File the IC3 complaint with full bank details; in variant A help the buyer file their own | Security Manager | IC3 complaint number logged |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; the carrier assigns breach counsel | Chief Financial Officer | Claim number; counsel engaged |
| 1-2 h | Phone every party on the affected file and on any file the compromised mailbox touched in the last 90 days: "Use only the instructions in the portal; call us at the number in your contract packet before sending money" | Closers; transaction coordinators | Call log complete |
| 1-2 h | Search all mailboxes for the same sender, domain, subject lines, and rules; check SYS-02, SYS-10, and SYS-13 for payee changes in the last 30 days by the same user or to the same account | IRT with the MSSP | Hunt results recorded |
| 2-4 h | Convene the CMT if money left any account; first situation report (amount, recall status, other files at risk) | CMT chair | CMT meeting held |
| Same day | Notify the title insurance underwriter (variant B) and check closing protection letter coverage | President, Title and Closing | Underwriter notified |
| Same day | If an escrow or trust account is short, restore it from operating funds with CFO approval, so other clients' money is never used (Fla. Stat. 626.8473(4); r. 61J2-14.012(3)) | Chief Financial Officer | Account balanced; reconciliation note records the cause and the corrective action |

## 4. Analysis (RS.AN)
1. **Entry point.** Which account was compromised: an agent mailbox (most likely; about 310 agents still have no MFA), a client's own email, a staff mailbox, or none (pure spoofing from a look-alike domain)? Use identity provider sign-in logs, mailbox audit logs (180-day retention today, POAM-005), and message trace.
2. **Dwell time and reach.** When did the attacker first sign in, what rules did they create, and what messages did they read, send, or forward? List every transaction file with mail in the mailbox.
3. **Preserve evidence.** Export mailbox audit logs, sign-in logs, message headers, rules, and bank records before retention runs out, with chain of custody. Forensics holds the evidence under counsel.
4. **Data accessed (drives notices).** Build the affected-person list from the mailbox contents: name, data elements (Social Security number, driver license number, account numbers with access data, username and password), and state of residence. Separate:
   - **Title and Closing customer information** (closing packages, settlement statements, loan data): this decides whether there is an FTC notification event. Unauthorized access to unencrypted customer information is presumed to be acquisition unless reliable evidence shows otherwise (16 CFR 314.2(m)).
   - **Personal information** under Fla. Stat. 501.171(1)(g) and other states' laws, which can include brokerage clients, tenants, and agents.
5. **Funds trail.** Bank, amount, receiving bank and account, recall status, and any related accounts (often money-mule accounts used across many victims).

## 5. Containment and eradication (RS.MI)
1. Keep the compromised account locked until forensics confirms no persistence (rules, connected apps, MFA methods added by the attacker).
2. Reset credentials of any other account the attacker could reach, and of the client portal account if the phone number on it changed (callback rule, POL-02 4.14).
3. Re-verify every payee and bank account changed in the last 30 days in SYS-02, SYS-10, and SYS-13 by callback (STD-05).
4. For an agent: the Broker of Record suspends system access until the agent has MFA and completes the BEC module; repeat failures are handled under the agent agreement.
5. Report look-alike domains for takedown, and warn the other brokerages and lenders on affected files by phone.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel approves every notice and keeps the **decision log** (POL-03 4.5, 4.6).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Was Title and Closing customer information acquired without authorization, and is it unencrypted? Apply the presumption in 314.2(m) | General Counsel with breach counsel | Decision log with the evidence relied on |
| D2 | Number of consumers affected. At least 500 means FTC notice within 30 days of discovery (314.4(j)(1)) | General Counsel | Counting worksheet (POAM-020) |
| D3 | Florida: personal information of Florida residents accessed? Is a written no-harm determination supportable after consultation with law enforcement (501.171(4)(c))? 500 or more Floridians (Department notice)? More than 1,000 notices (consumer reporting agencies)? | General Counsel | Decision log; affected-person list by state |
| D4 | Residents of other states: apply the law of each state where affected individuals reside | Breach counsel | State-by-state table |
| D5 | Law enforcement delay requested in writing (314.4(j)(1)(vi); 501.171(4)(b))? | General Counsel | Copy of the request |
| D6 | Sales escrow deposit diverted with conflicting demands, or good-faith doubt about entitlement? Commission notice within 15 business days and a settlement procedure within 30 business days (r. 61J2-10.032(1)) | Broker of Record | Escrow dispute log |
| D7 | Contract notices: underwriter, insurer, lender clients, the national homebuilder | General Counsel with the President of Title and Closing | Contract register |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Bank recall; IC3 complaint; insurer hotline | Funds response lead; Security Manager; CFO |
| Same day | Underwriter notice (contract); CEO informs the audit committee chair and the PE sponsor; President of Title and Closing informs its board of managers | President, Title and Closing; CEO |
| Day 1-5 | Scope of data accessed; D1 to D3 decisions documented | General Counsel |
| Within 15 business days of the last demand or of the doubt | Florida Real Estate Commission escrow dispute notice, if D6 applies | Broker of Record |
| No later than 30 days after discovery | FTC notice through the ftc.gov form, if 500 or more consumers (D2) | General Counsel |
| No later than 30 days after determination | Florida individual notices; Department of Legal Affairs notice if 500 or more Floridians; consumer reporting agencies without unreasonable delay if more than 1,000 | General Counsel |
| As each state requires | Other states' notices | Breach counsel |

**Why discovery matters.** The FTC's 30 days run from the first day any employee, officer, or agent knew of the event. A contractor agent who ignored a suspicious email can start the clock without the company knowing (P01 R-019). That is why POL-03 4.1 and the revised agent agreement (effective 2027-01-01) require same-day reporting.

**Communications.**
- Affected clients: a call from the closer or managing broker the same day, then a written follow-up by mail or to a verified email address, never to the compromised mailbox.
- All open files: the standard wire fraud warning is repeated by phone at the next contact for 30 days.
- Agents: an alert through the agent services channel with the indicators and the reminder never to forward instructions.
- Media: holding statement approved by counsel; no comment on amounts or recovery.

## 7. Recovery (RC.RP, RC.CO)
Restore in the BIA priority order (P05): BP-01 closing and disbursement and BP-02 wire instruction delivery first, then BP-03 payoffs, BP-05 earnest money, BP-12 owner distributions, and BP-11 agent payouts.

| Order | Step | Validation |
|---|---|---|
| 1 | Resume the affected closing only after new instructions are posted in the portal and confirmed by a callback to the contract-file number | Callback log entry; second approver |
| 2 | Release held payments one by one after STD-05 verification | Two-person approval recorded |
| 3 | Return the compromised account to service with MFA (security key for staff) and no rules | IRT sign-off |
| 4 | Reconcile all affected escrow and trust accounts; explain any difference and the corrective action in the reconciliation (r. 61J2-14.012(3)) | Signed by the Broker of Record or the President of Title and Closing |
| 5 | Pursue recovery: bank recall results, insurance claim under the funds transfer fraud sublimit, closing protection letter claim where applicable | CFO tracks recoveries |

Tell affected clients, lenders, and the other side of the transaction when the closing is back on schedule (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; written report within 30 days (POL-03 4.11; 314.4(h)(7)). The report states which control failed and the remediation required (314.4(h)(5)).
- Update the risk register (P01 R-001 to R-003, R-019, R-022, R-052), the POA&M (P07), training content (AT-2 lessons learned), and this runbook.
- Include the event, the response, and any notices in the Qualified Individual's next report to Title and Closing's board of managers and the audit committee (314.4(i)(2)).
- Retain the incident record, decision log, and notices for at least 5 years (POL-01 4.12; Fla. Stat. 501.171(4)(c) for any no-harm determination).

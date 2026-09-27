# Incident Response Runbook: Business Email Compromise Targeting Closing Funds

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management and an in-house Closing Services division) |
| Tier / Vertical | Small / Real Estate and Rental and Leasing |
| Incident type | Business email compromise (BEC) targeting closing funds. **Variant A:** a contractor agent's mailbox is taken over and a buyer is sent altered wire instructions. **Variant B:** a spoofed lender payoff letter diverts an outgoing disbursement from the title escrow trust account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; part of the written incident response plan under 16 CFR 314.4(h) |
| Goals | Stop and recover the money first; contain the mailbox or channel; keep closings running safely; meet every notice deadline; fix the weakness that allowed it (POL-03 section 1) |
| Runbook owner | IT Manager (Qualified Individual) |
| Approved | 2026-09-21 by the COO |
| Last tested | Not yet. First tabletop exercise due 2026-12-15 (POAM-018) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | COO | Incident line (cell), then the out-of-band group chat on personal phones |
| Funds response, trust account (variant B) | Closing Services Manager | Controller | Cell; escrow bank wire room by phone |
| Funds response, sales and property management escrow | Controller | Closing Services Manager | Cell; escrow bank fraud desk by phone |
| Client contact (buyers, sellers, lenders) | Transaction Coordination Manager (variant A); Closing Services Manager (variant B) | Sales Manager for the agent's office | Phone only, to numbers from the contract file or the lender's published number |
| Technical response | MSP incident team | Forensic firm from the cyber insurer's panel | MSP 24x7 line |
| Legal and notice decisions | Outside counsel (insurer panel) | COO | Via the insurer hotline |
| Escrow disputes and Commission notice | Majority owner and Broker of Record | COO | Cell |
| Cyber insurer | Carrier claims hotline | n/a | Policy card in the incident binder |
| Title insurance underwriter | Agency or claims contact | n/a | **To be confirmed by 2026-10-31 (P03 G-037)** |
| Law enforcement | FBI IC3 (www.ic3.gov); FBI field office | Local police (for the report some banks require) | Numbers in the incident binder |

**Out-of-band first.** Assume the affected mailbox, and possibly others, is being read by the attacker. Do not discuss the incident by email. Coordinate on personal phones and the printed contact list in the incident binder at each office.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at both offices: this runbook, contacts, the notification matrix, and the incident log template (section 8)
- [ ] **24x7 fraud and wire desk numbers for all three escrow banks**, confirmed by phone, with the name of the relationship manager. **Gap until 2026-10-31 (POAM-018)**
- [ ] MFA on every mailbox, including all contractor agents, and legacy protocols blocked. **Gap until POAM-001 closes (2026-11-30)**
- [ ] Alerts on new forwarding rules, risky sign-ins, and bulk downloads, triaged 24x7 by the MSP. **Gap until POAM-003 closes (2026-12-31)**
- [ ] Written disbursement verification procedure with independent callback in use (POL-03 4.9). **Gap until POAM-002 closes (2026-10-31)**
- [ ] Wire instructions delivered only through the Closing Communications Portal; clients told at contract to call the closing team before sending any money (POL-05 4.4)
- [ ] External auto-forwarding blocked (POAM-006)
- [ ] Mailbox audit logging on and logs exported for 1 year (POAM-007)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A buyer or seller asks about new, changed, or "updated" wire instructions | Client call or email | Tell them **not to send money**. Call the incident line. Confirm instructions only by phone from the contract file number |
| Buyer says funds were sent but the escrow account has not received them | Closing Services or Controller | Declare immediately. This is the most common sign of variant A |
| Lender says a payoff was not received, or the payoff letter's bank account does not match the lender's records | Lender, closer | Declare immediately (variant B) |
| A deposit verification request (r. 61J2-14.008(2)(b)) comes back unconfirmed, or the holder says no deposit arrived | Transaction coordinator | Declare; treat as a possible diverted deposit |
| Unexpected inbox rules, forwarding, or sent messages the agent did not write | Agent, IT, MSP alert | Declare; start mailbox containment (section 5) |
| An agent or employee entered a password on a suspicious page, or approved an unexpected MFA prompt | Staff report | Reset, revoke sessions, review sign-ins; declare if there is any unusual activity |
| Email from a look-alike domain imitating the company, a lender, or a title company | Staff or client report | Declare if any client acted on it; otherwise log and block the domain |

**Declare a BEC incident when** a payment instruction may have been altered, any money may have gone to the wrong account, or a company mailbox shows signs of takeover.

**Record the time of discovery.** For the FTC rule, a notification event counts as discovered on the first day it is known to any employee, officer, or other agent of the company (16 CFR 314.4(j)(2)). Contractor sales associates act as the brokerage's agents, so **the day an agent learns of it can start the 30-day clock.** Florida's 30-day clock runs from the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(4)(a)).

## 3. First hour: stop the money (RS.MI)
Every minute counts. Once the receiving bank has accepted a payment order, a recall works only if that bank agrees (Fla. Stat. 670.211(3)), and funds are often moved out within hours.

**Variant A: buyer wired funds on altered instructions**
| Step | Who | Done when |
|---|---|---|
| 1. Call the buyer (number from the contract file). Tell them to call **their own bank's** fraud or wire department now and ask for a recall of the wire and a hold harmless or indemnity letter. Stay on the line or call back within 15 minutes | Transaction Coordination Manager | Buyer confirms the bank request and gives the reference number |
| 2. Give the buyer the fraudulent account and routing details and ask them to file an IC3 complaint the same day | Transaction Coordination Manager | Details sent by phone or through the portal, not by email |
| 3. Call the company's escrow bank to report the fraudulent receiving account and ask it to alert the receiving bank | Controller or Closing Services Manager | Bank reference number logged |
| 4. File the company's own IC3 complaint with full banking details | IT Manager | IC3 complaint ID logged |
| 5. Freeze the agent's transactions: no instruction changes on any of the agent's open files; call every party on those files to warn them, using contract-file numbers | Sales Manager with Closing Services | All parties reached |
| 6. Contain the mailbox (section 5, steps 1-3) | IT Manager with MSP | Sessions revoked, rules removed |

**Variant B: trust account disbursement sent on a spoofed payoff letter**
| Step | Who | Done when |
|---|---|---|
| 1. Call the escrow bank's wire room: request a recall of the wire and ask the bank to contact the receiving bank; request a hold harmless or indemnity letter | Closing Services Manager | Recall request reference logged |
| 2. Hold all other pending disbursements on that closing and any payoff received by email in the last 30 days until each is re-verified by independent callback | Closing Services Manager | Hold placed in the closing software |
| 3. File an IC3 complaint with full banking details | IT Manager | IC3 complaint ID logged |
| 4. Call the lender at its published number to confirm the real payoff amount and account, and tell it the loan was not paid | Closing Services Manager | Lender contact name and new payoff letter |
| 5. Tell the majority owner, the cyber insurer, and the title insurance underwriter the same day | COO | Claim or reference numbers logged |
| 6. Record the trust account impact; funds of other clients must not be used to cover the shortage unless the closing instructions allow it (Fla. Stat. 626.8473(4)). The majority owner decides how the company funds any shortage | Controller; majority owner | Decision recorded |

In both variants, start the incident log (section 8) in the first hour: timeline, actions, who, and when.

## 4. Analysis (RS.AN)
1. **Channel:** was a company mailbox taken over, or was the email spoofed from a look-alike domain? Review the message headers, the sender domain's registration date, and the mailbox's sign-in log.
2. **Mailbox activity** (if taken over): sign-ins by location and client, inbox and forwarding rules, messages sent, deleted, or read, and any third-party app consents. Export the audit logs **today**; default retention can be as short as 90 days (POAM-007).
3. **Other targets:** search all mailboxes for the same sender, domain, subject lines, and fraudulent account numbers. Other open transactions of the same agent or lender are the next targets.
4. **Data exposed:** list the clients whose information was in the mailbox or its forwarded copies, what data elements (Social Security, driver license, or passport numbers; bank account data; the agent's own password), and each person's state of residence. **Separate Closing Services customers' information** (customer information under 16 CFR 314.2(d)) from brokerage-only client data. This list drives section 6.
5. **Preserve evidence:** keep the fraudulent emails with full headers, the wire records, and the log exports. Maintain chain of custody for the forensic firm and law enforcement.

## 5. Containment and eradication (RS.MI)
1. Reset the password of the affected account, revoke all sessions and tokens, and require MFA before the account is used again (contractor accounts included).
2. Remove every inbox and forwarding rule the user did not create; remove unknown app consents and mobile device partnerships.
3. Block legacy authentication for the account (for all accounts once POAM-001 closes).
4. Block the fraudulent sender addresses and look-alike domains; report look-alike domains to the registrar for takedown.
5. Check the other mailboxes that received the same phishing message; reset any that show the same indicators.
6. If the Closing Communications Portal or integration service may have been touched, rotate their API keys and check the portal's wire instruction records against SYS-02.
7. Confirm with the MSP or forensic firm that no persistence remains before closing containment.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every regulatory and individual notice before it goes out.

**Notification determination** (counsel and the Qualified Individual, documented in the incident log):
1. Was unencrypted **customer information** acquired without authorization? Unauthorized access is presumed to be acquisition unless there is reliable evidence it was not (16 CFR 314.2(m)). If yes, count the consumers. **500 or more: notify the FTC within 30 days of discovery.**
2. Was **personal information** of Florida residents accessed (Fla. Stat. 501.171(1)(g))? A mailbox takeover always exposes at least the account holder's email address and password. If yes, notify affected Floridians within 30 days of the determination, unless counsel documents a no-harm determination under 501.171(4)(c).
3. Where do the other affected people live? Apply each state's law (about 30% of buyers live outside Florida).

A worksheet for counting consumers and deciding encryption status is due with the tabletop on 2026-12-15 (P03 G-044).

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Bank recall requests; buyer told to call their bank | Closing Services Manager or Transaction Coordination Manager |
| Day 0 | IC3 complaints (company and victim); cyber insurer and outside counsel engaged; title underwriter told (variant B) | IT Manager; COO |
| Day 0-1 | Call every party on affected transactions by phone: no wire instructions will come by email; confirm any instructions by calling the closing team | Transaction Coordination Manager |
| Day 0-2 | Staff and agent briefing by phone or in person: what happened, what to watch for, do not discuss outside the company | COO |
| Within 15 business days | If a missing deposit leads to conflicting demands or good-faith doubt about sales escrow funds: written notice to the Florida Real Estate Commission; start a settlement procedure within 30 business days (Fla. Admin. Code r. 61J2-10.032(1)) | Majority owner and Broker of Record |
| Within 30 days of discovery | FTC notice if 500 or more consumers (16 CFR 314.4(j)) | IT Manager and counsel |
| Within 30 days of determination | Florida individual notice; Department of Legal Affairs notice if 500 or more Floridians; or the no-harm determination sent to the Department | COO and counsel |
| Per each state's law | Other states' notices | Counsel |

**Plan to the shorter clock.** The FTC clock starts at discovery by anyone in the company, including a contractor agent. The Florida clock starts at determination. Counsel should fix both dates in the log on day 0.

**Escrow disputes.** The steps above for the Commission notice were added on 2026-09-21. The Broker of Record's detailed procedure (templates and the choice of settlement procedure) is due 2026-10-31 (P03 G-055).

## 7. Recovery (RC.RP, RC.CO)
1. Resume closings only through the verified channel: instructions posted in the Closing Communications Portal and confirmed by a phone call the client makes to the number in the contract packet.
2. Re-verify, by independent callback, every payoff and every disbursement instruction on the affected agent's and lender's open files before funds move.
3. Reschedule closings that cannot fund on time (P05 BP-01, MTD 8 hours); tell lenders so rate locks can be extended where possible.
4. Restore any mailbox content the attacker deleted from the vendor's retention (there is no independent email backup until POAM-004 closes).
5. If the Closing Communications Portal must be taken offline, phone every client with a pending closing and tell them that no wire instructions will be sent until it is back. An outage invites fraudsters to fill the gap (P05 BP-02).
6. Tell affected clients, agents, and lenders when the channel is safe again (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing the incident; documentation within 30 days (POL-03 4.8).
- Route every weakness found to the risk register (P01, especially R-001, R-002, R-004, R-032) and the POA&M (P07), and revise this runbook.
- Record the funds outcome: amount recalled, amount lost, insurance and underwriter claims.
- Retain all incident records for at least 5 years (POL-01 4.12; a Florida no-harm determination must be kept at least 5 years under 501.171(4)(c)).
- **First entry:** the March 2026 near miss (a spoofed wire instruction email that the buyer questioned) must be documented as the first lessons-learned record by 2026-10-31 (P03 G-040).

**Incident log template**
| Field | Entry |
|---|---|
| Incident ID and variant | |
| Discovery date and time; who first knew (employee, officer, or agent) | |
| Determination date (Florida) | |
| Transactions, clients, and amounts involved | |
| Bank recall and IC3 reference numbers | |
| Accounts and mailboxes affected; containment time | |
| Data exposed; consumer count; Florida and other-state counts | |
| Notification decisions, dates, and counsel sign-off | |
| Funds outcome | |
| Lessons learned and POA&M items opened | |

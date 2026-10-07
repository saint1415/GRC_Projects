# Incident Response Runbook: Business Email Compromise Targeting Closing Funds

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded residential real estate brokerage) with Cris Santos Title and Escrow, LLC; 9 states |
| Tier / Vertical | Enterprise / Real Estate and Rental and Leasing |
| Incident type | A coordinated business email compromise (BEC) campaign against closing funds. Attackers relay MFA to take over contractor agent and closer mailboxes, send buyers altered wire instructions, send closers a spoofed lender payoff letter, and copy closing documents. Includes the **SEC materiality assessment** (with the "series of related occurrences" question), the FTC Safeguards Rule notice, and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Funds Recall Procedure. Part of Title and Escrow's written incident response plan under 16 CFR 314.4(h) |
| Goals | Stop and recover the money first; contain every compromised identity in the campaign; keep closings running only on verified channels; meet every notice and disclosure deadline; fix the weakness that allowed it |
| Runbook owner | Director of Security Operations, with the General Counsel for sections 6 and 7 and the President of Title and Escrow for section 3 |
| Approved | Executive risk committee, 2026-09-08 |
| Last tested | Funds response drill with the two largest trust banks, 2026-03-12. The 2025 enterprise tabletop covered ransomware only and **the disclosure committee has never exercised a BEC case**. Next: BEC tabletop with the disclosure committee on 2026-11-17 (POAM-008) |
| Notification matrix | `notification-matrix.csv` (31 obligations: 2 funds response, 3 FTC, 5 SEC, 4 generic state, 7 Florida worked example, 1 real estate commission, 5 contractual, and 4 status rows for OFAC, CIRCIA, FinCEN, and FAR) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO (Qualified Individual) | CIO | Out-of-band group on company mobile phones |
| Funds response desk | President, Title and Escrow | Vice President, Escrow Accounting | Funds desk line; trust banks' wire rooms by phone |
| Brokerage response (agents, buyers, sellers, deposits) | Executive Vice President, Brokerage Operations | Florida Broker of Record (each state's broker of record for its offices) | Direct mobile |
| Crisis management team chair | Chief Operating Officer | CFO | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, President of Title and Escrow, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Cyber and crime insurers | Carrier claims hotlines | Broker | Policy cards in the incident binder |
| Title insurance underwriters | Agency and claims contacts | President, Title and Escrow | Incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office and IC3 | Local police (for reports some banks require) | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker is reading the affected mailboxes and may hold valid sessions in others. Do not discuss the incident by email or chat. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at each regional office and closing office.

## 1. Preparation checks (Identify / Protect)
- [ ] 24x7 wire room and fraud desk numbers for all 5 trust banks confirmed by phone this quarter, with named relationship managers
- [ ] Wire instructions delivered only inside the Closing Communications Hub; every contract packet tells clients the company never sends or changes wire instructions by email (POL-04 4.9)
- [ ] Payee bank account verification and independent callback numbers enforced in the Hub. **Gap: about 86% coverage and callbacks to letter numbers until POAM-006 closes (2027-03-31)**
- [ ] Phishing-resistant MFA and session binding for everyone in a transaction thread. **Gap: contractor agents on relayable push MFA until POAM-001 closes (2027-03-31)**
- [ ] SIEM alerts on new forwarding rules, token replay, impossible travel, and mass downloads for every tenant. **Gap: the three legacy tenants at AQ-06 to AQ-08 until POAM-003 closes (2026-12-15)**
- [ ] Bank-enforced dual approval on all trust accounts. **Gap: AQ-09 until the 2026-10-31 milestone of POAM-005**
- [ ] Materiality playbook with a fraud-loss scenario and a related-incident method, and a current disclosure committee roster. **Gap until POAM-008 closes (2026-11-30); section 6 below is the draft method**
- [ ] Outside counsel, forensics, insurers, and underwriter contacts confirmed this quarter; state breach law matrix updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A buyer or seller asks about new or changed wire instructions | Client call to an agent, closer, or the Hub | Tell them **not to send money**; call the funds response desk; confirm instructions only inside the Hub or by a call the client makes to the contract-packet number |
| A buyer says funds were sent but the trust account has not received them | Closer; escrow accounting | Declare immediately |
| A lender says a payoff was not received, or a payoff letter's account fails verification or differs from the payoff service | Payoff specialist; verification provider | Declare immediately |
| A deposit verification task (r. 61J2-14.008(2)(b), Florida worked example) comes back unconfirmed | Transaction coordinator | Declare; possible diverted deposit |
| Token replay, impossible travel, or relay-phishing indicators on an agent or closer account | Identity protection; SIEM | Automatic suspension (AC-2(13)); SOC reviews within 15 minutes; declare if the account touched a transaction thread |
| New external forwarding rule or inbox rule hiding lender or title messages | SIEM (enterprise tenant); local IT (legacy tenants until POAM-003 closes) | Declare; contain (section 5) |
| Payee change from a new device, or a payment to an account first seen in the last 30 days | Disbursement Hub (SI-4(5)) | Hold the payment file; escrow officer calls the payee through PRC-04.3 |
| Look-alike domain imitating the company, a lender, or a title company | Domain monitoring; staff report | Takedown request; declare if any client acted on it |

**Declare a severity-1 BEC incident when** a payment instruction may have been altered, any money may have gone to the wrong account, or a mailbox in a transaction thread shows signs of takeover. **Declare a BEC campaign** when two or more such incidents share infrastructure, techniques, sender domains, or receiving accounts; the campaign is then managed as one incident with one log.

**Record three dates, separately, in the incident log:**
1. **FTC discovery date:** the first day the event is known to any employee, officer, or other agent other than the person committing it (16 CFR 314.4(j)(2)). Contractor agents act as the company's agents, so **the day an agent learns of it can start the 30-day FTC clock**. Funds desk staff record the date the first person learned, not the date the SOC opened the case (POAM-018).
2. **State determination date:** for Florida, the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(4)(a)); other states use their own triggers.
3. **SEC materiality determination date:** recorded later by the disclosure committee (section 6). It starts the 4-business-day Form 8-K clock.

## 3. First hour: stop the money (RS.MI)
Once the receiving bank has accepted a payment order, cancellation works only if that bank agrees (Fla. Stat. 670.211, Florida worked example of UCC Article 4A), and diverted funds are often moved within hours. The funds response desk runs PRC-03.4.

**Variant A: a buyer wired funds on altered instructions sent from a compromised agent mailbox**
| Step | Who | Done when |
|---|---|---|
| 1. Call the buyer at the contract-file number. Tell them to call their own bank's wire or fraud department now and request a recall and a hold harmless or indemnity letter | Funds response desk | Buyer gives the bank reference number |
| 2. Give the buyer the fraudulent account details by phone or through the Hub and ask them to file an IC3 complaint the same day | Funds response desk | Details delivered (never by email) |
| 3. Call the receiving trust bank to flag the fraudulent account and ask it to contact the receiving bank | Vice President, Escrow Accounting | Bank reference logged |
| 4. File the company's IC3 complaint with full banking details; for a campaign, also call the FBI field office | CISO | IC3 complaint ID logged |
| 5. Freeze instruction changes on every open transaction of the affected agent; call every party on those files using contract-file numbers | Executive Vice President, Brokerage Operations with the closing offices | All parties reached |

**Variant B: a trust account disbursement was sent on a spoofed payoff letter or changed payee details**
| Step | Who | Done when |
|---|---|---|
| 1. Call the trust bank's wire room: request recall and contact with the receiving bank; request a hold harmless or indemnity letter | Funds response desk | Recall reference logged |
| 2. Hold every pending disbursement on the affected closing, and every payoff received outside the payoff service in the last 30 days, until re-verified through PRC-04.3 | President, Title and Escrow | Holds placed in the Disbursement Hub |
| 3. Call the lender at its published number to confirm the real payoff amount and account, and tell it the loan was not paid | Payoff specialist | New payoff confirmed |
| 4. File IC3; notify the cyber and crime insurers and the title underwriter the same day | CISO; President, Title and Escrow | Claim and reference numbers logged |
| 5. Record the trust account impact. Other clients' funds must not cover a shortage unless the closing instructions allow it (Fla. Stat. 626.8473(4), Florida worked example). The CFO decides how the company funds any shortage | Vice President, Escrow Accounting; CFO | Decision recorded |

**Variant C: a campaign (several mailboxes, tenants, or lenders at once)**
- The incident commander opens one campaign case and links every related case to it. The SOC searches all tenants (including the legacy tenants, by direct export until POAM-003 closes) for the same indicators.
- The President of Title and Escrow may impose an **enterprise disbursement hold**: no disbursement to a payee first verified in the last 30 days without a second escrow officer's callback, until the SOC lifts it.
- The Executive Vice President, Brokerage Operations sends a phone and text alert (no links) to all agents in affected states: no wire instructions by email; report any change request to the funds desk.

## 4. Analysis (RS.AN)
1. **Initial access and spread:** relayed MFA (adversary-in-the-middle kit), stolen session tokens from an agent's own device, password reuse, or spoofing from a look-alike domain. Use identity platform sign-in logs, token replay detections, mailbox audit logs, and message headers. For AQ-06 to AQ-08, export the legacy tenants' audit logs **today**.
2. **Other targets:** search every tenant for the same sender domains, subject lines, attachment hashes, phishing URLs, and fraudulent account numbers. Open transactions of the affected agents, closers, and lenders are the next targets.
3. **Funds tally:** for each attempt, record the amount, whether it was stopped, recalled, or lost, and the receiving bank. This feeds the materiality worksheet in section 6.
4. **Data exposed:** list the people whose information was in the compromised mailboxes, forwarded copies, or downloaded closing documents; the data elements (Social Security, driver license, or passport numbers; bank account data; credentials); and each person's state of residence. **Separate Title and Escrow customer information** (16 CFR 314.2(d)) from brokerage-only client data. This list drives section 7.
5. **Integrity of the TMCC:** confirm no payee, template, or approval rule was changed. Compare approved payee hashes with payment files (SI-7(1)) and review signed approvals (AU-10). If the Hub or bank channels may have been touched, rotate API keys and bank channel credentials.
6. **Evidence:** keep fraudulent emails with full headers, wire records, and log exports under chain of custody for forensics and law enforcement.

## 5. Containment and eradication (RS.MI)
1. Revoke all sessions and refresh tokens for affected accounts; reset passwords; require re-registration with a phishing-resistant authenticator before the account is used again (agents included, ahead of POAM-001).
2. Remove inbox and forwarding rules the user did not create, unknown app consents, and mobile device partnerships.
3. Block the phishing and relay infrastructure, sender addresses, and look-alike domains; request takedowns.
4. Put affected agents' SYS-01 accounts in read-only mode until the SOC clears them.
5. Disable accounts of departed agents found in the campaign; run the monthly departure reconciliation the same day (POAM-002).
6. Legacy tenants: the SOC (not local IT) directs containment, using the tenant's own admin console through PAM (POAM-018).
7. Forensics confirms no persistence remains before the campaign case moves to recovery.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. The materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering quantitative and qualitative factors. A cybersecurity incident includes "a series of related unauthorized occurrences" (17 CFR 229.106(a)), so a campaign of individually small diversions is assessed as a whole.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 6.2 | **Related-incident check:** the General Counsel and CISO decide whether the incident is related to earlier incidents (same actor, infrastructure, technique, or weakness) and, if so, assess them together. Funds incidents are also reviewed together every quarter even when each looked immaterial alone | General Counsel; CISO | Relationship decision logged |
| 6.3 | The disclosure committee convenes within 48 hours of declaration of a campaign, or of any incident with a loss or exposure above the playbook trigger, and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.4 | **Special trading blackout** to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.5 | Committee reviews the materiality worksheet (below) with facts from sections 3 to 5 | Committee | Worksheet completed |
| 6.6 | **Materiality determination** made and recorded with the date, time, and reasoning, whether material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.7 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Leave out technical details that would help attackers or impede response | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.8 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.9 | Align timing and content of client, agent, lender, media, and investor communications with the filing; brief the audit committee and board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.10 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Unrecovered funds the company must make good; recall and legal costs; forensic costs; notification and credit monitoring costs; insurance recoveries and retentions; lost Title and Escrow revenue from lenders or builders who move their business (P05 values) |
| Series | Number of related incidents, total amounts attempted and lost across them, duration of the campaign, and whether the same weakness keeps being exploited |
| Operational | Disbursement holds and delayed closings; offices or states affected; Hub or Disbursement Hub availability |
| Data | Number of consumers and states; data types (Social Security numbers, bank data, identity documents); whether data was published or used for further fraud |
| Legal and regulatory | FTC notice; state attorney general and real estate commission or insurance department inquiries; trust fund rule exposure; litigation by buyers, sellers, or lenders; license consequences |
| Reputation and strategy | Media coverage; loss of SL-1 business clients or homebuilder relationships; agent recruiting; effect on acquisitions |

**Worked example of the clocks (fictional dates):** a contractor agent learns on Friday 2027-02-26 that a buyer received changed wire instructions; that is the **FTC discovery date**. The SOC declares a campaign on Monday 2027-03-01 after finding 5 compromised mailboxes. On Wednesday 2027-03-03, forensics confirms that closing documents for about 1,900 Title and Escrow customers were copied from two closer mailboxes; that is the **Florida determination date** for the Floridians among them. The disclosure committee determines on Thursday 2027-03-11 at 15:00 that the campaign, assessed with two related incidents from 2027-01, is material. Deadlines:
- **Form 8-K:** by Wednesday 2027-03-17 (4 business days: March 12, 15, 16, and 17).
- **FTC notice:** no later than 30 days after 2027-02-26, which is Sunday 2027-03-28; the plan files by Friday 2027-03-26.
- **Florida individuals and Department of Legal Affairs:** no later than Friday 2027-04-02 (30 days after 2027-03-03). The 15-day good-cause extension, if granted, applies only to individual notice.
- **Other states:** counsel's state table, planned to the earliest date per state.

The FTC date comes first even though the SOC opened the case later, which is why the first-report date must be captured at the closing office.

## 7. Notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | **FTC determination:** was unencrypted Title and Escrow customer information acquired without authorization? Unauthorized access is presumed to be acquisition unless reliable evidence shows it was not (16 CFR 314.2(m)). Count consumers; 500 or more requires FTC notice within 30 days of discovery with the six content items in 314.4(j)(1) | Chief Privacy Officer; CISO (Qualified Individual) | Signed determination and count |
| 7.2 | Build the affected population from forensic results: each person, data elements, and **state of residence**. Separate (a) Title and Escrow customers; (b) brokerage clients; (c) business clients' borrowers whose data came in lender closing packages; (d) agents and employees whose credentials were taken | Chief Privacy Officer; data team | Affected-person file with state counts |
| 7.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline per state | Outside counsel; General Counsel | State deadline table |
| 7.4 | **Florida worked example:** individual notice within 30 days of the determination; Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at once. The deemed-compliance path in 501.171(4)(g) is not available because the FTC rule has no individual notice procedure | General Counsel | Florida filings |
| 7.5 | **Plan to the shortest clock** across the FTC, every state, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.6 | Honor any law enforcement delay request (FTC public disclosure under 314.4(j)(1); Fla. Stat. 501.171(4)(b) and other states); document it | General Counsel | Delay record |
| 7.7 | **Escrow disputes:** if a diverted or missing earnest money deposit leads to conflicting demands, the broker of record notifies the real estate commission (Florida worked example: within 15 business days, r. 61J2-10.032(1)) and starts a settlement procedure | Florida Broker of Record (each state's broker of record) | Commission notice |
| 7.8 | Notify contractual parties: title underwriters, trust banks, SL-1 business clients with affected files, SL-2 relocation clients if relocation data is involved, and insurers | Contract owners | Contract notices logged |
| 7.9 | Engage the mail vendor, call center, and credit monitoring provider; mailbox owners never receive notices at a compromised address | Chief Privacy Officer | Vendors active |
| 7.10 | Track inbound vendor notices (Fla. Stat. 501.171(6) and contract terms) if the campaign started at a vendor, such as a lender or the e-signature service | Director of Third-Party Risk Management | Vendor notices logged |

**Extortion:** if the attacker threatens to publish closing documents, no payment may be made without CEO approval, legal review, and an OFAC sanctions check (POL-03 4.6). Paying does not remove notification or disclosure duties.

## 8. Recovery (RC.RP, RC.CO)
1. Resume disbursements only through verified paths: payee verification or an independent callback by a second escrow officer for every payee touched by the campaign.
2. Re-verify every payoff and disbursement instruction on the affected agents', closers', and lenders' open files before funds move.
3. Reschedule closings that cannot fund safely (P05 BP-05: MTD 4 hours; BP-04: MTD 8 hours); tell lenders so rate locks can be extended.
4. Restore deleted mailbox content from the independent mailbox backup (enterprise tenant) or the provider's retention (legacy tenants).
5. If the Hub must be taken offline, phone every client with a pending closing and say no instructions will be sent until it is back; an outage invites fraudsters to fill the gap (P05 BP-06).
6. Lift the enterprise disbursement hold only when the SOC confirms containment and the President of Title and Escrow agrees.
7. Tell affected clients, agents, and lenders when the channels are safe again (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing the incident; written report within 30 days; root cause recorded in the case before closure (POL-03 4.3).
- Update the risk register (P01: R-001, R-002, R-005, R-044, R-053), the POA&M (P07), this runbook, and the materiality playbook.
- Record the funds outcome: amounts attempted, stopped, recalled, and lost; insurance and underwriter claims.
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure and adds it to the quarterly related-incident look-back.
- Retain all records, including materiality minutes and notification determinations, for at least 7 years; a Florida no-notice determination must be kept at least 5 years (501.171(4)(c)).

**Incident log template**
| Field | Entry |
|---|---|
| Incident or campaign ID; variant (A, B, C) | |
| FTC discovery date and who first knew (employee, officer, or agent) | |
| State determination dates | |
| Related incidents assessed together (IDs) | |
| Transactions, clients, and amounts attempted, stopped, recalled, and lost | |
| Bank recall and IC3 reference numbers | |
| Identities, mailboxes, and tenants affected; containment time | |
| Data exposed; consumer count; counts by state | |
| Materiality determination date, time, and result | |
| Notification decisions, dates, and counsel sign-off | |
| Lessons learned and POA&M items opened | |

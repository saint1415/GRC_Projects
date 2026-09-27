# Incident Response Runbook: Core Processor Cyber Incident and Extended Outage

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (regional commercial bank), subsidiary of Cris Santos Company, Inc. (bank holding company) |
| Tier / Vertical | Mid-Market / Finance and Insurance |
| Incident type | Ransomware at the core processor takes the core banking system (SYS-01) down for more than a day. Variants: a digital banking provider outage, and a cyber incident in the bank's own payments hub that stops correspondent services |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF GV.SC-08 (suppliers included in incident planning) |
| Policy basis | POL-03 Incident Response Policy (4.4 to 4.7, 4.11, 4.12); STD-03 Third-party risk; STD-08 Contingency and recovery |
| Regulatory basis | 12 CFR Part 53 (53.3 bank notice; 53.4 inbound notice from the processor and outbound notice to bank respondents); 12 CFR 225.302 (holding company); 12 CFR 30 App. B III.C.1.h, III.D, and Supplement A II.A.2 |
| Companion documents | `ir-runbook.md` (BEC and fraudulent wire); `notification-matrix.csv`; BIA (P05); risk register (P01 R-003, R-004, R-009) |
| Runbook owner | Chief Operating Officer (business lead and CMT chair) with the ISO (security lead) |
| Approved | 2026-09-18 by the Chief Operating Officer |
| Last tested | Not yet. Core outage tabletop with the core processor's client team scheduled 2027-01-20 (POAM-012) |

## 0. Why this runbook exists
The core supports 12 of the 17 BIA processes. A 72-hour core outage would cost about $850,000 and delay about $500 million of customer and respondent payments (P05). Unlike a BEC fraud, a multi-day core outage will almost certainly be a **notification incident** for the bank and the holding company, and it disrupts services the bank provides to its 18 respondents. The processor's stated RTO is 4 hours (SOC 2 system description), but a ransomware attack at the processor could exceed it for all its client banks at once (P01 R-003).

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| CMT chair | Chief Operating Officer | President and CEO | Declares severity; approves workarounds, spending, and customer relief |
| Security lead | Information Security Officer | IT Risk and Compliance Manager | Cut and later re-establish connections safely; assess exposure of bank data; hunt for indicators |
| Technology lead | Chief Information Officer | Infrastructure Manager | Offline modes, alternate processing, reconciliation after restoration |
| Notification decision | President and CEO with the ISO and General Counsel | COO | Notification incident determination; OCC and Federal Reserve notices |
| Respondent notices | Correspondent Services Director | Director of Payments Operations | 53.4-type notices and updates to respondent institutions |
| Liquidity | Chief Financial Officer | Controller | Funding position from Federal Reserve statements; borrowing lines; large-payment holds |
| Branch operations | Retail Banking Director | Director of Deposit Operations | Offline teller mode, limits, customer queues |
| Payments | Director of Payments Operations | Correspondent Services Director | Wire and ACH decisions without core balances |
| Legal | General Counsel | Outside counsel (insurer panel if bank data may be affected) | Contract rights, notices, privilege |
| Customer and media communications | Director of Marketing and Communications | Contact Center Director | Website banner, branch scripts, contact center messages, media statement |
| Board liaison | President and CEO | Chief Risk Officer | Board Risk Committee chair and holding company board informed the same day |

## 2. Detection, severity, and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Processor notice of a computer-security incident affecting services (53.4) | Designated contact mailbox and phone (ISO and COO) | Log the notice time; open a vendor incident; security lead assesses connections |
| Core transactions failing at branches for more than 30 minutes | Branch staff; service desk | Confirm with the processor; branches move to offline teller mode |
| Processor status page or industry alert (FS-ISAC) about an attack on the processor | Threat intelligence | Open a vendor incident; prepare to cut connections |
| Processor reports possible exposure of client data | Processor incident statement | Raise to severity 1; privilege protocol (General Counsel) |

**Severity levels:**
- **Severity 3:** core unavailable under 4 hours, no data concern. Technology lead manages it.
- **Severity 2:** outage expected to exceed 4 hours, or any processor cyber incident. CMT chair informed; notification incident determination started.
- **Severity 1:** outage expected to exceed 8 hours (the MTD for BP-01 to BP-03), or any sign that bank data was accessed. Convene the CMT within 2 hours (POL-03 4.4).

**Record these times:** the processor's notice; the bank's own detection; the notification incident determination (starts the 36-hour clock); the time correspondent services were first disrupted (starts the 4-hour test for respondent notices).

## 3. First 24 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-1 h | **Isolate the connections** if the processor reports a cyber incident: disable the payments hub API credentials and file transfers to the core; ask the processor to confirm the private circuits are quarantined on its side; block processor IP ranges except the status channel | Security lead | Connections disabled; confirmation logged |
| 0-1 h | Branches to offline teller mode with per-transaction limits; contact center script live | Retail Banking Director; Contact Center Director | Mode confirmed at all 28 branches |
| 0-2 h | Request a written incident statement from the processor: what happened, whether bank data is affected, indicators of compromise, expected restoration | General Counsel with the COO | Request sent; tracked in the decision log |
| 0-4 h | Hunt for the processor's indicators in bank logs (SIEM, firewalls, payments hub) | Security lead with the MSSP | Hunt results recorded |
| 0-4 h | **Notification incident determination** (section 5) | CEO, ISO, General Counsel | Decision recorded with time and reasons |
| 2-4 h | Liquidity position from the Federal Reserve account statement and the payments hub log; hold large outgoing wires until confirmed | CFO | Position approved by the CFO |
| 4 h | If correspondent services have been disrupted for 4 hours, or are reasonably likely to be, notify bank respondents' designated contacts (section 5) | Correspondent Services Director | Notices sent and logged |
| 4-8 h | Payments decisions: which wires may be sent against last known balances (section 4) | Director of Payments Operations with the CFO | Decision documented |
| 8-24 h | Customer and media communication; relationship managers call the top 200 treasury customers | Communications; Treasury Management Director | Messages sent |
| Within 36 h of a "yes" determination | OCC notice and Federal Reserve notice | President and CEO | Notices sent; times logged |

## 4. Business continuity workarounds (RC.RP)
| Process (P05) | Workaround | Capacity and limits |
|---|---|---|
| BP-03 Branch services | Offline teller mode; cash withdrawals up to $1,000 per customer per day; deposits accepted and posted later | Offline files must be posted in sequence at restoration |
| BP-01 Customer wires | Wires allowed against the prior night's balance from the data warehouse extract, up to $250,000 per customer with COO approval above that; callbacks continue | Risk of overdrafts; the CFO sets a daily aggregate cap |
| BP-02 Correspondent payments | Respondents' wires sent against their Federal Reserve-settled positions as confirmed by phone with each respondent; limits per respondent | Respondents notified; volume capped by the CFO |
| BP-05 ACH | Incoming files held and posted at restoration; outgoing files processed for payroll customers with prior-day balances | Late returns tracked |
| BP-04 Online banking | Banner message; balances frozen at last update; transfers disabled | Contact center volume about 4 times normal |
| BP-07 Cards | Card processor stand-in limits | Set with the card processor |
| BP-13 Liquidity | Federal Reserve statement; borrowing lines on standby | CFO approves |

**Trigger to escalate further:** outage expected beyond 72 hours, or any evidence that bank data was stolen. The CMT then decides whether to move processing to an alternate provider arrangement, and the CEO briefs the board.

## 5. Legal and regulatory analysis (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel confirms each notice.

1. **Is it a notification incident for the bank?** The definitions in 12 CFR 53.2(b)(4) and (7) look at the effect on the bank's operations; they are not limited to systems the bank owns. A multi-hour core outage that stops branch, wire, and online banking services for a material portion of customers meets 53.2(b)(7)(i). Record the determination as soon as the expected duration makes that effect "reasonably likely". The OCC must receive notice as soon as possible and **no later than 36 hours** after the determination (53.3).
2. **Holding company.** The same event affects the holding company's only subsidiary. The Federal Reserve must receive notice within 36 hours of the holding company's determination (12 CFR 225.302). The CEO signs one determination record for both.
3. **Inbound notice.** The processor must notify the bank's designated contact as soon as possible when an incident disrupts covered services for 4 or more hours (53.4). If the notice went to the wrong people (the processor has the bank's contacts, but 4 other providers do not yet; POAM-015), log that as a finding.
4. **Outbound notice to respondents.** General Counsel's working view is that the bank's correspondent processing services are covered services, so the bank must notify each affected bank respondent's designated contact as soon as possible once it determines the incident has disrupted, or is reasonably likely to disrupt, those services for 4 or more hours (53.4; 225.303 or 304.24 for respondents supervised by the Federal Reserve or FDIC). Credit union respondents are notified under their agreements. Respondents then make their own notification decisions.
5. **Bank data at the processor.** If the processor reports that bank customer information was accessed, the bank remains responsible for regulator and customer notice (Supplement A II.A.2): OCC notice of unauthorized access to sensitive customer information as soon as possible, customer notice if misuse has occurred or is reasonably possible, and state notices under the law of each state where affected individuals reside (Florida as the worked example). Under Fla. Stat. 501.171, a third-party agent must notify the bank within 10 days of determining a breach; the bank's own clocks then apply.
6. **Ransom.** The bank does not pay the processor's attacker. If the processor considers paying, ask for confirmation of its OFAC sanctions check (OFAC advisory, 2021-09-21) and document it. CIRCIA reporting is **not yet required** (no final rule as of 2026-09-25).
7. **Contracts and insurance.** Check the processor contract for service credits and termination rights (no recovery terms today; R-003). The CFO notifies the cyber insurer (business interruption) and records costs.

## 6. Reconnection (RC.RP)
Do not reconnect to the processor until:
- [ ] the processor provides written confirmation of containment and eradication, ideally with a third-party forensic attestation;
- [ ] the processor's indicators of compromise have been searched for in bank logs with no findings;
- [ ] credentials, certificates, and API keys for the payments hub and file transfers are rotated;
- [ ] the connection is re-established with least privilege and monitored by the MSSP for 30 days;
- [ ] the CMT chair approves reconnection.

Then post offline branch files in sequence, post queued ACH, reconcile wires sent during the outage against core postings and the Federal Reserve account, clear overdrafts created by the workarounds, and release online banking. The Controller signs off the reconciliation before the CMT stands down.

## 7. Variants
| Variant | Key differences | Regulatory notes |
|---|---|---|
| **Digital banking provider outage** (SYS-02) | Branches and core work; online banking and business wire initiation stop. Business wire requests go to relationship managers with callback; ACH files by secure upload | Notification incident only if a material portion of customers cannot bank; the provider owes a 53.4 notice (contact on file since 2026-03) |
| **Payments hub or correspondent portal cyber incident** (SYS-03, bank-run) | The bank is the victim and the service provider. Secondary wire room and second-region failover (9 hours in the 2025 test; R-004) | Notification incident likely if wires stop for a business day; outbound respondent notices after 4 hours; bank data exposure analysis is the bank's own |
| **Card processor outage** (SYS-11) | Stand-in authorization; branch cash | Processor owes a 53.4 notice (contact on file) |

## 8. Post-incident (ID.IM)
- Lessons learned within 14 days of full restoration, including cash, liquidity, and respondent impact.
- Update the risk register (P01 R-003, R-004, R-009), the BIA values (P05) if impacts differed from estimates, the vendor review (P09 `vendor-soc2-review.csv`), and this runbook.
- Use the event in the 2027 core processor contract negotiation (recovery time and incident notice terms).
- Report in the annual board report (III.F); retain the decision log and processor correspondence for at least five years (POL-01 4.14).

## 9. Worked example (tabletop script)
| Time | Event | Clock or decision |
|---|---|---|
| Day 0, 05:40 | Processor detects ransomware in its primary data center and shuts down client connections | |
| Day 0, 06:25 | Processor calls the bank's designated contact line (ISO and COO) under 53.4; estimated restoration "unknown" | Inbound notice logged |
| Day 0, 06:40 | Security lead disables payments hub API credentials and file transfers to the core | Isolation complete |
| Day 0, 08:00 | Branches open in offline teller mode; CMT convened (severity 1) | |
| Day 0, 10:30 | Processor says restoration will take "at least 48 hours"; no evidence yet of client data theft | |
| Day 0, 11:00 | CEO, ISO, and General Counsel determine a notification incident: branch, wire, and online banking services to a material portion of customers are disrupted and reasonably likely to stay disrupted. Recorded 11:00 | **36-hour clock starts (bank and holding company)** |
| Day 0, 12:00 | Correspondent services disrupted since 05:40 (respondent settlement accounts are on the core); notices sent to the 11 bank respondents' designated contacts and to the 7 credit unions under their agreements | Outbound notices sent |
| Day 0, 15:00 | OCC supervisory office notified by phone and email; Federal Reserve contact notified for the holding company | Well within 36 hours |
| Day 2, 18:00 | Processor restores from clean backups at its secondary site; forensic attestation received Day 3 | |
| Day 3, 09:00 | Bank reconnects after the checklist; offline files posted; reconciliation complete Day 3, 22:00 | CMT stands down Day 4 |
| Day 12 | Processor confirms that no bank customer data left its network (forensic report) | No customer notice required; decision and basis recorded |

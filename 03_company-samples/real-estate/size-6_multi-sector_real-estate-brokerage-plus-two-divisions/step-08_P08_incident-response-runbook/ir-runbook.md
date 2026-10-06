# Incident Response Runbook: Business Email Compromise Targeting Closing Funds (Cross-Division)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Real Estate and Rental and Leasing |
| Incident type | Business email compromise: a contractor agent's mailbox is taken over and used to divert a buyer's closing funds on a sale that touches all three divisions. Variant A2 covers a brokerage earnest money deposit; variant B covers a Homebuilding trade partner bank change fraud |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06). This runbook is part of the written incident response plans of Home Loans and Title (16 CFR 314.4(h)) |
| Runbook owner | Group CISO (Qualified Individual); notifications owned by the Group General Counsel |
| Approved | 2026-09-17 by the Group CISO, the Group General Counsel, the President, Mortgage, and the President, Title |
| Last tested | Technical playbooks (mailbox takeover, wire recall) tested quarterly. **The multi-regulator notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop is due 2026-12-15 (POAM-007) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** a contractor agent who is one of the about 9,900 still signing in with a password only (scenario gap 1) enters credentials on a fake e-signature page. The attacker signs in to group email (SYS-G4) through a legacy protocol from a hosting provider and syncs the whole mailbox (3 years of mail). It adds an inbox rule that moves messages containing "wire," "closing," or "title" into an unused folder.
- **Dwell:** for 9 days the attacker watches the agent's transactions and picks a new-home sale: a home built by Homebuilding, financed by Home Loans, and closing with Title.
- **Fraud:** two days before closing, the attacker emails the buyer from the agent's real mailbox, with the thread history, saying Title has "updated wiring instructions after an audit" and attaching a PDF. The buyer ignores the portal warning and wires $186,000 cash to close to a mule account at another bank.
- **Discovery (Day 0):** on closing morning Title's receipt check shows no funds. The buyer says the wire was sent. The Title closer calls the SOC fraud line. Within an hour the SOC finds the inbox rule and the legacy-protocol sessions.
- **Forensic estimate at Day 6:** the mailbox held records about 1,420 consumers: Title customer information on 640 (commitments, settlement statements), Home Loans customer information on 530 (closing disclosures, pre-approval letters, some with Social Security numbers and driver license images), and brokerage-only client data on 380 (some people appear in more than one group). About 1,060 are Florida residents; 360 live in 4 other states.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO (Qualified Individual) | Group Chief Risk Officer | Out-of-band bridge |
| Funds recovery | Group Treasurer | Title escrow accounting director | Bank wire rooms by phone from numbers on file |
| Technical response | Group SOC and identity teams | Forensic firm on the insurer's panel | SOC bridge |
| Notifications and legal | Group General Counsel with panel breach counsel | Division general counsels | Out-of-band bridge |
| Title decisions (FTC, insurance commissioners, underwriter) | President, Title | Title compliance officer | Division bridge |
| Home Loans decisions (FTC, SAR, investors) | President, Mortgage | Home Loans BSA officer | Division bridge |
| Brokerage decisions (clients, escrow, agents) | Residential Brokerage president | Florida Broker of Record | Division bridge |
| Homebuilding liaison | Homebuilding chief operating officer | Homebuilding security and compliance lead | Division bridge |
| SEC materiality | Disclosure committee | Chief Financial Officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office and IC3; Secret Service field office | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read any mailbox it has touched. Use the crisis line and managed mobile devices. Never contact a buyer, seller, lender, or trade partner using details from an email; use the numbers in the title file, the contract, or the vendor master.

## 2. Preparation checks (Identify / Protect)
- [x] Wire instructions to consumers only through the Closing Communications Portal (SYS-B2), with identity proofing before display
- [x] Callback to verified numbers and dual approval with hardware keys for every title escrow trust wire (P07: 59 of 60 sampled wires had a callback record)
- [x] 24x7 SOC with mailbox rule and risky sign-in alerts for employees
- [ ] MFA for every contractor agent and legacy protocols blocked (**gap until POAM-001 closes**)
- [ ] Sign-in analytics for the contractor tier (**gap until POAM-005 closes**)
- [ ] Payee verification for brokerage refunds, owner payouts, commissions, and trade partner bank changes (**gap until POAM-003 closes**)
- [ ] SYS-B1 and SYS-M2 audit logs in the SIEM (**gap until POAM-004 closes**)
- [ ] Notification matrix complete with per-institution counting and insurance commissioner rows, and exercised (**gap until POAM-007 closes**)
- [x] Forensic retainer and insurer panel confirmed; bank wire room contacts in the offline binder
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Expected closing funds not received, or a buyer says they wired to a new account | Title receipt check; buyer call | Treat as diverted funds; open a Severity 1 case; start section 4 immediately |
| New inbox rule that hides or forwards closing-related mail | SYS-G4 alerts | Disable the account sessions; review the mailbox |
| Legacy-protocol or anonymizing-network sign-in to an agent account | SYS-G1 and SYS-G4 logs (agents not yet covered by analytics) | Revoke sessions; reset; review |
| Payee or bank account change request received by email | Any staff member | Do not act; report to the SOC within 1 hour (POL-03 4.1) |
| A trade partner or property owner reports a missing payment | Homebuilding accounts payable; property accounting | Variant B: treat as diverted funds |

**Severity 1** (group scale, POL-03 4.2): any diverted funds, or customer information of a financial institution in an account controlled by an attacker.

**Record discovery dates per institution and per state clock** (POL-03 4.3). Under the Safeguards Rule a notification event is discovered on the first day it is known to any employee, officer, or other agent of the institution (314.4(j)(2)). The parent's SOC runs security monitoring for Home Loans and Title as their service provider, and group policy (POL-03 4.3) conservatively counts knowledge by the SOC or by a contractor agent handling their customers' files. **This runbook therefore treats Day 0, the day the SOC knew, as the discovery date for both institutions;** counsel may refine this, but no clock is planned from a later date. State clocks run from the determination of a breach (Fla. Stat. 501.171(4)(a), worked example), which counsel records separately; for planning, these clocks also start on Day 0.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Recall the wire.** The buyer calls their bank's wire room now to request a recall; the Group Treasurer calls the group's bank and asks it to alert the receiving bank; file an IC3 complaint with full banking details (POL-03 4.7) | Group Treasurer; buyer | Recall requests logged with times; IC3 complaint number |
| 2. Disable the agent account; revoke all sessions and tokens; reset the password; enforce MFA; remove the inbox rule; block legacy protocols for the account | Group identity director | Account secured |
| 3. Hold all open transactions the agent touched: Title calls every buyer and seller from numbers in the title file and confirms that instructions come only from the portal | President, Title; Florida Broker of Record | Every open party reached |
| 4. Search all mailboxes for the attacker's messages, lookalike domains, and the same inbox rule; block the sender infrastructure | Group SOC | Search complete; block list applied |
| 5. Preserve evidence: mailbox audit logs, sign-in logs, message traces, the buyer's emails and wire receipt; legal hold | SOC; forensic firm | Evidence list signed |
| 6. Call the cyber insurer; engage breach counsel and forensics through the panel (before other vendors) | Group Chief Risk Officer | Claim number issued |
| 7. Notify the presidents of Title, Home Loans, and the brokerage **on the bridge** (this starts the parent's third-party agent notice; written notice follows within 10 days) | Incident commander | Each acknowledges |
| 8. Escalate to the disclosure committee within 24 hours of declaration (POL-03 4.6) | Group CISO | Committee convened |
| 9. Decide whether the closing can proceed (buyer's other funds, seller and lender agreement); Homebuilding adjusts the handover date | President, Title; Homebuilding chief operating officer | Decision recorded |

## 5. Analysis (RS.AN)
1. **Mailbox scope.** Use mailbox audit logs (sync and read events) to decide what the attacker accessed. A full legacy-protocol sync means the whole mailbox was acquired. Under the Safeguards Rule, unauthorized access is presumed to be acquisition unless there is reliable evidence that it was not (314.2(m)).
2. **Count per institution.** Tag every person in the mailbox by whose customer information it is: Title, Home Loans, or brokerage-only. The FTC threshold of 500 applies **to each institution separately** (POL-03 4.4). In this exercise both cross it: Title 640, Home Loans 530.
3. **Count per state and per covered entity.** For each covered entity, count affected residents of each state and which data elements were present (Social Security number, driver license, account number with access code, credentials). These drive state individual notices, attorney general or department notices, and consumer reporting agency notices.
4. **Other data in the mailbox.** Outside lenders' borrower data (lender notices) and data of loans already sold to investors (investor notices, per contract).
5. **The agent's own credentials** are personal information under Florida law (501.171(1)(g)1.b., worked example), so the agent gets a notice too.
6. **Root cause:** password-only agent access with legacy protocols, no sign-in analytics for the contractor tier, and a buyer who acted on an email. Feed these to P01 GR-01, GR-02, BR-001, and BR-003.

## 6. Containment and eradication (RS.MI)
1. Enforce MFA and block legacy protocols for **all** agents still under the expired exception, starting with those with open transactions this week (accelerates POAM-001).
2. Turn on the contractor tier in sign-in analytics (accelerates POAM-005).
3. Remove any matching inbox rules found in other mailboxes; reset those accounts.
4. Add the attacker's domains and accounts to the email gateway block list and the SYS-G5 payee deny list.
5. Confirm with forensics that no persistence remains (app consents, forwarding, delegated access) before closing the case.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (30 rows).** Counsel approves every notice. The matrix has four layers:
1. **Funds recovery** (not notice duties, but the most time-critical): wire recall, IC3, insurer.
2. **Inside the group:** the parent, as third-party agent for the subsidiaries whose data sits in group email, notifies Title, Home Loans, and the brokerage within 10 days (Fla. Stat. 501.171(6)(a), worked example). In practice this happens on the bridge on Day 0.
3. **Each entity's own duties:** Title and Home Loans **each** file their own FTC notice; each covered entity sends its own state notices (coordinated letters that name the right entity); Title notifies insurance commissioners in states that enacted a version of NAIC Model #668; the Home Loans BSA officer decides on a SAR.
4. **Outward and contractual:** underwriter, outside lenders, investors, other clients in the mailbox, and the SEC materiality decision.

| When (from discovery, Day 0) | Action | Owner |
|---|---|---|
| Day 0, first hour | Wire recall requests; insurer; IC3 complaint; parent notice to the three subsidiaries on the bridge | Group Treasurer; Group Chief Risk Officer; incident commander |
| Day 0 | Warn every party in the agent's open transactions by phone and in SYS-B2; underwriter notice for the affected closing | President, Title; Florida Broker of Record |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 72 hours of determination | Insurance commissioners in adopting states where Title's affected customers or licenses are (generic; Title list) | Title compliance officer |
| Within 4 business days of a materiality determination | Form 8-K Item 1.05 if material | Disclosure committee |
| Within 10 days of determination | Written third-party agent notice from the parent to each subsidiary | Group General Counsel |
| Within 30 days of discovery | **FTC notice by Title and FTC notice by Home Loans** (as soon as possible; 30 days is the outer limit) | President, Title; President, Mortgage |
| Within 30 days of determination | Florida individual notices by each covered entity; Department of Legal Affairs notice for any covered entity with 500 or more Florida residents; consumer reporting agencies if more than 1,000 at a single time. Apply each other state's law the same way | Each covered entity with counsel |
| Within 30 days of initial detection | SAR decision documented by the Home Loans BSA officer (31 CFR 1029.320) | Home Loans BSA officer |
| Per contract | Outside lenders and loan investors | President, Title; President, Mortgage |

**Plan to the shortest clock.** In this scenario the order is: wire recall (minutes), insurer and IC3 (same day), insurance commissioners (72 hours), SEC (if material), the parent's third-party agent notice (10 days), then the 30-day FTC and state notices.

**Materiality factors for the disclosure committee:** the funds lost ($186,000, within the insurance sublimit); the number of people affected (about 1,420); regulatory exposure (two FTC notices, state attorneys general, insurance commissioners); effect on lender and investor relationships; and whether the incident shows a pattern (11 loss events in 12 months). In this exercise the committee concluded the incident was not material and documented why. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination, not at discovery.

### Variant A2: brokerage earnest money deposit
The same takeover diverts a $25,000 earnest money deposit that the buyer was supposed to wire to a brokerage escrow account. The steps above apply, plus: if the deposit's loss leads to conflicting demands on escrowed funds or good-faith doubt about who is entitled to them, the Broker of Record notifies the real estate commission within 15 business days and starts a settlement procedure within 30 business days (Fla. Stat. 475.25(1)(d)1.; Fla. Admin. Code r. 61J2-10.032(1), worked example).

### Variant B: Homebuilding trade partner bank change fraud
An attacker spoofs a framing subcontractor's email and asks accounts payable to change its bank account. The change is entered in SYS-H1 with one approver, and the next weekly payment of $640,000 goes to the attacker. No consumer data is involved, so there are no FTC or state breach notices. The steps are: wire or ACH recall through the group bank, IC3, insurer, a call to the real trade partner from the number in the vendor master, lien exposure review, and a materiality check by the disclosure committee. Root cause and fix: POAM-003 (trade partner portal, callback through SYS-G5, 10-day hold).

## 8. Recovery (RC.RP, RC.CO)
Email is a High-criticality process (P05 BP-G02: RTO 4 hours), but here it never went down. Recovery is about restoring trust:
1. Confirm identity and email controls for the agent tier (BP-G01, BP-G02).
2. Reopen the affected closing only after Title confirms good funds and the buyer re-verifies instructions in the portal (BP-MT01, BP-BR02).
3. Resume the agent's transactions under a new account, with MFA and a managing broker review of every open file.
4. Tell affected clients what happened and how instructions will reach them (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-01, GR-02, GR-04, BR-001, BR-003, MT-009), the POA&M (POAM-001, POAM-003, POAM-005, POAM-007), the notification matrix, and this runbook.
- Include the incident and the response in the Qualified Individual's next annual reports to the Home Loans and Title boards (314.4(i)(2)), and consider it in the next Reg S-K Item 106 description.
- Retain all incident records for 6 years (POL-01 4.13).

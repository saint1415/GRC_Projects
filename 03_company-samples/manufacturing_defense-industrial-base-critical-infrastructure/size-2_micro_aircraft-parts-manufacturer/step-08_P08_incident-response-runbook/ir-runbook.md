# Incident Response Runbook: Exfiltration of Controlled Unclassified Information (CUI)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts machine shop, DoD subcontractor) |
| Tier / Vertical | Micro / Defense Industrial Base |
| Incident type | Exfiltration of CUI. Worked scenario: an attacker guesses the password of the shared "orders" mailbox in the commercial suite (SYS-02, no MFA), adds a rule that forwards every message to an outside address, and receives Supplier B drawing packages for 3 weeks |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Contract basis | DFARS 252.204-7012(c) to (g) and (m)(2)(ii), text checked on eCFR (version date 2026-09-23) |
| Runbook owner | President (decision maker); Office Manager (incident coordinator) |
| Approved | 2026-08-31 by the President |
| Last tested | Not yet. First tabletop with the MSP and a DIBNet login check due 2026-11-30 (POAM-008) |

## 0. Roles and notification chain (Govern)
The shop has 7 people and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics; the President makes every external decision and files the DoD report.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Decision maker and DoD reporter | President | Office Manager (second certificate holder) | Cell phone (printed contact card) |
| Incident coordinator (log, evidence custody) | Office Manager | President | Cell phone |
| Technical response | MSP 24x7 emergency line | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel counsel; panel forensic firm | Company's export counsel | Assigned on the first insurer call |
| CUI owner contact | Supplier B security contact (scenario); Prime A security contact | Buyer at each customer | Printed contact list (due 2026-09-30) |
| CUI data custodian (what was taken) | CNC Programmer | Quality Inspector | Cell phone |
| Cloud provider | CUI suite provider security support | Provider account team | Support portal; number in the binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** employee or outside report → Office Manager → President and MSP emergency line (at the same time) → insurer hotline (President) → counsel and forensics (through the insurer). The CUI suite provider is called if there is any sign that SYS-01 accounts were touched.

**Out-of-band first.** Assume the commercial suite is watched. Coordinate by phone and text, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Two current DoD-approved medium assurance certificates (President, Office Manager), usable from a clean laptop (252.204-7012(c)(3)). **Gap until POAM-008 closes (2026-10-31)**
- [ ] DIBNet field list filled in advance: CAGE code, Prime A and Supplier B purchase order numbers, customer points of contact, facility clearance status (none), company points of contact
- [ ] Printed binder in the office and at the President's home: this runbook, contact card, notification matrix, DIBNet field list, evidence custody form
- [ ] Audit log export each month and alerts for forwarding rules, mass download, and foreign sign-ins in both suites (AU-6, SI-4). **Gap until POAM-007 closes (2026-12-31)**
- [ ] No shared mailbox receives CUI; Supplier B sends to SYS-01 (P01 R-001). **Gap until 2026-10-31**
- [ ] MSP contract: 24-hour incident notice and "do not reimage before images are taken" (POAM-009)
- [ ] Insurer hotline and policy number checked at each renewal

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A customer says it saw an external forward or bounce from a company mailbox, or received phishing from it | Customer report (scenario: Supplier B) | Office Manager calls the MSP to check mailbox rules and sign-ins; President told at once |
| New forwarding rule, sign-in from abroad, or many downloads in a short time | Suite alert (from 2026-10-31); MSP report | MSP suspends the account and calls the Office Manager |
| Employee entered a password on a page that looked like a sign-in page | Employee report (POL-03 4.2) | MSP resets the password and revokes sessions; check sign-in logs |
| Drawings or models appear somewhere they should not (a forum, a competitor's quote, a foreign request) | Customer, DC3, FBI, or other agency | Declare at once |
| CUI typed into a public AI tool or sent to a personal account | Employee report or monitoring | Declare; treat the tool or account as the "attacker" destination (P10) |

**Declare a CUI exfiltration incident** when any evidence shows that an unauthorized party used a company account or session, or that CUI left company control. Suspected is enough.

**Record the time of discovery.** The 72-hour DoD reporting clock runs from discovery of the cyber incident (252.204-7012(a), (c)). A cyber incident includes possible copying of information to unauthorized media or disclosure to unauthorized persons (252.204-7012(a)). **The commercial suite counts.** It was never meant to hold CUI, but once Supplier B's drawings were in it, it became a covered contractor information system, and the reporting duty applies to it like any other.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Before changing anything:** export the mailbox audit log, message trace for the last 90 days, sign-in log, and the forwarding rule's details (destination, creation time) to a restricted SYS-01 folder | MSP with the Office Manager watching | Files saved; hashes and time written on the custody form |
| 2. Disable the shared mailbox sign-in; remove the forwarding rule; revoke all sessions; reset the password; block legacy sign-in for the whole commercial suite | MSP | Sign-in log shows no further attacker activity |
| 3. Block the attacker's forwarding address and sign-in IP addresses | MSP | Blocks confirmed |
| 4. Check the other 5 commercial suite accounts and the 6 SYS-01 accounts for the same IP addresses, new rules, or new MFA methods | MSP | List of accounts checked, with results |
| 5. Call the President. Start the 72-hour clock in the incident log | Office Manager | Discovery time agreed and written down |
| 6. Call the insurer hotline; counsel and forensics assigned | President | Claim number issued |

## 4. Analysis (RS.AN)
Led by the panel forensic firm through counsel, with the MSP supplying access and logs.
1. **Review for compromise of covered defense information** (252.204-7012(c)(1)(i)): which accounts, devices, and data were affected, and whether the attacker reached anything else (SYS-01, the laptops, the RMM tool).
2. **Exact list of what left:** from the message trace, every message forwarded, with date, sender, attachment names, and sizes. The commercial suite's default log retention limits how far back this goes (P01 R-022), which is why step 3.1 comes first.
3. **What the files are:** the CNC Programmer maps each attachment to its part number, revision, and customer. The President marks each as CUI, ITAR, or EAR controlled and records the customer's distribution statement.
4. **Where it went:** the forwarding destination and attacker IP addresses, including any sign of a foreign destination. This feeds the export control decision and the law enforcement report.
5. **How they got in:** password spraying or reuse against a mailbox without MFA, through legacy sign-in. Confirm no malware on company computers (MSP antivirus and forensic review of the Office Manager's laptop, which opens the orders mailbox).
6. **Malware:** this attack usually leaves nothing on company computers. If anything malicious is found, quarantine it, do not delete it (section 6).

## 5. Containment and eradication (RS.MI)
1. Confirm every attacker session is revoked and no other mailbox has a forwarding rule.
2. Retire the shared mailbox. Ask Supplier B, in writing, to send drawings only to the SYS-01 address, and confirm it did so.
3. Move any CUI still in the commercial suite into SYS-01 and delete it from the commercial suite, **after** the evidence export is complete and counsel agrees.
4. Turn on MFA and block legacy sign-in for every commercial suite account, and set alerts for new forwarding rules.
5. Do not delete, rotate out, or overwrite any log or image covered by the preservation rule.

**Preservation (252.204-7012(e)).** Keep images of any affected computer and all relevant monitoring data (mailbox audit logs, message trace, sign-in logs, firewall logs) for **at least 90 days from submission of the DIBNet report**, so DoD can ask for them or decline. The Office Manager is the evidence custodian. If the CUI suite was touched, ask its provider to preserve its own logs; it must also meet paragraphs (c) to (g) (252.204-7012(b)(2)(ii)(D)).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews each external notice. The DoD report is not delayed for counsel review.

| When | Action | Owner |
|---|---|---|
| Hour 0 | Discovery time recorded; clock started | Office Manager |
| Hour 0-4 | Insurer notified; counsel and forensics engaged | President |
| **Within 72 hours of discovery** | **DIBNet report** with the elements required on DIBNet, from a clean laptop with the medium assurance certificate. Report what is known; mark unknowns; update later | President (Office Manager backup) |
| As soon as practicable after the report | Give the DoD-assigned **incident report number** to Supplier B (the next higher-tier subcontractor whose CUI was taken), and to Prime A if any of its CUI is involved (252.204-7012(m)(2)(ii)) | President |
| When malware is isolated | Submit to **DC3** as DC3 or the Contracting Officer instructs; never to the Contracting Officer (252.204-7012(d)) | Office Manager with the MSP |
| On request | DoD access to information or equipment; damage assessment information (252.204-7012(f), (g)) | President |
| Day 1-5 | Voluntary report to the FBI (IC3) or CISA | President |
| After analysis | Export decision: did an unauthorized export or release occur? If yes, DDTC voluntary disclosure (initial notice immediately after discovery; full disclosure within 60 calendar days, 22 CFR 127.12(c)) and, for EAR items, BIS voluntary self-disclosure (15 CFR 764.5). Record the reasoning either way | President (Empowered Official) with export counsel |
| Day 0-2 | Staff briefing: what happened, phishing reminder, no discussion outside the company | President |
| Only if employee personal information is involved | Florida notice within 30 days after determination (Fla. Stat. 501.171) | Office Manager with counsel |

**Plan to the 72-hour clock.** It is the shortest clock in the matrix, and today the company cannot meet it because it has no certificate. Until POAM-008 closes, the President's fallback is to tell Supplier B and Prime A within 72 hours by phone and in writing that a reportable incident occurred and that the DIBNet report will follow as soon as the certificate is issued, with counsel's advice. That fallback does not satisfy the clause; it limits the damage.

**Extortion.** If the attacker demands payment not to publish the drawings, no payment may be made without the President, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not change any reporting duty.

## 7. Recovery (RC.RP, RC.CO)
Exfiltration rarely takes systems down, so recovery is mostly about trust and about the boundary. Restore or confirm in BIA priority order (P05):
1. DoD reporting capability (clean laptop, certificate, printed contacts)
2. Shop network and firewall: attacker IP addresses blocked
3. CNC machines and the CMM: confirm the attacker could not reach them (they are not reachable from the commercial suite)
4. Quality PC and CAM workstation: MSP antivirus and forensic check clean
5. CUI suite: no attacker sign-ins; sharing settings and alerts confirmed
6. Commercial suite and ERP: MFA everywhere, legacy sign-in off, no CUI left
7. Payroll and accounting: no change unless personal information was involved

**Validate before closing:** 14 days with no attacker activity, alerts in place, the evidence set complete, and Supplier B confirmed sending to SYS-01 only. Tell Supplier B and Prime A when containment is complete (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of containment, with the MSP and counsel; written summary within 30 days (POL-03 4.11).
- Update the risk register (P01, especially R-001, R-006, R-022), the POA&M (P07), the SSP boundary (P02), training content (AT-2), and this runbook.
- Recalculate the SPRS score if any control changed, and tell the President before any affirmation (POL-02 A.6).
- Keep the incident log, custody forms, DIBNet report, and decisions for at least 6 years (POL-02 A.8), and the 252.204-7012(e) evidence for at least 90 days from the report, or longer if DoD asks.

# Incident Response Runbook: Ticketing and POS Account Takeover Exposing Customer Device Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company (electronics and device repair service) |
| Tier / Vertical | Sole Proprietorship / Other Services (except Public Administration) |
| Incident type | Someone signs in to the ticketing and POS platform (SYS-01) with the owner's credentials, exports customer records and ticket notes that hold device passcodes, account passwords, and possibly card numbers, and texts customers fake "pay now" links. This is the point-of-sale compromise and customer device data exposure scenario for a one-person shop |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner-technician, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the security consultant due 2026-09-30 (P01 R-012) |

Keep a printed copy at the counter and at home. Assume the SYS-01 account and anything it can reach are in the attacker's hands: **work from the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Independent security consultant | Help lock accounts, export logs, check the laptop, tablet, and bench PC | Hour 0 |
| Ticketing and POS vendor support | Lock the account, end all sessions, confirm what was exported and when, keep logs past 90 days | Hour 0-1 |
| Breach counsel (Florida privacy attorney) | Breach determination, notices, law enforcement contact, any extortion demand | Hours 0-4 |
| Payment processor | **Within 24 hours of suspecting card data exposure** (merchant agreement). Card numbers were in ticket notes until the purge | Hours 0-24 |
| Cyber insurer, **if any** | No standalone cyber policy. Ask the general liability carrier whether a cyber endorsement applies *before* hiring any outside firm | Hours 0-4 |
| Fill-in technician | Ask whether they received a suspicious message or entered the password anywhere; tell them the password changed | Hours 1-4 |
| FBI (IC3 online report) | Report the account takeover and the fraud texts; supports the Florida (4)(c) consultation | Day 1 |
| Customers who report a text | Tell them not to pay or click; the shop never asks for payment by link | As calls come in |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: a customer calls about a payment text or link the shop did not send; SYS-01 shows a sign-in from an unknown device or place, or a customer list export the owner did not run; the owner is locked out of SYS-01; a sign-in alert arrives on the phone that the owner did not cause; the processor or the vendor reports suspicious activity. **Write down the date and time.** Florida's 30-day clocks run from "the determination of the breach or reason to believe a breach occurred" (Fla. Stat. 501.171(3)(a) and (4)(a)); the processor's 24-hour clock runs from suspicion.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. From the phone, change the SYS-01 password, turn on MFA, and end every session. If locked out, call vendor support to lock the account | Only the owner's phone is signed in |
| 2. In SYS-01, turn off outgoing texts until the scope is known; check whether the attacker changed the shop's text templates or user list, or turned on payment links (the shop does not use them) | Templates and settings verified |
| 3. Export the SYS-01 activity log (90 days) and the email sign-in history **before they roll over**; screenshot the export records | Logs saved to the productivity suite |
| 4. Change the email password and confirm MFA; delete any forwarding rules the owner did not create | Email clean |
| 5. Call the consultant, the vendor, then counsel | All three engaged |
| 6. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What was exported?** From the vendor and the activity log: which export (full customer list, ticket notes, invoices), when, and from where. The answer sets the number of affected customers.
2. **What was in the notes?** Use the note search from P03 (passcodes, account passwords, card numbers). Count customers by state of residence from their addresses. Until the purge is complete (POAM-003), assume about 3,100 passcodes, 85 account passwords, and up to 4 card numbers.
3. **Card data.** If any exported note held a card number, call the processor now (24-hour term) and follow its instructions. Do not attempt your own card investigation.
4. **How did they get in?** Check the owner's and the fill-in technician's recent emails and texts for a fake sign-in page; check whether the password was reused anywhere. The consultant checks the laptop and tablet for malware.
5. **Devices in custody.** Customers whose passcodes were exposed still have devices in the shop or at home. For devices still in the shop, tell customers at pickup to change the passcode. Do not change customers' passcodes or sign in to their accounts on their behalf.
6. **Preserve evidence.** Keep the exported logs, screenshots, the fraud text samples customers forward, and the paper log, with a note of who saved what and when.

## 5. Hours 8-24: keep the shop running and prepare notices (RS.CO, RC.RP)
- **Shop:** keep repairing and releasing devices. If SYS-01 is still locked, use numbered paper intake forms and the printed custody list (P05). Take payment only on the P2PE terminal.
- **Warn customers now** (counsel approves the text): "We did not send any payment link. Do not click or pay. We will contact you directly." Post the same notice on the website. This is a safety message, not the breach notice.
- **Breach assessment with counsel:** which records count as personal information under Fla. Stat. 501.171(1)(g) (an email address with an account password clearly does; a card number with a required code does), whether a written no-harm determination under (4)(c) is possible for any group, and which other states' laws apply.
- **Account passwords:** customers whose email and account passwords were in notes are told first and individually, because their accounts are at direct risk.
- **Extortion:** no payment without counsel's advice and an OFAC sanctions check. Paying does not remove notice duties.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of suspicion | Payment processor (merchant agreement) | Any card number may have been exposed |
| Within 30 days of determination | Each affected Florida resident (mail or email) | Personal information of Florida residents accessed |
| Within 30 days of determination | Florida Department of Legal Affairs (no extension for this notice) | 500 or more Florida residents affected |
| Without unreasonable delay | Nationwide consumer reporting agencies | More than 1,000 individuals notified at one time |
| Per each state's law | Residents of other states, and their regulators where required | Out-of-state customers affected (about 12% of records) |

**Plan to the shortest clock.** The processor's 24 hours comes first; Florida's 30 days runs from determination, so the date in the log matters.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, internet, the terminal, SYS-01 with MFA and named accounts only, the tablet, the bench PC, then email and the website. Before reopening SYS-01 texts, confirm the templates are the shop's own and payment links are still off. Close the incident when notices are sent, logs are saved, and the cause is fixed. Within 30 days of closing it, record lessons learned, update P01 (R-001, R-012), P07, and this runbook, and keep all incident records for at least 5 years (POL-01 8.9).

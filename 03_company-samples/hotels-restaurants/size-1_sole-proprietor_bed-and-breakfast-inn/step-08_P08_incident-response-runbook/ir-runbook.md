# Incident Response Runbook: Reservation System and OTA Account Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company (six-room bed-and-breakfast inn) |
| Tier / Vertical | Sole Proprietorship / Accommodation and Food Services |
| Incident type | The inn's version of a point-of-sale and reservation system compromise: a phishing email dressed as an OTA guest complaint installs an information stealer on the laptop. Passwords saved in the browser let the attacker sign in to the innkeeping software, OTA-2, and email, send upcoming guests fake "payment verification" links, view virtual card numbers and door codes, and read the card forms and ID photos in email |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner-innkeeper, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-09-30 (POAM-009) |

Keep a printed copy in the office and in the owner's apartment. Assume the laptop, the innkeeping account, and email are in the attacker's hands: **use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| On-call IT consultant | Isolate the laptop, preserve evidence, check the phone and router | Hour 0 |
| Payment facilitator risk line | **Contract: within 24 hours of suspicion.** Freeze payouts if needed; coordinate card brand reporting | Hours 0-4 |
| Innkeeping software vendor support | End all sessions; pull the activity log; check exports, messages sent, and card displays; pause guest messaging templates | Hours 0-2 |
| OTA-2 (and OTA-1) partner support | Lock the partner account; warn affected OTA guests through the OTA | Hours 0-2 |
| Breach counsel | Breach determination, Florida and other-state notices, guest messages | Hours 0-8 |
| Insurer, **if any** | No standalone cyber policy. Ask whether the business owner's policy has a data breach endorsement *before* hiring outside firms | Hours 0-8 |
| Email provider account recovery | Lock out the attacker; check forwarding rules and sessions | Hours 0-2 |
| Relief innkeeper | Run check-ins and breakfast while the owner handles the incident | As needed |
| U.S. Secret Service or FBI (IC3 online report) | Report the fraud against guests; supports any later law enforcement delay | Day 1 |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: a guest asks about a "payment verification" or "card declined, re-enter details" message; the innkeeping software, an OTA, or email reports a sign-in the owner did not make; guest messages appear in the sent history that the owner did not write; the facilitator or a card brand reports fraud linked to the inn. **Write down the date and time.** It starts the facilitator's 24-hour clock and Visa's 3-calendar-day clock (on reasonable suspicion, not confirmation). Florida's 30-day clock runs from determination of the breach or reason to believe a breach occurred (Fla. Stat. 501.171(4)).

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** and do not sign in to anything from it | Laptop offline, still on |
| 2. From the phone: change the innkeeping, email, and OTA passwords (new, unique), sign out all sessions, turn on MFA, delete email forwarding rules | Only the owner's phone is signed in |
| 3. **Guest safety:** in the lock app, regenerate door codes for guests in house and all upcoming reservations, change the master code, and check the lock app user list | New codes sent by phone call or text from the owner's phone |
| 4. Call the payment facilitator risk line and record the case number | Case number in the log |
| 5. Message every guest with an upcoming stay, from the phone and through OTA-1 and OTA-2: **the inn never asks for card details by message; ignore any such request** | Warning sent |
| 6. Call the IT consultant, then counsel. Start the paper incident log: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Innkeeping software.** Ask the vendor for the activity log for the past 60 days: sign-ins by place and device, full card number displays, profile exports, messages sent, door code views. This tells whether card data was displayed (card brand rows apply) and which guests were messaged.
2. **Email and photo backup.** Search for card forms (about 85 emails before the purge; check whether the purge had happened) and ID photos. Export the email provider's sign-in history before it rolls over.
3. **OTA portals.** Ask both OTAs which reservations and virtual cards were viewed, and which guests received messages.
4. **Laptop and phone.** The consultant images the laptop disk (chain-of-custody note: who, when, where stored) and checks the phone and router for the same malware or changes. Keep owner devices on the phone hotspot.
5. **Payments.** In the facilitator portal, check for refunds or payout changes the owner did not make.

## 5. Hours 8-24: keep the inn running and prepare notices (RS.CO, RC.RP)
- **Guests in house:** new door codes are working; the relief innkeeper or owner is on site; the mechanical override keys stay in the lockbox.
- **Reservations:** the innkeeping software is reachable from the phone. If it must stay locked for the vendor's review, close availability in both OTAs and use the printed 14-day arrivals list (P05 BP-01).
- **Laptop:** do not clean and reuse it. The consultant reinstalls it from clean media with encryption on and no saved passwords, after evidence is saved.
- **Breach assessment with counsel:** which Florida residents' names were accessed with ID numbers (ID photos), or with card numbers and security codes (card forms)? Count affected people and their states of residence; this sets which rows of `notification-matrix.csv` apply. With about 1,900 ID photos, more than 500 Floridians and more than 1,000 notices are likely if the photo backup was reached.
- **Card brands:** the facilitator tells the owner what Visa and the other brands need. If card numbers were displayed or emailed forms were read, at-risk account numbers go to Visa through the facilitator within 3 calendar days.
- **Extortion:** nothing is paid without counsel's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of suspicion | Payment facilitator (contract) | Any suspected card data or payment account compromise |
| Within 3 calendar days of suspicion | Visa, through the facilitator; other brands as the facilitator directs | Visa account data possibly accessed |
| Within 30 days of determination | Florida individual notices; Department of Legal Affairs if 500+ Floridians (the 15-day good-cause extension applies only to individual notices) | Florida residents' personal information accessed |
| Without unreasonable delay | Consumer reporting agencies | More than 1,000 notified at one time |
| Per each state | Notices to guests who live in other states | Non-Florida residents affected |

**Plan to the shortest clock.** The facilitator's 24 hours and Visa's 3 days end long before Florida's 30 days. Card brand reporting and legal notice run in parallel; neither replaces the other.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, room access for guests, internet, innkeeping access with MFA, a clean laptop, payments, then email and accounting. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-004, R-005), P07, and this runbook, and keep all incident records for 5 years (POL-01 8.6; a Florida no-harm determination must be kept at least 5 years, 501.171(4)(c)).

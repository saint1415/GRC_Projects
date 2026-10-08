# Incident Response Runbook: Ransomware and Takeover of the Irrigation Control Account

| Field | Value |
|---|---|
| Organization | Cris Santos Company (precision-agriculture crop farm) |
| Tier / Vertical | Sole Proprietorship / Agriculture, Forestry, Fishing and Hunting |
| Incident type | Ransomware on farm-management and irrigation control systems, adapted to this size: ransomware on the farm laptop, and takeover of the SYS-01 irrigation control account and the booking platform with passwords stolen from the laptop browser. The SaaS platforms themselves are not encrypted. Worst case: a freeze night in January |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours; SP 800-82 Rev. 3 sections 6.4 and 6.5 for the irrigation steps |
| Policy basis | POL-01 sections 10 and 11 |
| Owner and approver | Owner-operator, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT technician and the mutual-aid neighbor due 2026-11-30 (POAM-007 contacts by 2026-09-30) |

Keep a printed copy in the home office and inside the pump house. Assume the laptop and every password saved in it are in the attacker's hands: **use the phone, this paper copy, and the switches in the pump house.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Mutual-aid neighbor | Start or watch freeze protection if the owner is tied up | Hour 0 on a freeze night |
| On-call IT technician | Isolate the laptop, preserve evidence, check the phone, tablet, and router | Hour 0 |
| FMIS vendor support | Lock the account, end all sessions, pull the activity log, confirm records are intact or restore them | Hours 0-2 |
| Irrigation dealer | Verify pump, pivot, fertigation, and alarm settings; change the controller password | Hours 1-8 |
| Booking platform vendor | Lock the admin account; report exports, site changes, refunds | Hours 1-4 |
| Bank | Watch for payee changes and unusual payments | Hours 1-4 |
| Breach counsel (privacy attorney) | Breach determination, Florida notices, ransom questions | Hours 2-8, if personal information may be involved |
| Farm liability insurer | No cyber policy today (EV-018, EV-028; whether the farm liability policy covers cyber events is an open intake request). Ask whether any cyber coverage applies before hiring outside help | Hours 2-8 |
| FBI (IC3 online report) | Voluntary report; supports OFAC mitigation | Day 1 |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: a ransom note or renamed files on the laptop; the antivirus reports ransomware; SYS-01 shows an irrigation command, schedule, or alarm change the owner did not make; a pump or the pivot starts or stops unexpectedly; the owner cannot sign in to SYS-01 or the booking platform; a vendor warns of a new sign-in. **Write down the date and time.** Florida's 30-day clock runs from the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI): crop first
| Step | Done when |
|---|---|
| 1. **Crop first.** If a freeze is forecast or irrigation is running, go to the pump house: switch the pump controller to local and run it by Hand; start the freeze zone by hand if the field thermometer is near the critical temperature. Call the neighbor if you need someone at the pump house while you do the next steps. If remote commands may have reached the River Field pivot, switch its panel to local at the next safe moment (SP 800-82r3 6.4.4) | Pump in local; freeze zone running if needed |
| 2. Turn off Wi-Fi on the laptop. **Do not power it off** (memory may hold evidence). Do not pay or reply to the attacker | Laptop offline, still on |
| 3. From the phone, reset the SYS-01 password, sign out all sessions, turn on MFA, and set the dealer's account to viewer | Only the owner's phone is signed in |
| 4. From the phone, reset the booking, email, and bank passwords and turn on MFA where it is off; call the bank | Accounts secured |
| 5. Call the IT technician. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What did the attacker do in SYS-01?** Ask the vendor for the activity log and export it before it rolls over. List every command, setting change, user change, and deleted record.
2. **Are the pump and pivot settings right?** With the dealer, compare schedules, setpoints, fertigation rates, and alarm thresholds against the device list (POL-01 Appendix A). Restore the correct values and record each change in the change log (POL-01 7.8). Keep the equipment in local mode until this is done.
3. **Food safety check.** If the fertigation rate or injector was changed, close the affected U-pick block and stop sales from it until the owner confirms what was applied. This is a farm safety decision, not a legal notice (the farm registers no food facility).
4. **What was on the laptop?** With the technician, list what was stored or synced: W-9 scans, the customer export spreadsheet, program documents, saved passwords. This decides who is affected.
5. **What happened in the booking platform?** Ask the vendor whether the admin account exported customers, changed the site, or issued refunds, and whether customer passwords were exposed.
6. **Other devices.** The technician checks the phone, tablet, and router (change the router admin password; confirm the customer Wi-Fi is isolated).
7. **Preserve evidence.** The technician images the laptop disk and saves logs with a chain-of-custody note (who, when, where stored). No wiping until counsel agrees, if personal information is involved.

## 5. Hours 8-24: keep farming and prepare notices (RS.CO, RC.RP)
- **Irrigation:** stays in local and Hand until settings are verified and MFA is on. On a freeze night the owner or the neighbor stays with the pump; the standalone freeze alarm is the backup.
- **Sales:** if the booking site is down or changed, post a notice on the farm's social page, take walk-ins, and use the card reader on a clean phone.
- **Laptop:** do not decrypt and reuse it. The technician reinstalls it from clean media, with separate user accounts, after evidence is saved.
- **Records:** if SYS-01 records were deleted, ask the vendor to restore from its backups (RPO 1 hour); use the latest monthly export for anything else (POL-01 8.4).
- **Breach determination (with counsel):** were names with Social Security numbers (W-9s) or customer credentials accessed? If yes, count affected people and their states. That sets which rows of `notification-matrix.csv` apply.
- **Ransom:** not paid without counsel's advice and an OFAC sanctions check. Paying does not remove notice duties if data was taken.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 30 days of determination | Each affected Florida individual (mail or email) | W-9 data or customer credentials accessed |
| Within 30 days of determination | Florida Department of Legal Affairs | 500 or more Floridians affected (only possible through the booking accounts) |
| Without unreasonable delay | Nationwide consumer reporting agencies | More than 1,000 notified at once |
| Within 10 days of the vendor's determination (inbound) | Booking or accounting vendor tells the farm | A breach at the vendor |
| Within 10 calendar days | FAA safety event report | Only if a drone operation caused serious injury or more than $500 damage |
| On FDA request (24 hours if kept offsite) | Qualified exemption records | Any time, including during the outage |

**Most likely outcome:** a small breach notice (the 2 individuals with W-9 data) and a large operational problem (the irrigation account). Plan the notice anyway; the 30-day clock runs while the farm is recovering.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: manual irrigation, owner access and phone, internet, a clean device, SYS-01, booking and card reader, then email, files, and accounting. Recovery ends when SYS-01 settings are verified, MFA is on everywhere, the laptop is rebuilt, and any notices are sent. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-005), P07, and this runbook, and keep the incident records for at least 5 years (the Florida no-harm determination must be kept that long).

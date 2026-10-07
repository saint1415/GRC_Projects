# Incident Response Runbook: Ransomware on the Office Laptop and Takeover of Email

| Field | Value |
|---|---|
| Organization | Cris Santos Company (unarmed private security patrol, licensed Class "B" agency) |
| Tier / Vertical | Sole Proprietorship / Emergency Services |
| Incident type | Ransomware on the home office laptop encrypts the synced cloud drive, including the client code spreadsheet, while the attacker takes over the email account and tries the patrol app admin console. This is the one-person version of a dispatch outage: the business loses its codes and its client channel at night, and alarm response stops unless the owner works from the phone and the sealed code book |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 sections 10 and 11 |
| Owner and approver | Owner, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-09-30 (POAM-009) |

Keep one printed copy in the home safe and one in the vehicle. Assume the laptop, the email account, and anything synced to it are in the attacker's hands: **use the phone, the patrol app, and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Each client whose codes or keys may be exposed | Contract: notice within 2 hours of a code that may be compromised. Recommend changing alarm and gate codes | Hours 0-2 |
| Backup patrol agency | Cover tonight's patrols if the owner is tied up (verbal arrangement until the written agreement is signed) | Hours 0-2 |
| On-call IT technician | Isolate the laptop, preserve evidence, check the phone and router | Hour 0-1 |
| Breach counsel (Florida data privacy attorney) | Breach determination under Fla. Stat. 501.171, notices, ransom questions, Chapter 493 exposure | Hours 0-8 |
| Insurance agent | Ask whether the liability policy covers any of this **before** hiring outside help; no cyber policy exists | Hours 0-8 |
| Patrol app vendor support | Revoke all admin sessions; pull the admin sign-in and export log; confirm no client data was exported | Hours 1-4 |
| Email provider account recovery | Lock out the attacker; remove forwarding rules and unknown devices | Hours 0-2 |
| Mobile carrier | Put a port-out and SIM change lock on the number (email used text codes) | Hours 0-2 |
| Alarm monitoring companies (4 clients) | Confirm the owner is still reachable as responder, or give the backup agency's number | Hours 0-4 |
| FBI (IC3 online report) | Voluntary report; supports OFAC mitigation if payment is ever considered | Day 1 |

Contact numbers are kept on the printed copies only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: a ransom note or renamed files on the laptop; the antivirus reports ransomware; the email provider or patrol app alerts on a sign-in the owner did not make; a client reports an odd email or invoice from the business; the code spreadsheet will not open. **Write down the date and time.** Two clocks start here: the **2-hour client clause** runs from discovery, and Florida's **30-day clock** runs from determination of a breach or reason to believe a breach occurred (Fla. Stat. 501.171(4)(a)). If the owner is on patrol, finish making the current site safe first, then start section 3 from the vehicle.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** (memory may hold evidence). Do not reply to or pay the attacker | Laptop offline, still on |
| 2. From the phone, sign in to the patrol app, change the admin password from the password manager, turn on MFA if still off, and sign out all other sessions | Only the phone is signed in |
| 3. From the phone, recover the email account: new password, sign out everywhere, authenticator MFA, delete forwarding rules | Only the phone is signed in |
| 4. Open the sealed code book from the safe (or read the vault on the phone). **Answer alarms from it tonight**; do not use the spreadsheet | Codes available without the laptop |
| 5. Call each client whose codes were in the spreadsheet or post orders. Recommend code changes; log each call with the time | All calls made within 2 hours |
| 6. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What was exposed?** With the IT technician, list what was in the synced drive (code spreadsheet, contracts, report exports, video clips) and in email. Note which files hold driver license numbers or injury notes; that list decides who is an affected individual under 501.171(1)(g).
2. **Patrol app check.** Ask the vendor for 30 days of admin sign-ins and exports. If an unknown session read post orders or reports, every client and every person named in those reports is in scope.
3. **Phone and router.** The technician checks the phone and router. Work from the phone hotspot until the router is checked. Turn on the carrier SIM lock.
4. **Preserve evidence.** The technician images the laptop disk and saves the email, patrol app, and router logs, with a chain-of-custody note (who, when, where stored). No wiping until counsel agrees.
5. **Keys.** Confirm every key and card against the key log. Keys are not affected by ransomware, but the code key for the tags may have been in the drive.

## 5. Hours 8-24: keep patrolling and prepare notices (RS.CO, RC.RP)
- **Patrols tonight:** the patrol app works on the phone, the code book is in hand, and the keys are in the lockbox. If the owner cannot patrol, the backup agency covers and each client is told who is coming.
- **Laptop:** do not decrypt and reuse. The technician reinstalls it from clean media after evidence is saved, with separate business and family accounts, and files are restored from the versioned backup (once in place, POAM-005).
- **Breach determination:** counsel and the owner decide whether personal information was accessed. Encrypted data is not personal information under 501.171(1)(g)2. If no identity theft or financial harm is likely after investigation and consultation with law enforcement, the written determination goes to the Department of Legal Affairs within 30 days and is kept 5 years (501.171(4)(c)).
- **Count affected individuals and where they live.** This sets which rows of `notification-matrix.csv` apply.
- **Licensing:** a release of client information can be grounds for discipline under Fla. Stat. 493.6118(1)(e). Counsel advises on communications; keep all records producible, because the department can ask for them "immediately" (493.6121(2)). If a client makes an insurance claim, notify the department (493.6110(1)).
- **Ransom:** not paid without counsel's advice and an OFAC sanctions check. Paying does not remove notice duties if data was taken.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 2 hours of discovery | Clients whose codes or keys may be exposed | Codes or keys possibly exposed |
| Within 24 hours of discovery | Clients whose other information was affected | Reports, post orders, or video affected |
| Within 10 days of the vendor's determination | Vendor to owner (inbound) | A vendor's systems were breached |
| Within 30 days of determination | Florida individuals; Department of Legal Affairs if 500 or more; no-harm determination if used | Personal information of Florida residents accessed |

**Plan to the shortest clock.** The contracts' 2-hour clause comes due long before any statute.

## 7. After day 1 (RC.RP, RC.CO, ID.IM)
Restore in P05 order: phone and patrol app, codes and keys, reports, records, then the laptop. Send each affected client a short written update when patrols are back to normal and again when the incident closes. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-003), P07, and this runbook, and keep all incident records for 5 years (POL-01 8.8).

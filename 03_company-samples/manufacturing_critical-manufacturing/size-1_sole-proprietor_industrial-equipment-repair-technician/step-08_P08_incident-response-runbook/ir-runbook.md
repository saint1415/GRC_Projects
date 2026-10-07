# Incident Response Runbook: Ransomware on the Service Laptop During a Breakdown Call

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated industrial equipment repair service) |
| Tier / Vertical | Sole Proprietorship / Critical Manufacturing |
| Incident type | Ransomware on the service laptop encrypts the local and synced Customer Machine Library during a breakdown call, so a Customer A coil winding line (distribution transformer production) stays down until its program can be reloaded, with a risk that the infection reaches plant equipment through the laptop or a USB stick. Adapted from the registry default "Ransomware disrupting production of grid equipment": the business has no production of its own, so the disruption is to the customer's grid-equipment line |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 sections 10 and 11 |
| Owner and approver | Owner-technician, 2026-09-11 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-10-31 (POAM-008) |

Keep a printed copy in the van and at home. Assume the laptop, the synced library, and possibly the email account are in the attacker's hands: **use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Customer A plant controls engineer | Stop the laptop and sticks touching plant equipment; agree how to get the line back; this call starts the exhibit S4 coordination | Hour 0, by phone |
| On-call IT consultant (NDA) | Isolate the laptop, preserve evidence, check the phone and sticks, provide a clean loaner laptop | Hour 0 |
| Productivity suite provider support | Sign out sessions; help restore files to their pre-encryption versions; confirm the account is clean | Hours 1-2 |
| Attorney (business counsel) | Contract notices, any claim from a customer, ransom questions | Hours 0-4 |
| Customer B and Customer C contacts | NDA notice if their programs or passwords were on the laptop or a stick | Within 24 hours |
| Seven local plants | Courtesy notice if their programs or passwords were exposed | Same day |
| Referral technician (once the arrangement exists) | Cover other breakdown calls while the owner is tied up (P05) | As needed |
| FBI (IC3 online report) and CISA | Voluntary reports; agree timing with Customer A | Day 1 |
| General liability carrier | Only if a customer claims damage; no cyber policy today (exhibit S8 requires one from 2027-09-30) | When a claim is raised |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a ransomware incident when any of these happens (POL-01 10.2): a ransom note or renamed, unreadable files on the laptop; the antivirus reports ransomware; the suite warns of mass file changes or a sign-in the owner did not make; a customer's machine behaves oddly right after the owner connected. **Write down the date and time.** That time starts the **24-hour clock for the Customer A notice** (exhibit S4). Notice is required when the incident affects or could affect Customer A's systems or information, or a device used on its equipment, which the service laptop always is.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. **Unplug the laptop from the machine network and any USB stick. Do not connect anything else to plant equipment.** Turn off Wi-Fi and unplug any cable. Do not power the laptop off (memory may hold evidence) and do not pay or reply to the attacker | Laptop offline, still on; nothing of the owner's connected to a customer machine |
| 2. Tell the Customer A plant controls engineer by phone what happened and which machines the laptop or sticks touched today | Customer A informed verbally; time noted |
| 3. From the phone, sign out all suite sessions, change the suite and accounting passwords, and check for new forwarding rules. Do not delete encrypted files in cloud storage: version history is the way back | Only the owner's phone signed in |
| 4. Bag and label every USB stick that was in the van; none is used again until scanned on a clean machine | Sticks quarantined |
| 5. Call the IT consultant, then the attorney. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: get the customer's line back safely (RS.AN, RS.MI, RC.RP)
1. **What did the laptop touch?** List every machine the laptop or a stick connected to since the last clean scan. Customer A decides with the owner whether those controllers need checking before production resumes.
2. **Get a clean program for the stopped machine, in this order:** Customer A's own copy (the customer-held copy once 7.5 is in place); the offline backup drive (once POAM-003 is done); the pre-encryption version from cloud version history, restored on a clean device. Never take a file from the infected laptop.
3. **Check it before loading.** Compare the file's hash with the library index (once complete) or with Customer A's record. Load it through Customer A's own engineering workstation or a clean loaner laptop, after the plant's media scanning station (exhibit S3). After loading, compare the controller program with the clean copy (POL-01 7.7).
4. **Preserve evidence.** The IT consultant images the laptop disk and saves the antivirus and suite logs, with a chain-of-custody note. No wiping until the attorney agrees.
5. **Other customers.** Note which other customers' programs and passwords were on the laptop and sticks. Start password changes with each customer for any password in the spreadsheet (until it is replaced by the password manager, POAM-007).

## 5. Hours 8-24: notices and the next day (RS.CO)
- **Written notice to Customer A within 24 hours** of discovery, with what is known: time found, machines touched, data that may be exposed, actions taken, next update time. Keep coordinating until Customer A agrees the incident is closed.
- **Customers B and C:** prompt written notice if their information may be exposed (NDAs). **Local plants:** courtesy notice the same day.
- **Utility work:** if the laptop or sticks were used on substation cabinets since the last clean scan, tell Customer A which cabinets, so it can coordinate with the utility. The utility decides its own regulatory reporting; the owner does not report to NERC or DOE.
- **Ransom:** not paid without the attorney's advice and an OFAC sanctions check. A payment would not make the library trustworthy again; every restored program still needs its integrity check.
- **Personal information:** confirm with the attorney that no personal information as defined in Fla. Stat. 501.171 was involved (see the matrix). If it was, plan to the 30-day clock.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of discovery | Customer A (exhibit S4; flows down CIP-013-2 R1.2.1 and R1.2.2) | Always, for this scenario |
| Same day | Customer A, if a firmware hash does not match (exhibit S5) | Hash mismatch |
| Prompt (target 24 hours) | Customers B and C (NDAs) | Their information may be exposed |
| Within 30 days of determination | Florida individual notice (Fla. Stat. 501.171) | Only if personal information of Florida residents was breached |
| Voluntary | CISA; FBI (IC3) | Recommended |
| Not applicable | CIRCIA (proposed), DFARS 252.204-7012, FAR 52.204-23 and -25 | See the matrix for why |

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, a clean laptop with the engineering software, the library (from customer-held copies and the offline backup, each checked against its hash), the field kit with new sticks, email and files, accounting, then the vibration analytics app. The infected laptop is rebuilt from clean media to the POL-01 Appendix C baseline only after evidence is saved. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-013), P07, and this runbook, and keep all incident records for at least 3 years (POL-01 8.9).

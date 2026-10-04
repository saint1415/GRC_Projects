# Incident Response Runbook: Ransomware on the Teaching Laptop

| Field | Value |
|---|---|
| Organization | Cris Santos Company (tutoring and educational support service) |
| Tier / Vertical | Sole Proprietorship / Educational Services |
| Incident type | Ransomware on the laptop that encrypts the synced student folders (the encrypted copies sync to cloud storage) and steals student folders and the portal password spreadsheet. The client-management SaaS and the portal are not affected |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner-tutor, 2026-07-31 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-09-30 (P01 R-013) |

Keep a printed copy at home and in the teaching bag. Assume the laptop and the email account are in the attacker's hands: **use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| On-call IT technician | Isolate the laptop, preserve evidence, check the phone and router | Hour 0 |
| Breach counsel (privacy attorney) | Breach determination under Fla. Stat. 501.171, notice wording, ransom questions, recordings and consent | Hours 0-4 |
| Email and files suite vendor support | Lock sessions, stop sync, restore files from version history before the 30-day window closes | Hours 1-4 |
| Website-builder vendor support | Force a password reset for every portal member account; confirm no administrator changes | Hours 1-8 |
| Client-management SaaS vendor support | Confirm no unusual sign-ins; it holds the parent contact list needed for notices | Hours 4-8 |
| FBI (IC3 online report) | Voluntary report; supports OFAC mitigation if payment is ever considered | Day 1 |
| Designated emergency contact (family member) | Only if the owner is unable to act: message families from the sealed emergency sheet | As needed |
| Backup tutor | Urgent SAT and ACT students if sessions stop for more than two days (P05) | Day 2 |

There is **no cyber insurance**: the general liability policy does not cover data breach costs, so counsel and the IT technician are paid directly. Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a ransomware incident when any of these happens: a ransom note or renamed files on the laptop; the antivirus reports ransomware; the email suite shows a mass of changed files; a message claims to have student data; the email suite warns of a sign-in the owner did not make. **Write down the date and time.** Florida's 30-day clock runs from the determination of the breach or reason to believe a breach occurred (Fla. Stat. 501.171(4)(a)), so treat the moment you see a ransom note as the start unless counsel says otherwise.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** (memory may hold evidence) and do not pay or reply to the attacker | Laptop offline, still on |
| 2. From the phone, **pause desktop sync** in the email suite web console (or sign the laptop out of the suite) so no more encrypted files reach cloud storage | Sync stopped |
| 3. From the phone, change the email suite password, sign out all sessions, turn on MFA if still off, and check for new forwarding rules | Only the phone is signed in |
| 4. From the phone, change the website-builder, video platform, and client-management SaaS passwords | All accounts secured |
| 5. Call the IT technician, then counsel | Both engaged |
| 6. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Portal passwords.** The stolen spreadsheet lists every student's portal user name and password. Have the website builder force a reset on all 61 member accounts (34 active and 27 inactive), close the 27 inactive accounts, and email each current family a link to set a new password. Check the builder's activity history for member sign-ins from unknown places.
2. **What was in the student folders?** With the IT technician, list the folders the laptop synced: about 265 students (55 current, about 210 former). Mark which hold evaluations or IEP and 504 plans with diagnosis information (about 39). This list decides who is owed a Florida notice.
3. **Restore.** Ask the email suite vendor to restore the student folders to a version from before the encryption. Version history lasts 30 days, so start this on day 1. If the independent backup is in place (POAM-008), restore from it instead.
4. **Other systems.** Check the client-management SaaS, video platform, and accounting SaaS sign-in histories. If nothing unusual, record that they were not affected. The IT technician checks the phone and the router (admin password, connected devices).
5. **Preserve evidence.** The IT technician images the laptop disk and saves the ransom note, logs, and sign-in histories, with a chain-of-custody note (who, when, where stored). No wiping until counsel agrees.

## 5. Hours 8-24: keep teaching and prepare notices (RS.CO, RC.RP)
- **Sessions:** move the next day's online sessions to in person or to a phone call with printed worksheets, or teach from the IT technician's loaner laptop through the browser (P05). Call any family whose session is affected; the schedule is in the client-management SaaS on the phone.
- **Laptop:** do not decrypt and reuse. The IT technician reinstalls it from clean media, with encryption on, a separate family account, and MFA on every service, after evidence is saved.
- **Breach determination with counsel:** was unencrypted personal information accessed? Stolen evaluations with names and working portal passwords meet the Florida definition. Decide the notice list and date.
- **Count and locate affected people.** This sets which rows of `notification-matrix.csv` apply. Check addresses: former students may now live outside Florida.
- **Ransom:** not paid without counsel's advice and an OFAC sanctions check. Paying does not remove notice duties when data was taken.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Day 1 | Portal password reset for every member account | Always (spreadsheet stolen) |
| Within 30 days of determination | Florida notice to each affected individual (through the parent for minors, as counsel confirms) | Names with evaluation or diagnosis information, or portal passwords, were accessed |
| Within 30 days of determination | Florida Department of Legal Affairs | Only if 500 or more Floridians (not expected: at most about 100) |
| Same time, after counsel review | Voluntary message to all current families | Recommended |
| Within 2 days | FBI IC3 report | Voluntary |

**No federal breach notice applies.** COPPA has no breach notification rule, and FERPA and the GLBA Safeguards Rule do not apply to this business. Because there is no federal notice to substitute, Florida's deemed-compliance path (501.171(4)(g)) is not available.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, the client-management SaaS, a clean teaching device, the video platform, student folders, the portal, then accounting. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-004, R-007), P07, and this runbook, feed them into the annual program evaluation (16 CFR 312.8(b)(5)), and keep all incident records for at least 3 years (POL-01 12.3).

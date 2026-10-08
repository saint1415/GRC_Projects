# Incident Response Runbook: Ransomware on the Practice Laptop

| Field | Value |
|---|---|
| Organization | Cris Santos Company (solo primary care physician practice) |
| Tier / Vertical | Sole Proprietorship / Health Care and Social Assistance |
| Incident type | Ransomware on the laptop, with PHI taken from downloaded files and the email account. The EHR (SaaS) is not affected |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Physician-owner, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-09-30 (POAM-006) |

Keep a printed copy in the suite and at home. Assume the laptop and the email account are in the attacker's hands: **use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| On-call IT consultant (BA) | Isolate the laptop, preserve evidence, check other devices | Hour 0 |
| Breach counsel (health care privacy attorney) | Privilege, breach determination, notices, ransom questions | Hours 0-4 |
| Cyber insurer, **if any** | No standalone cyber policy today (EV-014, EV-029; the endorsement question is an open intake request). Call the professional liability carrier to ask whether a cyber endorsement applies *before* hiring any outside firm | Hours 0-4 |
| EHR vendor support | Revoke laptop sessions; pull the audit log for the account; confirm the EHR is clean | Hours 1-4 |
| Billing company (BA) | Warn of possible fraud using stolen patient and claim data; confirm its systems are clean; watch for fake payment-change requests | Hours 4-8 |
| Email provider account recovery | Lock out the attacker; review forwarding rules and sessions | Hours 1-2 |
| FBI (IC3 online report) | Voluntary report; supports OFAC mitigation if payment is ever considered | Day 1 |
| Covering physician | Urgent patient needs if the owner is tied up (P05) | As needed |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a ransomware incident when any of these happens: a ransom note or renamed files on the laptop; the antivirus reports ransomware; an email or post claims to have practice data; the email provider warns of a new sign-in the owner did not make. **Write down the date and time.** Under 45 CFR 164.404(a)(2), discovery is the first day the breach is known, or by reasonable diligence would have been known, to the owner. Florida's 30-day clock runs from determination of the breach (Fla. Stat. 501.171(4)).

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** (memory may hold evidence) and do not pay or reply to the attacker | Laptop offline, still on |
| 2. From the phone, change the email password, sign out all sessions, turn on MFA if still off, and delete any forwarding rules | Only the owner's phone is signed in |
| 3. From the tablet or phone, change the EHR password and end all other EHR sessions | EHR sessions revoked |
| 4. Call the IT consultant, then counsel | Both engaged |
| 5. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What was on the laptop?** With the consultant, list the downloads (patient lists, visit summaries, lab PDFs) and any synced email folders. This list decides how many patients are affected.
2. **What was in email?** Search sent, received, and stored files for PHI. Export the email provider's sign-in and activity history before it rolls over.
3. **EHR check.** Ask the EHR vendor for the account's access log for the past 30 days. Look for sign-ins from unknown places or bulk exports. If none, record that the EHR was not affected.
4. **Other devices.** The consultant checks the tablet and phone for the same malware. Keep them off the building Wi-Fi; use the phone hotspot.
5. **Preserve evidence.** The consultant images the laptop disk and saves logs, with a chain-of-custody note (who, when, where stored). No wiping until counsel agrees.

## 5. Hours 8-24: keep seeing patients and prepare notices (RS.CO, RC.RP)
- **Clinic:** the EHR is reachable from the tablet over the hotspot. Use the printed schedule and paper notes if needed (P05, BP-01). E-prescribing continues from the EHR.
- **Laptop:** do not decrypt and reuse. The consultant reinstalls it from clean media (encryption on, MFA on every account) after evidence is saved.
- **Breach assessment:** counsel and the owner begin the four-factor risk assessment (45 CFR 164.402): nature and extent of the PHI, who took it, whether it was actually acquired or viewed, and how far the risk was reduced. Unencrypted PHI taken by a criminal is presumed a breach.
- **Count affected patients and their states of residence.** This sets which rows of `notification-matrix.csv` apply.
- **Ransom:** not paid without counsel's advice and an OFAC sanctions check. Paying does not remove notice duties if data was taken.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 30 days of determination | Florida individual notice, or HIPAA notice with a copy to the Department of Legal Affairs (deemed-compliance path); Department notice if 500+ Floridians | Florida residents affected |
| Within 60 days of discovery | HIPAA individual notices; HHS notice at the same time if 500+; media if more than 500 Florida residents | Breach of unsecured PHI |
| Within 60 days after year end | HHS breach log | Fewer than 500 affected |

**Plan to the shorter clock.** Florida's 30 days (from determination) can end before HIPAA's 60 days (from discovery).

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, internet, a clean device, EHR access, cloud fax, billing feed, then email and files. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-004), P07, and this runbook, and keep all incident records for 6 years (POL-01 8.8).

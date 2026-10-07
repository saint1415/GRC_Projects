# Incident Response Runbook: Ransomware on the Dispatch and Back-Office Laptop

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight broker arranging truck and rail shipments) |
| Tier / Vertical | Sole Proprietorship / Transportation Systems |
| Incident type | Ransomware on the owner's laptop, which is the broker's dispatch and back-office workstation, with theft of synced carrier packets. The TMS, email, bank, and railroad portal sessions saved in the laptop's browser are at risk. Adapted from the registry default (ransomware on dispatch and train control back-office systems); see `../00_company-facts.md` section 3 |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 sections 10 and 11 |
| Owner and approver | Owner, 2026-09-08 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-10-31 (POAM-006) |

Keep a printed copy at the home office and in the laptop bag. Assume the laptop and anything signed in on it are in the attacker's hands: **use the phone and this paper copy.** Loads in transit come first: the BIA gives in-transit tracking an MTD of 8 hours (P05 BP-02).

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| On-call IT consultant | Isolate the laptop, preserve evidence, check the phone | Hour 0 |
| Business bank fraud line | Hold the next ACH batch; check for new payees or changed bank details; recall anything suspicious | Hour 0 to 1 |
| Transportation attorney | Breach decision, notices, surety and FMCSA questions, ransom questions | Hours 0 to 4 |
| TMS vendor support | Revoke sessions; pull the audit log; confirm carrier bank details were not changed | Hours 1 to 4 |
| Email and file suite provider | Lock out the attacker; review sign-ins, forwarding rules, and admin accounts | Hours 1 to 2 |
| Drivers and carriers with loads in transit | Keep loads moving; warn them to ignore emailed payment or pickup changes | Hours 1 to 8 |
| Largest shipper | Contract notice within 72 hours of discovery if its data is involved | By hour 72 |
| Railroads (portal administrators) | Report suspected misuse of portal user IDs saved in the browser | Hours 4 to 8 |
| Insurance agent | Confirm whether any policy has a data breach endorsement (no cyber policy today) | Day 1 |
| FBI (IC3 online report) and CISA | Voluntary reports; support bank recovery and OFAC mitigation | Day 1 |
| Backup broker (once the agreement exists) | Follow loads in transit if the owner is tied up | As needed |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a ransomware incident when any of these happens: a ransom note or renamed files on the laptop; the antivirus reports ransomware; files in the cloud folders turn unreadable; a carrier, shipper, or railroad reports emails from the business that the owner did not send; the email suite warns of a new sign-in the owner did not make. **Write down the date and time.** Florida's 30-day clock runs from determination of the breach or reason to believe one occurred (Fla. Stat. 501.171(4)); the largest shipper's 72-hour clock runs from discovery.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** and do not pay or reply to the attacker | Laptop offline, still on |
| 2. From the phone, open the TMS app and save the in-transit list (driver, phone, appointment, consignee), or use the last 7 a.m. or 2 p.m. download | In-transit list in hand |
| 3. Call the bank fraud line: hold the ACH batch; review payees changed in the last 30 days | Payments held |
| 4. From the phone, change the email password, sign out all sessions, remove unknown forwarding rules and admin accounts, and confirm MFA is on | Only the owner's phone signed in |
| 5. Change the TMS password, end other TMS sessions, and open the TMS bank detail change log | TMS sessions revoked |
| 6. Call the IT consultant, then the attorney. Start the paper incident log: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: keep loads moving, scope, and contain (RS.AN, RS.MI)
1. **Loads in transit.** Call or text every driver on the in-transit list from the phone. Confirm the next appointment and tell them to ignore any emailed change to pickup, delivery, or payment. Use the tracking app's web page from the phone if the TMS is slow.
2. **What was on the laptop?** With the consultant, list the synced folders and downloads (carrier packets, shipper contracts, rail shipping instructions). This list decides which carriers, drivers, and shippers are affected.
3. **What was in email and the TMS?** Export the email sign-in and activity history and the TMS audit log before they roll over. Look for bulk downloads, new rules, or changed bank details.
4. **Saved sessions.** Change the passwords for the accounting SaaS, load board, railroad portals, and FMCSA account from the phone. Check the public FMCSA record and the load board profile for changed contact details.
5. **Preserve evidence.** The consultant images the laptop disk and saves logs, with a chain-of-custody note (who, when, where stored). No wiping until the attorney agrees.

## 5. Hours 8-24: keep booking and prepare notices (RS.CO, RC.RP)
- **Operations:** buy a new laptop the same day; the consultant sets it up with encryption and MFA on every account before it signs in to anything. Book new loads only with carriers already in the carrier file until the TMS log is checked.
- **Rail:** ask each rail shipper's traffic staff to confirm the next car orders and shipping instructions in the portal; call the railroad's customer service center if a portal user ID is locked.
- **Breach decision:** the attorney and the owner decide whether personal information was accessed (Social Security numbers, driver license numbers, driver location, each with a name, are personal information under Fla. Stat. 501.171(1)(g)). Data in encrypted form is excluded, but files synced to an unlocked laptop were readable to the attacker.
- **Count affected individuals by state of residence.** This sets which rows of `notification-matrix.csv` apply.
- **Ransom:** not paid without the attorney's advice and an OFAC sanctions check. Paying does not remove notice duties if data was taken.

## 6. Deadlines (from `notification-matrix.csv`)
| Deadline | Notice or action | Applies when |
|---|---|---|
| Within 72 hours of discovery | Largest shipper (contract) | Its data was involved |
| Promptly | Railroads, under the portal terms | Portal credentials may have been exposed |
| Within 7 business days of each notice | Answer any surety claim (49 CFR 387.307(e)(1)(ii)) and any FMCSA suspension notice (387.307(e)(5)-(6)) | Carriers went unpaid and filed bond claims |
| Within 30 days of determination | Florida individual notices; Department notice if 500 or more Floridians; or a written no-harm determination sent to the Department | Florida residents' personal information accessed |
| Within 30 days of a change | Correct the FMCSA registration record (49 U.S.C. 13904(g)) | Contact details changed |
| Varies | Other states' notices | Affected carriers or drivers outside Florida |

**Plan to the shortest clock.** The shipper's 72 hours ends first. **Watch the money:** if the ACH hold lasts past carriers' due dates, call each carrier before it files a bond claim, because an unanswered claim can now lead to suspension of the broker's authority.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, in-transit contact, internet, TMS on the clean laptop, railroad portals, email and files, then accounting and bank. Release the held ACH batch only after every bank detail in it has been confirmed by call-back (POL-01 6.3). Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-003), P07, and this runbook, and keep all incident records at least 5 years (POL-01 8.8).

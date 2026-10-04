# Incident Response Runbook: Ransomware on the Brokerage Laptop

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight forwarder and customs broker) |
| Tier / Vertical | Sole Proprietorship / Transportation and Warehousing |
| Incident type | Ransomware on the owner's laptop that encrypts the synced records archive and steals client files (POAs, invoices, importer of record numbers). The customs software (SaaS) is not encrypted, but saved browser sessions put it, email, and the bank at risk. Adapted from the registry default "ransomware disrupting terminal operating system": the customs software is this business's equivalent of a terminal operating system |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner, 2026-09-14 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-10-31 (POAM-006) |

Keep a printed copy in the home office and in the car. Assume the laptop and the email account are in the attacker's hands: **use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| On-call IT consultant | Isolate the laptop, preserve evidence, check the phone and router | Hour 0 |
| Customs counsel (attorney) | Privilege, breach determination, the CBP and state notices, ransom questions | Hours 0-4 |
| Business bank (fraud line) | Watch for and stop unusual wires; reset online banking; recall any wire sent in the last 72 hours on changed instructions | Hours 0-2 |
| Customs software vendor support | End all sessions; reset credentials; pull the account's sign-in log; confirm entries were not changed | Hours 1-4 |
| Email and file suite provider | End sessions; remove forwarding rules; restore the archive from version history to a clean location | Hours 1-4 |
| Backup licensed broker | File urgent entries and answer CBP holds under its own POA if the owner cannot work by hour 8 (once the agreement exists, P05) | Hours 4-8 |
| Professional liability carrier | No cyber policy. Ask whether the professional liability policy has a cyber or funds transfer fraud endorsement **before** hiring any outside firm | Hours 0-8 |
| FBI (IC3 online report) | Voluntary report; supports OFAC mitigation and any wire recall | Day 1 |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a ransomware incident when any of these happens: a ransom note or renamed files on the laptop or in the cloud archive; the antivirus reports ransomware; the file suite warns of mass file changes; an email or post claims to have client data. **Write down the date and time.** Two clocks start:
- **CBP: 72 hours from discovery** of a known breach of customs records (19 CFR 111.21(b)). Data theft or encryption of the archive is a breach of records for this purpose; CBP's rule has no materiality test.
- **Florida: 30 days from determination** of a breach of personal information (Fla. Stat. 501.171(4)).

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** (memory may hold evidence) and do not reply to or pay the attacker | Laptop offline, still on |
| 2. From the phone, pause file sync in the file suite web console so encrypted files stop spreading | Sync paused |
| 3. From the phone, change the email password, sign out all sessions, delete any app passwords and forwarding rules | Only the phone is signed in |
| 4. From the phone, change the passwords for the customs software, bank, accounting SaaS, and CBP portals, and end their other sessions. Call the bank fraud line | Sessions revoked; bank alerted |
| 5. Call the IT consultant, then counsel | Both engaged |
| 6. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What was on the laptop?** With the consultant, list the synced archive folders, downloads, and scans. Mark every file that holds an importer of record number, a POA, or bank details. **This list is the CBP notice.**
2. **Which importer of record numbers?** Export the client list from the customs software (from the phone or a clean device) and match it to the affected folders. Note which numbers are Social Security numbers (six individual importers) and which are EINs.
3. **Customs software and bank check.** Ask the vendor and the bank for sign-in logs for the past 30 days. Look for new devices, changed payees, or entries amended without the owner. If none, record that.
4. **Phone and router.** The consultant checks the phone and changes the router admin password. Keep the phone off the household Wi-Fi; use cellular data.
5. **Preserve evidence.** The consultant images the laptop disk and saves logs, with a chain-of-custody note (who, when, where stored). No wiping until counsel agrees.

## 5. Hours 8-24: keep cargo moving and prepare notices (RS.CO, RC.RP)
- **Filings:** sign in to the customs software from the wiped spare laptop (P05) over the phone hotspot. Check the arrivals list for the next 48 hours and ISF deadlines (24 hours before lading, 19 CFR 149.2(b)). If the owner cannot file, the backup broker files urgent entries under its own POA.
- **Payments:** no new payees or changed bank details until the incident is closed, and then only after a call-back (POL-01 8.6).
- **Archive:** restore from the independent backup (once POAM-002 is done) or from version history to a clean folder. Records must still be producible to CBP within 30 days of any request (111.25(b)).
- **Laptop:** do not decrypt and reuse. The consultant reinstalls it from clean media after evidence is saved.
- **CBP notice draft:** with counsel, draft the email to the CBP Security Operations Center: what happened, when it was discovered, the records affected, and the list of known compromised importer identification numbers. **Send within 72 hours of discovery even if the picture is incomplete**, then send the updated list within 10 business days.
- **State notices:** count affected individuals by state of residence. Start the Florida determination; counsel decides whether the "no likely harm" written determination in 501.171(4)(c) is supportable.
- **Port systems check:** if the attacker used stolen credentials for a terminal or port community portal, counsel decides whether to report under 33 CFR 6.16-1 (FBI, CISA, and the Captain of the Port, immediately).
- **Ransom:** not paid without counsel's advice and an OFAC sanctions check. Paying does not remove the CBP or state notice duties if data was taken.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 72 hours of discovery | CBP Security Operations Center (cbpsoc@cbp.dhs.gov), with compromised importer identification numbers | Any known breach of customs records |
| Within 24 hours (contract) | The CTPAT importer client whose agreement asks for it; other clients promptly | That client's records affected |
| Within 10 business days of the CBP notice | Updated list of compromised importer identification numbers | After the first CBP notice |
| Within 30 days of determination | Florida individuals (or the written no-harm determination, sent to the Department within 30 days); Department of Legal Affairs if 500 or more Floridians | Florida residents' personal information accessed |
| Per each state's law | Individuals in other states | Non-Florida residents affected |

**Plan to the shortest clock.** The CBP 72-hour notice will almost always come first. It goes to CBP, not to individuals, so it does not replace the Florida notice.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, internet, a clean device, customs software access, email, banking, then accounting and the archive. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-003, R-004), P07, and this runbook, and keep all incident records for 5 years (POL-01 8.9).

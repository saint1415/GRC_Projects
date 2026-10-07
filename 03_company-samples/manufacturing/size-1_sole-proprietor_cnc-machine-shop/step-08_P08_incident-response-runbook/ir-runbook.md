# Incident Response Runbook: Ransomware on the Shop Laptop

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated CNC machine shop) |
| Tier / Vertical | Sole Proprietorship / Manufacturing |
| Incident type | Ransomware on the shop laptop that encrypts the synced Jobs folder and the VMC program share, with theft of customer drawings (OEM confidential and aerospace FCI). The machines and SaaS providers are not the target but may be affected |
| Why this type | The vertical's scenario (an exploited vulnerability in a fielded medical device) fits a device maker, not a parts supplier. Ransomware is the shop's top risk (P01 R-001) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner-machinist, 2026-09-04 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-10-15 (P01 R-012) |

Keep a printed copy in the office and at home. Assume the laptop and the productivity suite account are in the attacker's hands: **use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| On-call IT technician (NDA) | Isolate the laptop, save evidence, check the phone, router, and VMC | Hour 0 |
| Business attorney (with data-breach experience) | Contract notice wording, ransom questions, what to tell customers | Hours 0-4 |
| Insurance agent | No cyber policy today. Ask whether the general liability policy covers anything *before* paying any outside firm | Hours 0-4 |
| Productivity suite provider support | Lock out the attacker, restore file versions from before the attack, pull sign-in and sharing history | Hours 1-4 |
| Aerospace customer (buyer and security contact) | Contract notice within 72 hours if its drawings may be affected; it has its own duties up the chain | By hour 72 |
| Each affected OEM quality contact | Contract notice within 5 business days; hold on any lot whose program cannot be verified | Within 5 business days; product holds before any shipment |
| Bank | Watch for payment fraud; confirm no bank-detail changes | Hours 4-8 |
| FBI (IC3 online report) | Voluntary; supports OFAC mitigation if payment is ever considered | Day 1 |
| Emergency contact and overflow shop | Only if the owner is tied up for days (P05) | As needed |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a ransomware incident when any of these happens: a ransom note or renamed files on the laptop; files in the Jobs folder that will not open on the phone either; the antivirus reports ransomware; someone claims to have shop or customer data; the provider warns of a sign-in the owner did not make; or the VMC shows program files that were not sent. **Write down the date and time.** The 72-hour aerospace clock and the 5-business-day OEM clock both run from discovery.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Unplug the laptop's network cable and turn off its Wi-Fi. **Do not power it off** (memory may hold evidence). Do not reply to or pay the attacker | Laptop offline, still on |
| 2. From the phone, pause sync on the productivity suite (or sign the laptop out of the account), change the password, sign out all sessions, and check sharing and forwarding rules | Only the phone is signed in; sync stopped |
| 3. Unplug the VMC's network cable. **Do not load any program** until the source is known clean. Jobs already running from controller memory may finish if they are released repeat programs | VMC offline |
| 4. From the phone, change the accounting SaaS password and check for new bank details or payees | Accounting checked |
| 5. Call the IT technician, then the attorney. Start the paper incident log: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Which customers' files?** With the technician, list the folders that were encrypted or accessed. For each customer, note whether the files are OEM confidential, aerospace FCI, or ordinary. This list decides which notices apply.
2. **Was data taken?** Ask the provider for sharing, download, and sign-in history. Check whether the attacker made new sharing links. Record the answer, even if it is "unknown".
3. **Any CUI or ITAR data?** If a file with those markings turns up, tell the aerospace customer the same day (POL-01 10.3).
4. **Other devices.** The technician checks the phone and the router (admin password, new port forwards, firmware). Keep the VMC off the network.
5. **Preserve evidence.** The technician images the laptop disk and saves logs, with a chain-of-custody note (who, when, where stored). No wiping until the attorney agrees.

## 5. Hours 8-24: keep making parts and prepare notices (RS.CO, RC.RP)
- **Production:** the machines keep running released repeat jobs from controller memory. New programs wait for a clean laptop.
- **Restore files:** restore the Jobs folder from the separate backup (once POAM-002 is done) or from provider versions dated before the attack. Scan the restored files on the clean device.
- **Verify programs before any cut:** compare each OEM program with its released hash (POL-01 8.5). A program that cannot be verified must not run for an OEM part. Tell the OEM and hold any lot made after the earliest possible compromise until it is re-inspected.
- **Laptop:** do not decrypt and reuse. The technician reinstalls it from clean media (encryption on, standard user account, MFA on every account) after the evidence is saved.
- **Notices:** with the attorney, draft the aerospace notice (due within 72 hours) and the OEM notices (due within 5 business days). Say what is known, what is not, and what the shop is doing.
- **Ransom:** not paid without the attorney's advice and an OFAC sanctions check. Paying does not remove any customer notice duty if data was taken.
- **CMMC:** if the incident shows a Level 1 requirement is no longer met, the shop must fix it and re-assess before claiming a current status again (notification matrix).

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 72 hours of discovery | Aerospace customer (PO terms) | Its drawings may be affected |
| Before any shipment | Affected OEM (hold lots) | A released program may be altered or unverified |
| Within 5 business days | Each affected OEM (SQA or NDA) | Its confidential information was accessed |
| Before any payment | OFAC sanctions check | A ransom payment is considered |
| No later than 30 days after determination | Florida residents (Fla. Stat. 501.171) | Only if personal information of individuals is found; not expected |

DFARS 252.204-7012 reporting and CIRCIA do not apply today (reasons in the matrix).

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, machines on released programs, a clean laptop, the verified Jobs folder, inspection records, quoting, then accounting. Within 30 days of closing the incident: record lessons learned; update P01 (R-001, R-005, R-006), P07, and this runbook; keep all incident records for six years (POL-01 8.9). By 2026-12-31, the owner asks the insurance agent whether the general liability policy covers any cyber event and gets a cyber insurance quote.

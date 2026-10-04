# Incident Response Runbook: Ransomware on Farm-Management and Irrigation Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm) |
| Tier / Vertical | Micro / Agriculture, Forestry, Fishing and Hunting |
| Incident type | Ransomware on the office computers that run the farm's records and irrigation management, starting from a phishing email, with theft of payroll and H-2A files (double extortion) and misuse of a stolen SYS-01 password to reach the irrigation module |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT steps follow NIST SP 800-82 Rev. 3 guidance |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office Manager (Security Coordinator) |
| Approved | 2026-08-31 by the Owner and General Manager |
| Last tested | Not yet. First tabletop with the MSP and the irrigation dealer due 2026-11-30; first hand-operation drill due 2027-02-28 (POAM-004) |

**Scenario used to write this runbook.** A Tuesday in early June, two weeks into watermelon harvest, 10 days without rain. On Monday the Office Manager opened an email that looked like a payroll service notice and entered her password on a fake page. Malware on the office desktop collected the passwords saved in its browser, including the Technician's SYS-01 administrator password (no MFA; P01 R-003). At 06:10 Tuesday the Field Supervisor finds the desktop showing a ransom note; the Owner and General Manager's laptop, on the same flat network, is also encrypted, and the synced Office folder is full of renamed files. At 06:40 the Technician sees in the SYS-01 app that both River Tract pivots were stopped at 02:15 and the watermelon drip schedule was deleted. An email to the Owner and General Manager claims the attackers hold "all your worker files" (P01 R-001, R-005).

## 0. Roles and notification chain (Govern)
The farm has 7 people and no IT staff. The MSP does the technical work on the office computers, the suite, and the backup; the cyber insurer supplies breach counsel and forensics; the Technician owns everything that touches irrigation.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager (Security Coordinator) | Owner and General Manager | Cell phone (numbers on the printed contact card) |
| Decision maker (money, ransom, notices, harvest changes) | Owner and General Manager | Office Manager | Cell phone |
| Safety and OT lead | Irrigation and Equipment Technician | Field Supervisor (after the 2027 drill) | Cell phone and radio |
| Field records and crew | Field Supervisor | Owner and General Manager | Cell phone and radio |
| Technical response | MSP after-hours line (in the MSP contract) | MSP technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel counsel; panel forensic firm engaged by counsel | n/a | Assigned on the first hotline call |
| Irrigation dealer | Dealer service line | Dealer service technician's cell | Phone; on site only during the incident |
| FMIS vendor | Vendor support line | Vendor security contact | Phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** whoever finds it → Office Manager and Technician (at the same time) → MSP after-hours line and Owner and General Manager → insurer breach hotline (Owner and General Manager) → breach counsel and forensics (through the insurer). The FMIS vendor is called as soon as SYS-01 misuse is suspected.

**Out-of-band first.** Assume email and the office computers are compromised. Coordinate by phone, text on company phones, and radio, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the farm office, at the pump station, and at the Owner and General Manager's home: this runbook, contact card, notification matrix, paper daily hours sheets, paper Produce Safety forms, paper harvest log and load tickets, and the hand-operation procedure
- [ ] Hand-operation procedure written, posted at the pump station and in each pivot panel, and drilled with a second person (POAM-004). **Gap until 2027-02-28**
- [ ] Farm-held copy of the controller program on the encrypted office drive (POAM-003). **Gap until 2026-09-30**
- [ ] 90-day immutable backup with MFA on the console, restore-tested in the last 90 days (POAM-003, POAM-004). **Gap until 2026-10-31**
- [ ] MFA on every SYS-01 account and irrigation change alerts on (POAM-008; R-003). **Gap until 2026-09-30**
- [ ] Dealer gateway on request only (POAM-002). **Gap until 2026-10-31**
- [ ] MSP-managed EDR with after-hours alerting (POAM-005). **Gap until 2026-12-31**
- [ ] Insurer hotline and policy number checked each renewal; Security Coordinator registered as breach contact with the payroll service and filing agent (POAM-010)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Ransom note on a computer; files will not open; names changed | Staff report | **Unplug the network cable or turn off Wi-Fi. Do not turn the computer off.** Call the Office Manager and the Technician |
| A pivot, pump, drip zone, or fertigation pump starts, stops, or changes when nobody scheduled it | Technician; SYS-01 alert (once on) | Put the equipment in local or Hand control; call the Office Manager |
| Office folder files changing in bulk; backup job failure | MSP alert; staff report | MSP pauses sync and the backup job; Office Manager opens an incident |
| Someone typed a password into a page reached from an email | Staff report | MSP resets the password and signs out all sessions; check sign-ins and forwarding rules |
| Email or call claiming to hold farm or worker data | Extortion message | Do not reply. Save it. Declare an incident |
| Gateway session nobody requested | Technician | Power off the gateway; declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any device or in the Office folder, an unexplained irrigation command is confirmed, or someone claims to hold farm data.

**Write down two times:** when the incident was discovered, and when the farm determined, or had reason to believe, that personal information was accessed. Florida's 30-day notice clock runs from that determination (Fla. Stat. 501.171(4)(a)). The packer-shipper's 24-hour clock runs from when the farm became aware of anything that could affect product safety, traceability, or loads.

## 3. First hour (RS.MA, RS.MI): safety and crop first
| Step | Who | Done when |
|---|---|---|
| 1. **Put irrigation in a safe state.** Switch the pump station and each pivot panel to local or Hand control; turn fertigation off and close the injection valve; check pressure and flow at the meter faces; start the drip zones and the two River Tract pivots by hand as the crop needs | Technician, with the Field Supervisor driving to the River Tract | All pumps and pivots in local control; fertigation off; water running where needed |
| 2. Unplug the office desktop and laptops from the network and leave them **powered on** for evidence. Unplug the wireless bridge to the pump station. Power off the dealer gateway | Office Manager with the Technician | Computers, pump station link, and gateway offline |
| 3. Call the MSP after-hours line. The MSP pauses Office folder sync and the SYS-08 backup job so it cannot copy encrypted files over good versions | Office Manager; MSP | MSP confirms sync and backup paused |
| 4. From the Owner and General Manager's phone (not an office computer), change the Technician's SYS-01 password, sign out all SYS-01 sessions, turn on MFA for every SYS-01 user, and turn on irrigation change alerts. Call the FMIS vendor to pull the SYS-01 audit trail | Owner and General Manager with the Technician | SYS-01 sessions revoked; vendor engaged |
| 5. Call the insurer's breach hotline and give the claim details | Owner and General Manager | Claim number issued; counsel assigned |
| 6. MSP resets passwords and signs out all sessions for the Office Manager and every suite administrator; removes any forwarding rules | MSP with the Office Manager | Suite sessions revoked |
| 7. Start paper operations: daily hours sheets and Produce Safety forms to the Field Supervisor; paper harvest log and load tickets; phone the packer-shipper's field buyer about today's loads | Field Supervisor; Owner and General Manager | Paper workflow running; loads confirmed by phone |
| 8. Open the incident log: timeline, actions, who, and when | Office Manager | Log open |

**Heat and drought.** If the incident happens in May or June in dry weather, the Technician and the Field Supervisor run the drip zones and pivots by hand on a written schedule until section 5 is complete. Automation is not trusted until then.

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP and the FMIS vendor supplying access and logs.
1. **Scope.** Which computers, accounts, and services are affected? Sources: the MSP antivirus console, suite sign-in and file activity logs, the SYS-01 audit trail, and the firewall logs. **Export the firewall and suite logs on Day 0**: the firewall keeps only about 7 days.
2. **Initial access.** Find the phishing email, the account used, and the first computer. Search all mailboxes for the same message and remove it.
3. **Irrigation integrity.** Which SYS-01 irrigation commands and schedule changes did the attacker make, and from where? Did anything reach the pump station controller through the bridge or the gateway? The dealer compares the controller program with the farm-held copy (once POAM-003 is done) and checks the fertigation limits. **If any fertigation setting changed, treat affected fields as a possible food safety issue** and go to section 6 (packer-shipper row).
4. **Data theft.** Did payroll and H-2A files leave? Check suite download and sharing activity, forwarding rules, and large outbound transfers in the firewall logs. **This drives the Florida breach determination.**
5. **Backups.** Before any restore, the MSP confirms which SYS-08 versions predate the attack and that the backup console was not accessed by the attacker.
6. **Preserve evidence.** Forensics images the affected computers and keeps exported logs with a chain-of-custody record.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's senders, domains, and addresses in the suite and at the firewall (MSP).
2. Disable compromised accounts; remove attacker-added forwarding rules, app consents, and MFA registrations; remove saved passwords from every browser.
3. Wipe and rebuild the desktop and the Owner and General Manager's laptop from the MSP's standard image. **Do not decrypt and reuse them.** Encrypt the rebuilt desktop.
4. Keep the pump station link and the gateway disconnected until the dealer has checked the controller on site and the program matches the approved copy.
5. Confirm with forensics that no persistence remains, including in the MSP's remote management tool, before reconnecting anything. If the MSP's tool may be the entry point, the Owner and General Manager asks the insurer's forensic firm to lead eradication (P01 R-021).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 1 | MSP engaged; insurer notified; counsel and forensics assigned | Office Manager; Owner and General Manager |
| Day 0, within 24 hours of awareness | Packer-shipper told of anything that could affect product safety, lot traceability, or committed loads (grower agreement). If fertigation may have been changed, say which fields and harvest dates | Owner and General Manager |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA, as counsel advises, before any ransom decision | Owner and General Manager with counsel |
| Day 0-1 | Crew briefing in English and Spanish: what happened, paper procedures, whom to call, do not discuss outside the farm | Field Supervisor |
| As soon as known | Florida breach determination documented with its date; list each affected person and where they live | Owner and General Manager with counsel |
| Within 30 days of the determination | Notice to each affected individual in Florida (English and Spanish); people living in other states under their states' laws; H-2A workers at home-country addresses by farm policy | Office Manager with counsel |
| Only if 500 or more Floridians (not expected: about 25 people) | Department of Legal Affairs notice within 30 days; consumer reporting agencies only if more than 1,000 | Owner and General Manager with counsel |
| Each payday | H-2A earnings statements issued on time from paper hours and the payroll service (20 CFR 655.122(k)) | Office Manager |
| On request | Produce Safety records to FDA from paper forms and the latest monthly export (21 CFR 112.166(a)); H-2A records to DOL within 72 hours (655.122(j)(2)) | Field Supervisor; Office Manager |

**Plan to the 30-day clock.** Florida's deadline runs from the determination, not from the end of the investigation. Counsel should set the determination date early and in writing.

**Inbound notices.** If the payroll service or the H-2A filing agent is where the breach happened, it must notify the farm no later than 10 days after its determination (Fla. Stat. 501.171(6)(a)). The farm still sends the notices to individuals.

**Not triggered for this farm (see the matrix for reasons):** the Reportable Food Registry (the farm is not a responsible party), CIRCIA (not final, and the farm is below the proposed size criterion), the Florida Department and consumer reporting agency notices (below their thresholds), and FAR 52.204-25 (no federal contracts).

**Ransom decision:** only the Owner and General Manager, with breach counsel's and the insurer's advice and after an OFAC sanctions check (POL-03 4.8). Paying does not remove notice duties if data was taken, and it does not make SYS-01 settings or the controller trustworthy again.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Hand operation of irrigation stays in place throughout (people first, not systems)
2. Suite and SYS-01 administrator access from a clean device, with MFA re-registered
3. SYS-01 irrigation module and harvest log: confirm with the FMIS vendor that the farm's tenant is clean; rebuild the deleted drip schedule from the Technician's notes
4. Pump station controller: checked on site by the dealer and verified against the farm-held program copy. Return to automatic one zone and one pivot at a time with the Technician watching a full cycle. **Fertigation returns last**, after a supervised test at low rate
5. Field tablet and phones for daily hours and Produce Safety records; paper entries keyed in, paper kept as the original
6. Office desktop and laptop rebuilt by the MSP
7. Payroll (repeat the prior week through the payroll service if needed, then correct from paper hours) and the Office folder restored from the newest clean SYS-08 version, no longer synced to the desktop
8. Telematics, drone, and SYS-09

**Validate before reconnecting:** antivirus or EDR clean, passwords changed, saved browser passwords removed, patches current, and the controller program matching the approved version. Tell the crew, the packer-shipper, and the insurer when each process is back (RC.CO). Keep paper procedures until each process meets its RTO in P05.

**End of recovery:** declared by the Owner and General Manager when irrigation has run on automation for 72 hours without unexplained commands, SYS-01 alerts are on for every irrigation change, and the paper hours and Produce Safety records for the incident period have been keyed in and checked.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, the dealer, and counsel. Written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-003, R-004, R-005, R-020), the POA&M (P07), the contingency plan, and this runbook.
- Keep the incident log, breach determination, notices, and forensic report for at least 3 years (POL-02 A.7), and any Florida no-harm determination for at least 5 years (Fla. Stat. 501.171(4)(c)).

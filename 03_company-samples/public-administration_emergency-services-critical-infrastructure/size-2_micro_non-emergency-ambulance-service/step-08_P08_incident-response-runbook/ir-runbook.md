# Incident Response Runbook: Dispatch Outage from Ransomware

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed BLS ambulance service, non-emergency transport only) |
| Tier / Vertical | Micro / Emergency Services |
| Incident type | Ransomware from a phishing email encrypts the office desktops (including the dispatch desk) and the shared drive; the attacker also uses a stolen platform password to export trip records. The company loses its dispatch board and must dispatch manually |
| Why this scenario | The registry scenario is a computer-aided dispatch outage from ransomware. Here the CAD is vendor SaaS, so ransomware cannot encrypt it. The outage comes from losing the dispatch desk and from locking down a compromised login, which is the realistic version for a company this size (P01 R-001, R-002) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office Manager (Privacy Officer and Security Officer) |
| Approved | 2026-09-04 by the Owner |
| Last tested | Not yet. First manual dispatch drill due 2026-10-31 and first tabletop with the MSP due 2026-11-30 (POAM-009) |

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The MSP does the technical work on office devices, the platform vendor checks its own service, and the cyber insurer supplies breach counsel and forensics. The Office Manager runs the incident and keeps the log. The Scheduler-Dispatcher keeps patients moving.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Owner | Cell phone (numbers on the printed contact card) |
| Decision maker (money, ransom, refusing trips) | Owner | Office Manager | Cell phone |
| Dispatch continuity | Scheduler-Dispatcher | Owner (works from the owner laptop or on-call phone) | On-call phone |
| Technical response, office devices | MSP help line (weekdays 7:00 a.m. to 6:00 p.m.) | Insurer's 24x7 hotline outside MSP hours (P01 R-016) | Phone only |
| Platform vendor | Vendor 24x7 support line | Vendor account manager | Phone; security contact under the BAA |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel | Insurer panel counsel | Not applicable | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm | Not applicable | Engaged by breach counsel (keeps the work under legal privilege, as counsel advises) |
| Clinical questions | Medical Director | Not applicable | Cell phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** whoever finds it → Office Manager → Owner and platform vendor support (at the same time) → insurer breach hotline (Owner) → MSP when its line opens, or the insurer's forensic firm before then → breach counsel (through the insurer). The Scheduler-Dispatcher starts manual dispatch without waiting for any of these calls.

**Out-of-band first.** Assume email and the shared drive are compromised. Coordinate by phone and text on the company phones, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the dispatch desk, in the on-call bag, in each ambulance, and at the Owner's home: this runbook, the contact card, the notification matrix, the four-factor breach assessment form, paper trip intake forms, and paper patient care report forms
- [ ] Next-day run sheet printed every night by 7:00 p.m., with pickup times, addresses, facility phone numbers, and crew assignments; a copy goes in the on-call bag (P05). **Gap: printed "most nights"; never drilled until POAM-009 closes**
- [ ] Phone vendor web portal login (with MFA) on the on-call phone, so request lines can be forwarded without the office
- [ ] Platform MFA for every user and named dispatch accounts (**gap until POAM-002 and POAM-003 close**)
- [ ] Backups: 90-day immutable versions, restore-tested within the last 90 days (**gap until POAM-009 and POAM-010 close**)
- [ ] MSP-managed EDR with after-hours monitoring (**gap until POAM-013 closes**)
- [ ] Insurer hotline number and policy number checked at each renewal; the policy's panel vendors listed on the contact card

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Dispatch desktop shows a ransom note, files will not open, or names have changed | Scheduler-Dispatcher or on-call person | **Unplug the network cable or turn off Wi-Fi. Do not turn the computer off.** Start manual dispatch. Call the Office Manager |
| Dispatch board shows trips, crews, or changes nobody made, or a sign-in alert arrives | Any user | Call the Office Manager; do not keep using the shared account |
| Export log shows a full trip-list export nobody expected | Office Manager weekly check | Call the platform vendor to suspend sessions; declare an incident |
| A staff member clicked a link and typed a password | Staff report | Office Manager has the account reset and all sessions signed out; check the suite and platform sign-in logs |
| Antivirus or EDR alert that is not cleared automatically | MSP console | MSP isolates the device and calls the Office Manager |
| Email or call from someone claiming to have patient data | Extortion message | Do not reply. Save the message. Declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any device or in the shared drive, or when someone claims to hold company data. **Declare a platform compromise** when a sign-in or export from an unknown location is confirmed. In this scenario both are declared together.

**Write down the discovery time.** Under 45 CFR 164.404(a)(2), a breach counts as discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member. The first report by the person who found it starts that clock. Florida's 30-day clock starts at the company's determination of a breach, or reason to believe one occurred (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI, RC.RP)
| Step | Who | Done when |
|---|---|---|
| 1. Switch to manual dispatch: take out the printed run sheet, call each crew phone with its first pickups, and run status on the paper board. If no run sheet was printed, rebuild the first pickups from the on-call phone's platform app, which is unaffected unless the platform is suspended | Scheduler-Dispatcher | Both crews have their first 3 pickups |
| 2. Disconnect affected computers from the network; leave them powered on for evidence | Scheduler-Dispatcher, guided by the Office Manager | Devices offline |
| 3. Forward the request lines to the on-call phone from the phone vendor's web portal | Scheduler-Dispatcher | Test call rings the on-call phone |
| 4. Call platform vendor support: suspend all sessions, disable the shared dispatch account, force password resets for administrators, and preserve the access and export logs | Office Manager | Vendor confirms the actions and gives a case number |
| 5. Call the insurer's breach hotline and give the claim details | Owner | Claim number issued; counsel assigned |
| 6. Call the MSP (or, before 7:00 a.m. and on weekends, the insurer's forensic firm): isolate devices, pause shared drive sync, and suspend the backup job so it cannot copy encrypted files over good versions | Office Manager | Isolation and backup protection confirmed |
| 7. Call both dialysis centers and any hospital with a discharge booked that day: transports are running, times may slip, use the backup number for new requests | Scheduler-Dispatcher | Facilities informed |
| 8. Open the incident log: timeline, actions, who, when | Office Manager | Log started |

**911 rule.** Any caller who describes an emergency is told to hang up and dial 911, whatever the state of the systems (POL-03 4.6).

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP and the platform vendor supplying access and logs.
1. **Scope.** Which computers, accounts, and services are affected? Sources: antivirus or EDR console, suite sign-in and file activity logs, platform access and export logs, firewall logs, phone system sign-in log.
2. **Initial access.** Find the phishing email, the account used, and the first computer. Search all mailboxes for the same message and remove it. Check whether the shared dispatch password was typed into a fake sign-in page or taken from the desktop.
3. **Preserve evidence.** Forensics images affected computers and exports suite, platform, and firewall logs before they age out (suite logs are kept 180 days). Keep a chain-of-custody record for every image and export.
4. **Data theft.** What left? Check the platform export log (which trips, which fields, how many patients), suite downloads and forwarding rules, and large outbound transfers in firewall logs. A full trip-list export would include names, dates of birth, addresses, insurance identifiers, and pickup and destination details for up to about 5,200 patients. **This drives the breach decision.**
5. **Backups.** Before any restore, the MSP confirms which backup versions predate the attack and that the backup console was not accessed by the attacker.
6. **Tablets.** Crews keep documenting offline. Confirm with the MSP through MDM that no tablet or phone shows signs of compromise before reconnecting it to the platform.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's senders, domains, and IP addresses in the suite and at the firewall (MSP).
2. Retire the shared dispatch account for good; issue named accounts with MFA to the Scheduler-Dispatcher, the Office Manager, and the Owner before the board is used again (POAM-002, POAM-003).
3. Disable any compromised accounts; remove attacker-added forwarding rules, app consents, and MFA registrations.
4. Wipe and rebuild affected computers from the MSP's standard image. **Do not decrypt and reuse them.**
5. Confirm with forensics that no persistence remains, including in the MSP's remote management platform and any remote access tool, before reconnecting anything.
6. If the MSP's own tools may be the entry point, the Owner asks the insurer's forensic firm to lead eradication and requires the MSP to show its own investigation results (P01 R-003).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice before it goes out. The Office Manager, as Privacy Officer, signs the four-factor breach risk assessment (45 CFR 164.402). Under the 164.402 definition, an impermissible acquisition, access, use, or disclosure of PHI is presumed to be a breach unless the assessment shows a low probability that the PHI has been compromised. A confirmed export of the trip list will almost certainly be a breach.

| When | Action | Owner |
|---|---|---|
| Hour 1 | Platform vendor and insurer notified; counsel and forensics assigned; MSP engaged | Office Manager; Owner |
| Day 0 | Facilities told that transports continue (no details of the breach until counsel approves) | Scheduler-Dispatcher |
| Day 0-2 | Voluntary report to the FBI (IC3) or CISA, as counsel advises. Make it before any ransom decision: full and timely reporting is an OFAC mitigating factor | Owner with counsel |
| Day 0-1 | Staff briefing: what happened, manual dispatch steps, do not discuss outside the company, send patient, facility, and media questions to the Owner | Office Manager |
| Within 72 hours | Notice to the regional hospital under the transport agreement if its patients may be affected | Owner with counsel |
| As soon as scope is known | Four-factor breach risk assessment documented; count affected individuals by state of residence | Office Manager with counsel |
| Within 30 days of determination | Florida individual notice, or HIPAA notice relied on under 501.171(4)(g); notice to the Department of Legal Affairs if 500 or more Floridians (a timely copy of the HIPAA notice is deemed compliance with 501.171(3)); consumer reporting agencies if more than 1,000 | Office Manager and counsel |
| Within 60 days of discovery | HIPAA individual notices; HHS notice at the same time if 500 or more; media notice if more than 500 Florida residents | Office Manager and counsel |
| Within 60 days after year end | HHS breach log if fewer than 500 | Office Manager |

**Plan to the shorter clock.** For a company this size, determination and discovery are usually days apart at most. Florida's 30-day deadline therefore usually arrives before HIPAA's 60-day outer limit. Counsel should decide in week 1 whether to send one HIPAA-compliant notice by the Florida date.

**Inbound notices.** If a vendor's system is where the breach happened (the platform vendor, the MSP, the phone vendor, or the billing company), it must notify the company under its BAA (164.410, no later than 60 days) and, as a Florida third-party agent, within 10 days of its determination (501.171(6)(a)). The company still sends the notices to individuals and regulators.

**Ransom decision:** only the Owner, with breach counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.8). Paying does not remove notification duties if data was taken, and the trip records are safe at the platform vendor, so payment is unlikely to be needed for recovery.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Manual dispatch continues from the run sheet and crew phones until step 3 is done
2. Request lines: confirm forwarding; return them to the office once a clean device is in place
3. Platform access from a clean device: the owner laptop (checked by the MSP) or the on-call phone, using named accounts with MFA; the vendor confirms the tenant is clean
4. Office internet: firewall checked and its credentials changed; hotspot from a crew phone if needed
5. Tablets and hotspots: tablets checked through MDM and synced; any paper patient care reports entered within 24 hours so hospitals can get records within 48 hours of dispatch
6. Office desktops: rebuilt by the MSP with encryption on (POAM-012) and only approved software (POAM-014)
7. Email and the shared fax mailbox: suite accounts cleaned; forwarding rules removed
8. Billing interface: the billing company resumes pulling trips; queued trips released
9. Shared drive: restored by the MSP from the newest clean version; staff check key folders (crew schedule, payroll files, certification records) before sync is turned back on

**Before reconnecting any device:** EDR or antivirus shows clean, passwords are changed, and patches are current. Tell staff and facilities when the board is back (RC.CO). Keep manual dispatch running until dispatch from the board meets its 2-hour RTO in P05 for a full shift.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, the platform vendor, and counsel. Written summary within 30 days (POL-03 4.11).
- Review with the Medical Director whether any transport was delayed enough to affect a patient, and record the result.
- Update the risk register (P01, especially R-001, R-002, R-003, R-008, R-016), the POA&M (P07), the BIA if recovery times were wrong, and this runbook.
- Keep the incident log, breach assessment, notices, and forensic report for 6 years (POL-02 A.7).

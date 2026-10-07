# Incident Response Runbook: Ransomware with PHI Exfiltration

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (primary care office, two physicians) |
| Tier / Vertical | Micro / Health Care and Social Assistance |
| Incident type | Ransomware with theft of PHI (double extortion), starting from a phishing email |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office Manager (Privacy Officer and Security Officer) |
| Approved | 2026-08-31 by the owner physician |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POAM-004) |

## 0. Roles and notification chain (Govern)
The practice has 7 people and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics. The Office Manager runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Owner physician | Cell phone (numbers on the printed contact card) |
| Decision maker (money, ransom, closing the office) | Owner physician | Associate physician | Cell phone |
| Technical response | MSP incident line (24x7 emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel | Insurer panel counsel | n/a | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm | n/a | Engaged by breach counsel (keeps the work under legal privilege, as counsel advises) |
| EHR vendor | Vendor support line | Vendor account manager | Phone; vendor security contact per BAA |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** staff member → Office Manager → MSP incident line and owner physician (at the same time) → insurer breach hotline (owner physician) → breach counsel and forensics (through the insurer). The EHR vendor is called if there is any sign that EHR credentials were used.

**Out-of-band first.** Assume email is compromised. Coordinate by phone and text on personal phones, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the front desk and at the Office Manager's and owner physician's homes: this runbook, contact card, notification matrix, downtime forms, and the four-factor breach assessment form
- [ ] Backups: 90-day immutable versions, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-003 and POAM-004 close**
- [ ] MSP-managed EDR with alert monitoring (SI-4). **Gap until POAM-005 closes**
- [ ] MFA on MSP-held administrator logins (backup console, firewall). **Gap until POAM-002 closes**
- [ ] Downtime kit at the front desk: paper visit forms, printed next-day schedule (P05)
- [ ] Insurer hotline number and policy number checked each renewal; MSP contract includes incident notice terms

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A staff member clicked a link in an email and typed a password | Staff report | Office Manager has the MSP reset the password and sign out all sessions; check the suite sign-in log and forwarding rules |
| Files will not open, names changed, or a ransom note appears | Staff report | **Unplug the network cable or turn off Wi-Fi. Do not turn the computer off.** Call the Office Manager |
| Shared-drive files changing in bulk; sync errors; backup job failure | Suite alert, MSP alert | MSP pauses sync and the backup job; Office Manager opens an incident |
| Antivirus or EDR alert that is not cleared automatically | MSP console | MSP isolates the device and calls the Office Manager |
| Email or call from someone claiming to have patient data | Extortion message | Do not reply. Save the message. Declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any device or in the shared drive, or when someone claims to hold practice data.

**Write down the discovery time.** Under 45 CFR 164.404(a)(2), a breach counts as discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member. The staff member's first report starts that clock. Florida's 30-day clock starts at the practice's determination of a breach, or reason to believe one occurred (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Disconnect affected computers from the network; leave them powered on for evidence | Staff, guided by the Office Manager | Devices offline |
| 2. Call the MSP incident line; MSP isolates devices remotely, pauses shared-drive sync, and suspends the backup job so it cannot copy encrypted files over good versions | Office Manager; MSP | MSP confirms isolation and backup protection |
| 3. Call the insurer's breach hotline and give the claim details | Owner physician | Claim number issued; counsel assigned |
| 4. Reset passwords and sign out all sessions for the affected user and all administrators (EHR, suite, fax, backup console); confirm MFA is intact | MSP with Office Manager | Sessions revoked |
| 5. Start the downtime procedure: paper forms, printed schedule, clinical work on the physicians' laptops or tablets if they are clean | Office Manager with physicians | Patients being seen |
| 6. Open the incident log: timeline, actions, who, when | Office Manager | Log started |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Scope.** Which computers, accounts, and cloud services are affected? Sources: MSP antivirus or EDR console, suite sign-in and file activity logs, EHR audit trail, firewall logs.
2. **Initial access.** Find the phishing email, the account used, and the first computer. Search all mailboxes for the same message and remove it.
3. **Preserve evidence.** Forensics images affected computers and exports suite and firewall logs before they age out (suite log retention is shorter than one year; POAM-008 context). Keep a chain-of-custody record for every image and export.
4. **Data theft.** Did PHI leave? Check suite download and sharing activity, email forwarding rules, EHR report exports, and large outbound transfers in firewall logs. **This drives the breach decision.**
5. **Backups.** Before any restore, the MSP confirms which backup versions predate the attack and that the backup console was not accessed by the attacker.
6. **EHR.** The EHR is SaaS and is usually unaffected. The Office Manager asks the EHR vendor to check for unusual sign-ins or exports from the practice's accounts.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's email senders, domains, and IP addresses in the suite and at the firewall (MSP).
2. Disable any compromised accounts; remove attacker-added forwarding rules, app consents, and MFA registrations.
3. Wipe and rebuild affected computers from the MSP's standard image. **Do not decrypt and reuse them.**
4. Confirm with forensics that no persistence remains, including in the MSP's remote management platform, before reconnecting anything.
5. If the MSP's own tools may be the entry point, the owner physician asks the insurer's forensic firm to lead eradication and requires the MSP to show its own investigation results (P01 R-013).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice before it goes out. The Office Manager, as Privacy Officer, signs the four-factor breach risk assessment (45 CFR 164.402). Under the 164.402 definition, an impermissible acquisition, access, use, or disclosure of PHI is presumed to be a breach unless the assessment shows a low probability that the PHI has been compromised. Plan on notification unless forensics and counsel support that finding.

| When | Action | Owner |
|---|---|---|
| Hour 1 | MSP engaged; insurer notified; counsel and forensics assigned | Office Manager; owner physician |
| Day 0-2 | Voluntary report to the FBI (IC3) or CISA, as counsel advises. Make it before any ransom decision: full and timely reporting is an OFAC mitigating factor | Owner physician with counsel |
| Day 0-1 | Staff briefing: what happened, downtime steps, do not discuss outside the practice, send patient and media questions to the owner physician | Office Manager |
| Day 0-3 | Patients arriving or calling: short script (systems down, care continues, more information to follow) | Front Desk Coordinator |
| As soon as scope is known | Four-factor breach risk assessment documented; count affected individuals by state | Office Manager with counsel |
| Within 30 days of determination | Florida individual notice, or HIPAA notice relied on under 501.171(4)(g); copy of the notice to the Department of Legal Affairs if 500 or more Floridians (deemed compliance with 501.171(3)); consumer reporting agencies if more than 1,000 | Office Manager and counsel |
| Within 60 days of discovery | HIPAA individual notices; HHS notice at the same time if 500 or more; media notice if more than 500 Florida residents | Office Manager and counsel |
| Within 60 days after year end | HHS breach log if fewer than 500 | Office Manager |
| At the start and weekly | Status to the local hospital referral network if shared patients or connections are affected (their questionnaire asked for this) | Owner physician |

**Plan to the shorter clock.** For a practice this size, determination and discovery are often days apart at most. Florida's 30-day deadline therefore usually arrives before HIPAA's 60-day outer limit. Counsel should decide in week 1 whether to send one HIPAA-compliant notice by the Florida date.

**Inbound notices.** If the MSP or a SaaS vendor is where the breach happened, it must notify the practice under its BAA (164.410, no later than 60 days) and, as a Florida third-party agent, within 10 days of its determination (501.171(6)(a)). The practice still sends the notices to individuals and regulators.

**Ransom decision:** only the owner physician, with breach counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.7). Paying does not remove notification duties if data was taken.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Internet and office network: firewall checked and credentials changed; cellular failover or a phone hotspot if the line is down
2. Clean devices for the front desk and physicians: rebuilt desktops; laptops and tablets checked by the MSP
3. EHR/PM access: vendor-hosted; confirm with the vendor that the practice's accounts are clean
4. Cloud fax: new portal passwords
5. Procedure-room workstation and ECG and spirometer: rebuilt with vendor-approved software; re-import any results not already in the EHR
6. Email and phones: suite accounts cleaned; forwarding rules removed
7. Claims: queued charges submitted
8. Shared drive: restored by the MSP from the newest clean version; staff check key folders (forms, scanned records awaiting import, billing worksheets) before sync is turned back on

**Before reconnecting any device:** EDR or antivirus shows clean, passwords are changed, and patches are current. Tell staff and patients when services are back (RC.CO). Keep paper downtime until each function meets its RTO in P05.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and counsel. Written summary within 30 days (POL-03 4.10).
- Update the risk register (P01, especially R-001, R-002, R-005, R-013), the POA&M (P07), and this runbook.
- Keep the incident log, breach assessment, notices, and forensic report for 6 years (POL-02 A.7).

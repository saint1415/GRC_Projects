# Incident Response Runbook: Ransomware with Student Record Exposure

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (K-12 tutoring and learning center) |
| Tier / Vertical | Micro / Educational Services |
| Incident type | Ransomware with theft of student records (double extortion), starting from a phishing email that steals a staff member's suite password |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Center Director (Information Security Coordinator) |
| Approved | 2026-08-28 by the Owner |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POAM-005, POAM-013) |

## 0. Roles and notification chain (Govern)
The company has 7 employees, 14 contractor tutors, and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics. The Center Director runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Center Director | Owner | Cell phone (numbers on the printed contact card) |
| Decision maker (money, ransom, closing the center) | Owner | Center Director | Cell phone |
| Technical response | MSP incident line (24x7 emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Tutoring platform actions and district contact | Director of Tutoring | Center Director | Cell phone |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel | Insurer panel counsel | n/a | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm | n/a | Engaged by breach counsel (keeps the work under legal privilege, as counsel advises) |
| School district | District contract contact | District technology office | Phone numbers in the data privacy agreement |
| SaaS vendors | Platform, scheduling, and suite vendor support lines | Vendor account managers | Phone; security contacts in the vendor folder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** staff member or contractor tutor → Center Director → MSP incident line and Owner (at the same time) → insurer breach hotline (Owner) → breach counsel and forensics (through the insurer). The Director of Tutoring checks the tutoring platform for misuse of the same password. **The district is called within 48 hours of discovery** if there is any sign that district roster data was reached (section 6).

**Out-of-band first.** Assume email is compromised. Coordinate by phone and text on personal phones, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the front desk and at the Center Director's and Owner's homes: this runbook, contact card, notification matrix, downtime steps, parent and staff message templates
- [ ] Backups: 90-day immutable versions, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-004 and POAM-005 close**
- [ ] MFA on every tutoring platform account and every MSP-held administrator login (IA-2(1)). **Gap until POAM-002 closes**
- [ ] MSP-managed EDR with after-hours alert monitoring and suite alerts for mass downloads and forwarding rules (SI-4). **Planned by 2026-12-31 (P01 R-001, R-002)**
- [ ] "Student files" folder limited to two people and shrunk under the retention schedule (P01 R-002; POL-04 4.9)
- [ ] District roster data only in the platform, never in email or on contractor computers (POAM-008)
- [ ] Insurer hotline and policy numbers checked each renewal; district contact numbers checked each school year

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A staff member or tutor clicked a link and typed a password | Staff report | Center Director has the MSP reset the password and sign out all sessions; check the suite sign-in log, forwarding rules, and shared-drive downloads |
| Files will not open, names changed, or a ransom note appears | Staff report | **Unplug the network cable or turn off Wi-Fi. Do not turn the computer off.** Call the Center Director |
| Shared-drive files changing in bulk; sync errors; backup job failure | Suite alert, MSP alert | MSP pauses sync and the backup job; Center Director opens an incident |
| Antivirus alert that is not cleared automatically | MSP console | MSP isolates the device and calls the Center Director |
| Email, call, or message to the company or to parents claiming to hold student data | Extortion message | Do not reply. Save the message. Declare an incident |
| Unknown sign-in or export in the tutoring platform | Platform log or vendor notice | Director of Tutoring disables the account; declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any device or in the shared drive, or when someone claims to hold company data.

**Write down two times.** (1) **Discovery** of unauthorized access to district data: starts the district's 48-hour clock. (2) **Determination** of a breach, or reason to believe one occurred: starts the Florida 30-day clocks (Fla. Stat. 501.171(3)-(4)) and the 10-day third-party agent clock to the district (501.171(6)(a)). The Center Director records both in the incident log, with counsel.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Disconnect affected computers from the network; leave them powered on for evidence | Staff, guided by the Center Director | Devices offline |
| 2. Call the MSP incident line; MSP isolates devices remotely, pauses shared-drive sync, and suspends the backup job so it cannot copy encrypted files over good versions | Center Director; MSP | MSP confirms isolation and backup protection |
| 3. Call the insurer's breach hotline and give the claim details | Owner | Claim number issued; counsel assigned |
| 4. Reset passwords and sign out all sessions for the affected user and every administrator (suite, platform, scheduling, backup console, website); confirm MFA is intact | MSP with the Center Director and Director of Tutoring | Sessions revoked |
| 5. Start downtime steps (P05): printed schedule at the front desk; in-person sessions with printed packets; online sessions moved to staff-hosted video meetings with recording off, or rescheduled | Center Director with the Director of Tutoring | Sessions continuing or rescheduled |
| 6. Open the incident log: timeline, actions, who, when | Center Director | Log started |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Scope.** Which computers, accounts, and cloud services are affected? Sources: MSP antivirus console, suite sign-in and file activity logs, platform audit log, scheduling platform admin log, firewall logs.
2. **Initial access.** Find the phishing email, the account used, and the first computer. Search all mailboxes for the same message and remove it.
3. **Preserve evidence.** Forensics images affected computers and exports suite, platform, and firewall logs before they age out (firewall logs keep 7 days). Keep a chain-of-custody record for every image and export.
4. **Data theft.** Did student information leave? Check shared-drive download and sharing activity in the "Student files" folder, mailbox forwarding rules, roster attachments in sent mail, platform exports, and large outbound transfers in firewall logs. **This drives every notice decision.**
5. **What was taken, and whose.** Build three lists with counsel: (a) district program students (district notice; district decides its own notices); (b) private-pay students and parents whose data is Florida "personal information" (501.171(1)(g): for example, a child's name with an evaluation report describing a mental or physical condition, or a parent's email address with a password); (c) everyone else affected. Count Florida residents for the 500 and 1,000 thresholds.
6. **Backups.** Before any restore, the MSP confirms which backup versions predate the attack and that the backup console was not accessed by the attacker.
7. **SaaS platforms.** The tutoring and scheduling platforms are SaaS and usually unaffected. The Director of Tutoring and the Enrollment and Billing Coordinator ask each vendor to check for unusual sign-ins or exports from the company's accounts.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's email senders, domains, and IP addresses in the suite and at the firewall (MSP).
2. Disable any compromised accounts; remove attacker-added forwarding rules, app consents, and MFA registrations.
3. Wipe and rebuild affected computers from the MSP's standard image. **Do not decrypt and reuse them.**
4. Confirm with forensics that no persistence remains, including in the MSP's remote management platform, before reconnecting anything.
5. If the MSP's own tools may be the entry point, the Owner asks the insurer's forensic firm to lead eradication and requires the MSP to show its own investigation results (P01 R-013).
6. If any contractor tutor's computer may be involved (for example, a roster file or a reused password), the contractor stops using it for company work until counsel and forensics clear it.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice before it goes out. COPPA has no breach notice duty, and FERPA has none for the company; the duties come from the district contract and Florida law.

| When | Action | Owner |
|---|---|---|
| Hour 1 | MSP engaged; insurer notified; counsel and forensics assigned | Center Director; Owner |
| Within 48 hours of discovery | **District notice** under the data privacy agreement if there is any sign district data was reached; agree on who tells program families. Follow with written facts the district needs for its own FERPA record (34 CFR 99.32) | Owner and Director of Tutoring, with counsel |
| Day 0-2 | Voluntary report to the FBI (IC3) or CISA, as counsel advises. Make it before any ransom decision: full and timely reporting is an OFAC mitigating factor | Owner with counsel |
| Day 0-1 | Staff and contractor tutor briefing: what happened, downtime steps, do not discuss outside the company, send parent and media questions to the Owner | Center Director |
| Day 0-3 | Parents calling or asking at the front desk: short script (systems disrupted, sessions continue or are rescheduled, more information to follow). If extortion messages reach parents, counsel approves a same-day message telling them not to reply or pay | Enrollment and Billing Coordinator; Owner |
| As soon as scope is known | Breach determination recorded; Florida residents counted | Center Director with counsel |
| Within 10 days of determination | Florida third-party agent notice to the district, if district data is personal information (501.171(6)(a)) | Owner with counsel |
| Within 30 days of determination | Florida notice to affected individuals (for children, delivered to the parent or guardian as counsel advises); Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 | Center Director and counsel |
| At the start and weekly | Status updates to the district until it confirms closure | Director of Tutoring |

**The district clock comes first.** The 48-hour contract term will almost always arrive before any statutory deadline. Missing it risks the contract (about 16 percent of revenue), so the Owner calls the district even if scope is still unclear and follows up in writing.

**Inbound notices.** If a SaaS vendor or the MSP is where the breach happened, it must notify the company within 10 days of its determination as a Florida third-party agent (501.171(6)(a)). The company still owes the district and Florida notices.

**Ransom decision:** only the Owner, with breach counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.7). Paying does not remove notice duties if data was taken, and it does not guarantee the stolen files are deleted.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Scheduling platform access from a clean device, so the front desk knows who is coming
2. Clean staff laptops and front-desk desktop; center network checked and credentials changed; phone hotspot if the line is down
3. Tutoring platform: confirm with the vendor that the company's accounts are clean; online sessions return to the platform
4. Email and video meetings: suite accounts cleaned; forwarding rules removed
5. District program reporting: paper attendance sheets entered
6. Shared drive: restored by the MSP from the newest clean version; the Center Director checks the "Student files" folder before sync is turned back on
7. Billing batch re-run
8. Payroll and HR files

**Before reconnecting any device:** antivirus shows clean, passwords are changed, and patches are current. Tell staff, contractor tutors, and parents when services are back (RC.CO). Keep downtime steps until each function meets its RTO in P05.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and counsel. Written summary within 30 days (POL-03 4.10).
- Update the risk register (P01, especially R-001, R-002, R-005, R-010, R-013), the POA&M (P07), this runbook, and the next annual risk assessment (16 CFR 312.8(b)(2)).
- Keep the incident log, breach determination, notices, and forensic report for at least 5 years (Fla. Stat. 501.171(4)(c) requires 5 years for a no-harm determination; the company keeps all incident records for the same period).

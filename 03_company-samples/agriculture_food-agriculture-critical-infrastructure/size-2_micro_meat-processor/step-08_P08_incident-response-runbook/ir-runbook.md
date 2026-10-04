# Incident Response Runbook: Ransomware Halting Processing Lines and Cold-Chain Monitoring

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) |
| Tier / Vertical | Micro / Food and Agriculture |
| Incident type | Ransomware that starts with a phishing email on the office desktop, spreads over the flat network to the labeling PC and the Line 1 stuffer HMI, stops both lines, and cuts cold-chain monitoring when the network is isolated |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office Manager (security and compliance lead), with the Production Supervisor (food safety) |
| Approved | 2026-08-31 by the owner |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POAM-009) |

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The MSP does the technical work on the PCs and network; the equipment vendors help with their machines; the cyber insurer supplies breach counsel and forensics. The Office Manager runs the incident; the Production Supervisor runs the product decisions.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Owner | Cell phone (numbers on the printed contact card) |
| Decision maker (money, ransom, stopping production) | Owner | Office Manager | Cell phone |
| Food safety lead (holds, product review, FSIS notice) | Production Supervisor | Owner (HACCP-trained) | Cell phone |
| Machines and refrigeration | Maintenance and Sanitation Technician | Refrigeration contractor; equipment vendors by phone | Cell phone |
| Technical response (PCs, network, backup) | MSP help line (emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel firms | n/a | Assigned by the insurer on the first call |
| FSIS | FSIS inspection program personnel assigned to the plant; local FSIS District Office | n/a | Numbers in the binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** staff member → Office Manager and Production Supervisor (at the same time) → MSP help line and owner → insurer breach hotline (owner) → breach counsel and forensics (through the insurer).

**Out-of-band first.** Assume email and the office desktop are compromised. Coordinate by phone and text on personal phones, using the printed contact card.

**The MSP contract gap.** The MSP contract today promises a next-business-day response and excludes the plant machines. On a weekend or at night, the owner calls the insurer hotline at once rather than waiting for the MSP (P01 R-012).

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binders in the production office, the office, and the owner's home: this runbook, the contact card, the notification matrix, paper CCP and SSOP forms, the manual temperature log, pre-printed labels for top products, and the product hold log
- [ ] Offline copies of approved smokehouse cycles, stuffer HMI settings, packager recipes, and label templates in the office safe (POL-04 4.5). **Gap until POAM-010 closes**
- [ ] Immutable backups, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-009 and POAM-010 close**
- [ ] Plant network separated from the office (SC-7). **Gap until POAM-012 closes**
- [ ] MSP-managed EDR with after-hours alerts (SI-3). **Gap until POAM-013 closes**
- [ ] Cold-chain alert escalation and a cellular backup for the gateway (P01 R-004)
- [ ] Sealed emergency credentials in the safe (POL-02 B.7)
- [ ] Insurer hotline number and policy number checked at each renewal

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Files will not open, names changed, or a ransom note appears on the office desktop or labeling PC | Staff | **Unplug the network cable. Do not turn the PC off.** Call the Office Manager |
| The stuffer HMI or packager HMI shows a ransom screen, freezes, or loses its settings | Operator | Stop the line safely (section 3); call the Production Supervisor and the Office Manager |
| The label printer prints wrong or blank labels, or templates are missing | Operator | Stop labeling; hold the product; call the Production Supervisor |
| The cold-chain dashboard stops updating or shows the gateway offline | Production Supervisor; vendor alert (after R-004 fix) | **Start the manual temperature log at once**; call the Office Manager |
| A smokehouse cycle runs with settings nobody approved | Operator; Production Supervisor | Treat as possible tampering (POL-03 4.6); abort and hold; call the incident line |
| Antivirus alert the MSP cannot clear | MSP | MSP isolates the PC and calls the Office Manager |
| Email or call claiming to hold company data | Extortion message | Do not reply. Save it. Declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any PC or machine, or when a machine loses its settings with signs of malicious activity.

**Write down the times:** discovery, the last trusted CCP reading for each batch in progress, the start of manual monitoring, and when each line stopped. These times drive product decisions and any notice deadlines.

## 3. First hour: make the plant safe (RS.MA, RS.MI)
**Order matters: people, then product, then evidence and systems.**

| Step | Who | Done when |
|---|---|---|
| 1. Confirm refrigeration is running (the condensing units run on their own controls) and start the **manual temperature log** for both coolers, the freezer, the blast chill cooler, and the truck, at least every hour | Production Supervisor; Maintenance and Sanitation Technician | First manual entries recorded |
| 2. Smokehouse: if the cycle is running normally on the controller and the controller shows no sign of tampering, let it finish and record the handheld core temperature on paper; otherwise abort and hold the batch | Production Supervisor | Cycle finished with a paper record, or batch on hold |
| 3. Chilling: check product in the blast chill cooler with a calibrated handheld probe every 30 minutes on paper until the wireless probe is trusted again | Production Supervisor | Paper chilling record started |
| 4. Stop Lines 1 and 2 safely; switch the stuffer to manual stop; do not restart until section 7 | Production workers | Lines stopped |
| 5. **Hold all product** made, cooked, chilled, or labeled since the last trusted record, and any product labeled since the label PC was last known good. Tag and segregate it | Production Supervisor | Hold tags on product; hold log started |
| 6. Isolate: unplug the firewall's internet link and the office desktop; disable the smokehouse portal module and the packaging vendor's remote desktop; leave affected PCs powered on | Office Manager with the MSP on the phone | Links down; photos of cable positions taken |
| 7. Call the MSP help line and the insurer's breach hotline | Office Manager; owner | MSP engaged; claim number issued |
| 8. Tell the FSIS inspection program personnel on site (or by phone) that electronic monitoring is down and that paper monitoring and holds are in place | Production Supervisor | Time recorded |
| 9. Open the incident log: timeline, actions, who, when | Office Manager | Log started |

**Isolating the network cuts cold-chain monitoring.** The gateway sits on the same network until the plant network and cellular backup are in place. That is why step 1 comes before step 6, and why the manual log continues until section 7 confirms the gateway is back on a clean network.

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs and the Maintenance and Sanitation Technician supplying machine access.
1. **Scope.** Which PCs, machines, accounts, and services are affected? Sources: antivirus console, suite sign-in and file activity logs, firewall logs (only 7 days today; export them at once), records app edit history, smokehouse portal session log, remote desktop tool log.
2. **Initial access.** Phishing email, the packaging vendor's remote desktop tool, or the smokehouse portal? These are the likely paths (P01 R-001, R-002, R-003). Search all mailboxes for the phishing message and remove it.
3. **Did the attacker touch the process?** With the Production Supervisor, compare every smokehouse cycle, stuffer setting, packager recipe, and label template with the offline approved copies. Check the records app for entries made or deleted during the incident window. **Any unexplained difference is treated as possible tampering** (POL-03 4.6).
4. **Preserve evidence.** Forensics images affected PCs and exports logs before they age out. Keep a chain-of-custody record for every image and export.
5. **Data theft.** Did employee personal information (HR files, payroll exports) or formulations leave? This drives the Florida breach decision.
6. **Backups.** Before any restore, the MSP confirms which backup versions predate the attack and that the backup console was not accessed by the attacker.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's senders, domains, and addresses in the suite and at the firewall (MSP).
2. Disable compromised accounts; reset all administrator passwords and the shared passwords and PIN; remove attacker-added forwarding rules and MFA registrations.
3. Wipe and rebuild the office desktop and labeling PC from clean media. **Do not decrypt and reuse them.**
4. Stuffer HMI: the equipment vendor restores the HMI image and settings from the offline copy, or reinstalls it on site. If no clean copy exists, the vendor rebuilds the settings and the Production Supervisor verifies them against the formulation sheets.
5. Keep the smokehouse portal and the packaging remote desktop disconnected. Vendors work on site or in supervised sessions only.
6. Confirm with forensics that persistence is removed, including in the MSP's remote management platform, before reconnecting anything.

## 6. Food safety decisions and reporting (RS.CO)
**Food safety decisions come first, and they are the Production Supervisor's** (owner as backup). Follow `notification-matrix.csv`; breach counsel confirms personal-information notices.

**Product on hold.** For each held lot, the Production Supervisor documents the review required for an unforeseen deviation (9 CFR 417.3(b)): segregate and hold, decide acceptability using the paper records, handheld readings, controller display photos, and product testing where needed, and dispose of anything that cannot be shown safe. Product may not ship until its records are complete and reviewed (417.5(c)). Afterwards, decide whether the HACCP plan needs reassessment (417.3(b)(4)).

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | MSP engaged; insurer notified; FSIS personnel told; holds in place | Office Manager; owner; Production Supervisor |
| Hour 0-24 | Decide whether any **already-shipped** product may be adulterated or misbranded (shipped after an unapproved cycle or label change, or after unmonitored storage). If so, notify the FSIS District Office **within 24 hours** of that determination (9 CFR 418.2) and start the recall procedure (418.3), tracing lots from invoices or paper delivery tickets | Production Supervisor with the owner |
| Day 0-2 | Voluntary report to FBI (IC3) or CISA, as counsel advises; before any ransom decision | Owner |
| Day 0-2 | Tell the grocery chain and other wholesale customers about delivery impact, and any recall, under their supplier agreements | Owner |
| Day 0-1 | Staff briefing: what happened, paper procedures, do not discuss outside the company, send customer questions to the owner | Office Manager |
| As soon as known | Decide with counsel whether employee personal information was accessed or acquired | Office Manager |
| Within 30 days of determination | Florida notice to affected individuals; Department of Legal Affairs only if 500 or more Floridians (unlikely here) | Office Manager and counsel |

**Plan to the shortest clock.** The 24-hour FSIS clock starts at *learning or determining*, and the determination must be made with reasonable speed. Do not wait for the IT work to finish before asking the shipped-product question.

**Inbound notices.** If the payroll service or the MSP is where a breach happened, it must notify the company within 10 days of its determination as a Florida third-party agent (501.171(6)(a)). The company still sends the notices to individuals.

**Ransom decision:** only the owner, with breach counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.8). Paying does not make held product safe or remove any notice duty.

**CIRCIA:** not in effect, and as proposed the company would be far below the size criterion. Recheck when the final rule is published.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. **Temperature monitoring:** cold-chain gateway reconnected on a clean network (or the cellular backup); dashboard checked against the manual log for one hour before the manual log stops
2. **Smokehouse and CCP records:** controller settings compared with the approved copies; cook logs exported; paper records entered into the records app
3. **Labeling PC and label printer:** rebuilt; label templates restored and each one checked against the approved copy; first label of each product checked by a second person
4. **Line 1 stuffer:** HMI restored by the vendor; settings verified
5. **Records app on the tablets:** accounts reset; paper SSOP and HACCP records entered
6. **Accounting and email:** suite accounts cleaned; paper orders and delivery tickets entered
7. **Payroll and office files:** restored from the newest clean backup
8. **Retail counter:** the provider-managed terminal is unaffected; confirm

**Validate before restart (POL-03 4.11):** each line restarts only after the Production Supervisor confirms its settings match the approved versions and signs a restart check, and the first batch on each line is verified against critical limits with a handheld reading. Tell staff, customers, and the FSIS personnel when normal monitoring resumes (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and the Production Supervisor. Written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-002, R-004, R-006), the POA&M (P07), this runbook, and the HACCP plans if the incident revealed a deviation the plans did not foresee (9 CFR 417.3(b)(4)).
- Keep the incident log, hold and disposition records, notices, and the forensic report for at least 3 years (POL-02 A.7), and product records with the HACCP records (417.5(e)).

# Incident Response Runbook: Ransomware on the Dispatch and Office Back-Office Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (short line freight railroad, 16 route miles, north Florida) |
| Tier / Vertical | Micro / Transportation Systems |
| Incident type | Ransomware that starts with a phishing email to an office account, spreads across the flat office network to the dispatch desktop (radio console), and encrypts the synced shared drive, with possible theft of employee records and SSI |
| Why not "train control back office" | The railroad has no PTC system (no duty under 49 CFR 236.1005(b)(1); the interchange move runs under 236.1006(b)(4)). The back office that carries movement authority is the dispatch desk and the operations system (00_company-facts.md section 5) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office Manager (Security Lead) |
| Approved | 2026-08-31 by the Owner and General Manager |
| Last tested | Not yet. First tabletop with the MSP and first paper dispatch drill due 2026-11-30 (POAM-004) |

**Two rules above all others:**
1. **Trains move only under authority the dispatcher can trust.** The moment the dispatch desktop or the operations system is in doubt, the dispatcher switches to paper dispatch (POL-03 4.3).
2. **The TSA clock starts at discovery.** A cyber attack must be reported to TSA as soon as possible and within 24 hours of initial discovery (49 CFR 1570.203(a)(1); Appendix A to part 1570, "Cyber Attack"). The company target is 12 hours. Do not wait for the investigation.

## 0. Roles and notification chain (Govern)
The railroad has 7 people and no IT staff. The MSP does the technical work, the cyber insurer supplies breach counsel and forensics, and the General Manager keeps trains safe. During an incident the General Manager may be at the dispatch desk, so the Office Manager runs the cyber side and the Roadmaster relieves either role.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Operations lead (train safety) and dispatcher | Owner and General Manager | Roadmaster (relief dispatcher) | Dispatch desk radio and phone; cell phone |
| Incident lead (cyber) and incident log | Office Manager (Security Lead) | Owner and General Manager | Cell phone (printed contact card) |
| TSA Security Coordinator (makes the TSA report) | Owner and General Manager | Roadmaster (alternate Security Coordinator) | Cell phone; reachable 24/7 (1570.201(f)(2)) |
| Decision maker (money, ransom, holding trains, outside statements) | Owner and General Manager | None; the Roadmaster decides only on train movements | Cell phone |
| Technical response | MSP incident line (emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the incident binder |
| Breach counsel and forensics | Insurer panel firms | n/a | Assigned by the insurer on the first call |
| Operations system (SYS-01) | Operations SaaS vendor support line | Vendor account manager | Phone; ask for the security team |
| Connecting Class I | Class I yard office and car management office | Class I dispatcher for the interchange move | Numbers in the incident binder |
| Law enforcement and federal partners | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Notification chain in the first hour:** employee → Office Manager (and the dispatcher, if dispatch, radio, or tablets are affected) → MSP incident line and General Manager at the same time → insurer breach hotline (General Manager) → breach counsel and forensics (through the insurer). The TSA call follows within 12 hours (section 4). The Class I is called as soon as interchange or the EDI link may be affected.

**Out-of-band first.** Assume email and the shared drive are compromised. Coordinate by phone and text on personal phones, using the printed contact card. Movement authority stays on the radio.

## 1. Preparation checks (Identify / Protect)
- [ ] Incident binder at the dispatch desk and in the General Manager's and Roadmaster's vehicles: this runbook, the contact card, `notification-matrix.csv`, the TSA report form with the 1570.203(c) fields, and the paper dispatch kit list (POL-03 4.1). **TSA report form update due 2026-10-15 (POAM-006)**
- [ ] Paper dispatch kit at the desk: paper track warrant forms, dispatcher log sheets, printed timetable and special instructions, track chart, current slow orders and bulletins (P05 BP-01)
- [ ] Written paper dispatch procedure, drilled in the last 6 months. **Gap until POAM-004 closes (procedure and first drill 2026-11-30)**
- [ ] Weekly export of car inventory and authority history from SYS-01, so the railroad holds its own copy. **Gap until POAM-003 milestone 2026-09-30**
- [ ] Backups: 90-day immutable versions, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-003 and POAM-004 close**
- [ ] MSP-managed EDR with alert monitoring on the 5 computers (SI-3, SI-4). **Gap until POAM-005 closes**
- [ ] MFA on the backup console, the firewall management login, and the telematics portal (IA-2(1)). **Gap until POAM-002 closes**
- [ ] Dispatch desktop on its own firewall segment (SC-7). **Gap until POAM-010 closes**
- [ ] Spare base radio in the enginehouse tested each quarter; handhelds charged
- [ ] Insurer hotline and policy number checked at each renewal; MSP contract amendment with 24-hour incident notice and a recovery commitment (POAM-009, by 2026-12-31)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Radio console freezes, files renamed, or a ransom note on the dispatch desktop | Dispatcher | **Switch to paper dispatch now (section 3, step 1).** Unplug the desktop's network cable; leave it powered on. Call the Office Manager |
| A ransom note, locked files, or renamed files on an office or shop computer | Employee | Unplug the network cable or turn off Wi-Fi. **Do not turn the computer off.** Call the Office Manager and tell the dispatcher |
| Shared-drive files changing in bulk; sync errors; backup job failure | Suite alert, MSP alert | MSP pauses sync and the backup job; Office Manager opens an incident |
| An authority, train sheet, switch list, or slow order in SYS-01 that nobody entered, or conflict checks behaving oddly | Dispatcher or crew | Treat SYS-01 as untrusted; paper dispatch; call the Office Manager and the operations SaaS vendor |
| Someone clicked a link and typed a password, or approved an MFA prompt they did not start | Employee | MSP resets the password, signs out all sessions, and checks forwarding rules; Office Manager opens an incident (this alone is a TSA-reportable cyber attack; see the 2025 event in P01 R-009) |
| Antivirus or EDR alert that is not cleared automatically | MSP console | MSP isolates the device and calls the Office Manager |
| Email or call from someone claiming to hold company data | Extortion message | Do not reply. Save the message. Declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any device or in the shared drive, when the integrity of SYS-01 data is in doubt because of suspected malicious activity, or when someone claims to hold company data.

**Write down the discovery time** in the incident log. It starts the TSA 24-hour clock (1570.203(a)(1)) and is needed for every other deadline. Florida's 30-day clock for employee notices starts later, at the determination of a breach (Fla. Stat. 501.171(4)(a)).

## 3. First hour: make operations safe, then contain (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Switch to paper dispatch.** Stop issuing authorities in SYS-01. Read the active authorities from the last train sheet or the dispatcher log, then do a **radio roll call** of every train, the hi-rail truck, and every work group to confirm location and authority. Issue no new authority until the roll call is complete. Trains without radio contact stop | General Manager (dispatcher) | Every movement accounted for on paper |
| 2. **Keep radio up.** If the console is down, dispatch on a handheld through the mile 8 repeater, or set up the spare base radio from the enginehouse | General Manager; Mechanic | Dispatcher has radio contact with all movements |
| 3. **Decide today's operating plan.** Whether the interchange turn runs; propane cars stay on the customer's track or in the yard until shipping papers and emergency response information are on paper (P05 BP-04) | General Manager | Plan for the shift set |
| 4. **Tell the Class I** yard office if the interchange turn is delayed, and the car management office if EDI may carry bad data. The Class I dispatcher's authority on the 2.5-mile move is not affected; the crew follows it as usual | General Manager or Office Manager | Class I informed |
| 5. **Isolate.** MSP disconnects affected computers remotely, pauses shared-drive sync on every desktop, and suspends the backup job so it cannot copy encrypted files over good versions. Leave affected computers **powered on** for evidence | Office Manager; MSP | MSP confirms isolation and backup protection |
| 6. **Reset access.** From a clean device (the General Manager's laptop, checked by the MSP), reset passwords and sign out all sessions for the affected user, both SYS-01 administrators, the shared crew login, the suite administrators, the backup console, the firewall, and the telematics portal. Confirm MFA settings were not changed | MSP with the Office Manager | Sessions revoked |
| 7. **Call the cyber insurer's breach hotline** and give the claim details | General Manager | Claim number issued; counsel assigned |
| 8. **Open the incident log:** timeline, actions, who, and when | Office Manager | Log started |

## 4. Report to TSA within 12 hours (RS.CO)
The General Manager, or the Roadmaster as alternate Security Coordinator, calls the TSA Transportation Security Operations Center by the method TSA prescribes (number on the contact card). Do not wait for the investigation to finish. "When in doubt, report" (POL-03 4.4).

The report includes, as available and applicable (49 CFR 1570.203(c)):
1. Name and contact information of the person reporting
2. Affected train, facility, or infrastructure: the Junction office and dispatch desk, the systems affected, and any affected train with its current location
3. Origin and destination of any affected train, and its route (for example the interchange turn to the Class I yard)
4. Description of the incident, who has been notified, and what action has been taken
5. Descriptions of individuals, accounts, or email senders known or suspected to be involved
6. The source of any threat information

Record the call time, the reference given, and the name of the TSA person who took the report. Call again with material updates. If either SSI-marked document in the "TSA" folder, or the hazmat security plan, may have been taken or seen by the attacker, also inform TSA under 1520.9(c) (POL-03 4.5).

## 5. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Scope.** Which computers, accounts, and cloud services are affected? Sources: the MSP antivirus console (EDR once deployed), suite sign-in and file activity logs, the SYS-01 audit trail (from the vendor), firewall logs, and the backup console log.
2. **Initial access.** Find the phishing email, the account used, and the first computer. Search all 7 mailboxes for the same message and remove it. Check whether the MSP's remote tool was used (P01 R-004).
3. **Preserve evidence.** Forensics images affected computers and exports suite, firewall, and SYS-01 logs before they age out. Keep a chain-of-custody record for every image and export.
4. **Operations data integrity.** Ask the operations SaaS vendor to confirm whether any company account changed authorities, train sheets, slow orders, or the hazmat car list during the incident window. **Any SYS-01 data used again must match the paper dispatcher log and a radio roll call.**
5. **Data theft.** Did employee personal information or SSI leave? Check suite download and sharing activity, mailbox forwarding rules, payroll and HR (SYS-08) sign-ins, and large outbound transfers in firewall logs. This drives the Florida breach decision and the 1520.9(c) notice.
6. **Backups.** Before any restore, the MSP confirms which backup versions predate the attack and that the attacker never signed in to the backup console.
7. **Radio and telematics.** The repeater is linked by radio, not by IP, and the telematics units cannot control a locomotive. Confirm the base station still works on the spare console path and change the telematics portal password.

## 6. Containment and eradication (RS.MI)
1. Block the attacker's senders, domains, and IP addresses in the suite and at the firewall (MSP).
2. Disable compromised accounts; remove attacker-added forwarding rules, app consents, and MFA registrations.
3. Wipe and rebuild affected computers from the MSP's standard image. **Do not decrypt and reuse them.** The dispatch desktop is rebuilt with the radio vendor's supported configuration; if the certified console version for a supported operating system is not yet available, the rebuilt desktop stays off the office network until POAM-010 and POAM-011 are done.
4. Confirm with forensics that no persistence remains, including in the MSP's remote management tool, before anything reconnects.
5. If the MSP's own tools may be the entry point, the General Manager asks the insurer's forensic firm to lead eradication and requires the MSP to show its own investigation results (P01 R-004).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6). Paper dispatch continues until the dispatch desk is verified.
1. Radio contact with all trains: handhelds through the repeater or the spare base radio (1 h)
2. Paper dispatch and the security contact card (1 h)
3. Internet and office network: firewall checked and credentials changed; General Manager's phone hotspot until the cellular failover router is installed (2 h)
4. Clean dispatch endpoint with access to SYS-01: the General Manager's laptop, checked by the MSP, then the reimaged dispatch desktop (4 h)
5. Crew tablets: wiped if any doubt, signed back in after the crew password change (8 h)
6. Email and phones: suite accounts cleaned; office line forwarded to the General Manager's cell until then (8 h)
7. Shared drive: restored by the MSP from the newest clean version; staff check the timetable, track charts, and security plan folders before sync is turned back on (48 h)
8. Accounting, payroll, and telematics (72 h)

**Cut back from paper to SYS-01** only when: the dispatch endpoint is clean and patched; every active authority in SYS-01 matches the paper log and a radio roll call; and the General Manager approves. Tell crews, the 6 customers, and the Class I when normal operations resume (RC.CO).

## 8. Notifications (RS.CO)
**Follow `notification-matrix.csv` (19 obligations).** Breach counsel reviews breach notices to individuals before they go out. The TSA call and the Class I call are never held for that review (POL-03 4.6).

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer notified; MSP engaged; Class I told if interchange or EDI is affected | General Manager; Office Manager |
| Within 12 hours (company target; legal limit 24 hours from discovery) | TSA report (1570.203) | General Manager or Roadmaster |
| Same day as the TSA report | Voluntary report to CISA and the FBI (IC3), before any ransom decision | Office Manager with counsel |
| Promptly, if SSI was released | TSA notice under 1520.9(c) | General Manager |
| Immediately, only if a reportable accident or incident occurs (for example during paper dispatch) | National Response Center call (225.9). A hazmat incident under 171.15 within 12 hours | General Manager |
| Within 30 days after month end | FRA monthly report, only if a reportable accident or incident occurred (225.11) | General Manager |
| Day 0-1 | Staff briefing: paper procedures, do not discuss outside the company, send customer and media questions to the General Manager | General Manager |
| Within 30 days of determining a breach | Florida notice to affected current and former employees (about 40 records exist, so the Department of Legal Affairs and consumer reporting agency notices are unlikely to apply). Notices under other states' laws for former employees who moved away | Office Manager with counsel |

**Inbound notices.** If the payroll and HR SaaS, the productivity suite vendor, or the MSP is where the breach happened, it must notify the company no later than 10 days after it determines the breach, as a Florida third-party agent (501.171(6)(a)). The company still sends the notices to individuals.

**Ransom decision:** only the Owner and General Manager, with breach counsel's and the insurer's advice and after an OFAC sanctions check (POL-03 4.8). Paying does not remove any reporting or notice duty.

**Not applicable today:** SD 1580-21-01E reporting to CISA (not in 1580.101 and no TSA designation); the TSA surface cyber NPRM and CIRCIA (proposed only). Recheck if TSA designates the railroad or a final rule is published.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, counsel, and both dispatchers. Written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-002, R-004, R-005, R-006), the POA&M (P07), the contingency plan, and this runbook. Check whether the hazmat security plan needs a cyber update (R-014).
- Give TSA any follow-up information it asks for.
- Keep the incident log, TSA report record, breach assessment, notices, and forensic report for at least 3 years (POL-02 A.7).

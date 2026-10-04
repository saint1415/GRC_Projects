# Incident Response Runbook: Ransomware Spreading from Business IT toward Field SCADA

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer, one field) |
| Tier / Vertical | Micro / Mining, Quarrying, and Oil and Gas Extraction |
| Incident type | Ransomware that starts with a phishing email on a field office PC and spreads across the flat field office network to the SCADA host (and its attached USB backup) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 (sections 3.3.8, 6.4, 6.5) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office Manager (Security Coordinator), with the Field Superintendent for field steps |
| Approved | 2026-08-31 by the Owner |
| Last tested | Not yet. First tabletop with the MSP and the SCADA integrator due 2026-11-30 (POAM-012) |

**The one rule that overrides everything below: safety first.** The hardwired safety shutdowns (H2S detection, tank high-level, SWD pump high-pressure) do not depend on SCADA. Never disable, bypass, or reset them as part of incident response. If anyone is unsure whether a site is safe, the Field Superintendent shuts it in under the emergency response plan.

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The MSP does the office technical work, the SCADA integrator does the SCADA work, and the cyber insurer supplies breach counsel and forensics. The Office Manager runs the incident and keeps the log; the Field Superintendent runs the field.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Owner | Cell phone (printed contact card) |
| Decision maker (money, ransom, outside statements) | Owner | Office Manager | Cell phone |
| Field and OT decisions (isolation, manual operations, shut-ins) | Field Superintendent | Field Technician; on-call Lease Operator for isolation only (POL-03 4.4) | Cell phone; field radio |
| Office technical response | MSP 24x7 emergency line | MSP lead technician's cell | Phone only |
| SCADA technical response | SCADA integrator emergency number | Integrator's lead technician | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance broker | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel counsel; panel forensic firm (confirm OT capability, POAM-012) | n/a | Assigned by the insurer on the first call |
| Production accounting vendor and bank | Vendor support line; bank fraud line | Account managers | Numbers in the binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** staff member → Office Manager (or Field Superintendent in the field) → MSP line and Field Superintendent, at the same time → Owner calls the insurer hotline → counsel and forensics through the insurer → integrator if the SCADA host is involved. The bank is called at once if there is any sign that email or production accounting credentials were used.

**Out-of-band first.** Assume email is compromised. Coordinate by cell phone, text, and field radio, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at both offices and in each field truck: this runbook, the contact card, the isolation decision table (section 3), the notification matrix, and the manual-operations route sheet
- [ ] SCADA host backup on a rotated encrypted drive kept at the main office, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-003 and POAM-004 close**
- [ ] Firewall between the field office PCs and the SCADA host (SC-7). **Gap until POAM-002 closes**
- [ ] EDR with after-hours alerting (SI-4). **Gap until POAM-009 closes**
- [ ] Integrator's always-on tool removed; vendor sessions through the MFA session tool (AC-17). **Gap until POAM-001 closes**
- [ ] Network cable to the SCADA host labeled "SCADA: pull to isolate" at the field office switch, with this step taped next to it
- [ ] Sealed SCADA host administrator password in the main-office safe (POL-02 B.8)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Files will not open, names changed, or a ransom note on any computer | Staff report; antivirus alert | **Unplug the network cable or turn off Wi-Fi. Do not turn the computer off.** Call the Office Manager |
| HMI shows a ransom note or unfamiliar screens, freezes, or wells start or stop without a command | Lease Operator, Field Technician | Call the Field Superintendent at once; go to section 3 |
| SCADA vendor text "connector offline" outside a known outage | On-call phone | On-call Lease Operator checks the field office; start 2-hour patrols (BP-01) |
| Staff member clicked a link and typed a password | Staff report | MSP resets the password and signs out all sessions; check forwarding rules |
| Email or call claiming to hold company or owner data | Extortion message | Do not reply; save it; declare an incident |
| Bank or vendor reports an unusual payment or bank detail change | Bank; production accounting | Office Manager calls the bank fraud line; declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any device, or someone claims to hold company data.
**Declare an OT incident as well** when any sign of the attack appears on the SCADA host, the engineering laptop, or a controller.
**Write down the time of discovery.** Florida's 30-day clock for individual notices runs from the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(4)), and counsel needs the timeline.

## 3. First hour (RS.MA, RS.MI)
### 3.1 Isolation decision table
| Situation | Decision | Who decides |
|---|---|---|
| Ransomware on an office PC; SCADA host looks normal | **Pull the SCADA host network cable now** (its polling of the radio base keeps working on the direct serial link) and unplug the field office router from the internet. Alarm call-out stops, so start 2-hour patrols | Field Superintendent; Field Technician or on-call Lease Operator if the Field Superintendent cannot be reached in 15 minutes (POL-03 4.4) |
| Signs on the shared field desktop or engineering laptop, SCADA host looks normal | Same as above; unplug the affected computer as well. Do not plug the engineering laptop into anything | Same |
| SCADA host affected, or staff cannot trust what the HMI shows | **Go to manual operations.** Twice-daily routes, hand gauging, local start and stop; SWD facility run from its local PLC panel with a Lease Operator on site. Do not send commands from the affected HMI | Field Superintendent |
| Any doubt about site safety | Shut in the affected site under the emergency response plan | Field Superintendent |

Field controllers run their own logic and the safety shutdowns are hardwired, so isolating or losing the SCADA host does not stop the wells by itself. What stops is remote visibility (BP-03, MTD 72 hours) and after-hours alarm call-out (BP-01, MTD 4 hours). Produced water storage lasts about 12 hours (BP-02), so the SWD facility must be watched on site from the start.

### 3.2 First-hour steps
| Step | Who | Done when |
|---|---|---|
| 1. Disconnect affected computers; leave them powered on for evidence | Staff, guided by the Office Manager | Devices offline |
| 2. Apply the isolation decision table; record the time | Field Superintendent | SCADA host isolated or confirmed clean |
| 3. Start 2-hour patrols of the tank battery, SWD facility, and the 6 sour wells nearest homes; SWD on local panel if needed | Field Superintendent; Lease Operators | Patrol schedule running |
| 4. Call the MSP emergency line; MSP isolates office devices remotely and suspends the cloud backup job so it cannot overwrite good versions | Office Manager; MSP | MSP confirms |
| 5. Call the insurer's breach hotline | Owner | Claim number issued; counsel assigned |
| 6. Reset passwords and sign out all sessions for the affected user and all administrators (suite, production accounting, mobile viewer, backup console); confirm with the bank that no ACH batch is pending | MSP with the Office Manager; Production Accountant | Sessions revoked; bank confirmed |
| 7. Open the incident log: timeline, actions, who, when | Office Manager | Log started |

## 4. Analysis (RS.AN)
Led by the forensic firm through counsel, with the MSP and the integrator supplying access and logs.
1. **Scope.** Which computers, accounts, and services are affected? Sources: MSP antivirus or EDR console, suite sign-in and file activity logs, production accounting user activity, the SCADA host event log (export it at once; it overwrites), and the router.
2. **Initial access.** Find the phishing email, the account, and the first computer. Search all mailboxes for the same message and remove it.
3. **Path to SCADA.** Check the shared field desktop for the saved remote desktop shortcut and recent connections to the SCADA host; check the integrator's tool for sessions; confirm the 2022 port forward is still gone.
4. **OT integrity.** The Field Technician, with the integrator, compares the SWD PLC, tank battery PLC, and a sample of pump-off controllers against the saved program copies (once POAM-003 provides them; until then, the integrator's archive). Check the SCADA vendor cloud audit report for setting changes.
5. **Personal information.** Did owner or employee data leave? Check the laptops and shared drive for owner exports, suite download and forwarding activity, and production accounting export history. **This drives the Florida and other-state breach decision.**
6. **Backups.** Before any restore, confirm which cloud backup versions predate the attack and that the backup console was not used by the attacker. The USB drive attached to the SCADA host must be treated as compromised.
7. **Preserve evidence.** Forensics images affected computers and exports logs with a chain-of-custody record. Evidence collection never delays a safety action.

## 5. Containment and eradication (RS.MI)
1. Keep the SCADA host isolated until eradication is confirmed on both the office and field side.
2. Block attacker senders, domains, and addresses in the suite and at both offices' internet connections.
3. Disable compromised accounts; remove attacker-added forwarding rules and MFA registrations; rotate the HMI operator password, the field Wi-Fi password, and the SCADA host administrator password.
4. Wipe and rebuild affected office computers from the MSP's standard image. **Do not decrypt and reuse them.**
5. Rebuild an affected SCADA host with the integrator on clean hardware (the spare PC) from the verified rotated backup. Reload controller programs only from verified copies. **Never run a decryptor on the SCADA host.**
6. Confirm with forensics that no persistence remains, including in the MSP's remote management platform and the integrator's tool, before reconnecting anything.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews every legal notice before it goes out. No binding federal cyber incident reporting rule applies to the company (P03 section 1); the clocks below come from environmental law, Florida and other state law, and contracts.

| When | Action | Owner |
|---|---|---|
| Immediately, if any oil reaches water | Oil discharge notice to the National Response Center (40 CFR 110.6), plus any state notice in the emergency response plan | Field Superintendent |
| Hour 1 | MSP and integrator engaged; insurer notified; counsel and forensics assigned | Office Manager; Owner |
| Day 0-1 | Voluntary report to CISA and the FBI, before any ransom decision (timely reporting is an OFAC mitigating factor) | Owner with counsel |
| Day 0-1 | Crude purchaser told if loads will be missed; partners told if their data or wells are affected | Owner |
| Day 0-1 | Staff briefing: what happened, manual operations, do not discuss outside the company | Field Superintendent; Office Manager |
| As soon as scope is known | Breach determination for owner and employee data, documented with counsel; count affected people by state | Office Manager with counsel |
| Within 30 days of determination | Florida individual notices (501.171(4)), unless counsel supports a documented no-harm determination, which must then go to the Department of Legal Affairs within 30 days; other states' notices per each state's law | Office Manager and counsel |
| Within 30 days, if ever triggered | Department of Legal Affairs notice only if 500 or more Floridians are affected (501.171(3)); consumer reporting agencies only if more than 1,000 are notified (501.171(5)). **Neither is reachable with today's records** | Office Manager and counsel |
| Per license | Seismic data licensor told if licensed data was exposed | Owner |

**Inbound notices.** If the breach happened at the production accounting vendor, the payroll service, or the MSP, the vendor must tell the company within 10 days of its determination (501.171(6)). The company still sends the notices to individuals.

**Ransom decision:** only the Owner, with counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.8). Paying does not remove notice duties if data was taken, and a decryptor never runs on the SCADA host.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Field safety call-out: on-call Lease Operator and 2-hour patrols (immediate)
2. SWD facility on its local PLC panel (6 h)
3. SCADA host from the verified rotated backup on clean hardware, with the alarm connector to the vendor cloud (24 h target; untested until POAM-004 closes)
4. Field radio base and cellular modems checked (24 h)
5. Smartphones and email for run ticket photos (24 h; paper run tickets until then)
6. Production accounting access from a clean laptop (72 h)
7. Bank portal, payables, payroll (72 h)
8. Shared drive restored by the MSP from the newest clean version (120 h)

**Before reconnecting the SCADA host:** the Field Superintendent and the Office Manager both confirm that office computers are clean, passwords are rotated, controller programs match verified copies, the SCADA vendor connector is send-only, and the integrator's access is through the MFA session tool (or disabled until POAM-001 closes). The Field Superintendent declares the return to normal remote operations and tells field staff, the purchaser, and the partners (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, the integrator, and counsel. Written summary within 30 days (POL-03 4.11).
- Update the risk register (P01, especially R-001, R-002, R-003, R-019), the POA&M (P07), the emergency response plan, and this runbook.
- Keep the incident log, breach determination, notices, and forensic report for at least 5 years (POL-02 A.7).

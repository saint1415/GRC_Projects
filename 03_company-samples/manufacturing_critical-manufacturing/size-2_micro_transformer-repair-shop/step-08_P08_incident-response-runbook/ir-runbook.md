# Incident Response Runbook: Ransomware Disrupting Production of Grid Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (transformer repair and remanufacturing shop, Florida) |
| Tier / Vertical | Micro / Critical Manufacturing |
| Incident type | Ransomware that starts from a phishing email, encrypts the office computers and the synced shared drive, and reaches the test PC and the oven HMI over the flat network, stopping shipments of rebuilt distribution transformers during hurricane season |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 section 6.4 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office Manager (Security Coordinator), with the Shop Manager for the shop equipment sections |
| Approved | 2026-08-31 by the Owner |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POL-03 4.11) |

## 0. Roles and notification chain (Govern)
The shop has 7 people and no IT staff. The MSP does the technical work on computers and the network; the cyber insurer supplies breach counsel and forensics; the oven OEM and the test set vendor help with their equipment. The Office Manager runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Owner | Cell phone (numbers on the printed contact card) |
| Decision maker (money, ransom, shutdown, customer promises) | Owner | Shop Manager | Cell phone |
| Shop safety and equipment restart | Shop Manager | Lead Winder | Cell phone; in person |
| Technical response (computers, network, suite) | MSP incident line (24x7 emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel counsel; panel forensic firm | n/a | Assigned by the insurer on the first call |
| Oven controls | Oven OEM support line | n/a | Number on the oven panel and in the binder |
| Test PC | Test set vendor support line (business hours) | n/a | Number in the binder |
| Cooperative security contact | Per the exhibit | Cooperative account manager | Number and email in the binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** employee → Office Manager → Shop Manager (shop safety) and MSP incident line and Owner (at the same time) → insurer breach hotline (Owner) → breach counsel and forensics (through the insurer).

**Out-of-band first.** Assume email and the suite are compromised. Coordinate by phone and text on personal phones, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the office and in the Owner's truck: this runbook, contact card, notification matrix, notice templates (cooperative, contracting officer, employees), paper travelers, paper test forms, and the oven OEM's printed recipe sheet
- [ ] Separate shop equipment network, so the test PC and oven HMI are not reachable from office computers (SC-7). **Gap until POAM-003 closes (2026-12-31)**
- [ ] Oven OEM modem on a keyed switch and powered off (MA-4). **Gap until POAM-006 closes (2026-10-31)**
- [ ] ERP export, nightly test database copy, OT program copies, and a restore tested within the last 90 days (CP-9). **Gap until POAM-007 closes (2026-12-31)**
- [ ] MSP-managed EDR with after-hours alerting (SI-3, SI-4). **Gap until POAM-009 closes (2026-12-31)**
- [ ] ERP MFA and named MSP logins with MFA (IA-2(1)). **Gap until POAM-002 closes (2026-09-30)**
- [ ] Unplug points labeled: the cable modem, the firewall's link to the Wi-Fi access point, the test PC network cable, the oven HMI network cable
- [ ] Insurer hotline number and policy number checked at each renewal; the insurer knows MFA is not yet on the ERP

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Files will not open, names changed, or a ransom note appears on any computer | Employee report | **Unplug the network cable or turn off Wi-Fi. Do not turn the computer off.** Call the Office Manager |
| The test PC or oven HMI screen is locked, shows a note, or settings change on their own | Field Service and Test Technician; oven operator | **Step back and do not touch the controls.** Call the Shop Manager, who calls the Office Manager |
| Shared drive files changing in bulk; sync errors; backup job failures | Suite alert; MSP alert | MSP pauses sync and the backup job; Office Manager opens an incident |
| Antivirus or EDR alert that is not cleared automatically | MSP console | MSP isolates the computer and calls the Office Manager |
| An employee clicked a link and typed a password | Employee report | Office Manager has the MSP reset the password and sign out all sessions; check sign-in logs and forwarding rules |
| Email or call from someone claiming to hold shop data | Extortion message | Do not reply. Save the message. Declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any computer or in the shared drive, when the test PC or oven HMI shows unauthorized changes, or when someone claims to hold shop data. The Office Manager declares, or the Owner if she cannot be reached.

**Write down two times.** Each starts a clock:
- **Confirmation** of an incident related to the services supplied to the cooperative starts the cooperative's **72-hour** notice clock (exhibit sec. 1). Section 4 step 5 decides whether it applies.
- **Determination** of a breach of employee personal information, or reason to believe one occurred, starts Florida's **30-day** clock (Fla. Stat. 501.171(4)).

## 3. First hour: safety, isolation, and calls (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safe state.** <br>- *Drying oven:* if the PLC is running normally, let the cycle finish under an operator's watch at the panel; otherwise follow the OEM's safe-shutdown steps. <br>- *Oil rig:* stop. <br>- *Test bay:* stop any test and de-energize. <br>- *Winding machine:* stop at the end of the current layer | Shop Manager with the operators | Every area in a known safe state, logged with times |
| 2. **Isolate the shop equipment.** Unplug the test PC and oven HMI network cables. Make sure the OEM modem is powered off | Shop Manager | Shop equipment has no network path |
| 3. **Isolate the office.** Unplug affected computers, leaving them powered on for evidence. MSP isolates computers remotely, pauses shared drive sync, and suspends the backup job so it cannot copy encrypted files over good versions. If spread continues, unplug the cable modem | Office Manager with the MSP | Spread stopped; backup protected |
| 4. **Call the insurer's breach hotline.** Engage counsel and forensics through the insurer | Owner | Claim number issued |
| 5. **Protect accounts.** Reset passwords and sign out all sessions for the affected user and all administrators (ERP, suite, AI portal, backup service); confirm MFA is intact; use the sealed emergency credential if needed (POL-02 B.10) | MSP with the Office Manager | Sessions revoked |
| 6. **Go manual.** Paper travelers and the printed schedule; hold new job releases; paper test forms only for units the Shop Manager can test from the test set's front panel | Shop Manager | Paper workflow running |
| 7. **Start the incident log:** timeline, decisions, who, and when (paper if needed) | Office Manager | Log open |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Scope.** Which computers, accounts, and cloud services are affected? Sources: MSP antivirus or EDR console, suite sign-in and file activity logs, ERP audit trail, firewall logs. **Export the firewall logs at once: they keep only 7 days** (POAM-003).
2. **Shop equipment.** Did the attacker reach the test PC or the oven HMI, or only office computers? The Shop Manager compares oven settings with the OEM's printed recipe sheet, and the test PC's latest results with the copies in the shared drive. **No shop equipment is trusted until checked.**
3. **Initial access.** Find the phishing email, the account used, and the first computer. Also check the MSP's RMM tool, the test PC (exposed to the internet until 2026-08-11), and the oven modem. Search all mailboxes for the same message and remove it.
4. **Preserve evidence** before any wipe (POL-03 4.10): images of key computers, the test PC disk, and the suite and firewall logs, with a chain-of-custody record.
5. **What was taken.** Did the rewind data sheet library, the federal order folder (FCI), cooperative site data, or HR files leave? Check suite download and sharing activity, forwarding rules, and outbound transfers in firewall logs. Were the field laptop or a badge holder's credentials exposed? **This drives the cooperative, Florida, and contracting officer decisions.**
6. **ERP.** The ERP is SaaS and is usually unaffected. The Office Manager asks the ERP vendor to check for unusual sign-ins, exports, or deletions from the shop's accounts.
7. **Backups.** Before any restore, the MSP confirms which backup versions predate the attack and that the backup service was not accessed by the attacker.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's senders, domains, and IP addresses in the suite and at the firewall (MSP).
2. Disable compromised accounts; remove attacker-added forwarding rules, app consents, and MFA registrations. Change every shared password (test PC, Wi-Fi, alarm code if it was stored on a computer).
3. **Rebuild, do not decrypt and reuse.** The MSP wipes and rebuilds affected office computers from its standard image.
4. **Test PC.** Rebuild with the test set vendor from its media, or move to the replacement PC if delivered (POAM-008). Restore the test database only from a copy that predates the attack.
5. **Oven HMI.** The OEM reloads the HMI project and checks the PLC program and recipes against its records. Until copies exist (POAM-007), this depends on the OEM.
6. Confirm with forensics that no persistence remains, including in the MSP's RMM platform, before reconnecting anything. If the MSP's own tools may be the entry point, the Owner asks the insurer's forensic firm to lead eradication and requires the MSP to share its own investigation results (P01 R-009).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every legal notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | MSP engaged; insurer notified; counsel and forensics assigned | Office Manager; Owner |
| Day 0 | Staff briefing: what happened, manual steps, report anything odd, do not post online; send customer and media questions to the Owner | Office Manager |
| Day 0-1 | Voluntary report to the FBI (IC3 or field office) and CISA, as counsel advises. Make it before any ransom decision: full and timely reporting is an OFAC mitigating factor | Owner with counsel |
| Day 0-1 | Delivery-impact calls to utilities with open storm orders, then other customers with due dates | Owner |
| **Within 72 hours of confirmation** | **Incident notice to the cooperative** if the incident relates to the services the shop supplies (section 4 step 5). If unsure, counsel decides early. The deadline is a contract term | Office Manager with counsel |
| Within 1 business day | Access-revocation notice to the cooperative if a badge holder's credentials or field laptop may be compromised | Office Manager |
| Within 1 business day of identification | FAR 52.204-25(d) report to the contracting officer if covered equipment is identified during the rebuild | Office Manager |
| As soon as the delay is known | Contracting officer told of any delivery impact on the federal order (no cyber incident reporting duty under FAR 52.204-21) | Owner |
| Within 30 days of determination | Florida notice to affected current and former employees (fewer than 500, so no Department of Legal Affairs notice) | Office Manager with counsel |
| Ongoing | Coordinate with the cooperative until closure (exhibit sec. 2) | Office Manager |

**Not required:**
- **No CIRCIA report.** The rule is proposed only; report voluntarily instead.
- **No DFARS report.** The shop has no DoD work.
- **No FAR 52.204-21 incident report.** The clause has no reporting paragraph.
- **No DOE-417 or NERC report.** The shop is not a utility or a NERC-registered entity.

**Inbound notices.** If the MSP or the payroll service is where the breach happened, Florida law requires it to notify the shop within 10 days of its determination (501.171(6)(a)). The shop still sends the notices to employees.

**Ransom decision:** only the Owner, with breach counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty.

**Storm season.** If a hurricane watch covers a utility customer's service area during the incident, the Owner tells that utility within 24 hours how many storm-stock units are tested and ready to ship, and how many are waiting for test reports. This is a business commitment, not a legal deadline.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6). **No shop equipment restarts until the Shop Manager has checked its settings and programs (POL-03 4.4).**
1. **Shop safety:** oven and test bay already in a safe state (step 1).
2. **Internet and network:** firewall checked and credentials changed; shop equipment stays unplugged from the office network. Phone hotspots if the line is down. 2 hours.
3. **Clean office computers:** rebuilt desktops; laptops checked by the MSP. 4 hours.
4. **Test PC and test set (BP-04, RTO 8 hours; 3 to 5 days today):**
   - rebuild or replace, then restore the latest clean test database copy;
   - the Shop Manager checks the last day's results against the front-panel readings before any report is signed;
   - until then, paper test forms and a report template on a clean laptop, signed by the Shop Manager.
5. **ERP (BP-01, BP-05, RTO 8 hours):** vendor-hosted; confirm the shop's accounts are clean; re-key paper travelers and shipments made since the incident.
6. **Email and shared drive:** suite accounts cleaned; forwarding rules removed; restore the shared drive from the newest clean backup version and check key folders (rewind library, federal order folder, test report copies) before turning sync back on. 8 hours.
7. **Oven controls (BP-03, RTO 12 hours):** OEM verifies the PLC program and recipes; Shop Manager approves restart.
8. **Winding machine programs (BP-02):** from the Lead Winder's USB stick after it is scanned on a clean computer. 24 hours.
9. **Field laptop and AI portal (BP-06):** rebuilt laptop; portal password changed. 24 hours.
10. **Billing and payroll (BP-08):** payroll service repeats the prior payroll if needed. 72 hours.

**Before reconnecting any device:** antivirus or EDR shows clean, passwords are changed, and patches are current.

**Communicate restoration (RC.CO):**
- Tell staff when each function is back.
- Tell utilities, other customers, and the contracting officer when shipments resume.
- Send a final update to the cooperative if it received the 72-hour notice.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and counsel. Written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-002, R-003, R-009, R-024), the POA&M (P07), the BIA recovery times (P05), and this runbook.
- Keep the incident log, notices, and forensic report for at least 5 years (POL-02 A.7), or longer if counsel or the insurer requires.

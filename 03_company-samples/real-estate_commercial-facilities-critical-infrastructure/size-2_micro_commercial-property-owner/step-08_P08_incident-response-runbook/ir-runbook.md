# Incident Response Runbook: Ransomware on Building Automation Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| Tier / Vertical | Micro / Commercial Facilities |
| Incident type | Ransomware on the BAS: entry through the controls contractor's remote-desktop access to the BAS front-end workstation, spreading over the Property A network to office computers and the synced shared drive, with possible theft of leasing files |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT safety steps from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Property Manager (security and privacy lead) |
| Approved | 2026-08-31 by the Managing Member |
| Last tested | Not yet. First tabletop with the MSP and the controls contractor due 2026-11-30 (POAM-008) |

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The MSP handles office IT, the controls contractor handles the BAS, and the cyber insurer supplies breach counsel and forensics. The Property Manager runs the incident and keeps the log; the Building Engineer keeps the buildings safe.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Property Manager | Managing Member | Cell phone (printed contact card) |
| Decision maker (money, ransom, closures, public statements) | Managing Member | Property Manager | Cell phone |
| Building safety and manual operation | Building Engineer | A Maintenance Technician trained on manual operation (R-017) | Cell phone |
| Office IT response | MSP incident line (24x7 emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| BAS response | Controls contractor emergency line | Contractor service manager | Phone only |
| Access control and video platform | Vendor support line | Security integrator | Phone; vendor security contact in the subscription terms |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel counsel; panel forensic firm | n/a | Assigned by the insurer on the first call |
| Law enforcement | FBI field office or IC3; CISA | Local police (physical security issues) | Numbers in the binder |
| Night entrance coverage | Local guard company (on call) | n/a | Number in the binder |

**Notification chain in the first hour:** staff member → Property Manager → Building Engineer, MSP incident line, and Managing Member (at the same time) → controls contractor → insurer breach hotline (Managing Member) → breach counsel and forensics (through the insurer).

**Out-of-band first.** Assume email and the shared drive are compromised. Coordinate by phone and text on personal phones, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the management office and at the Property Manager's and Managing Member's homes: this runbook, the contact card, the notification matrix, the tenant contact list, manual operating notes, and sealed break-glass credentials (POL-02 B.7)
- [ ] Contractor remote access only through the approved service with MFA and per-session approval (MA-4). **Gap until POAM-003 closes**
- [ ] MFA on platform administrators and the backup console (IA-2(1)). **Gap until POAM-002 closes**
- [ ] Immutable 90-day backups; BAS workstation image restored within the last 90 days; controller program copies on file (CP-9, CP-4). **Gap until POAM-007 and POAM-008 close**
- [ ] Building devices on their own network segment (SC-7). **Gap until POAM-004 closes**
- [ ] EDR with after-hours alerting on office computers and the BAS workstation (SI-3, SI-4). **Gap until 2026-12-31**
- [ ] Spare laptop pre-imaged by the MSP and kept by the Building Engineer
- [ ] Insurer hotline and policy number checked at each renewal

## 2. Detection and declaration (Detect)
| Trigger | Source | First action |
|---|---|---|
| Ransom note or locked screen on the BAS workstation; BAS graphics will not open | Building Engineer or technician | **Unplug the workstation's network cable. Do not turn it off.** Call the Property Manager and the Building Engineer |
| HVAC setpoints or schedules change by themselves; many alarms at once or no alarms at all | Building Engineer; tenant complaints | Building Engineer checks the plant in person; treat as a possible incident |
| A contractor session nobody scheduled; the contractor says it was not them | Building Engineer; controls contractor | Disable the contractor account; disconnect the workstation |
| Files renamed or will not open in the shared drive; sync errors | Staff; suite alert | MSP pauses sync and the backup job; Property Manager opens an incident |
| Antivirus alert on an office computer that is not cleared automatically | MSP console | MSP isolates the computer and calls the Property Manager |
| Email or call claiming to hold company or tenant data | Extortion message | Do not reply. Save it. Declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any device or in the shared drive, or when someone claims to hold company data.

**Write down two times.** The time the incident was first reported starts the internal clock and the 72-hour lease notice clock (plan from discovery). The date the company determines that a breach of personal information occurred, or has reason to believe one did, starts Florida's 30-day clock (Fla. Stat. 501.171(4)(a)). Record both in the log.

## 3. First hour (Respond: contain and keep the buildings safe)
| Step | Who | Done when |
|---|---|---|
| 1. **Safety check.** Confirm the rooftop units are running; switch them to hand operation at the units if the field controllers misbehave. Walk both Property A entrances and the Property B service doors to confirm they lock and release correctly. Fire alarm and elevators are on separate systems: do not touch them | Building Engineer with a Maintenance Technician | Cooling confirmed; entrances checked |
| 2. Disconnect the BAS workstation and any affected office computer from the network; leave them powered on for evidence. Field controllers keep running their last programs | Building Engineer; staff guided by the Property Manager | Devices offline |
| 3. Call the MSP incident line: isolate office computers remotely, pause shared-drive sync, suspend the backup job so it cannot overwrite good versions, and block the remote-desktop tool at the firewall | Property Manager; MSP | MSP confirms isolation and backup protection |
| 4. Call the controls contractor: disable the shared contractor account, confirm whether any session was theirs, and stand by to come on site | Building Engineer | Account disabled; contractor's answer logged |
| 5. Call the insurer's breach hotline and give the claim details | Managing Member | Claim number issued; counsel assigned |
| 6. From a clean device (spare laptop or a phone), sign in to the access control platform with break-glass credentials if needed, check the administrator change log, reset administrator passwords, and confirm MFA | Property Manager | Platform administrators confirmed |
| 7. Open the incident log: timeline, actions, who, when | Property Manager | Log started |

## 4. Analysis (Respond: analyze)
Led by the forensic firm through breach counsel, with the MSP and the controls contractor supplying access and logs.
1. **Scope.** Which devices and accounts are affected: the BAS workstation, office computers, suite accounts, the platform, the backup console? Sources: MSP antivirus console, suite sign-in and file activity logs, firewall logs (7 days only, so export them at once), the remote-desktop service's connection history (30 days), and the platform's administrator log.
2. **Initial access.** Confirm how the attacker got in: the contractor account (which password, from where), a phishing email, or another path. Ask the remote-desktop vendor, through the contractor, for connection records.
3. **Preserve evidence.** Forensics images the BAS workstation and affected computers and exports logs before they age out. Keep a chain-of-custody record.
4. **BAS integrity.** The controls contractor compares the supervisory controller and field controller programs with its copies. Any unexplained change is treated as attacker activity and reversed before automatic control resumes.
5. **Data theft.** Did the leasing folder, HR files, or email leave? Check suite download and sharing activity, forwarding rules, and large outbound transfers in firewall logs. **This drives the Florida decision.** Count affected people by state of residence.
6. **Backups.** Before any restore, the MSP confirms which versions predate the attack and that the backup console was not used by the attacker.

## 5. Containment and eradication (Respond: mitigate)
1. Keep the BAS workstation off the network. Run the buildings on field controller programs and hand operation until a clean workstation is ready.
2. Remove the always-on remote-desktop tool from every device. Contractor access resumes only through the approved remote access service (POL-02 B.8).
3. Reset every password the attacker could have seen: the BAS workstation, supervisory controller, suite administrators, platform administrators, backup console, and Property A firewall. Remove attacker-added forwarding rules, app consents, and MFA registrations.
4. Wipe and rebuild affected office computers from the MSP's standard image. **Do not decrypt and reuse them.**
5. Rebuild the BAS workstation (section 7, priority 5) from clean media or a pre-attack image, on the new building-device segment if it is ready.
6. Confirm with forensics that no persistence remains, including in the MSP's remote management platform, before reconnecting anything. If the MSP's or contractor's own tools were the entry point, the forensic firm leads eradication and the provider must show its own investigation results (P01 R-010, R-011).

## 6. Reporting and communication (Respond: report and communicate)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 1 | MSP and controls contractor engaged; insurer notified; counsel and forensics assigned | Property Manager; Managing Member |
| Same business day | Service notice to all tenants if HVAC or access is degraded: what tenants will notice, what to do, when the next update comes. Do not speculate about cause | Property Manager |
| Within 24 hours of declaration | Voluntary report to CISA or the FBI (IC3), as counsel advises, and before any ransom decision | Managing Member with counsel |
| Day 0-1 | Staff briefing: what happened, manual operation duties, do not discuss outside the company, send tenant and media questions to the Managing Member | Property Manager |
| Within 72 hours of discovery | Notice to tenants whose leases (signed since 2024) require it if their employees' data in the access control system may have been accessed. Send the same notice to tenants on older leases | Property Manager with counsel |
| As soon as scope is known | Record the Florida determination date; decide with counsel whether notice is required; count affected people by state | Property Manager with counsel |
| No later than 30 days after the determination | Notice to each affected Florida resident (guarantors, applicants, employees); Department of Legal Affairs only if 500 or more Floridians; consumer reporting agencies only if more than 1,000; other states as each requires | Property Manager and counsel |
| If card data or the terminal is involved | Processor and acquirer notice per the merchant agreement and PIM (not expected: the terminal is stand-alone on cellular) | Bookkeeper |

**Inbound notices.** If the incident started at a vendor that holds personal information for the company (property management system, payroll service, tenant screening service, access control platform, backup), it must notify the company within 10 days of its determination as a Florida third-party agent (501.171(6)(a)); the company still sends the notices to individuals.

**Face match data.** If the access control platform reports a breach that includes face match templates from the June to July 2026 trial, treat them as biometric personal information for notice purposes until counsel decides otherwise (P10).

**Ransom decision:** only the Managing Member, with breach counsel's and the insurer's advice and after an OFAC sanctions check (POL-03 4.8). Paying does not remove notice duties if data was taken, and it does not restore controller programs.

## 7. Recovery (Recover)
Restore in BIA priority order (P05):
1. Administrator accounts and one clean laptop: break-glass credentials, password resets, MFA confirmed
2. Property A firewall and network: rules checked, credentials changed, building devices separated (temporary rules if the segment is not built yet)
3. Tenant communications: email and tenant portal from clean devices
4. Access control administration: platform reviewed, credentials issued since the attack checked against request forms; on-call guard at night until done
5. BAS workstation: restored from the newest clean image to the spare laptop or rebuilt by the controls contractor; controller programs verified against the contractor's copies; supervised automatic control resumed one rooftop unit at a time while the Building Engineer watches
6. Cameras: confirm recording at both properties
7. Work orders on clean tablets
8. Rent and accounting from the Bookkeeper's rebuilt desktop
9. Shared drive: restored by the MSP from the newest clean version; staff check the leasing and HR folders before sync is turned back on
10. Card terminal and payroll (normally unaffected)

**Before reconnecting any device:** antivirus or EDR shows clean, passwords are changed, patches are current, and the device sits on the right network segment. Tell staff and tenants when services are back. Keep manual operation until each function meets its RTO in P05.

## 8. Post-incident (Identify: improve)
- Lessons-learned meeting within 14 days of recovery, with the MSP, the controls contractor, and counsel. Written summary within 30 days (POL-03 4.13).
- Update the risk register (P01, especially R-001, R-002, R-003, R-004), the POA&M (P07), and this runbook.
- Keep the incident log, the Florida determination record, notices, and the forensic report for at least 5 years (POL-02 A.7; 501.171(4)(c)).

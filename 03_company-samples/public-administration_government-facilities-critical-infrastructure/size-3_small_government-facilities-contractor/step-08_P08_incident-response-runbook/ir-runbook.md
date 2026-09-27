# Incident Response Runbook: Intrusion into Building Access Control and Automation Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings) |
| Tier / Vertical | Small / Government Services and Facilities |
| Incident type | Unauthorized access to the BAS supervisory platform, access control tenants, or site OT networks, for example through the integrator's remote-support tool or a stolen technician credential, leading to door schedule changes, setpoint changes, or theft of cardholder data |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (Information Security Officer) |
| Approved | 2026-08-31 by the Chief Operating Officer |
| Last tested | Not yet. First tabletop with the county due 2026-11-30 (POAM-016) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | Chief Operating Officer | ROC line, then the out-of-band group on personal phones |
| Operations lead (building safety) | Director of Operations | Controls Engineering Manager | Cell |
| BAS technical lead | Controls Engineering Manager | Senior BAS controls technician | Cell |
| Access control technical lead | Security Systems Supervisor | Security systems technician | Cell |
| Customer liaison | Site Manager of the affected contract | Director of Operations | Cell; customer contact list in the incident binder |
| Contract and FAR notices | Contracts Manager | Chief Operating Officer | Cell |
| Legal counsel and forensics | Outside counsel and an OT-capable responder through the insurer's panel | n/a | Insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can see company email and chat. Coordinate on personal phones and the printed contact list. **Customer security staff are part of the response**: they control guards, lobbies, and lock-downs at their buildings.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at the ROC and each site office: this runbook, contacts, customer notice terms, manual-mode procedures, emergency revoke lists
- [ ] All remote access through the jump host; integrator tool removed (AC-17). **Gap until POAM-001 closes**
- [ ] Named BAS accounts; no default passwords (IA-2, IA-5). **Gap until POAM-002 and POAM-003 close**
- [ ] Known-good copies of controller programs and door schedules in the central repository, with hashes (CP-9). **Gap until POAM-007 closes**
- [ ] Logs from the jump host, access control portal, supervisory server, and edge firewalls kept 1 year (AU-11). **Gap until POAM-015 closes**
- [ ] Manual-mode procedures for each state and county building (CP-2). **Gap until POAM-008 closes; the federal building has them**
- [ ] OT-capable responder confirmed with the insurer (IR-7)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Doors unlocked outside schedule, or schedule changed with no ticket | Access control alarms; customer security staff | ROC confirms with the Site Manager; if no authorized change, declare |
| Setpoints, schedules, or programs changed with no ticket; equipment running oddly (all air handlers off, chillers cycling) | BAS alarms; building engineers | Controls lead checks the audit trail; if unexplained, declare |
| Remote session nobody booked; integrator tool active outside a visit | Jump host, edge firewall, workstation check | Disconnect; declare |
| Administrator account created or cardholder export run by an unknown user | Access control audit trail | Disable the account; declare |
| Customer or GSA reports suspicious activity | Customer IT or security | Declare and start the notice clocks |

**Declare an incident when** any change to a door, schedule, setpoint, program, or account cannot be tied to an approved ticket, or an unknown remote session reached a site network.

**Record the time of discovery.** It starts the 24-hour customer clocks, the "immediately" clock for GSA, and the Florida 10-day third-party agent clock once a breach of personal information is determined.

## 3. First hour: make the buildings safe, then contain (RS.MA, RS.MI)
**Safety comes before evidence.** Wrong door states and HVAC settings affect people now.

| Step | Who | Done when |
|---|---|---|
| 1. Tell the customer's security staff and Site Manager what is happening; agree on door posture (for example lock exterior doors to scheduled state, post guards at key entrances) | Site Manager | Customer security acknowledges |
| 2. Put affected BAS equipment in local or manual mode per the building recovery procedure; restore safe setpoints at the controller | Operations lead with building engineers | Building conditions stable |
| 3. Cut remote paths: disable the integrator tool, shut client VPN routes, and block site tunnels to the supervisory server if it may be compromised. Controllers keep running on their last programs | IT/OT Systems Administrator | No remote session into any site |
| 4. In the access control platform, disable any unknown or suspect administrator accounts, force password resets for all company administrators, and export the audit trail | Security Systems Supervisor | Accounts disabled; audit export saved |
| 5. Call the cyber insurer's hotline; engage counsel and an OT-capable responder through the insurer | Chief Operating Officer | Claim number issued |
| 6. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

**Do not** reboot or re-download controllers, wipe the supervisory server, or restore backups yet. That destroys evidence and may push a tampered program to more devices.

## 4. Analysis (RS.AN)
1. **Scope:** which sites, controllers, doors, and accounts were touched? Compare door schedules and controller programs against the last known-good copies. Check jump host recordings, edge firewall logs, the access control audit trail, and cloud audit logs.
2. **Initial access:** the integrator tool, a technician credential, a default controller password, or the county network? Get the integrator's own logs through the subcontract.
3. **Preserve evidence:** image the county engineering workstation and the supervisory server VMs (cloud snapshots). Export logs before retention expires (the edge firewalls keep only about 7 days). Keep chain of custody.
4. **Data theft:** was the cardholder list, badge photos, or the **face template set** exported? Were drawings or GSA CUI in file storage accessed? **This drives the breach determination.**
5. **Reach into GSA:** did the attacker use or obtain credentials of any of the 16 staff with GSA access, or touch GSA CUI? If there is any chance, **report to GSA IT immediately** (BTTRG 1.6.1). GSA handles its own systems.
6. **Supply chain angle:** if the entry point was equipment or software, check it against FAR 52.204-25, 52.204-23, and FASCSA orders; the clause clocks start at identification.

## 5. Containment, eradication, and restoration of control (RS.MI)
1. Remove the integrator remote-support tool permanently. Rebuild the county engineering workstation from a clean image.
2. Rotate every credential the attacker could have seen: shared BAS passwords, controller passwords, access control administrator accounts, VPN profiles, integrator accounts.
3. Rebuild the supervisory server from a clean image and restore its database from a backup dated before the first malicious action.
4. Restore controller programs and door schedules from the known-good repository, **verifying hashes**, one site at a time, with the building engineer on site to watch equipment behavior.
5. Have the customer's security staff walk every changed door and confirm the correct state.
6. Confirm with the responder that no persistence remains (scheduled tasks, new accounts, remote tools) before reconnecting sites.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice about personal information.

| When | Action | Owner |
|---|---|---|
| Immediately | Report to GSA IT if GSA systems, data, CUI, or staff credentials may be involved | Site Manager (Federal) |
| Within hours, and no later than 24 hours after discovery | Notice to the county and/or state agency under the contract. Include the facts the customer needs for its own state report: summary, last backup date and location, data types, estimated fiscal impact | Site Manager; IT Manager |
| Customer's clock | County and state must report to the Cybersecurity Operations Center and FDLE within 48 hours (12 hours for ransomware) of discovery (Fla. Stat. 282.3185(5); 282.318(3)(c)9.c.). The company's notice must leave them time | Site Manager |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA, coordinated with the customer | IT Manager |
| As soon as known | Breach determination for personal information (face templates, cardholder data, employee data), with counsel | Chief Operating Officer and counsel |
| No later than 10 days after breach determination | Third-party agent notice to the customer with all information it needs (Fla. Stat. 501.171(6)(a)). The 24-hour contract notice already started this conversation | Chief Operating Officer |
| No later than 30 days after determination | Individual notice for the company's own employee data if affected; Department of Legal Affairs if 500+ (Fla. Stat. 501.171(3)-(4)) | Chief Operating Officer and counsel |
| One business day / 3 business days | FAR 52.204-25(d) / 52.204-23(c) and 52.204-30(c) reports if covered equipment or articles are identified | Contracts Manager |
| Within 1 week after remediation | Input to the county's after-action report (Fla. Stat. 282.3185(6)) | IT Manager |

**Plan to the shortest clock.** The contract clocks (24 hours, or immediately for GSA) run first and must feed the customers' own 48-hour and 12-hour state reports.

**Ransom demands.** Florida state agencies, counties, and municipalities may not pay a ransom (Fla. Stat. 282.3186). The company will not pay on a customer's behalf. Any payment for the company's own systems needs the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying would not remove any notice duty.

**Public records.** Incident reports to the customer may become public records unless an exemption applies. Mark security details (door layouts, vulnerabilities) as exempt security system information (Fla. Stat. 119.071(3)(a)) and let the customer's custodian decide on requests.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Identity provider and administrator access (break-glass if needed)
2. ROC connectivity and the jump host (rebuilt; the only remote path)
3. Access control administrator access; re-verify all door schedules and recent cardholder changes
4. BAS supervisory server; bring sites back one at a time from manual mode
5. CMMS work order flow
6. Video management and exports
7. Controller program repository
8. Reporting and invoicing

**Validate before reconnecting each site:** credentials rotated, programs match the hashed known-good copies, door states walked by customer security, and the edge firewall allows management traffic only from the jump host. Tell the customer in writing when each site returns to normal operation (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting with each affected customer within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-003, R-005, R-019), the POA&M (P07), the subcontractor terms, and this runbook.
- Keep all incident records at least 3 years, or longer where a contract or the customer's public records schedule requires (POL-01 4.11).

# Incident Response Runbook: Intrusion into Building Access Control and Automation Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed facilities support contractor operating government buildings) |
| Tier / Vertical | Mid-Market / Government Services and Facilities |
| Incident type | Unauthorized access to the BAS clusters, access control tenants, or site OT networks, for example through a subcontractor's remote-support tool at a County B site, a stolen technician credential, or a device with a default password, leading to door schedule changes, setpoint changes, or theft of cardholder data and face templates |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions, with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-ransomware.md` (ransomware with data theft in the corporate and cloud environment); `notification-matrix.csv`; BIA (P05); manual-mode (building recovery) procedures |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. OT tabletop with County A scheduled 2026-11-18 (POAM-012) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so building safety, technical, and business and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, VP Operations, Director of Building Technology, HR Director, affected program manager | Customer communications at executive level, external statements, contract and insurance decisions, resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. OT Security Engineer, Controls Engineering Manager, Security Systems Manager, IT Director, MSSP, the insurer's OT-capable responder (through counsel), access control SaaS vendor contact | Containment, investigation, eradication, restoration of control |
| **Building operations command** | VP Operations (lead), ROC Manager, affected program manager and site managers, the customer's facilities director and security staff | Safe state of each affected building, manual-mode operation, guard posts, door lock-downs |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | ROC line, then the out-of-band group on personal phones |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Operations lead (building safety) | VP Operations | ROC Manager | Cell |
| OT technical lead | Director of Building Technology | OT Security Engineer | Cell |
| Breach and notice decisions | General Counsel | Outside breach counsel (insurer panel) | Out-of-band group |
| Customer liaison | Program manager of the affected contract | VP Operations | Cell; customer contact list in the incident binder |
| Contract and FAR notices | Contracts Director | General Counsel | Cell |
| Forensics (OT-capable) | Insurer panel responder, engaged by counsel | MSSP incident response team (IT parts) | Insurer hotline |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the incident binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can see company email, chat, and the CMMS. Coordinate on personal phones and the printed contact list. **Customer security staff are part of the response.** They control guards, lobbies, and lock-downs at their buildings.

**Legal privilege protocol.** General Counsel engages the forensic responder through the insurer panel and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from conclusions. Do not speculate in writing.

## 1. Preparation checks (Identify / Protect)
- [x] Printed incident binder at both ROCs, each regional office, and each site office: this runbook, contacts, the notification matrix, emergency revoke lists, and manual-mode procedures where they exist
- [x] Broker with MFA, approval, and recording for company staff at all 46 sites (AC-17)
- [ ] All subcontractor remote access through the broker; tools removed (AC-17, MA-4). **Gap until POAM-001 closes (2026-12-31)**
- [ ] No default or shared device credentials (IA-5, IA-2). **Gap until POAM-002 and POAM-003 close**
- [ ] Known-good controller programs and door schedules in the repository, with hashes (CP-9, SI-7). **Gap until POAM-020 and POAM-014 close**
- [ ] BAS, tenant, and OT sensor events in the SIEM (AU-2, SI-4). **Gap until POAM-011 closes; until then the OT Security Engineer reviews them weekly**
- [ ] Manual-mode procedures for every County A, County B, City, and school site (CP-2). **Gap until POAM-009 and POAM-010 close; federal and state sites have them**
- [x] Insurer panel OT-capable responder confirmed; contact list verified 2026-09-15
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Doors unlocked outside schedule, or schedule changed with no ticket | Access control alarms at the ROC; customer security staff | ROC confirms with the site manager; if no approved change, declare |
| Any command to the elections warehouse voting equipment cage doors | Tenant alert (from 2026-10-15) | Declare immediately; Supervisor of Elections annex notice within 1 hour |
| Setpoints, schedules, or programs changed with no ticket; equipment running oddly (all air handlers off, chillers cycling) | BAS alarms; building engineers; weekly change report | Controls lead checks the cluster audit trail; if unexplained, declare |
| Remote session nobody booked; subcontractor tool active outside a visit; new device or modem on an OT network | Broker, edge firewall, OT sensors, panel inspection | Disconnect; declare |
| Administrator account created, or a bulk cardholder or face template export, by an unknown user | Tenant audit trail | Disable the account; declare |
| Customer, subcontractor, or GSA reports suspicious activity | Customer IT or security; subcontractor notice | Declare and start the notice clocks |

**Declare an incident when** any change to a door, schedule, setpoint, program, or account cannot be tied to an approved ticket, or an unknown remote session or device reached a site network.

**Severity 1 (escalate to the CMT within 1 hour, POL-03 4.5):** a confirmed intrusion into customer OT, any unauthorized door or cage command, or a suspected breach of cardholder data or face templates.

**Record the time of discovery in the incident log.** It starts every contract clock (6 hours for suspected ransomware at County A, 24 hours for other County A, state, County B, and City incidents, 48 hours for the school district, immediately for GSA) and, through the customers, their own 12-hour and 48-hour state reports.

## 3. First 4 hours: make the buildings safe, then contain (RS.MA, RS.MI)
**Safety comes before evidence.** Wrong door states and HVAC settings affect people now.

| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Tell the customer's security staff and facilities director what is happening; agree on door posture (for example lock exterior doors to their scheduled state; guards at key entrances) | Program manager | Customer security acknowledges |
| 0-30 min | Put affected BAS equipment in local or hand mode; restore safe setpoints at the controller; protect critical rooms first | VP Operations with site engineers | Building conditions stable |
| 0-60 min | Cut remote paths: disable the subcontractor tool at the workstation, block its relay at the edge firewall, suspend broker sessions to the affected sites, and block tunnels from a cluster that may be compromised. Controllers keep running on their last programs | OT Security Engineer | No remote session into any affected site |
| 0-60 min | In the affected tenant, disable unknown or suspect administrator accounts, force password and key resets for all company and subcontractor administrators, and export the audit trail before anything else changes | Security Systems Manager | Accounts disabled; audit export saved with a hash |
| 0-60 min | Call the insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages the OT-capable responder | General Counsel | Claim number; counsel on the call |
| 1-2 h | Convene the CMT; first situation report (sites affected, safety status, data at risk, notices due and when) | CMT chair | CMT meeting held |
| 1-2 h | Check the other customers: same subcontractor, same tool, same credentials? If yes, start this runbook for them too | OT Security Engineer | Exposure list per customer |
| 2-4 h | Staff briefing script (text and phone): what happened, do not discuss externally, report anything unusual, call-back rule for any "vendor" call | VP Operations with HR | Script sent |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner for severity 1 | CEO | Notice given |

**Do not** reboot or re-download controllers, wipe a cluster or workstation, or restore backups yet. That destroys evidence and may push a tampered program to more devices.

## 4. Analysis (RS.AN)
1. **Scope.** Which sites, controllers, doors, and accounts were touched? Compare door schedules and programs against the last known-good copies. Use broker recordings, edge firewall logs, the tenant audit trail, cluster audit trails, OT sensor data, and cloud audit logs.
2. **Initial access.** A subcontractor tool, a technician credential, a default device password, the County B office network (flat site), or a modem? Get the subcontractor's own logs through the subcontract; if the subcontract lacks a cooperation clause (SUB-4 to SUB-7 today), counsel requests them in writing.
3. **Preserve evidence.** Image the engineering workstation and snapshot the cluster virtual machines. Export edge firewall logs before local retention (14 days) expires. Record chain of custody: who collected, when, hash, and where stored. The responder holds evidence under counsel.
4. **Data theft.** Were cardholder records, badge photos, or **face templates** exported? Were drawings, security system layouts, or GSA CUI in file storage accessed? **This drives the breach determination.**
5. **Spread to other customers.** The same subcontractor serves the City and County B. The same tenant platform serves all four state and local customers. Check each for the same indicators.
6. **Reach into GSA.** Did the attacker use or obtain credentials of any of the 152 staff with GSA access, or touch GSA CUI? If there is any chance, **report to GSA IT immediately** (BTTRG 1.6.1). GSA handles its own systems.
7. **Supply chain angle.** If the entry point was equipment or software, check it against FAR 52.204-25, 52.204-23, and FASCSA orders; the clause clocks start at identification, including when a subcontractor tells the company.

## 5. Containment, eradication, and restoration of control (RS.MI)
1. Remove the subcontractor's tool permanently. Rebuild the engineering workstation from a clean image. Move the subcontractor onto the broker before it returns (POAM-001).
2. Rotate every credential the attacker could have seen: device passwords at the affected sites (into the vault), cluster accounts, tenant administrator accounts, VPN and broker credentials, subcontractor accounts.
3. Rebuild the affected cluster from a clean image and restore its database from a backup dated before the first malicious action.
4. Restore controller programs and door schedules from the repository, **verifying hashes**, one site at a time, with the building engineer on site watching equipment behavior. Where no repository copy exists, use vendor commissioning files and treat the site as high risk until reprogrammed.
5. Have the customer's security staff walk every changed door and confirm the correct state and schedule.
6. The responder confirms no persistence remains (scheduled tasks, new accounts, remote tools, modems) before sites reconnect.

## 6. Legal, regulatory, and customer communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel confirms every notice about personal information and keeps the **decision log**.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Time of discovery (contract clocks) and time of breach determination (Florida 10-day and 30-day clocks) | General Counsel | Decision log |
| D2 | Was personal information accessed? Cardholder names with credential data, badge photos, face templates (treated as biometric data; whether templates computed from camera images fall within the Fla. Stat. 501.702 exclusion for data generated from video is unsettled, so counsel confirms), or employee data | General Counsel with the responder | Decision log |
| D3 | Which customers are affected, and is each a covered entity or governmental entity under Fla. Stat. 501.171? Counsel confirms; the company acts as third-party agent either way | General Counsel | Customer notice log |
| D4 | Residency of affected people (Florida and other states) | General Counsel | Affected individuals list |
| D5 | Has law enforcement asked for a delay of individual notice? (Fla. Stat. 501.171(4)(b) requires a written request) | General Counsel | Decision log |
| D6 | Is any covered telecommunications, video, Kaspersky, or FASCSA item involved? | Contracts Director | FAR report log |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Immediately | Report to GSA IT if GSA systems, data, CUI, or staff credentials may be involved | Federal Program Manager |
| Within 1 hour | Supervisor of Elections notice if the voting equipment cage doors or their log are involved | County A Program Manager |
| Within 6 hours (County A, suspected ransomware) or 24 hours (County A other incidents; state, County B, City) or 48 hours (school district) | Contract notice to each affected customer, with the facts the customer needs for its own report: summary, last backup date and location, data types, estimated fiscal impact | Program manager with General Counsel |
| Customer's clock | Counties and the City report to the Cybersecurity Operations Center, FDLE, and the sheriff within 48 hours of discovery (12 hours for ransomware) (Fla. Stat. 282.3185(5)); the state agency reports within 48 hours (12 hours for ransomware) (Fla. Stat. 282.318(3)(c)9.c.). The company's notice must leave them time | Program manager |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA, coordinated with the customer | Security Manager through General Counsel |
| 1 business day / 3 business days | FAR 52.204-25(d) report / 52.204-23(c) and 52.204-30(c) reports if covered items are identified | Contracts Director |
| No later than 10 days after breach determination | Third-party agent notice to each affected customer with all the information it needs (Fla. Stat. 501.171(6)(a)); the earlier contract notice already started this | General Counsel |
| No later than 30 days after determination | If company employee data is affected: individual notice and, if 500 or more Floridians, the Department of Legal Affairs (Fla. Stat. 501.171(3)-(4)); consumer reporting agencies if more than 1,000 | General Counsel |
| Each other state | Residents of other states: apply the law of each state where affected individuals reside | General Counsel |
| Within 1 week after remediation | Input to the county's or city's after-action report to the Florida Digital Service (Fla. Stat. 282.3185(6)) | Security Manager |

**Ransom demands.** An OT intrusion may come with extortion. Florida state agencies, counties, and municipalities may not pay or otherwise comply with a ransom demand (Fla. Stat. 282.3186), and the company will not pay on a customer's behalf. Any payment for the company's own systems follows `ir-runbook-ransomware.md`.

**Public records.** Incident reports to customers may become public records unless an exemption applies. Mark door layouts and vulnerability details as exempt security system information (Fla. Stat. 119.071(3)(a)) and let each customer's custodian decide on requests.

**Communications.**
- Customers: the program manager calls first, then sends the written notice; executive calls from the COO for severity 1.
- Media: holding statement approved by General Counsel and the customer; the customer leads any public statement about its building.
- Staff and subcontractors: out-of-band briefings only.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
| Order | Resource | Target (BIA) | Validation |
|---|---|---|---|
| 1 | Identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 2 | Local operator workstations at the EOC and the state data center building | 0 h (local) | Critical rooms stable throughout |
| 3 | ROC (primary or backup) | 2 h | Alarm consoles show all unaffected sites |
| 4 | Remote access broker (the only remote path) | 2 h | Rebuilt or verified; subcontractor access removed |
| 5 | SIEM and EDR consoles | 4 h | Monitoring confirmed before wider reconnection |
| 6 | Tenant administrator access; re-verify door schedules and recent cardholder changes | 4 h | Customer security walk-through complete |
| 7 | BAS clusters; sites back one at a time from manual mode | 12 h | Programs match hashed copies; equipment behavior normal |
| 8 | CMMS work order flow | 24 h | Tickets reconciled |
| 9 | Video management and exports | 24 h | Evidence exports preserved |
| 10 | Controller program repository | 48 h | Coverage report |

**Validate before reconnecting each site:** credentials rotated, programs match the known-good copies, door states walked by customer security, and the edge firewall accepts management only from the broker. Tell each customer in writing when each site returns to normal operation (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting with each affected customer within 14 days of recovery; written report within 30 days (POL-03 4.11).
- Update the risk register (P01, especially R-001, R-003, R-004, R-005, R-019, R-050), the POA&M (P07), the subcontractor terms, and this runbook.
- Keep all incident records, including the decision log and notices, at least 3 years, or longer where a contract or the customer's public records schedule requires (POL-01 4.12).

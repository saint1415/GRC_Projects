# Incident Response Runbook: Ransomware on Building Automation Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| Tier / Vertical | Small / Commercial Facilities |
| Incident type | Ransomware on the building automation system (BAS), entering through the BAS integrator's remote-support tool, with possible spread to access control, video, and corporate systems |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager |
| Approved | 2026-08-31 by the Chief Operating Officer |
| Last tested | Not yet. First tabletop exercise with engineering and console staff due 2026-11-30 (POAM-019) |

**Safety comes first.** The company's product is safe, cooled, and secure space. In this incident the building keeps running on its own: BAS field controllers keep their last programs and schedules, door controllers cache credentials for up to 72 hours, and life-safety systems (fire alarm, elevators, emergency voice) are on separate networks with only read-only relays into the BAS. Nothing in this runbook touches life-safety systems.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | COO | Incident line (cell), then the out-of-band group chat on personal phones |
| OT safety lead | Director of Engineering | On-duty chief engineer | Cell; engineering radio at each property |
| Physical security lead | Security Manager | Security console shift lead | Security console (24x7) |
| Technical response | MSP incident team | Forensic firm with OT experience (engaged through the insurer's panel) | MSP 24x7 line |
| BAS vendor support | BAS integrator (a clean, known technician, verified by call-back) | Equipment manufacturers' service lines | Numbers in the incident binder, **not** from email |
| Breach and notice decisions | COO with outside breach counsel | Majority owner | Cell; counsel via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Tenant communications | Property Managers (one per property) | COO | Printed tenant contact lists |
| Card payment contacts | Controller | n/a | Acquirer and P2PE provider numbers in the binder |
| Law enforcement and government | FBI field office or IC3; CISA | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the BAS integrator's own systems may be compromised. Coordinate on personal phones, engineering radios, and the printed contact lists in the incident binder at each property.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at each property and at the security console: this runbook, contacts, the notification matrix, tenant contact lists, and the manual operating procedures
- [ ] Manual (degraded-mode) operating procedures for chillers, air handlers, lighting, and doors at each property (CP-2). **Gap until POAM-008 closes (2026-12-31)**
- [ ] Always-on remote-support tool removed; integrators only through the remote access gateway with MFA (AC-17, MA-4). **Gap until POAM-001 and POAM-002 close**
- [ ] Immutable BAS server backups in a separate account, plus current controller programs and graphics, with a restore test in the last 90 days (CP-9, CP-4). **Gap until POAM-004 and POAM-005 close**
- [ ] OT segments with deny-by-default rules (SC-7, AC-4). **Gap until POAM-006 and POAM-007 close**
- [ ] Two break-glass administrator accounts sealed and tested (POL-02 4.7)
- [ ] Two pre-imaged spare laptops for engineering, held by the Director of Engineering (P05)
- [ ] Forensic retainer with OT experience confirmed through the insurer panel (POAM-019)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note or unreadable graphics on the BAS server or an engineering workstation | Chief engineer, engineering staff | Call the incident line and the Director of Engineering. **Do not power off** the server. Unplug the workstation's network cable |
| BAS graphics show setpoints, schedules, or equipment states nobody changed; alarms stop arriving | Chief engineer | Check equipment locally; if confirmed, treat as a BAS compromise |
| Remote-support session nobody approved | Tool console, chief engineer | Call the integrator on a known number to confirm; if not confirmed, disconnect the BAS server network and declare |
| Many files changing at once on file storage or a corporate endpoint | EDR alert (MSP 24x7), backup job failure | MSP isolates the endpoint; IT Manager opens the incident |
| Door controllers offline, badges failing, or unexplained door unlocks | Security console, access control platform alerts | Security Manager checks the platform; guards to affected entrances |
| Extortion email or leak-site post naming the company or its tenants | Email, insurer threat intelligence, law enforcement | Declare; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any system, or an extortion claim names company or tenant data.
**Record two times:** when the incident was discovered, and (later) when the company determined a breach of personal information occurred or had reason to believe one occurred. The Florida 30-day clock runs from the second (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Make the building safe.** Chief engineers check chillers, air handlers, and critical tenant spaces locally; switch plant equipment to local hand control where the BAS is no longer trusted; start hourly manual rounds | Director of Engineering and chief engineers | Each property reports stable cooling and equipment status |
| 2. **Cut the entry path.** Disconnect the BAS server's network at the Property A OT firewall (block all BAS server traffic) and stop the remote-support tool service. Leave the server powered on for memory evidence | IT Manager with the MSP | No traffic to or from the BAS server |
| 3. **Stop spread.** Block routing between corporate and OT segments at Property A; at Properties B and C (flat networks), disconnect the site-to-site VPN and isolate the switch ports of engineering devices | IT Manager with the MSP | Tunnels down; OT ports isolated |
| 4. **Secure the doors.** Confirm door controllers still work on cached credentials; set perimeter doors to scheduled lock; post guards at main entrances with printed tenant lists | Security Manager | Entrances staffed; door status confirmed |
| 5. Call the cyber insurer's breach hotline. Engage counsel and an OT-capable forensic firm through the insurer | COO | Claim number issued |
| 6. Revoke the integrator's and all BAS accounts; reset identity provider administrator credentials (break-glass if needed); revoke all sessions | IT Manager | Sessions revoked |
| 7. Start the incident log: timeline, actions, who, and when. Start the chain-of-custody form | IT Manager | Log open |

**Do not** power off field controllers, door controllers, or NVRs, and do not reset controllers to factory settings. That erases the programs the company does not yet hold copies of (gap under POAM-004).

## 4. Analysis (RS.AN)
1. **Scope:** which systems are affected: BAS server, engineering workstations, historian VM, security console PCs, NVRs, corporate endpoints, cloud file storage, backup vault? Check EDR, identity provider sign-in logs, cloud audit logs, the remote-support tool history, and firewall logs.
2. **Field devices:** with the integrator's clean technician, compare field controller programs at a sample of devices against the last known-good copies. Look for changed setpoints, disabled alarms, or new logic.
3. **Initial access:** confirm the path: integrator credentials used on the remote-support tool, or a compromise at the integrator itself. **Ask the integrator whether other customers are affected.** If the integrator is compromised, treat all of its access as hostile until it proves otherwise.
4. **Preserve evidence:** forensics images the BAS server and affected hosts and exports logs before they roll over (firewall and BAS logs use short default retention; POAM-015). Keep chain of custody.
5. **Personal information:** determine whether the attacker reached any system holding personal information: visitor ID scans (SYS-11), HR and payroll (SYS-12), tenant employee badge records (SYS-02 portal from a console PC), or corporate files in cloud storage. Look for archive or transfer tools and large outbound transfers. **This drives the breach determination (section 6).**
6. **Backups:** confirm the backup vault and the BAS server image are intact before any restore. Today they sit in the production account (gap), so assume they may be deleted or encrypted until checked.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure (IP addresses, domains) at all three firewalls and in the cloud network rules.
2. Uninstall the remote-support tool permanently. Integrator access resumes only through the remote access gateway with named accounts, MFA, and per-session approval (POL-02 4.9).
3. Rotate all OT local passwords, the cloud and identity provider administrator credentials, service accounts, and the historian connection credentials. Change any remaining default passwords.
4. Rebuild the engineering workstations and security console PCs from the standard image. **Do not decrypt and reuse them.**
5. Rebuild the BAS server from a clean image and the vendor's installation media, not from an image that may contain the attacker's tools. Patch before reconnecting.
6. Reload any field controller whose program was changed, from a verified copy supplied by the integrator.
7. Confirm with forensics that persistence is removed before any system reconnects to an OT network.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every legal notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer notified; counsel and forensics engaged | COO |
| Hour 0-4 | Tenant service notice if building services are degraded (lease service interruption clauses): what is affected, what to expect, who to call | Property Managers, approved by the COO |
| Within 24 hours | Voluntary report to CISA and the FBI (CPG 5.B). Supports OFAC mitigation if payment is considered | IT Manager |
| Day 0-2 | Staff briefing script: what happened, manual procedures, do not discuss outside the company, send media calls to the COO | COO |
| Within 72 hours of discovery | If tenant employee data in the access control system may have been accessed: notice to the 12 tenants with 72-hour clauses; notice to all other tenants promptly (contractual) | COO and Property Managers |
| As soon as known | Breach determination under Fla. Stat. 501.171 documented with counsel: was personal information accessed? Record the determination date | COO with counsel |
| Within 30 days of determination | Notice to affected Florida residents; notice to the Department of Legal Affairs if 500+ Florida residents; consumer reporting agencies if more than 1,000 | COO with counsel |
| Within 30 days of a no-harm determination | If counsel supports a written no-harm determination instead of notice: send it to the department and keep it 5 years (501.171(4)(c)) | COO with counsel |
| Only if card data or terminals involved | Acquirer and P2PE provider per the merchant agreement | Controller |

**Two separate questions.** Ransomware that stays on the BAS server encrypts operational data and drawings, which are not personal information under Fla. Stat. 501.171. The Florida notice duties start only if the attacker reached personal information: visitor ID numbers, employee Social Security numbers, account numbers with access codes, biometric data (none collected today), or possibly badge access history if counsel treats it as geolocation information. Tenant notice clauses in leases are contractual and have their own triggers and clocks.

**Ransom decision:** requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove notice duties if data was taken, and it does not restore controller programs that were changed.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6):
1. Identity provider and administrator access (break-glass if needed)
2. Property networks and the OT firewall rules, rebuilt deny-by-default before any OT device reconnects
3. Access control platform administration, from a clean console PC; re-verify door schedules and administrator accounts
4. Clean engineering workstations and security console PCs (2 pre-imaged spares first)
5. BAS server: clean rebuild, restore the BAS database from a verified backup, reconnect field controllers one property at a time, then check each plant system with the chief engineer before leaving hand control (RTO 12 hours; unproven until the first restore test under POAM-005)
6. Video recorders and the console
7. Visitor management
8. Property management system access, then card terminals and payroll if affected

**Validate before reconnecting:** EDR is clean, credentials are rotated, the system is patched, and the chief engineer confirms equipment runs correctly under BAS control. Tell tenants when services are back to normal (RC.CO). Keep manual rounds going until each property has run 24 hours under BAS control without unexplained alarms.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the integrator (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-003, R-015), the POA&M (P07), the manual operating procedures, and this runbook.
- Review the integrator relationship: contract terms, remote access design, and whether the security addendum was met (POL-01 4.8).
- Retain incident records, evidence logs, and any written no-harm determination for at least 5 years (POL-01 4.12).

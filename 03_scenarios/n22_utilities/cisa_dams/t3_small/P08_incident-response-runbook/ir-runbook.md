# Incident Response Runbook: Unauthorized Access to Spillway and Turbine Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensee of the fictional Cypress Fork Hydroelectric Project) |
| Tier / Vertical | Small / Dams |
| Incident type | An unauthorized person gains access to the PCDMS (SCADA, HMI, gate PLC, or unit controls) and views, changes, or operates spillway gates or turbine units. Most likely path today: a stolen on-call operator password on the password-only OT VPN, then the shared HMI account (P01 R-001, R-014) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy; Emergency Action Plan (EAP); FERC Security Plan, Internal Emergency Response sub-element |
| Runbook owners | Plant Manager (OT response) and Chief Dam Safety Engineer (reporting and EAP) |
| Approved | 2026-08-31 by the Vice President of Operations |
| Last tested | Not yet. First tabletop with the sheriff, county emergency management, and the FBI field office due 2026-11-30 (POAM-018) |
| Handling | Mark "Privileged - Security Sensitive Material". Keep printed copies in the control room safe and the Plant Manager's go-bag |

**The one rule that overrides everything else: keep the dam under control.** Put gates and units under local control and confirm their physical positions before doing anything else. Evidence can be lost; people downstream cannot be put at risk.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (first hour) | Operations Supervisor on shift | Senior control room operator | Control room phone; radio channel 1 |
| Incident commander (OT) | Plant Manager | Vice President of Operations | Cell; radio |
| Dam safety, EAP, and FERC reports | Chief Dam Safety Engineer | Compliance and Security Coordinator | Cell |
| OT technical lead | Controls Engineer | I&C technician; SCADA integrator (emergency line) | Cell; integrator 24x7 line |
| IT technical lead | IT Manager | MSP (corporate only) | Cell |
| Law enforcement and FERC security contact | Compliance and Security Coordinator | Operations Supervisor | Cell |
| Legal, insurer, communications | Vice President of Operations | President | Cell; insurer hotline card in the incident binder |
| Outside agencies | County sheriff (911); county emergency management; FBI field office; CISA; FERC Regional Engineer | | Numbers posted in the control room and in the incident binder |

**Out-of-band first.** Assume the attacker can see email and chat, and may see the HMI. Coordinate by radio and personal phones using the printed contact list.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder in the control room safe: this runbook, contacts, notification matrix, local control checklists for each gate and unit, EAP flowchart
- [ ] Operators trained and drilled on running all 4 gates and 3 units from local panels (annual EAP readiness test, 18 CFR 12.25(b))
- [ ] After-hours remote HMI set to view-only until MFA is live (POAM-001 interim). **In place from 2026-09-15**
- [ ] Known-good copies of gate PLC logic, unit PLC logic, governor settings, and HMI projects, stored offline with hashes (POAM-006). **Gap until 2026-11-30**
- [ ] OT firewall change to "isolate" pre-built and tested: blocks all corporate, VPN, vendor, and cloud connections while keeping the control LAN running (POAM-003)
- [ ] OT logging and monitoring (POAM-008, POAM-009). **Gap until 2027-03-31**: until then, detection depends on operators and process alarms
- [ ] OT incident response retainer through the insurer (POAM-018)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A gate moves, or a gate setpoint changes, with no operator command in the control room | Gate position alarm; spillway camera; SCADA event journal | **Local control now** (section 3, step 1). Declare the incident |
| A unit trips, changes load, or its governor settings change unexpectedly | Unit alarms; offtaker call about output | Unit to local control; check the event journal |
| Reservoir level falling or tailwater rising faster than the operating plan | Reservoir and tailwater level alarms; downstream gauge; data acquisition system | Compare with the gate positions seen at the spillway; treat as a possible project emergency (EAP) |
| OT VPN sign-in at an unusual time or from an unusual place, or an HMI session nobody claims | VPN log (once forwarded); an operator notices the HMI mouse moving | Disconnect the VPN at the OT firewall; declare the incident |
| A vendor says it did not start a session that is active | Vendor call | Drop the vendor connection; declare |
| Unknown device on the control LAN, unfamiliar USB drive, or HMI behaving oddly | Operator; I&C technician; OT monitoring (planned) | Isolate the device; call the Controls Engineer |
| Threat or extortion message naming the dam | Email; phone; social media | Preserve; call the sheriff; declare |

**Declare the incident when** any gate or unit command, setpoint change, or program change cannot be tied to an authorized person, or an unauthorized remote session is found. When in doubt, declare. A declaration can be closed later; a late one cannot be undone.

**Record the time of discovery.** The 18 CFR 12.10(a)(1) report to the Regional Engineer is due as soon as practicable after the condition is discovered, preferably within 72 hours. A security incident (physical and/or cyber) is a reportable condition in its own right (12.3(b)(4)(xi)), even if no water was released.

## 3. First 30 minutes (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Local control.** Send operators to the 4 gate panels and 3 unit panels; switch each to local; stop any unplanned movement; return gates to the positions in the operating plan; confirm positions by eye and by the mechanical indicators, not the HMI | Operations Supervisor | Every gate and unit is in local control and its position is confirmed by a person on site |
| 2. **Assess downstream risk.** If a surge or uncontrolled release has happened or may happen, activate the EAP at the right level and sound the sirens | Chief Dam Safety Engineer (Operations Supervisor may activate without waiting) | EAP level declared, or a documented decision that no EAP condition exists |
| 3. **Call the sheriff and county emergency management** in parallel with step 2, as the Internal Emergency Response sub-element requires | Compliance and Security Coordinator or Operations Supervisor | Both agencies notified; times logged |
| 4. **Cut remote paths.** Apply the pre-built "isolate" rule at the OT firewall: drop the OT VPN, vendor connections, corporate access, and cloud replication. Do not power off HMIs or PLCs | Controls Engineer (by phone guidance if off site) | Only the control LAN remains; no external sessions |
| 5. Disable the shared operator account on the VPN and change it on the HMI from the control room console | Controls Engineer | Old credentials no longer work |
| 6. Start the incident log: times, actions, who, gate and unit positions, readings | Operations Supervisor | Log open (paper) |
| 7. Call the Plant Manager, Vice President of Operations, and the cyber insurer hotline | Operations Supervisor; Vice President of Operations | Commanders engaged; claim number issued |

Keep the dam in local control, staffed around the clock, until step 3 of section 7 is complete. The BIA sets a 4-hour limit for all-local gate operation before relief crews are needed (P05, BP-01); call in the next shift early.

## 4. Analysis (RS.AN)
1. **What moved and when.** Pull the SCADA event journal, gate PLC event buffer, governor logs, historian trends, and spillway camera video for the whole period. Build a timeline of every command and position change.
2. **Who and how.** OT VPN connection logs, OT firewall logs, vendor connection records, and corporate identity provider sign-ins for the on-call operators. Because the HMI uses one shared account, identify the operator only from the VPN source and shift records (this is why POAM-002 matters).
3. **What changed.** Compare the running gate PLC logic, unit PLC logic, and governor settings with the known-good offline copies (hash and line-by-line compare). Until POAM-006 closes, the only reference copy is from 2026-04-11 plus the integrator's 2018 project files.
4. **Where else.** Check the engineering workstation, the historian, the DMZ replica, the backup NAS, and the corporate side for the same account or tools. Check the gauge modems and panel web interfaces for sign-ins.
5. **Preserve evidence.** Export logs before they roll over (the SCADA journal keeps 90 days). Image the engineering workstation and HMI drives only when the Plant Manager confirms operations are stable. Keep chain of custody (who collected what, when, hash values). Collected evidence is CEII: store it in the restricted library (POL-04).
6. **Scope decision.** Record in writing whether water was released, whether units were damaged (inspect for water hammer effects), whether personal information was touched, and whether any other system was reached.

## 5. Containment and eradication (RS.MI)
1. Keep the "isolate" rule in place. No remote access, vendor access, or cloud replication until step 5 below is done.
2. Remove the attacker's access: reset every OT credential (VPN, HMI, engineering, panel web, modem, firewall administrator); remove resident vendor tools; block attacker addresses at the corporate and OT firewalls.
3. Reload gate PLC, unit PLC, and governor logic from the verified known-good copy if any difference was found. Changes must be approved by the Plant Manager and tested with gates in local lockout before returning to SCADA control.
4. Rebuild the HMI servers and engineering workstation from clean media if any sign of malware or unknown software is found. The SCADA integrator does the rebuild under the Controls Engineer's supervision.
5. Confirm with the OT incident responder that no persistence remains before reconnecting anything.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Safety reports never wait for counsel. Counsel reviews everything else.

| When (from discovery) | Action | Owner |
|---|---|---|
| Immediately | Sheriff and county emergency management; EAP notifications if a project emergency exists | Compliance and Security Coordinator; Chief Dam Safety Engineer |
| Immediately | Operator of the upstream county water control structure, if flows or coordination are affected (Rev. 3A 4.2) | Operations Supervisor |
| Within the first hours | Offtaker control center (schedule change); cyber insurer hotline | Operations Supervisor; Vice President of Operations |
| As soon as practicable, **preferably within 72 hours** | Initial report to the FERC Regional Engineer by email or telephone under 18 CFR 12.10(a)(1). In practice call the same day | Chief Dam Safety Engineer |
| Usually within **one working day** | Security incident report to the FERC Regional Office (Rev. 3A 3.2, 4.2). Can be the same call as the 12.10 report | Compliance and Security Coordinator |
| Same day, voluntary | FBI field office and CISA; HSIN suspicious activity report | Compliance and Security Coordinator |
| If recreation areas are closed for security | Notice to the FERC Regional Office as soon as practical (usually within one working day); closures over 30 days need prior coordination (Rev. 3A 3.3.4) | Environmental and License Compliance Manager |
| When the Regional Engineer directs | Written 12.10(a)(2) report, verified under 12.13: causes, preceding events, measures taken, damage, injuries, property damage | Chief Dam Safety Engineer |
| Within 30 days of determination, only if personal information was breached | Florida notices under Fla. Stat. 501.171 (individuals; Department of Legal Affairs if 500 or more) | Vice President of Operations and counsel |

**Not required here:** NERC CIP-008 reporting (not a BES facility) and CIRCIA reporting (proposed rule only). Mark all security reports to FERC "Privileged - Security Sensitive Material" and keep security details to what FERC needs.

**Staff and public.** Brief staff that the dam is under local control and safe, and not to discuss the incident outside the company. Public statements come only from the Vice President of Operations, coordinated with county emergency management when the EAP is active.

**Ransom:** if the intrusion comes with an extortion demand, payment needs the President, counsel, the insurer, and an OFAC sanctions check (POL-03 4.9). Paying does not remove any reporting duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Local manual control of gates and units (already in place from section 3)
2. Gate PLC and SCADA supervisory control of gates, from verified logic, tested with gates in local lockout
3. Instrumentation data acquisition and sirens; confirm readings against manual reads
4. Unit control through SCADA
5. Security cameras and card access
6. Offtaker RTU telemetry
7. Corporate email and identity provider access for OT staff
8. Historian replica, cloud reporting, and the instrumentation SaaS feed (one-way only)
9. Remote access: **only through the MFA jump host, never the old VPN profile**. Vendor access last, per session

**Validate before each step:** logic matches the known-good copy; credentials are new; the firewall allows only the flows needed for that step. The Plant Manager signs off each step in the incident log. Tell staff, the offtaker, and (if the EAP was activated) county emergency management when normal operation resumes (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery with operations, security, IT, dam safety, and the outside agencies that responded (POL-03 requires documentation within 30 days).
- Update the risk register (P01: R-001, R-003, R-014), the POA&M (P07), the Security Plan and its Internal Emergency Response sub-element, the Section 9 determination, and this runbook.
- Include the incident and the actions taken in the next Annual Security Compliance Certification Letter, without security-specific details (Rev. 3A 8.0).
- Keep the incident file in the restricted CEII library; keep 12.10 records as permanent project records under 18 CFR 12.12(a)(1)(iii)(B).

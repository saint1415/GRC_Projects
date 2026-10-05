# Incident Response Runbook: Unauthorized Access to Spillway and Turbine Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hydroelectric generation company; 46 developments, 63 dams, 8,640 MW in six states) |
| Tier / Vertical | Enterprise / Dams |
| Incident type | An unauthorized person gains access to plant, gate, or fleet control systems and views, changes, or operates spillway gates or turbine units. The worked example is at **PD-04 Cane Mill Dam** (Security Group 2 dam, 112 MW BES plant with low impact BES Cyber Systems) through a vendor's always-on connection, the path rated Very High in P01 (R-003). The runbook also covers the same event at an HOC-operated plant or at HOC-A or HOC-B (medium impact) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Regulatory Reporting Procedure; PRC-03.4 Local Control Fallback Procedure; the EAPs; the Security Plans' Internal Emergency Response sub-elements; the CIP-008-6 plan |
| Runbook owners | Director of Security Operations (incident commander, security) and Director, Hydro Operations Center (operations), with the General Counsel for section 7 and the Director, NERC Compliance for section 6 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | CIP-008 tabletop 2026-02-24 (HOC scenario; no disclosure committee). OT exercise with the FBI field office and county emergency management 2025-11. **Next:** disclosure committee tabletop with this scenario on 2026-11-18 (POAM-013) |
| Notification matrix | `notification-matrix.csv` (35 obligations: 10 FERC and 18 CFR Part 12, 4 NERC, 5 DOE-417, 4 SEC, 5 state, and 7 other rows for OFAC, CIRCIA status, Balancing Authorities, clients, offtakers, insurance, and FAR status; law enforcement is in the FERC group) |
| Handling | BCSI and "Privileged - Security Sensitive Material". Printed copies in each HOC, each plant control room, and the incident binders |

**The rule that overrides everything else: keep the dams under control.** Put affected gates and units under local control and confirm their physical positions before doing anything else. Operators may do this without approval (POL-03 4.2). Evidence can be lost; people downstream cannot be put at risk.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Operations incident commander | HOC shift supervisor (first hour); Director, Hydro Operations Center | Plant manager of the affected plant | HOC recorded lines; radio |
| Security incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| OT technical lead | Director, OT Security | Director, Hydro Control Systems Engineering; OT incident response retainer firm | Out-of-band group |
| Dam safety, EAP, and 18 CFR 12.10 | Vice President, Dam Safety (Chief Dam Safety Engineer) | Regional dam safety engineer | Direct mobile |
| FERC security reports and law enforcement | Vice President, Corporate Security | Security dispatch supervisor | Security dispatch |
| NERC and DOE reporting | Director, NERC Compliance | NERC compliance analyst on call | Direct mobile |
| Executive incident lead | CISO | CIO | Out-of-band group |
| Crisis management team chair | Chief Operating Officer | Senior Vice President, Hydro Operations (CIP Senior Manager) | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Compliance Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Piedmont plants (until integration) | PD plant manager | Vice President, Integration Management Office | Plant phone; mobile |
| Communications | Vice President, Corporate Communications (coordinated with county emergency management if an EAP is active) | Vice President, Investor Relations | Direct mobile |
| Outside parties | County sheriff and emergency management; FBI field office; CISA; E-ISAC; FERC Regional Engineer; Balancing Authority control rooms; OT retainer; cyber insurer | | Numbers in the incident binder (PD-04 and PD-06 numbers added by 2026-10-31, POAM-013) |

**Out-of-band first.** Assume the attacker can see corporate email and chat and may see the HMIs. Coordinate on recorded HOC lines, radio, and company mobile phones using the printed contact lists.

## 1. Preparation checks (Identify / Protect)
- [ ] Local control checklists for every gated dam and unit, by river system (PRC-03.4), in each control room and the incident binders
- [ ] Operators and plant crews drilled on local gate and unit operation; EAP readiness tested annually (18 CFR 12.25(b))
- [ ] Pre-built "isolate" rule sets at every plant gateway firewall and at the PD legacy VPN concentrator: drop all remote, vendor, and corporate paths while the control network keeps running
- [ ] Known-good copies of PLC, governor, and gate logic with hashes, offline. **Gap at 14 plants until POAM-008 closes; PD plants have only the integrator's copies**
- [ ] OT network monitoring. **Gap at 24 HOC-operated plants and all PD plants (POAM-003, POAM-001)**; detection there depends on operators, process alarms, and firewall logs
- [ ] PD vendor connections disabled outside approved windows (interim since 2026-09-18); cellular datalogger modems disabled (since 2026-09-02)
- [ ] Materiality playbook, 8-K templates, and disclosure committee roster current. **Gap until POAM-013 closes**
- [ ] OT incident response retainer covers the PD platform. **Gap: retainer extension due 2026-12-31 (P05 DEP-25)**

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A gate moves, or a gate setpoint changes, with no operator command | Gate position alarm; spillway camera; SCADA event journal; PD local HMI | **Local control now** (section 3, step 1); declare |
| A unit trips, changes load, or its governor settings change unexpectedly | Unit alarms; Balancing Authority call about output; AGC deviation | Unit to local control; check the event journal; declare if not explained |
| Reservoir falling or tailwater rising faster than the operating plan | Level alarms; downstream gauges; DSMS | Compare with gate positions seen on site; treat as a possible project emergency |
| Remote session nobody claims; vendor says it did not start an active session | Intermediate System dashboard; PD VPN log; vendor call | Drop the session; isolate the path; declare |
| OT sensor alert (new device, unusual protocol command to a PLC) | SOC OT sensors (HOCs and 11 plants) | SOC triage with the HOC within 15 minutes |
| Threat or extortion message naming a dam | Email; phone; social media | Preserve; call law enforcement; declare |

**Declare the incident when** any gate or unit command, setpoint change, or logic change cannot be tied to an authorized person, or an unauthorized remote session is found. When in doubt, declare.

**Record these times separately in the incident log:**
1. **Discovery of the condition** (18 CFR 12.10): starts the "as soon as practicable, preferably within 72 hours" clock.
2. **Determination of a Reportable Cyber Security Incident** (CIP-008-6 for HOC systems; CIP-003-9 Attachment 1 Section 4 for low impact plants such as PD-04): starts the 1-hour E-ISAC and CISA clock.
3. **Materiality determination** (SEC): recorded later by the disclosure committee; starts the 4-business-day Form 8-K clock.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Local control.** Dispatch operators to the affected gate and unit panels; switch to local; stop any unplanned movement; return gates to the operating plan positions; confirm positions by eye and mechanical indicators, not the HMI | HOC shift supervisor; plant crew | Every affected gate and unit in local control with positions confirmed on site |
| 2. **Downstream risk.** If a surge or uncontrolled release has happened or may happen, activate the EAP at the right level and sound sirens | Plant operator or HOC shift supervisor (no need to wait); Vice President, Dam Safety | EAP level declared, or a documented decision that no EAP condition exists |
| 3. **Sheriff and county emergency management**, in parallel with step 2 | Security dispatch | Both notified; times logged |
| 4. **Cut remote paths** at the affected plant: apply the "isolate" rule set; at PD plants, disable the vendor connection and the legacy VPN at the concentrator. Do not power off HMIs or PLCs | OT security team (by phone guidance if off site) | No external sessions remain |
| 5. **Protect the rest of the fleet.** Suspend all vendor sessions fleet-wide at the Intermediate Systems; raise SOC monitoring to the HOC ESPs and plants with sensors; check whether the same vendor or account reaches other plants | Director, OT Security; SOC | Vendor sessions suspended; scope query started |
| 6. Revoke the vendor's and any shared account credentials at the affected plant | OT security team | Old credentials no longer work |
| 7. Notify the Balancing Authority and Transmission Operator of lost capability; notify other dam owners on the river if flows are affected | HOC shift supervisor | Calls logged on recorded lines |
| 8. Start the incident log and evidence register; call the OT retainer and the insurer hotline | Incident commanders | Log open; retainer engaged; claim number |

Plants stay in local control, staffed around the clock, until recovery step validation in section 9. The BIA sets a 4-hour MTD for gate operations at unattended Group 1 and 2 dams (P05 BP-01); call the next crews early.

## 4. Analysis (RS.AN)
1. **What moved and when.** SCADA event journal, PLC and gate controller buffers, governor logs, historian trends, camera video. Build one timeline of every command and position change.
2. **Who and how.** Vendor connection logs, VPN logs, Intermediate System records, firewall logs, OT sensor data where present. At PD plants, shared accounts mean attribution depends on the connection source (R-033).
3. **What changed.** Compare running logic and governor settings with known-good copies (hash and line-by-line). Where copies are stale, use the vendor's original logic plus change records.
4. **Where else.** Same vendor, account, tools, or indicators at other plants, the HOCs, the COC, and the corporate network. Check other PD plants first while POAM-001 is open.
5. **Evidence.** Export logs before they roll over; image engineering workstations and HMIs only when operations confirm they are not needed for control. Chain of custody with hashes. Evidence is BCSI or CEII: store it in the restricted repository.
6. **Scope decision (written):** water released or not; units damaged or not; personal information touched or not; HOC or medium impact systems reached or not. This decides which rows of the notification matrix apply.

## 5. Containment and eradication (RS.MI)
1. Keep the "isolate" rules in place at the affected plant and suspend vendor access fleet-wide until the scope is known.
2. Reset every credential at the affected plant (VPN, HMI, engineering, gateway, panel web interfaces); remove resident vendor tools.
3. Reload logic and governor settings from verified copies where any difference was found; test with gates in local lockout before returning control.
4. Rebuild HMIs and engineering workstations from clean media if any malware or unknown software is found.
5. For PD plants, do not restore the legacy VPN or the vendor's always-on path; restore remote access only through the HOC Intermediate Systems (POAM-001).
6. The OT retainer confirms no persistence before anything is reconnected.

## 6. Regulatory and operational reporting (RS.CO)
**Follow `notification-matrix.csv`.** Safety calls never wait for counsel. The Director, NERC Compliance and the Vice President, Dam Safety join the incident bridge in the first hour.

| When | Action | Owner |
|---|---|---|
| Immediately | Sheriff and county emergency management; EAP notifications if a project emergency exists; Balancing Authority and Transmission Operator by voice | Security dispatch; plant operator; HOC shift supervisor |
| Within 1 hour of determining a Reportable Cyber Security Incident | E-ISAC and CISA notice: CIP-008-6 R4 for HOC systems (required clock); CIP-003-9 Attachment 1 Section 4 for low impact plants such as PD-04 (company procedure uses the same 1 hour) | Director, NERC Compliance |
| Within 1 hour, 6 hours, or later per criterion, **if the company is the filer** | Form DOE-417 (Emergency Alert within 1 hour; Normal Report within 6 hours; attempted compromise by the end of the next calendar day; System Report by the later of 24 hours or the end of the next business day; final within 72 hours). Until the filer role is confirmed, call the Balancing Authority to agree who files | Director, NERC Compliance |
| Same day in practice; preferably within 72 hours | 18 CFR 12.10(a)(1) initial report to the Regional Engineer (a security incident is a reportable condition even if no water was released) | Vice President, Dam Safety |
| Usually within one working day | Security incident report to the FERC Regional Office (can be the same call) | Vice President, Corporate Security |
| By the later of 24 hours or the end of the next business day | EOP-004-4 report if an Attachment 1 threshold is met | Director, NERC Compliance |
| Within 7 calendar days of new information | CIP-008-6 R4.3 updates | Director, NERC Compliance |
| Same day, voluntary | FBI field office and CISA; HSIN suspicious activity report | Vice President, Corporate Security; CISO |
| Within 24 hours of confirmed client impact | SL-1 and SL-2 client notices (contract) | Vice President, Hydro Services |
| When the Regional Engineer directs | Written 12.10(a)(2) report, verified under 12.13 | Vice President, Dam Safety |

Mark all security reports to FERC "Privileged - Security Sensitive Material" and keep security details to what FERC needs. Reports to E-ISAC include functional impact, attack vector, and level of intrusion, as known.

## 7. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 to 6. It does not wait for the investigation to finish: the determination is made without unreasonable delay after discovery, from the perspective of a reasonable investor, using quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.5). An unauthorized gate movement at any dam is always severity 1 | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** for committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 7.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 to 6, including the regulators already notified | Committee | Worksheet completed |
| 7.5 | **Materiality determination** recorded with the date, time, and reasoning, whether material or not yet material. If not yet material, set the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 7.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident and its material impact or reasonably likely material impact. **Do not include technical details that would impede response or remediation, and no BCSI, CEII, or Security Plan details** | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; given the public safety angle of a dam incident, counsel considers whether to request one through the Department of Justice | General Counsel | Filing confirmation |
| 7.8 | Align timing and content with regulator reports, county emergency management messages, client and offtaker notices, and investor messages; brief the audit committee and the safety, risk, and reliability committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 7.9 | Reassess as facts change; counsel decides whether an amended filing is needed (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples the committee considers |
|---|---|
| Public safety | Any uncontrolled release, EAP activation, evacuation, injury, or near miss downstream; recreation closures |
| Operational | MW and units affected and for how long (P05: about $10.0 million of generation value per day fleet-wide; PD-04 alone about $130,000 a day); HOC control lost or not; Blackstart Resources affected |
| Regulatory | 18 CFR 12.10 reports; FERC inspection follow-up; potential NERC CIP violations and penalties (the PD self-reports already filed); DOE or E-ISAC inquiries |
| Contractual | SL-1 and SL-2 clients affected; offtaker and Balancing Authority obligations; insurance coverage |
| Reputation and strategy | National media; effect on relicensing, the Piedmont integration, and future acquisitions; state regulators and communities |
| Data | Any CEII, BCSI, or personal information taken; whether it was published |

**Worked example of the clocks (fictional dates).** Tuesday 2026-10-13, 02:40: the PD-04 night operator sees spillway gate 3 opening with no command. By 02:52 the gate is in local control and closed to the plan position; tailwater rose 1.1 feet and fell back; no EAP condition (documented 03:30 by the Vice President, Dam Safety). Security dispatch calls the sheriff and county emergency management at 02:58. The OT team disables the vendor connection at 03:05 and finds an active session from the vendor's account that the vendor did not start.
- **CIP-003-9 low impact:** at 06:10 the Director, NERC Compliance determines a Reportable Cyber Security Incident (PD-04 is a low impact BES asset). E-ISAC and CISA are notified at 06:55, within the company's 1-hour rule. No HOC system was reached, so CIP-008-6 R4 does not apply; if it had, its 1-hour clock would run from the same kind of determination.
- **18 CFR 12.10:** initial report to the Regional Engineer at 08:15 the same morning, well inside the preferred 72 hours (the outer target was 2026-10-16 02:40).
- **FERC security report:** same call; within one working day.
- **DOE-417:** the unit at PD-04 also tripped at 02:44. The NERC compliance team calls Balancing Authority B at 03:30 to agree who files, since the company's filer role is not yet confirmed.
- **SEC:** the disclosure committee meets Wednesday 2026-10-14 and again Friday 2026-10-16, and determines the incident **material** at 15:00 on Friday, mainly on qualitative grounds (an attacker moved a spillway gate at a Group 2 dam; national media; FERC and NERC follow-up; the open Piedmont self-reports). The Form 8-K is due by **Thursday 2026-10-22** (4 business days: October 19, 20, 21, and 22).
- **Breach laws:** forensics confirms no personal information was touched, so no state notices are needed; counsel documents the decision.

## 8. Ransom or extortion
If the intrusion comes with an extortion demand, payment needs the CEO, the General Counsel, the cyber insurer, and an OFAC sanctions check (POL-03 4.7). Report to the FBI and CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove any reporting or disclosure duty, and no payment ever substitutes for local control of the dams.

## 9. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), validating each step:
1. Local manual control of gates and units (in place from section 3)
2. Gate PLC and supervisory control of gates from verified logic, tested with gates in local lockout; for HOC-operated plants, HOC control from HOC-A or HOC-B
3. Dam safety instrumentation, data acquisition, and sirens; readings confirmed against manual reads
4. ICCP and real-time data to the Balancing Authorities; identity and break-glass access
5. Unit control through SCADA; pumped storage and Blackstart Resource readiness
6. Physical security systems at the affected dam
7. Corporate access for OT staff; scheduling and offtaker communications
8. One-way data to the DSMS and the data platform
9. Remote access: **only through the HOC Intermediate Systems, never the old VPN or vendor tool**; vendor access last, per session

**Validate before each step:** logic matches the verified copy; credentials are new; firewall rules allow only the flows that step needs. The plant manager and the Director, OT Security sign off each step in the incident log. Tell county emergency management (if the EAP was active), the Balancing Authority, clients, and staff when normal operation resumes.

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery with operations, security, dam safety, NERC compliance, and the outside agencies that responded; plan updates within 90 days (CIP-008-6 R3.1).
- Update the risk register (P01: R-003, R-008, R-031 to R-033, R-047), the POA&M (P07), the Security Plan and its Internal Emergency Response sub-element, the Section 9 determination, and this runbook.
- Include the incident and actions in the next Annual Security Compliance Certification Letter without security-specific details (Rev. 3A 8.0).
- Disclosure committee reviews the effect on the next Item 106 disclosure.
- Keep the incident file in the restricted repository; keep 12.10 records as permanent project records (18 CFR 12.12); keep CIP-008 records for the NERC audit period (CIP-008-6 R2.3).

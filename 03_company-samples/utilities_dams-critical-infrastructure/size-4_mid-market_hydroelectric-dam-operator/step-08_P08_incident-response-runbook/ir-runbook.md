# Incident Response Runbook: Unauthorized Access to Spillway and Turbine Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (owner and operator of 4 FERC-licensed hydroelectric projects; RMOS provider) |
| Tier / Vertical | Mid-Market / Dams |
| Incident type | An unauthorized person or process gains access to the HCDMS (ROC SCADA, plant HMIs, gate PLCs, governors, or data acquisition) and views, changes, or operates spillway gates or generating units, at a company dam or an RMOS client project. Most likely paths today: an OEM direct VPN at Pine Hollow or Sawgrass Run, an RMOS client tunnel into the ROC SCADA zone, or an undocumented panel modem (P01 R-001, R-002, R-041) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy; EAPs for all 4 dams; Internal Emergency Response sub-elements (BWB, CDS, PNH); BWB Rapid Recovery sub-element; CIP-003-9 low impact cyber security plan |
| Companion documents | `ir-runbook-ransomware.md` (corporate ransomware with RMOS data theft and forced IT/OT separation); `notification-matrix.csv`; BIA (P05); EAPs |
| Runbook owners | OT Security Manager (technical response) and Chief Dam Safety Engineer (EAP and FERC reporting) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Cyber inject in the BWB Security Plan drill on 2026-10-28; joint OT tabletop with the FBI, county emergency management, and an RMOS client by 2027-03-31 (POAM-008) |
| Handling | Restricted (CEII). Mark "Privileged - Security Sensitive Material". Printed copies in each control room safe and the ROC incident binder |

**The rule that overrides everything else: keep the dams under control.** Put the affected gates and units under local control and confirm their physical positions before anything else. Evidence can be lost; people downstream cannot be put at risk.

## 0. Governance, roles, and contacts (Govern)
Three tiers, so operational, technical, and business and legal decisions each have one owner.

| Tier | Members | Decides |
|---|---|---|
| **Operations command** | Incident commander on shift: ROC shift supervisor, until the Vice President of Generation Operations takes over. Plant Managers, Chief Dam Safety Engineer, ROC Manager | Local control, gate and unit positions, EAP activation, staffing of panels, return to SCADA control |
| **Cyber response team** | Lead: OT Security Manager. OT security engineers, Manager of Controls Engineering, IT Director, MSSP, OT incident response firm (through counsel), SCADA platform vendor | Isolation, investigation, eradication, verification of logic and settings, recovery sequence |
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, General Counsel, CFO, Vice President of Generation Operations, Vice President of Hydro Services, vCISO, Corporate Security Manager, Director of Communications, outside counsel | External statements, client and offtaker decisions, regulatory and legal strategy, resources, board notice |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (first hour) | ROC shift supervisor | Senior ROC operator | ROC console phone; radio channel 1 |
| Incident commander (operations) | Vice President of Generation Operations | ROC Manager | Personal phone; radio |
| Cyber response lead | OT Security Manager | Manager of Controls Engineering | Out-of-band group on personal phones |
| EAP, 12.10, and FERC dam safety contact | Chief Dam Safety Engineer | Plant Manager of the affected dam | Personal phone |
| FERC security contact and law enforcement | Corporate Security Manager | ROC shift supervisor | Personal phone |
| NERC reporting (CIP-003, EOP-004) | NERC Compliance Manager | General Counsel | Personal phone |
| Legal and privilege | General Counsel | Outside counsel (insurer panel) | Out-of-band group |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| RMOS clients | Vice President of Hydro Services | RMOS desk lead | Client duty contact list in the binder |
| Outside agencies | County sheriffs and emergency management (3 counties); FBI field office; CISA; FERC Regional Engineer and Regional Office; E-ISAC | | Numbers posted in every control room and in the binder |

**Out-of-band first.** Assume the attacker can see email and chat, and may see SCADA screens. Coordinate by radio and personal phones from printed lists.

**Legal privilege protocol.** The General Counsel engages the OT incident response firm through outside counsel. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs, gate positions) separate from conclusions. **Safety and regulatory reports never wait for counsel**; counsel reviews everything else.

## 1. Preparation checks (Identify / Protect)
- [ ] Incident binder in every control room safe: this runbook, contacts, the notification matrix, local control checklists for each of the 20 gates and 12 units, EAP flowcharts, the EOP-004 Attachment 2 form
- [ ] Operators drilled on local operation of all gates and units (annual EAP readiness test); 12 more staff cross-trained by 2027-03-31 (POAM-018)
- [ ] OEM VPNs disabled except during approved sessions (interim from 2026-09-15); OEMs on jump hosts by 2026-11-30 (POAM-001)
- [ ] Pre-built "isolate" rules on every site OT firewall and the ROC: drop OEM VPNs, RMOS client tunnels, jump host sessions, corporate access, and the cloud push while keeping site control LANs and the ROC-to-site SCADA links running. Separate rule to cut one site off from the ROC
- [ ] RMOS client tunnel rules narrowed to client SCADA objects (2026-10-15); separate RMOS zone by 2027-03-31 (POAM-002)
- [ ] Known-good copies of gate PLC logic, unit PLC logic, governor and exciter settings, and HMI projects, offline with hashes: **complete for the ROC and BWB only** until 2026-12-31 (POAM-007)
- [ ] OT monitoring at the ROC and BWB; **gap at CDS, PNH, SGR** until 2027-06-30 (POAM-005). Until then, detection there depends on operators and process alarms
- [ ] OT incident response firm on the insurer panel; retainer confirmed annually

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A gate moves, or a gate setpoint changes, with no command from an authorized operator | Gate position alarm; spillway camera; SCADA event journal; plant operator | **Local control now** (section 3, step 1). Declare |
| A unit trips, changes load, or its governor or exciter settings change unexpectedly | Unit alarms; BA/TOP or cooperative calls about output | Unit to local control; check the event journal; declare if unexplained |
| Reservoir falling or tailwater rising faster than the operating plan | Level alarms; river gauges; data acquisition | Compare with gate positions seen on site; treat as a possible project emergency |
| Commands to company objects from an RMOS client tunnel, or a client reports commands it did not send | SCADA journal; client call | Apply the RMOS isolate rule; declare |
| Vendor session nobody approved; OEM VPN up outside an approved window; traffic from a panel modem | Jump host alerts; firewall logs; OT sensors (ROC, BWB) | Drop the session at the firewall; declare |
| Unknown device on a plant LAN, unfamiliar USB drive, HMI behaving oddly | Operator; I&C technician; OT sensor | Isolate the device; call the Manager of Controls Engineering |
| Threat or extortion message naming a dam | Email; phone; social media; FBI | Preserve; call the sheriff and the Corporate Security Manager; declare |

**Declare the incident** when any gate or unit command, setpoint change, or logic change cannot be tied to an authorized person, or an unauthorized remote session is found. When in doubt, declare. Every declared OT incident affecting gates or units is **severity 1**.

**Record three times in the log:** time of discovery (starts the 18 CFR 12.10 clock); time the event was recognized as an EOP-004-4 event type (starts the 24-hour or next-business-day clock); time the CIP-003 plan determination was made (Reportable Cyber Security Incident or not).

## 3. First hour (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | 1. **Local control.** Operators go to the panels of the affected dam (and, if the ROC is suspect, all dams); switch to local; stop any unplanned movement; return gates to the operating plan; confirm positions by eye and mechanical indicators, not by HMI | ROC shift supervisor; Plant Managers | Every affected gate and unit in local control with its position confirmed by a person on site |
| 0-15 min | 2. **Downstream risk.** If a surge or uncontrolled release has happened or may happen, activate the EAP at the right level and sound the sirens. Do not wait for cyber analysis | Chief Dam Safety Engineer (the ROC shift supervisor may activate) | EAP level declared, or a logged decision that no EAP condition exists |
| 0-15 min | 3. Call the county sheriff and emergency management of the affected county in parallel with step 2 (Internal Emergency Response) | ROC shift supervisor or Corporate Security Manager | Both agencies notified; times logged |
| 0-30 min | 4. **Cut remote paths.** Apply the isolate rules: OEM VPNs, RMOS tunnels, jump hosts, corporate access, cloud push. If the attack came through the ROC, cut the ROC from the sites and let each site run locally. Do not power off HMIs or PLCs | OT Security Manager (phone guidance to the ROC if off site) | No external sessions; isolation confirmed at each firewall |
| 0-30 min | 5. Disable suspected accounts (SCADA domain, jump host, HMI shared accounts) and change them from a clean console | OT security engineer | Old credentials no longer work |
| 0-30 min | 6. Tell RMOS clients whose projects the ROC operates to take local control under their operating orders | Vice President of Hydro Services or RMOS desk lead | Each client confirms local control |
| 0-60 min | 7. Call the BA/TOP control center (BWB, CDS output and ICCP status) and the cooperative (PNH, SGR) | ROC shift supervisor | Calls logged |
| 0-60 min | 8. Call the cyber insurer hotline; General Counsel engages outside counsel and the OT incident response firm | Chief Financial Officer; General Counsel | Claim number; counsel engaged |
| 0-60 min | 9. Convene the CMT; first situation report (gates, units, downstream status, clients, decisions needed). CEO informs the audit committee chair and the sponsor within 4 hours | CMT chair | Meeting held |

Keep affected dams in local control, staffed around the clock, until section 7 is complete. The BIA sets about 4 hours of all-local operation before relief crews are needed (P05, BP-01): call in the next shift early, and pre-stage crews if a flood is forecast.

## 4. Analysis (RS.AN)
1. **What moved and when.** Pull the SCADA event journal, gate PLC event buffers, governor and exciter logs, historian trends, and camera video. Build a timeline of every command and position change at each affected dam.
2. **Who and how.** Jump host logs and recordings, OEM VPN and firewall logs, RMOS tunnel logs, OT sensor data (ROC, BWB), identity provider sign-ins of staff with OT access. At PNH and SGR, shared HMI accounts mean attribution depends on network sources and shift records (POAM-004).
3. **What changed.** Compare running gate PLC logic, unit PLC logic, governor and exciter settings, and HMI projects with the known-good offline copies (hash and line compare). For CDS, PNH, and SGR, use the newest verified copy and ask the OEMs for their reference settings (5 governor settings are held only by them until POAM-007 closes).
4. **Where else.** Check every other site and the ROC for the same accounts, tools, or connections; check RMOS client sites through their staff; check river gauge modems and panel web interfaces.
5. **Preserve evidence.** Export logs before they roll over (plant HMI logs at PNH and SGR keep about 14 days). Image engineering workstations and HMI drives only when the Plant Manager confirms operations are stable. Keep chain of custody (who, what, when, hashes). Evidence is CEII: store it in the restricted library.
6. **Scope decisions, in writing:** water released (yes or no, volume); units damaged (inspect for water hammer or overspeed); client works affected; personal information touched; other systems reached; whether the event meets an EOP-004-4 event type (for BWB or CDS) and whether it is a Reportable Cyber Security Incident under the CIP-003 plan.

## 5. Containment and eradication (RS.MI)
1. Keep the isolate rules in place. No vendor access, client tunnels, or cloud push until step 5 is done.
2. Remove attacker access: reset every OT credential (SCADA domain, HMI, jump host, firewall, panel web, modem); remove unauthorized remote tools and devices; block attacker infrastructure at all firewalls.
3. Reload gate PLC, unit PLC, and governor logic and settings from verified copies wherever a difference was found. The Plant Manager approves; test with gates in local lockout before any return to SCADA control.
4. Rebuild SCADA servers, HMIs, or engineering workstations from clean media if any malware or unknown software is found, under the Manager of Controls Engineering with the SCADA platform vendor.
5. The OT incident response firm confirms no persistence before anything reconnects.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Decision points are logged with the decider and time.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is there a project emergency? (EAP) | Chief Dam Safety Engineer; the ROC shift supervisor may activate | EAP log |
| D2 | Is this a condition affecting project safety? Any security incident affecting project works is | Chief Dam Safety Engineer | Decision log with discovery time |
| D3 | Is it a Reportable Cyber Security Incident under the CIP-003 plan (ROC, backup ROC, BWB, CDS)? | NERC Compliance Manager with the OT Security Manager | CIP-003 determination record |
| D4 | Does it meet an EOP-004-4 event type (intentional damage or physical threat at BWB or CDS)? | NERC Compliance Manager | Operating Plan checklist |
| D5 | Was personal information or RMOS client data accessed? | General Counsel | Decision log |
| D6 | Public statement, and coordination with county emergency management | CMT chair | Approved statement |

| When (from the trigger) | Action | Owner |
|---|---|---|
| Immediately | Sheriff and county emergency management; EAP notifications if D1 is yes; RMOS clients to local control; other dam owners if affected (Rev. 3A 4.2) | ROC shift supervisor; Chief Dam Safety Engineer; Vice President of Hydro Services |
| Within the first hours | BA/TOP and cooperative; cyber insurer; audit committee chair and sponsor (within 4 hours) | ROC shift supervisor; CFO; CEO |
| Same day, in practice | **18 CFR 12.10(a)(1) initial report** to the Regional Engineer: required as soon as practicable after discovery, preferably within 72 hours | Chief Dam Safety Engineer |
| Usually within **one working day** | Security incident report to the FERC Regional Office (Rev. 3A 3.2, 4.2); can be the same call | Corporate Security Manager |
| By the later of 24 hours after recognition or the end of the next business day | **EOP-004-4 report** if D4 is yes (Attachment 2 or the DOE-OE-417 form) | NERC Compliance Manager |
| Company rule: within 24 hours of the D3 determination | **E-ISAC notice** if D3 is yes (CIP-003-9 Attachment 1 Section 4.2; the standard sets no fixed deadline) | NERC Compliance Manager |
| Per the DOE-417 criteria clocks, only if the company is a required respondent (to be confirmed) | DOE-417 | NERC Compliance Manager |
| Same day, voluntary | FBI field office and CISA; HSIN suspicious activity report | OT Security Manager through counsel; Corporate Security Manager |
| Within 24 hours (written) | RMOS client written notice | Vice President of Hydro Services |
| When the Regional Engineer directs | Written 12.10(a)(2) report, verified under 12.13 | Chief Dam Safety Engineer |
| If recreation areas are closed | FERC Regional Office as soon as practical (usually within one working day); over 30 days needs prior coordination (Rev. 3A 3.3.4) | Environmental and License Compliance Manager |
| Within 30 days of determination, only if personal information was breached | State notices, Florida as the worked example (individuals; Department of Legal Affairs if 500 or more) | General Counsel |

**Not required:** NERC CIP-008 reporting (no high or medium impact BES Cyber Systems) and CIRCIA reporting (proposed rule only). Mark all security reports to FERC "Privileged - Security Sensitive Material" and limit security details to what FERC needs.

**Staff and public.** Staff hear only that the dams are under local control and safe, and are told not to discuss the incident outside the company. Public statements come only from the CMT, coordinated with county emergency management when an EAP is active.

**Ransom:** if the intrusion comes with an extortion demand, follow POL-03 4.9 (CEO approval, counsel, insurer, OFAC check). Payment does not remove any reporting duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 8), one site at a time:
1. Local manual control of gates and units (in place since section 3)
2. Sirens and data acquisition; confirm readings against manual reads
3. ROC SCADA from verified images, or the backup ROC once confirmed clean (it shares the SCADA domain, P05 finding 2)
4. Site links back to the ROC, one site at a time, with segmented rules
5. ICCP link to the BA/TOP
6. Gate supervisory control from the ROC, from verified logic, tested with gates in local lockout
7. Unit control through SCADA (BWB and CDS first, then PNH and SGR)
8. RMOS client control, one client at a time, after client confirmation and narrowed rules
9. Remote access: **jump hosts only**, staff first, vendors last, per session; no OEM VPNs
10. Historian replica and the one-way cloud push

**Validate before each step:** logic and settings match verified copies; credentials are new; firewall rules allow only the flows needed for that step. The Vice President of Generation Operations signs off each step. Tell staff, clients, the BA/TOP, the cooperative, and (if an EAP was activated) county emergency management when normal operation resumes (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery with operations, dam safety, security, controls engineering, IT, the clients involved, and the agencies that responded; documented within 30 days (POL-03 4.11).
- Update the CIP-003 plan within 180 calendar days if this was a Reportable Cyber Security Incident (CIP-003-9 Attachment 1 Section 4.6).
- Update the risk register (P01: R-001, R-002, R-004, R-041), the POA&M (P07), the Security Plans and their Internal Emergency Response and Rapid Recovery sub-elements, the Section 9 determination, the BWB Vulnerability Assessment update, and this runbook.
- Report the incident in the next Annual Security Compliance Certification Letter without security-specific details (Rev. 3A 8.0).
- Keep the incident file in the restricted library; keep 12.10 records as permanent project records (18 CFR 12.12).

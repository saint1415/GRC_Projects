# Incident Response Runbook 2: Suspected OT Compromise Through a Vendor Remote Connection, with Untrusted SCADA Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed interstate natural gas transmission pipeline operator) |
| Tier / Vertical | Mid-Market / Energy |
| Incident type | An attacker is suspected of reaching OT through a vendor path: the remote access gateway (stolen vendor or staff credentials), the SCADA vendor's support environment, the SCADA integrator, or an undocumented OEM connection like the cellular modem found in P07. What controllers see or what field devices do may no longer be trustworthy |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3 (OT incident response); CSF GV.SC-08 (suppliers in incident planning) |
| Policy basis | POL-02 (remote access and supplier paths); POL-03 (4.4 safety first, 4.5 isolation, 4.6 shutdown decision, 4.7 evidence); STD-04 OT remote access and field device standard; STD-07; TSA Cybersecurity Incident Response Plan (SD Pipeline-2021-02G Section III.F; C-ENERGY-R03); emergency plan (49 CFR 192.615); control room management (192.631; C-ENERGY-R04) |
| Companion documents | `ir-runbook.md` (runbook 1: roles, CMT, communications, and the operate-or-shut-down decision, which this runbook reuses); `notification-matrix.csv`; P01 R-002, R-003, R-011, R-012, R-048; P07 POAM-002, POAM-003, POAM-009, POAM-010, POAM-014 |
| Runbook owner | Director of Gas Control (operations lead), with the Security Manager (incident commander) and the SCADA and OT Engineering Manager (OT technical lead) |
| Approved | 2026-09-17 by the Chief Operating Officer. To be adopted into the TSA Cybersecurity Incident Response Plan by 2026-12-31 (POAM-008) |
| Last tested | Not yet. A controller and station technician tabletop on this scenario is scheduled for 2027-02-17, including the compressor station technicians for the first time (POL-03 4.11; POAM-015) |

## 0. Why this runbook is different from runbook 1
In runbook 1 the attacker is in business IT and the job is to keep it out of OT. Here the attacker may already be **in** OT, through a path the company opened for a supplier. The SCADA screen may be wrong. The first question is not "is OT clean?" but **"can the controllers trust what they see and what the field does?"** Safety comes from the parts of the system that do not depend on SCADA: the hardwired emergency shutdown systems at each compressor station (independent of SCADA and PLC logic), field crews with local gauges, and the manual operation plan.

The P07 assessment found the conditions that make this scenario plausible: an OEM cellular modem at Compressor Station 4 outside the DMZ and the TSA plan (R-003, Very High), an OEM service account with full rights on unit control panels (POAM-002), no OT monitoring at Compressor Stations 2, 4, and 5 (POAM-014), and no PLC logic backups at those stations (POAM-009).

## 1. Roles (Govern)
Use the CMT, IRT, and operations command in runbook 1 section 0, with these differences:

| Role | Primary | Backup | Responsibility in this scenario |
|---|---|---|---|
| Operations lead | Director of Gas Control | Shift supervisor on duty | Leads from the start. Decides isolation, BCC failover, and manual operation; recommends any curtailment to the COO |
| Incident commander | Security Manager | OT Security Engineer | Investigation, vendor coordination, CISA report |
| OT technical lead | SCADA and OT Engineering Manager | OT Security Engineer | Evidence from OT hosts, logic comparison, rebuild |
| Field verification lead | VP Operations | Area Managers; Compressor Station Supervisors | Local readings, station checks, manual operation staffing |
| Vendor liaison | Supply Chain Manager with the General Counsel | Security Manager | Contract notices, vendor incident statement, technician lists, data return |
| Vendor technical contacts | SCADA software vendor, SCADA integrator, compressor OEM | n/a | Engaged **only by phone through known numbers**, never through the suspected path, and only after the General Counsel approves |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A vendor session outside an approved window, from an unexpected source, or without a matching approval | Gateway logs; session recordings; SIEM | Terminate the session; declare Severity 1 |
| OT sensor alert: a new device, a new external connection, engineering commands from an unexpected host, or a PLC program download | OT sensors at the GCC, BCC, and Compressor Stations 1 and 3; MSSP | MSSP calls the OT Security Engineer and the shift supervisor within 15 minutes (STD-02) |
| SCADA values that disagree with field readings, setpoints or alarms changed with no change record, or commands no controller issued | Controller; station technician; shift supervisor | **Controller follows the control room management and emergency procedures first**, then reports. Severity 1 |
| A compressor unit trips, loads, or unloads with no operational cause, especially at Compressor Stations 2, 4, or 5 (no sensors) | Station control; controller | Station technician checks the unit panel locally; report as a possible cyber cause until ruled out |
| A vendor reports a breach of its support environment, or credentials of its technicians are found exposed | Vendor notice; threat intelligence; CISA or TSA alert | Disable that vendor's accounts at once; hunt for its indicators; Severity 2, raised to 1 if any indicator is found in OT |
| An unknown modem, cellular router, or cable found at a site | Site walkdown; technician | Do not unplug until the SCADA and OT Engineering Manager confirms the effect on the unit; photograph and report |

**Declare** when any trigger cannot be explained within 30 minutes by a known change or maintenance. **Every trigger in this table is a potential cybersecurity incident under SD 01G Section II.C.2** (unauthorized access to an OT system, malicious software, or activity that could disrupt operations). **Record the time of identification** for the 72-hour CISA clock.

## 3. First hour (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| T+0 | 1. **Safety actions first.** If values look wrong or the pipeline is moving outside limits, controllers act under the abnormal operating and emergency procedures, including pressure reduction or valve closure through field crews if SCADA cannot be trusted (192.615(a)(6)). The hardwired ESD systems remain available at every station | Controllers; shift supervisor | Safety actions logged |
| T+0 to 10 min | 2. **Cut every vendor path:** disable all vendor accounts at the remote access gateway; terminate active sessions; confirm the OEM modem at Compressor Station 4 is disconnected and send technicians to check the units at Compressor Stations 2 and 5 for similar devices | OT Security Engineer; Compressor Station Supervisors | Accounts disabled; sessions closed; station reports by radio |
| T+0 to 15 min | 3. **Close the IT/OT DMZ** at the GCC and BCC, as in runbook 1, so the attacker cannot use business IT as a second path | Director of Gas Control (authority); OT Security Engineer | Session tables clear |
| T+10 to 30 min | 4. **Field verification.** Field technicians read local gauges and flow computers at the affected area, all compressor stations, the 4 receipt interconnects, and the largest delivery points, and compare by radio with SCADA. Any mismatch beyond normal tolerance means SCADA data for that area is untrusted | VP Operations; Area Managers | Comparison sheet completed |
| T+15 to 30 min | 5. If the GCC SCADA is suspected and the BCC is not, **fail over to the BCC**. Do not fail over if the attacker could have used the same credentials at the BCC (until separate BCC administrative credentials exist, POAM-009, assume they share credentials) | Director of Gas Control; SCADA and OT Engineering Manager | Decision recorded |
| T+15 to 30 min | 6. **Lateral owners:** if monitoring of either operated lateral is lost or untrusted, notify the owner within 30 minutes (OSA) | Shift supervisor | Call logged |
| T+30 to 60 min | 7. **Preserve evidence without disturbing operations:** export gateway logs and session recordings, OT firewall logs, and sensor captures to write-once storage. Do not reboot SCADA servers or HMIs that are still in control. Memory capture only with the vendor-approved kit (until POAM-010 delivers it, ask the retainer to bring an OT-qualified capture method) | OT Security Engineers; retainer | Evidence hashed and logged |
| T+30 to 60 min | 8. Convene the CMT; call the insurer hotline; General Counsel engages breach counsel and the retainer | COO; CFO; General Counsel | Claim number; CMT convened |
| T+60 min | 9. **Decision point 1:** use the runbook 1 decision tree, with the extra questions below | Director of Gas Control recommends; COO decides | Decision recorded |

## 4. The operate-or-shut-down decision in this scenario (RS.AN, RS.MI)
Apply runbook 1 section 4, with these additional questions:

| Question | How to check | If the answer is bad |
|---|---|---|
| Were any commands sent to field devices or station controls that no controller issued? | SCADA command log against the shift log; station control event logs; OT sensor captures where available | Treat the affected area as untrusted. If commands cannot be stopped by isolation, this meets outcome C criterion 1 |
| Has PLC or RTU logic changed? | Compare running logic with the latest known-good copy. Stations 1 and 3: company backups with hashes. Stations 2, 4, and 5: OEM and integrator copies until POAM-009 closes, which takes longer and is less certain | Put that station in local manual control under the Compressor Station Supervisor; the ESD system remains the safety layer |
| Are setpoints, alarm limits, or displays different from the approved baseline? | SCADA and OT Engineering Manager compares the configuration with the baseline | Restore approved values through management of change with point-to-point verification (192.631(c)(2)) |
| Can field crews hold the affected area safely in manual operation? | VP Operations staffing plan (about 180 field staff per shift for full manual operation) | If not beyond the 8-hour MTD for gas control (BP-01), consider outcome C for that area only |

**Prefer the smallest safe action.** Untrusted data at one station or area calls for local manual control of that station or area, not a system shutdown. Outcome C applies only under the runbook 1 criteria, and the COO approves it.

## 5. Analysis, containment, and eradication (RS.AN, RS.MI)
1. **Which path?** Gateway logs and recordings for the last 90 days (the OT log retention limit until POAM-005 closes); identity provider sign-ins for gateway users; the OEM's diagnostic logs (request them in writing); the SCADA vendor's and integrator's records of who connected.
2. **Which accounts?** The OEM service account on unit control panels (full rights until POAM-002 closes), shared station logins at Compressor Stations 2, 4, and 5, and any field device still on a default or overdue password (POAM-004).
3. **Where did the attacker go?** Sensor data at the 4 monitored sites. At Compressor Stations 2, 4, and 5 and the field there is no OT monitoring (POAM-014), so the retainer deploys portable passive sensors there before those stations return to remote control.
4. **Contain:** keep vendor access disabled; change every credential the vendor could have known, starting with OT domain administrators (9 today, target 4; POAM-002) and station passwords; block the vendor's source ranges at the gateway.
5. **Eradicate:** rebuild compromised hosts from known-good media; reload PLC and RTU logic from verified copies; remove any undocumented connection permanently (POL-02; STD-04).
6. **Supplier side:** require a written incident statement from the vendor (what happened, which customers, indicators, technicians involved, containment status). The vendor's own SOC 2 report and contract terms are reviewed for its incident notice duties (P09 vendor review program; STD-03 requires notice within 24 hours in new contracts).

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv` and the runbook 1 decision log (D1 to D6).** Differences in this scenario:
- **CISA (SD 01G II.C):** unauthorized access to an OT system is a reportable cybersecurity incident. Report as soon as practicable and no later than 72 hours after identification. Include the affected pipeline facilities, the earliest known date of compromise, indicators, the impact on operations, and planned responses such as a reversion to manual operation (SD 01G II.C.5). Supplemental information within 24 hours of it becoming available. Consider early notice to TSA under IC Surface-2025-01.
- **NRC (49 CFR 191.5):** if any release meets 191.3 paragraph (1), or the Director of Pipeline Safety and Compliance judges the event significant (paragraph (3)), notify within 1 hour of confirmed discovery.
- **9-1-1 centers and officials (192.615(a)(8)):** if any area moves to emergency response.
- **Lateral owners:** within 30 minutes of losing or distrusting monitoring (OSA). Under the OSAs, each lateral owner makes its own regulatory notices for its lateral; the company gives it the facts it needs within the times the OSA sets.
- **Shippers and upstream pipelines; FERC posting:** as in runbook 1, only if capacity or service is reduced.
- **The vendor:** the General Counsel sends written notice under the contract and asks for preservation of the vendor's logs. Other customers of the vendor may be at risk; CISA is the channel for sharing indicators, not direct calls by staff.
- **SSI:** incident reports to CISA and TSA under the directive are SSI. Mark them and store them in the SSI repository.

## 7. Recovery and return to remote control (RC.RP, RC.CO)
Return each area to remote control only when all of these are true, and record the sign-offs:
- [ ] The path the attacker used is closed, and every other vendor path is reviewed against the TSA plan list of external connections (STD-04 quarterly review, run now).
- [ ] Logic in every PLC and RTU in the area matches a verified copy; station configurations match the baseline.
- [ ] SCADA values match field readings at every station and delivery point in the area for at least one full shift.
- [ ] Changed points and displays have point-to-point verification (192.631(c)(2)).
- [ ] Monitoring is in place for the area (permanent sensors or the retainer's portable sensors).
- [ ] The Director of Gas Control recommends and the COO approves.

**Vendor access returns one vendor at a time**, through the remote access gateway only, with named technician accounts, MFA, per-session approval, and recording. The OEM's diagnostic data moves through the DMZ historian replica to the OT analytics account, never through a modem (POAM-003).

The leak-detection model (P10 AI-001) and the predictive maintenance service (AI-002) stay out of the control room until their input data is confirmed clean and they are revalidated, because their inputs came from the affected OT.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; written report within 30 days (POL-03 4.12).
- Operating experience review under 192.631(g): did control room actions or SCADA data contribute? Add lessons to controller training (192.631(h)) and to the station technician module (POAM-015).
- File a Cybersecurity Implementation Plan amendment for any permanent change to vendor access or architecture (SD 02G Section VI).
- Reassess the vendor's tier and contract terms (STD-03); decide whether to keep the vendor.
- Update P01 (R-002, R-003, R-011, R-012, R-048), the POA&M, this runbook, and the TSA incident response plan.

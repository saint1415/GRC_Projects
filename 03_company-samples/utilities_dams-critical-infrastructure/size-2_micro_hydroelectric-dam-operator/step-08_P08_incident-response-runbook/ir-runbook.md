# Incident Response Runbook: Unauthorized Access to Spillway and Turbine Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (owner and operator of the fictional Bramble Shoals Hydroelectric Project) |
| Tier / Vertical | Micro / Dams |
| Incident type | An unauthorized person gains access to the HPCDMS (the HMI PC, the gate PLC, or the unit controls) and views, changes, or operates the spillway gates or the turbine units. Most likely paths today: the shared remote desktop password, or the integrator's cellular VPN (P01 R-001, R-002, R-003) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy; Emergency Action Plan (EAP) |
| Runbook owner | Plant Superintendent (incident commander and 18 CFR 12.10 reports) |
| Approved | 2026-08-31 by the Owner and General Manager |
| Last tested | Not yet. First tabletop with the integrator due 2026-11-30 (POAM-011) |
| Handling | Restricted (POL-04). Printed copies in the control room, the office safe, and the Plant Superintendent's home |

**The rule that overrides everything else: keep the dam under control.** Put gates and units in local control and confirm their positions by eye before anything else. Evidence can be lost; people at the tailrace and the canoe launch cannot be put at risk.

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The plant is staffed 07:00 to 17:30 and unattended overnight, when the on-call operator-mechanic is about 30 minutes away. The controls integrator does OT technical work, the MSP covers office IT only, and the cyber insurer supplies breach counsel and an incident response firm.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| First responder | Operator-mechanic on duty (day) or on call (night) | Any staff member on site | On-call phone; control room phone |
| Incident commander | Plant Superintendent | Owner and General Manager | Cell (printed contact sheet) |
| OT technical lead | Controls and Electrical Technician | Controls integrator emergency line | Cell; integrator number on the contact sheet |
| Decisions on money, outside statements, ransom; insurer | Owner and General Manager | Plant Superintendent | Cell; insurer hotline card in the binder |
| Incident log, evidence folder, MSP contact | Office and Compliance Administrator | Plant Superintendent | Cell |
| Office IT (only if the office network is involved) | MSP emergency line | MSP technician | Phone |
| Breach counsel and incident response firm | Insurer panel firms | n/a | Assigned on the first hotline call |
| Outside agencies | County sheriff (911); county emergency management; FERC Regional Engineer and Regional Office; county public works (downstream weir); FBI field office; CISA | | Numbers posted in the control room and on the contact sheet |

**Notification chain in the first hour:** first responder → Plant Superintendent → Controls and Electrical Technician and Owner (at the same time) → sheriff and county emergency management if anyone downstream may be at risk → insurer hotline (Owner) → integrator. The MSP is called only if an office device may be involved.

**Out-of-band first.** Assume the intruder can see the HMI and may see email. Coordinate by personal phone and text using the printed contact sheet.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the control room and the office safe: this runbook, the contact sheet, the notification matrix, the local control checklist for each gate and unit, the EAP notification flowchart
- [ ] All 3 operator-mechanics, the Plant Superintendent, and the Controls and Electrical Technician can run both gates and both units from the local panels (annual EAP readiness test, 18 CFR 12.25(b); last 2026-02-17)
- [ ] The cable to the office side of the firewall and the integrator's cellular router power plug are labeled "PULL IN AN INCIDENT"
- [ ] The Controls and Electrical Technician and the Plant Superintendent can end all remote desktop sessions and turn off unattended access from the tool's administrator console on a phone
- [ ] Remote desktop password limited to 5 staff (done 2026-08-12); integrator router off except for watched sessions (from 2026-09-15). **Named accounts, MFA, and session alerts are a gap until POAM-002 closes (2026-11-30)**
- [ ] Known-good copies of gate and unit PLC logic, the HMI project, and governor and exciter settings on encrypted drives. **Gap until POAM-006 closes: today the only reference is the integrator's 2023-05-18 copy**
- [ ] Insurer hotline and policy number checked at each renewal (next 2026-11-01)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A gate moves, or the tailrace horn and strobes go off, with no operator command | Gate position alarm (monitoring callout); staff, the canoe outfitter, or a neighbor reports the horn | **Local control now** (section 3). Declare the incident |
| A unit trips, starts, or changes load unexpectedly | Unit alarm callout; cooperative calls about output | Unit to local; declare if no one on site caused it |
| Headpond falling or tailwater rising faster than the operating plan | Level alarms in the monitoring service | Treat as a possible project emergency; check gate positions by eye |
| An HMI session nobody claims, or the HMI mouse moving by itself | Operator on site; session alert (after POAM-002) | End all remote sessions from the console; declare |
| The integrator says it did not start an active session, or a weekly review finds a session nobody can explain | Integrator call; weekly review (POAM-010) | End sessions; unplug the router; declare |
| Setpoint, alarm limit, or program changes nobody made | HMI event journal; operator notices | Local control; declare |
| Threat or extortion message naming the dam | Email, phone, social media | Preserve it; call the sheriff; declare |

**Declare the incident when** any gate or unit command, setpoint change, or program change cannot be tied to an authorized person, or an unauthorized remote session is found. When in doubt, declare. A declaration can be closed later; a late one cannot be undone.

**Write down the time of discovery.** The 18 CFR 12.10(a)(1) report is due as soon as practicable after discovery, preferably within 72 hours. A security incident (physical and/or cyber) is a reportable condition on its own (12.3(b)(4)(xi)), even if no water was released.

## 3. First 30 minutes (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **People first.** If a gate is opening or has opened while recreation users may be at the tailrace, canoe launch, or fishing area, call 911 and ask the sheriff to clear the area below the dam | First responder | Call made; time logged |
| 2. **Cut remote access from a phone.** End all remote desktop sessions and turn off unattended access in the tool's administrator console; change the password | Controls and Electrical Technician (Plant Superintendent if unreachable) | No remote session active |
| 3. **Local control.** At the hoist house, switch both gate panels to local; stop any unplanned movement; return gates to the operating plan positions; confirm by eye and the mechanical indicators, not the HMI. At the powerhouse, switch both units to local or shut them down | First responder (at night on arrival, about 30 minutes) | Both gates and both units in local control, positions confirmed by a person on site |
| 4. **Pull the plugs.** Unplug the integrator's cellular router and the labeled cable to the office side of the firewall. Do not power off the HMI PC, PLCs, or data logger | First responder or Controls and Electrical Technician | Control network isolated; monitoring gateway may stay on (outbound only) |
| 5. **Downstream risk.** If a sudden release has happened or may happen, activate the EAP at the right level and call county emergency management; tell county public works (downstream weir) if flows are affected | Plant Superintendent (first responder may activate without waiting) | EAP level declared, or a written decision that no EAP condition exists |
| 6. Start the paper incident log: times, actions, who, gate and unit positions, headwater and tailwater readings | First responder, then the Office and Compliance Administrator | Log open |
| 7. Call the Owner; the Owner calls the insurer hotline before any outside firm is hired | Plant Superintendent; Owner | Claim number issued; counsel assigned |

**Stay in local control.** Keep a person at the gate panels around the clock until section 7 is complete. The BIA sets an 8-hour limit for local gate control with 7 staff (P05, BP-01); call in everyone early, and ask the integrator for emergency support within the first 2 hours.

## 4. Analysis (RS.AN)
1. **What moved and when.** HMI event journal (about 180 days), gate and level trends from the monitoring service, and camera video of the spillway (about 14 days on the NVR). Build a timeline of every command and position change.
2. **Who and how.** Export the remote desktop connection log now (the vendor keeps only 30 days). Ask the integrator for its own records of the period and whether its office or engineers' computers may be compromised. Because the HMI uses one shared account, the person can be identified only from the remote session record and the on-call rota.
3. **What changed.** With the integrator, compare running gate and unit PLC logic and governor settings with the newest known copy (2023-05-18 until POAM-006 closes, so differences may be legitimate later changes; the integrator's work orders explain them).
4. **Where else.** Check the engineering laptop, the office PCs that could reach the HMI PC, the camera NVR, and the cellular data gateway web page for sign-ins.
5. **Preserve evidence.** Copy logs before they roll over; photograph HMI screens; keep a record of who collected what and when. Image the HMI PC only after the Plant Superintendent confirms operations are stable. Evidence is Restricted (POL-04).
6. **Scope decision (written).** Was water released? Were units damaged? Was any employee personal information touched (suite, payroll)? Was any other system reached?

## 5. Containment and eradication (RS.MI)
1. Keep remote access off and the plugs pulled until step 5 below.
2. Reset every OT credential: remote desktop tool, HMI, engineering software, firewall administrator, NVR, cellular gateway, and gate panel codes.
3. If any logic or setting differs without an explanation, the integrator reloads it from the verified copy. The Plant Superintendent approves, and gates are tested in local before returning to automatic control.
4. If there is any sign of malware on the HMI PC, the integrator rebuilds it from clean media (the operating system is unsupported, so this may bring forward the POAM-008 replacement).
5. The insurer's incident response firm confirms nothing persists before anything is reconnected.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Safety reports never wait for counsel. Counsel reviews everything else.

| When (from discovery) | Action | Owner |
|---|---|---|
| Immediately | Sheriff (911) and county emergency management; EAP notifications if a project emergency exists | First responder; Plant Superintendent |
| Immediately, if flows are affected | County public works, operator of the downstream weir (Rev. 3A 4.2) | Plant Superintendent |
| Within the first hours | Cooperative (forced outage); insurer hotline | Plant Superintendent; Owner |
| As soon as practicable, **preferably within 72 hours** | Initial report to the FERC Regional Engineer by email or telephone (18 CFR 12.10(a)(1)). In practice call the same day | Plant Superintendent |
| Usually within **one working day** | Security incident report to the FERC Regional Office (Rev. 3A 3.2, 4.2); can be the same call | Owner (FERC primary security contact) |
| Same day, voluntary | FBI field office and CISA; HSIN suspicious activity report once the account exists | Owner |
| If recreation facilities are closed for security | Notice to the FERC Regional Office as soon as practical (usually within one working day); over 30 days needs prior coordination (Rev. 3A 3.3.4) | Plant Superintendent |
| When the Regional Engineer directs | Written report verified under 12.13: causes, preceding events, measures taken, damage, injuries, property damage (12.10(a)(2)) | Plant Superintendent |
| Within 30 days of determination, only if employee personal information was breached | Florida notice to affected individuals (Fla. Stat. 501.171(4)) | Owner with counsel |

**Not required here:** NERC CIP-008 reporting (not a BES facility; not registered) and CIRCIA reporting (proposed rule only). The cooperative is told at once about any forced outage so it can handle its own duties. Mark security reports to FERC "Privileged - Security Sensitive Material" and limit details to what FERC needs.

**Staff and public.** Tell staff the dam is under local control and safe, and not to discuss the incident outside the company. Public statements come only from the Owner, coordinated with county emergency management if the EAP is active.

**Ransom.** Any payment needs the Owner, the insurer, counsel, and an OFAC sanctions check (POL-03 4.9). Paying does not remove any reporting duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Local control of gates and units (already in place from section 3)
2. Gate PLC automatic level control and HMI supervision, from verified logic, tested with gates in local first
3. Data logger readings and the tailrace horn and strobes; check readings against manual reads
4. Monitoring service and alarm callouts (outbound only)
5. Unit control through the HMI
6. Cameras and NVR, with new passwords
7. Office IT links, **without** any route into the control network (POAM-004 design)
8. Remote access last: **only on the single path with named accounts and MFA** once it exists; until then, on-site operation only. The integrator router stays unplugged

**Before each step:** logic matches the verified copy; credentials are new; only the connections that step needs are open. The Plant Superintendent signs each step in the log. Tell staff, the cooperative, and (if the EAP was activated) county emergency management when normal operation resumes.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days with all staff, the integrator, and any agency that responded; written up within 30 days (POL-03 4.12).
- Update the risk register (P01 R-001 to R-003), the POA&M (P07), the SSP, the EAP security trigger page, and this runbook.
- Keep the 12.10 reports as permanent project records (18 CFR 12.12(a)(1)(iii)(B)) and the incident file in the restricted CEII folder.

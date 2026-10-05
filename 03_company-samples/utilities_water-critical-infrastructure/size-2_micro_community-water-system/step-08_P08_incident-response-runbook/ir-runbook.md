# Incident Response Runbook: Remote-Access Compromise of the Treatment-Plant HMI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (privately held community water system, 2,850 population served) |
| Tier / Vertical | Micro / Water and Wastewater Systems |
| Incident type | An unauthorized person connects to the SCADA HMI computer through the remote desktop tool (SYS-04) and changes the process, for example by raising the hypochlorite pump speed and silencing the HMI high-chlorine alarm |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Chief Operator (incident lead for the WTSS), with the Office Manager for the log, the MSP, and customer data |
| Approved | 2026-08-31 by the Owner and General Manager. Becomes the cyber annex of the emergency plan by 2026-10-31 (POAM-012) |
| Last tested | Not yet. First tabletop with the integrator and MSP, with a hand-operation drill, due 2026-11-30 (P03 G-048) |

**The rule that overrides everything else here: keep the water safe first, then investigate.** Any licensed operator may take the section 3 actions at any time without waiting for anyone.

**What limits the worst case.** The hypochlorite pump's mechanical stroke setting caps its output at about 2.5 times the normal rate, whatever the PLC or HMI commands. Normal feed holds about 1.2 mg/L free chlorine leaving the plant, so the Chief Operator estimates the worst-case plant outlet residual at roughly 3 mg/L. The chlorine analyzer's own high and low relays call the on-call phone through the alarm dialer, even if the attacker silences the HMI alarm. Neither can be changed from SCADA.

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The SCADA integrator and the MSP do the technical work; the cyber insurer supplies breach counsel and forensics.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Safe-water actions (first 60 minutes) | Licensed operator on duty or on call | Chief Operator | On-call phone; alarm dialer calls it |
| Incident lead | Chief Operator | Owner and General Manager | Cell phone (printed contact sheet) |
| Decision maker (money, notices, outside communications, ransom) | Owner and General Manager | Chief Operator | Cell phone |
| Incident log, MSP, customer data | Office Manager | Customer Service and Billing Clerk | Cell phone |
| OT technical response | SCADA integrator (on site only, never by remote session during the incident) | None (single point of recovery, P05) | Integrator office and technician cell |
| Office IT technical response | MSP incident line | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Policy card in the plant binder |
| Breach counsel and forensics | Insurer panel firms | n/a | Assigned on the first hotline call |
| Remote desktop tool vendor | Vendor support (to preserve relay and connection logs) | n/a | Vendor support portal from a clean device |
| Primacy agency | State drinking water program, district office | After-hours emergency number (being added, P03 G-011) | Contact sheet |
| Law enforcement | FBI field office or IC3 | CISA | Contact sheet |

**Notification chain in the first hour:** operator → Chief Operator and Owner (same call) → integrator (asked to come on site) and Office Manager → insurer hotline (Owner) → breach counsel and forensics (through the insurer). The Office Manager calls the MSP if any office computer or account may be involved.

**Out-of-band first.** Assume the attacker can see the HMI computer and may have read email (the SCADA drawings and password spreadsheet sat in the shared folder until 2026-09-30). Coordinate by phone calls and texts on company and personal phones, using the printed contact sheet.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed plant binder in the control room and at the Owner's and Chief Operator's homes: this runbook, the contact sheet, the notification matrix, the Tier 1 notice templates (including a chemical overfeed and treatment interruption template, P03 G-014), the paper grab-sample log, and the customer contact list printed within the last 31 days (P03 G-013)
- [ ] Written hand-operation steps for each well, the aerator, the hypochlorite feed, and the high-service pumps (P03 G-033, due 2026-10-31)
- [ ] Offline, encrypted copies of the PLC program and HMI project less than 31 days old, on 2 drives (CP-9). **Gap until POAM-005 closes (first copies 2026-09-15)**
- [ ] Remote desktop tool with named accounts, MFA, and no unattended access (AC-17, IA-2(1)). **Gap until POAM-002 and POAM-004 close (2026-09-30)**
- [ ] Remote desktop connection history kept by the tool vendor for 90 days; the Chief Operator can export it (AU-6, weekly review from 2026-10)
- [ ] Portable colorimeter calibrated, with reagents for at least 7 days of 4-hour grab samples
- [ ] Alarm dialer tested monthly on the chlorine high and low relays
- [ ] Insurer hotline and policy number checked at renewal (2026-11-01)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Alarm dialer call: chlorine high or low, with no process cause | Analyzer relays (independent of SCADA) | Go to section 3. Verify with a grab sample |
| The HMI cursor moves, screens change, or a remote session banner appears when no one is using it | Operator in the control room | Go to section 3 now, then call the Chief Operator |
| A pump speed, setpoint, mode, or alarm limit that no one on shift changed; an alarm that was silenced or disabled | Operator rounds; HMI event list; remote monitoring app | Section 3. Treat as an incident until the change is explained |
| Customer calls about strong chlorine taste or smell, or a skin or eye complaint | Billing Clerk; on-call phone | Grab sample at the plant and at the nearest hydrant; call the Chief Operator |
| Remote connection in the tool's history at a time no one on call or at the integrator connected | Weekly log review (from 2026-10); tool vendor notice | Chief Operator ends any active session and declares |
| The integrator, MSP, tool vendor, CISA, or the FBI reports a compromise of the remote desktop tool or of their own systems | Phone or email | Chief Operator disconnects the HMI computer's network cable and checks the history for the exposure window |

**Declare an HMI compromise incident when** any control action on the WTSS cannot be traced to an authorized person, or a remote session reached the HMI computer that no authorized person made.

**Write down two times in the incident log:** when the incident was first reported, and when the company learned of any situation that may need a Tier 1 notice. The 24-hour Tier 1 clocks run from the second (40 CFR 141.202(b)).

## 3. First 60 minutes: safe water and containment (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Put the hypochlorite pump in **hand** at the panel and set it to the normal rate. Put any well or high-service pump that looks changed in hand | Operator | Feed in hand at the normal rate |
| 2. Take chlorine grab samples at the plant entry point and at the nearest hydrant downstream. Repeat every 30 minutes until 2 results in a row are in the normal range, then every 4 hours on the paper log (40 CFR 141.403(b)(3)(i)(A)) | Operator | Two normal results 30 minutes apart |
| 3. **Cut remote access:** end the remote session if one is open, then unplug the HMI computer's network cable. **Do not turn it off** (evidence). The HMI screen stays usable for local viewing, but all control stays in hand | Operator, by phone with the Chief Operator | No remote session possible |
| 4. Decide the operating mode: (a) hand operation of the plant with an operator on site, or (b) PLC in automatic with the HMI computer disconnected and an operator watching. **If the PLC program may have been changed, choose hand operation** | Chief Operator | Mode written in the incident log |
| 5. Estimate whether off-target water reached customers: time the feed was high or low, ground tank and elevated tank levels, flows, and hydrant grab results | Chief Operator | Yes or no, with evidence |
| 6. Call the insurer's breach hotline | Owner | Claim number issued; counsel assigned |
| 7. Open the incident log and the timeline | Office Manager | Log open |
| 8. Ask the integrator to come on site. No remote work by the integrator until section 5 is complete | Chief Operator | Arrival time agreed |

If high or low chlorine may have reached customers, or treatment was interrupted, the Chief Operator starts the Tier 1 decision (section 6) **at the same time**, not after the investigation.

**Staffing.** In hand operation the plant must be staffed around the clock. The 3 licensed operators work 12-hour shifts. If hand operation will last more than 48 hours, the Owner asks the county utility or a neighboring system for a relief operator (P01 R-013).

## 4. Analysis (RS.AN)
1. **Scope.** Which settings changed, when, and from where. Sources: the HMI alarm and event list (photograph it before anything is rebuilt), the remote desktop tool's connection history (export it from a clean device; it is kept for only 90 days), the remote monitoring trend for chlorine, pump speed, and tank levels, and the daily operator log.
2. **Initial access.** Which account or password was used, from which device or address. Was the shared password reused elsewhere or known to former staff or integrator technicians? Ask the tool vendor to preserve its relay logs.
3. **PLC integrity.** The integrator, on site, compares the running PLC program with the company's offline copy (once POAM-005 exists; until then with the integrator's own copy, whose date is unknown and must itself be checked against the 2018 as-builts and the operators' knowledge of setpoints). Check that the key switch is in RUN.
4. **Spread.** Could the attacker reach the office computers, the remote monitoring gateway, or the productivity suite from the HMI computer (flat network until POAM-006 closes)? The MSP checks office computers and the suite sign-in log. If the billing system or payroll accounts were reached, customer or employee personal information may be involved (Fla. Stat. 501.171 rows in the matrix).
5. **Evidence.** Forensics (through the insurer) images the HMI computer before it is rebuilt, where this does not delay safe-water actions. Keep chain of custody. Photograph the panels, the HMI screens, and the pump stroke setting.

## 5. Containment and eradication (RS.MI)
1. Keep the remote desktop tool off until it is rebuilt with named accounts, MFA, and no unattended access (POAM-002, POAM-004). The integrator works on site, watched, until then.
2. Change every credential the attacker could have seen: the remote desktop password, HMI logins, HMI administrator and PLC passwords, modem and gateway passwords, the firewall login, and any password in the spreadsheet.
3. Rebuild the HMI computer from known-good media with the integrator. **Do not clean and reuse it.**
4. Reload the PLC program from the verified copy if any difference is found. Set a PLC program password and leave the key switch in RUN.
5. Turn on MFA for the remote monitoring service and confirm the gateway's write-back is still off.
6. Confirm with forensics that nothing persists on office computers before the HMI computer is reconnected to any network.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel confirms each legally required notice. The Chief Operator owns the public notice clock and the Owner approves the notice.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline called; counsel assigned | Owner |
| Hour 0-4 | Decide whether this is a waterborne emergency such as a failure or significant interruption in key treatment processes (Tier 1 trigger, 40 CFR 141.202(a) Table 1 item (7)). If yes or unsure, call the primacy agency and draft the notice from the template | Chief Operator with the Owner |
| No later than 24 h after learning of the situation | If Tier 1: deliver the notice in a form reasonably calculated to reach all persons served, using at least one listed method (local radio, posting throughout the service area, or hand delivery by door hanger, 40 CFR 141.202(c)), and start primacy agency consultation. Phone calls from the printed contact list, starting with the school, are a supplement | Chief Operator; Customer Service and Billing Clerk |
| Within 24 h of declaration | Report to the FBI (tampering with a public water system is a federal crime, 42 U.S.C. 300i-1) and, voluntarily, to CISA | Chief Operator |
| By the end of the next business day | Only if the state-determined minimum chlorine residual was not restored within 4 hours: notify the state (40 CFR 141.405(a)(1)) | Chief Operator |
| Within 48 h | If a drinking water regulation was violated, including missed monitoring while the residual record was lost: report it to the state (40 CFR 141.31(b)) | Chief Operator |
| Within 10 days of completing notices | Public notice certification with a copy of each notice to the primacy agency (40 CFR 141.31(d)(1)) | Chief Operator |
| Within 30 days of determination | Only if customer personal information was accessed: Florida individual notice, and Department of Legal Affairs notice if 500 or more Floridians (Fla. Stat. 501.171) | Office Manager with breach counsel |
| Day 0-2 | Staff briefing: what happened, the operating mode, and do not discuss it outside the company | Owner |

**The shortest clock is public health, not data.** For this incident the 24-hour Tier 1 notice and primacy agency consultation will come due long before any data breach clock. Email and the billing system may be off limits during the investigation, so use the printed contact list and local radio.

**Not current obligations.** CIRCIA is proposed only (no final rule as of 2026-09-25). As proposed, the company would not be covered: it is SBA-small and serves fewer than 3,300 people. Recheck when a final rule is published and if the population served passes 3,300.

**Ransom** (if the incident turns into extortion): requires the Owner, breach counsel, the insurer, and an OFAC sanctions check (POL-03 4.9).

## 7. Recovery (RC.RP, RC.CO)
Restore in the BIA priority order (P05 section 6). **SCADA comes back last.**
1. Hand operation of the wells, aerator, and chlorine feed (in place from section 3)
2. High-service pumps and elevated tank level checked by the field technician
3. Chlorine grab samples every 4 hours on the paper log; continuous monitoring must resume within 14 days (40 CFR 141.403(b)(3)(i)(A))
4. Public notice capability: printed contact list, template, radio contact
5. Plant staffing plan; relief operator after 48 hours
6. HMI computer rebuilt from known-good media with a verified PLC program, then reconnected **one process at a time**, each loop watched in hand before it is switched back to automatic
7. Remote monitoring alarms by app (the alarm dialer covers critical alarms until then); the anomaly detection feature stays off until the trend data is verified (P10)
8. Remote access, only after named accounts and MFA are in place

**Validate before returning to automatic control:** all credentials changed; PLC program verified against the known-good copy; remote desktop tool rebuilt or removed; 24 hours of stable operation on the first process returned to automatic. Tell customers when any notice is lifted, using the same channels as the notice (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the integrator, the MSP, and the primacy agency contact if a notice was issued. POL-03 4.13 requires the write-up within 30 days.
- Update the risk register (P01 R-001, R-002, R-004, R-006, R-010, R-011), the POA&M (P07), the emergency plan, and training.
- Keep incident records for at least 5 years (POL-02 A.7), and public notices and certifications for 3 years (40 CFR 141.33(e)).

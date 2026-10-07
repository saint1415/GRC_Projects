# Incident Response Runbook: Unauthorized Access to Crane Controllers Through Vendor Remote Access

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed marine cargo terminal operator: Terminal 1, Terminal 2 and an off-dock depot in Florida) |
| Tier / Vertical | Mid-Market / Transportation and Warehousing |
| Incident type | An OT safety incident: an attacker uses a vendor's remote access path to reach crane or yard equipment controllers and changes settings, programs or motion. Most likely path today: the T2 mobile harbor crane OEM's always-on cellular appliance with a shared account (P01 R-003). Other paths: the OCR or reefer monitoring vendors' own remote tools (R-018), the TOS vendor support path (R-037), or a compromised T1 OEM account in the privileged remote access service |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions; OT steps informed by NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy (4.4, 4.8, 4.10); POL-02 4.10 remote access. Part of the Cyber Incident Response Plan required by 33 CFR 101.650(g)(2) |
| Companion documents | `ir-runbook.md` (ransomware, for IT containment and recovery steps); `notification-matrix.csv`; BIA (P05 BP-05, BP-06); both FSPs (SSI); OEM emergency procedures for each crane type |
| Runbook owner | Director of Maintenance and Engineering (OT lead), with the Director of IT and Cybersecurity (CySO) as incident commander |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. First exercise in the 2026-11-18 cyber drill (T2 mobile harbor crane scenario, POAM-029) |
| Handling | SSI once controller details and vendor access paths are added (POL-04 4.2) |

## 0. Governance, roles and contacts (Govern)
The three tiers in `ir-runbook.md` section 0 apply. In this incident **safety decisions belong to terminal operations command**, and the incident commander may not overrule a decision to keep equipment stopped.

| Role | Primary | Backup | Decides or does |
|---|---|---|---|
| Incident commander and Coast Guard reporting | CySO | Security Manager (alternate CySO) | Declaration, 6.16-1 report, IT containment, forensics through counsel |
| OT lead | Director of Maintenance and Engineering | Senior crane electrician on duty | Safe state, lockout, controller checks, OEM coordination, return-to-service sign-off |
| Terminal operations | T2 General Manager (T2) or T1 General Manager (T1) | Shift superintendent | Stopping vessel work, berth changes, manual working |
| Safety | Terminal General Manager with the Director of Maintenance and Engineering | Shift superintendent | Clearing people from danger zones; injury response; OSHA report for employees |
| MTSA security | Terminal FSO | Security supervisor on duty | Breach of security and TSI determinations; NRC and COTP reports under the FSP |
| OT network | OT network engineer | Security analyst (OT) | Disconnecting the vendor path; passive capture; firewall changes |
| Vendor relations | Director of Maintenance and Engineering for OEMs; Procurement Manager for contracts | CySO | OEM engagement as both a responder and a possible compromised party |
| Legal | General Counsel | Outside counsel (insurer panel) | Privilege; vendor contract notices; OSHA and injury legal issues |
| CMT chair | Chief Operating Officer | CEO | Terminal closure, customer statements, resources |

## 1. Preparation checks (Identify / Protect)
- [ ] T2 OEM cellular appliance off by default, enabled per session through an approval call to the T2 shift superintendent (POAM-003, 2026-10-15). Until then: **the T2 superintendent must know where the appliance and its power switch are** (T2 crane electrical house 2)
- [ ] All 27 vendors with access through the privileged remote access service, with per-session approval, MFA and recording (POAM-003, 2026-12-31). Today only the T1 crane OEM is onboarded
- [x] T1 PLC programs and HMI settings held offline in the Maintenance and Engineering safe (known-good copies with hashes)
- [ ] T2 mobile harbor crane PLC programs and HMI settings held by the company (POAM-011, 2026-12-31). Until then, known-good copies come from the OEM
- [x] T1 OT zone firewall and passive OT monitoring sensors
- [ ] T1 OT alerts in the MSSP 24x7 workflow (POAM-006, 2027-01-31). Until then, the OT analyst reviews alerts on business days and the MSSP does not see them
- [ ] T2 OT zone and sensors (POAM-022, POAM-024, 2027-03-31)
- [x] OEM 24x7 emergency numbers for each crane type in the incident binders and in each crane cab
- [ ] Contract terms requiring the T2 OEM, OCR vendor and reefer monitoring vendor to notify the company of vulnerabilities and incidents without delay and to support forensics (POAM-019)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A crane, RTG or mobile harbor crane moves, slows or stops unexpectedly; drives fault together; limits or setpoints changed on the HMI | Crane operator; mechanic | **Emergency stop.** Operator reports by radio to the superintendent, who calls the OT lead and the CySO line |
| Remote session to a controller that no one approved; vendor account active outside a scheduled window | Privileged remote access service log (T1); T2 appliance status light or OEM call; firewall logs | Terminate the session; disconnect the path; call the CySO line |
| T1 OT sensor alert: new connection to a PLC, program download, write command or firmware change | Passive OT sensors (T1) | OT analyst or on-call analyst calls the OT lead and the CySO line |
| A vendor reports a compromise of its remote support tool, accounts or update channel | Vendor notice; CISA or Coast Guard advisory | Disable that vendor's access everywhere; check its recent sessions; declare if any session is unexplained |
| Reefer setpoints changed on many units at once | Reefer monitoring system; reefer technicians | Restore setpoints locally; disconnect the vendor tool; declare |

**Declare a severity 1 OT incident when** any controller change, motion or session cannot be explained by an approved work order, or when a vendor confirms its access path was compromised. Record the date and time of discovery and declaration.

## 3. First hour (RS.MA, RS.MI, RS.CO)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-5 min | **Safety first.** Emergency stop on the affected crane; stop all moves by cranes of the same type and on the same network; clear people from under suspended loads and boom paths; land any suspended load only if it is safe to do so in local control | Operator; shift superintendent; OT lead | Equipment stopped; area clear |
| 0-10 min | Injury check. Call emergency services for any injury. Notify the terminal General Manager | Shift superintendent | Injuries handled |
| 0-15 min | **Cut the vendor path.** Power off the T2 OEM cellular appliance; disable the vendor's accounts in the privileged remote access service and the vendor's own tools at the firewall; block the vendor's address ranges | OT network engineer (on site: senior crane electrician) | No remote path to any controller |
| 0-15 min | Lock out the affected equipment (lockout/tagout) until the OT lead signs off | OT lead | Lockout tags placed |
| 0-30 min | **Preserve evidence before restarting anything.** Photograph HMI screens; export controller event logs, the appliance log and the remote access service recordings; start a passive capture on the affected segment; do not reboot controllers | OT analyst with the senior crane electrician | Evidence listed in the incident log with hashes |
| 0-60 min | **Report under 33 CFR 6.16-1** to the COTP for the affected terminal, the FBI field office and CISA. State that equipment is stopped and whether anyone was hurt | CySO (alternate CySO or the terminal FSO if unreachable) | Report times and reference numbers recorded |
| 0-60 min | FSO decides on the MTSA reports: breach of security, suspicious activity, or a TSI if there is significant loss of life or disruption (101.305) | Terminal FSO with the terminal General Manager | Decision in the FSO records |
| 0-60 min | Call the insurer hotline; counsel engaged; counsel engages a forensic firm with OT experience | General Counsel | Claim number |
| 0-60 min | Call the OEM's emergency line: tell it its access path is suspected, ask it to preserve its own logs, and ask whether other customers are affected | OT lead | OEM contact and ticket recorded |
| 1 h | Convene the CMT; decide whether to stop all work at the terminal or continue with unaffected equipment in local control | CMT chair with terminal operations command | Decision recorded |
| 1 h | **If a company employee was killed, hospitalized as an in-patient, lost an eye or suffered an amputation:** report to OSHA (fatality within 8 hours; others within 24 hours, 29 CFR 1904.39). For injured longshore workers, inform their employer through the hiring hall | Terminal General Manager with the General Counsel | Report made and recorded |

## 4. Analysis (RS.AN)
1. **What changed.** With the OEM, compare each affected controller's program, firmware version and HMI settings with the known-good copy (T1: company offline copies; T2: OEM copies until POAM-011 closes). List every difference and when it was made.
2. **How the attacker got in.** Review the appliance or remote tool logs, the shared account's sign-in history, firewall logs and the T1 OT sensor timeline. Establish the first unauthorized session and every controller reached.
3. **Spread.** At T2, the flat network means the gate servers, OCR, PACS and VMT Wi-Fi share the segment: check them for attacker activity (R-002). At T1, check that the OT zone firewall held. Check other cranes of the same type at both terminals, because OEM access is often common across sites.
4. **Other customers and vendors.** Ask the OEM and CISA whether the same access path was used elsewhere. If the vendor itself was compromised, treat every vendor using the same type of tool as suspect until checked.
5. **Data and SSI.** Check whether network maps, crane documentation or FSP extracts were accessible through the vendor path (SSI disclosure, 1520.9(c)).
6. **Safety analysis.** The OT lead documents whether safety interlocks and limit switches worked as designed. If any safety function was bypassed in software, all cranes of that type stay stopped until the OEM confirms the fix.

## 5. Containment and eradication (RS.MI)
1. Keep every vendor path closed except a single, monitored path for the OEM's recovery work: a company laptop on site, or a session through the privileged remote access service with MFA, recording and a company engineer watching.
2. Replace the shared OEM account with named accounts; rotate every OT engineering and HMI credential at the affected terminal (POL-02 4.1).
3. Reload known-good programs and settings on every affected controller; verify hashes before and after.
4. At T2, insert a temporary firewall between the gate and crane segments before any crane reconnects to the TOS (ahead of the full T2 OT zone, POAM-022).
5. Remove vendor-installed remote tools found during the analysis.

## 6. Legal, regulatory and external communication (RS.CO)
**Follow `notification-matrix.csv`.** The decision points in `ir-runbook.md` section 6 apply, plus these:

| Decision point | Question | Decider | Record |
|---|---|---|---|
| O1 | Was this a TSI (significant loss of life or significant disruption), a breach of security, or suspicious activity? | Terminal FSO with the COTP | FSO records |
| O2 | Is an OSHA report due for a company employee (8 hours for a fatality; 24 hours for in-patient hospitalization, amputation or loss of an eye)? | Terminal General Manager with the General Counsel | OSHA report confirmation |
| O3 | Does the vendor contract require the vendor to notify us, cooperate and preserve logs? If not, what can we require now? | General Counsel with the Procurement Manager | Contract register; letter to the vendor |
| O4 | Should other terminal operators be warned (through the Area Maritime Security Committee, CISA or the Coast Guard) because the OEM serves them too? | CySO with the General Counsel | Information-sharing record (101.650(e)(3)(iii)) |
| O5 | Do carriers with vessels at berth or due need a revised plan or a diversion? | Vice President Terminal Operations | Customer communications log |

**Timeline:**
| When | Action | Owner |
|---|---|---|
| Immediately (first hour) | 6.16-1 report to the COTP, FBI and CISA | CySO |
| Without delay | MTSA reports per the FSP (NRC; COTP for a TSI) | Terminal FSO |
| Within 8 or 24 hours of the event | OSHA report for a company employee, if O2 is yes | Terminal General Manager |
| Within 24 hours | Carrier alliance notice if T1 alliance vessels are affected; notice to carriers with vessels at berth or due at the affected terminal | Director of Commercial and Customer Service through counsel |
| Promptly | SSI disclosure report, if applicable | Terminal FSO |
| As facts develop | Updates to the COTP and the FBI; information sharing on the OEM path (O4) | CySO |
| Throughout; kept 2 years | Incident and threat records (101.640; 105.225(b)(3), (6)) | Terminal FSO |

Personal information is rarely involved in this incident. If the vendor path also reached gate servers holding driver data, the Florida decision in `ir-runbook.md` section 6 (D4 to D6) applies.

## 7. Recovery and return to service (RC.RP, RC.CO)
Return equipment to service one crane at a time, in the BIA order for the affected terminal (P05: BP-05 crane and equipment support, then BP-01 or BP-06 vessel operations).

| Step | Action | Sign-off |
|---|---|---|
| 1 | Controller program, firmware and HMI settings match the known-good copy (hash verified) | OT lead and OEM |
| 2 | Safety interlocks, limit switches and emergency stops tested under the OEM's return-to-service procedure, with no load and then with a test load | Senior crane electrician; OEM |
| 3 | Local-control operation for one shift with a supervisor present | Shift superintendent |
| 4 | Reconnection to the TOS through the T1 OT zone firewall, or the T2 temporary firewall | OT network engineer; CySO |
| 5 | Vendor remote access restored only through the privileged remote access service, with named accounts, MFA, per-session approval and recording (POL-02 4.10) | Director of Maintenance and Engineering; CySO |
| 6 | Lockout removed; the crane returns to vessel work | Terminal General Manager |

Tell the COTP, the crew, longshore labor (through the hiring hall) and affected carriers when each crane is back in service (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of return to service; written report within 30 days (POL-03 4.13), including the safety analysis from section 4.6.
- Update the risk register (P01: R-002, R-003, R-018, R-037, R-042), the POA&M (P07, especially POAM-003, POAM-011 and POAM-022), the vendor contract (POAM-019), this runbook and the Cybersecurity Plan (101.650(g)(3)).
- Review all 27 vendor access paths against the lessons learned, not only the one involved.
- Keep all incident records for at least 2 years (POL-01 4.11; 101.640).
- Use the incident as a scenario in the next cyber drill and the annual exercise at both terminals (101.635).

# Incident Response Runbook: Intrusion into Process Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical formulator and packager) |
| Tier / Vertical | Small / Chemical |
| Incident type | Intrusion into the DCS through the integrator's remote access path. The attacker changes setpoints and alarm limits on the aqueous ammonia process, then deploys ransomware on the historian and HMIs |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 (sec. 3.3.8 and 6.4) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (security officer for IT and OT), with the Plant Manager for process decisions |
| Approved | 2026-09-04 by the VP Operations and the Plant Manager |
| Last tested | Not yet. First OT tabletop exercise due 2026-11-30 (POAM-008). The 2026 RMP notification exercise will use this scenario with the business network down (POAM-011) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (process) | Plant Manager | Shift Supervisor on duty until the Plant Manager arrives | Control room radio; cellular phone |
| Cyber incident lead | IT Manager | Systems administrator | Incident line (cellular); out-of-band group on company cellular phones |
| OT technical lead | Controls Engineer | DCS integrator lead engineer (on-site only, once the remote path is cut) | Cellular phone |
| Release reporting and responders | EHS Manager | Plant Manager | Cellular phone; printed call list in the control room and gatehouse |
| Legal counsel | Outside counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Forensics (IT and OT) | Forensic firm with OT experience (retainer, POAM-008) | DCS vendor incident response service | Numbers in the incident binder |
| Communications | VP Operations | Customer Service Manager (customers only) | Cellular phone |
| Law enforcement and CISA | FBI field office | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the business network, email, and VoIP phones are compromised or down. Use company cellular phones, handheld radios, and the printed incident binder in the control room and gatehouse.

## 1. Preparation checks (Identify / Protect)
- [ ] Incident binder in the control room and gatehouse: this runbook, the notification matrix, call lists, the loss-of-DCS operating procedure, and network diagrams (Restricted-Security, POL-04)
- [ ] Cellular phones charged and a radio at the gate; emergency notification tested with the business network down (CP-8). **Gap until POAM-011 closes (2026-11-30)**
- [ ] Offline, verified copy of the DCS configuration, recipes, and SIS program less than 7 days old, plus a restore test within 90 days (CP-9, CP-4). **Gap until POAM-004 and POAM-005 close**
- [ ] SIS keyswitch in run and locked; checked this shift (POAM-003)
- [ ] Integrator remote tool disabled except for supervised call-in sessions (interim), then replaced by the remote access gateway (POAM-001)
- [ ] Firewall and remote access logs kept at least 90 days, and 1 year in the log workspace once POAM-012 closes (AU-11)
- [ ] Forensic and DCS vendor response retainers signed (POAM-008)
- [ ] Clean spare hardware for 1 operator station and the EWS, and vendor installation media with verified hashes

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Setpoint, alarm limit, or controller mode changes no operator made | Operator notices; DCS event journal; process drifting toward limits | Shift Supervisor takes manual control or puts the unit in a safe state, then calls the incident line |
| Alarms that should have sounded did not, or alarm limits are wider than the safe limits | Operator rounds; field gauges disagree with HMI values | Treat the HMI as untrusted; use field gauges and the SIS status panel |
| Mouse moving or screens changing on the EWS or an HMI with no one at it | Operator or Controls Engineer | Do not touch it. Photograph the screen. Pull the EWS network cable. Call the incident line |
| SIS trip, or ammonia gas detector alarm, with no clear process cause | SIS panel; gas detection | Follow the emergency action plan first. Then report as a possible cyber cause |
| Ransom note, or historian and HMI screens locked or encrypted | Operators; historian users | Isolate (section 3). Do not pay or contact the attacker |
| Unusual remote session, or firewall traffic from the integrator's address outside a scheduled session | Firewall or remote access logs; passive sensor once installed (POAM-012) | IT Manager opens an incident and cuts the remote path |

**Declare an OT cyber incident when** any unexplained change to setpoints, alarms, logic, or recipes is confirmed, when an unauthorized remote session into OT is seen, or when malware or a ransom note appears on any OT workstation or the historian.

**Record the time of discovery** in the incident log. Release reporting clocks run from knowledge of the release, not from the cyber declaration.

## 3. First hour: safe state first (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safe state.** Stop ammonia additions and transfers. Close the ammonia remote isolation valve from the SIS panel if levels, pressures, or HMI values cannot be trusted. Hold Blend Hall A. Use field gauges and portable ammonia detectors | Shift Supervisor | Process stable and verified by field readings |
| 2. **Release check.** If ammonia is released or gas detectors alarm, follow the emergency action plan: evacuate, call 911, then the release notices in section 6 | Shift Supervisor; EHS Manager | Responders called; notices under way |
| 3. **Cut the remote path.** Disable the integrator's remote tool and block the integrator's addresses at the IT/OT firewall. Disconnect the historian's business-side network card | IT Manager (Controls Engineer if on site first) | No inbound remote path to OT |
| 4. **Isolate OT from IT.** Set the IT/OT firewall to deny all traffic. The DCS controllers and SIS keep running without the business network | IT Manager with the Controls Engineer | Firewall in deny-all; plant control continues locally |
| 5. **Do not power off** HMIs, the EWS, or the DCS servers unless the Plant Manager decides the process requires it. Pull network cables from infected workstations only | Controls Engineer | Evidence kept in memory |
| 6. **Check the SIS.** Confirm the keyswitch is in run and locked. Confirm SIS trips are healthy from the SIS panel, not from the DCS | Controls Engineer; I&E technician | SIS confirmed independent and in run |
| 7. **Call the insurer; engage counsel and OT forensics** through the insurer | Controller | Claim number issued |
| 8. **Start the incident log:** timeline, decisions, who did what, and when | IT Manager | Log open (paper if needed) |

## 4. Analysis (RS.AN)
1. **Cyber cause screening.** For every unexplained process event during the incident window, ask these questions. The same questions are added to the RMP incident investigation procedure (P03 G-054).
   - Was the change made from the EWS, an HMI, or the integrator's session?
   - Which account made it? The DCS event journal shows the account, though shared accounts limit attribution until POAM-009 closes.
   - Does the running configuration match the last good offline copy?
   - Does the SIS program checksum match the approved copy?
2. **Scope.** Which components were reached: the EWS, operator stations, the DCS servers, the historian, the SIS? Check the firewall logs, the remote tool's own logs on the EWS, Windows event logs, and the DCS event journal. Check the business network for the initial foothold (phishing, VPN).
3. **Evidence preservation (chain of custody).**
   - Export the DCS event journal and SIS event log before they roll over. The DCS keeps about 90 days.
   - Save firewall logs, even though only errors are logged today.
   - Have forensics take memory captures and disk images of the EWS, affected HMIs, and the historian.
   - Photograph screens, the keyswitch, and any USB drives.
   - Keep the USB backup drive sealed. It may hold the attacker's changes.
4. **Integrity of the process.** The Controls Engineer and Process Engineer compare every setpoint, alarm limit, and interlock bypass with the RMP safety information (40 CFR 68.48(a)(3)) and the configuration baseline. They also compare master recipes with the ERP bills of materials. List every difference.
5. **Data taken.** Check for theft of recipes, OT diagrams, legacy CVI, or employee personal information. Any theft of employee personal information drives the Florida breach notice rows of the matrix.
6. **Backups.** Confirm the offline copy is intact and older than the first sign of intrusion before using it.

## 5. Containment and eradication (RS.MI)
1. Keep OT isolated from IT until eradication is confirmed. The plant can run Blend Hall B and ship finished goods on paper (P05).
2. Disable the shared integrator account and all shared DCS engineering accounts. Rotate all DCS, SIS, historian, and firewall passwords from a clean workstation.
3. **Remove the remote desktop tool permanently.** No vendor remote access until the gateway with MFA, approval, and recording is in place (POL-02 4.6).
4. Rebuild infected HMIs, the EWS, and the historian from vendor media with verified hashes. **Do not decrypt and reuse them.**
5. Restore DCS configuration and recipes only from a verified offline copy, and only after the Controls Engineer has reconciled every difference found in section 4 step 4.
6. Remove the SIS engineering software from the EWS (POAM-003). Reload the SIS program from the approved copy only if the checksum differs, and then a full proof test is required before restart.
7. Forensics confirms that no persistence remains on the business network (VPN accounts, the domain, and office endpoints) before any IT/OT connection is restored.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Release notices never wait for the cyber investigation. Counsel confirms all other notices before they go out.

| When | Action | Owner |
|---|---|---|
| Immediately, if a release at or above an RQ occurs (ammonia 100 lb) | National Response Center (40 CFR 302.6); SERC and LEPC (40 CFR 355.40-355.43); 911 for county fire rescue (68.90(b)(3)) | EHS Manager (Shift Supervisor calls 911 first) |
| Within 8 or 24 hours | OSHA, if a worker dies (8 h) or is hospitalized, or suffers an amputation or loss of an eye (24 h) (29 CFR 1904.39) | EHS Manager |
| Within 48 hours | Start the RMP incident investigation if the event could reasonably have caused a catastrophic release (68.60(b)). A manipulated ammonia setpoint meets this test | EHS Manager |
| Day 0 | Insurer notified; counsel and forensics engaged | Controller |
| Within 24 hours (company target) | Voluntary report to CISA and the FBI. It helps with response support and is a mitigating factor if a ransom payment is ever considered | IT Manager |
| As soon as practicable | Written follow-up to the SERC and LEPC after any immediate EPCRA notice (355.40(b)) | EHS Manager |
| Day 1-3 | Customer notice of delivery impact (not a breach notice) | Customer Service Manager, approved by the VP Operations |
| Within 30 days of determination | Florida notice to affected employees if their personal information was breached (Fla. Stat. 501.171(4)) | HR Manager with counsel |
| Within 6 months | RMP accident history correction if the 68.42 criteria are met (68.195(a)); a public meeting within 90 days if there were offsite impacts (68.210(b)) | EHS Manager |

**Not required:**
- CFATS reporting: authority expired 2023-07-28 and has not been reauthorized.
- CIRCIA: proposed only.
- USCG MTSA reporting: not an MTSA facility.
- FAR 52.204-25: no federal contracts.

**Ransom decision:** requires the CEO, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). The plant's recovery plan does not depend on payment: the DCS is rebuilt from verified offline copies, not decrypted.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6). **Safety gates come before speed.**
1. Emergency notification path (BP-09): cellular phones and call lists, already in use
2. SIS verified: checksum matches the approved copy, keyswitch in run, and a proof test if the program was reloaded (BP-02)
3. Tank farm level monitoring (BP-03): manual gauging until the DCS is trusted
4. Clean DCS configuration and recipes (BP-04), restored from the verified offline copy and reconciled line by line with the safety information
5. **Blend Hall A restart (BP-01).** The Plant Manager approves it after a pre-startup review that confirms:
   - setpoints, alarm limits, and interlocks match the safe limits
   - all accounts are rotated
   - the remote path is removed
   - an MOC is recorded for the restoration
6. ERP access and the loading rack (BP-07), then the LIMS (BP-05), physical security systems (BP-08), packaging (BP-06), finance (BP-10), and payroll (BP-11)
7. **Historian and AI-001 last,** from clean media, with one-way replication only. AI-001 recommendations stay off until the Process Engineer confirms the historian replica was not altered (P10)

**Realistic timing today:** with no tested offline backup, rebuilding Blend Hall A could take weeks (P05 key finding). After POAM-004 and POAM-005 close, the target is the 12-hour RTO for BP-01.

**Recovery communications:** tell operators, customers, the LEPC (if it was notified of a release), and the insurer when each service is restored.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of restart. POL-03 4.11 requires documentation within 30 days.
- Complete the RMP incident investigation report, including cyber contributing factors, and resolve its recommendations (68.60(d)-(e)).
- If the hazard review is affected, update it (68.50(d)). If the RMP must be corrected, file within the 68.195 deadlines.
- Update the risk register (P01, especially R-001, R-002, R-006, R-007, and R-027), the POA&M (P07), the SSP (P02), and this runbook.
- Keep incident records for at least 5 years (POL-04 4.9; 40 CFR 68.200; 68.60(g)).

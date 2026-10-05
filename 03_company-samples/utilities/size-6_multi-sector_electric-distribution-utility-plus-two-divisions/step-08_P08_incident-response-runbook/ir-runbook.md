# Incident Response Runbook: Intrusion into Distribution Control Systems (OT) Spanning Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Utilities |
| Incident type | Intrusion into distribution control systems (OT) that enters through a shared service and touches all three divisions: unauthorized commands on the Distribution Operations Platform (DOP), probing of a low impact transmission substation and the TCC, an attempt on the Gas Production POC, and theft of client and Electric Utility BCSI from Engineering Services |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT practices from NIST SP 800-82 Rev. 3 |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06). For the Electric Utility this runbook supports, and does not replace, the CIP-008-6 plan (TCC), the CIP-003-9 low impact plan (substations), and the EOP-004-4 Operating Plan |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel; operational decisions by the control center shift supervisors |
| Approved | 2026-09-15 by the Group CISO, the Group General Counsel, and the CIP Senior Manager |
| Last tested | Technical SOC playbooks tested quarterly; CIP-008-6 plan tested 2025-11-12. **The cross-division notification matrix and a DOP intrusion have never been exercised** (scenario gap 9); the first cross-division tabletop is due 2026-12-15 (POAM-004) |

**Safety first.** The grid and field operations must stay safe for the public, line crews, and field operators. The control center shift supervisor on duty decides every isolation step that affects operations (POL-03 4.3). Crews working under clearances are protected before anything else.

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Times are illustrative.
- **Entry (Day 0, 09:40):** an Engineering Services protection engineer clicks an adversary-in-the-middle phishing link. The attacker steals the session token for SYS-G1 and uses it at the SYS-G4 gateway, where the engineer's role holds standing access to the DOP, the 74 substations, and the Gas Production POC (P07 AC-02i.02; P01 GR-01).
- **Engineering Services data (10:05 to 13:30):** with the same session, the attacker downloads files from SYS-S1: three client projects (one with a client's substation BCSI) and the Electric Utility TCC network diagrams that were stored there (P03 G-031).
- **DOP (13:50 to 14:20):** from the DOP jump host the attacker reaches an engineering workstation using the engineer's DOP role and, at 14:05, sends open commands to 6 feeders in one district: about 38,000 customers (about 70 MW) lose power. The attacker also tries to log in to a transmission substation gateway through a front-end processor path (the broad gateway rules, P03 G-011) and scans the TCC Electronic Access Point from the DOP DMZ.
- **Gas Production (14:30):** the attacker opens a session to the POC jump host; SCADA console logins fail.
- **Detection:** at 14:07 a DCC operator sees breaker operations no one ordered; at 14:09 the TCC EAP sensor alerts the group SOC.
- **Restoration:** DCC operators close the feeders by SCADA at 14:40 after confirming the field is safe, then by crews where SCADA is distrusted; all customers are restored by 15:15.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Operational incident commander (DOP) | DCC shift supervisor | Electric Utility distribution operations director | DCC console phone; radio |
| Operational lead (TCC) | TCC shift supervisor | Electric Utility system operations director | TCC console phone |
| Operational lead (Gas Production) | POC shift supervisor | Gas Production vice president of operations | POC phone; radio |
| Technical incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| OT remote access | Group OT security director | SYS-G4 on-call engineer | Bridge |
| CIP determinations and reports | Electric Utility NERC compliance director | On-call compliance analyst | Bridge; printed forms at both TCCs and DCCs |
| CIP Senior Manager | Electric Utility senior vice president of transmission and distribution operations | Electric Utility president | Bridge |
| Client notices | Engineering Services contracts director | Engineering Services security and compliance lead | Bridge |
| Legal and notifications | Group General Counsel with outside counsel | Division general counsels | Bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Electric Utility customer operations director | Bridge |
| External | RC, BA, neighboring TOPs; DOE Emergency Operations Center; E-ISAC; CISA; FBI field office; insurer hotline | | Printed binder at each control center |

**Out-of-band first.** Assume the attacker can read corporate email, chat, and anything reachable with SYS-G1 sessions. Use the crisis line, control center phones, and radio.

## 2. Preparation checks (Identify / Protect)
- [x] Printed binders at the TCC, backup TCC, DCC, backup DCC, and POC: this runbook, the notification matrix, contacts, DOE-417 forms, and manual switching procedures
- [x] Manual switching procedures for every feeder; crews trained in storm drills
- [x] OT network sensors at the TCC EAPs (CIP-005-7 Part 1.5)
- [ ] Per-session approval and no standing affiliate access on SYS-G4 (**gap until POAM-001 closes**)
- [ ] OT sensors in the DCC networks (**gap until POAM-003 closes**)
- [ ] Offline, immutable DOP backups with a tested full restore (**gap until POAM-009 closes**)
- [ ] DCC reporting checklist with DOE-417 criteria 2, 3, 11, 12, and 14 (**gap until POAM-004 closes**)
- [ ] Client notice register at Engineering Services (**gap until POAM-021 closes**)
- [x] OT-capable incident response firm through the insurer panel
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A breaker, recloser, or switch operates and no operator, crew, or automatic scheme did it | DOP event log; operator | Shift supervisor treats it as a possible intrusion; calls the SOC |
| Alert on a TCC EAP sensor or Intermediate System | Group SOC | Apply the CIP-008-6 attempt criteria; call the TCC shift supervisor and the NERC compliance director |
| SYS-G4 session the OT owner did not approve, or from an unusual location | SYS-G4; SOC | Terminate the session; disable the account |
| Failed logins on a substation gateway or POC console | Gateway logs; POC | Notify the SOC and the OT owner |
| Bulk downloads of CEII or BCSI folders on SYS-S1 | SYS-S1 events; SOC | Suspend the account; start client notice assessment |

**Severity 1** (POL-03 4.2): any effect on grid or field operations, any suspected compromise of an OT environment or SYS-G4, or more than one division involved. This scenario meets all three.

**Record the clock times** (POL-03 4.4), because each duty runs from a different one:
- **Incident occurred** (14:05 feeder commands): DOE-417 Emergency Alert within 1 hour, so by **15:05**.
- **Determination of an attempt to compromise** the TCC EACMS (made 15:40 by the NERC compliance director with the CIP Senior Manager): CIP-008-6 notice by the **end of the next calendar day**.
- **Engineering Services identifies the client-data incident** (16:30, when the SOC links the SYS-S1 downloads to the stolen session): client notices within 24, 48, or 72 hours by contract.
- **Disclosure committee convened** within 24 hours of the Severity 1 declaration; the 4-business-day Form 8-K clock starts only at a materiality determination.

## 4. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Make the grid safe: confirm every crew clearance in the affected district; put the 6 feeders and their devices in local or manual control; send crews | DCC shift supervisor | Crews confirmed safe; manual control in place |
| 2. Cut the attacker's path: terminate all SYS-G4 sessions; disable the engineer's SYS-G1 and SYS-G4 accounts and revoke tokens; suspend all Engineering Services entitlements on SYS-G4 | Group OT security director; group identity director | Sessions ended; entitlements suspended |
| 3. Isolate, do not power off: disconnect the DOP DMZ from the corporate network and from the SYS-G4 connector. Keep the DOP running if trusted for monitoring; otherwise operate manually | OT engineering manager; DCC shift supervisor decides | Isolation recorded; operating mode recorded |
| 4. Notify the TCC, the RC, and neighboring TOPs that a distribution intrusion is under way and that the TCC EAP was probed | TCC shift supervisor | Calls logged |
| 5. **DOE-417 Emergency Alert by 15:05** (criterion 3; check criterion 14 as well once the attempt is determined). Phone the DOE Emergency Operations Center first if operations are critical | DCC shift supervisor starts; NERC compliance director files | Form submitted or phoned |
| 6. POC on alert: disconnect the POC SYS-G4 connector; confirm wells and stations are on safe control | POC shift supervisor | Connector off; status confirmed |
| 7. Call the insurer hotline; engage counsel and the OT-capable response firm | Group Chief Risk Officer | Claim number issued |
| 8. Brief the Group CISO and the CIP Senior Manager; convene the disclosure committee within 24 hours | Group CISO; Group General Counsel | Committee scheduled |

## 5. Analysis (RS.AN)
1. **Scope by environment.** From SYS-G4 recordings, DOP and domain logs, substation gateway logs, the TCC EAP sensor, POC logs, and SYS-S1 events, list every system touched. Note the DOP logs are not in the SIEM (POAM-008); export them before they roll over.
2. **CIP determinations (Electric Utility).**
   - TCC: did any BES Cyber System or EACMS get compromised or disrupted? If yes, it is a Reportable Cyber Security Incident (CIP-008-6 R4, 1 hour). In the scenario the EAP blocked the scan: an **attempt to compromise** under the plan's criteria (end of next calendar day).
   - Substation gateway: the login attempts failed and the relays were unaffected, so the low impact incident is **not Reportable**. Record the determination and approver; CIP-003-9 has no attempt reporting.
   - The DOP is not a BES Cyber System: its event is reported through DOE-417 criterion 3, not CIP-008.
3. **BCSI and CEII.** List every file taken from SYS-S1, by client. The Electric Utility TCC diagrams are its own BCSI: treat them as compromised, review EACMS rule sets they describe, and record the event for the CIP-004-7 R6 and CIP-011-3 self-report (POAM-015).
4. **Personal information.** Confirm whether any file or mailbox content held personal information (SSNs, bank accounts, credentials). That decides state breach notices. In the scenario none was found.
5. **Gas Production.** Confirm the POC console logins failed and no SCADA values changed. Compare RTU and PLC values with field readings at two compressor stations.
6. **Root cause** for P01: phishing-resistant MFA not required for engineers, standing SYS-G4 access (GR-01), broad gateway rules (EU-021), BCSI on SYS-S1 (GR-06).

## 6. Containment and eradication (RS.MI)
1. Keep all Engineering Services and vendor SYS-G4 access suspended until per-session approval is in force for the DOP (accelerates POAM-001). Restore access one named engineer at a time, by work order.
2. Reset all DOP domain, jump host, and engineering workstation credentials from a clean workstation; rotate any gateway credentials the attacker tried.
3. Limit gateway rules at all 74 substations to DNP3 from the FEPs before reconnecting (accelerates POAM-014).
4. Rebuild the DOP jump host and the engineering workstation from vendor media; do not reuse them.
5. Verify relay settings at the probed substation against approved files; the TCC decides whether the 230 kV and 115 kV elements stay in service meanwhile.
6. Remove the phished engineer's SYS-S1 sessions; restrict CEII and BCSI folders on the affected projects (accelerates POAM-020).
7. Confirm with the response firm that no persistence remains in SYS-G4, SYS-G1, the DOP, or the POC before reconnecting.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (29 rows).** The NERC compliance director runs the Electric Utility clocks; the Engineering Services contracts director runs the client clocks; the Group General Counsel approves every other external notice.

| When (Day 0 is the incident) | Action | Owner |
|---|---|---|
| Immediately | RC, BA, and neighboring TOPs by phone | TCC shift supervisor |
| Day 0, by 15:05 (1 hour after the 14:05 commands) | DOE-417 Emergency Alert, criterion 3 | DCC shift supervisor; NERC compliance director |
| Day 0 | Voluntary report to CISA and the FBI; insurer notice | Group CISO; Group Chief Risk Officer |
| Day 0 | Engineering Services notifies the Electric Utility on the bridge (affiliate as vendor, POL-01 4.8) | Engineering Services security and compliance lead |
| Same day as the decision | Clients told to revoke the phished engineer's access at their sites | Engineering Services contracts director |
| By end of Day 1 (next calendar day after the 15:40 determination) | CIP-008-6 R4 attempt notice to the E-ISAC and CISA (or through DOE-417 criterion 14 shared with both) | NERC compliance director |
| Within 24 hours of the Severity 1 declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 24, 48, or 72 hours of identification (16:30 Day 0), per contract | Notices to the 3 clients whose files were taken | Engineering Services contracts director |
| Within 72 hours of the incident | DOE-417 final report | NERC compliance director |
| Within 7 calendar days of new information | CIP-008-6 updates | NERC compliance director |
| Within 4 business days of a materiality determination | Form 8-K Item 1.05, if the committee finds the incident material | Disclosure committee; Group General Counsel |
| Only if personal information was taken | State breach notices (Florida worked example: 30 days after determination) | Group Chief Privacy Officer |
| Checked and not triggered | EOP-004-4 (about 70 MW, below the 300 MW threshold; no damage); TSA (no pipeline); FAR 52.204-25 and 52.204-23 (no covered equipment found) | NERC compliance director; Engineering Services federal programs manager |

**Plan to the shortest clock.** In this scenario the order is: DOE-417 Emergency Alert (1 hour), client access revocation (same day), CIP-008-6 attempt notice (next calendar day), 24-hour client notices and the disclosure committee, DOE-417 final report (72 hours), 72-hour client notices, then any Form 8-K and state notices.

**Materiality factors for the disclosure committee:** customer outage (38,000 customers for about 70 minutes) and public safety implications; regulatory exposure (NERC self-reports, DOE, state regulators); client relationships and contracts at Engineering Services; cost of response and remediation; reputational effect of an OT intrusion at a public utility. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination, not at discovery.

**Ransom or extortion:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.7).

**Customer communications:** outage updates through the IVR, outage map, and media; no attack details without counsel.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Manual operation by crews and radio dispatch (from step 1)
2. TCC normal operation confirmed (it was not compromised)
3. DOP on trusted servers: standby cluster if clean, otherwise rebuild (RTO 2 hours; unproven after a destructive attack until POAM-009)
4. Field communications and substation gateways, one district at a time, after gateway rules are verified
5. OMS and customer outage communications
6. Gas Production POC connector, after the POC owner confirms integrity
7. SYS-S1 access for Engineering Services, project by project, with restricted CEII and BCSI folders
8. **SYS-G4 last** (BIA priority 18): only with per-session approval and no standing affiliate access

**Validate before reconnecting:** credentials rotated, systems rebuilt or verified, monitoring in place, remote access off until approved. Tell customers and clients when service is restored (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10). For the CIP-008-6 plan, document lessons and update the plan within 90 calendar days of the response (CIP-008-6 R3 Part 3.1).
- Update P01 (GR-01, GR-02, GR-03, GR-06, EU-001, EU-021, ES-003), the POA&M (POAM-001, POAM-003, POAM-004, POAM-009, POAM-014, POAM-015, POAM-020, POAM-021), the notification matrix, and this runbook.
- Add the facts to the CIP Senior Manager's self-report decisions (POL-01 4.13).
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain incident records for 6 years, and CIP evidence for at least three calendar years (POL-01 4.11).

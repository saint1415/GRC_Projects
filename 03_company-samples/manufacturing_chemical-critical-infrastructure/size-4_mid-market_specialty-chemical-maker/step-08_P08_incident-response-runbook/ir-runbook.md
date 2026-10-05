# Incident Response Runbook 1: Intrusion into the Port Plant Process Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed specialty chemical formulator and packager) |
| Tier / Vertical | Mid-Market / Chemical |
| Incident type | An attacker reaches the Port plant PCBMS through a vendor session on the OT remote access gateway (or through a foothold on the business network and the IT/OT conduits), changes Ammonia Unit setpoints and alarm limits, probes the SIS engineering workstation, and then deploys destructive malware on the historian, historian clients, and terminal HMIs |
| Second runbook | `ir-runbook-ransomware.md` (ransomware with data theft on corporate IT and the cloud) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy; part of the Cyber Incident Response Plan required by 33 CFR 101.620(b)(6) and 101.650(g)(2) |
| Runbook owner | Information Security Manager (CySO), with the Port Plant Manager for process decisions |
| Approved | 2026-09-22 by the Chief Operating Officer and the Port Plant Manager |
| Last tested | Not yet. Joint cyber and process tabletop on 2026-11-17 (also the RMP tabletop under 40 CFR 68.96(b)(2) and the first USCG exercise under 33 CFR 101.635(c)); POAM-011 |

## 0. Roles, crisis management, and legal (Govern)
**Three teams, one timeline.** The process incident command (in the control room), the cyber incident team (in the OT server room or the emergency operations center), and the crisis management team (at headquarters or by phone bridge) work from one incident log kept by the cyber incident team.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Process incident commander | Port Plant Manager | Shift Supervisor on duty until relieved | Control room radio; company cellular phone |
| Cyber incident manager | Information Security Manager (CySO) | OT Security Engineer (alternate CySO) | Incident line (cellular); out-of-band chat on company phones |
| OT technical lead | Controls Engineering Manager | Senior Port controls engineer; DCS integrator lead (on site only) | Cellular phone |
| Process safety | Process Safety Manager (Port plant) | VP EHS and Process Safety | Cellular phone |
| Emergency response team and release reporting | VP EHS and Process Safety | Emergency response team leader | Radio; printed call list |
| MTSA reporting | Facility Security Officer | CySO | Cellular phone; FSP contact sheet |
| Crisis management team chair | Chief Operating Officer | Chief Executive Officer | Phone bridge in the incident binder |
| Legal and privilege | General Counsel (engages outside counsel through the insurer panel) | Outside counsel | Cellular phone |
| Finance, insurer, lenders | Chief Financial Officer | Controller | Carrier hotline on the policy card |
| Communications (customers, media, community) | Director of Corporate Communications, approved by the COO | Director of Customer Solutions (customers only) | Cellular phone |
| External support | MSSP (IT); DCS vendor incident response service (OT forensics); insurer panel forensics | | Numbers in the incident binder |

**Legal privilege.** Forensic firms are engaged by outside counsel. Written analysis goes to counsel. Facts needed for safety and regulatory reports are never held back for privilege.

**Out-of-band first.** Assume the business network, email, and VoIP are compromised. Use company cellular phones, radios, the satellite phone in the control room, and the printed incident binder (control room, gatehouse, emergency response vehicle).

## 1. Preparation checks (Identify / Protect)
- [ ] Incident binder current: this runbook, `notification-matrix.csv`, call lists checked monthly, the operating procedure for an untrusted DCS, network maps (SSI, POL-04). **Call list gap until POAM-016 closes (2026-11-17)**
- [ ] Verified offline copies of DCS, batch, and SIS configurations less than 7 days old in the fire safe, with hashes (CP-9). **Restore never tested until POAM-005 (2026-11-10)**
- [ ] SIS keyswitches in run; position checked each shift (keyswitch alarm due under POAM-006)
- [ ] Gateway approvals recorded in the gateway (from 2026-10-01); vendor accounts limited to their zones
- [ ] OT sensor alerts routed to the control room until the MSSP OT service starts (POAM-004)
- [ ] DCS vendor incident response service and insurer panel forensics (with OT experience) on contract
- [ ] Clean spare hardware: one DCS server, two operator stations, one EWS; vendor media with verified hashes

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Setpoint, alarm limit, or controller mode changes no operator made | Operator; DCS event journal; process drifting toward limits | Shift Supervisor takes the unit to a safe state (section 3), then calls the incident line |
| Field gauges disagree with HMI values; alarms that should have sounded did not | Operator rounds; terminal staff | Treat the HMI as untrusted; use field gauges and the SIS panel |
| Activity on an EWS or the SIS EWS with nobody at it; a gateway session nobody approved | Operator; OT Security Engineer; gateway log | Do not touch it. Photograph the screen. End the gateway session; pull the network cable from the workstation |
| OT sensor alert: new engineering protocol traffic, a scan, or a new device | OT sensor (control room display) | Shift Supervisor informs the CySO; CySO decides on declaration within 30 minutes |
| SIS trip or gas detection alarm with no clear process cause | SIS panel; gas detection | Emergency response plan first; report as a possible cyber cause |
| Tank level reading jumps, or tank gauging values differ from manual dips | Terminal staff | Stop transfers; gauge manually; call the incident line |
| Ransom note or locked screens on the historian, historian clients, or HMIs | Operators | Isolate (section 3); do not contact the attacker |

**Declare an OT cyber incident** when any unexplained change to setpoints, alarm limits, logic, recipes, or tank data is confirmed; when an unauthorized session into OT is seen; or when malware appears on any OT system. The CySO declares; the Shift Supervisor does not need permission to put units in a safe state.

**Severity.** OT-1: any manipulation of control or safety functions, or any release. OT-2: malware or unauthorized access in OT without process effect. OT-3: suspicious activity under investigation. OT-1 convenes the crisis management team within 1 hour.

**Record the time of discovery.** The 6.16-1 report is due immediately; release reporting runs from knowledge of the release, not from the cyber declaration.

## 3. First hour: safe state first (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safe state.** Stop ammonia unloading, transfers, and dilution. Close the Ammonia Unit remote isolation valves from the SIS panel if HMI values cannot be trusted. Hold the Peroxide Unit with temperature trips active. Stop all tank farm transfers and any barge transfer (local emergency stop). Hold Blend Hall 1 batches | Shift Supervisor | Units stable on field readings |
| 2. **Release check.** If ammonia is released or detectors alarm: emergency response plan, shelter-in-place or evacuation, 911, community notification from the cellular launch path, then the release notices | Shift Supervisor; emergency response team; VP EHS | Responders called; notices under way |
| 3. **Report under 6.16-1.** Call the FBI, CISA, and the Captain of the Port immediately. A suspected manipulation is enough; the rule covers threatened incidents | FSO with the CySO | Reports made and logged with times and reference numbers |
| 4. **Cut remote access.** Disable all vendor accounts on the gateway; block the gateway's outbound sessions at the firewall | OT Security Engineer | No remote path into OT |
| 5. **Isolate OT from IT.** Set the IT/OT firewall pair to deny all except the historian replica (turned off if the historian is affected). DCS controllers and the SIS run without the business network | OT Security Engineer with the Controls Engineering Manager | Firewall in deny-all; local control continues |
| 6. **Do not power off** DCS servers, EWS, or HMIs unless the process incident commander decides the process requires it. Pull network cables from affected workstations only | Controls Engineering Manager | Memory evidence kept |
| 7. **Check the SIS.** Keyswitches in run; trips healthy from the SIS panel; SIS EWS disconnected from the SIS network until checked | Process Safety Manager; I&E | SIS confirmed independent |
| 8. **Call the insurer; counsel engages forensics** (insurer panel and the DCS vendor service) | CFO; General Counsel | Claim number; engagement letters |
| 9. **Convene the crisis management team** (OT-1) | COO | First call held within 1 hour |

## 4. Analysis (RS.AN)
1. **Cyber cause screening** for every unexplained process event: which workstation, which account (limited by shared console accounts until POAM-002 closes), does the running configuration match the last good offline copy, does the SIS logic match the approved copy? The same questions start the RMP and PSM incident investigations (68.81; 1910.119(m)), which must begin within 48 hours.
2. **Scope.** Gateway session logs and recordings, firewall and conduit logs in the SIEM, OT sensor records, DCS event journals, Windows logs on DCS servers and workstations, and the business network for the initial foothold (phishing, vendor credential theft).
3. **Evidence and chain of custody.** Export DCS and SIS event logs before they roll over (about 90 days). Preserve gateway recordings. Forensics takes memory and disk images of the EWS, SIS EWS, affected HMIs, and the historian. Photograph screens and keyswitches. Seal the most recent offline backup until it is checked.
4. **Process integrity.** The Controls Engineering Manager and Process Safety Manager compare every setpoint, alarm limit, interlock bypass, and tank level limit with the process safety information (68.65; 1910.119(d)) and the configuration baseline; the Director of Technical Services compares master recipes with the ERP bills of materials. Every difference is listed.
5. **Data taken.** Check for theft of recipes, network maps, the FSP or Cybersecurity Plan drafts (SSI), and legacy CVI. SSI loss is reported to the Coast Guard through the FSO; the 6.16-1 report covers data on the facility.
6. **Clean backup point.** Confirm the offline copy predates the first sign of intrusion (gateway and sensor records) before using it.

## 5. Containment and eradication (RS.MI)
1. Keep OT isolated from IT until eradication is confirmed. The plant can ship from storage, run manual gauging, and use the Inland plant for the top 15 formulations (P05).
2. Disable all vendor gateway accounts and shared console accounts; rotate every DCS, SIS, terminal, gateway, and firewall credential from a clean workstation.
3. Vendor access returns only through the gateway with phishing-resistant MFA, per-session approval, and live monitoring by the OT Security Engineer.
4. Rebuild affected servers and workstations from vendor media with verified hashes. **Do not decrypt and reuse them.**
5. Restore configurations and recipes only from a verified offline copy, after every difference from section 4 is reconciled.
6. Reload SIS logic from the approved copy only if the compare fails; a full proof test is then required before restart.
7. Forensics confirms no persistence on the business network and in the identity provider before any IT/OT connection is restored.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Safety and release notices never wait for the cyber investigation. Counsel reviews other notices before they go out, but does not delay them past their deadlines.

| When | Action | Owner |
|---|---|---|
| Immediately | 911 and community notification if the public may be affected (68.95); National Response Center for a release at or above an RQ (302.6); LEPC and SERC (355.40-355.43) | Shift Supervisor; VP EHS and Process Safety |
| Immediately | FBI, CISA, and the Captain of the Port (33 CFR 6.16-1). This also meets the NRC reporting duty for reportable cyber incidents (101.620(b)(7)) | FSO with the CySO |
| Without delay | NRC report of any breach of security or suspicious activity; COTP report of any TSI (101.305) | FSO |
| Within 8 or 24 hours | OSHA, for a fatality (8 h) or hospitalization, amputation, or eye loss (24 h) (29 CFR 1904.39) | VP EHS and Process Safety |
| Within 48 hours | Start the RMP and PSM incident investigations (68.81(b); 1910.119(m)(2)) | Process Safety Manager |
| Day 0 | Insurer; outside counsel; PE sponsor and lender notice per the agreements | CFO; General Counsel |
| Day 0-1 | Water utility and pulp and paper customers: supply status and allocation (not a breach notice) | Director of Customer Solutions; VP Sales and Customer Service |
| As soon as practicable | Written EPCRA follow-up (355.40(b)) | VP EHS and Process Safety |
| Within 6 months / 90 days | RMP accident history update (68.195(a)); public meeting if offsite impacts (68.210(b)) | VP EHS and Process Safety |

**Community and media.** Statements about a release come from the process incident commander with county fire rescue. Statements about a cyber cause are approved by the General Counsel and the COO, and are coordinated with the FBI and the Coast Guard.

**Ransom decision.** Requires the CEO, counsel, the insurer, and an OFAC sanctions check (POL-03 4.9). Recovery does not depend on payment: the PCBMS is rebuilt from verified offline copies.

**Not required:** CFATS reporting (authority lapsed); CIRCIA (proposed only); SEC 8-K (privately held).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 8). **Safety gates come before speed.**
1. Emergency notification and response (BP-10): cellular path, already in use
2. SIS verified: logic compare passes, keyswitches in run, proof test if logic was reloaded (BP-06)
3. Tank farm levels (BP-02): manual gauging until tank gauging is rebuilt and checked against dips
4. Ammonia Unit on a verified DCS (BP-03). The Port Plant Manager approves restart after a pre-startup safety review (68.77) that confirms setpoints, alarm limits, and interlocks match the process safety information, credentials are rotated, vendor access is restricted, and an MOC records the restoration
5. Clean DCS configuration and recipes (BP-16), then Blend Hall 1 (BP-05)
6. Loading bays (BP-08) in local mode with two-person verification until bay controllers are verified
7. Peroxide Unit (BP-04), dock transfer PLC (BP-01), packaging (BP-07)
8. **Historian, AI-001, and AI-003 last,** from clean media, with one-way replication only. AI-001 recommendations stay off until the Director of Data and Analytics confirms the data platform was not altered (P10)

**Realistic timing today:** with no tested full restore, the Port plant could be down about 7 days (P05 scenario; P01 R-002). After POAM-005 closes, the target is the 12-hour RTO for BP-03 and BP-05.

## 8. Post-incident (ID.IM)
- Lessons-learned review within 14 days of restart, documented within 30 days; corrective actions tracked "as soon as possible" for USCG exercises and incidents (101.635(c)(6)).
- RMP and PSM incident investigation reports with cyber contributing factors; PHA updates if needed (68.67; 1910.119(e)).
- Cybersecurity Plan amendments to the Coast Guard if measures changed (101.630(e)).
- Update the risk register (P01: R-001, R-002, R-006, R-008, R-013, R-014), the POA&M (P07), the SSP (P02), and this runbook.
- Keep incident records for at least 5 years (68.200), and at least as long as the FSP record rules (101.640; 105.225).

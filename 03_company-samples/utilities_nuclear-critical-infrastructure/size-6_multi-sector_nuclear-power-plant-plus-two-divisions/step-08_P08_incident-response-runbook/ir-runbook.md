# Incident Response Runbook: Cyber Attack on a Station Business Network with an Attempted Pivot to Digital Assets

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Nuclear Reactors, Materials, and Waste |
| Incident type | Cyber attack on the Station A plant business network (part of the PBN-WMS, P02) with an attempted pivot toward CDAs through the PMMD kiosk update path. Entry through a phished Engineering and Radiation Services engineer; effects in all three divisions |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06); each station CSP's incident response measures (10 CFR 73.54(e)(2)) for anything inside the CSP boundary |
| Runbook owner | Group CISO; NRC notifications owned by the fleet security director; all other notices owned by the Group General Counsel |
| Approved | 2026-09-17 by the Group CISO, the Chief Nuclear Officer, and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-regulator matrix and the SOC-to-CST handoff have never been exercised together** (scenario gap 8); the first joint tabletop is due 2026-12-15 (POAM-011) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Times and counts are illustrative. Day 0 is the day the SOC first sees activity on a CSP-adjacent asset.
- **Entry (Day -6):** an Engineering and Radiation Services outage engineer assigned to Station A's coming refueling outage is phished with an adversary-in-the-middle page. The attacker replays the engineer's session token. The engineer holds a standing cross-division account (P01 GR-01, NG-001; scenario gap 1).
- **Reconnaissance (Day -6 to Day -1):** using the token, the attacker reads Station A file shares and downloads about 1,100 CDA work packages from the WMS (CDA identifiers, firmware versions, network details). No alert fires (POAM-007). The attacker also reads the engineering collaboration platform (SYS-E1), including client engineering projects for 2 external utilities and the contractor/vendor access authorization files for about 2,900 outage workers (scenario gap 5).
- **Lateral movement (Day -1):** the attacker reaches a station server through the flat Station A server subnet and then the **kiosk update server** (POAM-010). From a compromised group jump host, the attacker also scans the Radioactive Waste Management Florida facility subnets, including the vault PACS server, and tries to sign in to the fleet operations center's intermediate system (EACMS).
- **Attempted pivot (Day 0, 01:50):** the attacker stages a modified malware-signature package containing a dropper on the kiosk update server. The packages are not signature-checked (POAM-004).
- **Detection (Day 0, 02:10):** EDR on the kiosk update server alerts on a new scheduled task. **Day 0, 04:00:** one Station A kiosk pulls the modified package before the server is isolated. **Day 0, 04:40:** the SOC calls the Station A CST (later than the 30 minutes in POL-03 4.3, because the SOC playbook does not yet list CSP-adjacent assets).
- **Outcome found by Day 2:** the CST confirms that the 2 PMMD devices scanned on the affected kiosk after 04:00 were held and never connected to a CDA, and that no data crossed the one-way devices upward. No CDA, safety, security, or emergency preparedness function was affected. The Florida vault never lost monitoring, but the facility isolated its business network for 3 hours and guards were posted. The EACMS sign-in attempts failed.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander (business systems) | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Incident commander (inside the CSP boundary) | Station A CST lead | Fleet cyber security program manager | Station CST bridge; control room phone |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| NRC notifications (73.77, 50.72) | Fleet security director | Station A site vice president | ENS from the station; commercial backup numbers in the offline binder |
| Plant operations | Station A shift manager | Plant manager | Control room |
| NERC CIP determination | CIP Senior Manager | Fleet operations center manager | CIP bridge |
| Part 37 determination (Florida vault) | Florida facility Radiation Safety Officer | Part 37 reviewing official | Facility security office |
| Engineering and Radiation Services data (SGI, access authorization files, clients) | Engineering and Radiation Services security and compliance lead | SGI program manager; contractor/vendor access authorization program manager | Division bridge |
| Notifications and legal | Group General Counsel with outside counsel | Division general counsels | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Station communications managers | Out-of-band bridge |
| Law enforcement | FBI field office (**only through the fleet security director** for anything about station systems, POL-03 4.4) | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat. Use the crisis line and managed mobile devices. The printed binder in each station's work control center and at the Florida facility holds contacts, this runbook, the 73.77 decision aid, and the notification matrix.

## 2. Preparation checks (Identify / Protect)
- [x] One-way devices between Level 3 and the business network at each station; no remote access to Level 4 (CSP)
- [x] 24x7 SOC with EDR on all business servers, including the kiosk update server (SI-4; P07 satisfied except bulk-read detection)
- [x] Immutable backups of the WMS and station file servers in provider B (CP-9; P07 satisfied)
- [ ] SOC escalation rules that call the CST within 30 minutes for CSP-adjacent assets (**gap until POAM-011 closes**)
- [ ] Kiosk update packages signature-checked; update server on a restricted segment (**gap until POAM-004 and POAM-010 close**)
- [ ] Cross-division accounts bound to assignments; division laptops behind a device check (**gap until POAM-001 and POAM-005 close**)
- [ ] Bulk-read detection for CDA work packages (**gap until POAM-007 closes**)
- [ ] Notification matrix complete and exercised across divisions (**gap until POAM-011 closes**; `notification-matrix.csv` is the 2026 version)
- [x] Forensic retainer (business systems only) and cyber insurer panel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Any alert on a CSP-adjacent asset (kiosk update server, plant data replica servers, receive side of a one-way device) | EDR, SIEM | **Call the station CST within 30 minutes** (POL-03 4.3); declare Severity 1 |
| Bulk reads or exports of CDA work packages; phishing asking for CDA or security details | SIEM, email security, user reports | Call the fleet security director: possible 73.77(a)(3) intelligence gathering (8-hour clock) |
| Session token used from a new device or location by a cross-division account | SYS-G1 risk signals | Revoke sessions; check station and division access |
| Scans or sign-in attempts against the fleet operations center EACMS | SIEM, CIP monitoring | Call the CIP Senior Manager: possible CIP-008 attempt to compromise |
| Scans of the Florida facility security subnets or any loss of vault monitoring | SIEM, facility security office | Call the Florida Radiation Safety Officer: possible Part 37 suspicious activity |
| Access to SGI-adjacent shares or access authorization files by an unexpected account | Collaboration audit logs | Call the Engineering and Radiation Services security and compliance lead |

**Severity 1** (group scale, POL-03 4.2): any incident touching a CSP-adjacent asset, SGI, access authorization information, the fleet operations center, or the Florida vault security systems.

**Record discovery times conservatively.** The NRC clocks in 73.77(a) run from discovery. The group SOC is corporate, not part of the licensee, but **this runbook treats the time the SOC first recognized activity on a CSP-adjacent asset as discovery** (Day 0, 02:10 in the scenario). Counsel and the fleet security director may refine this later, but no clock is planned from a later time. The same rule applies to CIP-008 (from the CIP Senior Manager's determination, which must be made promptly) and Part 37 (from discovery or the LLEA notice).

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Call the Station A CST and the fleet security director; start the 73.77 decision log | SOC director | CST lead on the bridge |
| 2. CST disables all 9 kiosks' update pull and quarantines the Station A kiosk that pulled the package; holds every PMMD scanned since the last good update | Station A CST lead | Kiosks in hold; PMMD list captured |
| 3. Isolate the kiosk update server and the compromised station server at the station firewall (keep the one-way devices and the WMS running) | Fleet IT director | Firewall change logged |
| 4. Disable the engineer's account, revoke all tokens, and revoke every cross-division session at Station A pending review | Group identity director | Sessions revoked |
| 5. Block the compromised jump host; confirm no group identity reaches the CIP Electronic Security Perimeter or the Florida vault systems | Group SOC director; CIP Senior Manager; Florida RSO | Confirmations on the bridge |
| 6. Florida facility: post guards at the vault as a compensatory measure; isolate the facility business network if scanning continues | Florida facility Radiation Safety Officer | Guards posted; monitoring confirmed |
| 7. Snapshot the kiosk update server and the station server for forensics; legal hold on logs. Nothing is copied out of the CSP boundary except under the CSP procedure | SOC; CST | Evidence list signed |
| 8. Brief the Station A shift manager: no plant impact known; site work continues; WMS stays up | Station A CST lead | Shift manager acknowledges |
| 9. Call the cyber insurer and outside counsel; brief the Group CISO; convene the disclosure committee within 24 hours (POL-03 4.6) | Group Chief Risk Officer; Group General Counsel | Committee convened |

**Do not report to the FBI or CISA from the SOC.** The fleet security director makes or approves every external report about station systems, because a report to another agency about an event related to the cyber security program starts its own 4-hour NRC clock when no other 73.77 notice covers the event (73.77(a)(2)(iii)).

## 5. Analysis (RS.AN)
1. **Could the attack have reached a CDA?** The CST answers this for the 73.77 decision: what the modified package contained, which kiosks pulled it, every PMMD scanned since, and whether any of those PMMD reached a CDA. In the scenario, the answer is that it **could have** compromised a CSP security control (the kiosks), which protects CDAs. That supports a 4-hour notice under 73.77(a)(2)(i), not a 1-hour notice, because no function was adversely impacted.
2. **Reconnaissance.** List every CDA work package the attacker read. Give the list to the CST and the fleet security director for the 73.77(a)(3) decision and include it in the NRC notice. Identify packages that relate to the 2 external clients (they may need to make their own decisions).
3. **Identity path.** Trace the engineer's token across SYS-G1 applications: station shares, WMS, SYS-E1, and any division system. Confirm no SGI was reached (SGI is only on stand-alone systems).
4. **Personal information.** Confirm whether the access authorization files were opened or downloaded. If yes, list affected individuals by state of residence. These drive state notices.
5. **Other divisions.** Confirm the Florida vault never lost monitoring and the EACMS attempts failed. Record the determinations by the Radiation Safety Officer and the CIP Senior Manager with times.
6. **Root cause:** cross-division standing access (GR-01), the unverified kiosk update path on a flat subnet (GR-02), and no bulk-read detection (GR-04). Feed these to P01 and the POA&M.

## 6. Containment and eradication (RS.MI)
1. Rebuild the kiosk update server on the restricted segment; restore only vendor-signed packages verified by the CST (accelerates POAM-004 and POAM-010).
2. CST re-images the affected kiosk and verifies all 9 kiosks from known-good media under the CSP procedure. Enter the event and every weakness found in the station CAP within 24 hours (73.77(b)).
3. Remove standing cross-division accounts at Station A; re-grant only for current outage assignments (accelerates POAM-001).
4. Move the access authorization files to the restricted repository now (accelerates POAM-012).
5. Confirm with forensics that no persistence remains in SYS-G1, the jump host, or station servers before reconnecting the server subnet.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (37 rows).** Counsel approves every notice except the NRC, CIP, and Part 37 telephone notices, which the licensee programs make within hours and counsel reviews afterward. The matrix has three layers:
1. **Regulator clocks measured in hours,** owned by the program that holds the license or registration: NRC (73.77, 50.72) by the fleet security director; E-ISAC and CISA (CIP-008-6 R4) by the CIP Senior Manager; the Florida Bureau of Radiation Control (Part 37 by license condition) by the Radiation Safety Officer.
2. **Contract and intercompany notices:** utility clients whose engineering data or access authorization reliance is affected; dosimetry customers (not affected in this scenario); Nuclear Generation by the other divisions immediately.
3. **Group-level duties:** state breach notices, SEC materiality, DOE contracting officers if FCI was involved, and the insurer.

| When (scenario times; discovery Day 0, 02:10) | Action | Owner |
|---|---|---|
| Day 0 by 02:40 (target) | CST on the bridge (actual 04:40 in the scenario, which is the gap to fix) | SOC director |
| **Day 0 by 06:10** | **NRC notice under 73.77(a)(2)(i):** cyber attack that could have compromised a support system protecting CDAs (4 hours from discovery). Include the reconnaissance information | Fleet security director |
| Day 0 by 15:30 | Decide whether the work package reconnaissance needs its own 73.77(a)(3) notice: 8 hours from when the SOC identified the bulk reads (Day 0, about 07:30 in the scenario). If the 06:10 notice already covered it, record why | Fleet security director with counsel |
| Day 0 | Voluntary report to the FBI and CISA, **made by the fleet security director after the NRC notice**, so 73.77(a)(2)(iii) is not a separate trigger (the event already required a 73.77(a) notice) | Fleet security director with the Group CISO |
| Day 0 (as soon as the scans are seen) | Florida: LLEA notified of suspicious activity at the vault; **Bureau of Radiation Control within 4 hours after the LLEA notice** (37.57(b)) | Florida facility Radiation Safety Officer |
| Within 24 hours of discovery | CAP entries for the event and each weakness (73.77(b)); disclosure committee convened | Station A CST; Group General Counsel |
| **By the end of the next calendar day** after the CIP Senior Manager determines the EACMS sign-ins were an attempt to compromise | E-ISAC and CISA notice (CIP-008-6 R4); updates within 7 calendar days of new information | CIP Senior Manager |
| Without delay after confirming client data was read | The 2 affected utility clients (they may have their own 73.77(a)(3) decisions about reconnaissance of their CDAs) | Engineering and Radiation Services security and compliance lead |
| Within 4 business days of a materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 30 days of determining the breach | Florida notice to affected outage workers; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 notified at once. Apply each other state's law the same way | Engineering and Radiation Services (owner of the access authorization files) with counsel |
| **Within 60 days of the 06:10 telephone notice** | Written security follow-up report on NRC Form 366 (73.77(d)) | Fleet security director (licensing) |
| Confirm before use | DOE contract incident terms if FCI was involved (**unverified** in this sample) | Contracting division |

**Plan to the shortest clock.** In this scenario the order is: NRC 4-hour, Part 37 4-hour after the LLEA notice, NRC 8-hour decision on the reconnaissance, CAP 24-hour, CIP-008 next calendar day, client notices, SEC (if material), state 30-day notices, NRC 60-day written report.

**Clocks that do not apply here (and why):**
- 73.77(a)(1) and 50.72: no function was adversely impacted and no emergency class was declared. Re-decide at once if the CST finds any CDA effect.
- 37.57(a): no actual or attempted theft, sabotage, or diversion of vault material was found; the facility handled it as suspicious activity under 37.57(b).
- CIP-008 Reportable Cyber Security Incident (1 hour): the EACMS attempts failed; this was an attempt to compromise, not a compromise.
- DOE-417 and CIRCIA: not applicable (see the matrix).

**Materiality factors for the disclosure committee:** any effect on plant operation or outage schedule; NRC, NERC, and Agreement State regulatory exposure; the number of workers whose access authorization information was exposed and the effect on licensees that rely on the contractor/vendor program; client contract exposure in Engineering and Radiation Services; costs; and reputational effects for a nuclear operator. Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom:** not part of this scenario. If extortion follows, POL-03 4.7 applies: board risk committee decision, counsel, insurer, and an OFAC sanctions check.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA order (P05 `bia.csv`, `recovery_priority`), confirming each step is clean before the next:
1. Identity (BP-G01, RTO 1 hour): revoke and re-issue tokens; confirm conditional access rules
2. Network and remote access (BP-G03, RTO 2 hours) and SOC visibility (BP-G02, RTO 4 hours)
3. NRC and offsite notifications capability (BP-NG02, RTO 1 hour) was never affected; confirm
4. Clearance and tagging (BP-NG03, RTO 4 hours) and outage work (BP-NG04, RTO 8 hours): the WMS stayed up; verify integrity of work packages changed during the dwell period
5. Site access processing (BP-NG05) and contractor/vendor access authorization processing (BP-ER05, RTO 8 hours): re-grant outage access from the schedule only
6. PMMD kiosk operations (BP-NG10, RTO 24 hours): return kiosks to service only after CST verification. Until then, PMMD for urgent work use Station B or C kiosks under the CSP procedure

Tell station staff, outage contractors, and the affected clients when services are restored (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10). Include the CST and the SOC in one session.
- Update P01 (GR-01, GR-02, GR-04, GR-05, NG-003, NG-005, ER-004), the POA&M (POAM-001, -004, -007, -010, -011, -012), the notification matrix, this runbook, and the SOC escalation rules.
- Nuclear Oversight reviews the event as part of the next 73.55(m) review.
- Consider the Regulation S-K Item 106 description for the next annual report.
- Retain records for at least 6 years, and CSP-related records as 73.54(h) requires.

**Pending change.** The NRC's proposed "Modernizing Security Requirements" rule (91 FR 38928) would replace the 73.77 categories with notification under 50.72 or 73.1200 based on the function affected. It is **not final**. This runbook uses the current 73.77 text until a final rule and CSP change take effect.

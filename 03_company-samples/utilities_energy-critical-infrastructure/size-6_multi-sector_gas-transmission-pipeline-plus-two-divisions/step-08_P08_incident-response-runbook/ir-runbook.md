# Incident Response Runbook: Ransomware on Business IT Forcing a Precautionary Pipeline Shutdown (Cross-Division)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Energy (focus division: Gas Transmission) |
| Incident type | Ransomware that starts in corporate shared services, encrypts the corporate directory, file shares, and the gas measurement servers, reaches a Transmission regional OT DMZ through the shared OT remote access gateway, steals royalty owner and Integrity Services client files, and leads to a precautionary controlled shutdown of the transmission Eastern segment |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT response guidance from NIST SP 800-82 Rev. 3 (sections 3.3.8, 3.3.9, 6.4, 6.5) |
| Policy basis | POL-03 Incident Response Policy; division supplements (P06); Gas Transmission Cybersecurity Incident Response Plan (SD 02G III.F, SSI); emergency plans (49 CFR 192.615) |
| Runbook owner | Group CISO; operations decisions owned by the Vice President of Gas Control and division presidents; notifications owned by the Group General Counsel |
| Approved | 2026-09-22 by the Group CISO, the Group General Counsel, and the Gas Transmission president |
| Last tested | The TSA plan exercise on 2026-04-22 tested containment and IT/OT isolation. **No exercise has combined the shutdown decision with the cross-division notification matrix** (scenario gap 8); the first cross-division tabletop, using this scenario, is due 2026-12-15 (POAM-004) |

**The lesson this runbook is built on.** Ransomware on business IT does not by itself make the pipeline unsafe: gas control, station shutdowns, and controller sign-in do not depend on corporate systems (P05). A precautionary shutdown is justified only when the group **cannot trust or cannot see its OT**, or cannot keep custody measurement and scheduling going long enough to operate commercially and safely. This runbook makes that decision explicit, owned, and limited to the segment that needs it, because shutting down a 7,400-mile interstate system would cut firm supply to local distribution companies and power plants, which is a public safety risk of its own.

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (Day -9):** an attacker phishes a corporate finance analyst with an adversary-in-the-middle page, steals a session, and finds credentials for a directory service account in a script on a file share.
- **Dwell (Day -9 to Day 0):** the attacker gains directory administrator rights, copies the monthly royalty owner payment files from the finance share (about 140,000 owners with Social Security or taxpayer numbers and bank accounts; P01 GP-005), and copies Integrity Services engineering shares holding SSI (Transmission plan excerpts and assessment results of 4 TSA-designated clients; scenario gap 2).
- **OT DMZ (Day -2):** using an Integrity Services engineer's gateway account, which the shared OT remote access gateway allows toward Transmission landing servers (scenario gap 3), the attacker reaches a PAM landing server in the Eastern regional OT DMZ and stages tools. No evidence yet of access beyond the DMZ, but 2 of the 6 Eastern segment compressor stations are among the 5 stations without OT sensors.
- **Impact (Day 0, 02:10):** encryption of corporate directory servers, file shares, ERP application servers, and the gas measurement servers (SYS-T4, which are directory members; scenario gap 1). The nominations platform (SYS-T5) runs but has no measured volumes. Extortion email names all three divisions.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| OT lead | Group OT Security Director | SOC OT desk manager | OT bridge |
| Operate-or-shut-down recommendation | Vice President of Gas Control | Director of Gas Control | Gas Control Center direct line; radio |
| Shutdown decision (Gas Transmission) | Gas Transmission president | Group CISO with the Group Chief Risk Officer (only if the president cannot be reached) | Out-of-band bridge |
| Controller on duty | Shift lead controller (primary or backup center) | Director of Gas Control | Console phone; radio |
| Field operations (Gathering and Production) | Vice President of Field Operations Technology | Haynesville Operations Center shift lead | Field radio; satellite phones |
| TSA Cybersecurity Coordinator (CISA report) | Director of Pipeline Cybersecurity | Group OT Security Director; SOC OT desk manager | Coordinator phone list |
| PHMSA notices | Pipeline Safety Compliance Director (Transmission); Gathering Compliance Manager (gathering) | Vice President of Gas Control | Cell |
| FERC, shipper, and posting notices | Vice President of Commercial Operations | Director of Gas Control | Cell |
| SSI and client notices | Integrity Services Client Security Officer | Group General Counsel | Division bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Law enforcement | FBI field office or IC3; CISA Central (844-729-2472) | n/a | Numbers in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat and controls the directory. Use the crisis line, managed mobile devices, radio, and the printed binder kept at both gas control centers, the Haynesville Operations Center, and the corporate command center (contacts, this runbook, the notification matrix, the manual operation plan).

## 2. Preparation checks (Identify / Protect)
- [x] Gas control does not depend on the corporate directory (named local SCADA accounts) (P02 section 11)
- [x] Offline SCADA backups at both gas control centers; immutable cloud backups in the provider B vault (CP-9; P07 satisfied)
- [x] IT/OT isolation authority written into POL-03 4.4 and the TSA plan (SD 02G III.F.1.d)
- [x] Hardwired station emergency shutdown independent of SCADA
- [ ] Measurement servers out of the corporate directory (**gap until POAM-007 closes**; interim block on directory administrator logons by 2026-10-31)
- [ ] 72-hour manual scheduling and measurement procedure, exercised (**gap until POAM-006 closes**; today only 8 hours tested)
- [ ] OT remote access gateway split by division (**gap until POAM-001 closes**)
- [ ] OT sensors at all 41 stations and deviation alerts on all external connections (**gap until POAM-003 closes**)
- [ ] One reporting procedure with FERC, SSI, client, and Part 191 steps and night owners (**gap until POAM-005 closes**)
- [ ] Integrity Services SSI program, so stolen SSI can be scoped by register (**gap until POAM-019 closes**)
- [x] Forensic retainer with OT experience and the insurer panel confirmed

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Encryption, mass file renames, or ransom notes on servers | EDR; file integrity alerts | Declare Severity 1; open the bridge |
| Directory administrator activity at unusual times or from new hosts | SIEM; identity analytics | Disable the account; start triage |
| Gateway session from an engineer account to a division it does not normally serve | Gateway logs; SOC rule | Terminate session; disable account; check the landing server |
| New tools or accounts on an OT DMZ server | EDR on DMZ servers; OT sensors | Severity 1; Gas Control told at once |
| Anything abnormal on SCADA (values that disagree with field readings, commands the controller did not issue) | Controller | **Controller follows control room and emergency procedures first**, then calls the Director of Gas Control and the SOC OT desk |
| Measured volumes stop flowing to nominations | Commercial Operations | Treat as part of the incident until ruled out |
| Extortion email or leak-site post naming any division | Email; threat intelligence; law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): encryption in shared services, or any incident in which OT is affected or cannot be shown to be unaffected.
**Record the time of identification** of the cybersecurity incident for the SD 01G 72-hour clock, and record each other clock's start in the incident log as it occurs (see `notification-matrix.csv`, column `clock_starts`).

## 4. First hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| T+0 to 15 min | 1. Tell controllers at both gas control centers and the Haynesville shift lead. **Close all IT/OT DMZ connections** for Transmission and Gathering and **shut the OT remote access gateway** for all divisions. Do not wait for proof that OT is affected | Director of Gas Control; Vice President of Field Operations Technology (authority, POL-03 4.4); Group OT Security Director | Firewalls show no IT-to-DMZ sessions; gateway down |
| T+0 to 30 min | 2. Controllers confirm SCADA is responsive and consistent (line pack, key pressures, compressor status). Controllers keep operating | Controllers on duty | Status to the Vice President of Gas Control |
| T+0 to 30 min | 3. Isolate encrypted servers with EDR; keep them powered on for memory capture (SD 02G III.F.1.b) | SOC; forensic retainer | Isolation confirmed |
| T+0 to 45 min | 4. Disable compromised directory accounts; take the directory offline for authentication to systems that touch OT; keep SCADA consoles on local accounts | Group identity director | Accounts disabled |
| T+30 to 60 min | 5. Call the insurer hotline; engage breach counsel and the forensic retainer | Group Chief Risk Officer | Claim number issued |
| T+30 to 60 min | 6. Put field crews on standby at the Eastern segment compressor stations, the 4 largest delivery points, and interconnects for manual operation; alert Gathering field crews at the 6 Transmission receipt points | Vice President of Gas Control; Vice President of Field Operations Technology | Crews dispatched or on standby |
| T+60 min | 7. **Decision point 1** (section 5) | Vice President of Gas Control recommends; Gas Transmission president decides | Decision and reasons in the incident log |
| T+0 to 24 h | 8. Coordinator prepares the CISA report (target 24 hours; limit 72 hours); counsel opens the notification tracker | Director of Pipeline Cybersecurity; Group General Counsel | Report drafted |
| Within 24 h of declaration | 9. Disclosure committee convened (POL-03 4.7) | Group General Counsel | Committee meets |

## 5. The operate-or-shut-down decision (RS.AN, RS.MI)
The Vice President of Gas Control recommends and the Gas Transmission president decides, except where 192.615(a)(6) requires a controller or field supervisor to act at once for safety (POL-03 4.3 and 4.5). Gathering and Production makes its own shut-in decisions for its fields under the same questions.

**Decision point 1 (T+60 min), asked segment by segment: is OT trustworthy and visible right now?**

| Question | How to check | If yes | If no or unknown |
|---|---|---|---|
| Are the DMZ and gateway closed and holding? | Firewall session tables; gateway status | Continue | Close again; escalate |
| Can the SOC show OT traffic is normal? | OT sensor console at both centers and the stations that have sensors; deviation from baseline | Continue | Treat the segment as **not visible** |
| Do SCADA values agree with the field? | Field crews read local gauges at 3 or more sites per segment and compare by radio | Continue | Manual operation of that segment (outcome B) |
| Was any server in that segment's DMZ touched by the attacker? | EDR and PAM logs on the regional DMZ landing servers | Continue | Treat the segment as **not trustworthy** until the DMZ is rebuilt |
| Can custody measurement and scheduling continue? | Commercial Operations: flow computers buffer about 35 days; manual scheduling tested for 8 hours | Continue on manual fallback; recheck every 4 hours | Plan a curtailment before the 24-hour nominations MTD (P05 BP-T05) |

**Outcomes:**
- **A. Isolate and operate (default).** All answers yes. Keep the DMZ and gateway closed, run scheduling on the manual fallback, recheck every 4 hours.
- **B. Manual operation of a segment.** SCADA values cannot be trusted but field crews can run the segment safely. Consider reducing pressure to widen margins. The 4-hour MTD for gas control (P05 BP-T01) sets the next decision point.
- **C. Controlled precautionary shutdown of a segment.** Choose this when the segment is not trustworthy or not visible and manual operation cannot be staffed safely beyond the MTD, or when there is evidence that someone other than a controller is sending commands. Follow the O&M manual shutdown procedures and the emergency plan. **Before closing any delivery,** coordinate with each affected LDC and power plant and with Gathering and Production, because a supply loss to homes creates its own safety risk.

**In this scenario:** the Western and Central segments meet outcome A. The Eastern segment does not: the attacker staged tools on the Eastern regional DMZ landing server, and 2 of its 6 compressor stations have no OT sensors, so the SOC cannot show OT is clean there. Manual operation of all 6 stations and their deliveries for more than a few hours is not staffable. At T+5 h, after supply is rerouted where interconnects allow, the Gas Transmission president orders a **controlled precautionary shutdown of the Eastern segment** (6 compressor stations). Gathering and Production shuts in the Haynesville volumes that flow into the Eastern segment.

**What does not justify a shutdown on its own:** loss of email, ERP, billing, or file shares. These have MTDs of 72 to 120 hours (P05).

**Decision point 2 (T+4 h, then every 4 h):** reassess with forensic findings. A shutdown is lifted only under section 9.

## 6. Analysis, containment, and eradication (RS.AN, RS.MI)
1. **Scope:** forensic retainer and SOC use EDR, directory and gateway logs, cloud audit logs, and firewall archives. Regional DMZ firewall logs older than 90 days are not available (POAM-013).
2. **OT paths (Group OT Security Director with the retainer):** image the Eastern DMZ landing server before cleanup; review PAM recordings for every gateway session in 30 days; check historian brokers, patch relays, and the leak-detection scoring server; inspect the 2 unsensored stations by portable passive capture.
3. **Data stolen:** confirm which royalty owner files and which Integrity Services project folders were copied. Without an SSI register (POAM-019), Integrity Services must review folders by hand to find SSI and CEII; plan for days, not hours.
4. **Preserve evidence:** memory images, labeled equipment, chain of custody, legal hold on logs (SD 02G III.F.1.b; POL-03 4.10).
5. **Contain and eradicate:**
   - rebuild the directory from a known-good backup in an isolated environment; reset all privileged and service credentials, including krbtgt twice;
   - disable the Integrity engineer's gateway account and every account with standing cross-division access;
   - rebuild the Eastern DMZ landing server and any server the attacker touched; do not decrypt and reuse encrypted servers;
   - block attacker infrastructure at the perimeter and in cloud network rules.
6. **Confirm** with the retainer that persistence is removed before anything reconnects to a DMZ.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (32 rows).** Counsel approves every notice. The matrix has three layers:
1. **Inside the group:** corporate shared services notifies Gathering and Production about the royalty owner files on the bridge on Day 0 (treated as a third-party agent notice under Fla. Stat. 501.171(6)(a) as the worked example); Integrity Services tells Gas Transmission which Transmission SSI was taken.
2. **Each division's own regulators:** Gas Transmission reports to CISA under SD 01G, to PHMSA (191.5), and to FERC (260.9); Gathering and Production decides its own Part 191 duties and owns the royalty owner notices; Integrity Services and Gas Transmission each report the SSI release to TSA (1520.9(c)); Integrity Services notifies clients under contract.
3. **Group:** SEC materiality and Form 8-K; OFAC if a payment is discussed; FBI.

| When (Day 0 = encryption, 02:10) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, forensics engaged; internal notices on the bridge (royalty files; Transmission SSI) | Group Chief Risk Officer; incident commander |
| Within 1 hour of the shutdown decision | **NRC telephonic notice** (191.5): the cyber-caused Eastern segment shutdown is reported as significant in the operator's judgment (191.3 paragraph (3)) | Pipeline Safety Compliance Director |
| Before closing deliveries, then every 4 hours | LDCs, power plants, and other shippers; interconnecting pipelines; capacity postings updated (284.13(d)(1)) | Vice President of Commercial Operations |
| At the earliest feasible time after the interruption | **FERC service interruption report** (260.9(a)(1)(ii)) by email, with a copy to each affected state commission (260.9(e)) | Vice President of Commercial Operations |
| If an emergency exists | 9-1-1 centers and county emergency managers along the segment (192.615(a)(8)) | Vice President of Gas Control |
| Day 0 to 1 | Voluntary FBI report; voluntary CISA reports for Gathering and Production and Integrity Services | Group CISO |
| Target 24 hours; limit 72 hours after identification | **CISA report under SD 01G** stating it satisfies the directive; supplements within 24 hours of new information | Director of Pipeline Cybersecurity |
| Within 24 hours of declaration | Disclosure committee convened | Group General Counsel |
| Within 48 hours of confirmed discovery | Revise or confirm the NRC notice (191.5(c)) | Pipeline Safety Compliance Director |
| Promptly after awareness | **SSI disclosure reports to TSA** (1520.9(c)) for Transmission SSI and the 4 designated clients' SSI | Integrity Services Client Security Officer; Director of Pipeline Cybersecurity |
| Within 72 hours of confirmation (shorter where negotiated) | Client notices (31 clients, including the 4 designated clients) | Integrity Services Client Security Officer |
| Within 4 business days of a materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 30 days of determination | Florida notices: about 8,000 owners, the Department of Legal Affairs (500 or more), and consumer reporting agencies (more than 1,000). Apply each other state's law the same way, to the shortest clock | Gathering and Production with the Group General Counsel |
| Within 30 days of detection | PHMSA Form F 7100.2 (191.15); copy to FERC within 30 days (260.9(d)) | Pipeline Safety Compliance Director |

**Plan to the shortest clock.** In this scenario the order is: NRC (1 hour), shipper and FERC notices (as early as feasible), CISA (target 24 hours), client 72-hour notices, SEC (4 business days after the determination), then state breach notices (shortest state clock first; Florida 30 days).

**Materiality factors for the disclosure committee:** loss of firm deliveries on the Eastern segment and its duration; revenue at about $16.7 million per day for Gas Transmission and the shut-in Haynesville volumes; regulatory exposure (TSA, PHMSA, FERC, state attorneys general); client contract exposure in Integrity Services; costs of notification and recovery; and national attention to a pipeline shutdown. The 4-business-day clock starts at the determination, made without unreasonable delay, not at discovery. Reports to TSA and CISA contain SSI and must not be quoted in the public filing.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not restore trust in OT and does not remove any notice duty when data was taken.

**Not required, and why:** NERC CIP-008 (not registered), DOE-417 (no electric operations), CIRCIA (not in effect), FAR clauses (no federal contracts). See the matrix.

## 8. Recovery (RC.RP, RC.CO)
Restore in the P05 recovery order, adjusted for what was hit:
1. BP-G01 identity (rebuilt directory, clean credentials) and BP-G03 network
2. BP-T01, BP-T03, BP-P02: confirm gas control and safety monitoring are unaffected (they never depended on the directory)
3. BP-G02 SOC visibility, including portable sensors at the 2 unsensored Eastern stations
4. BP-T07 notices (running from the bridge since Day 0)
5. BP-T05 nominations and BP-T04 measurement: measurement servers restored **into a temporary isolated enclave with local accounts**, not back into the corporate directory (accelerates POAM-007); volumes reconciled from flow computer buffers
6. BP-G04 OT remote access gateway, reopened **division by division** with only named, approved accounts (accelerates POAM-001)
7. Integrity Services shares (BP-E04) after the SSI review; Integrity Data Platform (BP-E01) only if forensics shows it was touched (in this scenario it was not)
8. ERP, billing, royalty payments, and payroll

**Before reopening any DMZ:** the retainer confirms the directory and gateway are clean; the Eastern landing server is rebuilt; the Director of Gas Control signs off.

**If SCADA hosts or station logic must be restored:** use the offline backup after a malware scan and hash comparison (SD 02G III.F.1.c; POL-03 4.11), verify against the build sheet, perform point-to-point checks on any changed point (192.631(c)(2)), and run a failover test.

**Restarting the Eastern segment:**
1. OT sensors (fixed or portable) show normal traffic at all 6 stations for 24 hours; station logic compared with the offline baseline.
2. Field crews confirm SCADA values against local readings at every compressor station and major delivery point.
3. Start-up under the O&M manual procedures, coordinated with LDCs, power plants, interconnects, and Gathering and Production.
4. The Gas Transmission president approves on the Vice President of Gas Control's recommendation. FERC and shippers are told when service is restored.

**Leak-detection model** (BP-T06) is restored last and only after revalidation (P10 AI-001), because its inputs passed through the affected DMZs.

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.12).
- Review control room actions under 192.631(g); add lessons to controller training (POAM-011).
- File TSA plan amendment requests within 50 days for any permanent change (SD 02G VI.D), such as the measurement enclave or gateway tiers.
- Update P01 (GR-01, GR-02, GR-04, GR-05, GR-09), the POA&M, the notification matrix, this runbook, and the Reg S-K Item 106 description for the next annual report.
- Retain incident records for at least 3 years (POL-01 4.14), longer where PHMSA, FERC, or litigation holds require.

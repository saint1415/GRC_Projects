# Incident Response Runbook: Intrusion into Process Control Systems Spanning Three Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Chemical |
| Incident type | Intrusion through the group OT remote access gateway into the Plant C1 DCS (setpoint and alarm limit changes on a chlorine process), probing of Terminal T1 OT, and ransomware on ERP-connected servers that stops order release and electronic shipping papers for Distribution and Hazmat Transport, with theft of HR and driver records |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel; process decisions by the Plant C1 Plant Manager as incident commander |
| Approved | 2026-09-17 by the Group CISO, the Group General Counsel, and the Plant C1 Plant Manager |
| Last tested | Technical OT playbooks tested in 2026. **The multi-regulator notification matrix has not been exercised** (scenario gap 8). The first cross-division tabletop, combined with the Plant C1 RMP tabletop (40 CFR 68.96(b)(2), due before 2026-12-21) and the Terminal T1 annual cyber exercise, is set for 2026-12-08 (POAM-009). Owners were named for all 38 matrix rows on 2026-09-15 |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (Day 0, 02:10):** an attacker uses a credential stolen from one of the 14 integrators (a shared team account with its MFA device) to open a session on the group OT remote access gateway. No site approval is needed (P01 GR-01).
- **Plant C1 (02:40):** from the gateway jump host the attacker reaches a Plant C1 EWS, widens the high-temperature alarm limits on hypochlorite reactor train 2, and raises the chlorine feed setpoint. The SIS trips train 2 on the feed ratio at 02:51 and isolates the chlorine feed. **No release; no injuries.** The night shift superintendent sees the trip and an alarm limit that does not match the operating procedure.
- **Terminal T1 (03:05):** using the same team account, the attacker scans the terminal OT DMZ and tries logins on the tank gauging interface units (DS-001, DS-005).
- **ERP (05:30):** the attacker, already inside an ERP integration server from the corporate side, deploys ransomware on 37 ERP-connected servers. Order release and shipping paper printing stop for all three divisions. HR and driver qualification exports on a file server were copied out on Day -2.
- **Forensic estimate at Day 4:** personal information of about 7,400 current and former drivers and employees in 41 states (about 1,900 in Florida).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Process incident commander (Plant C1) | Plant C1 Plant Manager | Shift superintendent on duty until the Plant Manager arrives | Control room radio; cellular phone |
| Cyber incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| OT technical lead | Group OT Security Director | Plant C1 Controls Engineering Manager | OT desk bridge |
| Terminal T1 lead | Terminal T1 Terminal Manager with the CySO and FSO | Distribution security and compliance lead | Terminal radio; cellular phone |
| Shipping continuity | Group ERP director with the Hazmat Transport dispatch director | Distribution warehouse operations director | Out-of-band bridge |
| Release reporting and responders | Specialty Chemicals EHS director | Plant C1 shift superintendent | Printed call list; cellular and satellite phones |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement and CISA | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat. Use the crisis line, managed mobile devices, plant radios, and the printed binder in each control room, the Terminal T1 control room, every truck terminal dispatch office, and the ERC backup site.

## 2. Preparation checks (Identify / Protect)
- [x] Independent SIS on every RMP-covered process, proof-tested (P02 CP-12, SC-7(21))
- [x] Offline, verified Plant C1 configuration and recipe copies; restore tested 2026-08-12 (P07 CP-9 satisfied)
- [x] Release notification independent of the business network: cellular and satellite phones, printed call lists (P02 CP-8)
- [x] Group ERC backup site with offline SDS for the top 500 products (P05 BP-G06)
- [x] Forensic firm with OT experience and the DCS vendor response service on retainer
- [ ] Per-session site approval and named integrator accounts on the gateway (**gap until POAM-001 closes**; interim phone approval at Plant C1)
- [ ] DCS event journal forwarded to the SIEM (**gap until POAM-023 closes**)
- [ ] Pre-printed shipping papers for all bulk products, not only the top 500 (**gap**, P01 GR-03)
- [ ] Notification matrix exercised (**gap until POAM-009 closes**)
- [ ] Terminal T1 rack and gauging PLCs separated from the office segment (**gap until POAM-011 closes**)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Setpoint, alarm limit, or controller mode changed with no operator action | Operators; DCS event journal; process drifting toward limits | Shift superintendent puts the unit in a safe state, then calls the OT desk |
| SIS trip with no clear process cause | SIS panel | Follow the emergency procedures first; then report as a possible cyber cause |
| HMI values that disagree with field gauges | Operator rounds | Treat the HMI as untrusted; use field gauges and the SIS status panel |
| Gateway session outside an approved window, or from a new location | Gateway logs; OT desk | Disconnect the session; disable the account; call the site |
| Scans or failed logins on Terminal T1 OT | OT sensor at Terminal T1 | Terminal T1 CySO opens an incident; Coast Guard report (section 7) |
| Ransom note, or ERP servers encrypted | EDR; users | Declare Severity 1; isolate (section 4) |

**Declare Severity 1** (POL-03 4.2) on any confirmed unauthorized change to OT, ransomware on a system that produces shipping papers, or an incident in more than one division. In the scenario, Severity 1 is declared at 03:20 when the OT desk links the Plant C1 trip to the gateway session.

**Record the discovery times.** Release clocks run from knowledge of a release; the RMP incident investigation clock from the incident (the 02:40 setpoint change); the Coast Guard report from evidence of the Terminal T1 cyber incident; Florida breach clocks from the determination of a breach; and the SEC clock from the materiality determination. The incident log records each one.

## 4. First hours: safe state first (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safe state at Plant C1.** Keep train 2 shut down; stop chlorine unloading; confirm the chlorine cars are isolated; hold train 1 and the blend halls in a safe state until setpoints and alarm limits are verified against the operating procedures with field readings | Shift superintendent; Plant Manager | Process stable and verified by field instruments |
| 2. **Release check.** Gas detectors and field checks at the reactors and the unloading area. If a release at or above an RQ occurred, make the release notices now (section 7) | Shift superintendent; EHS | Release ruled out, or notices under way |
| 3. **Cut remote access group-wide.** Disable the integrator team account and every gateway session; suspend all integrator accounts; disconnect the hub's connections | Group OT Security Director | No remote path into any plant or Terminal T1 |
| 4. **Isolate OT DMZs** at Plant C1 and Terminal T1 from the business network (deny all at the OT firewalls). Plants and the terminal keep running locally | Plant C1 Controls Engineering Manager; Terminal T1 Terminal Manager | Firewalls in deny-all; local control continues |
| 5. **Do not power off** HMIs, EWS, or DCS servers unless the incident commander decides the process requires it. Pull network cables from suspect workstations only | Controls Engineering | Evidence kept in memory |
| 6. **Check the SIS** from the SIS panel, not the DCS: keyswitch in run, trips healthy, program checksum matches the approved copy | Controls Engineering; I&E technician | SIS confirmed independent and unchanged |
| 7. **Contain the ERP ransomware.** Isolate ERP integration servers; block lateral movement; protect the provider B vault | Group SOC director; Group cloud platform director | Spread stopped; vault intact |
| 8. **Keep hazmat moving safely.** ERC switches to its backup site if needed; terminals and plants use pre-printed shipping papers; dispatch holds Division 5.1 and Class 3 PG II security plan loads at terminals until dispatch integrity is confirmed; security plan elements raised and staff notified (172.802(b)(2)) | Group ERC manager; Hazmat Transport dispatch director | No load leaves without valid shipping papers and a monitored emergency number |
| 9. **Call the insurer; engage counsel and OT forensics** through the panel | Group Chief Risk Officer | Claim number issued |
| 10. **Start the RMP incident investigation** within 48 hours of the 02:40 change (68.81(b)) | Plant C1 Process Safety Manager | Team named |

## 5. Analysis (RS.AN)
1. **Cyber cause screening at Plant C1.** For every process event in the window: which station and account made the change; whether the running configuration matches the last approved offline copy; whether the SIS checksum matches. Shared integrator accounts limit attribution (POAM-001, POAM-002), so gateway recordings and integrator records are pulled.
2. **Scope across sites.** List every site the stolen team account could reach (the integrator supports 5 plants and Terminal T1). Check gateway recordings, OT sensor data, and EWS logs at each. The 7 legacy plants have no sensors; send engineers to check them on site.
3. **Evidence.** Export DCS event journals, SIS logs, gateway recordings, and firewall logs before they roll over; image the affected EWS and ERP servers; chain of custody (POL-03 4.8).
4. **Process integrity.** Controls Engineering and the Process Safety Manager compare every setpoint, alarm limit, interlock bypass, and recipe at Plant C1 with the process safety information (68.65(c)(1)(iv)) and the approved baseline. Recipes pushed from SYS-C8 in the window are compared with the library history.
5. **Data taken.** Confirm what the HR and driver qualification exports contained (names, addresses, Social Security numbers, driver's license numbers, and for drivers some drug and alcohol testing results). Count affected people by state of residence. Testing results raise the harm and the handling rules of 49 CFR 382.405.
6. **Terminal T1.** Confirm whether any gauging or rack device was changed; the 4 units whose default passwords were changed on 2026-09-10 are checked first.

## 6. Containment and eradication (RS.MI)
1. Keep OT DMZs isolated until forensics confirms no persistence on the gateway, the hub, or corporate identity.
2. Re-issue every integrator account as a named account with a new authenticator before any remote access returns. Remove the hub's standing connections permanently (accelerates POAM-001).
3. Rebuild the affected EWS and ERP servers from clean media. **Do not decrypt and reuse them.**
4. Restore DCS configuration and recipes at Plant C1 only from the verified offline copy, after Controls Engineering has reconciled every difference found in section 5 step 4.
5. Reset all OT domain and DCS passwords from a clean workstation; rotate SIS engineering credentials.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (38 rows, each with a named owner).** Release notices and Coast Guard reports are made by the facility owners immediately and confirmed to counsel afterward; other notices are approved by counsel first. The matrix has four layers:
1. **Safety and environment (never wait for the cyber investigation):** CERCLA and EPCRA release notices if any release reached an RQ (not triggered in the scenario); RMP responder and community notification; the RMP incident investigation within 48 hours (triggered); OSHA if anyone is hurt.
2. **Transportation and maritime:** the Terminal T1 Coast Guard report under 33 CFR 6.16-1 to the FBI, CISA, and the Captain of the Port, immediately (triggered); NRC reports under 101.305 if the FSO judges the probe a breach of security; DOT 171.15 reports only if an incident occurs in transportation; the ERC number kept monitored throughout.
3. **Group disclosure and privacy:** disclosure committee within 24 hours; Form 8-K Item 1.05 within 4 business days after a materiality determination; Florida and other state breach notices for the stolen HR and driver records.
4. **Customers and partners:** water utility customers told within 4 hours of switching to manual replenishment; shippers told the same day about held loads; the integrator asked for its own investigation under the security addendum.

| When (from Day 0, 02:40) | Action | Owner |
|---|---|---|
| Immediately, if a release at or above an RQ occurs (chlorine 10 lb) | National Response Center (40 CFR 302.6); LEPC and SERC (355.40 to 355.43); county responders and community notification (68.95) | Shift superintendent, then EHS |
| Day 0, 03:20 | Severity 1 declared; insurer, counsel, OT forensics engaged; board risk committee chair informed | Group CISO; Group Chief Risk Officer |
| Day 0, immediately after the Terminal T1 probe is confirmed | FBI, CISA, and the Captain of the Port (33 CFR 6.16-1) | Terminal T1 CySO |
| Day 0 | Voluntary report to the FBI and CISA for Plant C1 and the ERP ransomware (group target 24 hours) | Group CISO |
| Day 0, within 4 hours of the switch to manual replenishment | Water utility customers on the managed inventory service | Distribution managed inventory service director |
| Day 0 | Shippers told about held loads; employees told which security plan elements are raised | Hazmat Transport dispatch director; senior officials |
| Within 24 hours of declaration | Disclosure committee convened (POL-03 4.6) | Group CISO; Group General Counsel |
| Within 48 hours of the 02:40 change | RMP incident investigation started (68.81(b)) | Plant C1 Process Safety Manager |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 30 days of the breach determination | Florida notice to about 1,900 residents (501.171(4)); Department of Legal Affairs (500 or more Floridians, 501.171(3)); consumer reporting agencies without unreasonable delay (more than 1,000 notified, 501.171(5)). Apply each other state's law the same way for the other 40 states | Group General Counsel |
| Within 30 days of discovery, if a transportation incident occurred | DOT Form F 5800.1 (171.16) | Hazmat Transport Vice President of Safety and Compliance |

**Plan to the shortest clock.** In this scenario the order is: release check and Coast Guard report (immediate), utility customers (4 hours), disclosure committee (24 hours), RMP investigation (48 hours), SEC (4 business days after the determination), then the 30-day state notices.

**Materiality factors for the disclosure committee:** the chlorine process was manipulated (process safety and community exposure, even with no release); the number of plants and the terminal reachable through the gateway; days of lost shipping across three divisions (about $49 million of revenue per day across divisions at full stop); water utility supply; Coast Guard and EPA regulatory exposure; personal information of about 7,400 people; and remediation cost. Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.7). Control systems are rebuilt from verified copies, so recovery does not depend on payment. Paying would not remove any notice duty for the stolen data.

**Not required:** CIRCIA (proposed only, not in effect); CFATS reporting (authority expired 2023-07-28); FAR or DFARS reporting (no federal contracts); TSA Security Directive reporting (not a designated operator).

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7). **Safety gates come before speed.**
1. SIS and gas detection verified at Plant C1 (BP-SC02); release notification path and the ERC confirmed (BP-SC09, BP-G06). These never depended on IT.
2. Identity, cloud, WAN, and SOC visibility confirmed clean (BP-G01, BP-G04, BP-G03).
3. En route security monitoring confirmed for loads on the road (BP-HT03).
4. **Plant C1 restart (BP-SC01, BP-SC04).** The Plant Manager approves after a pre-startup safety review (68.77) confirms setpoints, alarm limits, interlocks, and recipes against the process safety information, all accounts are rotated, no remote path is open, and an MOC records the restoration.
5. Managed inventory service orders (BP-DS04) and Terminal T1 transfers and racks (BP-DS01, BP-DS02); Terminal T1 restarts only after the CySO confirms the gauging and rack devices.
6. ERP rebuilt from code and restored from the provider B vault (BP-G05); TMS shipping papers re-enabled (BP-HT01).
7. Other plants, branches, and the rest of the recovery order.
8. **The OT remote access gateway last** (BP-G02), with named accounts only.
9. **AI-001 stays off** until the historian replica is confirmed unaltered (P10).

**Realistic timing:** Plant C1 can restart within its 24-hour RTO because its offline copies are tested. The 7 legacy plants could take weeks if any were reached, because their backups are untested (P05 key finding 4). ERP order release returns within about 8 hours using the vault; shipping continues on pre-printed papers meanwhile.

**Recovery communications:** tell operators, utility customers, shippers, the Captain of the Port (Terminal T1), county responders (if notified), and the insurer when each service is restored.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; documented within 30 days (POL-03 4.11).
- Complete the RMP incident investigation report with cyber contributing factors and resolve its recommendations (68.81(d)-(e)); add the scenario to the Plant C1 PHA update (POAM-004).
- Terminal T1: record the incident (101.625(d)(10)), use it in the Cybersecurity Assessment, and amend the Plan when it exists (101.650(e)(1)(v)).
- Update P01 (GR-01, GR-02, GR-03, SC-001, DS-001, HT-004), the POA&M, the notification matrix, the three hazmat security plans, and this runbook.
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain incident records per POL-01 4.11 (at least 5 years for RMP records; 2 years for MTSA records; 6 years for group security records).

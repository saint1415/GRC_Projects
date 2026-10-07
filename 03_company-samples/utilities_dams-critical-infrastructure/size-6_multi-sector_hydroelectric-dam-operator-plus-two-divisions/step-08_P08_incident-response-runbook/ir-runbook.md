# Incident Response Runbook: Unauthorized Access to Spillway and Turbine Control Systems Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Hydro, Constructors, Engineering, and corporate shared services) |
| Tier / Vertical | Multi-Sector / Dams |
| Incident type | An unauthorized party controls spillway gates or turbine units at a Hydro plant through a path that belongs to another division: here, a Constructors commissioning kit on the DEV-05 Cutter's Bend gate control network. One incident then touches Hydro OT (FERC, NERC, DOE), Constructors data (DFARS, state breach law), the Engineering DSMS (client contracts), and the group (SEC) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | Group POL-03 Incident Response Policy and the division supplements (P06); Hydro CIP-008 and CIP-003 incident response plans; DEV-05 Emergency Action Plan (EAP); FERC Security Plan, Internal Emergency Response sub-element; FPE incident plan |
| Runbook owners | Group CISO (runbook); General Counsel (notification matrix); Senior Vice President, Hydro Operations (OT response at Hydro plants) |
| Approved | 2026-09-10 by the Group CISO, the General Counsel, and the Senior Vice President, Hydro Operations (CIP Senior Manager) |
| Last tested | Hydro OT playbooks: annual HOC failover 2026-06-13 and the CIP-008 plan test. **The cross-division path and the notification matrix have never been exercised** (gap 8). First cross-division tabletop with the disclosure committee: 2026-11-17, using this scenario (POAM-009) |
| Handling | Mark "Privileged - Security Sensitive Material" and treat as BCSI and CEII. Printed copies in the HOC-A and HOC-B incident binders, each plant control room, the Constructors and Engineering command centers, and the General Counsel's office |

**The rule that overrides everything else: keep every dam under control.** Put affected gates and units into a known safe state under local control and confirm their physical positions before anything else. Evidence can be lost; people downstream cannot be put at risk (POL-03 4.2).

## 0. Scenario used to build and test this runbook
An exercise scenario built on the real DEV-05 finding, not a real event. Forensic review of the actual DEV-05 kit found no sign of malicious use (P07). The exercise asks: what if the 41-day exposure had been used? Counts are illustrative.
- **Entry:** an attacker finds the DEV-05 commissioning kit's cellular router on the internet, logs in with its default password (POAM-003), and reaches the remote support tool on the commissioning laptop (gap 1). The laptop sits on the DEV-05 gate control network (SYS-H3) and can also reach the Unit 2 governor through the plant control network (SYS-H2).
- **Day 0, 02:10:** HOC-A sees Radial Gate 7 opening with no HOC command, then Unit 2 load dropping from 78 MW to 20 MW after a governor setpoint change. The HOC ESP firewall logs and blocks connection attempts from the DEV-05 plant network toward the HOC SCADA servers.
- **On the laptop:** USACE drawings marked CUI that synced from another Constructors project (a covered defense information exposure, gap 5), and a crew badging list of 1,180 workers with names, home addresses, and driver's license numbers (about 290 Florida residents; the rest mostly Tennessee, Georgia, and Alabama).
- **DSMS:** DEV-05 is one of the 17 plants that replicate historian data to the Engineering DSMS over a two-way connection (gap 3). Whether the attacker touched that path is unknown at declaration.
- **Downstream:** Gate 7 reached 3.4 feet before local crews stopped it. The river at the public access point 2 miles downstream rose 1.4 feet. No one was hurt; deputies cleared 6 boaters.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander, OT (first hours) | HOC shift supervisor (HOC-A) | HOC-B shift supervisor | HOC hotline; OT radio; HOC-A bridge |
| Incident commander, OT (after handover) | Senior Vice President, Hydro Operations (CIP Senior Manager) | HOC Manager (HOC-A) | Out-of-band bridge |
| Group incident commander (single commander for the cross-division incident, POL-03 4.3) | Group CISO | Group SOC director | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Dam safety, EAP, and 18 CFR 12.10 reports | Vice President, Dam Safety (Chief Dam Safety Engineer) | DEV-05 plant manager (may activate the EAP) | Cell; HOC bridge |
| FERC security contact, law enforcement, physical security | Director, Hydro Security | DEV-05 plant manager (alternate FERC security contact for the project) | Cell; security dispatch at HOC-A |
| OT technical lead | Director, OT Security | OT security engineer on call; co-sourced OT incident response firm (retainer) | OT bridge |
| IT and cloud technical lead | Group SOC director | Group cloud platform director | SOC bridge |
| NERC, DOE, and EOP-004 reports | NERC Compliance Director | Chief Compliance Officer | Cell; compliance bridge |
| DFARS and FAR reports | Federal Programs Compliance Director | Constructors security and compliance lead | Cell; DIBNet certificate holders listed in the binder |
| Constructors project response (DEV-05 site, kit, crews) | DEV-05 project manager | Constructors security and compliance lead | Cell; jobsite radio |
| DSMS client notices | DSMS General Manager | Engineering security and compliance lead | Division bridge |
| Notifications and legal | General Counsel with outside counsel | Division general counsels | Out-of-band bridge |
| SEC materiality | Disclosure committee (General Counsel chairs) | Chief Financial Officer | Committee call |
| Insurance | Chief Financial Officer | Group Chief Risk Officer | Carrier breach hotline |
| Communications | Group communications lead, coordinated with county emergency management while the EAP is active | Hydro communications lead | Out-of-band bridge |
| Outside agencies | County sheriff (911); county emergency management; FERC Regional Engineer and Regional Office; FBI field office; CISA; E-ISAC | n/a | Numbers in every binder and posted at the HOCs |

**Out-of-band first.** Assume the attacker can see corporate email, chat, and possibly HMI screens. Coordinate by OT radio, the HOC hotline, and managed mobile devices, using the printed contact lists.

**Do and check.** The Director, OT Security reports to the incident commander for OT. The NERC Compliance Director makes reporting determinations on a separate line to the Chief Compliance Officer, so reporting decisions are not made by the team that runs the response (00_company-facts.md section 2).

## 2. Preparation checks (Identify / Protect)
- [x] HOC-B can take over fleet control (failover 2026-06-13 took 2.6 hours against a 2-hour RTO; POAM-008 fixes the ICCP restart)
- [x] Local control checklists for every gate and unit at all 41 HOC-operated plants; operators drilled during annual EAP tests
- [x] Offline SCADA backups at both HOCs (CP-9)
- [x] Interim rule from 2026-07-16: commissioning kits connect to Hydro OT only in escorted, scheduled sessions approved by the HOC shift supervisor
- [ ] Commissioning standard and kit inventory with EDR (**gap until POAM-001 and POAM-002 close**, 2026-12-31 and 2026-11-30)
- [ ] Default and generic credentials removed from field devices (**gap until POAM-003 closes**, 2026-12-31)
- [ ] OT network monitoring at every HOC-operated plant (**gap until POAM-006 closes**, 2027-06-30). DEV-05 has no OT sensor today, so detection depends on HOC process alarms
- [ ] Current gate PLC and governor logic backups everywhere (**gap until POAM-010 closes**, 2027-03-31)
- [ ] One-way DSMS transfer at the 17 two-way plants (**gap until POAM-005 closes**, 2027-03-31)
- [ ] Notification matrix complete and exercised (**gap until POAM-009 closes**: matrix complete 2026-10-31, tabletop 2026-11-17)
- [x] Forensic and OT incident response retainers through the insurer panel
- [ ] Two Constructors staff with current DoD-approved medium assurance certificates for DIBNet, with renewal tracked (**gap until CN-013 treatment completes**, 2026-10-31; today there is one certificate holder)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A gate moves or a gate setpoint changes with no HOC or local operator command | HOC gate position alarms; SCADA event journal; spillway cameras | **Local control now** (section 4). Declare an OT incident |
| A unit trips, changes load, or its governor or exciter settings change unexpectedly | HOC unit alarms; Balancing Authority call | Unit to local control or a controlled shutdown; declare |
| Connection attempts from a plant network toward the HOC ESP | HOC ESP firewall and EACMS logs; group SOC | Keep the block; start the CIP-008 attempt determination |
| Reservoir falling or tailwater rising faster than the operating plan | Level alarms; river gauges (SYS-H4); DSMS alerts | Check gate positions by camera and in person; treat as a possible project emergency (EAP) |
| An unknown device, router, or remote support session on a plant network | Plant staff; OT sensors where present; Constructors staff | Disconnect it physically; call the Director, OT Security |
| A Constructors or OEM laptop behaves oddly, or its owner did not start a session | Constructors staff; EDR (where enrolled) | Isolate the laptop; open a SOC case; tell the HOC |
| Unusual traffic from a plant historian toward the DSMS, or from the DSMS toward a plant | Cloud audit logs; DSMS monitoring | Break the replication link; tell the HOC and the DSMS General Manager |
| Extortion message naming a dam or division | Email; phone; threat intelligence; law enforcement | Preserve; call the sheriff and the FBI; declare Severity 1 |

**Declare an OT incident** when any gate or unit command, setpoint change, or logic change cannot be tied to an authorized person, or an unauthorized connection to plant or gate control is found. The HOC shift supervisor declares without waiting for anyone. **The Group CISO declares Severity 1** as soon as a second division is involved (here, the Constructors kit), and names the single group incident commander (POL-03 4.3).

**Record each clock start in the incident log** (POL-03 4.4):
| Clock | Starts at | Scenario time |
|---|---|---|
| 18 CFR 12.10(a)(1); FERC Security Program report | Discovery of the condition | Day 0, 02:10 |
| CIP-003-9 Att. 1 Sec. 4.2 (DEV-05 low impact) | Determination that it is a Reportable Cyber Security Incident | Day 0, 03:40 (NERC Compliance Director) |
| CIP-008-6 R4 Part 4.2 (HOC ESP attempt) | Determination using the plan's Part 1.2.1 criteria | Day 0, 09:00 |
| EOP-004-4 | Recognition that a threshold is met | Evaluate on Day 0 |
| Form DOE-417 | The incident, or determination for an attempted cyber compromise | Day 0 (coordinate with the Balancing Authority) |
| DFARS 252.204-7012(c) | Discovery of a cyber incident affecting a covered contractor information system | **Planned from Day 0, 02:10**, although CUI on the laptop was confirmed on Day 1. Counsel may refine; no clock is planned from a later time |
| DSMS client notice (contract) | Confirmation that client data is affected | Only if confirmed |
| Florida and other state breach laws | Determination of the breach | Day 6 (counsel) |
| Form 8-K Item 1.05 | Materiality determination | Disclosure committee decision date |

## 4. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safe state.** From HOC-A, command Gate 7 to stop and Unit 2 to its scheduled load. If the plant does not obey within 2 minutes, or obeys and then reverses, stop remote control: dispatch the DEV-05 on-call operators and the roving crew to the gate house and powerhouse, switch all 10 gates and 4 units to local, and set them to the operating plan positions. Confirm positions by eye and mechanical indicators, not the HMI | HOC shift supervisor | Every DEV-05 gate and unit in local control with its position confirmed by a person on site (HY-021: crews must reach the panels inside the BIA limit of 4 hours, about 1 hour in a flood) |
| 2. **Downstream risk.** Decide whether an EAP condition exists; if a sudden release has happened or is likely, activate the EAP and sound the sirens | Chief Dam Safety Engineer (the HOC shift supervisor or plant manager may activate without waiting) | EAP level declared, or a documented decision that no EAP condition exists |
| 3. **Sheriff and county emergency management** in parallel with step 2, as the Internal Emergency Response sub-element requires; ask the sheriff to clear the river below DEV-05 | Director, Hydro Security or HOC shift supervisor | Both agencies notified; times logged |
| 4. **Cut the attacker's path physically.** At DEV-05, unplug the commissioning kit's cellular router and the laptop network cable. Do not power off the laptop (memory evidence); bag and tag it. Do not power off gate PLCs, HMIs, or governors | DEV-05 operator with the Director, OT Security on the phone | No cellular or remote support path remains; photos taken |
| 5. **Contain at the boundary.** Keep the HOC ESP block; close the DEV-05 plant gateway to all traffic except HOC SCADA; break the DEV-05 historian replication to the DSMS | Director, OT Security | Firewall changes logged under the Hydro OT emergency change procedure and reviewed afterward |
| 6. **Sister sites.** Tell every Constructors commissioning kit at the other 6 rehabilitation projects to disconnect now, whatever its session status | Constructors security and compliance lead through the project managers | All kits confirmed disconnected |
| 7. **Basin and grid partners.** Phone the operators of the 2 downstream projects and the Balancing Authority and Transmission Operator for DEV-05 | HOC shift supervisor | Calls logged |
| 8. **Escalate.** Group SOC opens the case; the Group CISO declares Severity 1 and names the group incident commander; the General Counsel opens the notification matrix; insurer hotline called | Group SOC director; Group CISO; General Counsel; Chief Financial Officer | Bridge open; claim number issued |

Keep DEV-05 in local control, staffed around the clock, until recovery step 3 in section 8 is signed off. Call in relief crews early.

## 5. Analysis (RS.AN)
1. **What moved and when.** Pull the HOC SCADA event journal, gate PLC event buffers, Unit 2 governor logs, historian trends, and spillway camera video. Build one timeline of every command and position change, from both HOC and plant records.
2. **How the attacker got in.** Router logs (from the device and the cellular carrier), remote support tool logs, laptop memory and disk images, and the Constructors project file for the kit. Confirm when the router's default password was last used.
3. **What changed.** Compare running gate PLC logic and governor settings with the last known-good copies. DEV-05 is one of the plants where logic backups must be confirmed current (POAM-010); if the reference copy is older than the Constructors gate replacement, ask Constructors for its commissioning baselines and verify them independently, because the kit itself is suspect.
4. **Where else.** Check the HOC ESP and EACMS logs for any successful connection (the CIP-008 attempt or compromise decision depends on it); the DEV-05 historian and the DSMS for any traffic other than replication (cloud audit logs on SYS-E1); the other 6 rehabilitation sites' kits; and SYS-C1 for the CUI drawings' source project.
5. **Regulated data on the laptop.** Inventory the files: CUI-marked USACE drawings (which contract, which markings), client drawings from other projects, and the crew badging list (people by state of residence). Decide with counsel whether the attacker could have accessed them; the remote support tool gave full desktop access, so the working assumption is yes.
6. **Preserve evidence.** Chain of custody for every item (who collected it, when, hash values). Keep laptop and router images and monitoring data at least 90 days from the DoD report (DFARS 252.204-7012(e)). OT evidence is BCSI and CEII: store it in the restricted library (POL-03 4.9).
7. **Scope decisions in writing:** whether water was released beyond the operating plan; whether units were damaged (inspect Unit 2 for effects of the load change); whether any HOC BES Cyber System was compromised or only attempted; whether the DSMS was reached; whether personal information and CUI were accessed.

## 6. Containment and eradication (RS.MI)
1. Keep DEV-05 in local control and the gateway restricted. No vendor, Constructors, or DSMS connection until step 5 below is done.
2. Remove the attacker's access: reset every DEV-05 OT credential (HMI, engineering, gate panels, governor interface, firewall administrator); disable the remote support tool's account with its vendor; block attacker addresses at the corporate and OT boundaries.
3. Reload gate PLC and governor logic from a verified known-good copy wherever a difference was found. The Chief Dam Safety Engineer approves any gate logic reload; gates are tested in local lockout before return to HOC control. Hydro change control applies, not Constructors' (POAM-019).
4. Rebuild any DEV-05 HMI or engineering workstation that shows unknown software. Retire the commissioning laptop and router as evidence; issue replacements only under the commissioning standard.
5. Confirm with the OT incident response firm that no persistence remains at DEV-05, in the HOC EACMS, in the DSMS, or on the other kits.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (34 rows).** The General Counsel approves every notice, **except** safety reports to the FERC Regional Engineer, EAP notifications, and law enforcement calls, which never wait for counsel (POL-03 4.5). Each division sends its own regulators' notices; the General Counsel keeps one log so the facts match across them.

| When | Action | Owner |
|---|---|---|
| Immediately (Day 0, from 02:10) | Sheriff and county emergency management; EAP notifications if a project emergency exists; downstream project operators; Balancing Authority and Transmission Operator | Director, Hydro Security; Chief Dam Safety Engineer; HOC shift supervisor |
| Within 1 hour of the CIP-003 determination (Hydro plan target) | Low impact Reportable Cyber Security Incident notice to the E-ISAC (CIP-003-9 Att. 1 Sec. 4.2; the standard sets no deadline) | NERC Compliance Director |
| Day 0 | Initial report to the FERC Regional Engineer by email or telephone (18 CFR 12.10(a)(1): as soon as practicable, preferably within 72 hours; plan to call the same morning). Same call covers the FERC Regional Office security report (Rev. 3A 3.2 and 4.2: usually within one working day) | Chief Dam Safety Engineer; Director, Hydro Security |
| Day 0 | Form DOE-417 if the form's criteria are met and the Balancing Authority is not filing: Emergency Alert criteria within 1 hour, Normal Report criteria within 6 hours of the incident; final report within 72 hours | NERC Compliance Director with the Balancing Authority |
| Day 0, voluntary | FBI field office and CISA; HSIN Dams portal suspicious activity report | Group CISO; Director, Hydro Security |
| By the end of the next calendar day after the attempt determination (Day 1) | CIP-008-6 R4 notice to the E-ISAC and CISA for the attempt to compromise the HOC ESP. If any HOC BES Cyber System or EACMS was compromised or disrupted, the clock is 1 hour after that determination | NERC Compliance Director |
| By the later of 24 hours after recognition or the end of the next business day | EOP-004-4 event report, if a threshold is met (for example, damage to Unit 2 or the hoists, or the unauthorized device treated as suspicious activity at the Facility) | NERC Compliance Director |
| Within 24 hours of the Severity 1 declaration | Disclosure committee convened; materiality assessment starts (POL-03 4.6) | General Counsel |
| Within 72 hours of discovery (by Day 3, 02:10) | DFARS 252.204-7012(c) report at dibnet.dod.mil; submit isolated malware to DC3 as instructed (paragraph (d)); start the 90-day preservation (paragraph (e)) | Federal Programs Compliance Director |
| Within 1 business day of identifying covered telecommunications equipment (if the router is a covered brand), or 3 business days for a Kaspersky or FASCSA covered article; further information within 10 business days | FAR 52.204-25(d), 52.204-23(c), or 52.204-30 reports to the contracting officer | Federal Programs Compliance Director |
| Within 48 hours of confirmation, only if DSMS client data is affected | DSMS client notices under the master agreement security schedule | DSMS General Manager |
| Within 4 business days after a materiality determination | Form 8-K Item 1.05 if the committee finds the incident material | Disclosure committee; General Counsel |
| Within 7 calendar days of determining new or changed attribute information | CIP-008-6 R4 Part 4.3 updates | NERC Compliance Director |
| As each contract requires (3 require 72 hours) | Owners of other projects whose drawings were on the laptop; client CEII owners under their NDAs | Constructors project managers and Engineering security and compliance lead, with counsel |
| No later than 30 days after the breach determination (Day 6 plus 30) | Florida notice to the about 290 Florida residents on the badging list (Fla. Stat. 501.171(4)). No Department of Legal Affairs notice (fewer than 500 Floridians) and no consumer reporting agency notice (not more than 1,000 Floridians notified). Apply each other state's law to its residents the same way | Constructors with counsel |
| When the Regional Engineer directs | Written 12.10(a)(2) report, verified under 12.13: causes, preceding events, measures taken, damage, injuries | Chief Dam Safety Engineer |
| If recreation areas below DEV-05 are closed for security | Notice to the FERC Regional Office as soon as practical (usually within one working day); closures over 30 days need prior coordination (Rev. 3A 3.3.4) | Director, Lands and Recreation |

**Not required here:** CIRCIA reporting (proposed rule only; not published as final as of 2026-09-25). Mark all security reports to FERC "Privileged - Security Sensitive Material" and keep security details to what FERC needs.

**Plan to the shortest clock.** In this scenario the order is: safety calls, the CIP-003 E-ISAC notice (Hydro's 1-hour target), DOE-417 if required, the 12.10 and FERC security reports (same morning), the CIP-008 attempt notice (Day 1), EOP-004 (if a threshold is met), DFARS (Day 3), then SEC (if material), contract notices, and state breach notices.

**Materiality factors for the disclosure committee:** public safety exposure and any EAP activation; FERC and NERC enforcement exposure (the DEV-05 path was already self-reported to SERC on 2026-09-30); effects on Hydro revenue (about $17.0 million a day) and on DEV-05 availability; DoD contract eligibility while CMMC status is open (GR-06); DSMS client confidence; cost of response and remediation; and the reputational effect of an intrusion that reached a spillway gate. Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery. Whatever the decision, record it and its date; the committee reviews it again if facts change (GR-11).

**Ransom:** if the intrusion comes with an extortion demand, payment needs board committee approval, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any reporting duty.

**Staff and public.** Brief HOC, plant, and Constructors staff that DEV-05 is under local control and safe, and not to discuss the incident outside the company. Public statements come only from the group communications lead, coordinated with county emergency management while the EAP is active.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. **Spillway gate operation and reservoir management (BP-H02):** local manual control of all DEV-05 gates, already in place from section 4
2. **Dam safety monitoring and EAP early warning (BP-H03):** confirm DEV-05 instrumentation and siren readiness against manual readings
3. **Real-time fleet operations (BP-H01):** return DEV-05 gates to HOC SCADA control, one gate at a time, from verified logic tested in local lockout; the Chief Dam Safety Engineer signs off
4. **Physical security monitoring (BP-H07):** cameras and intrusion detection at DEV-05 checked for tampering
5. **Unit control and generation (BP-H04):** Unit 2 back to HOC dispatch after governor settings are verified and the unit inspection is complete; tell the Balancing Authority
6. **Security monitoring (BP-G02):** temporary OT sensor installed at DEV-05 before remote control is fully restored (accelerates POAM-006 for Group 1 dams)
7. **DSMS data collection (BP-E01):** DEV-05 data to the DSMS **one-way only** (temporary file transfer through the OT DMZ until the diode is installed under POAM-005)
8. **Commissioning and testing at owner sites (BP-C04):** last. The DEV-05 gate project restarts only under the commissioning standard: kits enrolled in EDR, no cellular routers, sessions through the Intermediate Systems, CIP-003-9 Attachment 1 Section 5 review before every connection (POAM-001, POAM-002)

**Validate before each step:** logic matches the verified copy; credentials are new; the gateway allows only the flows that step needs. The Senior Vice President, Hydro Operations signs off each step in the incident log. Tell staff, the Balancing Authority, the downstream project operators, and (if the EAP was activated) county emergency management when normal operation resumes (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 30 days of recovery (POL-03 4.10). For a real Reportable Cyber Security Incident at the HOCs, document lessons learned, update the CIP-008 plan, and notify plan roles within 90 calendar days (CIP-008-6 R3); update the low impact plan, if needed, within 180 calendar days (CIP-003-9 Att. 1 Sec. 4.6).
- Update the risk registers (P01: GR-01, GR-03, GR-04, GR-11, HY-001, HY-009, HY-018, HY-020, HY-022, CN-003, CN-010, CN-013, EN-006), the POA&M (POAM-001, -002, -003, -005, -006, -009, -010, -019), the DEV-05 Security Plan and its Internal Emergency Response sub-element, the Section 9 determination, the notification matrix, and this runbook.
- Include the incident and the actions taken in the next Annual Security Compliance Certification Letter without security-specific details (Rev. 3A 8.0).
- Keep 12.10 reports as permanent project records (18 CFR 12.12(a)(1)(iii)(B)); keep CIP evidence for the CIP retention periods; keep DFARS images and monitoring data at least 90 days from the report; keep the rest of the incident file 6 years in the restricted library.
- Consider whether the Reg S-K Item 106 description in the next Form 10-K needs to change.
- **Tabletop success criteria for 2026-11-17:** local control confirmed inside the BIA limit; every clock start recorded with the right trigger; the CIP-003, 12.10, DFARS, and SEC owners each produce a draft notice from the same fact sheet; the disclosure committee records a materiality decision and its date.

# Incident Response Runbook: Intrusion into Process Control Systems at a Chemical Facility

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded specialty chemical formulator and packager; 14 plants in eight states) |
| Tier / Vertical | Enterprise / Chemical |
| Incident type | Intrusion into the PLT-01 process control systems through a compromised integrator account on the central remote access gateway, with unauthorized alarm limit and setpoint changes on the ammonia unit, followed by ransomware on the process historian and OT workstations. Includes the **SEC materiality assessment and Form 8-K Item 1.05** step and the MTSA, release, and process safety reporting |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.4 Release Reporting Checklist; the PLT-01 Cyber Incident Response Plan (MTSA annex, SSI) |
| Runbook owner | Director of Security Operations, with the Director of OT Security (sections 3 to 5 and 8), the PLT-01 Plant Manager (safe state and release reporting), and the General Counsel (sections 6 and 7) |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | OT ransomware tabletop 2026-03-19 and remote access compromise drill 2026-06-24 (technical and plant response; **the disclosure committee did not take part**). Next: enterprise OT tabletop with the disclosure committee on 2026-11-12, which is also the 2026 MTSA exercise (POAM-004) |
| Notification matrix | `notification-matrix.csv` (35 obligations: 6 MTSA, 10 release and process safety, 4 SEC, 2 generic state, 4 Florida worked example, and 9 others: OFAC, voluntary CISA and FBI, CFATS status, CIRCIA status, 2 FAR rows marked not applicable, insurance, and customer contracts) |

**The first rule of this runbook: make the process safe before anything else.** Forensics, recovery, and disclosure all wait for the plant manager to confirm that every affected unit is in a safe state and that the safety instrumented systems can be trusted. This order comes from the BIA (P05: BP-02 and BP-13 have the shortest recovery targets) and from POL-03 4.2.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander, process safety | PLT-01 Plant Manager | Operations superintendent on shift | Plant radio; control room hotline |
| Incident commander, cyber response | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| OT technical lead | Director of OT Security | PLT-01 Cybersecurity Officer (CySO) | Out-of-band group on company mobile phones |
| MTSA reporting and Coast Guard liaison | PLT-01 CySO (accessible 24x7) | Director of OT Security (alternate CySO); PLT-01 FSO for breach of security and TSI reports | CySO mobile; FSO mobile |
| Control system engineering | PLT-01 Controls Engineering Manager | Director of Automation Engineering | Direct mobile |
| Process safety and release reporting | Process Safety Manager, PLT-01 | Vice President, Process Safety and EHS | Direct mobile |
| Executive incident lead | CISO | CIO | Out-of-band group |
| Crisis management team chair | Chief Operating Officer | Senior Vice President, Manufacturing | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, Vice President, Investor Relations; **plus the Senior Vice President, Manufacturing and the Vice President, Process Safety and EHS once POAM-004 closes**; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Outside counsel and OT forensics | Retained firms (engaged through counsel and the insurer panel); DCS vendor emergency response service | MSSP OT practice | Retainer hotlines |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Customers | Vice President, Digital Services (SL-1); Vice President, Toll Manufacturing (SL-2); Senior Vice President, Water Treatment Business (utilities) | Account teams | Direct mobile |
| Agencies | FBI field office; CISA; Captain of the Port; National Response Center; LEPC and SERC | | Numbers in the PLT-01 emergency kit and incident binder |

**Out-of-band first.** Assume email, chat, VoIP, and the identity platform may be compromised. Use company mobile phones, plant radios, the out-of-band conferencing service, and the printed incident binder in the PLT-01 control room and at headquarters.

## 1. Preparation checks (Identify / Protect)
- [ ] Untrusted-DCS safe-state procedures for the ammonia unit, Chlor Unit, and terminal approved and trained (**gap until POAM-025 closes**)
- [ ] Approved SIS programs and DCS logic in the OT backup vault, with offline copies; SIS comparison done this month (**manual until POAM-009 closes**)
- [ ] Restore tested for each PLT-01 DCS area in the last 12 months (**1 of 3 until POAM-003 closes**)
- [ ] SIEM alerts on alarm limit changes on safety-relevant tags and SIS keyswitch position (**gap until POAM-022 closes**)
- [ ] Only named integrator accounts on the gateway (**3 shared accounts disabled 2026-09-15; named accounts due with POAM-005**)
- [ ] Emergency notification kit (cellular phones, printed call lists, radios) tested this quarter at PLT-01 (done) and at the other plants (**gap until POAM-017 closes**)
- [ ] Materiality playbook covers OT incidents and the disclosure committee roster includes operations (**gap until POAM-004 closes**)
- [ ] Outside counsel, OT forensics, DCS vendor emergency service, and insurer contacts confirmed this quarter
- [ ] OT logs retained 1 year online and 2 years in archive (AU-11)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Alarm limit, setpoint, or interlock bypass changed without a matching MOC or work order | Operator or shift supervisor; DCS audit trail; SIEM use case (POAM-022) | Shift supervisor restores the approved value only if safe, puts the unit on manual or safe hold, and calls the SOC and the CySO |
| SIS keyswitch out of run, SIS mode change, or SIS program mismatch | SIS diagnostics; monthly comparison (POAM-009) | Treat as severity 1; isolate the unit per the untrusted-DCS procedure |
| Remote session outside an approved window, from an unusual location, or with unusual targets | Gateway session logs; SOC | Terminate the session; disable the account; open a severity-1 case |
| New device, new protocol, or engineering command from an unexpected host on the control network | Passive OT monitoring | SOC OT analyst calls the controls engineer on duty; open a case |
| Ransom note, encrypted files, or mass failures on the historian, OT DMZ servers, or OT workstations | EDR on OT DMZ servers; operators; allowlisting alerts | Declare severity 1; isolate the OT DMZ from the enterprise at the IT/OT boundary |
| Integrator or vendor reports its own compromise | Vendor notice (101.650(f)(2) duty) | Disable that vendor's gateway accounts at all plants; open a case |
| Unexplained process upset with no process cause | Operators; process engineers | Treat as possible manipulation until ruled out |

**Declare a severity-1 OT incident when** any unauthorized change to control logic, alarm limits, setpoints, or safety functions is confirmed at a PSM or RMP process, any SIS integrity question cannot be resolved within 1 hour, or ransomware is confirmed on any OT host.

**Record three times, separately:**
1. **Evidence time** (MTSA 6.16-1): when evidence of an actual or threatened cyber incident at PLT-01 exists. The report to the FBI, CISA, and the Captain of the Port is due immediately.
2. **Incident time** (RMP 68.81 and PSM (m)): when the incident that could reasonably have resulted in a catastrophic release occurred. The process safety investigation must start within 48 hours.
3. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. First hour: safe state and immediate reports (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Put the affected unit in a safe state under the untrusted-DCS procedure: manual hold or isolation of the ammonia feed, verify levels and pressures with field instruments and operator rounds, stop barge transfers if the terminal is involved | Shift supervisor; PLT-01 Plant Manager | Unit in safe state; plant manager confirms |
| 2. Confirm the SIS can be trusted: keyswitch in run, no faults, program matches the approved copy (compare from the vault). If trust cannot be confirmed within 4 hours, isolate and empty the unit (P05 BP-02) | PLT-01 Controls Engineering Manager; Process Safety Manager | SIS trust confirmed or unit isolated |
| 3. Terminate the gateway session; disable the integrator account and every account of that integrator at all plants; block the source | SOC; Director of OT Security | Accounts disabled; blocks confirmed |
| 4. **If any release reached or may reach a reportable quantity:** report immediately to the National Response Center and the LEPC and SERC, and call responders; the PLT-01 hazardous materials team responds on site (40 CFR 302.6; 355.40; 68.95) | PLT-01 Plant Manager (person in charge) | Report numbers logged |
| 5. **Report immediately to the FBI, CISA, and the Captain of the Port** (33 CFR 6.16-1). If the event is also a breach of security or a TSI, the FSO reports it without delay (101.305) | PLT-01 CySO; PLT-01 FSO | Report times logged |
| 6. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains OT forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 7. COO activates the crisis management team; other plants on the same gateway check for sessions from the same integrator | COO; Director of OT Security | Crisis team running; other plants report back |
| 8. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander, cyber response | Log open |

## 4. Analysis (RS.AN)
1. **Process impact first:** which tags, alarm limits, setpoints, recipes, or interlocks were changed, when, and from which station or session. Source: DCS audit trail, historian, gateway recordings. Compare current DCS configuration with the vault baseline.
2. **Scope:** hosts, accounts, and plants touched. Use gateway logs (all plants), passive OT monitoring, EDR on OT DMZ servers, SIEM, and identity platform logs. Check every plant behind the gateway, because the gateway is a shared service (P01 R-002).
3. **Initial access:** compromised integrator credential (phishing, reuse, or the integrator's own network). Ask the integrator for its own investigation under the contract notification duty.
4. **Evidence:** OT forensics images EWS, OT DMZ servers, and historian disks, and exports DCS audit trails and gateway recordings before they roll over. Controllers and SIS logic solvers are not imaged; their programs are uploaded and hashed with the vendor present. Chain of custody is kept in the evidence register.
5. **Data:** the GC-PCBMS holds no personal information. Check whether the attacker moved into the business network (HR, payroll, SL-1 portal), which would start the state breach track in section 7.
6. **Business impact:** Finance and the BIA owners estimate daily impact using P05 values (about $2.5 million a day if PLT-01 batch production stops; about $13.15 million a day if the shared OT services take down several plants). These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. **Contain at the IT/OT boundary:** if ransomware is present, close the OT DMZ conduits to the enterprise (order relay, historian replication, gateway jump hosts). Plants run locally; production orders come by phone and paper from the ERP team.
2. Disable the compromised integrator's access at all plants; reset all gateway credentials for PLT-01 targets; rotate OT DMZ service account secrets.
3. Rebuild EWS, operator stations, OT DMZ servers, and the historian from vault images; never decrypt and reuse encrypted hosts.
4. Reload DCS control logic and SIS programs **only from the copies approved through MOC**, then verify with the vendor and the comparison tool. Every reload is a change: it goes through MOC, and the unit restarts only after a pre-startup safety review if process safety information changed (40 CFR 68.75; 68.77).
5. OT forensics and the DCS vendor confirm persistence is removed before each area is reconnected.
6. If a measure in the approved Cybersecurity Plan cannot be maintained during recovery (for example, monitoring is down), notify the Captain of the Port and request temporary permission to operate (101.665).

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration. **Any OT incident that forces a plant to a safe state is severity 1** (POL-03 4.6) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration, with the Senior Vice President, Manufacturing and the Vice President, Process Safety and EHS attending, and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 3 to 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer (for example, restart date slipping past a set number of days) | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation, and do not include SSI | General Counsel; CFO; outside securities counsel; FSO reviews for SSI | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; given the target is chemical infrastructure, counsel asks the FBI early whether a request will be made | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of customer, community, media, and investor communications with the filing; brief the audit committee and the board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost production from P05 values (PLT-01 about $2.5 million a day; enterprise about $13.15 million a day); recovery, forensic, and vendor costs; customer penalties and service credits; ransom demand; insurance coverage and retention |
| Operational | Plants and units in safe state or shut down, and for how long; restart path and pre-startup reviews needed; ability to shift volume to other plants; water utility supply |
| Safety and environment | Any release, injury, or near miss; whether safety systems were targeted; community impact |
| Legal and regulatory | Coast Guard actions at PLT-01 (operating restrictions, plan amendments); EPA or OSHA inquiries after an RMP or PSM incident; state agency interest; customer contract breaches (SL-1, SL-2, utilities) |
| Data | Whether formulations, toll customer recipes, SSI, or personal information were taken or published |
| Reputation and strategy | National media; community and investor reaction to a chemical plant incident; effect on customers and on acquisitions |

**Worked example of the clocks (fictional dates):**
- **Tuesday 2027-02-02, 03:40:** the shift supervisor sees that the anhydrous ammonia vessel high-level alarm limit was raised without MOC, and the SIEM alerts on the same change. Gateway logs show an integrator session at 03:12. The unit goes to safe hold at 03:52; field gauges show the level never exceeded its normal band, and no release occurred. **Severity 1 declared 03:55.** The CySO reports to the FBI, CISA, and the Captain of the Port at 04:20 (6.16-1: immediately).
- **RMP and PSM:** the event could reasonably have resulted in a catastrophic release, so the incident investigation must start by **Thursday 2027-02-04, 03:40** (48 hours). It starts on 2027-02-02 at 10:00.
- **Wednesday 2027-02-03, 22:10:** ransomware encrypts the historian and 14 OT workstations. Blend halls go to safe state; PLT-01 batch production stops. The disclosure committee, already convened at 14:00 that day, meets again.
- **Friday 2027-02-05, 15:00:** the committee determines the incident is material (PLT-01 restart expected to take more than 10 days, safety systems targeted, Coast Guard involvement). **The Form 8-K is due by Thursday 2027-02-11** (4 business days: February 8, 9, 10, and 11).
- If forensics later shows the attacker took HR data from the business network, the state breach clocks start from that determination (Florida: 30 days for individuals and, if 500 or more Floridians, the Department of Legal Affairs).

## 7. Other notifications and the breach track (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Release reporting (if any release): written EPCRA follow-up as soon as practicable; RMP accident history within six months if 68.42 criteria are met; public meeting within 90 days if offsite impacts occurred | Vice President, Process Safety and EHS | Follow-up notices; RMP update |
| 7.2 | OSHA report if a worker was hospitalized (24 hours) or killed (8 hours) | Plant EHS manager | OSHA report |
| 7.3 | MTSA: record the incident (105.225(b)(3)); notify the COTP of any temporary deviation (101.665); after the incident, review the Cybersecurity Plan and submit amendments if needed | PLT-01 CySO; PLT-01 FSO | Records; COTP correspondence |
| 7.4 | Voluntary CISA and FBI reports for any other plant affected through the shared gateway | CISO | Report confirmations |
| 7.5 | **Personal information track (only if business network data was taken):** build the affected population with **state of residence**; apply each state's law using counsel's state matrix; Florida worked example: individuals within 30 days of determination (15-day good-cause extension for individual notice only), Department of Legal Affairs within 30 days if 500 or more Floridians, consumer reporting agencies if more than 1,000 | General Counsel; outside counsel | State deadline table; notices |
| 7.6 | Customers: SL-1 and SL-2 per contract; toll customers whose recipes were in the PLT-01 batch system are told whether their recipes were accessed or altered; the top 200 water utilities are called if supply is at risk | Customer owners | Contract notices logged |
| 7.7 | **Plan to the shortest clock** across MTSA, release reporting, process safety, SEC, and any state law. Publish one master calendar | General Counsel with the CISO | Master calendar |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.9). Paying does not restore trust in the control system: logic must still be reloaded from approved copies. Paying does not remove reporting or disclosure duties.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Safe state confirmed for every PSM unit; SIS trust confirmed against approved logic
2. Emergency notification path (kit, radios, mass notification)
3. Identity platform, break-glass accounts, and security tooling (EDR console, SIEM, OT monitoring) for clean-room validation
4. OT backup vault access and clean engineering workstations
5. PLT-01 DCS and batch management, one area at a time: ammonia unit and Chlor Unit first (restart only after MOC and, where required, a pre-startup safety review), then the blend halls and additives unit
6. Other plants on the shared gateway, after their sessions are reviewed
7. ERP order relay, shipping documentation, loading racks, and LIMS
8. Water utility allocation and SL-1 telemetry status updates
9. PLT-01 terminal automation and tank gauging (barge transfers resume after the FSO and CySO approve)
10. Historian and the one-way replication path to Cloud provider A (AI-001 stays suspended until the AI governance committee reviews data integrity, P10)

**Validate before reconnecting:** EDR or allowlisting clean, credentials rotated, logic hashes match approved copies, logging to the SIEM, and the plant manager's sign-off for each area. Keep manual operation until each process meets its RTO. Tell customers, utilities, and staff when services return (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Complete the RMP and PSM incident investigation report and resolve its recommendations (68.81(d)-(e)); feed the cyber scenario into the next PHA revalidation (POAM-024).
- Update the risk register (P01: R-001, R-002, R-006, R-012), the POA&M (P07), this runbook, the materiality playbook, and the PLT-01 Cybersecurity Plan.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality determination minutes, MTSA records, and investigation reports, for at least 6 years (POL-01 4.11), and longer where a rule requires it.

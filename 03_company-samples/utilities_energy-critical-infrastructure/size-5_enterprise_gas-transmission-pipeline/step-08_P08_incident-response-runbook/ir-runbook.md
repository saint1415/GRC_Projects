# Incident Response Runbook: Ransomware on Business IT Forcing a Precautionary Pipeline Shutdown

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded interstate natural gas transmission company: PS-1, PS-2, PS-3, and operated JV-1 to JV-3; 9 states) |
| Tier / Vertical | Enterprise / Energy (natural gas pipeline) |
| Incident type | Ransomware on business IT (with data theft) that leads the company to order a precautionary shutdown of **one pipeline system (PS-1)** because its OT integrity cannot be confirmed in time, while the other systems keep running. Includes TSA reporting to CISA, PHMSA notices, the SEC materiality assessment and Form 8-K Item 1.05, and multi-state breach notices |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT response guidance in NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 IT/OT Isolation Procedure; PRC-03.4 Multi-State Breach Notification Procedure; emergency plans (49 CFR 192.615); control room management procedures (49 CFR 192.631) |
| Runbook owner | Director of Security Operations, with the Vice President, Gas Control for sections 4 and 8, and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-08. Annex to the Cybersecurity Incident Response Plan v5 (SD Pipeline-2021-02G Section III.F) |
| Last tested | Enterprise exercise 2026-03-18 at GCC-1 (containment and IT/OT isolation; isolation completed in 9 minutes). **Not yet tested:** isolation at GCC-2 and PS3-CR (POAM-012, 2026-12-10 and 2027-02-24) and the disclosure committee step (tabletop 2026-11-12, POAM-013) |
| Notification matrix | `notification-matrix.csv` (31 obligations: 3 TSA and CISA, 1 SSI, 3 PHMSA, 1 emergency officials, 1 FERC posting, 4 SEC, 4 generic state, 4 Florida worked example, plus OFAC, law enforcement, insider trading, contractual rows, and 4 rows confirmed as not applicable or not in force) |
| Handling | The full runbook, with network details and contact numbers, is SSI as part of the Cybersecurity Incident Response Plan. This sample contains no SSI |

**The lesson this runbook is built on.** Ransomware on business IT does not by itself make a pipeline unsafe. The BIA (P05) shows gas control needs no business IT: nominations, measurement, and invoicing all have manual workarounds. A shutdown is justified only when the company **cannot trust or cannot see its OT** for a pipeline system, or cannot staff safe manual operation beyond the gas control MTD (4 hours, P05 BP-01). At this size the decision is made **per pipeline system and segment**: GCC-1 controls PS-1, PS-2, and the JV pipelines, and each can be trusted, run manually, or shut down on its own evidence.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (cyber) | Director of Security Operations | SOC manager on duty | SOC bridge on the out-of-band conferencing service |
| OT incident lead and TSA Cybersecurity Coordinator | Director of OT Security | Director of Security Operations; CISO (alternates) | Coordinator 24x7 line |
| Operations lead | Vice President, Gas Control | Gas control shift supervisor at GCC-1 | GCC direct lines; radio |
| Controllers on duty | Desk controllers at GCC-1, GCC-2, PS3-CR | Qualified relief controllers | Console phones; radio |
| Shutdown decision (per pipeline system) | Chief Operating Officer | CEO | Out-of-band group on company mobile phones |
| Executive incident lead | CISO | Chief Information Officer | Out-of-band group |
| Crisis management team chair | Chief Operating Officer | Senior Vice President, Operations | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| PHMSA notices | Vice President, Pipeline Safety and Compliance | Director of Pipeline Safety Compliance | Direct mobile |
| Shippers, interconnects, JV owners | Vice President, Commercial Operations; Vice President, Contract Operations | Directors of scheduling and contract operations | Direct mobile; shipper contact list in the binder |
| Outside breach counsel and forensics (IT and OT) | Retained firms engaged through counsel and the insurer panel | Managed security service provider incident team (IT only; no OT access) | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Government | CISA Central (844-729-2472); FBI field office; TSA through CISA and the Coordinator | State emergency management agencies along the affected system | Numbers in the binder |

**Out-of-band first.** Assume email, chat, the business phone system, and the enterprise identity platform may be compromised. Use company mobile phones, the out-of-band conferencing service, satellite phones at the GCCs, and the printed incident binder at GCC-1, GCC-2, PS3-CR, and each regional office.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at each control room: this runbook, the decision tables in section 4, the isolation procedure (PRC-03.3), the manual operation plan, contacts, and the notification matrix
- [ ] IT/OT isolation procedure exercised at every control room in the last 12 months (POL-03 4.5). **Gap: GCC-2 and PS3-CR until POAM-012 closes**
- [ ] Offline SCADA backups at the other GCC, less than 7 days old, scanned when made (CP-9). **Gap: PS-3 backups are online only until POAM-016's first milestone (2026-12-31)**
- [ ] OT monitoring live and baselined, so the company can show OT traffic is normal (SI-4). **Gap: 22 stations, including all 20 PS-3 stations, until POAM-005 closes; OT integrity checks there take longer (section 4)**
- [ ] All vendor OT access through the gateway; no always-on paths (AC-17). **Gap: 7 modems until POAM-004 closes (2026-12-15); they are switched off at the carrier in step 3.2**
- [ ] Immutable IT backups in separate accounts, restore-tested in the last 90 days for tier-1 IT (CP-9)
- [ ] EDR on 98% of IT endpoints; SIEM receives logs from all forwarded IT and OT sources (12 months online)
- [ ] Break-glass OT and IT accounts sealed and tested this quarter (POL-02 4.12)
- [ ] Materiality playbook, 8-K templates, and disclosure committee roster current. **Gap: curtailment factors until POAM-013 closes (2026-11-30)**
- [ ] Pre-drafted notices for shippers, interconnects, JV owners, and state emergency managers in the binder

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file encryption, or EDR tamper alerts on business endpoints or servers | EDR; staff report; backup job failures | SOC opens a severity-1 case; isolate hosts through EDR (do not power off); page the incident commander and the Director of OT Security |
| Shipper services platform, measurement system, or ERP unreachable with no provider outage | Monitoring; shipper calls | Treat as possible ransomware until ruled out |
| Suspicious activity in a GCC DMZ (historian replica, patch staging, log collector) or on the OT remote access gateway | OT monitoring cell; gateway alerts | Severity 1; recommend DMZ isolation to the Vice President, Gas Control at once |
| Anything unusual on a console or station HMI: unexpected pop-ups, slow displays, values that disagree with the field, commands no controller issued | Controller; station operator | **Controller follows the control room management and emergency procedures first**, then calls the shift supervisor and the OT monitoring cell |
| Extortion message or leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve; do not engage without counsel |
| Supplier reports ransomware affecting company data or access (SCADA vendor, compression manufacturer, payroll SaaS) | Supplier notice | Disable that supplier's gateway accounts; open a supplier incident case (section 7) |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production system, or OT is affected or suspected (POL-03 4.3).

**Record these times separately in the incident log:**
1. **Identification of the cybersecurity incident:** starts the 72-hour TSA report to CISA (SD 01G Section II.C).
2. **Confirmed discovery of a PHMSA incident** (if the shutdown or a release is judged an incident under 49 CFR 191.3): starts the 1-hour NRC notice.
3. **Materiality determination** (made later by the disclosure committee): starts the 4-business-day Form 8-K clock.
4. **Determination of a breach of personal information:** starts state clocks (Florida: 30 days).

## 3. First hour (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| T+0 to 15 min | 3.1 Tell the shift supervisors at GCC-1, GCC-2, and PS3-CR. **Close the IT/OT DMZ connections at every control room** under PRC-03.3. Do not wait for proof that OT is affected (POL-03 4.5) | Vice President, Gas Control (authority); OT security engineers | DMZ firewalls show no sessions from business IT; time recorded |
| T+0 to 15 min | 3.2 Disable all vendor gateway accounts except named emergency support; have the carrier suspend the 7 vendor modems; suspend the managed security service provider's cloud administrator roles | Director of OT Security | Accounts and modems disabled |
| T+0 to 30 min | 3.3 Controllers confirm SCADA is responsive and values make sense (line pack, key pressures, compressor status) for each pipeline system. Controllers keep operating | Controllers; shift supervisors | Status per system reported to the Vice President, Gas Control |
| T+0 to 30 min | 3.4 Isolate affected IT hosts through EDR; block attacker infrastructure; revoke sessions and rotate privileged credentials; use break-glass accounts if single sign-on is affected | SOC; identity team | Hosts contained; revocations logged |
| T+0 to 60 min | 3.5 Confirm IT backup accounts are untouched (immutability locks, no recent deletions) | Director of Cloud Platform Engineering | Backup integrity confirmed |
| T+15 to 45 min | 3.6 CISO briefs the CEO and the General Counsel; counsel engages forensics under privilege; insurer notified; COO activates the crisis management team | CISO; General Counsel; COO | Engagement letters; claim number |
| T+30 to 60 min | 3.7 Put field crews on standby to staff compressor stations and key meter stations for manual operation on each pipeline system | Senior Vice President, Operations | Crews on standby or dispatched |
| T+60 min | 3.8 **Decision point 1** (section 4) | Vice President, Gas Control recommends per system; COO decides | Decision recorded in the incident log |
| Ongoing | 3.9 Start the incident log and the evidence register | Incident commander | Log open (paper if needed) |

## 4. The operate-or-shut-down decision, per pipeline system (RS.AN, RS.MI)
The Vice President, Gas Control recommends and the Chief Operating Officer decides for each pipeline system (POL-03 4.6). A controller or field supervisor who must act at once for safety under the emergency plan (49 CFR 192.615(a)(6)) does so without waiting.

**Decision point 1 (T+60 min), asked separately for PS-1, PS-2, PS-3, and JV-1 to JV-3:**
| Question | How to check | If yes | If no or unknown |
|---|---|---|---|
| Are the DMZs closed and holding? | DMZ firewall session tables at each GCC | Continue | Close again; escalate |
| Do SCADA values agree with the field? | Field crews read local gauges at 3 or more sites per system and compare by radio | Continue | Move that system to **manual operation** |
| Is there any sign of activity in OT? | OT monitoring cell reviews baselines, OT domain logons, gateway and privileged sessions, and recent configuration changes (no active scanning). **Where sensors are missing (22 stations), check station HMI local logs and firewall logs by hand** | Continue | Treat that system's OT as untrusted |
| Is any business IT system needed to run safely in the next 24 hours? | BIA (P05): no. Nominations go by phone and secure email; measurement is estimated from SCADA | Continue | Not expected |

**Outcomes for each pipeline system:**
- **A. Isolate and operate (the default).** All answers are yes. Keep the DMZs closed. Run scheduling manually (P05 BP-05 workaround). Recheck every 4 hours.
- **B. Manual operation.** SCADA values for that system cannot be trusted, but field crews can hold it safely. Follow the manual operation plan (192.631(c)(3)). Consider reducing pressure to widen safety margins. The 4-hour gas control MTD (P05) sets decision point 2.
- **C. Controlled precautionary shutdown or curtailment.** Choose this when manual operation cannot be staffed safely beyond the MTD, when there is evidence that someone other than a controller is sending commands to field devices, or when the Vice President, Gas Control judges that neither SCADA nor manual operation can keep the system within its operating limits. Shut down by segment under the O&M manual (192.605) and the emergency plan. Before closing any delivery point, coordinate with the LDCs and power generators it serves, because a loss of gas supply to homes and power plants creates its own safety risk.

**Decision point 2 (T+4 h, then every 4 h):** reassess each system with the forensic findings. A shutdown is lifted only under section 8.

**What does not justify a shutdown on its own:** loss of the shipper services platform, measurement, invoicing, email, or the ERP. These are business processes with MTDs of 12 to 120 hours (P05).

**Worked example (fictional; dates used throughout this runbook).** Monday 2027-01-11, 06:40: EDR detects encryption on file servers and the ERP; the incident is identified and declared. By 07:00 all three control rooms have closed their DMZs. By 08:30 forensics finds the attacker's tools on the PS-1 station engineering jump host in the GCC-1 DMZ, which had an open session to 6 PS-1 compressor stations before isolation, 3 of them legacy stations without OT monitoring. PS-2, PS-3, and the JV pipelines show no OT activity and stay under outcome A. PS-1 moves to outcome B at 09:00. At 13:00 the Senior Vice President, Operations reports that manual operation of 41 PS-1 stations cannot be staffed beyond the evening, and controllers cannot rule out changed set-points at the 3 unmonitored stations. **At 14:00 the COO orders a controlled precautionary shutdown of the PS-1 mainline south of the affected stations**, after the LDCs and power generators it serves confirm they can draw on other supply or curtail.

## 5. Analysis, containment, and eradication (RS.AN, RS.MI)
1. **Scope (forensics with the SOC):** affected hosts, cloud accounts, identities, and data stores, from EDR, the SIEM, cloud audit logs, and identity logs. Collect local logs from stations that do not forward (90-day retention) before they roll over.
2. **Initial access:** phishing, stolen credentials, an exploited internet-facing edge device (R-048), or a supplier path. Check the OT remote access gateway and the 7 modem paths first.
3. **Evidence:** capture memory before powering off or reimaging any host (POL-03 4.12; POAM-024); image the DMZ jump host before cleanup; label and secure affected equipment; keep chain of custody in the evidence register.
4. **OT integrity per system (OT forensics firm with SCADA and compression engineering):** compare PLC logic and set-points at affected stations with the golden copies; check SCADA host file integrity; confirm no unauthorized commands in the historian and SCADA event journal; at legacy stations, compare logic manually.
5. **Exfiltration:** determine what left: employee personal information (HR and payroll files), shipper commercial data, SSI (TSA plans and assessments), or CEII (engineering data). This drives sections 6 and 7.
6. **Contain and eradicate:** block attacker infrastructure; disable compromised accounts; reset privileged and service credentials in IT; rebuild affected IT hosts from clean images (never decrypt and reuse); rebuild the DMZ jump host; patch the initial access path.
7. **Business impact for the disclosure committee:** Finance estimates daily impact from P05 values and the tariff. In the worked example: about $3.5 million a day of reservation charge credits for curtailed PS-1 firm service (fictional estimate), shipper claims, response costs, and the effect on the PS-1 customers that generate power for Florida.

## 6. Reporting, SEC materiality, and disclosure (RS.CO)
**Follow `notification-matrix.csv`.** Pipeline notices are owned by the Vice President, Pipeline Safety and Compliance; the TSA report by the Cybersecurity Coordinator; SEC and breach notices by the General Counsel.

### 6.1 Operational and regulatory reports
| When | Action | Owner |
|---|---|---|
| Within 1 hour of confirmed discovery of a 191.3 incident | **NRC telephonic notice (191.5).** A precautionary shutdown of a pipeline system for a cyber event is judged "significant in the judgment of the operator" (191.3 paragraph (3)) by default. Worked example: shutdown at 14:00, NRC call by 15:00 | Vice President, Pipeline Safety and Compliance |
| Before any curtailment, then as conditions change | Post the outage or reduction on the informational postings website (18 CFR 284.13(d)(1)); notify affected shippers under the tariff; call interconnects, LDCs, and power generators; notify JV owners if a JV is affected | Vice President, Commercial Operations; Vice President, Gas Control |
| If an emergency exists | 9-1-1 centers and public officials along the affected system (192.615(a)(8)); state emergency management agencies; Florida first in the worked example | Vice President, Gas Control |
| As soon as practicable, no later than 72 hours after identification | **TSA report to CISA** (SD 01G Section II.C), with all required content available. Company target: within 24 hours. Worked example: identified 2027-01-11 06:40; due by 2027-01-14 06:40; filed 2027-01-11 17:30 | Director of OT Security |
| Within 24 hours of new information | Supplemental report to CISA (SD 01G Section II.C.5) | Director of OT Security |
| Within 48 hours of confirmed discovery | Revise or confirm the NRC notice (191.5(c)). Worked example: by 2027-01-13 15:00 | Vice President, Pipeline Safety and Compliance |
| Promptly, if SSI was taken | Inform TSA (49 CFR 1520.9(c)) | General Counsel |
| Within 30 days of detection | PHMSA Form F 7100.2 (191.15(a)(1)), with supplements as facts develop. Worked example: by 2027-02-10 | Vice President, Pipeline Safety and Compliance |

### 6.2 SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. The materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, using quantitative and qualitative factors. It does not wait for the investigation to finish.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.2.1 | CISO briefs the General Counsel within 24 hours of a severity-1 declaration (POL-03 4.8) | CISO | Brief logged |
| 6.2.2 | Disclosure committee convenes within 48 hours and meets at least every 2 business days until a decision. The Vice President, Gas Control attends to explain the shutdown | General Counsel | Minutes started |
| 6.2.3 | **Special trading blackout** to committee members, responders with knowledge, and executives (POL-05 4.8) | General Counsel | Notice sent |
| 6.2.4 | Committee completes the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet complete |
| 6.2.5 | **Materiality determination** recorded with date, time, and reasoning, whether material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee | Determination minute signed |
| 6.2.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident and its material impact or reasonably likely material impact. Do not include technical details that would impede response or remediation, and no SSI | General Counsel; CFO; outside counsel | Draft approved by the CEO and CFO |
| 6.2.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.2.8 | Align shipper, media, investor, and employee messages with the filing; brief the audit committee and risk committee chairs before filing | Communications; Investor Relations | Messages approved |
| 6.2.9 | Reassess as facts change; counsel decides whether an amended filing is needed; carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist; curtailment rows added under POAM-013):**
| Factor | What the committee considers |
|---|---|
| Quantitative | Reservation charge credits owed for curtailed firm service; shipper claims; lost interruptible revenue; deferred invoicing (P05 BP-10); response, forensic, and restoration costs; ransom demand; insurance coverage and retention |
| Operational | Which pipeline systems are shut down or in manual operation, for how long; restart timeline; effect on PS-1 customers that generate power |
| Safety and regulatory | Any release, injury, or near miss; PHMSA incident report; TSA inquiries; FERC tariff obligations; state public utility or emergency management involvement |
| Data | Employee and shipper records taken; SSI or CEII taken |
| Reputation and strategy | National media; effect on shipper and JV relationships, credit ratings, and pending expansion projects |

**Worked example of the SEC clock:** the committee convenes Tuesday 2027-01-12 and determines on Wednesday 2027-01-13 at 18:00 that the PS-1 shutdown is material. The 4 business days are January 14, 15, 19, and 20 (Monday 2027-01-18 is a federal holiday), so the Form 8-K is due by Wednesday 2027-01-20.

## 7. Breach notification workflow (RS.CO)
| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Build the affected-individual file from forensic results: each person, data elements, and **state of residence** (HR address for employees and former employees; business contacts for shippers) | General Counsel; Chief Human Resources Officer | File with state counts |
| 7.2 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: deadlines, regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline per state | Outside counsel | State deadline table |
| 7.3 | **Florida worked example:** individual notice within 30 days of determining the breach (15 more days only for individual notice, on written good cause to the Department); Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at once. Worked example: forensics confirms on 2027-01-22 that HR files of about 3,100 Florida employees and former employees were taken, so Florida notices are due by 2027-02-21 | General Counsel | Florida filings |
| 7.4 | **Plan to the shortest clock** across all states and publish one master calendar | General Counsel | Master calendar |
| 7.5 | Honor and document any law enforcement delay request where a state allows it | General Counsel | Delay record |
| 7.6 | Engage the mail vendor, call center, and credit monitoring provider | Chief Human Resources Officer | Vendors active |
| 7.7 | Track inbound supplier notices (for example Fla. Stat. 501.171(6): 10 days) if the incident started at a supplier | Director of Third-Party Risk Management | Supplier notices logged |
| 7.8 | Notify contractual parties per contract: shippers (SL-1), JV owners (SL-2), the insurer, lenders if the credit agreement requires it | Contract owners | Contract notices logged |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check and a report to the FBI or CISA (POL-03 4.9). Paying does not restore trust in OT; the section 8 checks still apply. Paying does not remove any reporting or disclosure duty.

## 8. Recovery and restart (RC.RP, RC.CO)
**Restore in BIA priority order (P05 section 7), in a clean environment first:**
1. Gas control for systems under outcome A or B (already running) and emergency communications
2. OT identity and OT privileged access, then SOC tooling for clean-room validation
3. Enterprise identity platform, network core, and DNS
4. Shipper services platform (nominations and postings), from immutable backups after validation
5. Email, collaboration, and telephony
6. Integrity analytics and AI-001 (only after revalidation, P10, because its data passed through the DMZ)
7. JV owner portal and statements
8. Measurement system (reconcile from flow computers, which keep at least 35 days of data)
9. Work management and learning systems
10. ERP and payroll
11. Invoicing and gas accounting
12. Engineering, GIS, and integrity records

**Before reopening any DMZ:** forensics confirms business IT and the DMZ are clean; the jump host and historian replica are rebuilt; vendor access is re-enabled one supplier at a time through the gateway; the Vice President, Gas Control signs off for each control room.

**Restarting a pipeline system after a shutdown (PS-1 in the worked example):**
1. OT forensics confirms PLC logic and set-points match golden copies at every affected station; any station that cannot be confirmed is reloaded from the offline golden copy.
2. Point-to-point checks on any display or point that changed (192.631(c)(2)).
3. Follow the O&M manual start-up procedures (192.605); coordinate with interconnects, LDCs, and power generators.
4. Controllers confirm SCADA values against field readings at every delivery point before returning to remote control.
5. The COO approves the restart on the Vice President, Gas Control's recommendation. Post the return to service (284.13(d)(1)).

Tell staff, shippers, JV owners, and officials as each service returns (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.13).
- Review control room actions under 192.631(g) and add lessons to controller training.
- Update the risk register (P01: R-001, R-003, R-012, R-013), the POA&M (P07), this runbook, the materiality playbook, and the Cybersecurity Incident Response Plan; request a TSA plan amendment if a measure changes permanently (POL-01 4.7).
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including determination minutes, PHMSA reports, and the CISA report, for at least 5 years (POL-01 4.11).

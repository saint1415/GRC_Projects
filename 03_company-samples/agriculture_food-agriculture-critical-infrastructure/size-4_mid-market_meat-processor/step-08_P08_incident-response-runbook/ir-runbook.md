# Incident Response Runbook: Ransomware Halting Processing Lines and Cold-Chain Monitoring

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed meat processor with two USDA-inspected plants) |
| Tier / Vertical | Mid-Market / Food and Agriculture |
| Incident type | Ransomware that starts on the business network, reaches SCADA, historians, and the MES at one or both plants, stops processing lines, and cuts cold-chain monitoring; may include theft of employee data or formulations |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions, with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-process-tampering.md` (suspected tampering with setpoints or formulations); `notification-matrix.csv`; BIA (P05); HACCP corrective action procedures; recall procedures; PSM and RMP emergency plans |
| Runbook owner | Security Manager (incident commander), with the Controls Engineering Manager (OT) and the VP FSQA (food safety) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Plant ransomware tabletop with outside counsel scheduled 2026-11-19 (POAM-012) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, plant, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, VP FSQA, Director of Communications, HR Director, VP of Sales and Customer Service, outside breach counsel | Business continuity, customer commitments, external statements, ransom recommendation to the CEO, resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director (IT recovery), Controls Engineering Manager (OT lead), OT security engineer, security analyst, MSSP, OT-capable forensic firm (through counsel), both controls integrators (on site only) | Containment, investigation, eradication, recovery sequence |
| **Plant command (one per affected plant)** | Plant Manager, Plant FSQA Manager, Director of Engineering and Maintenance (or the plant PSM coordinator), warehouse lead | Safe state, product holds, manual monitoring, refrigeration safety, line restart |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| OT lead | Controls Engineering Manager | Senior controls engineer | Cell; plant radio |
| Food safety lead (holds, FSIS notice) | VP FSQA | Plant FSQA Manager | Cell |
| Refrigeration and ammonia safety | Director of Engineering and Maintenance | Plant PSM coordinator; refrigeration contractor on site | Cell; engine room phone |
| Legal | General Counsel; outside breach counsel (insurer panel) | Company's outside general counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel OT-capable forensic firm, engaged by counsel | MSSP incident response team (IT only) | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Communications | Director of Communications | Outside crisis PR (through counsel) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, VoIP, and the identity provider are compromised. Use the pre-provisioned messaging group on personal phones, plant radios, and the printed call trees in the incident binders (FSQA office, engine room, and shipping office at each plant).

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs, product hold list) separate from legal conclusions. **Food safety records are never privileged and must stay available to FSIS** (9 CFR 417.5(f)).

## 1. Preparation checks (Identify / Protect)
- [x] Immutable cloud backups in the separate backup account, 35-day write-once retention (CP-9; restore test passed in P07)
- [x] EDR on all managed IT endpoints with 24x7 MSSP (escalation tested at 22 minutes in P07)
- [x] Plant 1 OT DMZ and remote access gateway with MFA
- [ ] Immutable offline OT backups; Plant 2 PLC and recipe repository; OT restore test within 90 days (CP-9, CP-4). **Gap until POAM-010 closes**
- [ ] Plant 2 segmented from its office network (SC-7). **Gap until POAM-016 closes**
- [ ] OT alerts reaching the MSSP (SI-4). **Gap until POAM-006 closes**
- [x] Incident binders at both plants: this runbook, contacts, notification matrix, manual CCP forms, manual temperature log forms, signed formulation sheets, label stock procedure
- [ ] Plant 2 manual temperature log procedure (POAM-019, due 2026-10-31)
- [ ] Daily offline traceability export to the FSQA office safe at each plant (due 2026-10-31; P01 R-016)
- [ ] Break-glass accounts for the identity provider and records application (planned; cloud break-glass exists)
- [x] Insurer panel counsel and OT-capable forensics confirmed; contact list verified 2026-09-15

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption on an office PC or server | EDR alert; staff report | MSSP isolates the host and calls the incident commander within 30 minutes |
| HMIs show "communication lost", SCADA screens freeze, or the MES will not load formulations | Operators; line supervisors | Supervisor calls the Controls Engineering Manager and the incident line. **Do not power off** SCADA or MES servers. Pull network cables only as directed |
| Cold-chain dashboard stops updating, or no alerts arrive during a known excursion | Warehouse lead | Start the manual temperature log at once; call the incident line |
| Backup deletion attempts, EDR tampering, or disabled logging | Cloud audit logs; EDR | Treat as a ransomware precursor; declare |
| New domain administrator or engineering account; engineering downloads outside a change ticket | SIEM; Plant 1 OT sensor | Disable the account; declare if unexplained |
| Extortion email or leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve the message |

**Severity 1 (declare immediately):** any confirmed ransomware execution, any loss of SCADA, MES, or cold-chain monitoring with signs of malicious activity, or an extortion claim naming company data.

**Record the times** of discovery and of every product-affecting event: last trusted CCP reading per line and cooler, start of manual monitoring, last verified formulation load. These times drive product decisions (9 CFR 417.3(b)) and notification clocks.

## 3. First 2 hours: make the plants safe (RS.MA, RS.MI)
**Order matters.** Protect people, then product in process, then evidence and systems.

| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | Confirm both refrigeration systems run on their local controllers and ammonia detection reads normal. If a controller shows signs of compromise, switch compressors to the manual operation procedure under the PSM operating procedures | Director of Engineering and Maintenance | Engine rooms report stable; no ammonia alarm |
| 0-30 min | Start manual temperature logging for every cooler, freezer, and loaded trailer, at least hourly | Warehouse leads at each plant | First manual entries recorded |
| 0-30 min | Put lines in a safe state: let smokehouse and oven cycles finish on local controllers where the cycle is intact, or abort and hold; stop brine injection and dosing; stop blenders; close CIP valves manually | Plant Manager with the Controls Engineering Manager | Every line stopped or finishing a verified cycle |
| 0-30 min | **Hold all product** made, cooked, chilled, blended, or stored since the last trusted CCP record, and any product dosed from the MES since the last verified formulation | Plant FSQA Managers | Hold tags on product; hold list started |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-60 min | Isolate: break the corporate-to-OT link at the Plant 1 OT DMZ, the Plant 2 perimeter, and the site-to-cloud VPN tunnels; disable the remote access gateway and confirm the Plant 2 modem is unplugged. Leave affected hosts powered on for memory evidence | IT Director and Controls Engineering Manager | Links down; photos of cable positions taken |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages OT-capable forensics | Chief Financial Officer | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Revoke all identity provider sessions; reset privileged credentials with break-glass accounts; disable all vendor accounts | Security Manager | Sessions revoked |
| 1-2 h | Brief the FSIS inspection personnel on site at each plant: electronic CCP monitoring is down, manual monitoring and holds are in place | Plant FSQA Managers | Briefing time recorded |
| 1-2 h | Convene the CMT; first situation report (plants affected, product held, refrigeration status, customer impact, decisions needed) | CMT chair | CMT meeting held |
| 2 h | CEO informs the audit committee chair and the sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope.** Which office hosts, OT servers, HMIs, engineering workstations, cloud accounts, and identities are affected, at which plant? Use EDR telemetry, identity provider sign-ins, cloud control-plane logs in the locked log bucket, firewall and gateway logs (plant logs keep only 30 to 90 days: export them first), and the Plant 1 OT sensor.
2. **Initial access.** Phishing, the Plant 2 integrator VPN, the refrigeration modem, an internet-facing appliance, or a Plant 1 gateway vendor account. These paths are the likely ones (P01 R-001, R-002, R-005, R-017, R-023, R-041).
3. **Did the attacker touch the process?** With the Controls Engineering Manager, compare PLC programs, smokehouse and oven cycles, injector and dosing rates, blend recipes, and every MES formulation with the repository and the signed formulation masters. Check CIP valve logic on both injector brine systems. **Any unexplained difference is handled under `ir-runbook-process-tampering.md` as possible intentional adulteration** (POL-03 4.5).
4. **Preserve evidence.** The forensic firm images affected servers and exports logs with chain of custody (who collected, when, hash, storage). OT evidence collection follows the forensic firm's OT procedure; no tools are run on PLCs.
5. **Exfiltration.** Did the attacker take employee data (HR exports, payroll files on shares), formulations, or the food defense plans? Build the **affected individuals list** by data element and state of residence. This drives the breach decision and the food defense reanalysis.
6. **Backups.** Confirm OT and cloud backups are intact and clean (taken before the attacker's first access) before any restore.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the plant firewalls, SD-WAN, and the cloud firewall.
2. Disable compromised accounts. Rotate every shared OT password, integrator and contractor credentials, and service accounts between the MES, ERP, WMS, and the cloud.
3. Rebuild affected office endpoints and OT Windows hosts (SCADA, historians, MES, engineering workstations) from clean media. **Do not decrypt and reuse them.**
4. Reload PLC programs from the repository wherever the comparison in section 4 step 3 failed or could not be completed. At Plant 2, use the integrator's copies only after the forensic firm checks them.
5. Keep all vendor remote access off. Vendors work on site under escort until the gateway is rebuilt and the forensic firm clears it.
6. Forensics confirms persistence is removed before anything is reconnected.

## 6. Food safety, process safety, legal, and external communication (RS.CO)
**Food safety decisions come first, and they are the VP FSQA's.** Follow `notification-matrix.csv`. Counsel confirms personal-data notices.

**Product on hold.** For each held lot, the Plant FSQA Manager documents the review required for unforeseen deviations (9 CFR 417.3(b)): segregate and hold, determine acceptability using manual records, chart recorders, historian replicas in the cloud, and product testing where needed, and dispose of anything that cannot be shown safe. Product may not ship until its records are complete (9 CFR 417.5(c)).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Has any **already-shipped** product possibly been affected (shipped after monitoring stopped, or after an unexplained formulation or setpoint change)? If evaluation shows it is adulterated or misbranded, notify the FSIS District Office within 24 hours of that determination (9 CFR 418.2) and start the recall procedure (418.3) | VP FSQA | Decision log; hold list; traceability export |
| D2 | Did refrigeration lose supervisory control in a way that could reasonably have caused a catastrophic release? Start a PSM and RMP incident investigation within 48 hours (1910.119(m); 68.81). Any release of 100 lb or more of ammonia in 24 hours goes to the National Response Center immediately (40 CFR 302.6), and to the LEPC and SERC if it can expose people off site (40 CFR 355.40-355.42) | Director of Engineering and Maintenance | Investigation record |
| D3 | Was employee personal information accessed or acquired? Date of determination (Florida clock) | General Counsel with counsel | Decision log |
| D4 | Number of affected individuals, by state (500 or more Floridians: Department of Legal Affairs; more than 1,000: consumer reporting agencies) | General Counsel | Affected individuals list |
| D5 | Customer notices due (24-hour event notice; 72-hour portal security notice)? | VP of Sales and Customer Service with counsel | Contract register |
| D6 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged; FSIS personnel on site briefed | CFO; Plant FSQA Managers |
| Hour 0-24 | D1 decision for shipped product; FSIS District Office notice within 24 hours of any determination | VP FSQA |
| Hour 0-24 | Customer notices under supply agreements (delivery impact, any hold or recall) | VP of Sales and Customer Service |
| Hour 0-48 | D2: PSM and RMP investigation started if the trigger is met | Director of Engineering and Maintenance |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA; supports OFAC mitigation and can bring OT response help | Security Manager through counsel |
| Within 72 hours of confirmation | Portal and EDI security notice to the largest customer if those services were affected | Security Manager with the General Counsel |
| Within 30 days of determination | Florida individual notice; Department of Legal Affairs notice if 500 or more Floridians (no extension for the Department notice) | General Counsel and counsel |
| Without unreasonable delay | Consumer reporting agencies if notice goes to more than 1,000 individuals at once | Counsel |
| Each other state | Plant 2 employees living in Georgia and former employees elsewhere: apply each state's law (counsel checks the list by state) | Counsel |

**Plan to the shortest clock.** The 24-hour FSIS clock starts at *learning or determining*, not at discovery of the cyber incident, but the product question must be answered with reasonable speed. Do not let IT work delay it.

**Ransom decision (POL-03 4.9).** Needs the CEO, the General Counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet; and a report to law enforcement. Paying does not make held product safe, does not restore trust in formulations, and does not remove any notification duty. The default position, approved by the CEO, is not to pay while backups are intact.

**CIRCIA:** not in effect. Recheck when the final rule is published; coverage depends on the affiliation question in P03.

**Communications.**
- Staff: briefings by plant radio and text at each shift change; the out-of-band channel only.
- Customers: direct calls from the VP of Sales and Customer Service, with the VP FSQA for any product question.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Each step is validated before the next begins: EDR clean or allowlisting on, credentials rotated, and forensics sign-off for the zone.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Refrigeration supervised and ammonia alarms visible (SYS-04) | 0.5 h | Controller logic and setpoints compared with the last approved export |
| 2 | Temperatures recorded (manual log until cold-chain gateways are on a clean network) | 1 h | Gateways reconnected only on the clean segment |
| 3 | Safe state for in-process product; held product evaluated | 2 h | FSQA hold list complete |
| 4 | SCADA and historians from a verified clean backup | 4 h | Historian gap covered by manual records |
| 5 | MES restored, then **every formulation compared with the signed master** before any dosing; Plant 2 blend recipes re-entered from signed sheets and approved | 8 h | Two-person check recorded |
| 6 | Packaging, labeling, and lot coding at both plants | 8 h | Manual labels with a second-person check until the MES and label server are back |
| 7 | Identity provider, SD-WAN, corporate network | 8 h | Sessions revoked; privileged credentials rotated |
| 8 | Records application, traceability database, EDI gateway | 12 h | Restore from the backup account; enter manual records |
| 9 | ERP and WMS for shipping | 12 h | Credentials rotated |
| 10 | Customer portal (8 h during a recall), payroll, finance | 24 to 48 h | Portal integrity check of lot data and certificates |

**Validate before restart (POL-03 4.10).** Each line restarts only after the Controls Engineering Manager confirms PLC programs, recipes, and setpoints match the approved versions, the Plant FSQA Manager signs the restart checklist, and the first batch on each line is verified against critical limits. Tell staff, customers, and the FSIS personnel on site when normal monitoring resumes (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery with plant command; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-002, R-005, R-007, R-015), the POA&M (P07), this runbook, the HACCP plans (reassessment under 9 CFR 417.3(b)(4) for the unforeseen deviation), and the food defense plans if any tampering was found or cannot be ruled out.
- PSM and RMP: complete the investigation report and resolve its findings (1910.119(m)(4)-(5)); keep it 5 years.
- Retain incident records for at least 3 years (POL-01 4.13), and hold and disposition records with the HACCP records.

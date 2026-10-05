# Incident Response Runbook: Ransomware Spreading from Business IT toward Field SCADA

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed independent crude oil producer with a Panhandle gathering system) |
| Tier / Vertical | Mid-Market / Mining, Quarrying, and Oil and Gas Extraction |
| Incident type | Ransomware (with possible data theft for extortion) that starts in business IT and spreads toward the SCADA network, most likely through the BCC or South Florida site firewalls that bypass the OT DMZ (P01 R-001) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions, with OT response and recovery guidance from NIST SP 800-82 Rev. 3 (sections 3.3.8, 6.4, 6.5) |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-ot-remote-access.md` (unauthorized remote command through a vendor path); `notification-matrix.csv`; BIA (P05); emergency response plan; pipeline emergency procedures |
| Runbook owner | Security Manager (incident commander), with the SCADA and Automation Manager for OT steps |
| Approved | 2026-09-16 by the Chief Operating Officer, with the VP Operations agreeing to the field steps |
| Last tested | Not yet. South Florida and Alabama OT tabletops 2026-12-08; crisis management tabletop with the CEO and General Counsel 2026-12-15 (POAM-016) |

**The rule that overrides everything below: safety first.** The hardwired safety shutdowns (H2S detection, tank high-level, compressor emergency shutdown) and the gathering pump station's high-pressure shutdown switches do not depend on SCADA. Never disable, bypass, or reset them as part of incident response. If anyone is unsure whether a site is safe, the Field Superintendent shuts it in under the emergency response plan. A suspected release is handled under the pipeline emergency procedures or the emergency response plan first and investigated as a cyber event second.

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers so that technical, operational, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, VP Operations, VP IT, Security Manager, HSE Director, Pipeline Compliance Manager, HR Director, outside breach counsel | Business continuity, area-wide shut-ins, external statements, the ransom recommendation to the CEO, spending, regulator and partner communications |
| **Incident response team (IRT)** | Incident commander: Security Manager. OT lead: SCADA and Automation Manager with the OT Security Engineer. VP IT (IT recovery lead), Security Analyst, MDR provider, OT-capable forensic firm (through counsel), SCADA integrator | Containment, isolation of IT/OT connections (POL-03 4.4), investigation, eradication, recovery sequence |
| **Field command** | VP Operations; Field Superintendents (Panhandle, South Florida, Southwest Alabama); Control Room Manager and OCC shift lead; HSE Director; Pipeline Compliance Manager | Manual operations, patrols, shut-in order, pipeline emergency procedures, spill and accident notices |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | VP IT | Out-of-band group on company and personal phones; printed call tree |
| OT lead | SCADA and Automation Manager | OT Security Engineer | Cell; OCC landline |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Field operations | VP Operations | Field Superintendent of the affected area | Cell; field radio |
| Control room | OCC shift lead | Control Room Manager; BCC on-call Production Controller | OCC and BCC landlines |
| Pipeline notices | Pipeline Compliance Manager | VP Operations | Cell; pipeline emergency binder |
| Spill and safety notices | HSE Director | HSE on-call | HSE on-call binder |
| Legal | General Counsel, with outside breach counsel (insurer panel) | Outside breach counsel | Cell; through the insurer hotline |
| Cyber insurer | Carrier breach hotline ($15 million limit, $500,000 retention) | Broker | Policy card in the incident binder |
| Forensics | OT-capable panel forensic firm, engaged by counsel | MDR provider's incident response team | Through counsel |
| Monitoring and IT containment | MDR provider 24x7 | n/a | MDR hotline |
| SCADA support | SCADA integrator emergency line | SCADA vendor support | Integrator contract card |
| Board and sponsor | CEO informs the audit committee chair and the PE sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, the identity provider, and VoIP are compromised. The CMT and IRT use a pre-provisioned messaging group on phones that are not enrolled in company single sign-on, plus OCC and BCC landlines and field radio. Printed incident binders are kept at headquarters, the OCC, the BCC, the 3 field offices, and the pump station.

**Legal privilege protocol.** General Counsel engages outside counsel, and counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions, and do not speculate in writing. Operational and safety records (shift logs, pipeline and spill notices) are kept as normal business records and are never delayed for privilege.

## 1. Preparation checks (Identify / Protect)
- [x] Immutable cloud backups in the separate backup account, 35-day write-once retention, separate administrator credentials (CP-9)
- [x] EDR on corporate endpoints and servers with 24x7 MDR and authority to isolate IT hosts (SI-3, SI-4; P07 SI-3 fully satisfied)
- [x] OT DMZ at the OCC with 22 reviewed rules (SC-7); labeled physical disconnect points for the OCC DMZ firewall pair
- [ ] Physical disconnect points labeled at the BCC and South Florida site firewalls, with the procedure taped to the rack. **Due 2026-10-31**
- [ ] Second offline set of SCADA images and controller programs in the headquarters safe with no network path, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-004 closes**
- [ ] BCC failover tested within the last 12 months (CP-7). **Gap until POAM-005 closes**
- [ ] 24x7 OT alert coverage (SI-4). **Gap until POAM-009 closes**; after hours, the OCC shift lead calls the OT Security Engineer on any OT sensor alert
- [x] Break-glass accounts sealed and tested for the identity provider, the cloud organization, and the OCC SCADA servers (POL-02 4.9); BCC SCADA break-glass due 2026-12-31
- [x] Manual-operations route sheets, shut-in order by area, and NRC contact sheets in the binders
- [ ] Manual release estimate tables (LACT tickets, tank gauges, line pack) at the OCC, BCC, and pump station (POAM-020, due 2026-11-30)
- [x] Insurer panel counsel and an OT-capable forensic firm confirmed; contact list verified 2026-09-16 and checked quarterly

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption on a corporate endpoint or server | EDR alert; staff report | MDR isolates the host (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Credential dumping, remote execution tools, or new domain administrators | EDR; SIEM; privileged access management | Disable the account; declare if unexplained |
| Backup deletion attempts, or disabling of EDR or logging | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| Remote desktop or file-share traffic from corporate subnets toward the BCC or South Florida HMIs, the historian, or engineering workstations | Site firewall logs; OT sensors (OCC and Central Facility only) | Treat as spreading toward SCADA; go to section 3.1 |
| An HMI shows a ransom note, unfamiliar screens, or commands nobody issued; setpoints change | Production Controller (POL-03 4.2) | OCC shift lead calls the OT Security Engineer and the Security Manager at once and starts the isolation decision table |
| Historian replica stops updating, or cloud workloads encrypt | Cloud alerts; data platform users | VP IT checks the OT data account and the historian push |
| Extortion email or leak-site post naming the company | Email; FBI; threat intelligence; insurer | Declare; preserve the message |

**Severity 1 (declare immediately):** any confirmed ransomware execution, any sign of the attack on the SCADA network, or an extortion claim naming company data. The CMT convenes within 2 hours (POL-03 4.5).

**Record the date and time of discovery in the incident log** (POL-03 4.3). Florida's notice clocks run from the determination of a breach (Fla. Stat. 501.171(3) and (4)), and the Part 195 clocks run from confirmed discovery of an accident, so counsel and the Pipeline Compliance Manager need an exact timeline.

## 3. First 4 hours (RS.MA, RS.MI)
### 3.1 Isolation decision table
| Situation | Decision | Who decides |
|---|---|---|
| Ransomware on corporate IT only; no sign on the SCADA side | **Open the IT/OT connections now:** the OT DMZ at the OCC (historian push and jump host), the BCC site firewall, and the South Florida site firewall. Suspend the historian push to the cloud. SCADA keeps running on its own network | OT Security Engineer or SCADA and Automation Manager with the VP Operations; the OCC shift lead if neither is reachable within 15 minutes (POL-03 4.4) |
| Signs at the BCC or the South Florida HMIs, but the OCC looks normal | Open all IT/OT connections; also **cut the BCC and South Florida links to the OCC SCADA network**; run the fields from the OCC | Same |
| Signs on the OCC historian, an engineering workstation, or OCC HMIs, but the BCC is clean | Open all connections; disconnect affected OCC hosts; **decide on failover to the BCC** only if the SCADA and Automation Manager confirms the BCC is clean (failover is untested, POAM-005) | SCADA and Automation Manager with the VP Operations |
| SCADA servers or HMIs at both the OCC and the BCC affected, or Production Controllers cannot trust what they see | **Go to manual operations.** Field Superintendents start route coverage and the shut-in order; leave field controllers running on local logic; do not send commands from affected HMIs | VP Operations with the Field Superintendents |
| Any doubt about site safety | Shut in the affected site under the emergency response plan | Field Superintendent |

Field controllers run their own logic and the safety shutdowns are hardwired, so opening the IT/OT connections or losing SCADA does not stop the wells by itself. What stops is remote visibility and control. The BIA limits (P05) set the pace:
- **Alarm call-out (BP-01, MTD 4 hours):** start roving patrols of the sour-gas sites in the Panhandle and Alabama within the first hour.
- **Water handling (BP-02, MTD 8 hours):** plant operators take the 3 injection plants to local panel control within 4 hours.
- **Gathering system (BP-04, MTD 8 hours):** a station operator runs the pump station from its local panel within 2 hours, and line riders patrol the 14-mile regulated trunk line every 4 hours. If monitoring cannot be staffed by hour 8, the trunk line is shut down under the company pipeline procedure.
- **Well monitoring (BP-03, MTD 24 hours):** the 180 cellular sites, mostly in South Florida, are shut in after 24 hours without coverage.

### 3.2 First 4 hours
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected corporate hosts through EDR; keep them powered on for memory evidence | MDR provider; Security Analyst | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log with the discovery time | Incident commander | Log open |
| 0-30 min | Apply the isolation decision table; record the time each connection was opened | OT Security Engineer; OCC shift lead | Connections open; times logged |
| 0-60 min | Confirm the OCC can still see and control the fields; if not, start manual operations and patrols per section 3.1 | OCC shift lead; Field Superintendents | Routes assigned or SCADA confirmed healthy |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages the forensic firm | CFO, with General Counsel | Claim number; counsel on the call |
| 0-60 min | Protect backups: confirm write-once retention in the backup account; suspend cross-account backup jobs; rotate backup administrator credentials out of band; **disconnect the BCC image staging share** and confirm the removable image drives are in the safe | VP IT; SCADA and Automation Manager | Backup integrity confirmed |
| 0-2 h | Revoke all identity provider sessions; reset privileged credentials with break-glass accounts; disable all vendor accounts at the jump host | Security Manager; VP IT | Sessions revoked |
| 0-2 h | If gathering system monitoring is degraded: station operator to the pump station; line riders out; Pipeline Compliance Manager on the call | Control Room Manager; Pipeline Compliance Manager | Pump station staffed; patrol log started |
| 1-2 h | Convene the CMT; first situation report (scope, field status, safety, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing script: what happened, manual operations, do not use affected systems, do not discuss outside the company | HR Director with the COO | Script sent by text and read at field offices |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope.** Which corporate endpoints, servers, cloud accounts, identities, and OT assets are affected? Use EDR telemetry, identity provider sign-in logs, cloud control-plane logs in the write-once archive, SD-WAN and site firewall logs, and OT sensor data from the OCC and the Central Facility. Export SCADA event journals and HMI logs at once, because field office and BCC logs roll over after 30 days (POAM-015).
2. **Path toward SCADA.** Check the BCC and South Florida site firewalls for remote desktop and file-share connections from corporate subnets, the jump host session records, and the historian push. Check whether the BCC image staging share was touched.
3. **OT integrity.** The SCADA and Automation Manager compares controller programs at critical sites against the repository, starting with the gathering pump station, the 3 injection plants, the compression stations, and any site a compromised workstation could reach. The Pipeline Compliance Manager compares pump station setpoints with the MOP record. For the roughly 40% of controllers not yet in the repository, use the integrator's archive and field verification.
4. **Initial access and dwell time.** Identify the entry point (phishing, an exposed edge device, or a vendor path), the first compromised account, and when the attacker first got in.
5. **Preserve evidence.** Forensics images key hosts and collects HMI screenshots, SCADA event logs, controller program uploads, and firewall logs, with chain of custody (who collected, when, hash, storage). Evidence collection must never delay a safety or pipeline action.
6. **Personal information.** Determine whether royalty owner or employee data was accessed or taken: the production accounting tenant, HR and payroll, file shares, and the data platform (including the owner deck copy until POAM-013 closes). Check egress volume, archive tools, and leak-site samples. Build the **affected individuals list** by data element and state of residence. This drives every breach notice.
7. **Vendor status.** Confirm the production accounting vendor, identity provider, cloud provider, and MDR provider are unaffected. If a vendor is the source, also follow `ir-runbook-ot-remote-access.md`.

## 5. Containment and eradication (RS.MI)
1. Keep the IT/OT connections open until eradication is confirmed on both sides.
2. Block attacker infrastructure at the SD-WAN, the site firewalls, and the cloud firewall.
3. Disable compromised accounts. Rotate service credentials (volume integration service, historian push, measurement collector, shipper portal service accounts) and any SCADA local account or controller password used from corporate systems.
4. Rebuild affected corporate endpoints and servers from standard images. **Do not decrypt and reuse them.**
5. Rebuild any affected SCADA server, HMI, or engineering workstation from a verified offline image with the integrator, on wiped hardware. **Never run a decryptor on SCADA systems.** Reload controller programs only from verified copies.
6. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts) is removed on both the IT and OT sides before any reconnection.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every legal notice before it goes out, except safety and pipeline telephone notices, which are never delayed for review. General Counsel keeps the **decision log** below (POL-03 4.7; P03 G-117).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Did a cyber event cause or hide a release? If a release meets 49 CFR 195.52(a), call the National Response Center within 1 hour of confirmed discovery; if oil reached water, call immediately under 40 CFR 110.6 | Pipeline Compliance Manager (gathering system); HSE Director (any facility) | Pipeline and spill notice log with call times |
| D2 | Did pressure on the gathering system rise above 110% of MOP because of a malfunction or unauthorized change? If so, a safety-related condition report is due within 5 working days of determination (195.55(a)(4), 195.56) unless an exception applies | Pipeline Compliance Manager | Decision log |
| D3 | Was personal information accessed or acquired? Which states' laws apply? Is there a documented, counsel-supported basis for a Florida no-notice determination (written, kept 5 years, sent to the department within 30 days)? | General Counsel with outside counsel | Decision log with facts and reasons |
| D4 | Date of determination (Florida clock) and number affected: total, by state, and Florida residents (thresholds: 500 Florida residents for the Department of Legal Affairs; more than 1,000 notified at once for consumer reporting agencies) | General Counsel | Affected individuals list |
| D5 | Has law enforcement asked for a delay? Get the request in writing | General Counsel | Decision log |
| D6 | Which contract notices are due (shippers, transmission pipeline, purchasers, partners, bank group, sponsor)? | General Counsel and CFO | Contract register |
| D7 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Immediately, if oil reaches water | Oil discharge notice to the National Response Center (40 CFR 110.6); state notices per the emergency response plan | HSE Director |
| Within 1 hour of confirmed discovery, if a gathering line accident meets 195.52(a) | National Response Center telephone notice; revise or confirm within 48 hours (195.52(d)) | Pipeline Compliance Manager |
| Hour 0-1 | Insurer hotline; counsel engaged | CFO; General Counsel |
| Hour 0-2 | Operational call to the transmission pipeline control center if LACT deliveries stop | Control Room Manager |
| Day 0-1 | Voluntary report to CISA and the FBI through counsel; supports the OFAC mitigating factor and warns the sector | Security Manager |
| Within 24 hours of confirmed impact | Shippers told about any effect on volumes, statements, or the portal (company practice until the gathering agreements are amended) | Measurement Supervisor |
| Per contract | Purchasers, gas gathering companies, non-operating partners, bank group, sponsor | VP Operations; CFO |
| Within 5 working days of determination | Safety-related condition report, if D2 applies | Pipeline Compliance Manager |
| Within 30 days of determination | Florida individual notices (501.171(4)); Department of Legal Affairs notice if 500 or more Florida residents (501.171(3)); consumer reporting agencies if more than 1,000 are notified at once (501.171(5)) | General Counsel and outside counsel |
| Each other state | Owners and employees in other states: counsel applies each state's law using the affected list by state | General Counsel |
| Within 30 days after discovery | PHMSA accident report (Form 7000-1) for any accident meeting 195.50 (195.54) | Pipeline Compliance Manager |

**Ransom decision (POL-03 4.10).** Requires the CEO, General Counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove breach notification duties if data was taken, and does not guarantee deletion. A decryptor is never run on SCADA systems. The CEO's default position is not to pay while clean backups and offline images are intact.

**Communications.**
- Royalty owners: a website notice and a call-center script if owner payments will be late, with a hotline through the insurer's notification vendor if personal information is involved.
- Shippers and partners: a direct call from the Measurement Supervisor or the CFO, then written notice.
- Media and regulators: holding statement approved by General Counsel; no technical details, ransom, or attribution comments.
- Staff and field crews: daily briefings by text and field radio, using the out-of-band channel only.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 8). Each step is validated before the next begins: forensics sign-off for the segment, credentials rotated, and for OT, controller programs matched to verified copies.

| Order | Resource | Target (BIA) | Validation |
|---|---|---|---|
| 1 | Field safety call-out: HSE on-call phone tree, roving patrols, line riders | Immediate | Patrol logs running |
| 2 | Gathering pump station and injection plant controllers on local panels | 2 h (pump station), 4 h (plants) | Setpoints compared with the MOP record and permit limits |
| 3 | SCADA servers and OCC HMIs from a clean, verified image, or failover to the BCC if it is clean | 12 h (target; untested until POAM-004 and POAM-005 close) | Image hash verified; integrator and SCADA and Automation Manager sign-off |
| 4 | Field communications (radio, microwave, cellular private network) | 12 h | Polling restored area by area |
| 5 | Identity provider and break-glass accounts, in parallel with 2 to 4 | 4 h | Sessions revoked; privileged credentials rotated |
| 6 | LACT flow computers and the measurement data service | 24 h | Flow computer configuration compared with the approved record; paper tickets until then |
| 7 | Compression station controllers | 12 h | Local panel operation until verified |
| 8 | Field data capture app and tablets | 24 h | Paper run tickets until then |
| 9 | Shipper portal | 24 h | Statements reconciled to LACT tickets before publishing; email statements until then |
| 10 | Volume integration service and production accounting | 72 h | Volumes rebuilt from tickets and meter data |
| 11 | ERP, payroll, finance, telematics | 72 h | Manual payments with call-back verification |
| 12 | Data platform and ML workspace | 120 h | Restore; permissions review; no owner deck copy restored |

**Before reconnecting the IT/OT connections**, the SCADA and Automation Manager and the Security Manager must both confirm that corporate systems are clean, credentials are rotated, controller programs match verified copies, and the OT DMZ rules (or, until POAM-003 closes, the reduced interim rule sets at the BCC and South Florida) are in place. The VP Operations declares the return to normal remote operations, and the Pipeline Compliance Manager confirms the gathering system is back under monitoring before patrols stop. Back-enter manual run tickets and gauge readings within 72 hours. Tell field crews, shippers, purchasers, and partners when normal operations resume (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the OCC, all 3 areas, the integrator, and the MDR provider; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-002, R-003, R-011, R-014, R-028, R-029), the POA&M (P07), the contingency plan, the pipeline emergency procedures, and this runbook.
- If the CMT activated the emergency response plan or the pipeline emergency procedures, record the joint after-action review with the HSE Director and the Pipeline Compliance Manager.
- Retain incident records, the decision log, and copies of every notice for at least 6 years (POL-01 4.14), and gathering system accident records as Part 195 requires.

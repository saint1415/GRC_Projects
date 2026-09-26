# Incident Response Runbook: Ransomware Spreading from Business IT toward Field SCADA

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer) |
| Tier / Vertical | Small / Mining, Quarrying, and Oil and Gas Extraction |
| Incident type | Ransomware that starts in business IT (credential phishing to the corporate network) and spreads toward the SCADA network through the IT/OT firewall and the dual-homed engineering workstation |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 (sections 3.3.8, 6.4, 6.5) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager, with the SCADA and Automation Supervisor for OT steps |
| Approved | 2026-08-31 by the CFO and the VP Operations |
| Last tested | Not yet. First joint tabletop due 2026-11-30 (POAM-012) |

**The one rule that overrides everything below:** safety first. The hardwired safety shutdowns (H2S detection, tank high-level, compressor emergency shutdown) do not depend on SCADA. Never disable, bypass, or reset them as part of incident response. If anyone is unsure whether a site is safe, the Field Superintendent shuts it in under the emergency response plan.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | CFO | Incident line (cell), then the out-of-band group text on company phones |
| OT lead | SCADA and Automation Supervisor | Senior automation technician | Cell; OCC landline |
| Operations decisions (manual operations, shut-ins) | VP Operations | Field Superintendents (Panhandle, South Florida) | Cell; field radio |
| OCC | OCC shift lead (Production Controller) | Second Production Controller on shift | OCC landline |
| Environmental and safety reporting | HSE and Regulatory Manager | HSE on-call | HSE on-call binder |
| Technical response | MDR service (once contracted, POAM-009); SCADA integrator | OT-capable forensic firm through the insurer's panel | MDR 24x7 line; integrator emergency number |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Communications | CFO | Outside PR (via counsel) | Cell |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume corporate email, chat, and the identity provider are compromised. Coordinate by company cell phones, the OCC landline, field radio, and the printed contact list in the incident binder at the OCC, both field offices, and headquarters.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at the OCC, both field offices, and headquarters: this runbook, contacts, the isolation decision table (section 3), the notification matrix, and the manual-operations route sheets
- [ ] Offline copy of SCADA server images and controller programs at the South Florida field office, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-003 and POAM-004 close**
- [ ] 24x7 monitoring of corporate EDR (SI-4). **Gap until POAM-009 closes**
- [ ] Integrator remote access tool removed; jump host in place (AC-17). **Gap until POAM-001 closes**
- [ ] Break-glass accounts sealed and tested: 2 for the identity provider and cloud, 1 for SCADA (POL-02 4.8)
- [ ] Physical disconnect point for the IT/OT link labeled in the OCC server room, with the procedure taped to the rack
- [ ] OT-capable forensic firm confirmed on the insurer panel (POAM-012)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or files renamed with an unknown extension, on a corporate computer or server | Staff report, EDR alert | Call the incident line. **Do not power off.** Unplug the network cable or turn off Wi-Fi |
| EDR detects credential dumping, remote execution tools, or mass file changes on corporate servers | EDR, MDR service | IT Manager opens the incident and calls the SCADA and Automation Supervisor |
| Unusual remote desktop or file-share traffic from corporate subnets toward HMIs, the historian, or the engineering workstations | IT/OT firewall log, OT monitoring (when live) | Treat as spreading toward SCADA; go to section 3 |
| HMI shows unfamiliar screens, a ransom note, commands the controller did not issue, or setpoints changing | Production Controller | OCC shift lead calls the SCADA and Automation Supervisor and the IT Manager at once (POL-03 4.2) |
| Historian replica stops updating or cloud workloads encrypt | Cloud alerts, data platform users | IT Manager checks the cloud tenant and the VPN |
| Extortion email or leak-site post naming the company | Email, law enforcement, insurer | Declare the incident; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any system, or an extortion claim names company data.
**Declare an OT incident as well when** any sign of the attack is seen on the SCADA network, an HMI, the historian, or an engineering workstation.
**Record the time of discovery.** Florida breach deadlines run from the determination of a breach (Fla. Stat. 501.171(3) and (4)), and counsel will need the timeline.

## 3. First hour (RS.MA, RS.MI)
### 3.1 Isolation decision table
| Situation | Decision | Who decides |
|---|---|---|
| Ransomware on corporate IT only; no sign on the SCADA side | **Open the IT/OT link now** (physical disconnect at the OCC) and disable the cloud VPN tunnel. SCADA keeps running in island mode | IT Manager with the VP Operations; OCC shift lead if neither is reachable within 15 minutes (POL-03 4.4) |
| Signs on the historian or an engineering workstation, but HMIs and SCADA servers look normal | Open the IT/OT link; unplug the affected workstation or historian from the SCADA network; SCADA keeps running | Same |
| HMIs or SCADA servers affected, or Production Controllers cannot trust what they see | **Go to manual operations.** Field Superintendents start route coverage and the shut-in order; leave field controllers running on their local logic; do not send commands from affected HMIs | VP Operations with the Field Superintendents |
| Any doubt about site safety | Shut in the affected site under the emergency response plan | Field Superintendent |

Controllers in the field run their own logic and the safety shutdowns are hardwired, so opening the IT/OT link or losing SCADA does not stop the wells by itself. What stops is remote visibility (BP-03 in P05, MTD 24 hours) and remote alarm call-out (BP-01, MTD 4 hours). Start roving patrols of the Panhandle sour-gas sites within the first hour if SCADA visibility is lost.

### 3.2 First-hour steps
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected corporate endpoints (cable out, Wi-Fi off). Leave them powered on for memory evidence | Staff with IT on the phone | Devices offline |
| 2. Apply the isolation decision table; open the IT/OT link and disable the cloud VPN tunnel | IT Manager, SCADA and Automation Supervisor | Link open; tunnel down; time recorded |
| 3. Confirm the OCC can still see and control the fields; if not, start manual operations | OCC shift lead, Field Superintendents | Routes assigned or SCADA confirmed healthy |
| 4. Call the cyber insurer's breach hotline. Engage counsel and forensics through the insurer | CFO | Claim number issued |
| 5. Revoke all identity provider sessions; reset administrator credentials using break-glass accounts; disable the integrator account | IT Manager | Sessions revoked |
| 6. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** which corporate endpoints, servers, cloud workloads, accounts, and OT assets are affected? Use EDR, identity provider sign-in logs, cloud audit logs, and IT/OT firewall logs. Export logs at once: firewall logs roll over after 7 days and identity provider logs after 30 (POAM-017).
2. **Path toward SCADA:** check the IT/OT firewall for remote desktop or file-share connections to HMIs, the historian, and the engineering workstations, and check the dual-homed workstation. Check the integrator's remote access tool logs.
3. **OT integrity:** the SCADA and Automation Supervisor compares controller programs at critical sites (injection plant, tank batteries, compression stations) against the last known good copies, starting with any site a compromised workstation could reach. Until the program repository exists (POAM-007), use the offline copies and the integrator's archive.
4. **Preserve evidence:** forensics images affected hosts and collects HMI screenshots, SCADA event logs, and controller program uploads. Maintain chain of custody. Evidence collection must never delay a safety action.
5. **Personal information:** determine whether royalty owner or employee data was accessed or taken (production accounting exports, the shared file area, HR files). Check file access logs and firewall egress. **This drives the Florida breach determination.**
6. **Backups:** confirm the offline SCADA copy and the cloud backups are intact before any restoration.

## 5. Containment and eradication (RS.MI)
1. Keep the IT/OT link open until eradication is confirmed on both sides.
2. Block attacker infrastructure (IPs, domains) at the office firewalls and in the cloud network rules.
3. Disable compromised accounts. Rotate service credentials (volume integration token, historian replica, SCADA local accounts that were used from corporate systems).
4. Rebuild affected corporate endpoints and servers from the standard image. **Do not decrypt and reuse them.**
5. Rebuild any affected SCADA server, HMI, or engineering workstation from the offline image with the integrator, on hardware that has been wiped. Reload controller programs only from verified copies.
6. Confirm with forensics that persistence mechanisms are removed on both the IT and OT sides before any reconnection.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Legal counsel confirms every legal notice before it goes out. No binding federal cyber incident reporting rule applies to the company (P03 section 1); the clocks below come from state law, environmental law, and contracts.

| When | Action | Owner |
|---|---|---|
| Immediately, if any oil reaches water | Oil discharge notice to the National Response Center (40 CFR 110.6); the HSE and Regulatory Manager also makes any state notices required by the emergency response plan | HSE and Regulatory Manager |
| Day 0 | Insurer notified; counsel engaged | CFO |
| Day 0-1 | Voluntary report to CISA and the FBI. Supports OFAC mitigation if payment is considered, and warns the sector | IT Manager |
| Day 0-1 | Crude purchaser and gas gathering company told about any delivery disruption (contract notices) | VP Operations |
| Day 0-5 | Staff briefing script: what happened, manual operations, do not discuss outside the company | CFO |
| As soon as known | Breach determination for royalty owner and employee personal information, documented with counsel | CFO |
| Within 30 days of determination | Florida individual notices (501.171(4)); Department of Legal Affairs notice if 500 or more Florida residents (501.171(3)); consumer reporting agencies if more than 1,000 (501.171(5)); other states' notices for owners and employees who live elsewhere | CFO and counsel |
| Per contract | Lender, non-operating partners (joint operating agreements) | CFO |

**Ransom decision:** requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove breach notification duties if data was taken, and a decryptor must never be run on SCADA systems; they are rebuilt from clean images.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Field safety call-out: HSE on-call phone tree and roving patrols (immediate)
2. Injection plant and SWD controllers on local panels (4 h)
3. SCADA servers and OCC HMIs from the verified offline image (12 h target; untested until POAM-004 closes)
4. Field communications (radio and cellular modems) (12 h)
5. Compression station controllers (12 h)
6. Identity provider and break-glass accounts (4 h), in parallel with steps 2-5
7. Field data capture app and tablets (24 h; paper run tickets until then)
8. Volume integration service and production accounting (72 h)
9. ERP, payroll, finance (72 h)
10. Data platform and ML workspace (120 h)

**Validate before reconnecting the IT/OT link:** the SCADA and Automation Supervisor and the IT Manager must both confirm that corporate systems are clean, credentials are rotated, controller programs match verified copies, and the OT DMZ rules (or, until POAM-002 closes, a reduced interim rule set) are in place. The VP Operations declares return to normal remote operations. Tell field crews, the purchaser, and partners when normal operations resume (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, including the OCC, field operations, and the integrator (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-003, R-026), the POA&M (P07), the contingency plan, and this runbook.
- Retain incident documentation per POL-01 4.12.

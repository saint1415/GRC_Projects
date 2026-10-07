# Incident Response Runbook: Ransomware on Building Automation Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial office and retail property owner-operator) |
| Tier / Vertical | Mid-Market / Commercial Facilities |
| Incident type | Ransomware on the building automation systems (BAS), entering through BAS Integrator B's always-on remote-support tool at a Platform B property, with possible spread across flat property networks to other Platform B sites, the SD-WAN, corporate systems, security console PCs, and the Platform A server |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions, with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-access-platform.md` (access control and video platform compromise or outage); `notification-matrix.csv`; BIA (P05); tower degraded-mode procedures; hurricane plan |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. OT ransomware tabletop with all 14 chief engineers, the executive team, and outside counsel on 2026-11-19 (POAM-011) |

**Safety comes first.** The company's product is safe, secure, cooled space. In this incident the buildings keep running on their own for a while: BAS field controllers keep their last programs and schedules, door controllers cache credentials for up to 72 hours, and life-safety systems (fire alarm, elevators, emergency voice) are on separate networks, with egress door releases hardwired to the fire alarm. **Nothing in this runbook touches life-safety systems.**

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, building, and business and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, IT Director, VP of Engineering, Director of Security Operations, VP of Property Management, Director of Marketing and Communications, HR Director, outside breach counsel | Business continuity, property closures or restricted hours, external statements, tenant and JV communication, ransom recommendation to the CEO, spending |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director (recovery lead), security analysts (including the OT analyst), GRC Analyst (log keeper), MSSP, forensic firm with OT experience (through counsel), BAS Integrator A, a clean Integrator B technician (verified by call-back) | Containment, investigation, eradication, recovery sequence |
| **Building operations command** | OT safety lead: VP of Engineering. Building Technology Manager, the 14 chief engineers, Director of Security Operations, SCC shift lead | Local hand control, manual rounds, door modes, officer posts, portable cooling, what may be touched on OT devices |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on company phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| OT safety lead | Vice President of Engineering | Building Technology Manager | Cell; engineering radio at each property |
| Physical security lead | Director of Security Operations | SCC shift lead | SCC (24x7) |
| Breach and notice decisions | General Counsel | Outside breach counsel | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | Company's outside corporate counsel | Insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($10 million limit, $250,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm with OT experience, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response (IT) | MSSP 24x7 security operations center | n/a | MSSP hotline |
| BAS vendor support | BAS Integrator A; a clean Integrator B technician confirmed by call-back to a known number | Equipment manufacturers' service lines | Numbers in the binder, **never** from email |
| Communications | Director of Marketing and Communications | Outside crisis communications firm (through counsel) | Out-of-band group |
| Board, PE sponsor, JV partner | CEO informs the audit committee chair and the sponsor's operating partner; CFO informs the JV partner | COO | Phone |
| Law enforcement and government | FBI field office or IC3; CISA | n/a | Numbers in the binder |

**Out-of-band first.** Assume email, chat, the SIEM console, and the integrators' own systems may be compromised. The CMT and IRT use a pre-provisioned messaging group on company phones; building operations use engineering radios and the printed binders at each property.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in email or chat.

## 1. Preparation checks (Identify / Protect)
- [x] OT zones with deny-by-default rules at Towers 1-4 (SC-7). **Tower 1 any-any rule found in P07; removal due 2026-09-30 (POAM-004)**
- [x] Write-once backups of the Platform A server and historian in the separate backup account (CP-9)
- [x] EDR with 24x7 MSSP on console PCs, the Platform A server, and corporate endpoints (SI-3)
- [ ] Integrator B off its always-on tool and onto the gateway (AC-17, MA-4). **Gap until POAM-003 closes (2026-11-30)**
- [ ] Platform B server images and controller program copies, with a restore test in the last 90 days (CP-9, CP-4). **Gap until POAM-010 closes**
- [ ] OT zones at Mixed-Use 1-2, Parks 1-2, and Retail 1-6 (SC-7). **Gap until POAM-004 closes (2027-06-30)**
- [ ] Degraded-mode procedures at every property (CP-2). **Towers 1-4 only until POAM-009 closes (2026-12-31)**
- [ ] Incident binder at each property and the SCC: this runbook, call tree, notification matrix, printed tenant contacts, degraded-mode procedures. **Due 2026-10-31 (POAM-011)**
- [x] Insurer panel counsel and OT-capable forensics confirmed; contact list verified 2026-09-15
- [ ] Two break-glass accounts per administration plane tested quarterly (POL-02 4.8). **First test 2026-10-15**
- [ ] Spare pre-imaged engineering laptops at every property (P05). **Due 2026-12-31 (POAM-009)**

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note or unreadable graphics on a BAS server or engineering workstation | Chief engineer or engineering staff | Call the incident line and the OT safety lead. **Do not power off** the server. Unplug the workstation's network cable |
| BAS shows setpoints, schedules, or equipment states nobody changed; alarms stop arriving at the SCC | Chief engineer; SCC | Check equipment locally; if confirmed, treat as a BAS compromise and declare |
| A remote-support session nobody approved | Chief engineer; gateway alert | Call the integrator on a known number; if not confirmed, disconnect the server's network and declare |
| Many files changing at once, or backup deletion attempts | EDR alert (MSSP 24x7); cloud audit logs; backup job failure | MSSP isolates the host; incident commander declares |
| Door controllers or NVRs offline across a property; unexplained door unlocks | SCC; platform alerts | Physical security lead posts officers; see also `ir-runbook-access-platform.md` |
| Extortion email or leak-site post naming the company or a tenant | Email; insurer threat intelligence; law enforcement | Declare; preserve the message |

**Severity 1 (declare immediately):** confirmed ransomware execution on any system, loss of supervisory control at a property because of malicious activity, or an extortion claim naming company or tenant data. Severity 1 activates the CMT within 2 hours (POL-03 4.4).

**Record two times in the incident log** (POL-03 4.3, 4.6): when the incident was **discovered**, and later when the General Counsel **determines** that a breach of personal information occurred or that there is reason to believe one occurred. The Florida 30-day clocks run from the determination (Fla. Stat. 501.171(3)(a), (4)(a)). Plan from discovery anyway: the 72-hour lease clauses may run from discovery (counsel to confirm per lease).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | **Make the buildings safe.** Chief engineers at affected properties check chillers, rooftop units, air handlers, and tenant data rooms locally; switch to local hand control where the BAS is not trusted; start hourly rounds; set site lighting to photocell override | OT safety lead and chief engineers | Each property reports equipment status to building operations command |
| 0-30 min | **Cut the entry path.** Block all traffic to and from the affected Platform B servers at the property firewall; stop the remote-support tool service; leave servers powered on for memory evidence | IT Director with the MSSP | No traffic to or from the servers |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log and chain-of-custody form | Incident commander; GRC Analyst | Log open |
| 0-1 h | **Stop spread across the portfolio.** Disconnect the SD-WAN tunnels of Parks 1-2 and Retail 1-6 from the hub; at Towers 1-4 and Mixed-Use 1-2, block OT conduits except the access control and video cloud connections; block the gateway for all integrators except a named, approved session | IT Director | Tunnels down; conduits restricted |
| 0-1 h | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages OT-capable forensics | Chief Operating Officer | Claim number; counsel on the call |
| 0-1 h | **Protect backups.** Confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | **Secure the doors.** Confirm door controllers work on cached credentials; set perimeter doors to scheduled lock; post officers at main entrances with printed tenant lists | Physical security lead | Entrances staffed; door status confirmed at each property |
| 0-2 h | Revoke all identity provider sessions; reset privileged credentials with break-glass accounts; disable Integrator B accounts and the shared site accounts | Security Manager | Sessions revoked |
| 1-2 h | Convene the CMT; first situation report (affected properties, occupant impact, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Tenant service notice for properties with degraded building services (lease service interruption clauses): what is affected, what to expect, who to call. Approved by counsel; sent through the tenant app and email, or the phone tree if those are affected | VP of Property Management | Notices sent |
| 2-4 h | Staff briefing script: what happened, manual procedures, do not discuss externally, send media calls to Communications | Director of Marketing and Communications with HR | Script sent by text and radio |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

**Do not** power off, reset, reload, or factory-default field controllers, door controllers, or NVRs. That can erase evidence and the only copy of a program (POL-03 4.5). Any action on an OT device needs the OT safety lead's approval.

## 4. Analysis (RS.AN)
1. **Scope.** Which systems are affected: Platform B servers and workstations, the Platform A server, console PCs, corporate endpoints, cloud workloads (historian, file storage, data warehouse), the backup account? Use EDR telemetry, firewall and SD-WAN logs, identity provider sign-ins, cloud audit logs in the locked bucket, and the gateway logs.
2. **Field devices.** With a clean integrator technician, compare controller programs at a sample of devices at each affected property against the last known-good copies (where they exist). Look for changed setpoints, disabled alarms, or new logic. Until POAM-010 closes, many Platform B programs exist only at Integrator B, so treat its copies as untrusted until the integrator proves its own environment is clean.
3. **Initial access and dwell time.** Confirm the path: Integrator B's shared credentials on its tool, a compromise at the integrator itself, or another route. **Ask Integrator B whether other customers are affected.** If the integrator is compromised, treat all of its access and media as hostile.
4. **Preserve evidence.** Forensics images the affected servers and exports logs before they roll over (Platform B servers keep only local logs, which roll over within days; firewall and identity logs are already in the SIEM and the locked bucket). Chain of custody: who collected, when, hash, storage. Evidence is held by the forensic firm under counsel.
5. **Personal information.** Determine whether the attacker reached any system holding personal information: visitor ID scans (SYS-11, through a console PC session), HR and payroll (SYS-12), access control credential records and access history (SYS-02 portal from a console PC), tenant contact and bank data (SYS-07), or corporate files in cloud storage. Look for archive tools, staging directories, and large outbound transfers. **This drives the breach determination (section 6).**
6. **Backups.** Confirm the backup vault and the Platform A image are intact and predate the attacker's first access before any restore.
7. **Life-safety check.** The OT safety lead confirms with the fire alarm and elevator vendors that their systems show no anomalies and that the relay points are intact. Record the confirmation.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at all 14 property firewalls, the SD-WAN, and the cloud firewall.
2. Uninstall the remote-support tool from every Platform B server permanently. Integrator B access resumes only through the remote access gateway (POL-02 4.9).
3. Rotate all OT local passwords, the gateway and identity provider administrator credentials, service accounts, and the historian connection credentials. Change any remaining default passwords.
4. Rebuild engineering workstations and console PCs from the standard image. **Do not decrypt and reuse them.**
5. Rebuild BAS servers from clean installation media and verified backups, not from an image that may contain the attacker's tools. Platform B servers are rebuilt on the upgraded platform if the hardware is ready (POAM-015); otherwise on clean, isolated replacements.
6. Reload any field controller whose program was changed, from a copy verified by the OT safety lead and a clean integrator technician.
7. Forensics confirms that persistence is removed before any system reconnects to an OT network or the SD-WAN.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every legal notice before it goes out. The General Counsel keeps the **decision log** (POL-03 4.6).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Did the attacker access personal information of Florida residents (or others)? Ransomware that stays on BAS servers encrypts operational data and drawings, which are not personal information under Fla. Stat. 501.171(1)(g). Visitor ID numbers, employee Social Security numbers, account numbers with access codes, user names with passwords, and biometric data are. Whether badge access history or plate reads count as "information regarding an individual's geolocation" is for counsel | General Counsel with outside counsel | Decision log with the analysis |
| D2 | Date of discovery and **date of determination** (Florida clocks); start time for each lease clock | General Counsel | Decision log |
| D3 | How many affected individuals, by state; 500 or more Florida residents (Department of Legal Affairs); more than 1,000 at one time (consumer reporting agencies) | General Counsel | Affected individuals list |
| D4 | Has law enforcement asked in writing for a delay of individual notice (501.171(4)(b))? | Outside counsel | Written request on file |
| D5 | Is a written no-harm determination supportable after investigation and consultation with law enforcement (501.171(4)(c))? If so, send it to the department within 30 days and keep it 5 years | General Counsel with outside counsel | Written determination |
| D6 | Contract notices due: 31 tenants with 72-hour clauses, other 2024-template tenants, the JV partner (2 business days), lenders, the acquirer (only if card data or terminals are involved) | General Counsel and CFO | Tenant notice register; contract register |
| D7 | Ransom decision | CEO, on CMT recommendation | See below |
| D8 | CIRCIA: is the final rule in effect at the time of the incident? If yes, the 72-hour covered incident report and 24-hour ransom payment report apply | General Counsel | Decision log |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | COO |
| Hour 0-4 | Tenant service interruption notices for degraded properties | VP of Property Management |
| Within 24 hours of declaration | Voluntary report to CISA and the FBI (POL-03 4.10; CPG 5.B). It may bring technical help and is a mitigating factor if a payment is ever considered (OFAC advisory) | Security Manager through counsel |
| Within 2 business days | JV partner notice if Tower 3, Tower 4, Retail 5, or Mixed-Use 2 is affected (management agreement) | CFO |
| Within 72 hours of discovery (plan) | If tenant employee data in the access control system may have been accessed: notice to the 31 tenants with 72-hour clauses; prompt notice to other tenants on the 2024 template | General Counsel and Property Managers |
| As soon as scoped | Breach determination documented (D1, D2) | General Counsel |
| Within 30 days of determination | Notice to affected Florida residents by mail or email with the content in 501.171(4)(e); notice to the Department of Legal Affairs if 500 or more Florida residents (501.171(3)); a 15-day extension of the individual notice deadline is possible only with good cause given to the department in writing within the 30 days | General Counsel with counsel |
| Without unreasonable delay | Consumer reporting agencies if notice goes to more than 1,000 individuals at a single time (501.171(5)) | Outside counsel |
| Each other state | Residents of other states (visitors and some tenant employees live elsewhere): apply each state's law | Outside counsel |
| Before any ransom payment | OFAC sanctions check; law enforcement report | Counsel |

**Ransom decision (POL-03 4.9).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove notice duties if data was taken, does not guarantee deletion, and does not restore controller programs that were changed. The default position, approved by the CEO, is not to pay while Platform A backups are intact and Platform B can be rebuilt by the integrators.

**Communications.**
- Tenants: service notices within 4 hours; a daily update while any property is degraded; a direct call from the Property Manager to each tenant with a 72-hour clause.
- JV partner and lenders: a call from the CFO, followed by written notice per the agreements.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments.
- Staff: briefings by radio and text twice a day; the out-of-band channel only.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7). Each step is validated before the next: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 2 | SD-WAN, property firewalls, and OT zone rules (rebuilt deny-by-default before any OT device reconnects) | 2 h | Rule review by the IT Director and the OT analyst |
| 3 | Access control administration from clean console PCs | 2 h | Door schedules and administrator list re-verified |
| 4 | Tenant notification channels | 2 h | Test notice delivered |
| 5 | SCC console PCs and video | 4 h | Video and alarm feeds from all properties |
| 6 | Clean engineering workstations and tablets | 4 h | Pre-imaged spares; EDR healthy |
| 7 | Platform A enterprise BAS server | 8 h | Restore from a pre-compromise backup; reconnect one property at a time; chief engineer checks each plant system before leaving hand control |
| 8 | Platform B site servers | 12 h target (no backups today; integrator rebuild took 3 to 6 days in 2025) | Clean rebuild; programs verified; one property at a time |
| 9 | Historian, energy analytics, data warehouse | 120 h | Restore; reconcile trend gaps |

Keep manual rounds going until each property has run 24 hours under BAS control without unexplained alarms. Tell tenants when services are back to normal (RC.CO). If any property remains untenantable for 3 consecutive business days (office) or 5 (retail), the CFO and General Counsel prepare for abatement claims (P05).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with both integrators; written report within 30 days (POL-03 4.13).
- Update the risk register (P01: R-001, R-002, R-004, R-029, R-050), the POA&M (P07), the degraded-mode procedures, and this runbook.
- Review the Integrator B relationship: contract terms, remote access, whether the security addendum was met, and whether a second integrator should be qualified.
- Retain incident records, evidence logs, the decision log, and any written no-harm determination for at least 5 years (POL-01 4.14).

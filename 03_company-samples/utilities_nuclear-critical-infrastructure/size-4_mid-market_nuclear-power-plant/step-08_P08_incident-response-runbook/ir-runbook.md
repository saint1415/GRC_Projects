# Incident Response Runbook: Business Network Attack with Attempted Pivot to Digital Assets

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed owner and operator of a single-unit nuclear generating station) |
| Tier / Vertical | Mid-Market / Nuclear Reactors, Materials, and Waste |
| Incident type | Cyber attack on the plant business network (phished credentials, then hands-on-keyboard activity, possibly ransomware) with an attempted pivot toward Level 3 and Level 4 digital assets through the receive server, vendor paths, or portable media |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions; CSP incident response procedures for anything in 73.54 scope |
| Policy basis | POL-03 Incident Response Policy (statements 4.4 to 4.6 are the hinge points) |
| Companion documents | `ir-runbook-insider-information-compromise.md`; `notification-matrix.csv`; BIA (P05); CSP incident response procedure (SRI); NERC low-impact Cyber Security Incident response plan |
| Runbook owner | IT Security Manager (incident commander), with the Cyber Security Program Manager for every CSP step |
| Approved | 2026-09-17 by the Site Vice President |
| Last tested | Not yet. Joint tabletop with IT, the CST, 2 Shift Managers, the MSSP, and outside counsel scheduled 2026-11-05 (POAM-012) |

## 0. Governance, roles, and contacts (Govern)
Three teams, so that plant safety, technical response, and business and legal decisions each have one clear owner.

| Team | Members | Decides |
|---|---|---|
| **Plant and regulatory command** | Shift Manager (in charge), Cyber Security Program Manager or CST on-call, Regulatory Affairs Manager, Director of Security | Whether anything in 73.54 scope is affected; every NRC notification (73.77, 50.72); isolating the one-way device feed; plant operating decisions. **Plant safety decisions are never delegated to IT** |
| **Incident response team (IRT)** | Incident commander: IT Security Manager. IT Director (recovery lead), security analysts, MSSP, forensic firm (through counsel), WMS and cloud vendor contacts | Containment, investigation, eradication, and recovery of the business network and cloud |
| **Crisis management team (CMT)** | Chair: Site Vice President. CEO, CFO, General Counsel, Plant General Manager, vCISO, Director of Security, Communications Director, HR Director, Outage Manager (during an outage), outside breach counsel | Business continuity, outage schedule, external statements, ransom recommendation to the CEO, resources |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| 73.77 decision and ENS | Shift Manager on duty | Shift Manager on call | Control room direct line (printed in the incident binder) |
| CSP technical lead | Cyber Security Program Manager | CST on-call engineer | CST on-call phone |
| CMT chair | Site Vice President | Plant General Manager | Out-of-band group |
| Legal and notifications | General Counsel | Outside breach counsel (insurer panel) | Out-of-band group |
| Cyber insurer | Carrier breach hotline ($25M limit, $1M retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| NERC low-impact plan | Compliance and GRC Lead | Site Vice President (CIP Senior Manager) | Phone |
| Balancing Authority | Dispatch desk | Shift Manager | Recorded line |
| Communications | Communications Director | Outside crisis PR (through counsel) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | Site Vice President | Phone |

**Out-of-band first.** Assume email, chat, and VoIP on the business network are compromised. Use the pre-provisioned messaging group on personal phones, plant radios, and printed call trees kept in the control room, the work control center, the outage control center, the TSC, and the EOF.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from conclusions. **Privilege never delays an NRC notification**; the Shift Manager reports facts as required.

## 1. Preparation checks (Identify / Protect)
- [x] One-way deterministic device from Level 3 to Level 2; no remote access to Level 4 (CSP)
- [x] Immutable backups in the separate cloud recovery account, 35-day write-once retention (CP-9; P07 fully satisfied)
- [x] EDR on all managed endpoints and servers with 24x7 MSSP (SI-3; P07 fully satisfied)
- [x] PMMD kiosks in service (MP-7; P07 fully satisfied)
- [ ] Receive server management interface re-homed to a management VLAN (POAM-011). **Disconnected since 2026-08-14**
- [ ] Alerting on attempts to reach boundary addresses (POAM-005). **Gap until 2026-11-15**
- [ ] WMS and CAP/EDMS failover tested (POAM-010). **Gap until 2026-11-14**
- [ ] Paper CAP intake forms at the CAP coordinator desk and the control room (POAM-010). **Gap until 2026-11-30**
- [ ] Vendor VPN accounts named and per-session (POAM-003). **Gap until 2026-11-30**
- [x] Incident binder in the control room, work control center, TSC, and EOF: this runbook, the call tree, `notification-matrix.csv`, the Shift Manager 73.77 decision aid, downtime procedures
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-17
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-20)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| EDR alert for credential theft, remote tools, or lateral movement | MSSP | MSSP isolates the host and calls the incident commander within 30 minutes |
| Any connection attempt from Level 2 or the cloud toward boundary addresses or the receive server | SIEM boundary use case (from 2026-11-15); firewall logs | **Call the CST on-call and the Shift Manager immediately (POL-03 4.4)** |
| Vendor VPN session nobody approved, or vendor activity outside a ticket | VPN logs; system owner | Disable the vendor account; call the incident commander; if the vendor also supports CDAs, call the CST |
| Unexpected change on the receive server, the historian replica, or PMMD kiosks | CST; file integrity alert | **CST leads under the CSP**; IRT supports |
| Ransom note, mass encryption, or deletion attempts on backups | EDR; cloud audit logs | Declare severity 1 |
| Scanning or reconnaissance aimed at Station addresses reported by the MSSP or threat intelligence | MSSP threat report | **Send to the CST the same day (possible 73.77(a)(3), 8-hour clock)** |
| Dispatch telemetry anomalies or RTU vendor path alerts | Dispatch desk; dispatch network sensor | Call the Compliance and GRC Lead (NERC plan) and the Shift Manager |

**Severity 1 (declare immediately):** confirmed ransomware execution; confirmed hands-on-keyboard attacker with administrator rights; any attempt to reach boundary addresses, the receive server, or a vendor path that also serves CDAs; or any event the CST says may touch 73.54 scope.

**Record the date and time of discovery** in the incident log when it is opened (POL-03 4.3). The 73.77 clocks run from discovery, and the 73.77(a)(2)(iii) clock runs from any report to another agency.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-15 min | Declare severity 1; open the out-of-band channel; start the incident log with the discovery time | Incident commander | Log open |
| 0-30 min | **Brief the Shift Manager and the CST on-call** using the decision aid facts: what was seen, where, when discovered, whether boundary addresses, vendor paths to CDAs, PMMD, or an insider are involved | Incident commander | Shift Manager acknowledges; decision point D1 opened |
| 0-60 min | **CST checks the CSP side:** one-way device health and logs, receive server integrity, PMMD kiosk logs, CDA vendor access status, Level 3 monitoring. CST decides whether to stop the one-way device feed (this does not affect Level 3 operation; data backfills later) | CST | CST statement to the Shift Manager |
| 0-60 min | Call the cyber insurer hotline before engaging vendors; counsel assigned; counsel engages forensics | CFO | Claim number; counsel on the call |
| 0-60 min | Protect the recovery account: confirm write-once retention; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Cut attacker paths: block attacker infrastructure; disable all vendor VPN accounts; sever the site-to-cloud VPN if cloud workloads are involved; revoke identity provider sessions; reset privileged credentials with break-glass accounts | IT Director; IT Security Manager | Paths cut |
| 0-2 h | **Plant downtime procedures as needed:** paper clearances (BP-02), paper RWPs (BP-06), paper narrative log (BP-01), printed call tree for the ERO (BP-08), phone telemetry with the Balancing Authority if the dispatch desk is affected (BP-10) | Plant General Manager; Director of Work Management; Radiation Protection Manager | Downtime procedures running |
| 0-4 h | **Shift Manager makes the 73.77 decision** (D1). If reportable under (a)(2)(i), the ENS call is due within 4 hours of discovery; under (a)(1), within 1 hour | Shift Manager | ENS call made, or "not reportable" documented with the basis |
| 1-2 h | Convene the CMT; first situation report | Site Vice President | CMT meeting held |
| 2-4 h | Staff and contractor briefing script (by text, radio, and postings): what happened, downtime steps, **no USB drives or laptops near plant equipment**, do not discuss externally | Communications Director with HR | Script delivered |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |
| Within 24 h | CAP entry for the event and any cyber security program weakness found (73.77(b)); paper CAP form if CAP is down | Regulatory Affairs Manager | CAP number recorded |

**If the event happens during a refueling outage:** the Outage Manager joins the CMT at once. Clearance and RWP downtime procedures start in the first hour, because those processes have 8 and 12 hour MTDs and the outage costs about $2.03 million per day (P05).

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, servers, cloud accounts, and identities are affected? Use EDR telemetry, identity provider sign-in logs, cloud control-plane logs from the locked bucket, VPN logs, and firewall flow logs.
2. **Initial access and dwell time.** Find the entry point (phishing, an edge appliance vulnerability, or a vendor account), the first compromised account, and the first date of access.
3. **Pivot attempts.** With the CST, map every attempt toward the receive server, its management interface, the PMMD kiosks, vendor paths that also serve CDAs, and the dispatch network. Each attempt goes into the Shift Manager's D1 record. **The CST alone decides whether any CDA was affected.**
4. **Data accessed.** Determine whether Security-Related Information (EDMS restricted folders, CAP security entries), personal information (ERP, access authorization enclave), or GDSR data was accessed or taken. Build the affected individuals list by state of residence. If SGI might be involved, switch to the insider runbook's SGI steps; SGI is never on the business network, so any SGI indication is itself a major finding.
5. **Preserve evidence.** Forensics images key hosts and exports logs before retention expires, with chain of custody. Evidence about anything in 73.54 scope stays with the CST under the CSP record rules (73.54(h)).

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the edge firewalls and the cloud firewall.
2. Disable compromised accounts. Rotate service account, vendor, and interface credentials (WMS, historian replica, GDSR, MSSP integrations).
3. Rebuild affected endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads from clean images in the isolated recovery network. Restore data from backups taken before the attacker's first access.
5. Forensics confirms persistence is removed before any reconnection.
6. **Receive server and one-way device feed:** reconnect only when the CST signs off. Historian replica data is backfilled from the plant historian through the one-way device.
7. **Portable media sweep:** the CST checks PMMD kiosk logs and quarantines any media that touched an affected Level 2 device in the dwell period.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel keeps the decision log (POL-03 4.8). Outside counsel confirms each legal notice before it goes out. **NRC notifications are made by the Shift Manager and are not delayed for legal review.**

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this reportable under 73.77(a)? Which paragraph and clock: (a)(1) 1 hour, (a)(2)(i) or (ii) 4 hours, (a)(3) 8 hours? | Shift Manager with the CST | Shift Manager log; CAP entry within 24 hours |
| D2 | Before **any** report to the FBI, CISA, the E-ISAC, or another agency: has the Shift Manager been told? Such a report can itself start a 4-hour NRC clock (73.77(a)(2)(iii)) | Incident commander and General Counsel | Decision log |
| D3 | Is a low-impact BES Cyber System affected, and is this a Reportable Cyber Security Incident requiring E-ISAC notification (CIP-003-9 Attachment 1 Section 4.2)? | Compliance and GRC Lead with the CIP Senior Manager | NERC incident record |
| D4 | Was personal information acquired? Date of determination (Florida 30-day clock); count of Floridians (500 for the Department of Legal Affairs; more than 1,000 for consumer reporting agencies); residents of other states | General Counsel | Affected individuals list |
| D5 | Contract notices: PPA-2 buyer (48 hours if GDSR or buyer data is affected), PE sponsor (24 hours), insurer | General Counsel and CFO | Contract register |
| D6 | Has law enforcement asked for a delay of consumer notices? | General Counsel | Decision log |
| D7 | Ransom decision | CEO on CMT recommendation | See below |
| D8 | Written follow-up: Form 366 within 60 days for (a)(1), (a)(2)(i), or (a)(2)(ii) notifications (73.77(d)) | Regulatory Affairs Manager | Submittal record |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Within 1 hour of discovery | ENS notification if 73.77(a)(1) applies (adverse impact on a 73.54 function). Not expected while the boundary holds | Shift Manager |
| Hour 0-1 | Insurer hotline; counsel engaged | CFO |
| Within 4 hours of discovery | ENS notification if 73.77(a)(2)(i) or (a)(2)(ii) applies | Shift Manager |
| Within 4 hours of any report to another agency | ENS notification under 73.77(a)(2)(iii), unless already notified under (a) | Shift Manager |
| Within 8 hours of receiving the information | ENS notification under 73.77(a)(3) for indications of intelligence gathering or pre-operational planning | Shift Manager |
| Within 24 hours | CAP entries for the notification and any program weakness (73.77(b)) | Regulatory Affairs Manager |
| Within 24 hours | PE sponsor notice; within 48 hours, PPA-2 buyer notice if GDSR or buyer data is affected | CEO; Energy Marketing and Settlements Manager |
| After D2 | Voluntary report to the FBI and CISA | IT Security Manager through General Counsel |
| Within 30 days of the breach determination | Florida notices to individuals and, if 500 or more Floridians, the Department of Legal Affairs | General Counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at one time | General Counsel |
| Varies | Residents of other states under each state's law | General Counsel with outside counsel |
| Within 60 days of the ENS call | Written follow-up report on NRC Form 366 (73.77(d)) | Regulatory Affairs Manager |

**CIRCIA** is proposed only and imposes no reporting duty today. If a final rule takes effect, its 72-hour and 24-hour reports will be added to this table (P01 R-049).

**Ransom decision (POL-03 4.9).** Needs the CEO, counsel, and the insurer; an OFAC sanctions check on the threat actor and any wallet; and a report to law enforcement through D2. The default position is not to pay while backups are intact. Paying does not remove any NRC or breach notification duty.

**Communications.**
- NRC: only through the Shift Manager and Regulatory Affairs. Resident inspectors are kept informed by Regulatory Affairs.
- Staff and contractors: briefings by radio and text; postings at access points.
- Media: holding statement approved by counsel and the Site Vice President. State clearly and only what is confirmed: for example, that plant safety systems are separate from the business network, if the CST has confirmed it. No technical details, ransom, or attribution comments.
- PPA buyers and the Balancing Authority: direct calls from the Energy Marketing and Settlements Manager.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Each step is validated first: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment. Anything touching the receive server needs CST sign-off.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | ERO callout service and printed call tree | 1 h | Test callout to 5 ERO members |
| 2 | Identity services and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 3 | Business network core, Station and EOF LANs; dispatch telemetry path | 2 h | Clean segments only |
| 4 | Clean endpoints for the work control center, RCA access point, and outage control center | 2 h | Pre-imaged spares; EDR healthy |
| 5 | WMS clearance and tagging module | 4 h | Restore; reconcile every active clearance against the paper log and field verification before switching back |
| 6 | RWP and dose tracking | 6 h | Reconcile paper RWPs and manual dose entries |
| 7 | WMS work orders and outage schedule; CAP | 8 h | Enter paper CAP forms in order; confirm 73.77(b) entries |
| 8 | SIEM feeds and EDR console | 8 h | Monitoring confirmed before wider reconnection |
| 9 | Access authorization enclave; EDMS | 12 h | Permissions review; verify procedure revisions |
| 10 | ERP (supply chain first) | 12 h (outage), 72 h (online) | Restore; payment change freeze until verified |
| 11 | Receive server and historian replica; then GDSR and cloud analytics | 24 h | CST sign-off; backfill data; GDSR data reconciled to revenue meters before sending to buyers |

Return processes from paper only after each system is validated. Tell staff, contractors, the PPA buyers, and the Balancing Authority when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 10 business days with the IRT, the CST, the Shift Managers involved, and the CMT; findings into the CAP and the P01 register.
- Update this runbook, the CSP incident response procedure if the CST finds a need (through the CSP change process), and the NERC low-impact plan within 180 calendar days if the event was a Reportable Cyber Security Incident (CIP-003-9 Attachment 1 Section 4.6).
- Retain the incident record, the D1 to D8 decision log, and evidence: CSP-related records until license termination (73.54(h)); the Form 366 copy 3 years or until license termination, whichever comes first (73.77(d)(12)); other records 6 years.
- Report to the audit committee at its next meeting.

# Incident Response Runbook: Ransomware on Dispatch and Train Control Back-Office Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (Class III short line freight railroad) |
| Tier / Vertical | Small / Transportation Systems |
| Incident type | Ransomware that enters through the dispatch system vendor's remote-access account and encrypts the CAD servers, dispatch consoles, and PTC administration workstation, with possible data theft |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT steps from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (proposed Cybersecurity Lead) |
| Approved | 2026-08-31 by the President and General Manager |
| Last tested | Not yet. First tabletop, with a manual dispatch step, due 2026-11-30 (POAM-011) |

**Two rules above all others:**
1. **Trains move only under authority the dispatcher can trust.** The moment the CAD system is suspect, dispatchers switch to manual dispatch (paper track warrants by radio).
2. **The TSA clock starts at discovery.** A cyber attack must be reported to TSA within 24 hours of initial discovery (49 CFR 1570.203). The company practice is to call within 12 hours, which also meets TSA's voluntary guidance.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (cyber) | IT Manager | Director of Finance and Administration | Incident line (cell), then the out-of-band group on personal phones |
| Operations commander (train safety) | Vice President of Operations | Chief Dispatcher | Dispatch center radio and phone |
| TSA Security Coordinator | Manager of Safety and Security | Chief Dispatcher (alternate) | Cell; dispatch center |
| Technical response | MSP incident team | Forensic firm (engaged through the cyber insurer's panel) | MSP 24x7 line |
| CAD system | Dispatch system vendor support | n/a | Vendor support line (calls only; **no remote access until cleared**) |
| PTC back office | PTC back office vendor operations center | n/a | Vendor 24x7 line |
| Host railroad | Class I's designated officer for the trackage-rights segment and its PTC help desk | Class I dispatcher for the segment | Numbers in the incident binder |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via the insurer hotline |
| Executive and communications | President and General Manager | Majority owner | Cell |
| Law enforcement and federal partners | FBI field office or IC3; CISA | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the domain are compromised. Coordinate on personal phones and the printed contact list in the incident binder at the dispatch center and North Yard.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at the dispatch center and North Yard: this runbook, contacts, the notification matrix, the TSOC number, the manual dispatch procedure, and the 1570.203(c) report form
- [ ] Manual dispatch kit at each console: paper track warrant forms, printed track chart, current bulletins, printed train sheets refreshed each shift (P05). **Gap until POAM-005 closes**
- [ ] Manual dispatch drilled in the last 6 months. **Gap until POAM-006 closes (first drill 2027-01-31)**
- [ ] Printed RSSM car list refreshed every 4 hours; clean standby laptop with cellular access to the TMS (P01 R-007)
- [ ] Immutable CAD backups in a separate account, restore-tested within 90 days (CP-9, CP-4). **Gap until POAM-004 and POAM-006 close**
- [ ] Vendor access only through the jump host (MA-4). **Gap until POAM-003 closes**
- [ ] EDR with 24x7 triage (SI-4). **Gap until POAM-009 closes**
- [ ] Two break-glass administrator accounts sealed in the dispatch center safe (POL-02 4.7)
- [ ] Forensic retainer and insurer panel confirmed (POAM-011)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note on a console or server, or CAD screens freeze or show files renamed | Dispatcher, EDR alert | Dispatcher tells the Chief Dispatcher; **start manual dispatch now**; call the incident line |
| CAD shows authorities or train sheets the dispatcher did not enter, or conflict checks behave oddly | Dispatcher | Treat CAD as untrusted; manual dispatch; call the incident line |
| Unexpected vendor session, or vendor says it did not connect | Firewall or vendor appliance, vendor | IT Manager disconnects the vendor appliance; opens an incident |
| PTC administration workstation encrypted, or PTC back office portal shows changes nobody made | PTC administrator | Stop data changes; call the PTC back office vendor and the incident line |
| Many files changing at once; backup job failures | EDR, backup report | IT Manager opens the incident |
| Extortion email or leak-site post naming the company | Email, law enforcement | Declare the incident; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any system, CAD data integrity is in doubt because of suspected malicious activity, or an extortion claim names company data.

**Record the time of discovery** in the incident log. It starts the TSA 24-hour clock and is needed for every other deadline.

## 3. First hour: make operations safe, then contain (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Switch to manual dispatch.** Each dispatcher reads active authorities from the last printed train sheet, then does a radio roll call of every train and work group to confirm location and authority. Stop issuing new authorities until the roll call is complete | Chief Dispatcher | Every movement accounted for on paper |
| 2. **Hold or restrict trains** as needed. PIH trains stay put until authority is confirmed. Decide whether interchange runs today | Vice President of Operations | Operating plan for the next 12 hours set |
| 3. **Cut vendor access.** Power off the dispatch vendor's VPN appliance and disable its account. Disable the staff remote-access VPN | IT Manager | No external sessions into the dispatch VLAN |
| 4. **Isolate the dispatch VLAN** from the office LAN and the cloud VPN at the HQ firewall. Leave affected servers and consoles **powered on** for memory evidence | IT Manager with the MSP | Dispatch VLAN isolated |
| 5. **Keep radio up.** Confirm dispatcher radio works on the gateway or the fallback repeater and handhelds | Signal and Communications Supervisor | Dispatch has radio contact with all trains |
| 6. **Tell the host railroad** if any company train is on, or due on, the Class I segment. Report any en route PTC failure or cut-out to the host's designated officer as soon as safe and practicable (236.1029(b)(4)). Stop PTC data changes from the company side | Chief Dispatcher; Vice President of Operations | Host informed; affected trains handled per the host's instructions |
| 7. **Call the cyber insurer's breach hotline.** Engage counsel and forensics through the insurer | President and General Manager | Claim number issued |
| 8. **Start the incident log:** timeline, actions, who, and when | IT Manager | Log open |

## 4. Report to TSA (RS.CO) within 12 hours
The Manager of Safety and Security (or the Chief Dispatcher as alternate) calls the TSOC. Do not wait for the investigation to finish. "When in doubt, report" (POL-03 4.4).

The report includes, as available (49 CFR 1570.203(c)):
1. Name and contact information of the person reporting
2. Affected facility or infrastructure: the dispatch center at Central Yard and the systems affected; any affected trains, with current location
3. Origin and destination of any affected train, and route
4. Description of the incident, who has been notified, and what action has been taken
5. Descriptions of individuals or accounts known or suspected to be involved (for example, the vendor account used)
6. Source of the threat information

Record the call time, the TSOC reference, and the name of the TSA person who took the report. Call again with material updates. If SSI may have been taken (for example, network diagrams or TSA-marked documents on the file server), also inform TSA under 1520.9(c).

**TSA location requests continue during the incident.** If TSA asks for RSSM car locations, answer within 30 minutes from the printed RSSM car list or the standby laptop (1580.203(d)).

## 5. Analysis (RS.AN)
1. **Scope:** which servers, consoles, workstations, and accounts are affected? Check EDR (once deployed), dispatch server logs before they overwrite (about 14 days, POAM-014), the firewall, the identity provider sign-in logs, and cloud audit logs.
2. **Initial access:** confirm the vendor account and appliance as the entry point, and whether the vendor itself was compromised. Ask the vendor whether other customers are affected.
3. **Preserve evidence:** forensics images affected hosts and exports logs. Keep chain of custody.
4. **CAD data integrity:** compare the last CAD backup and the paper train sheets. **Any authority data restored from backup must be confirmed by radio roll call before use.**
5. **PTC back office:** confirm with the PTC back office vendor whether the company's tenancy, locomotive and crew data, or keys were touched. The onboard units and the host's PTC system are separate from the office network, but the PTC workstation's credentials must be treated as compromised.
6. **Data theft:** check for archive tools and large outbound transfers. Employee records on the file server and SSI drive the Florida and TSA SSI decisions.
7. **Backups:** confirm the backup vault is intact before any restore. Check that the attacker's credentials could not reach it.

## 6. Containment and eradication (RS.MI)
1. Block attacker infrastructure (IPs, domains) at the HQ firewall and in the cloud network rules.
2. Reset all administrator, service, and vendor credentials from a clean workstation. Revoke all identity provider sessions. Rotate the PTC portal administrator credentials with the vendor.
3. Rebuild CAD servers, consoles, and the PTC administration workstation from known-good media and the vendor's certified build. **Do not decrypt and reuse them.**
4. Patch the rebuilt servers to the vendor-certified level before reconnecting.
5. The dispatch vendor reconnects only through the jump host with a named account and MFA (POAM-003). The always-on appliance is not restored.
6. Confirm with forensics that persistence is removed before recovery starts.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Manual dispatch continues until the CAD system is verified.
1. Manual fallbacks in place: paper dispatch, RSSM car list, TSOC contact (within 30 minutes)
2. Dispatcher radio (2 h)
3. Identity provider and administrator access, break-glass if needed (2 h)
4. Isolated dispatch VLAN, detector and crossing alarm path (4 h)
5. CAD system restored to clean servers from a verified backup (8 h target; unproven until POAM-006)
6. Crew management application (12 h)
7. PTC administration workstation and PTC back office access (24 h). Interchange resumes only after the host railroad agrees
8. TMS access from clean endpoints (24 h)
9. Office endpoints and the file server (48 h)
10. Finance, payroll, and HR (72 h)

**Cut back to the CAD system** only when: the servers are clean and patched; all active authorities in the CAD match the paper record and a radio roll call; and the Vice President of Operations approves. Tell crews, shippers, and the Class I when normal operations resume (RC.CO).

## 8. Notifications (RS.CO)
**Follow `notification-matrix.csv` (18 obligations).** Legal counsel confirms every notice except the TSA and host railroad calls, which go out without waiting.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Host railroad informed if the trackage-rights segment is affected; insurer notified | Chief Dispatcher; President and General Manager |
| Within 12 hours (company target; legal limit 24 hours) | TSA report to the TSOC (1570.203) | Manager of Safety and Security |
| Same day | Voluntary report to CISA and FBI | IT Manager |
| Promptly, if SSI was released | TSA notice under 1520.9(c) | Manager of Safety and Security |
| Immediately, only if a reportable accident/incident occurs | National Response Center call (225.9); hazmat incident call within 12 hours (171.15) | Manager of Safety and Security |
| Within 30 days after month end | FRA monthly report, if any reportable accident/incident occurred (225.11) | Manager of Safety and Security |
| Within 30 days of determining a breach | Florida notice to affected employees; Department of Legal Affairs if 500 or more (501.171) | Director of Finance and Administration with counsel |
| Day 0-5 | Staff briefing script: what happened, manual procedures, do not discuss outside the company | President and General Manager |

**Ransom decision:** requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any reporting duty.

**Not applicable today:** SD 1580-21-01E reporting to CISA (no TSA designation); the TSA surface cyber NPRM and CIRCIA (proposed only). Recheck if TSA designates the company or a final rule is published.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days). Include the dispatchers' experience with manual dispatch.
- Update the risk register (P01, especially R-001, R-003, R-005, R-006), the POA&M (P07), the contingency plan, and this runbook.
- Give TSA any follow-up information it requests.
- Keep all incident records for at least 5 years (POL-01 4.10).

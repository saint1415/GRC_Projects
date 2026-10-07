# Incident Response Runbook: CAD Outage from Ransomware

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (licensed private ambulance service; PE-backed) |
| Tier / Vertical | Mid-Market / Emergency Services |
| Incident type | Ransomware encrypts the CAD application servers, the integration engine, and communications center consoles, forcing manual dispatch at both centers, with possible theft of PHI (double extortion) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-billing-vendor-breach.md` (billing platform vendor breach); `notification-matrix.csv`; BIA (P05); County A communications center continuity plan; manual dispatch binders |
| Runbook owner | Security Manager (incident commander), with the Director of Communications (dispatch continuity lead) |
| Approved | 2026-09-16 by the Chief Operating Officer |
| Last tested | Not yet. Ransomware manual dispatch drill at both centers due 2026-11-30 (POAM-011); joint tabletop with both counties 2027-01-20 (POAM-014) |

**Two tracks run at once.** Track A keeps ambulances moving (dispatch continuity). Track B handles the security incident. **Track A never waits for Track B** (POL-03 4.2).

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so dispatch, technical, and business and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Dispatch command** | Director of Communications (lead), on-duty communications supervisors at both centers, Director of Field Operations, Medical Director | Entering and leaving manual mode, staffing both centers, County A overflow and mutual aid, deferral of interfacility work, clinical safety |
| **Incident response team (IRT)** | Incident commander: Security Manager. Director of IT (recovery lead), security analysts, MSSP, forensic firm (through counsel), CAD vendor, cloud provider support | Containment, investigation, eradication, CAD rebuild and recovery sequence |
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, vCISO, Medical Director, Compliance and Privacy Officer, Director of Government Contracts, HR Director, outside breach counsel | County and hospital relationships, external statements, notification decisions, ransom recommendation to the CEO, resources |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Dispatch continuity lead (Track A) | Director of Communications | On-duty communications supervisor | Center floor; supervisor cell; county P25 supervisor talkgroup |
| Incident commander (Track B) | Security Manager | Director of IT | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Breach and privacy decisions | Compliance and Privacy Officer | Outside breach counsel | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | Company's outside general counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($10 million limit, $250,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| County liaison | Director of Government Contracts | Chief Operating Officer | County A PSAP supervisor line; County B center director; county EMS offices |
| Clinical safety | Medical Director | Associate medical director | Cell |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | Chief Operating Officer | Phone |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, the hosted phone system's soft clients, and anything on the company network are compromised. Coordinate on personal phones, the county P25 supervisor talkgroup, and the printed call trees kept at both centers and every station.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in email, chat, or radio traffic.

## 1. Preparation checks (Identify / Protect)
- [x] Manual dispatch binders at both centers: paper incident cards, unit status boards, run cards by zone, radio procedures, county PSAP numbers, mutual-aid contacts
- [x] County P25 radio console positions at both centers and radios in every vehicle (county-operated)
- [x] Write-once CAD database copies in the backup account, 30-day retention (CP-9; P07 test restore in 38 minutes)
- [ ] Integration engine and call recordings in write-once backups (CP-9). **Gap until POAM-012 closes**
- [ ] CAD rebuild runbook tested in the isolated recovery network (CP-4, CP-10). **Gap until POAM-012 closes**
- [ ] Ransomware manual dispatch drill held at both centers in the last 6 months. **Gap until POAM-011 closes**
- [ ] EDR in block mode on all 24 consoles (SI-3). **Gap until POAM-019 closes**
- [ ] 12 pre-imaged spare console laptops kept offline, 6 at each center (POAM-014)
- [ ] Break-glass credentials sealed for the identity provider, CAD administration, and the cloud organization (POL-02 4.9). **Identity provider only today**
- [x] Paper patient care record kits in every ambulance (P05 BP-05)
- [x] Insurer panel counsel and forensics confirmed; call tree verified 2026-09-16
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| CAD client freezes or shows errors on several consoles at once, at either center | Telecommunicator | Supervisor starts Track A (manual mode) at once and calls the incident line |
| Ransom note on a console, or files renamed with an unknown extension | Telecommunicator; EDR alert | **Do not power off.** Unplug the console's network cable. Start Track A. Call the incident line |
| CAD servers or database unreachable; backup deletion attempts; EDR or logging disabled | MSSP; cloud audit logs; vault alert | MSSP isolates hosts and calls the incident commander within 30 minutes; treat as ransomware precursor |
| MDCs lose CAD but radio works | Crews | Crews switch to radio status reports; dispatch confirms manual mode |
| Station alerting fails or alerts falsely at several stations | Crews; supervisors | Supervisors alert stations by phone and radio; report to the incident line |
| Large outbound transfer from the data and reporting account | Cloud firewall flow logs (egress alerting due 2027-01-31) | Block the destination; declare |
| Extortion email or leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve the message |

**Severity 1 (declare immediately):** any confirmed ransomware execution, a CAD outage expected to exceed the 1-hour RTO, confirmed PHI exfiltration, or an extortion claim naming company data (POL-03 4.5).

**Record the date and time of discovery in the incident log** (POL-03 4.4). Under 45 CFR 164.404(a)(2), a breach is treated as discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member or agent. The Florida 30-day clock runs from determination of the breach or reason to believe one occurred (Fla. Stat. 501.171(4)).

## 3. Track A: keep dispatching (RC.RP; CP-2(5))
| Step | Who | Done when |
|---|---|---|
| A1. Announce "manual dispatch" to all units on the company talkgroups. Units report location and status by radio | On-duty supervisor at the primary center | All staffed units acknowledged |
| A2. Call the County A PSAP supervisor: CAD-to-CAD is down; ask the PSAP to voice-announce new medical calls and keep transferring callers by phone. This is also the contract notice for an outage longer than 15 minutes | On-duty supervisor | PSAP confirms |
| A3. Call the County B communications center: ask it to voice-announce calls in the company zones on the county talkgroup | On-duty supervisor | County B confirms |
| A4. Start paper incident cards and status boards. One telecommunicator takes calls and runs EMD from the paper protocol cards, one tracks units, the supervisor assigns. Staff the backup center as a second manual position for County B | Telecommunicators; Director of Communications | Boards match radio roll call |
| A5. Call in off-duty telecommunicators to double-staff both centers for manual mode | Director of Communications | Staffing plan for the next 3 shifts |
| A6. Forward request lines to supervisor cell phones if console phones are affected | Director of Communications | Test call answered |
| A7. Tell hospitals and nursing facilities that non-urgent interfacility trips may be delayed; defer scheduled non-urgent trips; critical care transfers continue | Communications supervisor (interfacility desk) | Facility call list done |
| A8. Supervisors alert stations by phone and radio if station alerting is affected; crews switch to paper patient care records if tablets cannot sync | Director of Field Operations | Crews confirm |
| A9. **At 2 hours in manual mode (P05 MTD)**, or sooner if the Medical Director judges it unsafe, ask County A to route overflow 911 calls to the mutual-aid provider. Revisit at every shift change | Chief Operating Officer with the Medical Director | County confirms routing |
| A10. Log every Track A decision with the time | Supervisors | Log kept at both centers |

## 4. Track B: first 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected consoles and servers through EDR network containment or by pulling cables; keep them powered on for memory evidence | MSSP; security analysts; telecommunicators with IT on the phone | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Operating Officer | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | Director of IT | Backup integrity confirmed |
| 0-2 h | Disable site and vehicle VPN tunnels into the dispatch production account if the CAD servers may be affected; block known attacker infrastructure at the cloud firewall; disable the CAD vendor remote tool and the station alerting vendor connection | Director of IT | Tunnels and vendor paths blocked |
| 0-2 h | Revoke all identity provider sessions; reset privileged credentials using break-glass accounts; change the CAD administrator and service credentials | Security Manager | Sessions revoked; credentials changed |
| 0-2 h | Snapshot the CAD servers, database, and integration engine for evidence before any restore | Director of IT with the MSSP | Snapshots taken, tagged, and stored in the backup account |
| 1-2 h | Convene the CMT; first situation report (dispatch status, scope, patient impact, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing script: manual mode steps, do not discuss externally, report anything unusual; send by text and post at centers and stations | Chief Operating Officer with HR | Script delivered |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | Chief Executive Officer | Notice given |

## 5. Analysis (RS.AN)
1. **Scope.** Which consoles, cloud servers, accounts, and vehicles are affected? Use EDR telemetry, identity provider sign-in logs, cloud control-plane logs in the locked log bucket, firewall and VPN logs, and the vendor remote tool's history.
2. **Initial access and dwell time.** Likely paths are phishing, the CAD vendor remote tool (P01 R-021), an unpatched console (R-004), an unmanaged vehicle router (R-007), or an edge appliance (R-035). Find the first compromised host and the date the attacker first got in.
3. **Preserve evidence.** Forensics images key hosts and exports logs before they roll over. CAD logs roll over after 30 days and integration engine logs after 14 days, so export them on day 0. Keep chain of custody (who collected, when, hash, storage). Evidence is held by the forensic firm under counsel.
4. **Exfiltration.** Determine whether CAD incident data (names, addresses, chief complaints), call recordings, or reporting database extracts were accessed or taken. Look for archive tools, staging folders, storage access, egress volume, and leak-site samples. Build the **affected individuals list** by data element, by state of residence, and, for any billing data, **by billing services client**. **This drives the breach determination and every notice.**
5. **SaaS and county systems.** Confirm the ePCR, billing platform, identity provider, and hosted phone system are unaffected and that stolen credentials were not used there. Tell both counties what indicators to look for on their side of the CAD-to-CAD links.

## 6. Containment and eradication (RS.MI)
1. Block attacker infrastructure at site firewalls, SD-WAN edges, and the cloud firewall.
2. Disable compromised accounts. Rotate CAD service accounts, integration engine credentials, vehicle VPN certificates if exposed, and the county interface credentials (tell each county first).
3. Rebuild consoles from the standard image, or deploy the spare laptops. **Do not decrypt and reuse encrypted machines.**
4. Rebuild the CAD application servers and the integration engine from clean images in the isolated recovery network with the CAD vendor. Restore the CAD database to a point in time before the attacker's first access, verified against the write-once copies.
5. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts, vendor agents) is removed before reconnection.

## 7. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice before it goes out. The Compliance and Privacy Officer keeps the **decision log** (POL-03 4.6).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a breach of unsecured PHI? Presumed yes unless a four-factor assessment (45 CFR 164.402) shows a low probability of compromise. Encrypted data with uncompromised keys is not unsecured PHI | Compliance and Privacy Officer with counsel | Decision log with the four factors |
| D2 | Date of discovery (HIPAA clock) and date of determination (Florida clock) | Compliance and Privacy Officer | Decision log |
| D3 | How many individuals in total, by state, and Florida residents (thresholds: 500 for HHS contemporaneous notice and the Florida Department of Legal Affairs; more than 500 residents of a state for media; more than 1,000 for Florida consumer reporting agencies) | Compliance and Privacy Officer | Affected individuals list |
| D4 | Does any billing services client's PHI sit in the affected systems? If so, the company owes business associate notices (D7 in the companion runbook) | Compliance and Privacy Officer with the Director of Revenue Cycle | Client attribution in the affected list |
| D5 | Has law enforcement asked for a delay? If oral, document it; the delay lasts no longer than 30 days unless confirmed in writing (164.412) | Counsel | Decision log |
| D6 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Within 15 minutes of the outage | County A PSAP told dispatch is manual (contract outage notice) | On-duty supervisor |
| Hour 0-1 | Insurer hotline; counsel engaged | Chief Operating Officer |
| Within 24 hours of discovery | County A security incident notice to the EMS office and county IT security (contract) | Director of Government Contracts |
| Within 72 hours of discovery | County B security incident notice (contract) | Director of Government Contracts |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA. It helps the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Security Manager through counsel |
| Within 2 business days | Lender agent notice under the credit agreement | Chief Financial Officer |
| As soon as scoped | Four-factor assessment documented (D1) | Compliance and Privacy Officer |
| Within 30 days of determination | Florida individual notice (or HIPAA notice, with a copy to the Department of Legal Affairs under the deemed-compliance path); Department of Legal Affairs notice if 500 or more Floridians | Compliance and Privacy Officer and counsel |
| Without unreasonable delay, no later than 60 days after discovery | HIPAA individual notices (first-class mail; substitute notice with a 90-day toll-free number if 10 or more addresses are out of date); HHS notice at the same time if 500 or more; media notice if more than 500 residents of a state | Compliance and Privacy Officer and counsel |
| Without unreasonable delay | Consumer reporting agencies if Florida notice goes to more than 1,000 individuals at once | Counsel |
| Each other state | Residents of other states: apply each state's law (counsel checks the affected list by state) | Counsel |
| Within 60 days after year end | HHS log entry for any breach under 500 | Compliance and Privacy Officer |

**Why the shorter clock matters.** Florida's 30 days run from the determination of a breach; HIPAA's 60 days are an outer limit that runs from discovery. If determination comes soon after discovery, Florida's deadline arrives first. Counsel decides early whether one HIPAA-compliant notice with a timely copy to the Department of Legal Affairs will satisfy Florida.

**CIRCIA is not yet in force.** If the final rule is published and matches the proposal, this incident would also need a CISA report within 72 hours, and a ransom payment report within 24 hours. Recheck the rule's status at each annual review.

**Ransom decision (POL-03 4.9).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet; and a report to law enforcement. Paying does not remove breach notification duties if data was taken, and does not guarantee a working decryptor. The default position, approved by the CEO, is not to pay while the write-once CAD database copies are intact. Manual dispatch and county help must be sustained while any decision is made.

**Communications.**
- Counties: the Director of Government Contracts holds a call with both county EMS offices at least twice a day while manual mode lasts.
- Hospitals and facilities: the interfacility desk calls each facility; the Medical Director calls emergency department medical directors if pre-alerts or record delivery are affected.
- Media: holding statement approved by counsel that ambulances are responding and 911 is working; no technical details, ransom, or attribution comments.
- Staff: shift-change briefings at both centers and every station; the out-of-band channel only.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Items 1 and 2 are already running from Track A. Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, and forensics sign-off.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | County P25 radio and manual dispatch at both centers | Immediate | Radio roll call matches boards |
| 2 | Phone lines and the County A caller transfer path | 30 min | Test transfer from County A |
| 3 | Identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 4 | Networks and clean consoles at the primary center, then the backup center | 1 h | Spare laptops or reimaged consoles; EDR in block mode |
| 5 | CAD servers and database | 1 h target; unproven until POAM-012 closes | Point-in-time restore before first access; CAD vendor integrity check |
| 6 | Station alerting controllers | 1 h | Test alert to each station |
| 7 | Vehicle routers and MDCs | 2 h | Re-enrollment; new VPN certificates if needed |
| 8 | Integration engine: County A and County B CAD-to-CAD, then the ePCR push | 4 h | Test incident with each county before going live |
| 9 | SIEM feeds and EDR console | 4 h | Monitoring confirmed before wider reconnection |
| 10 | ePCR sync; back-enter paper patient care records within 48 hours so hospitals can get them (Rule 64J-1.014, F.A.C.) | 8 h | Delivery report checked |
| 11 | Billing export and backlog | 48 h | Test batch accepted |
| 12 | Reporting database, posting model, and county reports | 72 h to 168 h | Reports reconciled with paper cards |

**Leaving manual mode.** The Director of Communications, not IT, decides when to switch back, one center at a time, after a test incident runs end to end (entry, EMD, unit recommendation, MDC, station alert, CAD-to-CAD). The decision is announced on the radio and to both counties (RC.CO). Paper incident cards are entered into CAD so response-time reports and state data are complete.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with both counties and the Medical Director; written report within 30 days (POL-03 4.11).
- The Medical Director reviews every call handled in manual mode for delays that affected patients.
- Update the risk register (P01: R-001, R-002, R-003, R-021), the POA&M (P07), the BIA's MTD assumptions, the County A continuity plan, and this runbook.
- Retain all incident documentation, including the decision log and notices, for 6 years (POL-01 4.12; 45 CFR 164.414(b)).

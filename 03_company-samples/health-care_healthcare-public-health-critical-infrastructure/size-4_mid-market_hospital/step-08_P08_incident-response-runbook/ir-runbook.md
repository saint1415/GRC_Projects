# Incident Response Runbook: Ransomware Forcing EHR Downtime and Ambulance Diversion

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed 112-bed community acute-care hospital with an off-campus outpatient center) |
| Tier / Vertical | Mid-Market / Healthcare and Public Health |
| Incident type | Ransomware (with possible PHI exfiltration) that encrypts the on-premises data center and campus endpoints, takes away EHR access and clinical servers, and forces ambulance diversion |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response and Downtime Policy |
| Companion documents | `ir-runbook-insider-access.md` (second incident type); `notification-matrix.csv`; BIA (P05); emergency operations plan and its IT outage annex (due 2026-12-15, POAM-022) |
| Runbook owner | Information Security Manager (incident commander for cyber) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Ransomware and 72-hour EHR downtime tabletop with clinical command, the executive team, and outside counsel scheduled 2026-11-10, counted as the 42 CFR 482.15(d)(2)(ii) additional exercise (POAM-011, POAM-013) |

## 0. Governance, roles, and contacts (Govern)
A hospital ransomware event is a cyber incident and a patient care emergency at the same time. The response runs as three linked teams under the **Hospital Incident Command System**, so technical, clinical, and legal decisions each have one owner.

| Team | Members | Decides |
|---|---|---|
| **Hospital command (Hospital Incident Command System)** | Hospital incident commander: CEO (or the administrator on call until the CEO arrives). Operations section: CNO. Medical specialist: CMO. Liaison: Director of Emergency Management. Public information: Director of Marketing and Communications | Activation of the emergency operations plan and IT outage annex, staffing, patient flow, diversion, transfers, external public statements |
| **Cyber crisis management team (CMT)** | Chair: COO. CFO, vCISO, IT Director, Compliance and Privacy Officer, HR Director, outside breach counsel | Business decisions, notifications, insurer, ransom recommendation to the CEO, affiliated practice and partner notices |
| **Incident response team (IRT)** | Incident commander: Information Security Manager. IT Director (recovery lead), security analysts, MSSP, forensic firm (through counsel), Director of Biomedical Engineering, Director of Facilities, EHR, PACS, LIS, and cloud vendor contacts | Containment, investigation, eradication, recovery sequence |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Cyber incident commander | Information Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| Hospital incident commander | CEO | Administrator on call | Hospital command center (main campus conference room 2) |
| CMT chair | Chief Operating Officer | CFO | Out-of-band group |
| Clinical command and diversion | CNO with the ED Medical Director and the administrator on call | House Supervisor | Command center; ED radio |
| Breach and privacy decisions | Compliance and Privacy Officer | Outside breach counsel | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | Hospital's outside general counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Medical devices and OT | Director of Biomedical Engineering; Director of Facilities | Manufacturer support lines | Radio; out-of-band group |
| Communications | Director of Marketing and Communications | Outside crisis PR (through counsel) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| County EMS and coalition | Administrator on call (diversion status) | Director of Emergency Management | EMS radio in the ED; analog line |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, VoIP, and smartphones are compromised or down. Command teams use a pre-provisioned messaging group on personal phones, the analog lines in the ED and house supervisor office, handheld radios, and printed call trees kept in every unit's downtime binder.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in email or chat.

## 1. Preparation checks (Identify / Protect)
- [x] Write-once cloud backups in the separate backup account, 35-day retention (CP-9 cloud copy)
- [x] EDR on all managed endpoints and servers with 24x7 MSSP (SI-3; P07 fully satisfied)
- [x] 12 downtime workstations with hourly extract; printed downtime forms in every unit binder
- [ ] Backup appliance separated from the directory (POAM-012). **Gap: local backups can be deleted with domain administrator rights**
- [ ] Restore test of the interface engine, LIS, dispensing cabinet server, and PACS in the last 90 days (CP-4). **Gap until POAM-011 closes**
- [ ] Sealed break-glass accounts for the identity provider, directory, EHR administration, and PACS (POL-02 4.11). **Gap except cloud**
- [ ] 72-hour downtime procedures and diversion criteria in the IT outage annex (POAM-010, POAM-022)
- [ ] Analog or cellular lines and radios on every unit (POAM-010). **Today only the ED and house supervisor office**
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-17
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-14)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption on servers or workstations | EDR alert; staff report | MSSP isolates hosts (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Backup deletion attempts, or disabling of EDR or logging | Backup appliance alerts; EDR tamper alert; cloud audit logs | Treat as ransomware precursor; declare |
| New domain administrator or privileged sign-in from a vendor account outside a scheduled session | SIEM; directory audit | Disable the account; declare if unexplained |
| Clinical systems failing across units at once (LIS, cabinets, monitoring gateway, EHR sign-in) | Service desk; House Supervisor | IT triage; declare if malicious or unexplained within 30 minutes |
| Large outbound transfer from the data warehouse, file services, or PACS | Cloud firewall flow logs (egress alerting due 2027-01-31) | Block the destination; declare |
| Extortion email or leak-site post naming the hospital | Email; threat intelligence; FBI; Health-ISAC | Declare; preserve the message |

**Severity 1 (declare immediately):** confirmed ransomware execution, confirmed PHI exfiltration, an extortion claim naming hospital data, or loss of any High-criticality BIA process (P05) from a suspected attack.

**Record the date and time of discovery in the incident register** (POL-03 4.3). Under 45 CFR 164.404(a)(2), a breach is treated as discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member or agent. This date can start the HIPAA 60-day clock.

## 3. First 4 hours (RS.MA, RS.MI, and clinical continuity)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident register entry with discovery time | Cyber incident commander | Register entry open |
| 0-30 min | **Activate downtime procedures on every unit.** Print fresh MARs, census, and active orders from the downtime workstations before they lose their last extract | House Supervisor; unit charge nurses | Printouts in each unit |
| 0-60 min | Activate the Hospital Incident Command System and open the command center; brief the CEO or administrator on call | Administrator on call; Director of Emergency Management | Command center open |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Operating Officer | Claim number; counsel on the call |
| 0-60 min | Protect backups: confirm the write-once cloud copies are intact; suspend replication from the backup appliance; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Disconnect the campus from the cloud hub and the internet except the EHR vendor connection, if the EHR vendor confirms it is unaffected; block known attacker infrastructure | IT Director | Routes down or filtered |
| 0-2 h | Revoke all sessions in the identity provider; disable vendor remote access and VPN accounts; reset privileged credentials using break-glass accounts | Information Security Manager | Sessions revoked |
| 0-2 h | **Protect patient monitoring:** biomedical engineering confirms bedside monitors, ventilators, pumps, and fetal monitors are alarming locally; assign observers for telemetry patients if the monitoring gateway or central stations are down (BP-03, MTD 2 h) | CNO; Director of Biomedical Engineering | Observers assigned |
| 0-2 h | **Protect building systems:** facilities engineers start hourly rounds of isolation room pressure, operating room pressure, pharmacy and blood bank temperatures, and medical gas alarms; switch building automation to local control if the OT network is affected | Director of Facilities | Rounds log started |
| 0-4 h | **Diversion decision** (section 3.1) at the 4-hour ED MTD, or earlier if CT, the laboratory, or the cath lab is down | CNO; ED Medical Director; administrator on call | Decision logged with time |
| 1-2 h | Convene the CMT; first situation report (scope, patient impact, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing script by radio, overhead page, and runners: what happened, downtime steps, do not discuss externally, report anything unusual | Director of Marketing and Communications with HR | Script delivered on every unit |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

### 3.1 Diversion decision (clinical command)
The decision belongs to the CNO, the ED Medical Director, and the administrator on call, together. The criteria below are the draft IT outage annex criteria (final by 2026-12-15).

| Situation | Decision | Notes |
|---|---|---|
| EHR down but downtime workstations, laboratory, CT, and phones working | Stay open; paper downtime | Review every 2 hours |
| EHR down for 4 hours (ED MTD) with no restoration estimate under 4 more hours | Consider full diversion of ambulances | Weigh ED census and staffing |
| CT or the LIS down | **Stroke and trauma diversion** at once | Stroke and STEMI patients go to the regional medical center 11 miles away |
| Cath lab hemodynamic system or the cardiology system down | **STEMI diversion** at once | Cath lab team stays to finish cases in progress |
| Phones and smartphones down on the units | Full diversion until radios or analog lines are working on every unit | Codes called overhead and by radio |
| Monitoring gateway down and observers cannot be staffed | Close telemetry admissions; consider diversion | ICU continues at the bedside |

**EMTALA reminders (42 CFR 489.24(b)).** Diversion applies only to ambulances not yet on hospital property. Any patient who arrives (walk-in, or an ambulance that disregards the diversion) has come to the ED and receives a medical screening examination and stabilizing treatment within the hospital's capability. Transfers of unstable patients follow the hospital's EMTALA transfer procedure on paper.

**Tell county EMS** by EMS radio and the analog line at each status change, and tell the regional medical center and the 180-bed hospital directly (482.15(c)(7); matrix row "Diversion status to county EMS"). Log every decision with the time and the reason.

## 4. Analysis (RS.AN)
1. **Scope.** Which servers, endpoints, identities, and cloud accounts are affected? Use EDR telemetry, identity provider sign-in logs, directory logs, cloud control-plane logs in the write-once log archive, and firewall flow logs.
2. **Initial access and dwell time.** Check the most likely entry points first: the 14 vendor VPN accounts (P01 R-010), phishing (R-011), and internet-facing devices (R-033). Identify the first compromised account and the date the attacker first got in.
3. **Preserve evidence.** Forensics images key hosts and exports logs before local retention expires (30 days or less on clinical servers), with chain of custody (who collected, when, hash, storage).
4. **Exfiltration.** Determine what PHI was accessed or taken: archive tools, staging directories, cloud storage access, egress volume, leak-site samples. Build the **affected individuals list** by data element and state of residence, and flag affiliated practice patients separately. **This drives the breach determination and every notice.**
5. **Medical devices and OT.** Biomedical engineering and manufacturers check the pump and cabinet servers, the monitoring gateway, the fetal surveillance server, the cath lab system, analyzers, and the device VLANs for spread. Facilities checks the building automation controller. Pumps keep running on their last drug library; any library change is verified by pharmacy before reconnection.
6. **Vendor status.** Confirm with the EHR vendor, identity provider, and MSSP that their platforms are unaffected and that the EHR connection from the hospital is safe to keep open.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the campus firewalls, the outpatient center SD-WAN, and the cloud firewall.
2. Disable compromised accounts. Rotate service account, interface, vendor, and device credentials (including the pump and cabinet server passwords, P01 R-054).
3. Rebuild affected endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild the virtualization cluster and clinical servers in BIA order (section 7) from backups taken before the attacker's first access, with manufacturers present for vendor-managed servers.
5. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts) is removed before each segment reconnects.
6. Medical devices and OT reconnect only after biomedical engineering or facilities confirms them clean, and only to their restricted segments.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice before it goes out. The Compliance and Privacy Officer keeps the **decision log** (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a breach of unsecured PHI? Presumed yes unless a four-factor assessment (45 CFR 164.402) shows a low probability of compromise. Encrypted data with uncompromised keys is not unsecured PHI | Compliance and Privacy Officer with counsel | Decision log with the four factors |
| D2 | Date of discovery (HIPAA clock) and date of determination (Florida clock) | Compliance and Privacy Officer | Decision log |
| D3 | Number of affected individuals in total, by state, and Florida residents (thresholds: 500 for HHS contemporaneous notice and the Florida Department of Legal Affairs; more than 500 residents of a state for media; more than 1,000 for Florida consumer reporting agencies) | Compliance and Privacy Officer | Affected individuals list |
| D4 | Has law enforcement asked for a delay? If oral, document it; the delay lasts no longer than 30 days unless confirmed in writing (164.412) | Counsel | Decision log |
| D5 | Are affiliated practice patients affected? The hospital is their business associate (164.410) and its services agreement promises initial notice within 5 business days | Compliance and Privacy Officer and counsel | Practice notice log |
| D6 | Did a compromised device or software contribute to a death or serious injury? (21 CFR 803.30, 10 work days) | Director of Biomedical Engineering with the CMO | MDR file |
| D7 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | COO |
| Hour 0-4 | Diversion status to county EMS and nearby hospitals at each change | Administrator on call |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA. It helps the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Information Security Manager through counsel |
| Within 5 business days of confirming the incident | Initial notice to affected affiliated practices (services agreement) | Compliance and Privacy Officer |
| As soon as scoped | Four-factor assessment documented (D1) | Compliance and Privacy Officer |
| Within 10 work days of awareness | FDA and manufacturer reports if a device contributed to a death, manufacturer if a serious injury (21 CFR 803.30) | Director of Biomedical Engineering |
| Within 30 days of determination | Florida individual notice (or HIPAA notice with a copy to the Department of Legal Affairs under the deemed-compliance path); Department of Legal Affairs notice if 500 or more Floridians (no extension for this notice) | Compliance and Privacy Officer and counsel |
| Without unreasonable delay, no later than 60 days after discovery | HIPAA individual notices (first-class mail; substitute notice with a 90-day toll-free number if 10 or more addresses are out of date); HHS notice at the same time if 500 or more; media notice if more than 500 residents of a state; business associate notice to the practices with identities | Compliance and Privacy Officer and counsel |
| Without unreasonable delay | Consumer reporting agencies if Florida notice goes to more than 1,000 individuals at once | Counsel |
| Each other state | Seasonal residents and visitors from other states: apply each state's law (counsel checks the affected list by state) | Counsel |
| Within 60 days after year end | HHS log entry for any breach under 500 | Compliance and Privacy Officer |
| Not yet required | CIRCIA reports (proposed 72 hours and 24 hours after a ransom payment) would apply to this 112-bed hospital if the rule is finalized as proposed; recheck at each runbook review | vCISO |

**Why the shorter clock matters.** Florida's 30 days run from the determination of a breach; HIPAA's 60 days are an outer limit that runs from discovery. If determination comes soon after discovery, Florida's deadline arrives first. Counsel decides early whether one HIPAA-compliant notice, with a timely copy to the Department of Legal Affairs, will satisfy Florida.

**Ransom decision (POL-03 4.10).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (civil penalties apply on a strict liability basis); and a report to law enforcement. Paying does not remove breach notification duties if data was taken, and does not guarantee working decryption or deletion. The default position, approved by the CEO, is not to pay while the write-once backups are intact.

**Communications.**
- Patients and families on site: unit leaders explain that the hospital is working on paper and that care continues.
- Public: a website notice and call-center script within 24 hours of any visible disruption (website hosted outside the hospital network), with a patient hotline through the insurer's notification vendor once notices are due.
- County EMS, the coalition, and nearby hospitals: diversion status and expected duration.
- Affiliated practices: a call from the Director of Physician Services on day 0, then written notice per D5.
- Media: holding statement approved by counsel through the public information officer; no technical details, ransom, or attribution comments.
- Staff: briefings at each shift change by radio, overhead page, and runners.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Clinical communications: analog lines and radios, then VoIP and smartphones | 0.5 h | Test calls from every unit |
| 2 | Identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 3 | Campus core network, then the monitoring segment | 1 h | Clean segments only; device rules re-applied |
| 4 | Monitoring gateway and central stations | 1 h | Biomedical engineering confirms alarm delivery |
| 5 | Clean endpoints for the ED, ICU, pharmacy, laboratory, and nursing stations | 2 h | 20 pre-imaged spare laptops; EDR healthy |
| 6 | EHR access (vendor-hosted) | 2 h target (vendor commits to 12 h) | Vendor integrity statement; interfaces re-enabled last |
| 7 | LIS and blood bank; dispensing cabinet server; pump server | 2 h | Pharmacy verifies drug library and cabinet profiles; laboratory verifies blood bank records |
| 8 | Fetal surveillance server and cardiology system | 2 h | Manufacturer validation |
| 9 | PACS and RIS | 2 h | Restore from pre-compromise backup; reconcile with modality local storage |
| 10 | Building OT on its own segment | 2 h | Facilities confirms setpoints and alarms |
| 11 | SIEM feeds and EDR console | 4 h | Monitoring confirmed before wider reconnection |
| 12 | Interface engine | 8 h | Restore; test messages; reconnect the reference laboratory, HIE, public health, and clearinghouse |
| 13 | Affiliated practice access | 8 h after EHR availability | Practice users re-enabled after credential checks |
| 14 | Clearinghouse connectivity and claims backlog | 48 h | Credentials rotated; test batch accepted |
| 15 | File services, payroll, then the data warehouse | 24 h, 72 h, 120 h | Restore; permissions review |

**Coming off diversion.** Clinical command ends diversion only when the ED, laboratory, CT, phones, and EHR (or stable paper workflows with enough staff) are back, and tells county EMS and the nearby hospitals at once.

Back-enter downtime documentation within 72 hours of restoration under HIM direction; paper records stay in locked unit binders until reconciled (POL-04 4.8). Keep downtime forms in use until each process is back within its RTO. Tell staff, patients, county EMS, the practices, and partners when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.15).
- Update the risk register (P01: R-001, R-002, R-003, R-005, R-006, R-010), the POA&M (P07), this runbook, and the emergency operations plan and its IT outage annex.
- Record the emergency plan activation and the after-action analysis in the emergency program binder (42 CFR 482.15(d)(2)(iii)). Under 482.15(d)(2)(i)(B), an actual emergency that activates the plan exempts the hospital from its next required full-scale community-based or facility-based functional exercise.
- Retain all incident documentation, including the decision log, diversion log, and notices, for 6 years (POL-01 4.13; 45 CFR 164.414(b) burden of proof).

# Incident Response Runbook: Ransomware with PHI Exfiltration

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed multi-specialty physician group with an ASC and an imaging center) |
| Tier / Vertical | Mid-Market / Health Care and Social Assistance |
| Incident type | Ransomware with exfiltration of PHI (double extortion) affecting the Enterprise Clinical Platform |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-vendor-outage.md` (clearinghouse or major vendor outage); `notification-matrix.csv`; BIA (P05); ASC emergency preparedness plan |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Executive tabletop with outside counsel scheduled 2026-11-12 (POAM-013); ASC cyber tabletop 2026-11-18 (POAM-022) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, business, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, Chief Medical Officer, vCISO, IT Director, Compliance and Privacy Officer, Director of Marketing and Communications, HR Director, outside breach counsel | Business continuity, patient diversion or cancellations, external statements, ransom decision (recommendation to the CEO), resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director (recovery lead), security analysts, MSSP, forensic firm (through counsel), EHR, PACS, and cloud vendor contacts | Containment, investigation, eradication, recovery sequence |
| **Clinical command** | Chief Medical Officer, ASC Administrator and ASC Medical Director, Imaging Center Director, Director of Clinic Operations | Downtime procedures, ASC emergency plan activation, case cancellations, patient safety |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Breach and privacy decisions | Compliance and Privacy Officer | Outside breach counsel | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | Company's outside general counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($10M limit, $250K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Communications | Director of Marketing and Communications | Outside crisis PR (through counsel) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, and VoIP are compromised. The CMT and IRT use a pre-provisioned messaging group on personal phones and printed call trees kept at every site.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in email or chat.

## 1. Preparation checks (Identify / Protect)
- [x] Immutable backups in the separate backup account, 35-day write-once retention (CP-9; P07 fully satisfied)
- [x] EDR on all managed endpoints with 24x7 MSSP (SI-3; P07 fully satisfied)
- [ ] Restore test of the interface engine, PACS, and data warehouse within the last 90 days (CP-4). **Gap until POAM-010 closes**
- [ ] Break-glass accounts sealed and tested for the IdP, EHR admin, cloud, and PACS (POL-02 4.9). **Gap for IdP, EHR, and PACS**
- [x] Downtime report workstation at each site with an hourly extract
- [ ] ASC cyber downtime procedures and pump manual-programming checklist (POAM-022)
- [x] Incident binder at every site: this runbook, call tree, downtime forms, notification matrix
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-15
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption | EDR alert; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Backup deletion attempts, or disabling of EDR or logging | Cloud audit logs; EDR tamper alert | Treat as ransomware precursor; declare |
| Privileged account anomaly (new domain admin, just-in-time elevation outside hours) | SIEM; access broker | Disable the account; declare if unexplained |
| Large outbound transfer from file services, data warehouse, or PACS | Cloud firewall flow logs (egress alerting due 2027-01-31) | Block the destination; declare |
| Extortion email or leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve the message |
| Clinic or ASC reports systems unavailable across a site | Staff report | IT triage; declare if malicious |

**Severity 1 (declare immediately):** any confirmed ransomware execution, confirmed PHI exfiltration, or an extortion claim naming company data.

**Record the date and time of discovery in the incident log** (POL-03 4.3). Under 45 CFR 164.404(a)(2), a breach is treated as discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member or agent. This date can start the HIPAA 60-day clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR (network containment); keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Operating Officer | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Sever site-to-cloud VPN tunnels and cloud hub routes to affected segments; block known attacker infrastructure | IT Director | Routes down or filtered |
| 0-2 h | Revoke all sessions in the IdP; reset privileged credentials using break-glass accounts; disable vendor remote access | Security Manager | Sessions revoked |
| 0-2 h | Activate downtime procedures at all affected sites. **ASC:** ASC Administrator decides whether to activate the ASC emergency plan and whether to start cases not yet begun (MTD 4 h) | Clinical command | Paper workflows running; decision documented |
| 1-2 h | Convene the CMT; first situation report (scope, patient impact, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing script: what happened, downtime steps, do not discuss externally, report anything unusual | Director of Marketing and Communications with HR | Script sent by text and posted at sites |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, servers, cloud accounts, and identities are affected? Use EDR telemetry, IdP sign-in logs, cloud control-plane logs in the locked log bucket, and firewall flow logs.
2. **Initial access and dwell time.** Identify the entry point (phishing, an exposed edge appliance, or vendor remote access), the first compromised account, and the date the attacker first got in.
3. **Preserve evidence.** Forensics images key hosts and exports logs before retention expires, with chain of custody (who collected, when, hash, storage). Evidence is held by the forensic firm under counsel.
4. **Exfiltration.** Determine what PHI was accessed or taken. Look for archive tools, staging directories, cloud storage access, egress volume, and leak-site samples. Build the **affected individuals list** by data element and state of residence. **This drives the breach determination and every notice.**
5. **Medical devices.** Clinical engineering and vendors check the ASC pump server, modalities, and device VLANs for spread. Pumps continue on their last library; manual programming uses independent double-check.
6. **Vendor status.** Confirm the EHR (SaaS), identity provider, and MSSP are unaffected. If a vendor is the source, also follow `ir-runbook-vendor-outage.md`.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at site firewalls, SD-WAN, and the cloud firewall.
2. Disable compromised accounts. Rotate service account, interface, and vendor credentials (interface engine, clearinghouse, labs, PACS vendor).
3. Rebuild affected endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads from clean images in the isolated recovery network. Restore data from backups taken before the attacker's first access.
5. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts) is removed before reconnection.
6. Legacy modality consoles: reconnect only after the vendor validates them, and only to their restricted flows.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice before it goes out. The Compliance and Privacy Officer keeps the **decision log** (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a breach of unsecured PHI? Presumed yes unless a four-factor assessment (45 CFR 164.402) shows low probability of compromise. Encrypted data with uncompromised keys is not unsecured PHI | Compliance and Privacy Officer with counsel | Decision log with the four factors |
| D2 | Date of discovery (HIPAA clock) and date of determination (Florida clock) | Compliance and Privacy Officer | Decision log |
| D3 | Number of affected individuals in total, by state, and Florida residents (thresholds: 500 for HHS contemporaneous notice and Florida Department of Legal Affairs; more than 500 residents of a state for media; more than 1,000 for Florida consumer reporting agencies) | Compliance and Privacy Officer | Affected individuals list |
| D4 | Has law enforcement asked for a delay? If oral, document it; the delay lasts no longer than 30 days unless confirmed in writing (164.412) | Counsel | Decision log |
| D5 | Contract notices due (hospital joint venture partner, payers, lenders)? | Counsel and CFO | Contract register |
| D6 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | COO |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA. It helps the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Security Manager through counsel |
| Day 0-3 | Joint venture partner notice per the joint venture agreement (contract term) | COO through counsel |
| As soon as scoped | Four-factor assessment documented (D1) | Compliance and Privacy Officer |
| Within 30 days of determination | Florida individual notice (or HIPAA notice, with a copy to the Department of Legal Affairs under the deemed-compliance path); Department of Legal Affairs notice if 500 or more Floridians | Compliance and Privacy Officer and counsel |
| Without unreasonable delay, no later than 60 days after discovery | HIPAA individual notices (first-class mail; substitute notice with a 90-day toll-free number if 10 or more addresses are out of date); HHS notice at the same time if 500 or more; media notice if more than 500 residents of a state | Compliance and Privacy Officer and counsel |
| Without unreasonable delay | Consumer reporting agencies if Florida notice goes to more than 1,000 individuals at once | Counsel |
| Each other state | Residents of other states: apply each state's law (counsel checks the affected list by state) | Counsel |
| Within 60 days after year end | HHS log entry for any breach under 500 | Compliance and Privacy Officer |
| Within 10 work days of awareness | FDA medical device report if information reasonably suggests a device (for example a compromised pump or modality) caused or contributed to a death (FDA and manufacturer) or serious injury (manufacturer) at the ASC or imaging center (21 CFR 803.30) | ASC Administrator or Imaging Center Director with the Chief Medical Officer |

**Why the shorter clock matters.** Florida's 30 days run from the determination of a breach. HIPAA's 60 days are an outer limit that runs from discovery. If determination comes soon after discovery, Florida's deadline arrives first. Counsel decides early whether one HIPAA-compliant notice with a timely copy to the Department of Legal Affairs will satisfy Florida.

**Ransom decision (POL-03 4.8).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove breach notification duties if data was taken, and does not guarantee deletion. The default position, approved by the CEO, is not to pay while backups are intact.

**Communications.**
- Patients: a website notice and call-center script within 24 hours of any visible disruption, with a patient hotline through the insurer's notification vendor.
- Referring providers and the hospital joint venture partner: a direct call from the Chief Medical Officer or COO.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments.
- Staff: daily text or phone briefings; the out-of-band channel only.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 2 | SD-WAN and site networks, ASC first | 2 h | Clean segments only; device VLAN rules re-applied |
| 3 | Clean endpoints for the ASC, then clinic front desks and providers | 2 h (ASC), 4 h (clinics) | Pre-imaged spares; EDR healthy |
| 4 | EHR access (vendor-hosted) | 2 h ASC read access, 4 h full | Vendor integrity statement; re-enable interfaces last |
| 5 | ASC infusion pump server and device VLAN | 8 h | Library version verified by pharmacy consultant |
| 6 | PACS and RIS | 6 h | Restore from pre-compromise backup; reconcile with modality local storage |
| 7 | Interface engine | 8 h | Restore; test messages; reconnect labs and clearinghouse |
| 8 | SIEM feeds and EDR console | 8 h | Monitoring confirmed before wider reconnection |
| 9 | Clearinghouse connectivity and claims backlog | 48 h | Credentials rotated; test batch accepted |
| 10 | File services, payroll, then data warehouse | 24 h, 72 h, 120 h | Restore; permissions review |

Back-enter downtime documentation within 72 hours of restoration. Keep downtime forms in use until each process is back within its RTO. Tell staff, patients, referring providers, and the joint venture partner when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-001, R-002, R-009, R-050), the POA&M (P07), this runbook, and the ASC emergency plan.
- Record the ASC emergency plan activation and the after-action analysis. Under 42 CFR 416.54(d)(2)(i)(B), an actual emergency that activates the plan exempts the ASC from its next required community-based or facility-based functional exercise.
- Retain all incident documentation, including the decision log and notices, for 6 years (POL-01 4.12; 45 CFR 164.414(b) burden of proof).

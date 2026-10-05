# Incident Response Runbook: Ransomware on Dispatch and Train Control Back-Office Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Class II regional freight railroad, north and central Florida) |
| Tier / Vertical | Mid-Market / Transportation Systems |
| Incident type | Ransomware that reaches, or threatens, the Train Dispatch and PTC Operations Platform (TDPO): the CAD/CTC office system, the PTC back office server (BOS) pair, dispatch consoles, crew management, and the dispatch zones. Usually starts in corporate IT (phishing, an exposed edge device, or a vendor path) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy; this runbook is part of the Cybersecurity Incident Response Plan required by SD 1580-21-01E II.D |
| Companion documents | `ir-runbook-vendor-outage.md` (TMS vendor ransomware or extended outage); `notification-matrix.csv`; BIA (P05); manual dispatch procedure; hazmat security plan |
| Runbook owner | Cybersecurity Manager (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet as written. First end-to-end CAD/CTC restore 2026-11-05 (POAM-011); operations-led exercise with IT/OT isolation and CTC-territory manual dispatch 2026-12-10 (POAM-012) |
| Handling | The company's live copy names contacts, network segments, and isolation points and is SSI. This sample omits them |

## 0. Governance, roles, and contacts (Govern)
The response runs on three teams, so safety, technical, and business decisions each have one owner. **Train safety decisions are never waiting on IT.**

| Team | Members | Decides |
|---|---|---|
| **Operations command** | Lead: Director of Network Operations; Chief Dispatcher on duty (acts until the Director arrives); Director of Signals and Communications; PTC Program Manager; Director of Safety, Security, and Hazmat | Stopping or holding trains; manual dispatch; local control point operation; holding trackage-rights trains; RSSM answers to TSA; FRA and hazmat reports |
| **Incident response team (IRT)** | Incident commander: Cybersecurity Manager. Director of IT (recovery lead), security engineers, OT security engineer, MSSP, forensic firm (through counsel), CAD/CTC vendor, PTC vendor | Containment, isolation (with operations command), investigation, eradication, recovery sequence; CISA reports |
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, Director of Network Operations, Director of Safety, Security, and Hazmat, HR Director, Director of Customer Service and Car Management, outside counsel | Business continuity, shipper and partner communications, external statements, ransom recommendation to the CEO, spending |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Cybersecurity Manager | Director of IT | Out-of-band group on company-issued phones on a separate carrier plan; printed call tree at both NOCs |
| Operations command lead | Director of Network Operations | Chief Dispatcher on duty | NOC hotline; radio |
| TSA Security Coordinator (1570.203, 1520.9(c), RSSM) | Director of Safety, Security, and Hazmat | Chief Dispatcher on duty | Out-of-band group |
| TSA Cybersecurity Coordinator (CISA report) | Cybersecurity Manager | Director of IT | Out-of-band group |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel), through the General Counsel | Company's outside general counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($15 million limit, $500,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm with OT experience, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | OT security engineer for OT alerts | MSSP hotline |
| CAD/CTC and PTC vendors | Vendor emergency support lines | Account managers | Numbers in the binder; access only through the PAM jump host |
| Host railroad and interchange partners | Host Class I's designated officer (PTC); interchange partner operations centers | Director of Network Operations | Numbers in the binder |
| Shared service clients | Each affiliate's and the contracted short line's operations contact | Director of Customer Service and Car Management | Numbers in the binder |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, VoIP, and the directory are compromised. Teams use the pre-provisioned messaging group and printed call trees. **Train radio stays on the radio system**; if the radio gateways are suspect, dispatchers use the fixed-channel fallback consoles that do not depend on the IP network.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel." Keep facts (timeline, logs) separate from legal conclusions. The CISA and TSA reports are made on facts; counsel reviews them but must not delay them.

## 1. Preparation checks (Identify / Protect)
- [x] Write-once backups of CAD/CTC, BOS, crew management, and file services in the separate backup account, 35-day retention, separate credentials, scanned at backup time (CP-9; P07 fully satisfied)
- [x] EDR on all Windows endpoints and servers, including dispatch consoles, with MSSP 24x7 monitoring of IT (SI-3; P07 fully satisfied)
- [x] Boundary firewall isolation profile at the HQ data center and both NOCs (closes all IT-to-dispatch-zone flows except the documented emergency set)
- [ ] End-to-end restore of CAD/CTC and the BOS in the clean-room environment within the last 90 days (CP-4). **Gap until POAM-011 closes (first test 2026-11-05)**
- [ ] Manual dispatch in CTC territory drilled in the last 12 months. **Gap until 2026-12-10 (POAM-010, POAM-012)**
- [ ] CAD/CTC, BOS, and field logs collected centrally (AU-2). **Gap until POAM-006 closes; until then, preserve local logs at once (step 3)**
- [x] 6 pre-imaged spare consoles at each NOC, kept offline and checked monthly
- [x] RSSM standby extract on 2 offline laptops at each NOC, refreshed every 4 hours (every 2 hours while PIH cars are in the HTUA from 2026-10-31, POAM-019); printed list at the NOCs
- [x] Break-glass accounts for the identity provider, directory, cloud organization, PAM, CAD/CTC, and BOS, sealed at each NOC (POL-02 4.10)
- [x] Incident binder at both NOCs: this runbook, call trees, manual dispatch forms, the notification matrix, CISA report template v2 with the directive statement
- [x] Insurer panel counsel and forensic firm confirmed; contact list verified 2026-09-15

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renaming or encryption on any server or endpoint | EDR alert; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Any EDR alert, unexpected reboot, or application failure on a dispatch console, CAD/CTC server, BOS, or PTC administration workstation | EDR; dispatcher report to the Chief Dispatcher | Chief Dispatcher calls the incident commander at once; treat as Severity 1 until ruled out |
| Unexpected CTC indications, routes, or signal requests that no dispatcher made | Dispatcher; signal maintainer | Chief Dispatcher stops issuing CTC authority in the affected territory and moves it to track warrants (section 3); call the incident commander |
| Backup deletion attempts, disabling of EDR or logging, or new privileged accounts | Cloud audit logs; EDR tamper alert; PAM | Treat as a ransomware precursor; declare |
| Lateral movement toward the IT/OT boundary (scans, remote execution attempts against dispatch zone addresses) | Boundary firewall logs; OT sensors at the NOCs | Declare; prepare the isolation decision (D1) |
| Extortion email, or a leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve the message |

**Severity 1 (declare immediately):** confirmed ransomware execution anywhere in the company, any malicious activity in a dispatch zone or on the BOS, or an extortion claim naming company data.

**Record the identification time in the incident log** (POL-03 4.3). The CISA 72-hour clock runs from the time the company identifies a cybersecurity incident, and the 1570.203 24-hour clock from initial discovery. The directive's definition includes events still under investigation, so the clock does not wait for proof.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | **Safety step.** If any TDPO component is suspect, the Chief Dispatcher stops issuing CTC authority from the affected consoles, holds trains at the next safe location, and starts manual dispatch: track warrants by radio in dark territory, and in CTC territory local control point operation by signal maintainers or track warrants over the CTC territory under the manual dispatch procedure. Vital field logic keeps signals safe on its own | Chief Dispatcher on duty | Every train accounted for on the paper train sheet; no conflicting authority |
| 0-30 min | Isolate affected IT hosts through EDR (network containment); keep them powered on for memory evidence | MSSP; security engineers | Hosts contained |
| 0-30 min | Declare Severity 1; open the out-of-band channel; start the incident log with the identification time | Incident commander | Log open |
| 0-30 min | **D1 isolation decision** (section 6). If there is any sign the attack can reach the dispatch zones, apply the boundary isolation profile at the HQ data center and both NOCs and cut the radio vendor and detector paths | Incident commander after informing the Director of Network Operations; COO confirms within 1 hour if traffic stops network-wide | Isolation applied and recorded, or a recorded decision not to isolate |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Operating Officer | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | Director of IT | Backup integrity confirmed |
| 0-60 min | **Break the standby link.** Stop replication from the primary CAD/CTC cluster to the hot standby at the backup NOC so that corruption does not replicate; do the same for the BOS pair if the primary BOS is suspect | Director of IT with the CAD/CTC vendor | Replication stopped; standby state preserved |
| 0-60 min | Preserve local CAD/CTC, BOS, and field controller logs (about 30 days locally) before they overwrite | OT security engineer | Copies hashed and stored |
| 0-2 h | Revoke all sessions in the identity provider; reset privileged credentials using break-glass accounts; disable all vendor access in PAM | Cybersecurity Manager | Sessions revoked |
| 0-2 h | **PTC.** If the BOS is suspect or isolated, hold trackage-rights trains or run them under the host's PTC failure procedure; report en route failures to the host's designated officer (236.1029(b)(4)) | PTC Program Manager with the Chief Dispatcher | Host informed; trains held or moving under the host's rules |
| 0-2 h | **RSSM.** Confirm the standby extract and printed list are current; the Chief Dispatcher can answer a TSA request within 30 minutes | Director of Safety, Security, and Hazmat | Answer ready |
| 0-12 h | **TSOC call** (IC Surface-2025-01 recommendation, and the start of the 1570.203 report) | Director of Safety, Security, and Hazmat | Call logged with the TSOC reference |
| 1-2 h | Convene the CMT; first situation report (scope, trains held, safety status, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Notify the affiliated short lines (and, from 2027-01-01, the contracted short line) that dispatch is manual; Class I host and interchange partners get operations calls | Director of Network Operations; Director of Customer Service and Car Management | Calls logged |
| 2-4 h | CEO informs the audit committee chair and the sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, servers, cloud accounts, and identities are affected? Did anything cross the IT/OT boundary? Use EDR telemetry, identity provider sign-in logs, boundary firewall logs, the OT sensors at the HQ data center and both NOCs, PAM session records, and the cloud control-plane logs in the locked log bucket.
2. **Field check.** Signal maintainers and the OT security engineer check the CTC field communication controllers at a sample of control points (starting with the 6 hub towers) for configuration changes against the last recorded baseline. Any unexplained change keeps that territory in manual operation until it is restored from a known-good configuration.
3. **Initial access and dwell time.** Identify the entry point (phishing, an exposed edge appliance, the radio or detector vendor path, or the PTC or CAD/CTC vendor session through the jump host), the first compromised account, and the date the attacker first got in. This sets the **restore point**: the last backup taken before the first access.
4. **Preserve evidence.** Forensics images key hosts and exports logs before retention expires, with chain of custody (who collected, when, hash, storage). Keep partially encrypted storage (SD 1580-21-01E II.D.1.a.iv).
5. **Exfiltration.** Determine what was taken. Look for archive tools, staging directories, cloud storage access, egress volume, and leak-site samples. Two questions drive the notices: **was SSI taken** (the CIP, CAP, network designs) and **was personal information taken** (ERP, HR files, crew records)?
6. **Vendor status.** Confirm the TMS, identity provider, MSSP, and cloud provider are unaffected. If the TMS vendor is the source or is also hit, run `ir-runbook-vendor-outage.md` in parallel.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the perimeter, the SD-WAN, the boundary firewalls, and the cloud firewall.
2. Disable compromised accounts. Rotate service account, vendor, and shared field credentials (POL-02 4.2), the TMS consist feed credentials, and the PTC messaging credentials with the host's agreement.
3. Rebuild affected IT endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild CAD/CTC and BOS servers in the clean-room environment in the operations workloads account from vendor media and the pre-compromise backup, scan the restored images, then deploy to the dispatch zone (STD-07).
5. Replace dispatch consoles with the pre-imaged spares; wipe the old consoles.
6. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts, firewall rule changes) is removed before reconnection.

## 6. Decision points and legal, regulatory, and external communication (RS.CO)
| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Isolate the dispatch zones and field network from IT? Default: **yes** whenever ransomware is confirmed in IT and its path to the boundary is unknown. Isolation keeps CAD/CTC running for dispatchers if CAD/CTC is clean; it cuts the TMS consist feed, crew management, and email from the dispatch zone | Incident commander after informing the Director of Network Operations; COO confirms within 1 hour if traffic stops network-wide (POL-03 4.7) | Incident log with the time and reason |
| D2 | Run trains under manual dispatch, and in which territories? Hold trains carrying PIH cars until authority is confirmed | Chief Dispatcher on duty, then the Director of Network Operations | Train sheet and decision log |
| D3 | Is this a cybersecurity incident under the directive (yes if unauthorized access, malicious software, denial of service, or potential operational disruption)? Identification time? | Incident commander | Decision log; drives the 72-hour CISA clock |
| D4 | Was SSI released to unauthorized persons? | Director of Safety, Security, and Hazmat with counsel | Decision log; TSA report under 1520.9(c) |
| D5 | Was personal information breached? Date of determination (Florida clock)? Affected list by state? | General Counsel with outside counsel | Decision log; affected individuals list |
| D6 | Did the incident cause or contribute to a reportable accident/incident or hazmat incident? | Director of Safety, Security, and Hazmat | FRA and NRC report records |
| D7 | Ransom decision | CEO, on CMT recommendation, after the OFAC check and law enforcement report | See below |
| D8 | Reconnect a restored system to the dispatch zone? | Incident commander, with forensics sign-off for that segment | Recovery checklist |

**Reporting timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | COO |
| Within 12 hours of discovery | TSOC telephone call (IC Surface-2025-01; company practice) | Director of Safety, Security, and Hazmat |
| Within 24 hours of initial discovery | 1570.203 report to TSA met, either by the CISA report below if it names the directive (SD 1580-21-01E II.C.5) or by a TSOC report with the 1570.203(c) content | Director of Safety, Security, and Hazmat with the Cybersecurity Manager |
| Target 24 hours, no later than 72 hours after identification | CISA report through www.cisa.gov/report or (844) 729-2472, stating it is made to satisfy SD 1580-21-01E, with the II.C.4 content: affected systems and locations, earliest known compromise, detection date, who has been notified, indicators, impact on train operations, and planned responses, including **reversion to manual operations of train movement and control** | Cybersecurity Manager |
| Within 24 hours of new information | Supplemental CISA reports | Cybersecurity Manager |
| Within 24 hours of confirming the incident | Notice to the shared service client railroads (contract) | Director of Customer Service and Car Management through counsel |
| Day 0-2 | Voluntary report to the FBI; it helps the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Cybersecurity Manager through counsel |
| Immediately | Notice to TSA if the incident prevents a directive measure on time (SD 1580-21-01E III.C) | Cybersecurity Manager |
| Promptly | TSA notice of SSI release (1520.9(c)), if D4 is yes | Director of Safety, Security, and Hazmat |
| Immediately / 12 hours / monthly | NRC telephone report (225.9) or hazmat notice (171.15), and the monthly FRA report (225.11), only if D6 is yes | Director of Safety, Security, and Hazmat |
| Within 30 days of determination | Florida individual notices and, for 500 or more Floridians, the Department of Legal Affairs; consumer reporting agencies if more than 1,000; other states' laws for non-residents | General Counsel and outside counsel |

**Ransom decision (POL-03 4.11).** Needs the CEO, after consulting the sponsor's operating partner, General Counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet; and a report to law enforcement. Paying does not remove reporting or breach notice duties and does not make a decrypted system trustworthy: CAD/CTC and the BOS are rebuilt regardless. The default position, approved by the CEO, is not to pay while clean backups exist.

**Communications.**
- Shippers: a portal and email notice within 24 hours of any visible service impact, through the Director of Customer Service and Car Management, using a holding statement approved by counsel.
- Class I partners and the host: operations calls from the Director of Network Operations, then written updates each shift.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments. **Never describe security measures or vulnerabilities** in public statements (SSI).
- Employees: shift briefings through the NOC; the out-of-band channel only; a reminder not to discuss the incident outside the company.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 8). Each step is validated before the next begins: EDR healthy, credentials rotated, patches applied to the vendor-certified level, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | RSSM fallback and out-of-band communications | 0.5 h (procedural) | TSA request answerable in 30 minutes |
| 2 | Identity provider, directory for the dispatch zones, and PAM (break-glass if needed) | 1 h | Sessions revoked; privileged and shared credentials rotated |
| 3 | Dispatch zones, boundary firewalls, clean consoles at the primary or backup NOC | 2 h | Isolation profile in place; pre-imaged spares only |
| 4 | CAD/CTC office system: the preserved standby if forensics confirms it is clean, otherwise a clean-room rebuild from the pre-compromise backup | 2 h | Train sheets reconciled with the paper train sheet; authority in force re-entered and checked by a second dispatcher before CTC control resumes |
| 5 | CTC code line and radio | 2 h (radio), 4 h (code line) | Field controller configurations compared with the known-good baseline before each territory returns to CTC |
| 6 | PTC back office (standby BOS or rebuild) | 6 h | Host's PTC system accepts messages; a test train initializes; consist data verified |
| 7 | Crew management | 6 h | Hours of duty records back-entered from the printed crew boards |
| 8 | TMS consist feed and access (vendor) | 8 h | Feed credentials rotated; consists compared with the printed consists |
| 9 | SIEM feeds, EDR console, and OT sensors | 8 h | Monitoring confirmed before wider reconnection |
| 10 | Interchange EDI | 12 h | Test files with each Class I partner |
| 11 | Email and file services | 12 h | Restored from backups taken before the first access |
| 12 | ERP and payroll | 48 h | Repeat the prior payroll if needed |
| 13 | Data warehouse and billing | 72 h | Bill from the last waybill extract |

**Return to CTC operation** is a safety decision. The Director of Network Operations returns each territory to CTC only after D8 is recorded for CAD/CTC and the field controllers in that territory, and after every dispatcher on duty has been briefed. Back-enter train sheets, warrants, and the dispatcher log within 72 hours (3-year retention, POL-04 4.8). Tell shippers, partners, and the shared service clients when service is restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.14), including the operations command decisions and how long manual dispatch ran.
- Update the risk register (P01: R-001, R-003, R-005, R-009, R-049), the POA&M (P07), this runbook, the manual dispatch procedure, and dispatcher and maintainer role training.
- If the incident changed Critical Cyber Systems or CIP measures permanently, file a CIP amendment within 50 days (POL-01 4.5). Include the incident and its lessons in the next CAP annual report.
- Keep the incident record, the decision log, and the reports for at least 5 years (POL-01 4.14). The record is SSI where it describes vulnerabilities (POL-04).

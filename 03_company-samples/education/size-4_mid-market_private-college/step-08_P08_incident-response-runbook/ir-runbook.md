# Incident Response Runbook: Ransomware with Student Record Exposure

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed private, for-profit college) |
| Tier / Vertical | Mid-Market / Educational Services |
| Incident type | Ransomware with exfiltration of student and financial aid records (double extortion) affecting the Student Information and Learning Platform (SILP) and campus systems |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy; together with POL-03 this runbook is part of the written incident response plan required by 16 CFR 314.4(h) |
| Companion documents | `ir-runbook-identity-fraud.md` (account takeover, refund diversion, fraudulent applicants); `notification-matrix.csv`; BIA (P05); IT DR plan (due 2026-12-31, POAM-010); Clery emergency procedures |
| Runbook owner | Information Security Manager (incident commander) |
| Approved | 2026-09-17 by the Chief Information Officer |
| Last tested | Not yet. Executive tabletop with outside counsel scheduled 2026-11-10 (POAM-014) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, business, and legal decisions each have a clear owner (314.4(h)(3)).

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Information Officer. President and CEO, CFO, Provost, Vice President of Student Affairs, vCISO (Qualified Individual), Chief Compliance Officer, General Counsel, Director of Marketing and Communications, HR Director, outside breach counsel | Teaching and campus continuity, term or exam changes, external statements, ransom recommendation to the CEO, resources |
| **Incident response team (IRT)** | Incident commander: Information Security Manager. Infrastructure team (recovery), security analysts, MSSP, forensic firm (through counsel), SIS, LMS, FAMS, identity, and cloud vendor contacts | Containment, investigation, eradication, recovery sequence |
| **Student services command** | Registrar, Director of Financial Aid, Bursar, Dean of Online Learning, Director of Campus Safety, Campus Directors | Paper workarounds, exam rescheduling, refund continuity, Clery emergency notification |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Information Security Manager | Senior security analyst | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Information Officer | President and CEO | Out-of-band group |
| Notification and breach decisions | Chief Compliance Officer | General Counsel | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | General Counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($5M limit, $150K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Communications | Director of Marketing and Communications | Outside crisis PR (through counsel) | Out-of-band group |
| Board, audit committee, and PE sponsor | CEO informs the board chair, the audit committee chair, and the sponsor's operating partner | CIO | Phone |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, and the phone system are compromised. The CMT and IRT use a pre-provisioned messaging group on personal phones and printed call trees kept at each campus.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in email or chat.

## 1. Preparation checks (Identify / Protect)
- [x] Immutable backups in the separate backup account, 30-day write-once retention (CP-9; P07 fully satisfied)
- [x] EDR on all staff endpoints and cloud servers with 24x7 MSSP
- [ ] Restore test of the integration platform, data warehouse, and partner portal in the last 90 days (CP-4). **Gap until POAM-011 closes; the 2026-08-13 attempt failed**
- [ ] IT DR plan (CP-2). **Gap until POAM-010 closes**
- [ ] Break-glass accounts sealed and tested for the identity provider, SIS, LMS, FAMS, cloud, and **emergency notification console** (POL-02 4.10). **Gap for SIS, LMS, FAMS, and the notification console (POAM-024)**
- [ ] SIS, FAMS, and LMS logs in the SIEM to scope record access (POAM-006)
- [x] Incident binder at each campus: this runbook, call tree, paper forms, notification matrix
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-17
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption | EDR alert; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Backup deletion attempts, or disabling of EDR or logging | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| Privileged account anomaly (new administrator, SaaS admin sign-in from a new country) | SIEM; access broker; identity provider | Disable the account; declare if unexplained |
| Large outbound transfer from the data warehouse, file services, or integration platform | Cloud firewall flow logs (egress alerting due 2027-01-31) | Block the destination; declare |
| Extortion email or leak-site post naming the college | Email; threat intelligence; FBI | Declare; preserve the message |
| A campus or the online division reports systems unavailable across a site | Staff report; service desk | IT triage; declare if malicious |

**Severity 1 (declare immediately):** any confirmed ransomware execution, confirmed exfiltration of customer information or education records, or an extortion claim naming college data.

**Record the date and time of discovery in the incident log** (POL-03 4.3). For the FTC notice, a notification event is treated as discovered on the first day it is known to any employee, officer, or other agent other than the person committing the breach (16 CFR 314.4(j)(2)). That date starts the 30-day FTC clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR (network containment); keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log with the discovery time | Incident commander | Log open |
| 0-30 min | **Campus safety check:** confirm the emergency notification console works through the break-glass path and that doors and cameras are operating. If an immediate threat exists, issue a Clery emergency notification (34 CFR 668.46(g)(1)) | Director of Campus Safety | Confirmed and logged |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Financial Officer | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | Chief Information Officer | Backup integrity confirmed |
| 0-2 h | Sever site-to-cloud VPN tunnels and hub routes to affected segments (Campus 3 first if involved); block known attacker infrastructure | Infrastructure team | Routes down or filtered |
| 0-2 h | Revoke all sessions in the identity provider; reset privileged credentials using break-glass accounts; disable integration service accounts and vendor remote access | Information Security Manager | Sessions revoked |
| 0-2 h | Activate paper workarounds (P05): printed rosters, paper add/drop, exam rescheduling notice for online students | Student services command | Workarounds running |
| 1-2 h | Convene the CMT; first situation report (scope, teaching impact, aid and refund impact, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing script: what happened, workarounds, do not discuss externally, report anything unusual | Director of Marketing and Communications with HR | Script sent by text and posted at campuses |
| 2-4 h | **File the FSA breach report** (suspected breach is enough; do not wait for forensics) | Chief Compliance Officer | Intake form submitted; time logged |
| 2-4 h | CEO informs the board chair, the audit committee chair, and the PE sponsor's operating partner | President and CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, servers, cloud accounts, SaaS tenants, and identities are affected? Use EDR telemetry, identity provider sign-in logs, cloud control-plane logs in the write-once bucket, firewall flow logs, and the SaaS vendors' audit logs (request exports now, because SIS and FAMS logs are kept only 180 days).
2. **Initial access and dwell time.** Identify the entry point (phishing, a stolen SaaS admin session, the Campus 3 flat network, a lab computer, or vendor remote access), the first compromised account, and the date the attacker first got in.
3. **Preserve evidence.** Forensics images key hosts and exports logs before retention expires, with chain of custody (who collected, when, hash, storage). Evidence is held by the forensic firm under counsel.
4. **Exfiltration.** Determine what was accessed or taken: integration platform files (refund files, ISIR extracts), the data warehouse, file services (aid spreadsheets), and any SaaS exports. Build the **affected individuals list** by data element (SSN, bank details, ISIR data, grades, user names with passwords) and **state of residence**. Separate customer information (FTC count) from education records (FERPA disclosure records). **This list drives every notice.**
5. **Campus safety systems.** If Campus 3 is involved, check door controllers and video recorders for tampering; keep doors on local control.
6. **Vendor status.** Confirm the SIS, LMS, FAMS, identity provider, and MSSP are unaffected. If a vendor is the source, its notice to the college under its contract and Fla. Stat. 501.171(6) also applies.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at campus firewalls, SD-WAN, and the cloud firewall.
2. Disable compromised accounts. Rotate service account, integration, SAIG workstation, and vendor credentials (bank file transfer, servicer, payment plan vendor).
3. Rebuild affected endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads from clean images in an isolated recovery network. Restore data from backups taken before the attacker's first access.
5. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts, new OAuth grants in SaaS tenants) is removed before reconnection.
6. Before restoring the SAIG workstations, tell FSA what happened and follow its instructions for reconnecting.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice before it goes out. The Chief Compliance Officer keeps the **decision log** (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a **notification event** under 16 CFR 314.2(m)? Unauthorized access to unencrypted customer information is presumed to be acquisition unless reliable evidence shows otherwise; encrypted data counts as unencrypted if the key was accessed | Chief Compliance Officer with counsel | Decision log |
| D2 | Number of affected consumers (500 or more triggers the FTC notice within 30 days of discovery) | Chief Compliance Officer | Affected individuals list |
| D3 | Date of discovery (FTC clock) and date of determination (state clocks, for example Florida) | Chief Compliance Officer | Decision log |
| D4 | For each state of residence, is this a breach under that state's law, and who must be notified (residents, attorney general or other regulator, consumer reporting agencies)? Florida worked example: 30 days from determination for individuals and, if 500 or more Floridians, the Department of Legal Affairs; more than 1,000 at once means consumer reporting agencies | General Counsel with outside counsel | State-by-state table |
| D5 | Has law enforcement asked for a delay? The FTC notice is still due within 30 days and must include the written determination (314.4(j)(1)(vi)); state delays follow each state's rule (Florida: written request, 501.171(4)(b)) | Counsel | Decision log |
| D6 | Contract notices due (employer partners within 72 hours, lender, PE sponsor)? | Counsel and CFO | Contract register |
| D7 | Ransom decision | President and CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | Chief Financial Officer |
| Hours 2-4 | **FSA breach report** through the Cybersecurity Breach Intake (immediately upon suspicion) | Chief Compliance Officer |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA. It helps the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Information Security Manager through counsel |
| Day 0-3 | Employer partner notice per the partner agreements (72 hours from confirmation) | Director of Corporate Partnerships through counsel |
| As soon as scoped | D1 to D4 documented | Chief Compliance Officer |
| No later than 30 days after discovery | **FTC notice** if 500 or more consumers (form at ftc.gov) | Chief Compliance Officer and counsel |
| No later than 30 days after determination | Florida individual notice, and the Department of Legal Affairs if 500 or more Floridians (15 more days for individuals only, with good cause in writing) | Chief Compliance Officer and counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 Floridians are notified at once | General Counsel |
| Per each state's law | Residents and regulators in the other states on the affected list | Outside counsel |
| When confirmed | FERPA disclosure record in each affected student's record (34 CFR 99.32(a)) | Registrar |
| Next annual report (October) | Qualified Individual reports the event and response to the board (314.4(i)(2)) | vCISO |

**Why the FTC clock usually comes first.** The FTC's 30 days run from discovery, which can be the first day any employee knew. State clocks such as Florida's run from determination, which comes later. The FTC notice goes to the FTC, not to students; student notices come from state law, because neither the Safeguards Rule nor FERPA requires notice to individuals.

**Ransom decision (POL-03 4.8).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove notification duties if data was taken, and does not guarantee deletion. The default position, approved by the CEO, is not to pay while backups are intact. **CIRCIA** ransom payment reporting is proposed only and not yet required.

**Communications.**
- Students: portal and website notice and a call-center script within 24 hours of any visible disruption; exam and deadline changes from the Provost; a student hotline through the insurer's notification vendor once notices go out.
- Employer partners: a direct call from the Director of Corporate Partnerships, then the written notice.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments.
- Staff and faculty: daily text briefings; the out-of-band channel only.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Emergency notification console (break-glass) | 30 min | Test message to the Campus Safety group |
| 2 | Identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 3 | Clean endpoints for the registrar, financial aid, student accounts, and the service desk | 4 h | Pre-imaged spares; EDR healthy |
| 4 | LMS and proctoring access (vendor-hosted) | 6 h | Vendor integrity statement; re-enable integrations last |
| 5 | SIS access (vendor-hosted) | 8 h | Vendor integrity statement; check for unauthorized changes to refund bank details |
| 6 | Email suite | 8 h | Mail rules and OAuth grants reviewed |
| 7 | Integration platform | 24 h | Restore; test each interface; reconcile the last refund file with the bank before sending a new one |
| 8 | FAMS and SAIG workstations | 24 h | FSA guidance followed; ISIRs re-requested if needed |
| 9 | Campus networks (Campus 3 last, after segmentation checks) | 24 h | Clean segments only |
| 10 | Employer partner portal | 24 h | Restore; partner sign-in test |
| 11 | ERP payroll, then data warehouse | 48 h, 120 h | Restore; permissions review |

**Refund continuity.** If refunds are due during the outage, the Bursar runs the emergency paper-check procedure from the last reconciled refund file so that no credit balance passes the 14-day limit (34 CFR 668.164(h)(2)).

Back-enter paper records within 72 hours of restoration. Tell students, faculty, staff, and employer partners when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days, including the remediation of weaknesses found (POL-03 4.12; 314.4(h)(5), (h)(7)).
- Update the risk register (P01: R-001, R-002, R-009, R-014), the POA&M (P07), this runbook, the IT DR plan, and the Clery procedures.
- Re-run the risk assessment for affected systems (314.4(b)(2)).
- Include the event and the response in the Qualified Individual's next written board report (314.4(i)(2)).
- Retain all incident documentation, including the decision log and notices, for at least 6 years (POL-01 4.14); Florida no-harm determinations for at least 5 years.

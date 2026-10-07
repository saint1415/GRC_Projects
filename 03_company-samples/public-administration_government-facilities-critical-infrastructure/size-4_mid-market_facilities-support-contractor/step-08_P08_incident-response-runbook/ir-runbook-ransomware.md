# Incident Response Runbook: Ransomware with Data Theft in the Corporate and Cloud Environment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed facilities support contractor operating government buildings) |
| Tier / Vertical | Mid-Market / Government Services and Facilities |
| Incident type | Ransomware that encrypts corporate IT and cloud workloads (BAS clusters, broker, file storage), disrupts the ROC, and steals data (cardholder records, drawings, GSA CUI, employee records) for extortion |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook.md` (OT intrusion; use it too if field devices or tenants are touched); `notification-matrix.csv`; BIA (P05) |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Ransomware tabletop with outside counsel and the insurer scheduled 2026-12-09 (POAM-012) |

## 0. Why this runbook exists
Ransomware is the company's most likely business-wide crisis (P01 R-002, High). The company runs building monitoring for 46 government sites from one cloud landing zone and one primary ROC. An attack there affects all four state and local customers at once and starts five different notice clocks. The County A clock for suspected ransomware is the shortest: 6 hours.

## 1. Roles (Govern)
The same three tiers as `ir-runbook.md` (CMT, IRT, building operations command), with these differences:
- **IRT recovery lead:** IT Director, with the MSSP's incident response team and the insurer panel forensic firm (through counsel).
- **Finance lead:** CFO for insurance, cash, and any payment question.
- **Business continuity lead:** VP Operations, who runs the 46 sites by hand and moves the ROC to the backup site if needed.

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption | EDR alert; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the Security Manager within 30 minutes |
| Attempts to delete backups, or to disable EDR, logging, or guardrails | Cloud audit logs; EDR tamper alert; guardrail alerts | Treat as a ransomware precursor; declare |
| Privileged account anomaly (new administrator, just-in-time elevation outside hours) | SIEM; broker | Disable the account; declare if unexplained |
| Large outbound transfer from the CUI library or file storage | Hub firewall flow logs | Block the destination; declare |
| Extortion email or leak-site post naming the company or a customer | Email; threat intelligence; FBI | Declare; preserve the message |
| ROC consoles or BAS clusters unavailable | ROC; Building Technology | IT triage; declare if malicious |

**Severity 1 (declare immediately):** any confirmed ransomware execution, confirmed data theft, or an extortion claim naming company or customer data.

**Record the time of discovery.** Suspected ransomware starts the **County A 6-hour contract clock**, and through County A and the City, their own **12-hour** ransomware reports to the state (Fla. Stat. 282.3185(5)(b)1.). The state agency has the same 12-hour duty (Fla. Stat. 282.318(3)(c)9.c.(I)).

## 3. First 6 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Security Manager | Log open |
| 0-60 min | Call the insurer hotline before engaging any vendor; counsel engaged; forensics engaged by counsel | General Counsel | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Building safety: ROC confirms every site's alarm status; if the primary ROC is affected, fail over to the backup ROC; site managers walk critical sites; the EOC and the state data center building go to local operator control | VP Operations | All 46 sites accounted for; critical rooms stable |
| 0-2 h | Sever site-to-cloud tunnels from affected segments; block attacker infrastructure at the hub; suspend broker sessions | IT Director; OT Security Engineer | Routes down or filtered |
| 0-2 h | Revoke all identity provider sessions; reset privileged credentials with break-glass accounts; disable subcontractor access | Security Manager | Sessions revoked |
| 1-2 h | Convene the CMT; situation report (sites affected, safety, data at risk, clocks running) | CMT chair | Meeting held |
| 2-6 h | **County A notice within 6 hours of discovering suspected ransomware**; state, County B, and City notices started early so they can meet their 12-hour reports | Program managers with General Counsel | Notices sent and logged |
| 2-6 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |
| 2-6 h | Staff briefing by text: what happened, work by phone and paper, do not discuss externally | VP Operations with HR | Script sent |

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, cloud accounts, clusters, and identities are affected? Use EDR telemetry, identity provider sign-in logs, cloud audit logs in the write-once bucket, and hub flow logs.
2. **Initial access and dwell time.** Phishing, an exposed edge appliance, a subcontractor path, or a compromised customer network? First compromised account and first date of access.
3. **Preserve evidence.** Forensics images key hosts and exports logs, with chain of custody. Evidence is held by the forensic firm under counsel.
4. **Exfiltration.** What was taken? Cardholder records (about 41,000 people), face templates, drawings and security system layouts, GSA CUI, employee and applicant records. Build the **affected individuals list** by data element and state of residence, and an **affected customer list**. This drives every notice.
5. **OT check.** Did the attacker reach BAS clusters, tenants, or site networks? If yes, also run `ir-runbook.md` sections 3 to 5.
6. **Vendors.** Confirm the access control SaaS vendor, identity provider, CMMS, and MSSP are unaffected.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the hub, the edge firewalls, and the identity provider.
2. Disable compromised accounts; rotate service account, broker vault, and subcontractor credentials.
3. Rebuild affected endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads in an isolated recovery network from clean images; restore data from backups taken before the attacker's first access.
5. Forensics confirms persistence is removed before reconnection.

## 6. Legal, regulatory, and customer communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel keeps the decision log (discovery time, determination time, data elements, residency, customers affected).

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | General Counsel |
| Within 6 hours | County A contract notice (suspected ransomware) | County A Program Manager with General Counsel |
| Within 24 hours | State, County B, and City contract notices (sent earlier, within hours, so their 12-hour state reports can be made) | Program managers |
| Within 48 hours | School district notice if its connection or data is involved | City and Schools Program Manager |
| Immediately | GSA IT if GSA CUI, GSA data, or staff with GSA access may be involved | Federal Program Manager |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA | Security Manager through counsel |
| No later than 10 days after determination | Third-party agent notice to each affected customer (Fla. Stat. 501.171(6)(a)) | General Counsel |
| No later than 30 days after determination | Employee and applicant notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 (Fla. Stat. 501.171(3)-(5)) | General Counsel |
| Each other state | Apply the law of each state where affected individuals reside | General Counsel |
| 1 or 3 business days | FAR clause reports if covered items are involved | Contracts Director |
| Within 1 week after remediation | Input to county and city after-action reports (Fla. Stat. 282.3185(6)) | Security Manager |

**Ransom decision (POL-03 4.8).**
- **Never on a customer's behalf.** Florida state agencies, counties, and municipalities may not pay or otherwise comply with a ransom demand (Fla. Stat. 282.3186). The company will not pay to recover customer systems or customer data.
- **For the company's own systems:** the CEO decides on the CMT's recommendation, with General Counsel and the insurer, after an **OFAC sanctions check** on the threat actor and any wallet (civil penalties can apply on a strict liability basis), and after reporting to law enforcement. Paying does not remove any notice duty and does not guarantee deletion.
- **Default position, approved by the CEO:** do not pay while isolated backups are intact.
- **CIRCIA:** the proposed 24-hour ransom payment report is **not yet required**; the final rule had not been published as of 2026-09-25.

**Communications.**
- Customers: program manager calls, then written notices; COO calls each customer executive for severity 1.
- Media: holding statement approved by General Counsel; no ransom, attribution, or technical details. Customers lead statements about their buildings.
- Staff and subcontractors: daily text or phone briefings on the out-of-band channel.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider and break-glass administrator access | 1 h | Sessions revoked; privileged credentials rotated |
| 2 | Local operator control at the EOC and the state data center building | 0 h (local) | Critical rooms stable |
| 3 | ROC (backup ROC if the primary is affected) | 2 h | Clean workstations; alarm consoles live |
| 4 | Remote access broker | 2 h | Rebuilt from a clean image; vault secrets rotated |
| 5 | SIEM and EDR consoles | 4 h | Monitoring confirmed before wider reconnection |
| 6 | Tenant administrator access (vendor-hosted) | 4 h | Administrator credentials rotated |
| 7 | Email, chat, and phones | 8 h | Clean tenant; mailbox rules checked |
| 8 | BAS clusters, County A and CT-S first | 12 h | Restored from pre-compromise backups; programs hash-checked |
| 9 | CMMS (vendor-hosted) and back-entry of paper work orders | 24 h | Reconciled |
| 10 | Controller program repository, ERP, and HR suite | 48 h (payroll), 72 h (ERP) | Restore; permissions review |

Keep manual-mode procedures and paper work orders in use until each process is back within its RTO. Tell each customer in writing when monitoring and administration are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with each affected customer; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-002, R-005, R-006, R-009, R-024), the POA&M (P07), and both runbooks.
- Keep all incident records, the decision log, and notices for at least 3 years, or longer where a contract or a customer's public records schedule requires (POL-01 4.12).

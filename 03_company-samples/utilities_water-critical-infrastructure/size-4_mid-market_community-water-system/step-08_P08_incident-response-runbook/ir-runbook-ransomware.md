# Incident Response Runbook: Ransomware with Customer Data Theft in Business IT

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed investor-owned water utility; Utility Services for 3 municipal clients) |
| Tier / Vertical | Mid-Market / Water and Wastewater Systems |
| Incident type | Ransomware encrypts business endpoints, servers, and cloud file services, after the attacker has copied customer data (double extortion). Affects customer service, billing for own and client accounts, field dispatch, and possibly the CIS through stolen administrator credentials. OT is not the target but must be protected from spread |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy (statements 4.2 to 4.8, 4.12); POL-04 |
| Companion documents | `ir-runbook.md` (OT HMI compromise); `notification-matrix.csv`; BIA (P05 BP-08, BP-10 to BP-14, BP-16); risk register (P01 R-005, R-006, R-035) |
| Runbook owner | Security Manager (incident commander), with the General Counsel for all notice decisions |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Executive ransomware tabletop with breach counsel scheduled 2027-02-24 (POAM-023) |

**Two rules shape this runbook.** First, water treatment does not depend on business IT, so the first technical goal is to keep the attack out of OT. Second, the Florida 30-day clocks run from the determination of a breach, so the General Counsel must document that date as soon as it is known.

## 0. Governance, roles, and contacts (Govern)
| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, General Counsel, CFO, vCISO, IT Director, Director of Water Operations, Director of Customer Service, Director of Utility Services, Communications Manager, HR Director; breach counsel | Business continuity, customer and client communications, ransom recommendation to the CEO, resources, regulator and law enforcement contact |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director (recovery lead), security analysts, MSSP, forensic firm (through counsel), CIS vendor, cloud and identity provider contacts | Containment, investigation, eradication, recovery sequence |
| **Operations command** | Director of Water Operations, ROC Supervisor, Plant Managers | Confirms plants and the ROC are unaffected; decides any OT isolation; keeps client alarm monitoring running |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Breach and notice decisions; decision log | General Counsel | Breach counsel | Out-of-band group |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card |
| Forensics and breach counsel | Insurer panel firms | MSSP incident response team | Through the insurer |
| Customer and client communications | Communications Manager with the Director of Customer Service and the Director of Utility Services | Outside crisis PR (through counsel) | Out-of-band group |
| Finance and cash | Chief Financial Officer | Controller | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office (and IC3) | CISA | ERP binder |

**Out-of-band first.** Assume email, chat, and the phone system's administration are compromised. **Legal privilege protocol:** counsel engages forensics; analysis is labeled "Privileged and confidential, prepared at the direction of counsel"; facts are kept separate from legal conclusions; no speculation in writing.

## 1. Preparation checks (Identify / Protect)
- [x] Immutable cloud backups in a separate account and region, 35-day write-once retention (P04)
- [x] EDR on all managed endpoints with 24x7 MSSP; MFA for all users
- [x] Regional IT/OT firewall deny-by-default; OT DMZ (P02 SC-7 at Regional)
- [ ] Lakes historian dual-homed to the business LAN (POAM-002, 2026-12-31). Until fixed, the Lakes historian's business interface is the first thing to disconnect
- [ ] Privileged access management for directory and SaaS administrators; service accounts vaulted (POAM-021, 2027-03-31)
- [ ] Company-held weekly export of CIS billing data and a tested restore of company data (P01 R-035)
- [ ] Bulk-export alerting in the CIS (POAM-023, 2026-12-31)
- [ ] Decision log template and client notice roles agreed with each municipal client (POAM-023, 2027-02-28)
- [x] Insurer panel counsel and forensics confirmed for 2026
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption | EDR alert; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Backup deletion attempts; EDR or logging disabled | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| Privileged account anomaly (new directory administrator; elevation outside hours) | SIEM; identity provider | Disable the account; declare if unexplained |
| Bulk export from the CIS or large outbound transfer from file services | CIS audit log; cloud firewall flow logs | Block the destination; declare |
| Extortion email or leak-site post naming the company or a municipal client | Email; threat intelligence; FBI; client | Declare; preserve the message |
| CIS vendor reports a cyber incident | Vendor notice | Follow section 4 step 5; declare if company or client data may be involved |

**Severity 1 (declare immediately):** confirmed ransomware execution, confirmed exfiltration of customer data, or an extortion claim naming company or client data.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | **Protect OT:** block all business-network flows to the OT DMZ at the IT/OT firewall except historian replication outbound; disconnect the Lakes historian's business interface; disable gateway sessions except approved emergency use; confirm with the ROC that plants and client monitoring are normal | IT Director; ROC Supervisor | OT isolated from business IT; ROC confirms normal operation |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-60 min | Call the insurer hotline before engaging any vendor; counsel engaged; counsel engages forensics | Chief Operating Officer | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention is intact; suspend cross-account jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Revoke all sessions in the identity provider; reset privileged credentials with break-glass accounts; rotate CIS administrator credentials and API keys with the CIS vendor | Security Manager | Sessions revoked |
| 0-2 h | Activate business workarounds (P05): contact center scripts and paper forms; printed map books for field dispatch; estimated billing hold | Director of Customer Service; Distribution and Field Services Director | Workarounds running |
| 1-2 h | Convene the CMT; first situation report (scope, data at risk, client impact, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing script by text and posted at sites | Communications Manager with HR | Script sent |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, servers, cloud accounts, SaaS tenants, and identities are affected. Sources: EDR telemetry, identity provider sign-in logs, cloud control-plane logs in the locked log bucket, CIS audit logs, and firewall flow logs.
2. **Initial access and dwell time.** Phishing, an exposed edge device, a stolen administrator or service account (P01 R-031, R-032), or a vendor.
3. **OT check.** The OT security analyst reviews Regional sensor alerts, gateway logs, and the Lakes historian for any sign of spread. If found, also start `ir-runbook.md`.
4. **Exfiltration and the affected list.** Determine what personal information was accessed or taken: own customers, client customers (by client), and employees. Build the **affected individuals list** by data element and state of residence (about 6% of customers have out-of-state billing addresses). Florida personal information includes a name with a financial account number plus any code or password needed to access that account, and a user name or email address with a password or security question that permits access to an online account (Fla. Stat. 501.171(1)(g)). Counsel decides which records meet the definition. **This list drives every notice.**
5. **Vendor status.** Confirm with the CIS, AMI, LIMS, and identity provider vendors whether their platforms are affected. If the CIS vendor is the source, it must notify the company within 10 days of its determination (501.171(6)(a)); the company still owns the notices.
6. **Preserve evidence** with chain of custody; forensics holds it under counsel.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the firewalls and the cloud firewall.
2. Disable compromised accounts; rotate service account, integration, and vendor credentials.
3. Rebuild affected endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads from clean images; restore data from backups taken before the attacker's first access.
5. Forensics confirms persistence is removed before reconnection. OT flows are restored last, after the IRT and the Director of Water Operations agree.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** The General Counsel keeps the decision log (POL-03 statement 4.5) and confirms every notice.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Date of determination of a breach or reason to believe a breach occurred (starts the Florida 30-day clocks) | General Counsel | Decision log |
| D2 | Number of affected Floridians (500 or more: Department of Legal Affairs; more than 1,000 at a single time: consumer reporting agencies) and residents of other states | General Counsel with forensics | Affected individuals list |
| D3 | Is notice not required because the breach will not likely result in identity theft or other financial harm (501.171(4)(c))? If so, document it, keep it 5 years, and send it to the Department within 30 days | General Counsel after consulting law enforcement | Written determination |
| D4 | Has law enforcement asked in writing to delay individual notice (501.171(4)(b))? | General Counsel | Copy of the request |
| D5 | Client data affected? As a third-party agent, notify each client no later than 10 days after determination (501.171(6)(a)); contracts require 24 hours. Who sends notices to the client's customers? | General Counsel and Director of Utility Services | Client notice record |
| D6 | Is public notice needed because water service or notice capability is affected (for example the CIS call campaign tool is down during a Tier 1 situation)? | Water Quality and Compliance Manager | Decision log |
| D7 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | Chief Operating Officer |
| Within 24 h of declaration | Municipal clients notified if their data or monitoring may be affected (contract) | Director of Utility Services |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA; it supports the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Security Manager through counsel |
| No later than 10 days after determination | Statutory third-party agent notice to each affected client (501.171(6)(a)), if not already given under the contract | General Counsel |
| No later than 30 days after determination | Florida individual notices by mail or email with the required content (501.171(4)); Department of Legal Affairs notice if 500 or more Floridians (501.171(3)). The 15-day extension in 501.171(3)(a) applies only to the individual notice, and only with good cause given to the Department in writing within the 30 days | General Counsel; Director of Customer Service; notification vendor |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at a single time (501.171(5)) | General Counsel |
| Per each state's law | Residents of other states: counsel applies each state's breach law to the affected list (most will be seasonal residents) | General Counsel |
| Per contract | Payment processor, if the customer portal's link to the hosted payment page could have been altered; lenders, if loan covenants require notice | CFO |

**Ransom decision (POL-03 statement 4.8).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove notice duties if data was taken. The default position, approved by the CEO, is not to pay while backups are intact and water operations are unaffected.

**Communications.**
- Customers: website and IVR message within 24 hours of any visible disruption ("billing and payments delayed; water service and water quality are not affected" only if the ROC has confirmed it); call center script; notification vendor hotline once notices go out.
- Municipal clients: direct call from the Director of Utility Services, then written notice; agree who tells their customers.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments.
- Staff: daily briefings through the out-of-band channel and posted at sites.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, and forensics sign-off.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Water operations and client alarm monitoring confirmed unaffected (no restore needed if isolated) | 2 h | ROC Supervisor confirmation; OT analyst review |
| 2 | Identity provider and administrator access (break-glass if needed) | 2 h | Sessions revoked; privileged credentials rotated |
| 3 | Public notice capability (offline exports, media lists, templates) | 4 h | Exports less than 31 days old |
| 4 | Clean endpoints for the contact center, dispatch, and the laboratory | 8 h | Pre-imaged spares; EDR healthy |
| 5 | LIMS access and compliance reporting | 8 h | Vendor confirmation; monthly report export available |
| 6 | Contact center phones and CIS access | 8 h | CIS credentials rotated; vendor integrity statement |
| 7 | Field dispatch, work orders, and GIS | 8 h | Restored access; printed map books until then |
| 8 | File services and the data lake | 24-72 h | Restore from pre-compromise backup; permissions review |
| 9 | Client billing, then own billing | 48 h, then 72 h | Test cycle; client approval for any delayed cycle |
| 10 | Payroll, HR, and finance close | 72 h | Vendor access restored; manual payroll if needed |
| 11 | AMI, analytics, engineering systems | 120-168 h | Restore; reconnect the OT DMZ replica last |

Tell customers and clients when billing and payments are back to normal (RC.CO). Waive late fees for the outage period, as the CFO approves.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 statement 4.13).
- Update the risk register (P01 R-005, R-006, R-031, R-032, R-035), the POA&M, this runbook, and the SOC 2 readiness file (P09 CC7.4 and CC7.5 evidence).
- Retain all incident documentation, the decision log, notices, and any no-notice determination for at least 5 years (POL-01 statement 4.14; Fla. Stat. 501.171(4)(c)).

# Incident Response Runbook: Ransomware That Disrupts Operations

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Mid-Market / Communications |
| Incident type | Ransomware on corporate IT and the cloud production account (OSS, mediation, portal, data warehouse), with possible data theft, that halts care, provisioning, dispatch, and billing; variant where the attacker also reaches the NOC tools or the management plane and causes a service outage |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF RC.RP and RC.CO |
| Policy basis | POL-03 Incident Response Policy (4.4, 4.5, 4.8); STD-07 Contingency and recovery standard |
| Companion documents | `ir-runbook.md` (network intrusion exposing CPNI); `notification-matrix.csv`; BIA (P05); NOC outage and storm plan; IT contingency plan (due 2026-12-31, POAM-009) |
| Runbook owner | IT Director (recovery lead) with the Security Manager (incident commander) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Covered in the 2026-11-19 tabletop (POAM-012); first mediation restore test 2026-11-12 (POAM-010) |

## 0. Why this runbook exists
A carrier's network keeps passing traffic, including 911 calls, when corporate IT is encrypted. The business does not: care agents lose the BSS agent desktop if workstations are encrypted, provisioning and dispatch stop with the OSS, and after 72 hours switch CDR buffers start to overflow (P05 BP-13). The two dangers specific to a carrier are (1) the attack spreading from IT into the NOC tools or the management plane, which would turn an IT outage into a 911-affecting network outage with FCC clocks, and (2) data theft from the CDR archive or the BSS, which would add the CPNI process in `ir-runbook.md`.

## 1. Roles (Govern)
The three tiers in `ir-runbook.md` section 0 apply. Differences for this incident:

| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Incident commander | Security Manager | vCISO | Runs the response with the MDR and forensics |
| Recovery lead | IT Director | Director of Network Engineering | Restore order, clean builds, backup integrity |
| Network protection lead | Director of Network Engineering | NOC Director | Keep the management plane and NOC isolated from infected IT; decide on cutting the site-to-cloud VPN |
| Service and regulatory clocks | NOC Director | Vice President of Network Operations | PSAP, NORS, DIRS if service is affected |
| Customer operations | Director of Customer Operations | Customer Care Manager | Callback queue, offline account report, scripts, chatbot outage mode |
| Business Services | Director of Business Services | n/a | Hosted voice and SD-WAN customer notices under contract |
| Finance | Chief Financial Officer | Controller | Billing holds, cash forecast, lender notice |
| Legal and ransom decision support | General Counsel; breach counsel | n/a | Privilege, OFAC check, notices |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renaming, or encryption alerts | EDR; MDR; staff report | MDR isolates hosts (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Attempts to delete backups, disable EDR, or change cloud guardrails | Cloud audit logs; EDR tamper alerts | Treat as a ransomware precursor; declare |
| New privileged accounts or use of break-glass accounts | SIEM; PAM | Disable the account; declare if unexplained |
| OSS, BSS agent desktop, or mediation unavailable across sites | NOC; care center | IT triage; declare if malicious |
| Extortion email or leak-site post naming company data | Email; threat intelligence; FBI | Declare; preserve the message; start the CPNI determination in `ir-runbook.md` |

**Severity 1:** any confirmed ransomware execution, any sign of activity in the management plane or NOC tools, or an extortion claim naming customer data.

**Record the time of discovery.** If the NOC loses tools and any service is affected, that time starts the PSAP and NORS clocks.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MDR; security analysts | Hosts contained |
| 0-30 min | **Protect the network first.** Cut routes between corporate VLANs and the management plane at CO-1, CO-4, and the POPs; disable the site-to-cloud VPN if cloud workloads are affected; NOC moves to clean consoles or to CO-4 | Director of Network Engineering; NOC Director | Management plane reachable only from clean jump hosts |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-30 min | **Service check.** Is voice, 911, broadband, hosted voice, or any business circuit affected? If 911 is or may be affected, notify PSAPs within 30 minutes and start the NORS clock | NOC Director | Decision recorded; PSAPs notified if needed |
| 0-60 min | Call the insurer hotline before engaging vendors; counsel engaged; counsel engages forensics | Chief Operating Officer | Claim number |
| 0-60 min | Protect the backup account: confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Revoke all IdP sessions; reset privileged credentials using break-glass accounts; disable vendor remote access | Security Manager | Sessions revoked |
| 0-2 h | Customer operations downtime mode: callback queue, hourly offline account report from the BSS vendor, chatbot to outage-message mode, status page | Director of Customer Operations | Downtime mode running |
| 1-2 h | Convene the CMT; first situation report | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing script; field crews switch to phone dispatch from the NOC | HR Director; Manager of Field Operations | Script sent; dispatch running |
| 2-4 h | CEO informs the audit committee chair and the sponsor; CFO assesses lender notice | CEO; CFO | Notices given |

## 4. Analysis (RS.AN)
1. **Scope:** which endpoints, servers, cloud accounts, identities, and NOC tools are affected. Use EDR telemetry, IdP logs, and the cloud control-plane logs in the write-once log archive.
2. **Initial access and dwell time:** phishing, an exposed remote access appliance, a vendor account, or a cloud credential. Find the first compromised account and when it was used.
3. **Network spread check:** review jump host, TACACS+, and element login records for any attacker use. If there is any sign of management plane activity, also follow `ir-runbook.md` sections 3 to 5.
4. **Data theft:** look for archive tools, staging, cloud storage access, and egress volume from the CDR archive, data warehouse, and file shares. **If CPNI may have been taken, start the reasonable-determination step in `ir-runbook.md` section 6.**
5. **Evidence:** forensics images key hosts and exports logs before retention expires, with chain of custody, under counsel.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the internet edges and the cloud firewall.
2. Disable compromised accounts; rotate service account, API, and vendor credentials (BSS API, chatbot API client, CCaaS integrations, mediation).
3. Rebuild affected endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads from clean images in an isolated recovery subnet; restore data from backups taken before the attacker's first access.
5. Forensics confirms persistence is removed before reconnection to the management plane or the site-to-cloud VPN.

## 6. Regulatory, contractual, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each notice.

| When | Action | Owner | Basis |
|---|---|---|---|
| Within 30 minutes of discovering an outage that potentially affects a PSAP | PSAP notice; follow-up within 2 hours | NOC Director | 47 CFR 4.9(h) |
| Within 120 minutes (wireline) or 240 minutes or 24 hours (VoIP) | NORS notification; reports at 72 hours (wireline) and 30 days | NOC Director | 47 CFR 4.9(f), (g) |
| Hour 0-1 | Insurer hotline; counsel engaged | Chief Operating Officer | Contract |
| Day 0-2 | Voluntary report to the FBI and CISA | Security Manager through counsel | Voluntary (CIRCIA not in effect) |
| Within 24 hours of confirming the incident | Business Services customers whose services or data are affected | Director of Business Services | Contracts |
| Within 5 business days if approval flags are corrupted | Letter to the FCC on opt-out mechanism failure | Vice President of Regulatory Affairs | 47 CFR 64.2009(f) |
| Within 24 hours of any traceback request received during the outage | Traceback response from CDR queries (restore mediation access for the regulatory team first if needed) | Vice President of Regulatory Affairs | 47 CFR 64.6305(a)(2) |
| If CPNI was taken | CPNI process in `ir-runbook.md` section 6 (7-business-day law enforcement notice; 7-full-business-day hold) | Vice President of Regulatory Affairs | 47 CFR 64.2011 |
| If Florida-defined personal information was taken | Florida notices within 30 days of determination; other states per their law | General Counsel | Fla. Stat. 501.171 |

**Ransom decision (POL-03 4.8).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove notice duties if data was taken. The default position, approved by the CEO, is not to pay while the backup account is intact (P07 found CP-9 satisfied).

**Communications.**
- Customers: status page and recorded IVR message within 1 hour of visible disruption ("billing and account services are temporarily limited; your phone and internet service is not affected" only if that is confirmed by the NOC).
- Business Services customers: direct calls from their account representatives.
- Media: holding statement approved by counsel.
- Staff: daily briefings on the out-of-band channel.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). The network is protected first; IT is rebuilt behind it.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | NOC monitoring and management plane on clean consoles | 0.5 h | No attacker activity; 911-tagged alarms visible |
| 2 | Identity provider and administrator access | 1 h | Sessions revoked; privileged credentials rotated |
| 3 | Clean endpoints for care agents, the NOC, and dispatch | 4 h | Pre-imaged spares (40 at CO-1, 15 at CO-4); EDR healthy |
| 4 | BSS access (vendor-hosted) and contact center | 8 h | Vendor confirms no compromise; API keys rotated |
| 5 | OSS (dispatch first, then provisioning) | 8 h dispatch; 24 h provisioning | Restore validated in the isolated subnet |
| 6 | SIEM feeds and EDR console | 8 h | Monitoring confirmed before wider reconnection |
| 7 | Portal, app, and chatbot | 24 h | Gateway allow-list verified |
| 8 | Mediation and rating | Before 72 h | CDR counts reconcile with switch buffers |
| 9 | SYS-18 legacy CLEC billing; payroll and finance SaaS | 72 h | Restore validated |
| 10 | Data warehouse | 168 h | Approval-filtered views re-applied before any model runs |

Keep downtime procedures in place until each process is back within its RTO. Back-enter provisioning orders and tickets within 72 hours. Tell customers and Business Services customers when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-003, R-026, R-027), the POA&M (POAM-009, POAM-010), the IT contingency plan, and this runbook.
- Final NORS report within 30 days if a report was filed.
- Retain incident documentation at least 3 years (POL-01 4.13), and CPNI breach records at least 2 years (47 CFR 64.2011(d)).

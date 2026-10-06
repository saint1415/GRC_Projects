# Incident Response Runbook: Ransomware Affecting Agency Systems Holding CJI and FTI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Mid-Market / Public Administration |
| Incident type | Ransomware spread through the managed services remote management platform (SYS-10) to agency-hosted servers holding CJI (AG-02) and into the company network and ACMC administration environment, with data theft that may include FTI from the AG-01 enclave |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-insider-misuse.md` (insider access to FTI, CJI, or motor vehicle records); `notification-matrix.csv`; BIA (P05); contingency plan (STD-07, due 2026-12-31) |
| Runbook owner | Security Operations Manager (incident commander) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Agency tabletop with the AG-01, AG-02, and AG-03 security contacts scheduled 2026-12-15 (POAM-012) |

**Why this incident.** It is the company's only Very High risk scenario before testing (P01 R-001), and P07 made it more likely by finding an exposed SYS-10 automation token (R-050). Ransomware delivered through remote management tools is a known pattern against managed service providers: one compromised console reaches every customer at once.

**Whose clocks.** Most legal clocks belong to the **agencies**: the sheriffs' CJIS reporting, AG-01's 24-hour IRS reporting, and every Florida agency's 12-hour ransomware report. The company's job is to tell each agency fast enough and give it the facts it must report. The company's own legal clock is the 10-day third-party agent notice under Fla. Stat. 501.171(6)(a), plus the law of each other state as mapped by counsel.

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, business, legal, and agency decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, CTO, General Counsel, vCISO, Director of Information Security, Director of Contracts and Compliance, VP of Customer Delivery, HR Director, outside breach counsel | Business continuity, customer communications, external statements, ransom recommendation to the CEO, resources |
| **Incident response team (IRT)** | Incident commander: Security Operations Manager. Director of Cloud Operations (ACMC recovery lead), Director of Managed Services (agency systems lead), security engineers, MDR provider, forensic firm (through counsel), cloud and SYS-10 vendor contacts | Containment, investigation, eradication, recovery sequence |
| **Agency coordination cell** | Lead: Director of Contracts and Compliance. Director of Customer Support, account directors, and each agency's named security contact | Agency notices and fact sheets, agency decisions on their own systems, reconnection approvals |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Operations Manager | Director of Information Security | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Agency notices and breach determinations | Director of Contracts and Compliance | General Counsel | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel), engaged by the General Counsel | General Counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MDR provider incident response team | Through counsel |
| Monitoring and first response | MDR provider 24x7 security operations center | n/a | MDR hotline |
| ACMC recovery | Director of Cloud Operations | FTI enclave administrator group lead | On-call phone |
| Agency systems recovery | Director of Managed Services | Managed services shift lead | On-call phone |
| Agency security contacts | AG-01 disclosure officer; AG-02 local agency security officer; AG-03 information security manager; AG-04 records custodian; AG-39 terminal agency coordinator; IT contacts for the other agencies | Named alternates in each contract | Printed contact list in the incident binder |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume the attacker can read company email, chat, tickets, and SYS-10, and may hold identity provider sessions. Coordinate on personal phones and the printed contact list. **Never put FTI, CJI, or motor vehicle record data in the incident log, email, or tickets** (POL-03 4.3).

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions.

## 1. Preparation checks (Identify / Protect)
- [x] Write-once backups in the separate backup account and region B, 35-day retention (CP-9; P07 fully satisfied)
- [x] Write-once log archive that production administrators cannot delete (AU-9; P07 fully satisfied)
- [x] Phishing-resistant keys and just-in-time elevation for cloud administrators
- [ ] SYS-10 automation tokens scoped, vaulted, and rotated; agency credentials vaulted per session (IA-5). **Gap until POAM-003 closes (2027-01-31)**. The exposed token was revoked on 2026-08-19
- [ ] SYS-10 sessions recorded and SYS-10 logs in the SIEM (MA-4, SI-4). **Gap until POAM-003 and POAM-006 close**
- [ ] No SYS-10 path into the landing zone (AC-17). **Gap until 2026-12-31**
- [ ] Central "disable all agents" procedure agreed with the SYS-10 vendor (R-013). **Due 2027-03-31**
- [ ] Timed restore of each regulated tenant within 8 hours (CP-4). **Gap until POAM-009 closes**
- [x] Incident binder at both offices and with each on-call lead: this runbook, the notification matrix, the agency contact list, and the agency fact sheet template (section 6.2)
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-17
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Scripts or software pushed through SYS-10 outside a work order, or many agency servers changing at once | SYS-10 console; agency EDR; agency IT calls | Director of Managed Services suspends SYS-10 automation and calls the incident commander |
| Ransom note, mass file encryption, or EDR ransomware detection on a jump server, engineer laptop, or agency server | EDR (company or agency); staff report | MDR or agency isolates the host; incident commander declares within 30 minutes |
| Use of the revoked SYS-10 token or an unknown SYS-10 API client | SYS-10 audit log | Treat as ransomware precursor; declare |
| Database instances, snapshots, keys, or logging changed outside a change ticket in any landing zone account (including the FTI enclave key) | Cloud audit log alert through the MDR | Declare. Protect the vault and log archive first |
| A managed services or administrator session from an unfamiliar network, or push MFA prompts the user did not start | Identity provider logs; user report | Revoke sessions; open an incident |
| Large outbound transfer from containers, storage, the analytics service, or a jump server | Network hub flow logs; export alerts (due 2026-12-31) | Block the destination; declare |
| Extortion email to the company or an agency, or a leak-site post naming the company or a customer | Email; agency; threat intelligence; FBI | Declare; preserve the message |

**Severity 1 (declare immediately and convene the CMT):** confirmed ransomware execution on any company or agency system the company administers; administrator rights in the ACMC used by an unknown actor; confirmed theft of agency data; or an extortion claim naming company or agency data. When in doubt, declare. The first reports to agencies are for **suspected** incidents.

**Record the time of discovery** in the incident log (T0). Clocks that start there:
- the 1-hour CJI report (CJISSECPOL IR-6a), which also covers ransomware found in AG-02's own servers;
- the 24-hour FTI report by AG-01, which must not wait for an internal investigation (Pub. 1075 sec. 1.8.4);
- the 12-hour ransomware reports by Florida agencies, which run from **their** discovery. In practice that is when the company tells them, so the company tells them within the first hour.

The 10-day clock under Fla. Stat. 501.171(6)(a) starts at the determination of a breach "or reason to believe the breach occurred," which in a data-theft case can be the same day.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | **Cut the spread path:** disable SYS-10 automation and all SYS-10 sessions; ask the vendor to suspend the tenant; block SYS-10 at the network hub and at each agency jump server (agency IT does this on their side) | Director of Managed Services | No SYS-10 sessions or jobs running; agencies confirm |
| 0-30 min | Isolate infected hosts through EDR; keep them powered on for memory evidence | MDR provider; agency IT for agency servers | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the offline incident log with T0 | Incident commander | Log open |
| 0-60 min | **Protect what is left in the landing zone:** apply an organization-wide deny rule on deleting or changing snapshots, database instances, keys, and logging; confirm vault lock and log archive are intact; revoke all administrator sessions; require break-glass for any further admin work | Director of Cloud Operations | Deny rule active; vault and archive confirmed |
| 0-60 min | **Tell the agencies (suspected incident):** AG-02 and AG-39 (CJI), AG-01 (FTI) first, then AG-03, AG-04, and the managed services agencies AG-08 to AG-14, then all other customers. Say what is known, what is not, and when the next update comes | Director of Contracts and Compliance | Each contact reached by phone, call time logged, written follow-up through the agreed secure channel |
| 0-60 min | Call the cyber insurer's breach hotline before engaging any vendor; counsel engages forensics | Chief Operating Officer with the General Counsel | Claim number; counsel on the call |
| 0-2 h | Stop spread into agency interfaces: suspend the AG-02 and AG-39 message-switch connectors, AG-01 file transfer, the AG-03 API, and the AG-04 feed at the integration hub; block outbound traffic from production except to agency endpoints | Director of Cloud Operations | Interfaces down; egress blocked |
| 0-2 h | Put the ACMC in maintenance mode with a neutral status message if production is affected or cannot be verified clean | Director of Customer Support | Status page updated |
| 1-2 h | Convene the CMT; first situation report (scope, agencies affected, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | First written fact sheet to every affected agency (section 6.2), so Florida agencies can file within their 12 hours | Director of Contracts and Compliance | Fact sheets sent |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |
| 2-4 h | Staff briefing: what happened, who speaks to agencies, no outside discussion, report anything unusual | Incident commander with HR | Briefing sent by text |

**Do not** power off agency servers or delete attacker resources without the agency's agreement and forensic sign-off, and do not restore into a compromised account. Agencies command their own systems (POL-03 4.11).

## 4. Analysis (RS.AN)
1. **Scope across three environments.** (a) Agency-hosted servers reached through SYS-10: which agencies, which servers, what was pushed. (b) The company network: engineer laptops, jump servers, identity provider. (c) The landing zone: which accounts, roles, and resources the attacker touched, from the cloud audit logs in the log archive. List every tenant whose data sits in an affected database, bucket, or analytics table.
2. **Initial access and dwell time.** Confirm how SYS-10 was reached (for example a phished engineer with push MFA, the previously exposed token, or a vendor compromise) and the date the attacker first got in. If the vendor was the source (R-013), also coordinate with the vendor and other customers through counsel.
3. **Preserve evidence.** Forensics images key hosts and exports SYS-10 logs before the vendor's 90-day retention drops them (R-038). Chain of custody: who collected what, when, with hashes. Evidence is held by the forensic firm under counsel and kept 7 years (POL-03 4.6). Agency servers are imaged with each agency's agreement; the sheriff decides with its CSA how CJI-bearing images are handled.
4. **Exfiltration.** Determine whether data was copied out: database exports or snapshot sharing, storage reads, analytics queries, jump server staging folders, and outbound volume by destination. **This drives every breach decision.** For each tenant and agency system, record the record counts and data elements involved (FTI; CJI and CHRI; motor vehicle record information; Social Security numbers; driver license numbers) and where affected individuals live.
5. **FTI enclave.** Confirm whether any enclave role, key, or replica was touched. Confirm the state of the AG-01 key with AG-01 before any key action. Remember that FTI copied to the analytics service before 2026-09-08 (P03 PB-09) may be in older backups.
6. **Agency facts.** Keep a running fact sheet for each agency (section 6.2), updated at least every 12 hours.

## 5. Containment and eradication (RS.MI)
1. Remove attacker persistence: new users, roles, API clients, access keys, federation trusts, functions, scheduled jobs, and changed network rules, in SYS-10, the identity provider, and every landing zone account. Compare accounts against the infrastructure-as-code baseline.
2. Rotate every secret: SYS-10 tokens and every agency credential held in it (with each agency), database credentials, interface keys and certificates, pipeline secrets, and break-glass credentials after use.
3. Rebuild ACMC components from infrastructure code in clean accounts. Build container images from the repository after checking recent commits and pipeline changes for tampering (R-015). Only signed images deploy.
4. Reimage every affected laptop and jump server. Agencies rebuild their own servers, with company help where contracted.
5. Forensics confirms that persistence is gone before recovery starts in each environment.

## 6. Legal, regulatory, and external communication (RS.CO)
### 6.1 Decision points and notice timeline
**Follow `notification-matrix.csv`.** Counsel confirms every external notice. The Director of Contracts and Compliance keeps the **decision log**.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a breach of security under Fla. Stat. 501.171(1)(a) for each Florida tenant, and a breach under the law of each other state? | Director of Contracts and Compliance with counsel | Decision log |
| D2 | Date of determination (starts the 10-day agency notice clock) | Director of Contracts and Compliance | Decision log |
| D3 | Counts of affected individuals by tenant, data element, and state of residence (agencies need them for their 500 and 1,000 thresholds) | Director of Contracts and Compliance | Affected individuals list |
| D4 | Has law enforcement asked for a delay? | Counsel | Decision log |
| D5 | Contract notices due (all agencies; lenders; insurer) | General Counsel and CFO | Contract register |
| D6 | Ransom decision | CEO, on CMT recommendation | See 6.3 |

| When | Action | Owner |
|---|---|---|
| T0 + 1 hour | Phone notice of a suspected incident to AG-02 and AG-39 (CJISSECPOL IR-6) and AG-01 (Pub. 1075 Exhibit 7 contract), then all other affected agencies | Director of Contracts and Compliance |
| T0 + 1 hour | Insurer breach hotline; counsel engaged | Chief Operating Officer |
| T0 + 4 hours | First written fact sheet to every affected agency | Director of Contracts and Compliance |
| Agency T0 + 12 hours | Each Florida state agency, county, or city reports the ransomware incident to the Cybersecurity Operations Center and the FDLE Cybercrime Office (Fla. Stat. 282.318(3)(c)9.c.(I); 282.3185(5)(b)) | Agencies, with company facts |
| T0 + 24 hours | AG-01 reports to TIGTA and the IRS Office of Safeguards (Pub. 1075 sec. 1.8.2-1.8.4). The company confirms the report was made, and reports directly if it cannot confirm | AG-01; Director of Contracts and Compliance confirms |
| As each state CSA requires | AG-02 and AG-39 report the security violation to their CSOs and the FBI (Security Addendum 4.01) | Agencies, with company facts |
| Within 48 hours | Voluntary report to the FBI (IC3) and CISA, coordinated with the agencies | Security Operations Manager through counsel |
| No later than 10 days after determining a breach | Written third-party agent notice to each affected Florida agency with all information it needs (Fla. Stat. 501.171(6)(a)); notices to State B and State C agencies on the clocks counsel has mapped | Director of Contracts and Compliance and counsel |
| Agency: 30 days after determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 (Fla. Stat. 501.171(3)-(5)). The company can send notices on an agency's behalf if asked (501.171(6)(b)) | Agencies |
| Agency: 1 week after remediation | After-action report by each affected county or city to the Florida Digital Service (Fla. Stat. 282.3185(6)) | Agencies, with company input |

**Plan to the shortest clock.** The 1-hour CJI report comes first, and the 12-hour Florida reports run on the agencies' side. A company that waits for its own investigation leaves the agencies in breach of their duties.

### 6.2 Fact sheet for agency reports
Florida agency reports and the IRS data incident report ask for specific facts (Fla. Stat. 282.318(3)(c)9.b.; Pub. 1075 sec. 1.8.3). Keep one fact sheet per agency, with no FTI or CJI in it:
- summary of facts; date and time the incident occurred and was discovered; how it was discovered
- whether the agency's own servers (managed services) or its ACMC tenant, or both, are affected
- the date of the most recent backup, where it is, whether it was affected, and that it is cloud-based
- types of data and data elements involved; potential number of records (a range if unknown), and residents by state when known
- systems involved and where (cloud account and U.S. region; agency server names); whether any company employee was involved
- estimated fiscal impact to the agency, if known; details of any ransom demand
- the company's point of contact and the time of the next update

### 6.3 Ransom decision
- Florida state agencies, counties, and municipalities **may not pay or otherwise comply with a ransom demand** (Fla. Stat. 282.3186). The data and the servers belong to the agencies. The company will not negotiate over agency data or systems without each agency's agreement.
- Any payment by the company requires the CEO, counsel, the insurer, consultation with every affected agency, an **OFAC sanctions check** on the threat actor and any wallet, and a report to law enforcement (POL-03 4.7). The default position, approved by the CEO, is not to pay while the vault copies are intact.
- Paying does not remove any notice duty if data was taken.

### 6.4 Other communications
- Agency users: status page updates at least every 4 hours while the ACMC is down (Director of Customer Support).
- Agency executives: a call from the CTO or COO to each regulated customer's executive sponsor within the first day.
- Media: only the Chief Operating Officer speaks, after affected agencies have seen the statement. AG-01 shares any media release about FTI with the Office of Safeguards before release (Pub. 1075 sec. 1.8.5).
- Staff: daily briefings on the out-of-band channel; no posts or outside discussion.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 8). Each step is validated before the next begins: forensics sign-off for the environment, credentials rotated, EDR healthy, and the agency's approval for anything that touches its systems.

| Priority | Resource | Target | Validation |
|---|---|---|---|
| 1 | Out-of-band communications, phones, status page | 1 h | Contact list confirmed |
| 2 | Identity provider and break-glass access; MDR monitoring | 1 h | Sessions revoked; privileged credentials rotated |
| 3 | Managed services: clean SYS-10 instance (or on-site support at AG-02) with vaulted credentials only | 4 h (contract severity 1 response) | Vendor and forensics confirm clean; agency approves reconnection |
| 4 | Clean landing zone accounts and network rules from infrastructure code | 3 h | Baseline match; guardrails active |
| 5 | Regulated-tier cluster and FTI enclave database from the last clean vault copy | 6 h | Record counts and checksums match; AG-01 confirms key state |
| 6 | Application tier and agency sign-in: AG-02 and AG-39, then AG-03, then AG-04, then AG-01 | 8 h (contract RTO) | Tenant tests pass |
| 7 | Integration hub, replaying agency files and messages | 8 h | FIPS 140-3 certified modules on CJI paths; each agency approves its interface (AG-02 and AG-39 confirm whether their CSA must approve first) |
| 8 | Municipal tenants | 24 h | Tenant tests pass |
| 9 | Pipeline, then monitoring and patching for managed agencies | 24 h | Signed images only |
| 10 | Staging and development, analytics, payroll, billing | 48-72 h | Restore; permissions review |
| 11 | AI eligibility assistant (only after P10 conditions are met) | After all others | Validation set rerun |

**Warning (current state).** Today the full restore of a large tenant takes about 14 hours, not 8 (R-006). Tell the agencies early so they can plan manual work (P05 section 4), and restore regulated tenants in parallel where staff allow. Document storage is not yet in the vault (POAM-009): if production storage was destroyed, documents uploaded since the last agency resend may be lost.

Tell agency users when each tenant is back (RC.CO). Agencies keep their manual workarounds until their process is back within its RTO.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; documented within 30 days (POL-03 4.10). Invite the AG-01, AG-02, and AG-39 security contacts.
- Post-incident review of the incident procedures, with fixes made as soon as reasonably possible and training on the changes given immediately to all staff with FTI access (Pub. 1075 sec. 1.8.4).
- Refresher training within 30 days for staff involved (POL-03 4.9; CJISSECPOL AT-2).
- Update the risk register (P01, especially R-001, R-002, R-003, R-013, R-050), the POA&M (P07), the BIA (P05), and this runbook.
- Provide each affected county or city's after-action input within 1 week of remediation (Fla. Stat. 282.3185(6)).
- Report to the audit committee at its next meeting, or sooner if the CEO decides.
- Retain the incident log, evidence, and notices for 7 years (POL-01 4.13).

# Incident Response Runbook: Ransomware with Data Theft at Title and Closing

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC (PE-backed residential real estate brokerage with property management and title and closing services) |
| Tier / Vertical | Mid-Market / Real Estate and Rental and Leasing |
| Incident type | Ransomware with theft of customer information (double extortion) affecting the TMCC: the headquarters file server with scanned closing files, the integration service and data warehouse, and company endpoints, with possible spread to SaaS administration |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy (4.2 to 4.12); STD-07 Contingency and recovery standard (draft) |
| Companion documents | `ir-runbook.md` (business email compromise targeting closing funds); `notification-matrix.csv`; BIA (P05 section 8 recovery priorities); risk register (P01 R-004, R-013, R-014, R-024, R-030) |
| Written incident response plan | With the BEC runbook, the written plan required by 16 CFR 314.4(h) (N53-R01) |
| Runbook owner | Security Manager (Qualified Individual) as incident commander; IT Director as recovery lead |
| Approved | 2026-09-29 by the Chief Operating Officer and the President of Title and Closing |
| Last tested | Not yet. Executive ransomware tabletop with breach counsel, including the FTC consumer count, scheduled 2027-02-10 (POAM-009, POAM-020) |

## 0. Governance, roles, and contacts (Govern)
| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, President of Title and Closing, Broker of Record, General Counsel, vCISO, Security Manager, IT Director, Director of Marketing, HR Director, breach counsel | Closing delays and rescheduling, client and lender communications, statements, ransom recommendation to the CEO, spending |
| **Incident response team (IRT)** | Incident commander: Security Manager (Qualified Individual). IT Director (recovery lead), security analysts, MSSP, panel forensic firm (through counsel), SaaS vendor and cloud provider support contacts | Containment, investigation, eradication, recovery sequence |
| **Business continuity leads** | President of Title and Closing (closings and disbursements), Director of Transaction Services (contract deadlines), Controller (escrow accounts), Director of Property Management (rent window and maintenance dispatch) | Downtime procedures, which closings proceed, manual disbursement with dual approval and callbacks |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager (Qualified Individual) | IT Director | Out-of-band group on personal phones; printed call tree |
| Recovery lead | IT Director | Senior infrastructure engineer | Out-of-band group |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Notification decisions | General Counsel | Breach counsel (insurer panel) | Out-of-band group |
| Cyber insurer | Carrier breach hotline ($10 million limit, $250,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 operations center | n/a | MSSP hotline |
| Banks | Wire rooms and fraud desks (bank card in each closing room) | Relationship managers | Verified 2026-09-15 |
| Board, PE sponsor, Title and Closing board of managers | CEO; President of Title and Closing | COO | Phone |
| Law enforcement | FBI field office and IC3 | CISA (voluntary report) | Numbers in the binder |

**Out-of-band first.** Assume email, chat, and the voice system are compromised. Use the pre-arranged messaging group and printed call trees at every closing office.

**Legal privilege protocol.** Breach counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts and legal conclusions apart; do not speculate in writing.

## 1. Preparation checks (Identify / Protect)
- [x] Write-once backups of cloud workloads in the separate backup account, second region, separate credentials (P07 CP-9: system-level backups satisfied; test restore 40 minutes)
- [x] EDR on all company endpoints and servers with 24x7 MSSP response; MSSP escalated a test event in 18 minutes (P07 SI-4)
- [x] Phishing-resistant security keys for all administrators (P07 IA-2(1))
- [x] 20 pre-imaged spare laptops at headquarters for closers and wire release staff
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-15
- [ ] Independent backup of email, files, and SYS-01 data. **Gap until POAM-008 closes (2027-03-31)**
- [ ] Restore tests of the integration service and data warehouse (first test 2026-12-15, POAM-008)
- [ ] Downtime procedures for SYS-01, SYS-02, SYS-04, and SYS-10, with a closing downtime drill (2027-01-21, POAM-008)
- [ ] Integration secrets in the key vault, not configuration files (POAM-012)
- [ ] Headquarters file server restricted and scanned closing files moved to encrypted cloud storage (POAM-013)
- [ ] Egress alerting on the file server and data warehouse (POAM-005)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renaming or encryption | EDR alert; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Attempts to delete backups, or to disable EDR or logging | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| New administrator in the identity provider, productivity suite, or cloud outside change control | SIEM; privileged access service | Disable the account; declare if unexplained |
| Large outbound transfer from the file server, integration service, or data warehouse | Firewall flow logs (egress alerting due with POAM-005) | Block the destination; declare |
| Extortion email, call to clients, or leak-site post naming the company or Title and Closing | Email; client report; threat intelligence; FBI | Declare; preserve the message |
| A SaaS vendor reports a compromise of the company's tenant | Vendor notice (Fla. Stat. 501.171(6)(a); contract) | Declare; follow section 4 for the vendor's data |

**Severity 1 (declare immediately):** any confirmed ransomware execution, confirmed or claimed theft of customer information, or loss of the ability to disburse funds.

**Record discovery and determination dates** (POL-03 4.3). Discovery starts the FTC 30-day clock for a notification event involving at least 500 consumers (16 CFR 314.4(j)(1)-(2)). Determination starts the Florida 30-day clocks (Fla. Stat. 501.171(3), (4)(a)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | Declare Severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; counsel engages forensics | Chief Financial Officer | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-60 min | **Freeze money movement:** the President of Title and Closing and the Controller call the 3 banks to put the company's online banking users on hold except named wire release staff on clean devices; no payee changes are accepted until the incident commander clears it | Funds response lead; Controller | Banks confirm holds |
| 0-2 h | Cut SD-WAN and cloud hub routes to affected segments; block attacker infrastructure | IT Director | Routes down or filtered |
| 0-2 h | Revoke all sessions in the identity provider; reset administrator credentials using break-glass accounts; disable the contract developer's pipeline access and vendor remote access | Security Manager | Sessions revoked |
| 0-2 h | Start downtime procedures: closers use printed disbursement worksheets; wire instructions by phone only (BP-02 fallback); closings not yet funded are rescheduled by the President of Title and Closing | Business continuity leads | Downtime running; decisions documented |
| 1-2 h | Convene the CMT; first situation report (scope, closings affected that day, funds in motion, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff and agent briefing by text: what is affected, downtime steps, never accept changed instructions, report anything unusual | Director of Marketing with HR and Agent Services | Briefing sent |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner; President of Title and Closing informs its board of managers | CEO; President, Title and Closing | Notice given |

**Fraud follows ransomware.** Criminals watch for outages and send "our systems are down, use these new instructions" emails. During the incident every party on every open file is told by phone that instructions will never change by email.

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, servers, cloud accounts, and identities are affected? Use EDR telemetry, identity provider sign-in logs, cloud control-plane logs in the locked log bucket, and firewall flow logs.
2. **Initial access and dwell time.** Find the entry point (phishing, an exposed edge device, stolen integration secrets, or the developer pipeline) and the date the attacker first got in.
3. **Preserve evidence.** Forensics images key hosts and exports logs before retention expires, with chain of custody. Mailbox audit logs keep only 180 days today (POAM-005), so export them first.
4. **Exfiltration.** Determine what was taken: the scanned 2012 to 2018 closing files on the file server, data warehouse extracts, integration service data, or SaaS exports. Use egress volume, archive tools, staging folders, and leak-site samples.
5. **Affected-person list (drives every notice).** Build it with the consumer counting worksheet (POAM-020): consumers by data element (Social Security number, driver license, account data with access codes, loan data), by entity (Title and Closing customer information versus brokerage and tenant data), and by state of residence. The file server alone holds files on tens of thousands of consumers, so plan for the FTC threshold of 500 to be exceeded.
6. **SaaS status.** Confirm with the vendors that SYS-01, SYS-02, SYS-04, SYS-10, and SYS-13 tenants were not accessed with stolen credentials. If a vendor is the source, its notice duty to the company runs no later than 10 days after its determination (Fla. Stat. 501.171(6)(a)), but do not wait for it.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at site firewalls, SD-WAN, and the cloud firewall.
2. Disable compromised accounts. Rotate integration service secrets, the portal database credential, SaaS API keys, and bank platform credentials.
3. Rebuild affected endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads from code in the clean recovery network; restore data from backups taken before the attacker's first access.
5. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts, new SaaS administrators, connected apps) is removed before reconnection.
6. Treat the Closing Communications Portal as compromised until its code and pipeline are verified: redeploy from the reviewed repository with a company approver (POAM-010) and confirm that displayed wire instructions match SYS-02.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel confirms every notice with breach counsel and keeps the **decision log** (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Notification event: unencrypted Title and Closing customer information acquired without authorization? Access is presumed to be acquisition unless reliable evidence shows otherwise; data is unencrypted if the key was accessed (16 CFR 314.2(m)) | General Counsel with breach counsel | Decision log |
| D2 | At least 500 consumers? If yes, FTC notice within 30 days of discovery with the six items in 314.4(j)(1)(i)-(vi) | General Counsel | Counting worksheet |
| D3 | Florida residents affected; 500 or more (Department of Legal Affairs); more than 1,000 notices (consumer reporting agencies) | General Counsel | Affected-person list by state |
| D4 | Other states (about 25% of buyers live outside Florida): apply the law of each state where affected individuals reside | Breach counsel | State-by-state table |
| D5 | Law enforcement delay requested in writing (FTC public disclosure under 314.4(j)(1)(vi); Florida individual notice under 501.171(4)(b))? | General Counsel | Copy of the request |
| D6 | Contract notices: lender clients, the national homebuilder, the title insurance underwriter, the mortgage joint venture partner if referral data is involved | General Counsel with the President of Title and Closing | Contract register |
| D7 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | CFO |
| Day 0-2 | Report to the FBI (IC3) and a voluntary report to CISA. It helps the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory). CIRCIA reporting is not yet required (final rule not published) | Security Manager through counsel |
| Day 0-3 | Lender clients, homebuilder, and underwriter per contract | President, Title and Closing through counsel |
| As soon as scoped | D1 and D2 documented | General Counsel |
| No later than 30 days after discovery | FTC notice if D2 is met | General Counsel |
| No later than 30 days after determination | Florida individual notices by mail or verified email; Department of Legal Affairs notice if 500 or more Floridians (the 15-day good-cause extension can apply only to the individual notices, never to the Department notice) | General Counsel and breach counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at a single time | Breach counsel |
| As each state requires | Other states' individual and regulator notices | Breach counsel |

**Why the clocks differ.** The FTC's 30 days run from discovery, so they usually start first. Florida's 30 days run from determination. Neither law lets the company wait for the forensic report to finish; scope with the best information available and supplement later.

**Ransom decision (POL-03 4.8).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove notice duties when data was taken and does not guarantee deletion. The default position, approved by the CEO, is not to pay while backups are intact.

**Communications.**
- Buyers and sellers with closings in the next 10 days: a call from the closer the same day; closing dates confirmed by phone.
- All clients and agents: a website notice and an agent alert within 24 hours of any visible disruption, repeating that wire instructions never change by email.
- Lenders and the homebuilder: a direct call from the President of Title and Closing.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments.
- Staff and agents: daily text briefings through the out-of-band channel.

## 7. Recovery (RC.RP, RC.CO)
Restore in the BIA priority order (P05 section 8). Each step is validated before the next: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA) | Validation |
|---|---|---|---|
| 1 | SYS-03 identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 2 | SYS-09 banking access for named wire release staff on clean devices | 1 h | Bank holds lifted only for verified users; dual approval confirmed |
| 3 | SYS-06 headquarters network and the title operations center | 2 h | Clean segments only |
| 4 | SYS-07 clean endpoints for closers and wire release staff (pre-imaged spares) | 2 h | EDR healthy |
| 5 | SYS-02 title production access (vendor-hosted) | 4 h (vendor states 24 h) | Vendor confirms tenant integrity; payee data compared with the last known-good export |
| 6 | SYS-05 Closing Communications Portal | 4 h | Redeployed from reviewed code; instructions match SYS-02 |
| 7 | SYS-04 productivity suite | 4 h | Forwarding rules and connected apps reviewed |
| 8 | SYS-01 transaction management platform (vendor-hosted) | 8 h | Deadline export reconciled |
| 9 | SYS-08 SIEM feeds and EDR console | 8 h | Monitoring confirmed before wider reconnection |
| 10 | SYS-10 property management platform | 8 h (work orders), 24 h (payments) | Owner payout accounts compared with the last known-good export |
| 11 | SYS-05 integration service | 24 h | Rebuilt from code; secrets from the key vault |
| 12 | SYS-11 CRM and SYS-13 accounting system | 24 h | Agent payout accounts compared with the last known-good export |
| 13 | SYS-05 data warehouse and the headquarters file server | 72 h | Restore; access limited to Title and Closing records staff |

Back-enter downtime records within 72 hours of restoration, and reconcile every escrow and trust account before normal disbursement resumes (Fla. Stat. 626.8473(5); r. 61J2-14.012). Tell clients, lenders, agents, and the homebuilder when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11; 314.4(h)(5), (h)(7)).
- Update the risk register (P01 R-004, R-013, R-014, R-024), the POA&M (P07), the BIA, and this runbook.
- Include the event and the response in the Qualified Individual's next written report to Title and Closing's board of managers and the audit committee (314.4(i)(2)).
- Retain all incident documentation, including the decision log and notices, for at least 5 years (POL-01 4.12).

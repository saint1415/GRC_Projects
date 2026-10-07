# Incident Response Runbook B: Ransomware with Customer Data Theft

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (investor-owned electric distribution utility, with a Utility Services line for 4 client utilities) |
| Tier / Vertical | Mid-Market / Utilities |
| Incident type | Ransomware on corporate IT and cloud workloads with theft of customer data from the CIS export share (double extortion). Scenario: a phished dispatcher's credentials and a known-exploited VPN flaw give a criminal group access; it steals the nightly CIS extract (about 410,000 records with SSNs, driver license numbers, and bank account numbers, including the 4 client utilities' customers), then encrypts corporate servers and the OMS virtual machines |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy; Identity Theft Prevention Program (response steps) |
| Companion documents | `ir-runbook.md` (runbook A, OT intrusion); `notification-matrix.csv`; BIA (P05); crisis management plan; breach counsel playbook (state-by-state, due 2026-11-30) |
| Runbook owner | Information Security Manager (incident commander) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Executive ransomware tabletop with breach counsel and a client utility observer scheduled 2027-02-17 (with runbook A); client notification drill with Client A in 2027-Q1 (P03 G-071) |

**Two rules that shape every step.** (1) If there is any sign the attacker can reach OT, run runbook A in parallel and isolate the OT DMZ first. (2) The clocks for customers, the Florida Department of Legal Affairs, and the client utilities run from the **determination** of a breach, so record when it is made.

## 0. Governance, roles, and contacts (Govern)
| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. President and CEO, Chief Financial Officer, General Counsel, vCISO, Vice President of Customer Operations, Director of Utility Services, Director of Corporate Communications, HR Director, outside breach counsel | Business continuity, client utility communications, external statements, breach determinations (with counsel), ransom recommendation to the CEO, resources |
| **Incident response team (IRT)** | Incident commander: Information Security Manager. Director of Information Technology (recovery lead), security analysts, MSSP, forensic firm (through counsel), cloud, CIS, and AMI vendor contacts | Containment, investigation, eradication, recovery sequence |
| **Business continuity leads** | Director of System Operations (dispatch and switching on paper), Director of Customer Service (contact center and IVR), Director of Utility Services (client services), Controller (payments) | Manual workarounds from the BIA; customer and client service levels |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Information Security Manager | Director of Information Technology | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | President and CEO | Out-of-band group |
| Breach determinations and privilege | General Counsel with outside breach counsel | Outside breach counsel | Insurer hotline, then direct |
| Cyber insurer | Carrier hotline ($25 million limit, $500,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Customer data owner and Identity Theft Prevention Program administrator | Vice President of Customer Operations | Credit and Collections Manager | Out-of-band group |
| Client utilities | Director of Utility Services | Utility Services contract manager | Client duty officer list (updated each quarter) |
| Communications | Director of Corporate Communications | Outside crisis PR (through counsel) | Out-of-band group |
| Board and private equity sponsor | President and CEO informs the audit committee chair and the sponsor's operating partner | General Counsel | Phone |
| Law enforcement | FBI field office | CISA | Numbers in the binder |

**Legal privilege protocol.** General Counsel engages the forensic firm through the insurer panel. Analysis is labeled "Privileged and confidential, prepared at the direction of counsel". Facts are kept separate from legal conclusions; nobody speculates in email or chat.

## 1. Preparation checks (Identify / Protect)
- [x] Immutable backups in the separate backup account, write-once, second region (CP-9; P04)
- [x] EDR on all corporate endpoints and servers with 24x7 MSSP (SI-3; P07 fully satisfied)
- [x] MFA for all users, the VPN, and the cloud console
- [ ] CIS export minimized (no SSNs or driver license numbers) and kept 35 days (POL-04 5.4). **Gap until POAM-012 closes**
- [ ] SIEM alert on bulk reads from the CIS export share. **Due 2026-12-31 (P01 R-003)**
- [ ] Phishing simulations for field and DCC staff (POAM-010)
- [ ] Legacy IT/OT rules removed so ransomware cannot reach OT (POAM-003)
- [x] OMS restore tested in the last 12 months (2026-05-19, 3 hours 10 minutes)
- [ ] Breach counsel state-by-state playbook and client utility notice templates (due 2026-11-30)
- [x] Incident binder at headquarters, both DCCs, and each operations center: this runbook, call tree, notification matrix, paper switching and dispatch forms
- [ ] Out-of-band messaging group tested each quarter (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption | EDR alert; staff report | MSSP isolates the host and calls the incident commander within 30 minutes |
| Backup deletion attempts, or disabling of EDR, logging, or cloud guardrails | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| Large reads or downloads from the CIS export share or the meter data warehouse | Data-access logs; SIEM (bulk-read alert due 2026-12-31) | Block the account and destination; declare |
| VPN sign-in from an unusual location followed by internal scanning | Identity provider; firewall; EDR | Disable the account; declare if unexplained |
| Extortion email, or a leak-site post naming the company or a client utility | Email; threat intelligence; FBI; client | Declare; preserve the message |
| Client utility or CIS vendor reports suspicious activity in a client partition | Client; vendor notice | Declare; notify the Director of Utility Services |

**Declare when** malicious encryption, credential theft with internal movement, or unauthorized bulk access to customer data is likely. Severity: **High** if customer or client data may have been taken or if dispatch, contact center, or Utility Services stop.

**Record the times:** first sign of the attacker; declaration; when access to personal information was suspected; and when a breach was **determined** or there was reason to believe one occurred (the 10-day client clock and the 30-day Florida clocks run from this).

## 3. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Protect OT first:** disconnect the OT DMZ from the corporate network and the site-to-cloud VPN; confirm SCADA is unaffected; switch dispatch and switching to paper if the OMS is affected (BP-02 and BP-04 workarounds) | Incident commander with the Director of System Operations | OT isolated; DCC confirms safe operation |
| 2. Contain IT: MSSP network-isolates affected hosts; disable compromised accounts; block the VPN for all but break-glass users; revoke cloud sessions | Incident commander; MSSP | Spread stopped (no new encryption for 2 hours) |
| 3. Protect backups: confirm the backup account is untouched; freeze changes to vault policies | Director of Information Technology | Backup administrators confirm vault lock and last good copies |
| 4. Stop the data loss: block outbound destinations; disable access to the CIS export share; take a snapshot of the share for forensics | Incident commander | Egress blocked; share locked |
| 5. Convene the CMT; call the insurer hotline; General Counsel engages breach counsel and forensics | Chief Operating Officer; General Counsel | Claim number; engagement letters |
| 6. Business continuity: contact center to recorded outage message and storm call vendor if the IVR integration fails; Utility Services clients told to expect delays (within 48 hours of awareness, contract) | Director of Customer Service; Director of Utility Services | Workarounds running; clients informed |
| 7. If any electrical system operation was interrupted by the cyber event, run the DOE-417 criterion 3 step (1 hour) from runbook A | Director of System Operations | Filed or confirmed not required |
| 8. Start the incident log and the decision log (times and who decided) | Incident commander; General Counsel | Logs open |

## 4. Analysis and breach determination (RS.AN)
1. **Scope systems:** which servers, endpoints, cloud accounts, and SaaS tenants were encrypted or accessed. Check the analytics account (CIS export, meter data warehouse) and the operations workloads account (OMS).
2. **Scope data:** which CIS extract files were read or copied, which fields, and how many people. Split by: company customers versus each client utility's customers; Florida residents versus each other state (mailing address); data elements (SSN, driver license number, bank account number, portal credentials).
3. **Is it a breach?** Under Fla. Stat. 501.171(1)(a), a breach is unauthorized access of data in electronic form containing personal information. Information that is encrypted, secured, or modified so that it is unusable is excluded from personal information (501.171(1)(g)2); counsel considers whether the keys were also taken. Counsel decides, applying each state's definition for non-Florida residents.
4. **Who notifies whom:**
   - For the company's own customers, the company is the covered entity and notifies individuals, the Department of Legal Affairs (500 or more Florida residents), and consumer reporting agencies (more than 1,000 notices).
   - For client utilities' customers, the company is the **third-party agent**: it notifies each client within the 48-hour contract clause and the 10-day statutory limit (501.171(6)(a)), and gives the client everything it needs. The client gives notice unless it asks the company to send notices on its behalf (501.171(6)(b)).
5. **No-harm determination:** if, after investigation and consultation with law enforcement, counsel concludes the breach has not and will not likely result in identity theft or financial harm, the written determination must be kept for 5 years and sent to the Department within 30 days (501.171(4)(c)). Not expected for SSNs taken by an extortion group.
6. **Identity theft risk:** the Vice President of Customer Operations applies the Identity Theft Prevention Program response steps to affected accounts (heightened verification on move-ins, bank account changes, and portal profile changes).
7. **Preserve evidence** under counsel's direction: EDR telemetry, cloud audit logs, share access logs, VPN logs, ransom notes, leak-site captures.

## 5. Containment and eradication (RS.MI)
1. Reset all privileged credentials (identity provider, cloud, PAM, service accounts) from clean devices; force password resets and re-enroll MFA for affected users.
2. Patch or replace the exploited VPN appliance; review all internet-facing devices for known-exploited vulnerabilities.
3. Rebuild affected servers and OMS virtual machines from gold images; do not decrypt and reuse.
4. Confirm with the forensic firm and the MSSP that persistence is removed and detections are in place.
5. Remove SSN and driver license fields from the rebuilt CIS export before it is turned back on (POAM-012).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel tracks every clock and approves every notice.

| When | Action | Owner |
|---|---|---|
| Within hours | Insurer hotline; FBI and CISA (voluntary, same day); audit committee chair briefed | General Counsel; Information Security Manager; President and CEO |
| Within 48 hours of awareness | Each affected client utility (contract); daily updates after that | Director of Utility Services |
| Within 10 days of determination (at most) | Formal third-party agent notice to each affected client, with the data each client needs for its notices (501.171(6)(a)) | General Counsel with the Director of Utility Services |
| Before any payment | OFAC sanctions check; CEO, General Counsel, and insurer approval; board briefed (POL-03 4.9) | General Counsel |
| Within 30 days of determination | Notice to affected Florida residents (15 more days only with good cause given to the Department in writing within 30 days; law enforcement delay on written request) | Vice President of Customer Operations with General Counsel |
| Within 30 days of determination | Florida Department of Legal Affairs, if 500 or more Florida residents (no extension available for this notice) | General Counsel |
| Without unreasonable delay | Nationwide consumer reporting agencies, if more than 1,000 individuals are notified at a single time | General Counsel |
| Per each state's law | Residents of other states and their regulators, per the breach counsel playbook | General Counsel |
| Throughout | Customer, staff, and media statements; call center scripts; credit monitoring offer as counsel advises | Director of Corporate Communications |
| If the OMS outage interrupted operations or more than 50,000 customers lost service for 1 hour or more | DOE-417 per runbook A section 6 | Director of System Operations |

**Ransom decision.** The CMT recommends; the President and CEO decides with General Counsel and the insurer. Payment does not change any notification duty, because the data has already left the company.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 8), skipping items that were not affected:
1. Identity provider, PAM, and break-glass accounts verified
2. OMS switching and clearance module (RTO 2 hours), then outage prediction and dispatch (RTO 4 hours), restored from the backup account into a clean network segment
3. Truck tablet back end (RTO 12 hours)
4. Email, chat, and contact center integration (RTO 8 hours)
5. Load-forecasting workspace and the day-ahead schedule (RTO 12 hours; reuse the prior day's schedule meanwhile)
6. Utility Services client services and partitions (RTO 24 hours), in the order agreed with the clients
7. CIS export (rebuilt without SSNs and driver license numbers), meter data warehouse, billing, finance, payroll

**Validate before reconnecting:** each restored system is scanned, patched, and monitored; the OT DMZ is reconnected last, after the CMT chair approves. Tell customers and clients when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with a client utility representative; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-002, R-003, R-018, R-024, R-037, R-043), the POA&M (P07), and the SOC 2 readiness tracker (P09 CC7.4, CC7.5).
- Review the Identity Theft Prevention Program Red Flags in light of the stolen data (16 CFR 681.1(d)(2)(iv)).
- Keep incident and notification records for at least 5 years (the Florida no-harm determination rule sets 5 years; POL-01 4.15 sets the minimum).

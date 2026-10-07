# Incident Response Runbook: Compromise of Provider Tooling Affecting Downstream Customers

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider) |
| Tier / Vertical | Micro / Information Technology |
| Incident type | An attacker signs in to the RMM tool with a shared support account and pushes a malicious script to managed customer servers, including Bank A's (P01 R-001, Very High) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Lead Systems Engineer (Information Security Lead) |
| Approved | 2026-09-15 by the Owner |
| Last tested | Not yet. First tabletop with the MDR provider and a bank scenario due 2026-10-28 (POAM-011) |

## 0. Roles and notification chain (Govern)
Seven people run the company. The MDR provider watches laptops, sign-ins, and firewalls. The cyber insurer supplies breach counsel and forensics. In this incident the RMM tool reaches about 310 servers of 22 customers, including Bank A's 8 branch servers and Bank B's 9 servers.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Lead Systems Engineer | On-call Systems Engineer, then the Owner | Cell phone (numbers on the printed contact card) |
| RMM technical lead | Systems Engineer who authors RMM scripts | Second Systems Engineer | Cell phone |
| Communications lead (banks, customers, records) | Operations Manager | Owner | Cell phone; bank service register (POL-03 4.8) |
| Decision maker (spending, customer-wide pauses, ransom) | Owner | Lead Systems Engineer for containment only (POL-03 4.4) | Cell phone |
| MDR provider | MDR 24x7 security operations line | MDR account manager | Number in the MDR contract and on the contact card |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Policy card in the incident kit |
| Breach counsel and forensics | Insurer panel firms | Company outside counsel | Assigned on the first hotline call |
| RMM vendor | Vendor security incident line (priority 1 case) | Vendor account manager | Vendor support portal and phone |
| Bank A and Bank B | Bank-designated points of contact | Each bank's CEO and CIO (12 CFR 53.4(a)(2)) | Bank service register; **no valid designated contact today (POAM-011)** |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident kit |

**Notification chain in the first hour:**
1. Whoever sees it calls the on-call engineer.
2. The on-call engineer calls the incident commander.
3. The incident commander calls the Owner and the MDR line at the same time.
4. The Owner calls the insurer's breach hotline.
5. Counsel and forensics are engaged through the insurer.

The Operations Manager joins at once to start the incident log and pull up the bank and customer contact lists.

**Out-of-band first.** The RMM tool is outside single sign-on, but an attacker may also hold staff email. Coordinate by phone and text on company phones, using the printed contact card. Do not discuss the incident in the team chat until the identity provider is confirmed clean.

## 1. Preparation checks (Identify / Protect)
- [ ] Named RMM accounts only; shared support accounts removed and every RMM secret rotated. **Gap until POAM-001 closes (first milestone 2026-10-15)**
- [ ] RMM console limited to company VPN egress addresses (POAM-005, 2026-11-30) and two-person approval for scripts aimed at more than one customer (POAM-004, 2026-11-30)
- [ ] RMM audit logs sent to the MDR with alerts for multi-customer scripts and new-location sign-ins; 12-month retention. **Gap until POAM-009 closes (RMM logs by 2026-11-30)**. Until then the RMM vendor keeps only 30 days
- [ ] "Stop the tool" steps written and tested: pause all scripts and policies, end all sessions, disable technician accounts (step 3.1 below)
- [ ] Break-glass RMM and identity provider accounts sealed offline (POAM-002, 2026-10-31)
- [ ] Bank service register current: designated contacts and CEO and CIO contacts for both banks, verified quarterly. **Gap until POAM-011 closes (2026-10-31)**
- [ ] Customer security contact list exported from the PSA monthly and printed in the incident kit
- [ ] Notice templates ready: bank notice, MSA customer notice, Florida third-party agent notice
- [ ] Insurer hotline and policy number checked at renewal; RMM vendor incident contact on file

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Script or policy run against servers of more than one customer, or outside a change window | RMM job history; MDR alert once POAM-009 closes | Incident commander checks the job owner by phone |
| RMM sign-in from a new device or a non-company address, or on a shared account | RMM audit log; vendor sign-in alert email | End the session; call the account holder |
| Several customers report the same new process, service, account, or encrypted files on managed servers | Support tickets; customer calls | Support Engineer groups the tickets and calls the on-call engineer |
| The MDR reports suspicious activity on a staff laptop or identity account linked to RMM use | MDR escalation call | Treat as a possible tool compromise until ruled out |
| RMM vendor advisory or notice of a platform compromise | Vendor, CISA advisory | Treat as an incident until scope is known |

**Declare an incident when** a script or session the company did not authorize runs on any managed customer server, or the RMM vendor reports a compromise that may affect the company's tenant.

**Record three kinds of times in the incident log (POL-03 4.3):**
1. **Discovery:** when any workforce member first saw an indicator.
2. **Confirmation:** this starts the MSA's 72-hour customer notice clock.
3. **Each determination:**
   - the bank 4-hour determination (by the 2-hour mark);
   - the date unauthorized access to bank customer information is known or suspected, which starts the 24-hour bank contract notice;
   - the determination of a breach of personal information on a customer's systems, which starts the Florida 10-day agent notice.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Stop the tool.** Pause all scripts, scheduled jobs, and automation policies for all customers; end all technician sessions; disable every technician account except the incident commander's named or break-glass account | RMM technical lead | Job queue empty; no active sessions |
| 2. Revoke RMM API tokens and integrations (PSA, MDR); rotate the RMM tenant administrator credentials | RMM technical lead | Tokens revoked |
| 3. **Preserve evidence.** Export the RMM audit log, job history, and script library before the 30-day window rolls over; export identity provider and VPN sign-ins; ask the MDR to preserve its data. Hash and store the exports in the evidence folder (POL-03 4.12) | Incident commander | Exports hashed and logged |
| 4. Call the insurer's hotline; counsel and forensics engaged through the insurer | Owner | Claim number issued |
| 5. Open a priority-1 case with the RMM vendor; ask whether other tenants are affected | RMM technical lead | Case number |
| 6. Call each affected managed services customer's security contact. Advise them to isolate affected servers or block the RMM agent's outbound connection at their firewall | Operations Manager with a Support Engineer | All affected customers reached |
| 7. **Check the bank servers.** Were Bank A's or Bank B's servers among those the script reached? If so, call the bank now even before the 4-hour determination (relationship call by the Owner) | Incident commander; Owner | Bank list checked; call made |
| 8. Open the incident log: timeline, actions, who, when | Operations Manager | Log started |

**The incident commander may take steps 1, 2, and 6 without further approval** (POL-03 4.4). Pausing managed services for all 22 customers is acceptable: BP-04 tolerates 72 hours (P05), and restoring a compromised tool fast would spread harm.

## 4. Analysis (RS.AN)
Led by the insurer's forensic firm through counsel, with the incident commander supplying access and logs.
1. **Initial access.** Which account and session ran the script?
   - With the shared support accounts (until POAM-001 closes), identify the person through sign-in time, device, and source address, and phone every technician.
   - Check whether the shared password and MFA seed in the team vault were used from outside, and whether a staff laptop was compromised (MDR and EDR data).
   - Ask the RMM vendor whether its platform was the entry point.
2. **Blast radius.** List every script, customer, and server the attacker's sessions touched, from the RMM job history. Compare with the full agent list (about 310 servers, 22 customers).
3. **What the script did.** Forensics analyzes it: ransomware, credential theft, new accounts, remote access tools, or data collection. Send indicators of compromise to every affected customer.
4. **Data impact.** Did the script read or send out data? For each affected customer, record what personal information the servers hold and what the script touched. **This drives the bank 24-hour contract notice, the Florida agent notice, and each customer's own notices.**
5. **Bank service impact.** For each bank, did the incident materially disrupt or degrade covered services, or is it reasonably likely to, for four or more hours? **Decide by the 2-hour mark and record the decision and its time.** Pausing RMM patching alone rarely disrupts a bank for 4 hours. A script that encrypts or disables bank branch servers almost always does.
6. **Other company tools.** Did the attacker reach the identity provider, the hypervisor manager, the cloud tenant, the DNS account, or the PSA vault (which holds customer server passwords)? Check sign-ins by the same device or address. If any is touched, widen scope and follow the P05 recovery order. Rotate every customer server password stored in the PSA vault for affected customers.

## 5. Containment and eradication (RS.MI)
1. Keep RMM automation paused until forensics confirms eradication. Read-only monitoring may resume only if forensics confirms the channel is clean.
2. Before any session reopens:
   - replace every technician account with a named account and personal MFA;
   - turn on the console address restriction and two-person script approval (POAM-001, POAM-004, POAM-005).
3. Review the full script library and scheduled policies for tampering. Restore scripts from the last known-good export.
4. Re-register or reissue agents on affected servers if the vendor or forensics finds agent-level tampering, in coordination with each customer.
5. Help customers remove persistence (new accounts, services, scheduled tasks, remote access tools) using the indicators from forensics. **The customer approves every action on its own server.**
6. Block attacker infrastructure at the DC-1 firewalls and share indicators with customers and the MDR.
7. Confirm with forensics that the attacker has no remaining access to company tools before recovery.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews every notice before it goes out. A bank notice that is due must not wait for counsel; the Owner approves it and counsel reviews follow-ups (POL-03 4.7).

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer notified; counsel and forensics engaged; affected customers called; relationship call to any affected bank | Owner; Operations Manager |
| By the 2-hour mark | **Bank 4-hour determination** recorded for each bank whose servers or VMs were touched | Incident commander and Owner |
| As soon as possible after a "yes" determination | **Bank notice** to each affected bank's designated contact, or its CEO and CIO if none was provided (12 CFR 53.4(a); 304.24(a)). Phone first, then email. Record time and recipient | Operations Manager (Owner signs) |
| Within 24 hours of knowing or suspecting unauthorized access to a bank's customer information | **Bank contract notice** under each bank contract's security exhibit, whether or not the 4-hour test is met | Operations Manager |
| Within 72 hours of confirmation | **MSA notice** to every affected customer: what happened, affected servers, indicators, actions taken, next update time | Operations Manager; counsel |
| Day 0-2 | Voluntary report to the FBI (IC3 or field office) and CISA, as counsel advises. Make it before any ransom decision: full and timely reporting is an OFAC mitigating factor | Incident commander |
| No later than 10 days after determining a breach of personal information on a customer's servers | **Florida third-party agent notice** to each affected customer as covered entity, with all the information it needs for its own notices (Fla. Stat. 501.171(6)(a)). The MSA notice usually satisfies this earlier. Counsel checks other states' service-provider duties for customers with non-Florida data subjects | Operations Manager; counsel |
| Within 30 days of determination, only if the company's own personal information was breached (for example portal customer contacts with passwords) | Florida notice to individuals; Department of Legal Affairs if 500 or more Florida residents; consumer reporting agencies if more than 1,000 (501.171(3)-(5)) | Owner; counsel |
| Every business day until resolved | Update affected customers and banks. Each bank must notify its own regulator within 36 hours of its own determination (for example 12 CFR 53.3), so give banks facts early | Operations Manager |

**Plan to the shortest clock.** For a bank, the order is usually:
1. the relationship call in hour 1;
2. the 53.4 notice right after the 2-hour determination;
3. the 24-hour contract notice;
4. the MSA's 72 hours.

The Florida 10-day agent deadline is the outer limit for breach facts, not a target.

**Not applicable today** (see `notification-matrix.csv`):
- FedRAMP incident reporting: no federal customer (P03 G-001).
- DFARS 72-hour reporting: no covered defense information.
- CIRCIA: no final rule as of 2026-09-25.

**Ransom decision:**
- Only the Owner decides, after counsel, the insurer, and an OFAC sanctions check (POL-03 4.10).
- The company never pays on a customer's behalf. Customers decide for their own servers.
- Paying does not remove any notice duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). In this incident the DC-1 platform is usually untouched, so recovery centers on customers' servers and the RMM tool:
1. **DC-1 network, firewalls, VPN, and cluster management** (priority 1): confirm untouched (analysis step 6). Change the shared hypervisor and BMC credentials if there is any doubt.
2. **Managed DNS account** (priority 2): confirm no zone changes; compare with the nightly export once POAM-006 closes.
3. **Support line, ticketing, and contact lists** (priority 3): keep customers and banks informed.
4. **Customer portal** (priority 4) and **backup service** (priority 5): confirm the portal's service account and the backup console were not used by the attacker.
5. **MDR monitoring** (priority 6): confirm it receives RMM logs and the new alerts before the RMM tool returns.
6. **Customer servers:** customers restore affected servers from their own backups or rebuild them. Company engineers help through each customer's own remote access, with the customer's approval, not through the RMM tool.
7. **RMM tool** (priority 7; 24-hour RTO **after integrity validation**). Reopen customer by customer only when all of these hold:
   - named accounts, the address restriction, and two-person approval are on;
   - the script library is verified;
   - forensics signs off;
   - the customer agrees.

   Bank servers come back last, after each bank confirms.
8. **Billing and administration** (priority 8): service credits under the MSA are worked out after recovery.

**Validate before reconnecting,** and tell each customer and bank when managed services resume (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing, with the MDR provider and counsel; written summary within 30 days (POL-03 4.14).
- Update the risk register (P01: R-001, R-012, R-014, R-019), the POA&M (P07: POAM-001, POAM-004, POAM-005, POAM-009, POAM-011, POAM-012), and this runbook.
- Review the RMM vendor's incident report and contract terms (POL-02 A.5).
- Keep the incident log, evidence exports, determinations, and every notice for at least 3 years (POL-02 A.7), and longer if litigation is expected.

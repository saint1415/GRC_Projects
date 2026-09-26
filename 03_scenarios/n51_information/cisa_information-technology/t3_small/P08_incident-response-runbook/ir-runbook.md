# Incident Response Runbook: Compromise of Provider Tooling Affecting Downstream Customers

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) |
| Tier / Vertical | Small / Information Technology |
| Incident type | An attacker uses a stolen RMM technician session to push a malicious script to managed customer servers (P01 R-001, Very High) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy (SEV1) |
| Runbook owner | IT Manager (Information Security Officer) |
| Approved | 2026-09-25 by the COO |
| Last tested | Not yet. First tabletop exercise due 2026-12-15 (POAM-018) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | Chief Operating Officer | Incident bridge (phone), then the out-of-band group chat on company phones |
| RMM technical lead | Managed Services Lead | Senior managed services engineer | Incident bridge |
| Platform and network lead | Director of Platform Engineering | Senior platform engineer | Incident bridge |
| Customer communications | NOC and Support Manager | COO | Status page; customer security contact list |
| Bank liaison | Sales Director | CEO | Bank-designated contact list (P03 G-227) |
| Legal counsel | Outside counsel (through the insurer's panel if a claim is opened) | Company outside counsel | Insurer hotline; counsel's cell |
| Cyber insurer | Carrier breach hotline | Controller | Policy card in the incident kit |
| Forensics | Firm on the insurer's panel | n/a | Through the insurer |
| RMM vendor | Vendor security incident line | Vendor account manager | Vendor support portal (priority 1) |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident kit |
| Decisions on ransom or customer-wide shutdown | CEO | COO | Cell |

**Out-of-band first.** Assume the attacker can read company email and chat, because the RMM tool and the productivity suite share the identity provider. Coordinate on the phone bridge and the printed contact list in the NOC incident kit.

## 1. Preparation checks (Identify / Protect)
- [ ] Named RMM technician accounts with hardware keys; console limited to company egress addresses; two-person approval for multi-customer scripts. **Gap until POAM-002 closes (2026-11-30)**
- [ ] RMM audit logs forwarded to the SIEM, with alerts for new-device sign-ins and scripts sent to more than one customer. **Gap until POAM-002 and POAM-010 close**
- [ ] Global "stop" procedure tested: suspend script execution and technician sessions for all customers within 10 minutes (Managed Services Lead)
- [ ] Customer security contact list and bank-designated contacts current (verified quarterly; **9 of 14 banks today, POAM-019**)
- [ ] Notice templates ready: status page, customer notice, bank notice, Florida third-party agent notice
- [ ] Forensics retainer and insurer panel confirmed; RMM vendor's incident contact on file
- [ ] RMM audit log retention checked (the vendor keeps 90 days by default); export procedure documented

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Script sent to servers of more than one customer, or at an unusual hour | RMM audit log alert (once POAM-002 closes); RMM job history | NOC pages the incident commander |
| Technician sign-in from a new device or a non-company address | IdP and RMM sign-in logs | Revoke the session; call the technician by phone |
| Many customer servers show the same new process, service, or scheduled task started by the RMM agent | Customer EDR, customer reports, RMM monitoring | Open a SEV1 ticket |
| Customers report encrypted files, new admin accounts, or outbound traffic from managed servers | Support tickets, phone | Group tickets; check whether the customers share the RMM tool |
| RMM vendor advisory or notice of a platform compromise | Vendor, CISA, threat intelligence | Treat as SEV1 until scope is known |

**Declare a SEV1 incident when** a script or session the company did not authorize runs on any managed customer server, or the RMM vendor reports a compromise affecting the company's tenant.

**Record three times in the incident log:**
1. **Discovery**, when a workforce member first saw an indicator.
2. **Confirmation**, which starts the MSA's 72-hour clock.
3. **Each determination** that starts a legal clock: the bank 4-hour determination, and the determination of a breach of personal information.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Stop the tool.** Suspend script execution and scheduled jobs for all customers; end all technician sessions; disable all technician accounts except the incident commander's break-glass account | Managed Services Lead | RMM job queue empty; no active sessions |
| 2. Revoke RMM API tokens and integrations (ticketing, SIEM); rotate the RMM tenant administrator credentials | Managed Services Lead | Tokens revoked |
| 3. **Preserve evidence.** Export the RMM audit log, job history, and script library before retention rolls over; snapshot the identity provider sign-in logs | IT Manager | Exports hashed and stored in the evidence folder |
| 4. Call the insurer's hotline; engage counsel and forensics through the insurer | COO | Claim number issued |
| 5. Open a priority-1 case with the RMM vendor and ask whether other tenants are affected | Managed Services Lead | Case number |
| 6. Post a status page notice: managed services automation paused; hosting unaffected (if true) | NOC and Support Manager | Notice live |
| 7. Call each affected managed services customer's security contact. Advise them to isolate affected servers or block the RMM agent's outbound connection at their firewall | NOC with account managers | All affected customers reached |
| 8. Check whether bank customers' managed servers are among those affected. Start the bank 4-hour assessment | Sales Director and IT Manager | Bank list checked |

**The incident commander may take steps 1, 2, and 7 without further approval** (POL-03 4.4). Pausing automation for all 58 managed services customers is acceptable. BP-04 has a 72-hour MTD (P05), and restoring a compromised tool fast would spread harm.

## 4. Analysis (RS.AN)
1. **Initial access.** Which account and session ran the script? With shared technician accounts (gap until POAM-002), identify the person through IdP sign-in time, device, and source address, and phone every technician. Check for session token theft from a technician laptop (EDR) and for RMM vendor-side compromise.
2. **Blast radius.** List every script, customer, and server the attacker's sessions touched, from the RMM job history. Compare with the full agent list (about 1,900 servers, 58 customers).
3. **What the script did.** Forensics analyzes the script: ransomware, credential theft, new accounts, remote access tools, or data collection. Get indicators of compromise to all affected customers.
4. **Data impact.** Did the script access or send out data? Check for personal information on the affected servers, based on customer information and the script's actions. **This drives the Florida third-party agent notice and customers' own notices.**
5. **Service impact.** For each bank, did the incident materially disrupt or degrade covered services, or is it reasonably likely to, for four or more hours? Record the determination and the time.
6. **Other company tools.** Check whether the attacker also reached the identity provider, the control plane, hypervisor managers, or the CI/CD pipeline. Look at IdP sign-ins by the same device or address and at control plane bulk-action logs. If any is affected, widen scope and follow the P05 recovery order.
7. **Future federal tenants.** Once agency tenants exist, decide within minutes whether federal customer data is affected or likely affected (IEC-CSO-EFR), estimate the PAIN rating (N1 to N5, section 6), or treat it as PAIN-5.

## 5. Containment and eradication (RS.MI)
1. Keep RMM automation paused until eradication is confirmed. Allow read-only monitoring only if forensics confirms the monitoring channel is clean.
2. Replace all technician accounts with named accounts and new hardware keys, and turn on the console IP restriction and two-person script approval before any session reopens (POAM-002).
3. Review the full script library and scheduled jobs for tampering, and restore scripts from version control.
4. Re-register or reissue RMM agents on affected servers if the vendor or forensics finds agent-level tampering. Coordinate with each customer.
5. Support customers in removing persistence (new accounts, services, scheduled tasks, remote access tools) using the indicators from forensics. The customer approves every action on its server.
6. Block attacker infrastructure at the company edge and publish indicators to customers.
7. Confirm with forensics that the attacker no longer has access to company tools before recovery.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Legal counsel confirms every notice before it goes out. The incident commander records each trigger time.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer notified; counsel and forensics engaged; status page notice | COO; NOC and Support Manager |
| As soon as possible after the 4-hour determination | **Bank notice** to each affected bank's designated contact, or its CEO and CIO if none was provided (12 CFR 53.4(a)). Phone first, then email. Record time and recipient | Sales Director with the IT Manager |
| Within 72 hours of confirmation | **MSA notice** to every affected customer: what happened, affected servers, indicators, actions taken, next update time | NOC and Support Manager; counsel |
| Day 0-2 | Voluntary report to the FBI (IC3 or field office) and CISA; supports OFAC mitigation if a ransom is considered | IT Manager |
| No later than 10 days after determining a breach of personal information on customer servers | **Florida third-party agent notice** to each affected customer as covered entity, with the information it needs for its own notices (Fla. Stat. 501.171(6)(a)). Check other states' service-provider duties for customers with non-Florida data subjects | IT Manager; counsel |
| Within 30 days of determination, if the company's own personal information was breached | Florida notice to individuals, the Department of Legal Affairs (500 or more Florida residents), and the consumer reporting agencies (more than 1,000 individuals) (501.171(3)-(5)) | COO; counsel |
| Every business day until resolved | Update affected customers and banks. Banks must notify their own regulator within 36 hours of their determination (for example 12 CFR 53.3), so give them facts early | NOC and Support Manager; Sales Director |

**Plan to the shortest clock.** The bank notice has no fixed number of hours; it is due "as soon as possible" after the company's determination, and the banks' own 36-hour clock depends on it. The MSA's 72 hours then applies to all customers. The Florida 10-day third-party agent deadline is the outer limit for breach facts, not a target.

**After FedRAMP certification (not applicable today).** A FedRAMP Reportable Incident needs:
- an Initial Incident Report to FedRAMP (fedramp_security@fedramp.gov), the agency customers under their own procedures, and all necessary parties through the trust center, within **1 hour** for PAIN-3 to PAIN-5, 24 hours for PAIN-2, or 1 business day for PAIN-1;
- ongoing reports every 6 hours at PAIN-3 to PAIN-5;
- a final report within 6 hours of resolution at PAIN-3 to PAIN-5, or 1 business day at PAIN-1 and PAIN-2 (IEC-CSO-IIR, -OIR, -FIR).

The PAIN scale: N1 minimal effect on one or more agencies; N2 narrow effect; N3 disruptive effect on one agency; N4 debilitating effect on one agency or disruptive effect on more than one; N5 debilitating effect on more than one agency. The company plans to keep the RMM tool out of agency tenants (P03 G-012), which would keep this incident type outside FedRAMP reporting.

**Ransom decision:** only the CEO decides, after consulting counsel and the insurer and completing an OFAC sanctions check (POL-03 4.7). The company does not pay on a customer's behalf. Customers make their own decisions for their own servers.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). In this incident the hosting platform is usually unaffected, so recovery focuses on customers and the RMM tool:
1. **Identity provider and administrator access.** Confirm the identity provider is clean; use break-glass accounts if needed.
2. **Edge network, DNS, and hosting platform** (BP-03, BP-01). Confirm they were not touched (analysis step 6).
3. **NOC, ticketing, and status page** (BP-05). Keep customers informed.
4. **Customer servers.** Customers restore affected servers from their own backups or rebuild them. Managed services engineers help through the customers' own remote access, not the RMM tool.
5. **SIEM** (BP-07). Confirm it has the RMM logs and new alerts before the RMM tool returns.
6. **RMM tool** (BP-04, priority 6, 24-hour RTO **after integrity validation**). Reopen customer by customer only after:
   - named accounts, IP restriction, and two-person approval are on;
   - the script library is verified;
   - forensics signs off;
   - the customer agrees.

**Validate before reconnecting,** and tell each customer when managed services resume (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned review within 14 days of closing, documented within 30 days (POL-03 4.10).
- Update the risk register (P01: R-001, R-015, R-025), the POA&M (P07: POAM-002, POAM-010, POAM-012, POAM-020), and this runbook.
- Review the RMM vendor's report and contract terms (POL-01 4.8).
- Keep all incident records, evidence exports, and notices for at least 3 years (POL-01 4.11), and longer if litigation is expected.

# Incident Response Runbook: Compromise of Shared Services Affecting Subsidiaries

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed holding company with four operating subsidiaries) |
| Tier / Vertical | Mid-Market / Management of Companies and Enterprises |
| Incident type | Compromise of the shared services platform affecting all subsidiaries: a stolen administrator session or credential leads to takeover of the directory, theft of data from shared file stores and the reporting warehouse (Finance customer information, plan PHI, employee SSNs), and ransomware on HQ servers, the plant, endpoints, and cloud workloads |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy. For Finance, POL-03 and this runbook are the written incident response plan under 16 CFR 314.4(h). For the group health plan, they are the sponsor's security incident procedures (45 CFR 164.308(a)(6)) |
| Companion documents | `ir-runbook-payment-fraud.md` (treasury payment fraud through business email compromise); `notification-matrix.csv`; BIA (P05); subsidiary BIA workarounds |
| Runbook owner | Security Manager (incident commander; Qualified Individual for Finance; plan Security Official) |
| Approved | 2026-09-22 by the CEO |
| Last tested | Not yet. Group tabletop for this scenario on 2026-11-18 with the subsidiary Presidents, the MSSP, and outside counsel (POAM-011) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers so that technical, business, and legal decisions each have a clear owner, and so that every affected company is represented.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: CFO. CEO, General Counsel, vCISO, VP of Information Technology, VP of Human Resources, the President of each affected subsidiary, outside breach counsel | Business continuity across subsidiaries, external statements, extortion decision (recommendation to the CEO and board chair), resources, lender and sponsor notices |
| **Incident response team (IRT)** | Incident commander: Security Manager. VP of Information Technology (recovery lead), security analysts, GRC analyst (decision log), MSSP, forensic firm (through counsel), identity, cloud, and SaaS vendor contacts | Containment, investigation, eradication, recovery sequence |
| **Business continuity leads** | Supply President (counters and deliveries), Home Services President (dispatch and emergency calls), Fabrication Plant Manager (production), Finance President (collections and servicing), Treasurer (payments) | Activate BIA workarounds; decide what each subsidiary does while systems are down |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | VP of Information Technology | Out-of-band messaging group on personal phones; printed call tree |
| CMT chair | CFO | CEO | Out-of-band group |
| Legal and notification decisions | General Counsel | Outside breach counsel | Out-of-band group |
| Finance customer information decisions | Finance President with counsel | CFO | Out-of-band group |
| Plan PHI decisions | VP of Human Resources (plan Privacy Official) with counsel | Benefits Manager | Out-of-band group |
| Cyber insurer | Carrier breach hotline ($10M limit, $200K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Board and sponsor | CEO informs the audit committee chair and the sponsor's operating partner (within 24 hours) | CFO | Phone |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume the attacker controls the directory and can read email, chat, and the suite's phones. The CMT and IRT use a pre-provisioned messaging group on personal phones and printed call trees kept at every site (P01 R-043).

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in writing.

**Why this incident is different at a holding company.** One directory and one identity provider serve five companies. The account first compromised may belong to the holding company, but the data at risk belongs to each subsidiary and to the health plan, and each has its own notice duties and clocks. **Record which company's data, and which plan's data, each affected system holds.**

## 1. Preparation checks (Identify / Protect)
- [x] Immutable cloud backups in the separate backup account, 35-day write-once retention (P07 CP-9 cloud results)
- [x] EDR on managed endpoints and servers with 24x7 MSSP (P07 SI-3)
- [x] Two break-glass accounts for the cloud identity provider, tested 2026-06
- [ ] Off-site immutable backups of HQ servers and the plant server. **Gap until POAM-010 closes (2027-01-31)**
- [ ] Directory forest recovery procedure tested. **Gap until POAM-010 closes**
- [ ] MFA for directory administration and phishing-resistant keys for administrators. **Gap until POAM-002 and POAM-003 close**
- [ ] SIEM coverage of the servicing system, warehouse, ERP, HRIS, file servers, and plant. **Gap until POAM-006 closes**
- [ ] Data map of Finance customer information, plan PHI, and employee SSNs. **Gap until 2026-12-31 (P03 ID.AM-07)**
- [x] Incident binder at every site: this runbook, call tree, BIA workarounds, notification matrix
- [x] Insurer panel counsel and forensics confirmed; contacts verified 2026-09-22
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| New Domain Admins member, new global administrator, new federation or app consent, MFA method added to an administrator | Directory and identity provider audit logs in the SIEM | Treat as critical: go to section 3 immediately |
| Sign-in from an unfamiliar location right after an approved MFA prompt, or token reuse | Identity provider risk detection; MSSP | Revoke sessions; declare if an administrator or a treasury, HR, benefits, or Finance user |
| Mass file renaming or encryption, ransom note | EDR alert; staff report | MSSP isolates the host and calls the incident commander within 30 minutes |
| Backup deletion attempts, disabling of EDR or logging | Cloud audit logs; EDR tamper alert | Ransomware precursor: declare |
| Large outbound transfer from file servers or the warehouse | Firewall flow logs (egress alerting due with POAM-015) | Block the destination; declare |
| Extortion email or leak-site post naming any group company | Email; MSSP threat intelligence; FBI | Declare; preserve the message |
| Branch, shop, or plant reports systems unavailable | Staff report | IT triage; declare if malicious |

**Severity 1 (declare immediately):** any confirmed directory or identity provider administrator compromise, ransomware execution, confirmed data exfiltration, or extortion claim.

**Record the date and time of discovery and of determination in the incident log** (POL-03 4.3). Three clocks can start here:
- FTC: discovery is the first day the event is known to any employee, officer, or agent of Finance other than the attacker (16 CFR 314.4(j)(2)). Shared IT staff are treated as Finance's agents.
- HIPAA: a breach is discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member or agent of the plan (164.404(a)(2)).
- Florida: 30 days from the determination of a breach or reason to believe one occurred (501.171(3)-(4)); 10 days for the holding company, as third-party agent, to tell an affected subsidiary (501.171(6)(a)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log and decision log | Incident commander; GRC analyst | Logs open |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | CFO | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention; suspend cross-account backup jobs; rotate backup administrator credentials out of band | VP of Information Technology | Backup integrity confirmed |
| 0-2 h | **Contain identity.** Use break-glass accounts to revoke all identity provider sessions and refresh tokens; disable directory synchronization so directory changes stop flowing to the cloud; remove unknown administrators, app consents, and federation changes; reset administrator credentials | Security Manager | Admin lists match the approved list; sync stopped |
| 0-2 h | Disable vendor remote access (machine vendors, seller's IT provider, MSSP script execution beyond isolation); sever site-to-cloud VPN routes for affected segments; isolate the plant network at its firewall | VP of Information Technology | Routes down or filtered |
| 0-2 h | **Treasury freeze.** Treasurer and CFO tell the banks to hold ACH files and wires not yet released, and switch to bank-portal-only payments with callback | Treasurer | Banks confirm |
| 0-2 h | Activate BIA workarounds by priority: Home Services dispatch to mobile phones and paper (BP-12, MTD 8 h); Supply paper tickets (BP-09); Finance phone payments (BP-16); plant repeat programs from controllers (BP-14) | Business continuity leads | Workarounds running |
| 1-2 h | Convene the CMT; first situation report (scope, companies affected, safety, decisions needed) | CFO | CMT held |
| 2-4 h | Staff briefing by text: what happened, workarounds, do not discuss externally, report anything unusual | VP of Human Resources with the Presidents | Script sent |
| 2-4 h | CEO informs the audit committee chair and the sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope identities.** Which accounts did the attacker use? Check identity provider sign-ins, directory security logs on all 3 domain controllers, privileged group changes, and new service accounts. Assume every Tier 0 credential is compromised until forensics shows otherwise.
2. **Initial access and dwell time.** Identify the entry point (adversary-in-the-middle phishing, an exposed edge device, vendor remote access, or Home Services North) and the first date of access.
3. **Preserve evidence.** Forensics images key hosts (domain controllers, file servers, the SFTP server) and exports logs before they roll off, with chain of custody.
4. **Data exfiltration by company.** Determine what was accessed or taken, store by store, and **map each to its owner company and data type**:

| Store | Owner | Data | Decision owner |
|---|---|---|---|
| HQ file share with Finance exports; reporting warehouse loan tables; SFTP ACH files | Finance | Customer information | Finance President |
| HR site (stop-loss files, high-cost claimant reports); benefits mailbox | Group health plan | PHI | VP of Human Resources (plan Privacy Official) |
| HRIS exports; HR site | Each employer | Employee SSNs, bank accounts | VP of Human Resources |
| Supply legacy shares | Supply | Contractor credit and pricing | Supply President |
| Data room and deal sites | Holding company | Deal information | VP of Corporate Development |

   Build the **affected individuals list** by data element, company, and state of residence. Without the data map this will take time (P03 RS.AN-08), so start immediately.
5. **Plant safety.** The Plant Manager checks that no machine program was altered before restarting cutting (STD-11; P01 R-049). Run a first-piece check on every program used after the incident.
6. **Vendor status.** Confirm the ERP, loan servicing, HRIS, treasury, and identity vendors are unaffected; if a vendor is the source, record it for notice terms.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at site firewalls, SD-WAN, and the cloud firewall.
2. **Directory:** if forensics confirms domain compromise, plan a forest recovery from a pre-compromise system-state backup in an isolated network, then reset the domain's key account twice, and rotate every service account and integration secret (including the ACH signing account and SaaS API keys).
3. Rebuild affected endpoints and servers from gold images. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads from clean images in an isolated recovery network; restore data from backups taken before the first access.
5. Confirm with forensics that persistence (scheduled tasks, remote tools, rogue accounts, app registrations) is removed before reconnecting any site.
6. Home Services North: keep its network disconnected from group systems until its devices are checked.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out. The GRC analyst keeps the **decision log** for the General Counsel (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Did a Safeguards Rule notification event occur, and does it involve 500 or more consumers? Unauthorized access to unencrypted customer information is presumed acquisition (16 CFR 314.2(m)) | Finance President with counsel | Decision log with consumer count |
| D2 | Is this a breach of unsecured plan PHI? Presumed yes unless the four-factor assessment shows a low probability of compromise (164.402) | VP of Human Resources with counsel | Decision log with the four factors |
| D3 | Discovery dates (FTC, HIPAA) and determination date (Florida) | General Counsel | Decision log |
| D4 | Counts in total, by company, by state, and Florida residents (thresholds: 500 for FTC, HHS contemporaneous notice, and the Department of Legal Affairs; more than 500 residents of a state for media; more than 1,000 for consumer reporting agencies) | General Counsel | Affected individuals list |
| D5 | Has law enforcement asked for a delay (FTC 314.4(j)(1)(vi); HIPAA 164.412; Florida 501.171(4)(b))? | General Counsel | Decision log |
| D6 | Contract notices due (lenders, sponsor, bank partner, card processor)? | CFO with counsel | Contract register |
| D7 | Extortion payment decision | CEO and board chair, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | CFO |
| Day 0 | Affected subsidiary Presidents told whose data may be involved (internal; the legal outer limit for the holding company as third-party agent is 10 days after determination, Fla. Stat. 501.171(6)(a)) | Security Manager |
| Day 0 | Benefits Committee told of any incident involving plan ePHI (164.314(b)(2)(iv) term; POL-03 4.6) | Security Manager |
| Day 0-1 | Sponsor operating partner (contract: 24 hours); audit committee chair | CEO |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA; supports OFAC mitigation if any payment is ever considered | Security Manager through counsel |
| Day 0-3 | Bank partner notice if servicing data on participated loans is involved (contract: 72 hours; from 2027-01) | Finance President |
| As soon as scoped | D1 and D2 decisions documented | Finance President; VP of Human Resources |
| Within 30 days of discovery | **FTC notice** if a notification event involves 500 or more consumers | Finance President and counsel |
| Within 30 days of determination | Florida individual notice (15-day good-cause extension available for this notice only) and Department of Legal Affairs notice if 500 or more Floridians (no extension) | Each affected company, with counsel |
| Without unreasonable delay, no later than 60 days after discovery | HIPAA individual notices for plan members; HHS at the same time if 500 or more; media if more than 500 residents of a state | VP of Human Resources and counsel |
| Without unreasonable delay | Consumer reporting agencies if Florida notice goes to more than 1,000 individuals at once | General Counsel |
| Each other state | Residents of other states: apply each state's law (counsel checks the affected list by state) | General Counsel |
| Per contract | Lenders under the credit agreement and warehouse line | CFO |
| Next September | Event and response in the Qualified Individual's report to Finance's Board of Managers (314.4(i)(2)) | Security Manager |
| Within 60 days after year end | HHS log entry for any plan breach under 500 | VP of Human Resources |

**Why the shortest clock matters.** The FTC 30-day clock starts at discovery, which is usually earlier than the Florida determination, and HIPAA's 60 days are an outer limit, not a target. Treat the first day any employee knew as the start for every clock.

**Extortion payment decision (POL-03 4.8).** Requires the CEO, the board chair, the General Counsel, the insurer, and an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis), plus a report to law enforcement. Paying does not remove any notice duty if data was taken. The default, approved by the CEO, is not to pay while clean cloud backups exist.

**Communications.**
- Customers: holding statements approved by counsel for each subsidiary; Home Services posts emergency-call instructions (gas smell: leave and call the gas utility or 911) on its website and phone greeting within 2 hours of any dispatch outage.
- Borrowers: Finance's phone payment line message; no late fees during the outage.
- Employees: daily text briefings; the out-of-band channel only.
- Media: one spokesperson (CEO), holding statement only, no technical details or comment on payment.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, forensics sign-off for the segment.

| Order | Resource | Target (BIA) | Validation |
|---|---|---|---|
| 1 | Cloud identity provider and administrator access (break-glass) | 1 h | Sessions revoked; admin list approved; cloud-only admin accounts until the directory is clean |
| 2 | HQ, distribution center, and shop networks | 2 h | Clean segments only; plant stays isolated |
| 3 | Clean endpoints for dispatch, counters, and treasury | 4 h | Pre-imaged spares; EDR healthy |
| 4 | Suite phones and email | 4 h | Mailbox rules and app consents reviewed |
| 5 | Field-service and distribution systems through single sign-on | 4 h | Vendor confirms no tenant changes |
| 6 | Bank portals | 4 h | New tokens for affected users; bank confirms no pending fraudulent items |
| 7 | EDR console and SIEM feeds | 8 h | Monitoring confirmed before wider reconnection |
| 8 | SFTP server | 8 h | New keys and rotated ACH signing secret; file totals reconciled with the bank before release |
| 9 | Loan servicing through single sign-on | 8 h | Export logs reviewed |
| 10 | On-premises directory (forest recovery if compromised) | 12 h target, unproven | Clean forest; sync re-enabled only after validation |
| 11 | Plant server and HQ scanner server | 12 h | Programs checked against known-good hashes |
| 12 | ERP (vendor-hosted) | 24 h | No unauthorized vendor master or bank-detail changes |
| 13 | HRIS and payroll | 24 h | No direct deposit changes in the window |
| 14 | Integration service; reporting warehouse; board portal | 24 h; 72 h; 72 h | Restore; reconcile control totals with subsidiary systems |

Tell subsidiary Presidents, the bank partner, lenders, and staff when services are restored (RC.CO-03).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with every affected subsidiary President; written report within 30 days (POL-03 4.11).
- Add weaknesses to the POA&M (P07) with owners and dates (314.4(h)(5)).
- Update the risk register (P01, especially R-001, R-002, R-003, R-004), this runbook, and the notification matrix (314.4(h)(7)).
- Retain all incident documentation, including the decision log and notices, for at least 6 years (POL-01 4.16; for the plan, 45 CFR 164.530(j) documentation and 164.414(b) burden of proof).

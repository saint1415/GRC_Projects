# Incident Response Runbook: Exfiltration of Controlled Unclassified Information (CUI)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed aircraft parts manufacturer, DoD subcontractor) |
| Tier / Vertical | Mid-Market / Defense Industrial Base |
| Incident type | Exfiltration of CUI: an adversary-in-the-middle phishing page steals an engineer's enclave session; the attacker uses it to open a virtual desktop, run PLM exports, and move drawings and models out. Variant B: a supplier that holds company CUI is breached |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy |
| Contract basis | DFARS 252.204-7012(c) to (g) and (m)(2)(ii), text checked on eCFR (version date 2026-09-23) |
| Companion documents | `ir-runbook-plant2-ransomware.md` (ransomware on the Plant 2 shop floor); `notification-matrix.csv`; BIA (P05); risk register (P01 R-002, R-008, R-009, R-010) |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. CUI exfiltration tabletop with a DIBNet reporting drill and outside counsel on 2026-11-18 (POAM-013) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, business, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, Director of Trade Compliance and Contracts, Vice President of Operations, HR Director, outside counsel | Customer and prime communications, export disclosure decisions (with the Empowered Official), extortion response (recommendation to the CEO), resources, board and sponsor updates |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director, security analysts, GRC analyst (evidence log), MSSP, forensic firm (through counsel), cloud provider security contact | Containment, investigation, eradication, recovery, evidence preservation |
| **Data and contract cell** | Director of Engineering (what was taken), Director of Trade Compliance and Contracts (CUI and export status, DIBNet, primes), Director of Additive and Engineering Services (services customers) | File-by-file impact, prime and customer notices, export classification |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on company mobile phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| DoD reporting and prime notices | Director of Trade Compliance and Contracts | Security Manager (second certificate holder) | Phone |
| Export control decisions | Director of Trade Compliance and Contracts (Empowered Official) | Outside export counsel | Phone |
| Legal | General Counsel; outside counsel (insurer panel) | Outside government contracts counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier hotline ($15 million limit, $500,000 retention) | Broker | Policy card in the incident binder (CFO) |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Cloud provider | Provider security contact (government-community offering) | Account team | Contact from the CRM, in the binder |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume the enclave suite's email and chat are watched. The CMT and IRT use a pre-provisioned messaging group on company mobile phones and the printed call tree in the incident binders at both plants.

**Legal privilege protocol.** General Counsel decides at declaration whether outside counsel directs the investigation. If so, counsel engages the forensic firm, and analysis is labeled "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs, file lists) separate from legal conclusions. **Privilege never delays the DIBNet report or evidence preservation.**

## 1. Preparation checks (Identify / Protect)
- [x] Two current DoD-approved medium assurance certificates (Director of Trade Compliance and Contracts, Security Manager), valid to 2027-05 (252.204-7012(c)(3))
- [ ] Clean reporting laptop on the corporate network, stored in the trade compliance office, with the certificate and DIBNet bookmark. **Due 2026-10-31**
- [x] DIBNet field list prepared: company CAGE code, subcontract numbers for all three primes, prime security contacts, facility clearance status (none), points of contact
- [x] SIEM keeps 1 year searchable and 6 years archived (AU-11; P07 satisfied)
- [x] MSSP alerts for impossible travel, new mailbox rules, new sync clients, and mass download from the suite
- [ ] Alerts for PLM bulk export and virtual desktop download volume (R-002). **Due 2027-01-31**
- [ ] Phishing-resistant authenticators for all enclave users (IA-2(2)). **Due 2027-01-31**
- [x] Forensic firm through the insurer panel; cloud snapshot procedure for SYS-03 workloads
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)
- [x] Incident binders at both plants: this runbook, call tree, notification matrix, DIBNet field list

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Engineer reports entering credentials on a page that looked like the company sign-in page | Staff report (POL-03 4.2) | Security analyst revokes the user's sessions and opens an incident |
| Sign-in with a valid session from an unfamiliar location or anonymizing service; same session used from two places | Identity provider risk alert via the MSSP | MSSP revokes sessions (playbook) and calls the Security Manager within 30 minutes |
| PLM export of more than 200 files by one user in an hour, or large downloads from a virtual desktop | PLM and desktop alerts (from 2027-01) | Open an incident; suspend the account |
| Hundreds of files synced from the suite, a new sync client, or a new mailbox forwarding rule | Suite audit alerts via the MSSP | Open an incident; suspend the account |
| A prime, DC3, the FBI, or another agency reports company data seen elsewhere | External notice | Declare at once |
| A supplier reports a breach of company CUI | Supplier notice (variant B, section 9) | Declare; follow section 9 |

**Declare a CUI exfiltration incident (severity 1) when** any evidence shows an unauthorized party used an enclave identity or session, or CUI left the enclave to a place the company does not control.

**Record the time of discovery.** The 72-hour DoD reporting clock runs from discovery of the cyber incident (252.204-7012(a), (c)). A compromise includes possible copying of information to unauthorized media (252.204-7012(a)). Do not wait for proof that CUI was taken: suspected unauthorized access to the enclave starts the clock.

## 3. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke all sessions and tokens for the affected account; reset the password; remove any MFA method the attacker registered; issue a hardware key | Security analyst with the MSSP | Sign-in logs show no further attacker activity |
| 2. End any virtual desktop sessions the attacker opened; snapshot the session host before recycling it | IT Director | Snapshot hash recorded |
| 3. Block the attacker's IP addresses and phishing domain in the identity provider, cloud firewall, and email filtering | Security analyst | Blocks confirmed |
| 4. Find other recipients of the phishing message; revoke sessions for anyone who clicked | Security analyst | Recipient and clicker list |
| 5. **Before changing anything else:** export identity, suite, PLM, desktop, and cloud firewall logs for the last 90 days to the evidence store; image the engineer's workstation (kept powered on, isolated by EDR) | Security Manager with the GRC analyst | Hashes recorded; chain of custody started |
| 6. Call the Director of Trade Compliance and Contracts and the COO. Start the 72-hour clock in the incident log | Security Manager | Discovery time agreed and written down |
| 7. CFO calls the insurer hotline; General Counsel engages counsel and, through counsel, the forensic firm | CFO; General Counsel | Claim number issued |
| 8. COO convenes the CMT (within 4 hours) | COO | First CMT meeting held |

## 4. Analysis (RS.AN)
1. **Review for compromise of covered defense information** (252.204-7012(c)(1)(i)): identify compromised computers, servers, specific data, and user accounts, and check what else the attacker could reach from the session (PLM, the MFT gateway, the build preparation server, mailboxes).
2. **Exact file list:** from PLM, desktop, and suite logs, list every file the attacker's sessions opened, exported, downloaded, or synced, with path, time, and source address.
3. **What the files are:** the Director of Engineering maps each file to part number, program, and owner (Prime A, B, or C; Customer D or E; a services customer). The Director of Trade Compliance and Contracts marks each as CUI, ITAR, or EAR controlled and records the distribution statement.
4. **Where the data went:** attacker infrastructure, hosting location, and any sign of a foreign actor. This feeds the export decision and the law enforcement report.
5. **Initial access and persistence:** the phishing page, the stolen token, mailbox rules, app consents, new devices, MFA methods, and any desktop or PLM activity.
6. **Malware:** adversary-in-the-middle kits usually leave nothing on company systems. If EDR or forensics isolates malicious software, keep it for DC3 (section 6).

## 5. Containment and eradication (RS.MI)
1. Confirm every attacker session is revoked across the identity provider, suite, virtual desktops, and PLM.
2. Remove attacker-created mailbox rules, app consents, registered devices, and sync partnerships.
3. Tighten conditional access: block sign-in from outside the United States for enclave accounts and require compliant devices for sync clients (logged under CM-3).
4. Rebuild the engineer's workstation **only after its image is captured and hashed**.
5. Confirm with the forensic firm that no persistence remains before closing containment.
6. Do not delete, rotate out, or overwrite any log, snapshot, or image covered by the preservation rules below.

**Preservation rules (252.204-7012(e)).** Keep images of all known affected systems and all relevant monitoring and packet capture data for **at least 90 days from submission of the DIBNet report**, in the backup account under the Security Manager's custody. Ask the cloud provider to preserve its own logs, since it must also comply with paragraphs (c) to (g) (252.204-7012(b)(2)(ii)(D)).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews each external notice except the DoD report, which is never delayed for review.

| When | Action | Owner |
|---|---|---|
| Hour 0 | Discovery time recorded; clock started | Security Manager |
| Hour 0-4 | Insurer notified; counsel and forensics engaged; CMT convened | CFO; General Counsel; COO |
| Within 24 hours | Audit committee chair and PE sponsor informed | CEO |
| **Within 72 hours of discovery** | **DIBNet report** with the elements required on DIBNet, from the clean reporting laptop with a medium assurance certificate. Report what is known; mark unknowns and update later | Director of Trade Compliance and Contracts (Security Manager backup) |
| As soon as practicable after the report | Give the DoD-assigned **incident report number** to each affected prime (252.204-7012(m)(2)(ii)) | Director of Trade Compliance and Contracts |
| When malware is isolated | Submit to **DC3** as DC3 or the Contracting Officer instructs; never to the Contracting Officer (252.204-7012(d)) | Security Manager |
| On request | Give DoD access to information or equipment for forensic analysis; provide damage assessment information if the Contracting Officer asks (252.204-7012(f), (g)) | Director of Trade Compliance and Contracts with General Counsel |
| Within 72 hours of confirming customer data was affected | Notice to affected services customers, and to Customer D or E per their agreements | Director of Trade Compliance and Contracts |
| Day 1-5 | Voluntary report to the FBI (IC3) or CISA | Security Manager |
| After analysis | Export decision: did an unauthorized export or release occur? If yes, DDTC voluntary disclosure (initial notice immediately after discovery; full disclosure within 60 calendar days, 22 CFR 127.12(c)(1)) and, for EAR items, BIS voluntary self-disclosure (15 CFR 764.5). Record the reasoning either way | Director of Trade Compliance and Contracts with export counsel |
| Only if employee personal information is involved | Florida notice within 30 days after determination (Fla. Stat. 501.171) | General Counsel with the HR Director |
| Day 0-5 | Staff briefing: what happened, phishing reminder, no discussion outside the company | COO |

**Plan to the 72-hour clock.** It is the shortest clock in the matrix. Draft the DIBNet report in parallel with analysis, and file updates as the file list and export decisions firm up.

**Extortion.** If the attacker demands payment to not publish the models, no payment may be made without the CEO's decision after advice from counsel, the insurer, and an OFAC sanctions check (POL-03 4.11). Paying does not change any reporting duty.

## 7. Recovery (RC.RP, RC.CO)
Exfiltration rarely takes systems down, so recovery is mostly about trust. Restore or confirm in BIA priority order (P05):
1. DoD reporting capability (clean laptop, certificates, contact list)
2. Identity provider: affected sessions revoked, authenticators re-registered, conditional access tightened
3. Plant networks and firewalls: attacker blocks in place
4. MES and DNC: confirm the attacker did not reach them (not reachable from the suite or desktops)
5. PLM, virtual desktops, MFT gateway, build preparation server: confirm no attacker activity; rotate MFT partner credentials if the gateway was touched
6. Enclave endpoints: reimaged workstation returned
7. Collaboration suite: sharing settings and alerts confirmed

**Validate before closing:** no attacker activity for 14 days of MSSP review, alerts in place for the paths used, and the preserved evidence set complete. Tell affected primes and customers when containment is complete (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of containment; documented within 30 days (POL-03 4.13).
- Update the risk register (P01 R-002, R-008, R-009), the POA&M (P07), training (AT-2), and this runbook.
- Check whether the SSP or SPRS score needs updating (POL-01 4.9). Tell the CEO before the next annual affirmation (32 CFR 170.22).
- Keep incident records for at least 6 years (POL-01 4.16), and the 252.204-7012(e) evidence for at least 90 days from the report or longer if DoD asks.

## 9. Variant B: a supplier that holds company CUI is breached
About 22 suppliers and outside processors receive drawings. Under the flowed-down clause, a supplier that discovers a cyber incident reports it to DoD itself and gives its incident report number to the company (252.204-7012(m)(2)(ii)). Nine suppliers are still on legacy purchase orders without the clause (P03 G-119), so for them the company may learn of a breach only informally.

| Step | Action | Owner |
|---|---|---|
| 1 | Record the supplier's notice, its DoD incident report number (if any), and which company drawings it held (MFT transfer log and the quality transport log for paper) | Director of Supply Chain |
| 2 | Suspend the supplier's MFT account; stop new CUI to the supplier | Security Manager |
| 3 | Decide whether the company's own systems were affected (for example, the supplier's MFT credentials used against the gateway). If yes, this is also a company cyber incident: start the company's 72-hour clock and follow sections 2 to 8 | Security Manager |
| 4 | Inform each affected prime with the supplier's incident number and the list of affected parts (contract practice) | Director of Trade Compliance and Contracts |
| 5 | If the supplier had no flowdown, ask counsel whether the company must report, and fix the purchase order before any further CUI is sent | General Counsel; Director of Supply Chain |
| 6 | Export decision for the drawings involved (section 6) | Director of Trade Compliance and Contracts |
| 7 | Re-verify the supplier's SPRS and CMMC status before restoring CUI access (POL-01 4.11) | Director of Supply Chain |

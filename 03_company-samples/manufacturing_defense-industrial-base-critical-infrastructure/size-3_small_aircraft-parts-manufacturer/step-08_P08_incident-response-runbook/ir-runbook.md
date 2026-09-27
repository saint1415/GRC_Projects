# Incident Response Runbook: Exfiltration of Controlled Unclassified Information (CUI)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts manufacturer, DoD subcontractor) |
| Tier / Vertical | Small / Defense Industrial Base |
| Incident type | Exfiltration of CUI: an adversary-in-the-middle phishing page steals an engineer's enclave session token, and the attacker syncs CAD models and drawings from enclave file storage (SYS-02) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Contract basis | DFARS 252.204-7012(c) to (g) and (m)(2)(ii), text checked on eCFR (version date 2026-09-23) |
| Runbook owner | IT Manager (incident commander) |
| Approved | 2026-08-31 by the Vice President of Operations |
| Last tested | Not yet. First tabletop with a DIBNet reporting drill on 2026-11-18 (POAM-002, POAM-004) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | Vice President of Operations | Incident line (cell), then the out-of-band group chat on company mobile phones |
| Technical response | Systems Administrators (2) | Forensic firm on retainer (due 2026-10-31); 24x7 managed detection provider (from 2027-01-31) | Cell; retainer hotline |
| DoD reporting and prime notices | Contracts Manager | IT Manager (second certificate holder) | Cell |
| Export control decisions | Contracts Manager (ITAR Empowered Official) | Outside export counsel | Cell |
| CUI data owner (what was taken) | Director of Engineering | Quality Manager | Cell |
| Legal counsel | Outside counsel (government contracts and export) | Insurer panel counsel | Via Vice President of Operations |
| Cyber insurer | Carrier hotline | n/a | Controller holds the policy card |
| Cloud provider | Provider security support (government-community offering) | Provider account team | Support portal and phone in the incident binder |
| Executive and communications | Vice President of Operations | President | Cell |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the enclave suite's email and chat are watched. Coordinate by phone and the printed contact list in the incident binder (IT office and the Contracts Manager's office).

## 1. Preparation checks (Identify / Protect)
- [ ] Two current DoD-approved medium assurance certificates (Contracts Manager, IT Manager), stored so they work from a clean corporate laptop (252.204-7012(c)(3)). **Gap until POAM-002 closes (2026-10-31)**
- [ ] DIBNet report fields gathered in advance: company CAGE code, contract and subcontract numbers, prime contacts, facility clearance status (none), points of contact
- [ ] Log retention of 1 year in the log workspace; alerts for mass download, unfamiliar sign-in location, and new mailbox rules (AU-6, AU-11). **Gap until POAM-008 closes (2026-12-31); retention is 90 days today**
- [ ] Forensic retainer with cloud and endpoint imaging capability, and a written snapshot procedure for SYS-03 VMs (IR-4). **Gap until POAM-004 closes**
- [ ] Phishing-resistant authenticators for all enclave users (IA-2(2)). **Planned by 2027-01-31 (P01 R-002)**
- [ ] Printed incident binder: this runbook, contacts, notification matrix, DIBNet field list
- [ ] Break-glass accounts tested (P05)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Engineer reports entering credentials on a page that looked like the company sign-in page | Staff report (POL-03 4.2) | IT Manager revokes the user's sessions and opens an incident |
| Sign-in from an unfamiliar location or an anonymizing service with a valid session, or the same session used from two places | Identity provider risk alert; log review | Open an incident; revoke sessions |
| Hundreds of files downloaded or synced by one account in a short time, or a sync client registered from a new device | Collaboration suite audit alert (from 2026-11); weekly log review | Open an incident; suspend the account |
| New mailbox rule forwarding or deleting messages; new app consent | Suite audit log | Open an incident |
| A prime, DC3, the FBI, or another agency reports that the company's data was seen elsewhere | External notice | Declare the incident at once |

**Declare a CUI exfiltration incident when** any evidence shows that an unauthorized party used an enclave identity or session, or that CUI left the enclave to a place the company does not control.

**Record the time of discovery.** The 72-hour DoD reporting clock runs from discovery of the cyber incident (252.204-7012(a), (c)). A cyber incident includes any compromise, including possible copying of information to unauthorized media (252.204-7012(a)). Do not wait for proof that CUI was taken: suspected unauthorized access to the enclave is enough to start the clock.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke all sessions and refresh tokens for the affected account; reset the password; remove any MFA method the attacker registered; issue a hardware key | Systems Administrator | Sign-in logs show no further activity from the attacker's sessions |
| 2. Block the attacker's IP addresses and the phishing domain in the identity provider, the enclave firewall, and email filtering | Systems Administrator | Blocks confirmed |
| 3. Search for other users who received the same phishing message; revoke sessions for anyone who clicked | IT Manager | List of recipients and clickers |
| 4. **Before changing anything else:** export identity provider sign-in logs, suite file audit logs, and mailbox audit logs for the last 90 days to the evidence store; take a disk and memory image of the engineer's workstation (it stays powered on and is isolated by EDR) | IT Manager | Hashes recorded; chain of custody form started |
| 5. Call the Contracts Manager and the Vice President of Operations. Start the 72-hour clock on the whiteboard and in the incident log | IT Manager | Discovery time agreed and written down |
| 6. Call the cyber insurer's hotline; engage counsel and the forensic retainer | Vice President of Operations and Controller | Claim number issued |

## 4. Analysis (RS.AN)
1. **Review for compromise of covered defense information** (252.204-7012(c)(1)(i)): identify compromised computers, servers, specific data, and user accounts, and check other systems the attacker could have reached (PLM through virtual desktops, the SFTP gateway, mailboxes).
2. **Exact file list:** from the suite file audit log, list every file the attacker's sessions opened, downloaded, or synced, with path, time, and source IP. The 90-day log retention limits how far back this can go (P01 R-009).
3. **What the files are:** the Director of Engineering maps each file to its part number, program, and customer (Prime A, Prime B, or Customer C). The Contracts Manager marks each as CUI, ITAR, or EAR controlled and records the customer's distribution statement.
4. **Where the data went:** attacker IP addresses, hosting location, and any sign of a foreign actor. This feeds the export control decision and the law enforcement report.
5. **Initial access and persistence:** the phishing page, the stolen token, any mailbox rules, app consents, new devices, or MFA methods. Check whether the attacker used the session to reach PLM or the SFTP gateway.
6. **Malware:** adversary-in-the-middle kits usually leave nothing on company systems. If EDR or forensics isolates malicious software, keep it for DC3 (section 6).

## 5. Containment and eradication (RS.MI)
1. Confirm every attacker session is revoked across the identity provider, suite, and virtual desktops. Require re-registration of authenticators for affected users.
2. Remove attacker-created mailbox rules, app consents, registered devices, and sync partnerships.
3. Tighten conditional access: block sign-in from outside the United States for enclave accounts, and require compliant devices for sync clients (policy change logged under CM-3).
4. Rebuild the engineer's workstation from the standard image **only after its image is captured and hashed**.
5. Confirm with the forensic firm that no persistence remains before closing containment.
6. Do not delete, rotate out, or overwrite any log or image covered by the preservation rules below.

**Preservation rules (252.204-7012(e)).** Keep images of all known affected systems and all relevant monitoring and packet capture data for **at least 90 days from submission of the DIBNet report**. Raise log workspace retention for the affected tables to at least 1 year at once. Ask the cloud provider to preserve its own logs, since it must also comply with paragraphs (c) to (g) (252.204-7012(b)(2)(ii)(D)).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews each external notice. The DoD report is not delayed for counsel review.

| When | Action | Owner |
|---|---|---|
| Hour 0 | Discovery time recorded; clock started | IT Manager |
| Hour 0-4 | Insurer notified; counsel and forensics engaged | Vice President of Operations |
| **Within 72 hours of discovery** | **DIBNet report** with the elements required on DIBNet, from a clean corporate laptop with the medium assurance certificate. Report what is known; mark unknowns and update later | Contracts Manager (IT Manager backup) |
| As soon as practicable after the report | Give the DoD-assigned **incident report number** to Prime A and/or Prime B (252.204-7012(m)(2)(ii)) | Contracts Manager |
| When malware is isolated | Submit to **DC3** as DC3 or the Contracting Officer instructs; never to the Contracting Officer (252.204-7012(d)) | IT Manager |
| On request | Give DoD access to information or equipment for forensic analysis; provide damage assessment information if the Contracting Officer asks (252.204-7012(f), (g)) | Contracts Manager |
| Day 1-5 | Voluntary report to the FBI (IC3) or CISA | IT Manager |
| After analysis | Export decision: did an unauthorized export or release occur? If yes, DDTC voluntary disclosure (initial notice immediately after discovery; full disclosure within 60 calendar days, 22 CFR 127.12(c)) and, for EAR items, BIS voluntary self-disclosure (15 CFR 764.5). Record the reasoning either way | Contracts Manager (Empowered Official) with export counsel |
| If Customer C data was taken | Notice under the customer agreement | Contracts Manager |
| Only if employee personal information is involved | Florida notice within 30 days after determination (Fla. Stat. 501.171) | HR Manager and counsel |
| Day 0-5 | Staff briefing: what happened, phishing reminder, no discussion outside the company | Vice President of Operations |

**Plan to the 72-hour clock.** It is the shortest clock in the matrix. Draft the DIBNet report in parallel with analysis, and file updates as the file list and export decisions firm up.

**Extortion.** If the attacker demands payment to not publish the models, no payment may be made without the President, counsel, the insurer, and an OFAC sanctions check (POL-03). Paying does not change any reporting duty.

## 7. Recovery (RC.RP, RC.CO)
Exfiltration rarely takes systems down, so recovery is mostly about trust. Restore or confirm in BIA priority order (P05):
1. DoD reporting capability (clean laptop, certificate, contact list)
2. Identity provider: all affected sessions revoked, authenticators re-registered, conditional access tightened
3. Plant enclave network and firewall: attacker blocks in place
4. MES and DNC: confirm the attacker did not reach them (they were not reachable from the suite)
5. PLM, virtual desktops, and SFTP gateway: confirm no access by attacker sessions; rotate SFTP partner credentials if the gateway was touched
6. Enclave endpoints: reimaged workstation returned to the engineer
7. Collaboration suite: sharing settings and alerts confirmed

**Validate before closing:** no attacker activity for 14 days of review, alerts in place for mass download and unfamiliar locations, and the preserved evidence set is complete. Tell affected primes when containment is complete (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of containment; documented within 30 days (POL-03 4.10).
- Update the risk register (P01, especially R-002, R-008, R-009, R-016), the POA&M (P07), training content (AT-2), and this runbook.
- Check whether the SPRS score or the SSP needs updating because of control changes (POL-01 4.9).
- Keep all incident records for at least 6 years (POL-01 4.11), and the 252.204-7012(e) evidence for at least 90 days from the report or longer if DoD asks.

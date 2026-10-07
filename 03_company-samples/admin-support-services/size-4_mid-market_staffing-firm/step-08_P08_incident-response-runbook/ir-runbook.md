# Incident Response Runbook: Payroll and HR System Breach Exposing Worker PII

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed staffing and temporary help firm) |
| Tier / Vertical | Mid-Market / Administrative and Support and Waste Management and Remediation Services |
| Incident type | Payroll and HR system breach exposing worker PII: an adversary-in-the-middle phishing kit relays a payroll specialist's password and push approval for the payroll platform (SYS-02); the attacker exports the associate register (names, SSNs, addresses, bank accounts) and changes direct deposits before Friday payroll. Variants: the attacker uses the exposed integration API key (P01 R-052), or takes over associate portal accounts at scale (R-001) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response and Contingency Policy |
| Companion documents | `ir-runbook-payroll-outage.md` (payroll platform outage before payday); `notification-matrix.csv`; BIA (P05); risk register (P01 R-001, R-002, R-003, R-052) |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-22 by the Chief Operating Officer |
| Last tested | Not yet. Executive tabletop with outside counsel scheduled 2026-11-12 (POAM-012) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, business, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, IT Director, Director of Compliance and Privacy, Director of Payroll and Billing, CHRO, Director of Marketing, outside breach counsel | Pay continuity, external statements, client and lender notices, extortion decision (recommendation to the CEO), resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director, security analyst, GRC analyst (log keeper), MSSP, forensic firm (through counsel), payroll and ATS vendor security contacts, integration contractor lead | Containment, investigation, eradication, recovery sequence |
| **Payroll command** | Director of Payroll and Billing, Controller, payroll specialists, payroll vendor fraud desk | Bank-change freeze, recall of diverted payments, verified re-payment, Friday payroll |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Legal and notices | General Counsel with outside breach counsel (insurer panel) | Director of Compliance and Privacy | Through the insurer hotline, then direct |
| Breach determinations and decision log | Director of Compliance and Privacy | General Counsel | Out-of-band group |
| Payroll containment and pay continuity | Director of Payroll and Billing | Controller | Cell; payroll vendor fraud desk |
| Cyber and crime insurers | Carrier breach hotline ($5M limit, $100K retention); crime carrier ($250K social engineering sublimit) | Broker | Policy cards in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Communications | Director of Marketing | Outside crisis PR (through counsel) | Out-of-band group |
| Board, PE sponsor, lender | CEO informs the audit committee chair and the sponsor's operating partner; CFO informs the agent bank | COO | Phone |
| Law enforcement | FBI IC3 and field office | n/a | Numbers in the binder |

**Out-of-band first.** Assume the attacker can read email and chat. Use the pre-provisioned messaging group on personal phones and the printed call tree kept at HQ.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions.

## 1. Preparation checks (Identify / Protect)
- [x] SSO with number-matching push MFA and managed-device conditional access for the payroll platform
- [x] 24x7 MSSP monitoring of identity provider sign-ins (impossible travel, new devices)
- [x] Call-back verification for staff-entered bank changes
- [ ] Phishing-resistant authenticators for payroll staff (POAM-003 and R-002, due 2027-03-31). **Gap until it closes**
- [ ] Alerts on payroll register exports and bank-change spikes in the SIEM (POAM-006, due 2027-01-31). **Gap until it closes**
- [ ] Integration secrets in the secrets service and split by job (POAM-004, due 2026-11-30)
- [ ] Written bank-change freeze and session-revocation procedure agreed with the payroll and ATS vendors (POAM-012)
- [ ] Residence-state report of affected people, runnable in under 1 hour (P03 G-082)
- [ ] English and Spanish notice templates approved by counsel (P03 G-142)
- [x] Incident binder at HQ: this runbook, call tree, notification matrix, vendor fraud desk numbers

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Several associates report on payday that pay did not arrive or their bank account changed without their request | Branch calls; contact center | Contact center opens a Security ticket (pay diversion is an incident, POL-03 4.3); payroll pulls the bank-change report for the last 14 days |
| A payroll specialist reports an MFA prompt they did not start, or entering a password on a page reached from a link | Staff report | Revoke sessions, reset, and review payroll sign-ins and exports; declare if any export or change occurred |
| Sign-in to the payroll platform from a new device or unusual location, especially just after a push approval | IdP risk alert via the MSSP | MSSP calls the incident commander within 30 minutes |
| Bulk export of the employee register, or many bank changes in one session | Payroll alert (once POAM-006 closes); payroll specialist notice | Declare immediately |
| Calls to the payroll API from an unknown address or outside the integration schedule | Cloud and API logs | Revoke the key; declare |
| Vendor tells the firm of a breach at its end | Payroll or ATS vendor (Fla. Stat. 501.171(6)) | Declare; request the information needed for notice |
| Extortion email claiming to hold associate data | Email | Declare; preserve the message; do not reply |

**Severity 1 (declare immediately):** any confirmed export or download of associate SSNs or bank data, more than 10 unauthorized bank changes, or use of the payroll API key by an unknown party.

**Record the time of determination.** Florida's 30-day clocks run from the determination of a breach or reason to believe a breach occurred (Fla. Stat. 501.171(3)(a), (4)(a)). The Director of Compliance and Privacy writes it in the decision log, with who decided what and when.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-30 min | **Freeze all bank-account changes** in the payroll platform and the associate portal; if firm admin accounts may be compromised, ask the vendor fraud desk to freeze at the vendor side | Director of Payroll and Billing with the payroll vendor | Freeze confirmed in writing |
| 0-60 min | Disable the compromised user; revoke all payroll and ATS sessions in the identity provider; remove unknown MFA devices; rotate the payroll API key and pause integration jobs | IT Director; Security Manager | No active sessions; old key rejected |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics; notify the crime carrier of diverted funds | CFO | Claim numbers; counsel on the call |
| 0-2 h | List every bank change and export in the last 60 days (as far as logs allow); payroll specialists confirm each change by call-back to the phone on file | Director of Payroll and Billing | Fraudulent changes identified |
| 0-2 h | Ask the payroll vendor's bank to stop or recall pending deposits to fraudulent accounts; ask receiving banks to freeze funds | Controller with the payroll vendor | Recall requests logged |
| 1-2 h | If any I-9 module data or E-Verify account may be involved, notify DHS E-Verify **immediately** (MOU Art. II.A.16) | Director of Compliance and Privacy | Call or email logged |
| 1-2 h | Convene the CMT; first situation report (scope, payroll impact, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff and associate briefing scripts: pay will be made whole; the firm will never ask for bank details by text or email; how to verify a call from the firm | Director of Marketing with the CHRO | Scripts sent by text; branches and the contact center briefed |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner; CFO informs the agent bank under the credit agreement | CEO; CFO | Notices given |

**Pay the associates.** Diverted pay is still owed. The Director of Payroll and Billing runs an off-cycle payment to verified accounts (or issues pay cards) for every associate whose pay was diverted, within 1 business day (POL-03 4.7). This decision is pre-approved by the COO and does not wait for fund recovery or the insurance claim.

## 4. Analysis (RS.AN)
1. **Scope.** Which payroll accounts, API keys, and sessions were used; which reports and exports ran; whether the attacker also reached email, the ATS (I-9 module, consumer reports), the credentialing platform, the VMS, or the data warehouse. Sources: identity provider sign-ins, payroll audit reports (export them now; the vendor keeps only 180 days), ATS admin history, cloud and API logs, and EDR telemetry.
2. **Initial access and dwell time.** Identify the phishing message and the relay page, or how the API key was obtained (repository, image, contractor device), and the first unauthorized action.
3. **Preserve evidence.** Forensics exports logs before they expire, with chain of custody (who collected, when, hash, storage). Evidence is held by the forensic firm under counsel.
4. **Data involved.** List the exported fields and record counts. Name with SSN is personal information under Fla. Stat. 501.171(1)(g)1.a.(I). A financial account number counts only with a code or password that permits access ((1)(g)1.a.(III)), so bank numbers alone may not trigger Florida notice; counsel confirms, and other states may differ. If credential files were reached, medical information ((IV)) is involved; if timekeeping data was reached, biometric data ((VI)) and geolocation ((VII)) may be.
5. **Who is affected and where they live.** Run the residence-state report for every person in the export (current and former associates, candidates, clinicians). This drives which state laws apply and every notice count.
6. **MSP program.** Check whether VMS data or payrolled MSP workers are in the export; if so, the MSP clients' 48-hour notice applies.

## 5. Containment and eradication (RS.MI)
1. Block the phishing domains and sender addresses; search and purge the same message from all mailboxes.
2. Move payroll staff to phishing-resistant authenticators as an emergency change, or until then require vendor-side call-back for every payroll administrator sign-in.
3. Rotate every integration secret, move them to the secrets service, and remove keys from images and the repository history.
4. Check for persistence: new payroll users, changed notification emails, report schedules sending data outside the firm, mail forwarding rules, new API clients.
5. Keep the bank-change freeze until every change since the compromise date has been verified by call-back.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice. The Director of Compliance and Privacy keeps the **decision log** (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a breach of security under Fla. Stat. 501.171(1)(a) and the law of each affected person's state? | Director of Compliance and Privacy with the General Counsel and counsel | Decision log |
| D2 | Time of determination (starts the Florida 30-day clocks) | Director of Compliance and Privacy | Decision log |
| D3 | Number affected: total, by state, and Florida residents (thresholds: 500 Floridians for the Department of Legal Affairs; more than 1,000 notices at once for consumer reporting agencies) | Director of Compliance and Privacy | Affected-person list |
| D4 | Has law enforcement asked in writing for a delay (501.171(4)(b))? | General Counsel | Written request on file |
| D5 | Contract notices due (MSP clients 48 hours; health care and other clients per contract; lender; insurers) | General Counsel and CFO | Contract register |
| D6 | Extortion decision, if any | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotlines; counsel engaged | CFO |
| Immediately, if E-Verify data is involved | DHS E-Verify notice (888-464-4218 or E-Verify@dhs.gov, subject "Privacy Incident - Password") | Director of Compliance and Privacy |
| Day 0-1 | IC3 report for payroll diversion | Security Manager through counsel |
| Day 0-2 | MSP client notice within 48 hours of confirmation, if program data is involved | VP Managed Workforce Solutions through counsel |
| Day 0-3 | IRS notice to dataloss@irs.gov, subject "W2 Data Loss", contact details only | Controller |
| As soon as scoped | Breach determination documented (D1, D2) | Director of Compliance and Privacy |
| Within 30 days of determination | Florida individual notices by mail or email (English and Spanish); Department of Legal Affairs notice if 500 or more Floridians. Individual notices may get 15 more days only if good cause is given to the department in writing within the 30 days | General Counsel and Director of Compliance and Privacy |
| Without unreasonable delay | Nationwide consumer reporting agencies if more than 1,000 people are notified at once | General Counsel |
| Per each state's law | Residents of other states and their regulators | Outside counsel |

**Plan to the 30-day clock.** It runs from determination, not from the end of the investigation. With about 168,000 records in the register, a full-register export means the residence-state report, mailing vendor, and call center must be ready in days, not weeks.

**Credit monitoring and identity protection** for affected people is a firm decision taken with counsel and the insurer; it is not stated as a Florida requirement here.

**Extortion (POL-03 4.8).** Any payment requires the CEO, the General Counsel, and the insurer; an **OFAC sanctions check**; and a report to law enforcement. Paying does not remove notice duties.

**Communications.**
- Associates: text and email from a known short code, branch scripts, and a hotline through the insurer's notification vendor. Never include links that ask for bank details.
- Clients and MSP clients: direct call from the account executive or VP, then written notice where contracts require it.
- Media: holding statement approved by counsel; no technical details.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05), with the payday override in effect:
1. Identity provider and payroll platform access for the payroll team, with all sessions revoked and the strongest available authenticators
2. Verified bank data for every associate whose account changed (call-back list complete), then lift the bank-change freeze
3. Integration jobs restarted with new, scoped keys; reconciliation of new hires, rates, and time since the compromise
4. Weekly payroll on schedule (BP-01, MTD 48 hours), with the Controller reviewing every bank change since the incident
5. Data warehouse access only after full SSNs and bank numbers are removed (POAM-002)

**Validate before closing recovery:** no unknown users, API clients, or report schedules; all diverted associates paid; the next weekly payroll reconciled; forensics sign-off. Tell associates and clients when normal operations resume (RC.CO-03).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.10).
- Update the risk register (P01 R-001, R-002, R-003, R-021, R-052), the POA&M (P07), and this runbook.
- Keep any Florida no-harm determination at least 5 years (501.171(4)(c)) and all incident records at least 6 years (POL-01 4.12).

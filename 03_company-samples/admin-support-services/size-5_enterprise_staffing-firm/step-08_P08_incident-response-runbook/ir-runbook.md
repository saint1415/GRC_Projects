# Incident Response Runbook: Payroll and HR System Breach Exposing Worker PII

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded staffing and workforce solutions company; 38 states and DC) |
| Tier / Vertical | Enterprise / Administrative and Support and Waste Management and Remediation Services |
| Incident type | Compromise of the payroll and HR platform (ALPP) through a privileged account: theft of associate personal information (SSNs, bank accounts, addresses, pay, Form I-9 and E-Verify data) and diversion of pay, with an extortion demand. Includes the SEC materiality assessment and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Payroll Engine Recovery Procedure |
| Why this incident | It joins the top risks in P01: help desk social engineering of a payroll administrator (R-023), mass exfiltration (R-003), payroll diversion (R-001, R-013), and late or inaccurate disclosure (R-010) |
| Runbook owner | Director of Security Operations, with the General Counsel for sections 6 and 7 and the Senior Vice President, Payroll and Associate Services for section 5.2 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise payroll diversion and data theft tabletop 2026-03-19 (technical, payroll, and privacy response; **the disclosure committee did not take part**). Next: full tabletop with the disclosure committee on 2026-11-12 (POAM-013) |
| Notification matrix | `notification-matrix.csv` (29 obligations: 4 generic state, 6 Florida worked example, 5 SEC and disclosure, E-Verify, IRS, 2 federal contract, 6 contractual, plus law enforcement, OFAC, CIRCIA status, and HIPAA status rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Senior Vice President, Payroll and Associate Services | Crisis line |
| Payroll protection lead | Senior Vice President, Payroll and Associate Services | Vice President, Payroll Technology | Crisis line |
| Treasury | Treasurer | Assistant Treasurer | Direct mobile; bank fraud lines in the incident binder |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Employment eligibility (E-Verify, Form I-9) | Vice President, Employment Compliance | Director of Employment Eligibility Compliance | Direct mobile |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Client communications | Segment presidents; Vice President, Payrolling Services (SL-2); Vice President, Product, Workforce Management Platform (SL-1); Vice President, Government Solutions | Account managers | Crisis line |
| Associate communications | Vice President, Associate Service Center | Vice President, Corporate Communications | Crisis line |
| Media and investors | Vice President, Corporate Communications; Vice President, Investor Relations | Outside communications firm | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the identity platform may be compromised: this scenario starts with a stolen privileged identity. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at each payroll center.

## 1. Preparation checks (Identify / Protect)
- [ ] Privileged MFA resets require live video verification with the user's manager (POL-02 4.10); the SIEM alerts on "MFA reset followed by export or bank-change activity within 24 hours"
- [ ] Bulk export use cases live for the ATS and payroll engine (**gap until POAM-016 closes**)
- [ ] Associate bank-change anomaly scoring and holds (**gap until POAM-001 closes**)
- [ ] Pay file hashing and auto-hold on the SFTP staging server (**gap until POAM-019 closes**)
- [ ] Immutable backups of the payroll database restore-tested in the last 90 days (CP-9); prior-week advance procedure rehearsed by the three payroll centers
- [ ] SIEM receives logs from all ALPP components, **except ACQ-1 systems (gap until POAM-003 closes)** and the DC-2 I-9 archive (**POAM-007**)
- [ ] Materiality playbook with the PII cost model, 8-K templates, and current disclosure committee roster (**gap until POAM-013 closes**)
- [ ] Outside counsel's state breach law matrix updated in the last 12 months; mail vendor, call center, and credit and identity monitoring provider on retainer
- [ ] Bank and paycard program manager fraud contacts confirmed this quarter

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| MFA reset for a payroll, Treasury, or administrator account followed by exports, report runs, or bank-change activity | Identity platform; SIEM correlation | Revoke sessions; suspend the account; open a severity-1 case |
| Bulk export or unusual report volume from the payroll engine or ATS | Database activity monitoring; SaaS audit logs (bulk export use case) | Block the session; preserve logs; open a case |
| Spike in associate bank changes, many changes to the same bank or routing number, or changes from new devices shortly before the Thursday cutoff | Fraud rules; payroll operations; Associate Service Center | Freeze bank changes made since the spike began; open a case |
| Associates report missing pay on Friday | Associate Service Center; branches; social media | Treat as possible diversion; check change history for the affected associates |
| Unexpected access to Form I-9 records or E-Verify case data in SYS-02 | SYS-02 audit trail; vendor alert | Open a case; notify the Vice President, Employment Compliance; start the DHS notice step (section 7.5) |
| Extortion message or leak-site post naming the firm or associate data | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |
| A vendor reports a breach of associate data (screening provider, paycard manager, time capture, onboarding) | Vendor notice under contract or state law (Florida example: 501.171(6)) | Open a vendor incident case; start the third-party track in section 7.10 |

**Declare a severity-1 incident when** a privileged ALPP account is confirmed misused, bulk associate data is confirmed exported, more than 100 bank changes are confirmed fraudulent in one pay cycle, or an extortion claim names associate data.

**Record three times, separately:**
1. **Suspicion of E-Verify data exposure:** starts the "immediately" DHS notice under MOU Art. II.A.16. Do not wait for confirmation.
2. **Determination of a breach (or reason to believe one occurred):** starts state clocks that run from determination, such as Florida's 30 days (Fla. Stat. 501.171(3)-(4)). Counsel records this date.
3. **Materiality determination time (SEC):** recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. Severity, the payroll window, and the first 4 hours (RS.MA, RS.MI)
**Severity scale (STD-03.1) with the payroll window.** The BIA (P05) shows that the same outage is far worse between Monday 06:00 and Thursday 14:00 (Eastern), when payroll runs and ACH files go to the banks. Inside that window, every incident that touches SYS-03, SYS-04, the integration platform, the SFTP staging service, or bank-change functions is **raised one severity level**, and the payroll protection lead joins the bridge at once.

| Severity | Definition | Outside the payroll window | Inside the payroll window |
|---|---|---|---|
| 1 | Confirmed privileged compromise, bulk data theft, pay diversion over 100 associates, or a payroll engine outage | Crisis team within 1 hour | Crisis team within 30 minutes; payroll go or no-go decision by 12:00 Thursday |
| 2 | Suspected compromise of an ALPP account; pay diversion under 100 associates; partial outage | Incident commander within 2 hours | Treated as severity 1 |
| 3 | Single-user incident with no pay or bulk data impact | SOC handles | Treated as severity 2 |

**First 4 hours:**
| Step | Who | Done when |
|---|---|---|
| 1. Suspend the compromised identity; revoke all its sessions and tokens; reset its MFA only after video verification by a second administrator | Identity team | Revocation logged |
| 2. Freeze all associate and staff bank-account changes made since the earliest suspicious event; queue them for out-of-band verification | Payroll protection lead | Change freeze confirmed |
| 3. Remove export rights from all non-essential roles in the payroll engine and ATS for the duration; block the attacker's IP ranges and devices | Payroll Engine Application Manager; SOC | Rights removed; blocks confirmed |
| 4. Treasury calls Banks A and B and the paycard program manager: hold or verify outgoing files not yet transmitted; ask about recall of any fraudulent entries already sent | Treasurer | Bank case numbers |
| 5. Confirm the payroll database backups and the SFTP staging area are untouched; preserve current pay files and hashes | Cloud Platform Engineering; Treasurer | Backup and file integrity confirmed |
| 6. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 7. If SYS-02 or E-Verify could be involved, the Vice President, Employment Compliance notifies DHS E-Verify immediately (matrix row "E-Verify breach notice to DHS") | Vice President, Employment Compliance | DHS notice logged |
| 8. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** identities used, sessions, reports run, exports, files staged, bank changes made, and SYS-02 records opened. Sources: identity platform logs, payroll engine audit trail and database activity monitoring, SaaS audit logs (SYS-01, SYS-02, SYS-04), SFTP logs, PAM records, and SIEM correlation. For ACQ-1 systems, collect logs locally, because they are not in the SIEM.
2. **Initial access:** help desk social engineering, MFA fatigue, phishing, a stolen session token, a client integration key, or ACQ-1. Check the help desk ticket and call recording for the MFA reset first.
3. **Evidence:** forensics exports logs before they roll over; chain of custody kept in the evidence register; hashes recorded for each artifact.
4. **Data taken:** determine which records left, for whom, and with which elements (name, SSN, bank account, address, date of birth, pay, Form I-9 images, E-Verify case results). Tie every record to the person's **state of residence** from the payroll engine address. Separate four groups: (a) associates; (b) internal staff; (c) SL-2 client-sourced workers; (d) candidates. **This drives section 7.**
5. **Money moved:** list every bank change made by the attacker, the pay date affected, and whether funds left. The Treasurer reconciles with the banks.
6. **Integrity:** confirm no pay rules, tax tables, or bank file settings were changed (compare to the last approved configuration and the change log). If integrity cannot be confirmed, the payroll protection lead decides whether to run the next payroll from the last verified register (section 5.2).
7. **Business impact:** Finance estimates costs with the P05 values and the cost model in section 6 (for example, about $2.4 million per day if payroll is delayed; about $18.5 million of invoices per business day if billing stops). These estimates feed section 6.

## 5. Containment, eradication, and payroll protection (RS.MI)
### 5.1 Contain and eradicate
1. Contain by identity and by component: suspend affected accounts, rotate payroll engine service credentials, SFTP keys, tokenization service credentials, and client integration keys that the attacker could have seen.
2. Reset all privileged credentials touched by the attacker's session; review every MFA reset in the last 30 days.
3. Remove any persistence (new accounts, API tokens, mailbox rules, scheduled reports to outside addresses).
4. Close the initial access path (for example, suspend phone-based MFA resets until video verification is enforced) before reconnecting.
5. Forensics confirms persistence is removed before normal operations resume.

### 5.2 Protect the next payroll
1. **Go or no-go by Thursday 12:00 (Eastern):** the payroll protection lead, Treasurer, and CISO decide whether the payroll engine and pay files can be trusted. If not, run the prior-week advance procedure (P05 BP-01 workaround) for associates on continuing assignments, with true-up the next week.
2. **Every bank change since the earliest suspicious event** is reverted to the previous account unless the associate confirms the change through the app with a fresh out-of-band code.
3. **Associates whose pay was diverted** are paid the same day by instant paycard funding or courier check once their identity is confirmed. The firm absorbs the loss and pursues recovery; associates are never asked to wait for the bank.
4. **Pay files** are regenerated from the verified register and hashed; Treasury confirms totals with each bank by phone before release.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet and cost model (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time, and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of associate, client, media, and investor communications with the filing; brief the audit committee and risk and technology committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Cost model below; lost or deferred revenue from P05 values; insurance coverage and retention ($50 million tower); effect on liquidity and covenants |
| Operational | Payrolls missed or delayed and for how many associates; segments, sites, and clients affected; SL-1 and SL-2 service disruption |
| Data | Number of people and states; data types (SSNs, bank accounts, Form I-9 images, E-Verify data, consumer reports); whether data was published |
| People | Associates harmed by diverted pay or identity theft; clinicians unable to work shifts |
| Legal and regulatory | Expected state attorney general inquiries, class actions, FTC or CFPB interest, DHS E-Verify inquiry, contracting officer actions, client contract claims |
| Reputation and strategy | Media coverage; managed-program client loss (SL-1 contracts are the largest relationships); effect on recruiting, since applicants choose firms they trust |

**PII breach cost model (draft v0.9, finalized with POAM-013 by 2026-10-31).** For each scenario size the committee estimates: (a) notification and call center cost per person; (b) credit and identity monitoring cost per enrolled person, assuming an enrollment rate counsel provides; (c) reimbursement of diverted pay; (d) forensic, legal, and outside counsel fees; (e) client contract credits and claims, using the contract register's notice and liability terms; (f) revenue at risk from client loss, using P05 segment revenue; (g) regulatory and litigation reserves set by counsel. Unit costs come from the insurer's panel vendors and the firm's 2025 fraud data; they are fictional placeholders until the model is approved and are not stated here.

**Worked example of the clocks (fictional dates).** A caller persuades the service desk to reset a payroll administrator's MFA on Monday 2027-03-01 at 18:40. Overnight the attacker exports the associate master file (about 1.2 million current and former associates in 50 states) and changes 3,800 bank accounts. On Wednesday 2027-03-03 at 09:15 the SOC's reset-then-export rule fires (declaration). Because SYS-02 records were opened, DHS E-Verify is notified the same morning. The bank-change freeze and file holds stop most diversions before the Thursday 2027-03-04 cutoff. The committee convenes Thursday and determines materiality on Friday 2027-03-05 at 15:00. **The Form 8-K is due by Thursday 2027-03-11** (4 business days: March 8, 9, 10, and 11). Forensics confirms SSNs and bank data left the firm on Monday 2027-03-08; counsel records that as the Florida determination date, so **Florida individual and Department notices are due by Wednesday 2027-04-07**. Counsel must also decide whether a "reason to believe a breach occurred" arose earlier (for example, at declaration on 2027-03-03, or when an extortion message claimed data theft), which would move the Florida dates forward. Other states' clocks come from counsel's matrix, and the shortest one sets the plan.

## 7. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Breach determination: counsel and the Chief Privacy Officer decide whether a breach of personal information occurred under each relevant state's definition, and record the date | Chief Privacy Officer; outside counsel | Signed determination with date |
| 7.2 | Build the affected population from forensic results: each person, data elements, and **state of residence** (payroll engine and ATS addresses). Keep the four groups from section 4 separate (associates, internal staff, SL-2 workers, candidates) | Chief Privacy Officer; data team | Affected-person file with state counts |
| 7.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules, and any offer of identity protection services a state requires. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.4 | **Florida worked example:** individual notice within 30 days of determining the breach (15 more days only on written good cause to the Department within the 30 days); Department of Legal Affairs notice within 30 days if 500 or more Floridians (no extension); consumer reporting agencies if more than 1,000 are notified at once; a no-harm determination is not available when SSNs were taken | General Counsel | Florida filings |
| 7.5 | **E-Verify:** DHS notified immediately on suspicion (done in section 3, step 7); follow up with DHS as facts develop. **Form I-9 records:** document what was accessed; the Form I-9 retention duties continue unchanged | Vice President, Employment Compliance | DHS notice and follow-up log |
| 7.6 | **IRS:** report W-2 and SSN data loss to the IRS (dataloss@irs.gov, subject "W2 Data Loss") so it can watch for fraudulent returns; do not send personal information | Controller | IRS notice logged |
| 7.7 | **Plan to the shortest clock** across every state, DHS, the SEC, and contracts. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.8 | Honor any law enforcement delay request (Florida example: 501.171(4)(b)) and document it | General Counsel | Delay record |
| 7.9 | Engage the mail vendor, call center (toll-free line staffed for at least 90 days), and the credit and identity monitoring provider; give associates a way to verify notices are genuine, since criminals will imitate them | Chief Privacy Officer; Vice President, Associate Service Center | Vendors active |
| 7.10 | **Contractual notices:** SL-2 payrolling clients, SL-1 clients if affected, hospital clients under their BAAs, commercial clients whose data was involved, federal and state agency contracting officers for Government Solutions, banks, the paycard program manager, and the insurer, per contract | Contract owners | Contract notices logged |
| 7.11 | Track inbound vendor notices (state third-party agent laws, Florida example 501.171(6)) if the incident started at a vendor | Director of Third-Party Risk Management | Vendor notices logged |

**HIPAA does not set these clocks.** The firm is not a HIPAA business associate (P03 section 1), so 45 CFR 164.410 does not apply. Hospital BAAs are handled as contractual notices in step 7.10.

**Extortion decision:** any payment requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.7). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove notification or disclosure duties, and it does not get the data back.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean state first:
1. Identity platform and break-glass access; enforce video verification for privileged MFA resets
2. Network core, SD-WAN, DNS, colocation links
3. Security tooling (EDR console, SIEM) with the new detection rules from this incident
4. Integration platform and the Workforce Management Platform (tell SL-1 clients the status)
5. Payroll engine and bank and paycard file transfer: restore or verify configuration, rotate all keys, regenerate files from the verified register, hash, and confirm totals with the banks
6. ATS and time capture; re-enable bank changes only with out-of-band confirmation
7. Onboarding and Form I-9 platform; E-Verify accounts reviewed and passwords reset
8. ACQ-1 systems (if involved)
9. Associate Service Center scripts for affected associates; branch talking points
10. ERP and internal HCM; data platform extracts (resume only after the extract no longer carries clear-text SSNs and bank numbers, POAM-004)

**Validate before reconnecting:** EDR clean, credentials rotated, logging to the SIEM, and a parallel payroll check passed. Keep the prior-week advance procedure available until two normal payrolls run cleanly. Tell associates, clients, and staff when services return (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.10).
- Update the risk register (P01: R-001, R-003, R-010, R-013, R-023), the POA&M (P07), this runbook, and the materiality playbook and cost model.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality determination minutes, breach determinations, and the DHS notice, for at least 7 years (POL-01 4.11).

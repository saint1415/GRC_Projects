# Incident Response Runbook: Business Email Compromise and Taxpayer Data Theft

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP (national CPA and tax firm; 64 offices in 14 states; clients in all 50 states) |
| Tier / Vertical | Enterprise / Professional, Scientific, and Technical Services |
| Incident type | Business email compromise (BEC) of one or more staff mailboxes through adversary-in-the-middle phishing, theft of client tax documents from mail and the DMS, and attempted refund and payroll diversion, including an **Incident Disclosure Committee step** (client-impact assessment and notice to SEC-registrant clients) and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 Incident Disclosure Committee and Client-Impact Procedure; PRC-03.3 Multi-State Breach Notification Procedure. With POL-03, this runbook is part of the written incident response plan required by 16 CFR 314.4(h) (N54-R01) |
| Runbook owner | Director of Security Operations, with the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-08 |
| Last tested | Not yet for this incident type. The ransomware runbook was exercised on 2026-02-24. **First tabletop with the Incident Disclosure Committee and e-file operations: 2026-11-19 (POAM-010)** |
| Notification matrix | `notification-matrix.csv` (31 obligations: 2 FTC, 3 IRS and state tax agency, 1 law enforcement, 3 generic state, 8 Florida worked example, 2 HIPAA business associate, 2 client contract, 1 SEC (not applicable to the firm), 5 federal contract, 1 OFAC, 1 CIRCIA status, 2 insurance) |

**Why there is no Form 8-K step for the firm.** The Enterprise tier normally includes an SEC materiality step. The firm is a private partnership owned by its CPA partners (Fla. Stat. 473.309(1)(b)), not an SEC registrant, so Form 8-K Item 1.05 does not apply to it. The SEC said registrants are not exempt from disclosing incidents on third-party systems they use (SEC Release 33-11216). About 140 issuer audit clients and many SL-1 and SL-2 clients are registrants, so an incident at the firm can start **their** materiality clock. Section 6 replaces the 8-K step with the Incident Disclosure Committee's client-impact assessment and prompt, accurate client notice.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on firm phones) |
| Executive incident lead | CISO (Qualified Individual) | CIO | Out-of-band group on firm mobile phones |
| Incident Disclosure Committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Incident Disclosure Committee members | CFO, Chief Risk Officer, CISO, Chief Privacy Officer, National Tax Leader, Vice Chair, Assurance, Chief Communications Officer; outside breach counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach determinations | Chief Privacy Officer | Deputy General Counsel | Direct mobile |
| IRS and state tax agency reporting | Director of e-file Operations (single point of contact for all 30 EFINs) | Responsible Official for the affected EFIN | Stakeholder Liaison numbers in the incident binder |
| Tax operations (return holds, bank change checks) | National Tax Leader | Director of Tax Operations | Crisis line |
| SL-1 and SL-2 client service | Managing Principals, Client Accounting Services and Tax Compliance Outsourcing | Their deputies | Crisis line |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | Managed security service provider incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Chief Communications Officer | Deputy | Direct mobile |
| Law enforcement | FBI field office or IC3 | Secret Service field office if directed | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read mail in compromised mailboxes and may hold valid session tokens for others. Coordinate by phone, the out-of-band bridge, and the printed binder. Never discuss the response by email until the incident commander confirms the tenant is clean.

## 1. Preparation checks (Identify / Protect)
- [ ] Phishing-resistant MFA and device-bound sessions for all tax staff (IA-2(2)). **Gap until POAM-001 closes (2027-01-15)**
- [ ] Browser email blocked from unmanaged devices (AC-20). **Gap until POAM-001 closes**
- [ ] Token replay and role-based bulk export detections live (SI-4). **Gap until POAM-004 closes (2026-12-31)**
- [ ] Mailbox audit, sign-in, and DMS logs retained 1 year online in the SIEM (AU-11); AF-05 tenant logs exported to the SIEM (**gap until POAM-005**)
- [ ] Call-back rule for any change to refund bank details, client email, or vendor payment details (POL-05 4.3)
- [ ] Alert on bank account changes after reviewer approval (SI-4(12)); weekly EFIN and PTIN volume check in season
- [ ] EFIN-to-Responsible Official map current, including AF-05 and AF-06 EFINs (**gap until POAM-010**)
- [ ] State law matrix updated in the last 12 months and client notice register current (**gap until POAM-023**)
- [ ] Break-glass accounts sealed and tested this quarter (POL-02 4.12)
- [ ] Outside counsel, forensics, mail vendor, call center, and credit monitoring contracts confirmed before each filing season

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A client asks about an email "from the firm" requesting documents, payment, or new bank details | Client call, contact center | Log the time. Call the security hotline. Do not reply to the thread |
| A request to change a refund direct deposit account on a return, or an SL-1 employee's direct deposit | Preparer, reviewer, SL-1 staff | Freeze the change; call back on the number on file; report to the hotline |
| A staff member approved an MFA prompt they did not start, or entered credentials on a page that then failed | Staff report; report-phish button | SOC revokes sessions and refresh tokens and resets credentials immediately |
| Sign-in from a new device or hosting network with a valid session and no MFA prompt (token replay) | SIEM (after POAM-004); impossible travel alerts | Revoke sessions; open a severity-1 case |
| New inbox rule that moves, deletes, or forwards mail; new connected app consent | SIEM alert | Open a case; record the rule before removal |
| Bulk download from the DMS or mailbox sync from a new device | Behavior analytics | Open a case; suspend the session |
| E-file reject for a duplicate SSN, or IRS notices about returns clients did not file | e-file operations, clients | Open a case; check for data theft |
| Returns filed per EFIN or PTIN above the firm's count | Weekly EFIN and PTIN check | Director of e-file Operations calls the Stakeholder Liaison and opens a case |

**Declare a severity-1 BEC incident when** an unauthorized sign-in or session replay to any firm mailbox, the DMS, or the portal staff interface is confirmed; a malicious rule, forwarding, or app consent is found; or clients report requests sent from a firm address that staff did not send.

**Record three dates in the incident log. Each starts a different clock:**
| Date | Definition | Clock it starts |
|---|---|---|
| Discovery | First day the event is known to any employee, officer, or other agent other than the attacker (16 CFR 314.4(j)(2)); for PHI, also the day it would have been known with reasonable diligence (45 CFR 164.410(a)(2)) | FTC notice no later than 30 days; business associate notice no later than 60 calendar days |
| Confirmation | The incident is confirmed as an event that can result in unauthorized disclosure, misuse, modification, or destruction of taxpayer information | IRS report no later than the next business day (Pub. 1345); client contract notices |
| Determination | The firm determines a breach occurred, or has reason to believe one occurred (state laws; Fla. Stat. 501.171 worked example) | Florida individual and Department notices no later than 30 days; third-party agent notices to clients no later than 10 days |

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke all sessions and refresh tokens for affected accounts; reset passwords; remove and re-register MFA after verifying the user in person or by video with a manager | SOC; Identity team | Attacker sessions ended |
| 2. Export mailbox audit, sign-in, message trace, DMS, and portal logs for the last 90 days **before any cleanup**; record hash values | SOC | Evidence register entries |
| 3. Record, then remove, malicious inbox rules, forwarding, delegates, and app consents; search the tenant for the same rules, senders, and sign-in sources | SOC; Director of Collaboration Services | Tenant sweep complete |
| 4. Block attacker infrastructure and lookalike domains; purge the phishing message from all mailboxes | SOC | Blocks and purge confirmed |
| 5. Freeze every refund bank account, address, and email change entered in the last 30 days in the tax application and SL-1 payroll engine, and hold e-file transmission of affected returns | National Tax Leader; Managing Principal, Client Accounting Services | Hold list created |
| 6. CISO briefs the General Counsel and the CEO and Managing Partner; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 7. Start the incident log (timeline, decisions, who, when) and record the discovery date | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Initial access.** Confirm how accounts were taken: adversary-in-the-middle page, push approval, legacy authentication (the 9 exception mailboxes), password reuse, or a printer-scanner scan-to-email account (R-064). Find every recipient of the same phishing message and every account that signed in from the attacker's sources.
2. **Scope of access.** From mailbox, DMS, and portal logs, list every message, attachment, and file the attacker opened, downloaded, or synced. Where item-level records are missing, **assume every item in the mailbox or folder was accessed** (16 CFR 314.2(m) presumes acquisition from unauthorized access unless reliable evidence shows otherwise).
3. **Messages sent by the attacker.** Search sent and deleted items and message trace for messages to clients, vendors, staff, and taxing authorities. List each recipient asked for documents, payments, or bank changes.
4. **Diversion check.** List every bank account change in the tax application and payroll engine in the period. Compare with prior-year data, call the client on the number on file, and classify each return or payroll as held, transmitted and accepted, or not affected.
5. **Data inventory and count.** Build one list of affected people from the documents involved: individual clients, spouses and dependents, owners and employees named on business returns, SL-1 client employees, and global mobility assignees. Record data elements, whether the person is an FTC "consumer" (an individual tax client), whether PHI is involved, which client business the data belongs to, and **state of residence**.
6. **Client impact.** Identify every client whose data or services were affected, and flag SEC-registrant clients (issuer audit clients, SL-1 and SL-2 registrants). Sources: engagement codes on DMS folders, mailbox correspondents, and the practice management system.
7. **Evidence.** Forensics images any affected laptop if malware or a token theft tool is suspected; keep logs with chain of custody; preserve attacker messages with full headers.

## 5. Containment and eradication (RS.MI)
1. Disable or reset every account that shows the attacker's sources, rules, or app consents; rotate shared and service mailbox credentials.
2. Block the specific session and device identifiers; require reauthentication tenant-wide for high-risk groups (tax reviewers, e-file operations, SL-1 payroll staff).
3. Reimage affected laptops; change printer-scanner passwords at the affected hub (POAM-012).
4. Warn targeted clients out of band: phone first, then a portal message. Tell them the firm never asks for bank changes by email.
5. Keep held returns and payrolls on hold until the client confirms bank details by phone and the Stakeholder Liaison's guidance is received.

## 6. Incident Disclosure Committee: client impact and notification decisions
This step runs in parallel with sections 4 and 5. It does not wait for forensics to finish.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.3) | CISO | Brief logged |
| 6.2 | The committee convenes within 24 hours of confirmation and meets at least daily until notices are set | General Counsel | Minutes started |
| 6.3 | **Confidentiality and trading caution.** Data in the mailbox may include clients' material non-public information (tax provisions, deal files). Responders with access are reminded of the firm's independence and insider trading rules, and the access list is kept | General Counsel | Reminder sent; access list kept |
| 6.4 | **Client-impact assessment** using the worksheet below, for each affected client | Committee | Worksheet completed per client |
| 6.5 | **Notice decision and timing** for each client, recorded with date, time, and reasoning. SEC-registrant clients are told within their contract term and in any case promptly enough to make their own materiality determination; the target is 48 hours after confirmation | Committee (General Counsel records) | Decision minute signed |
| 6.6 | Notices give the client the facts it needs for its own decision: what data or services were affected, the time window, containment status, and a named contact. They do not speculate about the client's materiality or include technical details that would help the attacker | General Counsel; engagement partners | Notices sent and logged |
| 6.7 | Regulatory notices (FTC, IRS, states, health care clients, contracting officers) are planned to the shortest clock in `notification-matrix.csv` and approved by counsel (section 7) | Chief Privacy Officer; General Counsel | Master calendar |
| 6.8 | Brief the Audit and Risk Committee chair before external statements; align client, regulator, media, and staff messages | General Counsel; Chief Communications Officer | Messages approved |
| 6.9 | Keep reassessing as facts change; send updates to clients when the scope changes; carry lessons into the Qualified Individual's next report to the Partnership Board (314.4(i)) | Committee | Reassessment logged |

**Client-impact worksheet (firm playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Data | Types (SSNs, bank accounts, PHI, tax provisions, deal or audit evidence); number of individuals; whether material non-public information was exposed |
| Services | SL-1 payroll or SL-2 filing delays; audit timetable effects for issuer clients |
| Contract | Notice terms (from the register, POAM-023); business associate agreement terms; SOC report commitments |
| Fraud | Refund or payroll diversion attempts against the client's employees or owners |
| Regulatory | Whether the client may have its own notice or disclosure duties (state laws, HIPAA, SEC) |
| Relationship | Independence considerations for audit clients; reputational effect |

**Worked example of the clocks (fictional dates, tabletop script):**
| Date | Event | Clock effect |
|---|---|---|
| Mon 2027-02-08 | A tax senior manager enters credentials on a fake sign-in page during filing season and tells a colleague the page "looked odd," but no one reports it | Counsel decides whether this is "known to" an employee under 314.4(j)(2). The plan assumes it is: FTC target **Wed 2027-03-10** |
| Tue 2027-02-09 | A client calls about an email "from the firm" asking to change her refund account. Incident declared; sessions revoked | Discovery recorded no later than today |
| Wed 2027-02-10 | Forensics confirms the attacker synced the mailbox and downloaded 6,800 attachments and one DMS folder of SL-2 tax provision workpapers for two SEC-registrant clients; 41 bank change requests were sent | Confirmation. IRS report due by **Thu 2027-02-11**; made the same afternoon. Committee convenes |
| Thu 2027-02-11 | Committee completes the client-impact worksheet: both registrant clients notified that evening (contract term 48 hours) | Clients start their own materiality assessments |
| Fri 2027-02-12 | Counsel and the Chief Privacy Officer determine a breach: about 3,100 individual tax clients (FTC consumers), 1,300 SL-1 client employees, and 4,600 individuals in total across 31 states, including 2,200 Floridians | Florida notices due by Sun 2027-03-14, so sent by **Fri 2027-03-12**; Department notice required (500 or more Floridians); consumer reporting agencies required (more than 1,000). SL-1 client businesses notified as third-party agent by **Mon 2027-02-22**. Other states per counsel's matrix |

The FTC deadline (2027-03-10) comes before the Florida deadline (2027-03-12 target), so the master calendar starts there. If the committee had not assumed the earlier discovery date, the FTC deadline would move to 2027-03-11; planning to the earlier date removes that argument.

## 7. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out. The Chief Privacy Officer decides breach status with the General Counsel (POL-03 4.6).

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | **FTC (314.4(j)):** if 500 or more consumers, file on the ftc.gov form with the (j)(1)(i)-(vi) content no later than 30 days after discovery | General Counsel | FTC submission |
| 7.2 | **IRS and states' tax agencies:** Stakeholder Liaison report no later than the next business day after confirmation; state tax agencies through the Federation of Tax Administrators list; ask for guidance on held and transmitted returns | Director of e-file Operations | Report log |
| 7.3 | Build the affected-individual file with **state of residence** for every person, separated into: (a) the firm's own clients; (b) SL-1 and SL-2 client businesses' employees and assignees (the firm is a third-party agent); (c) PHI held as a business associate | Chief Privacy Officer; data team | Affected-individual file with state counts |
| 7.4 | **Third-party agent duty:** notify each client business whose data the firm maintains, with what it needs to give its own notices (Florida worked example: no later than 10 days after determination, 501.171(6)(a)); offer to send notices on its behalf where the contract allows | Managing Principals, SL-1 and SL-2 | Client notices |
| 7.5 | **Business associate duty:** if PHI was involved, notify each covered entity client without unreasonable delay and no later than 60 calendar days after discovery, with each individual's identity (164.410), or sooner under the agreement | Chief Privacy Officer | Covered entity notices |
| 7.6 | Apply **each state's law** for every state with affected residents, using counsel's matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.7 | **Florida worked example:** individual notice within 30 days after determination (a 15-day extension is available only for this notice, on written good cause to the Department); Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at a single time. The FTC notice does not satisfy Florida, because the FTC rule requires no notice to individuals (501.171(4)(g) does not apply) | General Counsel | Florida filings |
| 7.8 | **Plan to the shortest clock** across the FTC, IRS, every state, business associate agreements, and client contracts. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.9 | Honor any law enforcement delay request (FTC public disclosure delay; state provisions such as 501.171(4)(b)); document it | General Counsel | Delay record |
| 7.10 | Letters to individuals include the state-required content and the IRS-recommended advice: watch for IRS letters; file Form 14039 only if the IRS sends a notice or an e-filed return is rejected for a duplicate SSN; get an IRS Identity Protection PIN. Engage the mail vendor, call center, and credit monitoring provider | Chief Privacy Officer | Letters mailed |
| 7.11 | Check each affected federal contract for agency notice terms (FAR 52.204-21 itself has none) | Managing Principal, Government Services | Contract check log |

**Extortion:** if the attacker demands payment not to publish stolen documents, any payment needs the CEO and Managing Partner, the General Counsel, the insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any notification duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean state first:
1. Identity platform and administrator access (break-glass accounts if needed)
2. Security tooling validation: no sign-ins from attacker sources; new detections in place
3. Tax application and the e-file queue: release held returns only after call-back confirmation and Stakeholder Liaison guidance; file extensions early for any client whose return cannot be released in time
4. Email: cleaned mailboxes, or new mailboxes where forensics cannot clear the old ones
5. SL-1 payroll engine: release held payrolls after call-back; pay affected employees by check if needed
6. Client portal and DMS: confirm no portal or DMS access from attacker sources; move targeted clients to portal-only delivery
7. SL-2 corporate tax portal: confirm with each affected client before resuming exchanges
8. Practice management and billing: check vendor and client payment details

**Validate before closing:** no attacker sign-ins for 14 days, all affected users on phishing-resistant MFA, all held returns and payrolls resolved. Tell staff, clients, and affected individuals when normal service resumes (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days of closing (POL-03 4.11).
- Update the risk register (P01: R-001, R-004, R-009, R-016, R-017), the POA&M (P07), training content, and this runbook.
- Include the event, the response, and the notices in the Qualified Individual's next written report to the Partnership Board (314.4(i)(2)).
- Retain all records, including committee minutes and breach determinations, for at least 7 years (POL-01 4.13); this also covers the 5-year retention of any Florida no-harm determination (501.171(4)(c)).

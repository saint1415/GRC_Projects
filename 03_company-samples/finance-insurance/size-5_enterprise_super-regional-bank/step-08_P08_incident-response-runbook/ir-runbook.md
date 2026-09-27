# Incident Response Runbook: Business Email Compromise and Fraudulent Wire Transfers

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded bank holding company); Cris Santos Bank, N.A.; Cris Santos Investment Services, LLC |
| Tier / Vertical | Enterprise / Finance and Insurance |
| Incident type | Business email compromise (BEC) affecting several commercial clients: a compromised bank mailbox in commercial client services, harvested client treasury credentials, and fraudulent wires to new beneficiaries. Includes the 12 CFR 53.3 and 225.302 notification incident determination, the SAR steps, and the **SEC materiality assessment and Form 8-K Item 1.05** step |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Notification Incident Determination Procedure; POL-02 4.11 (callback and beneficiary confirmation) |
| Regulatory basis | 12 CFR 30 App. B III.C.1.g and Supplement A (N52-R02); 12 CFR 53.3 and 53.4; 12 CFR 225.302; 12 CFR 21.11; Form 8-K Item 1.05 and 17 CFR 229.106 (N52-R08); 17 CFR 248.30 (N52-R05, broker-dealer only); state breach laws |
| Runbook owner | Director of Cyber Defense, with the Head of Payments Operations for sections 3 and 5 and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-18 |
| Last tested | Tabletop 2026-03-26 (destructive attack scenario with the disclosure committee). BEC tabletop with the disclosure committee, including the related-occurrence step, scheduled for 2026-12-03 (POAM-017) |
| Notification matrix | `notification-matrix.csv` (36 obligations: 5 banking regulator, 4 SAR, 3 law enforcement and payments, 5 SEC, 2 Regulation S-P, 3 generic state, 5 Florida worked example, 2 contractual, OFAC, CIRCIA status, and 5 not-applicable rows kept to show the applicability check) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Cyber Defense | Cyber Defense Center manager on duty | Incident bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Wire recall, holds, and callback team | Head of Payments Operations | Wire operations manager | Wire room direct line |
| Treasury channel containment and client contact | Head of Treasury Management | Treasury support director | Direct mobile |
| Fraud rules and holds | Director of Fraud Strategy | Fraud operations manager | Fraud desk |
| SAR, FinCEN, and law enforcement | BSA/AML Officer | Deputy BSA/AML Officer | Direct mobile |
| Notification incident determination (53.3, 225.302) | CISO with the incident commander; Chief Risk Officer informed | Director of Technology and Operational Risk | Determination log in case management |
| Customer notice and state breach law | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, Chief Risk Officer, CISO, Chief Privacy Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Crisis management team chair | Chief Operating Officer | Head of Commercial Banking | Crisis line |
| Broker-dealer (if its customers are affected) | President, Cris Santos Investment Services, with its Chief Compliance Officer | Broker-dealer operations head | Direct mobile |
| Outside counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | Cyber Defense Center incident team | Retainer hotline |
| Insurance | Financial institution bond and cyber carriers | Broker | Claim lines in the incident binder (held by the CFO) |
| Communications | Head of Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Regulators and law enforcement | OCC supervisory office and Federal Reserve contacts; FBI field office and IC3 | Secondary contacts | Incident binder |

**Out-of-band first.** If a bank mailbox may be involved, assume email and chat are compromised. Coordinate on company phones, the out-of-band bridge, and the printed incident binder held at the Cyber Defense Center, DC-1, DC-2, and the alternate wire room.

## 1. Preparation checks (Identify / Protect)
- [ ] Incident binder current: this runbook, contacts, OCC and Federal Reserve points of contact, wire recall forms, the notification matrix, and the materiality worksheet
- [ ] Callback team routing for every email, phone, or fax payment instruction, including branch-originated ones (POL-02 4.11). **Gap until POAM-007 closes**
- [ ] Out-of-band confirmation of every new treasury beneficiary. **Today only at $100,000 or more (POAM-007)**
- [ ] Alert on a new beneficiary followed by a wire within 24 hours, any amount. **Gap until POAM-006 closes**
- [ ] Phishing-resistant MFA and token protection for commercial client service staff (POL-02 4.4); inbox rule alerts in the SIEM
- [ ] Core maintenance events in the SIEM. **Gap until POAM-003 closes**
- [ ] 12 CFR 53.4 designated contacts given to all critical bank service providers. **9 missing until POAM-019 closes**
- [ ] Role-based BEC training for commercial client service staff. **Gap until POAM-015 closes**
- [ ] Materiality playbook includes the related-occurrence step. **Gap until POAM-017 closes**

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Client reports a wire it did not send, or asks where a payment went | Client call to treasury support or relationship manager | Report to Payments Operations and the Cyber Defense Center **within 15 minutes**; start the recall at once (section 3, step 1) |
| Callback reaches the client, who denies the request | Callback team | Do not send; report within 15 minutes; tell the client its email may be compromised |
| New beneficiary added and paid within 24 hours, or several new beneficiaries at one client in a day | Fraud scoring; daily beneficiary report (rule from POAM-006) | Hold the payment; callback to the number on file |
| Inbox rule that hides or forwards client replies, or a sign-in from an unfamiliar token or location on a bank mailbox | SIEM identity alerts; email security | Revoke sessions; disable the rule; open a case |
| Clients report emails from a bank employee asking them to "re-validate" treasury access or change payment details | Client calls; phishing reports | Treat as a bank-side compromise; declare severity 1 |
| Beneficiary bank reports a suspicious incoming wire from the bank | Beneficiary bank fraud desk | Payments Operations opens the incident |
| Look-alike domain of the bank or a client registered | Brand monitoring (SI-8) | Block; takedown; watch for use |

**Declare a BEC incident when** a payment was sent, or was about to be sent, on instructions the client did not give, or client or bank credentials are confirmed to be in an attacker's hands. **Severity 1** when a bank system (mailbox, treasury administration, payments hub) is compromised, more than one client is affected, or losses exceed $1 million.

**Record four times, separately:**
1. **Initial detection** (SAR clock, 12 CFR 21.11(d)): when the bank first learned of facts that may be a basis for a SAR.
2. **Notification incident determination** (53.3 and 225.302 clocks): recorded for every severity 1 and 2 incident, whether the answer is yes or no (POL-03 4.4; POAM-011).
3. **Breach determination** (state law clocks; Florida: determination of the breach or reason to believe a breach occurred).
4. **Materiality determination** (SEC clock): recorded later by the disclosure committee (section 6).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Call each beneficiary bank's wire or fraud desk, request a recall and a freeze, follow up in writing, and send the recall message through Federal Reserve payment services where available | Head of Payments Operations | Recall requests acknowledged; reference numbers logged |
| 2. Report to the FBI through IC3 with wire details (amount, date, beneficiary bank, account) | BSA/AML Officer | IC3 complaint numbers logged |
| 3. Suspend the affected clients' treasury users; cancel pending wires and ACH files; block the fraudulent beneficiary templates | Head of Treasury Management | Users suspended; items cancelled |
| 4. If a bank mailbox is involved: revoke all sessions and tokens, reset credentials, remove inbox rules and forwarding, and search all mailboxes for the same rules and senders | Director of Cyber Defense; Director of Identity and Access Management | Sessions revoked; search results logged |
| 5. Decide whether to suspend new beneficiary additions, or all wire initiation, in the treasury channel until the scope is known; record the start time (it feeds the 53.3 determination) | Head of Treasury Management with the CISO | Decision and time logged |
| 6. Call affected clients at the phone number on file (never one from an email); tell them to secure their email and that emailed instructions are refused until further notice | Relationship managers with treasury support | Calls logged |
| 7. Notify the bond and cyber insurance carriers | Chief Financial Officer | Claim numbers issued |
| 8. Open the incident log, linked to the BSA case number, and start the timeline and evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Initial access.** Bank mailbox (phishing, token theft), client mailbox, stolen treasury credentials, or insider. Pull sign-in logs, token issuance, and mailbox audit logs for the bank staff involved; export treasury platform audit trails (sign-ins, devices, IP addresses, beneficiary and limit changes) for every affected client.
2. **Scope across clients.** Search for the same beneficiary accounts, IP addresses, devices, sender domains, and inbox rules across all treasury clients, the legacy commercial platform, and digital banking. **Related occurrences are one incident for the materiality assessment** (17 CFR 229.106(a) defines a cybersecurity incident to include a series of related unauthorized occurrences).
3. **Controls that failed.** Was the callback done? Was the beneficiary confirmed out of band? Did the fraud rules fire? Record each, because it drives the funds-transfer liability analysis and the refund decision (section 6).
4. **Customer information accessed.** List what the attacker could read: client emails and attachments in the bank mailbox (account numbers, loan documents, owners' personal information), and what the treasury sessions showed. A user name and password that allow access to an account are sensitive customer information under Supplement A.
5. **Business impact.** Losses sent, amounts recalled, the duration of any treasury channel suspension, and the number of clients affected. Use P05 values (BP-09: about $5.2 million per 24 hours of treasury outage; BP-01: about $6.8 million per 24 hours of wire outage).
6. **Evidence.** Preserve mailbox exports, audit trails, recall correspondence, and call recordings with a chain-of-custody log; SAR supporting documents are kept 5 years (12 CFR 21.11(g)).

## 5. Containment and eradication (RS.MI)
1. Keep affected client users suspended until each client confirms its email is clean and new credentials are issued out of band; require phishing-resistant MFA for the client administrator before re-enabling.
2. Delete fraudulent beneficiaries and reset limits to agreed levels; flag the clients so emailed instructions are refused.
3. Require out-of-band confirmation of every new beneficiary for all treasury clients for 30 days (an interim form of POAM-007), and lower the fraud rule threshold for beneficiary-plus-wire patterns.
4. For bank mailboxes: confirm no persistence (app consents, forwarding, delegated access); block attacker infrastructure and look-alike domains at the email gateway; give IP addresses to the treasury platform vendor.
5. If the legacy commercial platform is involved, apply the callback-for-every-beneficiary control there too and prioritize those clients for migration (POAM-004).
6. Send a same-day alert to client service, branch, and wire staff with the red flags seen.

## 6. Reporting decisions (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each notice before it goes out.

**Notification incident determination (12 CFR 53.2(b)(7); 53.3; 225.302).** The CISO and the incident commander answer, and record with date and time:
- Has the incident materially disrupted or degraded, or is it reasonably likely to, the bank's ability to serve a **material portion of its customers**? A suspension of wire initiation for all treasury clients longer than the BP-09 MTD (4 hours) is treated as yes.
- Has it affected a **business line whose failure would cause a material loss** of revenue, profit, or franchise value (for example, treasury management services)?
- Could it threaten U.S. financial stability? (Not expected for this incident type.)

A fraud against one client through the client's own email is usually **not** a notification incident. A bank-side compromise that forces a channel-wide suspension may be. Record the answer either way, and **reassess whenever the facts change** (for example, when a suspension is extended). If yes, the OCC must receive notice within 36 hours of the determination, and the Federal Reserve too for the parent.

**Supplement A regulator and customer notice.** Separate from Part 53: notify the OCC as soon as possible when the bank becomes aware of unauthorized access to sensitive customer information, and notify customers as soon as possible when misuse has occurred or is reasonably possible.

**Customer liability.** If the bank did not follow the security procedure agreed in the treasury agreement (for example, a required callback), the payment order may not be effective as the client's order, and the bank would have to refund it with interest (Florida worked example: Fla. Stat. 670.202 and 670.204). Counsel decides. Do not tell a client the loss is theirs before counsel has reviewed it.

**SAR confidentiality.** Staff never mention a SAR to clients, media, or investors (12 CFR 21.11(k)).

## 7. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 to 6. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity 1 incident within 24 hours of declaration (POL-03 4.6) | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 7.4 | **Related occurrences.** The committee lists every occurrence linked by actor, infrastructure, or method (other clients, the legacy platform, earlier BEC cases) and assesses them together | CISO; General Counsel | Related-occurrence list in the minutes |
| 7.5 | Committee reviews the materiality worksheet (below) with facts from sections 4 to 6 | Committee | Worksheet completed |
| 7.6 | **Materiality determination** recorded with date, time, and reasoning, whether material or not yet material. If not yet material, set the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 7.7 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. No technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.8 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (substantial risk to national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 7.9 | Align client, media, and investor messages with any filing, and never reveal a SAR; brief the audit committee and board risk committee chairs | Communications; Investor Relations; General Counsel | Messages approved |
| 7.10 | Keep reassessing as facts change; carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Losses sent and recalled; refunds counsel expects under the treasury agreements; response and notification costs; insurance recovery and retentions; any channel outage cost from P05 values. Compared with, for example, pre-tax income (about $1.45 billion) and quarterly earnings expectations |
| Operational | Channels suspended and for how long; number of clients affected; whether bank systems were compromised |
| Data | Number of individuals and states; data types (account numbers, credentials, Social Security numbers) |
| Legal and regulatory | Notification incident determination; OCC or CFPB supervisory interest; client litigation; refund liability |
| Reputation and strategy | Media coverage; commercial client attrition; effect on treasury growth plans |
| Related occurrences | Whether this is part of a series of related unauthorized occurrences that together change the answer |

## 8. Recovery (RC.RP, RC.CO)
A BEC incident rarely takes systems down; recovery means restoring trustworthy payment services. If bank systems were compromised or the channel was suspended, restore in BIA priority order (P05 section 7):
1. Identity platform and administrator access (break-glass accounts if needed)
2. Payments hub, sanctions screening, and the callback team's phone lines
3. Treasury platform wire and ACH initiation (with the 30-day interim beneficiary confirmation from section 5)
4. Digital banking payment initiation, if it was suspended
5. Legacy commercial platform, last, with callbacks for every beneficiary

**For each affected client:** new credentials issued out of band; phishing-resistant MFA for administrators; beneficiaries and limits reviewed with the client; a written note of the agreed security procedure; the amount recalled and any refund decision recorded.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-001, R-005, R-016, R-017, R-014, R-015), the POA&M (P07), this runbook, and the materiality playbook.
- Add the case, with names removed, to role-based BEC training (POAM-015).
- Report the incident and management's response in the annual report to the board risk committee (12 CFR 30 App. B III.F) and consider it for the next Item 106 disclosure.
- Retain records, including the determination log and materiality minutes, for at least 7 years (POL-01 4.11).

## 10. Worked example (tabletop script, fictional dates)
| Time | Event | Clock or decision |
|---|---|---|
| Mon 2027-03-08, 14:20 | A commercial client service associate enters credentials on an adversary-in-the-middle phishing page; the attacker steals a session token for the bank mailbox and adds an inbox rule hiding replies from 6 clients | Not yet known |
| Mon 16:00 to Tue 09:30 | From the bank mailbox, the attacker emails the 6 clients a "treasury re-validation" link, harvests 9 client user credentials with one-time passcodes, adds 14 new beneficiaries, and sends 23 wires, all under $100,000, totaling $1.94 million | Out-of-band confirmation not triggered (below $100,000); no beneficiary-plus-wire alert (the gaps in POAM-006 and POAM-007) |
| Tue 2027-03-09, 10:05 | One client calls about a wire it did not send; treasury support reports within 15 minutes | **Initial detection: SAR clock starts (due Thu 2027-04-08)** |
| Tue 10:20 | Recalls started for all 23 wires; IC3 reports filed; mailbox sessions revoked; 9 client users suspended | Severity 1 declared (bank mailbox compromised; 6 clients) |
| Tue 11:10 | Head of Treasury Management and the CISO suspend wire initiation for all treasury clients while the scope is unknown | Suspension start time recorded |
| Tue 12:30 | First 53.3 determination: **not a notification incident** (suspension under 2 hours; one business line partially affected); reasons recorded; reassess at 15:00 | Recorded |
| Tue 15:00 | Forensics cannot yet rule out other compromised mailboxes; suspension will continue | Reassessment scheduled for 16:00 |
| Tue 16:00 | Second determination: **notification incident** (wire initiation unavailable to all 41,000 treasury clients for nearly 5 hours, beyond the 4-hour MTD for BP-09). The parent is also affected | **36-hour clocks start: OCC and Federal Reserve notices due by Thu 2027-03-11 04:00** |
| Tue 16:40 | Wire initiation restored with out-of-band confirmation of every new beneficiary | Suspension lasted 5.5 hours |
| Tue 17:30 | CISO briefs the General Counsel; blackout issued | Within 24 hours of declaration |
| Tue 19:30 | OCC and Federal Reserve notified by email and telephone; OCC also told of unauthorized access to sensitive customer information (Supplement A) | Both 36-hour notices met |
| Wed 2027-03-10, 09:00 | Disclosure committee convenes; related-occurrence search finds 2 earlier BEC cases with the same beneficiary bank (February 2027, $0.31 million) | Related occurrences assessed together |
| Thu 2027-03-11, 15:00 | **Materiality determination: not material at this time.** Facts: $2.25 million sent across related occurrences, $1.23 million recalled; refund exposure under review; no evidence of other compromised mailboxes; 5.5-hour channel suspension. Next review Tue 2027-03-16 or on new facts | If it had been material, the Form 8-K would be due Wed 2027-03-17 (4 business days: March 12, 15, 16, 17) |
| Fri 2027-03-19 | Forensics confirms the attacker opened attachments in the mailbox holding personal information of 412 business owners and guarantors (names with Social Security numbers), 260 of them Florida residents | **Breach determination: Florida individual notices due Sun 2027-04-18** (Department notice not required: under 500 Floridians); other states per counsel's matrix |
| By Mon 2027-03-29 | Supplement A customer notices sent to the 412 individuals and the 6 clients; copy of the notice provided to the Florida Department of Legal Affairs to use the deemed-compliance path | Well before the Florida 30-day limit |
| By Thu 2027-04-08 | SARs filed; audit committee told promptly after filing | 12 CFR 21.11(d), (h) |

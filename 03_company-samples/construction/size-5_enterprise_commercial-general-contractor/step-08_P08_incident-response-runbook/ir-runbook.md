# Incident Response Runbook: Business Email Compromise Redirecting Progress Payments

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded commercial and institutional building general contractor; about 300 projects in 8 states) |
| Tier / Vertical | Enterprise / Construction |
| Incident type | Business email compromise (BEC) that redirects progress payments, with the SEC materiality assessment (including related occurrences), a federal EFT variant, a CUI check, and a multi-state breach notification workflow when a compromised mailbox holds personal information |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 DoD Cyber Incident Reporting (DIBNet) Procedure; POL-01 4.13 and PRC-01.5 payee verification |
| Runbook owner | Director of Security Operations (incident commander), with the Vice President, Treasury for payment response (section 3) and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Technical tabletop 2026-02-24 (SOC, Treasury, IT; **the disclosure committee and AQ-1 did not take part**). Next: full tabletop with the disclosure committee, AQ-1 finance, and a DIBNet drill on 2026-11-19 (POAM-009, POAM-010) |
| Notification matrix | `notification-matrix.csv` (29 obligations: 2 payment response, 8 federal contract and DoD, 4 SEC, 4 generic state, 5 Florida worked example, 4 contractual, plus CIRCIA status and OFAC) |

## Why this incident type
Payment fraud is the company's most frequent loss event. About $700 million a month moves through owner pay apps (about 300 a month, average about $1.33 million) and subcontractor payments (about 10,500 ACH payments a month). In 2026 the company had two events: EV-2026-04, a supplier bank change accepted by email at AQ-1 ($612,000 paid, $455,000 recovered, $157,000 net loss), and EV-2026-06, false remittance instructions sent to an owner from a lookalike domain (caught by call-back, no loss). P01 rates the main paths High (R-001, R-002, R-003) and the disclosure gap High (R-051).

## Scenario variants
Variants can happen together. A single attacker often tries more than one.

| Variant | What happens | Money at risk |
|---|---|---|
| **A. Outbound: an owner pays the attacker** | An adversary-in-the-middle phishing page captures a project manager's session and bypasses push MFA. The attacker reads the mailbox, adds an inbox rule that hides the owner's replies, and just before the pay app window (the 20th to the 25th) sends "updated remittance instructions" from the real mailbox or a lookalike domain | One monthly pay app, typically $0.5 million to $5 million |
| **B. Inbound: the company pays the attacker** | A spoofed or compromised subcontractor or supplier mailbox asks accounts payable to change bank details before the next payment run. Highest risk at AQ-1 until POAM-003 closes, because AQ-1 changes payees in its own ERP | One payment run for that payee, typically $50,000 to $2 million |
| **C. Federal: SAM EFT change** | The attacker gets into the SAM Entity Administrator account and changes the company's EFT information, so a federal progress payment goes elsewhere. Under FAR 52.232-33(e)(2) the loss may fall on the company | One federal progress payment (federal receipts are about $88 million a month) |
| **D. Insider-assisted** | A staff member with vendor master rights helps an outside party, or creates a fictitious vendor (P01 R-004) | Several payments before detection |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Payment response lead | Vice President, Treasury | Director of Payment Operations | Treasury fraud line (number on the printed card) |
| Bank recall | Director of Payment Operations | Treasury manager on duty | Bank fraud desk numbers on the printed card, never from email |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair (if project delivery or billing is disrupted) | Chief Operating Officer | President, Building Group | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Chief Accounting Officer, CISO, Chief Risk Officer, Vice President, Investor Relations, President, Federal Group; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Personal information determinations | General Counsel with outside breach counsel | Chief Compliance Officer | Direct mobile |
| Federal contracts, CUI determination, DIBNet | Director of Government Contracts; Director, CMMC Program Office | Federal project security manager for the job | Direct mobile; medium assurance certificate held by two staff |
| Owner and subcontractor contact | Project executive for the job (a different person if the project manager's mailbox is compromised) | Regional vice president | Numbers from the contract file, not from email |
| AQ-1 contact | AQ-1 controller | Vice President, Integration Management Office | Direct mobile |
| Outside counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | Managed security service provider incident team | Retainer hotline |
| Cyber insurer | Carrier hotline (social engineering sublimit $2.5 million) | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI IC3 (www.ic3.gov) and field office | U.S. Secret Service field office | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker is reading company email and possibly chat. Coordinate on company mobile phones and the out-of-band bridge. Never discuss the response in email threads the attacker may see.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at HQ-1 and every regional office: this runbook, the notification matrix, bank fraud desk numbers, and verified phone numbers for owner AP contacts and the top 100 subcontractors by spend
- [ ] Payee and bank changes verified by Payment Operations with a structured call-back record (POL-01 4.13). **Gap at AQ-1 until POAM-003 closes**
- [ ] Dual approval for all wires and for ACH batches above $250,000; positive pay at all three banks (POL-02 4.3)
- [ ] Phishing-resistant MFA for Treasury, Payment Operations, AP, and executives (done); **project management staff by 2027-03-31 (POAM-017)**
- [ ] SIEM BEC use cases (new inbox rules, external forwarding, impossible travel, token replay, vendor master change after a mailbox anomaly) for all tenants. **AQ-1 tenant gap until POAM-004 closes**
- [ ] DMARC at reject on all company domains; lookalike domain monitoring and takedown service (P01 R-007)
- [ ] Owner remittance letter on every pay app cover sheet: "We will never change our bank details by email. Call the number in your contract before paying a new account."
- [ ] Materiality procedure PRC-03.2 with a payment fraud scenario and related-occurrence rule (**gap until POAM-009 closes, 2026-12-15**); 8-K templates and disclosure committee roster current
- [ ] SAM Entity Administrator accounts on security keys; SAM EFT data reconciled to bank records monthly
- [ ] Logs retained 1 year online and 7 years archived (AU-11); SYS-01 download events in the SIEM (**gap until POAM-018 closes**)
- [ ] Counsel's state breach law matrix updated in the last 12 months (P01 R-053)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Owner or subcontractor asks about a bank change the company did not make | Phone call; owner AP; project team | Declare immediately. Ask the caller not to pay any new account and to call its bank if it already paid |
| Expected owner payment not received within 2 business days of its due date | Treasury cash application report | Call the owner's AP at the number on file; confirm where the payment was sent |
| Subcontractor says "we never received payment" | Subcontractor call; AP inquiry log | Check the vendor master change log; declare if bank details changed in the last 90 days |
| SIEM alert: new inbox rule, external forwarding, token replay, or risky sign-in on a project manager, AP, or Treasury account | SOC | Triage within 15 minutes; revoke sessions; declare if unexplained |
| Payee bank change requested by email, especially near a payment run | Payment Operations call-back | Do not change; call the payee at the number on file; report to the SOC (POL-05 4.4) |
| Lookalike domain registered or used in owner correspondence | Domain monitoring; owner report | Declare if used; start takedown |
| SAM notice of a registration change the company did not make | SAM email to the Entity Administrator | Declare (variant C) |
| Report from AQ-1 staff or AQ-1 finance | AQ-1 controller; SOC hotline | Treat as severity 2 until scoped; AQ-1 payment files held (POAM-010) |

**Declare a BEC incident when** a payment instruction is shown to be false, a mailbox or session shows unexplained rules or sign-ins, or money is missing. Any confirmed diversion of $250,000 or more, any federal payment, or any event involving personal information or CUI is **severity 1**.

**Record three times, separately:**
1. **Discovery time:** when any workforce member first knew of the incident. Starts the DFARS 252.204-7012(c) 72-hour clock if CUI turns out to be affected, and many state breach clocks.
2. **Personal information determination time:** when the company determines, or has reason to believe, that personal information was accessed. Starts the Florida 30-day clocks (Fla. Stat. 501.171(3)-(4)).
3. **Materiality determination time:** recorded later by the disclosure committee (section 6). Starts the 4-business-day Form 8-K clock.

## 3. First hour: stop the money (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Request a bank recall** of every payment that may have been diverted (IC3: "time is of the essence"). For variant A, the project executive asks the owner to call its own bank now, and Treasury calls the receiving bank's fraud desk | Director of Payment Operations; project executive with the owner | Recall reference numbers recorded |
| 2. Freeze bank-detail changes in the ERP vendor master and the AQ-1 ERP; hold unreleased ACH batches and AQ-1 payment files | Director of Payment Operations | Freeze confirmed in both ERPs |
| 3. Revoke all sessions for the affected accounts; reset passwords; remove attacker MFA methods and OAuth grants; disable the account if in doubt | SOC; identity team | Sign-in logs show no new sessions |
| 4. Export evidence before it rolls off: identity sign-ins, mailbox audit logs, inbox rules, sent items, message trace, SYS-01 activity, vendor master change logs, payment hub approvals | SOC | Exports saved to the evidence register with hashes |
| 5. Notify the insurer's hotline; the General Counsel engages outside counsel, who retains forensics under privilege | Vice President, Treasury; General Counsel | Claim number; engagement letters |
| 6. File the IC3 complaint the same day (POL-03 4.4) | Director of Security Operations | IC3 complaint number |
| 7. Brief the CISO; for severity 1, the CISO briefs the General Counsel within 24 hours (POL-03 4.5) | Incident commander | Brief logged |
| 8. Start the incident log (timeline, decisions, who, when) | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Initial access.** Find the phishing message or credential source. Look for an adversary-in-the-middle sign-in: a new session from an unfamiliar location minutes after a successful push approval.
2. **Persistence and spread.** Inbox and forwarding rules, OAuth app consents, new MFA methods, mailbox delegates, and the same actor's sign-ins to SYS-01, the ERP, the payment hub, SAM, and other mailboxes. For AQ-1, collect tenant and ERP logs locally while POAM-004 is open.
3. **CUI determination (required for every incident, POL-03 4.7).** Did the mailbox, SYS-01 folders, or files the attacker reached hold CUI or other covered defense information? If yes, the DFARS 252.204-7012(c) review and 72-hour DIBNet report apply (PRC-03.4), with image preservation for 90 days from the report (252.204-7012(e)). FCI exposure alone has no notice duty, but it is recorded for the Level 1 scope (notification matrix, "CMMC status currency").
4. **Personal information determination.** List what the attacker could read: certified payrolls and HR files with Social Security numbers, bank details of employees, and the account holder's own email address and password (personal information under Fla. Stat. 501.171(1)(g)). This drives section 7.
5. **Client data.** BTS client building layouts, camera locations, or credentials in the mailbox trigger client notice and immediate credential rotation (notification matrix, "BTS client notice").
6. **Money trail.** For each payment: amount, date, receiving bank and account, recall status, IC3 number, and whether the payment was federal (variant C) or meant for a subcontractor on a federal job (FAR 52.232-27).
7. **Other victims.** Did the attacker email other owners or subcontractors from the mailbox? Use sent items and message trace; call each one.
8. **Business impact for section 6.** Finance estimates the loss, recovery, insurance (sublimit $2.5 million less retention), and costs, using P05 values: for example, a pay app window disruption defers about $13.2 million of receipts per day (BP-02).

## 5. Containment and eradication (RS.MI)
1. Remove malicious rules, forwarding, OAuth grants, and delegates; re-register MFA with a security key.
2. Block the attacker's sign-in sources and lookalike domains at the mail gateway; start takedown.
3. Reset credentials for every system the user reached with single sign-on. For variant C, reset the SAM Entity Administrator account and compare SAM EFT data with bank records.
4. Hunt across all project manager, AP, Treasury, and AQ-1 mailboxes for the same rules and sign-in patterns.
5. Keep the vendor-master freeze until every bank change of the last 90 days is re-verified by call-back with a structured record.
6. For variant D, preserve evidence and involve the General Counsel and Chief Human Resources Officer before any interview.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5 and does not wait for the investigation to finish. The materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, using quantitative and qualitative factors. A payment fraud loss is a cybersecurity incident when it results from unauthorized access to company information systems (for example, a compromised mailbox), and 17 CFR 229.106(a) defines a cybersecurity incident to include "a series of related unauthorized occurrences".

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident and every payment fraud event within 24 hours (POL-03 4.5) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** for committee members, responders with knowledge, and executives (POL-05 4.9) | General Counsel | Blackout notice sent |
| 6.4 | **Related-occurrence review:** list every payment fraud and BEC event in the last 24 months (from the SOC case register, including AQ-1 events such as EV-2026-04 and EV-2026-06), and decide whether they share an actor, technique, or weakness. Assess them together as well as alone | CISO; Chief Risk Officer | Related-occurrence memo |
| 6.5 | Committee completes the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.6 | **Materiality determination** recorded with date, time, and reasoning, whether material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.7 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident and its material impact or reasonably likely material impact, including on financial condition and results of operations. Leave out technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.8 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.9 | Align owner, subcontractor, employee, media, and investor communications with the filing; brief the audit committee and board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.10 | Keep reassessing as facts change (for example, a failed recall or a second related event); counsel decides whether an amended filing is needed (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Gross and net loss after recall and insurance; trend of related losses; forensic, legal, and notification costs; effect on liquidity, bonding capacity, and covenants (gross margin is about $336 million a year) |
| Pattern | Related occurrences (step 6.4): repeated events through the same weakness, such as AQ-1 payee changes, may be material together when none is alone |
| Operational | Pay app window disrupted; payments to subcontractors delayed; projects affected |
| Data | Personal information exposed (number of people, states, Social Security numbers); CUI affected and DIBNet report filed |
| Legal, contract, and regulatory | Federal contract consequences (CMMC status currency, DoD inquiries); owner or surety claims; state attorney general inquiries; litigation |
| Reputation and strategy | Owner and subcontractor trust; media coverage; effect on federal and institutional awards and on integration of acquisitions |

**Worked example of the clocks (fictional dates):** an owner calls on Tuesday 2027-03-23 at 10:00 asking about "our new bank"; it paid a $2.4 million pay app to an attacker account on Friday 2027-03-19 (discovery: 2027-03-23). Treasury requests a recall at 10:40. Forensics finds the project manager's mailbox was compromised and held certified payroll files with Social Security numbers for 1,850 workers in four states, 1,210 of them Florida residents. The disclosure committee convenes on Thursday 2027-03-25 and reviews this event with EV-2026-04 and EV-2026-06 as possible related occurrences.
- **If the committee determines materiality on Tuesday 2027-03-30 at 15:00,** the Form 8-K is due by **Monday 2027-04-05** (4 business days: March 31, April 1, April 2, and April 5).
- **Counsel determines on Friday 2027-04-02** that personal information was accessed. Florida's 30-day clocks run from that determination: notices to 1,210 Florida residents and to the Department of Legal Affairs (500 or more) no later than 2027-05-02, a Sunday, so the plan targets Friday 2027-04-30. Consumer reporting agencies are notified without unreasonable delay because more than 1,000 people are notified at once. The other three states follow counsel's matrix; any state with a shorter clock sets the plan.
- **Counsel must also decide** whether a "reason to believe a breach occurred" arose earlier (for example, when the SOC found the inbox rule on 2027-03-23), which would move the Florida dates forward.
- **If CUI had been in the mailbox,** the DIBNet report would have been due by Friday 2027-03-26 at 10:00 (72 hours after discovery), before any of the other deadlines.

## 7. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Personal information determination, documented with the date and the reasoning (POL-03 4.8). Do not wait for funds recovery to finish | General Counsel | Signed determination |
| 7.2 | Build the affected population from forensic results: each person, data elements, and **state of residence** (from HR and payroll records). Separate employees, subcontractor workers whose data the company holds (certified payroll attachments), and owner or client contacts | Chief Human Resources Officer; data team | Affected-individual file with state counts |
| 7.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules, and law enforcement delay provisions. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.4 | **Florida worked example:** individual notice no later than 30 days after determination; Department of Legal Affairs notice no later than 30 days if 500 or more Floridians (the 15-day good-cause extension applies only to the notice to individuals); consumer reporting agencies if more than 1,000 are notified at once; a written no-harm determination only with counsel's agreement, kept 5 years and given to the Department within 30 days | General Counsel | Florida filings |
| 7.5 | **Plan to the shortest clock** across DoD (if CUI), the SEC, and every state. Publish one master calendar | General Counsel | Master calendar |
| 7.6 | Honor any written law enforcement delay request (Fla. Stat. 501.171(4)(b) and matching state provisions); document it | General Counsel | Delay record |
| 7.7 | Engage the mail vendor, call center, and credit monitoring provider | Chief Human Resources Officer | Vendors active |
| 7.8 | Notify contract parties: owners whose payment channel was compromised, BTS clients whose facility details were exposed, sureties if working capital is affected, and the insurer | Contract owners | Contract notices logged |
| 7.9 | Track inbound vendor notices (state third-party agent laws such as Fla. Stat. 501.171(6)) if the incident started at the payroll or HR vendor | Director of Third-Party Risk Management | Vendor notices logged |

**Federal variant (C) and federal subcontractors.** Correct SAM, and tell the Contracting Officer and paying office for each affected contract (FAR 52.232-33). If the diverted payment was meant for a subcontractor on a federal job, pay the real subcontractor within 7 days of receiving the Government's payment after call-back verification (FAR 52.232-27(c)); do not hold real subcontractors hostage to the recovery argument.

**Paying twice.** In variant A the owner may still owe the company; in variant B the subcontractor must still be paid. Counsel decides who bears the loss. The company keeps paying real subcontractors while that is argued, because liens and work stoppages cost more.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7). For BEC, "restored" means "verified":
1. Identity platform: affected accounts re-secured with security keys; break-glass accounts confirmed
2. Out-of-band contact list re-verified (owner AP contacts, subcontractor payment contacts)
3. Email: mailboxes cleaned; alerts confirmed for every affected tenant, including AQ-1
4. Treasury and payment hub: dual approval and positive pay confirmed; bank 3 interim controls (EXC-2026-022) confirmed
5. ERP vendor master and AQ-1 ERP: every bank change of the last 90 days re-verified before the freeze is lifted
6. SAM: EFT information matches the bank; Entity Administrator on a security key
7. Pay app cycle resumes with a remittance confirmation call to each affected owner for the next two cycles
8. SYS-01: external users on affected projects re-certified

**Tell people when it is safe (RC.CO):** written confirmation of the real bank details to affected owners and subcontractors, and a short briefing to staff on what to watch for.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-001, R-002, R-003, R-005, R-007, R-008, R-051), the POA&M (P07), training content (POAM-011), PRC-03.2, and this runbook.
- Add the event to the related-occurrence register used in step 6.4.
- Confirm every CMMC Level 1 and Level 2 requirement is still met before the next award or affirmation (notification matrix, "CMMC status currency").
- Disclosure committee reviews the effect on the next Item 106 disclosure.
- Retain all records, including determination minutes, for at least 6 years (POL-01 4.11). Keep any Florida no-harm determination for at least 5 years (501.171(4)(c)).

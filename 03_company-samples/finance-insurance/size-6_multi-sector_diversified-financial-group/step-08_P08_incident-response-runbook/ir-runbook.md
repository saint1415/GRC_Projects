# Incident Response Runbook: Business Email Compromise and Fraudulent Wire Transfer Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Finance and Insurance |
| Incident type | Business email compromise (BEC) that starts with stolen workforce session tokens in shared identity and email (SYS-G1, SYS-G4) and spreads to three divisions: a fraudulent CRE loan funding wire released by the bank, vendor-impersonation emails to client banks, support console access to every platform tenant, and exposed guarantor and client customer data |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; POL-02 4.13 (payment instruction verification); division supplements (P06) |
| Regulatory basis | 12 CFR 30 App. B III.C.1.g and Supplement A; 12 CFR 225 App. F III.C.1.g; 12 CFR 53.3, 53.4, 225.302, 225.303, 304.24; 12 CFR 21.11 and 225.4(f); Form 8-K Item 1.05; state breach laws (Fla. Stat. 501.171 worked example) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-10 by the Group CISO and the Group General Counsel |
| Last tested | BEC playbooks for bank wire operations tested quarterly. **The multi-regulator matrix has not been exercised across divisions** (scenario gap 5); the first cross-division tabletop, using this scenario, is due 2026-12-15 (POAM-006) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Amounts and counts are illustrative. Day 0 is a Tuesday.
- **Day -9, entry:** an adversary-in-the-middle phishing page ("updated closing statement") steals the session token of a CRE Lending closer. Single sign-on sessions last 12 hours and are not device-bound (P07 AC-12; POAM-003). The attacker adds an inbox rule that hides messages containing "wire", "payoff", and "closing", and reads 11 months of mail: closing packages with personal financial statements of about **1,860 guarantors in 14 states** (about **610 in Florida**).
- **Day -6, spread:** from the closer's real mailbox the attacker sends a "shared document" lure to 40 internal contacts. A Financial Software client implementation manager falls for it. With that session the attacker (a) reads 2025 core conversion files still in the mailbox, holding names, account numbers, and Social Security numbers of about **31,200 consumers of 2 client banks**, and (b) opens the **support console**, which lets support roles read every tenant's configuration and business user contact list (P07 AC-06; POAM-008).
- **Day -3, client fraud:** from the implementation manager's mailbox, fake "new remittance instructions" go to the accounts payable teams of 23 client banks. 4 of them pay invoices totaling **$1.1 million** to the attacker.
- **Day -1, funding fraud:** the attacker sends CRE Lending's funding team "the borrower's updated disbursement instructions" for a closing the next day, with a phone number in the letter. The funding officer calls that number (not an independently verified one; P03 RE-G06) and an accomplice confirms. At 15:20 CRE Lending's two funding approvers submit and approve a **$14.2 million wire** in the bank tenant of the digital banking platform. The bank's callback for new high-value beneficiaries reaches CRE Lending's designated treasury contact, who confirms. The bank releases the wire.
- **Day 0, discovery:** at 09:05 the title agent reports that the funds never arrived. The closer reports to the group SOC at 09:14.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Wire recall and holds | Head of Commercial Payments Operations | Senior wire operations manager | Wire room direct lines |
| Platform containment | Head of Digital Banking Platform | Financial Software chief technology officer | Platform bridge |
| Bank notification incident determination | Group CISO with the bank chief operations officer | Group Chief Risk Officer | Out-of-band bridge |
| Holding company determination | Group General Counsel with the Group Chief Risk Officer | Group Chief Financial Officer | Out-of-band bridge |
| Client bank notices (53.4, contracts) | Client risk and assurance director | Financial Software division CISO | Division bridge; client contact register |
| Guarantor and customer notices; state law | Group Chief Privacy Officer with outside breach counsel | Division counsel | Out-of-band bridge |
| SARs | Bank BSA/AML Officer; nonbank BSA/AML Officer | Group Chief Compliance Officer | Phone |
| SEC materiality | Disclosure committee (chair: Group Chief Financial Officer) | Group General Counsel | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office and IC3 | CISA (voluntary) | Contacts in the offline incident binder |
| Regulators | OCC supervisory office (bank); Federal Reserve point of contact (holding company) | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read group email and chat. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, the notification matrix, and the client contact register.

## 2. Preparation checks (Identify / Protect)
- [x] Dual control and callbacks to independently verified numbers for bank wire operations (P07 AC-5 satisfied)
- [x] 24x7 SOC with EDR and an email security gateway (SI-3, SI-8)
- [x] Forensic retainer, cyber insurance, and financial institution bond confirmed
- [x] Disclosure committee charter includes cybersecurity materiality
- [ ] Device-bound workforce sessions of 8 hours or less (**gap until POAM-003 closes**)
- [ ] Token replay and inbox-rule detection across identity, email, and consoles (**gap until POAM-004 closes**)
- [ ] Tenant-scoped support console access (**gap until POAM-008 closes**)
- [ ] CRE funding only through verified instructions, with trained closers (**gap until POAM-019 closes**)
- [ ] Bank-designated contacts for all 212 client banks and a 4-hour timer (**gap until POAM-005 closes**)
- [ ] Bank and holding company determination criteria that cover affiliate-origin incidents and deliberate suspensions (**gap until POAM-006 closes**)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A payee says funds never arrived, or a customer or affiliate reports a wire it did not intend | Branch, treasury management, CRE closing team, title agent | Report to the SOC **within 15 minutes** (POL-03 4.1); start the wire recall at once |
| Inbox rule hiding payment words; mail forwarding to outside addresses | Mailbox audit (after POAM-004) | Disable the session; review the mailbox |
| The same session token used from new infrastructure or two places | SYS-G1 risk signals; SIEM | Revoke sessions; review all activity of the identity |
| Support console access across many tenants in a short time | Support console logs (after POAM-004) | Suspend the support account; start triage |
| A client bank asks whether a changed remittance instruction is real | Client support; account managers | Treat as a potential BEC; open an incident |

**Severity 1** (group scale, POL-03 4.2): a confirmed fraudulent payment over $1 million, or confirmed attacker access to a shared service or to more than one division. In the scenario, Severity 2 is declared at 09:30 (the wire) and raised to **Severity 1 at 10:45**, when the SOC links the closer's token pattern to the implementation manager's account and the support console.

**Record every clock start in the incident log:**
- initial detection of the fraud (starts SAR clocks): Day 0 09:14;
- the time of any suspension of customer-facing functions (POL-03 4.3);
- the bank's and the holding company's notification incident determinations (each starts a 36-hour clock);
- the Financial Software division's 4-hour determination (starts "as soon as possible" client bank notices);
- each entity's breach determination under state law (starts the Florida 30-day clocks and the 10-day third-party agent clock);
- the disclosure committee's materiality determination (starts the 4-business-day Form 8-K clock, if material).

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Call the beneficiary bank's wire and fraud desk; request a recall and freeze; follow up in writing | Head of Commercial Payments Operations | Recall acknowledged (Day 0 09:40) |
| 2. Report to the FBI through IC3 with the wire details | Bank BSA/AML Officer | IC3 number logged (Day 0 10:05) |
| 3. Revoke all sessions and reset credentials for the closer and the implementation manager; remove inbox rules; block the attacker's domains and addresses | Group identity director; SOC | Sessions revoked; rules removed |
| 4. Suspend the implementation manager's and all non-essential support console access; export support console logs | Head of Digital Banking Platform | Support access limited to 12 named on-call staff |
| 5. **Decision:** suspend business wire and ACH initiation on the platform for all tenants until business payment templates and limits are confirmed unchanged. Record the decision time (Day 0 11:15). Consumer banking and branch and phone wires continue | Incident commander with the Group CISO (POL-03 4.3) | Suspension live; decision logged |
| 6. Warn the 23 client banks that received fake remittance emails, by phone to known contacts | Client risk and assurance director | All 23 reached |
| 7. Call the insurers; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim numbers issued |
| 8. Escalate to the disclosure committee within 24 hours of Severity 1 (POL-03 4.7) | Group CISO | Committee convened Day 0 16:00 |
| 9. Tell each division's operations what is and is not affected | Division liaisons | Confirmed |

## 5. Analysis (RS.AN)
1. **Identity path.** From SYS-G1 and SYS-G4 logs, list every session the attacker used, every mailbox rule, every sent message, and every application reached. Identity logs are kept 1 year searchable (AU-11), so the full 9-day window is available.
2. **Payments.** Confirm no bank template, beneficiary, or limit was changed in any tenant, using the tenant audit logs and the support console export. In the scenario, no changes were found; business payments resume at 16:45 with forced re-authentication and step-up for all business users (**5.5 hours**).
3. **Data exposed, by entity:**
   - *CRE Lending:* guarantor personal financial statements (names, Social Security numbers, account numbers): about 1,860 individuals in 14 states. They are commercial guarantors, not GLBA "consumers" (12 CFR 1016.3(e)(1)), so state breach laws, not Supplement A, drive their notices.
   - *Financial Software:* 2025 conversion files with about 31,200 consumers of 2 client banks. This is the client banks' customer information, held by the division as their service provider. The client banks decide their own OCC or FDIC and customer notices; the division gives them facts, counts by state, and a template.
   - *All tenants:* tenant configurations and business user contact lists (names, emails, phone numbers, user IDs) were readable. No passwords, balances, or account numbers. Treat as a phishing risk for every client and for the bank's business users.
4. **Losses:** $14.2 million wire (recall froze $9.8 million; **$4.4 million unrecovered**); $1.1 million paid by 4 client banks on fake invoices.
5. **Root cause:** a replayable 12-hour session token, the support console's all-tenant reach, funding on emailed instructions with callbacks to numbers in the package, and conversion files kept in email. Feed these to P01 GR-01, GR-02, GR-04, and GR-19.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (38 rows).** Counsel approves every notice. The matrix has four layers:
1. **The bank and the holding company (their own regulators).** Two separate determinations, because they are two banking organizations with two regulators.
2. **The Financial Software division as bank service provider** to 310 client institutions and to the bank itself.
3. **Each entity's data duties:** CRE Lending to guarantors under state law; the division to the 2 client banks whose customers' data was exposed (contract and state third-party agent rules).
4. **Group duties:** SARs, the disclosure committee, insurers, and law enforcement.

### 6.1 Notification incident determinations (12 CFR 53.2(b)(7); 225.301(b)(7))
The determination officials answer, and record with the date and time:
- Has the incident materially disrupted or degraded, or is it reasonably likely to, the ability to deliver banking products or services to a **material portion of customers**? (Here: about 310,000 bank business users could not initiate wires or ACH digitally for 5.5 hours on a business day.)
- Has it affected a **business line** whose failure would cause material loss of revenue, profit, or franchise value? (For the holding company: the platform service for 310 client institutions was suspended.)
- Did it start in an affiliate, or was the disruption a **deliberate containment decision**? Neither changes the test. The rule asks about effect, not cause.

**Scenario decisions:** the bank determined a notification incident at **Day 0 13:40**; the OCC received notice by phone and email at 17:30 (well within 36 hours). The holding company determined separately at **Day 0 14:30**; the Federal Reserve received notice at 18:00.

### 6.2 Bank service provider determination (12 CFR 53.4; 225.303; 304.24)
At the 4-hour mark of the suspension (**Day 0 15:15**) the client risk and assurance director determined that covered services had been materially disrupted for 4 or more hours for every client bank. Notices went out from 15:30: to the designated contact for 151 client banks, and to the CEO and CIO for the other 61 (verified by phone, because 20% of those fallback contacts were stale). The bank, as a tenant, received the same notice. Credit union clients received the same message under their contracts, so they could meet their own 72-hour NCUA reporting.

### 6.3 Timeline
| When (Day 0 = discovery) | Action | Owner |
|---|---|---|
| Day 0, 09:14 | Initial detection recorded (SAR clocks start) | Bank BSA/AML Officer |
| Day 0, 09:40 to 10:05 | Wire recall request; IC3 report; insurers notified | Payments operations; BSA/AML Officer; Group Chief Risk Officer |
| Day 0, 11:15 | Business payment initiation suspended for all tenants (decision time recorded) | Incident commander with the Group CISO |
| Day 0, 13:40 | Bank notification incident determination | Group CISO with the bank chief operations officer |
| Day 0, 14:30 | Holding company notification incident determination | Group General Counsel with the Group Chief Risk Officer |
| Day 0, 15:15 | 4-hour mark: bank service provider determination; client notices begin 15:30 | Client risk and assurance director |
| Day 0, 16:00 | Disclosure committee convened | Group Chief Financial Officer |
| Day 0, 16:45 | Business payments resume with step-up for all business users | Head of Digital Banking Platform |
| Day 0, 17:30 and 18:00 | OCC and Federal Reserve notices (36-hour deadlines were Day 2 01:40 and 02:30) | Group General Counsel |
| Day 1 | Contract notices: 88 clients with 24-hour terms already covered by the Day 0 notice; incident details follow within 72 hours for all clients | Client risk and assurance director |
| Day 1 | Notice to the 2 client banks whose customers' data was exposed (contract terms of 24 and 72 hours) | Client risk and assurance director |
| Day 3 | Materiality determination (not material; section 6.4) | Disclosure committee |
| Within 10 days of the division's determination | Florida third-party agent notice to the 2 client banks (Fla. Stat. 501.171(6)); apply other states' agent rules the same way | Group General Counsel |
| Within 30 days of CRE Lending's determination | Florida individual notices to about 610 guarantors (501.171(4)); Department of Legal Affairs notice (500 or more Floridians, 501.171(3)); consumer reporting agencies if more than 1,000 at a single time (counsel decides); other states' laws for the rest | Group Chief Privacy Officer |
| No later than 30 calendar days after initial detection | Bank SAR (12 CFR 21.11(d)); nonbank SARs under 225.4(f); bank board told of the filing (21.11(h)) | BSA/AML Officers |

**Plan to the shortest clock.** In this scenario the order is: wire recall (minutes), the 4-hour client determination, the 36-hour OCC and Federal Reserve notices, 24-hour contract notices, the 10-day Florida agent notice, the 30-day SAR and Florida notices. Make each determination early and write it down: the rules start the clocks at determination, and a late determination is itself a finding.

### 6.4 SEC materiality (Form 8-K Item 1.05)
The committee weighed:
- **Quantitative:** $4.4 million unrecovered, $1.1 million client losses (the division is considering credits), and about $3 million in response and notice costs, against about $18 billion in revenue.
- **Qualitative:** notices to the OCC and the Federal Reserve; notices to 310 client institutions, which is the division's franchise; phishing risk to business users across all tenants; possible client churn; regulator follow-up.

**Decision on Day 3: not material**, documented with reasons, and to be revisited if facts change (for example, client terminations, further data exposure found by forensics, or regulatory action). The 4-business-day clock would start only at a determination of materiality. The incident will be considered for the next Reg S-K Item 106 description.

### 6.5 Loss allocation and communications
- **The funding wire.** CRE Lending's own authorized users approved the payment, and the bank followed the agreed security procedure (MFA, dual approval, callback to the customer's designated contact). Under UCC Article 4A as enacted in Florida (Fla. Stat. 670.202, worked example), the order is likely effective as CRE Lending's. The loss stays in the group either way; counsel records the analysis because the same facts with an outside customer would decide who bears the loss.
- **Staff** do not discuss the case outside the response team and never mention a SAR (12 CFR 21.11(k)).
- **Client institutions** receive one consistent message from the division, approved by counsel, with a phishing warning for their business users.

## 7. Recovery (RC.RP, RC.CO)
A BEC rarely destroys systems. Recovery means restoring trusted payment service and closing the attacker's paths. Restore in BIA order (P05):
1. Identity: revoke sessions group-wide for the affected populations; bind sessions to devices for Financial Software and CRE Lending first (accelerates POAM-003)
2. Email: remove rules; purge conversion files and closing packages from mailboxes (accelerates POAM-023)
3. Platform business payments: re-enabled with forced re-authentication and step-up (done Day 0 16:45); support console limited to named on-call staff until POAM-008 closes
4. CRE funding: all fundings go through the bank's verified-instruction service with trained approvers before any new closing (accelerates POAM-019)
5. Client communications: status page and direct notices when service and support return to normal (RC.CO)

## 8. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.12).
- Update P01 (GR-01, GR-02, GR-03, GR-04, GR-19, RR-001, FS-001, FS-006), the POA&M (POAM-003 to POAM-006, POAM-008, POAM-019, POAM-023), the notification matrix, and this runbook.
- Check the event against the bank's risk appetite (App. D II.H): $4.4 million does not breach the $25 million annual payment-instruction fraud limit; recorded.
- Report the incident and responses in the annual reports to both boards (App. B III.F; App. F III.F).
- Retain incident records for at least 5 years (POL-01 4.12); SAR supporting documents as 12 CFR 21.11 requires.

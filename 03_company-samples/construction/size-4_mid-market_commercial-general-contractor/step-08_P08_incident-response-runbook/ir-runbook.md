# Incident Response Runbook: Business Email Compromise Redirecting Progress Payments

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial and institutional building general contractor) |
| Tier / Vertical | Mid-Market / Construction |
| Incident type | Business email compromise (BEC) that redirects progress payments, owner payments, or subcontractor payments |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy (4.2, 4.4, 4.7, 4.10, 4.11); POL-01 4.8 and 4.9 payment and remittance changes; STD-04 Payment verification |
| Companion documents | `ir-runbook-cui-incident.md` (compromise of covered defense information); `notification-matrix.csv`; BIA (P05); incident binder |
| Runbook owner | Security Manager (incident commander); Chief Financial Officer (payment response lead) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet as a BEC exercise. Payment-fraud tabletop with the bank and panel counsel scheduled 2026-12-09 (POAM-023). The 2025 tabletop covered ransomware |

## Scenario this runbook is built for
Four variants share one playbook. They often happen together, because the attacker who controls one mailbox reads every thread it touches.

| Variant | What happens | Money at risk |
|---|---|---|
| **A. Outbound: an owner pays the attacker** | An adversary-in-the-middle phishing page captures a Project Manager's password and session token, bypassing push MFA (shown possible in P07). The attacker reads the mailbox and SYS-01 for weeks, adds an inbox rule that hides replies from the owner's accounts payable, and, just before billing week, sends "updated remittance instructions" from the real mailbox or a lookalike domain. | One monthly pay app; average about $1.2 million (P01 R-001) |
| **B. Inbound: the company pays the attacker** | A spoofed or compromised subcontractor mailbox asks accounts payable to change bank details "before Friday's ACH run". The change is pushed through with an "urgent" override (2 of 25 sampled changes, P07 AC-5). | One subcontractor progress payment, $200,000 to $1.5 million (P01 R-002) |
| **C. Federal: SAM EFT change** | The attacker reaches the SAM Entity Administrator account and changes the company's EFT data, so a federal progress payment goes elsewhere. A fake remittance letter does not work on federal paying offices, because they pay only to the EFT data in SAM (FAR 52.232-33(b)). | One federal progress payment; the loss may fall on the company (FAR 52.232-33(e)(2)) |
| **D. Payroll: direct deposit change** | Phished employees' payroll self-service accounts are used to change direct deposit details (P01 R-026). | One payroll cycle per affected employee |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers so that technical, payment, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, Vice President of Operations, Director of Contracts and Compliance, HR Director; outside breach counsel | Owner and subcontractor communications, who bears a loss, external statements, notices to the surety, lenders, and PE sponsor, resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director, 2 security analysts, MSSP, panel forensic firm (through counsel), project platform and ERP vendor contacts | Containment, investigation, evidence, eradication, recovery |
| **Payment response cell** | Lead: CFO. Controller, accounts payable lead, billing lead, the Project Manager for each affected job (never the compromised one) | Bank recalls, payment freezes, owner and subcontractor call-backs, re-verification of bank details |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on company phones; printed call tree |
| Payment response lead | Chief Financial Officer | Controller | Out-of-band group |
| Bank recall | Controller | Accounts payable lead | Bank fraud desk number on the printed card in the incident binder (never a number from email) |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Legal and privilege | General Counsel | Outside breach counsel (insurer panel) | Out-of-band group; counsel through the carrier hotline |
| Cyber insurer | Carrier breach hotline ($10 million limit; $1 million social engineering sublimit; $250,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Owner contact | Project Executive for the job (a different person if the Project Manager's mailbox is compromised) | Vice President of Operations | Numbers from the prime contract file |
| Subcontractor contact | Project Manager for the job (not the compromised one) | Controller | Numbers from the vendor master as verified before the incident window |
| Federal contacts | Director of Contracts and Compliance | General Counsel | Contracting Officer and paying office numbers in the contract file |
| Board and sponsor | CEO informs the audit committee chair and the PE sponsor's operating partner | COO | Phone |
| Law enforcement | FBI IC3 (www.ic3.gov) and the local FBI field office | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker is reading company email and chat. Coordinate by phone and the pre-provisioned messaging group on company phones. Never discuss the response in an email thread the attacker can see, and never reply to the suspicious message.

**Legal privilege protocol.** General Counsel or outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from conclusions about fault or loss.

## 1. Preparation checks (Identify / Protect)
- [x] Dual approval for all ACH batches and wires in the bank portal; positive pay (SYS-10)
- [x] Incident binder at headquarters and the regional office: this runbook, verified numbers for the bank fraud desk, all 22 owners' accounts payable, the top 50 subcontractors, the MSSP, and the carrier hotline (verified 2026-09-15)
- [x] MSSP alerts on new inbox forwarding rules and risky sign-ins in SYS-04 and SYS-05
- [ ] Call-back rule with no override and evidence fields in the ERP (STD-04). **Gap until POAM-003 closes (2026-10-31)**
- [ ] Phishing-resistant MFA for Project Managers, billing, accounts payable, the Controller, the CFO, and executives. **Gap until POAM-012 closes (2026-12-31)**
- [ ] Remittance-change letter sent to all 22 owners and printed on every pay app cover sheet (POL-01 4.9). **Gap until POAM-023 closes (2026-10-31)**
- [ ] DMARC at reject and lookalike-domain monitoring. **Gap until POAM-023 closes (2026-12-31)**
- [ ] SYS-01 audit logs and SYS-02 vendor-master changes in the SIEM. **Gap until POAM-008 closes (2026-12-31)**
- [ ] Help desk MFA resets only after call-back to a number on file. **Gap until POAM-012 closes (2026-10-31)**
- [x] The CFO knows the carrier's social engineering claim conditions (prompt notice; proof that the verification procedure was followed)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| An owner or subcontractor asks about a bank change the company did not make | Phone call or owner accounts payable | Declare immediately. Ask the caller not to pay any new account and to call their bank if they already did |
| An expected owner payment has not arrived 2 business days after its due date | Controller's daily cash report | Call the owner's accounts payable at the number in the contract file and confirm where it was sent |
| A subcontractor says "we never received payment" | Subcontractor call | Check the vendor-master change log; declare if bank details changed in the last 90 days |
| New inbox rule, external forwarding, OAuth consent, or new MFA method on a payment-role account | MSSP alert from SYS-04 and SYS-05 | MSSP revokes sessions and calls the incident commander within 30 minutes; declare if not explained by the user within 1 hour |
| Sign-in from an unfamiliar network shortly after a successful push approval | SYS-04 risky sign-in alert | Treat as adversary-in-the-middle; declare |
| Staff report clicking a link and entering credentials, or an MFA prompt they did not cause | Staff report (POL-03 4.2) | Revoke sessions and reset now; review the mailbox for rules |
| SAM email about a registration or EFT change the company did not make | SAM notice to the Entity Administrator | Declare (variant C) |
| Several employees report missing pay | HR and payroll | Declare (variant D) |

**Severity 1 (declare immediately):** money has left or is about to leave to an unverified account, or a payment-role mailbox shows attacker rules or sessions.

**Record two times in the incident log** (POL-03 4.3):
- the time the incident was first known to any workforce member;
- later, the time the company determines, or has reason to believe, that personal information was accessed. Florida's 30-day clock runs from that determination (Fla. Stat. 501.171(4)(a)). If CUI is found in the mailbox, the DoD 72-hour clock runs from discovery of that cyber incident (DFARS 252.204-7012(c)(1)(ii)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | **Call the bank fraud desk to request a recall** of any payment that may have been diverted. For variant A, the owner's bank must request it: the Project Executive calls the owner's accounts payable and asks them to call their bank now | Controller (B, D); Project Executive with the CFO (A) | Recall reference number recorded |
| 0-30 min | Freeze all bank-detail changes in the ERP vendor master; hold unreleased ACH batches and wires; stop payroll direct deposit changes (D) | Controller; HR Director | Freeze confirmed in writing by the bank and the ERP administrator |
| 0-30 min | Revoke all sessions for the affected accounts in SYS-04; reset passwords; remove attacker MFA methods, OAuth grants, and delegates; disable the account if still in doubt | MSSP; Security Manager | Sign-in log shows no new sessions |
| 0-60 min | Declare severity 1; open the out-of-band group; start the incident log | Incident commander | Log open |
| 0-60 min | Call the cyber insurer's hotline before engaging any vendor; panel counsel assigned; counsel engages forensics | CFO | Claim number; counsel on the call |
| 0-2 h | Export evidence before it rolls off: SYS-04 sign-ins, mailbox audit log, inbox rules, message trace, sent items, SYS-01 audit log (vendor export), ERP vendor-master change log, bank portal activity (POL-03 4.7) | Security analysts with the MSSP | Exports in the incident folder with hashes |
| 1-2 h | File the IC3 complaint with the payment details (POL-03 4.4) | Security Manager | IC3 complaint number |
| 1-2 h | Convene the CMT; first situation report: money at risk, recall status, affected owners and subcontractors, decisions needed | CMT chair | CMT meeting held |
| 2-4 h | Phone every owner with a pay app in the last 60 days and every subcontractor paid or scheduled in the last 30 days, using numbers on file. Script: "Pay nothing to new bank details. Our details have not changed. Call this number to confirm any instruction" | Project Executives and Project Managers (assigned by the Vice President of Operations) | Call log complete |
| 2-4 h | Variant C: SAM Entity Administrator account secured; EFT data compared with the bank; Contracting Officers and paying offices for FC-1 to FC-4 called | Director of Contracts and Compliance | SAM corrected; calls logged |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner if more than $250,000 is at risk | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Initial access.** Find the phishing message or credential source. An adversary-in-the-middle sign-in shows as a session from an unfamiliar network minutes after a successful push approval.
2. **Persistence.** Look for:
   - inbox, forwarding, and transport rules
   - OAuth app consents and mailbox delegates
   - new MFA methods or help desk resets in the window (P07 found 3 of 10 resets without call-back)
   - the same actor's sign-ins to SYS-01, SYS-02, SYS-03, SAM, and the bank portal
3. **What the attacker could read.** List the mailbox, personal file storage in the productivity suite, chat, and SYS-01 projects the account could reach. **This drives every notification decision:**
   - certified payroll files, I-9 copies, or HR documents with Social Security or driver license numbers (personal information under Fla. Stat. 501.171(1)(g)1.a.). A bank account number counts in Florida only with a code or password that permits access to the account; other states' definitions differ;
   - the account holder's own email address and password (also personal information, 501.171(1)(g)1.b.);
   - **anything marked CUI** (FC-4 drawings or A&E packages that leaked into email). If present, this is also a cyber incident affecting covered defense information: switch to `ir-runbook-cui-incident.md` for that part and start the 72-hour clock;
   - federal drawings and pay apps (FCI): no notice duty under FAR 52.204-21, but record it for the CMMC scope review;
   - client facility security details (camera layouts, controller credentials): contract notice to the MBSS or installation client;
   - owners' and subcontractors' confidential pricing: contract notice where the contract requires it.
4. **Money trail.** For each payment: amount, date, receiving bank and account, recall status, IC3 number, and whether it was a federal job.
5. **Other victims.** Did the attacker email other owners, subcontractors, or the surety from the mailbox or a lookalike domain? Use sent items and message trace. Each recipient gets a call.
6. **Pay app integrity in SYS-01.** If the account could edit pay apps, compare each pay app and remittance page in SYS-01 with the ERP version and the copy the owner received.

## 5. Containment and eradication (RS.MI)
1. Remove malicious rules, forwarding, OAuth grants, and delegates. Re-register MFA with a FIDO2 security key for the affected user before access is restored.
2. Block the attacker's sign-in sources and lookalike domains at the mail gateway; request takedown of lookalike domains.
3. Reset credentials for every system the user reached by single sign-on. For variant C, also reset the SAM Entity Administrator credentials and review all SAM roles.
4. Hunt across all payment-role mailboxes (Project Managers, billing, accounts payable, executives) for the same rules, sign-in sources, and messages.
5. Keep the vendor-master freeze until every bank change from the last 90 days is re-verified by call-back and a second approver (STD-04). Keep the first-payment hold for any account changed in that window.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel confirms every notice before it goes out and keeps the decision log (POL-03 4.10).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Was personal information accessed? Of whom, and residents of which states? | General Counsel with forensics | Decision log; affected individuals list by state |
| D2 | Date of determination (Florida clock) | General Counsel | Decision log |
| D3 | Was CUI in the compromised accounts? If yes, run the CUI runbook in parallel | Security Manager and General Counsel | Decision log |
| D4 | Has law enforcement asked for a delay? Florida allows a delay on a written request (501.171(4)(b)) | General Counsel | Decision log |
| D5 | Who bears the loss with the owner or subcontractor, and does the company keep paying real subcontractors meanwhile? | CFO and General Counsel, approved by the CEO above $250,000 | CMT minutes |
| D6 | Are contract, surety, lender, or MBSS client notices due? | General Counsel and CFO | Contract register |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Minutes | Bank recall request; owner told to call its bank (variant A) | Controller; Project Executive |
| Hour 0-1 | Insurer hotline; counsel engaged | CFO |
| Day 0 | IC3 complaint "as soon as possible, regardless of the amount" | Security Manager |
| Day 0 | Variant C: correct SAM; tell the Contracting Officer and paying office for each affected federal contract (FAR 52.232-33) | Director of Contracts and Compliance |
| Day 0-2 | Written notice to every affected owner and subcontractor confirming the real bank details and the call-back rule | CFO |
| Within 72 hours of discovery | Only if CUI was in a compromised account: DoD report at https://dibnet.dod.mil (DFARS 252.204-7012(c)) through the CUI runbook | Director of Contracts and Compliance |
| Within 7 days of receiving the Government's payment | Variant B on a federal job: pay the real subcontractor even though the first payment was diverted (FAR 52.232-27(c)(1)) | CFO |
| As soon as known | Written personal information determination (D1, D2) | General Counsel |
| Within 30 days of that determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 (Fla. Stat. 501.171(3) to (5)). Residents of other states per their laws | General Counsel |
| Per contract | Owners, MBSS clients, the surety, lenders | General Counsel and CFO |

**Paying twice.** In variant A, the owner may still owe the company; in variant B, the subcontractor must still be paid. Counsel decides who bears the loss. The company does not stop paying real subcontractors while that is argued, because that invites liens on private jobs and interest penalties on federal ones (FAR 52.232-27(c)(2)).

**Insurance.** The $1 million social engineering sublimit is smaller than one average pay app, and the claim depends on proof that the verification procedure was followed. Keep the call-back records (or their absence) for the claim; do not reconstruct them after the fact.

**Communications.**
- Owners and subcontractors: a call from the Project Executive, then a letter from the CFO. No technical details or speculation about fault.
- Staff: a short briefing script by text: what happened, do not discuss externally, report any odd payment request, never use a phone number from an email.
- Media: holding statement approved by counsel, only if the incident becomes public.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). For BEC, **"restored" means "verified"**.

| Order | Resource | Target (BIA) | Validation before use |
|---|---|---|---|
| 1 | SYS-04 identity provider: affected accounts re-secured with FIDO2; break-glass accounts confirmed | 1 h | No attacker sessions; MFA methods reviewed |
| 2 | Out-of-band contact list (owners, banks, subcontractors) | 1 h | Numbers re-verified from contract files |
| 3 | SYS-05 email: mailboxes cleaned; alerts confirmed | 4 h | Rules, delegates, and OAuth grants clean across payment roles |
| 4 | SYS-01 project platform access for affected users | 8 h | Pay app pages compared with the ERP; session tokens revoked |
| 5 | SYS-02 ERP vendor master | 8 h in billing week | Every bank change in the last 90 days re-verified by call-back and second approval before the freeze is lifted |
| 6 | SYS-10 bank portal | 8 h in billing week | Dual approval and positive pay confirmed; new beneficiary hold active |
| 7 | SYS-14 SAM | Before the next federal invoice | EFT data matches the bank; Entity Administrator on a security key |
| 8 | SYS-03 payroll self-service (variant D) | Before the next payroll | Direct deposit changes in the window reversed after call-back to each employee |

The pay app cycle resumes with a remittance confirmation call to each owner for the next two cycles. **Tell people when it is safe (RC.CO):** a confirmation letter to owners and subcontractors, and a staff briefing on what to watch for.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days of closing (POL-03 4.13).
- Update the risk register (P01 R-001, R-002, R-025, R-026, R-033, R-040, R-041), the POA&M (P07), STD-04, training, and this runbook.
- If the company holds a CMMC status by then, General Counsel and the GRC analyst confirm that every requirement is still met before the next award or affirmation (notification matrix, "CMMC status currency").
- Retain all incident documentation for at least 6 years (POL-01 4.16). Keep any written Florida no-harm determination for 5 years (501.171(4)(c)).

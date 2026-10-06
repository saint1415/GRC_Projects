# Incident Response Runbook: Treasury Payment Fraud Through Business Email Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed holding company with four operating subsidiaries) |
| Tier / Vertical | Mid-Market / Management of Companies and Enterprises |
| Incident type | A supplier's or an executive's identity is used (through a spoofed or compromised mailbox, a phone call, or a takeover of a group mailbox) to change bank details or request an urgent payment, and a payment is released, or about to be released, to an account the attacker controls |
| Why this is the second incident type | The holding company moves about $3.5 million a business day for five companies. Business email compromise is the most likely cyber event to cause a direct loss (P01 R-005 High; R-006; R-050), and its first hour is about the bank, not the network |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 4.9 (bank first); POL-05 4.4 (callback verification); POL-02 4.14 (segregation of duties) |
| Companion documents | `ir-runbook.md` (shared services compromise; use it too if a group mailbox or identity was taken over); `notification-matrix.csv` |
| Runbook owner | Treasurer (payment response) with the Security Manager (technical response) |
| Approved | 2026-09-22 by the CEO |
| Last tested | Not yet. Group tabletop for this scenario on 2027-02-17 with the banks' fraud teams invited (POAM-011) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Payment response lead | Treasurer | CFO | Mobile phone; bank hardware tokens kept by each |
| Technical response (mailbox, identity, ERP changes) | Security Manager | VP of Information Technology | Incident line |
| Crisis decisions, lenders, sponsor | CFO | CEO | Mobile phone |
| Legal, law enforcement, insurers | General Counsel | Outside counsel (insurer panel) | Mobile phone |
| Subsidiary contact (whose supplier or payment it was) | Relevant subsidiary President and its office manager | Controller | Mobile phone |
| Banks | Each operating bank's fraud line and relationship manager | Treasury analysts | Numbers in the treasury binder and on the bank token cards |
| Insurers | Crime carrier (social engineering fraud sublimit $250,000); cyber carrier hotline | Broker | Policy cards |
| Law enforcement | FBI IC3 (online report); FBI field office | Local police report if the bank requires one | Numbers in the binder |

## 1. Preparation checks (Identify / Protect)
- [x] Bank-enforced dual approval for wires and ACH batches; positive pay on all operating accounts
- [x] ERP segregation of duties: vendor master changes separate from payment release (POL-02 4.14)
- [ ] Callback evidence required in the ERP before a bank-detail change can be saved (P01 R-005; due 2026-12-31). **Today the callback is a procedure; P03 sampling found 2 of 25 changes without a callback record**
- [ ] 5-day hold on the first payment to changed bank details (due 2026-12-31)
- [ ] Home Services North vendor payments moved into the ERP (due 2027-03-31; until then North office staff pay some vendors locally)
- [ ] Phishing-resistant keys for treasury and payables users (POAM-003)
- [x] Annual payment fraud training for treasury and shared payables staff
- [x] Bank fraud lines and recall procedures confirmed with each bank (2026-09)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A supplier says it was not paid, or asks about a payment it did not receive | Supplier; subsidiary office | Treasurer checks where the payment went; if the account is not the one on file before the last change, declare |
| A request to change bank details, or an urgent or unusual payment request, that fails callback | Payables or treasury staff (POL-05 4.4) | Do not change or pay; report to the Treasurer and the incident line; declare if a group mailbox may be involved |
| The bank flags a payment or a new payee | Bank alert | Treasurer calls the bank fraud line; declare if fraudulent |
| A new inbox rule that hides or forwards invoice or payment mail | Mailbox audit in the SIEM; user report | Security Manager follows `ir-runbook.md` section 3 for the mailbox; Treasurer reviews payments from that user's queue |
| A request that appears to come from the CEO, CFO, or a subsidiary President asking for a confidential urgent wire | Any employee | Verify by calling the executive on the number on file; report |

**Declare an incident** when any payment has gone, or was about to go, to an account not verified by callback, or when a group mailbox involved in payments shows signs of takeover.
**Record the time the fraud was first known** to any employee. If customer or employee personal information was in the compromised mailbox, the FTC, HIPAA, and Florida clocks in `notification-matrix.csv` may also start.

## 3. First hour: the money (RS.MI)
Speed matters more than anything else: banks can sometimes recall or freeze funds only while they are still in the receiving bank.

| Minute | Step | Who | Done when |
|---|---|---|---|
| 0-15 | Call the sending bank's fraud line. Give amount, date, receiving bank, and account. Ask for an immediate recall request to the receiving bank and a hold on any pending payments to the same account | Treasurer (CFO if the Treasurer is unavailable) | Bank reference number recorded |
| 0-15 | Stop every unreleased payment to the changed account in the ERP and the treasury system; put the vendor record on hold | Controller | Vendor on hold |
| 0-30 | File an FBI IC3 complaint with the transaction details (the bank may ask for it); keep the confirmation | Treasurer with the General Counsel | IC3 confirmation saved |
| 0-30 | Notify the crime carrier and the cyber carrier hotline; do not hire vendors before the carrier assigns them | CFO | Claim numbers |
| 0-60 | Check the last 10 business days for other payments to changed details across all five companies | Controller; treasury analysts | List reviewed |
| 0-60 | Contact the real supplier on a number from the vendor file (not the email) and confirm its correct details | Subsidiary office manager | Confirmed |

## 4. Analysis (RS.AN)
1. **How was the instruction delivered?** Spoofed or look-alike domain, a compromised supplier mailbox, a compromised group mailbox, or a phone call. If a group mailbox or identity was taken over, run `ir-runbook.md` sections 3 to 5 in parallel.
2. **Which control failed?** Callback skipped or done to a number in the request; second approver did not check the evidence; payment made outside the ERP (Home Services North).
3. **What else did the attacker see?** If a group mailbox was involved, list what it held: Finance customer information, plan PHI, employee data. That decides whether notification duties start (General Counsel).
4. **Preserve evidence:** the emails with full headers, call records, ERP change history, bank confirmations, and the IC3 receipt.

## 5. Containment and eradication (RS.MI)
1. Reset and re-register MFA for any affected group user; remove malicious inbox rules and app consents (`ir-runbook.md` section 5).
2. Block the look-alike domains in the mail filter; warn all payables and subsidiary office staff by text and email with the sender details.
3. Tell the real supplier that its identity or mailbox was used, so it can secure its systems and warn its other customers.
4. Re-verify by callback every bank-detail change made in the last 90 days for the affected subsidiary.

## 6. Reporting and communication (RS.CO)
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Sending bank fraud line; IC3 complaint; insurers | Treasurer; CFO |
| Day 0 | Affected subsidiary President; audit committee chair if the loss could exceed $250,000 | CFO |
| Day 0-1 | Sponsor operating partner if severity 1 (contract: 24 hours) | CEO |
| Per agreement | Lenders, if counsel decides the loss is a reportable event under the credit agreement or warehouse line | CFO with the General Counsel |
| If personal information was exposed | Follow the notice timeline in `ir-runbook.md` section 6 and the matrix | General Counsel |
| Within 30 days | Proof of loss to the crime carrier as the policy requires | CFO |

**Accounting.** The Controller records the loss and any recovery in the paying subsidiary's books; the CFO decides whether the supplier is still owed (usually yes) and pays it only after callback verification.

## 7. Recovery (RC.RP)
1. Release held payments to verified accounts only, with a second approver checking the callback record.
2. Resume normal vendor payment runs once the 90-day re-verification is done for the affected subsidiary.
3. Track recall status with the bank daily until closed.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days with the Treasurer, Controller, the affected subsidiary's office staff, and the Security Manager.
- Update the risk register (P01 R-005, R-006), the POA&M, payment fraud training, and this runbook.
- Keep the records for at least 6 years (POL-01 4.16).

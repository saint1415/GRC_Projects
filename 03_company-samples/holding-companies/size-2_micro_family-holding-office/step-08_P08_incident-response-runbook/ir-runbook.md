# Incident Response Runbook: Compromise of the Shared Tenant Affecting Subsidiaries and the Family

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (family holding company and single-family office) |
| Tier / Vertical | Micro / Management of Companies and Enterprises |
| Incident type | Compromise of the shared productivity and identity tenant (SYS-02): adversary-in-the-middle phishing of a staff member, mailbox takeover, a payment redirection attempt against a subsidiary or a family vendor, and access to the Family and Subsidiaries sites |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; POL-02 B.10 payment verification |
| Runbook owner | Family Office Director (Qualified Individual) |
| Approved | 2026-09-18 by the Principal |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POAM-008) |

## Why this incident
This is the registry's "compromise of shared services affecting subsidiaries" at Micro size. The office's one tenant is shared in three ways: the subsidiaries' presidents and controllers work in it as guests, the office approves the subsidiaries' large payments, and every family request arrives through it. One stolen session can therefore reach the family's records, the subsidiaries' board packs, and the payment approval chain at the same time (P01 R-001, R-002, R-003).

## 0. Roles and notification chain (Govern)
The office has 7 people and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics. The Family Office Director runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Family Office Director | Controller | Cell phone (numbers on the printed contact card) |
| Payment recall lead | Controller | Family Office Director | Bank fraud lines on the contact card |
| Decision maker (money, outside communications, any ransom question) | Principal | Eldest adult child (Board of Managers) | Cell phone |
| Technical response | MSP emergency line (number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's breach hotline | Insurance broker | Number on the policy card in the office safe |
| Breach counsel | Insurer panel counsel | Office's outside counsel | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm | n/a | Engaged by breach counsel (keeps the work under legal privilege, as counsel advises) |
| Banks and custodians | Fraud lines | Relationship managers | Contact card |
| Subsidiaries | Each Subsidiary President | Each subsidiary controller | Contact card |
| Law enforcement | FBI through IC3 | Local FBI field office | ic3.gov; contact card |

**Notification chain in the first hour:** staff member → Family Office Director → MSP emergency line and Controller (at the same time) → banks if money may have moved (Controller) → insurer breach hotline (Principal) → breach counsel and forensics (through the insurer) → Subsidiary Presidents if their payments, guests, or board files are involved.

**Out-of-band first.** Assume email and chat are read by the attacker. Coordinate by phone and text on personal phones, using the printed contact card. Never confirm a payment by replying to an email.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the office safe and at the Family Office Director's, Controller's, and Principal's homes: this runbook, contact card, notification matrix, and the payment log template
- [ ] Phishing-resistant security keys for staff and administrators (IA-2(1)). **Gap until POAM-002 closes**
- [ ] SYS-02 alerts for risky sign-ins, new inbox rules, forwarding, and mass downloads routed to the MSP and the Family Office Director; one-year logs (AU-6). **Gap until POAM-003 closes**
- [ ] Callback procedure and payment log in use (POL-02 B.10); bill pay dual approval on (done 2026-09-04)
- [ ] Need-to-know folders, so one mailbox does not reach every family's records (AC-6). **Gap until POAM-005 closes**
- [ ] Independent backup of mail and files (CP-9). **Gap until POAM-006 closes**
- [ ] Insurer hotline and policy number checked at renewal; banks' fraud line numbers checked each quarter
- [ ] Subsidiaries and family members told in writing that the office never changes bank details by email

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A subsidiary or vendor calls to confirm an email asking it to pay a "new" office account | Callback from outside | Tell them not to pay. Declare an incident. Identify the mailbox that sent it |
| A staff member entered a password on a page reached from an email, or approved an MFA prompt they did not start | Staff report | MSP revokes all sessions and resets the password and MFA; check sign-in log and inbox rules |
| New inbox rule that moves or deletes messages containing "wire", "payment", "invoice", or "bank" | SYS-02 alert (once POAM-003 closes) or staff noticing missing replies | Treat as a confirmed takeover. Declare |
| Sign-in from an unusual country or a new device for a staff or guest account | SYS-02 alert | MSP checks; declare if not explained within 1 hour |
| A family member reports an email "from the office" asking for documents or a transfer | Family member call | Declare; warn all family members by phone |
| Bank or custodian reports an unusual payment, a changed payee, or failed token attempts | Bank call | Controller freezes pending items with the bank; declare |

**Declare a tenant compromise** when any staff or guest mailbox shows sign-ins, rules, or messages the owner did not make, or when anyone receives a payment or bank-change request that the office did not send.

**Write down the key times.** Florida's 30-day clock starts at the office's determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(4)(a)). For the FTC rule, a notification event is discovered on the first day any employee, officer, or agent other than the attacker knows of it (16 CFR 314.4(j)(2)). The first staff report is that day.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **If money may have moved, call the sending bank's fraud line and request a recall now.** Then freeze pending wires, ACH batches, and bill pay runs | Controller | Bank reference number recorded |
| 2. Call the MSP emergency line. MSP revokes all sessions and tokens for the affected account, resets the password and MFA, disables the account if takeover is confirmed, and removes inbox rules and forwarding | Family Office Director; MSP | MSP confirms the account is contained |
| 3. Phone each Subsidiary President and controller: do not act on any payment or bank-change email from the office until called back; check their own mailboxes for messages from the affected account | Family Office Director | All three subsidiaries reached |
| 4. Call the insurer's breach hotline and give the claim details | Principal | Claim number issued; counsel assigned |
| 5. Revoke sessions for all staff and the MSP shared admin account as a precaution; confirm no new admin accounts, app consents, or MFA methods were added | MSP | Admin audit checked |
| 6. Phone family members whose folders the account could reach; tell them not to act on email requests from the office | Executive Assistant (from the contact card) | Families reached |
| 7. Open the incident log: timeline, actions, who, when | Family Office Director | Log started |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Scope.** Which accounts signed in from the attacker's sessions? Sources: SYS-02 sign-in and audit logs, the mailbox audit log, and admin activity. Check single sign-on access to SYS-01, SYS-03, SYS-04, and SYS-06 from those sessions.
2. **Initial access.** Find the phishing message, its sender, and its link. Search all mailboxes, including guests' messages, for the same message and remove it.
3. **Preserve evidence.** Export sign-in, audit, and mailbox logs at once, because the current license keeps them for less than a year (POAM-003 context). Keep a chain-of-custody record for every export.
4. **Payments.** List every payment, payee change, and bank-detail email in the period. Match each against the payment log and callbacks.
5. **Data accessed.** Which Family and Subsidiaries site files did the attacker open or download? Which mail did it read? This decides who must be notified. The question for Florida is unauthorized **access** to personal information (501.171(1)(a)). For the FTC rule, unauthorized access to unencrypted customer information is presumed to be acquisition unless reliable evidence shows otherwise (16 CFR 314.2(m)).
6. **Whose information.** Sort the people affected: family members (by state of residence), household and office employees, and any subsidiary personal information (the office is that subsidiary's third-party agent).
7. **Subsidiaries.** Ask each subsidiary's IT provider to check whether the attacker sent phishing from the office's account to subsidiary staff, and whether any subsidiary account was compromised as a result.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's sending domains, look-alike domains, and IP addresses in SYS-02 (MSP).
2. Disable compromised accounts; remove attacker-added inbox rules, forwarding, app consents, delegated mailbox permissions, and MFA methods.
3. Require re-registration of MFA for affected users with security keys as soon as they are available.
4. Remove and re-add guest accounts that received messages from the compromised mailbox after their owners confirm by phone.
5. Rotate shared credentials the mailbox held or could reach: bill pay and payroll passwords, any stored bank portal usernames (bank tokens are separate), and the MSP shared admin password.
6. Confirm with forensics that no persistence remains (no rules, no app consents, no unknown devices) before returning accounts to users.
7. If the MSP's account or tools may be the entry point, the Principal asks the insurer's forensic firm to lead eradication and requires the MSP to share its own investigation results (P01 R-005).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice before it goes out. The Family Office Director documents the breach decision for each group of affected people.

| When | Action | Owner |
|---|---|---|
| Hour 1 | Bank recall requests; MSP engaged; insurer notified; subsidiaries warned by phone | Controller; Family Office Director; Principal |
| Day 0-1 | Complaint to the FBI through IC3 with the fraudulent account details (helps recall efforts) | Controller with counsel |
| Day 0-1 | Staff briefing: what happened, how to verify requests, send all outside questions to the Principal | Family Office Director |
| Day 0-2 | Board of Managers informed | Principal |
| As soon as scope is known | Breach decision documented for each group; affected people counted by state of residence | Family Office Director with counsel |
| Within 24 hours of knowing subsidiary information is involved (legal limit 10 days) | Notice to the affected subsidiary as its third-party agent (501.171(6)(a)) | Family Office Director |
| Within 30 days of determination | Florida individual notices by mail or email; other states' notices under their own clocks. If counsel decides no notice is needed under 501.171(4)(c), the written determination goes to the Department within 30 days | Family Office Director and counsel |
| Within 30 days of discovery, only if 500 or more consumers | FTC notification event form (16 CFR 314.4(j)); not expected at the office's size | Family Office Director |
| Weekly until closed | Status to family members and Subsidiary Presidents | Principal |

**Plan to the shortest clock.** With only a few dozen people's information in the office, Florida's 30-day limit is the clock that matters most. Notices to family members are personal: the Principal or Family Office Director calls each adult before the written notice arrives.

**Inbound notices.** If a vendor (MSP, bill pay, payroll, vault, investment platform) is where the breach happened, it must notify the office within 10 days of its determination as a Florida third-party agent (501.171(6)(a)). The office still sends the notices to individuals.

**Ransom or extortion.** If the attacker threatens to publish family records, only the Principal decides, with breach counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.8). Paying does not remove notification duties.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Clean laptops for the Controller and Family Office Director, and bank tokens checked (approvals can resume with the Principal as backup approver)
2. Identity and email: affected accounts returned with new MFA; inbox rules and forwarding checked for every staff mailbox
3. Document vault: family users told to check their own folders; share links reviewed
4. Bill pay and payroll: payee list compared with the last known-good export; every bank-detail change since the start of the compromise verified by callback
5. Investment platform and custodian access: custodian instructions since the start of the compromise confirmed with each custodian
6. Accounting and consolidation: payee bank details in SYS-01 checked against the payment log
7. SYS-11 and reporting: no change expected; confirm with the MSP

**Before returning to normal:** every payment instruction received during the compromise window has been verified by phone, and subsidiaries and family members have been told the office is operating normally (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, counsel, and a representative of any affected subsidiary. Written summary within 30 days (POL-03 4.11).
- Update the risk register (P01, especially R-001, R-002, R-003, R-005, R-018), the POA&M (P07), training content, and this runbook.
- Record two measures in the lessons-learned summary: time from first report to account containment, and time from first report to the bank recall call.
- Keep the incident log, breach decisions, notices, and forensic report for at least 5 years (the Florida no-notice determination must be kept 5 years; the office keeps all incident records for the same period).
- Include the incident in the Family Office Director's annual written report to the Board of Managers.

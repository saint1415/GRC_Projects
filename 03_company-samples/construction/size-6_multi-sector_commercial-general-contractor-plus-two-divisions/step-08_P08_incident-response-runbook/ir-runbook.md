# Incident Response Runbook: Business Email Compromise Redirecting Progress Payments (Cross-Division)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Construction |
| Incident type | Business email compromise (BEC) that redirects progress payments, spreading from a Construction mailbox to Property accounts payable and Property tenants, in a mailbox that also holds CUI and certified payrolls |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; POL-01 4.15 payment instructions; division supplements (P06) |
| Runbook owner | Group CISO; payment response owned by the Group Treasurer; notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO, the Group Chief Financial Officer, and the Group General Counsel |
| Last tested | Technical BEC playbook tested 2026-06 (single division). **The cross-division notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop is due 2026-12-15 (POAM-004) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. It is set before the CUI purge under POAM-006 is complete. Amounts are illustrative.

| Thread | What happens | Division | Money or data at risk |
|---|---|---|---|
| **A. Owner pays the attacker** | An adversary-in-the-middle phishing page captures a Construction project executive's session despite number-matching MFA (P01 CON-027). The attacker reads the mailbox for 3 weeks, hides replies with inbox rules, and sends a hospital owner "updated remittance instructions" from the real mailbox. The owner pays a monthly pay application to the attacker | Construction | $2.4 million |
| **B. Property pays the attacker** | From the mailbox the attacker learns that a mechanical subcontractor also works on a Property tenant improvement project. A spoofed email asks Property accounts payable to change the subcontractor's bank account. One approver processes it in SYS-D3, outside the payment factory (scenario gap 3) | Property | $380,000 |
| **C. Tenants pay the attacker** | The attacker registers a lookalike of a property brand domain and mails rent "remittance change" letters to tenants at 3 properties. 3 tenants pay | Property | $610,000 in rent |
| **D. Data in the mailbox** | The mailbox holds 47 CUI-marked drawings from a DoD design-build project (part of the 212 messages found on 2026-07-14) and 31 subcontractor certified payroll files with names and full Social Security numbers of about 1,860 craft workers (about 1,240 in Florida, about 620 in 3 other states) | Construction (prime on the DoD contract) | DoD reporting; state breach notices |

**Day 0** is when the owner's accounts payable calls the project accountant to confirm that the "new account" received the payment. The project accountant calls the Group Treasurer, who calls the SOC.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Payment response lead | Group Treasurer | Group Controller | Bank fraud desk numbers on the printed card (never from email) |
| Construction liaison (owner contact, subcontractors, payroll data) | Construction VP of project controls | Construction security and compliance lead | Division bridge |
| Property liaison (accounts payable, tenants) | Property Controller | Property security and compliance lead | Division bridge |
| DoD reporting and federal contracts | Director of Federal Contracts Compliance (holds the DIBNet certificate) | Group General Counsel | Division bridge |
| Notifications and legal | Group General Counsel with outside breach and government contracts counsel | Division counsel | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group Chief Financial Officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Cyber insurer | Carrier breach hotline (social engineering sublimit $10 million) | Group Chief Risk Officer | Policy card in the incident binder |
| Law enforcement | FBI IC3 and field office | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read the compromised mailbox and may hold other sessions. Coordinate by phone and the crisis line. Call owners, tenants, and subcontractors only at numbers from the contract or lease file. The printed binder in each division's command center holds contacts, this runbook, and the notification matrix.

**Who calls the owner.** Not the compromised project executive. The project executive's manager makes the call with the Group Treasurer.

## 2. Preparation checks (Identify / Protect)
- [x] Payment factory: call-back and second approver for every vendor bank change (AC-5, SI-10; P07 satisfied)
- [x] Phishing-resistant MFA for finance, treasury, and project executives (POL-02 4.3). **This scenario assumes a project executive not yet moved from number-matching MFA**
- [x] 24x7 SOC with mailbox audit logging and alerts on new forwarding and inbox rules
- [x] Cyber insurance with a social engineering sublimit; forensic retainer through the insurer's panel
- [x] Disclosure committee charter includes cybersecurity materiality
- [ ] Property bank changes in the payment factory (**gap until POAM-031 closes**)
- [ ] Pay application remittance block generated only from verified bank data (**gap until POAM-009 closes**)
- [ ] DMARC reject on all property domains and lookalike monitoring of property brands (**gap until POAM-005 closes**)
- [ ] No CUI in commercial mailboxes (**gap until POAM-006 and POAM-011 close**)
- [ ] Certified payrolls received only through the PDPP intake with masked Social Security numbers (POL-04 4.7; **not yet in place**, P01 GR-13)
- [ ] Notification matrix exercised across divisions (**gap until POAM-004 closes**)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Owner, tenant, or subcontractor asks about a bank change the group did not make | Phone call | Declare at once. Ask the caller not to pay any new account and to call its own bank |
| Expected owner payment not received within 2 business days of its due date | Group cash application report | Call the owner's AP at the number on file |
| Subcontractor says "we never received payment" | Subcontractor call | Check the payment factory and SYS-D3 change logs; declare if bank details changed recently |
| New inbox rule, external forwarding, or a sign-in from a new device right after MFA approval | SYS-G1 and mailbox alerts | Revoke sessions; review the mailbox; declare if unexplained |
| A tenant forwards a "remittance change" letter | Property management | Declare; start the lookalike domain takedown |
| SAM notice of a registration change the group did not make | SAM email to an Entity Administrator | Declare (federal payment variant) |

**Severity 1** (group scale, POL-03 4.2): money diverted in more than one division, or CUI or personal information in an affected mailbox. This scenario is Severity 1 on Day 0.

**Record these times in the incident log** (POL-03 4.3):
- **Discovery of the cyber incident** (Day 0): starts the DoD 72-hour clock, because the mailbox is known to hold CUI.
- **Determination that personal information was accessed** (expected Day 4, after forensics confirms the attacker opened the payroll attachments): starts the Florida 30-day clocks. Do not wait for funds recovery to make this determination.
- **Materiality determination** by the disclosure committee: starts the 4-business-day Form 8-K clock if material.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Recall requests.** Call the group's bank fraud desk for the Property AP payment. Ask the owner and the 3 tenants to call their own banks at once | Group Treasurer; Property Controller | Recall reference numbers recorded |
| 2. Freeze all bank-detail changes in the payment factory **and in SYS-D3**; hold unreleased Property AP batches | Group Treasurer; Property Controller | Freeze confirmed in both systems |
| 3. Revoke all sessions for the project executive; reset the password; remove attacker MFA methods and OAuth grants; enroll a security key | Group identity director | Sign-in log shows no new sessions |
| 4. Export evidence before it rolls off: SYS-G1 sign-ins, mailbox audit log, inbox rules, sent items, message trace, SYS-D3 and payment factory change logs. Preserve images under DFARS 252.204-7012(e) | Group SOC director | Exports hashed and stored; legal hold set |
| 5. Call the cyber insurer; engage panel breach counsel and forensics | Group Chief Risk Officer | Claim number issued |
| 6. Phone every owner with a pay application from this project executive in the last 60 days, every tenant at the 3 properties, and every subcontractor paid by Property AP in the last 30 days, at numbers on file | Construction VP of project controls; Property Controller | Call logs complete |
| 7. Tell the Director of Federal Contracts Compliance that the mailbox held CUI; start the DoD report | Incident commander | Report drafting started |
| 8. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.6) | Group CISO | Committee convened |
| 9. Start the lookalike domain takedown request with the registrar and block the domain at the mail gateway | Group SOC director | Takedown request reference recorded |

## 5. Analysis (RS.AN)
1. **Initial access.** Find the phishing message and the adversary-in-the-middle sign-in (a new session from an unfamiliar location right after an approved MFA prompt).
2. **Persistence and spread.** Inbox and forwarding rules, OAuth app consents, new MFA methods, delegates, and the same actor's sign-ins to other accounts (other project executives, the PDPP, SAM). Check whether the attacker changed any remittance block in the PDPP (remittance edits are not yet in the SIEM, so pull the PDPP audit log directly; POAM-009).
3. **Mailbox contents.** List what the attacker could read. This drives the notices:
   - **CUI-marked drawings** (47 files): a cyber incident affecting covered defense information. DoD report within 72 hours of discovery (DFARS 252.204-7012(c)).
   - **Certified payrolls with Social Security numbers** (31 files, about 1,860 people): personal information under Fla. Stat. 501.171(1)(g) and other states' laws.
   - **The project executive's email address and password**: also personal information in Florida (501.171(1)(g)1.b.).
   - **FCI** on federal jobs: no separate notice duty under FAR 52.204-21, but a Level 1 requirement may no longer be met (notification matrix, "CMMC status currency").
   - **Client facility security details**: check for TSSI client data (none found in this scenario).
4. **Money trail.** For each payment: amount, date, receiving bank and account, recall status, and IC3 complaint number.
5. **Other victims.** Use sent items and message trace to find every owner, subcontractor, and design consultant the attacker emailed.
6. **Root cause.** Number-matching MFA on a payment-role user (CON-027), the free-text remittance block (POAM-009), Property's single-approver bank changes (POAM-031), property domains at DMARC monitor-only (POAM-005), and CUI and payroll files in email (POAM-006, P01 GR-13). Feed these to P01 GR-01, GR-02, and GR-13.

## 6. Containment and eradication (RS.MI)
1. Remove malicious rules, forwarding, OAuth grants, and delegates. Move every project executive still on number-matching MFA to phishing-resistant authenticators within 14 days (accelerates POL-02 4.3).
2. Block the attacker's sign-in sources and the lookalike domains at the mail gateway.
3. Reset credentials for any system the user reached through single sign-on. Review SAM EFT data against the bank.
4. Search all payment-role mailboxes (project executives, project accountants, Property AP) for the same rules or sign-in patterns.
5. Keep the bank-change freeze until every change in the last 90 days, in both the payment factory and SYS-D3, is re-verified by call-back and second approval. Route Property bank changes through the payment factory from now on (accelerates POAM-031).
6. Purge the CUI and certified payroll files from the mailbox with a record of each removal, after evidence is preserved (accelerates POAM-006).

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (27 rows).** Counsel approves every notice. Notices come from the **entity that owes them**: Cris Santos Construction, LLC for the DoD report, the owner, the subcontractors, and the payroll data; Cris Santos Properties, LLC for tenants; the holding company for the SEC.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Recall requests; owner and tenants told to call their banks | Group Treasurer; Property Controller |
| Day 0 | Insurer notified; counsel and forensics engaged; corporate tells Construction on the bridge that its data was in a corporate-run mailbox (third-party agent duty, worked example) | Group Chief Risk Officer; Group CISO |
| Day 0-1 | IC3 complaint filed "as soon as possible, regardless of the amount" | Group CISO |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Day 0-2 | Written notice to the owner, the 3 tenants, and the affected subcontractor confirming real bank details and the call-back rule; letter to all about 1,600 tenants restating the remittance rule | Construction VP of project controls; Property Controller |
| **Within 72 hours of discovery (by Day 3)** | DoD cyber incident report at dibnet.dod.mil for the CUI in the mailbox; images preserved 90 days from the report | Director of Federal Contracts Compliance |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 7 days of receiving the Government's payment | If any diverted payment was owed to a subcontractor on a federal job: pay the real subcontractor (FAR 52.232-27(c)) | Group Treasurer |
| As soon as known (expected Day 4) | Written personal information determination | Group General Counsel |
| Within 30 days of that determination | Florida individual notices; Department of Legal Affairs (about 1,240 Floridians, so 500 or more); consumer reporting agencies (more than 1,000 notices). Each other state's law applied the same way. The 14 affected subcontractors are told first | Group General Counsel |

**Plan to the shortest clock.** In this scenario the order is: bank recalls (hours), the DoD report (72 hours), SEC (if material), then the 30-day state notices.

**Materiality factors for the disclosure committee.** Quantitative: about $3.4 million diverted before recoveries and insurance, against about $18 billion revenue. Qualitative, which matter more here: a DoD report involving CUI while the group's CMMC statuses are under counsel review (P03 G-023) and Phase 2 begins; owner and tenant trust; personal information of about 1,860 craft workers; and whether the same weakness exists at other project executives. The committee documents its reasoning even if it decides the incident is not material. The 4-business-day clock starts at the determination, not at discovery.

**Paying twice.** The owner may still owe Construction for the pay application, and the subcontractor must still be paid by Property. Counsel decides who bears each loss. The group does not stop paying real subcontractors while that is argued, because that invites liens and, on federal jobs, interest penalties.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). For BEC, "restored" means "verified":
1. SYS-G1 identity: the affected account re-secured with a security key; break-glass accounts confirmed (BP-G01)
2. Cloud, network, and SOC visibility confirmed clean (BP-G03, BP-G02)
3. Payment factory: freeze lifted only after every bank change in the last 90 days is re-verified; Property bank changes now routed here (BP-G04)
4. Pay application processing: the next two cycles carry a remittance confirmation call to each owner (BP-C02)
5. Rent collection: tenants confirm the remittance rule in writing before the next billing (BP-P03)
6. Email last: mailbox cleaned, alerts confirmed, CUI and payroll files purged with records (BP-G07). Restoring email before identity is secured hands the channel back to the attacker (P05)
7. CMMC: the Director of Federal Contracts Compliance confirms every Level 1 requirement for the PDPP scope is still met before the next award or affirmation

**Tell people when it is safe (RC.CO):** send a confirmation to owners, tenants, and subcontractors, and brief project and accounting staff on what to watch for.

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.13).
- Update P01 (GR-02, CON-001, CON-027, PRP-003, PRP-005, GR-13), the POA&M (POAM-005, POAM-006, POAM-009, POAM-031), training content (POL-05 4.3, 4.5), the notification matrix, and this runbook.
- Add the incident to the CMMC evidence file and tell the Affirming Official before the 2027-01-20 affirmation.
- Consider the Reg S-K Item 106 description for the next annual report.
- Keep all incident records for 6 years (POL-01 4.11). Keep any written Florida no-harm determination for at least 5 years (501.171(4)(c)).

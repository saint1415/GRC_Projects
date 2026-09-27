# Incident Response Runbook: Compromise of Shared Services Affecting Subsidiaries

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (holding company with three operating subsidiaries) |
| Tier / Vertical | Small / Management of Companies and Enterprises |
| Incident type | Compromise of the shared identity and email tenant: adversary-in-the-middle phishing of a shared-services user, mailbox takeover, a payment redirection attempt, and access to shared file sites holding Finance customer information and employee records. Also covers escalation to an administrator account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy. For Finance, POL-03 and this runbook are the written incident response plan under 16 CFR 314.4(h) |
| Runbook owner | IT Manager (Qualified Individual for Finance) |
| Approved | 2026-09-25 by the CEO |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-016) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | Systems Administrator | Incident line (cell), then the out-of-band group on personal phones |
| Technical response | IT team; managed detection and response provider (from 2027-01-31) | Forensic firm through the insurer's panel | Provider 24x7 line |
| Executive decisions, payments, and bank | CFO | CEO | Cell |
| Finance customer information decisions | Finance President (with counsel) | CFO | Cell |
| Employee data decisions | HR Director (with counsel) | CFO | Cell |
| Subsidiary operations | Supply, Home Services, and Finance Presidents | Their deputies | Cell |
| Legal counsel | Outside breach counsel (insurer panel) | Group outside counsel | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Bank | Bank fraud line | Relationship manager | Numbers in the incident binder |
| MSP | MSP lead technician | MSP after-hours line | Cell |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read group email and chat. Coordinate on personal phones and the printed contact list in the incident binder at each site.

**Why this incident is different at a holding company.** One identity tenant serves all four companies. The first compromised account may belong to the holding company, but the data at risk belongs to each subsidiary, and each subsidiary may have its own notice duties. Record which company's data each affected system holds.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at HQ, the Supply warehouse, and the Home Services shop: this runbook, contacts, the notification matrix, and BIA workarounds
- [ ] Two break-glass accounts sealed and tested (POL-02 4.5). **Gap until POAM-003 closes**
- [ ] Hardware security keys for administrators and payment staff (POL-02 4.4). **Gap until POAM-004 closes**
- [ ] Identity, email, and cloud logs kept for 1 year (POAM-012). **Today only 30 days: export logs on day 0**
- [ ] 24x7 detection with authority to disable accounts (POAM-010). **Gap: nights and weekends uncovered**
- [ ] Immutable separate-account backups and a suite backup (POAM-008)
- [ ] Forensic retainer confirmed through the insurer panel (POAM-018)
- [ ] Data inventory showing where Finance customer information and employee SSNs are stored (P03 ID.AM-07)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Sign-in from an unfamiliar location right after a user approved an MFA prompt, or an "impossible travel" alert | Identity provider risk detection | Revoke the user's sessions; reset the password; review sign-ins and mailbox rules |
| A new inbox rule that forwards, hides, or deletes mail about invoices or payments | Mailbox audit, user report | Open an incident; preserve the rule; check for sent phishing |
| A vendor or employee bank-detail change requested by email | Payables or HR staff (POL-05 4.4) | Do not change; call back on the number on file; report to the incident line |
| Unusual bulk file access or downloads on Finance, HR, or deal sites | Suite audit (alerting planned) | Open an incident; identify files and data types |
| A new admin role assignment, new app consent, or MFA method added to an admin | Identity provider audit | Treat as critical: go to section 3 immediately |
| A payment the bank flags, or a vendor saying it was not paid | Bank, vendor | CFO calls the bank fraud line; open an incident |

**Declare an incident when** any account is confirmed used by someone other than its owner, any admin change cannot be explained, or any payment instruction is confirmed fraudulent.
**Record the time of discovery and the time of determination.** The FTC clock runs from discovery, the first day the event is known to any employee, officer, or other agent of Finance other than the attacker (16 CFR 314.4(j)(2)). Florida clocks run from the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(3)-(4), (6)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke all sessions and refresh tokens for affected accounts; reset passwords; remove attacker MFA methods | IT Manager | Accounts show no active sessions |
| 2. If any admin account is involved: sign in with a break-glass account, remove unknown admins, app consents, and federation changes | IT Manager | Admin role list matches the approved list |
| 3. Call the bank fraud line; hold or recall payments released in the last 5 business days to changed bank details | CFO | Bank confirms holds or recall requests |
| 4. Export identity, mailbox, and file audit logs before they roll off (30-day retention today) | Systems Administrator | Exports saved to the incident evidence folder with hashes |
| 5. Call the cyber insurer's breach hotline; engage counsel and forensics through the insurer | CFO | Claim number issued |
| 6. Tell the subsidiary Presidents whose data may be involved (same day, POL-03) | IT Manager | Each President acknowledges |
| 7. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Scope accounts:** which users and admins signed in from attacker infrastructure? Check the identity provider sign-in log, including token reuse and new MFA registrations.
2. **Scope mail:** inbox rules, sent items, mail read, and forwarded mail. Look for phishing sent to vendors or subsidiary staff.
3. **Scope files:** which collaboration sites and files the accounts opened or downloaded. Map each site to its company and data type (Finance customer information, employee SSNs, deal information). **This drives every notice decision.**
4. **Scope connected systems:** SSO sign-ins to the ERP, HRIS, loan servicing system (SYS-12), and distribution system (SYS-10). Check the cloud console and the SFTP server for access.
5. **Payments:** list vendor and employee bank-detail changes and payments in the window; confirm each by callback.
6. **Preserve evidence:** keep log exports and forensic images with a chain-of-custody record (RS.AN-06, RS.AN-07).
7. **Finance determination:** with counsel, decide whether a notification event occurred (16 CFR 314.2(m)). Unauthorized access to unencrypted customer information is presumed to be acquisition unless reliable evidence shows otherwise. Count affected consumers.

## 5. Containment and eradication (RS.MI)
1. Block attacker IP addresses and domains in conditional access and the email filter.
2. Remove malicious inbox rules, app consents, and forwarding; purge phishing messages sent from the account.
3. Require re-registration of MFA for affected users with hardware keys where issued.
4. Rotate secrets the attacker could have reached: SFTP service keys, integration service credentials, bank portal tokens of affected users.
5. Check endpoints of affected users with EDR; reimage if any malware is found.
6. Confirm with forensics that no persistence remains (new accounts, app registrations, federation settings) before closing containment.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Day 0 | Insurer notified; counsel engaged; bank fraud line called if payments are involved | CFO |
| Day 0 | Subsidiary Presidents told whose data may be involved (internal; the legal floor for the holding company as third-party agent is 10 days after determination, Fla. Stat. 501.171(6)(a)) | IT Manager |
| Day 0-2 | Voluntary report to FBI (IC3) and/or CISA; supports OFAC mitigation if any extortion payment is considered | IT Manager |
| Day 0-3 | Warn vendors and subsidiary customers who received phishing from the compromised account | CFO; subsidiary Presidents |
| As soon as known | Finance notification event decision and consumer count documented | Finance President and counsel |
| Within 30 days of discovery | **FTC notice** if the event involves 500 or more consumers (16 CFR 314.4(j)) | Finance President and counsel |
| Within 30 days of determination | Florida notice to individuals, and to the Department of Legal Affairs if 500 or more Floridians (Fla. Stat. 501.171(3)-(4)); consumer reporting agencies if more than 1,000 | Each affected company, with counsel |
| Per contract | Lender notice if the credit agreement requires it | CFO |
| Next September | Event and response included in the Qualified Individual's report to Finance's Board of Managers (314.4(i)(2)) | IT Manager |

**Plan to the shortest clock.** The FTC 30-day clock starts at discovery, which is often earlier than the Florida determination. Treat the first day any employee knew as the start for both.

**Not applicable here:** SEC Form 8-K Item 1.05 and Federal Reserve notice (the company is private and not a bank holding company). CIRCIA reporting is not yet required.

**Payment decision:** any extortion payment requires the CEO, the Board chair, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove notice duties.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Identity provider and administrator access (break-glass accounts if needed)
2. Site networks and internet
3. Clean endpoints for treasury, the Supply counter, and Home Services dispatch
4. Bank portal access with new tokens for affected users
5. Email, files, and phones (restore deleted mail from the suite backup once available)
6. SFTP server: verify files and keys; resume ACH files after the bank confirms
7. ERP (confirm no unauthorized vendor-master changes)
8. SSO to the loan servicing and distribution systems
9. HRIS and payroll (confirm no direct deposit changes)
10. Integration service, reporting database, board portal

**Validate before reconnecting:** sessions revoked, secrets rotated, admin list approved, and no unexplained changes in the ERP vendor master or HRIS bank details. Tell subsidiary Presidents, affected vendors, and staff when services are back (RC.CO-03).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the subsidiary Presidents (POL-03 requires documentation within 30 days).
- Add weaknesses to the POA&M (P07) with owners and dates (314.4(h)(5)).
- Update the risk register (P01, especially R-001, R-002, R-003, R-006), this runbook, and the notification matrix (314.4(h)(7)).
- Document the event and response (314.4(h)(6)) and keep the records for 6 years under the group retention schedule, in the restricted incident folder.

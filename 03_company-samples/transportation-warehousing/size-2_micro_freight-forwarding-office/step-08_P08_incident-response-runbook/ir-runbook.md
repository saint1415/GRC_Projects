# Incident Response Runbook: Business Email Compromise with Payment Diversion and Client Record Exposure

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (freight forwarding and customs brokerage office) |
| Tier / Vertical | Micro / Transportation and Warehousing |
| Incident type | Business email compromise (BEC): an attacker takes over a staff mailbox (or imitates a payee's domain), changes a carrier's or overseas agent's bank details, diverts a wire, and reads or copies client records in the mailbox and the Client Records Archive |
| Why this incident | Adapted from the registry default (ransomware on a terminal operating system), which does not fit an office with no terminal systems. BEC is the company's top risk (P01 R-001, R-003), a near-miss happened in 2026-05, and it triggers the 72-hour CBP notice in 19 CFR 111.21(b). Ransomware (R-002) follows the same first steps; section 9 lists what changes |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; POL-02 B.10 (payment call-back) |
| Runbook owner | Office and Compliance Manager (Security Coordinator) |
| Approved | 2026-08-31 by the owner |
| Last tested | Not yet. First tabletop with the MSP and the bank's fraud process due 2026-11-30 (POAM-008) |

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The MSP does the technical work; the bank tries to recover money; the cyber insurer supplies breach counsel and forensics. The Office and Compliance Manager runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office and Compliance Manager | Owner | Cell phone (numbers on the printed contact card) |
| Decision maker (money, notices, client communication) | Owner | Entry Supervisor | Cell phone |
| Wire recall | Accounting Specialist | Owner | Bank fraud line (number on the contact card, not from email) |
| Technical response | MSP incident line (emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel | Insurer panel counsel | Customs counsel for CBP questions | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm | n/a | Engaged by breach counsel |
| Customs platform vendor | Vendor support line | Vendor account manager | Phone; security contact in the contract |
| Law enforcement | FBI Internet Crime Complaint Center (IC3) | Local FBI field office | ic3.gov; numbers in the binder |

**Notification chain in the first hour:** staff member → Office and Compliance Manager → (at the same time) bank fraud line (Accounting Specialist or owner), MSP incident line, and owner → insurer breach hotline (owner) → breach counsel and forensics (through the insurer). The customs platform vendor is called if there is any sign the platform was reached from the compromised account.

**Out-of-band first.** Assume the attacker reads company email. Coordinate by phone and text, using the printed contact card. Never use phone numbers or links from the suspicious email.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the office and at the owner's and the Office and Compliance Manager's homes: this runbook, contact card, notification matrix, the CBP notice template, and the importer number data map
- [ ] Payment call-back and dual approval for new or changed payees in force (POL-02 B.10). **Gap until 2026-09-30 (R-001)**
- [ ] External-sender tag and impersonation protection on (SI-8). **Gap until POAM-012 closes**
- [ ] Suite alerts for risky sign-ins, new forwarding rules, and mass downloads routed to the Office and Compliance Manager and the MSP (SI-4, AU-6). **Gap until POAM-010 closes**
- [ ] Named accounts with MFA everywhere; entries@ converted (IA-2(1)). **Gap until POAM-001 and POAM-003 close**
- [ ] Suite audit logs kept at least 1 year (AU-11), so the investigation can see the attacker's activity
- [ ] Importer number data map current (POL-04 4.4), so the CBP notice can list compromised numbers within 72 hours

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A carrier, agent, or client says a payment never arrived | Phone call or email | Accounting Specialist checks the payee details on the last wire; if changed, **call the bank fraud line now** |
| Email asking to change bank details, or an "urgent" payment request from the owner | Staff report | Do not pay. Call the payee at a number on file. Report to the Office and Compliance Manager |
| A staff member entered a password on a strange page, or approved an MFA prompt they did not start | Staff report | MSP resets the password, signs out all sessions, and removes unknown MFA methods |
| New inbox rule that forwards or hides mail; sign-in from an unexpected country | Suite alert; MSP | MSP disables the account; Office and Compliance Manager opens an incident |
| Clients report emails from the company that staff did not send | Client call | Declare an incident |

**Declare a BEC incident** when any company mailbox shows sign-ins, rules, or sent mail the user did not make, or when any payment went to an account the payee does not recognize.

**Write down two times.** (1) **Discovery of a records breach**: when the company first knows that an attacker accessed a mailbox or files holding client customs records. This starts the **72-hour CBP clock** (111.21(b)). (2) **Florida determination**: when the company determines, or has reason to believe, that personal information was accessed. This starts the **30-day Florida clock** (501.171(4)(a)). The two can be the same day.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Call the bank fraud line** and ask for a recall of every wire sent to the changed account; ask the bank to contact the receiving bank | Accounting Specialist or owner | Recall request reference number written down |
| 2. Call the MSP incident line: disable the compromised account, reset its password, sign out all sessions, remove attacker MFA methods, inbox rules, and app consents | Office and Compliance Manager; MSP | MSP confirms |
| 3. Call the insurer's breach hotline (the social engineering coverage depends on prompt notice) | Owner | Claim number issued; counsel assigned |
| 4. Hold all outgoing wires until each pending payee is confirmed by call-back | Owner; Accounting Specialist | Hold in place |
| 5. Warn every carrier, agent, and client the attacker may have emailed, by phone: "do not act on bank-detail changes from us" | Owner; Export and Forwarding Coordinator | Calls logged |
| 6. Open the incident log: timeline, actions, who, when | Office and Compliance Manager | Log started |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Scope of access.** Which mailboxes, which files, which SaaS? Sources: suite sign-in and audit logs, mailbox audit, file access logs, customs platform audit trail, bank portal history.
2. **Initial access.** Find the phishing message or password reuse. Search all mailboxes for the same message and remove it.
3. **Preserve evidence.** Export suite logs before they age out (the plan default is shorter than one year, AU-11). Keep a chain-of-custody record.
4. **Records exposed.** Which client records did the attacker read, download, or forward? List every **importer identification number** in those records, using the data map (POL-04 4.4). Separate individuals' Social Security numbers (Florida personal information) from business EINs. **This list drives both the CBP and the Florida notices.**
5. **Money.** Which payments used attacker-supplied details? Amounts, dates, receiving banks.
6. **Customs platform.** Ask the vendor to check for sign-ins or exports from the company's accounts during the attack window. The platform uses its own MFA, so it is usually unaffected.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's sender addresses and look-alike domains in the suite (MSP).
2. Reset passwords for every user who shared a password with the compromised account, and every shared portal password the compromised user knew.
3. Remove attacker-added forwarding rules, delegates, app consents, and MFA methods on every mailbox, not only the first one.
4. Turn on impersonation protection and the external-sender tag if not already on.
5. If the MSP's remote tool or accounts may be involved, the owner asks the insurer's forensic firm to confirm eradication and requires the MSP to show its own investigation results (P01 R-014).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice before it goes out, but **no review may push the CBP notice past 72 hours**.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Bank fraud line; MSP; insurer | Accounting Specialist; Office and Compliance Manager; owner |
| Day 0 | IC3 complaint with wire details (also supports the bank's recall) | Owner |
| Day 0-1 | Staff briefing: what happened, call-back for every payment, refer client and agent questions to the owner | Office and Compliance Manager |
| **Within 72 hours of discovery** | **Email to the CBP Security Operations Center (cbpsoc@cbp.dhs.gov)** using the template: company name and filer code, broker license number, contact, what happened, dates, records involved, and the known compromised importer identification numbers. Send what is known; do not wait for forensics | Owner (signs); Office and Compliance Manager (prepares) |
| Within 72 hours | Affected clients told by phone, then in writing (client terms; CTPAT clients' security contacts) | Owner |
| **Within 10 business days of the CBP notice** | Updated list of additional compromised importer identification numbers to the CBP Security Operations Center; any later information within 72 hours of finding it | Office and Compliance Manager |
| Within 30 days of determination | Florida individual notices (individual importers and employees whose Social Security numbers or account credentials were accessed), unless counsel documents a no-harm determination under 501.171(4)(c), with the copy to the Department; Department notice if 500 or more Floridians (unlikely at this size) | Owner and counsel |
| As required | Other states' notices for affected individuals who live outside Florida | Counsel |

**Inbound notices.** If the MSP, the backup service, or a SaaS vendor is where the breach happened, it must notify the company within 10 days of its determination (501.171(6)(a)). The company still sends the CBP and Florida notices.

**Not applicable here (see the matrix):** the USCG maritime incident report (33 CFR 6.16-1) applies to incidents involving or endangering vessels and waterfront facilities, not an office mailbox; TSA, SEC, and FAR reports do not apply; CIRCIA is not in effect.

**Extortion.** If the attacker threatens to publish client data for payment, no payment is made without the owner's approval, counsel and insurer advice, and an OFAC sanctions check (POL-03 4.8).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Internet and office network: firewall checked; MSP and firewall credentials changed if exposed
2. Clean endpoints for the brokers and Entry Writers: MSP scans the compromised user's computer and reimages it if forensics finds malware
3. Customs platform: vendor confirms the company's accounts are clean; entries and ISFs resume
4. Email: compromised mailbox restored to the user with new credentials; any deleted mail restored from the suite backup (SYS-08)
5. Payments: resume only with call-back and dual approval for every changed payee; Accounting Specialist reviews the last 90 days of payee changes
6. Carrier and terminal portals: all shared passwords changed
7. Client Records Archive: any files changed or deleted by the attacker restored from SYS-08; staff check key folders

**Tell clients, agents, and carriers when normal operations resume** (RC.CO), and repeat the "we never change bank details by email" message.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, counsel, and the bank. Written summary within 30 days (POL-03 4.11).
- Update the risk register (P01, especially R-001, R-003, R-004), the POA&M (P07), training (share the attacker's emails as examples), and this runbook.
- Keep the incident log, CBP notices, breach determination, notices, bank and IC3 records, and the forensic report for at least 5 years (POL-02 A.7).

## 9. If the incident is ransomware instead (R-002)
The same chain applies, with these changes: unplug affected computers but leave them on; the MSP pauses suite sync and protects the backup console before anything else; restore the archive from SYS-08 only after forensics confirms which versions predate the attack. If client files were copied, the CBP 72-hour notice and the Florida clock apply exactly as in section 6.

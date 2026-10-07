# Incident Response Runbook: Email and ATS Takeover Exposing Contractor and Candidate PII

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent recruiter, sole proprietorship) |
| Tier / Vertical | Sole Proprietorship / Administrative and Support and Waste Management and Remediation Services |
| Incident type | The registry's "payroll and HR system breach exposing worker PII", adapted to this business: an attacker takes over the owner's email (SYS-02), uses it to reset and export the ATS (SYS-01), searches for SSNs and IDs, and sends the back-office partner a forged contractor bank-change form. The owner runs no payroll; the partner's payroll is the target, reached through the owner's mailbox |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 sections 6.6 and 10 |
| Owner and approver | Owner-recruiter, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT support technician due 2026-09-30 (POAM-006) |

Keep a printed copy at home and in the laptop bag. Assume the attacker can read the mailbox: **do not use email to coordinate the response until it is secured. Use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Back-office partner payroll desk and account manager | **Stop any bank change** received from the owner's address; hold the next pay change for every contractor; confirm the partner's own systems are clean | Hour 0 |
| On-call IT support technician | Help lock out the attacker, check the laptop and phone, save logs | Hour 0-1 |
| Breach counsel (privacy attorney) | Privilege, breach determination, Florida and other-state notices, extortion questions | Hours 0-4 |
| Professional liability carrier | No standalone cyber policy. Ask whether a cyber endorsement applies *before* hiring any outside firm | Hours 0-4 |
| Email provider and ATS vendor support | Account recovery; sign-in, mailbox-rule, and export logs before they roll over | Hours 1-4 |
| FBI IC3 (online report) | Business email compromise and attempted payroll diversion; supports fund recovery | Day 1 |
| Clients whose information was in the mailbox or ATS | Warn of possible phishing that uses real job orders; contract notice "promptly" | Hours 8-24, after counsel |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: a new-sign-in alert the owner did not cause; a forwarding or deletion rule the owner did not create; an ATS password-reset email the owner did not request; a contact asking about an email the owner did not send; the partner asking about a bank change; an ATS export the owner did not run. **Write down the date and time.** Florida's 30-day clocks run from "determination of the breach or reason to believe a breach occurred" (Fla. Stat. 501.171(3)-(4)), so the time the owner first had reason to believe matters.

| Severity | Meaning |
|---|---|
| 1 | Attacker had mailbox or ATS access, or a bank change was sent to the partner |
| 2 | Credentials entered on a phishing page, no sign of attacker access yet |
| 3 | Phishing message received and reported, nothing entered |

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. **Call the partner** and say: "Do not act on any bank or address change from my email. Hold changes for all my contractors until I call back." Note the name and time | Partner confirmed hold |
| 2. From the laptop (or the phone if the laptop is suspect), reset the email password, **sign out all sessions**, remove unknown MFA methods and app passwords, switch MFA to the authenticator app, and delete any forwarding or deletion rules | Only the owner's devices are signed in |
| 3. Reset the ATS password and turn on ATS MFA; end other ATS sessions; same for the partner portal and the e-signature service | Sessions revoked |
| 4. Call the IT technician, then counsel | Both engaged |
| 5. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

Do not delete phishing messages, rules, or sent items yet: they are evidence. Do not reply to the attacker.

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Save the logs first.** Export the email sign-in history and audit of mailbox rules, and ask the ATS vendor for its sign-in and export log for the last 90 days. These logs roll over; this step is time-critical.
2. **What did the attacker see?** With the IT technician, check what the attacker searched, opened, downloaded, or forwarded. Use the 2026-07-23 search results as the baseline: until the purge (POAM-002) is complete, assume the mailbox holds SSNs and IDs for 77 people (66 in Florida).
3. **What left the ATS?** Confirm whether an export or bulk download ran, and which fields it held (names, contact details, resumes, any ID attachments).
4. **What was sent?** Review sent items and the deleted folder for messages to the partner, clients, and candidates. List every recipient who may have received a forged message.
5. **Devices.** The technician checks the laptop and phone for malware or a malicious browser extension. If either is suspect, work from the other.
6. **Preserve evidence.** Save exported logs, screenshots, and the phishing message to an encrypted folder, with a chain-of-custody note (who, when, where stored).

## 5. Hours 8-24: keep working and prepare notices (RS.CO, RC.RP)
- **Business:** contractor pay is safe once the partner's hold is in place; clients approve time directly. Call clients with open searches from the printed continuity sheet if email is still unreliable (P05, BP-01 and BP-02).
- **Count affected people.** For each person whose data the attacker could reach, record the data elements against the Fla. Stat. 501.171(1)(g) list and the state of residence. Names and resumes alone are not personal information under 501.171; a name with an SSN, ID number, or account credentials is.
- **Breach determination with counsel:** record the date of determination. Decide on individual notice or, only with counsel's support, a written no-harm determination (501.171(4)(c)).
- **Warn people.** With counsel, tell contractors and candidates to expect no bank-change or document requests from the owner's email, and to call the owner if they receive one.
- **Extortion:** not paid without counsel's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Immediately (hour 0) | Partner payroll desk | Any sign of contact with the partner or a forged bank change |
| Within 30 days of determination | Florida individual notice (15-day extension only with written good cause to the Department within the 30 days) | Florida residents with a 501.171(1)(g) element affected |
| Within 30 days of determination | Florida Department of Legal Affairs | 500 or more Floridians (not expected today) |
| Without unreasonable delay | Consumer reporting agencies | More than 1,000 people notified at one time (not expected) |
| Varies | Each state where affected individuals reside | 11 people in 6 other states today |
| Promptly | Clients | Client information involved |

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, internet, email, partner portal, a clean device, ATS, then accounting and e-signature. Before closing, confirm on the restored mailbox that no forwarding rules, unknown MFA methods, app passwords, or connected apps remain. Close the incident when notices are sent, the partner confirms no diverted pay is outstanding, and the purge is verified. Within 30 days of closing, record lessons learned, update P01 (R-001 to R-004), P07, and this runbook, and keep all incident records for at least 5 years (POL-01 8.8).

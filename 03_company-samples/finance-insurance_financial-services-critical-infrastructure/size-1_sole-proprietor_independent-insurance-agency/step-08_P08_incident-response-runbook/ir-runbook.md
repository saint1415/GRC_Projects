# Incident Response Runbook: Business Email Compromise and Premium Payment Fraud

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent insurance agency) |
| Tier / Vertical | Sole Proprietorship / Financial Services |
| Incident type | Takeover of the agency mailbox (SYS-02), theft of attachments with client personal information, and fake invoices that redirect agency-billed premiums. Adapted from the vertical's "compromise of payment processing environment": at this size, the agency's payment environment is email invoicing into the premium trust account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 sections 8 and 11 |
| Owner and approver | Owner-agent, 2026-09-14 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-10-15 (P01 R-011) |

Keep a printed copy in the office and in the evacuation kit. Assume the attacker is reading the mailbox: **do not discuss the incident by email. Use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Bank fraud line (premium trust and operating accounts) | Stop or recall outgoing transfers; freeze new payees; confirm no account changes | Hour 0 if money moved; otherwise hour 1 |
| E&O insurer claims line | The cyber and social engineering endorsement requires notice as soon as practicable and use of its panel vendors (breach counsel, forensics) **before** hiring anyone | Hours 0-2 |
| Breach counsel (from the E&O panel) | Privilege, breach determination under 501.171, notices, insurer contract duties | Hours 1-4 |
| On-call IT consultant | Lock down the mailbox, preserve logs, check other accounts and devices | Hour 0 |
| Agency-billed clients with open invoices | Warn them by phone, at the number on file, not to pay any invoice with new bank details | Hours 0-4 |
| Affected insurers (addenda contacts) | 72-hour contractual notice; warn of fraudulent change requests on their policies | Within 72 hours of discovery |
| Bookkeeper | Watch the trust account for unexpected activity; confirm the bookkeeper's own email is not the source | Hours 1-4 |
| FBI IC3 (online complaint) | Voluntary report; supports any attempt to stop a transfer | Same day |
| Emergency servicing agent | Client service if the owner is tied up (P05) | As needed |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: a client asks about an invoice or bank details the owner did not send; a forwarding or inbox rule the owner did not create; a sign-in alert from an unknown place; sent items the owner did not write; an insurer or bank fraud call; a password reset the owner did not request. **Write down the date and time.** That time starts the insurers' 72-hour clock (discovery). Florida's 30-day clock runs from determination of the breach "or reason to believe a breach occurred" (Fla. Stat. 501.171(4)(a)), which may be the same day.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. If any client or the agency has sent money to a new account, call the bank fraud line first and ask for a recall; tell the client to call their bank too | Recall requested; reference numbers in the log |
| 2. From the phone (not the laptop), sign out all email sessions, change the email password, switch MFA to the authenticator app or security key, and remove the phone number as a sign-in method | Only the owner's devices are signed in |
| 3. Delete every forwarding and inbox rule the owner did not create, after photographing each one (destination address, conditions) | Rules recorded and removed; outside forwarding blocked |
| 4. Change the passwords of any account that reused the email password (P07 found 6 reused); check the AMS and bank sign-in history | Reused passwords changed |
| 5. Call the IT consultant, then the E&O claims line | Both engaged |
| 6. Start the paper incident log: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Who received fake invoices?** Search sent items and the deleted folder for messages the owner did not write. Phone every agency-billed client at the number on file, starting with open invoices; repeat the "we never change bank details by email" message (POL-01 8.1).
2. **What could the attacker read?** Export the email sign-in history and mailbox audit records before the 30-day window rolls over. List the attachments in the mailbox (applications, ID copies, loss runs, payroll, bank draft forms) and the clients they belong to. This list decides how many people are affected.
3. **Did it spread?** Check the AMS activity log, insurer portals, the bank, and the e-signature account for sign-ins from the same place. The IT consultant scans the laptop for an information stealer, because saved browser passwords may be the source.
4. **Preserve evidence.** Save logs, rule screenshots, fake invoices with full headers, and bank correspondence, with a chain-of-custody note (who, when, where stored). Do not delete the attacker's sent messages until counsel agrees.
5. **Lookalike domain?** If fake invoices came from a lookalike domain instead of the real mailbox, report it to the registrar and the email provider, and still check the real mailbox (steps above).

## 5. Hours 8-24: keep serving clients and prepare notices (RS.CO, RC.RP)
- **Clients:** the AMS and insurer portals keep working from the phone or a clean laptop. Send nothing with bank details by email until the mailbox is confirmed clean.
- **Insurers:** give each affected insurer its contractual notice (within 72 hours of discovery), and agree with it who notifies its policyholders.
- **Breach determination:** counsel and the owner decide whether unencrypted personal information was accessed (501.171(1)(a)). If counsel concludes notice is not required, the determination is written, kept 5 years, and sent to the Department of Legal Affairs within 30 days (501.171(4)(c)).
- **Count affected people and where they live.** Florida 500 or more: Department notice. More than 1,000 notified: consumer reporting agencies. Any of the about 60 seasonal residents: that state's law. This sets which rows of `notification-matrix.csv` apply.
- **Ransom or extortion:** none paid without counsel's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 72 hours of discovery | Each affected insurer (data security addendum) | Insurer policyholders' information involved |
| As soon as practicable | E&O insurer | Any suspected incident or fraud loss |
| Within 10 days of determination | Insurer, by statute, where the agency is its third-party agent (501.171(6)) | Backstop to the 72-hour clock |
| Within 30 days of determination | Florida individuals (15 more days only with written good cause); Department of Legal Affairs if 500+ Floridians (no extension) | Breach of Florida residents' personal information |
| Without unreasonable delay | Consumer reporting agencies | More than 1,000 individuals notified |
| Varies | Other states' residents and regulators | Seasonal residents affected |

**The FTC notice in 16 CFR 314.4(j) does not apply** to an insurance agency (P03 section 1.1). Plan to the insurers' 72 hours first; it is the shortest clock.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and second factors, internet, a clean device, the AMS, insurer portals, then banking and invoicing (with the callback rule). Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-005), P07, and this runbook, and keep all incident records for 5 years (POL-01 9.6).

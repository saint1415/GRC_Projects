# Incident Response Runbook: Business Email Compromise and Fraudulent Wire

| Field | Value |
|---|---|
| Organization | Cris Santos Company (state-registered investment adviser) |
| Tier / Vertical | Sole Proprietorship / Finance and Insurance |
| Incident type | Business email compromise and a fraudulent wire: a client's email account (or the owner's) is used to request a wire from a client's custodial account to an account the attacker controls, and the request is submitted |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 sections 7.6 and 10. A written plan is not required at this size (16 CFR 314.6 exempts 314.4(h)); the owner keeps one because Florida's 30-day notice clock needs it |
| Owner and approver | Owner-adviser, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-09-30 (POAM-007) |

Keep a printed copy in the home office and in the owner's bag. Assume any email account involved is in the attacker's hands: **use the phone, the custodian portal, and this paper copy. Never reply to the suspicious thread.**

## 1. Example
A client's real email address sends a friendly message in an existing thread: the client is closing on a condo and needs $48,500 wired to the title company today. The owner sends the custodian's third-party wire form for e-signature to that address. It comes back signed within the hour, the owner submits it, and the custodian releases the wire. Two days later the client calls about an unexpected withdrawal. The client's email account had been taken over. The attacker knew the account balance, which raises the question of whether the **owner's** mailbox (no MFA until 2026-09-15, with an unknown forwarding rule found on 2026-07-15) was also compromised.

## 2. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Custodian adviser fraud line | Recall the wire; freeze or restrict the client account; flag the receiving account | **Minute 0** |
| The client, at the phone number on file (never a number from an email) | Confirm what the client did and did not request; tell the client to secure their email and call their bank | Minutes 0-30 |
| On-call IT consultant | Check the owner's mailbox, devices, and SaaS accounts; preserve evidence | Hour 0-1 |
| Breach and securities counsel | Privilege, breach determination, notices, repayment questions, OFR questions | Hours 0-4 |
| FBI (IC3 online report) | A fast report can help freeze funds; supports any law enforcement delay | Hours 1-4 |
| Errors and omissions insurer, **if coverage exists** | Check for a social engineering or cyber endorsement *before* hiring any outside firm | Hours 0-4 |
| Compliance consultant | Records to keep; whether any OFR filing or Form ADV update is needed | Day 1 |
| Email suite and CRM vendor support | Lock accounts; export sign-in and audit logs before they roll over (30 days) | Hours 1-4 |

Contact numbers are kept on the printed copy only, not in this file.

## 3. Declare (Detect)
Declare an incident when any of these happens: a client disputes a withdrawal or transfer; the custodian flags a money movement; a request arrives to send money to a new account or to change bank instructions and the callback fails; a mailbox forwarding rule or sign-in the owner does not recognize appears; a client reports that "you" emailed them. **Write down the date and time.** That time starts two clocks: the FTC treats a notification event as discovered on the first day it is known to the adviser (16 CFR 314.4(j)(2)), and Florida's 30-day clock runs from determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(4)).

## 4. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Call the custodian's fraud line: ask for an immediate recall of the wire and a hold on the client's account. Write down the case number and the person's name | Recall requested; account restricted |
| 2. Call the client at the number on file. Confirm the request was not theirs. Ask them to change their email password, turn on MFA, and check their email forwarding rules | Client informed |
| 3. From the phone, sign in to the owner's email: change the password, sign out all sessions, turn on MFA if still off, and delete any forwarding or inbox rule the owner did not create | Only the owner's phone is signed in; rules clean |
| 4. Do the same for the CRM, portfolio platform, and e-signature service | All sessions revoked |
| 5. Call the IT consultant, then counsel | Both engaged |
| 6. Start the incident log on paper: times, what was seen, each action, who was called | Log started |

## 5. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Whose mailbox was used?** With the IT consultant, export the owner's email sign-in history, mailbox rules, and connected apps. Look for sign-ins from unknown places, rules that forward or hide messages, and messages sent that the owner did not write. If the owner's mailbox was accessed, **every client's information in it may have been seen**.
2. **What could the attacker see?** List the client statements, onboarding forms (SSNs, ID images), and account numbers in the owner's mailbox and shared folders. This list decides who must be notified.
3. **Other accounts.** Check the CRM and portfolio platform audit logs for exports or unusual access. Check the e-signature audit trail for the signed form (IP address and time).
4. **Other money movement.** Ask the custodian for every money movement request on all client accounts in the past 60 days, and call each client whose request came by email.
5. **Preserve evidence.** Save the email thread with full headers, the e-signature audit trail, the custodian case number, and the log exports, with a note of who saved each item and when. Delete nothing until counsel agrees.

## 6. Hours 8-24: keep clients safe and prepare notices (RS.CO, RC.RP)
- **Stop the same trick.** No money movement for any client without a callback to the number on file (POL-01 7.6). Send a short letter by **mail** to all clients: the adviser will always call before moving money and will never ask for bank details by email.
- **Breach determination.** With counsel, decide whether personal information was accessed (Fla. Stat. 501.171(1) definition: for example, name with an account number and a password or access code, or with an SSN). If the owner's mailbox was accessed, assume it was.
- **Count affected people and their states of residence.** This sets which rows of `notification-matrix.csv` apply. The FTC notice needs 500 or more consumers; Florida's Department notice needs 500 or more Floridians. Today the adviser holds records on about 160 consumers, so neither is expected, but count every time.
- **Notice method.** Florida allows notice by mail or email to the address on file. **Use mail** for any client whose email may be compromised.
- **Money.** Counsel advises on whether the adviser should make the client whole; do not promise anything in writing until then.

## 7. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Immediately | Custodian fraud line (recall) | Any suspected fraudulent money movement |
| Within 30 days of determination | Florida individual notice (mail or email to the address on file); Department of Legal Affairs if 500 or more Floridians | Personal information of Florida residents accessed |
| Within 30 days of determination | Written no-harm determination to the Department, if the adviser relies on it | Counsel concludes no identity theft or financial harm is likely |
| Within 30 days of discovery | FTC online form | 500 or more consumers' unencrypted customer information acquired |
| Varies | Other states' notices | Affected clients who live outside Florida |

**The 2026-07-15 forwarding rule** is logged as a suspected incident. Counsel reviewed it on 2026-08-20 and concluded that, because the sign-in history showed no foreign access and no client reported fraud, no notice was required on the facts known; the conclusion and the reasons are kept with the incident log for 5 years (POL-01 8.9). It is reopened if any client reports a suspicious request.

## 8. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, internet, a clean device, the custodian portal, CRM and email, then the portfolio platform. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002), P07, and this runbook, and keep all incident records for at least 5 years.

# Incident Response Runbook: Suspected Intrusion into a Client's Control Systems Through the Consultant's Access

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent utility engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Utilities |
| Incident type | Registry default "Intrusion into distribution control systems (OT)", adapted: the business runs no OT, so the incident is an attempt to reach **Client B's control systems through the owner's access**. The owner's email credentials are phished; the attacker finds the Client B gateway user name in the mailbox, tries the reused password, and the owner's phone receives an MFA push for a Client B session the owner did not start |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 (10.2 and 10.3 set the 24-hour and immediate client notices) |
| Owner and approver | Owner-engineer, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-09-30 (POAM-007) |

Keep a printed copy at the home office and in the field bag. Assume the email account and the laptop browser are in the attacker's hands: **use the phone for calls and this paper copy for steps.** The client owns its control systems and decides what happens inside them. The owner's job is to cut off the path, tell the client fast, and give it the facts.

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| **Client B system operations desk (24x7)** | Disable the owner's gateway account; check for session attempts and anything that got through. VAA-B (4) requires an immediate report | **Minute 0**, before anything else |
| On-call IT technician (NDA) | Help lock the email account; check the laptop; preserve logs | Hour 0-1 |
| Insurer breach response hotline (cyber endorsement, $100,000 sublimit) | Opens the claim; assigns breach counsel and, if needed, a forensic firm. Call **before** hiring anyone, or costs may not be covered | Hours 0-4 |
| Breach counsel (through the insurer) | Privilege; client notice wording; Florida notice decision | Hours 2-8 |
| Client B compliance contact | Written incident notice under VAA-B (5); Client B decides its own CIP-003-9 Section 4 and DOE-417 steps | Within 24 h of discovery |
| Client A security contact | Written notice under SSA-A (5), because the mailbox held Client A BCSI copies (P03 G-007) | Within 24 h of discovery |
| Email and file suite provider support | Help with account recovery if the attacker changed recovery settings | As needed |
| Phone carrier | Add a port-out and SIM change lock; the SMS codes and Client B push go to this phone | Hour 1 |
| Client C and Client D project managers | Their project files are in the suite; tell them if the log shows access | Day 1 |
| FERC CEII Coordinator | Only if CEII was exposed (it is kept off email; confirm) | Promptly, if it applies |
| FBI (IC3 online report) and CISA | Voluntary reports; useful to the clients and the insurer | Day 1 |

Contact numbers are on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare this incident when any of these happens: an MFA push or prompt for Client B or the suite that the owner did not start; a suite alert of a new sign-in or a new forwarding rule; a client says it received an odd email from the owner; Client B reports a session request the owner did not make. **Write down the date and time.** That is the discovery time for every 24-hour client clock (SSA-A (5), VAA-B (5)) and the start of the incident log.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. **Deny the push.** Never approve it, even to make it stop | Push denied |
| 2. **Call Client B's operations desk** from the phone: "an MFA push I did not start, for my gateway account". Ask them to disable the account and check the gateway for attempts. Note the name and time | Client B confirms the account is disabled |
| 3. From the phone (not the laptop), change the suite password, sign out all sessions, check that the recovery phone and email are still the owner's, delete any forwarding rules or connected apps the owner did not add, and switch MFA from SMS to the authenticator app | Only the owner's phone is signed in |
| 4. Change every password that matched the phished one (the reuse is how the attacker reached the gateway). Use the password manager | No reused password left |
| 5. Call the IT technician, then the insurer hotline | Both engaged |
| 6. Start the paper incident log: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What did the attacker see?** Export the suite sign-in history and file activity log before it rolls over. List the messages and files opened from unknown places. Check for the Client B gateway user name, Client A BCSI copies, the drafter's W-9 email, and any CEII (CEII should only be in the encrypted archive on the laptop).
2. **What did the attacker send?** Check sent items and deleted items for phishing sent from the owner's account to clients or the drafter. Warn anyone who received it.
3. **Is the laptop clean?** The IT technician runs a full scan and checks the browser for saved passwords and extensions. **No connection to any client system** from this laptop until the technician and Client B agree it is clean.
4. **Client B side.** Give Client B the times of the pushes, the sign-in locations from the suite log, and any other accounts that used the same password. Client B looks at its own gateway and network. Do not try to investigate Client B systems yourself.
5. **Preserve evidence.** Save the log exports, screenshots of the push prompts, and the phishing email (as an attachment) to the owner-only folder, with a note of who saved what and when. Delete nothing until counsel agrees.

## 5. Hours 8-24: notices and keeping work going (RS.CO, RC.RP)
- **Client B written notice** (VAA-B (5)) and **Client A written notice** (SSA-A (5)) within 24 hours of discovery: what happened, when, what the attacker could see, what has been done, and a contact. Cooperate with their questions. **Each client decides** whether this is a Reportable Cyber Security Incident under its own CIP program, whether to notify the E-ISAC, and whether a DOE-417 criterion is met. Do not make that call for them.
- **Personal information.** If the log shows the drafter's W-9 email was opened, counsel decides on notice under Fla. Stat. 501.171(4) (no later than 30 days after determination). One person is affected, so no Department notice (500 or more).
- **CEII.** If any CEII was exposed, report it to FERC promptly (NDA under 18 CFR 388.113(h)(2)).
- **Ransom or extortion:** not paid without the insurer's and counsel's advice and an OFAC sanctions check.
- **Work:** use the phone and the Client A portal (which has its own MFA) for urgent client contact. Field work for Client B waits until Client B re-enables a new account. Planning studies continue offline on the laptop once it is cleared.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Immediately | Phone report to Client B operations desk (VAA-B (4)) | Any suspected compromise of the gateway credentials |
| Within 24 hours of discovery | Written notice to Client B (VAA-B (5)) and Client A (SSA-A (5)) | Incident may affect their systems or information |
| Promptly | FERC CEII Coordinator | Any unauthorized disclosure of CEII |
| No later than 30 days after determination | Affected Florida individuals (Fla. Stat. 501.171(4)) | Personal information (the W-9) accessed |
| Per policy terms | Insurer claim | Any suspected incident |

The business itself has no NERC, DOE-417, or E-ISAC filing duty. Its 24-hour notices are what let the clients meet theirs.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, client contact, a clean device, software and settings, project files, then accounting. Ask Client B for a new gateway account only after the password manager, app-based MFA, and a clean (or new field) laptop are in place. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-003, R-013), P07, and this runbook, and keep all incident records for 6 years (POL-01 8.9).

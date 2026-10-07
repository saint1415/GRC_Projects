# Incident Response Runbook: Unauthorized Access to a Client's Spillway and Turbine Control Systems Through the Consultant's Account

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent dam safety engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Dams |
| Incident type | Someone other than the owner uses the owner's Client A gateway account to reach the view-only HMI screens and historian for Client A's spillway gates and units, most likely with a password or session token stolen from the laptop browser by information-stealing malware. The business runs no control system of its own |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner-engineer, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-09-30 (POAM-007) |

Keep a printed copy in the home office and in the field bag. Assume the laptop and anything its browser could reach are in the attacker's hands: **use the phone, the tablet, and this paper copy.**

**Whose incident is it?** The control systems, the gateway logs, and every FERC report about the dam belong to **Client A**. The owner's job is to cut off the path through the owner's side, tell clients fast, protect CEII, and give Client A the facts it needs. The owner never contacts FERC about Client A's dam unless Client A asks.

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Client A OT on-call line, then its Compliance and Security Coordinator | Confirm the account is disabled and the session is closed; ask Client A to keep its gateway logs; agree who tells FERC about Client A's CEII | Hour 0 |
| On-call IT technician (NDA) | Isolate the laptop, preserve evidence, check the phone and tablet | Hour 0-1 |
| Attorney (the owner's business attorney) | Contract notices, CEII report wording, insurer notice, any extortion demand | Hours 1-4 |
| Professional liability carrier | Notice of circumstances (no cyber policy; the policy excludes cyber costs) | Day 1 |
| Client B Chief Dam Safety Engineer | The laptop browser also held the Client B platform password | Within 24 hours |
| FERC CEII Coordinator | Only if upstream project CEII may have been disclosed (section 4, step 4) | Promptly once known |
| Signing certificate authority | Revoke the digital signing certificate if it was on the laptop | Hours 8-24 |
| FBI (IC3 online report) or CISA | Voluntary report, coordinated with Client A | Day 1 |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare this incident when any of these happens: Client A reports a gateway session the owner did not start; the phone shows a gateway MFA prompt the owner did not start; the suite or password manager reports a sign-in the owner did not make; the antivirus reports credential-stealing malware; anyone presents files that came from the laptop. **Write down the date and time.** The 24-hour clocks in CSCA-A (7) and GRS-B (3) start at discovery.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Do not open the gateway or any client system. Ask Client A to confirm the owner's account is disabled and the session ended, and to keep its gateway and HMI logs | Client A confirms; time written down |
| 2. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** and do not sign in to anything from it | Laptop offline, still on |
| 3. From the phone: change the suite password, sign out all sessions, check MFA methods and forwarding rules; change the accounting SaaS and Client B platform passwords; ask Client A to reset the portal and gateway credentials | Only the phone is signed in |
| 4. Call the IT technician, then the attorney | Both engaged |
| 5. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What did Client A see?** Get from Client A, in writing if possible: session start and end times, source network, screens viewed, and any blocked actions. The account is view-only, so no gate or unit command should have been possible; Client A confirms gate positions and unit status are normal and decides whether more checks are needed.
2. **What was on the laptop?** With the technician: which passwords and sessions the browser held (gateway, Client A portal, Client B platform, suite), whether the CEII container was open while the malware ran, and which client files sat in the Downloads folder.
3. **Other accounts.** Export the suite sign-in and file activity history. Ask Client B for its platform access log for the past 30 days.
4. **CEII.** If the container was open or any CEII copy may have been taken: report the upstream project CEII to FERC's CEII Coordinator promptly (388.113(h)(2)), and tell Client A about its own CEII so Client A can decide how FERC is told.
5. **Preserve evidence.** The technician images the laptop disk and saves the browser profile and antivirus logs, with a chain-of-custody note (who, when, where stored). No wiping until the attorney agrees.

## 5. Hours 8-24: notices and keeping work going (RS.CO, RC.RP)
- **Client A written notice (by hour 24):** what happened on the owner's side, what was exposed, what was done, and the next update time. Client A then decides whether its event is a security incident under 18 CFR 12.3(b)(4)(xi) to report to the Regional Engineer under 12.10(a) (as soon as practicable, preferably within 72 hours) and to its FERC Regional Office under Security Program Rev. 3A 3.2 (usually within one working day). The owner answers Client A's questions the same day.
- **Client B written notice (by hour 24):** the platform password was in the browser; say whether the access log shows misuse.
- **Signing certificate:** if it was in the laptop store, ask the certificate authority to revoke it and issue a new one on a hardware token (P01 R-013). Tell clients that any report sealed after the compromise time must be verified with the owner.
- **Work:** email from the tablet over the phone hotspot. No gateway work until Client A re-enables the account after its own review. Field work continues with paper forms.
- **Laptop:** do not clean and reuse. The technician reinstalls it from clean media with a standard daily account, the password manager, and encryption, after the evidence is saved.
- **Ransom or extortion:** not paid without the attorney's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of discovery | Client A (CSCA-A (7)); Client B (GRS-B (3)) | Always for Client A; Client B if its password or data may be exposed |
| Promptly | FERC CEII Coordinator (388.113(h)(2)) | Upstream project CEII may have been disclosed |
| Within 30 days of determination | Field assistant (Fla. Stat. 501.171(4)) | The W-9 copy was accessed |
| Client A's decision | 12.10(a) report to the Regional Engineer (preferably within 72 hours); Rev. 3A report to the FERC Regional Office (usually within one working day) | Client A's duty, supported by the owner's 24-hour notice |

**Plan to the shortest clock.** The owner's 24-hour notice to Client A is what lets Client A meet its own FERC timelines.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: phone and authenticator, internet, the suite from a clean device, client contact, a clean laptop, then Client A access when Client A agrees. Give Client A a written statement of the rebuild before it re-enables the account. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-009, R-013), P07, and this runbook, and keep all incident records for at least 6 years (POL-01 8.11).

# Incident Response Runbook: Ransomware on the Consultant's Laptop and Synced Files

| Field | Value |
|---|---|
| Organization | Cris Santos Company (pipeline integrity engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Energy |
| Incident type | Ransomware on the engineering laptop that encrypts local and synced cloud files and steals client data (including Client A's SSI working copies) and subcontractor W-9s, while a Client A portal session may be open |
| Why not the registry default | The registry default is "ransomware on business IT forcing precautionary pipeline shutdown". The consultant operates no pipeline and has no access to any client's operational technology. Whether a client isolates systems or takes operational precautions is the client's decision. The consultant's job is to give Client A the facts it needs within 24 hours (`../00_company-facts.md` section 5) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Engineer-owner, 2026-09-11 |
| Last tested | Not yet. Walkthrough with the IT support contractor due 2026-09-30 (POAM-009) |

Keep a printed copy and the contact sheet in the home office, and the contacts in the phone. Assume the laptop and the suite account are in the attacker's hands: **use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Insurer breach hotline (E&O cyber endorsement) | Panel breach counsel and forensics; coverage depends on calling first | Hour 0-1 |
| Client A security contact (24-hour line) | **Contract clock: 24 hours from discovery.** Client A decides whether to cut the consultant's portal access and what to check on its side. Client A reports to CISA under its own directive if its systems are affected | Hour 0-2, and no later than hour 24 |
| On-call IT support contractor | Isolate the laptop, preserve evidence, check the phone and network. Never given SSI | Hour 0-2 |
| Productivity suite provider support | Lock the account, list sessions, help restore file versions | Hour 1-2 |
| Accounting SaaS provider support | Check for sign-ins and bank-detail changes; lock the account | Hour 1-4 |
| Client B contract manager; Client C utility director | Client B contract clock: 72 hours. Client C: without delay | Hours 4-24 |
| TSA, coordinated with Client A | Report released SSI promptly (49 CFR 1520.9(c)) | Once SSI theft is likely; same day as the Client A call |
| Peer pipeline integrity engineer | Urgent client findings while the owner is tied up (P05 BP-01), once the arrangement is approved | As needed |
| FBI (IC3 online report) | Voluntary; supports OFAC mitigation if payment is ever considered | Day 1 |

Contact numbers are kept on the printed sheet and in the phone only, not in this file.

## 2. Declare (Detect)
Declare a ransomware incident when any of these happens: a ransom note or renamed files on the laptop; the suite shows mass file changes or deletions; the antivirus reports ransomware; someone claims to have client data; the suite or accounting provider warns of a sign-in the owner did not make. **Write down the date and time.** That time starts the Client A 24-hour clock and the Client B 72-hour clock. The Florida 30-day clock starts when a breach of subcontractor personal information is determined (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** (memory may hold evidence). Do not pay or reply to the attacker | Laptop offline, still on |
| 2. From the phone, pause file sync in the suite web console, change the suite password, sign out all sessions, and check MFA methods and forwarding rules | Only the owner's phone is signed in; sync paused |
| 3. From the phone, change the accounting SaaS password and check bank details and recent sign-ins | Accounting account secured |
| 4. Call the insurer hotline, then the Client A security contact. Tell Client A the laptop had portal access so it can disable the account and review its logs | Both called; time recorded |
| 5. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Which client data was on the laptop or in synced folders?** List by client and project. This list decides which client notices apply and what each client needs to know.
2. **Was SSI exposed?** Check whether the SSI folder was synced and whether the laptop held working copies. If SSI was on the laptop when it was compromised, treat it as released to unauthorized persons and agree with Client A how TSA is informed (1520.9(c)).
3. **Was subcontractor personal information exposed?** W-9s should be only in the accounting SaaS (POL-01 8.10). Check the file account and the laptop for stray copies.
4. **Client portal check.** Ask Client A to confirm the portal account is disabled and to share what its logs show for that account.
5. **Preserve evidence.** The forensics firm from the insurer panel (or the IT support contractor, if the insurer agrees) images the laptop and exports the suite activity log, with a chain-of-custody note (who, when, where stored). No wiping until counsel agrees.

## 5. Hours 8-24: keep client work moving and prepare notices (RS.CO, RC.RP)
- **Urgent findings (P05 BP-01):** if any client is waiting on an urgent ILI finding, call that client's integrity engineer from the phone and agree how to deliver it from a clean device or the client's portal.
- **Client A written notice before hour 24:** what happened, when it was found, which Client A data and SSI may be affected, the portal account status, and the next update time.
- **Files:** restore synced files from suite version history to a point before encryption, from a clean device, with the provider's help. Use the encrypted backup drive only after the forensics firm confirms it was disconnected and clean.
- **Laptop:** do not decrypt and reuse. Reinstall from clean media or replace it, with encryption, a standard daily account, and MFA on every account, after evidence is saved.
- **Breach decision for W-9 data:** with counsel, decide whether a breach of personal information occurred and record the determination date. That date starts the Florida 30-day clock.
- **Ransom:** not paid without counsel's advice and an OFAC sanctions check. Paying does not remove any client or legal notice duty if data was taken.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of discovery | Client A security contact (addendum s.6) | Always for this incident |
| Promptly | TSA, coordinated with Client A (49 CFR 1520.9(c)) | SSI likely released |
| Within 72 hours of discovery | Client B (NDA) | Client B data affected |
| Without delay | Client C | Client C data affected |
| Within 30 days of determination | Affected subcontractors (Fla. Stat. 501.171(4)) | W-9 data accessed |

**Plan to the shortest clock.** Client A's 24 hours runs out long before any statutory deadline. Client A's own CISA report under SD Pipeline-2021-01G Section II.C is due as soon as practicable and no later than 72 hours after Client A identifies a cybersecurity incident, so a late call from the consultant can push Client A against its own deadline.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: phone and MFA, internet, read access to client data, email and files, a clean laptop with the engineering software, local working files, then accounting. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-003, R-008), P07, and this runbook, give Client A a closing report, and keep all incident records at least 5 years (POL-01 8.10).

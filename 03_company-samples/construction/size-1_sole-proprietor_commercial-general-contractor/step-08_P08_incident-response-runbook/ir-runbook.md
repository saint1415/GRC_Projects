# Incident Response Runbook: Business Email Compromise Redirecting Progress Payments

| Field | Value |
|---|---|
| Organization | Cris Santos Company (commercial and institutional building general contractor) |
| Tier / Vertical | Sole Proprietorship / Construction |
| Incident type | Business email compromise (BEC) that redirects progress payments |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 (incident response) and 7.6 to 7.8 (payments) |
| Owner and approver | Owner (incident commander), 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-09-30 (POAM-007) |

Keep a printed copy in the truck and the home office. Assume the attacker is reading company email: **use the phone, call numbers from signed contracts, and work from this paper copy.**

## The three variants
| Variant | What happens | Money at risk |
|---|---|---|
| **A. Client pays the attacker** | A phishing page captures the owner's email password and text-message code. The attacker reads the mailbox, hides replies with an inbox rule, and sends a client "updated remittance instructions" just before pay app week | One pay app, typically $10,000 to $25,000 |
| **B. Owner pays the attacker** | A spoofed or hacked subcontractor mailbox asks the owner to change its bank account "before Friday's payment" (the March 2026 near miss) | One subcontractor payment, typically $3,000 to $15,000 |
| **C. Federal EFT change** | The attacker gets into SAM and changes the company's EFT information, so the FC-1 payment goes elsewhere. Under FAR 52.232-33(e)(2) the loss may fall on the company | One FC-1 payment |

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Bank fraud line (number on the back of the bank card, never from an email) | Recall the payment; hold new payees; watch the account | Minute 0 |
| The client's or subcontractor's contact, at the number in the signed contract | Stop any further payment to the new account; client calls its own bank | Hour 0-1 |
| On-call IT technician | Help lock the mailbox, check the laptop and router, save evidence | Hour 0-2 |
| FBI IC3 (www.ic3.gov) | Complaint "as soon as possible, regardless of the amount"; may help freeze funds | Hour 0-4 |
| Business attorney, and a breach attorney through the state bar referral service if personal information was exposed | Who bears the loss; Florida notice decision | Day 0-1 |
| Insurance agent | No cyber or social engineering coverage today; ask whether any policy responds | Day 0-1 |
| FC-1 Contracting Officer and paying office | Variant C, or if a VA payment or FC-1 subcontractor payment is affected | Day 0-1 |
| Standby general contractor | Keep jobsites supervised while the owner deals with the incident (P05) | As needed |

Phone numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a BEC incident when any of these happens:
- a client or subcontractor asks about a bank change the owner did not make;
- an expected client payment has not arrived 2 business days after its due date, and the client says it paid;
- a subcontractor says it was not paid after the owner sent payment;
- the monthly check (POL-01 7.8) finds an inbox rule, forwarding address, or sign-in the owner did not make;
- a bank-change request fails call-back (variant B attempt; log it even if no money moved);
- SAM sends a notice of a change the owner did not make.

**Write down two times:** when the owner first knew something was wrong, and later, when the owner determines (or has reason to believe) that personal information was accessed. Florida's 30-day clock runs from that second time (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. **Call the bank fraud line and request a recall** of any payment that may be diverted. For variant A, phone the client and ask it to call its own bank at once | Recall reference number written down |
| 2. Tell the bank to hold any new payee and pause scheduled ACH payments | Hold confirmed |
| 3. From the phone: change the email password, sign out all sessions, delete unknown inbox and forwarding rules, remove unknown sign-in methods | Only the owner's phone is signed in |
| 4. Change the passwords for SYS-01, SYS-02, and SAM, and check their recent sign-ins | Done and noted |
| 5. Phone every client with a pay app in the last 60 days and every subcontractor paid in the last 30 days, at the numbers in the contracts: "Do not pay to any new bank details" | Call list complete |
| 6. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **How did they get in?** With the IT technician, find the phishing email and check whether a sign-in from an unfamiliar place came right after a successful text-code sign-in.
2. **What could they read?** Search the mailbox and file storage for:
   - subcontractors' W-9 forms with Social Security numbers (Florida personal information);
   - the owner's own email address and password (also Florida personal information, 501.171(1)(g));
   - FC-1 drawings and pay apps (FCI: no notice duty under FAR 52.204-21, but record it for the CMMC scope);
   - anything marked CUI (none expected; P03 G-018).
3. **Who else got email from the attacker?** Check sent items and deleted items for messages to other clients and subcontractors.
4. **Save evidence before it rolls off:** email sign-in history, inbox rules, the fake remittance message with full headers, bank confirmations. Save to the business file storage with the date.
5. **Laptop and router.** The IT technician checks the laptop for malware and the router for changed settings (the router default password was found in P07).

## 5. Hours 8-24: keep the jobs running and prepare notices (RS.CO, RC.RP)
- **Jobs:** current plan sets are in the truck; RFIs and daily notes go by phone and paper (P05 BP-03).
- **Real payments continue.** Pay real subcontractors after call-back verification. On FC-1, the 7-day prompt payment clock still runs from receipt of the Government's payment (FAR 52.232-27(c)). Not paying invites stop-work and, on private jobs, liens.
- **Variant C:** correct SAM, then phone the FC-1 Contracting Officer and paying office (FAR 52.232-33).
- **IC3 complaint** filed with the recall reference and the receiving bank details.
- **Personal information decision** (with counsel): were W-9 forms or credentials accessed? If yes, the Florida notice clock is running.
- **Re-secure email** with a security key, then remove text-message codes (POAM-001).

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Immediately | Bank recall; client and subcontractor calls; IC3 | Any diverted payment |
| Immediately | SAM correction; Contracting Officer and paying office | Variant C |
| Within 7 days of the Government's payment | Pay the real FC-1 subcontractor | Diverted FC-1 subcontractor payment |
| Within 30 days of determination | Florida individual notice (W-9 subcontractors, any account holders) | Personal information accessed |
| Within 72 hours of discovery | DoD report (DFARS 252.204-7012(c)) | Not applicable today; no covered defense information |

**Plan to the shorter clock.** Do not wait for the funds recovery to finish before making the personal information decision.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: phone and second factors, internet, SYS-01, email, a clean laptop, bank and accounting, then the federal portals. For BEC, "restored" means **verified**: every bank change in the last 90 days re-confirmed by call-back, and a remittance confirmation call to each client for the next two pay app cycles. If the owner holds Final Level 1 (Self) by then, confirm every Level 1 requirement is still met before the next affirmation. Within 30 days of closing, record lessons learned, update P01 (R-001 to R-004), P07, and this runbook, and keep all records for 6 years (POL-01 8.7).

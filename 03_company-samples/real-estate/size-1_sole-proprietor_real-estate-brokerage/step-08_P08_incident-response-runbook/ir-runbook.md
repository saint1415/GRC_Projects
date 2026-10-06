# Incident Response Runbook: Business Email Compromise Targeting Closing Funds

| Field | Value |
|---|---|
| Organization | Cris Santos Company (residential real estate brokerage) |
| Tier / Vertical | Sole Proprietorship / Real Estate and Rental and Leasing |
| Incident type | Business email compromise (BEC). **Main case:** the owner's mailbox is taken over and a buyer is sent altered closing wire instructions that appear to come from the title company. **Variant:** a buyer's earnest money deposit meant for the brokerage's escrow account goes to a criminal account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Broker-owner, 2026-09-15 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-10-31 (P01 R-013). The May 2026 near miss is recorded as the first log entry |

Keep a printed copy in the home office and in the car. Assume the mailbox is being read by the attacker: **use the phone and this paper copy, never email, to talk about the incident.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| The buyer (number from the contract, not from any email) | Tell them to call **their own bank's** wire or fraud department now and ask for a recall | Minute 0 |
| Title company or closing attorney (number from their own website or the contract) | Stop the closing from relying on the wrong wire; alert their bank; check other parties | Minutes 0-15 |
| Escrow bank fraud desk (variant, or any outgoing escrow payment) | Recall request and hold; report the fraudulent receiving account | Minutes 0-15 |
| On-call IT technician | Lock the mailbox, remove rules, preserve logs, check the laptop and phone | Hour 0-1 |
| Legal counsel (real estate and privacy) | Florida notices, Commission notice, client communications | Hours 1-4 |
| Professional liability insurer | Claim notice **before** hiring outside firms; confirm whether funds transfer fraud is covered | Hours 1-4 |
| FBI IC3 (www.ic3.gov) | Complaint with full banking details; may help freeze funds | Same day |
| Backup broker (POL-01 11.2) | Take over other open transactions if the owner is tied up | As needed |

Contact numbers are kept on the printed copy only, not in this file. **Gap:** the bank fraud desk number and the insurer claims line are not yet confirmed (due 2026-10-31).

## 2. Declare (Detect)
Declare a BEC incident when any of these happens:
- A buyer, seller, or title company asks about new, changed, or "updated" wire instructions.
- A buyer says funds were sent but the title company (or the escrow bank) has not received them.
- A deposit verification request (r. 61J2-14.008(2)(b)) comes back unconfirmed.
- The email provider alerts on a new forwarding rule or an unusual sign-in, or messages appear in Sent that the owner did not write.
- The owner or the coordinator typed a password into a page that then looked wrong.

**Write down the date and time**, and who first knew (the owner, the coordinator, or a client). Florida's 30-day clock runs from the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(4)(a)).

## 3. First hour: stop the money, then the mailbox (RS.MI)
| Step | Done when |
|---|---|
| 1. Call the buyer at the contract number. **Tell them not to send any more money**, and if a wire went out, to call their bank's wire department now for a recall and a hold harmless or indemnity letter. Stay on the line or call back within 15 minutes | Buyer gives the bank's reference number |
| 2. Call the title company at an independently found number: give them the fraudulent account details by phone and ask them to alert their bank and hold the closing file | Title company contact name logged |
| 3. If escrow funds were sent out or were due in: call the escrow bank's fraud desk, request a recall or a watch, and report the fraudulent receiving account | Bank reference number logged |
| 4. From the phone (not the laptop), reset the email password, sign out all sessions, remove every forwarding and inbox rule the owner did not create, and remove unknown app connections. Do the same for the platform | Only the owner's devices are signed in |
| 5. Tell the coordinator by phone to stop using email for the brokerage until told otherwise | Coordinator confirms |
| 6. Start the incident log on paper: time, what was seen, each action, who was called, reference numbers | Log started |

Once the receiving bank has accepted the payment order, a recall works only if that bank agrees (Fla. Stat. 670.211), and funds are often moved out within hours. That is why the bank calls come before anything else.

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **How did they get in?** With the IT technician, export the email sign-in history and rule changes **today** (provider retention is limited). Was it the owner's account, the coordinator's use of it, or a look-alike domain with no takeover at all?
2. **Which other deals are at risk?** List every open transaction whose emails were in the mailbox. Call every buyer, seller, and title company on them at contract numbers: no instructions will ever come by email; confirm anything by calling.
3. **What personal information was exposed?** List the clients whose driver license images, bank statements, or screening reports were in the mailbox or its forwarded copies, and each person's state of residence. This list drives section 6.
4. **Devices.** The technician checks the laptop and phone for malware and replaces text codes with a security key before the mailbox is used again.
5. **Preserve evidence.** Keep the fraudulent emails with full headers, the wire records, and the log exports, with a note of who saved them and where.

## 5. Hours 8-24: keep closings safe and prepare notices (RS.CO, RC.RP)
- **Closings:** resume only through a verified channel. Wire instructions go through the platform's secure sharing and are confirmed by a phone call the client makes to the title company's published number. Postpone any closing that cannot be verified; tell the lender so the rate lock can be extended.
- **Escrow (variant):** if a buyer's deposit never reached the escrow account and the seller and buyer both claim the funds or the deal, the owner has a conflicting demand. Notify the Florida Real Estate Commission in writing within 15 business days and start a settlement procedure within 30 business days (r. 61J2-10.032(1)). Do not cover a missing deposit with other clients' escrowed funds.
- **Breach determination:** with counsel, decide whether personal information of Florida residents was accessed. A mailbox takeover always exposes the account's email address and password, and usually stored driver license images. If counsel documents a no-harm determination instead, keep it 5 years and send it to the Department of Legal Affairs within 30 days (501.171(4)(c)).
- **Insurance:** give the insurer the facts and reference numbers; follow its instructions on outside firms.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Minutes | Bank recall (buyer's bank and, for the variant, the escrow bank) | Any misdirected wire |
| Same day | IC3 complaint; insurer notice | Any attempt or loss |
| Within 15 business days | Florida Real Estate Commission | Conflicting demands or good-faith doubt over escrowed funds |
| Within 30 days of determination | Florida individual notice; Department of Legal Affairs if 500 or more Floridians (unlikely, about 260 in all records) | Personal information of Florida residents accessed |
| Per each state's law | Other states' notices | Affected clients outside Florida |

The FTC Safeguards Rule notice (16 CFR 314.4(j)) does **not** apply: the brokerage is not a financial institution (P03 section 1.1).

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner identity and phone, the verified phone channel, banking, email (clean, owner-only), then the platform. Within 30 days of closing the incident, record lessons learned, update P01 (R-001 to R-004), P07, and this runbook, record the funds outcome (amount recalled, amount lost, insurance claim), and keep all incident records for at least 5 years (POL-01 8.8).

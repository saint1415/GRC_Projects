# Incident Response Runbook: Card Skimming Through the Online Store

| Field | Value |
|---|---|
| Organization | Cris Santos Company (corner grocery with online and phone ordering) |
| Tier / Vertical | Sole Proprietorship / Retail Trade |
| Incident type | Payment card data compromise through e-commerce skimming, adapted to a redirect checkout: an attacker takes over the online store administrator account and adds a script that shows shoppers a fake card form before sending them on to the processor's real hosted payment page. The terminal and the processor's systems are not affected |
| Why this incident | It is the path to card data that P01 rates highest (R-001, with R-004 as the way in) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner, 2026-09-04 |
| Last tested | Not yet. Walkthrough with the outside IT helper due 2026-09-30 (P01 R-013) |

Keep a printed copy at the register and at home. Assume the email account and the online store are in the attacker's hands: **use the phone's cellular data and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Payment processor, merchant risk or fraud line | **The merchant agreement requires notice within 24 hours of suspicion.** The processor may open a card brand case and tell you what evidence to keep | Hours 0-4, and never later than hour 24 |
| Website builder support | Lock the account, list recent logins and setting changes, restore the checkout pages | Hours 0-2 |
| Outside IT helper | Check the laptop and phone, help collect screenshots and logs | Hours 1-4 |
| Breach counsel (Florida data breach attorney; ask the processor or the state bar referral service if none is on file) | Decide whether this is a breach under Fla. Stat. 501.171, who must be told, and what to say | Hours 4-24 |
| FBI IC3 online report; local police report | Record of the crime; supports a law enforcement delay if one is requested | Day 1 |
| Cyber insurer | **None.** The business owner's policy has no data breach coverage. All costs are out of pocket | n/a |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a suspected card data compromise when any of these happens: the processor sends a fraud or common point of purchase alert; two or more online customers report fraud on cards they used here; a customer says the payment page looked different or asked for card details twice; the website builder emails about a login or setting change the owner did not make; the monthly check (POL-01 7.7) finds an unknown script, add-on, or checkout change. **Write down the date and time.** That is when the 24-hour processor clock starts. Florida's 30-day clock runs from the determination of a breach or reason to believe a breach occurred (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. From the phone, on cellular data, change the email password, sign out all sessions, and turn on MFA if still off | Only the owner's phone is signed in to email |
| 2. Change the online store password, turn on MFA, and sign out all other sessions | Attacker locked out |
| 3. **Before removing anything**, take screenshots of the custom code setting, the add-on list, the checkout settings, and the store activity log | Evidence saved to the phone and printed |
| 4. Turn on the online store's "pause orders" or maintenance setting so no more shoppers reach checkout. Do **not** delete the store | Checkout closed |
| 5. Call the processor's fraud line; give the time of discovery and what was seen. Write down the case number and the name of the person | Processor notified |
| 6. Start the paper incident log: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **When did it start?** With website builder support, find the first unknown login and the date the script or setting was added. Orders from that date until checkout was paused are the **exposure window**.
2. **Who was exposed?** Export the list of online orders in the window (name, email, address, order date). Every customer who reached checkout is presumed affected. Keep the list only on the processor or website builder systems or on paper in the locked drawer, not on the shared laptop.
3. **What was taken?** Ask the processor to confirm whether the fake form sent data anywhere and whether its own hosted page was untouched. A fake card form usually captures the card number, expiration date, security code, and name.
4. **Remove the attack.** After screenshots, website builder support removes the script or setting and confirms the checkout redirect goes only to the processor's page. Remove any add-on the owner does not recognize.
5. **Check the way in.** The outside IT helper checks the laptop and phone for malware and saved-password theft. Change the passwords of every account that shared the old password.
6. **In the store:** keep selling. The terminal is not affected. Do not take card numbers by phone during the incident; ask phone-order customers to pay at delivery on the terminal.

## 5. Hours 8-24: decide and prepare notices (RS.CO, RC.RP)
- **Breach determination with counsel.** Under Fla. Stat. 501.171(1)(g), a name with a card number and its security code is personal information; captured by an attacker's form, it is very likely a breach of security. A no-notice determination under 501.171(4)(c) is unlikely for card data with security codes, and if made must be written, kept 5 years, and sent to the Department within 30 days.
- **Count affected customers and their states of residence.** This sets which rows of `notification-matrix.csv` apply. Most will be Florida residents; check each address.
- **Draft the customer notice** (counsel reviews): date range, what was taken (card details entered at checkout), what the store did, that customers should ask their card issuer for a new card, and how to reach the owner (501.171(4)(e)). Send by email or mail to the address in the store's records (501.171(4)(d)).
- **Processor instructions.** Follow them. The processor may require a forensic investigation; ask about cost before agreeing, since there is no insurance.
- **Extortion:** if anyone demands payment, do not pay or reply without counsel's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of suspicion | Processor (merchant agreement) | Always |
| Within 30 days of determination (plus 15 days only with written good cause to the Department) | Florida residents affected | Breach of personal information |
| Within 30 days of determination | Florida Department of Legal Affairs | 500 or more Floridians (unlikely at this store's volume) |
| Within 10 days, inbound | Website builder or processor to the store | The breach was in their system |
| Varies | Other states' residents | Any affected customer outside Florida |

**Plan to the shorter clock.** The processor's 24 hours runs from suspicion; Florida's 30 days runs from determination. The Department can impose civil penalties for late notice under 501.171(3) or (4), starting at $1,000 a day for the first 30 days (501.171(9)(b)).

## 7. After day 1 (RC.RP, ID.IM)
Reopen online checkout only when MFA is on for the store and email, the checkout redirect is confirmed clean, and no add-on or custom code runs on checkout pages (POL-01 7.7). Restore in P05 order. Within 30 days of closing the incident, record lessons learned; update P01 (R-001, R-004, R-013), P03 rows G-035 and G-028, P07, and this runbook; correct the PCI SAQ answers; and keep all incident records at least 5 years (POL-01 8.8).

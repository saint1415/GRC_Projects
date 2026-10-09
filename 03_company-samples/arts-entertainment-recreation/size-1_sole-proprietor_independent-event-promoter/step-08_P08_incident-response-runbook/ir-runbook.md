# Incident Response Runbook: Ticketing Account Takeover with Card Skimming

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent event promoter with one leased room) |
| Tier / Vertical | Sole Proprietorship / Arts, Entertainment, and Recreation |
| Incident type | Takeover of the owner's ticketing platform and website accounts (reused password, no MFA), followed by a patron export, a changed payout bank account, and a card-skimming script on the website pages that embed the checkout. This adapts the registry scenario "Ticketing platform breach exposing customer and card data" to an SAQ A merchant, which holds no card data of its own (`../00_company-facts.md` section 5) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-09-30 (POAM-006) |

Keep a printed copy in the office and at home. Assume the ticketing and website accounts are in the attacker's hands and the email may be watched: **use the phone and this paper copy, and call rather than email.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Payment processor risk team | Merchant agreement: notice **within 24 hours** of suspecting a card data compromise. Freeze payouts if the bank details changed; card brand steps run through the processor | Hours 0-4 (never later than 24 h) |
| Ticketing vendor support (security line) | Lock the account, end all sessions, restore the payout bank details, pull the activity log and export history | Hour 0-1 |
| Website builder support | Lock the account, list recent page and script changes, restore a clean version | Hour 0-1 |
| On-call IT consultant | Help secure the accounts, save evidence, check the laptop and phone | Hour 0-2 |
| Breach counsel (privacy attorney) | Breach determination, notices to patrons and the Florida Department of Legal Affairs, other states, extortion questions | Hours 2-8 |
| Business bank fraud line | Try to recall any diverted payout; watch for more transfers | Hour 0-2 if payout details changed |
| FBI (IC3 online report) and local police | Report number for the bank and processor; supports a law enforcement delay if needed | Day 1 |
| Marketing assistant and door contractor's lead | Stop using shared logins; do not post or change anything; report what they saw | Hour 0-1 |
| Insurer | No cyber policy (EV-023, EV-030); general liability excludes breach costs (EV-036). Budget for counsel and any forensic firm comes from the business | n/a |

## 2. Declare (Detect)
Declare an incident when any of these happens: an SYS-01 payout-change alert or activity log entry the owner did not make; an unknown user, export, or price change in SYS-01; an unknown script or page change on the website; fans reporting a strange payment form or fraud after buying; the processor reporting a common point of purchase. **Write down the date and time** in the incident log (POL-01 10.2). The processor's 24-hour clock starts at suspicion. Florida's 30-day clock runs from the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. From the phone, secure email first: change the password, sign out all sessions, check forwarding rules and recovery settings | Only the owner's devices signed in |
| 2. Call ticketing vendor support: lock the account, reset the password, turn on MFA, end sessions, check payout bank details and users | Account locked; payout details confirmed or restored |
| 3. Call website builder support: lock the account, reset the password, turn on MFA, list changes in the last 90 days | Account locked |
| 4. **Stop the skimmer:** unpublish the event pages that embed the checkout, or replace the widget with plain links to the vendor's hosted event pages | No owner page carries the checkout |
| 5. Pause any on-sale in progress and post on social: "Buy only through the official event page; we will contact anyone affected" | Fans warned |
| 6. Call the processor's risk team (24-hour term) and, if payouts changed, the bank | Both notified; times logged |
| 7. Start the paper incident log: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **When did it start?** With the vendors and the IT consultant, find the first unknown sign-in, script, or page change. That date opens the window of exposure.
2. **Card data.** Save a copy of the malicious script and the page versions (the website builder's history; screenshots). Ask the processor which card numbers were used on the embedding pages during the window. The owner holds no card numbers; the processor provides them for the card brand steps.
3. **Patron data.** Ask the ticketing vendor for the export history: which files, when, how many records. A patron export (names, emails, phones, orders) is not personal information under Fla. Stat. 501.171(1)(g) by itself, but it fuels phishing of fans and may be covered by other states' laws.
4. **Other changes.** Check prices and smart pricing settings, ticket limits, bot protection, connected apps, and email marketing campaigns for changes.
5. **Preserve evidence.** Do not delete the malicious script history or wipe devices until counsel and the processor agree (POL-01 10.3). If Visa requires a PCI forensic investigator, that investigator must not have served the business in the past 3 years.

## 5. Hours 8-24: keep selling safely and prepare notices (RS.CO, RC.RP)
- **Next show:** run doors from the scanner app with the attendee list downloaded before doors and a printed copy (P05, BP-01). Sell walk-ups only through the vendor's hosted event page.
- **Re-launch sales** only on the vendor's hosted event pages, with MFA on every account and the website's checkout embed removed until the approved script list and page check are in place (POL-01 7.8).
- **Breach determination with counsel:** count affected patrons by state of residence from the processor's card list and the order records. This sets which rows of `notification-matrix.csv` apply.
- **Extortion:** if the attacker demands payment not to publish the export, do not pay without counsel's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of suspicion | Processor risk team (merchant agreement) | Any suspected card data compromise |
| Within 3 calendar days | Visa, through the processor; incident report within 3 days after that | Suspected Visa account data compromise |
| Within 10 days of the vendor's determination (inbound) | Ticketing vendor or processor notice to the owner | Breach of a vendor system |
| Within 30 days of determination | Florida individuals (15 more days only with written good cause to the Department); Department of Legal Affairs if 500 or more Floridians | Card numbers with security codes taken from Florida residents |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 notified at once; other states per their own laws | As counted |

**Plan to the shortest clock.** The processor's 24 hours and Visa's 3 days end long before the Florida 30 days.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, door scanning, internet, ticket sales on hosted pages, email and files, website and marketing, accounting. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-003), P07, and this runbook, and keep the incident records for at least 3 years and any no-notice determination for at least 5 years (POL-01 8.7).

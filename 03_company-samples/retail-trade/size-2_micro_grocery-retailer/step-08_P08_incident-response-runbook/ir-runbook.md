# Incident Response Runbook: Payment Card Data Compromise (E-commerce Skimming)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (neighborhood grocery store with online ordering) |
| Tier / Vertical | Micro / Retail Trade |
| Incident type | Payment card data compromise through e-commerce skimming: a third-party script that the store loads on its online store (for example the chat widget) is altered at its vendor and draws a fake card form over the provider's card fields on the checkout page |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; PCI DSS v4.0.1 Requirement 12.10.1 (N44-45-R01) |
| Runbook owner | Store Manager (Security and PCI Lead) |
| Approved | 2026-08-31 by the Owner |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (P01 R-012) |

## 0. Roles and notification chain (Govern)
The store has 7 people and no IT staff. The provider runs the platform and the card fields; the MSP helps with the office computers, mailboxes, and network; the cyber insurer supplies breach counsel and forensics. The Store Manager runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Store Manager | Owner | Cell phone (numbers on the printed contact card) |
| Decision maker (money, notices, turning off online payments) | Owner | Store Manager | Cell phone |
| Provider notice (24 hours) | Bookkeeper | Owner | Provider merchant risk line and incident email (card in the binder) |
| Technical help (office PC, mailboxes, firewall) | MSP help line | MSP technician's cell | Phone |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel | Insurer panel counsel | n/a | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm; if the provider requires a PCI Forensic Investigator (PFI), the firm must be on the PCI SSC PFI list | n/a | Engaged through counsel |
| Marketing freelancer | Access suspended at the start | n/a | Contacted only by the Store Manager, with counsel's agreement |
| Law enforcement | FBI (IC3) or U.S. Secret Service field office | n/a | Numbers in the binder |

**Notification chain in the first hours:** whoever notices → Store Manager → Owner and Bookkeeper (at the same time) → provider within 24 hours (Bookkeeper) and insurer breach hotline (Owner) → counsel and forensics through the insurer → MSP if mailboxes or office devices may be involved.

**Out-of-band first.** Assume the dashboard, online store, and mailboxes may be compromised. Coordinate by phone and text on personal phones, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the back office and at the Owner's home: this runbook, contact card, notification matrix, provider incident line, insurance policy card, and the P05 recovery order
- [ ] No store-added scripts on the checkout page; approved script list for other pages (CM-7). **Gap until POAM-001 closes**
- [ ] Payment page monitoring alerting the Store Manager by text (SI-7, 11.6.1). **Gap until POAM-002 closes**
- [ ] MFA on every dashboard, online store, and mailbox login above cashier (IA-2(1)). **Gap until POAM-005 closes**
- [ ] Platform alerts for new users, payout changes, and settings changes (SI-4). **Gap until POAM-013 closes**
- [ ] Monthly saved copy of the online store's custom code setting and app list, kept outside the platform (known-good reference)
- [ ] Wallet cards with the 24-hour provider notice term for the Owner, Store Manager, and Bookkeeper (POAM-009)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| New, changed, or unknown script or security header on the checkout page | Payment page monitoring alert (from 2026-11-15) | Store Manager compares with the approved script list within 1 hour; if unexplained, open an incident |
| Provider says the store may be the common point of purchase for card fraud | Provider email or call | Bookkeeper opens the incident at once. **This is a suspected compromise: the 24-hour provider clock has started** |
| Two or more customers in 30 days report card fraud after ordering online | Customer calls, the orders mailbox, online reviews | Log each report; the Store Manager escalates at the second report |
| Custom code, app, or user change that nobody approved | Weekly activity log check; platform alert | Store Manager checks the change log; if unexplained, open an incident |
| The checkout page looks different (an extra card form, a pop-up asking for card details) | Staff testing an order, or a customer | Screenshot it; call the Store Manager |

**Declare an e-skimming incident when** an unauthorized script or change is confirmed on any online store page, or the provider reports a common point of purchase.

**Write down two times.** The **time of suspicion** starts the merchant agreement's 24-hour provider notice. The **time of determination** of a breach (or reason to believe one occurred) starts Florida's 30-day clock (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Capture evidence before changing anything:** save the checkout page as a browser sees it (full capture), copy the text of every script and the custom code setting, note the time, and export the platform activity log | Store Manager | Evidence saved to a restricted folder with a simple chain-of-custody log |
| 2. Suspend the marketing freelancer's login; end all dashboard and online store sessions; change passwords and check MFA for the Owner and Store Manager | Store Manager | Only the Owner and Store Manager can publish |
| 3. **Stop card capture online.** Turn off online card payment: orders become pickup only, paid on a countertop P2PE terminal in the store; pause delivery (P05 BP-02 workaround). Do not wait for the root cause | Store Manager with the Owner's approval | No customer can type a card number on the online store |
| 4. Notify the provider and follow its instructions, including any requirement to use a PFI. **No later than 24 hours after suspicion** | Bookkeeper | Provider reference number in the log |
| 5. Call the insurer's breach hotline; counsel and forensics are assigned | Owner | Claim number issued |
| 6. Ask the provider to confirm its card fields were not altered and to flag cards used online during the suspected window | Bookkeeper | Provider answer in the log |
| 7. Open the incident log: timeline, actions, who, when | Store Manager | Log started |

## 4. Analysis (RS.AN)
Led by the forensic firm through counsel, with the provider and the MSP supplying records.
1. **Window of exposure.** When did the bad script first load, and when was it removed? Sources: the platform activity log, browser captures, monitoring history (once live), and the script vendor's own notice if one exists. Export logs first; default retention may be short.
2. **Entry point.** A compromised script vendor (the chat widget in this scenario), the freelancer's login (password only until POAM-005 closes), a former employee's access, or an installed app.
3. **What was captured.** Usually card number, expiration date, security code, and name and billing address. **Check whether the script also ran on the sign-in page.** It loads on every page, so email addresses and passwords typed during the window may also be exposed; an email address with a password is personal information under Fla. Stat. 501.171(1)(g)1.b.
4. **Who was affected.** List orders paid online during the window from the platform's reports. Count unique cards and customers and **group them by state of residence** using billing addresses. Seasonal residents may live in other states.
5. **What was not affected.** In-store payments on the P2PE terminals and SNAP EBT never touch the online store. Record the evidence for both.
6. **Preserve evidence.** Keep the chain of custody. Do not contact the attacker's collection domain.

## 5. Containment and eradication (RS.MI)
1. Remove the bad script and its vendor from every page; restore the custom code setting from the known-good copy, minus anything not on the approved list.
2. Leave **no** store-added scripts on the checkout page; turn on the provider's checkout script restriction (POAM-001).
3. Change every administrator password; confirm MFA on every login above cashier; remove apps that are not needed.
4. Reset passwords for online customer accounts that signed in during the window, if forensics finds the sign-in page was affected (the provider can force a reset).
5. Confirm with a fresh browser capture that the page matches the approved list. Forensics and the provider must agree before online card payments reopen.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Within 24 hours of suspicion | Provider notice under the merchant agreement; follow provider and card brand instructions | Bookkeeper |
| Day 0 | Insurer notified; counsel and forensics engaged | Owner |
| Day 0-2 | Voluntary report to the FBI (IC3) or the U.S. Secret Service | Store Manager with counsel |
| Day 0-1 | Staff briefing: what happened, online orders are pickup only, what to tell customers, do not discuss outside the store | Store Manager |
| As soon as known | Breach determination under Fla. Stat. 501.171, dated and documented by counsel | Owner and counsel |
| Within 30 days of determination | Notice to affected Florida residents by mail or email; Department of Legal Affairs only if 500 or more Floridians | Owner and counsel |
| Without unreasonable delay | Consumer reporting agencies only if more than 1,000 people are notified at one time | Counsel |
| Per each state's law | Residents of other states and their regulators | Counsel |

**Law enforcement delay.** If a law enforcement agency determines that notice would interfere with a criminal investigation, individual notice is delayed for the period it specifies in a written request (501.171(4)(b)).

**No-notice decision.** Notice to individuals is not required if, after an appropriate investigation and consultation with law enforcement, the store reasonably determines that the breach has not and will not likely result in identity theft or other financial harm. The decision must be in writing, kept for 5 years, and sent to the Department of Legal Affairs within 30 days (501.171(4)(c)). Skimmed card numbers with security codes are used for fraud, so counsel should expect notice to be required.

**No federal shortcut.** Fla. Stat. 501.171(4)(g) lets an entity follow its primary or functional federal regulator's notice rules instead. The store has no such regulator for breach notice, so it follows 501.171 directly.

**Worked example (tabletop).** The altered chat widget script ran for 21 days before a customer called about a fraudulent charge. About 4 online card payments a day gives about 84 orders and, after removing repeat customers, about 75 unique cards: about 72 from Florida residents and 3 from residents of 2 other states. Result: notify the provider within 24 hours of the customer's call being linked to the store; notify the 72 Florida residents within 30 days of determination; **no** Department of Legal Affairs notice (fewer than 500 Floridians) and **no** consumer reporting agency notice (not more than 1,000); check the laws of the 2 other states. If the script also captured sign-ins, add those customers to the count and recheck the thresholds.

**Not applicable:** HIPAA (no pharmacy), the FTC Safeguards Rule notice (the store is not a financial institution under 16 CFR Part 314), SEC Form 8-K (privately held), and CIRCIA (no final rule; reporting is voluntary).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). In-store sales (BP-01) keep running on the P2PE terminals throughout, because in-store card data never touches the online store.
1. Administrator access: all passwords changed and MFA confirmed
2. Online store pages restored with only approved scripts; none on checkout
3. Payment page monitoring live and alerting (or, until POAM-002 closes, a manual browser capture compared each morning)
4. Online card payments reopened (BP-02, RTO 8 hours) after forensics and the provider agree. Until then, pickup only, paid in the store
5. Picking and delivery (BP-03) resume for prepaid orders
6. Customer accounts reset if sign-ins were affected; customers told when online payment is back (RC.CO)

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and counsel; written summary within 30 days (POL-03 4.11).
- Update the risk register (P01 R-001, R-002, R-012), the POA&M (P07), the approved script list, and this runbook.
- Review with the provider whether the store can still check the SAQ A statement on script attacks, or must validate the online channel another way (P03).
- Keep all incident records for at least 3 years (POL-02 A.8), and any no-notice documentation for 5 years.

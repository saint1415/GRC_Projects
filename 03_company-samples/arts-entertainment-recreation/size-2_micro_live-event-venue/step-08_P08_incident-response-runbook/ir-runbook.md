# Incident Response Runbook: Ticketing Channel Breach Exposing Customer and Card Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing; one music club) |
| Tier / Vertical | Micro / Arts, Entertainment, and Recreation |
| Incident type | A reused password opens the shared website administrator login and the Marketing Coordinator's ticketing account; the attacker (a) places a fake payment form over the checkout widget on the website event pages and (b) exports patron records from the ticketing platform |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Venue Manager (Security and Privacy Lead) |
| Approved | 2026-08-31 by the Owner and General Manager |
| Last tested | Not yet. First tabletop with the MSP and a call to the insurer's hotline due 2026-11-30 (POL-03 4.11) |

## How this incident unfolds (the scenario the runbook is built for)
1. The website administrator password is shared by the Owner, the Marketing Coordinator, and the web designer, and the Marketing Coordinator also uses it for her ticketing account. It turns up in an unrelated breach. There is no MFA on either login (P01 R-001, R-002; POAM-003).
2. The attacker signs in to the website builder and adds a script to the event page template. The script hides the ticketing vendor's checkout widget and shows a look-alike payment form. When a patron submits it, the script sends the card number, expiration date, and security code to the attacker, shows "payment failed, please try again", and then loads the real widget. The patron pays normally on the second try.
3. With the same password, the attacker signs in to the ticketing platform as the Marketing Coordinator, whose role can export patron lists, and exports about 47,000 patron records (name, email, phone, billing address, order history). No card numbers are in the export.
4. Nobody checks the website or reviews the ticketing audit log (P03 G-046, G-055), so the script runs through an on-sale and three weeks of sales.
5. Detection comes from outside: patrons complain on social media that they had to pay twice and then saw fraud on their cards, or the acquirer reports the company as a **common point of purchase**.

The ticketing vendor's platform and widget are not breached. **The company's own website and logins are the entry point**, so the company owns this incident. The vendor and the MSP must still help, and they hold much of the evidence.

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The MSP does the technical work on computers, the network, and the suite; the cyber insurer supplies breach counsel and forensics. The Venue Manager runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Venue Manager | Owner and General Manager | Cell phone (numbers on the printed contact card) |
| Decision maker (money, notices, ransom or extortion, pausing sales) | Owner and General Manager | Venue Manager | Cell phone |
| Website containment | Marketing Coordinator with the web designer | Venue Manager | Cell phone; website builder support line |
| Ticketing containment | Box Office and Ticketing Manager | Venue Manager | Cell phone; ticketing vendor priority support line |
| Technical response (computers, network, suite) | MSP incident line (number in the MSP contract) | MSP account technician's cell | Phone only |
| Acquirer and payment partner | Owner | Bookkeeper | Acquirer merchant risk line; payment partner support |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel | Insurer panel counsel | n/a | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm. If Visa requires one, a PCI Forensic Investigator (PFI) that has not served the company in the past 3 years | n/a | Engaged through counsel |
| Law enforcement | FBI field office or IC3; U.S. Secret Service field office | n/a | Numbers in the binder |

**Notification chain in the first hour:** whoever notices → Venue Manager → Owner, Marketing Coordinator, and Box Office and Ticketing Manager (at the same time) → MSP incident line → insurer breach hotline (Owner) → breach counsel and forensics (through the insurer) → acquirer (Owner, within 24 hours of suspicion) → ticketing vendor and website builder support.

**Out-of-band first.** Assume the attacker can read company email. Coordinate by phone and text on personal phones, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the back office and at the Owner's home: this runbook, contact card, notification matrix, the acquirer's merchant risk contact, and the vendors' priority support paths
- [ ] MFA on every ticketing account and on named website logins (POAM-003). **Gap until closed**
- [ ] Approved script list for event pages, weekly page check, and website change alerts (POAM-008). **Gap until closed**
- [ ] Weekly ticketing log check and monthly audit log export (POAM-006). **Gap until closed**
- [ ] Marketing role without patron export rights (POAM-001)
- [ ] Insurer hotline and policy number checked at each renewal; MSP contract amended with a 24-hour incident notice term (R-015)
- [ ] Manual door kit (printed door list, wristbands) in case ticketing access must be locked down on a show night (P05 BP-01)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Common point of purchase or compromise notice | Acquirer or payment partner | **Declare at once.** The 24-hour acquirer clock and Visa's 3-day clock start at suspicion |
| Patrons say they had to pay twice, or report card fraud soon after buying | Social media, box office mailbox, phone | Log each report; two or more in a week, the Venue Manager checks the event page from a clean device |
| Website change alert, or the weekly page check finds a script not on the approved list | Website builder; web designer (after POAM-008) | Marketing Coordinator asks the web designer within 1 hour; if nobody approved it, declare |
| Ticketing alert or weekly check: a bulk export, new user, or sign-in nobody recognizes | Ticketing audit log (after POAM-006) | Confirm with the user by phone; if it was not them, declare |
| An MFA prompt or password reset nobody started | Staff | Reset, sign out all sessions, review the account's actions |
| Vendor reports suspicious activity on the company's accounts | Ticketing vendor or website builder | Declare; ask the vendor for its evidence |

**Declare a ticketing channel breach when** an unapproved script or form is confirmed on a page that hosts the checkout widget, any ticketing or website account is confirmed misused, or the acquirer names the company as a common point of purchase.

**Record two times.** The time of **suspicion** starts the acquirer's 24-hour clock and Visa's 3-day clock. The time the company **determines** that a breach occurred, or has reason to believe one occurred, starts Florida's 30-day clock (Fla. Stat. 501.171(3)-(4)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Capture the event page as patrons see it (browser capture with the network log) from a clean device **before** changing anything, and save the script source | Marketing Coordinator with the Venue Manager | Files saved with the time to the incident folder |
| 2. Export the ticketing audit log, user list, and API token list, and the website's page history (the ticketing log keeps only 90 days) | Box Office and Ticketing Manager; Marketing Coordinator | Exports saved |
| 3. Remove the malicious script and every script not on the approved list. If the page cannot be cleaned quickly, replace the embedded widget with a plain link to the vendor-hosted event page | Marketing Coordinator with the web designer | A second capture shows a clean page |
| 4. Change the website password, give each person a named login with MFA, and sign out all website sessions | Marketing Coordinator | Website builder confirms sessions ended |
| 5. Disable the misused ticketing account; force a password reset and MFA for all venue users; sign out all sessions; revoke API tokens not in use | Box Office and Ticketing Manager | Vendor confirms sessions revoked |
| 6. Call the insurer hotline; engage counsel and forensics through the insurer | Owner | Claim number issued |
| 7. Call the MSP incident line: check the Marketing Coordinator's laptop for password-stealing malware, check suite sign-ins for the attacker's addresses, and reset suite passwords if needed | Venue Manager; MSP | MSP confirms the laptop is isolated and checked |
| 8. Notify the acquirer (within 24 hours of suspicion) and ask how it wants the Visa report and the card data extract handled | Owner | Acquirer case number recorded |
| 9. Open a priority case with the ticketing vendor: ask for its logs on the company's accounts and confirmation that its own widget code was not changed | Box Office and Ticketing Manager | Vendor case number recorded |
| 10. Start the incident log: timeline, actions, who, and when | Venue Manager | Log open |

**If this happens during an on-sale or on a show night:** do not take ticketing offline. Cleaning the page and locking accounts does not stop sales or scanning. If the vendor must suspend the company's accounts, the Venue Manager switches the door to the manual procedure (P05 BP-01) and the door sells for cash.

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP, the web designer, and the ticketing vendor supplying access and logs.
1. **Window of exposure.** Find when the script first appeared and when it was removed (website page history, earlier captures, the web designer's weekly checks once they exist). Every checkout through the website event pages in that window is at risk. The payment partner can list the card numbers used in that window for the acquirer and Visa.
2. **Initial access.** Reused password, phishing, or malware on a laptop? Check the website builder's and ticketing vendor's sign-in records (source addresses, times, devices) and the MSP's findings on the laptop.
3. **What else the attacker did.** Other exports, new users or API tokens, changed refund or payout settings, changed price tiers or fees, changed demand tools settings, other website changes.
4. **Two data sets, two decisions:**
   - **Skimmed card data** (name, card number, expiration date, security code): personal information under Fla. Stat. 501.171(1)(g)1.a.(III). Card brand rules apply.
   - **Patron export** (name, email, phone, address, order history): not personal information under the Florida definition by itself, but other states' definitions differ, and the FTC Act still applies to how the company protected it and what it tells patrons. Counsel decides on notice state by state.
5. **Residency.** Split affected patrons by billing state (about 84% Florida overall) to set the Florida counts (500 or more for the Department; more than 1,000 for consumer reporting agencies) and the list of other states.
6. **Preserve evidence** with chain of custody. Do not delete the attacker's script source, account records, or API tokens until the forensic firm has what it needs.

## 5. Containment and eradication (RS.MI)
1. Keep the event pages free of any script not on the approved list. Scripts return only through change control (POL-02 A.10 and A.11).
2. Block the attacker's collection domain at the venue firewall (MSP) and report it to the website builder and the ticketing vendor.
3. Remove patron export rights from the marketing role; keep no more than 2 ticketing administrators (POL-02 B.2).
4. Change every shared secret the Marketing Coordinator or the web designer knew, and check the suite, the acquirer portal, and the email marketing service for sign-ins from the attacker's addresses.
5. The MSP wipes and rebuilds any laptop with password-stealing malware. Forensics confirms no other persistence (other website users, plugins, API tokens, scheduled exports) before containment is closed.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews every notice before it goes out. Card brand rules are applied through the acquirer; they are not law, but missing them brings card brand assessments.

| When (from the clock that applies) | Action | Owner |
|---|---|---|
| Hour 0 | Insurer notified; counsel and forensics engaged; MSP engaged | Owner; Venue Manager |
| Within 24 hours of suspicion | Acquirer notified (merchant agreement, fictional term) | Owner |
| Within 3 calendar days of suspicion | Compromise event reported to Visa (through the acquirer) | Owner |
| Within 3 calendar days of notifying Visa | Incident report to Visa and the acquirer | Venue Manager and Owner, with forensics |
| Within 3 calendar days of determining the window of exposure | At-risk card numbers provided (the payment partner extracts them) | Owner |
| If Visa requires a PFI | PFI contract; initial report within 5 business days of signing; final report within 10 business days of completion | Owner and counsel |
| Day 0 to 2 | Voluntary report to the FBI (IC3) or the U.S. Secret Service | Venue Manager |
| Day 0 to 2 | Staff and contractor door leads briefed: what happened, what to say to patrons, where to send questions | Venue Manager |
| Within 30 days of determination | Florida individual notices (mail or email); Department of Legal Affairs notice if 500 or more Florida residents | Owner and counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at one time | Counsel |
| Per each state's law | Notices for patrons in other states | Counsel |
| After notices are final | Artists and promoters of affected shows told what happened and what patrons were told | Owner |

**Plan to the shortest clock.** The card brand clocks (24 hours and 3 days) run from suspicion and arrive long before Florida's 30 days. Florida's 30 days can arrive before the forensic report is final. Counsel should decide early whether to ask the Department for 15 more days to notify individuals (Fla. Stat. 501.171(4)(a)), which needs good cause given in writing within the first 30 days; that extension never moves the Department notice.

**Inbound notices.** If the breach happened at the ticketing vendor, the payment partner, or the MSP instead, Florida requires a third-party agent to notify the company within 10 days of its determination (Fla. Stat. 501.171(6)(a)). The company still sends the notices to individuals and the Department.

**What not to say.** No public statement blames the ticketing vendor. The entry point was the company's website and logins.

**Ransom or extortion:** if the attacker threatens to publish the patron export, the decision requires the Owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.9). Paying does not remove any notice duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Event entry: scanners and manifests checked for the next show; manual door kit ready (BP-01)
2. Venue network: attacker domain blocked; staff Wi-Fi password changed (BP-03, BP-05)
3. Online sales: event pages clean (third capture), widget or vendor link working, named website logins with MFA (BP-04)
4. Ticketing platform: all venue users on MFA, export rights removed, tokens reviewed (BP-04, BP-05)
5. Settlement for shows in the window of exposure; chargebacks tracked by the Bookkeeper (BP-06)
6. Patron communications: website notice and emails as counsel approves (BP-08)

**Before declaring recovery:** the website builder and ticketing vendor confirm no unknown users, sessions, plugins, or tokens; weekly page checks match the approved list; the MSP confirms clean laptops. Tell staff and, where counsel approves, patrons when normal service is confirmed (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, the web designer, and counsel. Written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-002, R-005, R-021), the POA&M (P07), the P03 scope decision, and this runbook.
- Expect the acquirer to ask for a new PCI DSS validation, possibly at a stricter level, and consider moving all online sales to vendor-hosted pages so no company page hosts the payment form.
- Keep all incident records, notices, and Florida determination documents for at least 5 years (Fla. Stat. 501.171(4)(c) sets 5 years for a no-notice determination; the company applies the same period to all incident records, POL-02 A.9).

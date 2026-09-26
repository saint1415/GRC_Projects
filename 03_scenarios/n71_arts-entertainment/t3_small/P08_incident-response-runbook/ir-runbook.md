# Incident Response Runbook: Ticketing Platform Breach Exposing Patron and Card Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing) |
| Tier / Vertical | Small / Arts, Entertainment, and Recreation |
| Incident type | Takeover of a venue account on the ticketing platform, followed by (a) an export of patron records and (b) a card-skimming script placed on the vendor-hosted checkout page through marketing settings |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (Information Security Lead) |
| Approved | 2026-08-31 by the General Manager |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-016) |

## How this incident unfolds (the scenario the runbook is built for)
1. A box office supervisor reuses a password that appeared in an unrelated breach. The attacker signs in to the ticketing platform as that supervisor. There is no MFA prompt (P01 R-001; POAM-003).
2. Using the supervisor's admin rights, the attacker runs the patron report and exports about 260,000 patron records (name, email, phone, billing address, order history). No card numbers are in the export.
3. The attacker adds a script to the checkout page through **marketing settings**, disguised as an analytics tag. The script copies what patrons type into the payment form (name, card number, expiration date, security code) and sends it to an attacker server (P01 R-002).
4. Nobody reviews the ticketing audit log or checkout content (P03 G-046, G-055), so the script runs through a busy on-sale week.
5. Detection comes from outside: the acquirer reports that the company is a **common point of purchase** for fraud on cards used at its checkout.

The vendor's platform itself is not breached. **The company's own account and settings are the entry point**, which is why the company, not the vendor, owns this incident. The vendor must still help, and it holds most of the evidence.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | General Manager | Incident line (cell), then the out-of-band group chat on personal phones |
| Ticketing platform containment | Director of Ticketing | Box office manager | Cell; vendor's priority support line and named account manager |
| Checkout content | Marketing Director | Director of Ticketing | Cell |
| Acquirer, card brands, insurer | Controller | General Manager | Acquirer merchant risk line; insurer breach hotline |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Through the insurer hotline |
| Forensics | Forensic firm from the insurer panel. If Visa requires a PFI, a PCI Forensic Investigator that has not worked for the company in the last 3 years | n/a | Through counsel |
| Communications | General Manager | Outside PR (through counsel) | Cell |
| Event-day continuity | Operations Director | Box office manager | Radio and cell |
| Law enforcement | FBI field office or IC3; U.S. Secret Service field office | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read company email. Coordinate on personal phones and the printed contact list in the incident binder in the IT office and the box office.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder: this runbook, contacts, the notification matrix, the acquirer's merchant risk contact, and the vendor's priority support path
- [ ] MFA enforced for all 34 venue users on the ticketing platform (POAM-003). **Gap until closed**
- [ ] No company-added scripts on checkout; vendor alerts on checkout setting changes (POAM-007, POAM-008). **Gap until closed**
- [ ] Ticketing audit log exported to the log service with 12-month retention and alerts (POAM-011, POAM-012). **Gap until closed**
- [ ] Current AOCs from the ticketing vendor and payment partner, and the vendor's incident contact (POAM-019)
- [ ] Forensic firm and counsel confirmed through the insurer panel
- [ ] Manual entry kit at every door (printed manifests, wristbands) in case the platform must be locked down on a show day (P05 BP-01)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Common point of purchase or compromise notice | Acquirer or payment partner | **Declare at once.** The 24-hour acquirer clock and Visa's 3-day clock start at suspicion |
| Alert: checkout or marketing setting changed, or a script not on the approved list | Vendor alert; weekly capture (after POAM-008) | Director of Ticketing and Marketing Director check with the agency within 1 hour; if nobody approved it, declare |
| Alert: new admin, admin sign-in from a new country, or a bulk patron export | Log service (after POAM-011) | Verify with the user by phone; if not them, declare |
| Staff report an MFA prompt or password reset they did not start | Staff | Reset, revoke sessions, review the account's actions |
| Patrons report fraud on cards soon after buying tickets | Guest services, social media | Log each report; three or more in a week, escalate to the IT Manager |
| Vendor reports suspicious activity on the company tenant | Ticketing vendor | Declare; ask the vendor for its evidence package |

**Declare a ticketing platform breach when** any unapproved change to checkout content is confirmed, any venue account is confirmed misused, or the acquirer names the company as a common point of purchase.

**Record the time of suspicion and the time of determination.** Suspicion starts the acquirer's 24-hour clock and Visa's 3-day clock. Determination of a breach (or reason to believe one occurred) starts Florida's 30-day clock (Fla. Stat. 501.171(3)-(4)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Capture the checkout page as patrons see it (browser capture with network log) **before** changing anything, and save the script source | Marketing Director with the IT Manager | Files saved with hashes to the incident folder |
| 2. Export the ticketing audit log, marketing settings history, and user list (the platform keeps only 90 days) | Director of Ticketing | Exports saved with hashes |
| 3. Remove the malicious script and **all** company-added scripts from checkout; lock marketing settings to one named admin | Marketing Director | Second capture shows no company-added scripts |
| 4. Disable the misused account; force password reset and MFA enrollment for all venue users; revoke all sessions; rotate the export API key | Director of Ticketing and IT Manager | Vendor confirms sessions revoked |
| 5. Call the insurer hotline; engage counsel and forensics through the insurer | Controller | Claim number issued |
| 6. Notify the acquirer (within 24 hours of suspicion) and ask how it wants the Visa report and card data extract handled | Controller | Acquirer case number recorded |
| 7. Open a priority case with the ticketing vendor: request its logs, the script's first-seen time, and confirmation that its own code was not changed | Director of Ticketing | Vendor case number recorded |
| 8. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

**If this happens during an on-sale or on a show day:** do not take the platform offline. Removing the script and locking accounts does not stop sales or scanning. If the vendor must suspend the tenant, the Operations Director switches doors to the manual entry procedure (P05).

## 4. Analysis (RS.AN)
1. **Window of exposure.** Find when the script first appeared and when it was removed (vendor records, audit log, earlier captures). Every checkout in that window is at risk. The payment partner can list the card numbers used in that window for the acquirer and Visa.
2. **Initial access.** How was the account taken: reused password, phishing, or the agency's accounts? Check the vendor's sign-in records for the account (source addresses, times, devices).
3. **What else the attacker did.** Other exports, new users, changed payout or refund settings, changed prices, changed bot mitigation settings, API key use from new addresses.
4. **Two data sets, two decisions:**
   - **Skimmed card data** (name, card number, expiration, security code): personal information under Fla. Stat. 501.171(1)(g)1.a.(III). Card brand rules apply.
   - **Patron export** (name, email, phone, address, order history): not personal information under the Florida definition by itself, but other states' definitions differ, and the FTC Act still applies to how the company protected it and what it tells patrons. Counsel decides on notice state by state.
5. **Residency.** Split affected patrons by billing state (about 78% Florida overall) to set the Florida counts (500+ for the Department; more than 1,000 for consumer reporting agencies) and the list of other states.
6. **Preserve evidence** with chain of custody. Do not delete the attacker's account until the forensic firm has what it needs. Do not log in to affected accounts to "look around".

## 5. Containment and eradication (RS.MI)
1. Block the attacker's exfiltration domain at the venue firewall and report it to the vendor so it can block it platform-wide.
2. Keep checkout free of company-added scripts. Any script returns only through change control with the approved list (POL-01 4.12 and 4.13).
3. Reduce ticketing admins to 3 and remove marketing rights from all agency accounts until the agency's own access is reviewed.
4. Replace the export API key with a read-only scoped key stored in the key vault.
5. Reset the passwords of any staff whose credentials appear in the forensic findings, company-wide, and check the identity provider sign-in logs for the same attacker addresses.
6. Forensics confirms no other persistence (other admin users, API keys, scheduled exports, webhooks) before closing containment.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out. Card brand rules are applied through the acquirer; they are not law, but missing them brings assessments.

| When (from the clock that applies) | Action | Owner |
|---|---|---|
| Hour 0 | Insurer notified; counsel and forensics engaged | Controller |
| Within 24 hours of suspicion | Acquirer notified (merchant agreement, fictional term) | Controller |
| Within 3 calendar days of suspicion | Compromise event reported to Visa (through the acquirer) | Controller |
| Within 3 calendar days of notifying Visa | Incident report to Visa and the acquirer | IT Manager and Controller |
| Within 3 calendar days of determining the window of exposure | At-risk card numbers provided (the payment partner extracts them) | Controller |
| If Visa requires a PFI | PFI contract; initial report within 5 business days of signing; final report within 10 business days of completion | Controller and counsel |
| Day 0 to 2 | Voluntary report to the FBI (IC3) or the U.S. Secret Service | IT Manager |
| Day 0 to 5 | Staff briefing: what happened, what to say to patrons, where to send questions | General Manager |
| Within 30 days of determination | Florida individual notices (mail or email); Department of Legal Affairs notice if 500+ Florida residents | General Manager and counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at once | Counsel |
| Per each state's law | Notices for patrons in other states | Counsel |
| After notices are final | Artists and promoters for affected shows told what happened and what patrons were told | General Manager |

**Plan to the shortest clock.** The card brand clocks (24 hours and 3 days) run from suspicion and arrive long before Florida's 30 days. Florida's 30 days can arrive before the forensic report is final. Counsel should decide early whether to ask the Department for the 15 additional days, which requires good cause in writing within the first 30 days.

**What not to say.** No public statement blames the ticketing vendor. The entry point was the company's account.

**Ransom or extortion:** if the attacker threatens to publish the patron export, the decision requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any notice duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Event entry: confirm scanners and manifests work for the next show; manual entry kit ready (BP-01)
2. Venue network and internet (BP-03, BP-04)
3. Ticketing platform: checkout clean (third capture), all venue users on MFA, admins reduced, marketing settings locked (BP-04, BP-05)
4. Box office: back in service; phone orders only on validated P2PE devices once installed (BP-04)
5. Settlement for shows in the window of exposure; chargebacks tracked by the Controller (BP-06)
6. Patron communications: website notice and email as counsel approves (BP-08)

**Validate before declaring recovery:** the vendor confirms no unknown admins, sessions, API keys, or webhooks; weekly checkout captures match the approved list; alerts are running. Tell staff and, where counsel approves, patrons when normal service is confirmed (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-006, R-008, R-026), the POA&M (P07), the P03 scope document, and this runbook.
- Expect the acquirer to ask for a new PCI DSS validation, possibly at a stricter level. Budget for it.
- Retain all incident records, notices, and the Florida determination documents for at least 5 years (Fla. Stat. 501.171(4)(c) sets 5 years for a no-notice determination; the company applies the same period to all incident records).

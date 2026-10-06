# Incident Response Runbook: Ticketing Platform Breach Exposing Patron and Card Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (live event venue operator with ticketing; private equity-backed; three Florida venues) |
| Tier / Vertical | Mid-Market / Arts, Entertainment, and Recreation |
| Incident type | A skimming script published through a compromised marketing agency tag manager account on the website event pages that embed the ticketing checkout form, plus an export of patron records through the agency's local account on the ticketing platform |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-event-day-outage.md` (loss of ticketing and scanning during doors); `notification-matrix.csv`; BIA (P05); venue emergency plans |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Card compromise tabletop with outside counsel and the acquirer relationship manager scheduled 2026-11-04 (POAM-016) |

## How this incident unfolds (the scenario the runbook is built for)
1. A marketing agency staff member receives a phishing email that imitates the tag manager vendor. The attacker captures the agency's tag manager password (a local account with no MFA) and, from the agency's shared password list, the agency's local ticketing account (P01 R-001, R-002).
2. The attacker publishes a new tag labeled as an analytics update. On event pages, it draws a fake payment form over the vendor's embedded checkout frame, captures what the patron types (name, card number, expiration date, security code), shows a "please try again" error, and then reveals the real form. The patron pays normally on the second try.
3. Using the agency's ticketing account, which has the marketing role, the attacker exports a patron segment of about 410,000 records (name, email, phone, billing address, purchase history). No card numbers are in the export.
4. The tag runs for 9 days, including a headliner on-sale. About 21,000 checkouts happen on affected pages in that window.
5. **Detection.** After POAM-010 closes, the payment page monitoring service alerts on the new script within hours. Until then, detection is likely to come from outside: the acquirer reports that the company is a **common point of purchase** for card fraud.

The ticketing vendor's platform and its checkout frame are not breached. **The company's own pages and accounts are the entry point**, which is why the company owns this incident. The vendor and the tag manager vendor must still help, and they hold much of the evidence.

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, business, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, Vice President of Ticketing, Vice President of Marketing and Digital, HR Director, outside breach counsel | Business decisions (pausing on-sales, taking pages offline), external statements, acquirer and card brand strategy, extortion decision (recommendation to the CEO), resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director, security analysts, MSSP, forensic firm or PCI Forensic Investigator (through counsel), ticketing vendor and tag manager vendor contacts | Containment, investigation, eradication, recovery |
| **Venue command** | Vice President of Venue Operations, Director of Safety and Security, the three venue General Managers | Event-day continuity if accounts or platform access must be locked during shows (see the companion runbook) |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Breach and privacy decisions | General Counsel | Outside breach counsel | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | General Counsel | Through the insurer hotline, then direct |
| Acquirer, card brands, QSA | Chief Financial Officer | Controller | Acquirer merchant risk line; card brand contacts through the acquirer |
| Cyber insurer | Carrier breach hotline ($10 million limit, $250,000 retention, $1 million card brand sublimit) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm through counsel. If a card brand requires a PFI: a PCI Forensic Investigator that has not served the company as QSA, advisor, consultant, or monitoring provider in the past 3 years (so not the QSA firm or the MSSP) | n/a | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Payment page and agencies | Vice President of Marketing and Digital | Digital team lead | Cell |
| Ticketing platform | Vice President of Ticketing | Box office operations manager | Vendor priority support line and named account manager |
| Communications | Vice President of Marketing and Digital (through counsel) | Outside crisis PR (through counsel) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | U.S. Secret Service field office (Visa recommends it for card compromises); FBI field office or IC3 | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read agency and company email. The CMT and IRT use a pre-provisioned messaging group on personal phones and printed call trees kept at HQ and each venue.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation where possible. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. A PFI, if required, reports directly to Visa; counsel reviews PFI communications but cannot control them.

## 1. Preparation checks (Identify / Protect)
- [x] EDR on all laptops and PCs with 24x7 MSSP escalation (SI-3; P07 fully satisfied)
- [x] Validated P2PE at box offices and bars (card data there is not exposed by this scenario)
- [ ] Payment page script inventory, two-person publishing, and the monitoring service with alerts to the MSSP (POAM-010, due 2026-10-30). **Gap until closed**
- [ ] Tag manager and all local ticketing accounts on SSO with MFA (POAM-003, due 2026-10-31). **Gap until closed**
- [ ] Ticketing audit log and tag manager history in the SIEM with 12-month retention and alerts for bulk exports and script publishes (POAM-007, POAM-008). **Gap until closed**
- [ ] Current AOCs and incident contacts for the ticketing vendor and payment partner, and an incident clause for the tag manager vendor and the agencies (POAM-021)
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-15
- [x] Incident binder at HQ and each venue: this runbook, the call tree, the notification matrix, the acquirer contact, vendor escalation paths
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Common point of purchase or compromise notice | Acquirer or payment partner | **Declare severity 1 at once.** The acquirer's 24-hour clock and Visa's 3-day clock run from suspicion |
| Alert: new or changed script or header on a page that embeds the payment form | Payment page monitoring service (after POAM-010) | Vice President of Marketing and Digital confirms with the agency within 1 hour; if nobody approved it, declare |
| Alert: tag manager publish by a single person, or from a new location | Tag manager history in the SIEM (after POAM-007) | Verify with the publisher by phone; if not approved, declare |
| Alert: bulk patron export, new ticketing admin, or sign-in to a local account from a new country | Ticketing audit log in the SIEM (after POAM-008) | Verify with the account owner by phone; if not them, declare |
| Patrons report card fraud soon after buying tickets, or a "payment failed, try again" pattern | Guest services, chatbot transcripts, social media | Log each report; 3 or more in a week, escalate to the incident commander |
| Vendor or agency reports suspicious activity | Ticketing vendor, tag manager vendor, marketing agency | Declare; request the vendor's evidence package |

**Declare a ticketing platform breach (severity 1) when** any unapproved script or change is confirmed on a page that embeds the payment form, any local or agency account is confirmed misused, or the acquirer names the company as a common point of purchase.

**Record two times in the incident log** (POL-03 4.3):
- **Time of suspicion:** discovery of evidence sufficient to raise a reasonable suspicion of a compromise. It starts the acquirer's 24-hour clock and Visa's 3-day clock.
- **Time of determination:** when the company determines a breach occurred or has reason to believe one occurred. It starts Florida's 30-day clocks (Fla. Stat. 501.171(3)-(4)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log with the time of suspicion | Incident commander | Log open |
| 0-30 min | **Capture before changing anything:** browser captures (with network logs) of affected event pages, the tag manager container version history, the malicious tag source, and the attacker's collection domain | Vice President of Marketing and Digital with a security analyst | Files hashed in the evidence folder |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; counsel assigned; counsel engages forensics | Chief Operating Officer | Claim number; counsel on the call |
| 0-60 min | Export the ticketing audit log, user list, and export history (the vendor keeps 90 days) and request the vendor's own logs and a hold on them | Vice President of Ticketing | Exports hashed; vendor case number |
| 1-2 h | **Contain the page:** roll the tag manager container back to the last approved version, or remove the tag manager from pages that embed the form; if in doubt, switch event pages to the vendor-hosted fallback pages until the page is clean | Vice President of Marketing and Digital | Second capture shows no unapproved scripts |
| 1-2 h | **Contain the accounts:** disable all agency accounts on the tag manager and ticketing platform; force password reset and MFA enrollment for all remaining local accounts; revoke all ticketing sessions; rotate the sync API key | Vice President of Ticketing and IT Director | Vendor confirms sessions revoked |
| 1-2 h | Block the attacker's collection domain at the web edge and SD-WAN firewalls; report it to the tag manager vendor | IT Director | Block in place |
| Within 24 h of suspicion | **Notify the acquirer** (merchant agreement) and agree how the Visa report, incident report, and at-risk account data will be handled | Chief Financial Officer | Acquirer case number recorded |
| 2-4 h | Convene the CMT; first situation report (scope, on-sales affected, decisions needed: pause upcoming on-sales? keep fallback pages?) | CMT chair | Meeting held |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

**If this happens during an on-sale or on a show day:** do not take the ticketing platform offline. Rolling back the tag manager and disabling agency accounts do not stop sales or scanning. If the vendor must suspend the tenant, venue command follows `ir-runbook-event-day-outage.md`.

## 4. Analysis (RS.AN)
1. **Window of exposure.** Find when the malicious tag was first published and when it was removed (tag manager version history, monitoring service alerts, browser captures, web edge logs). Every checkout on an affected page in that window is at risk. The payment partner can list the card numbers used on those pages in that window for the acquirer and Visa.
2. **Initial access.** How were the agency credentials taken? Work with the agency (counsel requests its cooperation under the contract amendment, POAM-021). Check identity provider and ticketing sign-in records for the same attacker addresses against company accounts.
3. **What else the attacker did.** Other exports, new users, API keys or webhooks, changed payout, refund, price, or bot mitigation settings, changes to other tags. Check the CMS and deployment pipeline for changes in the same period.
4. **Two data sets, two analyses:**
   - **Skimmed card data** (name, card number, expiration date, security code): personal information under Fla. Stat. 501.171(1)(g)1.a.(III) when the security code was captured. Card brand rules apply.
   - **Patron export** (name, email, phone, billing address, purchase history, no passwords): not personal information under the Florida definition by itself, but other states' definitions differ, and the FTC Act still governs how the company protected it and what it tells patrons. Counsel decides on notice state by state.
5. **Residency and counts.** Split affected individuals by billing state (about 71% Florida overall) to set the Florida counts (500 or more for the Department of Legal Affairs; more than 1,000 for consumer reporting agencies) and the list of other states.
6. **Preserve evidence** with chain of custody (who collected, when, hash, where stored). Do not delete the malicious tag version or the attacker's sessions until forensics has what it needs. Visa's guidance is not to log in to compromised systems and change things before evidence is preserved; the captures in section 3 come first.

## 5. Containment and eradication (RS.MI)
1. Keep pages that embed the form on the approved script list only; any script returns through change control (POL-01 4.12, 4.13).
2. Keep agency access suspended until the agency's own investigation and the contract amendment are complete; restore it only through SSO with MFA and two-person publishing.
3. Reduce ticketing administrators to 6 and remove export rights from the marketing role.
4. Replace the sync API key with a read-only scoped key in the secrets service.
5. Reset passwords for any company staff whose credentials appear in the forensic findings, and check identity provider sign-ins for the same attacker infrastructure.
6. Forensics confirms that no persistence remains (other tags, admin users, API keys, webhooks, CMS changes) before containment is closed.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice before it goes out. The General Counsel keeps the **decision log** (POL-03 4.6). Card brand rules are applied through the acquirer; they are not law, but missing them brings assessments.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Was card data compromised, and what is the window of exposure? | Incident commander with forensics | Decision log |
| D2 | Time of suspicion (card brand clocks) and time of determination (Florida clock) | General Counsel | Decision log |
| D3 | How many individuals in total, by state, and Florida residents? (Florida thresholds: 500 for the Department; more than 1,000 for consumer reporting agencies; substitute notice is allowed if direct notice would cost more than $250,000 or exceed 500,000 people) | General Counsel | Affected individuals list |
| D4 | Has law enforcement asked in writing for a delay of individual notices? | Counsel | Written request on file |
| D5 | Which contract notices are due: acquirer, insurer, County (from 2027-07-01), ticketing vendor, artists and promoters? | Counsel and CFO | Contract register |
| D6 | Extortion demand over the patron export? | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | COO |
| Within 24 hours of suspicion | Acquirer notified (merchant agreement) | CFO |
| Within 3 calendar days of suspicion | Compromise event reported to Visa Global Risk Investigations (through the acquirer) | CFO |
| Within 3 calendar days of notifying Visa | Incident report to Visa and the acquirer, with PCI DSS compliance documentation (the 2025 AOCs and the P03 readiness status) | Security Manager and CFO |
| Within 3 calendar days of determining the window of exposure | At-risk card numbers provided (the payment partner extracts them) | CFO |
| Within 5 business days of a Visa PFI requirement | PFI contract signed and Visa told the PFI and lead investigator; preliminary report within 5 business days of signing; final report within 10 business days of completing the investigation | CFO and counsel |
| Day 0-2 | Voluntary report to the U.S. Secret Service or FBI (IC3) | Security Manager through counsel |
| Within 48 hours (from 2027-07-01) | County notified if County PAC patrons or services are affected (County PAC agreement) | COO through counsel |
| Within 30 days of determination | Florida individual notices (mail or email); Department of Legal Affairs notice if 500 or more Floridians | General Counsel and outside counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at one time | Outside counsel |
| Per each state's law | Notices for residents of other states, including any state whose definition covers the patron export | Outside counsel |
| After notices are final | Artists and promoters of affected shows told what happened and what patrons were told | Vice President of Ticketing |

**Why the shortest clock matters.** The card brand clocks (24 hours and 3 days) run from suspicion and arrive long before Florida's 30 days. Florida's 30 days can arrive before the forensic report is final. Counsel decides early whether to ask the Department for 15 additional days to notify individuals, which requires good cause in writing within the 30 days; the extension applies only to the notice to individuals, never to the Department notice itself.

**As a Visa Level 2 merchant, expect a PFI.** Visa's guide lists Level 1 and Level 2 merchants among the entities more likely to be required to retain a PFI. Budget for it, and do not use the QSA firm or the MSSP, which are excluded by the 3-year independence rule.

**Extortion (POL-03 4.8).** If the attacker threatens to publish the patron export, any payment needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the actor and any wallet; and a report to law enforcement. Paying does not remove any notice duty. The default position, approved by the CEO, is not to pay.

**Communications.**
- Patrons: website notice and email as counsel approves; a call center script and a dedicated line through the insurer's notification vendor.
- Artists, promoters, and the County (when applicable): direct calls from the Vice President of Ticketing or the COO.
- Media: holding statement approved by counsel. No public statement blames the ticketing vendor or the agency; the entry point was on the company's own pages.
- Staff: briefings through the out-of-band channel only until email is confirmed clean.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Each step is validated before the next begins.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Event entry for the next shows (scanners, manifests, manual entry kits) | Before doors | Offline manifest downloaded; kit checked (BP-01) |
| 2 | Identity provider and administrator access | 2 h | Sessions revoked; privileged credentials rotated |
| 3 | Ticketing tenant: local accounts on MFA, admins reduced, marketing role without export rights | 4 h | Vendor confirms no unknown admins, sessions, API keys, or webhooks (BP-04, BP-05) |
| 4 | Event pages with the embedded form, on the approved script list, with monitoring live | 4 h (fallback pages meanwhile) | Third capture matches the approved list (BP-05) |
| 5 | Tag manager, for non-payment pages only, with two-person publishing | 24 h | Container reviewed line by line |
| 6 | Settlement for shows in the window; chargebacks tracked by the Controller | 12 h | Reconciliation (BP-07) |
| 7 | Patron communications | As counsel approves | Notices sent (BP-09) |

Tell staff, artists, and patrons (where counsel approves) when normal service is confirmed (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.13).
- Update the risk register (P01: R-001, R-002, R-003, R-034, R-037), the POA&M (P07), the PCI DSS scope document, and this runbook.
- Expect the acquirer to require a new PCI DSS validation and possibly a stricter level or conditions on MID-T. Budget for it and tell the QSA.
- Retain all incident records, notices, and Florida determination documents for at least 5 years (Fla. Stat. 501.171(4)(c) sets 5 years for a no-notice determination; the company applies the same period to all incident records).

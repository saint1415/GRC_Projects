# Incident Response Runbook: Payment Card Data Compromise (E-commerce Skimming)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional grocery retailer: 5 supermarkets, online ordering, a distribution center) |
| Tier / Vertical | Mid-Market / Retail Trade |
| Incident type | Payment card data compromise through e-commerce skimming: a malicious script injected into the website or in-app checkout page (for example through a compromised third-party tag or the marketing agency's account) captures card data that customers type into the processor's hosted payment fields |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy; PCI DSS v4.0.1 Requirement 12.10 (N44-45-R01); STD-10 Payment page script and change standard |
| Companion documents | `ir-runbook-ransomware.md` (ransomware across stores and the DC); `notification-matrix.csv`; BIA (P05); risk register (P01 R-002, R-010, R-042) |
| Runbook owner | Security Manager (incident commander) with the Director of E-commerce and Marketing (checkout owner) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Skimming tabletop with the acquirer contact and outside counsel scheduled 2026-11-05 (POAM-010) |

## 0. Governance, roles, and contacts (Govern)
The response runs on two tiers, so technical, business, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, IT Director, Director of E-commerce and Marketing, Director of Store Operations, Director of Customer Service, outside breach counsel | Whether to stop online card payments, customer and supplier communications, notice decisions, resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director, security analysts, Director of E-commerce and Marketing, MSSP, forensic firm or PCI Forensic Investigator (through counsel), e-commerce platform vendor, processor security team | Evidence, containment, investigation, eradication, safe reopening |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Checkout page actions | Director of E-commerce and Marketing | IT Director | Out-of-band group; e-commerce vendor priority line |
| Acquirer and card brand liaison | Chief Financial Officer | Controller | Acquirer merchant risk contact (number in the incident binder) |
| Breach decisions and decision log | General Counsel | Privacy and Compliance Manager | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | Company's outside general counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($10M limit, $250K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel. If the acquirer requires a PFI, the firm must be on the PCI SSC PFI list | MSSP incident response team | Through counsel |
| Payment processor | Processor security and fraud team | Account manager | Merchant portal and binder |
| Communications | Director of E-commerce and Marketing (customer and media messages) | Outside crisis PR (through counsel) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI (IC3) or U.S. Secret Service field office | n/a | Numbers in the binder |

**Out-of-band first.** Assume e-commerce admin accounts and email may be compromised. Coordinate by the pre-provisioned messaging group on personal phones and the printed call tree. **Suspend the marketing agency's e-commerce and tag manager access at the start of any suspected skimming incident.** Work with the agency only under the incident commander's supervision until forensics clears its accounts and tag vendors.

**Legal privilege protocol.** Outside counsel engages the forensic firm (or the PFI the acquirer requires) and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, captures, logs) separate from legal conclusions. Do not speculate in email or chat.

## 1. Preparation checks (Identify / Protect)
- [ ] Inventory of approved checkout scripts for the website and app, with owner, justification, and integrity value (6.4.3). **Gap until POAM-013 closes (2026-11-01)**
- [x] Tamper detection on the website checkout, alerting the security team (11.6.1)
- [ ] Tamper detection on the in-app web checkout. **Gap until POAM-013 closes (2026-11-15)**
- [ ] Tag manager removed from checkout pages. **Due 2026-10-15**
- [ ] Every e-commerce administrator signs in through single sign-on with MFA, including the agency (POAM-003)
- [x] Known-good copy of the checkout templates exported monthly and stored outside the platform
- [x] E-commerce admin logs sent to the SIEM with 12-month retention
- [ ] Acquirer 24-hour notice term and incident line on wallet cards for the CFO, Controller, and Store Managers (POAM-010, due 2026-10-15)
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-15
- [x] Incident binder (printed) at the support center: this runbook, call tree, notification matrix, P05 recovery order

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| New, changed, or unknown script or security header on a checkout page | Tamper detection alert | Security analyst compares with the script inventory within 1 hour; if unexplained, call the incident commander |
| Acquirer or processor reports that the company is a likely common point of purchase for fraud | Acquirer or processor notice | CFO opens the incident immediately. **This is a suspected compromise: the 24-hour acquirer clock is already running** |
| Several customers report card fraud after ordering online | Customer service, social media, store service desks | Log each report; escalate to the incident commander at 3 or more in 30 days (POL-03 4.2) |
| Theme, tag, or app change at an unusual time or by an unexpected account | SIEM use case on e-commerce admin logs | Analyst checks the change ticket (STD-10); declare if none |
| Checkout page sends data to an unfamiliar domain | Browser capture, vendor, or researcher report | Capture evidence; declare |

**Severity 1 (declare immediately):** a confirmed unauthorized script or change on a checkout page, or a common point of purchase notice. This also convenes the CMT (POL-03 4.4).

**Record two times in the incident log** (POL-03 4.3):
- the **time of first suspicion**, which starts the merchant agreement's **24-hour acquirer notice** (contract term, fictional);
- the **time of determination** of a breach or reason to believe one occurred, which starts Florida's **30-day** clocks (Fla. Stat. 501.171(3), (4)(a)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | **Capture evidence before changing anything:** save each checkout page as delivered (full network capture, website and app), copy each suspicious script, record hashes and times, export e-commerce admin and tag manager history | Security analysts | Evidence in a restricted folder with chain-of-custody log |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-60 min | **Stop card capture on the affected checkout.** Turn off online card payment for the affected channel (website, app, or both): orders become pay-at-pickup on store PIN pads; pause home delivery prepayment. Do not wait for root cause | Director of E-commerce and Marketing | No customer can type a card number into an affected page |
| 0-60 min | Suspend the agency's access; revoke all e-commerce admin sessions and app tokens; rotate tag manager credentials | Security Manager | Only 2 named company administrators can publish |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Financial Officer | Claim number; counsel on the call |
| 0-24 h | **Acquirer notice** with the facts known; follow its instructions, including any PFI requirement | Chief Financial Officer | Acquirer reference number recorded |
| 1-2 h | Convene the CMT; first situation report (scope, channels affected, customer impact, decisions needed) | CMT chair | CMT meeting held |
| 1-4 h | Ask the processor to confirm its hosted fields and SDK were not altered and to flag cards used in the suspected window | Chief Financial Officer | Processor confirmation in the log |
| 2-4 h | Store and customer service briefing script: online card payments paused, pay at pickup, what to tell customers, do not speculate | Director of Customer Service with the Director of Store Operations | Script sent to stores and the contact center |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Window of exposure.** Find when the malicious script first appeared and when it was removed, for each channel. Use tamper detection history, e-commerce admin and tag manager logs (12 months in the SIEM), browser captures, and the vendor's records.
2. **Entry point.** A compromised third-party tag vendor, the agency's account (password-only until POAM-003 closes), a former employee's account (R-035), or an installed app. Check whether the attacker also changed sign-in pages.
3. **What was captured.** Usually card number, expiration date, security code, name, and billing address. If the script also ran on sign-in pages, email addresses with passwords may be exposed, which is a separate personal information element under Fla. Stat. 501.171(1)(g).
4. **Who was affected.** List online orders paid by card during the window from e-commerce and processor reports. Count unique cards and customers, and **group them by state of residence** using billing addresses. Seasonal residents may live in other states.
5. **Confirm what was not affected.** In-store payments (PIN pads, separate path), the loyalty database, and the virtual terminal. Record the evidence for each.
6. **Preserve evidence.** Keep the chain of custody. Do not contact the attacker's collection domain.

## 5. Containment and eradication (RS.MI)
1. Restore the known-good checkout templates. Remove the malicious script, the compromised tag, and its vendor from all pages.
2. Allow only inventoried scripts with integrity values and a content security policy; confirm the tag manager is off checkout pages (STD-10).
3. Rotate every e-commerce admin credential, app token, and loyalty API key. Move any remaining local account to single sign-on with MFA or delete it.
4. Review installed apps and their permissions. Remove anything unneeded.
5. Confirm with a fresh browser capture and tamper detection that each page matches the approved inventory. **Online card payments reopen only when forensics agrees and the acquirer has no objection** (POL-03 4.9).

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice before it goes out. The General Counsel keeps the **decision log** (POL-03 4.6).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Was there a breach of security of personal information under Fla. Stat. 501.171(1)(a) (unauthorized access of electronic data containing personal information)? | General Counsel with counsel | Decision log |
| D2 | Time of determination (Florida clocks) | General Counsel | Decision log |
| D3 | Affected individuals in total, by state, and Florida residents (thresholds: 500 Floridians for the Department notice; more than 1,000 notified at one time for consumer reporting agencies) | Privacy and Compliance Manager | Affected individuals list |
| D4 | Has law enforcement asked for a delay (501.171(4)(b))? Get it in writing | Counsel | Decision log |
| D5 | Contract notices due (acquirer, suppliers, lender, sponsor)? | Counsel and CFO | Contract register |
| D6 | Is the 15-day good-cause extension for individual notice needed (501.171(3)(a))? It never extends the Department notice | Counsel | Written request to the Department |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Within 24 hours of suspicion | Acquirer notice; follow acquirer and card brand instructions | Chief Financial Officer |
| Hour 0-1 | Insurer hotline; counsel engaged | Chief Financial Officer |
| Day 0-2 | Voluntary report to the FBI (IC3) or the U.S. Secret Service | Security Manager through counsel |
| As soon as known | Breach determination documented (D1, D2) | General Counsel |
| Within 30 days of determination | Notice to affected Florida residents (or within 45 days with a timely written good-cause request to the Department); Department of Legal Affairs notice if 500 or more Floridians | General Counsel and counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at one time | Counsel |
| Per each state's law | Notice to residents of other states and their regulators | Counsel |

**No-notice decision.** Individual notice is not required if, after an appropriate investigation and consultation with law enforcement, the company reasonably determines that the breach has not and will not likely result in identity theft or other financial harm. That decision must be documented, kept 5 years, and sent to the Department within 30 days (501.171(4)(c)). **Skimmed card numbers with security codes are used for fraud, so counsel should expect notice to be required.**

**Worked example (tabletop scenario).** A malicious script ran on the website checkout for 12 days before tamper detection was extended to it; the app checkout was not affected. About 390 online orders a day, of which about 330 were paid by card online on the website, gives about 3,960 orders and, after removing repeat customers, about 3,300 unique cards. About 3,060 belong to Florida residents and 240 to residents of 14 other states. Result: acquirer notice within 24 hours of suspicion; Florida individual notices and the Department notice within 30 days of determination (500 or more Floridians); consumer reporting agency notice (more than 1,000 notified at one time); counsel applies the laws of the 14 other states.

**Not applicable:** the FTC Safeguards Rule notice (not a financial institution under 16 CFR Part 314), SEC Form 8-K (privately held), and CIRCIA (no final rule; reporting is voluntary).

**Communications.**
- Customers: notice letters or email per counsel; a website FAQ and call-center script; card reissue is handled by issuers.
- Stores: talking points for service desks; no speculation.
- Suppliers: only if supplier data was affected (contract term); otherwise none.
- Media: holding statement approved by counsel; no technical details.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). In-store sales (BP-01) keep running throughout, because store card data takes a separate path from the PIN pads to the processor.
1. Identity provider and administrator access, with all e-commerce credentials rotated
2. Checkout templates from the known-good copy, with only inventoried scripts
3. Tamper detection confirmed live on both checkouts
4. Online card payments reopened (BP-03, RTO 4 hours **after** the integrity check) once forensics agrees and the acquirer has no objection; until then, pay-at-pickup on PIN pads
5. Picking, pickup, and delivery (BP-04) continue from the order queue
6. Loyalty API keys rotated; pricing engine unchanged unless involved

Tell customers and stores when online card payments are available again (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Update the risk register (P01 R-002, R-010), the POA&M (P07), STD-10, and this runbook.
- Tell the QSA. The incident and its fixes must be reflected in the next SAQ D and AOC (P03 G-027, G-055).
- Keep the decision log and any no-notice documentation for at least 5 years, and other incident records for at least 3 years (POL-01 4.12; POL-03 4.6).

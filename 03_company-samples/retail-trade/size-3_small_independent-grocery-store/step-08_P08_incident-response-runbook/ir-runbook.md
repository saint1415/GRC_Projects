# Incident Response Runbook: Payment Card Data Compromise (E-commerce Skimming)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent grocery retailer, one supermarket plus online ordering) |
| Tier / Vertical | Small / Retail Trade |
| Incident type | Payment card data compromise through e-commerce skimming: a malicious script injected into the checkout page through a compromised third-party tag captures card data that customers type into the processor's embedded payment form |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; PCI DSS v4.0.1 Requirement 12.10 (N44-45-R01) |
| Runbook owner | IT Manager (Information Security Lead) |
| Approved | 2026-09-04 by the General Manager |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-005) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | General Manager | Incident line (cell), then the out-of-band group chat on personal phones |
| Storefront and checkout page actions | E-commerce and Marketing Manager | IT Manager | Cell; storefront vendor's priority support line |
| Acquirer and card brand liaison | Controller | General Manager | Acquirer's merchant risk contact (number in the incident binder) |
| Forensics | Forensic firm from the cyber insurer's panel. If the acquirer requires a PCI Forensic Investigator (PFI), the firm must be on the PCI SSC PFI list | n/a | Via the insurer hotline |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via the insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder (Controller) |
| Payment processor | Processor's security and fraud team | Processor account manager | Merchant portal and phone number in the binder |
| Communications | General Manager | Outside PR through counsel | Cell |
| Law enforcement | FBI (IC3) or U.S. Secret Service field office | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume that storefront admin accounts and email may be compromised. Coordinate by phone and the printed contact list in the office incident binder. **Suspend the marketing contractor's storefront access at the start of any suspected skimming incident.** Work with the contractor only under the IT Manager's supervision until forensics clears its account and tag vendors.

## 1. Preparation checks (Identify / Protect)
- [ ] Inventory of approved checkout scripts, with owner, reason, and integrity value (6.4.3). **Gap until POAM-003 closes**
- [ ] Payment page monitoring service live, alerting the IT Manager and the E-commerce and Marketing Manager by text (11.6.1). **Gap until POAM-004 and POAM-009 close**
- [ ] A known-good copy of the checkout template and theme, exported monthly and kept outside the storefront
- [ ] Storefront admin, identity provider, and cloud logs kept for 1 year (AU-11). **Gap until POAM-010 closes**
- [ ] Every storefront administrator signs in through single sign-on with MFA (POAM-001, POAM-006)
- [ ] Acquirer 24-hour notice term and the incident line printed on wallet cards for managers and the Controller (POAM-015)
- [ ] Insurer panel forensic firm and counsel confirmed (POAM-005)
- [ ] Printed incident binder in the office: this runbook, contacts, notification matrix, P05 recovery order

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| New, changed, or unknown script or security header on the checkout page | Payment page monitoring alert (from 2026-11-15) | E-commerce and Marketing Manager compares with the script inventory within 1 hour; if unexplained, call the incident line |
| Acquirer or processor reports that the company is a likely common point of purchase for fraud | Acquirer or processor notice | Controller opens the incident immediately. **This is a suspected compromise: the 24-hour acquirer response clock applies** |
| Several customers report card fraud after ordering online | Customer service, social media reviews | Log each report; escalate to the IT Manager when there are 2 or more in 30 days |
| Theme, tag, or app change at an unusual time or by an unexpected account | Storefront admin log review, weekly (from 2026-10-31) | IT Manager checks with the change record (POL-01 4.13) |
| Checkout page sends data to an unfamiliar domain | Browser capture, storefront vendor, or security researcher report | IT Manager captures evidence and opens the incident |

**Declare an e-skimming incident when** an unauthorized script or change is confirmed on the checkout page, or the acquirer or processor reports a common point of purchase.
**Record the time of suspicion and the time of determination.** Two clocks start here:
- the merchant agreement's **24-hour acquirer notice** runs from suspecting a compromise (contract term, fictional);
- Florida's **30-day notice** to individuals runs from "the determination of a breach or reason to believe a breach occurred" (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Capture evidence before changing anything:** save the page as delivered to a browser (full network capture), copy each suspicious script, record hashes and the time, and export the storefront admin log and tag manager history | IT Manager | Evidence saved to a restricted folder with a chain-of-custody log |
| 2. Suspend the marketing contractor's storefront and tag manager access. Revoke all storefront admin sessions and app tokens | IT Manager | Only the IT Manager and the E-commerce and Marketing Manager can publish |
| 3. **Stop card capture on the page.** Turn off online card payment: take pickup orders only, paid on a P2PE PIN pad at the service desk, and pause delivery (P05 BP-02 workaround). Do not wait for root cause | E-commerce and Marketing Manager | No customer can type a card number on the storefront |
| 4. Controller calls the acquirer and follows its instructions, including any requirement to use a PFI. **No later than 24 hours after suspicion** | Controller | Acquirer reference number recorded |
| 5. Call the cyber insurer's breach hotline. Engage counsel and forensics through the insurer | General Manager | Claim number issued |
| 6. Ask the processor to confirm that its embedded payment form was not altered, and to flag cards used during the suspected window | Controller | Processor confirmation in the incident log |
| 7. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Window of exposure:** find when the malicious script first appeared and when it was removed. Use the storefront admin log, tag manager publish history, browser captures, monitoring history, and the storefront vendor's records. Default log retention may be as short as 30 to 90 days, so export logs first (POAM-010).
2. **Entry point:** a compromised third-party tag vendor, the contractor's account (password only until POAM-001 closes), a former employee's account (R-009), or an installed app (R-032).
3. **What was captured:** usually card number, expiration date, security code, and name and billing address. Check whether the script also ran on sign-in pages. If it did, email addresses with passwords may also be exposed (a separate personal information element under Fla. Stat. 501.171(1)(g)).
4. **Who was affected:** list the orders paid online during the window from the storefront and processor reports. Count unique cards and customers, and **group them by state of residence** using billing addresses. Seasonal residents may live in other states.
5. **Confirm what was not affected:** in-store payments on P2PE PIN pads, and the loyalty database. Record the evidence for both.
6. **Preserve evidence:** keep the chain of custody. Do not contact the attacker's collection domain.

## 5. Containment and eradication (RS.MI)
1. Remove the malicious script by restoring the known-good checkout template. Remove the compromised tag and its vendor from all pages.
2. Remove the tag manager from the checkout page. Allow only inventoried scripts, with integrity values and a content security policy (POAM-003, POAM-004).
3. Rotate every storefront admin credential and app token. Move any remaining local account to single sign-on or delete it.
4. Review installed apps and their permissions. Remove anything unneeded.
5. Confirm with a fresh browser capture and the monitoring service that the page matches the approved inventory. Forensics must agree before card payments reopen online.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Legal counsel confirms every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Within 24 hours of suspicion | Acquirer notice under the merchant agreement; follow acquirer and card brand instructions | Controller |
| Day 0 | Insurer notified; counsel engaged | General Manager |
| Day 0-2 | Voluntary report to the FBI (IC3) or the U.S. Secret Service | IT Manager |
| Day 0-5 | Staff briefing script: what happened, what to tell customers, do not discuss outside the company | General Manager |
| As soon as known | Breach determination under Fla. Stat. 501.171, documented by counsel | General Manager and counsel |
| Within 30 days of determination | Notice to affected Florida residents; notice to the Department of Legal Affairs if 500 or more Florida residents | General Manager and counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at one time | Counsel |
| Per each state's law | Notice to residents of other states and their regulators | Counsel |

**Law enforcement delay.** If a law enforcement agency determines that notice would interfere with a criminal investigation, notice may be delayed for the period it specifies (Fla. Stat. 501.171(4)(b)). Keep the request in writing.

**No-notice decision.** Notice to individuals is not required if, after an appropriate investigation and consultation with law enforcement, the company reasonably determines that the breach has not and will not likely result in identity theft or other financial harm. That decision must be documented, kept for 5 years, and provided to the Department of Legal Affairs within 30 days (Fla. Stat. 501.171(4)(c)). **Skimmed card numbers with security codes are used for fraud, so counsel should expect notice to be required.**

**Worked example (tabletop).** The malicious script ran for 9 days before a customer complaint. About 95 online orders a day gives about 855 orders and, after removing repeat customers, about 700 unique cards. About 680 belong to Florida residents and 20 to residents of 4 other states. Result: notify the acquirer within 24 hours; notify Florida residents and the Department of Legal Affairs within 30 days of determination (500 or more Floridians); no consumer reporting agency notice (not more than 1,000 at one time); check the laws of the 4 other states.

**Not applicable:** HIPAA (no pharmacy), the FTC Safeguards Rule notice (the company is not a financial institution under 16 CFR Part 314), SEC Form 8-K (privately held), and CIRCIA (no final rule; reporting is voluntary).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). In-store sales (BP-01) keep running on P2PE PIN pads throughout, because in-store card data never touches the storefront.
1. Identity provider and administrator access (break-glass accounts if needed), with all storefront credentials rotated
2. Storefront checkout page from the known-good template, with only inventoried scripts
3. Payment page monitoring confirmed live and alerting
4. Online card payments reopened (BP-02, RTO 8 hours) after forensics agrees. Until then, online orders are pickup only and paid in the store
5. Order fulfillment (BP-03) continues from the storefront; printed pick lists if needed
6. Loyalty API keys rotated as a precaution; pricing engine unchanged unless it was involved

**Validate before reopening card payments online:** the page matches the approved script inventory, credentials are rotated, the compromised tag vendor is removed, and the acquirer has no objection. Tell customers when online payments are available again (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 4.10 requires documentation within 30 days).
- Update the risk register (P01 R-001, R-002, R-032), the POA&M (P07), and this runbook.
- Review with the acquirer whether the company can still check the SAQ A eligibility statement on script attacks, or must validate the online channel another way (P03).
- Keep all incident records for at least 3 years (POL-01 4.11), and the no-notice documentation, if any, for 5 years.

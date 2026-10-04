# Incident Response Runbook: Payment Card Data Compromise (E-commerce Skimming)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional supermarket chain; 112 stores in FL, GA, AL, SC, TN; online ordering) |
| Tier / Vertical | Enterprise / Retail Trade |
| Incident type | Payment card data compromise through e-commerce skimming: a malicious script on a page that hosts or leads to payment fields captures card data that customers type at checkout. Includes the acquirer and card brand track, the PCI forensic investigation, the SEC materiality assessment, and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); PCI DSS v4.0.1 Requirement 12.10 (N44-45-R01) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure |
| Runbook owner | Director of Security Operations, with the Vice President, Payments for section 6 and the General Counsel for sections 7 and 8 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-19 (ransomware scenario; **the disclosure committee did not take part and no card compromise was exercised**). Next: card compromise tabletop with the disclosure committee on 2026-11-12 (POAM-010) |
| Notification matrix | `notification-matrix.csv` (28 obligations: 5 acquirer, card brand, and processor; 4 generic state; 6 Florida worked example; 5 SEC and disclosure; 8 others, including law enforcement, insurance, client contracts, OFAC, SNAP EBT, and rows that do not apply) |

**Why this scenario.** In-store card data is encrypted at the PIN pad, so the card data exposure has moved to the browser (P01 R-002, High). The web checkout embeds the processor's hosted payment fields, but a script on the surrounding page can still overlay a fake payment form or redirect a customer. 47 scripts load on payment pages, and the express checkout and cart pages are outside the script controls until POAM-002 closes (P03 G-027, G-055; P07 SI-7).

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Technical lead | Director of E-commerce Engineering | E-commerce platform on-call lead | SOC bridge |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Payments liaison (acquirer, processor, card brands) | Vice President, Payments | PCI Program Manager | Direct mobile; acquirer merchant risk line in the incident binder |
| System owner (checkout decisions) | Chief Digital Officer | Director of E-commerce Engineering | Direct mobile |
| Crisis management team chair | Chief Operating Officer | Senior Vice President, Store Operations | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; the Vice President, Payments joins for card data incidents; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Outside breach counsel and forensics | Retained firms engaged through counsel; a PCI Forensic Investigator (PFI) from the PCI SSC list when the acquirer or a card brand requires one | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Customer care | Chief Marketing Officer (contact center and loyalty communications) | Contact center director | Direct mobile |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | U.S. Secret Service field office or FBI | IC3 online report | Numbers in the incident binder |

**Out-of-band first.** If the tag manager, content delivery network (CDN), or storefront admin accounts may be compromised, assume email and chat may be watched too. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder.

## 1. Preparation checks (Identify / Protect)
- [ ] Payment page script inventory, written justification, integrity values, and tamper detection cover **every** page that hosts or leads to payment fields (**gap until POAM-002 closes on 2026-10-16**: express checkout and cart pages) (PCI DSS 6.4.3, 11.6.1; SI-7)
- [ ] CDN and tag manager change logs reach the SIEM (**gap until POAM-002 closes**) (AU-6)
- [ ] Targeted risk analysis sets the payment page check frequency for every checkout path (**gap until POAM-018 closes**) (RA-3)
- [ ] TPSP list includes every script supplier on payment pages (**gap until POAM-003 closes**)
- [ ] Logs kept at least 12 months with 3 months immediately available (AU-11); storefront release history and tag manager container versions kept at least 12 months
- [ ] Acquirer and processor contacts, the merchant agreement notice term (24 hours from suspicion), and the Visa reporting route current in the incident binder
- [ ] Outside counsel retainer and a shortlist of PFI firms confirmed this quarter
- [ ] Materiality playbook includes card incident inputs and the disclosure committee roster is current (**gap until POAM-010 closes**)
- [ ] State breach law matrix from outside counsel updated in the last 12 months (last update 2026-04)
- [ ] Pre-approved customer notice and contact center scripts for a card compromise drafted and reviewed by Legal

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Tamper detection alert: new or changed script, or changed security-relevant HTTP header, on a payment page | Payment page change and tamper detection (PCI DSS 11.6.1) | SOC opens a severity-1 case if the script sends data to an unapproved domain; otherwise severity 2 until analyzed |
| Content security policy violation reports showing a request to an unknown domain from a checkout or cart page | CSP reporting endpoint (report-only on express checkout until POAM-002 closes) | Capture the report; compare the domain with the approved script list; open a case |
| Common point of purchase notice or fraud alert from the acquirer, processor, or a card brand naming the company | Acquirer or processor (often the first sign of a skimmer) | Treat as severity 1 until disproved; the acquirer clock has started |
| Customers report fraud on cards used only for online orders | Contact center trend report; social media | Customer care escalates to the SOC with order numbers |
| Security researcher or threat intelligence reports a skimmer on a company domain | Vulnerability disclosure inbox; intelligence feeds | Validate in an isolated browser; open a case |
| Unexpected change in the tag manager, CDN configuration, or storefront admin console | Change detection; admin audit logs | Revoke sessions for the account; open a case |
| A script supplier or TPSP reports a compromise of a script it serves | Vendor notice (POL-03 4.12) | Remove or pin the supplier's script; start the third-party track in section 8 |

**Declare a severity-1 card data incident when** a script on a payment page is confirmed to send data to an unapproved destination, or the acquirer, processor, or a card brand reports a common point of purchase that points to the company.

**Record three times, separately, in the incident log:**
1. **Suspicion time:** when anyone first had reason to suspect a compromise of card data. This starts the **24-hour acquirer notice** under the merchant agreement, and Visa expects suspected compromises to be reported immediately (Visa Core Rules 10.3.1.2, ID# 0007999).
2. **State-law determination time:** when the company determines a breach occurred, or has reason to believe one occurred. For Florida residents this starts the **30-day** clocks for individuals and the Department of Legal Affairs (Fla. Stat. 501.171(3), (4)). Other states use their own triggers.
3. **Materiality determination time:** recorded by the disclosure committee (section 7). This starts the **4-business-day Form 8-K** clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Preserve before removing:** capture the live page, every script with its hash, the tag manager container version, CDN configuration, and WAF and CDN logs, from desktop and mobile user agents (skimmers often target mobile browsers or specific regions) | SOC; E-commerce Engineering | Evidence register entries with hashes |
| 2. **Contain:** remove the malicious script; disable the tag manager on all payment pages; roll back to the last known-good release; switch the content security policy to block mode. If the source is not yet known, the Chief Digital Officer turns off the express checkout and routes all customers to the main checkout, which is under the script controls | E-commerce Engineering; Chief Digital Officer | Tamper detection shows a clean page on all paths |
| 3. Block the exfiltration domains and IP addresses at the CDN and WAF; check the main checkout and all other pages for the same code | SOC | Blocks confirmed; other pages checked |
| 4. Revoke sessions and rotate credentials for the tag manager, CDN, storefront admin, and pipeline accounts involved; rotate API keys for the processor's hosted fields if they could be exposed | Identity team; E-commerce Engineering | Revocations logged |
| 5. **Notify the acquirer within 24 hours of suspicion**, and follow its instructions; the acquirer reports to the card brands, or the company reports to Visa on the acquirer's behalf if the acquirer asks (section 6) | Vice President, Payments | Acquirer case number |
| 6. The CISO briefs the General Counsel and the CEO; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified through the breach hotline | CISO; General Counsel | Engagement letters and claim number |
| 7. Tell the processor (hosted fields and token vault); ask for fraud monitoring on cards used in the exposure window | Vice President, Payments | Processor ticket |
| 8. Start the incident log (timeline, decisions, who, when) and the evidence register with chain of custody | Incident commander | Log open |

Do not contact the attacker's domains from company networks, and do not announce the incident publicly until counsel and the disclosure committee agree on timing (section 7).

## 4. Analysis (RS.AN)
1. **Script analysis:** de-obfuscate the script; identify what it captured (card number, expiry date, security code, name, billing address, email, phone, account sign-in), how it captured it (fake payment form over the hosted fields, field listener on the page, redirect), and where it sent data.
2. **Initial access:** compromised tag manager or CDN account, a compromised third-party script supplier, a storefront vulnerability (the express checkout had not been penetration tested; P01 R-036), or a pipeline change. Check the tag manager first while POAM-002 is open.
3. **Exposure window:** from the first load of the malicious script (CDN logs, tag manager history, archived pages) to removal. Confirm with the PFI if one is engaged.
4. **Affected transactions and people:** from order management, list every order that loaded the affected page in the window, by checkout path and device type; count distinct cards and customers; record each customer's **state of residence** from the account and billing address. For loyalty members, link to the member record only through the privacy team. **This drives section 8.**
5. **Evidence:** keep chain of custody for every artifact; give the PFI and Visa access to records and systems when required (Visa Core Rules 10.3.1.1, ID# 0007123).
6. **Business impact:** Finance estimates costs using P05 values (for example, about $950,000 per day if online ordering and payment stop; BP-03) and the expected forensic, legal, notification, customer care, and card brand costs. Card brand assessments and fraud recovery claims are contractual and are not known in advance; record estimates as ranges. These estimates feed section 7.

## 5. Containment and eradication (RS.MI)
1. Remove every unauthorized script; review all 47 payment page scripts against the inventory and remove any without written justification and authorization (PCI DSS 6.4.3).
2. Remove the tag manager from all payment pages permanently; load approved scripts only with integrity values and an enforced content security policy.
3. Fix the initial access path (credential reset with phishing-resistant MFA for tag manager and CDN accounts; supplier removed or pinned to a verified version; vulnerability patched).
4. Extend change and tamper detection to every checkout path and set the check frequency from the targeted risk analysis (PCI DSS 11.6.1); during the investigation, run checks hourly.
5. Forensics (or the PFI) confirms the malicious code is gone from all pages and that no other company systems were affected before the express checkout is turned back on. The CISO and the Chief Digital Officer approve the restart.

## 6. Acquirer and card brand track (contractual)
| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | Notify the acquirer within 24 hours of suspicion (merchant agreement term, fictional); give the facts known so far and the case contact | Vice President, Payments | Acquirer case number |
| 6.2 | Report to Visa as the acquirer directs: members must report suspected or confirmed compromises immediately as Visa's What To Do If Compromised guide specifies; in the US region a merchant may report on the member's behalf (Visa Core Rules 10.3.1.2, ID# 0007999) | Vice President, Payments; PCI Program Manager | Report reference |
| 6.3 | Follow other brands' procedures as the acquirer instructs (Mastercard, American Express, and Discover rules were not reviewed for this runbook; American Express and Discover are contacted directly where the company has a direct agreement) | Vice President, Payments | Instructions logged |
| 6.4 | Engage a PFI through counsel when the acquirer or a card brand requires one, and give Visa, its agent, and the PFI access to premises, records, and systems (Visa Core Rules 10.3.1.1, ID# 0007123) | General Counsel; PCI Program Manager | PFI engagement letter |
| 6.5 | Send the list of potentially exposed card numbers to the acquirer through the secure channel the acquirer specifies, so issuers can monitor or reissue cards. Never send card numbers by email | PCI Program Manager | Transfer confirmation |
| 6.6 | Track contractual consequences: card brand assessments, fraud and operating expense recovery claims, and any requirement to revalidate PCI DSS compliance. Brief the QSA, because the 2026 ROC fieldwork runs from 2026-10-19 to 2026-11-20 | Vice President, Payments; CFO | Cost tracker updated for section 7 |

## 7. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 to 6. It does not wait for the PFI report: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration, with the Vice President, Payments, and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 7.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 to 6, including the acquirer's and card brands' instructions and the expected PFI timeline | Committee | Worksheet completed |
| 7.5 | **Materiality determination** made and recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer (for example, the PFI's count of exposed cards) | Committee (General Counsel records) | Determination minute signed |
| 7.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 7.8 | Align timing and content of customer notices, media statements, the acquirer, and investor communications with the filing; brief the audit committee and the risk and technology committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 7.9 | Keep reassessing as facts change (for example, a longer exposure window found by the PFI); counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Number of cards and customers exposed; forensic, legal, notification, and customer care costs; expected card brand assessments and fraud recovery claims (ranges); lost online sales if the express checkout stays off (P05 BP-03); insurance coverage, sublimits, and retention (P01 R-060) |
| Payments relationship | Acquirer conditions, possible PCI DSS revalidation, effect on the 2026 ROC and AOC due 2026-12-15, processor relationship |
| Data | Data elements captured (card with security code; account credentials); number of states; whether data appeared for sale |
| Customers and operations | Loyalty and online account trust; contact center volume; any effect on stores (none expected for checkout skimming) |
| Legal and regulatory | Expected state attorney general inquiries, FTC interest under Section 5, consumer class actions, card brand disputes |
| Reputation and strategy | Media coverage; effect on online growth and the retail media business; analyst reaction |

**Worked example of the clocks (fictional dates):** on Tuesday 2027-02-02 at 09:15 a security researcher reports a skimmer on the express checkout (suspicion). The acquirer is notified at 15:00 the same day, inside 24 hours. The disclosure committee convenes on Wednesday 2027-02-03. On Thursday 2027-02-04 forensics confirms the script captured card numbers with security codes entered on the express checkout from 2027-01-06 to 2027-02-02 (the state-law determination). On Monday 2027-02-08 at 17:00 the committee determines the incident is material; the Form 8-K is due by Friday 2027-02-12 (4 business days: February 9, 10, 11, and 12). Florida's 30-day clocks for individuals and the Department of Legal Affairs run from the determination to Saturday 2027-03-06, so the plan treats Friday 2027-03-05 as the last business day. Counsel must also decide whether the researcher's report on 2027-02-02 already gave "reason to believe a breach occurred", which would move the Florida dates to 2027-03-04; the plan uses the earlier date. Each other state's deadline is added from counsel's matrix, and the master calendar follows the shortest clock.

## 8. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 8.1 | Breach determination with counsel: which data elements were acquired, for which customers, and whether each state's definition of personal information is met (card number with security code; account sign-in credentials; Florida also covers geolocation, so confirm the script could not reach app location data) | Chief Privacy Officer | Signed determination with the date and time |
| 8.2 | Build the affected population from section 4: each customer, data elements, and **state of residence**. Customers are mainly in Florida, Georgia, Alabama, South Carolina, and Tennessee, but online shoppers and seasonal residents can live in any state | Chief Privacy Officer; data team | Affected-customer file with state counts |
| 8.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules, and substitute notice rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 8.4 | **Florida worked example:** individual notice within 30 days of determining the breach or having reason to believe one occurred (15 more days on written good cause to the Department, for individual notice only); Department of Legal Affairs notice within 30 days if 500 or more Floridians are affected, with no extension; consumer reporting agencies if more than 1,000 are notified at one time | General Counsel | Florida filings |
| 8.5 | **Plan to the shortest clock** across every state, the acquirer and card brands, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 8.6 | Honor any law enforcement delay request (for Florida, 501.171(4)(b)) and the matching provisions of other states; keep the written request | General Counsel | Delay record |
| 8.7 | Prepare the notice content: what happened, the exposure window, data elements, what the company is doing, what customers should do (review card statements, contact their card issuer), and contact details. Engage the mail vendor and contact center surge support | Chief Privacy Officer; Chief Marketing Officer | Notices approved by counsel |
| 8.8 | Notify contractual parties per contract: processor; SL-1 and SL-2 clients only if their data or services are affected; the insurer | Contract owners | Contract notices logged |
| 8.9 | Track inbound vendor notices if the incident started at a script supplier or TPSP (state third-party agent laws such as Fla. Stat. 501.171(6)(a); POL-03 4.12) | Director of Third-Party Risk Management | Vendor notices logged |

**No ransom expected.** Skimming is usually silent. If an extortion demand arrives, any payment needs the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.7). Paying does not remove notification or disclosure duties.

## 9. Recovery (RC.RP, RC.CO)
Checkout skimming rarely takes systems down; recovery means returning every checkout path to service with controls proven. Restore in BIA priority order (P05 section 7) where systems were changed or taken offline:
1. Identity platform and the tag manager, CDN, and storefront admin accounts (credentials rotated, phishing-resistant MFA)
2. E-commerce platform and hosted payment fields on the main checkout (P05 priority 8, RTO 4 hours)
3. Express checkout, only after integrity values, enforced content security policy, and tamper detection are live on it and forensics confirms it is clean
4. Order fulfillment (handhelds, order management, delivery handoff)
5. Loyalty and personalized offers, and the contact center with incident scripts

**Validate before reopening each path:** tamper detection clean for 24 hours in pre-production, the script inventory matches the page, CDN and tag manager logs in the SIEM. Tell customers, the acquirer, and the processor when checkout paths return (RC.CO).

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing the incident; written report within 30 days (POL-03 4.10).
- Update the risk register (P01: R-002, R-006, R-010, R-036), the POA&M (P07), this runbook, the materiality playbook, and the targeted risk analysis for payment page check frequency.
- Give the QSA the PFI report and remediation evidence; confirm with the acquirer whether revalidation is required.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality determination minutes, the breach determination, and the PFI report, for at least 3 years, and any Florida no-notice determination for at least 5 years (POL-01 4.15).

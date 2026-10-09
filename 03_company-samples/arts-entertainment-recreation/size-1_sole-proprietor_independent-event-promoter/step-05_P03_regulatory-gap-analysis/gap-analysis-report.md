# Regulatory Gap Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent event promoter with one leased room) |
| Tier / Vertical | Sole Proprietorship / Arts, Entertainment, and Recreation |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024). A contractual standard enforced through the merchant agreement, **not law** (N71-R04). Validation tool: SAQ A |
| Secondary rules | FTC Act Section 5, 15 U.S.C. 45(a)(1) and 45(n), and the FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (both under N71-R05); Fla. Stat. 501.171(2) and (8); a one-row BOTS Act applicability check |
| Assessment dates | 2026-07-27 to 2026-07-31 (self-assessment) |
| Assessor | Owner, with the on-call IT consultant (confidentiality agreement signed 2026-07-24). Evidence is the intake record and the owner's self-review (EV-038), checked on screen where possible |
| Adopted | 2026-08-31 |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the result for the rules analyzed here.

### 1.1 PCI DSS applies by contract
The owner is the merchant of record for ticket sales, and the merchant agreement requires PCI DSS compliance (EV-010). PCI SSC sets no size tiers and no exemption for sole proprietors; the card brands and the processor set validation rules. The processor's portal assigned **SAQ A** (EV-009). It has not stated a merchant level. With about 2,000 Visa transactions a year (EV-008), the business falls in Visa's Level 3 (1 to 1,000,000 Visa transactions a year), per Visa's *What To Do If Compromised* v10.0 as verified in the Small sample.

### 1.2 Is SAQ A true today? No.
PCI SSC describes SAQ A merchants as card-not-present merchants whose account data functions are completely outsourced to PCI DSS validated and compliant third parties, who keep only paper reports or receipts with account data, and who do not store, process, or transmit account data in electronic form on their own systems or premises (PCI SSC blog on the SAQ A update, January 2025). Three facts break that today:

| Channel | What happens | SAQ A fit |
|---|---|---|
| Online and walk-up | Patrons pay in the hosted checkout (vendor event pages, or the checkout widget embedded on the owner's website); walk-ups use their own phones | **Fits**, if the script eligibility criterion is met (below) |
| Phone orders (about 120 a year) | The owner keys the caller's card number into the SYS-01 box office screen on the laptop (EV-005, EV-028) | **Does not fit.** The laptop processes card data |
| Fans' emails and texts | 23 emails and 4 texts with card numbers were found (19 with security codes; EV-040) | **Does not fit.** Card data stored in the mailbox and on the phone |

**Script eligibility criterion.** In January 2025 PCI SSC removed Requirements 6.4.3 and 11.6.1 (and the related 12.3.1 targeted risk analysis) from SAQ A and added an eligibility criterion: the merchant confirms its site is not susceptible to attacks from scripts that could affect its e-commerce systems. PCI SSC states the underlying requirements remain in PCI DSS (blog above; PCI SSC FAQ "How does an e-commerce merchant meet the SAQ A eligibility criteria for scripts?"). The owner cannot confirm it today: three unreviewed scripts run on the event pages that embed the checkout (EV-011, EV-039; G-027, G-055).

**Decision.** The owner will **make SAQ A true before signing it** (due 2026-10-31): payment links replace keyed phone orders from 2026-09-01; the website and order emails tell fans never to send card details; any card data received is deleted on receipt; and the event pages carry only approved scripts. Until then, the laptop, mailbox, phone, and the Room's network are in scope, so this analysis rates every PCI DSS requirement group. The 25 rows that leave scope once the channels are fixed carry a **scope note** in `pending_rule_change`. The safeguards in those rows still matter for FTC reasonable security and Fla. Stat. 501.171(2), so they stay in P01 where they carry risk.

The owner must re-read the current SAQ A v4.0.1 eligibility criteria and questions in the processor's portal before signing. This analysis does not reproduce the SAQ; it lists PCI DSS requirement groups with short labels written for this analysis, because PCI DSS is copyrighted.

### 1.3 Secondary rules
- **FTC Act Section 5** empowers the FTC to act against "persons, partnerships, or corporations" (15 U.S.C. 45(a)(2)), so it reaches a sole proprietor with no size threshold. Broken privacy or security promises can be deceptive (45(a)(1)); a practice is unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that benefits do not outweigh (45(n)).
- **Rule on Unfair or Deceptive Fees, 16 CFR Part 464** (90 FR 2166, 2025-01-10; effective 2025-05-12). "Business" includes an individual, and "covered good or service" includes live-event tickets (464.1). Any offer, display, or advertisement of a ticket price must disclose the total price clearly and conspicuously (464.2(a)) and more prominently than other pricing information (464.2(b)); excluded fees and the final amount must be disclosed before payment (464.2(c)); fees may not be misrepresented (464.3). The rule reaches the owner's own social posts, flyers, and emails, not just the vendor's checkout.
- **BOTS Act, 15 U.S.C. 45c.** The owner is a "ticket issuer" (the definition names the sponsor or promoter of an event) and the Room's 280 capacity (EV-021) exceeds the 200-person threshold in the "event" definition (Pub. L. 114-274, sec. 3). The Act places **no compliance duty** on the owner; it protects the owner's bot protection and limits (P10).
- **Fla. Stat. 501.171.** "Covered entity" names a sole proprietorship (501.171(1)(b)), and about 85% of patron records have a Florida ZIP code (EV-006). The owner must take reasonable measures to protect electronic personal information (501.171(2)) and dispose of customer records by shredding or erasing (501.171(8)). Personal information includes a name with a card number and any required security code (501.171(1)(g)), which is exactly what fans emailed. Breach notice duties are in P08.

**Not applicable, with reasons:** Nevada Regulation 5.260, NIGC MICS, and the casino BSA/AML rules (N71-R01 to R03), because there is no gaming; COPPA (N71-R06), because the site is general audience and buyers must be 18 or older (EV-006, EV-013); CIRCIA (final rule not published); SEC disclosure (not a public company).

## 2. Method
1. **Requirements.** PCI DSS was broken into its 12 principal requirements and their requirement groups (for example 8.2). The payment page requirements were taken to the defined-requirement level (6.4.1, 6.4.2, 6.4.3, and 11.6.1), and the appendices were added. FTC and Florida rows cite the statute or rule section (Part 464 read on eCFR as of 2026-09-23; Fla. Stat. 501.171 read on the Florida Legislature site).
2. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping**; no official NIST mapping from PCI DSS v4.0.1, Part 464, or Florida law was used.
3. **Evidence.** Current state was established from the intake evidence (user and security settings exported from every SaaS account, device settings, the processor's PCI portal, the merchant agreement, statements, and the Room walk-through on 2026-07-22) and the owner's written self-review, checked on screen with the IT consultant from 2026-07-27 to 2026-07-31 (EV-038). Fieldwork added a browser capture of the event pages (2026-07-28, EV-039), a search of the mailbox, phone, laptop, and cloud storage for card numbers (2026-07-28, EV-040), the export folder and sharing report (EV-042), a review of 20 social posts and 6 flyers (EV-046), a review of the merchant agreement (EV-047), and a walkthrough of the Room on a show night (2026-07-30, EV-048). Where the self-assessment tests had run (2026-07-29), their results are cited too. The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 0 | 3 | 2 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 1 | 2 | 0 | 3 |
| PCI Req 3 Stored account data | 1 | 1 | 2 | 3 | 7 |
| PCI Req 4 Transmission | 0 | 1 | 1 | 0 | 2 |
| PCI Req 5 Malware and phishing | 1 | 2 | 1 | 0 | 4 |
| PCI Req 6 Secure systems and software | 2 | 1 | 3 | 1 | 7 |
| PCI Req 7 Restrict access | 1 | 0 | 2 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 1 | 2 | 3 | 0 | 6 |
| PCI Req 9 Physical access and media | 2 | 1 | 1 | 1 | 5 |
| PCI Req 10 Logging | 1 | 3 | 3 | 0 | 7 |
| PCI Req 11 Security testing | 0 | 0 | 6 | 0 | 6 |
| PCI Req 12 Policies and programs | 0 | 2 | 5 | 3 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **9** | **17** | **31** | **11** | **68** |
| FTC Act Section 5 | 0 | 2 | 1 | 0 | 3 |
| FTC Rule on Unfair or Deceptive Fees | 2 | 1 | 1 | 0 | 4 |
| BOTS Act (applicability check) | 0 | 0 | 0 | 1 | 1 |
| Fla. Stat. 501.171 | 0 | 2 | 0 | 0 | 2 |
| **Total (78)** | **11** | **22** | **33** | **12** | **78** |

Of the 55 rows with gaps, 6 are rated High, 18 Moderate, and 31 Low. Of the 57 PCI DSS rows in scope, 48 have gaps. Many are the "processes documented and roles assigned" rows that open each requirement, which POL-01 (P06) closes, and many others leave scope once keyed phone orders and emailed card data stop.

## 4. Action list (half page)
In order. The first four cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Turn on MFA on SYS-01 and the website; unique passphrases in a password manager | G-035, G-034 | High | 2026-09-15 |
| 2 | Named sub-users for the assistant (marketing role) and door staff (scan-only role); remove the shared logins | G-033, G-030 | High | 2026-09-15 |
| 3 | Payment links instead of keyed phone orders; notice to fans never to send card details; delete on receipt | G-011, G-010 | High | 2026-09-30 |
| 4 | Remove the pixel and chat plugin from event pages; approved script list; monthly page check (SAQ A script criterion) | G-027, G-055 | High | 2026-09-30 |
| 5 | Adopt POL-01; adopt and walk through the P08 runbook with the processor's 24-hour notice term | G-056, G-065 | Moderate | 2026-09-30 |
| 6 | Total price in every post, email, flyer, and listing | G-072, G-073 | Moderate | 2026-09-30 |
| 7 | PCI scope description, provider responsibility list, and evidence folder; then sign the 2026 SAQ A | G-060, G-063 | Moderate | 2026-10-31 |
| 8 | Rewrite the privacy notice to match the tools actually used | G-069 | Moderate | 2026-10-31 |
| 9 | Guest network for crews; ask the processor in writing about external scans for SAQ A | G-003, G-008, G-052 | Moderate | 2026-10-31 |
| 10 | Monthly log review; security course for the owner | G-046, G-061 | Moderate | 2026-11-30 |

**Before signing the 2026 SAQ A:** complete actions 1 to 4 and 7, re-search the mailbox and phone for card data, and keep the evidence. If an eligibility item is still open on 2026-10-31, ask the processor which questionnaire to use rather than attesting SAQ A again. High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending changes and watch items
- **PCI DSS.** v4.0.1 is the version in effect; the analysis is updated when PCI SSC publishes a new version or a new SAQ A.
- **TICKET Act (H.R. 1402, 119th Congress).** A pending bill, not law (status as checked in the Small sample). It would add all-in pricing rules by statute. Not treated as a current obligation.
- **FTC enforcement.** The FTC has used Part 464 and the BOTS Act in live-event ticketing cases (see the Small sample's P03 for the cases). These show how the FTC reads the rules; they create no new duty.

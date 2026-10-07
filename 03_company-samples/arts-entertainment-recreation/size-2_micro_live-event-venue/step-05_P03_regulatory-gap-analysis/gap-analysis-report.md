# Regulatory Gap Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing; one music club) |
| Tier / Vertical | Micro / Arts, Entertainment, and Recreation |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024). A contractual standard enforced through the merchant agreements, **not law** (N71-R04) |
| Secondary regulation | FTC Act Section 5, 15 U.S.C. 45(a)(1) and 45(n), and the FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (both under N71-R05), plus a one-row applicability check of the BOTS Act, 15 U.S.C. 45c |
| Assessment dates | 2026-07-13 to 2026-07-24; evidence refreshed with P07 results through 2026-08-12 |
| Assessor | Venue Manager (Security and Privacy Lead) with the Box Office and Ticketing Manager, the Bookkeeper, the Marketing Coordinator, and the MSP account technician |
| Approved | Owner and General Manager, 2026-08-31 |

## 1. Applicability

### 1.1 PCI DSS applies by contract, at any size
The company accepts payment cards through two merchant accounts, and both merchant agreements require PCI DSS compliance. PCI SSC sets no size tiers and no small-business exemption. Merchant levels and validation rules come from the card brands and the acquirer, not from PCI SSC.

**Merchant level.** The acquirer's letter of 2026-06-08 (fictional) classifies the company as a **Visa Level 3 merchant**. That is consistent with Visa's own table: Visa's *What To Do If Compromised* (v10.0, effective 2026-06-25) lists Level 3 merchants as those with 1 to 1,000,000 Visa transactions a year, and notes that Visa merged its former Levels 3 and 4 into one Level 3 on 2024-04-25 without changing PCI DSS compliance requirements. The company runs about 31,000 Visa transactions a year across both accounts. Other brands' level definitions were not verified; the acquirer applies them.

**The company has never validated.** No SAQ has been filed for either account since 2023, and the acquirer has charged a monthly non-validation fee on each account since March 2024. The letter requires an SAQ and AOC for each account by 2026-12-15.

**Validation type, by payment channel.** This is the core applicability finding.

| Merchant account | Channel | How card data flows | SAQ fit |
|---|---|---|---|
| MID-F (bar and merchandise) | Card present at the bar | PCI-listed validated P2PE readers from the POS vendor; manual entry disabled | **SAQ P2PE**, as the portal pre-selected |
| MID-T (tickets) | Online | Patrons pay in the ticketing vendor's checkout widget, embedded in the company's own website event pages, or on vendor-hosted event pages | Could fit **SAQ A** only if every element of the payment form comes directly from the compliant provider and the company confirms its site is not open to script attacks. **Today it cannot confirm that:** 6 unmanaged scripts load on the event pages and the website login is shared with no MFA (G-027, G-055) |
| MID-T | Door sales | The payment partner's PCI-listed validated P2PE readers, paired with the door tablets | Fits **SAQ P2PE** on its own, if the P2PE instruction manual is followed (G-042) |
| MID-T | Phone orders (about 300 a year) | The Box Office and Ticketing Manager types the caller's card number into the box office web app on the back-office PC | Not SAQ A (not fully outsourced). Not SAQ C-VT, which needs an isolated device used only for the virtual terminal; this PC is used for email, browsing, and bookkeeping on a shared network |
| MID-T | Email (unplanned) | Patrons and corporate renters email card details to the box office mailbox | Card data stored electronically, including security codes (G-010, G-011). No reduced SAQ allows this |

The portal's **SAQ A pre-selection for MID-T is wrong** for the account as it runs today. It came from 2023 enrollment answers that described the account as "online only". As operated today, the honest choice for MID-T is **SAQ D for Merchants**, which covers nearly all of PCI DSS. That is why this analysis rates every requirement group.

**SAQs checked.** PCI SSC published the v4.0.1 SAQs on 2024-10-15 (PCI SSC bulletin) and revised SAQ A in January 2025. The revision, effective 2025-03-31, removed Requirements 6.4.3 and 11.6.1 from SAQ A and added an eligibility criterion instead: the merchant confirms its site is not susceptible to attacks from scripts that could affect its e-commerce systems (PCI SSC blog, 2025-01-30; FAQ 1588). The SAQ C-VT and SAQ A eligibility wording summarized above was read in the v4.0 SAQ documents. PCI SSC says the v4.0.1 editions clarified the A, A-EP, and C-VT criteria, so the Owner must re-read the current v4.0.1 criteria before signing any SAQ.

### 1.2 The scope decision (for the Owner by 2026-09-30)
| Option | What it takes | 2026 result |
|---|---|---|
| **A. Validate as-is with SAQ D for MID-T** | Close as many of the 56 PCI DSS gap rows as possible by 2026-12-15, including network separation, logging, intrusion detection, internal scans, and a penetration test | Almost certainly **Non-Compliant**. The SAQ attestation allows a Non-Compliant status with a target date, and the acquirer may ask for an action plan |
| **B. Reduce scope first (recommended)** | By 2026-09-30: (1) **stop taking card numbers by phone**: help callers buy online or send them a purchase link; (2) **never accept card numbers by email or on forms**: purge what exists (done 2026-08-03), auto-reply to senders, take rental deposits through a payment link; (3) **fix the website**: named logins with MFA, remove every script not needed on event pages, weekly page checks, or send buyers to the vendor-hosted event pages instead of embedding the widget; (4) keep door sales on the validated P2PE readers and follow the instruction manual | With the acquirer's agreement: SAQ A for online plus SAQ P2PE for door sales on MID-T, and SAQ P2PE for MID-F. No card number then touches a company computer, mailbox, or network |

**One condition before phone orders stop.** Today, wheelchair spaces and companion seats for seated shows, and spaces on the accessible viewing platform for standing shows, can be bought **only by phone**. The ADA ticketing rule requires that individuals with disabilities can buy tickets for accessible seating during the same hours, through the same methods of distribution, and in the same types of sales outlets, including telephone service, as other patrons (28 CFR 36.302(f)(1)(ii)). The Box Office and Ticketing Manager must put accessible tickets on sale online first, and the box office phone line stays open for questions and seat holds (no card numbers). Accessible seating questions are also part of P10.

Option B costs almost nothing (staff time and the payment link feature in the ticketing platform). **It does not remove the need for the other controls.** Network separation, anti-malware, logging, and testing remain part of reasonable security under FTC Act Section 5 (G-069) and stay in P01 and P07. The 17 rows that would leave MID-T scope carry a scope note in the `pending_rule_change` column. The final SAQ requirement lists decide the exact set.

### 1.3 Secondary regulation
- **FTC Act Section 5** applies with no size threshold. The FTC may treat broken privacy or security promises as deceptive (45(a)(1)). It may treat a practice as unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that benefits to consumers or competition do not outweigh (45(n)).
- **Rule on Unfair or Deceptive Fees, 16 CFR Part 464** (effective 2025-05-12). "Covered good or service" includes live-event tickets (464.1). "Total price" means the maximum total of all fees or charges a consumer must pay, excluding government charges, shipping charges, and optional items (464.1). Any business that offers, displays, or advertises a price must disclose the total price clearly and conspicuously (464.2(a)) and more prominently than other pricing information (464.2(b)). Before the patron pays, excluded fees and the final amount must be disclosed (464.2(c)). Fees may not be misrepresented (464.3). The rule reaches the company's own website, emails, and social posts, not just the vendor's checkout. The club's $3.50 service fee and $1.50 facility fee are mandatory, so both belong in every advertised price.
- **BOTS Act, 15 U.S.C. 45c.** It prohibits circumventing a ticket issuer's security measures or purchase limits and reselling tickets obtained that way. The company is a "ticket issuer" (the definition names venue operators), and its room exceeds the 200-person capacity in the "event" definition. The Act places **no compliance duty** on the company. It matters because the company's bot screening records are evidence for FTC or state attorney general enforcement (P10).

**Not applicable, with reasons:** Nevada Regulation 5.260, NIGC MICS, and the casino BSA/AML rules (N71-R01 to R03), because there is no gaming; COPPA (N71-R06), because the site is not directed to children and accounts require age 18 or older; CIRCIA (final rule not published); SEC disclosure (privately held). Florida breach notification (Fla. Stat. 501.171) is handled in P08, and the Florida ticket statute (Fla. Stat. 817.36) in P10.

## 2. Method
1. **Requirements.** PCI DSS was broken into its 12 principal requirements and their requirement groups (for example 8.2). The payment page requirements were taken to the defined-requirement level (6.4.1, 6.4.2, 6.4.3, and 11.6.1), and the appendices were added. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted. Read the requirement text in the official standard (the Venue Manager downloaded v4.0.1 from the PCI SSC document library under its license terms).
2. **FTC rows** cite the statute (uscode.house.gov) and the rule text (eCFR, Part 464 as of 2026-09-23).
3. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 or Part 464 to CSF 2.0 or SP 800-53 was used.
4. **Documentary evidence.** Each status rests on a named document or record: the acquirer letter and portal, merchant statements, the ticketing user, role, and API token lists, the ticketing security settings, the suite user export and MFA report, the MSP's firewall export, patch report, anti-malware console export, and backup report, a browser capture of an event page on 2026-07-21, a card-number search of the mailboxes and the back-office PC on 2026-07-22, a review of the rentals binder on 2026-07-23, the P2PE listings, and vendor contracts. Interviews covered all 7 employees, the web designer, and the MSP account technician. Two show nights (2026-07-17 and 2026-07-18) and an on-sale (2026-07-21) were observed.
5. **Status.** Met, Partially met, Not met, or Not applicable, **as of the end of fieldwork**. Actions completed since then are noted in the remediation column but do not change the status. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 0 | 3 | 2 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 1 | 2 | 0 | 3 |
| PCI Req 3 Stored account data | 1 | 0 | 4 | 2 | 7 |
| PCI Req 4 Transmission | 0 | 1 | 1 | 0 | 2 |
| PCI Req 5 Malware and phishing | 0 | 3 | 1 | 0 | 4 |
| PCI Req 6 Secure systems and software | 0 | 1 | 3 | 3 | 7 |
| PCI Req 7 Restrict access | 1 | 1 | 1 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 0 | 1 | 5 | 0 | 6 |
| PCI Req 9 Physical access and card readers | 0 | 2 | 3 | 0 | 5 |
| PCI Req 10 Logging | 0 | 2 | 5 | 0 | 7 |
| PCI Req 11 Security testing | 0 | 0 | 6 | 0 | 6 |
| PCI Req 12 Policies and programs | 0 | 3 | 5 | 2 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **2** | **18** | **38** | **10** | **68** |
| FTC Act Section 5 | 0 | 2 | 1 | 0 | 3 |
| FTC Rule on Unfair or Deceptive Fees | 1 | 1 | 2 | 0 | 4 |
| BOTS Act (applicability check) | 0 | 0 | 0 | 1 | 1 |
| **Total (76)** | **3** | **21** | **41** | **11** | **76** |

Of the 62 rows with gaps, 12 are rated High, 29 Moderate, and 21 Low. Of the 58 PCI DSS rows in scope, 56 have gaps. Many of them are the "processes documented and roles assigned" group that opens each requirement, which POL-02 to POL-04 (P06) begin to close.

**What the numbers say.** The company has done the two hardest things right without knowing it: online payments run in the vendor's widget and every card reader is a validated P2PE device. Almost every High gap comes from three habits around those good choices: card numbers taken by phone and email, shared logins with no MFA, and an unmanaged website around the payment form. Fixing those habits is cheaper than any technology purchase in this plan.

## 4. Priority gaps
| Gap | Row | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Card security codes kept in email | G-011 (3.3) | High | Purged 2026-08-03; never accept card numbers by email | Box Office and Ticketing Manager | 2026-09-15 |
| Unmanaged scripts on the pages that host the checkout widget | G-027 (6.4.3) | High | Remove them, or move buyers to vendor-hosted pages | Marketing Coordinator | 2026-09-30 |
| No change detection on those pages | G-055 (11.6.1) | High | Weekly page check and website change alerts | Marketing Coordinator | 2026-09-30 |
| Shared and stale logins | G-033 (8.2) | High | Named door and website logins; last-day checklist | Box Office and Ticketing Manager | 2026-09-30 |
| No MFA on ticketing, website, or MSP-held consoles | G-035 (8.4) | High | Enforce MFA everywhere it is offered | Venue Manager | 2026-09-30 |
| Advertised ticket prices omit mandatory fees | G-072 (464.2(a)) | High | Total price in every price display | Marketing Coordinator | 2026-09-30 |
| PCI scope undocumented; wrong SAQ pre-selected | G-060 (12.5) | High | Scope document; Owner decides Option B by 2026-09-30 | Owner and General Manager | 2026-10-31 |
| No log review | G-046 (10.4) | High | Weekly 20-minute check with a checklist | Venue Manager | 2026-10-31 |
| No vulnerability or ASV scans | G-052 (11.3) | High | Contract an ASV for the website; MSP internal scans | Venue Manager | 2026-10-31 |
| Back-office PC on a flat network | G-003 (1.3) | High | Option B removes card data from the PC; separate staff network in any case | Venue Manager | 2026-10-31 |
| No incident response plan | G-065 (12.10) | High | POL-03, the P08 runbook, and a tabletop | Venue Manager | 2026-11-30 |
| Security not yet reasonable for 47,000 patron records | G-069 (45(n)) | High | P01 treatments and the P07 POA&M | Venue Manager | 2026-12-31 |
| P2PE readers not inventoried or inspected | G-042 (9.5) | Moderate | Inventory, pre-show inspection, tamper briefing | Bar Manager | 2026-09-30 |
| Forgotten API token | G-037 (8.6) | Moderate | Revoked 2026-08-12; tokens in the monthly account check | Marketing Coordinator | 2026-09-30 |
| Privacy notice contradicted by pixels and the old integration | G-070 (45(a)(1)) | Moderate | Remove pixels from event pages; rewrite the notice | Marketing Coordinator | 2026-10-31 |
| Facility fee misdescribed in the FAQ | G-075 (464.3) | Moderate | Correct the FAQ and fee labels | Owner and General Manager | 2026-09-30 |

**Before signing the 2026 AOCs (due 2026-12-15):** complete Option B and close G-011, G-027, G-055, G-033, G-035, G-042, and G-060, or file SAQ D for MID-T with an honest Non-Compliant status and target dates. The Owner should not sign any SAQ answer without evidence in the Bookkeeper's SAQ folder.

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person club: most actions are settings, habits, and one-page procedures, not new systems. The MSP performs the network and computer work under the Venue Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Stop handling card data | 2026-09-15 | No card numbers by email or on forms (purge and shredding done 2026-08-03); auto-reply and website notice; deposits by payment link | G-010, G-011, G-013, G-017, G-041 |
| 2. Logins, pages, and prices | 2026-09-30 | Accessible tickets on sale online, then no card numbers by phone; MFA in the ticketing platform and website; named door and website logins; script removal and weekly page check; reader inventory and inspections; new staff Wi-Fi password; total-price displays and fee labels; policies acknowledged; Owner's scope decision | G-008, G-027, G-033, G-034, G-035, G-037, G-042, G-055, G-056, G-057, G-072, G-073, G-075, G-030 |
| 3. Scope, scanning, and network | 2026-10-31 | Scope document and data-flow diagram; ASV contract and first scan; separate staff network and crew Wi-Fi; weekly log check starts; change log; privacy notice rewrite; service provider list and AOCs | G-002 to G-005, G-007, G-024, G-028, G-046, G-047, G-052, G-060, G-063, G-070, G-071 |
| 4. Validate | 2026-12-15 | SAQs and AOCs for both accounts with ASV reports, signed only with evidence on file | G-060 |
| 5. Detection and response | 2026-12-31 | EDR with after-hours alerts; tabletop with the MSP; training and phishing simulations; targeted risk analyses; remaining procedure rows; a penetration test by 2027-03-31 only if Option A is chosen | G-019 to G-021, G-044, G-045, G-049, G-053, G-054, G-058, G-061, G-062, G-065, G-069, and the "processes documented" rows |

**Progress check.** The Venue Manager reports progress to the Owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending changes and watch items
- **PCI DSS.** v4.0.1 is the version in effect. No newer version was found on the PCI SSC standards page when this analysis was finalized. The analysis will be updated when PCI SSC publishes one.
- **TICKET Act (H.R. 1402, 119th Congress).** Passed the House on 2025-04-29 and was placed on the Senate calendar on 2025-09-16. It is **not law** (bill status checked on govinfo.gov on 2026-10-06; the record was last updated 2026-07-10). It would add all-in pricing rules by statute. Not treated as a current obligation.
- **BOTS Act enforcement.** Executive Order 14254 (2025-03-31) directs the FTC to enforce the BOTS Act rigorously. This raises the value of keeping bot screening evidence (P10) but adds no duty for the company.

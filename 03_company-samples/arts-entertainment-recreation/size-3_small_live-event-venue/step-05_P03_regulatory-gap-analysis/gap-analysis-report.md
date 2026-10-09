# Regulatory Gap Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing, one venue building with two rooms) |
| Tier / Vertical | Small / Arts, Entertainment, and Recreation |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024). A contractual standard enforced through the merchant agreement, **not law** (N71-R04) |
| Secondary regulation | FTC Act Section 5, 15 U.S.C. 45(a)(1) and 45(n), and the FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (both under N71-R05), plus a one-row applicability check of the BOTS Act, 15 U.S.C. 45c |
| Assessment dates | 2026-07-13 to 2026-07-24; evidence refreshed with P07 results through 2026-08-07 |
| Assessor | IT Manager (Information Security Lead) with the Controller, the Director of Ticketing, and the Marketing Director |
| Approved | General Manager, 2026-08-31 |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the result for the rules analyzed here.

### 1.1 PCI DSS applies by contract
The company accepts payment cards through two merchant accounts, and its merchant agreement requires PCI DSS compliance. PCI SSC sets no size tiers. Merchant levels and validation rules come from the card brands and the acquirer, not from PCI SSC.

**Merchant level.** The acquirer's letter of 2026-05-18 (fictional) classifies the company as a **Visa Level 3 merchant**. That is consistent with Visa's own table: Visa's *What To Do If Compromised* (v10.0, effective 2026-06-25) lists Level 3 merchants as those with 1 to 1,000,000 Visa transactions a year, and notes that Visa merged its former Levels 3 and 4 into one Level 3 on 2024-04-25 without changing PCI DSS compliance requirements. The company runs about 335,000 Visa transactions a year across both accounts. Other brands' level definitions were not verified; the acquirer applies them.

**Validation type, by payment channel.** This is the core applicability finding.

| Merchant account | Channel | How card data flows | SAQ fit |
|---|---|---|---|
| MID-F (food, beverage, merchandise) | Card present at bars and stands | PCI-listed validated P2PE readers; card data encrypted in the device; the company holds no keys | **SAQ P2PE**, confirmed by the acquirer |
| MID-T (tickets) | Online | Patrons follow "Buy tickets" links from the company website to checkout pages hosted by the ticketing vendor (EV-029) | Could fit **SAQ A** only if every element of the payment page comes from the compliant provider and the company confirms its site is not open to script attacks. **Today it fails:** the company adds 9 third-party scripts to the checkout page (G-027) |
| MID-T | Box office windows | USB card readers attached to box office PCs. The readers encrypt, but they are **not part of a PCI-listed validated P2PE solution** | No reduced SAQ. The PCs and their network are in scope |
| MID-T | Phone orders | Staff type the caller's card number into the box office web app on the PCs | Not SAQ A (not fully outsourced). Not SAQ C-VT, which needs an isolated device used only for the virtual terminal with no attached card readers. These PCs are on the shared corporate segment and are used for email and browsing |

Because one merchant account (MID-T) combines all three ticket channels, the acquirer required **SAQ D for Merchants** for MID-T in 2026. The 2025 SAQ A for MID-T should not have been filed (G-060). SAQ D covers nearly all of PCI DSS, which is why this analysis rates every requirement group.

**SAQs checked.** PCI SSC published the v4.0.1 SAQs on 2024-10-15 (PCI SSC bulletin) and revised SAQ A in January 2025. The revision, effective 2025-03-31, removed Requirements 6.4.3 and 11.6.1 from SAQ A and added an eligibility criterion instead: the merchant confirms its site is not susceptible to attacks from scripts that could affect its e-commerce systems (PCI SSC blog, 2025-01-30; FAQ 1588). The SAQ C-VT and SAQ A eligibility wording summarized above was read in the v4.0 SAQ documents. PCI SSC says the v4.0.1 editions clarified the A, A-EP, and C-VT criteria, so the Controller must re-read the current v4.0.1 criteria before signing any SAQ.

### 1.2 The scope decision (for the majority owner by 2026-09-30)
| Option | What it takes | 2026 result |
|---|---|---|
| **A. Validate as-is with SAQ D** | Close as many of the 54 PCI DSS gap rows as possible by 2026-12-15, including segmentation, logging, intrusion detection, internal scans, ASV scans, and a penetration test | Almost certainly **Non-Compliant**. The SAQ attestation allows a Non-Compliant status with a target date, and the acquirer may ask for an action plan (Part 4 of the AOC) |
| **B. Reduce scope first (recommended)** | By 2026-11-15: replace the 4 USB readers with the payment partner's **validated P2PE devices**, which also accept key-entered phone orders, so no card number touches a PC; shred the slips; remove all company-added scripts from checkout and get the vendor's written confirmation of script protection (FAQ 1588) | With the acquirer's agreement (offered in its letter): SAQ P2PE for the box office and phone channels plus SAQ A for online. The 20 rows below that carry a scope note then leave MID-T scope |

Option B costs about $6,500 (6 devices and setup, fictional) and removes the 6 PCs and the corporate segment from PCI scope. **It does not remove the need for those controls.** Network separation, anti-malware, logging, and scanning remain part of reasonable security under FTC Act Section 5 (G-069) and stay in P01 and P07. Those 20 rows carry a scope note in the `pending_rule_change` column. The final SAQ requirement lists decide the exact set.

### 1.3 Secondary regulation
- **FTC Act Section 5** applies with no size threshold. The FTC may treat broken privacy or security promises as deceptive (45(a)(1)). It may treat a practice as unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that benefits to consumers or competition do not outweigh (45(n)).
- **Rule on Unfair or Deceptive Fees, 16 CFR Part 464** (90 FR 2066, published 2025-01-10, effective 2025-05-12). "Covered good or service" includes live-event tickets (464.1). Any business that offers, displays, or advertises a price must disclose the total price clearly and conspicuously (464.2(a)) and more prominently than other pricing information (464.2(b)). Before the patron pays, excluded fees and the final amount must be disclosed (464.2(c)). Fees may not be misrepresented (464.3). The rule reaches the company's own website and emails, not just the vendor's checkout. The FTC has already used it on live-event tickets: StubHub agreed to pay $10 million on 2026-04-09 over fee disclosures from 2025-05-12 to 2025-05-14 (FTC press release).
- **BOTS Act, 15 U.S.C. 45c.** It prohibits circumventing a ticket issuer's security measures or purchase limits and reselling tickets obtained that way. The company is a "ticket issuer" (the definition names venue operators) and its rooms exceed the 200-person capacity in the "event" definition. The Act places **no compliance duty** on the company. It matters because the company's bot detection records are evidence for FTC or state attorney general enforcement (P10). Executive Order 14254 (2025-03-31) directs the FTC to enforce the BOTS Act rigorously. The FTC brought BOTS Act cases against ticket brokers in August 2025 and July 2026 (Elite Events and Tickets, 2026-07-27).

**Not applicable, with reasons:** Nevada Regulation 5.260, NIGC MICS, and the casino BSA/AML rules (N71-R01 to R03), because there is no gaming; COPPA (N71-R06), because the site is not directed to children and accounts require age 18 or older; CIRCIA (final rule not published); SEC disclosure (privately held). Florida breach notification (Fla. Stat. 501.171) is handled in P08, and the Florida ticket resale statute (Fla. Stat. 817.36) in P10.

## 2. Method
1. **Requirements.** PCI DSS was broken into its 12 principal requirements and their requirement groups (for example 8.2). The payment page requirements were taken to the defined-requirement level (6.4.1, 6.4.2, 6.4.3, and 11.6.1), and the appendices were added. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted. Read the requirement text in the official standard (the company holds a licensed copy of v4.0.1). No newer PCI DSS version was found on the PCI SSC standards page on 2026-09-26.
2. **FTC rows** cite the statute (uscode.house.gov) and the rule text (eCFR, Part 464 as of 2026-09-23).
3. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 or Part 464 to CSF 2.0 or SP 800-53 was used.
4. **Evidence.** Current state was established from the intake evidence (configuration exports, the 2025 SAQs (EV-022), the merchant agreement (EV-023), the acquirer letter (EV-021), and the vendor AOCs and SOC 2 report (EV-025 to EV-027)), the firewall rule export (EV-051), a refreshed ticketing user export (EV-055), observation of an on-sale on 2026-07-17 (EV-052) and a show night on 2026-07-18 (EV-053), the reader reconciliation (EV-054), page captures including the checkout browser capture on 2026-07-21 (EV-056, EV-057), a TLS test (EV-058), a card-number search of box office PCs and file shares on 2026-07-22 (EV-059), and gap analysis interviews (EV-061) with the majority owner, General Manager, Controller, Director of Ticketing, Marketing Director, Food and Beverage Manager, box office staff, the marketing agency, and the integrator. The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 0 | 3 | 2 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 1 | 2 | 0 | 3 |
| PCI Req 3 Stored account data | 1 | 1 | 2 | 3 | 7 |
| PCI Req 4 Transmission | 0 | 1 | 1 | 0 | 2 |
| PCI Req 5 Malware and phishing | 0 | 3 | 1 | 0 | 4 |
| PCI Req 6 Secure systems and software | 0 | 1 | 3 | 3 | 7 |
| PCI Req 7 Restrict access | 1 | 1 | 1 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 0 | 1 | 5 | 0 | 6 |
| PCI Req 9 Physical access and card readers | 0 | 2 | 3 | 0 | 5 |
| PCI Req 10 Logging | 0 | 2 | 5 | 0 | 7 |
| PCI Req 11 Security testing | 0 | 0 | 6 | 0 | 6 |
| PCI Req 12 Policies and programs | 1 | 4 | 3 | 2 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **3** | **20** | **34** | **11** | **68** |
| FTC Act Section 5 | 0 | 2 | 1 | 0 | 3 |
| FTC Rule on Unfair or Deceptive Fees | 1 | 1 | 2 | 0 | 4 |
| BOTS Act (applicability check) | 0 | 0 | 0 | 1 | 1 |
| **Total (76)** | **4** | **23** | **37** | **12** | **76** |

Of the 60 rows with gaps, 12 are rated High, 29 Moderate, and 19 Low. Of the 57 PCI DSS rows in scope, 54 have gaps. Many of them are the "processes documented and roles assigned" group that opens each requirement, which POL-01 to POL-05 (P06) begin to close.

## 4. Priority gaps and roadmap
| Gap | Row | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Card security codes written on phone-order slips | G-011 (3.3) | High | Stop at once; shred all slips under witness; take phone payments live | Director of Ticketing | 2026-09-15 |
| Company-added scripts on the checkout page | G-027 (6.4.3) | High | Remove them; limit marketing settings to event pages | Marketing Director | 2026-09-30 |
| No checkout change or tamper detection | G-055 (11.6.1) | High | Vendor alerts on setting changes; written script-protection confirmation for SAQ A | Marketing Director | 2026-09-30 |
| Shared and stale ticketing accounts | G-033 (8.2) | High | Disable them; named seasonal accounts; same-day removal | Director of Ticketing | 2026-09-30 |
| No MFA on the ticketing platform or remote support tool | G-035 (8.4) | High | Enforce MFA for all 34 venue users and remote tools | IT Manager | 2026-09-30 |
| Advertised ticket prices omit mandatory fees | G-072 (464.2(a)) | High | Total price in every website, email, and social price display | Marketing Director | 2026-09-30 |
| PCI scope undocumented; 2025 SAQ A misfiled | G-060 (12.5) | High | Scope document; owner decision on Option B by 2026-09-30 | Controller | 2026-10-31 |
| No vulnerability or ASV scans | G-052 (11.3) | High | Contract an ASV; quarterly internal scans | IT Manager | 2026-10-31 |
| Box office PCs not segmented | G-003 (1.3) | High | Option B removes card data from the PCs; fallback is a dedicated segment | IT Manager | 2026-11-15 |
| No log review | G-046 (10.4) | High | Alerts on new admins, checkout changes, bulk exports | IT Manager | 2026-11-30 |
| No incident response plan | G-065 (12.10) | High | POL-03, the P08 runbook, and a tabletop | IT Manager | 2026-11-30 |
| Security not yet reasonable for 260,000 patron records | G-069 (45(n)) | High | P01 treatments and the P07 POA&M | IT Manager | 2027-01-31 |
| Full-admin API key in the export function | G-037 (8.6) | Moderate | Read-only scoped key in the key vault | IT Manager | 2026-10-15 |
| P2PE reader inventory short by 2 | G-042 (9.5) | Moderate | Report to the POS vendor; pre-event inspections | Food and Beverage Manager | 2026-09-30 |
| Privacy notice contradicted by checkout scripts | G-070 (45(a)(1)) | Moderate | Remove scripts; rewrite the notice | Marketing Director | 2026-10-31 |
| Fee purpose misdescribed in the FAQ | G-075 (464.3) | Moderate | Correct the FAQ and fee labels | Controller | 2026-09-30 |

**Before signing the 2026 AOCs (due 2026-12-15):** close G-011, G-027, G-055, G-033, G-035, and G-060, and complete Option B, or file SAQ D for MID-T with an honest Non-Compliant status and target dates. The majority owner should not sign any SAQ answer without evidence in the Controller's file.

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes and watch items
- **PCI DSS.** v4.0.1 is the version in effect. The analysis will be updated when PCI SSC publishes a new version.
- **TICKET Act (H.R. 1402, 119th Congress).** Passed the House on 2025-04-29 and was placed on the Senate calendar on 2025-09-16. It is **not law** (bill status checked on govinfo.gov, last updated 2026-07-10). It would add all-in pricing and speculative-ticket rules by statute. Not treated as a current obligation.
- **FTC v. Live Nation Entertainment and Ticketmaster** (filed 2025-09-18, C.D. Cal., with seven states). The complaint alleges deceptive advertised prices, deception about the enforcement of posted ticket limits, and BOTS Act violations. These are allegations, not findings, but they show why a posted limit must match how it is enforced (G-071).
- **FTC proposed rules on fees in other industries** (rental housing, 2026-03-13; online food delivery, 2026-04-16) are proposals for other sectors and do not change Part 464.

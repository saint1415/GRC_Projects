# Regulatory Gap Analysis: Cris Santos Company Holdings | Retail Trade | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Retail Trade (focus division: Grocery Retail) |
| Primary standard (focus division) | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024). A contractual standard enforced through the merchant agreement and card brand rules, **not law** (N44-45-R01) |
| Division rule sets | Financial Services: FTC Safeguards Rule (16 CFR Part 314, N44-45-R03) with Red Flags, Reg P, Reg V, FCRA, Reg B, and Reg Z rows. Grocery Wholesale: applicability findings for the wholesale vertical's primary rule, FDA record availability, PCI DSS for portal payments, FTC Act Section 5, and a NIST CSF 2.0 benchmark |
| Gap tables | `gap-analysis.csv` (Grocery Retail, 80 rows); `gap-analysis-grocery-wholesale.csv` (29 rows); `gap-analysis-financial-services.csv` (42 rows) |
| Assessment dates | 2026-05-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-31) |
| Assessors | Division security and compliance leads, the Financial Services chief compliance officer, and group legal, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit. The QSA was not involved; this is the internal pre-assessment before the 2026 ROC |

## 1. Applicability
### 1.1 What binds each division, at this size
| Division | Rule | Why it applies (or not) |
|---|---|---|
| Grocery Retail | PCI DSS v4.0.1 | The division accepts payment cards under a merchant agreement that requires compliance. PCI SSC sets no size tiers; the card brands do. Visa assigns **Level 1** to merchants with more than 6 million Visa transactions a year across all channels and requires an annual ROC by a QSA (or an internal resource if signed by an officer) and an AOC (Visa compliance validation page, checked 2026-10-04). The division handles about 257 million card transactions a year, and the acquirer confirmed Level 1 and a QSA ROC (letter of 2026-02-02, fictional) |
| Grocery Retail | FTC Act Section 5; FACTA | No size threshold (15 U.S.C. 45(a), 45(n); 15 U.S.C. 1681c(g)) |
| Grocery Retail | SNAP | Every store is an authorized SNAP retailer (7 CFR 278.1). EBT cards are not payment brand cards, so PCI DSS does not reach them by itself |
| Grocery Retail | Reg V affiliate marketing | The division uses Rewards Card eligibility information from its affiliate for marketing (12 CFR 1022.20(a) coverage; 1022.21) |
| Financial Services | FTC Safeguards Rule | "A retailer that extends credit by issuing its own credit card directly to consumers is a financial institution" (16 CFR 314.2(h)(2)(i)). Financial Services holds customer information on far more than 5,000 consumers, so the 314.6 exceptions do not apply |
| Financial Services | Red Flags Rule | Credit card accounts are covered accounts (16 CFR 681.1(b)(3)(i)); the division is a creditor under FTC FCRA enforcement (681.1(a)) |
| Financial Services | Reg P, Reg V, Reg B, Reg Z, FCRA, FTC Disposal Rule | CFPB regulations for a non-bank card issuer and lender (Reg P scope, 12 CFR 1016.1(b)); FCRA duties as a user of consumer reports; disposal of consumer report information (16 CFR 682.3) |
| Grocery Wholesale | NIST SP 800-171 through CMMC and DFARS 252.204-7012 (the wholesale vertical's primary rule) | **Does not apply.** The division has no DoD or federal contracts and handles no FCI or CUI. The vertical profile says wholesalers without defense business should benchmark against NIST CSF 2.0 (or CISA CPGs) instead, which this analysis does |
| Grocery Wholesale | FDA record availability | The distribution centers hold food, so records must be available within 24 hours of an FDA request (21 CFR 1.361; 21 CFR 1.1455(c) for listed foods). The food defense rule does not apply: 21 CFR 121.5(b) exempts the holding of food except in liquid storage tanks |
| Grocery Wholesale | PCI DSS v4.0.1 | Its own merchant account for portal invoice payments, validated by self-assessment (SAQ A) |
| Group | SEC Reg S-K Item 106; Form 8-K Item 1.05 | Publicly traded SEC registrant (N52-R08) |

**Not applicable, with reasons:** HIPAA (no pharmacies, a standing group decision); CCPA (no California business; GLBA data would also be exempt at the data level, Civ. Code 1798.145(e)); NYDFS Part 500 (no New York license); the Florida Digital Bill of Rights (the group has more than $1 billion in revenue but meets none of the online advertising, smart speaker, or app store tests in Fla. Stat. 501.702); COPPA (not directed to children; members 18 or older); INFORM Consumers Act (no third-party sellers); CTPAT (voluntary; not a member).

### 1.2 Why the Rewards Card falls between two programs
The Rewards Card is a private-label card that works only at group stores. It is not a payment brand card, so **PCI DSS does not cover it**. It is **customer information** of Financial Services, which the Safeguards Rule defines to include records "handled or maintained by or on behalf of you or your affiliates" (16 CFR 314.2). On the online checkout, customers type the Rewards Card number and code into a company-hosted field on the retail page, outside the processor's hosted payment fields. Before this analysis, the retail PCI program treated the field as out of scope and the Financial Services Safeguards program never looked at a retail page. Rows G-060 (PCI 12.5), FS-G07 (314.4(c)(2)), and FS-G09 (314.4(c)(4)) record the gap from both sides.

### 1.3 Why the retail scope is large
The PIN pads encrypt card data under the processor's encryption solution, but that solution is **not a PCI-listed validated P2PE solution**, so lanes, store controllers, POS networks, and the payment switch stay in scope. Online, the processor's hosted payment fields keep card data out of the storefront, but the checkout page around them is still a payment page under 6.4.3 and 11.6.1. These two choices explain why most retail rows apply.

**Lending licenses (context, not cyber rules).** Financial Services lends under state licenses, for example Florida's retail installment seller license (Fla. Stat. 520.32(1)) and consumer finance license (Fla. Stat. 516.02). Licensing is not scored here; the security duties for the same customer data are the FTC Safeguards Rule rows in this analysis (see `00_company-facts.md`).

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Grocery Retail | Grocery Wholesale | Financial Services | Group (corporate) |
|---|---|---|---|---|
| N44-45-R01 PCI DSS v4.0.1 | **Primary.** Level 1 merchant; QSA ROC | Applies to the portal payment page (SAQ A) | Applies to the cardholder portal bill payment page (SAQ A); the Rewards Card itself is outside PCI DSS | Common controls in the PCI responsibility matrix |
| N44-45-R02 FTC Act Section 5 | Applies (privacy statements, account security, pricing claims) | Applies (N42-R01; portal terms) | Applies (non-bank) | Applies |
| N44-45-R03 FTC Safeguards Rule | Applies **through Financial Services** for the Rewards Card field and CDP copies | Not applicable (not a financial institution) | **Primary.** Retailer-issued credit card (314.2(h)(2)(i)) | Group SOC and identity act as affiliate service providers (314.4(f)) |
| N44-45-R04 Red Flags Rule | Not applicable (no covered accounts) | Not applicable (business customers on invoice terms; counsel's 2026 review found no covered accounts) | Applies | Not applicable |
| N44-45-R05 FACTA truncation | Applies | Not applicable (no printed card receipts) | Not applicable (the division prints no card receipts) | Not applicable |
| N44-45-R06 CCPA | Not applicable | Not applicable | Not applicable | Not applicable |
| N44-45-R07 COPPA; N44-45-R08 INFORM | Not applicable | Not applicable | Not applicable | Not applicable |
| Reg V affiliate marketing (12 CFR 1022.21) | Applies (uses eligibility information) | Not applicable | Applies (provides notice and opt-out) | Group Chief Privacy Officer coordinates |
| Reg P, Reg B, Reg Z, FCRA, FTC Disposal Rule | Not applicable | Not applicable | Applies | Not applicable |
| SNAP (7 CFR 278.1) | Applies (380 authorized stores) | Not analyzed (no SNAP sales) | Not applicable | Not applicable |
| FDA record availability (21 CFR 1.361; 1.1455(c)) | Stores receive traceability records (not analyzed here) | **Applies** | Not applicable | ERP holds part of the records |
| CMMC, DFARS, FAR clauses (N42-R02 to N42-R05) | Not applicable | Not applicable (no federal contracts) | Not applicable | Not applicable |
| N52-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Same, for sole proprietor customers' personal cards | Same, plus the FTC notice | Coordinates (P08) |
| Contracts | Merchant agreement (24-hour notice; ROC each December 15) | Supply agreements (72-hour notice); SOC 2 requests | Card platform processing agreement | Intercompany service and data agreements |

## 3. Method
1. **Requirements.** PCI DSS rows follow the standard's 12 principal requirements and their requirement groups, with 6.4 split into its three defined requirements and 11.6 shown as 11.6.1, plus the three appendices. **Labels are short topics written for this analysis, not PCI SSC text**, because PCI DSS is copyrighted; read the requirement text in the group's licensed copy of v4.0.1. Federal rows (16 CFR 314.4, 681.1, 682.3; 12 CFR 1002.9, 1016.4, 1016.5, 1016.10, 1022.21, 1026.12, 1026.13; 21 CFR 1.361, 1.1455, 121.5; 7 CFR 278.1) were read on the eCFR (current through 2026-09-23). FCRA and FTC Act rows cite the U.S. Code. The Visa level was read on Visa's compliance validation page on 2026-10-04.
2. **Crosswalk.** Each PCI DSS and federal row carries an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5; no official NIST mapping from PCI DSS v4.0.1 was used. The wholesale benchmark rows are CSF 2.0 subcategories themselves, with SP 800-53 references taken from the NIST crosswalk.
3. **Evidence.** Interviews with each division's security, compliance, legal, digital, and operations leads; document review (2025 ROC and AOC, 2025 SAQ A for the wholesale merchant account, the Safeguards program and 2025 Qualified Individual report, contracts); configuration exports; browser captures of all four payment pages on 2026-07-28 and 2026-07-29; data discovery results; a 120-notice adverse action sample; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 scale.

## 4. Results
### 4.1 Grocery Retail: PCI DSS v4.0.1 and other retail rules (`gap-analysis.csv`)
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 3 | 2 | 0 | 0 | 5 |
| PCI Req 2 Secure configurations | 2 | 1 | 0 | 0 | 3 |
| PCI Req 3 Stored account data | 5 | 1 | 1 | 0 | 7 |
| PCI Req 4 Transmission | 2 | 0 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 4 | 0 | 0 | 0 | 4 |
| PCI Req 6 Secure systems and software | 4 | 2 | 1 | 0 | 7 |
| PCI Req 7 Restrict access | 3 | 0 | 0 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 4 | 2 | 0 | 0 | 6 |
| PCI Req 9 Physical access and PIN pads | 4 | 1 | 0 | 0 | 5 |
| PCI Req 10 Logging | 5 | 2 | 0 | 0 | 7 |
| PCI Req 11 Security testing | 4 | 2 | 0 | 0 | 6 |
| PCI Req 12 Policies and programs | 4 | 4 | 0 | 2 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **44** | **17** | **2** | **5** | **68** |
| FTC Act Section 5 | 1 | 3 | 0 | 0 | 4 |
| FACTA, SNAP | 2 | 0 | 0 | 0 | 2 |
| Reg V affiliate marketing | 0 | 0 | 1 | 0 | 1 |
| State breach notification laws | 0 | 1 | 0 | 0 | 1 |
| CCPA, Florida Digital Bill of Rights, COPPA, INFORM | 0 | 0 | 0 | 4 | 4 |
| **Total (80)** | **47** | **21** | **3** | **9** | **80** |

Of the 24 rows with gaps, 5 are rated High, 18 Moderate, and 1 Low.

**The program is mature where it has always been tested.** 44 of 63 applicable PCI DSS rows are Met: encryption, keys, malware, access control, physical security, scanning, and penetration testing. The gaps fall in three places:
- **Payment pages** (6.4.3 Not met; 6.5 and 11.6.1 Partially met, all High). Three scripts on the web checkout came from an "all pages" tag container and are not in the March 2026 inventory. Tamper detection covers the web checkout only, and its alerts go to a mailbox reviewed weekly. 11.6.1 allows evaluation at least once every seven days, so weekly review is the floor; for the group's top risk it is not enough.
- **The 46 acquired stores** (1.2, 1.3, 2.2, 6.3, 8.4, 9.5, 10.2, 10.4, 11.4). Flat networks, password-only back office access, late patches, missing logs, and no segmentation test. Before the QSA closes fieldwork, the group must fix these or agree with the acquirer how the stores are validated.
- **Scope and stray data** (3.2 Not met; 3.5 and 12.5 Partially met). About 31,000 card numbers in acquired settlement exports sat on a finance file share outside the CDE. 12.10.7 procedures were followed once found.

### 4.2 Grocery Wholesale (`gap-analysis-grocery-wholesale.csv`)
| Rule set | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| Wholesale vertical primary rule and federal clauses (CMMC, DFARS, FAR), CTPAT | 0 | 0 | 0 | 5 | 5 |
| FDA (21 CFR 1.361; 1.1455(c); 121.5(b)) | 0 | 2 | 0 | 1 | 3 |
| PCI DSS v4.0.1 (portal payments) | 0 | 2 | 2 | 0 | 4 |
| FTC Act Section 5 and customer contracts | 0 | 3 | 0 | 0 | 3 |
| NIST CSF 2.0 benchmark | 2 | 9 | 3 | 0 | 14 |
| **Total (29)** | **2** | **16** | **5** | **6** | **29** |

**Not met:** the portal payment page's SAQ A eligibility criterion was attested in 2025 without evidence, and the page loads the shared tag container (WD-G09); no tamper detection on that page (WD-G10); always-on OT vendor access (WD-G21, PR.AA-05); flat routes between IT and OT (WD-G24, PR.IR-01); no OT network monitoring (WD-G25, DE.CM-01).

**Food Traceability Rule date.** FDA proposed extending the compliance date from 2026-01-20 to 2028-07-20 (90 FR 38084, 2025-08-07). This analysis did not confirm that the extension was finalized, so the division plans as if 21 CFR 1.1455(c) applies now. Either way, 21 CFR 1.361 already requires records within 24 hours of an FDA request in a serious adulteration case.

### 4.3 Financial Services (`gap-analysis-financial-services.csv`)
| Rule | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| FTC Safeguards Rule (16 CFR 314.4, 314.6) | 12 | 11 | 1 | 2 | 26 |
| FTC Red Flags Rule (16 CFR 681.1) | 2 | 1 | 0 | 0 | 3 |
| Reg P (12 CFR 1016) | 3 | 0 | 0 | 0 | 3 |
| Reg V (12 CFR 1022.21) | 0 | 1 | 0 | 0 | 1 |
| FCRA (15 U.S.C. 1681b, 1681m(a)) | 2 | 0 | 0 | 0 | 2 |
| Reg B (12 CFR 1002.9) | 1 | 0 | 1 | 0 | 2 |
| Reg Z (12 CFR 1026.12(b), 1026.13) | 1 | 1 | 0 | 0 | 2 |
| FTC Disposal Rule (16 CFR 682.3) | 1 | 0 | 0 | 0 | 1 |
| PCI DSS (bill payment page) | 0 | 1 | 0 | 0 | 1 |
| CCPA | 0 | 0 | 0 | 1 | 1 |
| **Total (42)** | **22** | **15** | **2** | **3** | **42** |

**Not met:** the FTC notice for a notification event involving at least 500 consumers, due no later than 30 days after discovery (16 CFR 314.4(j)), has no procedure, owner, or place in the matrix (FS-G25); and adverse action reasons were not revalidated after the model was retrained: 11 of 120 sampled notices gave a first reason that did not match the model's main factor (12 CFR 1002.9(b)(2), FS-G37).

**High, Partially met:** the Rewards Card data flows on the retail checkout and in the CDP are outside the Financial Services data inventory (314.4(c)(2)), and the retail checkout, an externally developed application handling its customer information, was never evaluated (314.4(c)(4)).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Payment page scripts and tamper detection across divisions (1) | GR, GW, FS | PCI DSS 6.4.3, 6.5, 11.6.1; SAQ A eligibility | High | Payment-pages-only tag container; monitoring on all four payment pages with alerts to the SOC | Group digital director | 2026-11-30 |
| 2 | Rewards Card field between programs (2) | GR, FS | 16 CFR 314.4(c)(2), (c)(4); PCI DSS 12.5.2 | High | Isolated Rewards Card frame run by Financial Services; joint evaluation until then | Financial Services CISO | 2027-03-31 |
| 3 | FTC notice and cross-division notification (10) | All | 16 CFR 314.4(h), (j); merchant agreement; Fla. Stat. 501.171; Form 8-K Item 1.05 | High | P08 matrix rows with owners and clocks; tabletop | Group General Counsel | 2026-12-15 |
| 4 | Adverse action reasons from the credit model (8) | FS | 12 CFR 1002.9(b)(2); 15 U.S.C. 1681m(a) | High | Revalidate reason codes; regression tests; council approval (P10) | Financial Services chief credit officer | 2026-12-31 |
| 5 | Acquired stores in the CDE (3) | GR | PCI DSS 1.3, 8.4, 6.3, 10.4, 11.4 | High | Segment, MFA, patch, onboard, test before ROC fieldwork closes | Grocery Retail CISO | 2026-11-15 |
| 6 | Distribution center OT (6) | GW | CSF 2.0 PR.AA-05, PR.IR-01, DE.CM-01 | High | Vendor access through PAM; industrial demilitarized zones; OT monitoring | Grocery Wholesale security and compliance lead | 2027-03-31 |
| 7 | Stray card numbers and scope confirmation (4) | GR | PCI DSS 3.2, 3.5, 12.5.2 | Moderate | Delete; extend discovery to finance shares; re-confirm scope | Grocery Retail CISO | 2026-10-31 |
| 8 | Affiliate marketing opt-outs (5) | GR, FS | 12 CFR 1022.21; 15 U.S.C. 45(a)(1) | Moderate | Daily opt-out feed; exception rules per campaign | Group Chief Privacy Officer | 2026-12-31 |
| 9 | Service provider oversight (third parties) | All | PCI DSS 12.8; 16 CFR 314.4(f)(2)-(3) | Moderate | Complete the TPSP list; Safeguards-based card platform review; amend the intercompany agreement | Group Chief Risk Officer | 2027-03-31 |
| 10 | Program governance at Financial Services (11) | FS | 16 CFR 314.4(g), (i) | Moderate | Re-issue the supplement; 2026 Qualified Individual report covers service providers | Financial Services CISO | 2026-12-31 |
| 11 | Inheritance documentation (9) | GW, FS | 16 CFR 314.4(d)(1); SOC 2 readiness | Moderate | Inheritance matrices for SYS-D5 and SYS-D6 | Group CISO | 2026-12-31 |
| 12 | FDA record availability during an outage | GW | 21 CFR 1.361; 1.1455(c) | Moderate | 24-hour retrieval drill; full-volume WMS restore | Grocery Wholesale food safety director | 2027-03-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-021 to POAM-023 trace directly to this analysis).

**Before the 2026 ROC fieldwork (2026-10-19):** close or show substantial progress on rows G-003, G-027, G-028, G-035, G-055, and G-060, and agree with the QSA and the acquirer how the 46 acquired stores will be treated. A requirement that is not in place at the time of the ROC is reported as such; compensating controls need the QSA's review.

## 6. Pending changes and watch items
- **PCI DSS.** v4.0.1 remains current. PCI SSC ran a request for comments (June to July 2026) toward the next version. Rows carry this in `pending_rule_change`.
- **FDA Food Traceability Rule.** Compliance date extension proposed (90 FR 38084); final status not confirmed (section 4.2).
- **FTC.** The 2024 surveillance pricing 6(b) study is a study, not a rule; it is relevant to the pricing engine (P10). No FTC rule on pricing algorithms is treated as an obligation.
- **CIRCIA.** Reporting is not in effect (final rule not published as of 2026-09-25).
- None of these is treated as a current obligation, except where section 4.2 explains the conservative planning choice.

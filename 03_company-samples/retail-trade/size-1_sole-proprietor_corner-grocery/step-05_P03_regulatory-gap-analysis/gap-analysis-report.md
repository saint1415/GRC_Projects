# Regulatory Gap Analysis: Cris Santos Company | Retail Trade | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (corner grocery with online and phone ordering) |
| Tier / Vertical | Sole Proprietorship / Retail Trade |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024). A contractual standard enforced through the merchant agreement, **not law** (N44-45-R01) |
| Secondary rules | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n) (N44-45-R02); FACTA receipt truncation, 15 U.S.C. 1681c(g) (N44-45-R05); Fla. Stat. 501.171(2) and (8) |
| Assessment dates | 2026-08-10 to 2026-08-14 (self-assessment) |
| Assessor | Owner, with the outside IT helper. Evidence is self-attested, checked on screen or in the store where possible |
| Adopted | 2026-09-04 |

## 1. Applicability
**PCI DSS applies by contract, at any size.** The store accepts cards, and its merchant agreement with the processor requires PCI DSS compliance. PCI SSC sets no size tiers; merchant levels and validation rules come from the card brands and the processor. The processor has not stated a merchant level, and this analysis does not state brand level thresholds, because they were not verified from a card brand source. The processor's compliance portal assigned **SAQ B-IP** (countertop terminal with an IP connection) and **SAQ A** (online store that redirects to the processor's hosted payment page) in 2024 (fictional). The owner never completed either one and has paid a monthly non-compliance fee since March 2024.

**The portal's assignment rests on incomplete answers.** The owner's 2024 screening answers did not mention phone orders keyed into the terminal, the paper order pad, or the shared Wi-Fi. This analysis therefore rates each PCI DSS requirement group from the store's actual card flows, not from the SAQ forms, and the owner will correct the answers and confirm the SAQ types with the processor before completing them (row G-060).

**What is in scope, and why it is bigger than it needs to be:**
- **The terminal and its network.** The terminal is not part of a PCI-listed P2PE solution, so the network it sits on is in scope. That network is the store's only network, shared with the tablet, the laptop, the cameras, and customers' phones. Requirements 1 and 2 (network and secure configuration) therefore apply to the whole store network until the terminal is separated (rows G-001 to G-008).
- **Paper.** Until 2026-08-11 the phone-order pad held full card numbers, expiration dates, and **security codes**. Keeping security codes after authorization is the most serious finding of this analysis (row G-011, 3.3), together with storing and throwing away that paper (row G-041, 9.4). The practice stopped during fieldwork.
- **The online store.** The checkout redirects to the processor's hosted payment page, so the store's own pages are not the payment page. The owner's reading is that Requirements 6.4.3 and 11.6.1 (payment page scripts) therefore apply to the processor's page, not to the store's, and they are marked Not applicable with that reasoning, to be confirmed with the processor. **The redirect still matters:** whoever controls the online store administrator account can change where shoppers go or show them a fake form first. That is why MFA on that account (row G-035, 8.4) and change control on store settings (row G-028, 6.5) are rated as they are, and why the P08 runbook covers this attack.

**Rows marked Not applicable (20)** are: stored-data and key management requirements with nothing to protect (3.5 to 3.7); custom software (6.2); payment page script requirements that belong to the processor's page (6.4.3, 11.6.1); logging requirements for store-managed card systems, which the store does not have (10.1 to 10.7); penetration testing and intrusion detection that rely on segmentation or servers the store does not have (11.4, 11.5); service-provider-only requirements (12.4, 12.9); and Appendices A1 to A3. Not applicable to PCI does not mean unneeded: log review of the online store is part of reasonable security under FTC Act Section 5 (row G-071) and is in POL-01 7.7.

**Secondary rules.** FTC Act Section 5 applies with no size threshold. The FTC may treat inaccurate privacy or security statements as deceptive (45(a)(1)), and may treat a practice as unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits to consumers or competition (45(n)). FACTA receipt truncation applies to any business that accepts cards. **Florida's Information Protection Act names sole proprietorships**: a "covered entity" includes "a sole proprietorship, partnership, corporation, ... or other commercial entity that acquires, maintains, stores, or uses personal information" (Fla. Stat. 501.171(1)(b)). Two of its duties are checked here: reasonable measures for electronic personal information (501.171(2)) and disposal of customer records (501.171(8)), which reaches paper because "customer records" means material "regardless of the physical form" (501.171(1)(c)). Its breach notice duties are in P08.

**Not applicable, with reasons:** FTC Safeguards Rule and Red Flags Rule (no store credit, tabs, or covered accounts; N44-45-R03, R04), CCPA (no California business; revenue far below the threshold; N44-45-R06), COPPA (not directed to children; account holders 18 or older; N44-45-R07), INFORM Consumers Act (no third-party sellers; N44-45-R08), SEC disclosure (not a public company), and HIPAA (no pharmacy). **SNAP** retailer authorization (7 CFR 278.1) is a program rule, not a data security rule, and EBT cards are not payment brand cards, so they are outside PCI DSS. Its equal treatment rule (7 CFR 278.2(b)) matters for pricing and is applied in P10.

## 2. Method
1. **Requirements.** PCI DSS broken into its 12 principal requirements and their requirement groups (for example 8.4), with 6.4 split into its three defined requirements, 11.6.1 listed on its own, and the three appendices. This is the same structure as the Small retail sample, so the two can be compared. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted. Read the requirement text in the official standard.
2. **FTC, FACTA, and Florida rows** cite statute text verified on uscode.house.gov and the Florida Legislature's statutes site (2026).
3. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 to CSF 2.0 or SP 800-53 was used.
4. **Evidence.** Self-attested by the owner and checked on screen or in the store with the outside IT helper: router and account settings, the POS user list, a drawer and trash inspection on 2026-08-11, an online store add-on review and checkout walk-through on 2026-08-12, receipts, the processor's AOC, and the website builder's SOC 2 report.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gaps rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 0 | 2 | 3 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 0 | 3 | 0 | 3 |
| PCI Req 3 Stored account data | 1 | 1 | 2 | 3 | 7 |
| PCI Req 4 Transmission | 1 | 0 | 1 | 0 | 2 |
| PCI Req 5 Malware and phishing | 0 | 3 | 1 | 0 | 4 |
| PCI Req 6 Secure systems and software | 2 | 1 | 2 | 2 | 7 |
| PCI Req 7 Restrict access | 1 | 1 | 1 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 1 | 2 | 3 | 0 | 6 |
| PCI Req 9 Physical access, paper, and the terminal | 2 | 0 | 3 | 0 | 5 |
| PCI Req 10 Logging | 0 | 0 | 0 | 7 | 7 |
| PCI Req 11 Security testing | 0 | 0 | 3 | 3 | 6 |
| PCI Req 12 Policies and programs | 1 | 2 | 5 | 2 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **9** | **12** | **27** | **20** | **68** |
| FTC Act Section 5 | 0 | 3 | 1 | 0 | 4 |
| FACTA receipt truncation | 1 | 0 | 0 | 0 | 1 |
| Fla. Stat. 501.171 | 0 | 1 | 1 | 0 | 2 |
| **Total (75)** | **10** | **16** | **29** | **20** | **75** |

Of the 45 rows with gaps, 5 are rated High, 21 Moderate, and 19 Low. Many of the Low rows are "no written procedure" findings that POL-01 closed on adoption.

## 4. Action list (half page)
In order. The first four are free or nearly free and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Never write card data down; key phone orders while the customer is on the line (started 2026-08-11) | G-010, G-011 (3.2, 3.3) | High | 2026-09-15 |
| 2 | MFA and unique passphrases on the online store and email | G-035, G-034 (8.4, 8.3) | High | 2026-09-15 |
| 3 | Cross-cut shredder and locked drawer for anything with customer details | G-041 (9.4); G-075 (501.171(8)) | High | 2026-09-15 |
| 4 | Adopt POL-01 | G-056 and the procedure rows | Moderate | 2026-09-04 (done) |
| 5 | Change router, Wi-Fi, and terminal defaults; guest network for customers; separate POS user | G-007, G-008, G-030, G-033 | Moderate | 2026-09-30 |
| 6 | Terminal serial number, daily inspection, re-aimed camera, family member training | G-042 (9.5) | Moderate | 2026-09-30 |
| 7 | Adopt, print, and walk through the P08 runbook | G-065 (12.10) | Moderate | 2026-09-30 |
| 8 | Laptop encryption and deletion of old customer exports | G-074 (501.171(2)); G-071 | Moderate | 2026-09-30 |
| 9 | Fix the privacy notice and offer claims; AI rules (P10) | G-069, G-072 | Moderate | 2026-10-31 |
| 10 | Scope note, corrected portal answers, provider list, both SAQs with evidence; ask about scans | G-060, G-063, G-052 | High | 2026-11-30 |
| 11 | Terminal on its own network | G-003 (1.3) | Moderate | 2026-12-31 |

**Before signing the SAQs (due 2026-11-30):** close actions 1, 2, 3, and 10, and keep the evidence. Do not answer "no card data stored" or "no default passwords" unless the evidence supports it. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes and watch items
- **PCI DSS.** v4.0.1 remains current. PCI SSC ran a request for comments (June to July 2026) toward the next version; this analysis will be updated when a new version is published. Not a current obligation.
- **SAQ assignment.** The SAQ types depend on the processor's confirmation after the owner corrects the portal answers. If the terminal stays on a network shared with other devices, ask the processor which SAQ applies.

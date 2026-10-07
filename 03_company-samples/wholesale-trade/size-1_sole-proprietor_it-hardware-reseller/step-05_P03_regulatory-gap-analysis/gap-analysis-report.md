# Regulatory Gap Analysis: Cris Santos Company | Wholesale Trade | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (IT hardware reseller) |
| Tier / Vertical | Sole Proprietorship / Wholesale Trade |
| Primary regulation | FAR 52.204-21 Basic Safeguarding of Covered Contractor Information Systems (15 requirements), assessed as CMMC Level 1 (Self) under 32 CFR 170.15 and DFARS 252.204-7021 |
| Secondary | CMMC Level 1 procedure duties (scope, self-assessment, SPRS entry, affirmation, evidence retention); supply chain clause check: FAR 52.204-25 (Section 889) and FAR 52.204-23 |
| Assessment dates | 2026-08-03 to 2026-08-07 (self-assessment; row G-006 updated 2026-08-06 with a P07 finding) |
| Assessor | Owner, with the on-call IT consultant. Evidence is self-attested, checked on screen where possible |
| Workbook | `gap-analysis.csv` (25 rows) |
| Adopted | 2026-08-31 |

## 1. Applicability
**The registry's primary regulation does not apply at this size.** The Wholesale Trade profile names NIST SP 800-171 Rev. 2 via DFARS 252.204-7012 and CMMC Level 2. Those rules reach a contractor that handles Controlled Unclassified Information (CUI) under a contract containing DFARS 252.204-7012. The prime's BPA does not contain that clause, the prime provides no CUI (it keeps the network drawings and IP plans), and the owner receives only asset tag numbers, firmware version numbers, and building delivery lists. If the prime ever sends anything marked CUI, the owner stops, returns it, and re-scopes (POL-01 8.3), because CMMC Level 2 (Self) would then be the minimum (32 CFR 170.23(a)(2)).

**FAR 52.204-21 applies.** It is in the prime's BPA. The clause flows to "subcontracts ... (including subcontracts for the acquisition of commercial products or commercial services, other than commercially available off-the-shelf items), in which the subcontractor may have Federal contract information residing in or transiting through its information system" (52.204-21(c)). The staging and asset labeling service makes these orders more than COTS, and the asset tag and delivery lists are FCI: information "not intended for public release ... provided by or generated for the Government under a contract" (52.204-21(a)). There is no size exemption.

**CMMC Level 1 (Self) will apply from the first purchase order under the prime's new task order.** A subcontractor that will only process, store, or transmit FCI needs a CMMC Status of Level 1 (Self) (32 CFR 170.23(a)(1)). The prime must ensure the owner has a current status and affirmation before it awards (DFARS 252.204-7021(d)(4) and (f)(2)), and it set 2026-10-30 as the deadline. Level 1 means: every one of the 15 requirements is MET, with no POA&M allowed (32 CFR 170.15(a)(1); 170.21(a)(1); 170.24(c)(1)); results entered in SPRS; and an affirmation by the Affirming Official, who here is the owner (170.22). Artifacts are kept 6 years (170.15(c)(2)).

**Supply chain clauses apply as contract terms.** FAR 52.204-25 and FAR 52.204-23 are in the BPA. Paragraph (e) of 52.204-25 flows the clause down "excluding paragraph (b)(2)", so the owner's own use of covered equipment is not a subcontract issue, but providing it to the Government is. FAR 52.204-23(c) has a 3-business-day report, not the 1 business day of 52.204-25(d).

**Cross-sector duties that set the bar for "reasonable":** FTC Act Section 5 (15 U.S.C. 45(a); N42-R01) applies to the business with no size threshold, including truthful claims such as "new and genuine" on the website. Fla. Stat. 501.171(2) requires a covered entity, which "means a sole proprietorship, partnership, corporation ...", to "take reasonable measures to protect and secure data in electronic form containing personal information."

**Not applicable, with reasons:** FAR 52.204-21(b)(1)(xi) (no publicly accessible components; G-011); FAR 52.204-21(c) (no lower-tier subcontractor holds FCI; G-025); DFARS 252.204-7012 and SP 800-171 (no CUI); SEC rules, CCPA/CPRA, and CTPAT (see `../00_company-facts.md` section 1). The Trade Agreements Act was not analyzed: the owner holds no GSA Schedule or federal prime contract.

## 2. Method
1. **Requirements.** The 15 requirements are quoted from 48 CFR 52.204-21(b)(1) (eCFR, current as of 2026-09-23). CMMC practice IDs follow 32 CFR 170.14(c)(2), and each is linked to its SP 800-171 Rev. 2 equivalent per Table 2 to 32 CFR 170.15(c)(1)(ii). Requirement (ix) maps to three SP 800-171 requirements (3.10.3, 3.10.4, 3.10.5).
2. **Crosswalk.** SP 800-53 controls come from the SP 800-171 Rev. 2 Appendix D mapping, refined to Rev. 5 by the author; CSF 2.0 subcategories come from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference. Procedure and clause rows use an **author mapping** and are labeled as such.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT consultant: account exports, the file sharing report, device and router settings, a garage walkthrough on 2026-08-05, purchase history, and the BPA.
4. **Status.** Met, Partially met, Not met, or Not applicable. For CMMC Level 1, Partially met counts as NOT MET, and Not applicable counts as MET (32 CFR 170.24(b)(3)).

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| FAR 52.204-21(b)(1) basic safeguarding (CMMC Level 1) | 4 | 7 | 3 | 1 | 15 |
| CMMC Level 1 procedures (32 CFR 170.15, 170.19, 170.22) | 0 | 1 | 3 | 0 | 4 |
| DFARS 252.204-7021(d)(2) (FCI only on assessed systems) | 0 | 0 | 1 | 0 | 1 |
| FAR 52.204-25 (Section 889) | 0 | 1 | 2 | 0 | 3 |
| FAR 52.204-23 (Kaspersky) | 0 | 1 | 0 | 0 | 1 |
| FAR 52.204-21(c) flowdown | 0 | 0 | 0 | 1 | 1 |
| **Total (25)** | **4** | **10** | **9** | **2** | **25** |

**CMMC Level 1 result today: 10 of 15 requirements NOT MET** (the 7 partially met and 3 not met). A Level 1 (Self) status cannot be entered or affirmed until all 15 are MET. Of the 19 unmet or partially met rows, 6 are High gap risk, 10 Moderate, and 3 Low.

## 4. Action list (half page)
In order. The first five cost nothing and take under a day. Everything must be done by 2026-10-15 so the final self-assessment (2026-10-23) can find all 15 requirements MET.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Turn off AI assistant training, delete chats with DoD lines, and keep FCI only in approved locations | G-003, G-020 | High | 2026-09-30 |
| 2 | Password manager with unique passphrases; MFA by app on SYS-01 and email (router password done 2026-08-06) | G-006 | High | 2026-09-15 |
| 3 | Remove open file links; named-people sharing; quarterly account review | G-001 | Moderate | 2026-09-30 |
| 4 | Standard daily laptop account | G-002 | Moderate | 2026-09-30 |
| 5 | Adopt POL-01 (posting rule, approved locations, reporting steps) and the P08 runbook | G-004, G-022, G-024 | Moderate | 2026-08-31 |
| 6 | Business-only Wi-Fi network; router firmware update | G-010, G-012 | High | 2026-10-15 |
| 7 | Garage key lockbox, new keypad code, entry log, key inventory | G-008, G-009 | Moderate | 2026-10-15 |
| 8 | Device wipe method and disposal record; wipe the 2 old laptops | G-007 | Moderate | 2026-10-15 |
| 9 | Covered-manufacturer check on DoD quotes; clause note on DoD-bound purchase orders | G-021, G-023 | Moderate | 2026-10-15 |
| 10 | Final self-assessment, evidence folder, SPRS entry, and affirmation | G-016 to G-019 | High | 2026-10-30 |

High and Moderate gaps are in the risk register (P01, mainly R-004, R-006, R-007, R-008, R-010) and the POA&M (P07). The POA&M tracks the owner's work, but it is not a CMMC POA&M: Level 1 allows none.

## 5. Pending regulatory changes
These are **proposed** and are not treated as current obligations. The `pending_rule_change` column flags the affected rows.
- **FAR overhaul, parts 1, 2, 4, 33, 39, 40, 52, and 53** (FR Doc. 2026-12559, 2026-06-23; comments closed 2026-07-23). Its conversion table maps FAR 52.204-21 to a proposed 52.240-5 in FAR part 40, and a proposed 52.240-3 would consolidate the security prohibitions, including Section 889, with reporting standardized to 72 hours from discovery. The clause-number mapping was read from the proposed rule's table and should be rechecked when the rule is final.
- **CMMC phases.** Phase 2 begins 2026-11-10 (32 CFR 170.3(e)(2)) and adds Level 2 (C3PAO) requirements. It does not change Level 1, which is already in effect for the prime's new task order.

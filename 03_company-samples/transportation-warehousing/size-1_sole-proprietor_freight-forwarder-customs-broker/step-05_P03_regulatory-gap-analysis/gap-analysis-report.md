# Regulatory Gap Analysis: Cris Santos Company | Transportation and Warehousing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight forwarder and customs broker, NAICS 488510) |
| Tier / Vertical | Sole Proprietorship / Transportation and Warehousing |
| Regulation analyzed | 19 CFR Part 111, Customs Brokers (record, confidentiality, breach notice, supervision, and status duties), with the 19 CFR 163.5 storage standards that 111.21(c) and 111.23(a) bring in. Text checked against eCFR as of 2026-09-23. Modernization rule 87 FR 63267 (2022-10-18), effective 2022-12-19; continuing education rule 88 FR 41224 (2023-06-23), effective 2023-07-24 |
| Secondary | 46 CFR 515.33 (FMC ocean freight forwarder records); 15 CFR 30.10(a) (export records); Fla. Stat. 501.171(2), (3)-(4), and (8) |
| Assessment dates | 2026-08-17 to 2026-08-21 (self-assessment) |
| Assessor | Owner, with the on-call IT consultant. Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-09-14 |

## 1. Applicability
**The vertical's default regulation does not apply.** The registry names the USCG maritime cyber rule (33 CFR Part 101 Subpart F, N48-49-R01) for this vertical. Section 101.605(a) limits it to owners and operators of vessels, facilities, and OCS facilities "required to have a security plan under 33 CFR parts 104, 105, and 106." A home-office forwarder and broker owns no vessel and operates no facility. The terminals and carriers that handle its clients' cargo carry those duties themselves (row G-001).

**The TSA indirect air carrier rule does not apply.** 49 CFR Part 1548 governs "each indirect air carrier engaged indirectly in the air transportation of property on aircraft" (1548.1). The business arranges ocean freight only and refers air shipments to other forwarders (row G-002). It must recheck before arranging any air shipment.

**CTPAT is voluntary.** Customs brokers may join, but the owner is not a partner. Three CTPAT importer clients send yearly business partner security questionnaires, which P09 answers (row G-003, N48-49-R05).

**What does bind the business: 19 CFR Part 111.** A person must hold a broker license to transact customs business for others (111.2(a)(1)), and the duties in Subpart C apply to every broker. There is no size threshold: 111.28(a) names "every individual broker operating as a sole proprietor." The 2022 modernization rule added the duty most relevant to security: notify the CBP Security Operations Center within 72 hours of discovering "any known breach of electronic or physical records relating to the broker's customs business," including compromised importer identification numbers, with an updated list within 10 business days (111.21(b)). CBP's preamble to that rule says it intends the common meaning of "breach" and that the rule does not distinguish material from non-material breaches. A broker's importer identification numbers include Social Security numbers for importers with no employer identification number (19 CFR 24.5(b)(1)(ii)), which this business holds for six clients.

**Workforce rows.** The business has no employees. The employee information duty (111.28(b)) is recorded as not applicable, with the step to take if the owner hires.

## 2. Method
1. **Requirements.** Rows follow the regulation's own structure: each paragraph of Part 111 that imposes a duty touching records, information, client money, supervision, or status, at the most granular citation that can be checked separately, plus each standard in 163.5. Conduct rules with no information-handling element (111.31, 111.34, 111.35, 111.38, 111.40, 111.41, 111.42) are outside a security gap analysis; the owner self-attests compliance. Brief quotes are used; this is public-domain federal text.
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **This is an author mapping.** NIST has published no mapping for these rules.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT consultant where possible (eCBP portal pages, customs software user list, archive review and POA sample on 2026-08-19, closet and router checks on 2026-08-20).
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Source | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Applicability checks (USCG, TSA, CTPAT) | 0 | 0 | 0 | 3 |
| 19 CFR Part 111 | 10 | 15 | 2 | 2 |
| 19 CFR 163.5 (scanned records) | 1 | 2 | 4 | 1 |
| 46 CFR 515.33 | 0 | 1 | 0 | 0 |
| 15 CFR 30.10(a) | 1 | 0 | 0 | 0 |
| Fla. Stat. 501.171 | 0 | 2 | 1 | 0 |
| **Total (45)** | **12** | **20** | **7** | **6** |

Gap risk for the 27 Not met or Partially met rows: 2 High, 16 Moderate, 9 Low. The two High rows are the 72-hour CBP breach notice (G-008) and the missing back-up copy of scanned records (G-040). Both are already in force: the breach notice since 2022-12-19 and the storage standard since before the business started scanning in 2024.

**Reading the result.** Most licensing and conduct duties are met because one careful person does all the work. The gaps cluster in two places: **what happens to records when something goes wrong** (breach notice, backups, scanned originals) and **who else sees client records** (service providers, a consumer AI assistant, a messaging app). Both are information security problems that the customs rules turn into license problems.

## 4. Action list (half page)
In order. The first four cost nothing.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Adopt the P08 runbook with the CBP SOC 72-hour notice, the 10-business-day update, and a list of systems holding importer of record numbers | 111.21(b) | High | 2026-10-31 |
| 2 | Call-back before any new or changed payee | 111.29(a) | Moderate | 2026-09-30 |
| 3 | Keep paper originals from now on until the storage notice is resolved | 163.5(a) | Moderate | 2026-09-14 (done) |
| 4 | Stop pasting client data into the consumer AI assistant; record how each classification was checked | 111.24; 111.28(a); 111.39(b) | Moderate | 2026-10-31 |
| 5 | Independent versioned backup of the records archive, tested quarterly | 163.5(b)(2)(vi); 111.25(b) | High | 2026-10-31 |
| 6 | Confirm the U.S. data region for the email and file suite | 111.23(a) | Moderate | 2026-10-31 |
| 7 | With customs counsel: written client authorization for service providers; alternative storage notice to CBP Regulatory Audit; scanning procedure | 111.24; 163.5(b)(1)-(2) | Moderate | 2026-11-30 |
| 8 | Backup broker coverage agreement and an alternate contact for CBP | 111.3(b) | Moderate | 2026-12-31 |
| 9 | Finish 14 continuing education credits, then file the triennial status report | 111.102(b); 111.30(d) | Moderate | 2027-01-31; 2027-02-01 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The notification duties are in the P08 notification matrix.

## 5. Pending regulatory changes
- **No change to Part 111 is pending.** A Federal Register search on 2026-10-04 found no proposed or final rule amending Part 111 since the continuing education rule (88 FR 41224, 2023). The `pending_rule_change` column is "None" on those rows.
- **Part 163 is named in an advance notice.** CBP's "Heightened Import Disclosures for Supply Chain Visibility" (91 FR 56408, 2026-09-02) is an advance notice of proposed rulemaking that lists 19 CFR parts 141, 142, 143, and 163; comments are due 2026-12-01. It proposes no regulatory text yet and is not an obligation. The Part 163 rows say "monitor".
- **CIRCIA** (6 U.S.C. 681-681g): no final rule had been published as of 2026-09-25. It is not treated as a current obligation (see P08).

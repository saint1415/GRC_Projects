# Regulatory Gap Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated oilfield services contractor, NAICS 213112; sole proprietorship) |
| Tier / Vertical | Sole Proprietorship / Mining, Quarrying, and Oil and Gas Extraction |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, all 106 subcategories), applied to the owner's touch points with customer OT through NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (September 2023). **Voluntary benchmark: no binding federal sector cybersecurity rule applies** (section 1) |
| Binding duties checked | Customer A MSA security schedule (contract flow-down, 8 items); Fla. Stat. 501.171 (state law, 6 subsections) |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment; walkthrough 2026-07-21) |
| Assessor | Owner-operator, with the on-call IT technician. Evidence is self-attested, checked on screen where possible |
| Workbook | `gap-analysis.csv` (124 rows) |
| Regulatory driver label | `N21-BM` in the other deliverables points to this benchmark; `MSA-A (n)` to the Customer A rows (see `../00_company-facts.md` section 5) |
| Adopted | 2026-08-31 |

## 1. Applicability
**Step 1 was to find what binds a one-person contractor. No federal cybersecurity rule does; a customer contract does.**

| Candidate | Applies? | Why (citation) |
|---|---|---|
| **N21-R01** USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101 Subpart F | **No** | Applies to owners and operators of U.S.-flagged vessels, facilities, and OCS facilities required to have a security plan under 33 CFR parts 104 to 106 (101.605(a)). The owner works onshore and owns none of these |
| **N21-R02** TSA Security Directive Pipeline-2021-02G | **No** | Applies to owners and operators of pipelines or LNG facilities that TSA has notified are critical. The owner operates no pipeline. A TSA-notified customer could pass requirements down by contract; none has |
| **N21-R03** CIRCIA, proposed 6 CFR Part 226 | **No (proposed)** | No final rule as of 2026-09-25. As proposed, the size test is the SBA standard for the entity's NAICS code: about $180,000 in receipts against $47.0 million for NAICS 213112 (13 CFR 121.201). No proposed sector criterion is met |
| PHMSA pipeline safety, 49 CFR Parts 192 and 195, including operator qualification | **No** | Part 195 does not apply to transportation through "onshore production (including flow lines)" facilities (195.1(b)(8)). Operator qualification covers individuals performing covered tasks on a pipeline facility (195.501(b)) under the operator's program (195.505); gas gathering status is the operator's determination (192.8). The owner works only on production facilities |
| **Customer A MSA security schedule** | **Yes, by contract** | Customer A (about 45% of receipts) requires 8 security items, listed in `../00_company-facts.md` section 1. This is the business's main binding security duty, and Customer A's questionnaire is organized by CSF 2.0 |
| **Fla. Stat. 501.171** | **Yes, narrowly** | A "covered entity" includes a sole proprietorship that maintains personal information (501.171(1)(b)). The business holds W-9 forms (names and Social Security numbers) for 2 helpers. The 500-person and 1,000-person notice rows cannot be reached; the disposal duty covers only "customer records" (501.171(1)(c)), which the business does not hold, so POL-01 applies it voluntarily |
| Customers B, C, and D MSAs | Background | Confidentiality clauses only; covered by the CSF rows and POL-01 |
| FTC Act Section 5 | Background | Applies to any security promise the owner makes to customers (for example in questionnaire answers). Not decomposed into rows |

**Decision: NIST CSF 2.0 is the benchmark, with SP 800-82 Rev. 3 for the OT touch points.** This follows the vertical profile: onshore businesses without TSA-designated assets have no binding federal sector cyber rule, and CSF 2.0 is sector-neutral. It is also the structure of Customer A's questionnaire, so one analysis answers both. The owner runs no OT of its own, so SP 800-82 Rev. 3 is applied to what the owner brings into customer OT: the laptop, remote access, portable media, credentials, and control logic changes (sections 6.2.1, 6.2.4, 6.2.7, and 6.2.10). SP 800-82 Rev. 3 organizes its guidance by CSF 1.1 categories, so the link from each CSF 2.0 subcategory to a section is an **author mapping** (column `sp800_82r3_reference`). Three subcategories are not applicable at this size: GV.RR-04 (no employees), ID.RA-08 (no published products), and PR.AA-04 (no federated identity).

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from `00_universal-framework/frameworks/csf2_core.csv`. Florida rows follow the 2026 statute's subsections, with short quotes. Customer A rows follow the security schedule item numbers. Applicability screens cite eCFR text current as of 2026-09-23.
2. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in `nist_official_sp800_53r5`; `sp800_53_controls` is a key-control subset chosen by the author. Florida, contract, and screen rows use an author mapping.
3. **Evidence.** Self-attested by the owner, checked on screen with the IT technician where possible: SaaS security pages, laptop account and encryption settings, the password spreadsheet (reviewed, not copied), USB drives, router settings, Customer A emails, provider terms, and a walkthrough of the home office and truck (2026-07-21).
4. **Status.** Met, Partially met, Not met, or Not applicable, as of fieldwork. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 3 | 16 | 11 | 1 |
| CSF 2.0 Identify (21) | 4 | 8 | 8 | 1 |
| CSF 2.0 Protect (22) | 4 | 11 | 6 | 1 |
| CSF 2.0 Detect (11) | 0 | 2 | 9 | 0 |
| CSF 2.0 Respond (13) | 0 | 0 | 13 | 0 |
| CSF 2.0 Recover (8) | 0 | 2 | 6 | 0 |
| **CSF 2.0 subtotal (106)** | **11** | **39** | **53** | **3** |
| Customer A MSA security schedule (8) | 1 | 3 | 4 | 0 |
| Fla. Stat. 501.171 (6) | 0 | 2 | 1 | 3 |
| Applicability screens (4) | 0 | 0 | 0 | 4 |
| **Total (124)** | **12** | **44** | **58** | **10** |

Of the 102 unmet or partially met rows, 10 are rated High, 41 Moderate, and 51 Low. The 10 High rows are 8 CSF subcategories (GV.SC-05, ID.IM-04, PR.AA-01, PR.AA-03, PR.AA-05, PR.DS-11, RS.CO-02, RS.MI-01) and 2 Customer A items (MSA-A (3) 24-hour incident notice; MSA-A (8) cyber coverage).

**The pattern:** the owner now knows its risks (the 2026 risk assessment and BIA meet ID.RA-03 to ID.RA-05, ID.AM-05, and GV.OC-04), and SaaS defaults protect data in transit. But the business **cannot respond**: all 13 Respond subcategories are Not met, which matters because Customer A's contract expects notice within 24 hours. On the OT side, the gaps are about what the owner carries into customer systems: one administrator account, a password spreadsheet, a shared remote login, a mixed-use USB drive, and changes with no record.

## 4. Action list (half page)
In order. The first five cost under $50 in total and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | MFA on the accounting service; authenticator app for email; recovery codes sealed | PR.AA-03; Fla. Stat. 501.171(2) | High | 2026-09-15 (accounting); 2026-09-30 (email) |
| 2 | Adopt the P08 runbook; give Customer A the 24-hour notice contact; print the contact sheet | ID.IM-04, RS.CO-02, RS.MI-01; MSA-A (3) | High | 2026-09-15 (notice contact); 2026-09-30 (runbook walkthrough) |
| 3 | Email approval before every logic or setpoint change; start the change log | ID.RA-07, PR.PS-01; MSA-A (4) | Moderate | 2026-09-15 |
| 4 | Standard daily laptop account; password manager; delete the spreadsheet and its file versions | PR.AA-01, PR.AA-05, PR.PS-05; MSA-A (1) | High | 2026-09-30 |
| 5 | Dedicated, labeled program USB drives, scanned before every site use | PR.PS-01, DE.CM-09 | Moderate | 2026-09-30 |
| 6 | Customer A consent or no-training tier for the AI service; stop the chatbot (done 2026-07-24) | GV.SC-05, GV.SC-06; MSA-A (5) | High | 2026-09-30 |
| 7 | Send Customer A's questionnaire answers with this action list | MSA-A (7) | Low | 2026-09-30 |
| 8 | Cyber liability coverage of at least $1 million; certificate to Customer A | GV.RM-04; MSA-A (8) | High | 2026-10-31 |
| 9 | Encrypted offline program backups after every approved change; quarterly restore test | PR.DS-11, RC.RP-03 | High | 2026-10-31 |
| 10 | Customer B named accounts and MFA (requested 2026-07-24); session log | PR.AA-01, PR.AA-05, DE.CM-06 | High | 2026-10-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The answers to Customer A's questionnaire state the current status honestly and attach this list, because an inaccurate security promise to a customer creates its own exposure.

## 5. Pending changes (not current obligations)
- **CIRCIA** (proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25. If finalized as proposed, the business stays outside it. Recheck when final (GV.OC-03).
- **TSA surface cyber risk management rule** (NPRM Nov. 7, 2024; not final): relevant only if a customer that TSA designates passes requirements down by contract.
- **Business changes that would change applicability:** work on a regulated gathering or transmission line (operator qualification under the pipeline operator's program), work at an offshore or waterfront facility (USCG Subpart F through the facility's cybersecurity plan), or holding personal information of 500 or more people (Florida notice to the Department of Legal Affairs).

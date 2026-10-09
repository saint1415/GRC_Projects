# Regulatory Gap Analysis: Cris Santos Company | Food and Agriculture | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (custom-exempt meat processing shop, NAICS 311612; sole proprietorship) |
| Tier / Vertical | Sole Proprietorship / Food and Agriculture |
| Binding rules checked | FMIA custom exemption conditions that touch records, labels, ingredients, and product protection (9 CFR 303.1, 316.16, 317.16, 318.5-318.6, 320.1-320.4, 300.6(b)(2), 416.1-416.6, 424.21), read on eCFR (point-in-time 2026-09-23); Fla. Stat. 501.171 (2026 statute) |
| Benchmark | NIST Cybersecurity Framework (CSF) 2.0, all 106 subcategories, **as a voluntary benchmark** |
| Also recorded | Card processor merchant terms (contract); C-FOOD-AG-R01 (21 CFR Part 121), R02 (CIRCIA, proposed), R03 (USCG MTS rule), the Reportable Food Registry, and 9 CFR 417 and 418.2, all not applicable |
| Assessment dates | 2026-07-27 to 2026-07-31 (self-assessment) |
| Assessor | Owner-operator, with the on-call IT technician. Evidence is the intake record and the owner's self-review (EV-032), checked on screen where possible |
| Workbook | `gap-analysis.csv` (136 rows) |
| Adopted | 2026-08-31 |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the result for the rules analyzed here. **Step 1 was to find the rule that binds this shop. The vertical's primary regulation does not, and no binding cybersecurity rule does.**

| Candidate | Applies? | Why (citation) |
|---|---|---|
| FSMA intentional adulteration rule, 21 CFR Part 121 (**C-FOOD-AG-R01**) | **No** | Part 121 applies to a food facility "required to register under section 415" of the FD&C Act (21 CFR 121.1). The registration rule exempts "Facilities that are regulated exclusively, throughout the entire facility, by the U.S. Department of Agriculture under the Federal Meat Inspection Act" (21 CFR 1.226(g)). The shop handles only owner-delivered carcasses under the FMIA custom exemption and no FDA-regulated food, so it does not register (EV-021, EV-029). Even a registered shop of this size would be a very small business (under $10,000,000 a year, 121.3), exempt except for keeping documentation of that status for 2 years (121.5(a)) |
| CIRCIA (**C-FOOD-AG-R02**), proposed 6 CFR Part 226 | **No (proposed)** | No final rule as of 2026-09-25. As proposed, food and agriculture entities are covered only above the SBA size standard, which is 1,000 employees for NAICS 311612 (13 CFR 121.201) |
| USCG MTS cyber rule (**C-FOOD-AG-R03**) | **No** | The shop is not an MTSA-regulated facility (33 CFR 101.605) |
| Reportable Food Registry, 21 U.S.C. 350f | **No** | The duty falls on the person who registers a food facility (350f(a)); the shop registers none |
| FSIS HACCP (9 CFR 417) and 24-hour recall notice (418.2) | **No** | Both are written for official establishments (417.2(a): "Every official establishment"; 418.2: "Each official establishment"). Neither is among the conditions for custom operators in 303.1(a)(2) and (b) |
| **FMIA custom exemption, 9 CFR 303.1(a)(2) and (b)** | **Yes** | The shop operates only under this exemption. Its conditions are binding: sanitation standards (416.1-416.6, with listed exceptions), procedure and ingredient rules (318.5, 318.6, 424.21), "Not for Sale" marking (316.16, 317.16), custom records (303.1(b)(3)) plus Part 320 records, and FSIS access to records (300.6(b)(2), 320.4). FSIS reviewed the operation in March 2026 (EV-022) |
| **Fla. Stat. 501.171** | **Yes (treated as applying)** | "Covered entity" expressly includes a sole proprietorship (501.171(1)(b)). See section 1.2 |

**Decision: NIST CSF 2.0 is the cybersecurity benchmark.** No regulation tells the shop how to secure its systems. CSF 2.0 is the sector-neutral baseline the vertical profile pairs with Part 121, and it is used here on its own. It is voluntary; status ratings measure the shop against a target, not a legal duty. Seven subcategories are not applicable at this size (GV.RM-05, GV.RR-04, ID.RA-08, PR.AA-04, PR.AT-02, PR.PS-06, RC.CO-04), each with its reason in the workbook.

### 1.1 Where the custom exemption becomes a cybersecurity question
The custom exemption is a food safety rule, but four of its conditions now run through the shop's systems:
- **Records** (303.1(b)(3); 320.1-320.3): the custom records are one spreadsheet in a consumer file account. They must survive 2 years after the end of the transaction year and be producible to FSIS (300.6(b)(2)). A deletion or ransomware could erase the evidence that the shop meets the exemption.
- **Labels** (316.16; 317.16): "Not for Sale" labels print from a template on the laptop. A preprinted roll keeps this condition met if the laptop fails.
- **Curing agents** (424.21(c), applied through 303.1(b)(1)): cure and brine amounts are now scaled with a public AI chatbot and a laptop spreadsheet. An error there is an ingredient violation and a safety hazard.
- **Product protection** (303.1(b)(1); 416.4(d) through 303.1(a)(2)(i)): cold storage is watched by a SaaS service whose alerts can stop without warning. Applying 416.4(d) to a custom shop's storage is an **author reading**, because the sentence is worded for official establishments; 303.1(b)(1) ("shall not be adulterated") supports the same conclusion directly.

The sanitation conditions (416.1-416.5) are recorded as rows so the register is complete, but they are food safety duties, not IT duties, and rest on the owner's self-review and the shop walk-through (EV-032, EV-020).

### 1.2 Fla. Stat. 501.171 and the 2026 geolocation element
The shop collects no Social Security, driver license, or financial account numbers. Its records hold names with street addresses, phone numbers, and emails for about 640 livestock and product owners (EV-012, EV-013). The 2026 statute adds "Any information regarding an individual's geolocation" to the data elements that make a name personal information (501.171(1)(g)1.a.(VII)). The text read does not define geolocation, and it is not clear whether a customer's street address in a business record is covered. **Open question for counsel.** Until it is answered, the owner treats the records as personal information, which brings in the reasonable-measures duty (501.171(2)), the 30-day notices (501.171(3)-(4)), third-party agent notices (501.171(6)), and disposal (501.171(8)). The consumer reporting agency notice (501.171(5)) does not apply at about 640 individuals.

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows paraphrase or briefly quote the eCFR text current as of 2026-09-23 and the 2026 Florida Statutes.
2. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`; `sp800_53_controls` is a key-control subset chosen by the author. Regulation rows use an **author mapping**; NIST publishes none for 9 CFR or Florida law.
3. **Evidence.** Current state was established from the intake evidence (the cold-chain user, alert and log settings, the smokehouse app, booking form, email, accounting and banking settings, the laptop, phone and router settings, the custom records spreadsheet and the label check, the vendor terms and the cold-chain SOC 2 report, statements, the FSIS review record, and the shop walk-through on 2026-07-22) and the owner's written self-review, checked on screen with the IT technician from 2026-07-27 to 2026-07-29 (EV-032). The 12 saved chatbot cure answers were checked on 2026-07-30 (EV-033). Where the control tests had run (2026-07-29 and 2026-07-30), their results are cited too (EV-IA-2(1), EV-IA-5, EV-SC-7, EV-SI-3, EV-CP-9, EV-AU-6). The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
4. **Status.** Met, Partially met, Not met, or Not applicable, as of fieldwork. Items fixed after fieldwork (POL-01 adopted 2026-08-31) are scored as found and show the completion date as the target. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 3 | 10 | 16 | 2 |
| CSF 2.0 Identify (21) | 4 | 8 | 8 | 1 |
| CSF 2.0 Protect (22) | 4 | 10 | 5 | 3 |
| CSF 2.0 Detect (11) | 0 | 3 | 8 | 0 |
| CSF 2.0 Respond (13) | 0 | 0 | 13 | 0 |
| CSF 2.0 Recover (8) | 0 | 1 | 6 | 1 |
| **CSF 2.0 subtotal (106)** | **11** | **32** | **56** | **7** |
| FMIA custom exemption, 9 CFR (17) | 8 | 6 | 0 | 3 |
| Fla. Stat. 501.171 (6) | 0 | 2 | 3 | 1 |
| Card processor terms, contractual (1) | 1 | 0 | 0 | 0 |
| Not applicable rules: C-FOOD-AG-R01 to R03, Reportable Food Registry, 9 CFR 417, 9 CFR 418.2 (6) | 0 | 0 | 0 | 6 |
| **Total (136)** | **20** | **40** | **59** | **17** |

Of the 99 unmet or partially met rows, 10 are rated High, 46 Moderate, 42 Low, and 1 Very Low. Nine of the High rows are CSF subcategories (GV.PO-01, ID.RA-06, ID.IM-04, PR.AA-01, PR.AA-03, PR.DS-11, PR.IR-02, PR.IR-03, DE.CM-02); the tenth is the product protection condition (303.1(b)(1); 416.4(d)). The 11 open rows under binding rules are 1 High, 7 Moderate, and 3 Low.

**The pattern.** The shop meets the custom exemption today: the March 2026 FSIS review found nothing (EV-022), labels are right, and cure is locked up. What it lacks is **resilience**. Every binding condition that runs through a system (records, labels, cure amounts, cold storage) depends on a single copy, a single password, or a single phone. On the CSF side, the shop can identify its risks now (ID.RA-03 to ID.RA-05 are Met) but it **cannot respond or recover**: none of the 13 Respond subcategories was met at fieldwork.

## 4. Action list (half page)
In order. The first four cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | MFA on the cold-chain account and booking form; unique passphrases in a password manager; clear the browser store | PR.AA-01, PR.AA-03; Fla. Stat. 501.171(2) | High | 2026-09-15 |
| 2 | Adopt POL-01, the P08 runbook, and the notification matrix | GV.PO-01, ID.IM-04, RS.CO-02; Fla. Stat. 501.171(3)-(4) | High | 2026-08-31 (adopted) |
| 3 | Cure amounts only from the supplier's chart; record the check on each batch sheet | 9 CFR 424.21(c); PR.DS-10 | Moderate | 2026-09-30 |
| 4 | Register a shop security contact with each vendor; add pickup dates to the records | Fla. Stat. 501.171(6); 9 CFR 320.1(b)(1) | Low | 2026-09-30 |
| 5 | Offline notice, battery backup, second alert contact, hourly manual readings when alerts are down | 9 CFR 303.1(b)(1), 416.4(d); DE.CM-02, PR.IR-03 | High | 2026-10-15 |
| 6 | Versioned file plan, monthly encrypted export, printed cook programs and monthly records summary | 9 CFR 303.1(b)(3), 320.3(a); PR.DS-11 | High | 2026-10-15 |
| 7 | Guest network for customers; separate device network; router firmware | PR.IR-01, PR.PS-02 | Moderate | 2026-10-15 |
| 8 | Locked paper box; shred records older than the 320.3 period; counsel opinion on geolocation | Fla. Stat. 501.171(2), (8); 9 CFR 320.2(a) | Moderate | 2026-12-31 |
| 9 | Storm procedure and generator transfer switch | PR.IR-02 | High | 2027-05-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes (not current obligations)
- **CIRCIA** (proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25; as proposed it would not reach the shop. Recheck when final.
- **Fla. Stat. 501.171:** the 2026 amendment (ch. 2026-52) is already law and is applied above. Whether "geolocation" covers a street address is a reading question for counsel, not a pending change.
- **Business change triggers:** accepting wild game, selling any product, or adding a retail counter would change this analysis (FDA and state questions for game; 303.1(a)(2)(ii) separation and 303.1(d) retail rules for sales). The owner reruns P03 before any of these.

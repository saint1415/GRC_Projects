# Regulatory Gap Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (precision-agriculture crop farm, NAICS 111998; sole proprietorship) |
| Tier / Vertical | Sole Proprietorship / Agriculture, Forestry, Fishing and Hunting |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark**, with NIST SP 800-82 Rev. 3 (2023) applied to the irrigation OT |
| Binding rules checked | FDA Produce Safety Rule qualified exemption requirements (21 CFR 112.5-112.7 and Subpart O); Fla. Stat. 501.171 (2026 statute) |
| Also recorded | Card processor merchant terms (contract); 21 CFR Part 121 (N11-R01) and H-2A (20 CFR 655 Subpart B), both not applicable |
| Assessment dates | 2026-07-13 to 2026-07-17 (self-assessment) |
| Assessor | Owner-operator, with the on-call IT technician. Evidence is self-attested, checked on screen where possible |
| Workbook | `gap-analysis.csv` (122 rows) |
| Adopted | 2026-08-31 |

## 1. Applicability
**Step 1 was to find the rule that binds this farm. No binding cybersecurity rule does.**

| Candidate | Applies? | Why (citation) |
|---|---|---|
| FSMA intentional adulteration rule, 21 CFR Part 121 (**N11-R01**) | **No** | Part 121 applies to a food facility "required to register under section 415" of the FD&C Act (21 CFR 121.1). Farms do not have to register (21 CFR 1.226(b)). It is also a food defense rule, not an IT security rule |
| H-2A rules, 20 CFR Part 655 Subpart B | **No** | The subpart sets the process for an employer that wants to bring in H-2A workers (655.103(a)). The farm has no employees; the custom harvest operator brings its own crew |
| Reportable Food Registry, 21 U.S.C. 350f(d) | **No** | The duty falls on the person who registers a food facility (350f(a)(1)); the farm registers none |
| CIRCIA, 6 U.S.C. 681-681g; proposed 6 CFR Part 226 | **No (proposed)** | No final rule as of 2026-09-25. As proposed, food and agriculture entities are covered only above the SBA size standard; the farm is far below $2.5 million (13 CFR 121.201) |
| FAA Part 107 (small drones) | Yes, but not a cybersecurity rule | The owner holds a remote pilot certificate (107.12), the drone is registered (107.13), and safety events must be reported within 10 days (107.9). Part 137 does not apply: the drone dispenses nothing (137.3). Recorded in P08 only |
| FTC Act Section 5 | Background only | Applies to the farm's own promises to customers (for example on the booking site). Not decomposed into rows |

**Decision: NIST CSF 2.0 is the benchmark, with SP 800-82 Rev. 3 for the OT.** This follows the vertical profile: primary agricultural production has no binding federal cybersecurity regulation, and CSF 2.0 is the sector-neutral baseline. SP 800-82 Rev. 3 was written against CSF 1.1, so its Section 6 guidance is applied to the matching CSF 2.0 subcategories (author mapping, column `ot_application_sp800_82r3`). Neither document is binding; status ratings measure the farm against a voluntary target, not a legal duty. At this size the target is the CSF outcomes a one-person farm can reasonably run, and four subcategories are not applicable (GV.RR-04 no employees, ID.RA-08 no published software, PR.AA-04 no federation, PR.PS-06 no software development).

**Binding rules that reach the farm's data:**
- **Produce Safety Rule, qualified exemption.** The farm's produce sales are far above the $25,000 inflation-adjusted threshold (112.4(a); FDA lists $34,324 for 2023-2025), so it would be a covered farm, **except** that it qualifies for the exemption in 112.5: average annual food sales of about $172,000 are under the inflation-adjusted $500,000 cut-off (FDA lists $686,476 for 2023-2025), and about 56% of food is sold directly to qualified end-users (consumers). A qualified exempt farm must still show the farm name and complete business address at the point of purchase or, for Internet sales, in an electronic notice (112.6(b)(2)-(3)), and must keep records that prove eligibility, including a written annual review (112.7, 112.161(b)). **That is where cybersecurity matters: the exemption is only as good as the sales records in two SaaS platforms.** If the records are lost, the farm cannot show it qualifies.
- **Fla. Stat. 501.171.** The statute's definition of "covered entity" names a sole proprietorship (501.171(1)(b)). The farm holds personal information for 2 individuals (W-9 Social Security numbers) and uses a third-party agent for about 1,800 customer accounts (user names with passwords, 501.171(1)(g)1.b.).

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows cite the eCFR text current as of 2026-09-23 and the 2026 Florida Statutes, with short quotes or paraphrases. FDA's inflation-adjusted cut-offs come from its FSMA inflation-adjusted cut-offs page (content current as of 2026-05-13).
2. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`; `sp800_53_controls` is a key-control subset chosen by the author. Regulation rows use an author mapping.
3. **Evidence.** Self-attested by the owner, checked on screen with the IT technician where possible: SYS-01 user list and activity log (2026-07-15), router and pump controller settings (2026-07-16), file account listing, vendor terms, a sample of 10 sales records, and a walkthrough of the Home Farm and River Field (2026-07-14).
4. **Status.** Met, Partially met, Not met, or Not applicable, as of fieldwork. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 4 | 10 | 16 | 1 |
| CSF 2.0 Identify (21) | 4 | 6 | 10 | 1 |
| CSF 2.0 Protect (22) | 5 | 9 | 6 | 2 |
| CSF 2.0 Detect (11) | 0 | 3 | 8 | 0 |
| CSF 2.0 Respond (13) | 0 | 1 | 12 | 0 |
| CSF 2.0 Recover (8) | 0 | 1 | 7 | 0 |
| **CSF 2.0 subtotal (106)** | **13** | **30** | **59** | **4** |
| Produce Safety Rule qualified exemption (7) | 3 | 3 | 1 | 0 |
| Fla. Stat. 501.171 (6) | 0 | 2 | 4 | 0 |
| Card processor terms, contractual (1) | 1 | 0 | 0 | 0 |
| 21 CFR Part 121, N11-R01 (1) | 0 | 0 | 0 | 1 |
| H-2A, 20 CFR 655 Subpart B (1) | 0 | 0 | 0 | 1 |
| **Total (122)** | **17** | **35** | **64** | **6** |

Of the 99 unmet or partially met rows, 9 are rated High, 40 Moderate, and 50 Low. All 9 High rows are CSF subcategories: GV.SC-05, ID.RA-06, ID.IM-04, PR.AA-01, PR.AA-03, PR.AA-05, PR.DS-11, PR.IR-01, and PR.IR-03.

**The pattern:** the farm now knows its risks (the 2026 risk assessment and BIA meet ID.RA-03 to ID.RA-05 and ID.AM-05), and its data at rest and in transit is protected by default settings and vendors. It **cannot respond or recover**: 27 of the 32 Detect, Respond, and Recover subcategories are Not met. On the OT side, two accounts and one flat network stand between a stranger and the farm's irrigation.

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | MFA on SYS-01 and the booking platform; unique passphrases in a password manager | PR.AA-03, PR.AA-01; Fla. Stat. 501.171(2) | High | 2026-09-15 |
| 2 | Change the router and pump controller default passwords (with the dealer) | PR.AA-01 | High | 2026-09-15 |
| 3 | Add the complete business address to the booking and pre-order pages | 21 CFR 112.6(b)(2)-(3) | Moderate | 2026-09-15 |
| 4 | Dealer account to viewer role; service windows; separate laptop accounts for family | PR.AA-05, GV.SC-10 | High | 2026-09-30 |
| 5 | Adopt POL-01 and the P08 runbook and notification matrix; register the farm's breach contact with vendors | GV.PO-01, ID.IM-04, Fla. Stat. 501.171(4), (6) | High | 2026-08-31 (adopted); 2026-09-30 (contacts) |
| 6 | Business file plan with version history, encrypted backup drive, monthly exports; written annual eligibility review | PR.DS-11; 21 CFR 112.7(b), 112.164, 112.166 | High | 2026-10-31 |
| 7 | Guest isolation for customer Wi-Fi; separate pump house network | PR.IR-01 | High | 2026-11-15 |
| 8 | Standalone freeze alarm; written freeze-night procedure; rehearse with the mutual-aid neighbor | PR.IR-03, ID.IM-02, ID.IM-04 | High | 2026-11-15 to 2026-11-30 |
| 9 | Dealer security terms; AI yield vendor data terms or stop | GV.SC-05, GV.SC-06 | High | 2026-10-31 (AI); 2026-12-31 (dealer) |
| 10 | Monthly activity log review (weekly in freeze season); free security course | DE.CM-03, DE.AE-02, PR.AT-01 | Moderate | 2026-10-31 to 2026-11-30 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes (not current obligations)
- **CIRCIA** (proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25; as proposed it would not reach the farm. Recheck when final.
- **Produce Safety Rule:** FDA's cut-off values are updated with inflation each year, and FDA has said it expects farms to return in 2027 to averaging sales to qualified end-users over 3-year periods after its COVID-era flexibility ended on 2023-11-07. The annual review each January uses the current FDA values.
- **NIST SP 800-82 Rev. 4:** post-adoption note (checked 2026-09-25). NIST published an initial public draft on 2026-09-21 with comments due 2026-11-30. It is a draft and was not used; rows with an OT note flag it in `pending_rule_change`.
- **Fla. Stat. 501.171** was read as the 2026 statute; state bills were not tracked.

# Regulatory Gap Analysis: Cris Santos Company Holdings | Agriculture | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Agriculture, Forestry, Fishing and Hunting (focus division: Crop Farming) |
| Focus division benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark**, with NIST SP 800-82 Rev. 3 applied to OT; plus the binding farm record rules |
| Division regulations | Food Processing: FSMA intentional adulteration (21 CFR Part 121, N11-R01), preventive controls records (21 CFR 117 Subpart F), records access (21 CFR Part 1 Subpart J), OSHA PSM, FAR clauses in USDA contracts. Farm Supply: PCI DSS (contract), FTC Act Section 5 (N42-R01), portal commitments. Group: SEC disclosure (N42-R07), state breach laws |
| Gap tables | `gap-analysis.csv` (Crop Farming, 123 rows); `gap-analysis-food-processing.csv` (30 rows); `gap-analysis-farm-supply.csv` (22 rows); `gap-analysis-group.csv` (7 rows) |
| Assessment dates | 2026-05-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-31) |
| Assessors | Division security and compliance leads with each division's food safety, labor compliance, and OT leads, coordinated by the Group Chief Risk Officer; reviewed by group internal audit |

## 1. Applicability
### 1.1 Which rules bind which division
| Candidate | Crop Farming | Food Processing | Farm Supply | Basis |
|---|---|---|---|---|
| FSMA intentional adulteration, 21 CFR Part 121 (**N11-R01**) | **No** | **Yes**, all 11 facilities | No | Part 121 applies to facilities required to register under FD&C Act section 415 (21 CFR 121.1). Farms are exempt from registration (21 CFR 1.226(b)), and each Crop Farming operation is a farm under 21 CFR 1.227; farm activities subject to the Produce Safety standards are also exempt (121.5(d)). The 4 packinghouses pack mostly outside growers' produce, so they are not farms and they register; group counsel's 2024 review applies Part 121 to all 11 facilities. Food Processing is far above the very small business threshold (121.5(a), 121.3) |
| FDA Produce Safety Rule records, 21 CFR 112 Subpart O | **Yes**, all 38 farms (covered farms, 21 CFR 112.4(a)) | No | No | Average annual produce sales far above the inflation-adjusted $25,000 threshold |
| Preventive controls for human food, 21 CFR Part 117 | No (farms) | **Yes** | No | Registered facilities; food safety plans at all 11 |
| Records access, 21 CFR Part 1 Subpart J | No (1.327(a) excludes farms) | **Yes** | No (does not hold food) | 1.361: records within 24 hours of an official request |
| Food Traceability Rule, 21 CFR Part 1 Subpart S | Yes for listed foods (covered farms) | Yes for listed foods | No | FDA will not enforce before 2028-07-20 (Pub. L. 119-37, described at 91 FR 31723). Tracked, not a current gap driver |
| H-2A earnings records, 20 CFR 655.122(j)-(k) | **Yes** (about 9,000 H-2A workers) | No | No | Field tally in the FMIS is part of the earnings record |
| EPA Worker Protection Standard, 40 CFR 170.311(b) | **Yes** | No | No | Application records in the FMIS |
| OSHA PSM, 29 CFR 1910.119; EPA RMP, 40 CFR Part 68 | No | **Yes**, 2 frozen vegetable plants | No (no anhydrous ammonia or ammonium nitrate stored) | Anhydrous ammonia above 10,000 lb (1910.119 Appendix A; 40 CFR 68.130) |
| FAR 52.204-21, 52.204-23, 52.204-25 (N42-R04, N42-R05) | No | **Yes** (USDA commodity contracts) | No | Clauses in the contract files |
| PCI DSS (contract) | No | No | **Yes** | Acquirer requires an annual report on compliance by a QSA |
| FTC Act Section 5 (**N42-R01**) | Background | Background | **Yes** (portal and e-commerce statements) | Statements to growers and cooperatives |
| FTC Safeguards Rule, 16 CFR Part 314 | No | No | **No** | Grower trade credit is for business purposes; 314.2 defines a consumer by personal, family, or household purposes |
| SEC Reg S-K Item 106; Form 8-K Item 1.05 (**N42-R07**) | Via group | Via group | Via group | The holding company is an SEC registrant |
| State breach laws | Workers, including H-2A workers abroad | Employees | Employees, growers in credit files, online customers | Each state where affected individuals reside; Florida worked example, Fla. Stat. 501.171 |
| CIRCIA (proposed 6 CFR Part 226) | Not in effect | Not in effect | Not in effect | No final rule as of 2026-09-25 |

**Decision for the focus division.** Crop Farming has no binding federal cybersecurity rule. The group measures it against **NIST CSF 2.0** as a voluntary Target Profile, with **SP 800-82 Rev. 3** for OT (its Section 6 applies the Cybersecurity Framework to OT; it was written against CSF 1.1, so its guidance is applied to the matching CSF 2.0 subcategories as an author mapping in column `ot_application_sp800_82r3`). Status ratings for CSF rows measure the division against that voluntary target, not a legal duty. Binding rules that reach farm data (Produce Safety records, H-2A records, WPS records, state data security) are assessed as separate rows.

### 1.2 Excluded or not applicable, with reasons
- **N11-R01 at farms, and 21 CFR Part 1 Subpart J at farms:** see 1.1 (rows G-122 and G-123 in `gap-analysis.csv` record the decision).
- **FTC Safeguards Rule and California privacy law (N42-R08) at Farm Supply:** business-purpose credit, and no customers or operations in California (rows in `gap-analysis-farm-supply.csv`).
- **DFARS 252.204-7012 and CMMC (N31-33-R01, N31-33-R02, N42-R02, N42-R03):** no DoD contracts and no covered defense information in any division.
- **CIRCIA:** not in effect.

## 2. Regulation-by-division matrix
| Requirement | Crop Farming | Food Processing | Farm Supply | Group (corporate) |
|---|---|---|---|---|
| NIST CSF 2.0 (benchmark) with SP 800-82 Rev. 3 | **Primary (voluntary)** | Group program applies | Group program applies | Group program owner |
| N11-R01 21 CFR Part 121 | Not applicable (farms) | **Primary** | Not applicable | Group VP Food Safety and Quality coordinates |
| 21 CFR 112 Subpart O (Produce Safety records) | **Applies** | Not applicable | Not applicable | |
| 21 CFR 117 Subpart F (records) | Not applicable | **Applies** | Not applicable | |
| 21 CFR Part 1 Subpart J; 1.361 (24-hour records) | Not applicable; supplies lot data | **Applies** | Not applicable | |
| Food Traceability Rule (enforcement not before 2028-07-20) | Applies to listed foods (tracked) | Applies to listed foods (tracked) | Not applicable | |
| 20 CFR 655.122(j)-(k) (H-2A) | **Applies** | Not applicable | Not applicable | Group HR keeps payroll and H-2A documents |
| 40 CFR 170.311(b) (WPS records) | **Applies** | Not applicable | Not applicable | |
| OSHA PSM and EPA RMP | Not applicable | **Applies** (2 plants) | Not applicable | |
| Reportable Food Registry, 21 U.S.C. 350f(d) | Not applicable (no registered facility) | **Applies** | Not applicable | |
| FAR 52.204-21, -23, -25 (N42-R04, N42-R05) | Not applicable | **Applies** (USDA contracts) | Not applicable | |
| PCI DSS (contract) | Not applicable | Not applicable | **Primary** | Common controls carved in |
| N42-R01 FTC Act Section 5 | Background | Background | **Applies** (portal, e-commerce) | |
| Buyer, customer, and cooperative contract terms | Buyer 24-hour notice | Customer 24-hour notice; certification audits | Cooperative 72-hour notice; SOC 2 requests | Group General Counsel |
| N42-R07 SEC Item 106 and Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** |
| State breach laws (each state; Florida worked example) | Workers including H-2A | Employees | Growers, customers, employees | Coordinates notices |

## 3. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows cite the eCFR text current through 2026-09-23, the Federal Register, and the 2026 Florida Statutes, with short quotes or paraphrases. PCI DSS rows list requirement numbers with topic labels in our own words; the standard's text is not reproduced.
2. **Target Profile.** Each Crop Farming subcategory has a priority (High 37, Medium 40, Low 29), set by the division security and compliance lead and the Crop Farming division president from P01 and P05.
3. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (SRC-OLIR-CSF-53) in `nist_official_sp800_53r5`. `sp800_53_controls` is an author-selected key-control subset (the same subset used in the group's Small agriculture sample, reused because it still fits). Regulation rows carry an author mapping (no official NIST mapping exists for them).
4. **Evidence.** Interviews with division leadership, ROC staff, farm food safety coordinators, plant food defense and preventive controls qualified individuals, and the Farm Supply credit and portal teams; document review; configuration exports; record samples (120 farm records, 90 plant monitoring records); and P07 test results.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

**Current CSF Tier for Crop Farming: Tier 2 (Risk Informed)**, because the group program and risk process reach the division, but OT practices at the 14 acquired farms are ad hoc. **Target: Tier 3 (Repeatable) by 2027-12-31.** Food Processing and Farm Supply are assessed against their own regulations and are not profiled here.

## 4. Results
### 4.1 Crop Farming (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 12 | 19 | 0 | 0 |
| CSF 2.0 Identify (21) | 9 | 12 | 0 | 0 |
| CSF 2.0 Protect (22) | 5 | 17 | 0 | 0 |
| CSF 2.0 Detect (11) | 3 | 8 | 0 | 0 |
| CSF 2.0 Respond (13) | 7 | 6 | 0 | 0 |
| CSF 2.0 Recover (8) | 3 | 5 | 0 | 0 |
| **CSF 2.0 subtotal (106)** | **39** | **67** | **0** | **0** |
| Produce Safety records, 21 CFR 112 Subpart O (7) | 1 | 5 | 1 | 0 |
| H-2A earnings records and statements, 20 CFR 655.122(j)-(k) (4) | 1 | 3 | 0 | 0 |
| Worker Protection Standard records, 40 CFR 170.311(b) (2) | 0 | 2 | 0 | 0 |
| State data security (Florida worked example) (1) | 0 | 1 | 0 | 0 |
| Buyer agreements (contract) (1) | 0 | 0 | 1 | 0 |
| N11-R01 and Part 1 Subpart J (not applicable to farms) (2) | 0 | 0 | 0 | 2 |
| **Total (123)** | **41** | **78** | **2** | **2** |

Of the 80 partially met or not met rows, 22 are rated High, 43 Moderate, and 15 Low.

**The pattern.** The division meets most governance and risk outcomes because the group program reaches it (risk method, roll-up, board oversight). It falls short in the same places in every function: **OT at the 14 acquired farms, third-party access, and the seasonal workforce.** No CSF subcategory is wholly unmet, but most Protect and Detect outcomes stop at the boundary between corporate IT and farm OT. The two not met rows are binding or contractual: Produce Safety records signed by the person who did the work (G-108) and the buyer 24-hour notice (G-121).

### 4.2 Food Processing (`gap-analysis-food-processing.csv`)
| Regulation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FSMA intentional adulteration, 21 CFR Part 121 (N11-R01) (14) | 4 | 8 | 1 | 1 |
| Preventive controls records, 21 CFR 117 (5) | 2 | 3 | 0 | 0 |
| Records access and traceability, 21 CFR Part 1 (4) | 1 | 2 | 1 | 0 |
| Reportable Food Registry (1) | 0 | 1 | 0 | 0 |
| OSHA PSM (ammonia refrigeration) (2) | 1 | 1 | 0 | 0 |
| FAR clauses in USDA contracts (3) | 1 | 2 | 0 | 0 |
| Customer agreements (1) | 0 | 1 | 0 | 0 |
| **Total (30)** | **9** | **18** | **2** | **1** |

**Not met:** FP-G11 (21 CFR 121.157(b)(2)); FP-G23 (21 CFR 1.1455(c)(3)(ii)). FP-G23 is a readiness gap for a rule FDA will not enforce before 2028-07-20. The most important is 121.157(b)(2): the 2026 assessment is new information about vulnerabilities at actionable process steps (control system paths to setpoints and dosing), and it must trigger reanalysis. The vulnerability assessments (121.130(a)-(b)) and the food safety plans (117.126(b)) are written and signed, but they treat process controls as physical equipment (scenario gap 4).

### 4.3 Farm Supply (`gap-analysis-farm-supply.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| PCI DSS v4.0.1 requirements 1 to 12 (contract) (12) | 12 | 0 | 0 | 0 |
| FTC Act Section 5 (N42-R01) (4) | 1 | 2 | 1 | 0 |
| FTC Safeguards Rule (1) | 0 | 0 | 0 | 1 |
| State data security (Florida worked example) (1) | 0 | 1 | 0 | 0 |
| Portal terms and cooperative requests (2) | 0 | 0 | 2 | 0 |
| Federal contract rules and California privacy law (2) | 0 | 0 | 0 | 2 |
| **Total (22)** | **13** | **3** | **3** | **3** |

Card data controls are mature: the 2026 report on compliance found all 12 PCI DSS requirements in place. **Not met:** FS-G15 (15 U.S.C. 45(a)); FS-G19 (Portal terms); FS-G20 (SOC 2 Type 2). All three concern the Grower Agronomy Portal: an unsubstantiated AI performance claim, a 72-hour cooperative notice commitment with no operating process, and no independent assurance report (P09).

### 4.4 Group obligations (`gap-analysis-group.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| SEC disclosure (N42-R07) (3) | 1 | 2 | 0 | 0 |
| State breach notification laws (2) | 0 | 2 | 0 | 0 |
| OFAC advisory (1) | 1 | 0 | 0 | 0 |
| CIRCIA (proposed) (1) | 0 | 0 | 0 | 1 |
| **Total (7)** | **2** | **4** | **0** | **1** |

Across all four tables, 110 rows are partially met or not met: 30 High, 58 Moderate, and 22 Low.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation or benchmark | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Farm OT reachable from the corporate cloud and the integrator (1) | CF | CSF 2.0 PR.IR-01, PR.AA-03, DE.CM-06; SP 800-82r3 5.2.3, 6.2.10 | High | Integrator through group PAM; OT DMZ; farm directory under PAM | Crop Farming OT security manager | 2026-12-31 |
| 2 | Cyber missing from food defense and food safety plans (4) | FP | 21 CFR 121.130(a)-(b), 121.135, 121.157(b)(2); 117.126(b); 29 CFR 1910.119(l) | High | Reanalysis with cyber scenarios; setpoint integrity checks; control changes through MOC | Food Processing VP Food Safety and Quality | 2027-03-31 |
| 3 | Seasonal identity breaks record attribution (3) | CF | 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1) | High | Named crew accounts; season-end disablement | Crop Farming labor compliance director | 2026-11-30 |
| 4 | Traceability under outage untested (5) | CF, FP | 21 CFR 1.361; 112.166(a) | High | 24-hour records drill with the hub down; signed lot manifests | Group VP Food Safety and Quality | 2027-03-31 |
| 5 | Uneven inheritance and OT monitoring (2) | CF | CSF 2.0 ID.AM-01, ID.RA-01, DE.CM-01 | High | Inheritance matrix; OT monitoring and vulnerability management at all farms | Crop Farming security and compliance lead; Group SOC director | 2027-06-30 |
| 6 | Notification matrix incomplete (6) | All | Form 8-K Item 1.05; Fla. Stat. 501.171(3)-(6); buyer, customer, cooperative terms | Moderate | Multi-regulator matrix (P08); cross-division tabletop | Group General Counsel | 2026-12-15 |
| 7 | Portal AI and data-use commitments (7) | FS | N42-R01 (15 U.S.C. 45(a)); portal terms | High | Data-use review; substantiate or revise claims; SOC 2 readiness | Farm Supply digital agronomy general manager | 2027-03-31 |
| 8 | Grower credit files over-shared | FS | Fla. Stat. 501.171(2) (worked example) | High | Restrict access; bulk access alerts | Farm Supply credit director | 2026-11-30 |
| 9 | Farm records depend on one SaaS copy | CF | 21 CFR 112.162, 112.164(a)(1); 20 CFR 655.122(j)(4); 40 CFR 170.311(b)(6) | Moderate | Monthly export and retention schedule | Crop Farming Director of Food Safety | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-012, POAM-015, POAM-016, POAM-019, POAM-020, and POAM-022 trace directly to this analysis.

## 6. Pending changes (not current obligations)
- **CIRCIA** (6 CFR Part 226, proposed): no final rule as of 2026-09-25. As proposed it would reach food and agriculture entities through the SBA size-standard criterion, which every division exceeds. Recheck when a final rule publishes.
- **Food Traceability Rule:** FDA proposed extending the compliance date to 2028-07-20 (90 FR 38084, 2025-08-07), and Congress directed FDA not to enforce the rule before that date (Pub. L. 119-37, as FDA described at 91 FR 31723, 2026-05-28). Row FP-G23 tracks readiness.
- **NIST SP 800-82 Rev. 4:** initial public draft published 2026-09-21, comments due 2026-11-30. Not used; OT rows flag it in `pending_rule_change`.
- **H-2A rules (20 CFR Part 655):** DOL proposed on 2025-07-02 (90 FR 28919) to rescind its 2024 farmworker protections rule, which amended 20 CFR 655.122. No final rescission was found in the Federal Register as of 2026-09-25. The division follows the current text of 655.122(j)-(k).

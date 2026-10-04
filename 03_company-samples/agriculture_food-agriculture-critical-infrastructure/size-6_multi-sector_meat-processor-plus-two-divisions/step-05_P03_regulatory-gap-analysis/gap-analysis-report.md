# Regulatory Gap Analysis: Cris Santos Company Holdings | Food and Agriculture | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Food and Agriculture (focus division: Meat Processing, NAICS 311612) |
| Primary regulation | FSMA Intentional Adulteration rule, 21 CFR Part 121 (C-FOOD-AG-R01), applied to Plant 6, with FSIS HACCP and recall rules (9 CFR 417.2-417.5, 418.2-418.3) for electronic CCP records at all six plants and an OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3, voluntary) |
| Division regulations | Food Distribution: FDA registration, refrigerated storage (21 CFR 117.206), sanitary transportation (21 CFR 1.900-1.912), FSIS registration and records (9 CFR 320.1, 320.5), and the Food Traceability Rule (enforcement deferred). Grocery Retail: PCI DSS v4.0.1 (contractual), FACTA receipt truncation, FSIS grinding records, FTC Act Section 5 |
| Gap tables | `gap-analysis.csv` (Meat Processing, 88 rows); `gap-analysis-food-distribution.csv` (42 rows); `gap-analysis-grocery-retail.csv` (67 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31 (plant walkthroughs, including Plant 6 on 2026-07-14), with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads with the Plant 6 FSQA manager (qualified individual under 121.4(c)), the Division food safety manager (Distribution), and the Grocery Retail payments security manager; coordinated by the Group Chief Food Safety and Quality Officer and reviewed by group internal audit |

Regulatory text was read from eCFR (point-in-time 2026-09-23), govinfo.gov, federalregister.gov, and fda.gov. PCI DSS is a copyrighted standard: rows list requirement numbers with short topic labels in our own words.

## 1. Applicability
### 1.1 Who is what under the food rules
| Site | FDA status | FSIS status | Basis |
|---|---|---|---|
| Plants 1 to 5 | Not registered; Part 121 does not apply | Official establishments (federal grant of inspection) | 21 CFR 1.226(g) exempts facilities "regulated exclusively, throughout the entire facility" by USDA under the Federal Meat Inspection Act |
| Plant 6 | **Registered food facility**; Part 121 applies | Official establishment | Its plant-based protein line makes FDA-regulated food, so the plant is not regulated exclusively by USDA (1.226(g) does not apply) and must register (21 CFR 1.225); Part 121 covers facilities required to register (121.1) |
| Five DCs | Registered facilities (they hold FDA-regulated food); Part 121 does not apply because holding is exempt except in liquid storage tanks, and the DCs have none (121.5(b)) | Registered meat wholesaler and public warehouseman (9 CFR 320.5) | 21 CFR 1.225; 121.5(b); 9 CFR 320.5(a) |
| 120 stores | Retail food establishments, which do not register (21 CFR 1.226(c)) | Retail stores that grind beef keep grinding records (9 CFR 320.1(b)(4)) | 21 CFR 1.227 defines a retail food establishment as one whose primary function is selling food directly to consumers |

### 1.2 Part 121 at Plant 6: size and exemptions
- **Very small business (121.5(a)):** does not apply. The group's human food sales are thousands of times the $10 million base figure.
- **Small business:** 121.3 defines a small business as a business (including any subsidiaries and affiliates) employing fewer than 500 full-time equivalent employees; the group has 45,000 employees, so Plant 6 had no extended compliance period. The rule applied from the day the plant-based line began production in 2024.
- **Holding (121.5(b)), intact-container packing (121.5(c)), animal food (121.5(f)):** not claimed for any Plant 6 processing step.
- **Scope decision:** the plan covers every point, step, and procedure of the plant-based process, and every shared system that can reach that food (the brine and dosing skid, the CIP manifold, MES and the recipe master library, and the refrigeration controls). The same vulnerability method is applied voluntarily to the meat lines at all six plants; FSIS describes food defense plans as voluntary in FSIS-regulated establishments, and no food defense plan requirement appears in 9 CFR Parts 416-418. That voluntary work is **not** scored as Part 121 compliance.

### 1.3 Part 121 is not an IT rule, but it reaches the control system
Part 121 regulates intentional adulteration intended to cause wide-scale public health harm. It never mentions computers or networks. It becomes a cyber-physical rule at Plant 6 because a person with HMI, MES, or recipe-library access can add a contaminant (for example, route CIP chemical into brine) without touching the product, and the assessment must evaluate access to the product and the ability to contaminate it (121.130(a)(2)-(3)) and consider an inside attacker (121.130(b)). Treating control-system access as access to the product is an **author interpretation**, recorded as such in the CSV. Mitigation strategies can be cyber controls (named access, two-person formulation approval, a hardwired interlock), and a significant change such as the 2025 MES upgrade triggers reanalysis (121.157(b)(1)).

### 1.4 FSIS HACCP records at all six plants
"The use of records maintained on computers is acceptable, provided that appropriate controls are implemented to ensure the integrity of the electronic data and signatures" (9 CFR 417.5(d)). Entries must be made when the event occurs and be signed or initialed by the employee making them (417.5(b)). An establishment must notify the FSIS District Office within 24 hours of learning or determining that adulterated or misbranded product has entered commerce (418.2).

### 1.5 Food Distribution
- **Refrigerated storage (21 CFR 117.7, 117.206).** A facility solely engaged in the storage of unexposed packaged food is not subject to the hazard analysis and preventive controls subparts but must, for refrigerated packaged food that requires time and temperature control for safety, establish and monitor temperature controls, take corrective action on a loss of control, verify (calibration and review of monitoring and corrective action records within 7 working days, or a justified longer timeframe), and keep records. Cold-chain monitoring (SYS-G6) is how the DCs meet this.
- **Sanitary transportation (21 CFR 1.900-1.912).** Food Distribution is shipper, loader, carrier (private fleet), and receiver. Temperature control during transport, a written operating temperature to carriers, pre-cooling, receiver checks, carrier demonstration of temperature conditions on request, and the rule that food is not sold after a possible material temperature failure until a qualified individual decides (1.908(a)(6)) all depend on telematics data.
- **FSIS (9 CFR 320.1, 320.5).** As a meat wholesaler and public warehouseman, the division registers with FSIS and keeps transaction records.
- **Food Traceability Rule (21 CFR Part 1, Subpart S).** The DCs hold foods on the Food Traceability List. FDA's rule page states that the Continuing Appropriations, Agriculture, Legislative Branch, Military Construction and Veterans Affairs, and Extensions Act of 2026 directed FDA not to enforce the rule before July 20, 2028, and that FDA intends to comply. The rows are scored for readiness, not as current enforcement exposure.
- **No sector cyber rule.** The wholesale-trade profile's primary regulation (NIST SP 800-171 via CMMC and DFARS) applies only to defense contractors; the group has no federal contracts, so the division uses NIST CSF 2.0 as its benchmark.

### 1.6 Grocery Retail
**PCI DSS v4.0.1** (N44-45-R01) is not law. It applies through the acquirer contract, which requires an annual Report on Compliance by a QSA. The division is a merchant, so service-provider-only requirements are not applicable. Other rows: **FACTA receipt truncation** (15 U.S.C. 1681c(g), N44-45-R05), **FSIS grinding records** (9 CFR 320.1(b)(4)), **FTC Act Section 5** (N44-45-R02), and **state breach notification laws** (generic). The FTC Safeguards Rule (N44-45-R03) and Red Flags Rule (N44-45-R04) do not apply: the co-branded card is issued by a partner bank and the division extends no credit itself.

### 1.7 Excluded requirements, with reasons
- **CIRCIA (C-FOOD-AG-R02):** proposed only; no final rule as of 2026-09-25. As proposed (226.2(a)), the group would exceed the SBA size standard for its NAICS codes and would be covered. Tracked in the `pending_rule_change` column and in P08.
- **USCG MTS cyber rule (C-FOOD-AG-R03):** no MTSA-regulated facility.
- **CMMC, DFARS 252.204-7012, FAR 52.204-21 (N42-R02 to N42-R04):** no federal contracts.
- **CCPA and CPPA regulations (N42-R08, N44-45-R06):** the group does not do business in California.
- **COPPA (N44-45-R07) and INFORM (N44-45-R08):** no child-directed services; no online marketplace.
- **21 CFR Part 121 at the DCs and stores:** holding exemption (DCs); stores do not register.
- **OSHA PSM and EPA RMP:** apply to the ammonia systems at five plants and two DCs (threshold quantity 10,000 lb of anhydrous ammonia in 29 CFR 1910.119 Appendix A and 40 CFR 68.130). They are process safety rules managed by site PSM programs and are context here, not scored.

## 2. Regulation-by-division matrix
| Requirement | Meat Processing | Food Distribution | Grocery Retail | Group (corporate) |
|---|---|---|---|---|
| C-FOOD-AG-R01 FSMA Intentional Adulteration, 21 CFR Part 121 | **Primary.** Applies to Plant 6; voluntary method at Plants 1 to 5 | Not applicable (holding exemption, 121.5(b)) | Not applicable (retail food establishments do not register) | Group food defense standard |
| FDA food facility registration, 21 CFR 1.225-1.230 | Plant 6 registered; Plants 1 to 5 exempt (1.226(g)) | Five DCs registered | Exempt (1.226(c)) | Tracks renewals (2026-10-01 to 2026-12-31) |
| FSIS HACCP and recalls, 9 CFR 417, 418 | **Applies** at all six plants | Not applicable (not an establishment) | Not applicable | Group recall coordination |
| FSIS registration and records, 9 CFR 320.1, 320.5 | Records (320.1); registration not needed at official establishments (320.5(c)) | **Applies** (wholesaler and warehouseman) | Grinding records (320.1(b)(4)) | n/a |
| 21 CFR 117.206 refrigerated storage | Not scored (Plant 6's FDA line is under Part 117 preventive controls, outside this analysis) | **Applies** at five DCs | Not applicable | Cold-chain platform (SYS-G6) |
| Sanitary transportation, 21 CFR 1.900-1.912 | Plant 6 as a shipper; Plants 1 to 5 are outside the subpart (1.900(b)(3) excludes food located in facilities regulated exclusively by USDA) | **Applies** (shipper, loader, carrier, receiver) | Receiver at stores | n/a |
| Food Traceability Rule, 21 CFR 1.1300 et seq. | Plant 6 if its products contain listed foods (none today) | Applies; enforcement not before 2028-07-20 | Applies to listed foods; enforcement not before 2028-07-20 | Common lot key (P01 GR-19) |
| Reportable Food Registry, 21 U.S.C. 350f | Plant 6 (registered facility) | Five DCs (registered facilities) | Not a responsible party (stores do not register) | Coordinates (P08) |
| N44-45-R01 PCI DSS v4.0.1 | Not applicable | Not applicable (no card acceptance) | **Primary.** Annual ROC | Common controls in the ROC responsibility matrix |
| N44-45-R05 FACTA truncation | Not applicable | Not applicable | Applies | n/a |
| N42-R01 / N44-45-R02 FTC Act Section 5 | Applies (general) | Applies (3PL security claims) | Applies (loyalty, camera analytics) | Applies |
| N42-R07 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Employee data (each state where affected individuals reside; Florida worked example: Fla. Stat. 501.171) | Same | Loyalty, online, and employee data | Coordinates |
| C-FOOD-AG-R02 CIRCIA (proposed) | Tracked only | Tracked only | Tracked only | Tracked only |
| SOC 2 (contractual) | Not a service organization | **3PL service in scope** (P09) | Not a service organization (PCI ROC instead) | Group services carved in |

## 3. Method
1. **Requirements.** Part 121 rows follow the rule's structure at paragraph level (Subparts A, C, and D; 121.401 prohibited acts is enforcement context, not a row). FSIS rows are limited to the paragraphs that touch electronic monitoring, records, corrective actions for unforeseen deviations, reassessment, and notification. Food Distribution rows follow 21 CFR 117.206, 1.900-1.912, 9 CFR 320.1 and 320.5, and Subpart S. Grocery Retail rows list the 63 second-level PCI DSS v4.0.1 requirements by number with topic labels in our own words.
2. **Crosswalk.** NIST publishes no mapping for these food rules or for PCI DSS, so those rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. Benchmark rows use the official NIST CSF 2.0 to SP 800-53 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), showing a subset.
3. **Evidence.** Interviews at all six plants, DC-1 and DC-3, and 8 stores; review of the Plant 6 food defense plan, HACCP plans, monitoring, corrective action, and verification records (12-week and 12-month samples), sanitary transportation procedures, the 2025 ROC and the 2026 segmentation test, change records, and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated on the P01 risk scale.

## 4. Results
### 4.1 Meat Processing (`gap-analysis.csv`)
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| Part 121 Subpart A (121.1, 121.4 qualifications, 121.5 exemptions) | 12 | 5 | 3 | 0 | 4 |
| Part 121 Subpart C (121.126-121.157, food defense measures) | 37 | 16 | 14 | 5 | 2 |
| Part 121 Subpart D (121.305-121.325, records) | 13 | 11 | 0 | 0 | 2 |
| **Part 121 subtotal (Plant 6)** | **62** | **32** | **17** | **5** | **8** |
| FSIS HACCP (9 CFR 417), all six plants | 12 | 8 | 4 | 0 | 0 |
| FSIS recalls (9 CFR 418) | 2 | 1 | 1 | 0 | 0 |
| NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary) | 12 | 1 | 11 | 0 | 0 |
| **Total** | **88** | **42** | **33** | **5** | **8** |

The 38 open rows (partially met or not met) break down by gap risk as 18 High, 18 Moderate, and 2 Low. For Part 121 alone, the 22 open rows are 10 High, 10 Moderate, and 2 Low.

**The pattern.** Plant 6 has a working food defense program with a gap in what it looks at:
- **Records and monitoring are strong** (Subpart D fully met; monitoring and corrective actions met), because Plant 6 is built to the group reference architecture: named accounts, audit trails, and SYS-M5.
- **All 5 Not met rows are about change.** The 2025 MES upgrade changed how formulations reach the dosing skid and added remote engineering access, and no reanalysis followed (121.157(b)(1), (b)(2), (c), (d)), so there is nothing to verify (121.150(a)(4)).
- **The vulnerability assessment missed the control-system path** (121.130(a)(2)-(3), (b)) and the plant-based line's CIP manifold has no hardwired interlock (121.135(a); P01 MT-007).
- **FSIS record integrity is a two-plant problem.** 417.5(b) and (d) are partially met because Plants 2 and 5 have shared logins and disabled historian audit trails; the other four plants meet them.

### 4.2 Food Distribution (`gap-analysis-food-distribution.csv`)
| Regulation | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FDA registration (1.225-1.230) | 2 | 2 | 0 | 0 | 0 |
| Part 121 holding exemption (121.5(b)) | 1 | 0 | 0 | 0 | 1 |
| Refrigerated storage (117.7, 117.206) | 9 | 4 | 5 | 0 | 0 |
| Sanitary transportation (1.900-1.912) | 15 | 11 | 4 | 0 | 0 |
| FSIS registration and records (320.1, 320.5) | 3 | 2 | 1 | 0 | 0 |
| Food Traceability Rule (enforcement deferred) | 2 | 0 | 1 | 1 | 0 |
| NIST CSF 2.0 benchmark (voluntary) | 10 | 0 | 8 | 2 | 0 |
| **Total** | **42** | **19** | **19** | **3** | **1** |

The 22 open rows are 2 High, 15 Moderate, and 5 Low. The food rules are mostly met on paper; the gaps sit where those rules **depend on data from shared systems**: monitoring through one cold-chain alert path (117.206(a)(2), High), reviews beyond 7 working days at three DCs (117.206(a)(4)(iii)), and telematics data that cannot be attributed or retained long enough (1.908(a)(3)(iii), (e)(2)). The two Not met benchmark rows are scenario gap 7: drifted standards (GV.PO-01) and undocumented inheritance (GV.RR-02).

### 4.3 Grocery Retail (`gap-analysis-grocery-retail.csv`)
| Obligation | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| PCI DSS v4.0.1 (Req. 1 to 12) | 63 | 49 | 10 | 1 | 3 |
| FACTA, FSIS grinding records, FTC Act, state breach laws | 4 | 1 | 3 | 0 | 0 |
| **Total** | **67** | **50** | **13** | **1** | **3** |

The 14 open rows are 3 High, 10 Moderate, and 1 Low. Grocery Retail is the most mature division. Its open items come from its own testing: one store network design lets the Wi-Fi management network reach POS lanes (Req. 1.3, 2.3, 11.4; High), and payment page script management and tamper detection are incomplete (Req. 6.4 partially met, 11.6 Not met). Requirements 3.6 and 3.7 are not applicable because no account data is stored; 12.9 applies only to service providers.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Plant 6 reanalysis after the 2025 MES upgrade; control-system paths not assessed (3) | MP | 121.130(a), (b); 121.157(b)(1)-(2), (c), (d) | High | Reanalysis with P01 and P07 inputs; food defense sign-off in OT change control | Plant 6 FSQA manager | 2026-12-31 (POAM-023, POAM-007) |
| 2 | No interlock on the plant-based CIP path | MP | 121.135(a) | High | Hardwired CIP interlock; brine system as an actionable process step | Plant 6 plant manager | 2026-11-30 |
| 3 | Electronic CCP record integrity at Plants 2 and 5 (4) | MP | 9 CFR 417.5(b), (d) | High | Audit trails; named MES accounts; electronic signatures | Division controls engineering manager | 2026-12-31 (POAM-004) |
| 4 | No link from a cyber incident to the product decision and 24-hour notices (6) | MP, FD | 9 CFR 417.3(b), 418.2; 21 CFR 117.206(a)(3), 1.908(a)(6) | High | Food safety decision first in the P08 runbook; SOC playbooks; tabletop | Group Chief Food Safety and Quality Officer | 2026-12-15 (POAM-011) |
| 5 | DC temperature monitoring depends on one alert path (2) | FD, MP, GR | 117.206(a)(2); 417.3(b) | High | Local fallback alarms; tested group failover | Group cold-chain services manager | 2027-01-31 (POAM-005) |
| 6 | PCI segmentation path in one store design (5) | GR | PCI DSS Req. 1.3, 2.3, 11.4 | High | Fix the template; re-test 12 stores | Grocery Retail payments security manager | 2026-11-30 (POAM-020) |
| 7 | Food defense verification limited to records review | MP | 121.150(a)(3)(ii), (b) | Moderate | Interlock tests; access log reviews | Plant 6 FSQA manager | 2026-12-31 (POAM-024) |
| 8 | DC record reviews beyond 7 working days | FD | 117.206(a)(4)(iii) | Moderate | Weekly review workflow in SYS-G6 | Division food safety manager (Distribution) | 2026-12-31 (POAM-025) |
| 9 | Payment page scripts and tamper detection (5) | GR | PCI DSS Req. 6.4, 11.6, 12.8 | Moderate | Script inventory, justification, integrity checks, and tamper detection | Digital commerce director | 2026-12-31 (POAM-021) |
| 10 | Food Distribution standards and inheritance (7) | FD | Group policy; SOC 2 readiness | Moderate | Re-issue supplement; inheritance matrix | Food Distribution security and compliance lead | 2027-01-31 (POAM-016, POAM-017) |

**Housekeeping actions:** renew FDA registrations for Plant 6 and the five DCs between 2026-10-01 and 2026-12-31 (21 CFR 1.230(b)); report the DC-5 address change to FSIS (9 CFR 320.5(b)); bring agency workers' food defense training forward to before their first shift (121.4(b)(2)).

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-023 to POAM-025 trace directly to this analysis.

## 6. Pending regulatory changes
- **Part 121:** no proposed amendments found.
- **CIRCIA (C-FOOD-AG-R02):** final rule not published as of 2026-09-25. As proposed, the group would be covered by the size criterion and would owe CISA a covered cyber incident report within 72 hours and a ransom payment report within 24 hours. The P08 matrix carries it as "not in effect".
- **Food Traceability Rule:** FDA proposed extending the compliance date to July 20, 2028 (FR Doc. 2025-14967); FDA's rule page states that Congress directed it not to enforce the rule before that date. Food Distribution and Grocery Retail plan readiness by 2028-04-30.
- **PCI DSS:** PCI SSC ran a request for comments on v4.0.1 toward the next version in June and July 2026; v4.0.1 remains current.

None of these is treated as a current obligation.

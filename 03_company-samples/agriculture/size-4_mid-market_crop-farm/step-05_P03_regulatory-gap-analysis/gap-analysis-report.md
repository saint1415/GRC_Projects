# Regulatory Gap Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed diversified precision-agriculture crop farm with a central packinghouse and a Grower Services unit, NAICS 111998) |
| Tier / Vertical | Mid-Market / Agriculture, Forestry, Fishing and Hunting |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark**. NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security (September 2023), applied to the irrigation, fertigation, and packinghouse OT |
| Binding rules analyzed | Produce Safety Rule records (21 CFR 112 Subpart O); Food Traceability Rule records (21 CFR 1 Subpart S, readiness); H-2A earnings records and statements (20 CFR 655.122(j)-(k)); Worker Protection Standard application records (40 CFR 170.311(b)); PACA growers' agent accounting (7 CFR 46.32(b)); Florida data security, breach notice, and disposal (Fla. Stat. 501.171, 2026 statutes) |
| Also checked | PCI DSS and retail supplier agreements (contractual); 21 CFR Part 121 (N11-R01), found not applicable |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | Security Manager and the GRC analyst, with the vCISO, the Director of Food Safety and Quality, the HR Director, and the Vice President of Grower Services; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |
| Workbook | `gap-analysis.csv` (137 rows) |

## 1. Applicability
**Primary business line:** growing, packing, and marketing fresh produce (vegetables and melons, berries), plus peanuts and sod, and packing and marketing produce for about 30 contract growers.

**Step 1 was to find a cybersecurity rule that binds the company. None applies.**

| Candidate | Applies? | Why (citation) |
|---|---|---|
| FSMA intentional adulteration rule, 21 CFR Part 121 (vertical requirement **N11-R01**) | **No** | Part 121 applies to a food facility "required to register under section 415" of the FD&C Act (21 CFR 121.1). Farms are exempt from registration (21 CFR 1.226(b)). The packinghouse meets the farm definition as a secondary activities farm (21 CFR 1.227): it is not on a primary production farm, it packs, cools, holds, and ripens raw agricultural commodities only, the company's farms grow about 78% of what it packs, and the company owns it. Ripening with ethylene and packaging without further processing stay within the farm definition. Farm activities subject to the Produce Safety standards are also exempt (121.5(d)). The very small business exemption does not apply at this size (sales far above $10 million; 121.3 and 121.5(a)) |
| Reportable Food Registry, 21 U.S.C. 350f(d) | **No** | The duty falls on a "responsible party," the person who registers a food facility (350f(a)(1)); the company registers none. It stays in the P08 matrix as a customer-coordination item |
| CIRCIA, 6 U.S.C. 681-681g; proposed 6 CFR Part 226 | **Not yet (proposed)** | No final rule as of 2026-09-25. **As proposed, the company would be covered**, because it exceeds its SBA size standard ($2.5 million for NAICS 111998, 13 CFR 121.201); there is no agriculture sector criterion. See section 6 |
| SEC cybersecurity disclosure rules | No | Privately held |
| FAR 52.204-21 and 52.204-25 | No | No federal contracts or subcontracts. The NRCS conservation contract is a cost-share agreement, not a procurement contract |
| HIPAA | No | Not a covered entity |
| State comprehensive privacy laws | No (not found) | The company sells produce to businesses and runs a small Florida retail operation. Florida's Digital Bill of Rights is reported to reach only businesses with more than $1 billion in revenue (not verified here) |
| FTC Act Section 5 | Background only | Applies to the company's own privacy and security statements (online store, grower portal). Not decomposed into rows |

**Decision: use NIST CSF 2.0 as the benchmark, with SP 800-82 Rev. 3 for OT.** Primary agricultural production has no binding federal cybersecurity rule, and CSF 2.0 is the sector-neutral baseline in the vertical profile. SP 800-82 Rev. 3 Section 6 applies the Cybersecurity Framework to OT, and its Appendix F is the OT overlay for SP 800-53 Rev. 5 used in the SSP (P02). Because SP 800-82 Rev. 3 was written against CSF 1.1, its guidance is applied to the matching CSF 2.0 subcategories as an author mapping (column `ot_application_sp800_82r3`). Neither document is binding: status ratings measure the company against a voluntary Target Profile, not a legal duty.

**Binding rules that reach the company's data (assessed at requirement level):**
- **Produce Safety Rule records** (21 CFR 112.161-112.166). The company is a covered farm: average annual produce sales far exceed the inflation-adjusted $25,000 threshold (112.4(a)) and the $500,000 qualified exemption limit (112.5). Sweet corn and peanuts are "rarely consumed raw" and not covered produce (112.2(a)(1)); sod is not food. Only record requirements were assessed. The Rule's food safety standards (water, soil amendments, and so on) are outside a cybersecurity gap analysis.
- **Food Traceability Rule** (21 CFR 1.1315-1.1455). Tomatoes, peppers, and watermelons are on the Food Traceability List. The company is grower, initial packer (also for contract growers), and shipper. FDA proposed moving the compliance date to 2028-07-20 (90 FR 38084), and Pub. L. 119-37 sec. 780 directs FDA not to enforce the rule before that date. Rows are rated as **readiness**, not as current enforcement exposure. The spreadsheet exemption for small farms (1.1455(c)(3)(iii)(A), $250,000) does not apply.
- **H-2A earnings records and statements** (20 CFR 655.122(j)-(k)): up to 370 H-2A workers. Field tally in SYS-01 is part of the earnings record.
- **Worker Protection Standard** (40 CFR 170.311(b)): pesticide application and hazard information displayed within 24 hours, kept 2 years, and given on request.
- **PACA** (7 CFR 46.32(b)): Grower Services packs, grades, and markets produce for contract growers under pool agreements, which makes the company a growers' agent (7 CFR 46.2(q)). Growers' agents must keep auditable records of packing and grading results and render accurate, detailed accountings, showing how pool costs and prices are computed. This is the legal anchor for settlement integrity in P09 and for AI-004 grading in P10.
- **Fla. Stat. 501.171** (2026 statutes): the company is a "covered entity." Personal information includes Social Security, passport, and financial account numbers, **biometric data as defined in s. 501.702** (the 14 finger time clocks), and **geolocation** (operator location history in SYS-08), each with a name (501.171(1)(g)1.a.).
- **Contracts:** PCI DSS through the acquirer (requirement text is copyrighted and not reproduced); retail supplier agreements (24-hour notice, food defense plan, traceability).

Drones are flown under 14 CFR Part 107 by certificated remote pilots. Part 107 sets operating rules, not data or security duties, so it was not decomposed. The company does no aerial application (Part 137 does not apply).

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcomes come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows were decomposed from the eCFR text current as of 2026-09-23 and the 2026 Florida Statutes, with short quotes or paraphrases.
2. **Target Profile.** Each subcategory has a priority for the company's CSF Target Profile (**High 38, Medium 40, Low 28**), set by the vCISO and the COO from the risk register (P01) and BIA (P05).
3. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`. The `sp800_53_controls` column is the author's key-control subset. Regulation rows use an author mapping, because no official NIST mapping exists for them.
4. **Evidence.** Interviews with every process owner, document review, configuration exports, and walkthroughs of headquarters, the IOC, the packinghouse, and pump stations at Farms 1 and 2 (2026-07-14 to 2026-07-16; pump-station sample on 2026-08-12 with P07).
5. **Evidence sampling.** Where a requirement operates many times, a random sample was tested from a system-generated population, using the co-sourced firm's attribute sampling table (25 items for a control operating many times a year; 5 to 12 for weekly or monthly controls):
   - harvest and field sanitation records: 30 across the 3 farms (112.161);
   - H-2A worker records and earnings statements: 25 (May 2026 pay periods);
   - pesticide applications: 20 (WPS display timing);
   - Food Safety Coordinator review weeks: 12;
   - contract grower receiving tickets: 20 (FTR initial packer data);
   - weekly settlements reperformed: 5 (PACA accounting);
   - vendor contracts: 20 of 110;
   - incidents: 10 of 22;
   - terminations and transfers: 25 of 214 and 25 of 41 (shared with P07);
   - pump stations: 12 of 54 (shared with P07).
   Each `evidence` cell names its sample and result.
6. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

**Current CSF Tier: Tier 2 (Risk Informed).** IT practices are approved and risk-informed, but OT, vendors, and recovery are inconsistent. **Target: Tier 3 (Repeatable) by 2027-12-31**, meaning policies and standards issued and applied across IT and OT, and recovery demonstrated.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| CSF 2.0 Govern | 6 | 23 | 2 | 0 | 31 |
| CSF 2.0 Identify | 6 | 13 | 2 | 0 | 21 |
| CSF 2.0 Protect | 4 | 15 | 3 | 0 | 22 |
| CSF 2.0 Detect | 1 | 9 | 1 | 0 | 11 |
| CSF 2.0 Respond | 2 | 11 | 0 | 0 | 13 |
| CSF 2.0 Recover | 0 | 6 | 2 | 0 | 8 |
| **CSF 2.0 subtotal** | **19** | **77** | **10** | **0** | **106** |
| Produce Safety records, 21 CFR 112 Subpart O | 2 | 4 | 1 | 0 | 7 |
| Food Traceability Rule, 21 CFR 1 Subpart S (readiness) | 0 | 6 | 1 | 0 | 7 |
| H-2A records and statements, 20 CFR 655.122(j)-(k) | 0 | 4 | 0 | 0 | 4 |
| Worker Protection Standard, 40 CFR 170.311(b) | 1 | 2 | 0 | 0 | 3 |
| PACA growers' agent accounting, 7 CFR 46.32(b) | 0 | 1 | 0 | 0 | 1 |
| Fla. Stat. 501.171 | 0 | 5 | 1 | 0 | 6 |
| PCI DSS (contractual) | 1 | 0 | 0 | 0 | 1 |
| Retail supplier agreements (contractual) | 0 | 1 | 0 | 0 | 1 |
| 21 CFR Part 121, N11-R01 | 0 | 0 | 0 | 1 | 1 |
| **Total** | **23** | **100** | **13** | **1** | **137** |

**Gap risk ratings (113 rows Partially met or Not met):** 23 High, 55 Moderate, 35 Low.

**Reading the results.** This is a defined program with gaps in scale. Governance, risk assessment, and IT protection are largely in place: 19 subcategories are Met, including the risk appetite, the SP 800-30 method, federated identity, and MSSP alerting. The gaps concentrate where the program has not yet reached:
- **OT:** vendor remote access, flat farm networks, no OT logging or monitoring, unverified SCADA and PLC backups (PR.AA-01, PR.IR-01, DE.CM-01, DE.CM-06, RC.RP-03);
- **resilience for the shortest clocks:** freeze protection has no tested manual fallback (PR.IR-03, Not met);
- **regulated records:** shared crew logins make harvest and tally records unattributable (112.161(a)(4), Not met; 655.122(j)(1)), and no company-held copy exists;
- **vendors:** no supply chain program, and the vendors with OT or code access have no security terms (GV.SC-01, GV.SC-05);
- **Grower Services:** no secure development practice, and settlement accuracy is not independently checked (PR.PS-06; 7 CFR 46.32(b)).

The 10 CSF subcategories Not met are GV.SC-01, GV.SC-10, ID.AM-07, ID.RA-08, PR.AT-02, PR.PS-06, PR.IR-03, DE.CM-06, RC.RP-03, and RC.RP-05.

## 4. Priority gaps
| Gap | Row(s) | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Freeze protection depends on SCADA and one alarm path; manual start unwritten | G-073 | High | Standalone alarm, written and tested manual start, freeze-night roster (POAM-012) | Chief Operating Officer with the Farm 2 Farm Manager | 2026-11-30 |
| SCADA integrator's shared, always-on remote account without MFA; no supplier security terms | G-026, G-055, G-078 | High | Brokered, recorded vendor sessions with MFA; security schedule in OT and code vendor contracts (POAM-003, POAM-016) | Security Manager | 2026-12-31 |
| Flat Farm 1 and Farm 2 OT networks; broad packinghouse rule to controllers | G-071 | High | Remove the packinghouse rule by 2026-10-15; segment Farms 1 and 2 (POAM-018) | IT Director | 2027-03-31 |
| OT backups unverified; 31 of 68 PLC and HMI programs held only by the integrator | G-064, G-101 | High | Offline, versioned, verified OT backups (POAM-010) | Director of Irrigation and Water Resources | 2026-12-31 |
| Recovery of SCADA, the farm data hub, and the grower portal never tested | G-050, G-052, G-099, G-100 | High | Contingency plan covering OT and Grower Services; quarterly restore tests (POAM-009, POAM-011) | IT Director | 2027-03-31 |
| Shared crew logins on harvest and tally records | G-053, G-108, G-121 | High | Named crew accounts with tablet PINs; weekly tally edit review (POAM-001, POAM-005) | Farm Managers (3) | 2026-11-15 |
| No OT monitoring or logs; no egress alerts | G-075, G-079 | High | Passive OT monitoring into the SIEM; change alerts (POAM-020) | Security Manager | 2027-03-31 |
| Personnel share over-shared; no data inventory; biometric and geolocation data unmanaged | G-037, G-061, G-122, G-129 | High | Data inventory; restrict and purge; biometric retention rule (R-003, R-035) | HR Director | 2027-01-31 |
| Standing privileged access outside the cloud; no MFA for OT engineers | G-055, G-057 | High | Privileged access management and phishing-resistant MFA for all administrative planes (POAM-002) | Security Manager | 2027-03-31 |
| Regulated records depend on one SaaS copy; 24-hour export untested | G-110, G-111, G-113, G-123, G-126 | Moderate | Monthly full export to the backup account; quarterly 24-hour drill; retention schedule (POAM-022) | Director of Food Safety and Quality | 2026-12-31 |
| No secure development practice; settlement accuracy unchecked | G-070, G-045, G-128 | Moderate | STD-11 and an approval gate; weekly grade-to-case reconciliation (POAM-017, POAM-023) | Vice President of Grower Services | 2027-03-31 |
| No FTR electronic sortable spreadsheet | G-119 | Moderate | Integrate the key data elements in the farm data hub; export test (R-025) | Director of Food Safety and Quality | 2027-12-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list, with evidence, is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Rows moved toward Met (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Packinghouse controller credentials and firewall rule fixed (2026-10-15); named crew accounts (2026-11-15); freeze alarm and manual start tested (2026-11-30); vendor sessions brokered and contract terms signed (2026-12-31); offline OT backups; monthly FMIS export and first 24-hour drill; ransomware tabletop (2026-11-10); notice templates in English and Spanish | G-026, G-064, G-073, G-078, G-101, G-108, G-110, G-113, G-121, G-130, G-131 |
| **2. Build** | 2027 Q1 | Standards issued (STD-01 to STD-11); privileged access management for all administrative planes; quarterly access reviews; OT integrity tabletop (2027-01-20); OT segmentation at Farms 1 and 2; passive OT monitoring; secure development pipeline; 10 remaining Tier 1 vendor reviews | G-017, G-022, G-057, G-065, G-070, G-071, G-075, G-079 |
| **3. Prove** | 2027 Q2 | Restore tests show the BIA RTOs for SCADA, the farm data hub, and the portal; hurricane plan with cyber steps (2027-05-31); unsupported HMIs replaced; SOC 2 Type 2 observation period starts 2027-04-01 (P09) | G-050, G-099, G-100, G-103, G-066 |
| **4. Sustain** | 2027 Q3-Q4 | Annual risk assessment (July 2027); second independent assessment; FTR spreadsheet export tested; Tier 3 target reached by 2027-12-31 | G-119, G-115, G-116, G-117 |

Progress is reported quarterly to the audit committee as the number of rows moving from Partially met or Not met to Met.

## 6. Pending regulatory changes (not current obligations)
- **CIRCIA** (6 CFR Part 226, proposed, 89 FR 23644): no final rule as of 2026-09-25. As proposed, the company would be a covered entity because it exceeds its SBA size standard, and would have to report covered cyber incidents within 72 hours and ransom payments within 24 hours. The P08 matrix tracks it as "not yet required." Recheck when a final rule publishes, because scope may change.
- **Food Traceability Rule compliance date:** FDA proposed extending the compliance date to 2028-07-20 (90 FR 38084, 2025-08-07); no final rule was found in the Federal Register as of 2026-09-25. The appropriations provision (Pub. L. 119-37 sec. 780) directs non-enforcement before that date. The FTR rows carry this note in `pending_rule_change`.
- **H-2A rules (20 CFR Part 655):** the Department of Labor proposed on 2025-07-02 (90 FR 28919) to rescind provisions of its 2024 farmworker protections rule. No final rescission was found as of 2026-09-25. Whether it would change the content of 655.122(j)(1) was not verified. The company follows the current text.
- **No pending changes** were found for 21 CFR Part 112 records, 40 CFR 170.311, or 7 CFR 46.32. Fla. Stat. 501.171 was read as the 2026 statute; state bills were not tracked.

# Regulatory Gap Analysis: Cris Santos Company | Water and Wastewater Systems | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed investor-owned water utility: 11 community water systems and Utility Services for 3 municipal clients) |
| Tier / Vertical | Mid-Market / Water and Wastewater Systems |
| Primary regulation | SDWA section 1433, Community water system risk and resilience, 42 U.S.C. 300i-2 (as amended by AWIA 2018 section 2013; text in effect on 2026-09-25 per uscode.house.gov), for 3 covered PWSIDs |
| Benchmark for the cyber element | NIST CSF 2.0 outcomes, with OT guidance from NIST SP 800-82 Rev. 3 (September 2023) |
| Other regulations analyzed | SDWA public notification and reporting (40 CFR 141.31(b), (d)(1); 141.33(e); Part 141 Subpart Q); Ground Water Rule compliance monitoring and reporting (40 CFR 141.403(b)(3)(i)(A); 141.405(a)(1), (b)(5)(ii)); Fla. Stat. 501.171 for customer personal information (eCFR text verified 2026-09-23 version; Florida statute 2026 text) |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | Security Manager and the GRC analyst with the Emergency Management and Resilience Manager and the Water Quality and Compliance Manager; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability
**Primary business line:** drinking water supply, treatment, storage, and distribution through 11 community water systems, each with its own PWSID. Utility Services (contract operations, monitoring, and billing for 3 municipal systems) is a secondary line; the clients keep their own SDWA duties.

| Regulation | Applies? | Basis |
|---|---|---|
| SDWA section 1433 (C-WATER-R01) | **Yes, for 3 PWSIDs** | Each is a community water system (42 U.S.C. 300f(15)) serving "a population of greater than 3,300 persons" (300i-2(a)(1)). Population served is the only threshold; company size does not matter. EPA states that systems certify "for every individual PWSID number", so the Regional (171,400; size category 100,000 or more), Lakes (63,500; 50,000-99,999), and Ridge (27,400; 3,301-49,999) Systems each have their own RRA, ERP, and deadlines |
| SDWA section 1433, small systems | **No** | The 8 small systems serve 600 to 2,900 persons each. 300i-2(e) directs EPA to give them guidance; it puts no duty on them. The company applies the same method to them voluntarily because they share the ROC and staff |
| 40 CFR Part 141 public notification and reporting | **Yes, all 11 systems** | Every public water system must give public notice (141.201) and report to the State (141.31). The Regional System also sells water to a consecutive system (141.201(c)(1)) |
| Ground Water Rule compliance monitoring | **Yes, all 11 systems** | All are ground water systems that provide 4-log treatment of viruses and monitor under 141.403(b). The 3 covered systems serve more than 3,300 people and must monitor continuously (141.403(b)(3)(i)(A)) |
| Fla. Stat. 501.171 | **Yes** | The company is a covered entity for personal information of its own customers, and a third-party agent for the 15,600 client accounts it bills (501.171(1)(h)) |
| CIRCIA (C-WATER-R02) | **Not in effect** | Proposed only (section 5). Tracked in `pending_rule_change` |

**Deadlines for the covered systems:**
| System (size category) | RRA review (statute and EPA date) | RRA certified | ERP certification (EPA: six months from RRA certification) | ERP status |
|---|---|---|---|---|
| Regional (100,000 or more) | March 31, 2025 | 2025-03-24 | By 2025-09-24 | Certified 2025-09-19 |
| Lakes (50,000-99,999) | December 31, 2025 | 2025-12-17 | By 2026-06-17 | Certified 2026-06-12 |
| Ridge (3,301-49,999) | June 30, 2026 | 2026-06-24 | By **2026-12-24** | In progress; internal target 2026-12-04 |
| Next cycle | Five years after each 2025 or 2026 deadline (300i-2(a)(3)(B)) | | | Regional next RRA review by 2030-03-31 |

Sources: statute text at uscode.house.gov (42 U.S.C. 300i-2); EPA's AWIA section 2013 page, which gives the second-cycle dates, the six-month ERP rule, and the per-PWSID certification rule (as recorded in `02_industry-rules/utilities_water-critical-infrastructure/requirements.csv`, verified 2026-09-25).

**Watch item on population tiers.** The Ridge System (27,400) stays in the 3,301-49,999 category unless it passes 50,000, and a small system that grows past 3,300 would become covered. Acquisitions that merge PWSIDs could also change a category. The Emergency Management and Resilience Manager checks the population served each January against the primacy agency's inventory.

**What the statute does and does not require.** Section 1433 requires the RRA to assess the resilience of "electronic, computer, or other automated systems (including the security of such systems)" (300i-2(a)(1)(A)(ii)) and the ERP to include strategies to improve "the physical security and cybersecurity of the system" (300i-2(b)(1)). It prescribes no controls, and EPA does not require a particular standard or tool. This analysis therefore judges the cyber element against **NIST CSF 2.0** outcomes, applied to OT with **NIST SP 800-82 Rev. 3**. The 30 benchmark rows (G-021 to G-050) are voluntary outcomes used to judge whether the cyber element was actually assessed and addressed. They are not separate legal requirements.

**Excluded, with reasons:**
- **300i-2(f)** (alternative path using EPA-recognized standards): not used. Kept as one Not applicable row (G-020).
- **300i-2(a)(2), (a)(5), (e), (g)-(h)**: duties of EPA or limits on state demands, not duties of the system.
- **EPA's 2023 sanitary survey cybersecurity memorandum**: reported withdrawn in October 2023 in the vertical profile. Not re-verified here and not relied on.
- **Wastewater (POTW) requirements; EPA Risk Management Program (40 CFR Part 68); federal contract clauses; HIPAA; SEC disclosure rules**: not applicable (see `../00_company-facts.md` section 1).

## 2. Method
1. **Requirements.** Statutory rows follow the structure of 42 U.S.C. 300i-2 at paragraph level, quoting the text briefly. Benchmark rows use the CSF 2.0 subcategories most relevant to a water SCADA system, each tied to the SP 800-82 Rev. 3 section that explains it for OT. Part 141 and Florida rows were decomposed from the eCFR and statute text.
2. **Crosswalk.** Statutory, Part 141, and Florida rows were mapped to CSF 2.0 and SP 800-53 Rev. 5 by the author (no official mapping exists). Benchmark rows use a subset of NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`); controls added beyond it are labeled as author additions in `crosswalk_source`.
3. **Evidence.** Interviews with the COO, the Director of Water Operations, the Emergency Management and Resilience Manager, the 4 Plant Managers and their Chief Operators, the Water Quality and Compliance Manager, the Director of Customer Service, and the General Counsel; document review of the 3 RRAs, 3 ERPs, EPA receipts, public notice files, and contracts; configuration exports; and site walkthroughs at all 4 major plants and 3 small systems with P07.
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested, chosen at random by the co-sourced internal audit firm from system-generated populations:
   - EPA certification receipts: 5 of 5 (all certifications in the second cycle so far);
   - RRAs and ERPs: 3 of 3 each;
   - public notice files 2023-2026: 6 of 6;
   - violation reports 2025-2026: 4 of 4;
   - analyzer outages at the covered systems, January to June 2026: 16 of 16;
   - daily lowest residual records: 30 days per covered system;
   - remote gateway sessions, April to June 2026: 25 of 412;
   - OT vendor contracts and access agreements: 14 of 14;
   - operator training records: 20 of 162;
   - contracts with vendors holding customer data: 5 of 5;
   - disposal certificates: 10 of 22.
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Group | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 300i-2(a) Risk and resilience assessment | 6 | 6 | 0 | 0 | 12 |
| 300i-2(b)-(d), (f) ERP, coordination, records, alternative path | 1 | 6 | 0 | 1 | 8 |
| Cyber element benchmark (CSF 2.0 with SP 800-82r3) | 4 | 25 | 1 | 0 | 30 |
| 40 CFR 141.31, 141.33, Subpart Q (reporting and public notification) | 6 | 4 | 0 | 0 | 10 |
| Ground Water Rule (141.403, 141.405) | 2 | 1 | 0 | 0 | 3 |
| Fla. Stat. 501.171 | 3 | 5 | 0 | 0 | 8 |
| **Total** | **22** | **47** | **1** | **1** | **71** |

**Gap risk ratings (48 rows Partially met or Not met):** 19 High, 24 Moderate, 5 Low.

**Reading the results.**
- **Deadlines are met; content lags.** All 5 second-cycle certifications so far were on time (G-010 to G-012), and the Ridge ERP is on track for 2026-12-04. The weakness is substance. The Regional RRA predates the March 2026 interconnection, the Lakes cyber element was copied, and neither the Lakes nor the Ridge ERP has usable OT cyber procedures (G-004, G-013 to G-016). The ERP must incorporate the findings of the assessment (300i-2(b)), so the RRA addenda come first.
- **One program, two maturity levels.** The 25 Partially met benchmark rows nearly all say the same thing: the outcome is achieved at Regional and missing at Lakes, Ridge, or the small systems. The one Not met row is vendor monitoring (G-024), which is missing everywhere.
- **What is working.** Engineered safeguards and manual control (G-041), threat intelligence (G-028), roles (G-021), data protection (G-035), physical asset assessment (G-003), and the mechanics of Tier 1 notice and state reporting (G-051 to G-053, G-056, G-057).
- **Public notice under cyber conditions is the weak link in Part 141.** The notice rules are met in normal operations. A cyber event that takes down the CIS or email would expose missing offline contacts outside Regional (G-058), a missing cyber trigger (G-055), and missing Spanish content at Lakes and Ridge (G-060).

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Unmanaged remote paths into Lakes and Ridge (no MFA, no approval, no recording) | CSF PR.AA-03, PR.AA-05, DE.CM-06 (G-030, G-031, G-043) | High | Remove the Ridge agent and Lakes VPN; gateway only | IT Director (security officer) | 2026-10-31 |
| Ridge ERP lacks cyber strategies and procedures; Lakes annex does not fit Lakes | 300i-2(b), (b)(1)-(2) (G-013 to G-015) | High | Adopt P08 runbook 1 as each ERP's cyber annex; certify Ridge | Emergency Management and Resilience Manager | 2026-12-04 |
| Manual-mode procedures and drills missing at Lakes and Ridge | 300i-2(b)(3) (G-016) | High | Procedures for each chemical feed; Ridge drill before certification | Director of Water Operations | 2026-12-04 |
| RRA cyber elements out of date or copied | 300i-2(a)(1)(A)(ii) (G-004) | High | P01 views as dated addenda; EPA assessment for Lakes and Ridge | Emergency Management and Resilience Manager | 2026-12-31 |
| Integrator B has no security terms and has never been assessed | CSF GV.SC-05, GV.SC-07 (G-023, G-024) | High | Security amendment; first assessment; annual reviews | Director of Water Operations; Security Manager | 2026-12-31 |
| No company-held OT backups at Lakes, Ridge, or small systems | CSF PR.DS-11 (G-036) | High | Offline backups with hash verification | SCADA and Controls Engineering Manager | 2026-12-31 |
| Any-to-any tunnels; dual-homed Lakes historian; flat acquired networks | CSF PR.IR-01 (G-040) | High | Named flows; Ridge isolation; OT DMZ at Lakes and Ridge | IT Director (security officer) | 2027-06-30 |
| No OT monitoring or analysis outside Regional; slow escalation | CSF DE.CM-01, DE.AE-02 (G-042, G-044) | High | OT playbooks and ROC escalation (2026-11-30); sensors (2027-06-30) | Security Manager | 2027-06-30 |
| Shared and default credentials; no baselines; unsupported Ridge OS | CSF PR.AA-01, PR.PS-01, PR.PS-02 (G-029, G-037, G-038) | High | Named accounts; STD-01 baselines; Ridge isolation and replacement | SCADA and Controls Engineering Manager | 2027-09-30 |
| Recovery unproven at Lakes and Ridge | CSF RC.RP-01 (G-048) | High | Rebuild procedures and tests | SCADA and Controls Engineering Manager | 2027-03-31 |
| Offline contacts, cyber trigger, and Spanish content for Tier 1 notice | 40 CFR 141.202(a), (c); 141.205(c)(2) (G-055, G-058, G-060) | Moderate | Monthly exports for all systems; SOP trigger; translated templates | Water Quality and Compliance Manager; Director of Customer Service | 2026-12-04 |
| Grab sampling gap during a Ridge analyzer outage | 40 CFR 141.403(b)(3)(i)(A) (G-061) | Moderate | Timer and log; runbook step | Water Quality and Compliance Manager | 2026-11-30 |
| Breach notice procedure new and untested | Fla. Stat. 501.171(3), (4) (G-065, G-066) | Moderate | Decision log; client notice roles; ransomware tabletop | General Counsel | 2027-02-28 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Close the doors** | 2026 Q4 (to 2026-11-30) | Ridge agent removed and Lakes VPN retired; modem exposure closed; MSSP OT playbooks and ROC escalation; offline contact exports; grab sampling timer; OT training for Lakes and Ridge operators; OT tabletop 2026-11-17 | G-030, G-031, G-043, G-044, G-034, G-058, G-061 |
| **2. Certify with substance** | 2026-12 | RRA addenda for all 3 systems; Ridge ERP with cyber annex, manual-mode procedures, and drill certified by 2026-12-04; Integrator B amendment; OT backups at every site; tunnel rules restricted; Ridge isolated | G-001 to G-005, G-008, G-013 to G-016, G-023, G-024, G-036, G-055, G-060 |
| **3. Bring acquired systems to the Regional standard** | 2027 Q1-Q2 | Named accounts and vaulted credentials; STD-01 baselines; rebuild tests at Lakes (2027-01) and Ridge (2027-03); OT DMZ and sensors at WTP-L1 and WTP-G1; Lakes ERP cyber annex replaced; functional exercise | G-017, G-025 to G-027, G-029, G-037, G-040, G-042, G-048, G-050 |
| **4. Sustain** | 2027 Q3 onward | Ridge platform replaced; annual vendor reviews; quarterly exposure scans; annual RRA addendum refresh; preparation for the 2030 Regional review | G-038, G-024 (ongoing), G-004 (ongoing) |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met. The roadmap is also the ERP "strategies and resources to improve the resilience of the system" (300i-2(b)(1)) for each covered system.

## 6. Pending regulatory and guidance changes
- **CIRCIA** (proposed 6 CFR Part 226; NPRM 89 FR 23644, April 4, 2024) is **still proposed**. The Federal Register shows only town hall notices in 2026 (February 13 and May 26) and no final rule as of 2026-10-05. If finalized as proposed, the company would be a covered entity on two grounds: it exceeds the SBA size standard for NAICS 221310, and it owns community water systems serving more than 3,300 people. It would then report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours, and preserve related data. Rows G-015, G-030, G-039, G-045, G-046, and G-055 are flagged. None is treated as a current obligation.
- **NIST SP 800-82 Rev. 4** was released as an initial public draft (CSRC planning note dated 2026-09-21; comments due 2026-11-30). This analysis uses Rev. 3, the current final version. Section references in the benchmark rows will be re-checked when Rev. 4 is final.
- **State primacy agency rules.** The primacy agency may add state cyber or emergency planning requirements. None was identified for this analysis; the Water Quality and Compliance Manager checks the agency's rulemaking notices each quarter.

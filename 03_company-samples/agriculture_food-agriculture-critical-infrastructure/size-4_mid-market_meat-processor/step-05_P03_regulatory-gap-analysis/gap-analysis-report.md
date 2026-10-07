# Regulatory Gap Analysis: Cris Santos Company | Food and Agriculture | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed meat processor with two USDA-inspected plants) |
| Tier / Vertical | Mid-Market / Food and Agriculture (NAICS 311612) |
| Rules analyzed (binding) | FSIS Sanitation SOPs (9 CFR 416.11-416.17), HACCP (9 CFR Part 417), recalls (9 CFR Part 418), and Listeria control (9 CFR 430.4) where they touch electronic monitoring, records, and process control; OSHA PSM (29 CFR 1910.119) and EPA RMP (40 CFR Part 68) for the two ammonia systems, cyber-relevant paragraphs; Florida data security and disposal (Fla. Stat. 501.171(2), (6), (8)); customer contract terms |
| Benchmarks (voluntary) | The FSMA Intentional Adulteration rule's structure (21 CFR Part 121, C-FOOD-AG-R01) for the food defense plans; NIST CSF 2.0 with NIST SP 800-82 Rev. 3 for OT |
| Text sources | eCFR point-in-time 2026-09-23 (versioner API), read 2026-09-25 to 2026-10-04; federalregister.gov for pending rules |
| Assessment dates | 2026-07-06 to 2026-07-24 (walkthroughs: Plant 1 2026-07-08, Plant 2 2026-07-14); evidence refreshed with P07 results through 2026-08-21 |
| Assessors | GRC Analyst and the VP FSQA, with the Controls Engineering Manager and the Director of Engineering and Maintenance; reviewed by the vCISO and the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability
**Primary business line:** further processing of beef and pork into branded and private-label products at two FSIS official establishments, sold to grocery chains, foodservice distributors, and club stores. The tier calls for every rule that binds that line. The first question is which ones do.

### 1.1 The vertical's primary regulation does not apply
The vertical registry names the FSMA Intentional Adulteration rule (21 CFR Part 121, C-FOOD-AG-R01) as the sector's primary security rule. It applies to "the owner, operator or agent in charge of a domestic or foreign food facility that manufactures/processes, packs, or holds food for consumption in the United States and is required to register under section 415 of the Federal Food, Drug, and Cosmetic Act" (21 CFR 121.1).

The registration rule does not apply to "Facilities that are regulated exclusively, throughout the entire facility, by the U.S. Department of Agriculture under the Federal Meat Inspection Act" (21 CFR 1.226(g)). Both plants make only FSIS-inspected meat products. Neither has a seafood, plant-based, or other FDA-regulated line. So **neither plant registers with FDA, and Part 121 does not apply** (row G-001). For the same reason the Reportable Food Registry duty, which falls on the registrant (21 U.S.C. 350f), does not apply (G-004). FSIS notification under 9 CFR 418.2 takes its place.

**What would change the answer.** If either plant added an FDA-regulated product, that plant would lose the 1.226(g) exemption, have to register, and become subject to Part 121 in full. As an 850-employee company it would not be a "small business" under 121.3 (fewer than 500 full-time equivalent employees). The pending-change column of G-001 records that trigger.

**Food defense is still expected.** FSIS describes functional food defense plans as voluntary for FSIS-regulated establishments, and no food defense plan requirement appears in 9 CFR Parts 416-418 or 430, which were read on eCFR. The company's largest customers require a food defense plan by contract (G-082). The company therefore uses Part 121's method (vulnerability assessment, mitigation strategies, monitoring, verification, reanalysis) as a **voluntary benchmark** for its two plans (G-083 to G-088). Those rows are scored so the roadmap can show progress. They are not compliance findings.

### 1.2 What binds the primary business line
| Rule | Applies? | Why it is a cyber-relevant rule here |
|---|---|---|
| FSIS Sanitation SOPs, 9 CFR 416.11-416.17 | **Yes**, both plants (official establishments) | Daily records may be kept on computers only with "appropriate controls to ensure the integrity of the electronic data" (416.16(b)); CIP sequences that carry out the SSOPs run on PLCs |
| FSIS HACCP, 9 CFR Part 417 | **Yes**, both plants | CCP monitoring runs through historians and sensors; each record entry must be made when the event occurs, with date and time, signed or initialed by the employee (417.5(b)); computer records need "appropriate controls ... to ensure the integrity of the electronic data and signatures" (417.5(d)); critical limits are enforced by HMI setpoints (417.2(c)(3)); changes in "processing methods or systems" trigger reassessment (417.4(a)(3)(i)) |
| FSIS recalls, 9 CFR Part 418 | **Yes**, both plants | Notify the FSIS District Office within 24 hours of learning or determining that adulterated or misbranded product has entered commerce, with type, amount, origin, and destination (418.2), which depends on the traceability database |
| FSIS Listeria control, 9 CFR 430.4 | **Yes**, Plant 1 (post-lethality exposed ready-to-eat products, Alternative 2 with an antimicrobial agent) | The agent's dose is set by MES formulations; testing results and hold-and-test decisions live in the records application |
| OSHA PSM, 29 CFR 1910.119 | **Yes**, both ammonia processes (above 10,000 lb) | Controls, alarms, and interlocks are mechanical integrity equipment ((j)(1)(v)); changes to equipment and technology need management of change ((l)); incidents that could reasonably have resulted in a catastrophic release must be investigated within 48 hours ((m)) |
| EPA RMP, 40 CFR Part 68, Program 3 | **Yes**, both processes (subject to PSM, 68.10(l)(2)) | Parallel prevention duties (68.73, 68.75, 68.79, 68.81), emergency response program (68.95), and backup power for release monitoring equipment from 2027-05-10 (68.67(c)(3); 68.10(g)(1)) |
| Fla. Stat. 501.171 | **Yes** for employee personal information | Reasonable measures (2), third-party agent notice (6), disposal (8); breach notices are in P08 |
| Customer contracts | **Yes** | SOC 2 Type 2 for the portal and EDI services; food defense plan; 24-hour event notice |

**PSM and RMP are not IT rules either.** They never mention networks. They become cyber-relevant because the refrigeration controllers are networked, remotely accessed, and alarm through software. Rows that treat a network or remote access change as a "change to equipment or technology" (1910.119(l), 68.75), or a cyber compromise of a controller as an incident that "could reasonably have resulted in" a catastrophic release (1910.119(m), 68.81), are **author interpretations** and are labeled as such in the CSV.

### 1.3 Other vertical requirements and nearby rules
- **CIRCIA (C-FOOD-AG-R02):** proposed rule only; no final rule in the Federal Register as of 2026-09-25 (G-002). As proposed (226.2(a)), Food and Agriculture entities are covered only if they exceed the SBA size standard (1,000 employees for NAICS 311612). SBA counts all employees, including agency temporaries, averaged over the preceding 24 completed calendar months, and adds the employees of affiliates (13 CFR 121.106(a), (b)(1); 121.103(a)(6)). The company alone averages about 870. Whether the sponsor fund's other portfolio companies are affiliates (common control, 121.103(a)(1)) is a legal question referred to counsel. It decides proposed CIRCIA coverage and nothing else today.
- **USCG MTS cyber rule (C-FOOD-AG-R03):** does not apply; neither plant is an MTSA facility (G-003).
- **CFATS:** authority lapsed in July 2023 (vertical notes); not analyzed.
- **SEC disclosure rules, FAR cyber clauses, PCI DSS, HIPAA:** not applicable (privately held; no federal contracts; no card payments; not a covered entity).

## 2. Method
1. **Requirements.** Rows follow each rule's own structure at paragraph level, read from eCFR. FSIS Part 416 rows cover 416.11-416.16 (416.17, agency verification, is context). Part 417 rows cover every paragraph of 417.2-417.5 and 417.7 that sets a duty; 417.1 (definitions), 417.6 (inadequate systems), and 417.8 (agency verification) are context. PSM and RMP rows are limited to the paragraphs that touch controls, alarms, change, contractors, incidents, emergency response, and audits. Short quotes are from the public-domain CFR text.
2. **Crosswalk.** NIST has published no mapping for 9 CFR, 29 CFR 1910.119, 40 CFR Part 68, or Fla. Stat. 501.171, so those rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. Benchmark rows use the official NIST CSF 2.0 to SP 800-53 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), showing a subset.
3. **Evidence.** Interviews with the process owners at both plants; review of HACCP plans, SSOPs, hazard analyses, validation files, recall procedures, the Listeria program, PSM and RMP program documents, contracts, and the two food defense plans; configuration exports of historians, HMIs, the records application, and remote access paths; the two plant walkthroughs.
4. **Evidence sampling.** Where a requirement operates many times, a random sample was tested from a system-generated population, sized with the co-sourced internal audit firm's attribute sampling table:
   - CCP monitoring records: 60 production days (30 per plant);
   - pre-operational and SSOP records: 60 days (30 per plant);
   - pre-shipment reviews: 40 lots (25 Plant 1, 15 Plant 2);
   - deviation and corrective action records: 20 HACCP and 15 SSOP;
   - OT change records: 25 of 186 at Plant 1 and all 41 at Plant 2 (2026 Q1-Q2);
   - PSM management of change records: all 24 (18 Plant 1, 6 Plant 2) for 2025-2026;
   - ammonia detector and alarm test records: 12 months per plant;
   - Listeria hold-and-test events: all 7 in 2026 H1; environmental results: 40;
   - temporary worker orientation records: 30;
   - HR emails containing personal information: 20.
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated on the P01 risk scale and linked to P01 risk IDs.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| Applicability decisions (C-FOOD-AG-R01 to R03; 21 U.S.C. 350f) | 4 | 0 | 0 | 0 | 4 |
| FSIS Sanitation SOPs (9 CFR 416) | 12 | 7 | 5 | 0 | 0 |
| FSIS HACCP (9 CFR 417) | 29 | 17 | 11 | 1 | 0 |
| FSIS recalls (9 CFR 418) | 3 | 2 | 1 | 0 | 0 |
| FSIS Listeria control (9 CFR 430.4) | 5 | 3 | 2 | 0 | 0 |
| **FSIS subtotal** | **49** | **29** | **19** | **1** | **0** |
| OSHA PSM (29 CFR 1910.119) | 15 | 5 | 10 | 0 | 0 |
| EPA RMP (40 CFR 68) | 9 | 3 | 6 | 0 | 0 |
| Fla. Stat. 501.171 | 3 | 1 | 2 | 0 | 0 |
| Customer contracts | 2 | 0 | 2 | 0 | 0 |
| **Binding rules subtotal** | **78** | **38** | **39** | **1** | **0** |
| Part 121 structure (voluntary benchmark) | 6 | 1 | 4 | 1 | 0 |
| NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary benchmark) | 14 | 0 | 10 | 4 | 0 |
| **Total** | **102** | **39** | **53** | **6** | **4** |

**Gap risk ratings (59 rows Partially met or Not met):** 2 Very High, 22 High, 28 Moderate, 7 Low. For the binding rules alone, the 40 open rows are 15 High, 18 Moderate, and 7 Low. The 2 Very High ratings are both benchmark rows (Plant 2 segmentation and Plant 2 remote access).

**Reading the results.** The food safety programs themselves are sound: hazard analyses, HACCP plans, corrective actions, mock recalls, and the Listeria program are Met. The gaps sit where those programs meet the control systems:
- **Record integrity is the one Not met binding row** (417.5(d)). Shared logins, typed initials, a disabled audit trail at Plant 2, and a shared records administrator mean the company cannot show that electronic CCP records are trustworthy. The same root cause makes 416.16(a)-(b), 417.2(c)(6), and 417.5(b) only Partially met.
- **Changes to control systems bypass the food safety and process safety change processes.** OT change tickets never ask whether a HACCP reassessment (417.4(a)(3)) or SSOP revision (416.14) is needed, and controller and remote access changes bypass PSM and RMP management of change (1910.119(l); 68.75).
- **Incident response does not reach product or process safety.** There was no product hold step for a cyber incident (417.3(b)), no 418.2 decision point, and no cyber scenario in the PSM and RMP emergency plans.
- **Plant 2 is behind on almost everything**, from historian settings to physical control of the engine room.

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Plant 2 remote access without MFA (shared integrator VPN, refrigeration modem) | CSF PR.AA-03 (benchmark); 1910.119(l) | Very High | Plant 2 vendors onto the gateway; remove the modem; MOC review | Security Manager | 2026-10-31 |
| Plant 2 flat network | CSF PR.IR-01 (benchmark) | Very High | Plant 2 segmentation and OT DMZ | IT Director | 2027-03-31 |
| Electronic CCP and SSOP records lack integrity controls | 9 CFR 417.5(b), (d); 416.16(a)-(b); 417.2(c)(6) | High | STD-05; audit trails; named authenticated sign-off; record locking; time sync | VP FSQA | 2026-12-31 |
| HMI setpoints that enforce critical limits change without approval | 9 CFR 417.2(c)(3); 430.4(b)(2) | High | Named accounts; range limits; two-person approval; change alerts | Controls Engineering Manager | 2027-03-31 |
| OT changes skip HACCP reassessment and PSM MOC | 9 CFR 417.4(a)(3)(i); 416.14; 1910.119(l); 68.75 | High | One OT change process with FSQA and PSM review fields (STD-03) | Controls Engineering Manager | 2026-12-31 |
| No product hold or FSIS notice step for cyber incidents | 9 CFR 417.3(b); 418.2 | High | P08 runbooks; tabletop 2026-11-19 | VP FSQA | 2026-11-30 |
| No procedure for operating refrigeration without trustworthy supervisory control | 1910.119(f)(1)(i)(D)-(E); (n); 68.95 | High | Manual operation procedure and drill; cyber scenario in the emergency plans | Director of Engineering and Maintenance | 2026-12-31 |
| x-ray unit configuration not verified (default password found) | 9 CFR 417.4(a)(2)(i) | High | Configuration and credential checks in CCP verification | Plant 1 FSQA Manager | 2026-10-31 |
| Plant 2 cold storage monitoring has one alert path | 9 CFR 417.2(c)(4) | High | Escalation; dedicated gateway network; manual log | Director of Supply Chain and Logistics | 2026-10-31 |
| Food defense plans omit control-system paths (voluntary; contract-required plan) | C-FOOD-AG-R01 (benchmark: 21 CFR 121.130, 121.135); customer contracts | High | Reanalyze both plans with the Controls Engineering Manager; Injector 2 interlock | VP FSQA | 2026-12-31 |
| SOC 2 Type 2 not yet ready | Customer contract | High | P09 plan | Chief Financial Officer | 2027-12-31 |

High and Very High gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Rows closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Plant 2 vendors on the gateway and modem removed; Plant 2 historian audit trail on; x-ray and inspection device credential sweep; Plant 2 cold-chain escalation and manual log; P08 runbooks and first tabletop; offline traceability export and restore test; MOC scope expanded to controls and remote access | 417.2(c)(4), (c)(6); 417.4(a)(2)(i); 418.2; 1910.119(l); 68.75; CSF PR.AA-03 |
| **2. Build** | 2027 Q1 | STD-03 OT change process and STD-05 records integrity standard issued; named HMI and MES accounts; record locking and authenticated sign-off; food defense plans reanalyzed; PSM and RMP emergency plans updated; OT monitoring sent to the MSSP | 416.16(a)-(b); 417.5(b), (d); 417.3(b); 417.4(a)(3)(i); 1910.119(f), (n); 68.95; Part 121 benchmark rows |
| **3. Segment and prove** | 2027 Q2 | Plant 2 segmentation and OT DMZ; immutable OT backups with restore tests at both plants; backup power for the Plant 2 detection panel before the 2027-05-10 RMP date; SOC 2 observation period starts 2027-04-01 (P09) | CSF PR.IR-01, PR.DS-11; 68.67(c)(3) |
| **4. Sustain** | 2027 Q3-Q4 | Plant 1 PHA revalidation with cyber failure modes; HMI replacements; annual risk assessment (July 2027); second independent assessment | 1910.119(e)(3)(iii)-(iv); CSF PR.PS-02 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending regulatory changes
None of these is treated as a current obligation.
- **EPA RMP amendments.** EPA proposed changes to the 2024 Safer Communities by Chemical Accident Prevention rule, including provisions on third-party audits, employee participation, power loss, emergency response exercises, and process safety information (91 FR 8970, 2026-02-24; comment period extended to 2026-05-11 by 91 FR 16621). No final rule was found as of 2026-10-04. The current text still sets 2027-05-10 for several 2024 provisions (68.10(g)), including backup power for release monitoring equipment, so the roadmap plans to that date and the affected RMP rows carry a pending-change note.
- **CIRCIA:** the final rule was not published as of 2026-09-25. If it keeps the NPRM's size-based criterion, coverage depends on the affiliation question in section 1.3. If counsel concludes the company exceeds the standard with affiliates, the P08 notification matrix adds a 72-hour covered incident report and a 24-hour ransom payment report to CISA.
- **FDA registration trigger:** not a rule change, but a business change. Any FDA-regulated product line would bring registration, Part 121, and the Reportable Food Registry (G-001).

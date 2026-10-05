# Regulatory Gap Analysis: Cris Santos Company | Chemical | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed specialty chemical formulator and packager) |
| Tier / Vertical | Mid-Market / Chemical (NAICS 325998) |
| Primary regulation (binding) | **USCG cybersecurity rule**, 33 CFR Part 101 Subpart F (C-CHEMICAL-R02), at the Port plant, plus MTSA cyber reporting (33 CFR 6.16-1; 101.305) and SSI protection (49 CFR Part 1520) |
| Other binding rules in scope | EPA RMP Program 3 (40 CFR Part 68) and OSHA PSM (29 CFR 1910.119) for the elements that depend on the control system; CERCLA and EPCRA release reporting; DOT hazmat security plan (49 CFR 172.800-172.804, 172.704); Florida breach law for employee data |
| Voluntary benchmark | CFATS RBPS 8, 6 CFR 27.230(a)(8) (C-CHEMICAL-R01; the vertical registry's primary regulation; authority lapsed) |
| Tracked, not in effect | CIRCIA proposed rule (C-CHEMICAL-R03); 2026 RMP proposal (91 FR 8970) |
| Assessment dates | 2026-07-06 to 2026-07-31 (Port plant walkthrough 2026-07-14, Inland 2026-07-16, Distribution center 2026-07-21); rows G-010, G-013, G-015, G-031, and G-035 updated 2026-08-28 after P07 testing |
| Assessor | GRC Analyst and the Information Security Manager (CySO), with the VP EHS and Process Safety, the Process Safety Manager, the FSO, and the Controls Engineering Manager |
| Regulatory text checked | 2026-10-05: eCFR point-in-time 2026-09-23 for 33 CFR Parts 6, 101, 105, 154; 40 CFR Parts 68, 302, 355; 29 CFR 1910.119; 49 CFR Part 172; 46 CFR Part 153. Federal Register: the USCG final rule (FR Doc. 2025-00708) and searches for later amendments (none found), CIRCIA (no final rule), and the 2026 RMP proposal |

## 1. Applicability
Applicability was decided first, rule by rule, from the company's sites, chemicals, and quantities (`../00_company-facts.md`, threshold math).

**1. USCG cybersecurity rule (33 CFR Part 101 Subpart F): applies to the Port plant. Binding.**
- Subpart F applies to "the owners and operators of U.S.-flagged vessels, facilities, and OCS facilities required to have a security plan under 33 CFR parts 104, 105, and 106" (101.605(a)).
- Part 105 applies to a facility subject to 33 CFR Part 154 (105.105(a)(1)). Part 154 applies to a facility "capable of transferring oil or hazardous materials, in bulk, to or from a vessel" with a capacity of 250 barrels or more (154.100(a)). Hazardous materials are those listed under 46 CFR 153.40 (154.105).
- The Port plant's barge dock receives sulfuric acid and caustic soda solution, both in Table 1 to 46 CFR Part 153, from tank barges of up to 10,000 barrels. The Port plant therefore has a Coast Guard-approved FSP, and Subpart F applies (G-001).
- The Inland plant and the Distribution center have no marine transfer and are outside the FSP, so the rule does not reach them. The company applies the same standards there by policy (POL-01).
- **Timing.** The rule took effect on 2025-07-16. Its preamble (Section VII) describes three implementation periods: reporting of reportable cyber incidents from the effective date (101.620(b)(7)); training within 6 months, which the text sets as 2026-01-12 (101.650(d)(4)); and, within 24 months, designation of the CySO, the Cybersecurity Assessment (101.650(e)(1), by 2027-07-16), and submission of the Cybersecurity Plan (101.655, by 2027-07-16). The cybersecurity measures in 101.650(a) to (c) and (e) to (i) must be documented in, and operating under, that plan. The analysis rates them against the plan date, and flags the two dates already passed: incident reporting (G-045, G-046) and training (G-021).

**2. EPA RMP (40 CFR Part 68): applies to the Port plant, Program 3.**
- The Ammonia Unit holds 131,325 lb of anhydrous ammonia (TQ 10,000 lb) and interconnected 29% aqua ammonia (78,300 lb of ammonia; "Ammonia (conc 20% or greater)", TQ 20,000 lb).
- Program 1 is not available: the worst-case release endpoint reaches public receptors (68.10(j)(2)). The process is subject to OSHA PSM, so it is Program 3 (68.10(l)(2)). The Port plant is a responding stationary source (68.90(a)).
- The Inland plant is not covered: it buys aqua ammonia below 20% and hydrogen peroxide below 35%.
- RMP is not a cyber rule. It is included because the PCBMS carries the controls, interlocks, emergency shutdown, and notification paths the RMP relies on (G-048 to G-064).

**3. OSHA PSM (29 CFR 1910.119): applies to two Port plant processes.** Anhydrous ammonia (TQ 10,000 lb) in the Ammonia Unit and 70% hydrogen peroxide (listed at 52% or greater, TQ 7,500 lb; 104,860 lb held) in the Peroxide Unit (G-065 to G-070). PSM rows mirror the RMP rows where the text is parallel.

**4. DOT hazmat security plan (49 CFR 172.800): applies.** The company offers and transports 50% hydrogen peroxide (UN2014, Division 5.1, Packing Group II) in its own cargo tanks above 3,000 liters, a "large bulk quantity" of a Division 5.1 PG II material (172.800(b)(10)) (G-073 to G-080).

**5. CFATS (6 CFR Part 27): would apply, but cannot be enforced.** The Port plant holds 70% and 50% hydrogen peroxide, a chemical of interest for theft and diversion at a minimum concentration of 35% with a 400 lb STQ. The company was tiered and ran a Site Security Plan until the statutory authority expired on 2023-07-28. No reauthorization has been enacted. RBPS 8 is kept as a voluntary benchmark (G-081 to G-086).

**6. Other candidates:**
- **CIRCIA** (C-CHEMICAL-R03): proposed only; no final rule in the Federal Register as of 2026-10-05. As proposed, the company would be covered (it exceeds the SBA size standard of 650 employees, and it owns an MTSA facility). Tracked in G-089.
- **2026 RMP proposal** (91 FR 8970, 2026-02-24; comment period extended to 2026-05-11): proposed only. It would revise provisions on safer technology analysis, third-party audits, natural hazards, power loss, and emergency response exercises. Affected rows are flagged in `pending_rule_change`.
- **SEC cyber disclosure:** not applicable (privately held). **FAR clauses:** no federal contracts. **EAR:** U.S. customers only, no controlled technology. **HIPAA:** the employee health plan is fully insured.

## 2. Method
1. **Requirements.** Subpart F was decomposed to the paragraph level, following the rule's own structure (101.620, 101.625, 101.630, 101.635, 101.640, 101.645, 101.650(a) to (i), 101.655). RMP, PSM, release reporting, and DOT rows follow their section structure and cover only the elements that depend on the control system or on cyber measures. CFATS rows reuse the RBPS text (27.230(a)(5), (6), (8); 27.400).
2. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. These are author mappings; NIST publishes no mapping for 33 CFR Part 101, 40 CFR Part 68, 29 CFR 1910.119, 49 CFR Part 172, or 6 CFR Part 27.
3. **Evidence.** Interviews with 24 people (including all 4 shift supervisors and the three OT vendors), document review (FSP, plan draft, HAZOPs, MOC log, contracts), firewall and DCS exports, the OT sensor inventory, and the site walkthroughs. P07 test results were folded in on 2026-08-28.
4. **Status.** Met, Partially met, Not met, or Not applicable. "Not met" for a requirement whose date has not passed means the work has not started; the gap description says "not yet late". Gaps are rated with the P01 risk scale.

## 3. Results summary
| Rule | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| USCG cybersecurity rule, 33 CFR Part 101 Subpart F (binding) | 5 | 29 | 11 | 0 | 45 |
| MTSA cyber and security reporting, 33 CFR 6.16-1 and 101.305 (binding) | 1 | 0 | 1 | 0 | 2 |
| EPA RMP Program 3, 40 CFR Part 68 (binding) | 4 | 13 | 0 | 0 | 17 |
| OSHA PSM, 29 CFR 1910.119 (binding) | 2 | 4 | 0 | 0 | 6 |
| CERCLA and EPCRA release reporting (binding) | 1 | 1 | 0 | 0 | 2 |
| DOT hazmat security plan (binding) | 3 | 4 | 1 | 0 | 8 |
| CFATS RBPS 8 (voluntary benchmark) | 1 | 4 | 0 | 1 | 6 |
| Florida Stat. 501.171 (binding, employee data) | 1 | 1 | 0 | 0 | 2 |
| CIRCIA (proposed) | 0 | 0 | 0 | 1 | 1 |
| **Total** | **18** | **56** | **13** | **2** | **89** |

**Gap risk ratings (69 rows Partially met or Not met):** 16 High, 33 Moderate, 19 Low, 1 Very Low.

**Reading the results.**
- **Process safety is mature; cyber is behind the USCG clock.** 13 of the 18 Met rows are outside the USCG rule: process safety, release reporting, DOT, MTSA physical security reporting, the ERP benchmark row, and Florida vendor notice. Only 5 of 45 USCG rows are Met: applicability, CySO designation, IT lockout, MFA, and no internet-exposed OT.
- **Two USCG dates have already passed.** Training was due 2026-01-12 and is still incomplete (G-021). Cyber incident reporting has applied since the effective date, but the immediate report to the FBI, CISA, and the COTP under 6.16-1 is not in the FSP procedures (G-045, G-046). These are the most urgent compliance items.
- **The Port plant's 2023-2024 investments show up as Partially met, not Not met.** The DMZ, gateway, allowlisting, and offline backups exist; what is missing is coverage of terminal equipment, monitoring of what is logged, testing of what is backed up, and written evidence.
- **The RMP and PSM rows treat the control system as trustworthy equipment.** None is Not met, but 17 of 23 are Partially met because cyber-initiated failures are absent from the PHAs, MOC misses terminal and network changes, and SIS logic is verified only once a year.

## 4. Priority gaps
All 16 High gaps, in target date order.

| Gap | Rows | Action | Owner | Target |
|---|---|---|---|---|
| Cyber incident reporting (FBI, CISA, COTP immediately) not in FSP procedures | G-046 | P08 matrix and runbook steps; control room card; FSP amendment by 2026-12-31 | Facility Security Officer (Port plant) | 2026-10-31 |
| Default passwords on OT devices (tank gauging server found in P07) | G-010 | Sweep all OT devices; document compensating controls | OT Security Engineer | 2026-10-31 |
| Community and agency notification depends on the business network | G-062 | Cellular phones, monthly-checked call lists, second launch path | VP EHS and Process Safety | 2026-10-31 |
| OT backups not tested | G-034 | Full restore test 2026-11-10; then a regular test cycle | Controls Engineering Manager | 2026-11-30 |
| SSI (FSP, FSA, plan draft) over-shared | G-044 | Restricted share for named users; labels and training | Information Security Manager (CySO) | 2026-11-30 |
| Training deadline missed (59 employees, all contractors) | G-021 | Finish employees by 2026-10-31; contractor training at badge issue | Information Security Manager (CySO) | 2026-12-31 |
| No KEV process for OT | G-024 | Monthly KEV match; compensating control records | OT Security Engineer | 2026-12-31 |
| SIS logic verified only at yearly proof test | G-056, G-067 | Monthly logic compare; keyswitch alarm | Process Safety Manager (Port plant) | 2026-12-31 |
| Inland plant open to remote and office access (RBPS 8 benchmark) | G-082 | Inland remediation (P01 R-004) | Controls Engineering Manager | 2026-12-31 |
| IT-OT conduits logged but not monitored | G-036 | MSSP OT monitoring 24x7 | OT Security Engineer | 2027-01-31 |
| Cybersecurity Assessment not started | G-007 | Assessment 2027-01 to 2027-03 | Information Security Manager (CySO) | 2027-03-31 |
| Shared console accounts | G-014 | Unique operator accounts with badge-tap login | Controls Engineering Manager | 2027-03-31 |
| OT vendors have no duty to notify of vulnerabilities or incidents | G-030 | Notice clauses by amendment | General Counsel | 2027-03-31 |
| PHA ignores cyber-initiated control failures | G-051 | PHA addendum with P01 scenarios | Process Safety Manager (Port plant) | 2027-03-31 |
| Cybersecurity Plan about 30% complete | G-002 | Draft remaining sections; submit by 2027-06-15 | Information Security Manager (CySO) | 2027-06-15 |

(The table has 15 lines because the SIS logic gap appears in both the RMP row G-056 and the PSM row G-067.)

High and Moderate gaps are carried into the risk register (P01: R-001, R-002, R-006, R-008, R-011 to R-014, R-033) and the POA&M (P07). The full list, with evidence, is in `gap-analysis.csv`.

## 5. Program roadmap
The roadmap is built backward from the 2027-07-16 USCG date, with a month of margin for the Coast Guard's questions.

| Phase | Window | Outcomes | Rows closed (examples) |
|---|---|---|---|
| **1. Stop the bleeding** | 2026 Q4 | 6.16-1 reporting in procedures and the FSP; default password sweep; employee training complete and contractor training started; SSI share restricted; notification path independent of the business network; full DCS restore test; joint tabletop 2026-11-17 (also the RMP tabletop and the first USCG exercise) | G-010, G-021, G-034, G-040, G-044, G-046, G-062, G-064 |
| **2. Build the plan's content** | 2027 Q1 | Cybersecurity Assessment; critical systems list; KEV process; OT vendor notice clauses; MSSP OT monitoring; approved hardware and software list; standards STD-01 to STD-06; PHA addendum; DOT plan revision | G-007, G-008, G-016, G-024, G-030, G-036, G-051, G-074, G-079 |
| **3. Write and submit** | 2027 Q2 | Plan sections complete; USCG-scoped penetration test; first cyber drills; unique console accounts; submission by 2027-06-15 | G-002, G-003, G-014, G-025, G-039 |
| **4. Operate under the plan** | 2027 Q3 onward | Run the plan as approved; quarterly drills and reviews; first annual plan audit within 12 months of approval; Peroxide Unit HAZOP revalidation with cyber scenarios (2027-10) | G-033, G-043, G-066 |

Progress is reported quarterly to the audit committee as the count of rows moving to Met, with the USCG rows shown separately.

## 6. Pending regulatory changes
- **CIRCIA** (proposed 6 CFR Part 226; NPRM 89 FR 23644, 2024-04-04). Not in effect. If finalized as proposed, the company would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. The P08 notification matrix has a placeholder row marked "proposed, not in effect". No action is required until a final rule sets an effective date.
- **2026 RMP proposal** (91 FR 8970, 2026-02-24). Proposed only. It would revise several 2024 provisions, including power loss, natural hazards, third-party audits, and emergency response exercises. Until a final rule is published, the current text (including the 2027-05-10 standby power date in 68.10(g)(1)) governs, and G-050, G-052, G-053, and G-064 are planned against it.
- **CFATS reauthorization.** None enacted as of 2026-10-05. If CFATS returns, the Port plant would likely need a new Top-Screen and Site Security Plan, and the RBPS 8 rows would become binding. The legacy measures and this benchmark keep that transition short.

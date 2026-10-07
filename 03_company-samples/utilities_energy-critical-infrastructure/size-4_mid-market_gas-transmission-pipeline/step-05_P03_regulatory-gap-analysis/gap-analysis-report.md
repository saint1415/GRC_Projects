# Regulatory Gap Analysis: Cris Santos Company | Energy | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed interstate natural gas transmission pipeline operator) |
| Tier / Vertical | Mid-Market / Energy |
| Primary regulation | TSA Security Directive Pipeline-2021-02G (C-ENERGY-R03): **applies** (TSA-designated). Read from the TSA-published text, effective 2026-05-03 through 2027-05-02 |
| Also analyzed | TSA SD Pipeline-2021-01G (C-ENERGY-R02), effective 2026-01-16 through 2027-01-15; 49 CFR 192.631 control room management (C-ENERGY-R04), SCADA-relevant duties; the 49 CFR Part 1520 SSI duties the directives trigger. CFR text read from eCFR, current through 2026-09-23 |
| Assessment dates | 2026-07-06 to 2026-07-31 (designation status and directive versions confirmed 2026-07-07); evidence refreshed with P07 results through 2026-08-21 |
| Assessor | GRC lead and the Security Manager (Cybersecurity Coordinator), with the Director of Gas Control, the SCADA and OT Engineering Manager, and the Director of Pipeline Safety and Compliance; reviewed by the vCISO and the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Applicability
**Primary business line:** interstate transportation of natural gas under a FERC gas tariff, plus contract operation of two third-party laterals from the same control room.

| Regulation | Applies? | Basis |
|---|---|---|
| TSA SD Pipeline-2021-02G | **Yes** | The directive applies to "Owners and Operators of a hazardous liquid and natural gas pipeline or a liquefied natural gas facility notified by TSA that their pipeline system or facility is critical." Section II.A.1 covers owner/operators notified before July 26, 2022. TSA notified the company in 2021, and the company has held a TSA-approved Cybersecurity Implementation Plan since 2023. There is no size threshold; designation is TSA's decision (SD Section VII.P; footnote 9 ties the population to 6 U.S.C. 1207(b)). The company has 8 Critical Cyber Systems, so the Section II.A.5 "no Critical Cyber Systems" note does not apply |
| TSA SD Pipeline-2021-01G | **Yes** | Same designation (SD 01G Section II.A.1): Cybersecurity Coordinator (II.B), incident reporting to CISA (II.C), vulnerability assessment (II.D, submitted in 2021 and not required again) |
| 49 CFR 192.631 | **Yes, in full** | 192.631(a)(1) covers each operator with a controller who monitors and controls a pipeline facility through SCADA. The reduced-procedure exception in (a)(1)(ii) covers only control rooms limited to distribution with fewer than 250,000 services or transmission without a compressor station. The company has 5 compressor stations. As an interstate operator, PHMSA inspects it directly. Paragraph (d), fatigue mitigation (4 duties), is a human-factors duty with no SCADA content and is outside this analysis; PHMSA's 2024 inspection had no findings on it |
| 49 CFR Part 1520 (SSI) | **Yes, for SSI the company holds** | SD 02G Section IV.B requires plans, reports, and assessment results to be stored and transmitted consistent with Part 1520. The company is a covered person under 1520.7(j), (k), and (l). Rows cover the handling duties in 1520.9, 1520.13, and 1520.19 |

**Other applicable rules and where they are handled:**
| Rule | Where covered |
|---|---|
| 49 CFR 191.3, 191.5, 191.15 (incident definition and reporting) | P08 notification matrix |
| 49 CFR 192.605 and 192.615 (O&M manual, emergency plans, including emergency shutdown and rupture identification) | P08 runbooks; P10 (192.615(a)(12) for the leak-detection model) |
| 18 CFR 284.13(d)(1) (post all planned and actual service outages or reductions in service capacity) | P08 notification matrix |
| 18 CFR 284.12(a)(1)(vii) (NAESB WGQ Cybersecurity Related Standards, Version 4.0, incorporated by reference) | Applies to the customer activities website and electronic communications with shippers. **Not decomposed here:** NAESB standards are copyrighted and were not obtained for this analysis. Tracked as a follow-up for the 2027 cycle, with the website vendor's SOC 2 review (P09) |
| 18 CFR 260.8 and 388.113 (Form No. 567 system flow diagrams filed with a CEII request) | POL-04 handling rule for CEII; no cybersecurity duty on the company beyond the filing procedure |
| State breach notification laws (employees in 3 states; Fla. Stat. 501.171 as the worked example) | P08 notification matrix |

**Not applicable, with reasons:**
- **NERC CIP (C-ENERGY-R01):** the company is not a NERC-registered entity and owns no Bulk Electric System assets. Its 5 power plant customers are registered; gas supply coordination with them is contractual.
- **Form DOE-417 (formerly OE-417):** electric emergency incidents and disturbances only.
- **CIRCIA (C-ENERGY-R05):** proposed only and not in effect (final rule not published as of 2026-09-25). If finalized as proposed, the company would be covered twice over: under proposed 226.2(b)(14)(iv), as corrected by FR Doc. 2024-12084, as "a pipeline facility or system owner or operator required to report cyber incidents by the Transportation Security Administration," and under the size-based criterion, because it exceeds the SBA size standard. Section 6 covers what that would add.

## 2. Method
1. **Requirements.**
   - SD 02G and SD 01G rows follow each directive's own section numbering, at the most granular paragraph that imposes a separate duty. TSA states that neither directive is Sensitive Security Information, so brief quotes are used. Definitions (SD 02G Section VII) are applied, not listed as rows.
   - 192.631 rows follow the regulation's paragraph structure (public-domain federal text), reusing the decomposition validated in the company's industry samples.
   - Part 1520 rows follow 1520.9, with 1520.13 and 1520.19 where 1520.9 points to them.
2. **Crosswalk.** Every row maps to CSF 2.0 and SP 800-53 Rev. 5. All mappings are **author mappings**, labeled as such. No official NIST mapping exists for the TSA directives, 192.631, or Part 1520.
3. **Evidence.** Interviews (COO, vCISO, Security Manager, OT Security Engineers, Director of Gas Control, 5 shift supervisors, 6 controllers, SCADA and OT Engineering Manager, Director of Pipeline Safety and Compliance, 2 Compressor Station Supervisors, MSSP service lead), document review (the 3 TSA plans, TSA correspondence, CRM manual, O&M manual, emergency plan, test and exercise reports, PHMSA 2024 inspection letter, contracts), configuration exports, and walkthroughs of the GCC, the BCC, and Compressor Station 4 with two M&R stations.
4. **Evidence sampling.** Where a requirement operates many times, a random sample was tested from a system-generated population. Sizes follow the co-sourced firm's attribute sampling table (25 for controls that operate many times a year; fewer for small or periodic populations):
   - OT account terminations: 25 of 74 (6 exceeded 1 business day);
   - transfers: 15 of 41 (3 kept SCADA roles);
   - SCADA and network changes under MOC: 25 of 112 (3 without a P2P record);
   - vendor remote sessions: 30 of about 640 (all approved and recorded);
   - field device password register: 40 of about 310 devices (16 past schedule);
   - open CISA KEV entries on OT components: 23 of 23 (6 past the mitigation timeline);
   - DMZ firewall rules: 214 of 214 (4 temporary rules older than 30 days);
   - vendor contracts: 20 of 85 (8 without security terms);
   - CISA incident reports: 2 of 2;
   - file shares scanned for SSI markings: all general shares (11 unmarked SSI copies found).
   Each `evidence` cell names the sample and its result.
5. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| **A. SD Pipeline-2021-02G (primary)** | | | | | |
| II. Applicability, MSSPs, authorized representatives, implementation plan | 2 | 2 | 0 | 1 | 5 |
| III.A Critical Cyber Systems | 0 | 1 | 0 | 0 | 1 |
| III.B Network segmentation | 4 | 2 | 0 | 0 | 6 |
| III.C Access control | 3 | 4 | 2 | 0 | 9 |
| III.D Continuous monitoring and detection | 6 | 7 | 0 | 0 | 13 |
| III.E Patch management | 1 | 4 | 0 | 0 | 5 |
| III.F Incident response plan | 3 | 4 | 0 | 0 | 7 |
| III.G Assessment plan | 6 | 2 | 0 | 0 | 8 |
| IV. Records and SSI | 3 | 5 | 0 | 0 | 8 |
| V. Procedures | 2 | 1 | 0 | 0 | 3 |
| VI. Plan amendments | 0 | 0 | 2 | 1 | 3 |
| **Subtotal SD 02G** | **30** | **32** | **4** | **2** | **68** |
| **B. SD Pipeline-2021-01G** | **10** | **3** | **0** | **1** | **14** |
| **C. 49 CFR 192.631 (SCADA-relevant)** | **29** | **5** | **0** | **0** | **34** |
| **D. 49 CFR Part 1520 SSI duties** | **4** | **3** | **0** | **0** | **7** |
| **Total** | **73** | **43** | **4** | **3** | **123** |

**Gap risk ratings (47 rows Partially met or Not met):** 2 Very High, 12 High, 27 Moderate, and 6 Low. By regulation:
- SD 02G: 2 Very High, 12 High, 19 Moderate, 3 Low (36 gaps);
- SD 01G: 1 Moderate, 2 Low (3 gaps);
- 192.631: 4 Moderate, 1 Low (5 gaps);
- Part 1520: 3 Moderate (3 gaps).

**Reading the results.** The company has a defined, TSA-approved program, and most of the design is sound: segmentation, the remote access gateway, the Coordinator role, incident reporting, the assessment plan, and the pipeline safety duties are Met. The gaps fall in four places:
- **The edges of OT** (III.B.1.b, III.B.2.a, III.C.1.b, III.C.4, III.D.2.b, III.E.2.b): the OEM path, field device passwords, shared station logins, unmonitored stations, and overdue OT patches.
- **Isolation and shutdown governance** (III.D.4, III.F.1, III.F.1.d): the capability exists but has never been used live, and the decision criteria are not written.
- **Regulatory hygiene** (II.B.2, VI.B, VI.D, IV.B, Part 1520): the plan has drifted from the operation, and SSI copies escaped the repository.
- **Recovery evidence** (III.F.1.c): PLC logic backups and a full SCADA rebuild test are missing.

All 4 Not met rows are in SD 02G: III.C.1.b (expired password mitigation timeframe), III.C.4.b (former staff may know station passwords), VI.B and VI.D (unfiled plan amendments).

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| OEM cellular path into a compressor unit, outside the plan; OEM has no plan terms | SD 02G III.B.1.b; II.A.4 (G-011, G-004) | Very High | Survey all units; remove or route through the DMZ; OEM contract terms | SCADA and OT Engineering Manager | 2026-10-31 |
| Two permanent changes never filed as plan amendments | SD 02G VI.B, VI.D (G-067, G-068) | High | File both requests; TSA check in the MOC form | Security Manager | 2026-10-31 |
| Plan milestones missed without notice to TSA | SD 02G II.B.2 (G-007) | High | Notify TSA of revised dates; recover milestones | Security Manager | 2026-10-31 |
| Field device password mitigations expired | SD 02G III.C.1.b (G-017) | High | New timeframe filed with TSA; reset program by area | OT Security Engineer | 2027-03-31 |
| Zone controls bypassed (OEM) and temporary rules without expiry | SD 02G III.B.2.a (G-013) | High | Remove bypass; automatic rule expiry | OT Security Engineer | 2026-10-31 |
| No OT monitoring or baseline at 3 stations and field sites | SD 02G III.D, III.D.2.b (G-024, G-031) | High | Sensors at Compressor Stations 2, 4, and 5; field telecom baseline | Security Manager | 2027-03-31 |
| Isolation never performed live; no shutdown criteria | SD 02G III.D.4, III.F.1, III.F.1.d (G-036, G-042, G-046) | High | Live isolation drill; P08 decision tree adopted into the plan | Director of Gas Control; Security Manager | 2026-12-31 |
| KEV items on OT past timeline | SD 02G III.E.2.b (G-040) | High | Monthly KEV review with Gas Control; out-of-cycle window | SCADA and OT Engineering Manager | 2026-12-31 |
| PLC logic backups missing; rebuild untested | SD 02G III.F.1.c (G-045) | High | Collect PLC logic at all stations; bare-metal rebuild test | SCADA and OT Engineering Manager | 2026-12-31 |
| Station passwords known to former staff | SD 02G III.C.4.b (G-022) | Moderate | Change at every departure until individual logins | SCADA and OT Engineering Manager | 2026-10-31 |
| SSI copies unmarked on a general share | SD 02G IV.B; 1520.9(a)(1)-(4), 1520.13 (G-058, G-117, G-118, G-120) | Moderate | Remove, mark, data loss rule, annual training | Security Manager | 2026-11-30 |
| P2P records missing for 3 SCADA changes | 192.631(c)(2), (j)(1) (G-091, G-115) | Moderate | Verify; block release without a P2P record | Director of Gas Control | 2026-11-30 |
| Coordinator 24x7 reachability informal | SD 01G II.B.2.b (G-076) | Moderate | Published rota; quarterly test calls | Security Manager | 2026-12-31 |

High and Very High gaps are carried into the risk register (P01) and the POA&M (P07). The 192.631 gaps are also tracked in the compliance tracker kept by the Director of Pipeline Safety and Compliance, because PHMSA can cite them. The full list, with evidence, is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Regularize with TSA** | 2026 Q4 | OEM paths removed or rerouted; 2 amendment requests filed; revised milestone dates notified; station passwords changed at departures; SSI copies removed and marked; 2026 assessment plan update and annual report filed by 2026-11-20 | II.A.4; II.B.2; III.B.1.b; III.B.2.a; III.C.4.b; IV.B; VI.B; VI.D; III.G.2.d |
| **2. Prove isolation and recovery** | 2026 Q4 to 2027 Q1 | Live DMZ isolation drill; P08 decision tree adopted into the incident response plan; PLC logic collected at all stations; bare-metal rebuild test; OT log archive | III.D.3.b; III.D.4; III.F.1; III.F.1.c; III.F.1.d |
| **3. Extend to the edges** | 2027 Q1 to Q2 | Sensors and baselines at Compressor Stations 2, 4, and 5; field telecom baseline; field password reset program; station HMI replacement with individual logins and allowlisting | III.C.1.b; III.C.2; III.C.4; III.D.1.d; III.D.2.b; III.D.2.c; III.E.3 |
| **4. Sustain** | 2027 Q3 to Q4 | Architecture design review (due 2027); purple team exercise; NAESB WGQ cybersecurity standards review; SOC 2 Type 2 observation period (P09) | III.G.2.b; III.G.2.c |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met, and is the backbone of the 2026 and 2027 TSA annual reports.

## 6. Pending regulatory changes
None of these is treated as a current obligation.
- **Directive renewals.** SD 01G expires 2027-01-15 and SD 02G expires 2027-05-02. TSA has renewed both series each year; the 02G renewal memo states there were no substantive revisions. Each renewal must be confirmed on receipt (V.A.1; 01G III.A.1) and this analysis rechecked for changes, which TSA highlights in bold.
- **TSA "Enhancing Surface Cyber Risk Management" NPRM** (November 7, 2024) would make pipeline cyber requirements permanent regulations. It was not final as of 2026-09-25. The `pending_rule_change` column flags every SD row.
- **CIRCIA final rule** (C-ENERGY-R05): not published as of 2026-09-25. As proposed, it would add a covered cyber incident report to CISA within 72 hours and a ransom payment report within 24 hours. The company already reports to CISA within 72 hours under SD 01G; the ransom payment report would be new. The P08 matrix carries it as proposed only.
- **NIST SP 800-82 Rev. 4, initial public draft** (published 2026-09-21; comments due 2026-11-30) restructures the OT guide around CSF 2.0. It is a draft; this analysis uses Rev. 3 where OT guidance is cited.

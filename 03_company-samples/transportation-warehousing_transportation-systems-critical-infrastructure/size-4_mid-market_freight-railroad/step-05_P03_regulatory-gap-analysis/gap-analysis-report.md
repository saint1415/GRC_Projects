# Regulatory Gap Analysis: Cris Santos Company | Transportation Systems | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Class II regional freight railroad, north and central Florida) |
| Tier / Vertical | Mid-Market / Transportation Systems |
| Primary regulation named for this vertical | TSA Security Directive 1580/82-2022-01E, Rail Cybersecurity Mitigation Actions and Testing (C-TRANSPORTATION-R01): **applies**, analyzed section by section |
| Other rules analyzed | TSA SD 1580-21-01E, Enhancing Rail Cybersecurity (R01); 49 CFR part 1570 (S01); 49 CFR part 1580 subpart B and the 1570 training rules (S08); 49 CFR part 1580 subpart C (S02); 49 CFR part 1520 (S03); FRA 49 CFR part 236 subpart I tenant duties and 236.3 (S04) |
| Sources | Directive texts as published by TSA (SD 1580-21-01E effective 2026-01-16 to 2027-01-15; SD 1580/82-2022-01E effective 2026-05-03 to 2027-05-02); CFR text from eCFR, point in time 2026-09-23 |
| Assessment dates | 2026-07-06 to 2026-07-31 (applicability confirmed 2026-07-08); evidence refreshed with P07 results through 2026-08-21 |
| Assessor | Cybersecurity Manager and the 2 GRC analysts, with the Director of Safety, Security, and Hazmat, the PTC Program Manager, and the vCISO; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability
**Primary business line:** carload freight on 512 route miles of company track and 52 miles of trackage rights, including about 5,200 PIH tank cars a year, plus contract dispatching and car management for 2 affiliated short lines.

| Rule | Applies? | Basis |
|---|---|---|
| SD 1580/82-2022-01E and SD 1580-21-01E | **Yes** | Both apply to "each freight railroad carrier identified in 49 CFR 1580.101." 1580.101(b) covers a railroad that transports one or more of the categories and quantities of rail security-sensitive materials (RSSM) in a high threat urban area (HTUA). The company's PIH tank cars are RSSM (1580.3). On 2026-07-08 the Director of Safety, Security, and Hazmat confirmed against the route map that 24 route miles of the Jacksonville Subdivision, Jacksonville Terminal Yard, and the interchange tracks lie inside the Jacksonville HTUA in Appendix A to part 1580. The company has been covered since the first directive in each series and operates under a TSA-approved Cybersecurity Implementation Plan (CIP, 2023-03-14) and Cybersecurity Assessment Plan (CAP, most recent approval 2025-06-20) |
| 49 CFR 1570.105, 1570.201, 1570.203 | **Yes** | A freight railroad carrier under 1580.1(a)(1). 1570.203 makes a cyber attack (Appendix A to part 1570) reportable to TSA within 24 hours of initial discovery |
| 49 CFR part 1580 subpart B and 1570.109 to 1570.121 | **Yes** | Same 1580.101(b) status. The TSA-approved security training program, its delivery, and 5-year records apply |
| 49 CFR part 1580 subpart C | **Yes** | The company transports RSSM (1580.201). Location and shipping information within 30 minutes of a TSA request for a railroad other than Class I (1580.203(d)); attended carrier-to-carrier transfers inside an HTUA (1580.205(c)) |
| 49 CFR part 1520 | **Yes** | A covered person (1520.7). The CIP, CAP, CAP annual reports, and assessment results are SSI and must be protected under part 1520 (SD 1580/82-2022-01E IV.B) |
| FRA 49 CFR 236.1005(b)(1) | **No** | PTC installation is required of Class I railroads and railroads providing or hosting intercity or commuter passenger service. The company is neither |
| FRA 49 CFR 236.1006, 236.1029, 236.1033 | **Yes, as a tenant** | The 52-mile trackage-rights movement on the Class I's PTC line is longer than 20 miles, so the exception in 236.1006(b)(4)(iii)(A) for unequipped Class II and III trains is not available. Each controlling locomotive on that segment needs an operative onboard apparatus. The company runs its own tenant back office server pair, so the failure-handling and communications restoration duties reach it |
| FRA 49 CFR 236.3 | **Yes** | Signal apparatus housings must be secured against unauthorized entry. Included because the 150 signal locations hold the CTC field communication controllers |

**Not applicable rows (3):** G-008 (a TSA action, not a company duty; no notice of disagreement received), G-054 (the non-U.S. citizen Cybersecurity Coordinator conditions; both coordinators are U.S. citizens), and G-091 (PTC installation on company track).

**Other applicable rules and where they are handled:**
| Rule | Where covered |
|---|---|
| FRA accident/incident reporting, 49 CFR part 225 (S05) | P08 notification matrix (a cyber event alone is not reportable under part 225) |
| Hazmat security plan, 49 CFR 172.800 and 172.802; car security inspection 174.9; hazmat incident notice 171.15 (S06) | POL-01 risk assessment cycle; P08 notification matrix. The plan was reviewed 2026-03 |
| Fla. Stat. 501.171 (S07) | P08 notification matrix, for employee and customer-contact personal information |
| FRA inspection rules 49 CFR 213.7, 213.233, 215.13, 229.21, 228.11 (S09) | P05 recordkeeping dependencies; P10 AI-001 and AI-002 |
| Pipeline, aviation, and maritime rules (C-TRANSPORTATION-R02 to R05) | Not applicable to a railroad |
| TSA surface cyber NPRM (R06) and CIRCIA (R07) | Proposed only. Section 6 |

## 2. Method
1. **Requirements.**
   - Directive rows follow each directive's own section numbering (for example III.C.4.b) at the most granular level that states a separate duty. The directives are published by TSA and are not SSI; brief paraphrases are used.
   - CFR rows follow the regulation's section and paragraph structure. Brief quotes are used; this is public-domain federal text.
   - Each row was checked against the current text: SD 1580/82-2022-01E and SD 1580-21-01E as published by TSA, and eCFR at 2026-09-23 for parts 1520, 1570, 1580, and 236.
2. **Crosswalk.** Every row is mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. These are **author mappings** (`crosswalk_source` column). No official NIST mapping exists for the directives or these CFR parts.
3. **Evidence.** Interviews with the process owners, the TSA approval letters, the CIP milestone tracker, the CAP and its 2026-06-18 annual report, configuration exports, contracts, the incident log, and walkthroughs of the primary NOC and HQ data center (2026-08-11), the backup NOC and Jacksonville Terminal Yard (2026-08-12), and 6 tower sites, 8 signal locations, and 2 detectors (2026-08-13). The CIP and CAP were examined inside the restricted SSI library and are not reproduced here.
4. **Evidence sampling.** Where a requirement operates many times, a random sample from a system-generated population was tested, using the co-sourced internal audit firm's attribute sampling table (25 items for a control that runs many times a year at moderate risk). Samples used here:
   - security-sensitive new hires for TSA training timing: 25 of 118 (G-078);
   - recurrent training and training records: 25 records (G-079, G-080);
   - shipper-to-carrier RSSM transfers: 25 records (G-085);
   - carrier-to-carrier RSSM transfers inside the HTUA: 25 of about 900 in 2026 (G-086);
   - SSI documents for marking: 20 (G-089);
   - security events in the incident log: 12 of 31 in the last 12 months (G-057);
   - privileged accounts for MFA: 25 of 64 (G-018, shared with P07);
   - tower sites and signal locations for external connections and housing security: 6 of 38 and 8 of 150 (G-011, G-096).
   Each `evidence` cell names the sample and its result.
5. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork. Gaps were rated with the P01 risk scale.

**What counts as Met for a directive row.** TSA approved the CIP, so the test is whether the measure the CIP describes is actually in place and operating on the approved schedule (SD 1580/82-2022-01E II.B.2), not only whether the plan describes it.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| SD 1580/82-2022-01E, Rail Cybersecurity Mitigation Actions and Testing (R01) | 21 | 24 | 5 | 1 | 51 |
| SD 1580-21-01E, Enhancing Rail Cybersecurity (R01) | 7 | 10 | 0 | 1 | 18 |
| **TSA directives subtotal** | **28** | **34** | **5** | **2** | **69** |
| 49 CFR part 1570: applicability, Security Coordinator, reporting (S01) | 5 | 1 | 0 | 0 | 6 |
| 49 CFR part 1580 subpart B and 1570 training rules (S08) | 4 | 2 | 0 | 0 | 6 |
| 49 CFR part 1580 subpart C, RSSM (S02) | 5 | 1 | 0 | 0 | 6 |
| 49 CFR part 1520, SSI (S03) | 0 | 3 | 0 | 0 | 3 |
| **TSA regulations subtotal** | **14** | **7** | **0** | **0** | **21** |
| FRA 49 CFR part 236 (S04) | 3 | 2 | 0 | 1 | 6 |
| **Total** | **45** | **43** | **5** | **3** | **96** |

**Gap risk ratings (48 rows Partially met or Not met):** 17 High, 30 Moderate, 1 Low.

**The 5 Not met rows** are all in SD 1580/82-2022-01E:
- III.C.4.b (G-021): former signal maintainers still know the shared field controller passwords;
- III.E.3 (G-039): unpatched OT has no documented mitigations or timeline;
- III.F.2.b (G-042): the second architecture design review is overdue;
- III.F.2.d (G-044): fewer than one-third of CIP measures were assessed in the last plan year;
- VI.B and VI.D (G-051): no CIP amendment was filed for the affiliate dispatch desks.

**Reading the results.** This is a railroad with a real, TSA-approved program, not one starting from zero. The email, web, and malware defenses in III.D.1 are all Met, as are the Coordinator, training, RSSM, and PTC duties that the Safety department and PTC team have run for years. The gaps fall into three groups:
- **The approved plan is behind schedule.** The field zone milestone was missed (G-006), the assessment program is short of its one-third minimum (G-041, G-044), the architecture review is overdue (G-042), and TSA was not told (G-069). TSA inspects against the plan it approved, so this is the main compliance exposure (P01 R-010).
- **Field OT lags the data center.** Segmentation, external connection inventory, shared accounts, vendor access, monitoring, logging, and patching are strong at the HQ data center and the 2 NOCs, and weak across the 38 tower sites and 150 signal locations (G-011, G-012, G-014, G-021, G-030, G-033, G-038, G-039).
- **Response and recovery are unproven.** The incident response plan has never tested IT/OT isolation with operations staff, and restores have never been run end to end (G-035, G-063, G-064, G-067).

**Reporting.** 1 incident was reported to CISA in the last 12 months, at 41 hours, within the directive's 72 hours. But 2 of 12 sampled events met the directive's definition of a cybersecurity incident and were never assessed for reporting (G-057, G-074). The directive's definition includes events still under investigation, so the classification checklist in P08 now applies it from the first hour.

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| CIP field zone milestone missed; TSA not told | SD 2022-01E II.B.2; SD 21-01E III.C | High | Notify TSA; file a CIP schedule amendment; monthly CIP milestone review by the COO | Cybersecurity Manager | 2026-11-30 |
| Architecture design review overdue; one-third assessment minimum missed | SD 2022-01E III.F.2.a, b, d | High | Review in 2026-11 including field zones; quarterly CAP schedule run by a GRC analyst; P07 counted toward the plan year | Cybersecurity Manager | 2027-05-31 |
| Former maintainers know shared field passwords | SD 2022-01E III.C.4.b | High | Rotate all shared field passwords; vault in PAM; rotate at each departure | Director of Signals and Communications | 2026-12-31 |
| Undocumented external connections; vendors connect without MFA | SD 2022-01E III.B.1.b, III.C.2 | High | Complete the inventory; move the radio and detector vendors to the PAM jump host | Cybersecurity Manager | 2026-12-31 |
| No zones or zone boundary controls in the field | SD 2022-01E III.B.1.c, III.B.2.a | High | Field zone design with OT firewalls at the 6 hub towers and zone rules at the 32 other sites | Director of Signals and Communications | 2027-03-31 |
| OT patching and KEV gaps | SD 2022-01E III.E.1, III.E.2.b, III.E.3 | High | Certified CAD/CTC patches; OT in the weekly KEV review; documented mitigations and an upgrade timeline for 41 locations | Director of Information Technology; Director of Signals and Communications | 2026-12-31 |
| CAD/CTC, BOS, and field logs not collected; no field traffic audit | SD 2022-01E III.D.2.b, III.D.3.a | High | Forward logs to the SIEM; MSSP OT scope; OT sensors at hub towers | Cybersecurity Manager | 2027-03-31 |
| IT/OT isolation never exercised; no isolation authority | SD 21-01E II.D.1.c; SD 2022-01E III.D.4 | High | Isolation decision order in P08; operations-led exercise 2026-12-10 with CTC-territory manual dispatch | Cybersecurity Manager | 2026-12-31 |
| Events not assessed against the directive's incident definition | SD 21-01E II.C.1; 1570.203 | High | Classification checklist; identification time field; train the MSSP and chief dispatchers | Cybersecurity Manager | 2026-11-30 |
| SSI outside the library and unmarked CAP drafts | 1520.9(a); SD 2022-01E IV.B | Moderate | Remove copies; marking check before filing; vendor need-to-know records | Director of Safety, Security, and Hazmat | 2026-11-30 |
| No outage-mode drill for the 30-minute RSSM duty | 1580.203(d) | Moderate | Drill with the TMS unavailable; extract every 2 hours while PIH cars are in the HTUA | Director of Safety, Security, and Hazmat | 2026-11-30 |
| PTC vendor response (8 hours) exceeds the BIA RTO (6 hours) | 236.1033(f) | Moderate | Negotiate 4-hour response; twice-yearly failover test | PTC Program Manager | 2027-03-31 |

High and Moderate gaps are carried into the risk register (P01) and the P07 POA&M. The full list, with evidence, is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Rows closed (examples) |
|---|---|---|---|
| **1. Get back on plan** | 2026 Q4 | TSA notified of the missed milestone and CIP amendments filed (field zones schedule, affiliate desks, crossing monitors); shared logins removed; shared field passwords rotated and vaulted; vendors moved to the jump host; KEV review extended to OT with documented mitigations; incident classification checklist; architecture design review; first end-to-end restore (2026-11-05); operations-led isolation exercise (2026-12-10) | G-006, G-007, G-011, G-017 to G-021, G-038, G-039, G-042, G-051, G-057 to G-059, G-064, G-067, G-069, G-074 |
| **2. Build** | 2027 Q1 | Field zone segmentation and OT sensors at hub towers; CAD/CTC, BOS, and field logs in the SIEM; MSSP OT scope; CIP measure schedule in vendor contracts; OT purple team exercise; PTC vendor response terms | G-002, G-010, G-012, G-014, G-030, G-032 to G-034, G-043, G-095 |
| **3. Prove** | 2027 Q2 | Quarterly restore tests passing within RTO; encryption of the 2 leased circuits; OT inventory and diagrams complete; one-third CAP minimum met and reported; restricted-keyway locks at towers | G-015, G-041, G-044, G-049, G-063, G-096 |
| **4. Sustain** | 2027 H2 | Annual CIP and CAP updates on time; directive renewals checked; second full plan year at or above one-third | All |

Progress is reported to the COO monthly and to the audit committee quarterly as the count of rows moving to Met. The CAP annual report to TSA (due by 2027-06) will show the catch-up.

## 6. Pending regulatory changes
- **TSA Enhancing Surface Cyber Risk Management NPRM** (89 FR 88488, 2024-11-07; C-TRANSPORTATION-R06). **Still proposed;** no final rule as of 2026-09-26. As proposed, it would affect this company directly:
  - Proposed 49 CFR part 1580 subpart D would require a Cybersecurity Risk Management (CRM) program of any Class II or III railroad that "transports one or more of the categories and quantities of RSSM in an HTUA" (proposed 1580.301(b)(2)(ii)). The company meets that criterion, so the directive measures would move into regulation with new elements (for example supply chain risk management, proposed 1580.315).
  - Proposed 1580.325 would require cybersecurity incident reports to CISA within 24 hours, shorter than the directive's 72 hours. P08 already sets a 24-hour internal target where facts allow.
  - 34 directive rows are flagged in `pending_rule_change` as rows the NPRM would codify, and 4 reporting rows as rows the 24-hour proposal would tighten.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR part 226, 89 FR 23644; R07). The final rule has not been published. The proposed sector criterion would cover freight railroad carriers identified in 49 CFR 1580.1(a)(1), (4), or (5), which includes this company. A final rule would add 72-hour covered incident reports and 24-hour ransom payment reports to CISA.
- **Directive renewals.** SD 1580-21-01E expires 2027-01-15 and SD 1580/82-2022-01E expires 2027-05-02. TSA has renewed both series each year. The Cybersecurity Manager re-reads each renewal and updates this analysis within 30 days.
- **IC Surface-2025-01** (Notifying TSA of Significant Cybersecurity Incidents) recommends early notice to TSA ahead of the 72-hour CISA report (SD 1580-21-01E footnote 5). It is a recommendation, not a rule. P08 adopts it as a 12-hour TSOC call target.

None of these proposals is treated as a current obligation.

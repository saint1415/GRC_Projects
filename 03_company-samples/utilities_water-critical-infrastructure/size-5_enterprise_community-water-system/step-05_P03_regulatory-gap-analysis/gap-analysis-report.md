# Regulatory Gap Analysis: Cris Santos Company | Water and Wastewater Systems | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded parent of four state-regulated water utilities; 126 community water systems in FL, GA, NC, TN) |
| Tier / Vertical | Enterprise / Water and Wastewater Systems |
| Primary regulation | SDWA section 1433, Community water system risk and resilience, 42 U.S.C. 300i-2 (as amended by AWIA 2018 section 2013; text in effect on 2026-09-25 per uscode.house.gov), across the 86 covered systems |
| Benchmark for the cyber element | NIST CSF 2.0 outcomes, with OT guidance from NIST SP 800-82 Rev. 3 (September 2023) |
| Other regulations analyzed | SDWA public notification rule (40 CFR Part 141 Subpart Q) and reporting (141.31, 141.33(e)); hazardous substance release reporting (40 CFR 302.6; 40 CFR 355.40 and 355.42) and the RMP threshold for chlorine (40 CFR 68.130); SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach and data security laws (Florida worked example); CIRCIA tracked as proposed |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Vice President, Resilience and Emergency Management and the compliance reporting team; sampling for 8 rows reperformed by Internal Audit |
| Approved | Senior Vice President, Water Quality and Environmental Compliance and the CISO, 2026-08-21; roadmap reviewed by the safety, environmental, and risk committee of the board, 2026-09-10 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| SDWA section 1433 (C-WATER-R01) | **Yes, for 86 of 126 systems** | Each is a community water system (42 U.S.C. 300f(15)) serving a population greater than 3,300 persons (300i-2(a)(1)). Coverage is per system: EPA requires a certification for every individual PWSID. The 40 systems serving 3,300 or fewer are outside section 1433; the enterprise program covers them voluntarily. There is no business-size exemption; population served is the only threshold |
| Public notification rule and 141.31 reporting | **Yes, all 126 systems** | Every public water system must give Tier 1 notice for a waterborne emergency, including "a failure or significant interruption in key water treatment processes" (40 CFR 141.202(a) Table 1 item (7)) |
| Release reporting (40 CFR 302.6; 355.40 and 355.42) | **Yes** | Treatment chemicals, including gaseous chlorine at 9 plants, are hazardous substances; a cyber-caused release is reportable like any other |
| EPA Risk Management Program (40 CFR Part 68) | **Yes, 9 plants** | Gaseous chlorine above the 2,500-pound threshold quantity (40 CFR 68.130). Only the link to cyber-caused release scenarios is analyzed here |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| State breach and data security laws | **Yes** | The law of each state where affected customers reside; Florida (Fla. Stat. 501.171) is the worked example |
| State primacy agency drinking water rules | **Yes (each state)** | Operator licensing, monitoring, and reporting rules in each state. They follow the federal Part 141 structure for the rows analyzed here; state-specific additions are handled by each subsidiary's compliance team |
| CIRCIA (C-WATER-R02) | **Not in force** | No final rule as of 2026-09-25. If finalized as proposed, the company would be covered both by the water-sector criterion and because it exceeds the SBA size standard. Tracked in `pending_rule_change` |
| PCI DSS | Contractual only | Card numbers never enter company systems (hosted pages and IVR); duties sit mostly with the payment processor |
| SOX Section 404 | Separate program | IT general controls over ERP and billing revenue are tested by the SOX program and not repeated here |
| Not applicable | | Wastewater (POTW) requirements (no wastewater service); HIPAA (not a covered entity); federal contract clauses (none) |

**Section 1433 deadlines (EPA second cycle; "AWIA Section 2013" page, last updated May 14, 2026):**
| Size category | Systems | RRA review due | ERP review due | Status on 2026-08-14 |
|---|---|---|---|---|
| 100,000 or more | 11 | March 31, 2025 | September 30, 2025 | All certified on time |
| 50,000-99,999 | 17 | December 31, 2025 | June 30, 2026 | All certified on time |
| 3,301-49,999 | 58 | June 30, 2026 | Six months after each RRA certification (EPA lists December 31, 2026 for a system certifying on the last day) | 58 RRA reviews certified; 34 ERP reviews certified; 24 due by 2026-12-26 |

**What the statute does and does not require.** Section 1433 requires the RRA to assess the resilience of "electronic, computer, or other automated systems (including the security of such systems)" (300i-2(a)(1)(A)(ii)), and the ERP to include strategies to improve "the physical security and cybersecurity of the system" (300i-2(b)(1)). It does not prescribe controls. EPA states that it "does not require water systems to use any designated standards, methods, or tools", but each system is responsible for fully addressing the statute. This analysis therefore uses **NIST CSF 2.0** outcomes as the yardstick for the cyber element and **NIST SP 800-82 Rev. 3** for how each outcome applies to OT. The 28 benchmark rows (G-020 to G-047) are voluntary outcomes used to judge whether the cyber element was actually assessed and acted on. They are not separate legal requirements. AWWA cybersecurity guidance is also voluntary and is used by OT engineering as implementation detail only.

**Not relied on:** EPA's 2023 sanitary survey cybersecurity memorandum. The vertical profile records it as withdrawn in October 2023; that status was not independently re-verified for this analysis, and nothing here depends on it.

## 2. Method
1. **Decompose.** Statutory rows follow the structure of 42 U.S.C. 300i-2 at paragraph level, quoting the text briefly. Other rows follow the eCFR text (2026-09-23 versions of 40 CFR 141.202, 141.205, 141.31, 141.33, 302.6, 355.40, 355.42, 68.130, and 17 CFR 229.106), Form 8-K Item 1.05 and its instructions, and the Florida statute text.
2. **Crosswalk.** Statutory and regulatory rows were mapped to CSF 2.0 and SP 800-53 Rev. 5 by the author (no official mapping exists). Benchmark rows use a subset of NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). The `crosswalk_source` column labels each.
3. **Evidence sampling across systems.** The RRA and ERP rows were tested across the 86 covered systems: certification status and method checks on the full population, and in-depth review of 20 RRAs and 20 ERPs stratified by size category (6, 6, and 8), plus every acquired system not yet integrated. Control-level rows reuse P07 samples where the population is the same (60 items for large populations of key controls, at 95% confidence, a 5% tolerable deviation rate, and zero expected deviations; 25 to 40 items for smaller populations or lower-risk controls). **52 rows were tested by sampling, full-population analytics, or coverage checks; 33 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| 300i-2(a) Risk and resilience assessment | 8 | 3 | 0 | 0 | 11 |
| 300i-2(b)-(d), (f) ERP, coordination, records, alternative path | 3 | 4 | 0 | 1 | 8 |
| Cyber element benchmark (CSF 2.0 with SP 800-82r3) | 5 | 23 | 0 | 0 | 28 |
| 40 CFR 141 Subpart Q and 141.31, 141.33 | 5 | 3 | 0 | 0 | 8 |
| Release reporting and RMP | 1 | 2 | 0 | 0 | 3 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 4 | 1 | 0 | 0 | 5 |
| State breach and data security laws | 5 | 1 | 0 | 0 | 6 |
| CIRCIA (proposed) | 0 | 0 | 0 | 1 | 1 |
| **Total** | **32** | **39** | **0** | **2** | **73** |

**Gap risk levels across the 39 partially met rows:** High 14, Moderate 20, Low 5.

**The main finding.** Every statutory deadline has been met: all 86 RRA review certifications and all 62 ERP review certifications due so far were on time (G-010, G-012). The weaknesses are uneven depth across the portfolio and a concentrated set of OT gaps:
- **Uneven cyber element.** 14 of 86 RRA reviews did not assess automated systems to the enterprise standard: 12 used EPA's small-system checklist and AQ-05 and AQ-06 used their former owners' approaches (G-004). Their ERPs must incorporate the addenda before the 2026-12-26 deadline (G-012).
- **Acquired systems.** AQ-04 to AQ-06 account for most High benchmark gaps: no MFA on remote access (G-028), flat networks (G-037), shared accounts (G-027), backups held only by former integrators (G-033), and no tested rebuild (G-043).
- **Scale gaps.** OT monitoring covers about 84% of the population served but leaves 55 covered systems unmonitored (G-016, G-039). About 1,150 controllers are past vendor support (G-046). 31 OT vendor contracts lack security terms (G-021).
- **Disclosure.** The 8-K materiality process has never been exercised with an OT or public health scenario (G-059, G-060).

**What is working.** Hardwired chemical feed limits were confirmed at all 25 sampled plants (G-015). Tier 1 notices met the 24-hour clock in all 25 sampled cases (G-049, G-050). Governance, threat intelligence, incident planning, Item 106 board oversight, and Florida notice procedures are sound.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-004 | 300i-2(a)(1)(A)(ii) | 14 RRA cyber elements below the enterprise standard | Cyber addenda (POAM-019) | Vice President, Resilience and Emergency Management | 2026-12-11 |
| G-012 | 300i-2(b) | 24 ERP reviews due by 2026-12-26 | ERP sprint (POAM-019) | Vice President, Resilience and Emergency Management | 2026-12-26 |
| G-014 | 300i-2(b)(2) | No manual-mode procedures for each chemical at AQ-04 to AQ-06 | Write and drill procedures (POAM-001) | Chief Operating Officer | 2026-12-15 |
| G-021 | CSF GV.SC-05 | 31 OT vendor contracts lack security terms | POAM-012 | Director of Third-Party Risk Management | 2027-03-31 |
| G-027 | CSF PR.AA-01 | Shared and default credentials | POAM-001; POAM-004; POAM-009; POAM-002 | Director of Identity and Access Management | 2027-01-31 |
| G-028 | CSF PR.AA-03 | 29 systems without gateway MFA | POAM-001 | Vice President, Integration Management Office | 2027-01-31 |
| G-029 | CSF PR.AA-05 | Sessions approved after start; integrators outside the gateway | POAM-005; POAM-001 | Director of OT Security | 2027-01-31 |
| G-033 | CSF PR.DS-11 | AQ backups held by former integrators; stale GCR backups | POAM-001; POAM-016 | Director of OT Engineering | 2026-12-31 |
| G-034 | CSF PR.PS-01 | PLC change verification; default gateway settings | POAM-003; POAM-009 | Director of OT Engineering | 2027-03-31 |
| G-037 | CSF PR.IR-01 | Flat networks at AQ-04 to AQ-06 | POAM-001 | Vice President, Integration Management Office | 2027-01-31 |
| G-043 | CSF RC.RP-01 | No tested rebuild at AQ-04 to AQ-06; GCR transfer RTO | POAM-001; POAM-010 | Chief Operating Officer | 2027-02-28 |
| G-046 | CSF PR.PS-03 | Unsupported controllers and hosts | POAM-008; lifecycle program | Director of OT Engineering | 2027-06-30 |
| G-059 | Form 8-K Item 1.05 | Playbook has no OT scenario or operations member | POAM-014 | General Counsel | 2026-11-30 |
| G-060 | Form 8-K Item 1.05 (materiality determination) | No qualitative factors for public health impacts; timing untested | POAM-014 | General Counsel | 2026-11-30 |

## 5. Compliance roadmap
The roadmap works back from the last ERP review certification due date (2026-12-26).

| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Telemetry gateway fleet audit (POAM-009, 2026-10-31); disclosure committee tabletop with an OT and public health scenario, COO added (POAM-014, 2026-11-12); release reporting step in the runbook (G-056, G-057); AQ-05 agent removed and AQ-04 to AQ-06 manual-mode procedures (POAM-001); RRA cyber addenda for 14 systems (POAM-019, 2026-12-11); AQ public notice SOPs moved to the enterprise SOP (POAM-021, 2026-12-11); last 24 ERP reviews certified (POAM-019, 2026-12-26) | 300i-2(a)(1)(A)(ii), (b); 40 CFR 141.202; 302.6; 355.40; Item 1.05 | EPA portal receipts; addenda; tabletop report; revised SOPs |
| 2027 Q1 | AQ-04 to AQ-06 on the gateway with OT DMZs and SD-WAN (POAM-001, 2027-01-31); OT domain federation (POAM-002); backup control center retest (POAM-010, 2027-02-28); Internal Audit test of Item 106 statements before the 10-K (G-062); PLC logic comparison at GCR (POAM-003); integrator contract terms and attestation (POAM-012) | 300i-2(b)(1); CSF PR.AA, PR.IR, PR.PS; Item 106 | Gateway coverage report; retest report; Item 106 test workpapers |
| 2027 Q2 | GCR unsupported hosts replaced (POAM-008); first wave of OT monitoring extension (POAM-020) | CSF PR.PS-03, DE.CM-01 | Replacement records; coverage report |
| 2027 Q3 to Q4 | Monitoring extension complete (POAM-020, 2027-12-31); independent OT assessment rotation begins at a second ROCC (G-047); annual gap reassessment | 300i-2(b)(4); all | Coverage report; assessment report; updated P03 |

## 6. Pending regulatory changes
- **CIRCIA** (proposed 6 CFR Part 226; NPRM 89 FR 23644, April 4, 2024) is **still proposed**; no final rule had been published as of 2026-09-25. If finalized as proposed, the company would need to report covered cyber incidents to CISA within 72 hours of a reasonable belief that one occurred, report ransom payments within 24 hours, and preserve related data. Rows G-041, G-042, and G-073 carry the note. None of this is treated as a current obligation; reporting to CISA is voluntary today.
- **SEC:** no SEC proposal to amend or rescind Item 1.05 or Item 106 was found as of 2026-09-25, so both remain in force.
- **Section 1433 third cycle:** the next RRA reviews fall five years after the second-cycle deadlines (2030 for the largest category). Systems that cross a population category boundary through growth or acquisition are confirmed with EPA before the next cycle.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id` and by PWSID, so the company can respond quickly to an EPA information request, a primacy agency inspection or sanitary survey, a public utility commission inquiry, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- EPA portal receipts for every RRA and ERP certification, by PWSID, and the certification calendar;
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and notification matrix;
- public notice files, primacy agency consultation logs, and 141.31(d) certifications (kept 3 years, 141.33(e));
- RMP submissions and release reporting procedures;
- RRAs and ERPs themselves stay in the restricted repository (5-year retention, 300i-2(d)); they are shown on request but not copied into the binder, and no state or local agency can require them solely because of the EPA certification (300i-2(a)(5)).

## 8. Approval
Approved by the Senior Vice President, Water Quality and Environmental Compliance and the CISO on 2026-08-21. The roadmap was reviewed by the safety, environmental, and risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.

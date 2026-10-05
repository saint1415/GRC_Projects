# Regulatory Gap Analysis: Cris Santos Company | Chemical | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded specialty chemical formulator and packager; 14 plants in eight states) |
| Tier / Vertical | Enterprise / Chemical (NAICS 325998) |
| Regulations analyzed | USCG MTSA cybersecurity rule, 33 CFR Part 101 Subpart F (binding at PLT-01); EPA RMP, 40 CFR Part 68 (binding at 8 plants, control-system-dependent elements); OSHA PSM, 29 CFR 1910.119 (binding at 3 plants, same elements); CERCLA and EPCRA release reporting; DOT hazmat security plans, 49 CFR 172.800-172.804; SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach and data security laws (Florida worked example); CFATS RBPS 8 and CISA's RBPS 8 measures (voluntary enterprise benchmark); CIRCIA (proposed, tracked) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14); rows that depend on P07 testing updated 2026-08-28 |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Vice President, Process Safety and EHS; sampling reperformed by Internal Audit for 8 rows |
| Regulatory status checked | 2026-10-05: eCFR point-in-time 2026-09-23 for 33 CFR 101 Subpart F, 6.16-1, 105.105, 105.225, 154.100; 40 CFR 68, 302, 355; 29 CFR 1910.119; 49 CFR 172.704, 172.800-172.804; 17 CFR 229.106. Federal Register API for the MTSA rule, the RMP proposal, CFATS, and CIRCIA |
| Approved | Chief Compliance Officer and CISO, 2026-09-01; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability
Applicability was decided first, plant by plant, from each plant's chemicals, quantities, and waterfront status (`../00_company-facts.md` section 1 and the threshold math).

| Regulation | Applies? | Basis |
|---|---|---|
| USCG MTSA cybersecurity rule (C-CHEMICAL-R02) | **Yes, PLT-01 only** | The PLT-01 marine terminal transfers oil in bulk from tank barges of 250 barrels or more, so 33 CFR Part 154 applies (154.100(a)); a Part 154 facility must have a Part 105 Facility Security Plan (105.105(a)(1)); Subpart F applies to every facility required to have a Part 105 plan (101.605(a)). No size threshold. Training was due 2026-01-12; the Cybersecurity Assessment and Plan are due by 2027-07-16 (101.650(e)(1); 101.655). No other plant has a marine transfer |
| EPA RMP (40 CFR Part 68) | **Yes, 8 plants** | Program 3 at PLT-01, PLT-04, and PLT-05 because those processes are also covered by OSHA PSM (68.10(l)(2)); NAICS 325998 is not in the 68.10(l)(1) list. Program 2 at five plants holding 29% aqueous ammonia above the 20,000 lb TQ, where the worst-case release reaches public receptors (68.10(j)(2)). PLT-01 is a responding source (68.90(a)); the others are non-responding (68.90(b)) |
| OSHA PSM (29 CFR 1910.119) | **Yes, 3 plants** | Anhydrous ammonia (TQ 10,000 lb) and chlorine (TQ 1,500 lb) above threshold at PLT-01, PLT-04, and PLT-05. 50% hydrogen peroxide is below the 52% listing; atmospheric storage of isopropyl alcohol below its boiling point is excepted (1910.119(a)(1)(ii)(B)) |
| CERCLA and EPCRA release reporting | **Yes, all plants** | Ammonia RQ 100 lb, chlorine RQ 10 lb, sodium hypochlorite RQ 100 lb (40 CFR 302.4); ammonia and chlorine are EPCRA extremely hazardous substances |
| DOT hazmat security plan | **Yes, enterprise** | The company offers large bulk quantities (over 3,000 liters in one packaging) of Class 3 PG II solvent blends and 50% hydrogen peroxide, Division 5.1 PG II (172.800(b)(6) and (b)(10)) |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| State breach and data security laws | **Yes** | Employee personal information (12,000 employees and former employees) and SL-1 customer portal users; the law of each state where affected individuals reside, with Florida (Fla. Stat. 501.171) as the worked example |
| CFATS RBPS 8 (C-CHEMICAL-R01) | **Voluntary benchmark** | Nine plants filed Top-Screens for 50% hydrogen peroxide and six were tiered, including PLT-01. The statutory authority expired on July 28, 2023 (6 U.S.C. 621-629 shown as omitted); CISA states it cannot enforce CFATS. A Federal Register search on 2026-10-05 found no CFATS action. RBPS 8 is still the only chemical-sector federal cyber performance standard, so it is used as the benchmark for all 14 plants |
| CIRCIA (C-CHEMICAL-R03) | **Not in force** | Proposed 6 CFR Part 226 (89 FR 23644, 2024-04-04); no final rule as of 2026-10-05 (latest action: town hall notice, 2026-05-26). As proposed, the company would be covered by the size criterion (above the SBA standard of 650 employees) and by the MTSA facility criterion |
| SOX Section 404 | Separate program | IT general controls over the ERP and payroll are tested by the SOX program and not repeated here |
| FAR clauses; HIPAA | **No** | No federal prime or subcontracts; the employee health plan is a separate covered entity |

**Why RMP and PSM are in a cyber gap analysis.** Neither rule mentions cybersecurity. They are included because their process safety information, PHA, operating procedure, mechanical integrity, MOC, and emergency notification elements all depend on the control system working as designed. Treating a manipulated DCS as a failure of engineering controls under 68.67(c)(4) and 1910.119(e)(3) is an author interpretation, labeled as such in the rows.

## 2. Method
1. **Decompose.** Each binding rule was broken into citation-level duties from its own structure in the eCFR text (retrieved 2026-09-23 versions). For the MTSA rule, every measure in 101.650(a) to (i) is a separate row, plus the organizational, plan, drill, records, and communications duties in 101.620 to 101.655. RMP rows follow the Part 68 Program 3 sections; PSM rows follow the 1910.119 paragraphs. The CFATS benchmark uses the text of 6 CFR 27.230 and CISA's published RBPS 8 security measures (paraphrased).
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. All mappings are author mappings, because no official NIST mapping exists for these regulations; the `crosswalk_source` column says so.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and populations under 250 used 25 to 40 items; configuration and account data were checked in full with analytics. Selections were random. **26 rows were tested by sampling or full-population analytics; 14 found exceptions.** Two rows reuse the same sample as their RMP counterparts (G-066 with G-050, G-070 with G-055).
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| USCG MTSA cybersecurity rule, 33 CFR 101 Subpart F (binding, PLT-01) | 23 | 19 | 5 | 0 | 47 |
| EPA RMP, 40 CFR Part 68 (binding, 8 plants) | 9 | 8 | 0 | 0 | 17 |
| OSHA PSM, 29 CFR 1910.119 (binding, 3 plants) | 4 | 4 | 0 | 0 | 8 |
| CERCLA and EPCRA release reporting (binding) | 2 | 1 | 0 | 0 | 3 |
| DOT hazmat security plan (binding) | 5 | 3 | 0 | 0 | 8 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 4 | 0 | 0 | 0 | 4 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| CFATS RBPS text, 6 CFR 27 (voluntary benchmark) | 5 | 3 | 1 | 1 | 10 |
| CISA RBPS 8 security measures (voluntary benchmark) | 4 | 10 | 0 | 0 | 14 |
| CIRCIA (proposed) | 0 | 0 | 0 | 1 | 1 |
| **Total** | **60** | **51** | **6** | **2** | **119** |

**Gap risk levels across all regulations (57 gaps):** High 20, Moderate 28, Low 9.

**Reading the results.** The traditional process safety programs are sound: no RMP or PSM row is Not met, and proof testing, compliance audits, incident investigation, and responder coordination are all Met. The gaps sit where process safety depends on the control system: PHAs that do not consider a manipulated DCS, operating procedures that assume the HMI can be trusted, alarm limits that drift from the process safety information, and control changes outside MOC. Five of the six Not met rows are MTSA measures at PLT-01 (KEVs, default passwords, shared integrator credentials, removable media, and the Cybersecurity Assessment, which is not yet due). The sixth is the acquired plants against the RBPS 8 benchmark.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-017 | 33 CFR 101.650(a)(2) | Default passwords on 3 PLT-01 OT interfaces | Change and sweep all devices (POAM-013) | PLT-01 Controls Engineering Manager | 2026-09-30 |
| G-007 | 33 CFR 101.650(e)(3)(i); 101.625(d)(15) | 37 KEVs on critical OT without patch or documented compensating controls | Compensating controls for every open KEV; 7-day triage (POAM-002) | PLT-01 CySO | 2026-10-31 |
| G-021 | 33 CFR 101.650(a)(6) | 3 shared integrator accounts on the gateway | Named accounts (POAM-005) | Director of OT Security | 2026-10-31 |
| G-084, G-085 | Form 8-K Item 1.05 | Materiality process does not cover OT incidents and does not start from an OT event | OT factors, operations members, tabletop 2026-11-12 (POAM-004) | General Counsel | 2026-11-30 |
| G-045 | 33 CFR 101.650(h)(2) | Terminal network not monitored; no detections for alarm limit or SIS keyswitch changes | POAM-011; POAM-022 | Director of Security Operations | 2026-11-30 |
| G-053, G-068 | 40 CFR 68.69(a)(1)(iv); 29 CFR 1910.119(f)(1)(iv) | No procedure for running or shutting down a unit when the DCS cannot be trusted | Untrusted-DCS safe-state procedures (POAM-025) | PLT-01 Plant Manager | 2026-12-31 |
| G-061, G-074 | 40 CFR 68.90(b)(3); 355.40(a) | Emergency notification depends on business-network VoIP at 9 plants | Notification kits and quarterly tests (POAM-017) | Vice President, Process Safety and EHS | 2026-12-31 |
| G-097 | 6 CFR 27.230(a)(8) (benchmark) | Unmanaged integrator remote access at 3 acquired plants | Supervised call-in only; extend the gateway (POAM-014) | Director of OT Security | 2026-12-31 |
| G-043, G-113 | 33 CFR 101.650(g)(4); CISA RBPS 8 measure | OT backups not restore-tested for 2 of 3 PLT-01 DCS areas | Restore tests (POAM-003) | PLT-01 Controls Engineering Manager | 2027-02-28 |
| G-055, G-070, G-100 | 40 CFR 68.75; 29 CFR 1910.119(l); CISA RBPS 8 measure | 7 of 40 sampled DCS changes without MOC | Change log reconciliation; automated comparison (POAM-001) | Vice President, Process Safety and EHS | 2027-03-31 |
| G-051, G-067 | 40 CFR 68.67(c)(3)-(4); 29 CFR 1910.119(e)(3) | Cyber-initiated failures of controls not analyzed in 3 of 4 Program 3 PHAs | Add P01 ER-01 scenarios to PHA revalidations (POAM-024) | Vice President, Process Safety and EHS | 2027-03-31 |
| G-098 | 6 CFR 27.230(a)(8) (benchmark) | Acquired plants lack segmentation, named accounts, and vault backups | POAM-015 | Vice President, Integration Management Office | 2027-06-30 |
| G-110 | CISA RBPS 8 measure (lifecycle) | KEV backlog and unsupported operator stations | POAM-002; POAM-020 | Director of OT Security | 2027-06-30 |

The full list, with evidence and sampling, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Default passwords changed (POAM-013); KEV compensating controls (POAM-002); named integrator accounts (POAM-005); OT detections (POAM-022); disclosure committee OT tabletop, which is also the 2026 MTSA exercise (POAM-004); notification kits (POAM-017); contractor training (POAM-007); EWS device control (POAM-021); firewall rule cleanup (POAM-012); untrusted-DCS procedures (POAM-025); DOT security plan review adds the TMS (POAM-018); acquired plant remote tools disabled (POAM-014) | MTSA 101.650(a), (e)(3), (h), (i), 101.635(c); SEC Item 1.05; RMP 68.69, 68.90(b)(3); PSM (f); EPCRA 355.40; DOT 172.802(a) | Password sweep report; KEV register with compensating controls; tabletop report; kit test records; training records |
| 2027 Q1 | MTSA Cybersecurity Assessment (by 2027-01-31) and Cybersecurity Plan submitted to the COTP (by 2027-03-31) (POAM-008); approved list and network map (POAM-006); OT penetration test; restore tests for the Chlor Unit and blend halls (POAM-003); automated SIS comparison (POAM-009); PHA cyber scenarios (POAM-024); MOC reconciliation and configuration comparison (POAM-001); supplier contract amendments (POAM-010) | MTSA 101.630, 101.650(b), (e)(1)-(2), (f)(2), (g)(4), 101.655; RMP 68.67, 68.75; PSM (e), (l) | Assessment report (SSI); plan submission receipt; restore test reports; PHA revalidation records |
| 2027 Q2 | STAA before the 2027-05-10 compliance date; acquired plant OT DMZs, named accounts, and vault onboarding (POAM-015); monitoring extension (POAM-011); Blend Hall 1 console upgrade (POAM-020) | RMP 68.67(c)(9); RBPS 8 benchmark | STAA reports; integration records; coverage report |
| 2027 Q3 | Respond to COTP questions; first annual Cybersecurity Plan audit planned for one year after approval; annual risk analysis and gap reassessment | All | Updated P01 and P03 |

## 6. Pending regulatory changes
None of these is treated as a current obligation.
- **EPA RMP proposal (91 FR 8970, 2026-02-24; comment period extended to 2026-05-11 by 91 FR 16621).** The proposal would revise parts of the 2024 amendments, including safer technology and alternatives analyses, third-party audits, employee participation, community and emergency responder notification, natural hazards, power loss, and emergency response exercises. Every RMP row carries a note. Until a final rule is published, the current Part 68 text governs, including the 2027-05-10 compliance date in 68.10(g).
- **CFATS reauthorization.** If Congress reauthorizes CFATS, RBPS 8 becomes enforceable again for tiered facilities. The benchmark rows here would become the starting point for Site Security Plan updates at the six formerly tiered plants.
- **CIRCIA final rule.** The proposed rule would require covered cyber incident reports within 72 hours and ransom payment reports within 24 hours. No final rule has been published. P08 already targets voluntary reporting to CISA within 24 hours.
- **MTSA cybersecurity rule.** No amendment or delay was found in the Federal Register as of 2026-10-05; the eCFR text dated 2026-09-23 governs.
- **NIST SP 800-82 Rev. 4** is an initial public draft (2026-09-21). The OT standards stay on Rev. 3 until Rev. 4 is final.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a Coast Guard inspection or COTP plan review, an EPA RMP inspection or OSHA PSM inspection, a PHMSA security plan review, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- MTSA records under 33 CFR 105.225 (training, drills, exercises, incidents, audits), kept by the FSO as SSI where required;
- PHA, MOC, proof-test, compliance audit, and incident investigation records from the process safety system;
- the DOT security plan with its annual review record;
- release notification logs and exercise reports.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-09-01, with the Vice President, Process Safety and EHS concurring on the RMP, PSM, and release reporting rows. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, timed to feed the first annual Cybersecurity Assessment update.

# Regulatory Gap Analysis: Cris Santos Company | Food and Agriculture | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded further processor of meat products: 8 plants, 4 distribution centers; FL, GA, AL, NC, TN, TX) |
| Tier / Vertical | Enterprise / Food and Agriculture (NAICS 311612) |
| Primary regulation | FSMA Intentional Adulteration rule, 21 CFR Part 121 (C-FOOD-AG-R01), applicable at PLT-07; text read from eCFR (point-in-time 2026-09-23) |
| Other regulations analyzed | FSIS Sanitation SOP, HACCP, and recall rules where they touch electronic records, monitoring, and notification (9 CFR 416.16, 417, 418) at all 8 plants; FDA preventive controls record rules at PLT-07 (21 CFR 117.305, 117.315(c)); FDA registration renewal (21 CFR 1.230(b)); Reportable Food Registry (21 U.S.C. 350f); SEC Form 8-K Item 1.05 and Regulation S-K Item 106; hazardous substance release reporting (40 CFR 302.6; 355.40-355.42); state breach and data security laws (Florida worked example) |
| OT control benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (voluntary) |
| Assessment dates | 2026-06-01 to 2026-07-31 (plant walkthroughs 2026-06-15 to 2026-07-10; evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and corporate FSQA; sampling reperformed by Internal Audit for 8 rows |
| Approved | Chief Compliance Officer, SVP FSQA, and CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability

### 1.1 Which rules bind this company at this size
| Regulation | Applies? | Basis |
|---|---|---|
| FSMA Intentional Adulteration rule, 21 CFR Part 121 (C-FOOD-AG-R01) | **Yes, at PLT-07 only** | Part 121 applies to facilities required to register under FD&C Act section 415 (121.1). FDA's registration rule exempts "Facilities that are regulated exclusively, throughout the entire facility, by the U.S. Department of Agriculture under the Federal Meat Inspection Act" (21 CFR 1.226(g)). Seven plants make only FSIS-inspected meat products and are exempt. PLT-07 also makes FDA-regulated plant-based products, so it registered in 2022 and is covered. The company is neither a very small business (121.5(a)) nor a small business (121.3: fewer than 500 full-time equivalent employees, including subsidiaries and affiliates). Facilities other than small and very small businesses had 3 years after the July 26, 2016 effective date to comply (81 FR 34166), a period that ended before PLT-07's plant-based room opened, so the rule applied in full from its first day |
| FSIS Sanitation SOPs, HACCP, recalls (9 CFR 416, 417, 418) | **Yes, at all 8 plants** | Official establishments under the Federal Meat Inspection Act. Only provisions that depend on electronic systems, monitoring, or notification are analyzed |
| FDA preventive controls (21 CFR Part 117) | **Yes, at PLT-07** | Registered facility. The FSQA program owns Part 117; only the record requirements that depend on electronic systems (117.305(c), (d), (f); 117.315(c)) are analyzed here |
| FDA registration renewal (21 CFR 1.230(b)) | **Yes, at PLT-07** | Renewal window 2026-10-01 to 2026-12-31 |
| Reportable Food Registry (21 U.S.C. 350f) | **Yes, at PLT-07** | Applies to the registrant for FDA-regulated food; FSIS products follow 9 CFR 418.2 instead |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant (large accelerated filer) |
| Hazardous substance release reporting (40 CFR 302.6; 355.40-355.42) | **Yes, at 12 sites** | Each ammonia system holds well above ammonia's 100 lb reportable quantity (40 CFR 302.4). Included because a cyber-caused refrigeration upset could cause a reportable release |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside (employees in 6 states; online customers nationwide); Florida (Fla. Stat. 501.171) is the worked example |
| CIRCIA (C-FOOD-AG-R02) | **Not in force** | Proposed rule only (final rule not published as of 2026-10-04). As proposed (226.2(a)), the company would be covered because it exceeds the SBA size standard for NAICS 311612 (1,000 employees) |
| USCG MTS cyber rule (C-FOOD-AG-R03) | **No** | No MTSA-regulated facility (33 CFR 101.605) |
| OSHA PSM (29 CFR 1910.119) and EPA RMP (40 CFR Part 68) | Separate program | Each ammonia system exceeds the 10,000 lb threshold quantity in both rules; owned by the Director of Refrigeration and Process Safety and not restated here |
| SOX Section 404 | Separate program | IT general controls over ERP and payroll are tested by the SOX program |
| PCI DSS | Contractual | Hosted payment page and vendor-managed terminals; not analyzed |

### 1.2 Part 121 scope at PLT-07
- **In scope:** every point, step, and procedure of the plant-based process (receiving, liquid ingredient tanks, blending, forming, cooking, packaging) and **every shared system that can reach that food**: the central MES that releases formulations and setpoint ranges, the plant SCADA and HMIs that run the blending and dosing equipment, the shared CIP system, and the ammonia refrigeration.
- **Voluntarily in scope:** the other 7 plants run functional food defense plans using the same method. FSIS describes these as voluntary for FSIS-regulated establishments, and no food defense plan requirement appears in 9 CFR Parts 416-418. That work is **not** scored as Part 121 compliance here.
- **Open question for counsel:** whether FDA expects PLT-07's vulnerability assessment to cover its FSIS-inspected meat lines. The text requires an assessment "for each type of food manufactured, processed, packed, or held at your facility" (121.130(a)) and was not found to address mixed-jurisdiction facilities. PLT-07 covers both, so the answer changes documentation, not controls.

### 1.3 Part 121 is not an IT rule, but it reaches IT here
Part 121 regulates intentional adulteration intended to cause wide-scale public health harm and never mentions computers or control systems. It becomes a cyber-physical rule at PLT-07 because:
- **Attackers can reach the product through equipment.** A person who can change a blending setpoint or a formulation can adulterate food without touching it. Treating control-system access as "access to the product" under 121.130(a)(2)-(3) and (b) is an **author interpretation**, recorded as such in the CSV.
- **The 2026 MES migration was a significant change.** It moved formulation authority for PLT-07 to a cloud service shared with 6 other plants. That is a change in activities with "a reasonable potential to create a new vulnerability" that triggers reanalysis (121.157(b)(1)), which had to be completed before the change was operative or within 90 days after production began, unless a longer timeframe is justified (121.157(c)).
- **Records live in systems.** Monitoring and verification records must be accurate, indelible, legible, and created concurrently (121.305), which puts the records platform's integrity controls in scope.

## 2. Method
1. **Decompose.** Part 121 rows follow the rule's own structure at paragraph level: 121.1 and 121.4-121.5 (Subpart A), 121.126-121.157 (Subpart C), 121.305-121.325 (Subpart D). 121.401 (prohibited acts) is enforcement context, not a row. FSIS, FDA Part 117, SEC, EPA, and state rows are limited to provisions that depend on electronic systems, monitoring, notification, or disclosure. Regulatory text was read on eCFR (2026-09-23 point-in-time) and the U.S. Code; the 2016 final rule's compliance dates were read on govinfo.gov.
2. **Crosswalk.** NIST has published no mapping for 21 CFR Part 121, Part 117, or 9 CFR Parts 416-418, so those rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. Benchmark rows use the official NIST CSF 2.0 to SP 800-53 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), showing a subset.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations), stratified by plant; smaller populations used 25 to 40 items; populations under 10 and configuration items were tested in full. Selections were random. **40 rows were tested by sampling or full-population review; 15 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| Part 121 Subpart A (121.1, 121.4, 121.5) | 6 | 2 | 0 | 4 | 12 |
| Part 121 Subpart C (121.126-121.157) | 21 | 11 | 3 | 2 | 37 |
| Part 121 Subpart D (121.305-121.325) | 11 | 0 | 0 | 2 | 13 |
| **Part 121 subtotal (PLT-07)** | **38** | **13** | **3** | **8** | **62** |
| FSIS Sanitation SOPs (9 CFR 416.16) | 2 | 1 | 0 | 0 | 3 |
| FSIS HACCP (9 CFR 417) | 7 | 5 | 0 | 0 | 12 |
| FSIS recalls (9 CFR 418) | 1 | 1 | 0 | 0 | 2 |
| FDA preventive controls records (21 CFR 117) | 4 | 0 | 0 | 0 | 4 |
| FDA registration renewal (21 CFR 1.230(b)) | 1 | 0 | 0 | 0 | 1 |
| Reportable Food Registry (21 U.S.C. 350f) | 1 | 0 | 0 | 0 | 1 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 4 | 1 | 0 | 0 | 5 |
| Release reporting (40 CFR 302.6; 355.40-355.42) | 0 | 2 | 0 | 0 | 2 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| CIRCIA (proposed) and USCG MTS rule | 0 | 0 | 0 | 2 | 2 |
| NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary) | 1 | 11 | 0 | 0 | 12 |
| **Total** | **63** | **37** | **3** | **10** | **113** |

**Gap risk levels across all 40 open rows:** High 18, Moderate 18, Low 4. For Part 121 alone, the 16 open rows are High 8, Moderate 6, Low 2.

**The pattern.** PLT-07's food defense program is mature in its management components: monitoring, corrective actions, verification, records, and training are documented and sampled clean except for agency worker training records. The weakness is narrow and serious: **the vulnerability assessment and mitigation strategies still describe the plant as it was before the central MES migration.** All 3 Not met rows (121.157(b)(1), (c), (d)) and 5 of the 8 High Part 121 gaps come from that one missed reanalysis trigger. Across the FSIS plants, the gaps are in electronic record integrity at 3 plants (417.5(d)), reassessment after system changes (417.4(a)(3)), and the untested manual fallback for cold storage monitoring (417.2(c)(4)).

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-014 | 21 CFR 121.126(b)(1) | Central MES release path and supervisor HMI overrides not assessed | Reanalysis (POAM-006) | PLT-07 FSQA Manager | 2026-12-31 |
| G-015 | 21 CFR 121.126(b)(2) | No mitigation strategy for setpoint overrides at the blending step | Second-badge override and alerts (POAM-005) | SVP FSQA | 2027-03-31 |
| G-020 | 21 CFR 121.130(a) | Automated steps evaluated as before the MES migration | Reassess every automated step (POAM-006) | PLT-07 FSQA Manager | 2026-12-31 |
| G-022 | 21 CFR 121.130(a)(2) | Logical access paths changed in 2026 | Include MES, HMI, and remote access in the access rating (POAM-006) | PLT-07 FSQA Manager | 2026-12-31 |
| G-024 | 21 CFR 121.130(b) | Supervisor-level insider at the HMI not considered | Insider scenarios from P01 R-003 (POAM-006) | PLT-07 FSQA Manager | 2026-12-31 |
| G-026 | 21 CFR 121.135(a) | Setpoint overrides need no second approval | Second-badge override and alerts (POAM-005) | SVP FSQA | 2027-03-31 |
| G-044 | 21 CFR 121.157(b)(1) | No reanalysis after a significant change | Reanalysis now; food defense check in MES and OT change control (POAM-006) | PLT-07 FSQA Manager | 2026-12-31 |
| G-048 | 21 CFR 121.157(c) | Reanalysis not completed within the required timeframe | Complete by 2026-12-31 with a documented timeframe (POAM-006) | PLT-07 FSQA Manager | 2026-12-31 |
| G-066 | 9 CFR 417.2(c)(4) | Manual fallback for cold storage monitoring not exercised at 9 sites | Exercise at every site (POAM-008) | Vice President, Distribution and Transportation | 2027-03-31 |
| G-071 | 9 CFR 417.4(a)(3) | Changes in processing systems not always reassessed (PLT-03 inspection staffing; 5 of 40 OT changes) | Reassess PLT-03 now; FSQA gate in change control and AI intake (POAM-017, POAM-021) | SVP FSQA | 2026-12-31 |
| G-075 | 9 CFR 417.5(d) | Integrity of electronic CCP data not assured at 3 plants | Historian audit trails; PLT-08 migration (POAM-007) | Vice President, Engineering | 2026-12-31 |
| G-086 | Form 8-K Item 1.05 | Process untested for a production halt with product holds | Playbook update; tabletop 2026-11-18 (POAM-014) | General Counsel | 2026-11-30 |
| G-087 | Form 8-K Item 1.05 (materiality determination) | Quantitative factors incomplete for a food company | P05 values and recall cost method in the worksheet (POAM-014) | General Counsel | 2026-11-30 |
| G-104 | CSF 2.0 PR.IR-01 | PLT-05 and PLT-08 lack an OT DMZ | POAM-001; POAM-003 | Director of Network Engineering | 2027-03-31 |
| G-105 | CSF 2.0 PR.AA-03 | PLT-08 integrator VPN without MFA; PLT-05 modem | POAM-002; POAM-003 | Director of OT Security | 2027-03-31 |
| G-106 | CSF 2.0 PR.AA-05 | HMI setpoint overrides without a second approval | POAM-005 | SVP FSQA | 2027-03-31 |
| G-108 | CSF 2.0 PR.PS-02 | 118 HMIs and 9 engineering workstations unsupported | POAM-004 | Director of OT Security | 2027-12-31 |
| G-112 | CSF 2.0 GV.SC-07 | 71% of tier-1 OT vendors reviewed; cold-chain vendor concentration without a contracted RTO | POAM-008; POAM-015 | Director of Third-Party Risk Management | 2027-03-31 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | PLT-07 food defense reanalysis (start 2026-10-05, complete by 2026-12-31; POAM-006); agency worker training gate at PLT-07 (POAM-016); FDA registration renewal; PLT-03 HACCP reassessment and restored inspection staffing (POAM-021); historian audit trails at PLT-02 and PLT-05 (POAM-007); disclosure tabletop 2026-11-18 and playbook update (POAM-014); credential sweep (POAM-012); PLT-05 modem disconnected except supervised sessions (POAM-003 interim) | 121.4(b)(2), 121.130, 121.157; 1.230(b); 417.4(a)(3); 417.5(d); Form 8-K Item 1.05 | Signed reanalysis and plan revision; training records; reassessment record; audit trail configuration; tabletop report |
| 2027 Q1 | HMI second-badge overrides and alerts (POAM-005); PLT-08 integration and records migration (POAM-001, POAM-002, POAM-007); PLT-05 OT DMZ and gateway (POAM-003); manual cold storage log exercised at all 12 sites (POAM-008); MES RTO retest (POAM-010); cold-chain contract RTO; Internal Audit test of Item 106 statements | 121.135(a); 416.16(b); 417.2(c)(4); 417.5(b), (d); 418.2; Item 106; CSF PR.IR-01, PR.AA-03, PR.AA-05 | Configuration evidence; exercise records; DR test report; amended contracts |
| 2027 Q2 to Q4 | Unsupported HMI and workstation replacement (POAM-004, through 2027-12); OT monitoring at all plants (POAM-011); vendor review backlog (POAM-015) | CSF PR.PS-02, DE.CM-09, GV.SC-07 | Replacement records; monitoring coverage; vendor reviews |
| 2027 Q3 | Annual risk analysis and gap reassessment; check CIRCIA status | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **Part 121:** no proposed amendments were found. The most recent Federal Register document affecting Part 121 is a 2022-03-14 notice of availability of an FDA enforcement policy guidance on certain provisions of several FSMA rules (87 FR 14169); its content was not reviewed for this analysis.
- **CIRCIA:** the final rule had not been published as of 2026-10-04. If the final rule keeps the NPRM's size-based criterion, the company will be covered, and P08 must add a 72-hour covered incident report and a 24-hour ransom payment report to CISA. Reporting is voluntary until the final rule takes effect.
- **FSMA 204 traceability rule** (21 CFR Part 1, Subpart S): FDA proposed extending the compliance date (FR Doc. 2025-14967, 90 FR 38084); no final rule on the extension was found. The FSQA program confirmed that none of PLT-07's products is on the Food Traceability List, so the rule is not analyzed here.
- **SEC:** no SEC proposal to amend or rescind Item 1.05 or Item 106 was found as of 2026-10-04, so both remain in force.

None of these is treated as a current obligation.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to an FDA inspection at PLT-07, FSIS record review at any plant, an EPA or state inquiry after a release, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the PLT-07 food defense plan, vulnerability assessment, reanalysis records, and signed revisions (classified Restricted under POL-04 and released only to FDA on request, 121.320);
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- plant HACCP and SSOP record integrity documentation (417.5(d); 416.16(b));
- mock recall reports and the traceability export procedure;
- document retention of at least 3 years (POL-04).

## 8. Approval
Approved by the Chief Compliance Officer, the SVP FSQA, and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, or sooner after the PLT-07 reanalysis or a CIRCIA final rule.

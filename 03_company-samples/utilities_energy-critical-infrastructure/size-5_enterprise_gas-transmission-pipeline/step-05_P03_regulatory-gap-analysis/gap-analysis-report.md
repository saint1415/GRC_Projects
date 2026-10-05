# Regulatory Gap Analysis: Cris Santos Company | Energy | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded interstate natural gas transmission company: PS-1, PS-2, PS-3, and operated JV-1 to JV-3; 9 states) |
| Tier / Vertical | Enterprise / Energy (natural gas pipeline) |
| Primary regulation | TSA Security Directive Pipeline-2021-02G (C-ENERGY-R03), effective 2026-05-03 to 2027-05-02, analyzed requirement by requirement |
| Also analyzed | TSA SD Pipeline-2021-01G (C-ENERGY-R02); PHMSA control room management, 49 CFR 192.631 (C-ENERGY-R04); Sensitive Security Information, 49 CFR Part 1520; FERC CEII (18 CFR 388.113) and Form No. 567 (18 CFR 260.8); SEC Form 8-K Item 1.05 and Regulation S-K Item 106; state breach and data security laws (Florida worked example); applicability checks for NERC CIP (C-ENERGY-R01) and CIRCIA (C-ENERGY-R05) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Vice President, Pipeline Safety and Compliance; sampling for 12 rows reperformed by Internal Audit |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |
| Handling | The working papers behind the SD rows are SSI (49 CFR 1520.5(b)(5)) and are kept in the SSI library. This sample contains no SSI |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| TSA SD Pipeline-2021-02G (C-ENERGY-R03) | **Yes, in full** | TSA notified PS-1, PS-2, and JV-1 before July 26, 2022, that they are critical (SD 02G Section II.A.1). PS-3 was designated under its prior owner; the change of ownership was handled by a plan amendment (Section VI.A), approved 2025-09-12. The SD has no size threshold; it applies only by TSA notification. The company has Critical Cyber Systems, so the 60-day "no Critical Cyber Systems" notice in Section II.A.5 does not apply |
| TSA SD Pipeline-2021-01G (C-ENERGY-R02) | **Yes** | Same TSA designation (effective 2026-01-16 to 2027-01-15) |
| 49 CFR 192.631 (C-ENERGY-R04) | **Yes, all paragraphs** | Controllers monitor and control the pipelines through SCADA from three control rooms. The reduced-procedure exception in 192.631(a)(1) covers only distribution with fewer than 250,000 services or transmission without a compressor station; the company has 96 compressor stations. PHMSA enforces directly because the pipelines are interstate. This analysis covers the SCADA-relevant paragraphs; fatigue mitigation (192.631(d)) is tested by the PHMSA compliance program and is outside this cyber scope |
| 49 CFR Part 1520 (SSI) | **Yes** | The company prepares vulnerability assessments and plans provided to TSA (1520.5(b)(5); covered person under 1520.7(k) and (l)). SD 02G Section IV.B requires plans and assessment results to be handled under Part 1520 |
| FERC CEII and Form No. 567 | **Yes** | Each pipeline subsidiary is a major natural gas pipeline company with system delivery capacity above 100,000 Mcf per day (18 CFR 260.8(a)) and requests CEII treatment for engineering filings (18 CFR 388.113(d)) |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| State breach and data security laws | **Yes** | Employees live in all 9 operating states. The law of each state where affected individuals reside applies; Florida (Fla. Stat. 501.171) is the worked example |
| NERC CIP (C-ENERGY-R01) | **No** | Not a NERC-registered entity; owns no Bulk Electric System assets. Electric-driven compressor stations are customers of electric utilities |
| DOE Form DOE-417 | **No** | Electric industry reporting; the company has no electric operations |
| CIRCIA (C-ENERGY-R05) | **Not in force** | Final rule not published as of 2026-09-25. If finalized as proposed, the company would be covered (above the SBA size standard of $41.5 million for NAICS 486210) |
| SOX Section 404 | Separate program | IT general controls over ERP and payroll (SYS-11) are tested by the SOX program and not repeated here |
| HIPAA, PCI DSS | **No** | Not a covered entity (the employee health plan is administered separately); shippers pay by wire or ACH |

## 2. Method
1. **Decompose.** SD 02G and SD 01G were broken into lettered and numbered measures from the directive texts as issued (SD 02G dated 2026-05-01; SD 01G effective 2026-01-16). Where a parent measure has sub-measures, both are rated: the parent row summarizes the sub-measure gaps so a TSA inspector can read either level. 49 CFR 192.631, Part 1520, 18 CFR 388.113 and 260.8, and 17 CFR 229.106 were decomposed from the eCFR text; Item 1.05 from the Form 8-K instructions and SEC Release 33-11216; Florida from the statute text.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. There is no official NIST mapping for the security directives, 192.631, or the other rules, so every mapping is an **author mapping** and is labeled that way in `crosswalk_source`.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); populations under 250 and lower-risk controls used 25 to 40 items; configuration, account, and log-source data were checked in full with analytics. Selections were random; the field-device trace was stratified so PS-3 got 20 of 60 items. **39 rows were tested by sampling or full-population analytics; 19 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and has an owner and a date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| SD 02G Section II (applicability, plan) | 3 | 2 | 0 | 0 | 5 |
| SD 02G Section III (cybersecurity measures A to G) | 28 | 25 | 0 | 0 | 53 |
| SD 02G Section IV (records) | 1 | 2 | 0 | 0 | 3 |
| SD 02G Section V (procedures) | 2 | 0 | 0 | 0 | 2 |
| SD 02G Section VI (plan amendments) | 1 | 1 | 0 | 0 | 2 |
| TSA SD Pipeline-2021-01G | 10 | 2 | 0 | 1 | 13 |
| PHMSA 49 CFR 192.631 | 28 | 6 | 0 | 0 | 34 |
| SSI, 49 CFR Part 1520 | 6 | 1 | 0 | 0 | 7 |
| FERC CEII and Form No. 567 | 3 | 0 | 0 | 0 | 3 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| NERC CIP and CIRCIA (applicability rows) | 0 | 0 | 0 | 2 | 2 |
| **Total** | **91** | **42** | **0** | **3** | **136** |

**SD 02G (primary regulation):** 35 Met and 30 Partially met of 65 rows. No measure is wholly Not met. The partial rows concentrate in three places: the PS-3 acquisition (segmentation, encryption, console compensating controls, backups, exercises), the 22 legacy and unmonitored compressor stations (monitoring, logging, allowlisting, patching), and third parties (vendor modems, authorized representative attestations).

**Gap risk levels across all regulations:** High 15, Moderate 23, Low 4.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-005 | SD 02G II.B.2 | Plan milestones for 7 legacy station mitigations missed (2026-06-30) | Complete the mitigations and inform TSA of the revised date (POAM-003) | Director of Compression Engineering | 2026-12-31 |
| G-007 | SD 02G III.B | 12 of 20 PS-3 stations have flat networks | PS-3 segmentation (POAM-016) | Vice President, Integration Management Office | 2027-03-31 |
| G-009 | SD 02G III.B.1.b | 7 always-on vendor modems outside the OT remote access gateway | Remove the modems (POAM-004) | Director of OT Security | 2026-12-15 |
| G-011 | SD 02G III.B.2.a | No conduit firewalls on PS-3 flat station networks | POAM-016 | Vice President, Integration Management Office | 2027-03-31 |
| G-012 | SD 02G III.B.2.b | PS-3 polling crosses the shared corporate MPLS unencrypted | IPsec tunnels (POAM-016) | Director of Network Engineering | 2027-03-31 |
| G-020 | SD 02G III.C.4.b | 4 of 25 sampled departures did not trigger a shared password change | Automated change ticket; quarterly reconciliation (POAM-001) | Director of Compression Engineering | 2026-11-30 |
| G-022 | SD 02G III.D | No OT monitoring at 22 stations or at meter and valve sites | OT monitoring sensors (POAM-005) | Director of Security Operations | 2027-03-31 |
| G-029 | SD 02G III.D.2.b | No communications baseline monitoring at the same 22 stations | POAM-005 | Director of Security Operations | 2027-03-31 |
| G-034 | SD 02G III.D.4 | IT/OT isolation not exercised at GCC-2 or PS3-CR | Isolation exercises (POAM-012) | Director of OT Security | 2027-03-31 |
| G-035 | SD 02G III.E | Patch strategy gaps (see G-036 and G-039) | POAM-002; POAM-003 | Director of SCADA Engineering | 2027-01-31 |
| G-036 | SD 02G III.E.1 | 9% of applicable Known Exploited Vulnerabilities items past the plan timeline; 5 of 60 sampled patch items late | POAM-002 | Director of SCADA Engineering | 2027-01-31 |
| G-039 | SD 02G III.E.3 | No documented mitigations for 7 of 22 legacy stations that cannot be patched | POAM-003 | Director of Compression Engineering | 2026-12-31 |
| G-047 | SD 02G III.F.1.d | Isolation capability untested at GCC-2 and PS3-CR | POAM-012 | Director of OT Security | 2027-03-31 |
| G-123 | Form 8-K Item 1.05 | Materiality playbook lacks curtailment and shutdown factors; no OT shutdown exercise | Update playbook; tabletop 2026-11-12 (POAM-013) | General Counsel | 2026-11-30 |
| G-124 | Form 8-K Item 1.05 (materiality determination) | Escalation timelines never tested with an operational shutdown | POAM-013 | General Counsel | 2026-11-30 |

**Moderate and Low gaps not in the POA&M** have owners and dates in the CSV and are tracked in the compliance tracker: G-003 (authorized representative attestations, R-054), G-071 and G-075 (SD 01G coordinator update and report supplements), G-094 (PS-3 alarm set-point verification), G-111 (PS-3 records, R-056), and G-133 (payroll SaaS breach notice term, R-019).

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | PS-3 alarm set-point verification (G-094, by 2026-10-31); shared password change automation (POAM-001); vendor modem removal (POAM-004); disclosure committee tabletop and playbook update (POAM-013); TSA plan amendment requests (POAM-022); legacy station mitigations at 7 stations and revised date to TSA (POAM-003); SSI marking control (POAM-010); transfer trigger (POAM-008); point-to-point workflow block (POAM-009); memory capture step (POAM-024); leak model change control (POAM-019) | SD 02G II.B.2, III.B.1.b, III.C.3, III.C.4.b, III.E.3, III.F.1.b.iii, IV.B, VI.B; 192.631(c)(2), (e)(3), (f)(3); 1520.9(a)(4); Item 1.05 | Modem removal records; tabletop report; amendment filings; mitigation register; change workflow reports |
| 2026-11-14 | **Annual Cybersecurity Assessment Plan and annual report to TSA** (SD 02G III.G.3 and III.G.4), using P07 results | SD 02G III.G | Submission confirmation |
| 2027 Q1 | PS-3 segmentation and polling encryption (POAM-016 milestones); OT monitoring and log forwarding at the 22 stations (POAM-005, POAM-006); isolation exercises at GCC-2 and PS3-CR with PS-3 manual operation drill (POAM-012); KEV backlog cleared (POAM-002); PS-3 inventory walkdowns (POAM-015); PS-3 controller cyber AOC training (POAM-017); authorized representative attestations (G-003) | SD 02G III.A, III.B, III.D, III.E.1, III.F.1.d-e; 192.631(c)(3), (h)(1); SD 02G II.A.4 | Sensor coverage report; exercise after-action reports; patch reports; training records |
| 2027 Q2 | PS-3 cutover to the main SCADA platform and GCC-1 (POAM-016, 2027-06-30); first-phase station HMI and PLC replacement (POAM-003); supplier SBOM and incident notice terms (POAM-014); second PS-3 carrier (POAM-021); PS-3 records moved to the common repository (G-111) | SD 02G III.B, III.C.2, III.F.1.c; 192.631(j)(1) | Cutover report; plan amendment; contracts |
| 2027 Q2 to Q3 | Track renewal of SD 02G (expires 2027-05-02) and SD 01G (expires 2027-01-15); annual gap reassessment | All | Updated P03 |

## 6. Pending regulatory changes
- **TSA surface cyber rulemaking.** TSA's proposed rule *Enhancing Surface Cyber Risk Management* (89 FR 88488, 2024-11-07) would codify cyber risk management requirements for designated pipeline and rail owner/operators. No final rule was found in the Federal Register as of 2026-09-25, so the security directives remain the operative requirements. SD 02G rows carry this note in `pending_rule_change`.
- **Directive renewals.** SD 01G expires 2027-01-15 and SD 02G expires 2027-05-02. TSA has renewed both series each year; the 2026 renewal of SD 02G made no substantive changes. The Director of OT Security tracks each renewal and confirms receipt in writing (SD 02G Section V.A.1).
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting under SD 01G Section II.C continues; CIRCIA would add a separate report to CISA if finalized as proposed (72 hours for covered incidents, 24 hours for ransom payments). Not treated as a current obligation.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind it was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.

## 7. Regulator-ready package
The GRC team keeps an evidence binder, indexed by `req_id`, so the company can respond quickly to a TSA inspection or information request (SD 02G Section IV.C), a PHMSA control room management inspection (192.631(i) and (j)), a FERC data request, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row (SSI where they concern Critical Cyber Systems);
- the TSA-approved Cybersecurity Implementation Plan, the Cybersecurity Assessment Plan, and the plan index (SD 02G Section IV.A);
- the records TSA may inspect under Section IV.C.2: asset inventory, firewall rules, network and architecture diagrams, policies (P06), logs, and up to 24 hours of packet capture where sensors exist;
- the P01 risk register, P02 SSP, P05 BIA, P07 assessment and POA&M, and P08 runbook;
- control room management records (alarm reviews, point-to-point verifications, backup SCADA tests, training).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, or after the PS-3 cutover if earlier.

# Regulatory Gap Analysis: Cris Santos Company | Health Care | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-specialty medical group; FL, GA, AL, SC) |
| Tier / Vertical | Enterprise / Health Care and Social Assistance |
| Regulations analyzed | HIPAA Security Rule (all 69 crosswalk rows); HIPAA Breach Notification Rule; selected HIPAA Privacy Rule safeguards; SEC Form 8-K Item 1.05 and Reg S-K Item 106; CMS ASC emergency preparedness (42 CFR 416.54, cyber-relevant parts); Section 1557 (45 CFR 92.210); CLIA test report and retention rules; 42 CFR Part 2; FTC Health Breach Notification Rule; state breach and data security laws (Florida worked example) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer; sampling reperformed by Internal Audit for 10 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv), with counsel's review (EV-060). This section restates the results for the rules analyzed here.

| Regulation | Applies? | Basis |
|---|---|---|
| HIPAA Security Rule (N62-R01) | **Yes** | Health care provider that transmits health information electronically in standard transactions, so a covered entity (45 CFR 160.103). No size exemption; 164.306(b) affects how, not whether. Also a business associate for the 45 SL-1 client practices |
| HIPAA Breach Notification Rule (N62-R03) | **Yes** | Covered entity (164.404-164.408) and business associate (164.410) |
| HIPAA Privacy Rule (N62-R02) | **Yes** | Covered entity; only safeguard-related provisions are in scope here |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| 42 CFR 416.54 (N62-R08) | **Yes, for the 6 ASCs** | ASC condition for coverage. The clinics, imaging centers, and lab are not provider types covered by the CMS emergency preparedness rule; they follow the enterprise contingency program (EV-059) |
| 45 CFR 92.210 (N62-R07) | **Yes** | Receives federal financial assistance (Medicare, Medicaid) and operates a health program |
| CLIA (42 CFR Part 493) | **Yes, for the central lab** | CLIA-certified laboratory (EV-059). Only the test report (493.1291) and retention (493.1105) provisions that depend on the LIS are analyzed |
| 42 CFR Part 2 (N62-R05) | **Partly** | Not a Part 2 program; a lawful holder of records received from outside programs (2.16(a) applies; 2.16(b) does not) |
| FTC HBNR (N62-R06) | **No** | 16 CFR 318.1 excludes HIPAA covered entities and business associates acting as such |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example |
| HIPAA Security Rule NPRM (N62-R04) | **Not in force** | Proposed rule only; tracked in the `pending_rule_change` column |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25; reporting is voluntary |
| SOX Section 404 | Separate program | IT general controls over ERP and payroll (SYS-06) are tested by the SOX program and not repeated here |

HIPAA exclusions (Not applicable): 164.308(a)(4)(ii)(A), because the group performs no clearinghouse function; 164.314(a)(2)(ii), because there are no arrangements between governmental entities; and 164.314(b) with its four implementation specifications, because the employee health plan is a separate covered entity handled by the benefits program.

## 2. Method
1. **Decompose.** HIPAA Security Rule requirements and their Required and Addressable types come from NIST SP 800-66 Rev. 2 (all 69 rows in the Health Care crosswalk). Other regulations were broken into citation-level duties from the eCFR text (retrieved 2026-09-23 versions for 42 CFR 416.54, 42 CFR 493.1291 and 493.1105, 42 CFR 2.16, 45 CFR 92.210, 45 CFR 164.404, and 17 CFR 229.106), the SEC's compliance guide for Item 1.05, and the Florida statute text.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. HIPAA rows use the Health Care crosswalk (an author mapping, because NIST's official mapping is not yet published for CSF 2.0). Other rows are author mappings and are labeled that way.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and populations under 250 used 25 to 40 items; configuration and account data were checked in full with analytics. Selections were random. **40 rows were tested by sampling or full-population analytics; 16 found exceptions.** Current state was established from the intake evidence (exports, documents and records from the enterprise systems of record, EV-001 to EV-074), gap analysis interviews with control owners (EV-080), the samples, analytics and walk-throughs of 10 sites and the 6 ASCs (EV-081 to EV-086), the external TLS scan (EV-087), the AI inventory review (EV-088), and, where Internal Audit had already tested a control, its P07 results (for example EV-AC-2 and EV-IR-4). The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

**Addressable is not optional.** For each addressable specification, the group implements it, implements an equivalent, or documents why neither is reasonable and appropriate (164.306(d)(3)). All addressable gaps below are being implemented; none is documented as unreasonable.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| HIPAA Security Rule 164.308 | 14 | 15 | 0 | 1 | 30 |
| HIPAA Security Rule 164.310 | 9 | 3 | 0 | 0 | 12 |
| HIPAA Security Rule 164.312 | 5 | 7 | 0 | 0 | 12 |
| HIPAA Security Rule 164.314 | 2 | 2 | 0 | 6 | 10 |
| HIPAA Security Rule 164.316 | 5 | 0 | 0 | 0 | 5 |
| HIPAA Breach Notification Rule (N62-R03) | 9 | 2 | 0 | 0 | 11 |
| HIPAA Privacy Rule (N62-R02) | 1 | 1 | 0 | 0 | 2 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| CMS Emergency Preparedness, ASCs (N62-R08) | 6 | 3 | 0 | 0 | 9 |
| Section 1557 (N62-R07) | 0 | 3 | 0 | 0 | 3 |
| CLIA | 3 | 1 | 0 | 0 | 4 |
| 42 CFR Part 2 (N62-R05) | 0 | 1 | 0 | 1 | 2 |
| FTC Health Breach Notification Rule (N62-R06) | 0 | 0 | 0 | 1 | 1 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| **Total** | **63** | **41** | **0** | **9** | **113** |

**HIPAA Security Rule:** 35 Met, 27 Partially met, 0 Not met, 7 Not applicable (69 rows). Of the 27 partially met rows, 8 are standards, 8 are Required specifications, and 11 are Addressable specifications. No requirement is wholly Not met; the gaps are concentrated in the acquired practices, result integrity, medical devices, and third parties.

**Gap risk levels across all regulations:** High 15, Moderate 21, Low 5.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-005 | 164.308(a)(1)(ii)(D) | No information system activity review for two acquired-practice EHRs | SIEM collectors and interim weekly review (POAM-005) | Director of Security Operations | 2026-12-31 |
| G-007 | 164.308(a)(3) | Workforce security depends on manual processes at three acquired practices | Identity federation (POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| G-010 | 164.308(a)(3)(ii)(C) | 2 of 60 sampled terminations disabled 3 and 6 days late (both AQ) | Federation; interim daily reconciliation (POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| G-022 | 164.308(a)(7) | Contingency plan does not address loss of the primary clearinghouse | Add clearinghouse scenario; surge contract (POAM-019) | Vice President, Revenue Cycle | 2027-01-31 |
| G-024 | 164.308(a)(7)(ii)(B) | Clearinghouse concentration without recovery strategy; LIS RTO not demonstrated | Surge contract and fallback (POAM-019); LIS automation (POAM-011) | Vice President, Revenue Cycle | 2027-01-31 |
| G-026 | 164.308(a)(7)(ii)(D) | Fallback not tested; test results not fed back | Fallback test (POAM-019); plan update (POAM-011) | Vice President, Revenue Cycle | 2027-01-31 |
| G-038 | 164.310(d) | Inventory gaps | Discovery (POAM-010) | Director of Clinical Engineering | 2027-03-31 |
| G-048 | 164.312(b) | As 164.308(a)(1)(ii)(D) | POAM-005 | Director of Security Operations | 2026-12-31 |
| G-049 | 164.312(c) | Result integrity gaps | POAM-003; POAM-006 | Laboratory Director | 2027-03-31 |
| G-050 | 164.312(c)(2) | No mechanism to corroborate results were not altered after release | Reconciliation (POAM-006) | LIS Application Manager | 2027-03-31 |
| G-083 | Form 8-K Item 1.05; SEC Release 33-11216 | Process untested with current members; acquired entity reporting lines not in the playbook | Update playbook; tabletop 2026-11-12 (POAM-014) | General Counsel | 2026-11-30 |
| G-084 | Form 8-K Item 1.05 (materiality determination) | Escalation timelines never tested end to end | POAM-014 | General Counsel | 2026-11-30 |
| G-101 | 45 CFR 92.210(b) | Identification incomplete | Complete inventory including non-automated tools (POAM-020) | Chief Medical Information Officer | 2026-11-30 |
| G-102 | 45 CFR 92.210(c) | Mitigation not evidenced on local data | Local bias testing for AI-002 to AI-005 (POAM-020) | Chief Medical Information Officer | 2027-03-31 |
| G-103 | 42 CFR 493.1291(a) | Result integrity controls incomplete | POAM-003; POAM-006 | Laboratory Director | 2027-03-31 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Disclosure committee tabletop and playbook update (POAM-014); AQ termination reconciliation and first federation (POAM-001); SIEM collectors for AQ-08 and AQ-07 migration (POAM-005); lab change board and role split (POAM-003); inherited BAA review (POAM-022); AQ encryption (POAM-023); outreach portal account cleanup (POAM-002); 92.210 input inventory and council reviews (POAM-020); ASC downtime training (POAM-021) | SEC Item 1.05; HIPAA 164.308(a)(3), (a)(1)(ii)(D), (b)(1), 164.312(a)(2)(iv), (b), (c); CLIA 493.1291(a); 92.210(b); 416.54(d)(1) | Tabletop report; federation records; SIEM source list; change board minutes; signed BAAs |
| 2027 Q1 | Clearinghouse surge contract and fallback test (POAM-019); LIS DR retest (POAM-011); SD-WAN at AQ sites (POAM-016); LIS-to-EHR result reconciliation (POAM-006); device inventory 98% (POAM-010); local bias testing (POAM-020); ASC cyber exercise (POAM-021); Internal Audit test of Item 106 statements | HIPAA 164.308(a)(7); 164.310(d); 164.312(c); CLIA 493.1291(a); 92.210(c); 416.54(d)(2); Item 106 | Test reports; reconciliation reports; bias test results; exercise after-action report |
| 2027 Q2 | Unsupported analyzer workstations replaced (POAM-009); NAC at all sites (POAM-018); AQ-08 EHR migration (2027-04-30) | HIPAA 164.308(a)(1)(ii)(B); 164.308(a)(5)(ii)(B) | Replacement records; NAC coverage report |
| 2027 Q3 | Annual risk analysis and gap reassessment; review NPRM status | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. 35 HIPAA rows carry a note in `pending_rule_change`. If finalized as proposed, the verified proposals that matter most here are: removal of the addressable designation; encryption of all ePHI at rest and in transit with limited exceptions (AQ workstations and the lab MLLP segment); MFA; a written technology asset inventory and network map (medical devices); penetration testing at least every 12 months and vulnerability scanning; restoring certain systems within 72 hours (clearinghouse dependency and AQ EHRs); a compliance audit at least every 12 months; and business associate notice within 24 hours of activating a contingency plan. None of these is treated as a current obligation.
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the group can respond quickly to an OCR data request, a CMS or state survey of an ASC, a CLIA inspection, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- the latest breach log submissions and notification files;
- ASC emergency plans, training, and exercise records;
- 92.210 inventory and mitigation records (from P10);
- document retention of 6 years (164.316(b)(2)(i)).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.

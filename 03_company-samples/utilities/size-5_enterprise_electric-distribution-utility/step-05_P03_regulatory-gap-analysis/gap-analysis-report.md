# Regulatory Gap Analysis: Cris Santos Company | Utilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded investor-owned electric utility; NERC-registered DP, TO, and TOP; Florida and south Georgia) |
| Tier / Vertical | Enterprise / Utilities |
| Primary regulation | NERC CIP Reliability Standards under Federal Power Act section 215 (16 U.S.C. 824o): CIP-002-5.1a, CIP-003-9, CIP-004-7, CIP-005-7, CIP-006-6, CIP-007-6, CIP-008-6, CIP-009-6, CIP-010-4, CIP-011-3, CIP-012-2, CIP-013-2, CIP-014-3 |
| Also analyzed | NERC EOP-004-4 and Form DOE-417 (event and incident reporting); SEC Form 8-K Item 1.05 and Reg S-K Item 106; FTC Identity Theft Red Flags Rule (16 CFR 681.1) and Disposal Rule (16 CFR Part 682); state breach and data security laws (Florida worked example) |
| Versions checked | NERC CIP standards page (nerc.com), retrieved 2026-09-26: the versions above are "Mandatory Subject to Enforcement"; CIP-012-2 took effect 2026-07-01 and CIP-003-9 on 2026-04-01. DOE-417 instructions under OMB 1901-0288 (expires 2027-05-31). eCFR text for 16 CFR 681.1, 682.3, and 17 CFR 229.106 |
| Assessment dates | 2026-06-01 to 2026-07-31 (control center and substation walkthroughs 2026-07-14 to 2026-07-16; evidence sampling completed 2026-08-14) |
| Assessors | GRC team and the NERC compliance team (second line, under the Chief Compliance Officer); sampling for 12 CIP rows reperformed by Internal Audit |
| Approved | Chief Compliance Officer, CIP Senior Manager, and CISO, 2026-08-21; roadmap reviewed by the risk and reliability committee of the board, 2026-09-10 |

## 1. Applicability
### 1.1 NERC CIP: which standards apply and why
1. **Who must comply.** Section 215 of the Federal Power Act makes "all users, owners and operators of the bulk-power system" comply with approved reliability standards (16 U.S.C. 824o(b)(1)). The company is on the NERC Compliance Registry as a Distribution Provider, Transmission Owner, and Transmission Operator. SERC Reliability Corporation is its Regional Entity and Compliance Enforcement Authority.
2. **Scope for a TO and TOP.** For Responsible Entities other than Distribution Providers, the CIP standards apply to "All BES Facilities" (Applicability 4.2.2). For the DP function, only the Facilities in section 4.2.1 count; the company's DP equipment adds nothing beyond its TO and TOP scope.
3. **Categorization (CIP-002-5.1a, last approved 2026-03-12):**

| Asset | Attachment 1 criterion | Impact rating |
|---|---|---|
| EMS at the TCC and backup TCC | 1.3: Control Center performing TOP functional obligations for assets that meet criteria 2.4 and 2.5 | **High** |
| Substations P and R (500 kV) | 2.4: Transmission Facilities operated at 500 kV or higher | **Medium** (External Routable Connectivity) |
| Substation K (230 kV) | 2.5: 200 kV to 499 kV station connected to three or more other stations with an aggregate weighted value over 3,000 (five 230 kV lines at 700 = 3,500) | **Medium** (External Routable Connectivity) |
| Other 143 transmission substations | 3.2: Transmission stations and substations | **Low** |
| UFLS (about 2,600 MW in stages) | 2.10 requires 300 MW or more under a common control system without operator initiation; the company's relays act independently | Not medium (relays at transmission substations fall under the low impact assets) |
| ADMS and OMS at the DCC | Distribution facilities are not BES Facilities; the DCC is not a Control Center in the NERC Glossary sense (2024 compliance memo) | Not a BES Cyber System |

4. **Result.** Every CIP standard applies:
   - CIP-002-5.1a and CIP-003-9 apply in full, including the low impact Attachment 1 for 143 substations.
   - CIP-004-7 to CIP-011-3 apply to the high and medium impact BES Cyber Systems and their associated EACMS, PACS, and PCA, using each requirement part's "Applicable Systems" column. Parts written only for high impact systems (for example, CIP-007-6 R4.4 log review every 15 days, CIP-009-6 R2.3 operational exercise, CIP-010-4 R2.1 and R3.2) apply because the EMS is high impact.
   - CIP-012-2 applies because the company is a TOP that operates Control Centers.
   - CIP-013-2 applies to the high and medium impact systems and their EACMS and PACS.
   - CIP-014-3 applies because the company owns Transmission stations operated at 500 kV (Applicability 4.1.1.1). The R1 assessment identified Substation P.

### 1.2 Other requirements
| Regulation | Applies? | Basis |
|---|---|---|
| NERC EOP-004-4 | **Yes** | DP, TO, and TOP are listed responsible entities; Attachment 1 events for each function |
| Form DOE-417 | **Yes** | Mandatory under section 13(b) of the Federal Energy Administration Act of 1974; the company is an electric utility and files its own reports. Criteria were read from the current OMB-approved instructions, which add criterion 14 (attempted cyber compromise of high or medium impact systems) |
| SEC Form 8-K Item 1.05 and Reg S-K Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| FTC Identity Theft Red Flags Rule | **Yes** | A creditor under 15 U.S.C. 1681m(e)(4): it obtains consumer reports for deposit decisions and furnishes information to consumer reporting agencies. Utility accounts are covered accounts (16 CFR 681.1(b)(3)) |
| FTC Disposal Rule | **Yes** | The company possesses consumer information derived from consumer reports (16 CFR 682.1-682.2) |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example; Georgia and other states are handled through counsel's state matrix |
| TSA pipeline directives (N22-R02), NRC 10 CFR 73.54 (N22-R03), SDWA section 1433 (N22-R04) | **No** | No pipelines, no reactors, no water system |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25 |
| PCI DSS | **Contract only** | Noted, not assessed (card data stays with the processor and the charging platform vendor) |
| SOX Section 404 | Separate program | IT general controls over the ERP are tested by the SOX program |

## 2. Method
1. **Requirements.** Rows follow each standard's own structure (requirement, part, Attachment 1 section). Summaries are written in this repository's own words; the standards' text is not reproduced. The requirement type column records the standard's Violation Risk Factor. Regulations from the eCFR and the Florida statute follow their section structure.
2. **Applicable Systems.** For each CIP part, the team checked the "Applicable Systems" column (for example, high impact only, or medium impact at Control Centers) and scoped the evidence to those systems.
3. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **These are author mappings.** NIST has not published an official mapping for NERC CIP, the SEC rules, or the FTC rules.
4. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); smaller or lower-risk populations used 25 to 40 items; configuration data (rule bases, training and PRA dates, DLP scans) was checked in full with analytics. Selections were random. **49 rows were tested by sampling or full-population analytics; 11 found exceptions.** For a NERC requirement, any exception is treated as a potential noncompliance, not a tolerable deviation.
5. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / standard | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| CIP-002-5.1a | 6 | 0 | 0 | 0 | 6 |
| CIP-003-9 | 11 | 4 | 0 | 0 | 15 |
| CIP-004-7 | 17 | 2 | 0 | 0 | 19 |
| CIP-005-7 | 11 | 1 | 0 | 0 | 12 |
| CIP-006-6 | 14 | 0 | 0 | 0 | 14 |
| CIP-007-6 | 19 | 1 | 0 | 0 | 20 |
| CIP-008-6 | 12 | 0 | 0 | 0 | 12 |
| CIP-009-6 | 10 | 0 | 0 | 0 | 10 |
| CIP-010-4 | 14 | 0 | 0 | 0 | 14 |
| CIP-011-3 | 3 | 1 | 0 | 0 | 4 |
| CIP-012-2 | 3 | 2 | 0 | 0 | 5 |
| CIP-013-2 | 8 | 1 | 0 | 0 | 9 |
| CIP-014-3 | 5 | 1 | 0 | 0 | 6 |
| **NERC CIP subtotal** | **133** | **13** | **0** | **0** | **146** |
| NERC EOP-004-4 | 2 | 0 | 0 | 0 | 2 |
| Form DOE-417 | 4 | 1 | 0 | 0 | 5 |
| SEC Form 8-K Item 1.05 | 2 | 1 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 4 | 0 | 0 | 0 | 4 |
| FTC Red Flags Rule (16 CFR 681.1) | 4 | 5 | 1 | 0 | 10 |
| FTC Disposal Rule (16 CFR 682.3) | 1 | 0 | 0 | 0 | 1 |
| State breach and data security laws | 5 | 2 | 0 | 0 | 7 |
| **Total** | **155** | **22** | **1** | **0** | **178** |

**Gap risk levels (23 rows Partially met or Not met):** High 11, Moderate 12.

**Reading the results.** The CIP program is mature: 133 of 146 rows are Met, and CIP-006, CIP-008, CIP-009, and CIP-010 had no exceptions. The CIP gaps sit at the edges of the program: low impact substations with an old vendor access method, one late badge removal, undocumented firewall rules from a 2025 project, a missed patch source change, BCSI that leaked into a collaboration site, three procurements that skipped the supply chain assessment, and two plan-design weaknesses (CIP-012-2 availability and the CIP-014-3 timeline). The FTC Red Flags program is the weakest area outside NERC.

## 4. Potential noncompliance and self-reports
Ten rows describe six issues that are potential violations of an enforceable CIP standard, not only weaknesses. A "Self-Report" is the Compliance Monitoring and Enforcement Program term (NERC Rules of Procedure Appendix 4C) for a registered entity reporting that it has, or may have, violated a standard.

| Issue | Rows | Standard | Start of the potential noncompliance |
|---|---|---|---|
| Relay vendor remote access at 12 low impact substations without Section 6 methods | G-010, G-017, G-018, G-019 | CIP-003-9 R2, Att. 1 Sec. 6 | 2026-04-01 (effective date) |
| Physical access removed 27 hours after a termination action | G-034 | CIP-004-7 R5.1 | 2026-03-17 |
| BCSI in a general collaboration site open to 340 users | G-038, G-124 | CIP-004-7 R6.1; CIP-011-3 R1.2 | 2025-11 (first upload) |
| 9 of 212 Substation K EAP rules without documented reasons | G-043 | CIP-005-7 R1.3 | 2025-09 (relay upgrade) |
| Two missed 35-day patch evaluations for PACS servers | G-070 | CIP-007-6 R2.2 | 2026-02 |
| 3 of 25 CIP-scope procurements without the R1.1 risk assessment | G-139 | CIP-013-2 R2 | 2025-04 |

The CIP Senior Manager decided on 2026-08-21 to self-report all six issues to SERC by 2026-09-30 with mitigation plans. Two more rows are under review and not yet self-reported: CIP-012-2 R1 Parts 1.2 and 1.3 (G-128, G-129; judged a weakness in an identified method) and CIP-014-3 R5 (G-145; decision on 2026-10-15 whether a slipped timeline without a documented revision is a noncompliance). A known noncompliance is never accepted as a risk (P01 section 1).

## 5. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-010, G-017 to G-019 | CIP-003-9 R2, Att. 1 Sec. 6.1-6.3 | Relay vendor modems at 12 low impact sites: no method to determine, disable, or monitor vendor access | Route vendor access through the substation gateways with logging and a DCC disable control; remove modems (POAM-023) | Director, OT Engineering | 2026-12-31 |
| G-034 | CIP-004-7 R5.1 | 1 of 60 terminations: badge removed after 27 hours | Revocation triggered by the termination action itself; daily reconciliation (POAM-008) | Chief Human Resources Officer | 2026-11-30 |
| G-038, G-124 | CIP-004-7 R6.1; CIP-011-3 R1.2 | BCSI outside the repository with unauthorized access | Move files; review the 340 users; BCSI labels and blocking; quarterly DLP sweep (POAM-022) | Director, NERC Compliance | 2026-11-15 |
| G-043 | CIP-005-7 R1.3 | 9 EAP rules without reasons at Substation K | Document or remove; enforce reason field (POAM-020) | Director, OT Security | 2026-10-31 |
| G-070 | CIP-007-6 R2.2 | PACS patch evaluations missed twice | Patch source review each cycle; GRC tracking (POAM-021) | Director, Corporate Security | 2026-11-30 |
| G-139 | CIP-013-2 R2 | Supply chain plan skipped for 3 procurements | Purchasing system hard stop; retroactive assessments (POAM-019) | Director, Third-Party Risk Management | 2026-12-31 |
| G-154 | Form 8-K Item 1.05 | Materiality process never exercised with an OT scenario; no BIA outage costs in the worksheet | OT tabletop 2026-11-18; worksheet update (POAM-011) | General Counsel | 2026-12-15 |

Moderate gaps (CIP-012-2, CIP-014-3, DOE-417 criterion 14, the Red Flags program, and Fla. Stat. 501.171(2) and (8)) are listed with owners and dates in `gap-analysis.csv` and are tracked as POAM-024 to POAM-026.

## 6. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q3 (by 2026-09-30) | Six self-reports filed with SERC | CIP-003-9; CIP-004-7; CIP-005-7; CIP-007-6; CIP-011-3; CIP-013-2 | Self-report confirmations; mitigation plans |
| 2026 Q4 | Substation K rules (POAM-020); CIP-014 timeline decision and revision (POAM-025); DOE-417 criterion 14 in checklists; BCSI cleanup (POAM-022); termination trigger (POAM-008); PACS patch tracking (POAM-021); OT disclosure tabletop (POAM-011); Section 6 at 12 sites (POAM-023); purchasing hard stop (POAM-019); Red Flags training; export rights reduced | CIP-003 to CIP-014; DOE-417; SEC Item 1.05; 16 CFR 681.1(e)(3); Fla. Stat. 501.171(2) | Rule reasons; DLP sweep reports; tabletop report; gateway logs; purchase order controls |
| 2027 Q1 | Identity Theft Prevention Program update approved by the board committee; service provider oversight; TCC procedure update and second carrier entrance (POAM-024); SSN purge (POAM-026); Substation P barrier complete (POAM-025) | 16 CFR 681.1(d)-(e); CIP-012-2; Fla. Stat. 501.171(8); CIP-014-3 R5 | Program v2; board minutes; circuit records; purge logs |
| 2027 Q2 to Q3 | Annual gap reassessment; review of CIP-002 categorization before the EMS upgrade; prepare for EOP-004-5 (2027-10-01) | All | Updated P01 and P03 |
| 2028 | Virtualization revisions (2028-07-01), CIP-015-1 internal network security monitoring and CIP-014-4 (2028-10-01) | CIP-002-8 to CIP-013-3; CIP-015-1; CIP-014-4 | Transition plans |

## 7. Pending regulatory changes
These versions are approved but **not yet in effect**. None is treated as a current obligation. Dates are from the NERC standards pages.
- **Virtualization revisions, 2028-07-01:** CIP-002-8, CIP-003-10, CIP-004-8, CIP-005-8, CIP-006-7.1, CIP-007-7.1, CIP-008-7.1, CIP-009-7.1, CIP-010-5, CIP-011-4.1, and CIP-013-3. The EMS upgrade planned for 2027 will be designed with the new terms in mind.
- **CIP-015-1, 2028-10-01, and CIP-015-2, 2029-10-01:** internal network security monitoring inside the ESPs of high impact systems and medium impact systems with External Routable Connectivity. The OT sensors at the TCC, backup TCC, and Substations P, R, and K are a head start.
- **CIP-014-4, 2028-10-01:** physical security revisions; the next R1 assessment (due by 2027-08) will be planned against both versions.
- **CIP-003-11, 2029-07-01:** rewrites the low impact electronic access controls, including authentication and malicious communication detection for all routable access. The fix for the 12 Section 6 sites is designed to meet it.
- **EOP-004-5, 2027-10-01:** update the event reporting Operating Plan.
- **DOE-417:** the current OMB approval expires 2027-05-31; check for a revised form.
- **SEC:** no proposal to amend or rescind Item 1.05 or Item 106 was found as of 2026-09-25.
- **CIRCIA:** the final rule had not been published as of 2026-09-25. If finalized as proposed, the company would likely be a covered entity; reporting to CISA is voluntary until then.
- **Watch item:** DOE issued a request for information (FR Doc. 2026-18370, 2026-09-09) under an August 2026 executive order on bulk-power system security. It is not a requirement today.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row.

## 8. Regulator-ready package
The NERC compliance team keeps a CIP evidence library indexed by standard and requirement, and the GRC team keeps the non-NERC binder indexed by `req_id`, so the company can respond quickly to a SERC audit request, a spot check, an SEC comment letter, or a state attorney general inquiry:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the Reliability Standard Audit Worksheet responses kept current for each CIP standard;
- the P01 register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and notification matrix;
- self-reports, mitigation plans, and milestone evidence;
- DOE-417 and EOP-004 filings and the event log.

## 9. Approval
Approved by the Chief Compliance Officer, the CIP Senior Manager, and the CISO on 2026-08-21. The roadmap was reviewed by the risk and reliability committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, or sooner after a CIP-002 categorization change.

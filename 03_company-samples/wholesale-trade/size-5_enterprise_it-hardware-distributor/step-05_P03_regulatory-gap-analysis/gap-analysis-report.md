# Regulatory Gap Analysis: Cris Santos Company | Wholesale Trade | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded IT hardware and software distributor; DoD prime contractor and subcontractor through Federal Solutions) |
| Tier / Vertical | Enterprise / Wholesale Trade |
| Primary regulation | NIST SP 800-171 Rev. 2 (110 requirements), required by DFARS 252.204-7012(b)(2) and assessed under CMMC Level 2 (32 CFR 170.14(c)(3)), for the Federal Solutions CUI Enclave (FSCE) |
| Also analyzed | FAR 52.204-21 (CMMC Level 1) for the enterprise FCI scope; FAR 52.204-25 and 52.204-23; DFARS 252.246-7008; DFARS 252.204-7012, -7019/-7020, and -7021 clause duties with 32 CFR Part 170; SEC Form 8-K Item 1.05 and Regulation S-K Item 106; CCPA/CPRA and CPPA regulations; CTPAT; FTC Act Section 5; state breach and data security laws (Florida worked example) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14; rows G-115 and G-116 updated 2026-08-12 with a P07 finding) |
| Assessors | GRC team and CMMC Program Office (second line) with the Director, Government Contracts and the Chief Privacy Officer; sampling reperformed by Internal Audit for 8 rows |
| Working file | `gap-analysis.csv` (165 rows: G-001 to G-110 for the 110 SP 800-171 requirements, G-111 to G-125 for the 15 FAR 52.204-21 requirements, G-126 to G-165 for clause, regulation, and statute duties) |
| Approved | Chief Compliance Officer and the CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| DFARS 252.204-7012 and SP 800-171 Rev. 2 | **Yes** | In DoD prime contracts and subcontracts; Federal Solutions configuration jobs use covered defense information. No size exemption. CUI is permitted only in the FSCE, but any system that holds CUI becomes a covered contractor information system |
| DFARS 252.204-7021 and 32 CFR Part 170 (Level 2) | **Yes** | Two 2026 contracts require Level 2 (C3PAO), which DoD may require at its discretion in Phase 1 (170.3(e)(1)). Phase 2 (planned for 2026-11-10, 170.3(e)(2)) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13; contracting officers remove these requirements by modification before the next option period or at the next administrative modification (DoD Class Deviation 2026-O0025, Revision 3, DFARS 240.371-5). FSCE status: Conditional Level 2 (C3PAO) since 2026-05-14. The closeout is kept as a voluntary choice |
| FAR 52.204-21 and CMMC Level 1 | **Yes** | FCI in every DoD order (OCFP, productivity suite, endpoints). Orders exclusively for COTS items are outside CMMC (170.3(c)), but most federal orders include configuration, kitting, or delivery terms, so the company treats all DoD orders as FCI |
| DFARS 252.204-7019 and -7020 | **Yes** | SP 800-171 DoD Assessment score must be current in SPRS for the FSCE |
| FAR 52.204-25 and 52.204-23 | **Yes** | In all federal contracts; a hardware distributor is directly exposed to providing covered equipment |
| DFARS 252.246-7008 | **Yes** | Prescribed at 48 CFR 246.870-3(b) when DoD procures electronic parts or end items containing them, including commercial products |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| CCPA/CPRA (N42-R08) | **Yes, partly** | A "business" under Cal. Civ. Code 1798.140(d). The cybersecurity audit rule (Cal. Code Regs. tit. 11, 7120) does **not** apply: about 41,000 California consumers and about 420 with sensitive personal information are below the 250,000 and 50,000 thresholds. ADMT and risk assessment rules apply to the resume screening tool |
| CTPAT (N42-R06) | **Yes, voluntary** | Member since 2019 (importer entity type); the minimum security criteria are a condition of membership, not a regulation |
| FTC Act Section 5 (N42-R01) | **Yes** | No size threshold; applies to data security practices and security claims to resellers |
| State breach and data security laws | **Yes** | Personal information of employees, reseller contacts, and license registrants in all states. The law of each state where affected individuals reside applies; Florida is the worked example |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25; reporting is voluntary until then |
| PCI DSS | Outside this analysis | Contractual (acquiring bank); card data stays in the processor's hosted payment fields |
| SOX Section 404 | Separate program | ERP IT general controls are tested by the SOX program and not repeated here |

**Not applicable row:** G-155, the CPPA cybersecurity audit (below thresholds; rechecked each year).

## 2. Method
1. **Decompose.** The 110 SP 800-171 rows follow NIST's official structure (families 3.1 to 3.14), with the CMMC identifier and point value from the CMMC Scoring Methodology (32 CFR 170.24). The 15 FAR 52.204-21 rows quote the clause (48 CFR 52.204-21(b)(1)) and use the Level 1 identifiers in Table 2 to 32 CFR 170.15(c)(1)(ii). Clause and regulation rows cite each paragraph as read on eCFR (version date 2026-09-23); SEC rows follow 17 CFR 229.106 and the SEC's Item 1.05 compliance guide. CTPAT rows describe the program's criteria by section only, because the criteria text could not be retrieved from CBP during this analysis.
2. **Crosswalk.** SP 800-171 rows use the official SP 800-171 Rev. 2 Appendix D mapping (Rev. 4 control IDs, kept in `nist_official_sp800_53_appendix_d`), refined to Rev. 5 by the author; CSF 2.0 subcategories are derived from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference. All other rows are author mappings and are labeled that way.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); smaller populations used 25 to 40 items; accounts and contracts under 50 were checked in full. **20 rows were tested by sampling or full-population analytics; 6 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. For CMMC scoring, a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)), so every Partially met SP 800-171 row counts as NOT MET in the score. Gaps are rated with the P01 scale; High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| NIST SP 800-171 Rev. 2 (CMMC Level 2) | 104 | 2 | 4 | 0 | 110 |
| FAR 52.204-21 (CMMC Level 1) | 13 | 2 | 0 | 0 | 15 |
| FAR 52.204-25 (Section 889) | 1 | 2 | 0 | 0 | 3 |
| FAR 52.204-23 (Kaspersky) | 1 | 0 | 0 | 0 | 1 |
| DFARS 252.246-7008 | 2 | 2 | 0 | 0 | 4 |
| DFARS 252.204-7012 | 4 | 2 | 0 | 0 | 6 |
| DFARS 252.204-7019/-7020 | 2 | 0 | 0 | 0 | 2 |
| DFARS 252.204-7021 and 32 CFR Part 170 | 1 | 4 | 0 | 0 | 5 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 4 | 1 | 0 | 0 | 5 |
| CCPA/CPRA and CPPA regulations | 1 | 2 | 0 | 1 | 4 |
| CTPAT (voluntary program) | 1 | 1 | 0 | 0 | 2 |
| FTC Act Section 5 | 1 | 0 | 0 | 0 | 1 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| **Total** | **139** | **21** | **4** | **1** | **165** |

**Gap risk levels across all regulations (25 gaps):** High 11, Moderate 9, Low 5.

### SP 800-171 Rev. 2 by family
| Family | Met | Partially met | Not met |
|---|---|---|---|
| 3.1 Access Control | 20 | 1 | 1 |
| 3.2 Awareness and Training | 3 | 0 | 0 |
| 3.3 Audit and Accountability | 9 | 0 | 0 |
| 3.4 Configuration Management | 8 | 0 | 1 |
| 3.5 Identification and Authentication | 11 | 0 | 0 |
| 3.6 Incident Response | 2 | 1 | 0 |
| 3.7 Maintenance | 6 | 0 | 0 |
| 3.8 Media Protection | 8 | 0 | 1 |
| 3.9 Personnel Security | 2 | 0 | 0 |
| 3.10 Physical Protection | 6 | 0 | 0 |
| 3.11 Risk Assessment | 3 | 0 | 0 |
| 3.12 Security Assessment | 4 | 0 | 0 |
| 3.13 System and Communications Protection | 15 | 0 | 1 |
| 3.14 System and Information Integrity | 7 | 0 | 0 |
| **Total** | **104** | **2** | **4** |

**Score.** Using the CMMC Scoring Methodology (32 CFR 170.24), the internal score is **104 out of 110**, the same as the C3PAO score, but the composition has changed:
- **4 C3PAO POA&M items are still Not met:** 3.1.21, 3.4.9, 3.8.9, 3.13.9 (1 point each). The other 2 POA&M items (3.3.4 and 3.5.8) were remediated in 2026-07 and await the closeout assessment.
- **2 items drifted after certification and are Partially met:** 3.1.3 (CUI reached commercial systems through customer uploads) and 3.6.3 (the annual incident response test is overdue). Both are 1-point items.

**What this means for CMMC.** The closeout assessment covers only the POA&M items (32 CFR 170.21(b)), and it must be completed by 2026-11-10 or the Conditional status expires. The drift items matter as much: DFARS 252.204-7021(a) defines a "current" status as one with no changes in compliance since the status date, and the Affirming Official must attest after closeout that all requirements are implemented (32 CFR 170.22(a)(2)(ii)). The President, Federal Solutions will not sign that affirmation until 3.1.3 and 3.6.3 are also fixed. With CMMC Phase 2 suspended, the closeout is a voluntary choice. It keeps a Final Level 2 status ready for any program office that requires one. The SP 800-171 Rev. 2 work is owed either way under DFARS 252.204-7012.

**FAR 52.204-21.** 2 of 15 requirements are partially met because P07 found 3 shared dock kiosk accounts in the WMS at OH-1 that reach DoD ship-to data (G-115, G-116). CMMC Level 1 allows no POA&M (170.21(a)(1)), so these must be fixed and counsel must review the Level 1 entry before the 2027-01-15 affirmation.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-003 | SP 800-171 R2 3.1.3 | CUI flowed into commercial systems through customer uploads | Block attachments for federal-flagged accounts; CUI marking detection (POAM-007) | Vice President, E-commerce | 2026-10-15 |
| G-115 | 52.204-21(b)(1)(v) | Shared WMS kiosk accounts at OH-1 | Badge sign-in; disable accounts (POAM-003) | Vice President, Distribution Operations | 2026-10-31 |
| G-116 | 52.204-21(b)(1)(vi) | Kiosk users not individually authenticated | As above (POAM-003) | Vice President, Distribution Operations | 2026-10-31 |
| G-126 | 52.204-25(b)(1) | Drop-ship substitutions bypass the Section 889 screen | Screen before acceptance; weekly retro-screen (POAM-006) | Director, Government Contracts | 2026-12-31 |
| G-134 | 252.204-7012(b)(2)(i) | CUI held in systems not assessed for SP 800-171 | Prevent recurrence (POAM-007) | Director, CMMC Program Office | 2026-10-15 |
| G-135 | 252.204-7012(b)(2)(ii)(D) | CUI stored for a period in commercial cloud services | As above (POAM-007) | Director, CMMC Program Office | 2026-10-15 |
| G-142 | 252.204-7021(d)(1)(i) | Final Level 2 depends on the closeout | Closeout 2026-10-20 (POAM-020) | President, Federal Solutions | 2026-11-10 |
| G-143 | 252.204-7021(d)(2) | CUI processed on systems without Level 2 status | Prevent recurrence (POAM-007) | Vice President, E-commerce | 2026-10-15 |
| G-146 | 32 CFR 170.21(b) | 4 POA&M items open with the 180-day deadline approaching | Close by 2026-09-30; pre-assessment 2026-10-06 (POAM-020) | President, Federal Solutions | 2026-11-10 |
| G-147 | Form 8-K Item 1.05 | Playbook has no supplier-compromise scenario | Supply chain scenario; tabletop 2026-11-18 (POAM-014) | General Counsel | 2026-12-15 |
| G-148 | Form 8-K Item 1.05; 17 CFR 229.106(a) | No guidance on when a supplier event is a "cybersecurity incident" | Decision tree with outside securities counsel (POAM-014) | General Counsel | 2026-12-15 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q3 (September) | Close the 4 FSCE POA&M items and the 3.6.3 tabletop with a DIBNet drill (POAM-020) | SP 800-171 3.1.21, 3.4.9, 3.6.3, 3.8.9, 3.13.9 | Configuration evidence; tabletop report |
| 2026 Q4 | CUI upload controls (POAM-007, 2026-10-15); internal pre-assessment 2026-10-06; C3PAO closeout 2026-10-20 and affirmation; kiosk accounts removed (POAM-003); supply chain materiality tabletop 2026-11-18 (POAM-014); drop-ship screening and flowdowns (POAM-006); CCPA ADMT workflow or exclusion (POAM-021) | 252.204-7012(b); 252.204-7021(d); 32 CFR 170.21(b), 170.22; 52.204-21; 52.204-25; 252.246-7008; Item 1.05; CCPA regulations | Closeout results in SPRS; DLP reports; tabletop report; amended agreements |
| 2027 Q1 | Level 1 (Self) annual self-assessment and affirmation (2027-01-15); staffing agency and 3PL notice terms (POAM-017); Item 106 wording aligned and tested (POAM-022) | 52.204-21; 32 CFR 170.15; Fla. Stat. 501.171(6); 17 CFR 229.106 | SPRS entry; contract amendments; Form 10-K |
| 2027 Q2 | CTPAT partner records consolidated; review of pending FAR changes | CTPAT; proposed FAR part 40 | Updated security profile |
| 2027 Q3 | Annual gap reassessment | All | Updated P03 |

## 6. Pending regulatory changes
These are **proposed** and are not treated as current obligations.
- **FAR overhaul, parts 1, 2, 4, 33, 39, 40, 52, and 53** (FR Doc. 2026-12559, 2026-06-23; comments closed 2026-07-23). If finalized as proposed, a new FAR 52.240-7 clause for CUI would require **NIST SP 800-171 Rev. 3**, and a new FAR 52.240-3 would consolidate the security prohibitions, including Section 889, with reporting standardized to 72 hours from discovery. The `pending_rule_change` column flags affected rows. CMMC Level 2 itself is fixed to Rev. 2 in 32 CFR 170.14(c)(3).
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **CMMC phases (in effect, not proposed):** Phase 2 (planned for 2026-11-10 in 32 CFR 170.3(e)(2)) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 suspending CMMC Phase 2. Until 2028-11-09, DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self). SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). The text of 32 CFR Part 170 is unchanged.

## 7. Regulator-ready package
The GRC team and the CMMC Program Office keep an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a DCMA DIBCAC request under DFARS 252.204-7020, a contracting officer inquiry, a CPPA or state attorney general request, a CBP CTPAT validation, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the FSCE SSP, C3PAO findings report, POA&M, SPRS records, and hashed assessment artifacts kept for 6 years (32 CFR 170.17(c)(4));
- the P01 risk register, P02 OCFP SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- the CUI spill report, purge records, and notices to primes and contracting officers;
- Section 889 screening logs and DFARS 252.246-7008 notices and traceability files.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, plus an FSCE recheck after the closeout assessment.

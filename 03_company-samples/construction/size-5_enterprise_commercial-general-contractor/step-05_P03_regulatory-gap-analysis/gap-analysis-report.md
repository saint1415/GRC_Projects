# Regulatory Gap Analysis: Cris Santos Company | Construction | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded commercial and institutional building general contractor; federal and DoD work through the Federal Group) |
| Tier / Vertical | Enterprise / Construction |
| Primary regulation | NIST SP 800-171 Rev. 2 (110 requirements), required by DFARS 252.204-7012(b)(2) and assessed under CMMC Level 2 (32 CFR 170.14(c)(3)), for the Federal Programs CUI Enclave (FPCE) and its 16 installation plan rooms |
| Also analyzed | FAR 52.204-21 (CMMC Level 1) for the enterprise FCI scope; FAR 52.204-25, 52.204-26, and 52.204-23; DFARS 252.204-7012, -7019, -7020, and -7021 clause duties with 32 CFR Part 170; FAR 52.232-33 and 52.232-27 payment duties; SEC Form 8-K Item 1.05 and Regulation S-K Item 106; state breach and data security laws (Florida worked example) |
| Text verified | eCFR (48 CFR, 32 CFR Part 170, 17 CFR 229.106) as of 2026-09-23; Fla. Stat. 501.171 (2026); proposed FAR overhaul FR Doc. 2026-12559 |
| Assessment dates | 2026-06-01 to 2026-07-31 (FPCE readiness check 2026-07-06 to 2026-07-24; plan room walkthroughs 2026-07-14 to 2026-07-17; evidence sampling completed 2026-08-14) |
| Assessors | GRC team and CMMC Program Office (second line) with the Director of Government Contracts and outside government contracts counsel; sampling reperformed by Internal Audit for 8 rows |
| Working file | `gap-analysis.csv` (160 rows: G-001 to G-110 for the 110 SP 800-171 requirements, G-111 to G-125 for the 15 FAR 52.204-21 requirements, G-126 to G-160 for clause, regulation, and statute duties) |
| Approved | Chief Compliance Officer and the CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| DFARS 252.204-7012 and SP 800-171 Rev. 2 | **Yes** | In all 26 DoD contracts. Design-build and MILCON projects use CUI-marked drawings, which are covered defense information. No size exemption. Any system that holds CUI is a covered contractor information system, which is why CUI on the commercial project management platform matters |
| DFARS 252.204-7021 and 32 CFR Part 170 | **Yes** | In the 11 DoD awards since 2025-11-10 (4 at Level 2 (Self), 7 at Level 1 (Self)). Phase 2 was planned for 2026-11-10, when DoD intended to require Level 2 (C3PAO) for applicable awards (170.3(e)(2)). The DoD (Department of War) CIO memorandum of 2026-07-13 suspends Phase 2. Until 2028-11-09, DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self); from 2028-11-10 it includes the clause whenever the contractor will process, store, or transmit FCI or CUI on its own systems (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). For existing contracts, contracting officers remove CMMC requirements by modification before the next option period or at the next scheduled administrative modification. SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies |
| FAR 52.204-21 and CMMC Level 1 | **Yes** | In all 38 federal contracts. FCI is in the PDPP, the productivity suite, endpoints, and jobsite networks: the enterprise FCI scope. No size exemption; only COTS-item acquisitions are excluded |
| DFARS 252.204-7019 and -7020 | **Yes** | An SP 800-171 DoD Assessment score must be current in SPRS for the FPCE, and subcontractors must have one before award |
| FAR 52.204-25, 52.204-26, and 52.204-23 | **Yes** | In all federal contracts. BTS installs video surveillance and network equipment in federal buildings, so Section 889 is a direct operational risk |
| FAR 52.232-33 and 52.232-27 | **Yes** | Payment clauses in federal contracts. Included because business email compromise targets the same money flows (P08) |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| State breach and data security laws | **Yes** | Personal information of employees (including certified payroll Social Security numbers) and others in 8 states. The law of each state where affected individuals reside applies; Florida is the worked example |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25. Construction is not itself a critical infrastructure sector; recheck when final |
| HIPAA, PCI DSS, CCPA | **No** | See `../00_company-facts.md` section 1 (no PHI, no card payments, no California operations) |
| SOX Section 404 | Separate program | ERP IT general controls are tested by the SOX program and not repeated here |

**Size changes how, not whether.** None of these rules has a size exemption. What changes at enterprise size is scale (about 1,150 enclave users, 640 FCI subcontractors, 48 CUI subcontractors), the number of scopes (the FPCE at Level 2, the enterprise FCI scope at Level 1, and AQ-2's separate Level 1 scope), and the SEC disclosure duties.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. New DoD awards under DFARS Part 240 replace DFARS 252.204-7019 and -7020 with 252.240-7997, which covers DoD-led Medium and High assessments; the rows for 7019 and 7020 still describe the contracts awarded before that change. See `00_company-facts.md`.

## 2. Method
1. **Decompose.** The 110 SP 800-171 rows follow NIST's official structure (families 3.1 to 3.14), with the CMMC identifier and point value from the CMMC Scoring Methodology (32 CFR 170.24(c)(2)). The 15 FAR 52.204-21 rows quote the clause (48 CFR 52.204-21(b)(1)) and use the Level 1 identifiers in 32 CFR 170.15. Clause and regulation rows cite each paragraph as read on eCFR (version date 2026-09-23); SEC rows follow 17 CFR 229.106 and the SEC's Item 1.05 materials; the Florida rows follow the statute text.
2. **Crosswalk.** SP 800-171 rows use the official SP 800-171 Rev. 2 Appendix D mapping (Rev. 4 control IDs, kept in `nist_official_sp800_53_appendix_d`), refined to Rev. 5 by the author; CSF 2.0 subcategories are derived from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference. FAR 52.204-21 rows follow the 32 CFR 170.15 table to their SP 800-171 equivalents. All other rows are author mappings and are labeled that way.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); smaller populations used 25 items; populations under 50 and configuration data were checked in full. For the plan rooms, the team visited 6 of 16 sites, chosen to cover all three installation types. **36 rows were tested by sampling, site visits, or full-population analytics; 14 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. For CMMC scoring, a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)), so every Partially met SP 800-171 row counts as NOT MET in the score. Gaps are rated with the P01 scale; High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| NIST SP 800-171 Rev. 2 (CMMC Level 2) | 102 | 7 | 1 | 0 | 110 |
| FAR 52.204-21 (CMMC Level 1) | 13 | 2 | 0 | 0 | 15 |
| FAR 52.204-21(c) flowdown | 1 | 0 | 0 | 0 | 1 |
| FAR 52.204-25 and 52.204-26 (Section 889) | 4 | 1 | 0 | 0 | 5 |
| FAR 52.204-23 (Kaspersky) | 1 | 0 | 0 | 0 | 1 |
| DFARS 252.204-7012 | 4 | 2 | 0 | 0 | 6 |
| DFARS 252.204-7019/-7020 | 1 | 1 | 0 | 0 | 2 |
| DFARS 252.204-7021 and 32 CFR Part 170 | 2 | 4 | 0 | 0 | 6 |
| FAR payment clauses (52.232-33, 52.232-27) | 2 | 0 | 0 | 0 | 2 |
| SEC Form 8-K Item 1.05 | 2 | 1 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 4 | 1 | 0 | 0 | 5 |
| State breach and data security laws | 2 | 2 | 0 | 0 | 4 |
| **Total** | **138** | **21** | **1** | **0** | **160** |

**Gap risk levels across all regulations (22 gaps):** High 14, Moderate 6, Low 2.

### SP 800-171 Rev. 2 by family
| Family | Met | Partially met | Not met |
|---|---|---|---|
| 3.1 Access Control | 20 | 2 | 0 |
| 3.2 Awareness and Training | 3 | 0 | 0 |
| 3.3 Audit and Accountability | 9 | 0 | 0 |
| 3.4 Configuration Management | 8 | 1 | 0 |
| 3.5 Identification and Authentication | 11 | 0 | 0 |
| 3.6 Incident Response | 3 | 0 | 0 |
| 3.7 Maintenance | 6 | 0 | 0 |
| 3.8 Media Protection | 7 | 2 | 0 |
| 3.9 Personnel Security | 2 | 0 | 0 |
| 3.10 Physical Protection | 4 | 1 | 1 |
| 3.11 Risk Assessment | 3 | 0 | 0 |
| 3.12 Security Assessment | 3 | 1 | 0 |
| 3.13 System and Communications Protection | 16 | 0 | 0 |
| 3.14 System and Information Integrity | 7 | 0 | 0 |
| **Total** | **102** | **7** | **1** |

**Score.** Using the CMMC Scoring Methodology (32 CFR 170.24(c)(2)), the internal score is **96 out of 110**, against 110 at the 2026-02-27 self-assessment. 8 requirements drifted: 3.1.3 (1 point), 3.1.20 (1), 3.4.1 (5), 3.8.1 (3), 3.8.4 (1), 3.10.3 (1), 3.10.4 (1), and 3.12.4 (1).

**Why the plan rooms drove the drift.** The FPCE SSP treated the enclave as a cloud tenant plus laptops. It never described the 16 plan rooms, where CUI drawings are plotted, stored on paper, and handed to trades. DFARS 252.204-7012 defines media to include printouts, so paper drawing sets are CUI media. Six of the eight drifted requirements trace to that gap.

**What this means for the C3PAO assessment on 2027-01-25.** A score of 96 is above the 88 needed for a Conditional status (170.21(a)(2)(i)), but that does not help here:
- **3.1.20, 3.10.3, 3.10.4, and 3.12.4 can never be on a CMMC POA&M** (170.21(a)(2)(iii)).
- **3.4.1 (5 points) and 3.8.1 (3 points) carry more than 1 point**, so they cannot be on a POA&M either (170.21(a)(2)(ii)).
- Only 3.1.3 and 3.8.4 could be placed on a POA&M. The plan is to close all 8 before the assessment, with an internal mock assessment on 2026-12-15.

**Is the current status still current?** DFARS 252.204-7021(a) defines a current Final Level 2 (Self) status as one with no changes in compliance since the status date, plus a valid affirmation. Compliance has changed, so on counsel's advice the company will remediate, perform a new self-assessment, and post it with a new affirmation by 2026-12-15, and will not rely on the 2026-02-27 status for any new award before then (G-141).

**FAR 52.204-21.** 2 of 15 requirements are partially met: stale external accounts on federal projects in SYS-01 (G-111) and missing visitor logs at 5 of 12 federal civilian trailers (G-119). Level 1 allows no POA&M (170.21(a)(1)), so both must be fixed and counsel must review the evidence before the 2027-01-30 annual affirmation.

**The CUI found on SYS-01 was reported to DoD.** On 2026-07-09 the content search for this analysis found 1,214 CUI-marked files on the commercial project management platform for 2 DoD projects. Counsel treated the uploads as a compromise under DFARS 252.204-7012(a) (the copying of information to unauthorized media), and the company reported through DIBNet on 2026-07-11, within 72 hours of discovery (G-135). Evidence was preserved (G-137), contracting officers were told on 2026-07-14, and the purge, with the vendor's deletion attestation, finished on 2026-08-07.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-003 | SP 800-171 R2 3.1.3 | CUI flowed to SYS-01 on 2 DoD projects | Marking detection; route federal projects to the exchange gateway (POAM-019) | Director, CMMC Program Office | 2026-10-31 |
| G-020 | SP 800-171 R2 3.1.20 | 7 of 25 external recipients not verified before CUI sharing | Status check before gateway access (POAM-021; POAM-020) | Director, CMMC Program Office | 2026-12-15 |
| G-035 | SP 800-171 R2 3.4.1 | Plan room plotters and workstations not inventoried | Add with baselines (POAM-020) | Director, CMMC Program Office | 2026-11-15 |
| G-064 | SP 800-171 R2 3.8.1 | Paper CUI not secured at 3 of 6 plan rooms | Check-out logs; end-of-day sweep (POAM-020) | President, Federal Group | 2026-11-15 |
| G-077 | SP 800-171 R2 3.10.3 | Unescorted entry at 3 of 6 plan rooms | Badge-controlled doors; escort rule (POAM-020) | President, Federal Group | 2026-11-15 |
| G-078 | SP 800-171 R2 3.10.4 | No complete visitor logs at 4 of 6 plan rooms | Badge readers with retained logs (POAM-020) | President, Federal Group | 2026-11-15 |
| G-087 | SP 800-171 R2 3.12.4 | FPCE SSP omits plan rooms, paper CUI, and the CRM | SSP v3 (POAM-020) | Director, CMMC Program Office | 2026-10-31 |
| G-133 | 252.204-7012(b)(2)(i) | SP 800-171 not fully implemented on all systems that held CUI | POAM-019; POAM-020 | President, Federal Group | 2026-12-15 |
| G-134 | 252.204-7012(b)(2)(ii)(D) | CUI held in a cloud service without FedRAMP Moderate equivalence | POAM-019 | Director, CMMC Program Office | 2026-10-31 |
| G-140 | 252.204-7020(g)(2) | SPRS checks missing for 29 of 48 CUI subcontractors | Check in the award workflow (POAM-021) | Vice President, Procurement and Subcontracts | 2026-12-31 |
| G-141 | 252.204-7021(d)(1)(i) | Level 2 (Self) status may not be current | Remediate; new self-assessment and affirmation (POAM-020) | President, Federal Group | 2026-12-15 |
| G-142 | 252.204-7021(d)(2) | CUI processed on a system with only Level 1 status | POAM-019 | Director, CMMC Program Office | 2026-10-31 |
| G-144 | 252.204-7021(d)(4), (f); 32 CFR 170.23 | 7 of 11 subcontracts under 7021 contracts awarded without status verification | POAM-021 | Vice President, Procurement and Subcontracts | 2026-12-31 |
| G-149 | Form 8-K Item 1.05; 17 CFR 229.106(a) | Materiality process has no payment fraud scenario or related-occurrence rule | Playbook update; tabletop 2026-11-19 (POAM-009) | General Counsel | 2026-12-15 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 (October) | CUI marking detection on SYS-01 and federal project routing (POAM-019, 2026-10-31); FPCE SSP v3 (2026-10-31); plotter template fix | SP 800-171 3.1.3, 3.8.4, 3.12.4; 252.204-7012(b)(2)(ii)(D); 252.204-7021(d)(2) | Detection reports; SSP v3 |
| 2026 Q4 (November) | Plan room hardening at all 16 sites (2026-11-15); disclosure tabletop with a payment fraud scenario and a DIBNet drill (2026-11-19) | SP 800-171 3.4.1, 3.8.1, 3.10.3, 3.10.4; Item 1.05; 252.204-7012(c) | Badge logs; inventory; tabletop report |
| 2026 Q4 (December) | Internal mock assessment (2026-12-15); new Level 2 self-assessment and affirmation in SPRS; subcontractor status checks in the award workflow (2026-12-31); federal civilian trailer visitor logs and SYS-01 closeout removal (2026-12-31) | 32 CFR 170.16, 170.22; 252.204-7020(g)(2); 252.204-7021(f); 52.204-21(b)(1)(i), (ix) | Mock assessment report; SPRS entry; procurement records |
| 2027 Q1 | C3PAO certification assessment (2027-01-25, voluntary while CMMC Phase 2 is suspended); Level 1 annual self-assessment and affirmation (2027-01-30); Level 2 annual affirmation (2027-02-27); AQ-2 into the enterprise FCI scope (2027-03-31); SSN truncation in certified payroll attachments | 32 CFR 170.17, 170.15, 170.22; Fla. Stat. 501.171(2) | C3PAO findings report; SPRS records |
| 2027 Q2 to Q3 | Annual gap reassessment; review the proposed FAR overhaul if finalized | All | Updated P03 |

## 6. Pending regulatory changes
These are **proposed** and are not treated as current obligations.
- **FAR overhaul** (FR Doc. 2026-12559, 2026-06-23; comments closed 2026-07-23). If finalized as proposed: FAR 52.204-21 would be replaced by a new 52.240-5, Covered Federal Information; a new 52.240-7, Controlled Unclassified Information, would require **NIST SP 800-171 Rev. 3** for CUI in FAR contracts; and a new 52.240-3, Security Prohibitions and Exclusions, would consolidate prohibitions such as Section 889 and standardize reporting to 72 hours from discovery. The `pending_rule_change` column flags affected rows. CMMC Level 2 itself stays tied to Rev. 2 (32 CFR 170.14(c)(3)).
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **CMMC phases:** Phases 2 to 4 are already set in 32 CFR 170.3(e) and are treated as current law with future effective dates.

## 7. Regulator-ready package
The GRC team and the CMMC Program Office keep an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a C3PAO, a DCMA DIBCAC request under DFARS 252.204-7020(c), a contracting officer inquiry, a state attorney general, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections and site visit records for every sampled row;
- the FPCE SSP, the 2026-02-27 self-assessment, SPRS records, and assessment artifacts kept for 6 years (32 CFR 170.16(c)(4));
- the DIBNet report of 2026-07-11, preserved evidence, purge attestation, and contracting officer notices;
- the P01 risk register, P02 PDPP SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- Section 889 screening logs, the reasonable inquiry file, and subcontractor status checks.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, plus an FPCE recheck after the C3PAO assessment.

# Regulatory Gap Analysis: Cris Santos Company | Defense Industrial Base | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded tier-1 aerostructures and aircraft components manufacturer; DoD prime contractor and subcontractor) |
| Tier / Vertical | Enterprise / Defense Industrial Base |
| Primary regulation | CMMC Level 2 / NIST SP 800-171 Rev. 2 (110 requirements), required by DFARS 252.204-7012(b)(2) and assessed under 32 CFR 170.14(c)(3) |
| Also analyzed | CMMC Level 3 (24 requirements, 32 CFR 170.14(c)(4)); DFARS 252.204-7012, 252.204-7019, 252.204-7020, 252.204-7021; 32 CFR Part 170 scoping and Level 3 prerequisites; FAR 52.204-21 and 52.204-25; ITAR and EAR; NISPOM (32 CFR Part 117); SEC Form 8-K Item 1.05 and Regulation S-K Item 106; state breach and data security laws (Florida worked example) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team and CMMC Program Office (second line) with the Vice President, Trade Compliance and the Corporate Facility Security Officer; sampling reperformed by Internal Audit for 12 rows |
| Working file | `gap-analysis.csv` (180 rows: G-001 to G-110 for the 110 Level 2 requirements, G-111 to G-134 for the 24 Level 3 requirements, G-135 to G-180 for clause, regulation, and statute duties) |
| Approved | Director, CMMC Program Office and the CISO, 2026-08-21; roadmap reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| DFARS 252.204-7012 | **Yes** | In current DoD prime contracts and subcontracts; the company holds covered defense information. No size exemption. Applies to every covered contractor information system, including KS-1 |
| DFARS 252.204-7019 and 252.204-7020 | **Yes** | A current SP 800-171 DoD Assessment for each covered system must be in SPRS. Two entries: CEE and MOZ (CAGE codes of 6 sites) and KS-1 (its own CAGE code) |
| DFARS 252.204-7021 and 32 CFR Part 170 (Level 2) | **Yes** | In contracts awarded from 2025-11-10, most at Level 2 (C3PAO). Final Level 2 (C3PAO) since 2026-03-20; annual affirmation due 2027-03-20 (32 CFR 170.22). As a prime, the company must flow down CMMC requirements and confirm supplier status (252.204-7021(f); 32 CFR 170.23). CMMC Phase 2 is suspended; under DoD Class Deviation 2026-O0025, Revision 3, contracting officers remove these CMMC requirements by modification before the next option period or at the next scheduled administrative modification; until then the clauses stand. |
| CMMC Level 3 | **Yes, for the Program H bid** | A DoD requiring activity has said the Program H solicitation will require Level 3 (DIBCAC). Final Level 2 (C3PAO) with a maximum score on the Level 3 scope is a prerequisite (32 CFR 170.18(a); 170.24). The DoD (Department of War) CIO memorandum of 2026-07-13 suspends CMMC Phase 2, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self), so this requirement is suspended under DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5). The company keeps preparing, because SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies |
| FAR 52.204-21 | **Yes** | FCI in ERP and corporate systems |
| FAR 52.204-25 | **Yes** | Reporting duty if covered telecommunications equipment is found |
| ITAR and EAR | **Yes** | DDTC registrant; ITAR technical data on military programs; EAR technology on commercial programs; 90 foreign-person employees under deemed-export licenses |
| NISPOM (32 CFR Part 117) | **Yes, at FL-1** | Facility clearance for Program K; stand-alone classified system. Only cyber-relevant duties are analyzed |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant |
| State breach and data security laws | **Yes** | Employee personal information in 6 states plus remote staff. The law of each state where affected individuals reside applies; Florida is the worked example |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25; nothing required yet |
| SP 800-171 Rev. 3 | **Not required** | CMMC Level 2 is fixed to Rev. 2 (32 CFR 170.14(c)(3)); each row names its Rev. 3 counterpart for planning |

**Scope.** The 110 Level 2 rows cover the CMMC Assessment Scope "CEE and MOZ" at 7 sites, with the `gap_sites` column showing which site drives each gap. AZ-1 joined the scope on 2026-05-18 and has not yet been covered by a certification assessment. The `ks1_legacy_status` column scores the KS-1 legacy environment separately, because KS-1 holds CUI under DFARS 252.204-7012 but is outside the certified scope.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. New DoD awards under DFARS Part 240 replace DFARS 252.204-7019 and -7020 with 252.240-7997, which covers DoD-led Medium and High assessments; the rows for 7019 and 7020 still describe the contracts awarded before that change. See `00_company-facts.md`.

## 2. Method
1. **Decompose.** The 110 Level 2 rows follow the official structure of NIST SP 800-171 Rev. 2 (families 3.1 to 3.14), with the CMMC identifier and point value from the CMMC Scoring Methodology (32 CFR 170.24). The 24 Level 3 rows quote table 1 to 32 CFR 170.14(c)(4) (public domain). Clause and regulation rows cite each paragraph as checked on eCFR (version date 2026-09-23); SEC rows follow 17 CFR 229.106 and the SEC's Item 1.05 compliance guide.
2. **Crosswalk.** Level 2 rows map to CSF 2.0 and SP 800-53 Rev. 5 through NIST's official mappings via each requirement's SP 800-171 Rev. 3 counterpart (the route through Rev. 3 is the author's). Level 3 and clause rows are author mappings, labeled in `crosswalk_source`.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); smaller populations used 25 to 40 items; configuration and account data were checked in full with analytics; visitor logs were stratified by site. **43 rows were tested by sampling or full-population analytics; 26 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. For CMMC scoring, a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)), so every Partially met Level 2 row counts as NOT MET in the score. Gaps are rated with the P01 scale; High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| NIST SP 800-171 Rev. 2 (CMMC Level 2) | 94 | 16 | 0 | 0 | 110 |
| CMMC Level 3 (selected NIST SP 800-172 requirements) | 10 | 12 | 2 | 0 | 24 |
| DFARS 252.204-7012 (C-DIB-R01) | 7 | 3 | 0 | 0 | 10 |
| DFARS 252.204-7019 and 252.204-7020 (C-DIB-R03) | 1 | 2 | 0 | 0 | 3 |
| DFARS 252.204-7021 and 32 CFR Part 170 (C-DIB-R02) | 2 | 4 | 1 | 0 | 7 |
| FAR 52.204-21 (C-DIB-R04) | 1 | 0 | 0 | 0 | 1 |
| FAR 52.204-25 | 1 | 0 | 0 | 0 | 1 |
| ITAR (C-DIB-R05) | 1 | 1 | 0 | 0 | 2 |
| ITAR and EAR (C-DIB-R05; C-DIB-R06) | 2 | 0 | 0 | 0 | 2 |
| EAR (C-DIB-R06) | 0 | 1 | 0 | 0 | 1 |
| NISPOM 32 CFR Part 117 (C-DIB-R07) | 6 | 1 | 0 | 0 | 7 |
| SEC Form 8-K Item 1.05 | 0 | 3 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| **Total** | **133** | **44** | **3** | **0** | **180** |

**Gap risk levels across all regulations:** High 25, Moderate 20, Low 2.

### SP 800-171 Rev. 2 by family
| Family | Met | Partially met | Not met | KS-1 legacy not met |
|---|---|---|---|---|
| 3.1 Access Control | 20 | 2 | 0 | 5 |
| 3.2 Awareness and Training | 2 | 1 | 0 | 1 |
| 3.3 Audit and Accountability | 8 | 1 | 0 | 3 |
| 3.4 Configuration Management | 6 | 3 | 0 | 4 |
| 3.5 Identification and Authentication | 11 | 0 | 0 | 3 |
| 3.6 Incident Response | 3 | 0 | 0 | 0 |
| 3.7 Maintenance | 5 | 1 | 0 | 1 |
| 3.8 Media Protection | 7 | 2 | 0 | 3 |
| 3.9 Personnel Security | 1 | 1 | 0 | 0 |
| 3.10 Physical Protection | 4 | 2 | 0 | 0 |
| 3.11 Risk Assessment | 2 | 1 | 0 | 1 |
| 3.12 Security Assessment | 4 | 0 | 0 | 3 |
| 3.13 System and Communications Protection | 15 | 1 | 0 | 3 |
| 3.14 System and Information Integrity | 6 | 1 | 0 | 2 |
| **Total (110)** | **94** | **16** | **0** | **29** |

### Scores under 32 CFR 170.24
| Scope | Requirements NOT MET | Points subtracted | Score |
|---|---|---|---|
| Six certified sites (FL-1, FL-2, FL-3, GA-1, AL-1, TX-1) | 10 | 30 | **80** |
| Full CMMC Assessment Scope including AZ-1 | 16 | 60 | **50** |
| KS-1 legacy environment (outside the certified scope) | 29 | 124 | **-14** (SPRS shows 72 from 2025-01-28) |

**What the scores mean.**
- **Final Level 2 (C3PAO) status stands** until 2029-03-20, but DFARS 252.204-7021 defines a current status as one with no changes in compliance since the status date and an annual affirmation of continuous compliance. The COO cannot affirm on 2027-03-20 while 10 requirements are NOT MET in the certified sites. All must be closed and verified by 2027-02-28.
- **No CMMC POA&M route.** If a C3PAO assessed today, the score of 80 would be below the 88 needed for Conditional status (score / 110 of at least 0.8, 32 CFR 170.21(a)(2)(i)); 11 open requirements are worth more than 1 point; and 3.10.3, 3.10.4 can never be on a POA&M (170.21(a)(2)(iii)).
- **KS-1** must not be used for any contract that includes DFARS 252.204-7021, and its SPRS entry must be corrected (G-145).

### CMMC Level 3 readiness
| Item | Value |
|---|---|
| Requirements met | 10 of 24 |
| Partially met / Not met | 12 / 2 |
| Score today (1 point each, 32 CFR 170.24) | 10 of 24 (0.42); Conditional Level 3 needs at least 0.8 (170.21(a)(3)(i)) |
| Open requirements that can never be on a Level 3 POA&M (170.21(a)(3)(ii)) | RA.L3-3.11.4e, RA.L3-3.11.6e, RA.L3-3.11.7e, SI.L3-3.14.3e |
| Prerequisite | Final Level 2 (C3PAO) with the maximum score on the Level 3 scope (170.18(a); 170.24) |

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-001 | SP 800-171 Rev. 2 3.1.1 | 2 of 60 sampled separations were disabled late (4 and 9 business days), both contractor accounts whose separation notices arrived by email | Contractor separations fed from the supplier labor system; daily reconciliation of contractor rosters; 30-day review of contractor accounts | Director of Identity and Access Management | 2026-12-15 |
| G-003 | SP 800-171 Rev. 2 3.1.3 | 14 PLM project folders migrated from a legacy vault in 2026-04 lacked the ITAR attribute; an EAR-licensed foreign-person engineer opened 3 files in one of them (found 2026-08-11, access removed the same day) | Attribute check on every folder migration; weekly analytics comparing folder attributes with export classifications; access recertification for all 90 foreign-person employees | PLM Platform Manager | 2026-11-30 |
| G-035 | SP 800-171 Rev. 2 3.4.1 | No documented baseline for the 24 AZ-1 build-prep workstations, which were installed from the printer manufacturer image | Document and apply the engineering workstation baseline with printer software exceptions; add to configuration scanning | Director of Endpoint Engineering | 2026-12-15 |
| G-036 | SP 800-171 Rev. 2 3.4.2 | AZ-1 build-prep workstations do not meet the security configuration benchmark (local administrator rights, unneeded services) | As 3.4.1 | Director of Endpoint Engineering | 2026-12-15 |
| G-062 | SP 800-171 Rev. 2 3.7.5 | One printer manufacturer at AZ-1 connects through its own remote support tool without company MFA or session recording | Move the manufacturer to the PAM vendor gateway; block the tool at the AZ-1 firewall | Director of OT Engineering | 2026-11-15 |
| G-074 | SP 800-171 Rev. 2 3.9.2 | Same as 3.1.1: 2 contractor separations disabled late | As 3.1.1 | Chief Human Resources Officer | 2026-12-15 |
| G-077 | SP 800-171 Rev. 2 3.10.3 | At TX-1, 2 of 10 sampled visitors had no escort recorded in CUI areas (cannot be on a CMMC POA&M) | Escort assignment required at check-in; daily reconciliation by site security; refresher for TX-1 hosts | Director of Corporate Security | 2026-10-31 |
| G-078 | SP 800-171 Rev. 2 3.10.4 | At TX-1, 2 of 10 sampled visitor entries had no sign-out (cannot be on a CMMC POA&M) | As 3.10.3 | Director of Corporate Security | 2026-10-31 |
| G-088 | SP 800-171 Rev. 2 3.13.1 | At AZ-1, the build-prep workstation and printer segment was reachable from the corporate network over file-sharing ports | Move AZ-1 build-prep workstations and printers into an isolated MOZ segment with deny-by-default rules | Director of Network Engineering | 2026-12-15 |
| G-112 | 32 CFR 170.14(c)(4), table 1: AC.L3-3.1.3e | AZ-1 and FL-3 move files between domains by USB and file shares; no secure transfer solution there | Close in the Level 3 readiness program; see POAM-021 | Director of Network Engineering | 2027-03-31 |
| G-128 | 32 CFR 170.14(c)(4), table 1: RA.L3-3.11.6e | Supplier CMMC status verified for 176 of 380 CUI suppliers; no response playbook for component supply chain events | Close in the Level 3 readiness program; see POAM-023 | Director, CMMC Program Office | 2027-03-31 |
| G-129 | 32 CFR 170.14(c)(4), table 1: RA.L3-3.11.7e | The plan does not cover system components and IT or OT services; no annual update rule | Close in the Level 3 readiness program; see POAM-023 | Director, CMMC Program Office | 2027-03-31 |
| G-130 | 32 CFR 170.14(c)(4), table 1: CA.L3-3.12.1e | No penetration test of the CEE since 2025-06-12 | Close in the Level 3 readiness program; see POAM-013 | Director, CMMC Program Office | 2026-12-15 |
| G-133 | 32 CFR 170.14(c)(4), table 1: SI.L3-3.14.3e | AZ-1 printers share a segment reachable from the corporate network (cannot be on a Level 3 POA&M) | Close in the Level 3 readiness program; see POAM-005 | Director of OT Engineering | 2026-12-15 |
| G-135 | 252.204-7012(b)(1) and (b)(2)(i) | KS-1 legacy environment does not provide adequate security for the CUI it holds | Interim MFA, SIEM forwarding, and daily offsite backups at KS-1; migrate KS-1 CUI into the CEE and MOZ | Vice President, Integration Management Office | 2027-03-31 |
| G-143 | 252.204-7012(m)(1) | 4 of 60 sampled purchase orders that released CUI lacked the clause (manual purchase orders) | ERP blocks release of a CUI-flagged purchase order without the clause set; review open manual orders | Vice President, Supply Chain | 2026-12-31 |
| G-145 | 252.204-7019(b); 252.204-7020(d) | KS-1 SPRS entry overstates implementation | Post a corrected KS-1 score with a date to reach 110 | Director, CMMC Program Office | 2026-10-31 |
| G-148 | 252.204-7021(d)(1) and (d)(2) | 1 of 30 sampled work orders for 7021 contracts was routed to KS-1 for a secondary operation (2026-08), with the drawing on the KS-1 legacy MES | Hard block in ERP and MES routing; contract review; report to the contracting officer if counsel advises | Vice President, Contracts | 2026-10-31 |
| G-150 | 252.204-7021(d)(4) and (f)(2); 32 CFR 170.23 | 176 of 380 CUI suppliers (46%) verified at the required level | Verify all; block CUI release in the gateway to unverified suppliers; supplier outreach and sessions | Vice President, Supply Chain | 2027-01-31 |
| G-152 | 252.204-7021(f)(1) | Same 4 manual purchase orders lacked the clause set | As G-143 | Vice President, Supply Chain | 2026-12-31 |
| G-154 | 32 CFR 170.18(a) and 170.19(d) | Level 3 scope not decided; Level 2 score today 80 in the certified sites | Scope decision 2026-12-15; Level 2 assessment of the expanded scope 2027-05; DIBCAC request 2027-06 | Director, CMMC Program Office | 2026-12-15 |
| G-158 | 22 CFR 120.56 (release) with technology control plans | 14 migrated folders lacked the ITAR attribute; an EAR-licensed foreign-person engineer opened 3 ITAR files | Migration attribute check; weekly analytics; foreign-person access recertification | Vice President, Trade Compliance | 2026-11-30 |
| G-160 | 15 CFR 734.13(a)(2) | The same engineer reached technical data that his EAR license does not cover (an ITAR folder) | As G-158 | Vice President, Trade Compliance | 2026-11-30 |
| G-169 | Form 8-K Item 1.05; SEC Release 33-11216 | No data-theft scenario; no step to keep CUI, export-controlled, or classified details out of the filing | Update the playbook; tabletop 2026-11-19 with a CUI theft scenario | General Counsel | 2026-11-30 |
| G-170 | Form 8-K Item 1.05 (materiality determination) | Qualitative factors for loss of program data (customer trust, program eligibility) not in the worksheet | Add defense-specific factors to the worksheet | General Counsel | 2026-11-30 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | TX-1 visitor escort fix (POAM-003); ERP and MES routing block for 7021 work (POAM-020); corrected KS-1 SPRS score; PLM export attribute fix and foreign-person access recertification (POAM-002); ITAR full disclosure (due 2026-10-18); privileged training enforcement (POAM-011); reportability field (POAM-017); materiality playbook and tabletop 2026-11-19 (POAM-019); contractor separations feed (POAM-001); AZ-1 logging and remote access fixes (POAM-008, POAM-012); Level 3 scope decision (2026-12-15); AZ-1 segmentation and baselines (POAM-004, POAM-005); CEE penetration test (POAM-013) | 3.10.3, 3.10.4, 3.1.1, 3.1.3, 3.2.2, 3.3.1, 3.4.1, 3.4.2, 3.7.5, 3.13.1; 252.204-7021(d)(2); 252.204-7019; 22 CFR 120.56, 127.12; Item 1.05 | Visitor reconciliations; routing rule test; SPRS record; attribute analytics; tabletop report; segmentation test; penetration test report |
| 2027 Q1 | Supplier CMMC verification complete and gateway block (POAM-018); KS-1 migration complete (POAM-020); USB replacement at AZ-1 (POAM-006); vulnerability SLA recovery (POAM-009); readiness re-check of all 110 requirements in February; **annual affirmation 2027-03-20**; Level 3 items in POAM-014, POAM-015, POAM-016, POAM-021 to POAM-023 | 252.204-7012(m), 252.204-7021(f), 32 CFR 170.22, 170.23; 3.8.7, 3.11.3, 3.14.1; Level 3 requirements | Supplier status report; migration closure; readiness report; affirmation |
| 2027 Q2 | Level 2 assessment of the expanded scope (AZ-1 and KS-1), target 2027-05-03 to 2027-05-14; DIBCAC Level 3 request in June | 32 CFR 170.17, 170.18, 170.19 | C3PAO findings report |
| 2027 Q3 | Level 3 assessment window 2027-08-02 to 2027-08-13; annual risk and gap reassessment | 32 CFR 170.18 | DIBCAC findings report; updated P01 and P03 |

## 6. Pending regulatory changes
- **FAR CUI rule:** proposed (90 FR 4278, 2025-01-15), not final. DFARS 252.204-7012 remains the governing clause.
- **Revolutionary FAR Overhaul:** proposed rule (91 FR 37550, 2026-06-23) may renumber FAR clauses, including 52.204-21 and 52.204-25. Not final.
- **SP 800-171 Rev. 3:** published by NIST, but CMMC Level 2 is fixed to Rev. 2 (32 CFR 170.14(c)(3)). Rev. 3 is not treated as a current obligation.
- **CIRCIA:** final rule not published as of 2026-09-25; proposed reporting deadlines are not current obligations.
- **SEC:** no SEC proposal to amend or rescind Item 1.05 or Item 106 was found as of 2026-09-25.

## 7. Regulator-ready package
The CMMC Program Office keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a C3PAO or DIBCAC assessment, a DCMA DIBCAC assessment under DFARS 252.204-7020, a DCSA security review, a DDTC or BIS inquiry, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the CEE and MOZ SSPs (P02), P01 risk register, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- SPRS records, CMMC certificates and UIDs, and affirmation evidence packs;
- the cryptography register and the cloud provider CRM;
- the DIBNet submission log, the voluntary disclosure file, and NISPOM self-inspection reports;
- records kept for at least 6 years (POL-01).

## 8. Approval
Approved by the Director, CMMC Program Office and the CISO on 2026-08-21. The roadmap was reviewed by the risk and technology committee of the board on 2026-09-10. Next reassessment: readiness re-check in February 2027, full reassessment June to July 2027.

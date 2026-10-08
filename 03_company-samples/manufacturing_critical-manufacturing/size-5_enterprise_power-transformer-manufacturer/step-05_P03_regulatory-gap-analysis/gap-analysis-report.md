# Regulatory Gap Analysis: Cris Santos Company | Critical Manufacturing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded power and distribution transformer manufacturer; plants in FL, GA, TN, TX, NC, and OH) |
| Tier / Vertical | Enterprise / Critical Manufacturing (NAICS 335311) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, February 26, 2024), as a full profile of all 106 subcategories, with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (September 2023) as the OT implementation guide. **Voluntary**: no binding sector-wide cyber rule applies |
| Binding obligations analyzed | SEC Form 8-K Item 1.05 and Reg S-K Item 106; FAR 52.204-21, -23, -25, and -30 (11 civilian federal contracts); the Supplier Cyber Security Addenda in 88 utility contracts (flow-down of NERC CIP-013-2 R1 Part 1.2); DOE certification and records rules for distribution transformers (10 CFR 429.47, 429.71); EAR recordkeeping and screening; state breach and data security laws (Florida worked example) |
| Applicability checked | CIRCIA (proposed), ICTS connected vehicles rule, DFARS 252.204-7012, NERC CIP-013-2 direct applicability |
| Sources read | eCFR (version 2026-09-23) for 17 CFR 229.106, FAR 4.1903, 4.2306, 52.204-21, -23, -25, -30, 10 CFR 429.47 and 429.71, and 15 CFR 762.6 and 744.11; CIRCIA NPRM (89 FR 23644) and the Federal Register API (2026-10-05); the CIP-013-2 and CIP-013-3 pages on nerc.com; the SP 800-82 Rev. 3 PDF and the SP 800-82 Rev. 4 draft page on csrc.nist.gov; Fla. Stat. 501.171 |
| Assessment dates | 2026-06-01 to 2026-07-31 (plant walkthroughs 2026-06-08 to 2026-06-26; evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer, the Director of OT Security, and the Director of Federal Programs; sampling reperformed by Internal Audit for 8 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| NIST CSF 2.0 with SP 800-82 Rev. 3 | **Benchmark (voluntary)** | Critical manufacturing has no binding sector-wide cyber rule. CSF 2.0 is the language utilities use in supplier questionnaires and the basis of the P08 runbook (SP 800-61 Rev. 3 is a CSF 2.0 Community Profile); SP 800-82 Rev. 3 supplies OT guidance |
| SEC Form 8-K Item 1.05 and Reg S-K Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company. Item 106 text checked on eCFR (17 CFR 229.106(b), (c), (d)) |
| FAR 52.204-21 | **Yes** | FAR 4.1903 prescribes the clause when a contractor may have FCI residing in or transiting through its information system. The 11 civilian contracts are built to agency specifications (not COTS), and FCI sits in the ERP and labeled project sites |
| FAR 52.204-25 and 52.204-23 | **Yes** | In all 11 contracts. Clocks: covered telecommunications within 1 business day, then 10 business days (52.204-25(d)); Kaspersky covered articles within 3 business days, then 10 business days (52.204-23(c)) |
| FAR 52.204-30 | **Yes, in 8 contracts** | Prescribed at FAR 4.2306(c) and included in the 8 contracts awarded since 2024. SAM.gov review at least once every three months (c)(1); reports within 3 business days, then 10 business days ((c)(4)) |
| Utility Supplier Cyber Security Addenda | **Yes, by contract** | 88 utilities have added addenda that turn the six topics of CIP-013-2 R1 Part 1.2 into contract duties. The deadlines (24 or 48 hours for incident notice, 1 business day for access revocation, 30 days for vulnerability disclosure) are contract terms, not NERC requirements |
| NERC CIP-013-2 (direct) | **No** | Applies to the Responsible Entities in its section 4.1. The company is not NERC-registered. CIP-013-2 is "Mandatory Subject to Enforcement" (effective 2022-10-01); CIP-013-3 is "Subject to Future Enforcement" (FERC order 2026-03-19; effective date 2028-07-01) |
| DOE certification and records (10 CFR 429.47, 429.71) | **Yes, for distribution transformers** | Distribution transformers are covered equipment. Efficiency is certified by testing (429.47), and certification reports and underlying test data must be kept, indexed for DOE review, for 2 years after a model is discontinued (429.71). Analyzed because the records live in the test systems and TDMS |
| EAR (C-CRITICAL-MFG-R03) | **Yes, narrowly** | EAR99 exports (about 9% of revenue). Cyber-relevant duties: 5-year record retention (15 CFR 762.6(a)) and screening against the Entity List (Supplement No. 4 to 15 CFR Part 744) |
| CIRCIA (C-CRITICAL-MFG-R01) | **Not in force** | Proposed rule only; no final rule in the Federal Register as of 2026-10-05. If finalized as proposed, the company would be covered twice over: it exceeds the SBA size standard (800 employees for NAICS 335311) and proposed 226.2(b)(3) reaches electrical equipment manufacturing (NAICS subsector 335) regardless of size |
| ICTS connected vehicles rule (C-CRITICAL-MFG-R02) | **No** | No connected vehicles or vehicle systems |
| DFARS 252.204-7012 (C-CRITICAL-MFG-R04) | **No** | No DoD contracts or subcontracts; the bid review gate declined a flow-down request in 2026-04. If the board approves a CUI enclave in 2027, NIST SP 800-171 and CMMC become the binding target for that enclave |
| State breach and data security laws | **Yes** | Employee and applicant personal information in at least 6 states. The law of each state where affected individuals reside applies; Florida (Fla. Stat. 501.171) is the worked example |
| SOX Section 404 | Separate program | IT general controls over the ERP, HR, and payroll are tested by the SOX program and not repeated here |

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Decompose.**
   - CSF rows use the subcategory text from `00_universal-framework/frameworks/csf2_core.csv`, plus the SP 800-82 Rev. 3 section that gives OT guidance. SP 800-82 Rev. 3 Section 6 is organized by CSF 1.1 categories, so it is cited by **section number only** and CSF 2.0 IDs are used for the outcomes.
   - Regulation rows follow the official structure: CFR sections and paragraphs, FAR clause paragraphs (brief quotes of public-domain text), Form 8-K Item 1.05, and the addendum sections, each tied to its CIP-013-2 Part.
2. **Crosswalk.** CSF rows use the **official** NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`); where only part of a long mapping is listed, the `crosswalk_source` column says "subset." All other rows are **author mappings**, labeled as such.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and populations under 250 used 25 to 40 items; configuration and account data were checked in full with analytics; small populations (for example the 41 access-revocation notices) were tested in full. Selections were random. **35 rows were tested by sampling or full-population analytics; 22 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| CSF 2.0 Govern (with SP 800-82 Rev. 3) | 25 | 6 | 0 | 0 | 31 |
| CSF 2.0 Identify | 10 | 11 | 0 | 0 | 21 |
| CSF 2.0 Protect | 8 | 14 | 0 | 0 | 22 |
| CSF 2.0 Detect | 5 | 6 | 0 | 0 | 11 |
| CSF 2.0 Respond | 9 | 4 | 0 | 0 | 13 |
| CSF 2.0 Recover | 7 | 1 | 0 | 0 | 8 |
| **Subtotal CSF 2.0 profile** | **64** | **42** | **0** | **0** | **106** |
| FAR 52.204-21 (applicability, (b)(1)(i)-(xv), (c)) | 16 | 1 | 0 | 0 | 17 |
| FAR 52.204-25 | 1 | 0 | 0 | 0 | 1 |
| FAR 52.204-23 | 1 | 0 | 0 | 0 | 1 |
| FAR 52.204-30 | 1 | 1 | 0 | 0 | 2 |
| Utility addenda (CIP-013-2 R1.2 flow-down) | 2 | 4 | 0 | 0 | 6 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| DOE certification and records | 1 | 2 | 0 | 0 | 3 |
| EAR (C-CRITICAL-MFG-R03) | 1 | 1 | 0 | 0 | 2 |
| Direct applicability: CIP-013-2, CIRCIA, ICTS, DFARS | 0 | 0 | 0 | 4 | 4 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| **Total** | **96** | **54** | **0** | **4** | **154** |

**Gap risk levels across all regulations (54 partially met rows):** High 18, Moderate 31, Low 5.
- CSF profile: 13 High, 26 Moderate, 3 Low.
- Binding rules: 5 High (3 utility addenda, 2 SEC Form 8-K), 5 Moderate (FAR 52.204-21(c), FAR 52.204-30(c)(1), utility addendum sec. 5, and two DOE records rows), 2 Low (EAR screening at AQ-01; Florida third-party agent notice terms in AQ-01 contracts).

**Reading the results.** No requirement is wholly Not met; the program is mature. The gaps cluster in four places: the acquired Ohio plant, OT recovery and legacy assets, the customer-facing duties in the utility addenda, and disclosure readiness for a production outage. The federal contract safeguards are in good shape (16 of 17 rows Met), because FCI is kept in the ERP and labeled project sites, away from the plant floor and AQ-01.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-003 | CSF GV.OC-03 | 12 AQ-01 addenda not loaded; register does not flag the 27 addenda with 24-hour notice terms | Load contracts; deadline fields and clocks (POAM-016) | Chief Compliance Officer | 2026-12-31 |
| G-038 | CSF ID.AM-08 | 148 HMIs and engineering workstations and 37 MES kiosks on unsupported operating systems | Compensating controls for every asset; funded refresh (POAM-009) | Vice President, Manufacturing Engineering | 2027-06-30 |
| G-046 | CSF ID.RA-08 | 1 of 9 disclosures sent on day 38; SBOMs for 61% of releases | Disclosure tracker; SBOM for every release (POAM-019) | Director of Product Security | 2027-03-31 |
| G-047 | CSF ID.RA-09 | Contract manufacturer boot firmware not verified at final test | Verify boot images; SBOM requests (POAM-018; POAM-019) | Chief Technology Officer | 2027-03-31 |
| G-052 | CSF ID.IM-04 | Materiality procedure lacks a production-loss method; runbook mixes 24-hour and 48-hour terms | Update procedure and runbook (POAM-011; POAM-016) | General Counsel | 2026-11-30 |
| G-053 | CSF PR.AA-01 | OEM default passwords on 5 drying oven HMI web interfaces | Change passwords; commissioning check (POAM-012) | Vice President, Manufacturing Engineering | 2026-10-31 |
| G-055 | CSF PR.AA-03 | AQ-01 cellular routers without MFA; supplier MFA gaps | Gateway at AQ-01 (POAM-008); supplier MFA (POAM-002) | Director of OT Security | 2027-03-31 |
| G-064 | CSF PR.DS-11 | Controller restores tested at 2 of 7 plants; P3 MES backup incomplete | Restore tests; fix jobs (POAM-007) | Vice President, Manufacturing Engineering | 2027-06-30 |
| G-066 | CSF PR.PS-02 | Late critical patches; unsupported OT software | POAM-013; POAM-009 | Director of Security Operations | 2027-06-30 |
| G-071 | CSF PR.IR-01 | AQ-01 flat OT network, dual-homed MES, two-way trust | Remove trust; OT DMZ (POAM-004) | Vice President, Integration Management Office | 2027-03-31 |
| G-073 | CSF PR.IR-03 | ERP failover 11 h against an 8 h RTO | Automate failover (POAM-006) | Vice President, Enterprise Applications | 2027-01-31 |
| G-094 | CSF RS.AN-08 | No production-loss estimate for materiality | Calculator from P05 values (POAM-011) | CFO | 2026-11-30 |
| G-095 | CSF RS.CO-02 | 3 of 41 access notices late | POAM-016 | Chief Compliance Officer | 2026-12-31 |
| G-128 | Addendum sec. 1 (CIP-013-2 R1.2.1) | Single 48-hour clock; 4 of 30 sampled entries wrong | Per-utility clocks (POAM-016) | Chief Compliance Officer | 2026-12-31 |
| G-130 | Addendum sec. 3 (CIP-013-2 R1.2.3) | 3 of 41 notices after 1 business day | Automatic HR task (POAM-016) | Vice President, Spares and Services | 2026-12-31 |
| G-131 | Addendum sec. 4 (CIP-013-2 R1.2.4) | 1 of 9 disclosures on day 38 | Tracker with day-20 escalation (POAM-019) | Director of Product Security | 2026-12-31 |
| G-134 | Form 8-K Item 1.05 | Playbook exercised only on an IT breach; 2 new members | OT ransomware tabletop 2026-11-18 (POAM-011) | General Counsel | 2026-11-30 |
| G-135 | Form 8-K Item 1.05 (materiality determination) | No method for lost production and liquidated damages | Calculator (POAM-011) | CFO | 2026-11-30 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Disclosure committee OT tabletop and procedure update (POAM-011); per-utility notice clocks and AQ-01 contracts in the register (POAM-016); HMI default passwords changed (POAM-012); separation-of-duties conflicts removed and change workflow (POAM-003); AQ-01 identity federation (POAM-001); OT alerts to the 24x7 SOC (POAM-005); FASCSA review with backup owner (POAM-021); 2 subcontracts amended (G-123) | SEC Item 1.05; addendum secs. 1, 3, 4; FAR 52.204-21(c), 52.204-30(c)(1); CSF GV.OC-03, PR.AA-01, PR.AA-05, DE.AE-06 | Tabletop report; register exports; OEM change records; workflow configuration; SOC routing rules |
| 2027 Q1 | ERP failover retest at 8 hours (POAM-006); AQ-01 OT DMZ, gateway, and sensor (POAM-004, POAM-008, POAM-015); contract manufacturer assessed and boot image verification (POAM-018); SBOM for every release (POAM-019); AQ-01 DOE records in the TDMS (POAM-022); spare yard monitoring (POAM-023); Internal Audit test of Item 106 statements | CSF PR.IR-01, PR.IR-03, ID.RA-09, ID.RA-08; addendum sec. 5; 10 CFR 429.71; Item 106 | DR retest report; firewall and gateway records; assessment report; SBOM archive; TDMS index |
| 2027 Q2 | Controller restore tests at all 7 plants (POAM-007); OT refresh wave 1 (POAM-009); AQ-01 onto the enterprise ERP and MES (2027-06-30) | CSF PR.DS-11, RC.RP-02, ID.AM-08; EAR screening at AQ-01 | Restore test records; refresh records; migration sign-off |
| 2027 Q3 | Annual risk analysis and gap reassessment; check the status of CIRCIA, SP 800-82 Rev. 4, CIP-013-3 addendum revisions, and the FAR overhaul | All | Updated P01 and P03 |

## 6. Pending regulatory changes (none treated as current obligations)
- **CIRCIA** (C-CRITICAL-MFG-R01): no final rule in the Federal Register as of 2026-10-05 (the latest CIRCIA documents are the May 2026 town hall notice and the August 2026 Unified Agenda). If the proposed scope survives, the company would owe reports to CISA within 72 hours of a reasonable belief that a covered cyber incident occurred and within 24 hours of a ransom payment. The runbook already includes a voluntary CISA report (P01 R-060).
- **NIST SP 800-82 Rev. 4** is an initial public draft (published 2026-09-21; comments due 2026-11-30). Rev. 3 remains the final guide used here; update the section references in G-001 to G-106 when Rev. 4 is final.
- **CIP-013-3** takes effect 2028-07-01 for registered entities. Expect revised addenda from the 88 utilities before then.
- **FAR overhaul.** The Revolutionary FAR Overhaul proposed rule (FR Doc. 2026-12559, June 23, 2026) would move the information security clauses into FAR part 40, with 52.204-21 becoming 52.240-5. It is proposed only; the company follows the clauses in its awarded contracts and checks each new solicitation or modification.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-10-05, so Item 1.05 and Item 106 remain in force.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to an SEC comment letter, a contracting officer's request, a DOE records request, a BIS inquiry, or a utility's supplier audit under its addendum:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and notification matrix;
- the obligations register export (88 addenda, federal clauses, EAR, DOE), the 2026 notice log, and the PSIRT disclosure log;
- FAR 52.204-25 inquiry records and the 2025 contracting officer reports, and the FASCSA review log;
- DOE certification files and the TDMS index;
- Item 106 support file (board and committee minutes, program descriptions, assessor reports).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.

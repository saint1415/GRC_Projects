# Regulatory Gap Analysis: Cris Santos Company Holdings | Dams | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Dams (focus division: Cris Santos Hydro) |
| Primary program analyzed | FERC Division of Dam Safety and Inspections, *FERC Security Program for Hydropower Projects*, Revision 3A (March 30, 2016), applied to a fleet with **6 Group 1, 23 Group 2, and 50 Group 3 dams**. Source: https://www.ferc.gov/sites/default/files/2020-04/security.pdf |
| Also for Hydro | 18 CFR Part 12 (eCFR version 2026-09-23); NERC CIP-002-5.1a to CIP-013-2 for a medium and low impact Generator Owner and Generator Operator; EOP-004-4; Form DOE-417 |
| Division regulations | Constructors: DFARS 252.204-7012, the CMMC Program (32 CFR Part 170) with NIST SP 800-171 Rev. 2, and FAR 52.204-21, -23, -25, -30. Engineering: client contract and CEII duties, Part 12 independence rules, and its share of the federal contract clauses |
| Group-wide | SEC Reg S-K Item 106 and Form 8-K Item 1.05; state breach notification laws (Florida worked example); OFAC; CIRCIA (proposed, tracked only) |
| Gap tables | `gap-analysis.csv` (Hydro, 124 rows); `gap-analysis-constructors.csv` (39 rows); `gap-analysis-engineering.csv` (19 rows); `gap-analysis-group.csv` (9 rows) |
| Assessment dates | 2026-05-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-31); Section 9 determinations refreshed 2026-07-08 |
| Assessors | Division security and compliance leads, the NERC Compliance Director, the Federal Programs Compliance Director, and the Director, Hydro Security, coordinated by the Chief Compliance Officer; reviewed by group internal audit |

## 1. Applicability
### 1.1 Hydro: FERC Security Program and 18 CFR Part 12
**The Security Program applies to every Hydro project.** Hydro is a FERC licensee, and Part 12 applies to projects licensed under Part I of the Federal Power Act (12.1(a)(1)). The Security Program is D2SI guidance that FERC engineers inspect against, under the Regional Engineer's supervisory authority over project safety and security (18 CFR 12.4(b)(1)(i)).

**Duties depend on each dam's Security Group, not on company size** (Rev. 3A 3.3 and Table 3.3.8):

| Duty | Group 1 (6 dams) | Group 2 (23 dams) | Group 3 (50 dams) |
|---|---|---|---|
| Vulnerability Assessment (annual update, 5-year reprint) | Required (G-011) | Only for permanent closures (G-019) | Only for permanent closures |
| Security Assessment (annual update, 10-year reprint) | Included in the VA | Required (G-014) | Highly recommended |
| Security Plan with annual update and threat-level procedures | Required (G-015) | Required (G-015) | Highly recommended |
| Cyber/SCADA measures in the Security Plan or a separate plan | Required (G-016) | Required (G-016) | Required if remotely operated with Group 1 or 2 projects (G-018) |
| Internal Emergency Response sub-element | Required (G-008) | Required (G-008) | Not required |
| Rapid Recovery sub-element | Required (G-013) | Not required | Not required |
| Security Plan exercise | At least every 5 years (G-012) | Strongly recommended (G-017) | Not required |
| Annual Security Compliance Certification Letter by December 31 | Required (G-020 to G-022) | Required | Not required |

**Section 9 applies at the Critical level** (determination of 2026-07-08, G-034 and G-035): the HOC fleet SCADA connects powerhouses totaling more than 1,500 MW to one cyber asset (Table 9.1c note 1), and gate control at the 6 Group 1 and 17 Group 2 dams exceeds the population-at-risk thresholds (more than 60 people within 3 miles, more than 800 within 60 miles, or more than 12,500 in total). Critical assets need baseline and enhanced measures, answers to Form 3 Questions 5-33, and a plan and schedule for each negative answer (9.1.1.3). Group 3 dams operated from the HOCs follow the HOC's level (Section 9.1 note).

**Where FERC and NERC overlap.** Rev. 3A 9.4 says that where a cyber asset falls under both D2SI and NERC CIP, it must meet the CIP requirements to fulfill D2SI's criteria, and the CIP standards met should be referenced in the Security Plans. The fleet Cyber/SCADA Security Plan does this for the HOC systems (G-066).

**18 CFR 12.10** remains the binding reporting rule: a security incident (physical and/or cyber), gate misoperation, or unusual instrumentation reading is a condition affecting the safety of the project (12.3(b)(4)), reported as soon as practicable, preferably within 72 hours (12.10(a)(1)).

### 1.2 Hydro: NERC CIP
Hydro is registered as a Generator Owner and Generator Operator. 38 developments are BES generating plants under Inclusion I2 (units over 20 MVA or plants over 75 MVA, connected at 100 kV or above; NERC BES Definition Reference Document, version 3).

| CIP-002-5.1a Attachment 1 | Result |
|---|---|
| High impact (1.1 to 1.4) | **None.** Criterion 1.4 covers GOP Control Centers for assets meeting 2.1, 2.3, 2.6, or 2.9. No plant reaches 1,500 MW (2.1), no plant has been designated under 2.3 or 2.6, and Hydro owns no 2.9 scheme |
| Medium impact | **HOC-A and HOC-B** under criterion 2.11 (GOP Control Centers for 1,500 MW or more in the Eastern Interconnection) |
| Low impact | **38 BES plants** (criterion 3.3; 5 Blackstart Resources also under 3.4) |

So CIP-004 to CIP-011 and CIP-013 apply to the HOC BES Cyber Systems and their EACMS and PACS; CIP-003-9 Attachment 1 (including Section 6 vendor electronic remote access, in effect since 2026-04-01) applies to the 38 plants; CIP-012-2 applies to the ICCP links; CIP-014-3 does not apply (G-120). CIP-010-4 R2 applies only to high impact systems (G-111).

### 1.3 Constructors
Constructors holds 38 federal prime contracts. All include **FAR 52.204-21** (federal contract information) and **52.204-25**. 11 USACE contracts include **DFARS 252.204-7012**, so the systems that hold covered defense information must meet NIST SP 800-171 and report cyber incidents within 72 hours. DoD contracts above the micro-purchase threshold that involve FCI or CUI carry **CMMC** requirements under the phased rollout in 32 CFR 170.3(e); Phase 2 begins 2026-11-10. CMMC Level 2 requirements are identical to SP 800-171 Rev. 2 (32 CFR 170.14(c)(3)). Construction has no sector-specific cyber regulation, so these contract duties are the binding baseline.

When Constructors works inside a Hydro plant, **Hydro's** CIP-003-9 and FERC Section 9 duties reach its people and devices, because Hydro is the Responsible Entity and the licensee (CG-039).

### 1.4 Engineering
No sector regulator governs Engineering's security directly. Its binding duties come from **client contracts** (the DSMS security schedule; NDAs for client CEII that pass through the 18 CFR 388.113 terms), the **federal contract clauses** on its A-E contracts, and the **Part 12 independence rules** that apply through licensees (18 CFR 12.31(a)(3) to (5) and 12.65(b)). The profile for this sector names the FTC Safeguards Rule as its primary regulation, but Engineering is not a financial institution, so it does not apply (EG-016).

### 1.5 Group-wide
As an SEC registrant, the group must disclose material cybersecurity incidents on Form 8-K Item 1.05 within 4 business days after the materiality determination, and describe its program annually under Reg S-K Item 106. State breach laws apply in each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171).

## 2. Regulation-by-division matrix
| Requirement | Hydro | Constructors | Engineering | Group (corporate) |
|---|---|---|---|---|
| C-DAMS-R01 FERC Security Program Rev. 3A | **Primary.** 29 Group 1 and 2 dams with full duties; Section 9 Critical | Applies at Hydro sites through Hydro (vendor rules, training, OPSEC) | Applies to Hydro BCSI and security documents it holds; DSMS interconnection | Common controls support it (SOC, HR, training) |
| C-DAMS-R02 18 CFR 12.10 and Part 12 | **Applies.** Reporting, EAPs, gate tests, ODSP | Modifications reported by Hydro 60 days before work (12.11(b)(2)) | Independence rules: no 12D or ODSP audit work for Hydro (12.31, 12.65) | Not applicable |
| C-DAMS-R03 NERC CIP | **Applies.** Medium (HOCs) and low (38 plants); CIP-012 | Applies to its devices and remote access at Hydro BES plants (CIP-003-9 Att. 1 Sec. 5.2 and 6) | Applies to BCSI it receives (CIP-011-3; CIP-004-7 R6) | Supports PRAs, training, SOC |
| NERC EOP-004-4; DOE-417 | Applies (GO and GOP) | Not applicable | Not applicable | Not applicable |
| N23-R03 DFARS 252.204-7012 | Not applicable (no federal contracts) | **Applies** (11 USACE contracts) | **Applies** (14 USACE A-E contracts) | Hosts the FPE; SOC supports 72-hour reports |
| N23-R04 CMMC (32 CFR 170) and SP 800-171 Rev. 2 | Not applicable | **Applies.** Level 2 required; score 74 | **Applies** within the same FPE scope | Common controls inherited by the FPE |
| N23-R01 / N54-R04 FAR 52.204-21; N23-R02 FAR 52.204-25 | Not applicable | **Applies** (38 contracts) | **Applies** (20 A-E contracts) | Group procurement supports |
| FAR 52.204-23 and 52.204-30 | Not applicable | Applies where included | Applies where included | Group software blocklist |
| N54-R01 FTC Safeguards Rule; N54-R02 IRC 7216; N54-R06 HIPAA | Not applicable | Not applicable | Not applicable (no financial, tax, or PHI services) | Not applicable |
| Client contracts and CEII NDAs | Offtaker and ICCP agreements | Owner contracts; client facility security details | **Primary.** DSMS security schedule; SOC 2 at renewal; CEII NDAs | Intercompany terms missing (GG-008) |
| SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Employee and recreation customer data | Crew badging and payroll data | Client user contact data | Coordinates (Florida worked example) |
| CIRCIA (proposed 6 CFR Part 226) | Tracked only | Tracked only | Tracked only | Tracked only (not in effect) |

## 3. Method
1. **Requirements.** Hydro rows follow the Security Program's own structure (section 3.2 responsibilities, the group duties in 3.3 and Table 3.3.8, sections 4, 6, 7, and 8, each line of Tables 9.3a and 9.3b, Form 3 items not covered by those lines, and three Form 1 items), then 18 CFR Part 12 by section, then each applicable CIP requirement (at requirement or part level), then EOP-004-4 and Form DOE-417. Constructors rows follow the DFARS clause paragraphs, the CMMC rule sections, the SP 800-171 Rev. 2 requirements where evidence differed from the enclave baseline (23 rows covering the families most affected), and the FAR clauses. FERC documents, eCFR text, and NIST publications are U.S. government works; NERC standards are cited by requirement number with short summaries in our own words.
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **These are author mappings.** NIST has published no mapping for the FERC program or NERC CIP. For SP 800-171 Rev. 2 rows the mapping is informed by the official NIST CSF 2.0 to SP 800-171 Rev. 3 crosswalk in `00_universal-framework/crosswalks/`.
3. **Evidence.** Interviews, document review (Security Plans, VAs, SAs, certification letters, CIP evidence, the FPE SSP and SPRS record, DSMS contracts), configuration exports, site walkthroughs at HOC-A, DEV-02, DEV-05, and 2 jobsites (2026-07-13 to 2026-07-17), and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 4. Results
### 4.1 Hydro (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FERC Sec. 3 Requirements and responsibilities | 11 | 7 | 0 | 1 | 19 |
| FERC Sec. 4 Threat notification and communications | 3 | 0 | 0 | 0 | 3 |
| FERC Sec. 6 Security Assessment | 1 | 0 | 0 | 0 | 1 |
| FERC Sec. 7 Security Plan | 4 | 3 | 0 | 0 | 7 |
| FERC Sec. 8 Annual certification letter | 2 | 1 | 0 | 0 | 3 |
| FERC Sec. 9 and Form 3 Computer security and SCADA | 15 | 18 | 0 | 0 | 33 |
| FERC Appendix A Form 1 | 1 | 2 | 0 | 0 | 3 |
| 18 CFR Part 12 | 9 | 1 | 0 | 0 | 10 |
| NERC CIP | 32 | 7 | 0 | 3 | 42 |
| NERC EOP-004-4 and Form DOE-417 | 3 | 0 | 0 | 0 | 3 |
| **Total** | **81** | **39** | **0** | **4** | **124** |

Of the 39 partially met rows, **15 are High**, 22 Moderate, and 2 Low.

**The pattern.** The program is mature where it was designed: the HOCs meet every applicable medium impact CIP requirement except four rows (BCSI copies outside the library under CIP-004-7 R6 and CIP-011-3 R1, a recovery plan update still pending under CIP-009-6 R3, and one OEM renewal that skipped the CIP-013-2 steps), and the physical security, reporting, EAP, and certification duties are met across the fleet. The gaps sit **below the HOCs** and **where other divisions touch Hydro**:
- **Constructors inside Hydro plants:** commissioning kits bypassed the Intermediate Systems and were not treated as third-party Transient Cyber Assets or vendor remote access (G-053, G-067, G-085 to G-087). Because 3 of the affected plants are BES plants, this is a **potential noncompliance with CIP-003-9 Attachment 1 Sections 3, 5, and 6**, self-reported to SERC on 2026-09-30.
- **Engineering's DSMS:** two-way replication at 17 plants breaks segregation (G-051), and dam safety practice now leans on AI-001 alerts without an ODSP review (G-002, G-077).
- **Scale below the HOC:** OT monitoring at 14 of 41 plants (G-057), vulnerability assessments overdue at 15 plants (G-056), legacy hosts (G-046), and stale PLC backups (G-048).
- **Statements to FERC:** the 2025 certification letters reported Section 9 status for the HOC only (G-021). Plans and schedules for plant-level negative Form 3 answers went to the Regional Engineers on 2026-09-30 (G-036).

### 4.2 Constructors (`gap-analysis-constructors.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| DFARS 252.204-7012 | 2 | 5 | 0 | 0 | 7 |
| CMMC Program (32 CFR Part 170) | 1 | 2 | 1 | 0 | 4 |
| NIST SP 800-171 Rev. 2 (selected) | 16 | 5 | 2 | 0 | 23 |
| FAR 52.204-21, -23, -25, -30 | 2 | 2 | 0 | 0 | 4 |
| Hydro OT rules at Hydro sites | 0 | 0 | 1 | 0 | 1 |
| **Total** | **21** | **14** | **4** | **0** | **39** |

Of the 18 unmet or partially met rows, 10 are High and 8 Moderate.

**Not met:** the Conditional status test in 32 CFR 170.21(a)(2) (score 74, or 0.67 of 110, against the 0.8 minimum; and 3.12.4 and 3.10.3 to 3.10.5, which may not be on a POA&M, are open); CUI flow control (3.1.3), because CUI was found in 6 of 20 sampled USACE folders on the commercial project platform; physical controls at the 31 jobsite trailers that print CUI drawings (3.10.3 to 3.10.5); and Hydro's third-party rules at Hydro sites (CG-039). **The enclave itself is sound**: MFA, FIPS-validated encryption, logging, and boundary rows are all met. The problem is CUI that left it, and an SSP boundary that does not match where CUI goes (3.12.4).

### 4.3 Engineering (`gap-analysis-engineering.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| DSMS client contract commitments | 3 | 2 | 2 | 0 | 7 |
| Client CEII and confidentiality | 0 | 2 | 0 | 0 | 2 |
| 18 CFR Part 12 independence rules | 2 | 0 | 0 | 0 | 2 |
| Federal A-E contracts | 2 | 1 | 0 | 0 | 3 |
| Other obligations checked | 0 | 2 | 0 | 3 | 5 |
| **Total** | **7** | **7** | **2** | **3** | **19** |

**Not met:** clients must be told before material changes to alerting logic, but thresholds and AI-001 versions change without notice or change records (EG-005); and 23 renewals in 2027 require a SOC 2 Type 2 report that does not exist yet (EG-006; P09).

### 4.4 Group-wide (`gap-analysis-group.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| SEC cybersecurity disclosure | 2 | 1 | 0 | 0 | 3 |
| State breach notification (Florida worked example) | 0 | 2 | 0 | 0 | 2 |
| Other group-wide obligations | 1 | 1 | 1 | 1 | 4 |
| **Total** | **3** | **4** | **1** | **1** | **9** |

**Not met:** there are no written intercompany terms for the DSMS service to Hydro or for Constructors' work inside Hydro plants (GG-008). That single gap explains much of what the division tables found.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Construction connectivity into Hydro OT (1) | Hydro, Constructors | Rev. 3A Table 9.3a; Form 3 Q12; CIP-003-9 Att. 1 Sec. 3, 5, 6 | High | Commissioning standard; kit EDR; affiliates treated as vendors; SERC mitigation plan | Group CISO; NERC Compliance Director | 2026-12-31 |
| 2 | Plans and schedules and accurate Section 9 statements to FERC | Hydro | Rev. 3A 8.0, 9.1.1.3 | High | Letters sent 2026-09-30; full status in the 2026 certification letters | Director, Hydro Security | 2026-12-31 |
| 3 | DSMS two-way path and missing intercompany terms (3) | Hydro, Engineering | Table 9.3a segregation; CA-3 | High | One-way transfer at 17 plants; intercompany agreement | Director, OT Security; General Counsel | 2027-03-31 |
| 4 | CUI outside the enclave and CMMC status (5) | Constructors, Engineering | 252.204-7012(b); 32 CFR 170.21 | High | Purge CUI; trailers out of scope or controlled; SSP rewrite; score of at least 88 before 2027-03-15 | Federal Programs Compliance Director | 2027-03-15 |
| 5 | Monitoring, vulnerability assessment, and legacy OT below the HOC (2, 4) | Hydro | Table 9.3a, 9.3b; Form 3 Q14, Q15 | High | Sensors at 41 plants; 15 plant assessments; HMI and workstation replacement | Director, OT Security | 2027-12-31 |
| 6 | AI-001 reliance and DSMS change control (6, 10) | Hydro, Engineering | Rev. 3A 3.2; 18 CFR 12.64; client contracts | High | Weekly manual readings restored; change control with client notice; ODSP review | Chief Dam Safety Engineer; DSMS General Manager | 2026-12-31 |
| 7 | Multi-regulator notification not exercised (8) | All | CIP-008-6 R4; 12.10; 252.204-7012(c); Form 8-K Item 1.05; state laws | Moderate | Complete the matrix with the state appendix; tabletop 2026-11-17 | General Counsel | 2026-12-15 |
| 8 | Affiliate handling of BCSI and CEII (7) | All | CIP-011-3 R1; CIP-004-7 R6; client NDAs | Moderate | Restricted libraries; NDA and authorization for affiliate staff | Director, Hydro Security | 2026-12-31 |
| 9 | Supplier terms for the OEM and affiliates (9) | Hydro | CIP-013-2 R2; Form 3 Q32 | Moderate | Contract amendment; supplier assessments | Chief Procurement Officer | 2027-03-31 |
| 10 | DSMS SOC 2 report | Engineering | Client renewal terms | Moderate | Type 1 as of 2027-03-31, then Type 2 | DSMS General Manager | 2027-09-30 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). The plan and schedule that Section 9.1.1.3 asks for is the P07 POA&M filtered to the Section 9 rows.

## 6. Pending regulatory changes
- **FERC Security Program:** Revision 3A is the latest version this analysis could confirm on ferc.gov; the program page refused automated access, so a newer revision could not be ruled out. The Director, Hydro Security confirms the current revision with the Regional Engineers before each inspection.
- **NERC CIP:** the virtualization revisions (CIP-002-8, CIP-003-10, CIP-004-8, CIP-005-8, CIP-006-7.1, CIP-007-7.1, CIP-008-7.1, CIP-009-7.1, CIP-010-5, CIP-011-4.1, CIP-013-3) take effect 2028-07-01; CIP-015-1 (internal network security monitoring for high and medium impact systems) takes effect 2028-10-01 and CIP-015-2 on 2029-10-01; CIP-003-11 on 2029-07-01. HOC sensors already monitor inside both ESPs (G-121).
- **CMMC:** Phase 3 begins 2027-11-10 and Phase 4 (full implementation) 2028-11-10 (32 CFR 170.3(e)).
- **FAR:** the proposed FAR overhaul (FR Doc. 2026-12559, 2026-06-23) would move information security clauses into FAR Part 40 and require SP 800-171 Rev. 3 for CUI. It is proposed only.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226): no final rule as of 2026-09-25. If finalized as proposed, the group would likely be covered. Not treated as a current obligation (GG-007).

The `pending_rule_change` column records these per row. None of them is treated as a current obligation.

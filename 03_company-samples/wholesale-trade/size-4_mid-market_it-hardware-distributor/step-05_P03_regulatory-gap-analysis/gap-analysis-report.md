# Regulatory Gap Analysis: Cris Santos Company | Wholesale Trade | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed IT hardware and software wholesale distributor) |
| Tier / Vertical | Mid-Market / Wholesale Trade |
| Primary regulation | NIST SP 800-171 Rev. 2 (110 requirements), required by DFARS 252.204-7012(b)(2) and assessed under CMMC Level 2 (32 CFR 170.14(c)(3)), scoped to the CMMC Level 2 assessment scope |
| Secondary (same business line) | FAR 52.204-21 (15 requirements, CMMC Level 1) for the FCI stream; supply chain and reporting clauses in the subcontracts: FAR 52.204-25 (Section 889), FAR 52.204-30 (FASCSA orders), DFARS 252.246-7008, the 12 system criteria of DFARS 252.246-7007(c), and the DFARS 252.204-7012, -7019/-7020, and -7021 clause duties |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | Security Manager and the GRC analyst with the Director of Federal Programs and the Director of Quality and Product Compliance; reviewed by the vCISO and the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-17 |
| Workbook | `gap-analysis.csv` (155 rows) |

## 1. Applicability
**Primary business line:** distribution and configuration of IT hardware and software, including the federal channel (about 18% of revenue), which is where the binding cybersecurity rules come from. No sector-wide federal cybersecurity rule applies to wholesale trade; the obligations below are contract clauses that flow down from DoD prime contracts.

| Regulation | Applies? | Basis |
|---|---|---|
| DFARS 252.204-7012 and NIST SP 800-171 Rev. 2 | **Yes** | The Prime A, B, and C subcontracts contain the clause, and performance involves covered defense information (CUI configuration documents). Paragraph (b)(2) requires SP 800-171 on every covered contractor information system. No size exemption |
| CMMC Level 2 (C3PAO), 32 CFR Part 170 and DFARS 252.204-7021 | **Yes, from 2027-06-01** | CMMC applies to subcontractors at all tiers that process, store, or transmit CUI (32 CFR 170.23(a)). Prime A and Prime B require Level 2 (C3PAO) from 2027-06-01, the minimum when the prime requires it and CUI flows down (170.23(a)(3)). Phase 2 starts 2026-11-10 (170.3(e)(2)) |
| FAR 52.204-21 and CMMC Level 1 (Self) | **Yes, for the FCI stream** | Federal channel orders with kitting, imaging, or labeling are more than COTS, so they carry the clause and DFARS 252.204-7021 at Level 1 (Self). COTS-only orders are excluded (52.204-21(c); 32 CFR 170.3(c)) |
| FAR 52.204-25 | **Yes** | In all federal channel subcontracts |
| FAR 52.204-30 (DEC 2023) | **Yes** | In the Prime A and Prime B subcontracts and 5 of 7 federal channel purchase order templates. Text verified on eCFR (2026-09-23 version). As a subcontractor, the company receives the clause without paragraph (c)(1), which paragraph (e)(1) excludes from flowdown |
| DFARS 252.246-7008 | **Yes** | In all 3 CUI subcontracts; paragraph (e) requires flowdown to suppliers of electronic parts |
| DFARS 252.246-7007 | **Yes, through Prime A** | The clause's paragraphs (a) to (e) apply to a prime only if it is subject to the Cost Accounting Standards, but paragraph (e) requires the substance of (a) to (e) to be flowed down without that introductory condition. Prime A did so in 2025, so the company must keep a counterfeit electronic part detection and avoidance system meeting the 12 criteria in (c) |

**Not applicable, with reasons:**
- SP 800-171 3.13.5 and FAR 52.204-21(b)(1)(xi): no publicly accessible components in the scope (G-101, G-121).
- DFARS 252.204-7012(m): the company shares no covered defense information with subcontractors (G-152).
- SEC disclosure rules (private company), CCPA/CPRA (no California business today), and CTPAT (voluntary). See `../00_company-facts.md` section 1.

**Other obligations and where they are handled:**
| Obligation | Where covered |
|---|---|
| FTC Act Section 5 (N42-R01) | P06 policies and P09 (accurate security statements to resellers) |
| State breach notification laws (Florida as the worked example) | P08 notification matrix |
| Title VII and 29 CFR 1607 (AI resume screening) | P10 |

## 2. Method
1. **Requirements.** The 110 requirements, their Basic or Derived type, and their text come from NIST's SP 800-171 Rev. 2 requirements dataset. CMMC practice IDs follow 32 CFR 170.14(c); point values follow the CMMC Scoring Methodology (32 CFR 170.24). The 15 FAR 52.204-21 requirements are quoted from 48 CFR 52.204-21(b)(1) and linked to their SP 800-171 equivalents per Table 2 to 32 CFR 170.15(c)(1)(ii). Clause rows follow each clause's own paragraph structure from the eCFR text (2026-09-23 version).
2. **Crosswalk.** SP 800-53 controls come from the official SP 800-171 Rev. 2 Appendix D mapping (Rev. 4 IDs), refined to Rev. 5 by the author (column `nist_official_sp800_53_appendix_d` keeps the official list). CSF 2.0 subcategories are derived from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference. Clause rows use an author mapping and are labeled as such.
3. **Scope.** The CMMC Level 2 assessment scope is the enclave, the FIL, and their security protection assets (P02 section 7), **plus every place CUI was found**. Finding CUI in the ERP, the commercial email tenant, and the Integration Center brought those into scope for this assessment.
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested, chosen at random from system-generated populations using the co-sourced internal audit firm's attribute sampling table (25 items for a frequent control; whole populations where they were small or queryable):
   - enclave accounts against approved requests: 64 of 64;
   - terminations: 25 of 214; enclave leavers: 12 of 12; transfers: 25 of 96;
   - enclave change tickets: 25 of 180;
   - federal orders queried for attachments: all 4,860 (37 with CUI);
   - item master: all 68,000 active SKUs queried for a manufacturer of record;
   - federal drop-ship orders: 20 of 310;
   - broker purchase orders: 20 of about 410;
   - FIL jobs for traceability: 15;
   - incidents: 10 of 41;
   - enclave remediation tickets: 12; corporate critical findings: 50 of 50;
   - printed sheets found in the Integration Center walkthrough: 23 of 23.
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. For CMMC scoring, Partially met counts as NOT MET (170.24), except the partial credit rules for 3.5.3 and 3.13.11. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 3.1 Access Control | 18 | 4 | 0 | 0 | 22 |
| 3.2 Awareness and Training | 1 | 1 | 1 | 0 | 3 |
| 3.3 Audit and Accountability | 6 | 3 | 0 | 0 | 9 |
| 3.4 Configuration Management | 8 | 1 | 0 | 0 | 9 |
| 3.5 Identification and Authentication | 10 | 0 | 1 | 0 | 11 |
| 3.6 Incident Response | 2 | 1 | 0 | 0 | 3 |
| 3.7 Maintenance | 6 | 0 | 0 | 0 | 6 |
| 3.8 Media Protection | 5 | 4 | 0 | 0 | 9 |
| 3.9 Personnel Security | 1 | 1 | 0 | 0 | 2 |
| 3.10 Physical Protection | 5 | 1 | 0 | 0 | 6 |
| 3.11 Risk Assessment | 1 | 2 | 0 | 0 | 3 |
| 3.12 Security Assessment | 3 | 1 | 0 | 0 | 4 |
| 3.13 System and Communications Protection | 14 | 1 | 0 | 1 | 16 |
| 3.14 System and Information Integrity | 7 | 0 | 0 | 0 | 7 |
| **SP 800-171 Rev. 2 subtotal** | **87** | **20** | **2** | **1** | **110** |
| FAR 52.204-21 (CMMC Level 1) | 12 | 2 | 0 | 1 | 15 |
| FAR 52.204-25 (Section 889) | 0 | 2 | 1 | 0 | 3 |
| FAR 52.204-30 (FASCSA orders) | 0 | 0 | 3 | 0 | 3 |
| DFARS 252.246-7008 (sources of electronic parts) | 1 | 2 | 1 | 0 | 4 |
| DFARS 252.246-7007(c) (12 system criteria) | 5 | 6 | 1 | 0 | 12 |
| DFARS 252.204-7012 clause duties | 1 | 3 | 0 | 1 | 5 |
| DFARS 252.204-7019/-7020 (SPRS) | 0 | 1 | 0 | 0 | 1 |
| DFARS 252.204-7021 (CMMC status) | 0 | 1 | 1 | 0 | 2 |
| **Total (155)** | **106** | **37** | **9** | **3** | **155** |

**Gap risk ratings (46 rows Partially met or Not met):** 18 High, 20 Moderate, 8 Low.

**SP 800-171 detail.** Of the 22 unmet or partially met requirements, 8 are Basic and 14 are Derived. By gap risk, 7 are High, 8 Moderate, and 7 Low.

**Score.** Using the CMMC Scoring Methodology (32 CFR 170.24), the 2026 score is **52 out of 110**. The 2026-01 SPRS entry of 81 was supported by a documented self-assessment of the enclave as then scoped; the drop comes mainly from CUI that spread outside the enclave after Prime C's onboarding in 2026-03, and from deeper sampling. The posted score must be corrected (G-153).

**What the score means for CMMC.** A Conditional Level 2 status with a POA&M requires a score of at least 88 (0.8 of 110) and allows only 1-point requirements on the POA&M, plus 3.13.11 when encryption is used but not FIPS-validated (32 CFR 170.21(a)(2)). Of the 22 unmet requirements:
- **12 cannot be placed on a CMMC POA&M:** 10 have a point value above 1 (3.1.1, 3.1.5, 3.2.2, 3.3.1, 3.4.1, 3.8.1, 3.8.2, 3.8.7, 3.9.2, 3.11.2), and 2 are listed in 170.21(a)(2)(iii) (3.10.3 and 3.12.4). They must be fully met before the C3PAO assessment.
- **9 are 1-point requirements** that could go on a POA&M, closed within 180 days of the Conditional status date (170.17(c)(3)).
- **1 (3.13.11)** could go on a POA&M because encryption is in place but not FIPS-validated on the FIL VPN path.
Closing only the 12 non-eligible requirements would raise the score to 98, above the 88 threshold.

**Reading the results.** The enclave itself is largely sound: identification and authentication, maintenance, system integrity, and most boundary requirements are Met. The gaps concentrate in four places:
- **CUI scope creep** (3.1.1, 3.1.3, 3.8.1, 3.8.2, 3.8.4, 3.10.3, 3.12.4; 252.204-7012(b)(2)(ii)(D));
- **enclave administration** (3.1.4, 3.1.5, 3.3.8, 3.3.9, 3.5.6, 3.9.2);
- **FIL boundary logging and FIPS mode** (3.3.1, 3.13.11; 252.204-7012(e));
- **supply chain clauses**, which are the weakest area: FASCSA searches have never been run, flowdown terms are missing, and the counterfeit avoidance system is half built.

**FAR 52.204-21.** 2 of 15 requirements are Partially met: the forecasting platform receives FCI without FAR terms (G-113), and DC-2 visitor control was incomplete until 2026-08-14 (G-119). CMMC Level 1 allows no POA&M (170.21(a)(1)), so both must be corrected and the Level 1 affirmation reviewed (G-154).

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Posted SPRS score no longer reflects the system | 252.204-7019/-7020 (G-153) | High | On counsel's advice, post a corrected Basic Assessment | Director of Federal Programs | 2026-09-30 |
| FCI to the forecasting vendor without safeguards; DC-2 visitors | 52.204-21(b)(1)(iii), (ix); 252.204-7021 (G-113, G-119, G-154) | High | Filter federal orders from the feed; keep DC-2 check-in; Affirming Official review | Chief Operating Officer | 2026-10-31 |
| No FASCSA order search or reporting | 52.204-30(b), (c) (G-129, G-130) | High | Logged SAM.gov search; screening list entry; 3-business-day procedure | Director of Federal Programs | 2026-10-31 |
| Single DIBNet certificate holder | 252.204-7012(c); 52.204-25(d) (G-127, G-149) | High | Second medium assurance certificate; drill | Director of Federal Programs | 2026-10-31 |
| CUI outside the enclave; CUI in cloud services not approved for it | 3.1.1, 3.1.3, 3.8.1, 3.8.2, 3.10.3; 252.204-7012(b)(2)(ii)(D) (G-001, G-003, G-064, G-065, G-079, G-148) | High | CUI cleanup and blocks; FIL-only printing; Prime C onboarding | Director of Federal Programs; Federal Integration Lab Manager | 2026-11-30 |
| Inventory and SSP do not match the CUI boundary | 3.4.1, 3.12.4 (no POA&M allowed for 3.12.4) | High | Add FIL network devices and asset categories; update the SSP after cleanup | Director of Information Technology | 2026-11-30 |
| No inspection at DC-2; counterfeit avoidance system incomplete | 252.246-7007(c)(2), (6), (7); 252.246-7008(b) (G-137, G-141, G-142, G-132) | High | DC-2 inspection and quarantine; test lab; broker reassessments | Director of Quality and Product Compliance; Vice President of Supply Chain | 2026-12-31 |
| Covered-equipment screening holes | 52.204-25(b)(1) (G-126) | High | Manufacturer of record for all SKUs; drop-ship screening | Director of Federal Programs | 2026-12-15 |
| FIL firewall logs kept 30 days; enclave log history | 3.3.1; 252.204-7012(e) (G-020, G-151) | High | Forward FIL firewall logs; archive enclave history | Security Manager | 2026-12-31 |
| Role-based training; insider threat | 3.2.2, 3.2.3 | High | Administrator and Integration Center modules; insider threat content | HR Director | 2026-12-31 |
| Enclave administration and leaver removal | 3.1.5, 3.9.2, 3.5.6, 3.1.4, 3.3.8, 3.3.9 | Moderate | Access broker for the enclave; automated disable; audit role separation | Security Manager; Director of Information Technology | 2027-01-31 |
| Removable media on 3 FIL workstations; scanning frequency | 3.8.7, 3.11.2 | Moderate | Restore device control; monthly enclave scans | Security Manager | 2026-10-31 |
| No flowdown of supply chain clauses to suppliers | 52.204-25(e); 52.204-30(e); 252.246-7008(e); 252.246-7007(c)(9) (G-128, G-131, G-135, G-144) | Moderate | Purchase order terms and supplier acknowledgment | General Counsel | 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**Sequence.** Legal exposure first (SPRS correction, Level 1 items, FASCSA, DIBNet certificate), then the 12 requirements that cannot go on a CMMC POA&M, then the 1-point items. Target: a self-assessed score of at least 88, with only POA&M-eligible items open, by 2027-01-31; readiness review in 2027-02; C3PAO assessment in 2027-03, ahead of the 2027-06-01 requirement.

## 5. How this connects to the other deliverables
- **P02:** the SSP control statements carry the same gaps; the DOP SSP serves as the SP 800-171 3.12.4 plan with this workbook.
- **P07:** the assessment tested the controls behind the High gaps (AC-3, SA-9, SR-5, SR-10, SR-11, IR-6, AU-11, SC-13, MP-7).
- **P08:** the reporting rows (G-127, G-130, G-149, G-150, G-151) set the clocks in the notification matrix.

## 6. Pending regulatory changes
These are **proposed** and are not treated as current obligations. The `pending_rule_change` column flags the affected rows.

- **FAR overhaul, parts 1, 2, 4, 33, 39, 40, 52, and 53** (FR Doc. 2026-12559, 91 FR 37550, 2026-06-23; comments closed 2026-07-23). If finalized as proposed:
  - A new FAR 52.240-7 clause for CUI would require **NIST SP 800-171 Rev. 3** with DoD organization-defined parameters. Rev. 3 adds a Supply Chain Risk Management family (03.17), which the C-SCRM plan should anticipate (G-081).
  - CUI incidents would be reported within **72 hours of discovery** across agencies (G-149, G-055).
  - A new FAR 52.240-3 would consolidate the security prohibitions, including Section 889 and FASCSA orders, and standardize reporting to **72 hours from discovery** with one required report (G-126, G-127, G-129, G-130).
- **FAR prohibition on certain semiconductor products and services** (proposed rule, 91 FR 7223, 2026-02-17; comments closed 2026-04-20). For a hardware distributor this would add another screening list alongside Section 889 and FASCSA orders, effective 2027-12-23 if finalized as proposed. Not tied to a row; the C-SCRM plan (SR-2) tracks it.
- **DFARS printed circuit board acquisition restrictions** (advance notice of proposed rulemaking, DFARS Case 2022-D011, 91 FR 40508, 2026-07-02). No proposed rule text exists yet.
- A Federal Register search on 2026-09-25 found no proposed rule that would change DFARS 252.204-7012 itself or 32 CFR 170. CMMC Phase 2 (2026-11-10) is already scheduled in 32 CFR 170.3(e) and is treated as current.

# Regulatory Gap Analysis: Cris Santos Company Holdings | Commercial Facilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Commercial Facilities (focus division: Commercial Property, NAICS 531120) |
| Primary benchmark (focus division) | CISA Cross-Sector Cybersecurity Performance Goals, Version 2.0 (CPG 2.0), December 2025 (C-COMMERCIAL-FACILITIES-R05). **Voluntary.** Tailored for OT with NIST SP 800-82 Rev. 3 |
| Binding standards and law (focus division) | PCI DSS v4.0.1, SAQ P2PE requirements (C-COMMERCIAL-FACILITIES-R01, by contract); FTC Act Section 5 (C-COMMERCIAL-FACILITIES-R02); state reasonable-security and disposal laws (Florida worked example) |
| Division regulations | Construction: FAR 52.204-21, CMMC (32 CFR Part 170; DFARS 252.204-7021), FAR 52.204-25, DFARS 252.204-7012. Hotels: PCI DSS v4.0.1 (Report on Compliance), FTC Act Section 5, 16 CFR Part 464, 16 CFR 682.3, state lodging and disposal laws |
| Group-wide | SEC Reg S-K Item 106 and Form 8-K Item 1.05; CCPA/CPRA and the 2026 CPPA regulations; state breach notification laws; OFAC; CIRCIA (proposed, tracked) |
| Gap tables | `gap-analysis.csv` (Commercial Property, 59 rows); `gap-analysis-construction.csv` (38 rows); `gap-analysis-hotels.csv` (75 rows); `gap-analysis-group.csv` (11 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads with the Group OT security lead, the Construction director of federal contracts compliance, the Hotels payment security lead, and group counsel; reviewed by group internal audit |

## 1. Applicability
### 1.1 What the vertical names, and what binds each division
**No mandatory sector-specific cybersecurity regulation exists for commercial facilities.** The vertical overlay names the CISA CPGs, with PCI DSS for payment environments. At this size more rules bind the group through its other divisions, its public listing, and its customers:

| Candidate | Applies? | Reason |
|---|---|---|
| CISA CPG 2.0 (R05) | **Voluntary** | CPG 2.0 says the goals are not mandated by CISA and are meant to be adopted voluntarily, with no size tiers. The board risk committee adopted CPG 2.0 as the group OT baseline in January 2026, alongside the 2025 OT standard based on SP 800-82 Rev. 3. A CPG gap is **not** a compliance violation |
| PCI DSS v4.0.1 (R01; N72-R01) | **Yes, by contract** | Commercial Property is a merchant for event and amenity payments (about 41,000 transactions a year) and validates on SAQ P2PE. Hotels runs about 14 million card transactions a year; its acquirer requires an annual Report on Compliance by a QSA. Validation methods are set by the acquirer and card brands, not by PCI SSC. Parking revenue belongs to the contracted parking operator, which is merchant of record |
| FTC Act Section 5 (R02; N72-R02) | **Yes** | No size threshold. Reaches unreasonable security and misleading statements, including about biometric and analytics features |
| State reasonable-security, disposal, and breach laws | **Yes** | The group holds personal information of residents of many states (badge holders, visitors, guests, employees). Florida worked example: Fla. Stat. 501.171(2) (reasonable measures), (8) (disposal), (3)-(6) (notice, P08) |
| SEC disclosure (R04) | **Yes** | Exchange Act registrant. Reg S-K Item 106 annually; Form 8-K Item 1.05 within 4 business days after a materiality determination |
| CCPA/CPRA and 2026 CPPA regulations (R03) | **Yes** | The group does business in California (2 hotels) and its revenue exceeds the CPI-adjusted $26,625,000 threshold. It processed personal information of about 280,000 California consumers in 2025, so the cybersecurity audit rule (Cal. Code Regs. tit. 11, 7120) applies; with 2026 revenue over $100 million, the first audit report is due 2028-04-01. The ADMT rules apply to the hiring screening tool for California applicants (compliance by 2027-01-01) |
| CIRCIA (R06) | **No (proposed rule only)** | No final rule as of 2026-09-25. As proposed, the group would be covered under the size-based criterion because it exceeds its SBA size standard. Voluntary reporting to CISA is already group practice |
| FAR 52.204-21, CMMC, FAR 52.204-25, DFARS 252.204-7012 (N23-R01 to R04) | **Yes, Construction only** | 118 federal awards; CUI on 9 DoD contracts; 7 awards since 2025-11-10 carry DFARS 252.204-7021. No size exemption in any of them |
| 16 CFR Part 464 (fees) and 16 CFR 682.3 (disposal) | **Yes, Hotels** | Short-term lodging is a covered service (464.1). The group obtains background reports on applicants (682.3) |
| Florida Digital Bill of Rights | **No** | The group exceeds the $1 billion revenue test, but a "controller" must also meet one of the criteria in Fla. Stat. 501.702 (50% or more of revenue from online advertising, a consumer smart speaker and voice command service, or an app store with at least 250,000 applications), and the group meets none (definition verified on flsenate.gov 2026-10-06). The group still treats face templates as biometric data under 501.171 (P10) |

**Decision.** The binding rules for the focus division (state "reasonable measures", FTC Section 5) do not say what reasonable security is for building OT. The group therefore uses CPG 2.0, the Sector Risk Management Agency's own baseline, tailored with SP 800-82 Rev. 3, to define it. CPG rows are rated like requirements so the roadmap can show gaps, but a CPG gap is a risk, not a violation. PCI DSS, federal contract clauses, SEC rules, and the CPPA regulations are binding and are rated as such.

### 1.2 CPG 2.0 version and structure (verified)
The CPG 2.0 report (*Cross-Sector Cybersecurity Performance Goals, Version 2.0*, December 2025) replaces CPG 1.0.1, adds a GOVERN function aligned with NIST CSF 2.0, and has **34 goals** in six functions: 1 Govern (1.A-1.E), 2 Identify (2.A-2.E), 3 Protect (3.A-3.S), 4 Detect (4.A-4.B), 5 Respond (5.A-5.B), 6 Recover (6.A). The OT-only goals of v1.0.1 were folded into universal goals with "OT:" guidance lines, which this analysis used. The structure was verified on cisa.gov for the Small sample in this vertical and reused here.

### 1.3 Why the focus division's rows are group rows too
The Commercial Property division does not run its building systems alone. The BAACS (P02) is a corporate system, and the BTI unit in Construction services it. So most CPG rows describe group controls as they apply at Commercial Property sites, with hotel sites noted where they differ. Hotel building OT is covered by the same group plan (P01 HO-004).

## 2. Regulation-by-division matrix
| Requirement | Commercial Property | Construction | Hotels | Group (corporate) |
|---|---|---|---|---|
| R05 CISA CPG 2.0 (voluntary) | **Primary benchmark** for building OT and IT | Adopted for BTI tools and jobsite networks (not assessed row by row here) | Adopted for hotel building OT through the BAACS | Group OT standard; board adoption |
| R01 / N72-R01 PCI DSS v4.0.1 | Applies: SAQ P2PE (22 rows) | Not applicable (no card acceptance) | **Primary**: Report on Compliance (67 rows) | Common controls support both assessments |
| R02 / N72-R02 FTC Act Section 5 | Applies: analytics and biometric notices | Applies (general) | Applies: Wyndham-type practices; 16 CFR Part 464 fees | Applies |
| State reasonable security, disposal, breach | Applies (badge holders, visitors) | Applies (employees, subcontractor staff) | Applies (guests); Florida lodging register 509.101(2) | Matrix owner (P08) |
| N23-R01 FAR 52.204-21 and N23-R04 CMMC | Not applicable | **Primary**: Level 1 (Self) for SYS-D3; Level 2 (Self) for SYS-D4 | Not applicable | Director of federal contracts compliance sits in Construction |
| N23-R02 FAR 52.204-25 (Section 889) | Indirect: covered cameras found in 2 group buildings | **Applies**: delivery to the Government and own use | Not applicable | Group-wide product ban |
| N23-R03 DFARS 252.204-7012 | Not applicable | **Applies**: CUI on 9 DoD contracts; 72-hour reporting | Not applicable | SOC supports reporting |
| R04 SEC Item 106 and Item 1.05 | Via group | Via group | Via group | **Applies** (registrant) |
| R03 CCPA/CPRA and CPPA regulations | Limited (no California properties) | Limited (California applicants only if hired there) | **Applies** (2 California hotels; hiring ADMT) | Cyber audit (first report 2028-04-01) |
| R06 CIRCIA | Proposed only | Proposed only | Proposed only | Tracked |
| OFAC | Via group | Via group | Via group | Applies (POL-03) |
| SOC 2 (customer demand) | Third-party management service line (P09) | Not in scope (P09) | Not in scope (P09) | Common controls carved in |

## 3. Method
1. **Requirements.**
   - **CPG rows** are the 34 goals at goal level, citing the goal ID. Summaries paraphrase each goal and its OT line.
   - **PCI DSS rows** are listed by requirement number with short topic labels written for these analyses. PCI DSS is copyrighted, so its text is not reproduced; read the official standard. Commercial Property uses the eligibility statement and the 21 requirements in the v4.0.1 SAQ P2PE. Hotels uses the 12 principal requirements by requirement group, plus 3 defined requirements that drive scope (3.3.1, 6.4.3, 11.6.1) and the appendices.
   - **Federal clauses** (FAR, DFARS) and **32 CFR Part 170** were read from the eCFR (current through 2026-09-23). FAR 52.204-21 rows quote the clause's own text, split as in 32 CFR 170.15.
   - **Other rows**: Reg S-K Item 106 from the eCFR; CPPA regulations from the approved regulation text as summarized in `00_universal-framework/cross-sector/us-cross-sector-obligations.md`; state laws from the Florida Legislature's 2026 statutes.
2. **Crosswalk.**
   - CPG rows use the CSF 2.0 references published in CPG 2.0, with an SP 800-53 subset selected by the author from those references. For goal 3.O the author mapping (PR.DS-11; CP-9, CP-4, CP-10) is used and labeled.
   - FAR 52.204-21 rows follow the official chain (32 CFR 170.15 Table 2 to SP 800-171 R2, then NIST's CSF 2.0 to SP 800-171 Rev. 3 mapping).
   - All other rows carry an **author mapping**, labeled in `crosswalk_source`.
3. **Evidence.** Interviews, document review, configuration exports, site walkthroughs (12 properties, 6 hotels, 4 jobsites), the 2026-07-21 mailbox search, the 2026-07-23 card data discovery scan, the 2026-07-29 CUI discovery scan, the 2026-08-04 external exposure scan, contract samples, and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps are rated on the P01 risk scale.

## 4. Results
### 4.1 Commercial Property (`gap-analysis.csv`)
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| CPG 2.0 Govern (1.A-1.E) | 5 | 2 | 3 | 0 | 0 |
| CPG 2.0 Identify (2.A-2.E) | 5 | 1 | 4 | 0 | 0 |
| CPG 2.0 Protect (3.A-3.S) | 19 | 5 | 14 | 0 | 0 |
| CPG 2.0 Detect (4.A-4.B) | 2 | 0 | 2 | 0 | 0 |
| CPG 2.0 Respond (5.A-5.B) | 2 | 0 | 2 | 0 | 0 |
| CPG 2.0 Recover (6.A) | 1 | 0 | 1 | 0 | 0 |
| **CPG 2.0 subtotal** | **34** | **8** | **26** | **0** | **0** |
| PCI DSS v4.0.1 SAQ P2PE (eligibility plus 21 requirements) | 22 | 13 | 8 | 0 | 1 |
| Legal baseline (15 U.S.C. 45(a); state reasonable security and disposal) | 3 | 0 | 3 | 0 | 0 |
| **Total** | **59** | **21** | **37** | **0** | **1** |

The 37 partially met rows break down by gap risk as 4 High, 22 Moderate, and 11 Low. All four High gaps are CPG goals: **1.E** (managed service provider risk: the integrator), **3.F** (MFA: the legacy remote tools), **3.I** (segmentation), and **3.O** (backups and restoration).

**The pattern.** No goal is wholly unmet, because the group's IT program reaches most of them. But 26 of 34 goals are only partly met, and almost every shortfall is the same story: **the control exists at corporate and at segmented sites, and stops at the other buildings.** The OT standard is applied to new buildings and renovations. The 81 older properties and most hotels are waiting for segmentation, and while they wait, they have legacy remote tools, local shared accounts, unmonitored logs, and site programs outside group backup.

**PCI DSS findings are about paper and email, not systems,** as in the Small sample. The P2PE terminals keep card data out of group systems, but 6 emails with card numbers were found in 2 event mailboxes, which puts SAQ P2PE eligibility at risk until purged and blocked (G-035).

### 4.2 Construction (`gap-analysis-construction.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| FAR 52.204-21 (17 requirement rows plus (b)(2) and (c)) | 14 | 5 | 0 | 0 | 19 |
| CMMC program duties (32 CFR Part 170; DFARS 252.204-7021) | 1 | 5 | 2 | 0 | 8 |
| FAR 52.204-25 Section 889 | 2 | 3 | 0 | 0 | 5 |
| DFARS 252.204-7012 | 3 | 3 | 0 | 0 | 6 |
| **Total** | **20** | **16** | **2** | **0** | **38** |

Of the 18 rows with gaps, 4 are High, 13 Moderate, and 1 Low.

**Not met (2):** CUI on a system without the required CMMC status (CN-G-024: CUI drawings for 2 DoD client facilities were found in the BTI repository, SYS-D5), and no CMMC Level 2 (C3PAO) assessment scheduled for DoD solicitations that may require one (CN-G-027). CMMC Phase 2 (planned for 2026-11-10) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13, so the assessment is a voluntary choice. A program office may still require a specific CMMC level (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)).

**The cross-division link.** The BTI unit is part of Construction but works mainly for the other two divisions. Its repository received CUI from federal projects because BTI technicians install security systems at DoD client facilities and copied the drawings they needed into the tool they use for every building. This puts federal contract duties (DFARS 252.204-7012(b)(2) and (c)) on a tool the group's building platform depends on. It is why a BAACS incident in P08 has a DoD reporting branch.

**Level 1 status depends on a requirement now not fully met.** About 5,200 external users from closed projects remain active in SYS-D3 (CN-G-001). Level 1 requires every requirement MET, with no POA&M (32 CFR 170.21(a)(1)). Counsel is deciding by 2026-10-31 whether the January affirmation needs updating (CN-G-023).

### 4.3 Hotels (`gap-analysis-hotels.csv`)
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 3 | 2 | 0 | 0 | 5 |
| PCI Req 2 Secure configurations | 2 | 1 | 0 | 0 | 3 |
| PCI Req 3 Stored account data | 2 | 4 | 1 | 0 | 7 |
| PCI Req 4 Transmission | 2 | 0 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 4 | 0 | 0 | 0 | 4 |
| PCI Req 6 Secure systems and software | 4 | 2 | 0 | 0 | 6 |
| PCI Req 7 Restrict access | 2 | 1 | 0 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 4 | 2 | 0 | 0 | 6 |
| PCI Req 9 Physical access and devices | 5 | 0 | 0 | 0 | 5 |
| PCI Req 10 Logging | 6 | 1 | 0 | 0 | 7 |
| PCI Req 11 Security testing | 4 | 2 | 0 | 0 | 6 |
| PCI Req 12 Policies and programs | 8 | 2 | 0 | 0 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **46** | **17** | **1** | **3** | **67** |
| FTC Act Section 5, 16 CFR Part 464, 16 CFR 682.3, state lodging and disposal laws | 5 | 3 | 0 | 0 | 8 |
| **Total** | **51** | **20** | **1** | **3** | **75** |

Of the 21 rows with gaps, 4 are High, 15 Moderate, and 2 Low.

**The 74 hotels on the cloud PMS are in good shape; the 14 acquired hotels are not.** Almost every PCI gap traces to the legacy PMS at the 14 hotels acquired in 2025 (full card display, stored card numbers with the key on the same server, shared accounts, an unsupported version) or to the 6 hotels where segmentation tests failed. **Not met (1):** full card numbers displayed to every front desk user at the 14 hotels (HO-G-012, PCI 3.4).

**Fees and AI.** The booking engine shows total prices, but the guest messaging assistant and two pricing-engine channel feeds quoted base rates without the resort fee in July samples (HO-G-070, 16 CFR 464.2(a)-(b); P10).

### 4.4 Group-wide obligations (`gap-analysis-group.csv`)
| Obligation | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| SEC Reg S-K Item 106 and Form 8-K Item 1.05 | 3 | 2 | 0 | 0 | 5 |
| CCPA/CPRA and CPPA regulations | 0 | 2 | 1 | 0 | 3 |
| State breach notification, OFAC, CIRCIA | 1 | 1 | 0 | 1 | 3 |
| **Total** | **4** | **5** | **1** | **1** | **11** |

Of the 6 rows with gaps, 4 are Moderate and 2 Low. **Not met (1):** the CPPA ADMT rules for the hiring screening tool used for California hotel applicants, with a compliance date of 2027-01-01 (GRP-07).

### 4.5 All tables
| Table | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| Commercial Property | 59 | 21 | 37 | 0 | 1 |
| Construction | 38 | 20 | 16 | 2 | 0 |
| Hotels | 75 | 51 | 20 | 1 | 3 |
| Group-wide | 11 | 4 | 5 | 1 | 1 |
| **Total** | **183** | **96** | **78** | **4** | **5** |

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Integrator remote access and supplier oversight (1, 4) | CP, Hotels, Construction | CPG 1.E, 3.F; 1.D | High | Remove legacy remote tools; security terms in the intercompany agreement; BTI tools into the landing zone | Group OT security lead; Group General Counsel | 2026-12-31 |
| 2 | OT segmentation (1) | CP, Hotels | CPG 3.I, 3.S | High | OT zones at every owned property and hotel | Group OT security lead | 2027-12-31 |
| 3 | Site programs outside group backup (3) | CP, Hotels | CPG 3.O, 6.A | High | Export all site programs to the vault; manual procedures; multi-site restore | Group building technology director | 2027-03-31 |
| 4 | CUI outside the enclave (4) | Construction | DFARS 252.204-7012(b)(2); 252.204-7021(d)(2); 32 CFR 170.19 | High | Purge and block; intake check; counsel review of reporting and affirmations | Construction director of federal contracts compliance | 2026-11-30 |
| 5 | Legacy PMS and segmentation at hotels (5) | Hotels | PCI DSS 1.3, 3.2, 3.4, 11.4 | High | Mask now; migrate 14 hotels; fix and retest segmentation | Hotels payment security lead | 2027-03-31 |
| 6 | AI and biometrics (6) | All | 15 U.S.C. 45(a); Cal. Code Regs. tit. 11, 7200 et seq.; 16 CFR 464.2 | Moderate | Group AI program for every use case; ADMT compliance for California applicants; total price in AI channels (P10) | Group Chief Risk Officer; Group Chief Privacy Officer | 2026-12-31 |
| 7 | Cross-division notification not exercised (7) | All | Form 8-K Item 1.05; state laws; DFARS 252.204-7012(c); CPG 5.A, 5.B | Moderate | Complete the matrix with lease and owner clauses (P08); cross-division tabletop with a materiality decision | Group General Counsel | 2026-12-15 |
| 8 | OT visibility (2) | CP, Hotels | CPG 2.A, 3.Q, 4.B | Moderate | OT sensors at critical-occupancy sites; site log forwarding | Group SOC director | 2027-06-30 |
| 9 | CMMC Level 2 (C3PAO) readiness | Construction | 32 CFR 170.17; 170.3(e) | Moderate | Schedule a C3PAO assessment after the boundary fix | Construction director of federal contracts compliance | 2027-03-31 |
| 10 | SAQ P2PE eligibility | CP | SAQ P2PE eligibility; PCI DSS 3.3.1.2 | Moderate | Purge and block card data in email; stop paper capture | Commercial Property controller | 2026-10-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). The POA&M `source` column cites the P03 row behind each item.

**Before signing the 2026 SAQ P2PE:** close G-035 and G-038 and record the acquirer's confirmation. **Before the 2026 Report on Compliance fieldwork:** mask card display at the 14 hotels (HO-G-012) and retest segmentation at the 6 hotels (HO-G-052).

## 6. Pending regulatory changes
None of these is treated as a current obligation.
- **CIRCIA:** the final rule was not published as of 2026-09-25. As proposed (89 FR 23644), the group would be covered under the size-based criterion, so the P08 matrix would add 72-hour incident and 24-hour ransom payment reports to CISA when a final rule takes effect.
- **PCI DSS:** PCI SSC ran a request for comments on v4.0.1 (June to July 2026) toward a next version. v4.0.1 remains current.
- **CMMC phase-in:** Phase 2 (planned for 2026-11-10) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13. This is in effect, not pending. Until 2028-11-09 DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self). SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). The rule text still shows Phase 3 beginning 2027-11-10 and Phase 4 beginning 2028-11-10 (32 CFR 170.3(e)). Level 2 stays tied to NIST SP 800-171 R2 (32 CFR 170.14(c)(3)).
- **Revolutionary FAR Overhaul:** a proposed rule (FR Doc. 2026-12559, 2026-06-23) would renumber FAR 52.204-21 (proposed 52.240-5) and add CUI clauses based on NIST SP 800-171 Rev. 3. Not final; affected rows are flagged in `pending_rule_change`.
- **NIST SP 800-82 Rev. 4** is an initial public draft (2026-09-21). Rev. 3 remains the final guide used here.
- **CPG 2.0** states a targeted revision cycle of 24 to 36 months.

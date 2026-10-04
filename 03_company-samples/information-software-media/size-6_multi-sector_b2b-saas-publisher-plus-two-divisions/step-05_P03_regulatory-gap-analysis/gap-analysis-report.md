# Regulatory Gap Analysis: Cris Santos Company Holdings | Information | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Information (focus division: Cloud Software) |
| Primary analysis (focus division) | SOC 2 Trust Services Criteria with FTC Act Section 5 data security expectations (15 U.S.C. 45(a)), measured against the FTC's business guidance and the division's own security and data-use commitments |
| Division analyses | Technology Consulting: FAR 52.204-21, HIPAA business associate duties, and client commitments. Payments and Payroll: FTC Safeguards Rule (16 CFR Part 314) and PCI DSS v4.0.1 for service providers, plus sponsor bank terms and the money transmission question |
| Gap tables | `gap-analysis.csv` (Cloud Software, 45 rows); `gap-analysis-technology-consulting.csv` (28 rows); `gap-analysis-payments-and-payroll.csv` (47 rows) |
| Assessment dates | 2026-08-03 to 2026-08-28, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads, the Payments and Payroll Qualified Individual, and the consulting federal contracts compliance officer, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit and outside counsel (sections 1 and 6) |

## 1. Applicability
The first question at this tier is not "what does the rule say?" but "which entity does it bind, and in what role?" The group has three legal subsidiaries with different roles toward the same data.

### 1.1 Role of each division
| Entity | Role | Basis |
|---|---|---|
| Cloud Software | **Service provider** (processor) for customer worker data; a business for its own marketing, applicant, and workforce data | Customer DPAs; Cal. Civ. Code 1798.140 (CCPA service provider and business definitions) |
| Cloud Software | **Bank service provider** to about 420 bank and credit union customers (counsel's view) | 12 CFR 53.2(b)(2) and 53.4; 225.303; 304.24 |
| Cloud Software | **Affiliate service provider** to Payments and Payroll for the payroll handoff data | 16 CFR 314.2(r) (service provider definition); 314.4(f) |
| Technology Consulting | Federal contractor holding **federal contract information** under 14 contracts | 48 CFR 52.204-21 |
| Technology Consulting | **HIPAA business associate** of 31 hospital clients | 45 CFR 160.103; 164.302 |
| Payments and Payroll | **Financial institution** under the FTC Safeguards Rule (group legal decision, 2024) | 16 CFR 314.2(h)(1); example 314.2(h)(2)(vi): "A business that regularly wires money to and from consumers is a financial institution because transferring money is a financial activity" |
| Payments and Payroll | **PCI DSS service provider** for about 26,000 merchants | Sponsor bank B agreement and card network rules (contractual, not law) |
| Holding company | **SEC registrant** | Reg S-K Item 106; Form 8-K Item 1.05 |

### 1.2 FTC Act Section 5 (focus division)
Section 5(a) declares unfair or deceptive acts or practices in or affecting commerce unlawful (15 U.S.C. 45(a)(1)). The Cloud Software division is not in any statutory carve-out, and there is no size threshold (N51-R01). As in the industry's Small sample, the requirement set is the FTC's own business guidance (Start with Security, 28 practices; Protecting Personal Information; Data Breach Response), plus every security or data-use statement the division makes publicly or by contract. A statement that is not true is a deception risk even when the control behind it is reasonable.

At this size, the unfairness test (15 U.S.C. 45(n)) carries more weight than at the Small size: the WCP holds data on about 21 million workers who cannot protect it themselves, and Social Security numbers and bank details for 2.4 million of them.

### 1.3 SOC 2 (contractual)
SOC 2 is not a law. It applies because customers require it and the MSA promises a current report. Statements in the SOC 2 system description are representations, so G-040 tests one directly. Criterion-by-criterion readiness is in P09, which reuses the `related_tsc_criteria` column.

### 1.4 FTC Safeguards Rule (Payments and Payroll)
The division regularly moves money for workers and merchants. Group legal decided in 2024 to treat it as a financial institution under 16 CFR 314.2(h) and to apply the Part 314 program to all payroll and payment data it handles, rather than parse which workers have a "customer relationship" with it under 314.2(e). The small-institution exceptions in 314.6 do not apply (customer information on far more than 5,000 consumers). The FTC notice duty in 314.4(j) applies to notification events involving at least 500 consumers, within 30 days of discovery.

**The key finding is about affiliates.** 16 CFR 314.2(r) defines a service provider as any person or entity that receives, maintains, processes, or otherwise is permitted access to customer information through its provision of services directly to a financial institution. The WCP stores the division's customer information (the handoff files) as a service to it. The division must therefore oversee the WCP like any other service provider (314.4(f)): select it with care, bind it by contract, and assess it periodically. None of that is in place (gap 5).

### 1.5 Money transmission (stated as a question, not a conclusion)
- **Federal.** Whether a person is a money transmitter is "a matter of facts and circumstances" (31 CFR 1010.100(ff)(5)(ii)). The rule excludes a person that only "acts as a payment processor to facilitate the purchase of, or payment of a bill for, a good or service through a clearance and settlement system by agreement with the creditor or seller" (1010.100(ff)(5)(ii)(B)). Card acceptance for merchants is structured to fit that limitation. The payroll funds flow (employer to worker) does not obviously fit any listed limitation.
- **State.** Each state's money transmission law has its own definitions and exemptions. Outside counsel's state-by-state review is not complete.
- **This analysis asserts no conclusion.** It records the question as an open gap (PY-G46) with a dated decision (2027-03-31) and a group risk (GR-11).

### 1.6 Technology Consulting
FAR 52.204-21 applies to the 14 federal contracts because consultants' systems hold federal contract information. None of the contracts designates CUI, and the division holds no DoD contracts, so DFARS 252.204-7012 and CMMC do not apply. The FTC Safeguards Rule does not apply: the division does not prepare tax returns or perform other financial activities (N54-R01 reaches accountants and tax preparers). HIPAA applies directly for the 31 hospital clients because the division is their business associate (N54-R06).

### 1.7 Group-wide checks
| Requirement | Result |
|---|---|
| CCPA cybersecurity audit (Cal. Code Regs. tit. 11, 7120-7121) | **Applies.** The group meets the revenue test, and in 2025 it processed personal information of more than 250,000 California consumers as a business (marketing visitors, event registrants, business contacts, applicants, and its own California workforce), which meets 7120(b)(2)(A). With 2026 revenue over $100 million, the first audit covers 2027-01-01 to 2028-01-01 and the report is due 2028-04-01 (7121(a)(1)). The audit must be done by a qualified, objective, independent professional (7122). No auditor or scope has been selected (gap 8) |
| CCPA ADMT and risk assessments | Apply to group HR's resume screening pilot (employment decisions) from 2027-01-01; Cloud Software supports customers that are CCPA businesses using attrition-risk insights (P10) |
| GLBA-covered data under the CCPA | Payments and Payroll customer information subject to GLBA is exempt from the CCPA at the data level (Civ. Code 1798.145(e)), except the 1798.150 private right of action for breaches |
| DOJ Data Security Program (28 CFR Part 202) | Applies to all divisions. The WCP and payroll engine exceed the bulk thresholds for covered personal identifiers (more than 100,000 people) and personal financial data (more than 10,000). No covered data transactions exist today; vendor screening misses ownership by covered persons (G-045, GR-17) |
| SEC Reg S-K Item 106 and Form 8-K Item 1.05 | Apply to the holding company (P08 disclosure step) |
| Bank service provider notification | Applies to Cloud Software for its bank customers (G-044); sponsor bank notice terms are contractual (PY-G47) |
| State breach notification laws | Each state where affected individuals reside; Florida worked example in P08 (Fla. Stat. 501.171) |
| Not applicable | FedRAMP (no government edition), COPPA (not child-directed), FCC CPNI rules (not a carrier), PADFA (the group is not a data broker), DFARS 252.204-7012 and CMMC (no DoD contracts), NYDFS Part 500 (no New York license) |

## 2. Regulation-by-division matrix
| Requirement | Cloud Software | Technology Consulting | Payments and Payroll | Group (corporate) |
|---|---|---|---|---|
| N51-R01 FTC Act Section 5 | **Primary.** Reasonable security and truthful statements | Applies (client-facing statements; delivery AI) | Applies (FTC also enforces Part 314) | Applies to group statements (trust center, Item 106 text) |
| SOC 2 (contractual) | **Primary.** Annual Type 2 | Out of scope (P09) | First SOC 2 planned 2027 (P09); SOC 1 Type 2 for payroll today | Group services carved in |
| N52-R03 FTC Safeguards Rule, 16 CFR Part 314 | Affiliate service provider (handoff) | Not applicable | **Primary.** Financial institution | Common controls support the program |
| PCI DSS v4.0.1 | Hosts parent pages that embed checkout (12.8 relationship) | Not applicable | **Primary (contractual).** Service provider | Common controls in the CDE responsibility matrix |
| Money transmission (31 CFR 1010.100(ff)(5); state laws) | Not applicable | Not applicable | **Open question** (counsel review) | Board informed (GR-11) |
| N54-R04 FAR 52.204-21 | Not applicable | **Primary.** 14 contracts | Not applicable | Group controls inherited (undocumented, gap 10) |
| N54-R06 HIPAA (business associate) | Not applicable (no PHI in the WCP) | **Applies.** 31 hospital clients | Not applicable | Group controls inherited |
| N54-R05 DFARS 252.204-7012 and CMMC | Not applicable | Not applicable (no DoD contracts) | Not applicable | Not applicable |
| N51-R03 CCPA and CPPA regulations | Service provider for customer data; business for own data | Business for own data | GLBA data exempt at data level (except 1798.150) | **Cybersecurity audit applies** (first period 2027) |
| N51-R04 DOJ Data Security Program | Applies (bulk identifiers and financial data) | Applies (vendor and staffing agreements) | Applies (bulk financial data) | Vendor screening |
| Bank service provider rule (12 CFR 53.4; 225.303; 304.24) | **Applies** (about 420 bank customers) | Not applicable | Sponsor bank terms by contract | Matrix (P08) |
| N51-R08 SEC Item 106 and Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Third-party agent duties to customers (Florida: notice to the covered entity within 10 days) | Same, to clients | Own notices for its customer information | Coordinates |
| N51-R07 FedRAMP; N51-R02 COPPA; N51-R06 CPNI; N51-R05 PADFA | Not applicable | Not applicable | Not applicable | Not applicable |

## 3. Method
1. **Requirements.** FTC guidance rows reuse the practice headings of the three FTC guides (U.S. government works, quoted). FAR and CFR rows were read from the eCFR (current through 2026-09-23): 48 CFR 52.204-21, 16 CFR 314.2, 314.4, and 314.6, 31 CFR 1010.100(ff)(5), 12 CFR 53.2 and 53.4, and 45 CFR 164 sections as cited. PCI DSS rows list requirement numbers with short labels in our own words, checked against the PCI SSC v4.0.1 documents; the standard's text is not reproduced.
2. **Crosswalk.** Each row maps to CSF 2.0, SP 800-53 Rev. 5, and (for the focus division) SOC 2 criterion IDs. These are **author mappings**: no official NIST mapping exists for the FTC guidance, 16 CFR Part 314, or PCI DSS to CSF 2.0. NIST maps the FAR basic safeguarding controls to SP 800-171, not to CSF 2.0.
3. **Evidence.** Interviews with each division's security, privacy, product, legal, and compliance leads; configuration exports; contract registers; the trust center and product pages captured on 2026-08-12; the 2026 PCI DSS Report on Compliance; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale. The `related_risk_ids` column links each gap to the registers.

## 4. Results
### 4.1 Cloud Software (`gap-analysis.csv`)
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FTC Start with Security (reasonable security) | 28 | 18 | 10 | 0 | 0 |
| FTC Protecting Personal Information | 2 | 0 | 2 | 0 | 0 |
| FTC Data Breach Response | 1 | 0 | 1 | 0 | 0 |
| Deception: security and data-use representations and commitments | 12 | 3 | 6 | 3 | 0 |
| Bank service provider notification | 1 | 0 | 1 | 0 | 0 |
| DOJ Data Security Program | 1 | 0 | 1 | 0 | 0 |
| **Total** | **45** | **21** | **21** | **3** | **0** |

Of the 24 rows that are not met or partially met, 8 are rated High, 14 Moderate, and 2 Low.

**The main finding.** The division's controls are strong where the FTC guidance looks first (administrative access, passwords, encryption, patching, secure development). Its gaps sit where the divisions meet: the payroll handoff files (G-002, G-010, G-014), the keys and partner roles that reach customer data from another division (G-004, G-007), and three statements that are not true today (G-034 quarterly review of all access, G-040 30-day export retention in the SOC 2 description, G-042 "bias-tested and fair"). The three Not met rows are deception risks that can be fixed quickly by correcting the statements while the controls catch up.

### 4.2 Technology Consulting (`gap-analysis-technology-consulting.csv`)
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FAR 52.204-21 ((b)(1)(i)-(xv), (b)(2), (c)) | 17 | 6 | 10 | 0 | 1 |
| HIPAA (business associate) | 8 | 4 | 4 | 0 | 0 |
| Client contracts and FTC Act Section 5 | 2 | 0 | 2 | 0 | 0 |
| FAR 52.204-25 reporting | 1 | 0 | 1 | 0 | 0 |
| **Total** | **28** | **10** | **17** | **0** | **1** |

Of the 17 gaps, 12 are Moderate and 5 Low. Most FAR gaps trace to one cause, the acquired firm's separate stack (gap 9), and to federal projects sharing the commercial workspace (gap 11). Both have dated fixes.

### 4.3 Payments and Payroll (`gap-analysis-payments-and-payroll.csv`)
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FTC Safeguards Rule (16 CFR 314.4 and 314.6) | 26 | 11 | 12 | 1 | 2 |
| PCI DSS v4.0.1 (service provider) | 19 | 14 | 4 | 1 | 0 |
| Money transmission (open question) | 1 | 0 | 1 | 0 | 0 |
| Sponsor bank contracts | 1 | 0 | 1 | 0 | 0 |
| **Total** | **47** | **25** | **18** | **2** | **2** |

Of the 20 gaps, 5 are High, 13 Moderate, and 2 Low.

**Not met:** 16 CFR 314.4(f)(2) (no contract binding the affiliate that stores the handoff files) and PCI DSS 11.4.6 (segmentation test missed in 2026 H1). **High:** 314.4(c)(1) and (c)(8) (who can read the handoff files, and whether anyone would know), 314.4(f)(2), and PCI DSS 6.4.3 and 11.6.1 (2 of 5 checkout pages without complete script controls).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Static keys and the shared handoff bucket (1, 2) | CS, TC, PP | FTC Start with Security 2, 3, 5; 16 CFR 314.4(c)(1), (c)(8) | High | Workload identity; dedicated handoff channel with 7-day retention, customer-managed keys, read logging | Group CISO | 2026-12-31 |
| 2 | Untrue or unsubstantiated statements (3, 4) | CS | 15 U.S.C. 45(a) (deception): G-034, G-040, G-042 | High | Correct the trust center and product page now; tell the SOC 2 service auditor about G-040 | Cloud Software division CISO; chief product officer | 2026-10-31 |
| 3 | Affiliate oversight of the handoff (5) | PP, CS | 16 CFR 314.4(b), (f)(1)-(3); PCI DSS 12.8 | High | Intercompany agreement; WCP in the division's risk assessment and service provider reviews | Payments and Payroll division CISO (Qualified Individual) | 2026-12-31 |
| 4 | AI governance and data-use terms (4) | CS, group HR | 15 U.S.C. 45(a); CCPA ADMT rules; Colo. SB26-189 | High | P10 conditions; DPA amendments; pre-2023 customers excluded from tuning until amended | Group Chief Risk Officer | 2027-03-31 |
| 5 | PCI DSS scope maintenance (6) | PP | PCI DSS 11.4.6, 12.5.2.1, 6.4.3, 11.6.1 | High | Segmentation test now; script inventory and tamper detection on all checkout pages | Payments platform director | 2026-11-30 |
| 6 | Multi-division notification matrix (7) | All | 12 CFR 53.4; 16 CFR 314.4(j); 45 CFR 164.410; DPAs; sponsor bank terms; Form 8-K Item 1.05 | Moderate | Complete the matrix; cross-division tabletop | Group General Counsel | 2026-12-08 |
| 7 | CCPA cybersecurity audit readiness (8) | Group | Cal. Code Regs. tit. 11, 7120-7123 | Moderate | Select an independent auditor; map evidence; dry run | Group Chief Privacy Officer | 2027-03-31 |
| 8 | Acquired consulting firm (9) | TC | 48 CFR 52.204-21(b)(1)(i), (iii), (x), (xii)-(xv) | Moderate | Group EDR by 2026-11-30; identity migration by 2027-03-31 | Technology Consulting security and compliance lead | 2027-03-31 |
| 9 | Consulting inheritance (10) | TC | 45 CFR 164.308(a)(8) | Moderate | Inheritance matrix | Technology Consulting security and compliance lead | 2026-12-31 |
| 10 | Federal contract information (11) | TC | 48 CFR 52.204-21(b)(1)(i), (c) | Moderate | Separate federal project area; amend 9 subcontracts | Technology Consulting federal contracts compliance officer | 2027-01-31 |
| 11 | Money transmission question | PP | 31 CFR 1010.100(ff)(5); state laws | Moderate | Complete counsel's analysis; decide | Payments and Payroll chief compliance officer | 2027-03-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-025 to POAM-028 trace directly to this analysis).

## 6. Pending and watch items
- **FTC proposed AI-accuracy policy statement** (Docket FTC-2026-0727; comments closed 2026-07-31): **not final** as of 2026-09-25. Flagged on G-042 and G-043. Not treated as a current obligation.
- **FAR CUI proposed rule (2025) and the FAR Overhaul proposed rule (2026-06-23)**: not final. Flagged on IC-G16 and IC-G17.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06): **proposed only**. It would affect consulting's business associate work (for example, asset inventory and network map, encryption, MFA, and business associate notice within 24 hours of activating a contingency plan). Flagged on the HIPAA rows; not a current obligation.
- **CIRCIA**: the final rule had not been published as of 2026-09-25, so reporting is not mandatory. The group would likely be in scope as an entity above the SBA size standard in a critical infrastructure sector if the final rule keeps the proposed criterion.
- **Colorado SB26-189** (effective 2027-01-01): developer documentation duties for attrition-risk insights and deployer duties for group HR; enforcement posture is unsettled (see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`). Handled in P10.

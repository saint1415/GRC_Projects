# Regulatory Gap Analysis: Cris Santos Company Holdings | Admin and Support Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Administrative and Support and Waste Management and Remediation Services (focus division: Staffing) |
| Primary benchmark (Staffing) | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29, all 106 subcategories, **as a voluntary benchmark** (label `N56-BM`), plus the binding rules for Staffing's records |
| Division regulations | Consulting: HIPAA business associate duties (N54-R06) and FAR 52.204-21 (N54-R04). Home Health: HIPAA Security Rule as a covered entity (N62-R01) with Privacy and Breach Notification rows, Medicare home health conditions of participation, and Section 1557 |
| Group-wide obligations | SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach and data security laws (Florida worked example); Form I-9, E-Verify, and FCRA for every employing entity; CCPA for California workers and applicants; Colorado SB26-189 |
| Gap tables | `gap-analysis.csv` (Staffing and group-wide, 154 rows); `gap-analysis-consulting.csv` (47 rows); `gap-analysis-home-health.csv` (44 rows) |
| Text verified | eCFR (8 CFR 274a.2; 16 CFR 682.3; 16 CFR 314.2; 29 CFR 1630.14; 42 CFR 484.102 and 484.110; 45 CFR 160.103, 164.308, 164.504; 48 CFR 52.204-21 and 52.222-54) as of 2026-09-23; U.S. Code (15 U.S.C. 1681b, 1681m); 2026 Florida Statutes (501.171, 448.095, 934.03); E-Verify MOU for Employers (revision 06/01/13) |
| Assessment dates | 2026-05-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-31) |
| Assessors | Division security and compliance leads, the Staffing Vice President, Employment Compliance, the Consulting HIPAA compliance officer, and the Home Health HIPAA Privacy and Security Officers, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit |

## 1. Applicability
### 1.1 What each division is under the law
| Entity | Status | Basis |
|---|---|---|
| Staffing (employer of record for about 230,000 associates a week) | **Not a HIPAA business associate** for placements. Placed clinicians work under the client's direct control, so they are the client's workforce. Staffing creates, receives, maintains, or transmits no PHI on a client's behalf. No sector cybersecurity rule applies, so CSF 2.0 is the benchmark | 45 CFR 160.103 ("workforce"; "business associate") |
| Consulting | **Business associate** of about 160 hospital and health-system clients: its consulting and management services involve disclosure of PHI to it | 45 CFR 160.103 ("business associate" (1)(ii)) |
| Consulting, Federal Solutions | Federal contractor holding federal contract information on 11 civilian prime contracts | 48 CFR 52.204-21; 52.222-54 |
| Home Health | **Covered entity** (health care provider transmitting standard transactions); Medicare-certified home health agency | 45 CFR 160.103; 42 CFR Part 484 |
| Corporate shared services | Business associate of Home Health for IT hosting, identity, SOC, and EHR integration under the 2023 intercompany BAA. **Also receives Home Health PHI for payroll, which the BAA does not cover** (scenario gap 1) | 45 CFR 160.103; 164.308(b)(1); 164.504(e) |
| Every employing entity | Employer for Form I-9, E-Verify (MOU for Employers; Consulting also as a Federal contractor), FCRA, and the Disposal Rule | 8 CFR 274a.2; MOU; 15 U.S.C. 1681b(b); 16 CFR 682.3 |
| The holding company | SEC registrant | Form 8-K Item 1.05; 17 CFR 229.106 |

**Workers' own records are not PHI.** Clinician credential files and Home Health employees' payroll records are employment records held as employer, which the PHI definition excludes (45 CFR 160.103). They are still personal information under state law (Florida's definition includes medical history and condition, Fla. Stat. 501.171(1)(g)1.a.(IV)) and confidential medical files under the ADA (29 CFR 1630.14(b)(1)). Patient data in visit-pay records is different: it is Home Health PHI wherever it sits.

**The FTC Safeguards Rule (N54-R01), the primary regulation in the Consulting vertical's profile, does not apply.** It covers financial institutions, meaning institutions significantly engaged in activities financial in nature (16 CFR 314.2(h)(1)). Counsel concluded in 2026-07 that no Consulting line completes income tax returns, extends credit, or processes financial data as a service. HIPAA and FAR 52.204-21 are the binding rules for Consulting, so they are its gap targets.

### 1.2 Excluded requirements, with reasons
- **N56-R04 for Staffing:** not a business associate for placements (above). 214 hospital contracts contain BAA or confidentiality terms; they are tracked as contract duties.
- **N56-R05 TCPA:** recruiting texts go to opted-in candidates; contact-consent rules sit with marketing compliance, outside this security analysis.
- **N56-R06 PCI DSS:** no division accepts payment cards.
- **N56-R09 PHMSA:** no hazardous materials.
- **N54-R02, R03, R05, R07, R08:** no tax preparation, no DoD contracts, not a law or CPA firm.
- **N62-R05 42 CFR Part 2:** Home Health is not a Part 2 program. **N62-R06 FTC Health Breach Notification Rule:** excluded for HIPAA covered entities (16 CFR 318.1).
- **CIRCIA (proposed 6 CFR Part 226):** no final rule as of 2026-09-25.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Staffing | Consulting | Home Health | Group (corporate) |
|---|---|---|---|---|
| N56-BM NIST CSF 2.0 | **Primary benchmark** | Group program benchmark | Group program benchmark | Group program benchmark |
| N56-R03 Form I-9; E-Verify MOU | **Applies** (about 610,000 hires a year) | Applies; also Federal contractor terms (FAR 52.222-54; MOU Art. II.B) | Applies | Operates the GWP onboarding service |
| State E-Verify laws (Fla. Stat. 448.095 worked example) | Applies | Applies | Applies | Supports |
| N56-R02 FCRA; N56-R01 Disposal Rule | **Applies** (about 430,000 checks a year) | Applies | Applies | Supports |
| ADA confidential medical files (29 CFR 1630.14) | Applies (Healthcare Staffing clinicians) | Limited | Applies (clinicians) | GWP credentialing |
| N56-R04 / N54-R06 HIPAA business associate | Not applicable (placements) | **Applies** (client PHI) | n/a (covered entity) | Applies (for Home Health) |
| N62-R01 to R03 HIPAA as covered entity | Not applicable | Not applicable | **Primary** | Through the intercompany BAA |
| N62-R08 Medicare home health CoPs (42 CFR 484.102, 484.110) | Not applicable | Not applicable | **Applies** | Supports (shared services in the emergency plan) |
| N62-R07 Section 1557, 45 CFR 92.210 | Not applicable | Not applicable | **Applies** (Medicare and Medicaid) | Group AI standard (P10) |
| N54-R04 FAR 52.204-21 | Not applicable | **Applies** (Federal Solutions enclave) | Not applicable | Common controls inherited by the enclave |
| N54-R01 FTC Safeguards Rule | Not applicable | Not applicable (16 CFR 314.2(h)(1)) | Not applicable | Not applicable |
| N56-R08 NYC Local Law 144 | **Applies** (NYC requisitions) | Applies if NYC requisitions use the tool | Not applicable (no NYC operations) | GWP AI add-on |
| Colorado SB26-189 (from 2027-01-01) | Applies (Colorado requisitions) | Applies (Colorado requisitions) | Applies to employment decisions; the HIPAA covered entity carve-out does not reach them | Group AI program |
| CCPA and CPPA ADMT rules | Applies (California workers and applicants) | Applies | Not applicable (no California operations) | Group privacy office |
| State breach and data security laws | Each state where affected individuals reside (Fla. Stat. 501.171 worked example) | Same, plus third-party agent duties for client data (501.171(6)) | Same; HIPAA notice can satisfy Florida's individual notice with a copy to the Department (501.171(4)(g)) | Coordinates |
| SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| SOC 2 (contractual) | Managed Workforce Solutions in scope (P09) | Out of scope (P09) | Out of scope (P09) | Group services carved in |

## 3. Method
1. **Requirements.** The 106 CSF 2.0 subcategories come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). HIPAA Security Rule rows and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 (via the Health Care crosswalk). Other rows cite the eCFR, the U.S. Code, the 2026 Florida Statutes, the E-Verify MOU, and the cross-sector register (`00_universal-framework/cross-sector/us-cross-sector-obligations.md`) for CCPA and Colorado SB26-189.
2. **Target Profile (Staffing).** Each CSF subcategory has a priority: High 28, Medium 71, Low 7, set by the Staffing security and compliance lead and the Group CISO from P01 and P05. Subcategories that protect SSNs, I-9 records, and pay are High.
3. **Crosswalk.** CSF 2.0 to SP 800-53 uses the **official NIST informative reference** (SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`; the `sp800_53_controls` column lists the official controls that are also in the P02 GWP baseline. HIPAA rows use the Health Care crosswalk, an **author mapping** with NIST's official SP 800-53 mapping beside it (`nist_official_sp800_53r5_1_1`). All other rows carry an author mapping.
4. **Evidence.** Interviews; document review; configuration exports; a sample of 120 Forms I-9 with E-Verify cases across divisions; a mock I-9 inspection (2026-06); 40 Healthcare Staffing rejections; 40 consultant roll-offs; 25 consultant subcontracts; 50 closed engagements; the Home Health emergency plan and exercise reports; and P07 test results.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale. Obligations that start on 2027-01-01 are rated against readiness today.

**Current CSF Tier for Staffing: Tier 3 (Repeatable).** Target: Tier 3 everywhere, with Tier 4 (Adaptive) for identity and payroll fraud monitoring by 2027-12.

## 4. Results
### 4.1 Staffing and group-wide rows (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 25 | 6 | 0 | 0 |
| CSF 2.0 Identify (21) | 14 | 6 | 1 | 0 |
| CSF 2.0 Protect (22) | 16 | 6 | 0 | 0 |
| CSF 2.0 Detect (11) | 9 | 2 | 0 | 0 |
| CSF 2.0 Respond (13) | 10 | 3 | 0 | 0 |
| CSF 2.0 Recover (8) | 7 | 1 | 0 | 0 |
| **CSF 2.0 subtotal (106)** | **81** | **24** | **1** | **0** |
| Form I-9, 8 CFR 274a.2 (16) | 10 | 6 | 0 | 0 |
| E-Verify MOU (5) | 1 | 3 | 1 | 0 |
| Fla. Stat. 448.095 (4) | 3 | 1 | 0 | 0 |
| FCRA (4) | 3 | 1 | 0 | 0 |
| Disposal Rule; ADA medical files; NYC Local Law 144 (3) | 0 | 3 | 0 | 0 |
| State breach and data security laws, Florida worked example (6) | 1 | 5 | 0 | 0 |
| CCPA and CPPA ADMT; Colorado SB26-189 (3) | 1 | 0 | 2 | 0 |
| SEC Item 106 and Item 1.05 (2) | 1 | 1 | 0 | 0 |
| Vertical requirements not applicable to Staffing (5) | 0 | 0 | 0 | 5 |
| **Total (154)** | **101** | **44** | **4** | **5** |

Of the 48 rows partially met or not met, 4 are High, 35 Moderate, 8 Low, and 1 Very Low. The High rows are PR.AA-03 (SMS codes for associate bank changes), Fla. Stat. 501.171(2) (reasonable measures, for scenario gaps 1 and 2), and the two 2027-01-01 AI obligations (CPPA ADMT rules and Colorado SB26-189).

**The pattern:** Staffing runs the steps that happen once per hire well (I-9 timing, E-Verify cases, FCRA authorization). Its gaps are at the edges of the program: E-Verify accounts outside SSO (the one Not met MOU row, Art. II.A.3), the unlogged 2009-2016 I-9 archive (four I-9 rows), a phishable code guarding bank changes, and AI hiring duties that start in under four months. The one Not met CSF row is ID.RA-10: the AI ranking vendor was never assessed before use.

### 4.2 Consulting (`gap-analysis-consulting.csv`)
| Regulation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| HIPAA Security Rule, business associate (17) | 10 | 6 | 1 | 0 |
| HIPAA Privacy Rule, business associate (5) | 0 | 5 | 0 | 0 |
| HIPAA Breach Notification, 164.410 (2) | 1 | 1 | 0 | 0 |
| FAR 52.204-21 (16) | 15 | 1 | 0 | 0 |
| FAR 52.222-54 E-Verify (1) | 0 | 1 | 0 | 0 |
| State third-party agent duty (1) | 0 | 1 | 0 | 0 |
| FTC Safeguards, IRC 7216, DFARS, professional codes, CIRCIA (5) | 0 | 0 | 0 | 5 |
| **Total (47)** | **26** | **15** | **1** | **5** |

**Not met:** 164.308(a)(3)(ii)(C), termination procedures. Group access ends within 4 hours, but the client-issued EHR accounts consultants use are not inventoried, and clients were told of roll-off more than 5 business days late in 17 of 40 cases (scenario gap 7). **High partially met rows:** risk management (164.308(a)(1)(ii)(B)) and subcontractor assurances (164.308(b)(2) and 164.504(e)(2)(ii)(D)), because about 240 independent subcontractors handle PHI without subcontractor BAAs. The Federal Solutions enclave is in good shape: 15 of 16 FAR rows are met; the exception is patching speed ((b)(1)(xii)).

### 4.3 Home Health (`gap-analysis-home-health.csv`)
| Regulation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| HIPAA Security Rule (25 selected rows) | 13 | 10 | 2 | 0 |
| HIPAA Privacy Rule (4) | 0 | 2 | 2 | 0 |
| HIPAA Breach Notification (3) | 2 | 1 | 0 | 0 |
| Medicare emergency preparedness, 42 CFR 484.102 (5) | 2 | 3 | 0 | 0 |
| Medicare clinical records, 42 CFR 484.110 (3) | 2 | 1 | 0 | 0 |
| Section 1557, 45 CFR 92.210 (1) | 0 | 0 | 1 | 0 |
| Recording consent, Florida worked example (1) | 0 | 1 | 0 | 0 |
| 42 CFR Part 2; FTC HBNR (2) | 0 | 0 | 0 | 2 |
| **Total (44)** | **19** | **18** | **5** | **2** |

The Security Rule rows focus on where Home Health's evidence differs from the group's; other specifications rely on group common controls, which is why documenting inheritance (scenario gap 6) matters.

**Not met:**
- 164.308(b)(1), because corporate receives patient data for payroll without BAA coverage (gap 1).
- 164.316(b)(2)(iii), because the Home Health standards were last updated in 2023 (gap 3).
- 164.502(b) and 164.514(d)(3): the visit-pay feed sends names and addresses when pay needs only an anonymous visit ID, and there is no protocol for this routine disclosure.
- 45 CFR 92.210: the hospitalization risk model was never reviewed for protected-trait inputs.

**Why the visit-pay feed matters legally.** Paying Home Health's own clinicians is Home Health's business management, a health care operations activity, so sharing PHI with a business associate for it can be permitted. But only under a BAA that covers the service, and only the minimum necessary. Neither condition is met. The fix is to stop sending the identifiers rather than to paper over the flow.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Patient data in the GWP through the visit-pay feed (1) | HH, Group | 164.308(b)(1); 164.502(b); 164.514(d)(3); 484.110(d) | High | Anonymous visit IDs; purge historical identifiers; BAA amendment for anything that remains | Group Chief Privacy Officer; Home Health HIPAA Privacy Officer | 2026-12-31 (stop); 2027-03-31 (purge) |
| 2 | Phishable self-service authentication for bank changes (2) | Staffing, all workers | CSF PR.AA-03; Fla. Stat. 501.171(2) | High | Passkey or app authenticator; out-of-band confirmation; 3-day hold on first-time changes | Group payroll director | 2027-03-31 |
| 3 | AI hiring duties from 2027-01-01 (4) | All | 11 CCR 7200 et seq.; C.R.S. 6-1-1701 to -1709; NYC Admin. Code 20-870 et seq. | High | Notices, opt-out and appeal paths, adverse impact monitoring, vendor terms (P10) | Group Chief Privacy Officer; Group General Counsel | 2026-12-31 |
| 4 | Consulting subcontractor BAAs and client account control (7) | Consulting | 164.308(a)(3)(ii)(C); 164.308(b)(2); 164.504(e)(2)(ii)(D) | High | Subcontractor BAAs; client account register; roll-off notice within 1 business day | Group General Counsel; Consulting HIPAA compliance officer | 2027-03-31 |
| 5 | Multi-regulator notification not exercised (5) | All | 501.171(3)-(6); MOU Art. II.A.16; 164.404-410; Form 8-K Item 1.05 | Moderate | Complete the matrix; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 6 | E-Verify accounts and the I-9 archive (8) | All employing entities | MOU Art. II.A.3, II.A.15; 8 CFR 274a.2(g)(1)(i), (iv) | Moderate | Termination checklist and reconciliation; archive logging and object lock | Staffing Vice President, Employment Compliance | 2026-12-31 |
| 7 | Home Health inheritance and policy drift (3, 6) | HH | 164.308(a)(8); 164.316(b)(2)(iii) | Moderate | Inheritance matrix; re-issue supplement | Home Health security and compliance lead | 2026-12-31 |
| 8 | Home Health emergency plan lacks a cyber outage (BIA finding) | HH | 42 CFR 484.102(a)(1), (b)(2)-(4) | Moderate | Cyber outage hazard; daily priority list in declared emergencies | Home Health emergency preparedness coordinator | 2026-12-31 |
| 9 | Section 1557 review of the hospitalization risk model | HH | 45 CFR 92.210 | Moderate | Input review and mitigation record | Home Health chief clinical officer | 2026-12-31 |
| 10 | Retention and disposal (consumer reports, candidates) | Staffing, Group | 16 CFR 682.3; Fla. Stat. 501.171(8) | Moderate | Automated deletion | Group Chief Privacy Officer | 2027-06-30 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-024 to POAM-028 trace directly to this analysis (intercompany BAA scope, AI hiring readiness, Consulting subcontractor BAAs, the 92.210 review, and repository PHI classification and purge).

## 6. Pending regulatory changes
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**; the regulatory agenda projects a final rule in July 2027. If finalized as proposed it would affect Home Health (covered entity) and Consulting and corporate (business associates): the required and addressable distinction would be removed; encryption of all ePHI and MFA would be required; a written technology asset inventory and network map; penetration testing at least every 12 months, and vulnerability scanning; restoring certain systems within 72 hours; a compliance audit at least every 12 months; and business associates notifying covered entities within 24 hours of activating a contingency plan. The `pending_rule_change` column flags affected rows. None is treated as a current obligation.
- **Colorado SB26-189** takes effect 2027-01-01 (AG rules due by then). Litigation and federal preemption efforts around Colorado's AI laws continue; the group plans for the statute as signed.
- **CPPA rules:** ADMT compliance by 2027-01-01; risk assessments and cybersecurity audits phase in from 2027-2028.
- **FAR:** the FAR CUI rule and the FAR cyber incident reporting rule remain proposed; a FAR overhaul proposed rule was published 2026-06-23.
- **CIRCIA:** not in effect (final rule not published as of 2026-09-25).
- **Form I-9 and E-Verify:** no proposed change to the retention or electronic I-9 standards was found for 2025-2026. A DHS interim final rule (90 FR 48799, effective 2025-10-30) ended automatic extension of many renewal EADs, which shortens reverification lead time; onboarding reverification alerts were updated.

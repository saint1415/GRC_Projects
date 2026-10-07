# Regulatory Gap Analysis: Cris Santos Company Holdings | Management of Companies and Enterprises | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (holding company with two operating divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Management of Companies and Enterprises (focus: the holding company) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 group profile (voluntary), NIST CSWP 29 (2024-02-26), with division profiles; profile method from NIST SP 1301 (Quick-Start Guide for Creating and Using Organizational Profiles) |
| Group-level binding obligations | SEC Reg S-K Item 106 and Form 8-K Item 1.05; SOX section 404; HIPAA duties of the group health plan and its sponsor; Fla. Stat. 628.801 (insurance holding company); Fla. Stat. 501.171 (worked example of state law) |
| Division regulations | Insurance: state insurance data security laws based on NAIC Model #668 (Alabama, South Carolina, Tennessee in part), GLBA through the State of domicile, and the NAIC AI Model Bulletin (North Carolina). Health Care Services: HIPAA Security, Privacy, and Breach Notification Rules and Section 1557 (45 CFR 92.210) |
| Gap tables | `gap-analysis.csv` (group, 134 rows); `division-profiles.csv` (22 CSF categories x 3 profiles); `gap-analysis-insurance.csv` (48 rows); `gap-analysis-health-care-services.csv` (40 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from P07 (to 2026-08-28) |
| Assessors | Group CISO's governance team with the Group General Counsel, the Insurance chief compliance officer, and the Health Care Services HIPAA officers; applicability conclusions reviewed by outside counsel; results reviewed by group internal audit |

## 1. Applicability
A holding company's obligations come from what it is (a public registrant, a plan sponsor, the parent of insurers) and from what its subsidiaries do. Each candidate requirement was checked against its primary text.

### 1.1 Holding company (group level)
| Requirement | Applies? | Basis |
|---|---|---|
| **N55-R01** Reg S-K Item 106 (17 CFR 229.106) | **Yes** | Publicly traded registrant filing Form 10-K. Item 106 has no size exemption |
| **N55-R02** Form 8-K Item 1.05 | **Yes** | SEC registrant |
| **N55-R03** SOX section 404 (15 U.S.C. 7262) | **Yes, including 404(b)** | Large accelerated filer (17 CFR 240.12b-2: $700 million or more public float), so the 7262(c) exemption does not apply and the auditor attests |
| **N55-R04** Federal Reserve incident notification (12 CFR 225.300-225.303) | **No** | The group owns no bank or savings association, so it is not a bank holding company (12 CFR 225.2(b), (c)(1)) |
| **N55-R05** 12 CFR Part 225, Appendix F | **No** | Same reason. GLBA safeguards for the insurers come from the state insurance authority (15 U.S.C. 6805(a)(6)) |
| **N55-R06** HIPAA (group health plan) | **Yes, fully** | The self-insured plan has about 38,000 participants, so it is a group health plan and a covered entity (45 CFR 160.103). The holding company as sponsor receives PHI for plan administration beyond summary and enrollment information, so the plan-document rules apply in full: 164.504(f)(2) (privacy) and 164.314(b) (security) |
| **N55-R07** CIRCIA (proposed 6 CFR Part 226) | **Not yet** | Proposed only; no final rule as of 2026-09-25 |
| Fla. Stat. 628.801 | **Yes** | The holding company is the ultimate controlling person of two Florida-domiciled insurers: annual enterprise risk report by April 1 (628.801(2)); the Office of Insurance Regulation may examine affiliates (628.801(3)) |
| FTC Safeguards Rule (16 CFR Part 314) | **No** | No group entity is a non-bank financial institution under FTC jurisdiction; insurers are assigned to state insurance authorities (15 U.S.C. 6805(a)(6)) |
| State breach and data security laws | **Yes** | Each state where affected individuals reside; Florida worked example: Fla. Stat. 501.171(2) requires "reasonable measures to protect and secure data in electronic form containing personal information." Notice duties are in P08 |

### 1.2 Insurance division
- **Licensee status.** Both insurers are licensed in Florida, Georgia, Alabama, South Carolina, North Carolina, and Tennessee. The NAIC state page for Model #668 (Summer 2026) lists Alabama and South Carolina as adopting the model and Tennessee as adopting portions. Florida, Georgia, and North Carolina have only related general statutes. **So the model's duties bind the insurers through Alabama, South Carolina, and Tennessee law, as licensees there.** Each state's text varies; insurance counsel confirms the enacted sections, and the Tennessee rows are confirmed against its partial enactment.
- **What does not apply.** The annual certification in sec. 4I applies to insurers domiciled in the enacting state; these insurers are domiciled in Florida. The HIPAA deemer in sec. 9A(2) does not help, because the insurers are not HIPAA-regulated: workers' compensation, liability, and automobile medical payment coverage are excepted benefits (42 U.S.C. 300gg-91(c)(1)), which the HIPAA definition of health plan excludes (45 CFR 160.103). The insurers are not assuming insurers, so the reinsurer notice in sec. 6E does not apply.
- **The holding company is the insurers' Third-Party Service Provider.** Model sec. 3P covers a person, not itself a licensee, that contracts with a licensee to maintain, process, store, or otherwise access nonpublic information. The holding company processes claims payments and runs identity for the insurers under the 2017 intercompany agreement. The insurers must perform due diligence and require it to protect their information (sec. 4F).
- **GLBA.** Safeguards standards for insurers are enforced by the State insurance authority of the State of domicile (15 U.S.C. 6805(a)(6)), here Florida. Florida's administrative rules could not be read from this environment; counsel confirms any Office of Insurance Regulation safeguards rule (one row, `gap-analysis-insurance.csv`).
- **NAIC AI Model Bulletin.** Among the 6 licensed states, only North Carolina adopted it (Bulletin No. 24-B-19, 2024-12-18; NAIC implementation map as of 2026-04-01). The group applies it to all Insurance AI by choice.
- **NYDFS Part 500:** not applicable (no New York license).

### 1.3 Health Care Services division
- **HIPAA covered entity:** health care provider that transmits health information electronically in standard transactions (45 CFR 160.103). No size exemption; 164.306(b) lets it choose how, not whether.
- **The holding company is its business associate** (2021 BAA) for shared IT, identity, and patient refund payments.
- **Workers' compensation and employer disclosures** rely on 164.512(l) (as authorized by and to the extent necessary to comply with workers' compensation laws) and 164.512(b)(1)(v) (work-related findings to employers, with written notice to the individual).
- **Section 1557:** accepts Medicare and Medicaid, so 45 CFR 92.210 applies to patient care decision support tools.
- **Not applicable:** 42 CFR Part 2 (no federally assisted substance use disorder program); CMS emergency preparedness (physician offices and urgent care clinics are not among the covered provider types); FTC Health Breach Notification Rule (covered entities are excluded).

## 2. Regulation-by-division matrix
| Requirement | Holding company (group) | Insurance | Health Care Services |
|---|---|---|---|
| CSF 2.0 group profile (voluntary) | **Primary benchmark** (group Organizational Profile) | Division profile | Division profile |
| N55-R01 Item 106; N55-R02 Form 8-K Item 1.05 | **Applies** (registrant) | Via group (division facts feed materiality) | Via group |
| N55-R03 SOX 404 | **Applies** (ERP, HCM, treasury ITGCs) | Via group (claims payments and statutory feeds) | Via group (revenue feeds) |
| N55-R06 HIPAA, group health plan | **Applies** (plan sponsor; plan is a covered entity) | Employees are plan members | Employees are plan members; about 9,000 covered lives are also clinic patients |
| N55-R04, N55-R05 Federal Reserve | Not applicable (no bank) | Not applicable | Not applicable |
| N55-R07 CIRCIA | Not yet (proposed) | Not yet | Not yet |
| Fla. Stat. 628.801 | **Applies** (ultimate controlling person) | Registration and examination | Not applicable |
| N52-R07 Model #668 state laws | Reached as the insurers' Third-Party Service Provider (sec. 4F) | **Applies** in Alabama, South Carolina, Tennessee (in part) | Not applicable |
| N52-R01 GLBA | Via the insurers | **Applies** (Florida as State of domicile) | Not applicable |
| NAIC AI Model Bulletin | Group AI Standard | **Applies** in North Carolina; applied group-wide by choice | Not applicable |
| N62-R01 to N62-R03 HIPAA Security, Privacy, Breach | Applies as business associate of Health Care Services | Not a covered entity (excepted benefits) | **Applies** (covered entity) |
| N62-R07 Section 1557 (92.210) | Group AI Standard | Not applicable | **Applies** |
| FTC Safeguards Rule | Not applicable | Not applicable (state insurance authority) | Not applicable |
| State breach notification laws | Each state where affected individuals reside (Florida worked example: 501.171) | Same, plus commissioner notices | Same, with HIPAA notices (Florida deemed-compliance path) |

## 3. Method
1. **Group profile.** The five steps in CSF 2.0 section 3.1 and SP 1301. Scope: all 106 CSF 2.0 subcategories for the holding company and the SCSP. Each row has current practice, evidence, a **rating** (1 = not performed; 2 = informal or only in some divisions; 3 = defined and performed for the holding company and shared platform; 4 = consistent across the group; 5 = measured and improving), a **priority**, and a target. Status maps from the rating: 1 = Not met, 2-3 = Partially met, 4-5 = Met. CSF rows use NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 references.
2. **Division profiles.** `division-profiles.csv` rates the 22 CSF categories for each division with the same scale; the group column is the rounded mean of its subcategory ratings.
3. **Binding obligations.** SEC, SOX, HIPAA plan, Florida, Model #668, and Section 1557 rows were read from primary text (eCFR current through 2026-09-23, govinfo.gov, flsenate.gov, and the NAIC model and state pages). **Model #668 is NAIC copyrighted text, so rows give section numbers and short summaries in the author's words, not the model's text.** HIPAA Security Rule rows use the Health Care crosswalk in `02_industry-rules/health-care/` (author mapping, with NIST's official SP 800-53 mapping shown). Other rows carry an author mapping.
4. **Status:** Met, Partially met, Not met, or Not applicable. Risk levels use the P01 scale.

**CSF Tiers.** Current practice is **Tier 2 (Risk Informed)** for the group, with identity, monitoring, and incident handling at **Tier 3 (Repeatable)**. The target is Tier 3 group-wide by 2027-12-31 and a rating of 4 in every category for every profile.

## 4. Results
### 4.1 Group profile and group obligations (`gap-analysis.csv`, 134 rows)
| Area | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF Govern (GV, 31) | 14 | 17 | 0 | 0 |
| CSF Identify (ID, 21) | 13 | 8 | 0 | 0 |
| CSF Protect (PR, 22) | 11 | 11 | 0 | 0 |
| CSF Detect (DE, 11) | 9 | 2 | 0 | 0 |
| CSF Respond (RS, 13) | 9 | 4 | 0 | 0 |
| CSF Recover (RC, 8) | 6 | 2 | 0 | 0 |
| SEC Item 106 and Form 8-K Item 1.05 (7) | 5 | 2 | 0 | 0 |
| SOX 404 (4) | 3 | 1 | 0 | 0 |
| HIPAA, group health plan (11) | 3 | 3 | 5 | 0 |
| Florida 628.801(2) and 501.171(2) (2) | 0 | 2 | 0 | 0 |
| Not applicable checks (4) | 0 | 0 | 0 | 4 |
| **Total (134)** | **73** | **52** | **5** | **4** |

**What the profile shows.** The group's detection, response, and recovery outcomes are mostly consistent across divisions (Met), because they come from common controls. **Govern is the weakest Function** (17 of 31 partially met), and the weak Govern outcomes are the ones that describe a holding company's relationship with its subsidiaries: intercompany dependencies (GV.OC-05), supply chain coverage of intercompany services (GV.SC-01, -02, -05, -06), and division roles and authority (GV.RR-02). Four outcomes rated 2 carry High gap risk: data inventory for sensitive data in collaboration sites (ID.AM-07), identity proofing at recovery (PR.AA-02), excess privilege across divisions (PR.AA-05), and data in use by the AI assistant (PR.DS-10). Of the 106 profile outcomes, 32 are High priority, 56 Medium, and 18 Low.

**The 5 Not met rows are all the same gap:** the plan documents were never amended with the Security Rule's plan-sponsor terms (45 CFR 164.314(b) and (b)(2)(i)-(iv); scenario gap 3).

Of the 57 group rows that are partially met or not met, 4 carry High gap risk, 39 Moderate, and 14 Low.

### 4.2 Division profiles (`division-profiles.csv`)
| Profile | Categories rated 2 | Rated 3 | Rated 4 | Main difference from the group |
|---|---|---|---|---|
| Group (holding company and SCSP) | 0 | 8 | 14 | Baseline |
| Insurance | 3 | 15 | 4 | Supply chain (GV.SC), identity (PR.AA), and incident communications (RS.CO) rated 2: no oversight of the holding company as a service provider, caller and surge verification, commissioner and producer notices |
| Health Care Services | 7 | 14 | 1 | The acquired clinics pull down asset management, risk assessment, platform security, resilience, and monitoring; the 2023 supplement pulls down policy |

### 4.3 Insurance (`gap-analysis-insurance.csv`, 48 rows)
| Requirement group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Model #668 sec. 4A-4B (program and objectives) | 3 | 2 | 0 | 0 |
| Sec. 4C (risk assessment) | 3 | 2 | 0 | 0 |
| Sec. 4D (risk management) | 6 | 9 | 0 | 0 |
| Sec. 4E (board oversight) | 1 | 2 | 0 | 0 |
| Sec. 4F (Third-Party Service Providers) | 0 | 2 | 0 | 0 |
| Sec. 4G-4H (adjustments, incident response plan) | 1 | 2 | 0 | 0 |
| Sec. 4I (annual certification) | 0 | 0 | 0 | 1 |
| Sec. 5 (investigation) | 2 | 1 | 0 | 0 |
| Sec. 6 (notification) | 0 | 4 | 1 | 1 |
| Sec. 9A(2) (HIPAA deemer) | 0 | 0 | 0 | 1 |
| GLBA through the State of domicile | 0 | 1 | 0 | 0 |
| NAIC AI Model Bulletin (North Carolina) | 0 | 3 | 0 | 0 |
| **Total (48)** | **16** | **28** | **1** | **3** |

**Not met:** sec. 6F (no procedure to notify producers of record). **High gap risk:** sec. 4B(3) and 4D(2)(a), both driven by claimant bank-detail changes verified only with knowledge questions (INS-001). **The holding company appears in five Insurance rows** (4C(2), 4D(1), 4F(1), 4F(2), 5C): the insurers' largest service provider has never been treated as one.

### 4.4 Health Care Services (`gap-analysis-health-care-services.csv`, 40 rows)
| Requirement group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| HIPAA Security Rule 164.308 (18) | 7 | 11 | 0 | 0 |
| 164.310 (2) | 2 | 0 | 0 | 0 |
| 164.312 (6) | 3 | 3 | 0 | 0 |
| 164.314 and 164.316 (2) | 1 | 1 | 0 | 0 |
| HIPAA Privacy Rule (5) | 0 | 4 | 1 | 0 |
| HIPAA Breach Notification Rule (2) | 1 | 1 | 0 | 0 |
| Section 1557, 92.210 (2) | 0 | 1 | 1 | 0 |
| Not applicable checks (3) | 0 | 0 | 0 | 3 |
| **Total (40)** | **14** | **21** | **2** | **3** |

The Security Rule rows focus on specifications where the division's evidence differs from the group's common controls. **Not met:** routine-disclosure protocols (164.514(d)(3)) for the flows to the group insurer and to employers, and Section 1557 mitigation (92.210(c)). **High gap risk:** risk management (164.308(a)(1)(ii)(B)), access authorization (164.308(a)(4)(ii)(B)), minimum necessary (164.502(b)), and workers' compensation disclosures (164.512(l)): the adjuster role exposes non-work visits (scenario gap 6).

**Addressable is not optional.** For each addressable specification, the division must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). No addressable gap is being documented as unreasonable.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Identity recovery and cross-division privilege (1) | All | PR.AA-02, PR.AA-05; Model #668 4D(2)(a), (g); 164.308(a)(5)(ii)(D) | High | Division-scoped roles; verified MFA resets (POAM-001) | Group identity director | 2026-11-30 |
| 2 | Bank-detail change verification (5) | Insurance; payables | Model #668 4B(3), 4D(2)(a); SOX 404 | High | Verification to contact data on file; first-payment hold (POAM-013) | Group Treasurer; Insurance claims vice president | 2026-12-31 |
| 3 | AI assistant without labels or confirmed BAA scope (9) | All | ID.AM-07, PR.DS-10; 164.308(b)(1); Model #668 4G | High | Group AI Standard conditions (POAM-023; P10) | Group Chief Risk Officer | 2026-12-31 |
| 4 | Adjuster access to clinic charts (6) | Health Care Services; Insurance | 164.502(b); 164.512(l); 164.514(d)(3) | High | Work-injury-only role, then report delivery; routine-disclosure protocols (POAM-017) | Group Chief Privacy Officer | 2027-03-31 |
| 5 | Holding company not overseen as the insurers' service provider (2) | Insurance | Model #668 4C(2), 4F(1)-(2), 5C, 6D; GV.SC-06 | Moderate | Security schedule; affiliate assurance report (P09); intercompany incident clause (POAM-016) | Group General Counsel | 2027-03-31 |
| 6 | Plan sponsor terms and separation (3) | Group | 164.314(b)(2); 164.504(f)(2)(iii) | Moderate | Amend plan documents; stop export; restricted site (POAM-005, POAM-022) | Group benefits director | 2026-12-31 |
| 7 | Notification matrix incomplete and unexercised (7) | All | Model #668 sec. 6A, 6F; Form 8-K Item 1.05; 164.410 | Moderate | Matrix rows; tabletop (POAM-009, POAM-010) | Group General Counsel | 2026-12-15 |
| 8 | Acquired clinics outside the risk analysis, inheritance, and SIEM (8) | Health Care Services | 164.308(a)(1)(ii)(A), (a)(8); 164.312(b) | Moderate | Full analysis; inheritance matrix; SIEM onboarding (POAM-011, POAM-019) | Health Care Services HIPAA Security Officer | 2026-12-31 |
| 9 | ERP privileged access (4) | Group | SOX 404 (ITGC) | Moderate | PAM and emergency review (POAM-003, POAM-004) | Group Controller | 2026-12-31 |
| 10 | Health Care Services supplement drift | Health Care Services | 164.316(b)(2)(iii); GV.PO-02 | Moderate | Re-issue supplement (POAM-024) | Health Care Services HIPAA Security Officer | 2026-11-30 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-016, POAM-019, POAM-022, POAM-023, and POAM-024 trace directly to this analysis.

## 6. Pending regulatory changes and watch items
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **proposed only**; the regulatory agenda projects a final rule in July 2027. If finalized as proposed, it would remove the required and addressable distinction, require encryption of ePHI at rest and in transit with limited exceptions, MFA, a written technology asset inventory and network map, penetration testing at least every 12 months and vulnerability scanning, restoration of certain systems within 72 hours (the legacy EHR's 24-hour RPO and nightly backups would need review), a compliance audit at least every 12 months, and business associate notice to covered entities within 24 hours of activating a contingency plan (the holding company to Health Care Services and to the group health plan). Flagged in the `pending_rule_change` column; none is treated as a current obligation.
- **CIRCIA** (N55-R07) is proposed only; recheck the insurance and health care sector criteria when the final rule is published.
- **Model #668 adoption:** recheck the NAIC state page each year; if Florida, Georgia, or North Carolina enacts it, the analysis expands (and a Florida enactment would bring the sec. 4I annual certification).
- **NAIC AI Model Bulletin:** recheck the NAIC implementation map each year for the other licensed states.
- **Structural triggers:** acquiring a bank or savings association (N55-R04 and N55-R05 would apply); licensing in New York (NYDFS Part 500); fully insuring the health plan (the plan-document analysis would change); a clinic starting a federally assisted substance use disorder program (42 CFR Part 2).

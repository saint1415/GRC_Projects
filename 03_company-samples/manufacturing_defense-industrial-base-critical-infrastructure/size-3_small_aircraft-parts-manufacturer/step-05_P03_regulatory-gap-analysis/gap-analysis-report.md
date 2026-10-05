# Regulatory Gap Analysis: Cris Santos Company | Defense Industrial Base | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts manufacturer, DoD subcontractor) |
| Tier / Vertical | Small / Defense Industrial Base |
| Regulation analyzed | NIST SP 800-171 Rev. 2 (110 requirements), as required by DFARS 252.204-7012(b)(2) and assessed for CMMC Level 2 (32 CFR 170.14(c)(3)) |
| Secondary requirements | DFARS 252.204-7012 incident, cloud, and flowdown paragraphs; DFARS 252.204-7019, 252.204-7020, 252.204-7021; 32 CFR Part 170 scoping; FAR 52.204-21 |
| Assessment dates | 2026-07-13 to 2026-07-24 (plant walkthrough 2026-08-05) |
| Assessor | IT Manager with the Contracts Manager and Manufacturing Systems Engineer |
| Working file | `gap-analysis.csv` (128 rows: G-001 to G-110 for the 110 requirements, G-111 to G-128 for clause and regulation duties) |

## 1. Applicability
**DFARS 252.204-7012 applies now.** Both current subcontracts (Prime A and Prime B) include the clause, and the company receives and creates covered defense information (controlled technical information such as drawings, models, and NC programs). The clause has no small-business exemption and must be flowed down to any subcontract that involves covered defense information, including for commercial products or services (252.204-7012(m)(1)). It requires SP 800-171 on every covered contractor information system (252.204-7012(b)(2)(i)).

**DFARS 252.204-7019 and 252.204-7020 apply now.** A current SP 800-171 DoD Assessment score (not more than 3 years old) must be in SPRS. The 2024 Basic Assessment of 96 is current by date, but it is not accurate (section 3).

**CMMC Level 2 (C3PAO) applies from the next Prime A awards.** Current subcontracts predate 2025-11-10 and do not include DFARS 252.204-7021. Prime A has told suppliers that solicitations issued from 2026-11-10 (Phase 2, 32 CFR 170.3(e)(2)) will flow down Level 2 (C3PAO). A subcontractor that processes CUI under a prime contract requiring Level 2 (C3PAO) needs at least that status (32 CFR 170.23(a)(3)). There is no size exemption. The company's Affirming Official is the President (32 CFR 170.22).

**Scope.** The assessment covers the CUI Engineering Enclave defined in the SSP (P02), using the CMMC Level 2 asset categories in 32 CFR 170.19(c). The CNC machines and CMMs are Specialized Assets. The corporate network, payroll, and the MSP are Out-of-Scope Assets, separated by the enclave firewall (the MSP has no enclave accounts, confirmed 2026-07-16). ERP holds DoD purchase order data (FCI) and its scoping position is open (G-125).

**Not applicable, with reasons:**
- **3.13.14 (VoIP):** no VoIP components in the assessment scope. Scored as Met (32 CFR 170.24(b)(3)).
- **NISPOM (32 CFR Part 117):** the company has no facility clearance and no classified information.
- **CIRCIA:** the final rule is not published; nothing is required yet.

**Considered but not decomposed here:** ITAR and EAR. They shape access (U.S.-person checks), the encryption rows (3.13.11 and the carve-outs in 22 CFR 120.54(a)(5) and 15 CFR 734.18(a)(5)), and visitor control, and they are handled in POL-04 and P08.

## 2. Method
1. **Requirements.** The 110 rows follow the official structure of NIST SP 800-171 Rev. 2 (families 3.1 to 3.14), with the CMMC identifier and the point value from the CMMC Scoring Methodology (32 CFR 170.24(c)(2)). Requirement text is quoted from the public-domain NIST publication. The 18 clause rows cite the paragraph of each clause or section as checked on eCFR (version date 2026-09-23).
2. **Crosswalk.** CSF 2.0 and SP 800-53 Rev. 5 mappings are derived from NIST's official mappings through the SP 800-171 Rev. 3 counterpart of each requirement (the Rev. 2 to Rev. 3 change analysis, the SP 800-171r3 CUI overlay, and the CSF 2.0 to SP 800-171r3 mapping). The route through Rev. 3 is the author's; the `crosswalk_source` column says so for each row.
3. **Evidence.** Interviews, configuration exports (identity provider, sharing policy, firewall, SFTP, backup and logging settings), document review, and the plant walkthrough.
4. **Status.** Met, Partially met, Not met, or Not applicable. For CMMC scoring, a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)), so every Partially met row below counts as NOT MET in the score.

## 3. Results summary

### SP 800-171 Rev. 2 requirements (110)
| Family | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 3.1 Access Control | 13 | 9 | 0 | 0 |
| 3.2 Awareness and Training | 0 | 1 | 2 | 0 |
| 3.3 Audit and Accountability | 2 | 4 | 3 | 0 |
| 3.4 Configuration Management | 2 | 5 | 2 | 0 |
| 3.5 Identification and Authentication | 3 | 6 | 2 | 0 |
| 3.6 Incident Response | 0 | 1 | 2 | 0 |
| 3.7 Maintenance | 4 | 1 | 1 | 0 |
| 3.8 Media Protection | 1 | 5 | 3 | 0 |
| 3.9 Personnel Security | 1 | 1 | 0 | 0 |
| 3.10 Physical Protection | 3 | 3 | 0 | 0 |
| 3.11 Risk Assessment | 1 | 1 | 1 | 0 |
| 3.12 Security Assessment | 0 | 3 | 1 | 0 |
| 3.13 System and Communications Protection | 11 | 4 | 0 | 1 |
| 3.14 System and Information Integrity | 4 | 2 | 1 | 0 |
| **Total (110)** | **45** | **46** | **18** | **1** |

Of the 64 requirements not fully met, 20 are basic and 44 are derived requirements.

### Clause and regulation duties (18)
| Source | Met | Partially met | Not met |
|---|---|---|---|
| DFARS 252.204-7012 (cloud, special measures, reporting, malware, preservation, forensics, flowdown) | 1 | 2 | 7 |
| DFARS 252.204-7019 and 252.204-7020 (SPRS, Government access, subcontractor assessments) | 1 | 1 | 1 |
| DFARS 252.204-7021 and 32 CFR Part 170 (status, affirmation, scoping, subcontractor flowdown) | 0 | 2 | 2 |
| FAR 52.204-21 (FCI on corporate systems) | 0 | 1 | 0 |
| **Total (18)** | **2** | **6** | **10** |

### Score under 32 CFR 170.24
| Item | Value |
|---|---|
| Maximum score | 110 |
| Points subtracted for the 64 requirements not fully met | 175 (23 at 5 points, 8 at 3 points, 30 at 1 point, 3.5.3 and 3.13.11 at 3 points each as partially effective; 3.12.4 carries no point value) |
| **Recalculated score** | **-65** |
| SPRS score posted 2024-09-12 | 96 (withdrawn; corrected score due 2026-09-30) |
| Minimum for Conditional Level 2 status | 88 (score / 110 of at least 0.8, 32 CFR 170.21(a)(2)(i)) |

Conditional status also allows only 1-point requirements on a POA&M (plus 3.13.11 when encryption is used but not FIPS-validated), and never 3.1.20, 3.1.22, 3.12.4, 3.10.3, 3.10.4, or 3.10.5 (32 CFR 170.21(a)(2)(ii) and (iii)). Four of those six are open today: 3.1.20, 3.10.3, 3.10.4, and 3.12.4 (the SSP was rewritten on 2026-08-31 and will be verified in the readiness re-check). **The plan therefore aims for all 110 requirements Met before the C3PAO assessment**, with a POA&M used only as a fallback for 1-point items.

## 4. Priority gaps and roadmap
34 rows are rated High or Very High gap risk (33 High, 1 Very High). The highest-value items:

| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| G-124 Not eligible for Level 2 (C3PAO) awards | 252.204-7021(d)(1); 32 CFR 170.17, 170.22 | Very High | Complete this roadmap; C3PAO assessment; affirmation by the President | Vice President of Operations | 2027-02-26 |
| G-121 SPRS score overstates implementation | 252.204-7019(b); 252.204-7020(d) | High | Post -65 and a date-to-110; update after each milestone | Contracts Manager | 2026-09-30 |
| G-020, G-077, G-078 External systems and visitor control (cannot be on a POA&M) | 3.1.20; 3.10.3; 3.10.4 | High (3.1.20, 3.10.3) | Block public AI and file-sharing from the enclave; escort and log every shop-floor visitor | IT Manager; Facilities and Security Coordinator | 2026-10-31 |
| G-056, G-114, G-115, G-117 Cannot report to DoD or preserve evidence | 3.6.2; 252.204-7012(c), (e) | High | Medium assurance certificates; P08 runbook; forensic retainer; DIBNet drill 2026-11-18 | Contracts Manager; IT Manager | 2026-10-31 to 2026-11-30 |
| G-119 No DFARS flowdown to outside processors | 252.204-7012(m)(1) | High | Add clauses to purchase orders or stop sending CUI | Contracts Manager | 2026-10-31 |
| G-044 to G-046, G-053 Shared MES logins, no MFA, plaintext DNC password | 3.5.1; 3.5.2; 3.5.3; 3.5.10 | High | MES sign-in through SYS-01 with badge plus PIN; vault the DNC service credential | Manufacturing Systems Engineer | 2026-10-31 to 2026-11-30 |
| G-098 FIPS validation not confirmed on 2 CUI paths | 3.13.11 | High | FIPS mode on SFTP gateway and plant firewall VPN | Systems Administrators | 2026-11-30 |
| G-030, G-026 No log review; missing sources | 3.3.5; 3.3.1 | High | Weekly review with alerts; collect MES, DNC, firewall logs; 1-year retention | IT Manager | 2026-11-30 to 2026-12-31 |
| G-082, G-104 No vulnerability scanning; late patching | 3.11.2; 3.14.1 | High | Monthly authenticated scans; patch windows | Systems Administrators | 2026-11-30 |
| G-066, G-070 Paper CUI not destroyed; USB loading of CNC machines | 3.8.3; 3.8.7 | High | Locked shred bins; labeled drive inventory then DNC serial gateway | Quality Manager; Manufacturing Systems Engineer | 2026-10-31; 2027-01-31 |
| G-035, G-036, G-042 No baselines, hardening, or enforced allowlisting | 3.4.1; 3.4.2; 3.4.8 | High | Documented baselines; benchmark hardening; allowlisting enforcement | Systems Administrators | 2026-12-31; 2027-01-15 |
| G-109 No 24x7 or egress monitoring | 3.14.6 | High | Managed detection for the enclave | IT Manager | 2027-01-31 |

**Roadmap by milestone:**
1. **By 2026-09-30:** corrected SPRS score.
2. **By 2026-10-31:** all items that cannot be on a POA&M; DoD reporting certificates; flowdowns; ERP scoping position (G-125); asset categories and diagram (G-127).
3. **By 2026-11-30:** MES identity and MFA, FIPS confirmation, scanning, log review, P08 tabletop.
4. **By 2026-12-31:** baselines, CUI and insider threat training, first full self-assessment against SP 800-171A objectives.
5. **By 2027-01-31:** DNC serial gateway, allowlisting enforcement, 24x7 detection. Readiness re-check in late January 2027, then the C3PAO assessment (2027-02-15 to 2027-02-26).

The full list, with evidence, is in `gap-analysis.csv`. High and Very High gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **FAR CUI rule:** proposed (90 FR 4278, 2025-01-15) and not final. It would set Government-wide CUI safeguarding and reporting terms. Nothing changes for this company until it is final; DFARS 252.204-7012 remains the governing clause.
- **Revolutionary FAR Overhaul:** a proposed rule (91 FR 37550, 2026-06-23) would reorganize FAR parts including part 40. FAR 52.204-21 numbering may change (flagged on G-128). Not final.
- **SP 800-171 Rev. 3:** published by NIST, but CMMC Level 2 is fixed to Rev. 2 (32 CFR 170.14(c)(3)). Each row names its Rev. 3 counterpart in `pending_rule_change` for later planning. Rev. 3 is not treated as a current obligation.
- **CIRCIA:** the final rule is not published. Proposed reporting deadlines are not treated as current obligations.

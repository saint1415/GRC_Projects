# Regulatory Gap Analysis: Cris Santos Company Holdings | Defense Industrial Base | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Defense Industrial Base (focus division: Aircraft Parts) |
| Primary regulation | NIST SP 800-171 Rev. 2 (110 requirements), required by DFARS 252.204-7012(b)(2) and assessed for CMMC Level 2 (32 CFR 170.14(c)(3)) |
| Division regulations | Engineering Services: the same CUI rules plus NISPOM at two cleared centers; Defense Software: DFARS 252.239-7010 for the DoD edition, the FedRAMP Moderate equivalency duty for the industry edition, FTC Act Section 5, and SOC 2 commitments |
| Gap tables | `gap-analysis.csv` (Aircraft Parts: 143 rows, G-001 to G-110 for the 110 requirements and G-111 to G-143 for clause and regulation duties); `gap-analysis-engineering-services.csv` (35 rows); `gap-analysis-defense-software.csv` (36 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads with the Group CMMC program director and the division Empowered Officials; reviewed by group internal audit |

## 1. Applicability
### 1.1 Which rules reach which part of the group
- **DFARS 252.204-7012 applies now** to Aircraft Parts and Engineering Services: both hold DoD contracts and subcontracts with the clause and handle covered defense information. There is no small-business or size exemption, and the clause must be flowed down to subcontracts involving CDI, including for commercial products or services (252.204-7012(m)(1)).
- **CMMC Level 2 (C3PAO) applies from Phase 2 awards** (2026-11-10, 32 CFR 170.3(e)(2)). It applies at all tiers that process CUI (32 CFR 170.23). The group plans one assessment scope, the **Enterprise CUI Environment**, covering the GCEE, plants 1 to 8, the Engineering Services centers, and Defense Software's CUI support work. One scope means **one score**.
- **CMMC Level 3 (DIBCAC)** is expected for Program H from Phase 3 (2027-11-10, 32 CFR 170.3(e)(3)). Final Level 2 (C3PAO) status for the Level 3 scope is a prerequisite (170.18(a)(1)), and the Level 3 scope must equal or sit inside the Level 2 scope (170.19(e)).
- **The DoD edition (SYS-D3) is outside CMMC.** It is a Federal information system operated on behalf of DoD (32 CFR 170.3(b)). DFARS 252.204-7012(b)(1)(i) sends it to DFARS 252.239-7010 and the DoD Cloud Computing Security Requirements Guide.
- **The industry edition (SYS-D4) is a CSP to defense contractors.** Contractors that store CDI in it must ensure it meets security requirements equivalent to the FedRAMP Moderate baseline and complies with paragraphs (c) to (g) (252.204-7012(b)(2)(ii)(D)); 32 CFR 170.19(c)(2) applies the same rule to CMMC scoping. One of those contractors is the Aircraft Parts division.
- **NISPOM (32 CFR Part 117)** applies only at the two cleared Engineering Services centers.
- **SEC rules** apply to the group as a registrant.

### 1.2 Not applicable, with reasons
- **Plant 9 is outside the planned Level 2 scope** but not outside DFARS 252.204-7012, which applies to every covered contractor information system now. Its gaps are scored in the overall status column and excluded from the Level 2 scope score (`level2_scope_status`).
- **NISPOM for Aircraft Parts:** no facility clearance (G-143).
- **FTC Safeguards Rule, IRC 7216, HIPAA, and professional conduct rules** for Engineering Services: it is not a financial institution or tax preparer, handles no PHI, and is not a law or accounting firm (ES-G31 to ES-G34).
- **COPPA, CPNI, PADFA, and the rescinded OMB secure software attestation memos** for Defense Software (DS-G24 to DS-G27).
- **CIRCIA:** the final rule is not published; nothing is required yet.

## 2. Regulation-by-division matrix
| Requirement | Aircraft Parts | Engineering Services | Defense Software | Group (corporate) |
|---|---|---|---|---|
| C-DIB-R01 DFARS 252.204-7012 | **Primary.** Prime and subcontracts | Applies (N54-R05). Prime and subcontracts | (b)(1)(i) for the DoD edition (through 252.239-7010); CSP duties for SYS-D4 customers | Common controls; SOC; reporting support |
| C-DIB-R02 CMMC (32 CFR 170; 252.204-7021) | Level 2 (C3PAO) from Phase 2; Level 3 for Program H from Phase 3 | Level 2 (C3PAO) from Phase 2 | Level 2 for 3 subcontracts with CUI support work; DoD edition excluded (170.3(b)) | One Enterprise CUI Environment scope; CMMC program office |
| C-DIB-R03 DFARS 252.204-7019 and 7020 | Applies (DIBCAC High, 2024) | Applies (Basic, 2025) | Applies to its CMMC-scoped subcontracts | SPRS coordination |
| C-DIB-R04 FAR 52.204-21 | Applies (met by common controls) | Applies | Applies | ERP and corporate systems |
| C-DIB-R05 and R06 ITAR and EAR | Applies (registered) | Applies (registered; allied partner work) | Applies to export-controlled source code | Export compliance office |
| C-DIB-R07 NISPOM | Not applicable (no clearance) | **Applies at 2 cleared centers** | Not applicable | Entity-wide ITPSO |
| DFARS 252.239-7010 | Not applicable | Not applicable | **Applies to the DoD edition** | Supports through common controls |
| N51-R07 FedRAMP | Not applicable | Not applicable | DoD edition authorized; industry edition chooses the route to evidence equivalency | Provider A and suite authorizations relied on |
| N51-R01 FTC Act Section 5 | General | General | **Applies** (security claims) | General |
| N51-R04 DOJ Data Security Program | Not significant | Not significant | Precaution (government-related data) | Vendor screening |
| N51-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (registrant) |
| State breach notification laws | Employee data only | Employee data only | Customer contact data | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) |
| SOC 2 (contractual) | Not applicable (CMMC is the assurance) | Not applicable | **Industry edition Type 2** (P09) | Group services carved in |
| CIRCIA (proposed) | Tracked only | Tracked only | Tracked only | Tracked only |

## 3. Method
1. **Requirements.** The 110 SP 800-171 rows follow the official structure of NIST SP 800-171 Rev. 2 (families 3.1 to 3.14), with the CMMC identifier and the point value from the CMMC Scoring Methodology (32 CFR 170.24(c)(2)). Requirement text is quoted from the public-domain NIST publication. Clause and regulation rows cite the paragraph checked on eCFR (version date 2026-09-23). The Level 3 rows quote table 1 to 32 CFR 170.14(c)(4) for the seven requirements that 32 CFR 170.21(a)(3) keeps off a Level 3 POA&M. SOC 2 rows list criterion IDs with short labels in our own words.
2. **Crosswalk.** CSF 2.0 and SP 800-53 mappings for the 110 rows are derived from NIST's official mappings through each requirement's SP 800-171 Rev. 3 counterpart; the route through Rev. 3 is the author's (`crosswalk_source`). Other rows carry an author mapping.
3. **Evidence.** Interviews, configuration exports, document review, plant walkthroughs (plants 2, 4, 7, and 9), a field survey of 60 Engineering Services engineers, the SYS-D4 3PAO report, and P07 test results.
4. **Status and score.** Met, Partially met, Not met, or Not applicable. For CMMC scoring, a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)), so every Partially met row counts as NOT MET. `level2_scope_status` shows the status inside the planned Level 2 scope (Plant 9 excluded).

## 4. Results
### 4.1 Aircraft Parts: SP 800-171 Rev. 2 (`gap-analysis.csv`, rows G-001 to G-110)
| Family | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 3.1 Access Control | 19 | 3 | 0 | 0 |
| 3.2 Awareness and Training | 3 | 0 | 0 | 0 |
| 3.3 Audit and Accountability | 7 | 1 | 1 | 0 |
| 3.4 Configuration Management | 7 | 2 | 0 | 0 |
| 3.5 Identification and Authentication | 9 | 2 | 0 | 0 |
| 3.6 Incident Response | 3 | 0 | 0 | 0 |
| 3.7 Maintenance | 6 | 0 | 0 | 0 |
| 3.8 Media Protection | 6 | 3 | 0 | 0 |
| 3.9 Personnel Security | 2 | 0 | 0 | 0 |
| 3.10 Physical Protection | 4 | 2 | 0 | 0 |
| 3.11 Risk Assessment | 2 | 1 | 0 | 0 |
| 3.12 Security Assessment | 3 | 1 | 0 | 0 |
| 3.13 System and Communications Protection | 15 | 1 | 0 | 0 |
| 3.14 System and Information Integrity | 6 | 1 | 0 | 0 |
| **Total (110)** | **92** | **17** | **1** | **0** |

Of the 18 requirements not fully met, 8 are Plant 9 only (3.1.1, 3.5.3, 3.8.9, 3.10.3, 3.10.4, 3.11.2, 3.13.11, 3.14.1) and 10 are inside the planned Level 2 scope.

### 4.2 Aircraft Parts: clause and regulation duties (G-111 to G-143)
| Source | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| DFARS 252.204-7012 (cloud, special measures, reporting, malware, preservation, forensics, flowdown) | 7 | 3 | 0 | 0 |
| DFARS 252.204-7019 and 252.204-7020 | 1 | 2 | 0 | 0 |
| DFARS 252.204-7021 and 32 CFR Part 170, Level 2 (status, systems, flowdown, UIDs, scoping, ESPs, POA&M limits) | 0 | 4 | 3 | 0 |
| 32 CFR Part 170, Level 3 for Program H (prerequisite and the 7 non-POA&M requirements) | 2 | 4 | 2 | 0 |
| FAR 52.204-21 | 1 | 0 | 0 | 0 |
| ITAR and EAR | 2 | 1 | 0 | 0 |
| NISPOM | 0 | 0 | 0 | 1 |
| **Total (33)** | **13** | **14** | **5** | **1** |

Across all 143 Aircraft Parts rows, 19 carry a High gap risk, 16 Moderate, and 108 Low.

### 4.3 Score under 32 CFR 170.24
| Item | Aircraft Parts portion | Enterprise CUI Environment |
|---|---|---|
| Maximum score | 110 | 110 |
| Requirements NOT MET in the planned Level 2 scope | 10 (3.1.3, 3.1.20, 3.3.1, 3.3.4, 3.4.1, 3.4.9, 3.5.6, 3.8.7, 3.8.8, 3.12.4) | 14 (adds 3.1.21, 3.4.2, 3.8.6, 3.10.6 from Engineering Services) |
| Points subtracted | 23 (three at 5, one at 3, five at 1; 3.12.4 carries no point value) | 31 (adds 3.4.2 at 5 and three at 1) |
| **Score** | **87** | **79** |
| Minimum for Conditional Level 2 status | 88 (score / 110 of at least 0.8, 32 CFR 170.21(a)(2)(i)) | 88 |
| SPRS today | DIBCAC High Assessment, 98 (2024-06-07) | Engineering Services Basic Assessment, 101 (2025-03) |

**One scope, one score.** The Aircraft Parts portion alone is one point short of the Conditional threshold; Engineering Services' HPC hardening (3.4.2) and field gaps pull the shared scope to 79. Even at 88 or above, Conditional status would still be impossible today: a POA&M may hold only 1-point requirements (3.13.11 at 3 points only when encryption is used but not FIPS-validated), and never 3.1.20 or 3.12.4 (32 CFR 170.21(a)(2)(ii) and (iii)). **The plan is all 110 requirements Met in the scope by 2026-11-30**, with a POA&M only as a fallback for 1-point items. If the HPC cluster cannot be fixed in time, the group will carve it out of the scope and assess it later.

### 4.4 Engineering Services (`gap-analysis-engineering-services.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| SP 800-171 Rev. 2 (15 requirements where its evidence differs) | 6 | 9 | 0 | 0 |
| DFARS 252.204-7012, 7019, 7020, 7021 and 32 CFR Part 170 | 0 | 7 | 1 | 0 |
| FAR 52.204-21 | 1 | 0 | 0 | 0 |
| NISPOM (32 CFR 117.7, 117.8) | 4 | 1 | 0 | 0 |
| ITAR | 0 | 1 | 0 | 0 |
| Professional services rules (FTC Safeguards, IRC 7216, HIPAA, conduct rules) and CIRCIA | 0 | 0 | 0 | 5 |
| **Total (35)** | **11** | **18** | **1** | **5** |

All other SP 800-171 requirements rely on the same group common controls and the GCEE, which is why documenting inheritance for the HPC cluster and test systems (scenario gap 6) matters. **Not met:** no Level 2 (C3PAO) status yet (ES-G20). The field work gaps (3.1.3, 3.1.20, 3.1.21, 3.10.6; scenario gap 5) come from customer sites, where CUI moves between customer systems, GFE, and company laptops without a register. GFE inside company facilities is a Specialized Asset under 32 CFR 170.19(c)(1) and must be inventoried (ES-G22). The 2026-07 public chatbot pastes still need a documented reporting decision under 252.204-7012(c) and an export disclosure decision under 22 CFR 127.12 (ES-G29, ES-G30).

### 4.5 Defense Software (`gap-analysis-defense-software.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| DFARS 252.239-7010 (DoD edition) | 7 | 4 | 1 | 0 |
| DFARS 252.204-7012 ((b)(1)(i); CSP equivalency and (c) to (g) duties for SYS-D4) | 1 | 1 | 1 | 0 |
| CMMC (170.3(b) exclusion; 252.204-7021 for 3 subcontracts) | 0 | 1 | 0 | 1 |
| FedRAMP, FTC Act, DOJ Data Security Program, SEC | 3 | 1 | 1 | 1 |
| COPPA, CPNI, PADFA, secure software attestation | 0 | 0 | 0 | 4 |
| SOC 2 commitments (industry edition) | 2 | 7 | 0 | 0 |
| **Total (36)** | **13** | **14** | **3** | **6** |

**Not met:**
- **252.239-7010(c)(2):** DoD edition telemetry (Government-related data) was used in 2026-05 to retrain the model sold in the industry edition, without Contracting Officer approval.
- **252.204-7012(b)(2)(ii)(D) and 32 CFR 170.19(c)(2):** SYS-D4 has not shown FedRAMP Moderate equivalency (23 open 3PAO findings). DoD CIO guidance on what equivalency requires could not be retrieved for verification on 2026-10-04 (access denied), so this analysis relies only on the clause text; the division's chosen route is a FedRAMP Moderate authorization, which removes doubt.
- **FTC Act Section 5:** "FedRAMP-ready" and "CMMC compliant" claims are not substantiated.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Score below 88; non-POA&M items open (gaps 1, 2, 5, 6, 10) | AP, ES, DS | 32 CFR 170.21(a)(2); 252.204-7021(d)(1) | High | Close all 14 NOT MET requirements in the scope by 2026-11-30; readiness re-check; C3PAO window 2026-12-07 | Group CMMC program director | 2026-12-18 |
| 2 | SYS-D4 used for CUI without FedRAMP Moderate equivalency (4) | AP, DS | 252.204-7012(b)(2)(ii)(D); 32 CFR 170.19(c)(2); 3.1.20 | High | Aircraft Parts moves its CUI to the GCEE; Defense Software closes 23 findings and pursues authorization; written notices to CUI tenants | Defense Software president; Aircraft Parts VP of supply chain | 2026-11-30 (move); 2027-06-30 (authorization) |
| 3 | Government-related data reuse | DS | 252.239-7010(c)(2) | High | Stop reuse; retrain; data-use gate; counsel-led disclosure to Contracting Officers | Defense Software president | 2026-11-30 |
| 4 | Supplier status and flowdown at scale (3) | AP, ES | 252.204-7012(m)(1); 252.204-7020(g)(2); 252.204-7021(f); 32 CFR 170.23 | High | Verify SPRS and CMMC status before release; amend about 115 supplier orders and 46 subconsultant agreements | Group supply chain risk director | 2027-03-31 |
| 5 | Plant 9 (1) | AP | 252.204-7012(b)(2); 252.204-7021(d)(2) | High | Interim MFA, FIPS VPN, encrypted backups, visitor system; migration into the GCEE; no Phase 2 CUI work until then | Aircraft Parts VP of operations | 2027-03-31 |
| 6 | Multi-regulator reporting not exercised; no Defense Software certificate holder (8) | All | 252.204-7012(c)(1)(ii), (c)(3); 252.239-7010(d); 32 CFR 117.8(b) | High | Certificates for Defense Software and two more Engineering Services centers; cross-division tabletop 2026-11-18 | Group General Counsel | 2026-11-18 |
| 7 | Unsupported security claims | DS | FTC Act Sec. 5 | Moderate | Withdraw claims; legal review | Defense Software general counsel | 2026-10-31 |
| 8 | Program H Level 3 readiness (11) | AP | 32 CFR 170.18(a)(1); 170.21(a)(3) | Moderate | Threat-informed risk assessment, solution rationale, OT supply chain plan, Program H cell network | Program H chief engineer | 2027-09-30 |
| 9 | Supplement drift and AI use (7, 9) | ES | 3.1.21; 22 CFR 120.56, 127.12 | Moderate | Re-issue the supplement; document the chatbot reporting and disclosure decisions | Engineering Services security and compliance lead | 2026-11-30 |
| 10 | Adverse information not linked to CUI access | ES | 32 CFR 117.8(c) | Moderate | FSO-to-identity referral step | Group ITPSO | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-003 to POAM-009, POAM-014 to POAM-018, and POAM-020 to POAM-023 trace to this analysis).

## 6. Pending regulatory changes
- **SP 800-171 Rev. 3:** published by NIST, but CMMC Level 2 is fixed to Rev. 2 (32 CFR 170.14(c)(3)). Each SP 800-171 row names its Rev. 3 counterpart in `pending_rule_change` for later planning. Rev. 3 is not a current obligation.
- **FAR CUI rule:** proposed (90 FR 4278, 2025-01-15) and not final. DFARS 252.204-7012 remains the governing clause.
- **Revolutionary FAR Overhaul:** a proposed rule (FR Doc. 2026-12559, 2026-06-23) would renumber FAR clauses, including 52.204-21. Not final.
- **CIRCIA:** the final rule is not published as of 2026-09-25. Proposed reporting deadlines are not treated as current obligations.
- **CMMC phases:** Phase 3 (2027-11-10) brings Level 2 (C3PAO) to option periods and Level 3 (DIBCAC) to applicable awards; Phase 4 (2028-11-10) is full implementation (32 CFR 170.3(e)). These are scheduled, not pending, and drive the roadmap dates.

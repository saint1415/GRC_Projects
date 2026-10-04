# Regulatory Gap Analysis: Cris Santos Company Holdings | Wholesale Trade | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Wholesale Trade (focus division: IT Distribution) |
| Primary regulation | NIST SP 800-171 Rev. 2 (110 requirements), required by DFARS 252.204-7012(b)(2) and assessed for CMMC Level 2 (32 CFR 170.14(c)(3)), for the IT Distribution CUI environment |
| Division regulations | Logistics: FCI and physical protection duties that support the CUI environment, CTPAT (voluntary), 3PL contract commitments. Online Retail: PCI DSS v4.0.1 (contractual), the INFORM Consumers Act, and CCPA/CPRA with the CPPA regulations |
| Gap tables | `gap-analysis.csv` (IT Distribution: 141 rows, G-001 to G-110 for the 110 requirements and G-111 to G-141 for clause duties); `gap-analysis-logistics.csv` (24 rows); `gap-analysis-online-retail.csv` (59 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads with the Group CMMC program director, the Online Retail PCI compliance manager, and the Group Chief Privacy Officer; reviewed by group internal audit |

## 1. Applicability
### 1.1 Which rules reach which part of the group
- **DFARS 252.204-7012 applies now to IT Distribution's integration work.** The subcontracts with Primes A to F contain the clause, and performance involves covered defense information (CUI-marked configuration documents). There is no size exemption. Paragraph (b)(2) requires SP 800-171 on every covered contractor information system, which today includes the commercial ERP and collaboration tenant, because CUI was found in them.
- **CMMC Level 2 (C3PAO) applies from Phase 2 awards** (2026-11-10, 32 CFR 170.3(e)(2)) to subcontractors at all tiers that process CUI, when the prime contract requires it (32 CFR 170.23(a)(3)). DFARS 252.204-7021(d)(1) and (d)(2) then require a current status for every system that handles the CUI. The first option period that needs it starts 2027-04-01.
- **The COTS exclusion matters at this size.** About 70% of Federal Solutions revenue is orders exclusively for COTS products. Those carry FAR 52.204-25 but no CMMC requirement (32 CFR 170.3(c)), and FAR 52.204-21 excludes COTS subcontracts. The integration work is not COTS-only, so it carries both.
- **FAR 52.204-21 and Level 1 (Self)** apply to the FCI systems (ERP, EDI hub, WMS) used for integration subcontracts and DoD shipments. Logistics runs the WMS, so its handhelds are in scope.
- **Logistics provides physical protection for CUI Assets.** IC-1 and IC-2 sit inside DC-1 and DC-6; their badge and camera systems are Security Protection Assets (32 CFR 170.19(c)), and SP 800-171 family 3.10 is met partly by Logistics.
- **PCI DSS applies to Online Retail by contract.** Its acquirer classifies it as a Level 1 merchant and requires an annual ROC by a QSA. PCI DSS is an industry standard, not law. The reseller portal's card payments use a hosted payment page, so IT Distribution files only an annual self-assessment questionnaire.
- **The INFORM Consumers Act** applies because Online Retail operates an online marketplace with high-volume third-party sellers (15 U.S.C. 45f(f)(3): 200 or more sales and $5,000 or more in gross revenue in a continuous 12-month period within the prior 24 months).
- **CCPA/CPRA applies to the group** as a business (revenue far above the CPI-adjusted threshold). The cybersecurity audit applies because the revenue test is met and personal information of 250,000 or more consumers is processed; the first report is due 2028-04-01 because 2026 revenue exceeds $100 million (Cal. Code Regs. tit. 11, 7121(a)(1)).
- **SEC rules** apply to the group as a registrant.

### 1.2 Not applicable, with reasons
- **USCG maritime cybersecurity rule (33 CFR Part 101, Subpart F):** Logistics owns or operates no vessel or MTSA-regulated facility (LW-G21).
- **TSA security directives and DOT 49 U.S.C. 41712:** no rail, pipeline, aviation, or ticket agent operations (LW-G22, LW-G23).
- **FTC Safeguards Rule and Red Flags Rule:** Online Retail extends no consumer credit and offers no covered accounts; third-party lenders finance purchases (OR-G56, OR-G57).
- **FACTA receipt truncation and COPPA:** no printed point-of-sale receipts; no service directed to children (OR-G58, OR-G59).
- **CPPA ADMT rules:** no ADMT is used today for a "significant decision" as the regulation defines it; re-check before 2027-01-01 (OR-G53).
- **SP 800-171 3.13.5:** no publicly accessible component is inside the CUI environment (G-092).
- **CIRCIA:** the final rule is not published; nothing is required yet.

## 2. Regulation-by-division matrix
| Requirement | IT Distribution | Logistics | Online Retail | Group (corporate) |
|---|---|---|---|---|
| N42-R03 DFARS 252.204-7012 | **Primary.** Integration subcontracts with Primes A to F | Physical protection of IC-1 and IC-2; WMS kept free of CUI | Not applicable | Common controls; SOC; reporting support |
| N42-R02 CMMC (32 CFR 170; 252.204-7021) | Level 2 (C3PAO) from Phase 2; Level 1 (Self) for FCI systems | DC-1 and DC-6 badge systems in the Level 2 scope; WMS in the Level 1 scope | Not applicable | Group CMMC program office |
| DFARS 252.204-7019, -7020; 252.246-7008 | Applies (SPRS; electronic parts sourcing) | Receiving traceability supports 7008(c) | Not applicable | Supply chain risk office |
| N42-R04 FAR 52.204-21 | Applies (integration subcontracts) | Applies (WMS handles DoD shipment FCI) | Not applicable | ERP and EDI hub |
| N42-R05 FAR 52.204-25 (Section 889) | Applies (all DoD orders, including COTS) | Not applicable directly | Not applicable (commercial sales); the group checks marketplace electronics voluntarily | Screening list |
| N42-R06 / N48-49-R05 CTPAT (voluntary) | Supports through supplier due diligence | **Applies** (importer program operated by Logistics) | Not applicable | Trade compliance office |
| N48-49-R01 to R04, R06 (USCG, TSA, DOT) | Not applicable | Not applicable (no regulated operations) | Not applicable | Not applicable |
| N44-45-R01 PCI DSS v4.0.1 | Hosted payment page; annual self-assessment questionnaire | Not applicable | **Applies** (Level 1 merchant; ROC) | Common controls in the responsibility matrix |
| N44-45-R08 INFORM Consumers Act | Not applicable | Not applicable | **Applies** (online marketplace) | Not applicable |
| N42-R08 / N44-45-R06 CCPA/CPRA and CPPA regulations | Reseller contact data | Employee data (no California DCs) | **Applies** (consumers; sharing for advertising) | Group privacy program; cybersecurity audit 2028 |
| N44-45-R03 to R05, R07 (Safeguards, Red Flags, FACTA, COPPA) | Not applicable | Not applicable | Not applicable (reasons in 1.2) | Not applicable |
| N42-R01 / N44-45-R02 FTC Act Section 5 | General | General | **Applies** (consumer security and AI claims) | General |
| N42-R07 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (registrant) |
| State breach notification laws | Reseller contacts, employees | Employees, drivers | Consumers in every state | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) |
| SOC 2 (contractual) | Lifecycle Services ITAD (P09) | 3PL fulfillment (P09) | Not applicable (PCI DSS is the assurance) | Group services carved in |

## 3. Method
1. **Requirements.** The 110 SP 800-171 rows follow the official structure of NIST SP 800-171 Rev. 2 (families 3.1 to 3.14), with the CMMC identifier and the point value under the CMMC Scoring Methodology (32 CFR 170.24). Clause and regulation rows cite paragraphs read on eCFR (version date 2026-09-23), the U.S. Code for 15 U.S.C. 45f, and the CPPA's approved regulation text. PCI DSS rows list requirement IDs with short topic labels written for this analysis; the standard's text is not reproduced. CTPAT rows use topic labels for the cybersecurity, business partner, and risk assessment sections of the Minimum Security Criteria without criterion numbers.
2. **Crosswalk.** SP 800-53 controls for the 110 rows come from the official SP 800-171 Rev. 2 Appendix D mapping (Rev. 4 IDs), refined to Rev. 5 by the author; CSF 2.0 subcategories are derived from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference. All other rows carry an author mapping, labeled in `crosswalk_source`.
3. **Evidence.** Interviews, configuration exports, a CUI discovery scan of the ERP and the commercial collaboration tenant (2026-06-22), an item master extract (2026-07-14), a call recording sample (2026-07), the marketplace verification queue (2026-07-20), DC walkthroughs (DC-1, DC-6, DC-8), and P07 test results.
4. **Status and score.** Met, Partially met, Not met, or Not applicable. For CMMC scoring, a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)), so every Partially met row counts as NOT MET. Not applicable rows score as MET.

## 4. Results
### 4.1 IT Distribution: SP 800-171 Rev. 2 (`gap-analysis.csv`, G-001 to G-110)
| Family | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 3.1 Access Control | 19 | 3 | 0 | 0 |
| 3.2 Awareness and Training | 3 | 0 | 0 | 0 |
| 3.3 Audit and Accountability | 9 | 0 | 0 | 0 |
| 3.4 Configuration Management | 8 | 1 | 0 | 0 |
| 3.5 Identification and Authentication | 11 | 0 | 0 | 0 |
| 3.6 Incident Response | 1 | 2 | 0 | 0 |
| 3.7 Maintenance | 6 | 0 | 0 | 0 |
| 3.8 Media Protection | 9 | 0 | 0 | 0 |
| 3.9 Personnel Security | 2 | 0 | 0 | 0 |
| 3.10 Physical Protection | 5 | 1 | 0 | 0 |
| 3.11 Risk Assessment | 2 | 1 | 0 | 0 |
| 3.12 Security Assessment | 3 | 1 | 0 | 0 |
| 3.13 System and Communications Protection | 14 | 1 | 0 | 1 |
| 3.14 System and Information Integrity | 7 | 0 | 0 | 0 |
| **Total (110)** | **99** | **10** | **0** | **1** |

The program is mature inside the enclave. The 10 requirements not fully met (5 Basic, 5 Derived; 5 High and 5 Moderate gap risk) come from three causes: CUI outside the FFE (3.1.1, 3.1.3, 3.1.20), the IC-2 lab network (3.4.1, 3.11.2, 3.13.1), and cross-division response and physical controls (3.6.2, 3.6.3, 3.10.3, 3.12.4).

### 4.2 IT Distribution: clause duties (G-111 to G-141)
| Source | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FAR 52.204-21 (CMMC Level 1) | 12 | 3 | 0 | 0 |
| FAR 52.204-25 (Section 889) | 0 | 3 | 0 | 0 |
| DFARS 252.246-7008 | 1 | 3 | 0 | 0 |
| DFARS 252.204-7012 (cloud, reporting, preservation, flowdown) | 2 | 1 | 1 | 0 |
| DFARS 252.204-7019 and -7020 | 0 | 1 | 0 | 0 |
| DFARS 252.204-7021 and 32 CFR Part 170 | 0 | 3 | 1 | 0 |
| **Total (31)** | **15** | **14** | **2** | **0** |

Across all 141 IT Distribution rows, 114 are Met, 24 Partially met, 2 Not met, and 1 Not applicable; 11 carry a High gap risk and 15 Moderate.

**Not met:** 252.204-7012(b)(2)(ii)(D) (CUI in the commercial ERP and collaboration tenant, which have no FedRAMP Moderate equivalency evidence; G-133) and 252.204-7021(d)(1) (no Level 2 (C3PAO) status yet; G-138).

### 4.3 Score under 32 CFR 170.24
| Item | Value |
|---|---|
| Maximum score | 110 |
| Requirements NOT MET | 10 (3.1.1, 3.1.3, 3.1.20, 3.4.1, 3.6.2, 3.6.3, 3.10.3, 3.11.2, 3.12.4, 3.13.1) |
| Points subtracted | 29 (five at 5 points, four at 1 point; 3.12.4 is not scored because without an SSP the assessment cannot proceed) |
| **Score for the full CUI environment** | **81** |
| Minimum for Conditional Level 2 status | 88 (32 CFR 170.21(a)(2)(i)) |
| SPRS today | Basic Assessment 104 (2025-04-11), FFE servers only |

**What the score means.** Even above 88, Conditional status would not be possible today: a POA&M may hold only 1-point requirements, and never 3.1.20, 3.1.22, 3.10.3, 3.10.4, 3.10.5, or 3.12.4 (32 CFR 170.21(a)(2)(ii) and (iii)). Of the 10 NOT MET requirements, only 2 (3.1.3 and 3.6.3) could go on a CMMC POA&M. **The plan is all 110 requirements Met by 2026-12-15**, ahead of the C3PAO window starting 2027-01-11, with a POA&M only as a fallback for those two. The 2025 SPRS score of 104 is not supported for the full environment; counsel advises posting a corrected Basic Assessment (G-137).

### 4.4 Logistics (`gap-analysis-logistics.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| SP 800-171 3.10 for DC buildings around IC-1 and IC-2 | 4 | 1 | 0 | 0 |
| 32 CFR 170.19(c) Security Protection Assets | 0 | 1 | 0 | 0 |
| FAR 52.204-21 (FCI in DoD shipments) | 1 | 2 | 0 | 0 |
| CTPAT Minimum Security Criteria (voluntary) | 0 | 6 | 0 | 0 |
| 3PL client agreements | 0 | 3 | 0 | 0 |
| FTC Act, state breach laws, SEC | 2 | 1 | 0 | 0 |
| USCG, TSA, DOT | 0 | 0 | 0 | 3 |
| **Total (24)** | **7** | **14** | **0** | **3** |

Logistics has no sector cyber regulator for its operations. Its obligations come through the CUI environment it houses, the FCI in DoD shipments, a voluntary program, and client contracts. The weak points are the acquired DCs (shared handheld logins, unsupported devices), DC automation (vendor tunnels, flat networks, backups), and undocumented inheritance from group controls, which also blocks the 3PL SOC 2 description (P09).

### 4.5 Online Retail (`gap-analysis-online-retail.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| PCI DSS v4.0.1 (39 requirement rows) | 28 | 10 | 1 | 0 |
| INFORM Consumers Act (15 U.S.C. 45f) | 5 | 3 | 1 | 0 |
| CCPA/CPRA and CPPA regulations | 1 | 2 | 1 | 1 |
| FTC Act Section 5 and state breach laws | 2 | 0 | 0 | 0 |
| FTC Safeguards, Red Flags, FACTA, COPPA | 0 | 0 | 0 | 4 |
| **Total (59)** | **36** | **15** | **3** | **5** |

**Not met:**
- **PCI DSS 3.3.1:** sensitive authentication data (spoken security codes) is stored in contact center call recordings. This would make the November 2026 ROC non-compliant unless fixed first (OR-G06; POAM-017).
- **15 U.S.C. 45f(a)(2):** 46 high-volume sellers past the 10-day verification window (OR-G43; POAM-023).
- **Cal. Code Regs. tit. 11, 7150:** no risk assessment yet for sharing personal information or for sensitive personal information (OR-G52; deadline for pre-existing processing 2027-12-31).

Payment page script management and tamper detection (6.4.3, 11.6.1) cover 1 of 3 storefront brands; both are High because they are the main defense against web skimming (P01 OR-001).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | CUI outside the FFE; ERP and commercial tenant without equivalency (1) | ID | 252.204-7012(b)(2)(ii)(D); 3.1.1, 3.1.3, 3.1.20 | High | Purge, attachment block, DLP, prime exchange in the government-community tenant | Group CMMC program director | 2026-12-15 |
| 2 | Score 81 and non-POA&M items open; unsupported SPRS entry (1) | ID, LW | 32 CFR 170.21(a)(2); 252.204-7019/-7020; 252.204-7021(d)(1) | High | Close all 10 NOT MET requirements; corrected SPRS entry; C3PAO assessment | Group CMMC program director; IT Distribution president | 2027-01-22 |
| 3 | IC-2 lab network route, inventory, and scanning | ID | 3.4.1, 3.11.2, 3.13.1 | High | Remove the route; automated discovery; monthly scans | Integration center managers | 2026-10-31 |
| 4 | Section 889 screening gaps and broker flowdown (2) | ID, OR | 52.204-25(b)(1), (e); 252.246-7008(e) | High | Mandatory manufacturer of record; block for refurbished stock; broker terms | Group supply chain risk director | 2026-12-31 |
| 5 | Receiving serial validation and traceability (3) | LW, ID | 252.246-7008(c); CTPAT business partner criteria | Moderate | Serial capture and OEM validation at all 9 DCs | Logistics vice president of operations | 2027-03-31 |
| 6 | Card data in call recordings; payment page scripts (4) | OR | PCI DSS 3.2.1, 3.3.1, 3.5.1, 6.4.3, 11.6.1, 12.5.2 | High | Automatic pause, keypad entry, purge; script controls on all brands; scope re-confirmation before ROC fieldwork | Online Retail PCI compliance manager | 2026-11-30 |
| 7 | Marketplace verification and seller data (5) | OR | 15 U.S.C. 45f(a)(1)(C), (a)(2), (a)(3), (a)(4) | Moderate | Clear the backlog; automate suspension; restrict seller financial data | Online Retail marketplace director | 2026-12-31 |
| 8 | DC automation and acquired DCs (6, 7) | LW | CTPAT cybersecurity criteria; 52.204-21(b)(1)(i), (xii); 3PL agreements | High | PAM-brokered vendor access; OT segmentation and backups; handheld replacement; client MFA | Logistics vice president of operations | 2027-06-30 |
| 9 | Logistics inheritance and supplement drift (8, 9) | LW | 3PL assurance exhibit; POL-01 4.5 | Moderate | Inheritance matrix; re-issue the supplement | Logistics security and compliance lead | 2026-12-31 |
| 10 | Cross-division reporting readiness (10) | All | 252.204-7012(c); 52.204-25(d); Form 8-K Item 1.05 | High | Two more certificate holders; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 11 | CCPA cybersecurity audit and risk assessments (12) | OR, group | Cal. Code Regs. tit. 11, 7120-7121, 7150 | Moderate | Audit plan for the 2027 period; risk assessments | Group Chief Privacy Officer | 2027-06-30 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). The gap rows cite POAM-001 to POAM-012, POAM-014 to POAM-018, POAM-020, and POAM-022 to POAM-027 in their remediation actions. Five items were raised by this analysis itself (POAM-022 to POAM-024, POAM-026, and POAM-027); the others came from the P07 assessment or, for POAM-025, the P10 AI assessment.

## 6. Pending regulatory changes
These are **proposed** or scheduled and are not treated as current obligations.
- **Revolutionary FAR Overhaul, parts 1, 2, 4, 33, 39, 40, 52, and 53** (FR Doc. 2026-12559, 2026-06-23; comments closed 2026-07-23). If finalized as proposed, a new FAR 52.240-7 CUI clause would require NIST SP 800-171 Rev. 3 with DoD organization-defined parameters, and a new 52.240-3 would consolidate security prohibitions, including Section 889, with a 72-hour reporting standard. Rows affected are flagged in `pending_rule_change`. Not final.
- **SP 800-171 Rev. 3:** published by NIST, but CMMC Level 2 is fixed to Rev. 2 (32 CFR 170.14(c)(3)).
- **CMMC phases:** Phase 3 (2027-11-10) and Phase 4 (2028-11-10) are scheduled in 32 CFR 170.3(e), not pending; they drive dates for later option periods.
- **CIRCIA:** the final rule is not published as of 2026-09-25. Proposed deadlines are not current obligations.
- **PCI DSS:** the PCI Security Standards Council ran a request for comments (June to July 2026) on v4.0.1 toward the next version; v4.0.1 remains current.

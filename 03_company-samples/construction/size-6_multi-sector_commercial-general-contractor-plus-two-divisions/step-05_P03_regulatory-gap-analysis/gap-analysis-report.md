# Regulatory Gap Analysis: Cris Santos Company Holdings | Construction | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Construction (focus division: Commercial Construction) |
| Primary regulation | FAR 52.204-21 Basic Safeguarding, verified through CMMC Level 1 (Self) for the PDPP; escalating to NIST SP 800-171 R2, DFARS 252.204-7012, and CMMC Level 2 for the CUI enclave (SYS-G6) |
| Division regulations | A&E: DFARS 252.204-7012, NIST SP 800-171 R2, and CMMC Level 2 (shared enclave), plus FAR 52.204-21 on civilian work. Property: PCI DSS v4.0.1 for parking payments and FTC Act Section 5; the FTC Safeguards Rule tested for applicability. Group: SEC disclosure, state breach laws, OFAC |
| Gap tables | `gap-analysis.csv` (Construction, 42 rows); `gap-analysis-cui-enclave.csv` (all 110 NIST SP 800-171 R2 requirements, shared by Construction and A&E); `gap-analysis-ae.csv` (22 rows); `gap-analysis-property.csv` (20 rows); `gap-analysis-group.csv` (10 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment and enclave pre-assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads and the Director of Federal Contracts Compliance, with outside government contracts counsel; enclave rows scored by group internal audit's independent pre-assessment |
| Approved | 2026-09-15 by the board risk committee (with the P01 registers) |

## 1. Applicability
### 1.1 Who holds which obligation
Each operating subsidiary contracts in its own name, so obligations attach to the entity, not to the holding company (`../00_company-facts.md` section 7).

| Entity | Federal contract position | CMMC position | Basis |
|---|---|---|---|
| Cris Santos Construction, LLC | 212 federal awards: 151 civilian, 61 DoD. CUI on 23 DoD contracts. 13 awards since 2025-11-10 carry DFARS 252.204-7021 (9 Level 1, 4 Level 2) | Organization seeking assessment. Final Level 1 (Self) for the PDPP (2026-01-20); Final Level 2 (Self) for the enclave (2026-03-16). Affirming Official: Construction division president | FAR 52.204-21; DFARS 252.204-7012, -7019, -7020, -7021; 32 CFR 170.15, 170.16, 170.22 |
| Cris Santos Design, Inc. (A&E) | 88 federal architect-engineer awards; 47 DoD awards with CUI; subcontractor to Construction on 6 design-build projects | Organization seeking assessment for the same enclave. Final Level 2 (Self), 2026-03-16. Affirming Official: A&E division president | Same; 252.204-7012(m) as a subcontractor |
| Cris Santos Properties, LLC | 9 properties leased to federal agencies through GSA lease contracts | None today | Lease security terms (contractual); clause incorporation under counsel review |
| Corporate shared services | Operates the PDPP and the enclave for both contracting entities | External service provider in CMMC terms (same corporate family) | 32 CFR 170.19(c) scoping |
| Holding company | SEC registrant | n/a | 17 CFR 229.106; Form 8-K Item 1.05 |

**No size exemption applies.** FAR 52.204-21, FAR 52.204-25, DFARS 252.204-7012, and the CMMC rule apply regardless of size. The group is far above the SBA size standard (`../README.md`).

### 1.2 Why the analysis escalates from Level 1 to Level 2
FAR 52.204-21 sets 15 basic requirements for any system that holds FCI. The PDPP holds FCI on all federal jobs, so its CMMC Level 1 (Self) status is what DoD relies on. CUI is different: DFARS 252.204-7012(b)(2) requires NIST SP 800-171 on covered contractor information systems, (b)(2)(ii)(D) requires FedRAMP Moderate or equivalent for cloud services that store CUI, and DFARS 252.204-7021(d)(2) allows CUI only on systems with the required CMMC status. The group built the enclave for that purpose. The analysis therefore covers both scopes, and the most important finding is that CUI crossed from the Level 2 scope into the Level 1 scope (scenario gap 1).

### 1.3 Excluded requirements, with reasons
- **NIST SP 800-171 R2 3.8.6 and 3.13.5** in the enclave: not applicable (no digital CUI media transported; no publicly accessible enclave components). Both are recorded with reasons, as 32 CFR 170.24 expects.
- **DFARS 252.204-7012(b)(2)(ii)(B)-(C)** (alternative security measures and DoD CIO adjudication) for A&E: no alternative measures have been requested.
- **FTC Safeguards Rule (16 CFR Part 314):** neither Property nor A&E is a "financial institution" under 16 CFR 314.2. Commercial leasing to businesses and architecture and engineering services are not listed financial activities, and neither division has consumer customers.
- **HIPAA:** no division holds PHI. The group designs and builds health care facilities, but contracts exclude PHI and site surveys use escorts.
- **IRC 7216, ABA Model Rules, AICPA Code:** the A&E division provides no tax, legal, or accounting services.
- **CCPA/CPRA and Colorado SB26-189:** no California or Colorado operations; no AI tool makes consequential decisions about individuals in those states.
- **CIRCIA:** the final rule was not published as of 2026-09-25. Nothing in it is treated as a current obligation.

## 2. Regulation-by-division matrix
| Requirement | Construction (focus) | Property | A&E | Group (corporate) |
|---|---|---|---|---|
| N23-R01 FAR 52.204-21 | **Primary.** All 212 federal awards; PDPP is the Level 1 scope | Not applicable (no FAR supply or service contracts; leases are under counsel review) | Applies (N54-R04): 41 civilian awards rely on the same group common controls | Operates the PDPP and common controls |
| N23-R02 FAR 52.204-25 (Section 889) | Applies: TSSI installs video and access control at federal sites; annual SAM representation | Applies by group policy; lease clause incorporation unverified. 46 covered cameras found at 2 federally leased properties (P07) | Applies to its own systems and, through specifications, to design-build deliveries | Group approved-manufacturer list (POAM-029) |
| N23-R03 DFARS 252.204-7012, -7019, -7020 | Applies: 61 DoD awards, CUI on 23 | Not applicable | Applies (N54-R05): 47 DoD awards with CUI; subcontractor duties on design-build | Enclave operator; DIBNet reporting capability |
| N23-R04 CMMC (32 CFR 170; DFARS 252.204-7021) | Applies: Level 1 (PDPP) and Level 2 (enclave); subcontractor checks | Not applicable | Applies (N54-R05): Level 2 (enclave); subconsultant checks | Director of Federal Contracts Compliance runs scoping and SPRS for both entities |
| FAR 52.232-33 (SAM EFT data); 52.232-27 (prompt payment of subcontractors) | Applies (payment fraud exposure) | Not applicable | Applies (federal invoices) | Payment factory |
| FAR 52.222-8 (certified payroll) | Applies on covered federal construction | Not applicable | Not applicable | Group payroll |
| N53-R04 PCI DSS v4.0.1 | Not applicable | **Primary for Property**: merchant for parking revenue at 18 facilities | Not applicable | SOC monitoring of garage networks |
| N53-R01 / N54-R01 FTC Safeguards Rule | Not applicable | Not applicable (not a financial institution) | Not applicable | n/a |
| N53-R02 FTC Act Section 5 | Applies (general) | Applies: tenant portal security statements | Applies: digital twin service claims | Applies |
| N53-R03 CCPA/CPRA | Not applicable (no California operations) | Not applicable | Not applicable | Revisit on entry |
| N54-R06 HIPAA as business associate | Not applicable | Not applicable | Not applicable (no PHI) | Not applicable |
| N54-R09 / CIRCIA | Tracked only (proposed) | Tracked only | Tracked only | Tracked only |
| N53-R05 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Each state where affected individuals reside (Fla. Stat. 501.171 worked example): certified payrolls, employee data | Same: badge holder and tenant contact data | Same: employee data | Coordinates the notification matrix (P08) |
| SOC 2 (contractual) | TSSI managed service (P09) | Not in scope (P09) | Digital twin service (P09) | Group services carved in |

## 3. Method
1. **Requirements.** FAR and DFARS clauses and 32 CFR Part 170 were read from the eCFR (current through 2026-09-23). The 110 NIST SP 800-171 R2 requirements and their basic or derived type come from NIST's dataset in the Cybersecurity and Privacy Reference Tool. PCI DSS rows list requirement numbers with short topic labels in the author's own words; the standard's text is not reproduced.
2. **Crosswalk.** For the 15 FAR requirements and the 110 enclave requirements the mapping is **official** where NIST provides it: FAR to SP 800-171 R2 through 32 CFR 170.15 Table 2, R2 to Rev. 3 through NIST's withdrawal notes, CSF 2.0 through NIST's CSF 2.0 to SP 800-171 Rev. 3 mapping, and SP 800-53 through the Rev. 3 source controls. Where NIST lists no CSF 2.0 subcategory, the row says so and uses an author mapping. All other rows carry an **author mapping**, labeled in the `crosswalk_source` column.
3. **Evidence.** Interviews, document review, configuration exports, the 2026-07-14 CUI discovery scan, contract and subcontract samples, and P07 test results. Enclave rows use group internal audit's independent pre-assessment against every NIST SP 800-171A objective.
4. **Status.** Met, Partially met, Not met, or Not applicable. For CMMC purposes a requirement is MET only if every objective is met, so "Partially met" is scored as NOT MET in the enclave score (32 CFR 170.24).

## 4. Results
### 4.1 Construction (`gap-analysis.csv`)
| Regulation | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FAR 52.204-21 (15 requirements, (b)(2) and (c)) | 16 | 3 | 0 | 0 | 19 |
| CMMC program duties (32 CFR 170; DFARS 252.204-7021) | 2 | 4 | 4 | 0 | 10 |
| FAR 52.204-25 and related representations | 3 | 2 | 0 | 0 | 5 |
| DFARS 252.204-7012 | 3 | 2 | 1 | 0 | 6 |
| DFARS 252.204-7019 and -7020 | 1 | 0 | 0 | 0 | 1 |
| FAR 52.232-33 (SAM EFT data) | 0 | 1 | 0 | 0 | 1 |
| **Total** | **25** | **12** | **5** | **0** | **42** |

Open rows by risk: 10 High, 5 Moderate, 2 Low.

**Level 1 (PDPP).** 13 of the 15 basic requirements are met. Two are not fully met: stale external accounts (G-001, 3,800 accounts from closed projects) and visitor control in jobsite trailers (G-009). Level 1 allows no POA&M (32 CFR 170.21(a)(1)), so both must close before the 2027-01-20 annual affirmation (G-021). Counsel is reviewing what the July findings mean for the January affirmation (G-023, decision due 2026-10-31).

**Not met (5):** CUI on systems without the required Level 2 status (G-024); no CMMC status check before subcontract award (G-026; DFARS 252.204-7021(f)(2)); the enclave is not ready for a Level 2 (C3PAO) assessment (G-028); even a Conditional Level 2 status is not available yet (G-029); and CUI held in cloud services that are not FedRAMP Moderate authorized or equivalent (G-036).

### 4.2 CUI enclave, NIST SP 800-171 R2 (`gap-analysis-cui-enclave.csv`)
| Family | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 3.1 Access Control | 20 | 1 | 1 | 0 | 22 |
| 3.2 Awareness and Training | 2 | 1 | 0 | 0 | 3 |
| 3.3 Audit and Accountability | 8 | 1 | 0 | 0 | 9 |
| 3.4 Configuration Management | 8 | 1 | 0 | 0 | 9 |
| 3.5 Identification and Authentication | 11 | 0 | 0 | 0 | 11 |
| 3.6 Incident Response | 3 | 0 | 0 | 0 | 3 |
| 3.7 Maintenance | 6 | 0 | 0 | 0 | 6 |
| 3.8 Media Protection | 7 | 1 | 0 | 1 | 9 |
| 3.9 Personnel Security | 2 | 0 | 0 | 0 | 2 |
| 3.10 Physical Protection | 5 | 1 | 0 | 0 | 6 |
| 3.11 Risk Assessment | 3 | 0 | 0 | 0 | 3 |
| 3.12 Security Assessment | 3 | 1 | 0 | 0 | 4 |
| 3.13 System and Communications Protection | 14 | 1 | 0 | 1 | 16 |
| 3.14 System and Information Integrity | 7 | 0 | 0 | 0 | 7 |
| **Total** | **99** | **8** | **1** | **2** | **110** |

**Score.** Using the 32 CFR 170.24 point values, the 9 open requirements deduct 18 points: **92 of 110**. The March 2026 self-assessment had scored these requirements as MET. Open rows by risk: 4 High (3.1.20, 3.2.2, 3.4.8, 3.12.4), 2 Moderate (3.1.3, 3.13.11), and 3 Low (3.3.4, 3.8.4, 3.10.6).

**Why a score of 92 is not enough.** A Conditional Level 2 status needs at least 88 points, but also requires that POA&M items be 1-point requirements (with 3.13.11 as the only exception) and that none of the excluded requirements be on the POA&M (32 CFR 170.21(a)(2)). Today:
- **3.1.20** (external systems) is Not met because CUI is in the PDPP and commercial email. It is a requirement that cannot be on a POA&M.
- **3.12.4** (system security plan) is Partially met because the enclave SSP v2.3 (2025-03) does not describe the 2026 desktop expansion or the field release role. Without a current SSP an assessment cannot be completed (32 CFR 170.24(c)(2)(i)(B)(5)).
- **3.2.2** and **3.4.8** are 5-point requirements and cannot be on a POA&M.

These four must close before the group can seek Level 2 (C3PAO), targeted for 2027-02 (G-029; POAM-011, POAM-014, POAM-015, POAM-016). 3.13.11 (one gateway component not in FIPS mode) may be on a POA&M under 170.21(a)(2)(ii) and is being fixed anyway (POAM-013).

### 4.3 A&E (`gap-analysis-ae.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| DFARS 252.204-7012 and CMMC (N54-R05) | 4 | 3 | 4 | 1 | 12 |
| FAR 52.204-21 on civilian awards (N54-R04) | 1 | 0 | 0 | 0 | 1 |
| FAR 52.204-25 (N23-R02) | 1 | 1 | 0 | 0 | 2 |
| FTC Act Section 5 and client contracts | 0 | 2 | 0 | 0 | 2 |
| Applicability tests (FTC Safeguards Rule, HIPAA, IRC 7216 and professional codes, CIRCIA, Colorado SB26-189) | 0 | 0 | 0 | 5 | 5 |
| **Total** | **6** | **6** | **4** | **6** | **22** |

Open rows by risk: 6 High, 2 Moderate, 2 Low. **Not met (4):** CUI sent through commercial email from the enclave to field teams (AE-G02); one CUI-marked specification found in the AI estimating assistant (AE-G10, P07); no Level 2 status check for subconsultants before award (AE-G11); and not ready for Level 2 (C3PAO) (AE-G12). A&E shares every enclave gap in section 4.2, because both entities rely on the same enclave and the same SSP.

**Design-build reporting inside the group.** On the 6 design-build projects, A&E is Construction's subcontractor. DFARS 252.204-7012(m)(2)(ii) requires a subcontractor to give the prime the DoD incident report number as soon as practicable. The intercompany agreement does not yet say how (AE-G07, G-040; POAM-004).

### 4.4 Property (`gap-analysis-property.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI DSS v4.0.1, Requirements 1 to 12 (N53-R04) | 5 | 5 | 1 | 1 | 12 |
| FTC Act Section 5 (N53-R02) | 0 | 1 | 0 | 0 | 1 |
| FAR 52.204-25 through federal leases (applicability unverified) | 0 | 1 | 0 | 0 | 1 |
| Federal tenant lease security commitments | 0 | 1 | 0 | 0 | 1 |
| State breach notification laws | 1 | 0 | 0 | 0 | 1 |
| Building systems security (group standard) | 0 | 0 | 1 | 0 | 1 |
| Applicability tests (FTC Safeguards Rule, CCPA/CPRA, AI housing rules) | 0 | 0 | 0 | 3 | 3 |
| **Total** | **6** | **8** | **2** | **4** | **20** |

Open rows by risk: 1 High, 8 Moderate, 1 Low.

**PCI DSS.** Property stores no account data. The parking technology service provider handles card data and gives Property an attestation of compliance each year, so Requirement 3 is Not applicable and Requirements 4 to 8 rely mostly on the provider. Property's own gaps are network separation (pay stations share flat building networks at 6 garages), shared manager logins without MFA, unrecorded device inspections, no written responsibility matrix, and no segmentation test (Requirement 11, Not met). The validation method is set by Property's acquirer; the analysis does not assume a particular self-assessment questionnaire.

**Building systems.** No binding cyber regulation covers commercial building automation, access control, or video. The group standard is the yardstick, and Property does not meet it: 41 of 64 properties on flat networks, 11 integrators with persistent remote access, no SIEM coverage, and default credentials on 14 controllers (PRP-G20, High; POAM-022 to POAM-024).

**Section 889 at federally leased properties.** P07 found 46 cameras and 3 recorders from a covered manufacturer at 2 federally leased properties, installed by the previous owner in 2018. Whether and how the GSA lease contracts incorporate FAR 52.204-25 is under counsel review and is marked unverified. Group policy applies the prohibition anyway, and replacement is due 2026-12-15 (POAM-029).

### 4.5 Group (`gap-analysis-group.csv`)
| Obligation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| SEC Reg S-K Item 106 (2 rows) | 2 | 0 | 0 | 0 |
| SEC Form 8-K Item 1.05 | 0 | 1 | 0 | 0 |
| State breach notification laws; Florida third-party agent duty | 0 | 2 | 0 | 0 |
| FTC Act Section 5; OFAC | 2 | 0 | 0 | 0 |
| FAR 52.222-8 certified payroll handling | 0 | 1 | 0 | 0 |
| CIRCIA; HIPAA (applicability) | 0 | 0 | 0 | 2 |
| **Total (10)** | **4** | **4** | **0** | **2** |

Open rows by risk: 3 Moderate, 1 Low. The materiality process exists but has never been exercised (GR-G03), and the 14-state notification matrix has never been tested across divisions (GR-G04). Both are fixed by the cross-division tabletop due 2026-12-15 (POAM-004).

### 4.6 All tables combined
| Table | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| Construction | 42 | 25 | 12 | 5 | 0 |
| CUI enclave | 110 | 99 | 8 | 1 | 2 |
| A&E | 22 | 6 | 6 | 4 | 6 |
| Property | 20 | 6 | 8 | 2 | 4 |
| Group | 10 | 4 | 4 | 0 | 2 |
| **Total** | **204** | **140** | **38** | **12** | **14** |

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | CUI outside the enclave (1) | Construction, A&E | 252.204-7012(b)(2)(ii)(D); 252.204-7021(d)(2); SP 800-171 3.1.3, 3.1.20 | High | Purge and block CUI in the PDPP and commercial email; remove the field release role; enclave desktops in jobsite trailers; CUI training for field staff | Group CISO | 2026-12-31 (POAM-006, POAM-011, POAM-015) |
| 2 | Level 2 readiness and affirmation accuracy (2) | Construction, A&E | 32 CFR 170.17, 170.21(a)(2), 170.22; SP 800-171 3.12.4, 3.4.8 | High | Counsel decision on the January and March affirmations; rewrite the enclave SSP; close the four blocking requirements; independent re-test; C3PAO assessment | Group General Counsel; Group CISO | 2027-02-28 (POAM-016, POAM-030) |
| 3 | Subcontractor and subconsultant CMMC checks (8) | Construction, A&E | DFARS 252.204-7021(f)(2); 32 CFR 170.23 | High | Status check and award hold in prequalification; enclave guest accounts where a subconsultant has no status | Construction VP of procurement; A&E contracts director | 2026-12-31 (POAM-020) |
| 4 | Payment-instruction controls (3) | Property, Construction, A&E | FTC Act Section 5; FAR 52.232-33 | High | Property bank changes into the payment factory; validated remittance block in the PDPP; remittance letters to owners and tenants | Group Chief Financial Officer | 2026-12-31 (POAM-009, POAM-031) |
| 5 | Property building systems and PCI scope (4) | Property | Group standard; PCI DSS Requirements 1, 8, 9, 11, 12 | High | Segment building and pay station networks; integrators through group PAM; SIEM onboarding; responsibility matrix; segmentation test | Property VP of building operations; Property director of parking | 2027-06-30 (POAM-022 to POAM-024, POAM-028) |
| 6 | Section 889 screening not group-wide (5) | All | FAR 52.204-25(b), (d); 52.204-26 | Moderate | Group approved-manufacturer list; screen A&E specifications and Property procurement; replace covered equipment; counsel decision on any reporting duty | Group Chief Risk Officer | 2026-12-15 (POAM-018, POAM-029) |
| 7 | Cross-division notification not exercised (7) | All | 252.204-7012(c), (m); Form 8-K Item 1.05; state laws | Moderate | Complete the matrix (P08); intercompany prime and subcontractor reporting path; cross-division tabletop with a materiality decision | Group General Counsel | 2026-12-15 (POAM-004) |
| 8 | AI tools and CUI (6) | Construction, A&E | 252.204-7021(d)(2); FAR 52.204-21(b)(1)(iii) | High | Block federal uploads to the AI estimating assistant from A&E; enterprise terms; turn off pooled pricing (P10) | A&E federal practice leader; Construction VP of preconstruction | 2026-11-30 (POAM-019, POAM-025) |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). The POA&M `source` column cites the P03 row behind each item. Two items come from this analysis alone, with no P07 test behind them: POAM-028 (PCI DSS for parking) and POAM-030 (CMMC affirmations and Level 2 readiness).

## 6. Pending regulatory changes
- **CMMC Phase 2** begins on 2026-11-10 (32 CFR 170.3(e)(2)). DoD intends to require Level 2 (C3PAO) for applicable solicitations as a condition of award, which is why the enclave's readiness matters now.
- **CMMC stays on NIST SP 800-171 R2.** 32 CFR 170.14(c)(3) ties Level 2 to R2, even though NIST has published Rev. 3. The crosswalk shows the Rev. 3 successor for each requirement so the move is ready if DoD changes the rule.
- **Revolutionary FAR Overhaul (RFO) proposed rule** (FR Doc. 2026-12559, June 23, 2026) is **proposed only**. It would move information security clauses into FAR Part 40, would renumber FAR 52.204-21 (the proposed conversion table maps it to 52.240-5), and would add CUI clauses that require NIST SP 800-171 Rev. 3 and CUI incident reporting within 72 hours of discovery. None of this is treated as a current obligation. Affected rows are flagged in `pending_rule_change`.
- **CIRCIA** is not in effect (final rule not published as of 2026-09-25). The proposed scope would reach DFARS 252.204-7012 contractors.
- **PCI DSS:** v4.0.1 remains the current version.

# Regulatory Gap Analysis: Cris Santos Company Holdings | Health Care | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Health Care and Social Assistance (focus division: Care Delivery) |
| Primary regulation | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24) |
| Division regulations | Health Plan: HIPAA plus Medicare Advantage (42 CFR Part 422) and state insurance law; Health-Tech SaaS: HIPAA business associate duties plus SOC 2 and customer commitments |
| Gap tables | `gap-analysis.csv` (Care Delivery, all 69 crosswalk rows); `gap-analysis-health-plan.csv` (41 rows); `gap-analysis-saas.csv` (36 rows) |
| Assessment dates | 2026-05-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-31) |
| Assessors | Division security and compliance leads and division privacy officers, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit |

## 1. Applicability
### 1.1 Who is what under HIPAA
| Entity | HIPAA role | Basis |
|---|---|---|
| Care Delivery | Covered entity (health care provider that bills electronically) | 45 CFR 160.103 |
| Health Plan | Covered entity (health plan). The definition of health plan lists the Medicare Advantage program under Part C of title XVIII | 45 CFR 160.103 ("health plan", paragraph (xv)) |
| Health-Tech SaaS | Business associate of about 420 customers; directly subject to the Security Rule | 45 CFR 160.103 ("business associate"); 164.302 |
| Corporate shared services | Business associate of both covered-entity divisions (it creates, receives, maintains, and transmits their ePHI on SYS-G1 to SYS-G3) | Intercompany BAAs |
| Care Delivery (patient-app platform) | Also a business associate of 38 white-label practices | 45 CFR 160.103 |

There is no size exemption. 45 CFR 164.306(b) lets each entity consider its size, complexity, capabilities, and costs when choosing *how* to meet a standard, not *whether* to meet it.

### 1.2 Affiliated covered entity decision (confirmed as the scenario requires)
Under 45 CFR 164.105(b), legally separate covered entities under common ownership or control *may* designate themselves a single affiliated covered entity, and the designation must be documented. **No designation exists.** Group legal confirmed on 2026-08-14 that Care Delivery and the Health Plan operate as **separate covered entities**. Consequences used throughout this sample:
- Each covered entity has its own security and privacy officials, its own risk analysis, and **its own breach notification duties** (P08).
- PHI that moves between them is a **disclosure**, not an internal use. It needs a permission such as 164.506(c) (for example, 164.506(c)(4) health care operations disclosures, which require that both entities have a relationship with the individual) and must meet minimum necessary (164.502(b), 164.514(d)(3)).
- Designating an affiliated covered entity would not remove minimum necessary. Because it would combine health plan and provider functions, it would also bring the 164.504(g) rule: PHI of people who receive only one function's services may be used only for that function. The group decided not to designate for now and to revisit after the Group Data Platform zones are separated.

### 1.3 Excluded requirements, with reasons
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): neither covered entity is a clearinghouse.
- **164.314(a)(2)(ii)** (arrangements with governmental entities): none.
- **164.314(b)** (group health plans): Care Delivery is not a group health plan. The Health Plan is a health insurance issuer and HMO, not a group health plan; the holding company's own employee group health plan is assessed separately by Group HR.
- **42 CFR Part 2:** no division runs a federally assisted substance use disorder program.
- **FTC Health Breach Notification Rule (16 CFR Part 318):** all entities act as HIPAA covered entities or business associates, which 318.1 excludes.

## 2. Regulation-by-division matrix
| Requirement | Care Delivery | Health Plan | Health-Tech SaaS | Group (corporate) |
|---|---|---|---|---|
| N62-R01 HIPAA Security Rule | **Primary.** Covered entity | Applies. Covered entity | Applies. Business associate (164.302) | Applies. Business associate of both covered entities |
| N62-R02 HIPAA Privacy Rule | Applies. Minimum necessary; TPO disclosures to the Health Plan | Applies. Minimum necessary; 164.514(d)(3) protocols | Applies through BAAs: uses only as the BAA permits (164.502(a)(3)) | Applies through intercompany BAAs |
| N62-R03 Breach Notification | Own notices: 164.404-408 | Own notices: 164.404-408 | Notice to each affected customer: 164.410 and BAA terms | Notice to both covered entities: 164.410 |
| N62-R04 Security Rule NPRM | Tracked only (proposed) | Tracked only | Tracked only | Tracked only |
| N62-R05 42 CFR Part 2 | Not applicable (no Part 2 program) | Not applicable | Not applicable | Not applicable |
| N62-R06 FTC HBNR | Not applicable (covered entity) | Not applicable | Not applicable (business associate) | Not applicable |
| N62-R07 Section 1557, 45 CFR 92.210 | Applies (Medicare and Medicaid): scribe, predictive decision support | Precaution: MA payments are federal financial assistance under 45 CFR 92.4; whether UM tools "support clinical decision-making" is under counsel review | Not directly; customers may ask for tool information | Group AI standard (P10) |
| N62-R08 CMS emergency preparedness | Applies to the 14 ASCs (42 CFR 416.54). 42 CFR 482.15 does not apply (no hospitals) | Not applicable | Not applicable | Not applicable |
| Medicare Advantage, 42 CFR Part 422 (422.101(b)(6), 422.101(c)(1)(i), 422.118, 422.137, 422.566(d)) | Not applicable | **Applies** (MA organization; UM model) | Not applicable | Not applicable |
| N52-R01 GLBA and N52-R07 state insurance data security laws (NAIC Model #668 where enacted) | Not applicable | **Applies** in each state of operation (generic; text varies) | Not applicable | Supports Health Plan |
| N52-R04 NYDFS Part 500 | Not applicable | Not applicable (no New York license) | Not applicable | Not applicable |
| N51-R01 FTC Act Section 5 | Applies (general) | Limited (most insurance activity is outside FTC jurisdiction) | **Applies** (security and AI claims) | Applies |
| N51-R04 DOJ Data Security Program, 28 CFR Part 202 | Applies (health data above bulk thresholds) | Applies | Applies | Group vendor screening |
| N51-R07 FedRAMP; N51-R02 COPPA | Not applicable | Not applicable | Not applicable (no federal customers; no child-directed service) | Not applicable |
| N52-R08 / N51-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Same | Same, plus third-party agent duties to customers where state law sets them | Coordinates |
| SOC 2 (contractual) | Planned for the patient-app platform (P09) | Not in scope (P09) | Annual Type 2 (P09) | Group services carved in |

## 3. Method
1. **Requirements.** HIPAA Security Rule rows and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool). Medicare Advantage, Privacy Rule, and Breach Notification rows were read from the eCFR (current through 2026-09-23). State insurance rows are generic, based on NAIC Model #668, whose text varies by state.
2. **Crosswalk.** Security Rule rows use the Health Care crosswalk in `02_industry-rules/health-care/`, an **author mapping**, because NIST's official mapping is not yet published for CSF 2.0. Other rows carry an author mapping made for this analysis.
3. **Evidence.** Interviews with each division's security, privacy, clinical, and legal leads; document review; configuration exports; the 2026-07 UM case audit (60 cases); and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable.

**Addressable is not optional.** For each addressable specification, the entity must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). No addressable gap below is being documented as unreasonable.

## 4. Results
### 4.1 Care Delivery: HIPAA Security Rule (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 18 | 11 | 0 | 1 |
| 164.310 Physical safeguards | 11 | 1 | 0 | 0 |
| 164.312 Technical safeguards | 9 | 3 | 0 | 0 |
| 164.314 Organizational requirements | 2 | 2 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 4 | 1 | 0 | 0 |
| **Total (69)** | **44** | **18** | **0** | **7** |

Of the 18 partially met rows, 5 are standards, 7 are **Required** implementation specifications, and 6 are **Addressable**. Care Delivery is mostly compliant. Its gaps sit where it depends on shared services (the Group Data Platform, the notification matrix) or on the 14 practices acquired in 2025, plus one it created itself: as a business associate of 38 white-label practices, it lacks subcontractor terms with corporate for the practices' PHI (164.314(a)(2)(iii)).

### 4.2 Health Plan (`gap-analysis-health-plan.csv`)
| Regulation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| HIPAA Security Rule (17 selected rows) | 4 | 10 | 1 | 2 |
| HIPAA Privacy Rule | 0 | 3 | 1 | 1 |
| Medicare Advantage (42 CFR Part 422) | 8 | 5 | 1 | 0 |
| Section 1557 (precaution) | 0 | 1 | 0 | 0 |
| State insurance law (generic), GLBA, NYDFS | 2 | 1 | 0 | 1 |
| **Total (41)** | **14** | **20** | **3** | **4** |

The Health Plan's Security Rule rows focus on the specifications where its evidence differs from Care Delivery's. All other specifications rely on the same group common controls, which is why documenting inheritance (scenario gap 6) matters.

**Not met:** 164.316(b)(2)(iii) (standards not updated since 2024, gap 2); 164.514(d)(3) (no minimum-necessary protocols for routine feeds with Care Delivery, gap 1); 42 CFR 422.137(b) (the model-assisted UM workflow was never approved by the UM committee, gap 3).

**Utilization-management AI (gap 3).** 42 CFR 422.101(c)(1)(i) requires medical necessity determinations based on coverage and benefit criteria, whether the item or service is reasonable and necessary, the enrollee's medical history, physician recommendations, and clinical notes, and medical director involvement where appropriate. The model only auto-approves and never denies, and every sampled adverse determination had physician review (422.566(d), Met). But 11 of 60 sampled adverse cases lacked documented consideration of the clinical record, and the model was never presented to the UM committee (422.137). The model supports determinations; the record must show that it did not replace the individualized review.

### 4.3 Health-Tech SaaS (`gap-analysis-saas.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| HIPAA Security Rule (business associate) | 7 | 5 | 0 | 0 |
| HIPAA Privacy Rule (164.502(a)(3), 164.502(e)(1)(ii), 164.504(e)(2)(ii)) | 4 | 5 | 0 | 1 |
| HIPAA Breach Notification (164.410) | 1 | 2 | 1 | 0 |
| SOC 2 commitments and customer contracts | 1 | 3 | 2 | 0 |
| FTC Act, DOJ Data Security Program, FTC HBNR, FedRAMP | 0 | 2 | 0 | 2 |
| **Total (36)** | **13** | **17** | **3** | **3** |

**Not met:** the SOC 2 system description omits the AI feature and its model provider; customer contracts were not updated for AI processing (both gap 4); and the AI feature logs requests by tenant rather than by patient, so the SaaS could not identify each affected individual for a 164.410(c)(1) notice if the model provider were breached.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Mixed PHI and inconsistent purpose-based access on the Group Data Platform (1) | CD, HP, SaaS | 164.308(a)(4); 164.502(b); 164.514(d); 422.118(a) | High | Zone separation by covered entity; purpose tags at 100%; minimum-necessary protocol per routine feed | Group data platform director; Group Chief Privacy Officer | 2027-03-31 |
| 2 | UM model governance (3) | HP | 422.101(c)(1)(i); 422.137(b), (d) | High | UM committee approval; structured reviewer rationale; monthly audit | Health Plan medical director | 2026-12-31 |
| 3 | SaaS AI feature commitments (4) | SaaS | 164.504(e); 164.410(c)(1); SOC 2 description | High | System description update; customer notices and BAA amendments; per-patient logging | SaaS general manager | 2026-12-31 |
| 4 | Multi-regulator notification not exercised (5) | All | 164.308(a)(6)(ii); 164.404-410; Model #668 sec. 6; Form 8-K Item 1.05 | Moderate | Complete the matrix; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 5 | Health Plan inheritance not documented (6) | HP | 164.308(a)(8) | Moderate | Inheritance matrix | Health Plan security and compliance lead | 2026-12-31 |
| 6 | Division supplement drift (2) | HP | 164.316(b)(2)(iii) | Moderate | Re-issue supplement; annual alignment attestation | Health Plan security and compliance lead | 2026-11-30 |
| 7 | BAAs out of date | HP, SaaS, CD | 164.308(b)(1); 164.314(a)(2)(iii); 164.502(a)(3) | Moderate | Re-paper Health Plan intercompany BAA; subcontractor terms for practices' PHI; amend 97 SaaS BAAs at renewal | Group General Counsel | 2027-06-30 |
| 8 | Legacy EHR at acquired practices | CD | 164.312(b), (d); 164.308(a)(1)(ii)(D) | Moderate | Interim logging and review; migrate to SYS-D1 | Care Delivery IT director | 2027-06-30 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-006, POAM-018, and POAM-020 to POAM-023 trace directly to this analysis).

## 6. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. If finalized as proposed, these verified proposals would affect the group:
- The required and addressable distinction would be removed. Care Delivery's 6 addressable gaps would become mandatory.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (already largely met).
- MFA would be required (the legacy EHR and the broker portal fall short).
- A written technology asset inventory and network map would be required (the Group Data Platform data inventory is 61% complete).
- Penetration testing at least every 12 months, and vulnerability scanning.
- Restoring certain systems and data within 72 hours (the Health Plan claims core and Care Delivery LIS and PACS need testing against this).
- A compliance audit at least every 12 months.
- Business associates would notify covered entities within 24 hours of activating a contingency plan. That would affect corporate (to both covered entities), the SaaS (to its customers), and Care Delivery (to its 38 practices).

The `pending_rule_change` column flags affected rows. None of these is treated as a current obligation. CIRCIA reporting is also not in effect (final rule not published as of 2026-09-25).

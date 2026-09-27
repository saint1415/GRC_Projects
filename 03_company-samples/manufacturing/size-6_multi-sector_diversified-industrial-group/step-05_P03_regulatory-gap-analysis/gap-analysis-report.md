# Regulatory Gap Analysis: Cris Santos Company Holdings | Manufacturing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Manufacturing (focus division: Medical Devices, NAICS 334510) |
| Primary regulation | FD&C Act section 524B, ensuring cybersecurity of devices (21 U.S.C. 360n-2), with the FDA regulations and guidance that carry it out |
| Division regulations | Medical Devices also: HIPAA Security Rule and 164.410 for the device cloud (business associate). Distribution: FAR 52.204-21 (the CMMC Level 1 requirement set), FAR 52.204-25, and FDA distributor and importer duties. Testing: no binding cybersecurity rule, so NIST CSF 2.0 is the benchmark |
| Gap tables | `gap-analysis.csv` (Medical Devices, 57 rows); `gap-analysis-distribution.csv` (29 rows); `gap-analysis-testing.csv` (24 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Medical Devices: VP QA/RA and the Chief Product Security Officer (524B, FDA), the DCC HIPAA security official and privacy officer (HIPAA). Distribution: federal contracts compliance director and VP quality and regulatory. Testing: division security and compliance lead and laboratory quality director. Coordinated by the Group Chief Risk Officer; reviewed by group internal audit |

## 1. Applicability
### 1.1 Medical Devices: section 524B and FDA regulations
Section 524B(a) covers any person who submits a 510(k), PMA, PDP, De Novo, or HDE for a device that meets the "cyber device" definition in 524B(c): a device that (1) includes software validated, installed, or authorized by the sponsor, (2) can connect to the internet, and (3) has technological characteristics that could be vulnerable to cybersecurity threats. The section took effect 90 days after enactment on 2022-12-29 (Pub. L. 117-328 section 3305(d)).

| Product | 524B status | Why |
|---|---|---|
| IX-4 infusion system | **Applies** | 510(k) submitted and cleared in 2024; connects to the DCC |
| PM-7 monitors | **Applies** | 510(k) cleared 2025 |
| US-2 ultrasound | **Applies** | Cleared 2025; connects for image transfer and updates |
| AI-001 (US-2 image analysis) | **Will apply** | Submission planned 2027 Q2 (P10) |
| IX-3 infusion pump (legacy) | **Does not apply to its 2018 clearance** | Cleared before the effective date. Pub. L. 117-328 section 3305(c) preserves FDA's existing authority over the cybersecurity of devices cleared before 2022-12-29. IX-3 remains subject to the QMSR, 21 CFR 803 and 806, and FDA's postmarket cybersecurity guidance. Any future IX-3 modification that needs a new submission would bring in 524B |
| DCC, update service, build and signing pipeline | **Related systems** | The statute speaks of "the device and related systems." FDA's guidance includes manufacturer-controlled update servers and connections to health care facility networks |

There is **no size exemption**; the only route is an FDA exemption list under 524B(d), and none applies. Failure to comply with 524B(b)(2) is a prohibited act under 21 U.S.C. 331(q)(3).

**What is binding and what is not.** The statute and FDA's regulations (21 CFR 803, 806, 807, and 820) are binding. FDA's guidance documents (*Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions*, issued 2026-02-03, and *Postmarket Management of Cybersecurity in Medical Devices*, December 2016) are nonbinding. Guidance rows are rated because FDA uses them to judge "reasonable assurance" of cybersecurity.

**HIPAA for the device cloud.** Medical Devices is a business associate for the DCC only: it creates, receives, maintains, and transmits PHI for about 1,300 hospitals (45 CFR 160.103). The Security Rule applies under 45 CFR 164.302, and 164.410 sets its breach notice duty. At this size the Medical Devices HIPAA rows focus on the 22 specifications where DCC evidence differs from the group common controls; the others rely on the common control catalog (P02), assessed once in P07.

### 1.2 Distribution: federal contract clauses and FDA distributor and importer duties
- **FAR 52.204-21 applies.** The VA and DoD contracts include it, and Distribution processes Federal contract information (order, delivery, and facility data for about 380 federal facilities). The clause sets 15 basic safeguarding requirements (paragraph (b)(1)(i) to (xv)) and a flowdown duty (paragraph (c)).
- **CMMC Level 1 will apply.** 32 CFR 170.3(c) applies CMMC to DoD contracts under which a contractor processes FCI or CUI, including commercial items except those exclusively for COTS items. The DoD contract covers distribution services, so the COTS exception does not help. The contract was awarded before Phase 1 (2025-11-10); DoD may add a Level 1 (Self) requirement when it exercises the 2027-03-31 option (170.3(e)(1)), and Phase 4 (2028-11-10) reaches option periods on earlier contracts (170.3(e)(4)). Level 1 is exactly the 15 FAR requirements (170.14(c)(2)). No POA&M is allowed for Level 1, and the self-assessment and SPRS affirmation must be repeated every year (170.15(a)).
- **DFARS 252.204-7012 is present but not triggered.** The clause's safeguarding and 72-hour reporting duties attach to covered contractor information systems that process covered defense information. DoD has marked or provided none, and Distribution generates none (Group General Counsel decision, 2026-06-30). Recheck at every contract modification.
- **FAR 52.204-25 applies** (report covered telecommunications equipment within 1 business day of identification, with more within 10 business days).
- **FDA duties.** Distribution is a **distributor** under 21 CFR 803.3 for most products (keep device complaint records under 803.18(d)) and an **initial importer** for 6 foreign manufacturers' lines (MDR event files, 803.18(a); importer reports, 803.40; corrections and removals, 806.10; registration, 807.20(a)(5)). If it repackaged or relabeled devices it would become a manufacturer (803.3), which is why the private-label proposal is on hold.
- **Not applicable:** ITAR (no defense articles), CUI safeguarding (none held), DSCSA (no prescription drugs).

### 1.3 Testing: no binding cybersecurity rule, so CSF 2.0 is the benchmark
The Testing division was checked against each rule in the three vertical files:
- **Federal work and CUI:** none. It holds no federal contracts or subcontracts, so FAR 52.204-21, DFARS 252.204-7012, and CMMC do not apply (decision confirmed by the Group General Counsel on 2026-06-30).
- **FTC Safeguards Rule (N54-R01):** does not apply. It covers financial institutions, such as tax preparers; the division is not one.
- **HIPAA (N54-R06):** does not apply by design. Client contracts prohibit PHI. Gap 6 (PHI found in 3 submissions) is analyzed as a risk of becoming a subcontractor business associate without agreeing to it.
- **What does bind it:** client NDAs, its accreditation's confidentiality duties, EAR for client technical data, state breach laws for employee data, and the FTC Act.

With no binding security rule, the division benchmarks itself against **NIST CSF 2.0**, using 24 subcategories chosen for its risks (client confidentiality, the information barrier, the test range, acquired laboratories). Its SP 800-53 references come from NIST's official CSF 2.0 to SP 800-53 mapping.

### 1.4 Group-wide obligations
- **SEC (N42-R07):** Form 8-K Item 1.05 within 4 business days after a materiality determination; Reg S-K Item 106 annual disclosure. Applies at group level.
- **State breach notification laws:** each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171). The DCC holds PHI of patients in all 50 states; the group holds personal information of 45,000 employees.
- **FTC Act Section 5 (N42-R01):** security and AI claims in marketing (DCC, Testing services).
- **EAR (N31-33-R04):** Medical Devices technology and client technical data at Testing; managed by group trade compliance. Not scored in these tables.

## 2. Regulation-by-division matrix
| Requirement | Medical Devices | Distribution | Testing | Group (corporate) |
|---|---|---|---|---|
| N31-33-R05 FD&C Act 524B | **Primary.** IX-4, PM-7, US-2, AI-001; related systems | Not applicable (not a submitter) | Not applicable (tests support clients' submissions) | Funds the IX-3 plan |
| 21 CFR 820 (QMSR) | Applies (manufacturer) | Not applicable (no relabeling; private label on hold) | Not applicable | n/a |
| 21 CFR 803 | Manufacturer MDRs (803.50, 803.53) | Distributor complaint files (803.18(d)); importer reports (803.40) | Not applicable | n/a |
| 21 CFR 806 | Manufacturer corrections and removals | Importer corrections; executes manufacturers' holds | Not applicable | n/a |
| 21 CFR 807 | Registered manufacturer | Initial importer registration (807.20(a)(5)) | Not applicable | n/a |
| N62-R01 HIPAA Security Rule; N62-R03 Breach Notification | Applies to the DCC (business associate) | Not applicable (no PHI) | Not applicable by design; gap 6 is a risk | Supports the DCC (common controls) |
| N42-R04 FAR 52.204-21; N42-R02 CMMC Level 1 | Not applicable (no federal contracts) | **Primary for the division.** VA and DoD contracts | Not applicable (no federal work) | Common controls help meet it |
| N31-33-R01 / N42-R03 DFARS 252.204-7012 | Not applicable | Clause present; **not triggered** (no CDI) | Not applicable | n/a |
| N42-R05 FAR 52.204-25 | Not applicable | Applies | Not applicable | Procurement supports it |
| N31-33-R03 ITAR | Not applicable (no defense articles) | Not applicable | Not applicable | n/a |
| N31-33-R04 EAR | Applies (exports; deemed exports) | Limited (imports; restricted-party screening) | Applies to client technical data | Group trade compliance |
| NIST CSF 2.0 | Framework for group policy | Framework for group policy | **Benchmark** (no binding rule) | Group policy framework |
| N42-R07 SEC Item 1.05 and Item 106 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | DCC patients in all states | Employee and customer contact data | Employee data; client contracts | Coordinates |
| SOC 2 (contractual) | DCC Type 2 (P09) | Not in scope (P09) | Planned for client portal and LIMS (P09) | Group services carved in |

## 3. Method
1. **Requirements.** Section 524B rows follow the statute's structure, read from the U.S. Code on 2026-09-26: (a), (b)(1) to (b)(4), (c), (d), and the construction note. FDA regulation rows cite the eCFR (current through 2026-09-23). Guidance rows cite the guidance section. HIPAA rows and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 via the Health Care crosswalk. FAR, DFARS, and CMMC rows use the clause and regulation paragraphs read from the eCFR; CMMC Level 1 identifiers and their SP 800-171 R2 objectives come from 32 CFR 170.15.
2. **Crosswalk.** NIST has published no mapping for 524B, FDA regulations, or FAR 52.204-21 to CSF 2.0 and SP 800-53, so those rows carry an **author mapping**, labeled as such. HIPAA rows use the Health Care crosswalk (also an author mapping), with NIST's official OLIR controls shown for comparison. Testing rows use NIST's **official** CSF 2.0 to SP 800-53 mapping.
3. **Evidence.** Interviews with each division's security, regulatory, contracts, and quality leads; document review (submissions, procedures, BAAs, contracts, NDAs); configuration exports; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps rated on the P01 risk scale.

## 4. Results
### 4.1 Medical Devices (`gap-analysis.csv`)
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FD&C Act section 524B (statute) | 12 | 6 | 3 | 0 | 3 |
| FDA regulations (21 CFR 803, 806, 820) | 8 | 4 | 3 | 1 | 0 |
| FDA guidance (premarket 2026, postmarket 2016) | 14 | 8 | 5 | 1 | 0 |
| HIPAA Security Rule (business associate scope: DCC) | 22 | 17 | 5 | 0 | 0 |
| HIPAA Breach Notification Rule (164.410) | 1 | 0 | 1 | 0 | 0 |
| **Total** | **57** | **35** | **17** | **2** | **3** |

The 19 unmet or partially met rows break down by gap risk as 2 High and 17 Moderate.

**The main finding:** the division meets section 524B for every product it covers. The CVD program, ISAO membership, automated SBOMs, HSM signing, and quarterly patch cycles are what FDA expects. Its two Not met rows are both about **IX-3**, the product 524B does not cover: the IX-3 signing key sits outside the HSM service (G-014), and IX-3 cannot be monitored or patched to the standard applied to current products (G-034). The residual 524B gaps are supplier SBOM data (G-003, G-009) and hospital administrator MFA on drug library changes (G-006).

### 4.2 Distribution (`gap-analysis-distribution.csv`)
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FAR 52.204-21 (15 requirements, flowdown, CUI note) | 17 | 11 | 4 | 1 | 1 |
| CMMC, DFARS 252.204-7012, FAR 52.204-25 | 4 | 0 | 2 | 1 | 1 |
| FDA distributor and importer duties (21 CFR 803, 806, 807) | 8 | 5 | 3 | 0 | 0 |
| **Total** | **29** | **16** | **9** | **2** | **2** |

The 11 unmet or partially met rows break down by gap risk as 2 High, 7 Moderate, and 2 Low.

**The main finding:** most of the 15 FAR requirements are already met by group common controls (MFA, EDR, patching, firewalls, sanitization), but Distribution cannot prove it. It has never self-assessed, has not defined where FCI lives, and has no SPRS affirmation (DS-G19, Not met, High). Because CMMC Level 1 allows no POA&M, every one of the 15 requirements must be Met before affirmation, so the 4 Partially met FAR rows (access to FCI in file shares, handheld accounts, visitor logs) and the missing courier flowdown must be closed first.

### 4.3 Testing (`gap-analysis-testing.csv`)
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| NIST CSF 2.0 benchmark (24 subcategories) | 24 | 11 | 11 | 2 | 0 |

The 13 unmet or partially met rows break down by gap risk as 3 High, 8 Moderate, and 2 Low.

**Not met:** PR.AA-05 (the information barrier is broken by a collaboration space open to 212 Medical Devices engineers) and DE.CM-03 (no monitoring of cross-division access). Both are gap 5 and GR-05 in P01.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | IX-3 signing key outside the HSM service (1) | MD | 21 CFR 820.10(c); SPDF procedure | High | HSM signing or planned key transition (POAM-003) | VP Engineering | 2027-03-31 |
| 2 | IX-3 legacy lifecycle: no SBOM, end of support June 2027, 58% update adoption (1) | MD, DS | FDA postmarket guidance; 21 CFR 806 | High | End-of-support plan, SBOM by binary analysis, field campaign with Distribution (POAM-008, POAM-012, POAM-020) | Medical Devices division president | 2027-06-30 |
| 3 | No CMMC Level 1 self-assessment; FCI boundary undefined (4) | DS | 48 CFR 52.204-21; 32 CFR 170.15 | High | FCI enclave; close FAR rows; self-assess and affirm in SPRS (POAM-021) | Distribution federal contracts compliance director | 2027-02-28 |
| 4 | Testing information barrier not enforced (5) | TS, MD | CSF 2.0 PR.AA-05, DE.CM-03; client NDAs | High | Close the shared space; barrier groups; SOC alerts (POAM-010) | Testing division president | 2026-12-31 |
| 5 | Independence of intercompany tests not documented (5) | TS, MD | FDA premarket guidance V.C; CSF ID.IM-01 | Moderate | Signed independence statements; outside tester for the IX-3 fix (POAM-011) | VP Quality and Regulatory Affairs | 2026-11-30 |
| 6 | Device-to-breach decision point and BAA terms register (7) | MD | 164.308(a)(6)(ii); 164.314(a)(2)(i); 164.410; 820.35(a); 803.50 | Moderate | Joint PSIRT and complaint workflow; 164.402 step; complete the register (POAM-023) | VP Quality and Regulatory Affairs | 2026-12-31 |
| 7 | Cyber complaints not captured by the distributor and importer (7) | DS | 803.18(d)(1); 803.40 | Moderate | Intake prompts; daily importer review (POAM-022) | Distribution VP quality and regulatory | 2026-12-31 |
| 8 | PHI in client submissions (6) | TS | CSF ID.AM-07, GV.OC-03 | Moderate | Intake scanning and quarantine (POAM-017) | Testing laboratory quality director | 2026-12-31 |
| 9 | Generative AI drafting tool on client data (8) | TS | CSF GV.SC-05, PR.DS-10 | Moderate | Client consent clause; restrict use (POAM-018) | Testing laboratory quality director | 2026-11-30 |
| 10 | Supplier SBOM data and hospital administrator MFA (9) | MD | 524B(b)(1), (b)(2), (b)(3) | Moderate | Supplier SBOM enforcement (POAM-007); MFA for hospital administrators (MD-028) | Chief Product Security Officer | 2027-06-30 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-017, POAM-018, and POAM-020 to POAM-023 trace directly to this analysis).

## 6. Pending regulatory changes
- **Section 524B(b)(4) regulations.** FDA may add cybersecurity requirements by regulation. None were found as of 2026-09-25.
- **FDA guidance updates.** The premarket guidance was issued in September 2023 and revised in June 2025 and February 2026. Recheck the current version before each submission, including AI-001.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed**; the regulatory agenda projects a final rule in July 2027. If finalized as proposed, the DCC would face: removal of the required and addressable distinction; encryption at rest and in transit with limited exceptions; MFA (the hospital administrator gap would become a compliance issue); a written technology asset inventory and network map; penetration testing at least every 12 months, and vulnerability scanning; restoring certain systems within 72 hours; a compliance audit at least every 12 months; and business associate notice within 24 hours of activating a contingency plan.
- **FAR overhaul.** A proposed rule (FR Doc. 2026-12559, 2026-06-23) would move information-security clauses into a new FAR part 40, with 52.204-21 mapped to a proposed 52.240-5. It is not final. The separate FAR CUI proposal (90 FR 4278) was folded into it and is also not final.
- **CIRCIA** reporting is not in effect (final rule not published as of 2026-09-25).

The `pending_rule_change` column flags affected rows. None of these proposals is treated as a current obligation.

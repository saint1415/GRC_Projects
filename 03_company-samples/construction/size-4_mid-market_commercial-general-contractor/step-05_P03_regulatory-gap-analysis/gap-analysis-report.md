# Regulatory Gap Analysis: Cris Santos Company | Construction | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial and institutional building general contractor; DoD design-build prime on FC-4) |
| Tier / Vertical | Mid-Market / Construction |
| Primary regulation | NIST SP 800-171 Rev. 2 (110 requirements), as required by DFARS 252.204-7012(b)(2) and assessed for CMMC Level 2 (32 CFR 170.14(c)(3)) |
| Other rules for the primary business line | DFARS 252.204-7012 cloud, reporting, preservation, and flowdown paragraphs; DFARS 252.204-7019, 252.204-7020, and 252.204-7021; 32 CFR Part 170 scoping; FAR 52.204-21 (corporate FCI scope); FAR 52.204-25 and 52.204-26; Fla. Stat. 501.171 (employee data); NISPOM (not applicable) |
| Text verified | eCFR, 48 CFR and 32 CFR Part 170 as of 2026-09-23; Fla. Stat. 501.171 (2026) |
| Assessment dates | 2026-07-06 to 2026-07-31 (evidence sampling through the P07 walkthroughs, 2026-08-11 to 2026-08-13) |
| Assessors | GRC analyst and Security Manager, with the Director of Contracts and Compliance and the FC-4 Project Executive; reviewed by the vCISO and outside government contracts counsel |
| Working file | `gap-analysis.csv` (134 rows: G-001 to G-110 for the 110 requirements, G-111 to G-134 for clause and regulation duties) |
| Approved | Chief Operating Officer, 2026-09-17; G-123 (Very High) approved for treatment by the Chief Executive Officer |

## 1. Applicability
**FAR 52.204-21 applies now, to every system that holds FCI.** The clause is in FC-1 to FC-4. Drawings, submittals, schedules, daily logs, certified payrolls, and pay apps prepared for these contracts are FCI. There is no size exemption. At this size the clause is mostly met on corporate systems, so it is one summary row (G-128) plus the flowdown row (G-129), not 17 rows as in the Small sample.

**DFARS 252.204-7012 applies now, and its duties have been triggered.** FC-3 and FC-4 include the clause. On FC-4 the Government furnished CUI-marked drawings and the A&E subcontractor creates CUI design packages, so the company holds covered defense information (252.204-7012(a)). The clause requires "adequate security" on every covered contractor information system, including NIST SP 800-171 (252.204-7012(b)(2)(i)), FedRAMP Moderate equivalent security for any external cloud service that holds CDI ((b)(2)(ii)(D)), reporting within 72 hours of discovery of a cyber incident ((c)(1)(ii) and the definition of "rapidly report" in (a)), a medium assurance certificate ((c)(3)), image preservation for 90 days ((e)), and flowdown to subcontracts that involve CDI, including commercial products or services ((m)(1)). There is no small-business or size exemption. FC-3 holds no CDI, so the clause has no effect there today.

**DFARS 252.204-7019 and 252.204-7020 apply now.** A current SP 800-171 DoD Assessment (not more than 3 years old) must be in SPRS for each covered contractor information system relevant to an award (252.204-7019(b)). The 2025 Basic Assessment of 71 is current by date but not accurate (section 3). The company may not award a subcontract subject to SP 800-171 unless the subcontractor has at least a current Basic Assessment (252.204-7020(g)(2)).

**CMMC Level 2 (C3PAO) applies from the follow-on MATOC.** FC-1 to FC-4 predate Phase 1 (2025-11-10) and carry no DFARS 252.204-7021 clause. The Army Corps of Engineers has said the follow-on MATOC solicitation (expected 2027 Q1) will require Level 2 (C3PAO); Phase 2 of the phase-in begins 2026-11-10 (32 CFR 170.3(e)(2)). Level 2 is fixed to SP 800-171 Rev. 2 (32 CFR 170.14(c)(3)). The Affirming Official is the CEO (32 CFR 170.22). Subcontractors that will handle CUI need their own CMMC status at the level the company flows down (252.204-7021(d)(1)(ii), (f); 32 CFR 170.23).

**Scope assessed.** The 110 requirements were assessed where CUI actually is today, not only where it should be: the CPE, the commercial project management platform (SYS-01), 26 FC-4 rugged tablets, and printed CUI at the FC-4 trailer. The `gap_location` column marks each open row as "CPE", "Outside the enclave", or both, to support the scoping decision in section 4.

**Other rules considered:**
- **FAR 52.204-25 and 52.204-26:** apply in all four federal contracts. P07 found covered video surveillance equipment in rented jobsite cameras at FC-2, which was reported on time (G-130, G-131).
- **Fla. Stat. 501.171:** applies to employee personal information (G-133).

**Not applicable, with reasons:**
- **NISPOM (32 CFR Part 117):** no facility clearance and no classified information (G-134).
- **CIRCIA:** the final rule is not published; nothing is required yet.
- **SEC cyber disclosure rules:** the company is privately held.

## 2. Method
1. **Requirements.** The 110 rows follow the official structure of NIST SP 800-171 Rev. 2 (families 3.1 to 3.14), with the CMMC identifier and the point value from the CMMC Scoring Methodology (32 CFR 170.24(c)(2)). Requirement text is quoted from the public-domain NIST publication. The 24 clause and regulation rows cite the paragraph of each clause or section as checked on eCFR (version date 2026-09-23).
2. **Crosswalk.** CSF 2.0 and SP 800-53 Rev. 5 mappings are derived from NIST's official mappings through the SP 800-171 Rev. 3 counterpart of each requirement (the Rev. 2 to Rev. 3 change analysis, the SP 800-171r3 CUI overlay, and the CSF 2.0 to SP 800-171r3 mapping in `00_universal-framework/crosswalks/csf2_to_sp800-171r3.csv`). The route through Rev. 3 is the author's; the `crosswalk_source` column says so for each row. Clause rows use author mappings.
3. **Evidence sampling.** Each requirement was rated on sampled evidence, not on documents alone:
   - accounts: all 52 CPE accounts; 25 of 286 terminations; 15 of 38 transfers involving FC-4; the SYS-01 permission export for FC-4 folders;
   - data location: a content search of SYS-01 for CUI markings (1,140 items found); a sweep of all 26 FC-4 tablets; 20 A&E design sheets for markings;
   - change control: 20 CPE change tickets;
   - physical: walkthroughs of the FC-4 trailer and the headquarters project office; the July 2026 trailer visitor log against the installation gate record (41 visitors);
   - subcontractors: all 15 FC-4 subcontracts and their SPRS records.
4. **Status.** Met, Partially met, Not met, or Not applicable. For CMMC scoring, a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)), so every Partially met row counts as NOT MET in the score. The `points_deducted` column shows the value subtracted.

## 3. Results summary

### SP 800-171 Rev. 2 requirements (110)
| Family | Met | Partially met | Not met | N/A | Points lost |
|---|---|---|---|---|---|
| 3.1 Access Control (22) | 15 | 5 | 2 | 0 | 21 |
| 3.2 Awareness and Training (3) | 0 | 3 | 0 | 0 | 11 |
| 3.3 Audit and Accountability (9) | 7 | 1 | 1 | 0 | 10 |
| 3.4 Configuration Management (9) | 6 | 3 | 0 | 0 | 11 |
| 3.5 Identification and Authentication (11) | 8 | 3 | 0 | 0 | 11 |
| 3.6 Incident Response (3) | 0 | 2 | 1 | 0 | 11 |
| 3.7 Maintenance (6) | 6 | 0 | 0 | 0 | 0 |
| 3.8 Media Protection (9) | 4 | 3 | 2 | 0 | 13 |
| 3.9 Personnel Security (2) | 1 | 1 | 0 | 0 | 5 |
| 3.10 Physical Protection (6) | 2 | 4 | 0 | 0 | 8 |
| 3.11 Risk Assessment (3) | 2 | 1 | 0 | 0 | 5 |
| 3.12 Security Assessment (4) | 1 | 3 | 0 | 0 | 10 |
| 3.13 System and Communications Protection (16) | 14 | 2 | 0 | 0 | 4 |
| 3.14 System and Information Integrity (7) | 4 | 1 | 2 | 0 | 13 |
| **Total (110)** | **70** | **32** | **8** | **0** | **133** |

Of the 40 requirements not fully met, 19 are basic and 21 are derived. By location: 18 are open only because of CUI outside the enclave, 10 only in the CPE, and 12 in both.

### Clause and regulation duties (24)
| Source | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| DFARS 252.204-7012 (cloud, review, reporting, certificate, malware, preservation, forensics, flowdown, incident number) | 1 | 4 | 4 | 0 |
| DFARS 252.204-7019 and 252.204-7020 (SPRS score, Government access, subcontractor assessments) | 1 | 1 | 1 | 0 |
| DFARS 252.204-7021 and 32 CFR Part 170 (status and affirmation, CUI on assessed systems, subcontractor flowdown, scope, ESP) | 0 | 2 | 3 | 0 |
| FAR 52.204-21, 52.204-25, and 52.204-26 | 2 | 3 | 0 | 0 |
| Fla. Stat. 501.171 (employee data) | 0 | 1 | 0 | 0 |
| NISPOM | 0 | 0 | 0 | 1 |
| **Total (24)** | **4** | **11** | **8** | **1** |

**Gap risk across all 59 open rows:** 1 Very High, 26 High, 30 Moderate, 2 Low.

### Score under 32 CFR 170.24
| Item | Value |
|---|---|
| Maximum score | 110 |
| Points subtracted for the 40 requirements not fully met | 133 (21 at 5 points, 5 at 3 points including 3.13.11 as partially effective, 13 at 1 point; 3.12.4 carries no point value) |
| **Recalculated score, current scope (CPE plus where CUI actually is)** | **-23** |
| Score once CUI is removed from SYS-01, the tablets, and the trailer (outside-only gaps closed) | 31 |
| SPRS score posted 2025-02-14 | 71, CPE scope only (to be corrected by 2026-09-30) |
| Minimum for Conditional Level 2 status | 88 (score divided by 110 of at least 0.8, 32 CFR 170.21(a)(2)(i)) |

**Why 71 became -23.** The 2025 self-assessment described the enclave as designed and assumed CUI never left it. On sampled evidence, CUI reached the commercial project platform, tablets, and an open trailer table, which brings in access, mobile device, media, physical, authentication, and encryption requirements (54 points). Even inside the CPE, monitoring and correlation (3.3.5, 3.14.6, 3.14.7), incident handling and reporting (3.6.1 to 3.6.3), CUI training (3.2.1 to 3.2.3), and ongoing assessment (3.12.1, 3.12.3) were not in place.

**Point arithmetic.** 21 x 5 = 105, plus 5 x 3 = 15, plus 13 x 1 = 13, gives 133. 3.5.3 is deducted in full (5 points) because external SYS-01 users could reach CUI without MFA; the 3-point partial value applies only when MFA covers remote and privileged users (32 CFR 170.24(c)(2)(i)(B)(4)(i)). 3.13.11 is deducted 3 points because CUI outside the enclave was encrypted, but not with modules confirmed as FIPS-validated ((B)(4)(ii)).

**Conditional status limits.** Conditional status allows on a POA&M only requirements worth 1 point, plus 3.13.11 when encryption is used but not FIPS-validated, and never 3.1.20, 3.1.22, 3.12.4, 3.10.3, 3.10.4, or 3.10.5 (32 CFR 170.21(a)(2)(ii) and (iii)). Five of those six are open today: 3.1.20 (CUI in SYS-01 and subcontractor systems), 3.10.3, 3.10.4, and 3.10.5 (the FC-4 trailer), and 3.12.4 (the SSP describes the target state). **The plan therefore aims for all 110 requirements Met before the C3PAO assessment**, with a POA&M used only as a fallback for 1-point items.

## 4. Scoping decision: where CUI may live
Construction work moves drawings to trailers, tablets, and trade subcontractors. Three options were analyzed with the COO, the Vice President of Operations, the FC-4 Project Executive, and the vCISO on 2026-07-29:

| Option | What it means | Effect | Decision |
|---|---|---|---|
| A. Keep CUI in SYS-01 and bring it into scope | The commercial project platform would need FedRAMP Moderate equivalent security (252.204-7012(b)(2)(ii)(D)) and would join the CMMC scope with its 2,600 external users | The vendor has no FedRAMP authorization and could not show equivalence | **Rejected** |
| B. Confine CUI to the CPE and reach the field through virtual desktops | Remove CUI from SYS-01 and tablets; CUI RFIs and submittals move to a CPE workflow; FC-4 tablets become virtual desktop clients that allow only keyboard, video, and mouse traffic (Out-of-Scope Assets under 32 CFR 170.19(c)(1), Table 3); printed CUI only in a badge-locked CUI room in the trailer; trades receive CUI only through CPE guest accounts or their own verified systems | About 40 more CPE accounts; virtual desktop licenses; cellular coverage at the FC-4 site is adequate (tested 2026-08-12) | **Chosen.** Funded in the FY2027 plan; target 2026-12-31 |
| C. Ask the Army Corps to decontrol drawings | Some sheets (for example, finish schedules) may be over-marked | Only the Government can decide; does not solve the process problem | Pursued in parallel for specific sheets through the Contracting Officer; not relied on |

After option B, the outside-only gaps close and the score rises to 31 before any work inside the CPE. The remaining 79 points are in the CPE and in the requirements that span both.

## 5. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| G-123 Not eligible for Level 2 (C3PAO) awards | 252.204-7021(d)(1),(3); 32 CFR 170.17, 170.21, 170.22 | Very High | Complete this roadmap; C3PAO assessment; affirmation by the CEO | Chief Operating Officer | 2027-04-23 |
| G-120 SPRS score overstates implementation | 252.204-7019(b); 252.204-7020(d) | High | Post -23 with a date-to-110 of 2027-02-26, after counsel review; update after each milestone | Director of Contracts and Compliance | 2026-09-30 |
| G-112 Possible incident not reviewed | 252.204-7012(c)(1)(i) | High | Complete the review of the CUI found in SYS-01 and on tablets; report within 72 hours if compromise is found | Security Manager | 2026-10-15 |
| G-003, G-111, G-124 CUI outside the enclave | 3.1.3; 252.204-7012(b)(2)(ii)(D); 252.204-7021(d)(2) | High | Option B in section 4 | FC-4 Project Executive; IT Director | 2026-10-31 (removal); 2026-12-31 (virtual desktop field access) |
| G-020, G-118, G-122, G-125 Subcontractor flowdown and verification | 3.1.20; 252.204-7012(m)(1); 252.204-7020(g)(2); 252.204-7021(f) | High | Modify 14 trade subcontracts; verify SPRS for all 15; DFARS 252.204-7021 rider in templates before 2026-11-10 | Director of Contracts and Compliance | 2026-11-09 (rider); 2026-11-30 |
| G-113, G-114, G-055 to G-057 Incident capability and reporting | 252.204-7012(c)(1)(ii), (c)(3); 3.6.1 to 3.6.3 | High | Two medium assurance certificates; CUI incident runbook (P08); tabletop with DIBNet drill 2026-11-18 | Director of Contracts and Compliance; Security Manager | 2026-11-30 |
| G-030, G-109, G-110 Monitoring and correlation | 3.3.5; 3.14.6; 3.14.7 | High | Monitoring service in the government-community cloud with 24x7 alerting and correlation | Security Manager | 2027-01-31 |
| G-064 to G-068, G-075, G-077 to G-079 Printed CUI and the FC-4 trailer | 3.8.1 to 3.8.5; 3.10.1; 3.10.3 to 3.10.5 | High | CUI room with badge lock, numbered sets, shred bin, transport rule, escort and electronic visitor log | FC-4 Project Executive; Vice President of Operations | 2026-11-30 |
| G-018, G-019, G-045, G-098 Tablets with CUI | 3.1.18; 3.1.19; 3.5.2; 3.13.11 | High | Enroll the 9 unmanaged tablets; lock FC-4 tablets to the virtual desktop client | Vice President of Operations | 2026-12-31 |
| G-001, G-074 Account lifecycle | 3.1.1; 3.9.2 | High | Monthly A&E roster reconciliation; 30-day guest expiry; transfer trigger | FC-4 Project Executive; HR Director | 2026-11-30 |
| G-023 to G-025 CUI training | 3.2.1 to 3.2.3 | Moderate | CUI awareness and role-based training for all CPE users, FC-4 field staff, and trade foremen | HR Director; Security Manager | 2026-11-30 |
| G-084, G-086 Assessment and monitoring of controls | 3.12.1; 3.12.3 | Moderate | Full SP 800-171A self-assessment 2026-12; monthly control metrics | GRC analyst | 2027-03-31 |

**Roadmap by milestone:**
1. **By 2026-09-30:** corrected SPRS score of -23 posted for the CPE scope, with a date-to-110 of 2027-02-26.
2. **By 2026-10-31:** CUI removed from SYS-01 and the review under 252.204-7012(c)(1)(i) closed; two medium assurance certificates; shred bin and transport rule; trailer rekeyed; Section 889 check of rented equipment; SAM representation reviewed by counsel.
3. **By 2026-11-30:** CUI room in the FC-4 trailer; flowdown to 14 trades and SPRS verification of all 15 subcontractors; DFARS 252.204-7021 rider in templates (before 2026-11-10); CUI training; CUI incident tabletop with DIBNet drill (2026-11-18); asset inventory with CMMC categories.
4. **By 2026-12-31:** FC-4 tablets as virtual desktop clients; download and clipboard blocked; data loss prevention on CUI markings; CPE backup; monthly scanning including enclave laptops; full self-assessment against SP 800-171A objectives.
5. **By 2027-01-31:** CPE monitoring service with correlation and 1-year retention; ESP documentation if the MSSP runs it; monthly control metrics.
6. **2027-02-26:** target date for a score of 110; SSP re-verified.
7. **2027-03:** readiness check by the co-sourced internal audit firm; corrected SPRS score if all requirements are Met.
8. **2027-04-12 to 2027-04-23:** C3PAO Level 2 certification assessment, about 3 months before the expected follow-on MATOC award.

The full list, with evidence, is in `gap-analysis.csv`. High and Very High gaps are carried into the risk register (P01: R-003, R-004, R-007, R-008, R-009, R-016) and the POA&M (P07).

**A word on representations.** The SPRS score, the SAM representations, and any CMMC affirmation are statements to the Government. An inaccurate one creates exposure under the False Claims Act (31 U.S.C. 3729) and contract remedies (P01 R-008). The corrected score is posted with counsel review, and the internal audit firm reperforms every score before it is posted.

## 6. Pending regulatory changes
- **FAR CUI rule:** proposed (90 FR 4278, 2025-01-15) and not final. Nothing changes until it is final; DFARS 252.204-7012 remains the governing clause (flagged on G-111 and G-118).
- **Revolutionary FAR Overhaul:** a proposed rule (FR Doc. 2026-12559, 2026-06-23) would reorganize FAR parts, including part 40. FAR 52.204-21 numbering may change (flagged on G-128 and G-129). Not final.
- **SP 800-171 Rev. 3:** published by NIST, but CMMC Level 2 is fixed to Rev. 2 (32 CFR 170.14(c)(3)). Each requirement row names its Rev. 3 counterpart in `pending_rule_change` for later planning. Rev. 3 is not treated as a current obligation.
- **CMMC Phase 3 (2027-11-10, 32 CFR 170.3(e)(3)):** DoD intends to require Level 2 (C3PAO) for all applicable solicitations and as a condition to exercise option periods on contracts awarded after the effective date. **Phase 4 (2028-11-10)** reaches option periods on older contracts.
- **CIRCIA:** the final rule is not published. Proposed reporting deadlines are not treated as current obligations.

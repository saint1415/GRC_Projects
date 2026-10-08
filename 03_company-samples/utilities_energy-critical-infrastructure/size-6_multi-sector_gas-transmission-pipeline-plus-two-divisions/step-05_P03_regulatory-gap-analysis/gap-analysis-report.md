# Regulatory Gap Analysis: Cris Santos Company Holdings | Energy | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Energy (focus division: Gas Transmission) |
| Primary regulation (focus division) | TSA Security Directive Pipeline-2021-02G (C-ENERGY-R03), effective 2026-05-03 through 2027-05-02, with SD Pipeline-2021-01G (C-ENERGY-R02), effective 2026-01-16 through 2027-01-15. Both read from the TSA-published text |
| Division regulations | Gathering and Production: PHMSA gathering rules (49 CFR 192.8, 192.9, Part 191) plus NIST CSF 2.0 with SP 800-82 Rev. 3 as the voluntary benchmark. Integrity Services: SSI rules (49 CFR Part 1520), its role under clients' TSA directives, and client contracts |
| Gap tables | `gap-analysis.csv` (Gas Transmission, 127 rows); `gap-analysis-gathering-production.csv` (29 rows); `gap-analysis-integrity-services.csv` (21 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads with the Gas Transmission Pipeline Safety Compliance Director and the Gathering Compliance Manager, coordinated by the Group General Counsel; reviewed by group internal audit |
| Regulatory text | eCFR (point in time 2026-09-23) for 49 CFR Parts 191, 192, and 1520 and 18 CFR Parts 260, 284, and 388; TSA-published SD texts; Federal Register |

## 1. Applicability
### 1.1 Who is designated under the TSA directives
Both directives apply to "Owners and Operators of a hazardous liquid and natural gas pipeline or a liquefied natural gas facility notified by TSA that their pipeline system or facility is critical" (SD 02G applicability line; SD 01G Section II.A.1). There is no size threshold; designation is TSA's decision. SD 02G Section VII.P limits Owner/Operator to those identified by TSA "as one of the most critical interstate and intrastate natural gas and hazardous liquid transmission pipeline infrastructure and operations."

| Entity | TSA status | Basis |
|---|---|---|
| Gas Transmission | **Designated.** TSA notified the division in 2021 that its pipeline system is critical. TSA approved its Cybersecurity Implementation Plan on 2023-01-27 | TSA notification letter (SSI); SD 02G Sections II.A.1 and II.B |
| Gathering and Production | **Not designated.** No TSA notice; gathering systems are not on TSA's critical list | Correspondence file; confirmed 2026-06-12 (GG-07) |
| Integrity Services | **Not an owner/operator.** It is an **authorized representative** (SD 02G Section VII.A) for 9 designated clients when its OT Assessment Practice performs architecture design reviews or testing, and both it and the client are liable for its non-compliance (Section II.A.4) | Client engagement letters (IG-09) |
| Corporate shared services | Not an owner/operator. Corporate staff are not direct employees of the Gas Transmission subsidiary, so the implementation plan treats corporate as a provider of shared measures, in the way SD 02G Section II.A.3 treats a managed security service provider: **the division keeps sole responsibility** for the measures corporate performs | TSA plan inheritance annex (G-003) |

**Plans that set the inspection standard.** SD 02G says the TSA-approved Cybersecurity Implementation Plan "sets the security measures and requirements against which TSA inspects for compliance." The rows below test the SD requirements and, where the plan sets a schedule or a specific measure, the plan.

### 1.2 What else applies, by division
- **Gas Transmission:** PHMSA control room management, 49 CFR 192.631, in full (controllers use SCADA and the system has compressor stations, so the reduced-procedure exception in 192.631(a)(1)(ii) does not apply). Only the SCADA-relevant duties are decomposed (34 rows); paragraph (d), fatigue mitigation, is a human-factors duty outside this analysis. Part 1520 applies because the division holds SSI. FERC rules apply to it as an interstate natural gas company: service interruption reports (18 CFR 260.9), NAESB WGQ standards including the WGQ Cybersecurity Related Standards incorporated in 18 CFR 284.12(a)(1)(vii) (standard text not reproduced), and CEII requests (18 CFR 388.113).
- **Gathering and Production:** 192.631 does **not** apply. Under 192.9, Type B lines (192.9(d)) and Type C lines (192.9(e)) carry a listed set of Part 192 duties, and neither list includes 192.631; the division has no Type A lines. Type C lines 8.625 inches or larger need 192.615 emergency plans (192.9(e)(1)(iv)). Part 191 reporting applies to all onshore gathering lines, including Type R (191.1(a)). With no binding cyber rule, the group uses the mining and oil and gas vertical's benchmark: **NIST CSF 2.0 with SP 800-82 Rev. 3** (label `N21-BM`). The 22 subcategories were chosen for a SCADA-operated gathering system; this is not a full CSF profile. SP 800-82 Rev. 3 section numbers are cited; its Section 6 is organized by CSF 1.1 categories, so CSF 2.0 IDs are used for the outcomes.
- **Integrity Services:** it is a **covered person** under 49 CFR 1520.7(j) (access to SSI under 1520.11) and (k) (contracted to or acting for a covered person), so Part 1520 applies directly. Client contracts add a 72-hour incident notice, SOC 2 reporting, deletion, and subservice terms.

### 1.3 Screened out, with reasons
- **NERC CIP (C-ENERGY-R01) and DOE-417:** no NERC registration, no Bulk Electric System assets, no electric operations.
- **49 CFR 195.446:** no hazardous liquid pipelines.
- **USCG 33 CFR Part 101 Subpart F (N21-R01):** no MTSA or Outer Continental Shelf facilities.
- **FTC Safeguards Rule (N54-R01):** Integrity Services is not a financial institution under 16 CFR 314.2 (IG-20). Other professional-services rules (tax preparer, federal contractor, HIPAA business associate, professional conduct) do not apply (IG-21).
- **CIRCIA (C-ENERGY-R05):** final rule not published as of 2026-09-25; tracked only.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Gas Transmission | Gathering and Production | Integrity Services | Group (corporate) |
|---|---|---|---|---|
| C-ENERGY-R03 SD Pipeline-2021-02G | **Primary.** Designated; TSA-approved implementation plan, incident response plan, assessment plan | Not designated | Liable as authorized representative for 9 designated clients (II.A.4); client results are SSI (IV.B) | Performs shared measures; division keeps responsibility (II.A.3 by analogy) |
| C-ENERGY-R02 SD Pipeline-2021-01G | Applies. Coordinator 24/7; CISA report within 72 hours | Not designated; voluntary CISA reporting | Not an owner/operator | SOC OT desk manager is an alternate Coordinator |
| C-ENERGY-R04 49 CFR 192.631 | Applies in full | Does not apply (192.9) | Not an operator | Not applicable |
| PHMSA 192.615, Part 191 | Applies | Applies (Type C emergency plans; Part 191 for all gathering) | Not an operator | Not applicable |
| SSI 49 CFR Part 1520 | Covered person | Not applicable (no SSI held) | **Covered person** (1520.7(j), (k)) | Holds SSI on shared platforms; follows division rules |
| FERC 18 CFR 260.9, 284.12, 388.113 | Applies (interstate natural gas company) | Not applicable (gathering is not FERC-jurisdictional transportation in this sample) | CEII received from clients under agreements | Not applicable |
| N21-BM CSF 2.0 with SP 800-82 Rev. 3 | Used as the program framework | **Benchmark** for gap analysis | Used for OT assessment methodology | Group policies aligned to CSF 2.0 |
| Client contracts and SOC 2 | Shipper tariff and interconnect agreements | Purchaser and royalty agreements | **Applies** (72-hour notice; SOC 2 Type 2 on the IDP, P09) | Group services carved into the IDP report |
| FTC Act Section 5 | General | General | Applies to service and security claims (IG-17) | General |
| N55-R01 Reg S-K Item 106; N55-R02 Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach and data security laws | Employee data | **Royalty owners** in all 50 states (GG-05) | Client staff contact data | Coordinates; Florida worked example (Fla. Stat. 501.171) |
| C-ENERGY-R05 CIRCIA | Tracked (proposed) | Tracked | Tracked | Tracked |
| C-ENERGY-R01 NERC CIP | Not applicable | Not applicable | Not applicable | Not applicable |

## 3. Method
1. **Requirements.** SD rows follow the directives' own section numbers, at the most granular paragraph that imposes a separate duty; TSA states the SDs are not SSI. CFR rows follow the regulations' paragraph structure and use brief quotes of public-domain text. Client contract rows paraphrase the group's standard terms. The NAESB WGQ standards are copyrighted and are cited only by number.
2. **Crosswalk.** SD, CFR, and contract rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such; no official NIST mapping exists for them. CSF benchmark rows use the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), with OT additions from the SP 800-82 Rev. 3 overlay labeled as author additions.
3. **Evidence.** Interviews with the Director of Pipeline Cybersecurity, the Director of Gas Control, the SCADA Engineering Manager, the Gathering Compliance Manager, the Integrity Services Client Security Officer, and the OT Assessment Practice Leader; the TSA plans and correspondence (reviewed as SSI, cited by section only); configuration exports; and P07 test results, including OT tests at Compressor Station 27 (2026-08-12) and Arkoma field sites (2026-08-19).
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 4. Results
### 4.1 Gas Transmission (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| SD 02G Sections II and V (applicability, plan, procedures) | 6 | 1 | 0 | 1 |
| SD 02G III.A and III.B (Critical Cyber Systems, segmentation) | 5 | 2 | 0 | 0 |
| SD 02G III.C (access control) | 4 | 3 | 2 | 0 |
| SD 02G III.D (monitoring and detection) | 9 | 4 | 0 | 0 |
| SD 02G III.E (patching) | 1 | 4 | 0 | 0 |
| SD 02G III.F (incident response plan) | 6 | 1 | 0 | 0 |
| SD 02G III.G (assessment plan) | 6 | 1 | 1 | 0 |
| SD 02G IV and VI (records, SSI, amendments) | 5 | 3 | 2 | 1 |
| SD 01G (Coordinator, CISA reporting) | 11 | 2 | 0 | 1 |
| 49 CFR 192.631 (SCADA-relevant duties) | 29 | 5 | 0 | 0 |
| 49 CFR 1520.9 (SSI) | 5 | 2 | 0 | 0 |
| FERC 18 CFR 260.9, 284.12, 388.113 | 3 | 1 | 0 | 0 |
| **Total (127)** | **90** | **29** | **5** | **3** |

The TSA program is largely in place: 53 of 82 SD rows are met, 21 partially met, and 5 not met. The 34 gaps are rated 14 High, 16 Moderate, 4 Low. The **5 Not met rows** are all scenario gap 5, TSA plan discipline:
- **III.C.1.b and III.C.4.b (G-017, G-022):** station unit control panel password mitigations are past the plan schedule at 11 of 41 stations, and 7 technicians who left still know shared panel passwords.
- **VI.B and VI.D (G-067, G-068):** the revised panel schedule is a permanent change (in effect 45 or more days, Section VI.C) for which no amendment request was filed within 50 days.
- **III.G.2.b (G-051):** the biennial architecture design review lapsed on 2026-05-20.

The High partial gaps are about **the seams with corporate IT**: measurement servers in the corporate directory (III.B, III.B.2.a), an incident response plan that assumes business IT returns within 24 hours (III.F.1), the shared OT remote access gateway (III.C.3), missing baseline-deviation alerts on 4 external connections (III.D.2.b), and an assessment pace of 22% against the one-third annual requirement (III.G.2.d). One 192.631 gap is also High: leak-detection model threshold changes bypass control room change management (192.631(f)(3), G-104).

### 4.2 Gathering and Production (`gap-analysis-gathering-production.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| A. Binding rules: PHMSA gathering (192.8, 192.9, Part 191), state data security, TSA screen | 2 | 3 | 0 | 2 |
| B. CSF 2.0 Govern | 1 | 1 | 2 | 0 |
| B. CSF 2.0 Identify | 0 | 3 | 1 | 0 |
| B. CSF 2.0 Protect | 2 | 5 | 2 | 0 |
| B. CSF 2.0 Detect | 0 | 1 | 1 | 0 |
| B. CSF 2.0 Respond | 1 | 1 | 0 | 0 |
| B. CSF 2.0 Recover | 1 | 0 | 0 | 0 |
| **Total (29)** | **7** | **14** | **6** | **2** |

Gaps are rated 3 High, 16 Moderate, 1 Low. The binding pipeline safety rules are largely met; the open items are a loss-of-SCADA scenario in the Type C emergency plans (GG-02), a link from the cyber procedure to the Part 191 one-hour notice (GG-04), and royalty owner payment files kept on a file share without a retention limit (GG-05). The CSF gaps concentrate in two places: the **Arkoma acquired fields** (scenario gap 4: GG-13, GG-17, GG-21, GG-26 are Not met) and **governance drift** (inheritance undocumented, GG-09; supplement last aligned in 2023, GG-10).

### 4.3 Integrity Services (`gap-analysis-integrity-services.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Part 1520 (SSI) as a covered person | 0 | 3 | 5 | 0 |
| TSA SD 02G as authorized representative | 1 | 1 | 1 | 1 |
| Client contracts, CEII, FTC Act Section 5 | 0 | 5 | 1 | 0 |
| Client regulatory duties and screened-out rules | 1 | 0 | 0 | 2 |
| **Total (21)** | **2** | **9** | **7** | **3** |

Gaps are rated 7 High, 7 Moderate, 2 Low. **The division holds SSI but has no SSI program** (scenario gap 2). Part 1520 marking, need-to-know, destruction, intake, and disclosure-reporting duties are Not met (IG-03, IG-05 to IG-08), and the same gap makes it Not met as an authorized representative storing client assessment results (IG-12). The OT assessment methodology itself is sound (IG-11). The ILI anomaly classification model in client deliverables is undisclosed and unvalidated, and marketing claims Part 1520 handling that does not yet exist (IG-17).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | TSA plan schedule slip, no amendment request, review lapsed (5) | GT | SD 02G II.B.2, III.C.1.b, III.C.4.b, III.G.2.b, III.G.2.d, VI.B, VI.D | High | Notify TSA and file the amendment request by 2026-10-30; finish panel mitigations; complete the architecture design review; resource the assessment schedule | Director of Pipeline Cybersecurity | 2026-12-31 (POAM-008, POAM-009) |
| 2 | Business-critical services on corporate IT (1) | GT, GP | SD 02G III.B, III.B.2.a, III.F.1 | High | Measurement enclave with its own identity store; 72-hour manual scheduling and measurement procedure, exercised | Vice President of Commercial Operations | 2027-06-30 (POAM-006, POAM-007) |
| 3 | SSI program in Integrity Services (2) | IS, GT | 49 CFR 1520.7, 1520.9, 1520.13, 1520.19; SD 02G IV.B, II.A.4 | High | SSI owner, procedures, marking, need-to-know groups, separate SSI store, enforced deletion; contract addendum for designated clients | Integrity Services Client Security Officer | 2027-03-31 (POAM-019, POAM-020, POAM-024) |
| 4 | Shared OT access paths (3) | All | SD 02G III.C.3; CSF PR.AA-05 | High | Split the gateway by division; remove standing engineer access to the historian replica | Group OT Security Director | 2026-12-31 (POAM-001, POAM-002, POAM-021) |
| 5 | Arkoma acquired fields (4) | GP | CSF ID.AM-03, PR.AA-03, PR.PS-02, DE.CM-06 | High | Vendor access through the gateway with MFA and recording; migrate to SYS-P1 | Vice President of Field Operations Technology | 2027-06-30 (POAM-014, POAM-015) |
| 6 | AI in safety-relevant work (9) | GT, IS | 192.631(f)(3), (e)(5); client terms; FTC Act Section 5 | High | Model changes through control room management of change; validate and disclose the ILI model | Director of Gas Control; Vice President of Integrity Engineering | 2027-03-31 (POAM-023, POAM-026) |
| 7 | Cross-division notification (8) | All | SD 01G II.C.3; 49 CFR 1520.9(c); 18 CFR 260.9; 191.5; client 72-hour terms; Form 8-K Item 1.05 | Moderate | One reporting procedure with night owners, FERC, SSI, and client steps; cross-division tabletop | Group General Counsel | 2026-12-15 (POAM-004, POAM-005) |
| 8 | Control room records and training (6) | GT | 192.631(c)(2), (h)(1), (j)(1) | Moderate | Re-verify points at 3 stations; cyber abnormal-condition training | Director of Gas Control | 2027-03-31 (POAM-010, POAM-011) |
| 9 | Gathering governance (7, 10) | GP | CSF GV.RR-02, GV.PO-02 | Moderate | Inheritance matrix; re-issue the supplement | Gathering and Production security and compliance lead | 2026-12-31 (POAM-017, POAM-018) |
| 10 | Royalty owner data retention | GP | Fla. Stat. 501.171(2), (8) (worked example; each state's law) | Moderate | Stop monthly exports; purge history | Revenue Accounting Vice President | 2026-12-31 (POAM-025) |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-023, POAM-024, and POAM-025 trace directly to this analysis.

### Group-wide obligations
| Obligation | Status | Note |
|---|---|---|
| N55-R01 Reg S-K Item 106 (17 CFR 229.106) | Met | Annual disclosure of cyber risk management, strategy, and governance in the 10-K; P01 section 5 feeds it |
| N55-R02 Form 8-K Item 1.05 | Partially met | Disclosure committee charter covers cybersecurity materiality, but no cross-division exercise has included a materiality decision (POAM-004) |
| State breach laws (each state where affected individuals reside; Florida worked example) | Partially met | Matrix lists state duties for royalty owners and employees; not exercised across divisions (POAM-004) |
| OFAC ransomware advisory (2021-09-21) | Met | Sanctions check required before any payment (POL-03) |

## 6. Pending regulatory changes (none treated as current obligations)
- **SD renewals.** SD 01G expires 2027-01-15 and SD 02G expires 2027-05-02. Each renewal must be read for changes before the plan is next amended.
- **TSA "Enhancing Surface Cyber Risk Management" NPRM** (November 7, 2024) would make pipeline cyber requirements permanent regulations. Not final as of 2026-09-25.
- **CIRCIA final rule** (C-ENERGY-R05): not published as of 2026-09-25. Reporting duties would begin only on the final rule's effective date.
- **NIST SP 800-82 Rev. 4, initial public draft** (2026-09-21; comments due 2026-11-30) restructures the OT guide around CSF 2.0. The Gathering benchmark rows still use Rev. 3 section numbers.

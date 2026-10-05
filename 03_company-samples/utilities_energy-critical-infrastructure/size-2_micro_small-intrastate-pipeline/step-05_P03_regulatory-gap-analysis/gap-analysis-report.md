# Regulatory Gap Analysis: Cris Santos Company | Energy | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (small intrastate natural gas transmission pipeline operator) |
| Tier / Vertical | Micro / Energy |
| Primary regulation named for this vertical | TSA Security Directive Pipeline-2021-02G (C-ENERGY-R03): **not applicable**, kept as a readiness reference |
| Binding rules analyzed | PHMSA control room management, 49 CFR 192.631 (C-ENERGY-R04), at its reduced scope; and the SCADA-related duties in 49 CFR 192.605 and 192.615. Text read from eCFR, current through 2026-09-23 |
| Cyber benchmark analyzed | NIST CSF 2.0 outcomes, with NIST SP 800-82 Rev. 3 (Guide to OT Security, September 2023) as the OT implementation guide |
| Assessment dates | 2026-07-20 to 2026-07-31 (TSA status confirmed 2026-07-22) |
| Assessor | Office Manager (security program coordinator) and Operations Manager, with the MSP lead technician |
| Approved | 2026-09-15 by the Owner |

## 1. Applicability

### 1.1 TSA Security Directive Pipeline-2021-02G: does not apply
The directive applies to "Owners and Operators of a hazardous liquid and natural gas pipeline or a liquefied natural gas facility notified by TSA that their pipeline system or facility is critical." Section II.A.2 says that when TSA identifies additional critical owner/operators, "TSA will notify the Owner/Operator and provide specific compliance deadlines." There is no numeric threshold. Designation is TSA's decision, not a size test.

**Finding.** Cris Santos Company has never received a TSA notification. The Owner confirmed this on 2026-07-22, and the correspondence file holds no TSA letter. **SD Pipeline-2021-02G does not apply, and neither does SD Pipeline-2021-01G (C-ENERGY-R02)**, which has the same applicability. Both were read from the TSA-published text (02G effective 2026-05-03 through 2027-05-02; 01G effective 2026-01-16 through 2027-01-15). For a 26-mile line with 3 delivery points, designation is unlikely, but the company keeps the 20 SD rows (G-046 to G-065) as a readiness reference because they describe a sound cyber program for any pipeline.

### 1.2 What does apply
**49 CFR 192.631 applies, at a reduced scope.** 192.631(a)(1) covers "each operator of a pipeline facility with a controller working in a control room who monitors and controls all or part of a pipeline facility through a SCADA system." The company's 3 controllers do that, from the gas control desk and from laptops on call. But for a control room limited to "transmission without a compressor station," 192.631(a)(1)(ii) requires written procedures that implement **only paragraphs (d) (fatigue), (i) (compliance validation), and (j) (compliance and deviations)**. The company has no compressor station, so:
- 9 rows are analyzed: (a)(1), (a)(2), (d)(1) to (d)(4), (i), (j)(1), and (j)(2).
- Paragraphs (b), (c), (e), (f), (g), and (h) are recorded as Not applicable (6 rows). These include the alarm management, point-to-point verification, backup SCADA testing, and change management duties that bind the Small sample. The company keeps some of them as good practice and says so in each row.

As an intrastate operator, the company is inspected by the Florida Public Service Commission (FPSC), which holds a 49 U.S.C. 60105 certification from PHMSA. Rule 25-12.005, F.A.C., adopts 49 CFR Parts 191 and 192 by reference, and 192.631(i) directs procedures to the state agency for an intrastate facility.

**The SCADA-related duties in 192.605 and 192.615 also apply.** Because 192.631 binds so little here, the analysis adds the 6 duties in the O&M manual and emergency plan rules that govern how SCADA is used: 192.605(b)(12), (c)(1)(iii), and (c)(3), and 192.615(a)(6), (a)(11), and (a)(12). 192.615(a)(12) matters for the AI trial in P10: rupture identification procedures must "specify the sources of information, operational factors, and other criteria" personnel use.

**NIST CSF 2.0 with SP 800-82 Rev. 3 as the cyber benchmark.** No binding rule requires cybersecurity controls for this pipeline. The company chose CSF 2.0 because it is sector-neutral and is the framework SP 800-61 Rev. 3 and the P08 runbook use. SP 800-82 Rev. 3 supplies OT guidance. SP 800-82 Rev. 3 Section 6 is organized by CSF 1.1 categories, so this analysis cites SP 800-82 section numbers only and uses CSF 2.0 IDs for outcomes. The 24 subcategories (G-022 to G-045) were picked for relevance to a small SCADA-operated pipeline. This is not a full CSF profile.

**Not applicable, with reasons:**
- **NERC CIP (C-ENERGY-R01):** not a NERC-registered entity; no Bulk Electric System assets.
- **DOE Form DOE-417:** electric emergencies only; no electric operations.
- **CIRCIA (C-ENERGY-R05):** proposed only; no final rule had been published at approval. Under the proposal, as corrected (FR Doc. 2024-12084), the pipeline criterion would cover an owner or operator "required to report cyber incidents by the Transportation Security Administration," which the company is not. With about $1.1 million in receipts it is also far below the SBA size standard used by the proposed size criterion. Recheck when a final rule is published.

## 2. Method
1. **Requirements.**
   - 192.631, 192.605, and 192.615 rows follow each rule's own paragraph structure, at the most granular citation that imposes a separate duty. Brief quotes are used; this is public-domain federal text.
   - CSF rows use the subcategory text from `00_universal-framework/frameworks/csf2_core.csv`, with the SP 800-82 Rev. 3 section that gives OT guidance.
   - TSA SD rows follow the SD's own section numbers. TSA states the SD is not Sensitive Security Information.
2. **Crosswalk.**
   - Pipeline rule rows and TSA SD rows use an author mapping to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. No official NIST mapping exists for them.
   - CSF rows use the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). Where an OT control was added, the `crosswalk_source` column names it as an author addition.
3. **Documentary evidence.** Each status rests on a named document or record: the CRM procedures, O&M manual, emergency plan, rupture identification procedure, on-call schedule and hours-of-service log, training records, FPSC 2025 inspection letter, SCADA user list and role matrix, SCADA access settings, contracts, the MSP device list and patch report, carrier APN settings, and a walkthrough of the office and 2 field sites on 2026-07-22. Interviews covered all 7 staff and the MSP lead technician.
4. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork (2026-07-31). Actions completed since then are noted in the remediation column but do not change the status. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| **A. 49 CFR 192.631 (binding, reduced scope)** | 2 | 6 | 1 | 6 |
| **B. 49 CFR 192.605 and 192.615 (SCADA-related duties)** | 2 | 4 | 0 | 0 |
| **C. NIST CSF 2.0 with SP 800-82 Rev. 3 (benchmark)** | | | | |
| Govern | 0 | 1 | 3 | 0 |
| Identify | 0 | 2 | 3 | 0 |
| Protect | 0 | 7 | 3 | 0 |
| Detect | 0 | 0 | 2 | 0 |
| Respond | 0 | 0 | 2 | 0 |
| Recover | 0 | 0 | 1 | 0 |
| Subtotal CSF (24) | 0 | 10 | 14 | 0 |
| **D. TSA SD Pipeline-2021-02G (readiness only)** | 0 | 0 | 0 | 20 |
| **Total (65)** | **4** | **20** | **15** | **26** |

**Reading the results.** The pipeline safety program is in reasonable shape: the gaps in the binding rules are about records and keeping procedures current (fatigue on night callouts, deviation records), plus one High gap: no criteria for a precautionary shut-in after a cyber event (G-019). The cyber program barely exists: no CSF outcome is fully met, and 14 of 24 are not met at all.

The 35 unmet or partially met rows break down by gap risk as follows:
- Binding pipeline rules (sections A and B): 1 High, 9 Moderate, 1 Low.
- CSF benchmark (section C): 5 High, 17 Moderate, 2 Low.
- In total: 6 High, 26 Moderate, 3 Low.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| No criteria for a precautionary shut-in after a cyber event | 192.615(a)(6) (G-019); CSF RS.MI-01 (G-044) | High | Cyber annex with the P08 decision table, agreed with the municipal system | Operations Manager | 2026-11-30 |
| No cyber incident response plan | CSF ID.IM-04, RS.MA-01 (G-030, G-043) | High | P08 runbook (approved 2026-09-15); tabletop | Office Manager | 2026-11-30 |
| Password-only SCADA access with command rights | CSF PR.AA-03 (G-032) | High | Vendor app-based MFA on every SCADA account | Operations Manager | 2026-10-31 |
| Gas control desk on the flat office network | CSF PR.IR-01 (G-039) | High | Separate segment and dedicated workstations | Office Manager (MSP performs) | 2026-11-30 |
| Night callouts not counted toward hours-of-service; deviations not documented | 192.631(d)(1), (d)(4), (j)(2) (G-005, G-008, G-015) | Moderate | Count callouts; rest rule; deviation form | Operations Manager | 2026-10-31 |
| Fatigue education lapsed since 2023 | 192.631(d)(2) (G-006) | Moderate | Annual education with attendance records | Operations Manager | 2026-10-31 |
| Leak-module alerts not addressed in rupture identification procedures | 192.615(a)(12) (G-021) | Moderate | State that alerts are advisory only (P10) | Operations Manager | 2026-10-31 |
| Loss of the desk, a vendor outage, or untrusted SCADA data not in abnormal operation procedures | 192.605(c)(1)(iii) (G-017) | Moderate | Add three cases with the manual operation call list | Operations Manager | 2026-11-30 |
| Shared and stale SCADA credentials | CSF PR.AA-01 (G-031) | Moderate | Named desk accounts; last-day checklist | Operations Manager | 2026-10-31 |
| No supplier security terms | CSF GV.SC-05 (G-024) | Moderate | Addendum for the SCADA vendor, MSP, and carrier | Owner | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07). The 192.631 gaps (G-001, G-005 to G-008, G-014, G-015) are also tracked by the Operations Manager for the next FPSC inspection, because the FPSC can cite them (P01 R-020).

## 5. Remediation plan
The plan fits a 7-person company: most actions are one-page procedures, vendor settings, or MSP projects. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Governance and plans | 2026-09-30 | Policies POL-02 to POL-04 approved 2026-09-15; written roles; P08 runbook approved 2026-09-15 | G-022, G-023, G-043 |
| 2. Access and fatigue | 2026-10-31 | SCADA MFA and named desk accounts; last-day checklist; CRM procedure revision with callout counting, rest rule, and deviation form; fatigue education; rupture identification wording for the leak module; inventory and diagram; configuration export; awareness training starts; monthly log review starts | G-001, G-005 to G-008, G-015, G-021, G-026 to G-028, G-031, G-032, G-034, G-036, G-042 |
| 3. Separation and response | 2026-11-30 | Separate segment and dedicated desk workstations; cyber annex to the emergency plan; abnormal operation additions; on-call controller actions; tabletop | G-017, G-018 to G-020, G-030, G-037, G-039, G-044, G-045 |
| 4. Resilience and suppliers | 2026-12-31 | Second-carrier SIMs; office failover router; EDR and sign-in alerts; supplier addendums; supplier reviews; records filing; advisory checks; role reviews | G-014, G-024, G-025, G-029, G-033, G-040, G-041 |
| 5. Longer items | 2027-03-31 | Firmware review process; cyber scenarios in controller training | G-035, G-038 |

Remaining Low and process items (G-002 and G-016 upkeep, G-027) ride with phase 2. Progress is reviewed at the Owner's monthly meeting, using the P07 POA&M as the tracker.

## 6. Designation readiness and pending changes
**If TSA designated the pipeline.** SD 02G would require a TSA-approved Cybersecurity Implementation Plan (Sections III.A to III.E), a Cybersecurity Incident Response Plan exercised at least annually (III.F), and a Cybersecurity Assessment Plan (III.G). SD 01G would add a Cybersecurity Coordinator and alternate available 24/7 and reporting of cybersecurity incidents to CISA no later than 72 hours after identification.

Of the 20 SD readiness rows, 1 is ready (III.C.5: the company has no on-premises directory, so no domain trusts exist), 5 are partially ready, and 13 are not ready. The applicability row (G-046) has no readiness rating. Every not-ready item depends on a CSF gap already in the plan above. Plans submitted to TSA would become SSI under 49 CFR Part 1520, so POL-04 includes an SSI rule to activate on designation.

**Proposed changes (none treated as current obligations):**
- **TSA "Enhancing Surface Cyber Risk Management" NPRM** (November 7, 2024) would make pipeline cyber requirements permanent regulations. It was not final at approval. Its effect on non-designated pipelines was not analyzed here.
- **CIRCIA final rule** (C-ENERGY-R05): not published at approval. See section 1.2.

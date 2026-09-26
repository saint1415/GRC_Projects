# Regulatory Gap Analysis: Cris Santos Company | Energy | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (intrastate natural gas transmission pipeline operator) |
| Tier / Vertical | Small / Energy |
| Primary regulation named for this vertical | TSA Security Directive Pipeline-2021-02G (C-ENERGY-R03): **not applicable**, kept as a readiness reference |
| Binding rule analyzed | PHMSA control room management, 49 CFR 192.631 (C-ENERGY-R04), SCADA-relevant duties. Text read from eCFR, current through 2026-09-23 |
| Cyber benchmark analyzed | NIST CSF 2.0 outcomes, with NIST SP 800-82 Rev. 3 (Guide to OT Security, September 2023) as the OT implementation guide |
| Assessment dates | 2026-08-03 to 2026-08-14 (applicability confirmed 2026-08-05) |
| Assessor | IT Manager with the Gas Control Manager, SCADA Engineer, and Pipeline Safety and Compliance Manager |

## 1. Applicability

### 1.1 TSA Security Directive Pipeline-2021-02G: does not apply
The directive's applicability line reads: "Owners and Operators of a hazardous liquid and natural gas pipeline or a liquefied natural gas facility notified by TSA that their pipeline system or facility is critical." Section II.A.1 applies it to owner/operators of TSA-designated critical pipeline systems notified before July 26, 2022. Section II.A.2 says that when TSA identifies additional critical owner/operators, "TSA will notify the Owner/Operator and provide specific compliance deadlines." The definition of Owner/Operator in Section VII.P is limited to those "identified by TSA as one of the most critical interstate and intrastate natural gas and hazardous liquid transmission pipeline infrastructure and operations." Footnote 9 ties the population to 6 U.S.C. 1207(b), which covers the 100 most critical pipeline operators. There is no numeric threshold. Designation is TSA's decision, not a size test.

**Finding.** Cris Santos Company has never received a TSA notification. The President and the Pipeline Safety and Compliance Manager confirmed this on 2026-08-05, and the correspondence file holds no TSA letter. **SD Pipeline-2021-02G does not apply, and neither does SD Pipeline-2021-01G (C-ENERGY-R02)**, which has the same applicability. Both directives were read from the TSA-published text (02G effective 2026-05-03 through 2027-05-02; 01G effective 2026-01-16 through 2027-01-15).

**Why keep it as a readiness reference.** TSA can designate the pipeline at any time and would then set deadlines. The 20 SD rows in `gap-analysis.csv` (G-072 to G-091) are marked Not applicable and carry a readiness note pointing to the CSF benchmark row that would close each one. Section 5 summarizes what designation would add.

### 1.2 What does apply
**49 CFR 192.631 applies in full.** 192.631(a)(1) covers "each operator of a pipeline facility with a controller working in a control room who monitors and controls all or part of a pipeline facility through a SCADA system." The reduced-procedure exception covers only control rooms limited to distribution with fewer than 250,000 services or to "transmission without a compressor station." The company runs transmission **with** a compressor station, so the exception does not apply.

As an intrastate operator, the company is inspected by the Florida Public Service Commission (FPSC), which holds a 49 U.S.C. 60105 certification from PHMSA. Rule 25-12.005, F.A.C., adopts 49 CFR Parts 191 and 192 by reference. 192.631(i) directs procedures to the state agency for an intrastate facility.

**Scope of this analysis within 192.631.** 192.631 is a safety rule, not a cybersecurity rule. It contains no cyber controls. It is analyzed here because it is the binding rule that governs how controllers use SCADA:
- Rows G-001 to G-034 cover paragraphs (a), (b), (c), (e), (f), (g), (h), (i), and (j): 34 duties.
- **Paragraph (d), fatigue mitigation (4 duties), is outside this analysis.** It is a human-factors duty with no SCADA or information system content. The FPSC's 2025 inspection reviewed it with no findings.

**NIST CSF 2.0 with SP 800-82 Rev. 3 as the cyber benchmark.** With no binding cyber rule, the company chose CSF 2.0 because it is sector-neutral and is the framework that SP 800-61 Rev. 3 and the P08 runbook use. SP 800-82 Rev. 3 supplies the OT guidance for each outcome. Two cautions:
- SP 800-82 Rev. 3 Section 6 is organized by CSF 1.1 categories. This analysis cites SP 800-82 Rev. 3 **section numbers** only and uses CSF 2.0 IDs for the outcomes.
- The 37 CSF 2.0 subcategories (G-035 to G-071) were selected for relevance to a SCADA-operated pipeline. This is not a full CSF profile.

**Not applicable, with reasons:**
- **NERC CIP (C-ENERGY-R01).** The company is not a NERC-registered entity and owns no Bulk Electric System assets.
- **DOE Form OE-417.** This covers electric emergency incidents and disturbances. The company has no electric operations.
- **CIRCIA (C-ENERGY-R05)** is proposed only and not in effect. Under the proposal as corrected (FR Doc. 2024-12084, June 3, 2024), 226.2(b)(14)(iv) would cover "a pipeline facility or system owner or operator required to report cyber incidents by the Transportation Security Administration." The company has no TSA reporting duty. It is also below the SBA size standard used by the proposed size-based criterion. Recheck when the final rule is published.

**Other binding pipeline rules that touch this work** (used in P08, not decomposed here):
- 49 CFR 192.605, the O&M manual, including abnormal operation procedures for transmission lines.
- 49 CFR 192.615, emergency plans, including emergency shutdown (192.615(a)(6)) and controller actions (192.615(a)(11)).
- 49 CFR 191.3, 191.5, and 191.15, incident definition and reporting.
- Rule 25-12.084, F.A.C., FPSC telephonic notice.

## 2. Method
1. **Requirements.**
   - 192.631 rows follow the regulation's own paragraph structure, at the most granular citation that imposes a separate duty. Brief quotes are used; this is public-domain federal text.
   - CSF 2.0 rows use the subcategory text from `00_universal/frameworks/csf2_core.csv`, with the SP 800-82 Rev. 3 section that gives OT guidance.
   - TSA SD rows follow the SD's own section numbers. TSA states the SD is not Sensitive Security Information.
2. **Crosswalk.**
   - 192.631 and TSA SD rows use an author mapping to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. No official NIST mapping exists for either.
   - CSF rows use the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal/crosswalks/csf2_to_sp800-53r5.csv`). Where an OT control from the SP 800-82 Rev. 3 OT overlay (Appendix F) was added, the `crosswalk_source` column names it as an author addition (15 rows).
3. **Evidence.** Interviews (President, VP Operations, Gas Control Manager, 3 controllers, SCADA Engineer, IT Manager, MSP lead, Field Operations Manager), document review (CRM manual, O&M manual, emergency plan, test reports, FPSC 2025 inspection letter), configuration exports, and a walkthrough of the Gas Control Center and Compressor Station 1 on 2026-08-05.
4. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork (2026-08-14). Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| **A. 49 CFR 192.631 (binding)** | | | | |
| (a) General | 1 | 1 | 0 | 0 |
| (b) Roles and responsibilities | 3 | 2 | 0 | 0 |
| (c) Provide adequate information | 4 | 1 | 0 | 0 |
| (e) Alarm management | 5 | 1 | 1 | 0 |
| (f) Change management | 2 | 1 | 0 | 0 |
| (g) Operating experience | 2 | 0 | 0 | 0 |
| (h) Training | 5 | 2 | 0 | 0 |
| (i) and (j) Compliance validation and records | 2 | 1 | 0 | 0 |
| **Subtotal 192.631 (34)** | **24** | **9** | **1** | **0** |
| **B. NIST CSF 2.0 with SP 800-82 Rev. 3 (benchmark)** | | | | |
| Govern | 0 | 3 | 2 | 0 |
| Identify | 0 | 6 | 2 | 0 |
| Protect | 0 | 11 | 2 | 0 |
| Detect | 0 | 2 | 2 | 0 |
| Respond | 0 | 2 | 2 | 0 |
| Recover | 0 | 1 | 2 | 0 |
| **Subtotal CSF (37)** | **0** | **25** | **12** | **0** |
| **C. TSA SD Pipeline-2021-02G (readiness only)** | 0 | 0 | 0 | 20 |
| **Total (91)** | **24** | **34** | **13** | **20** |

**Reading the results.** The pipeline safety program is mature: 24 of the 34 SCADA-relevant duties in 192.631 are met, and the 10 gaps are about records and change control, not missing programs. The cyber program is not: no CSF outcome is fully met. The 47 unmet or partially met rows break down by gap risk as follows:
- 192.631 gaps: 8 Moderate and 2 Low.
- CSF gaps: 6 High, 23 Moderate, and 8 Low.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| No cyber incident response plan or IT/OT isolation criteria | CSF ID.IM-04, RS.MA-01, RS.MI-01 (G-047, G-065, G-068) | High | POL-03, the P08 runbook, and a cyber annex to the 192.615 emergency plan; IR retainer with OT experience | IT Manager | 2026-11-30 |
| Vendor remote access without MFA, shared, always on | CSF PR.AA-03 (G-049) | High | Named integrator accounts with MFA, enabled per session, recorded | SCADA Engineer | 2026-11-30 |
| SCADA backups exposed and never restored | CSF PR.DS-11 (G-054) | High | Monthly offline copy; annual bare-metal restore | SCADA Engineer | 2026-12-31 |
| No OT network monitoring | CSF DE.CM-01 (G-061) | High | Passive OT monitoring sensor with MSP alerting | IT Manager | 2027-03-31 |
| Alarm set-point verification overdue | 192.631(e)(3) (G-016) | Moderate | Complete verification; track all 15-month intervals | Gas Control Manager | 2026-10-31 |
| Display changes without point-to-point verification | 192.631(c)(2) (G-009) | Moderate | Verify both 2026 changes; P2P record before release | Gas Control Manager | 2026-10-31 |
| No controller authority for suspected SCADA compromise | 192.631(b)(3), (b)(5) (G-005, G-007) | Moderate | Controller role and authority for loss of SCADA integrity; controller notice before live SCADA changes | Gas Control Manager | 2026-11-30 |
| SCADA and firewall changes bypass the control room | 192.631(f)(3); CSF PR.PS-01 (G-022, G-055) | Moderate | Route through the MOC process with Gas Control sign-off | SCADA Engineer | 2026-12-31 |
| Controller training lacks cyber-caused AOCs | 192.631(h)(1); CSF PR.AT-02 (G-026, G-053) | Moderate | 3 cyber AOC scenarios; OT course for the SCADA Engineer | Gas Control Manager | 2027-03-31 |
| No supplier security terms | CSF GV.SC-05 (G-038) | Moderate | Security addendum for the integrator, MSP, telecom carrier, and model vendor | President | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The 192.631 gaps are also tracked in the compliance tracker kept by the Pipeline Safety and Compliance Manager, because the FPSC can cite them.

## 5. Pending regulatory changes and designation readiness
**If TSA designates the pipeline.** SD 02G would require:
- a TSA-approved Cybersecurity Implementation Plan covering Sections III.A to III.E;
- a Cybersecurity Incident Response Plan exercised at least annually (III.F);
- a Cybersecurity Assessment Plan with an architecture design review at least every two years and at least one-third of measures assessed each year (III.G).

SD 01G would add a Cybersecurity Coordinator and alternate available 24/7 (at least one a U.S. citizen eligible for a security clearance) and reporting of cybersecurity incidents to CISA as soon as practicable, but no later than 72 hours after identification.

Of the 20 SD readiness rows, 1 is ready (III.C.5, no domain trust), 6 are partially ready, and 12 are not ready. The applicability row (G-072) has no readiness rating. Every not-ready item maps to a CSF gap already on the roadmap. Closing the High and Moderate CSF gaps is also the fastest path to designation readiness. Plans and results submitted to TSA would become SSI under 49 CFR Part 1520 (SD Section I and IV.B), so POL-04 includes an SSI handling rule to activate on designation.

**Proposed or draft changes (none treated as current obligations):**
- **TSA "Enhancing Surface Cyber Risk Management" NPRM** (November 7, 2024) would make pipeline cyber requirements permanent regulations. It was not final as of 2026-09-25. Its applicability to non-designated pipelines was not analyzed here.
- **CIRCIA final rule** (C-ENERGY-R05): not published as of 2026-09-25. See section 1.2.
- **NIST SP 800-82 Rev. 4, initial public draft** (published 2026-09-21; comments due 2026-11-30) restructures the OT guide around CSF 2.0. It is a draft, and this analysis still uses Rev. 3. When Rev. 4 is final, the SP 800-82 section references in G-035 to G-071 should be updated.

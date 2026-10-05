# Regulatory Gap Analysis: Cris Santos Company | Water and Wastewater Systems | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (privately held community water system, 2,850 population served) |
| Tier / Vertical | Micro / Water and Wastewater Systems |
| Primary regulation named for this vertical | SDWA section 1433, 42 U.S.C. 300i-2 (C-WATER-R01): **not applicable** at this population; kept as a readiness reference |
| Binding rules analyzed | SDWA public notification rule, 40 CFR Part 141 Subpart Q, with the related reporting and record rules (141.31, 141.33); and the Ground Water Rule duties that depend on SCADA (141.401, 141.403). Text read from eCFR during fieldwork |
| Cyber benchmark analyzed | NIST CSF 2.0 outcomes, with NIST SP 800-82 Rev. 3 (Guide to OT Security, September 2023) as the OT implementation guide |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessor | Office Manager (security and compliance coordinator) and Chief Operator, with the MSP lead technician |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Applicability

### 1.1 SDWA section 1433: does not apply
Section 1433 requires a risk and resilience assessment and an emergency response plan from "each community water system serving a population of greater than 3,300 persons" (42 U.S.C. 300i-2(a)(1); the ERP duty in (b) uses the same threshold). The statute has no business-size test; population served is the only threshold.

**Finding.** The company is a community water system (40 CFR 141.2: at least 15 service connections used by year-round residents; it has 1,190). It serves **2,850 persons**, the figure it reports to the primacy agency. That is not greater than 3,300, so **section 1433 does not apply** and the company has no RRA or ERP certification to file with EPA. For systems of this size the statute gives EPA, not the system, a duty: to provide guidance and technical assistance on resilience assessments and emergency plans (300i-2(e)).

**Why the rows are kept anyway.** A 240-lot subdivision approved in 2026 could take the population served above 3,300 by about 2029. The statute's certification dates are fixed calendar dates (300i-2(a)(3)), and this analysis did **not verify** how EPA expects a system that newly crosses 3,300 to certify. The Owner will ask EPA before the subdivision connects. Until then, the 8 section 1433 rows (G-001 to G-008) record readiness only and are marked Not applicable.

### 1.2 What does apply
**The public notification rule applies to every community water system** (40 CFR 141.201(a)). The rule that matters for a cyber event is the Tier 1 notice: a "waterborne emergency (such as a failure or significant interruption in key water treatment processes ...)" requires notice to persons served and consultation with the primacy agency, each no later than 24 hours after the system learns of the situation (141.202(a) Table 1 item (7); 141.202(b)). A cyber-caused chlorine overfeed or loss of disinfection could be that situation. The related duties are the content rules (141.205), the 10-day certification (141.31(d)(1)), the 48-hour report of any violation (141.31(b)), and record keeping (141.33(e)). 9 rows (G-009 to G-017).

**The Ground Water Rule duties that depend on SCADA apply.** The company provides 4-log virus treatment by chlorination and, as a system serving 3,300 or fewer, chose continuous residual monitoring instead of a daily grab sample (141.403(b)(3)(i)(B)). That choice brings in the continuous-monitoring rules: record the lowest residual each day, grab-sample every 4 hours if the equipment fails, and resume continuous monitoring within 14 days (141.403(b)(3)(i)(A)). The record lives in the HMI historian, so its integrity is a security question. The analysis also covers cooperation with sanitary surveys (141.401(a)), whose evaluation includes "pumps, pump facilities, and controls" and "monitoring, reporting, and data verification" (141.401(c)), the significant deficiency clocks (141.403(a)(4)-(5)), and record retention (141.33(a), (c)). 8 rows (G-018 to G-025).

**NIST CSF 2.0 with SP 800-82 Rev. 3 as the cyber benchmark.** No binding federal rule requires cybersecurity controls from this water system. The company chose CSF 2.0 because EPA's free Water Cybersecurity Assessment Tool and CISA's resources use it, and it is the framework the P08 runbook follows. SP 800-82 Rev. 3 supplies OT guidance. The 23 subcategories (G-026 to G-048) were picked for relevance to a one-plant SCADA system. This is not a full CSF profile, and the rows are voluntary outcomes, not legal requirements.

**Not applicable or not analyzed row by row, with reasons:**
- **CIRCIA (C-WATER-R02):** proposed only; no final rule in the Federal Register as of approval. As proposed, the water-sector criterion covers community water systems serving more than 3,300 people, and the size criterion covers entities above the SBA size standard. The company is neither. Recheck when a final rule is published.
- **EPA's 2023 sanitary survey cybersecurity memorandum:** the vertical profile records that it was withdrawn in October 2023. This was not re-verified here, and the analysis does not rely on it. The sanitary survey rows use the regulation text only.
- **Fla. Stat. 501.171:** applies to customer personal information in the billing system. It drives the customer data rows in the P08 notification matrix and is not re-analyzed here.
- Wastewater (POTW) rules: the company runs no wastewater system.

## 2. Method
1. **Requirements.**
   - Section 1433 rows follow the statute's paragraph structure (42 U.S.C. 300i-2), read from the official U.S. Code text. Brief quotes only.
   - Part 141 rows follow each section's own paragraph structure, at the most granular citation that imposes a separate duty. Text read from eCFR (public domain).
   - CSF rows use the subcategory text from `00_universal-framework/frameworks/csf2_core.csv`, with the SP 800-82 Rev. 3 section that gives OT guidance (reused from the Small water sample, where they were checked).
2. **Crosswalk.**
   - Statute and Part 141 rows were mapped to CSF 2.0 and SP 800-53 Rev. 5 by the author (no official mapping exists). Labeled "Author mapping".
   - CSF rows use the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). Where an OT control was added (IA-2(1), MA-4), the `crosswalk_source` column names it as an author addition.
3. **Documentary evidence.** Each status rests on a named document or record: the 2023 emergency plan, the October 2024 boil water notice and certification, monthly operating reports for January to June 2026, the 2025 sanitary survey report, the compliance file, the 2018 integrator as-builts, the three vendor contracts, the HMI user list and trend, the remote desktop tool console, the MSP's firewall export and backup report, and the site visit on 2026-08-11. Interviews covered all 7 staff, the MSP lead technician, and the SCADA integrator.
4. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork (2026-07-24). Actions completed since then (policies, the runbook, the role designation, all approved 2026-08-31) are noted in the remediation column but do not change the status. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| A. SDWA section 1433 (readiness reference) | 8 | 0 | 0 | 0 | 8 |
| B. Public notification and reporting (binding) | 9 | 4 | 5 | 0 | 0 |
| C. Ground Water Rule and records (binding) | 8 | 6 | 2 | 0 | 0 |
| D. NIST CSF 2.0 with SP 800-82 Rev. 3 (benchmark) | 23 | 1 | 7 | 15 | 0 |
| **Total** | **48** | **11** | **14** | **15** | **8** |

Of the 29 unmet or partially met rows, 8 are rated High, 15 Moderate, and 6 Low. All 8 High gaps are benchmark rows.

**What the numbers say.** The binding drinking water duties are in good shape: none of the 17 binding rows is Not met. The company has issued a Tier 1 notice before (October 2024), certified it on time, and kept its records. The gaps there are about a cyber event specifically: there is no rule that a cyber-caused chlorine change is a possible Tier 1 situation (G-009), no after-hours primacy agency contact (G-011), a 2-year-old printed contact list (G-013), and no written fallback if the residual record cannot be trusted (G-020).

The cyber benchmark is where the company is weak: **15 of 23 outcomes are not met**, including every remote access, credential, backup, configuration, segmentation, and incident plan outcome for the SCADA system. That matches the 4 High risks in P01.

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| No company copy of the PLC program or HMI project | CSF PR.DS-11 (G-039) | High | Offline encrypted copies, monthly and after changes | Chief Operator | 2026-09-15 |
| No MFA on remote access to the HMI | CSF PR.AA-03 (G-035) | High | MFA on the remote desktop tool, monitoring service, firewall login | Chief Operator | 2026-09-30 |
| Uncontrolled remote and vendor access | CSF PR.AA-05 (G-036) | High | Attended, approved, reviewed sessions | Chief Operator | 2026-09-30 |
| No vulnerability identification | CSF ID.RA-01 (G-031) | High | CISA free scanning; monthly advisory review | Chief Operator | 2026-09-30 |
| PLC in remote-program; exposed modem | CSF PR.PS-01 (G-040) | High | Key switch to RUN; PLC password; private carrier plan | Chief Operator | 2026-10-31 |
| No cyber incident plan | CSF RS.MA-01 (G-045) | High | P08 runbook in the plant binder as the emergency plan's cyber annex | Owner and General Manager | 2026-10-31 |
| Flat network | CSF PR.IR-01 (G-043) | High | Separate OT network; guest Wi-Fi | Office Manager | 2026-11-30 |
| Shared and default credentials | CSF PR.AA-01 (G-034) | High | Named accounts; change commissioning passwords; password manager | Chief Operator | 2026-12-31 |
| No cyber trigger for a Tier 1 notice | 40 CFR 141.202(a) (G-009) | Moderate | Trigger and decision owner in the emergency plan | Chief Operator | 2026-10-31 |
| No written grab-sampling fallback for a compromised record | 40 CFR 141.403(b)(3)(i)(A) (G-020) | Moderate | Written fallback in the emergency plan and P08 | Chief Operator | 2026-10-31 |
| Contact list only in the billing system | 40 CFR 141.202(c) (G-013) | Moderate | Monthly printed export in the plant binder | Office Manager | 2026-10-31 |

## 5. Remediation plan
The plan fits a 7-person water system: most actions are settings, one-page procedures, or contractor work under the Chief Operator's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Stop the easy attacks | 2026-09-30 | Offline PLC and HMI backups; remote access with named accounts, MFA, and approval; MFA on the monitoring service and firewall login; CISA scanning; alert subscriptions; after-hours agency contact; cyber contacts in the binder; office backup restore test | G-011, G-024, G-031, G-032, G-035, G-036, G-039, G-046 |
| 2. Write it down | 2026-10-31 | Cyber annex (P08) in the emergency plan with the Tier 1 trigger and grab-sampling fallback; treatment interruption notice template; monthly contact list; 48-hour report rule; hand-operation steps; OT inventory; PLC key switch and password; private carrier plan; log reviews start | G-009, G-013, G-014, G-016, G-020, G-029, G-033, G-040, G-042, G-045 |
| 3. Separate and exercise | 2026-11-30 | Separate OT network with diagram; access alerts; recovery procedure with the integrator; cyber tabletop and hand-operation drill | G-030, G-043, G-044, G-047, G-048 |
| 4. Contracts, people, patching | 2026-12-31 | Contract addenda for the integrator, MSP, and monitoring vendor; training and phishing simulations; named HMI accounts and changed commissioning passwords; HMI patch plan | G-027, G-034, G-038, G-041 |
| Done at approval | 2026-08-31 | Policies (P06); role designation | G-026, G-028 |

**Progress check.** The Office Manager reports progress to the Owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory and guidance changes
- **CIRCIA** (proposed 6 CFR Part 226; NPRM 89 FR 23644, April 4, 2024) is **still proposed**. CISA held further town halls in 2026 on scope and burden. As proposed, the company would not be a covered entity. If the final rule changes the criteria, or if the population served passes 3,300 and the final rule keeps the water-sector criterion, reporting covered cyber incidents within 72 hours and ransom payments within 24 hours could apply. Rows G-045 and G-046 are flagged. Nothing here is treated as a current obligation.
- **Section 1433 coverage** could begin if the population served exceeds 3,300 (growth watch item). Rows G-001 to G-008 are flagged.
- **NIST SP 800-82 Rev. 4** was released as an initial public draft in 2026. This analysis uses Rev. 3, the current final version. Re-check the section references when Rev. 4 is final.

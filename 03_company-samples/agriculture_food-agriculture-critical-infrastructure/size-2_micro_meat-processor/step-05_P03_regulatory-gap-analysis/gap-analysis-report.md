# Regulatory Gap Analysis: Cris Santos Company | Food and Agriculture | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) |
| Tier / Vertical | Micro / Food and Agriculture (NAICS 311612) |
| Primary regulation | FSIS Sanitation SOPs, HACCP, and recall rules: 9 CFR 416.1-416.16 (selected paragraphs), 417.2-417.7, 418.2-418.4. Text read from eCFR (point-in-time 2026-09-23) |
| Applicability decisions | The vertical registry rules C-FOOD-AG-R01 (21 CFR Part 121), C-FOOD-AG-R02 (CIRCIA, proposed), and C-FOOD-AG-R03 (USCG MTS cyber rule), plus the Reportable Food Registry |
| IT and OT benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (voluntary) |
| Assessment dates | 2026-07-20 to 2026-07-31 (plant walkthrough 2026-07-22) |
| Assessors | Office Manager (security and compliance lead) and Production Supervisor (HACCP-trained under 9 CFR 417.7), with the MSP lead technician |
| Approved | 2026-08-31 by the owner |

## 1. Applicability

Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the results and the reasoning for the rules analyzed here.

### 1.1 Why not the FSMA Intentional Adulteration rule
The vertical registry names 21 CFR Part 121 as the primary regulation for food facilities. **It does not apply to this plant.** Part 121 applies to a food facility that "is required to register under section 415 of the Federal Food, Drug, and Cosmetic Act, unless one of the exemptions in § 121.5 applies" (21 CFR 121.1). The registration rule exempts "Facilities that are regulated exclusively, throughout the entire facility, by the U.S. Department of Agriculture under the Federal Meat Inspection Act" (21 CFR 1.226(g)). The plant makes only FSIS-inspected meat products and holds no FDA registration (EV-026), so it does not register and is outside Part 121. It would also qualify as a very small business under 121.5(a), which exempts all but documentation duties.

Two consequences follow:
- **Food defense is voluntary here.** No food defense requirement appears in 9 CFR Parts 416-418, which were read in full. FSIS food defense guidance for meat establishments is voluntary (as recorded in the Small sample's P03; the FSIS page was not re-read for this analysis). The company still treats deliberate tampering through equipment as a risk (P01 R-019), but it is not scored as a legal gap.
- **The Reportable Food Registry does not apply.** Its 24-hour report falls on the "responsible party," defined as the person who submits the FDA registration (21 U.S.C. 350f(a)(1)). The FSIS 24-hour notice in 9 CFR 418.2 is the equivalent duty for meat.

**If the plant ever adds an FDA-regulated product** (the Small sample's seafood room is the example), it would have to register, and Part 121 and the Reportable Food Registry would need a fresh analysis.

### 1.2 What does bind the plant: FSIS rules
As an official establishment under a federal grant of inspection, the plant must meet the FSIS Sanitation SOP rules (9 CFR 416.11-416.17), the HACCP rules (Part 417), and the recall rules (Part 418). None is an IT rule, but each now runs through systems at this plant:
- **CCP monitoring is automated.** The cooking CCP is monitored by the smokehouse controller's core-probe log and the chilling CCP by a wireless probe in the cold-chain service (417.2(c)(4)).
- **Records are electronic.** "The use of records maintained on computers is acceptable, provided that appropriate controls are implemented to ensure the integrity of the electronic data and signatures" (417.5(d)). Part 416 has a parallel sentence for SSOP records (416.16(b)).
- **Entries must be attributable.** Each HACCP entry must "be signed or initialed by the establishment employee making the entry" (417.5(b)), and SSOP records must be authenticated with the responsible employee's initials and date (416.16(a)). Shared logins defeat both.
- **Changes in "processing methods or systems" trigger reassessment** (417.4(a)(3)(i)). A new packaging machine, a new cook cycle, or a remote service module is such a change.
- **Unforeseen deviations require holding and reviewing product** (417.3(b)), and adulterated or misbranded product in commerce requires FSIS notice within 24 hours (418.2). A wrong cook cycle or a wrong label caused by a cyber event is exactly that kind of deviation.

**Rows selected.** Every paragraph of 416.11-416.16, 417.2-417.5, 417.7, and 418.2-418.4 that places a duty on the establishment is a row. From the general sanitation performance standards (416.1-416.6) only the paragraphs that bear on product protection and chemicals are rows (416.1, 416.4(c), 416.4(d)). FSIS verification sections (416.17, 417.8) and the inadequate-system criteria (417.6) are enforcement context, not rows.

**FSIS inspection context (verified items only).** FSIS inspection program personnel are assigned to the plant. FSIS verifies HACCP plans by reviewing the plan, CCP records, corrective actions, and critical limits, and by direct observation and record review (417.8), and verifies SSOPs the same way (416.17). A HACCP system may be found inadequate if records are not maintained as required (417.6(d)). This analysis does not describe inspection frequency, which was not verified.

### 1.3 Other vertical requirements
- **CIRCIA (C-FOOD-AG-R02):** proposed rule only; not in effect as of 2026-09-25. As proposed, coverage for this sector turns on exceeding the SBA size standard (226.2(a)). The company has 7 employees against a 1,000-employee standard (EV-001).
- **USCG MTS cyber rule (C-FOOD-AG-R03):** does not apply. The plant is not an MTSA-regulated facility (EV-037).
- **OSHA PSM and EPA RMP:** the plant uses no anhydrous ammonia (EV-021), so the 10,000 lb threshold quantity (29 CFR 1910.119 Appendix A; 40 CFR 68.130) is not reached.

### 1.4 IT and OT benchmark
No binding rule sets technical security controls for this plant. Ten benchmark rows use CSF 2.0 outcomes, tailored with SP 800-82 Rev. 3 (inventory, network separation, vendor remote access, authentication, backups, software maintenance, monitoring, incident response, supplier terms, training). They are **voluntary** and are scored so the roadmap can show which FSIS gaps depend on them.

## 2. Method
1. **Requirements.** FSIS rows follow the regulation's own structure at paragraph level, as described in section 1.2. Four applicability rows record the decisions in sections 1.1 and 1.3.
2. **Crosswalk.** NIST has published no mapping for 9 CFR Parts 416-418, so those rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. Benchmark rows use the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), showing a subset.
3. **Documentary evidence.** Each status rests on a named document or record from intake (2026-07-06 to 2026-07-17): the FSIS establishment file (EV-026); the three HACCP plans, hazard analyses, flow charts, reassessment and validation files (EV-027, EV-028); the SSOP document (EV-029); the recall procedure (EV-030); the training certificates and calibration log (EV-031, EV-032); the records app user list and settings (EV-005); the smokehouse controller settings and cook-log export folder (EV-008, EV-009); the cold-chain alert settings and gateway offline history (EV-006, EV-007); the firewall configuration (EV-017); the MSP device list, patch report, and backup report (EV-013, EV-015, EV-018); vendor contracts (EV-011, EV-012, EV-020); and the document request (EV-033). Fieldwork added interviews with the owner, the Production Supervisor, the Maintenance and Sanitation Technician, the Office Manager, two production workers, and the MSP lead technician (2026-07-20 to 2026-07-23, EV-047), the plant walkthrough on 2026-07-22 (EV-048), and a sample of 20 production days of SSOP records and 15 lots of HACCP and pre-shipment records from June and July 2026 (EV-049). The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**. Actions completed since then (for example, the controller password changed 2026-08-11) are noted in the remediation column but do not change the status. Gaps were rated on the P01 risk scale.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| Applicability (C-FOOD-AG-R01 to R03; Reportable Food Registry) | 4 | 0 | 0 | 0 | 4 |
| FSIS Sanitation (9 CFR Part 416) | 17 | 10 | 6 | 1 | 0 |
| FSIS HACCP (9 CFR Part 417) | 29 | 15 | 13 | 1 | 0 |
| FSIS Recalls (9 CFR Part 418) | 3 | 1 | 2 | 0 | 0 |
| **FSIS subtotal** | **49** | **26** | **21** | **2** | **0** |
| NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary) | 10 | 0 | 3 | 7 | 0 |
| **Total** | **63** | **26** | **24** | **9** | **4** |

The 33 unmet or partially met rows break down by gap risk as 10 High, 18 Moderate, and 5 Low. For the FSIS rules alone, the 23 open rows are 6 High, 12 Moderate, and 5 Low.

**What the numbers say.** The food safety program itself is sound. The hazard analyses, plans, critical limits, corrective actions, validation, and verification are all Met. The gaps sit where the program now depends on systems:
- **Records integrity is the only FSIS "Not met" theme.** 416.16(b) and 417.5(d) fail for the same reasons: shared logins, a shared vendor default administrator, and editable cook-log exports. 416.13(c), 416.16(a), 417.5(b), and 417.5(c) are partial for the same root cause.
- **The plans assume the systems always work.** Nothing says how to monitor a CCP when the controller log, the probe, or the internet is down (417.2(c)(4)), or what to do when a cycle or label may have been changed without approval (417.3(b), 418.2).
- **System changes are not food safety changes yet.** A new packager, a new cook cycle, and a remote service module were not treated as reassessment triggers (417.4(a)(3)), and two documents were modified without being re-signed (416.12(b), 417.2(d)).
- **The benchmark shows why.** Seven of ten benchmark rows are Not met: no inventory, no network separation, uncontrolled vendor access at fieldwork, no monitoring, no incident plan, no supplier terms, no training.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Electronic CCP records lack integrity controls | 9 CFR 417.5(d); 416.16(b) | High | Named accounts and administrators; read-only cook-log exports; records integrity procedure | Office Manager | 2026-12-31 |
| No fallback monitoring when systems are down | 417.2(c)(4) | High | Manual fallback in each plan and in the downtime binder | Production Supervisor | 2026-10-31 |
| No procedure for cyber-caused deviations | 417.3(b); 418.2 | High | Product hold, review, and 24-hour FSIS decision in the P08 runbook | Production Supervisor | 2026-10-31 |
| Cook cycles not protected or compared with approved versions | 417.2(c)(3) | High | Approved cycle list; monthly comparison; named access | Production Supervisor | 2026-12-31 |
| Single alert path for cold storage | 416.4(d) | High | Escalation; gateway offline alert; cellular backup; manual log | Production Supervisor | 2026-10-31 |
| Entries not attributable; reviewer not independent | 416.16(a); 417.5(b), (c) | Moderate | Named records app accounts; owner reviews lots the Production Supervisor recorded | Production Supervisor | 2026-10-31 |
| System changes not treated as HACCP changes | 417.4(a)(3)(i)-(ii); 417.2(d); 416.12(b); 416.14 | Moderate | Change log with a reassessment decision and signature step; reassess the June 2026 packaging change | Production Supervisor | 2026-10-31 |
| Recall procedure out of date for current lot records | 418.3 | Moderate | Update procedure; monthly lot and customer export; mock trace | Production Supervisor | 2026-10-31 |
| Flat network; uncontrolled vendor access (benchmark) | CSF PR.IR-01; PR.AA-05 | High | Plant network; named vendor accounts with MFA; on-request sessions | Office Manager; Maintenance and Sanitation Technician | 2026-11-30 |
| No incident plan; untested backups (benchmark) | CSF RS.MA-01; PR.DS-11 | High | P08 runbook and tabletop; restore tests and offline machine settings | Office Manager | 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person plant: most actions are one-page procedures, account settings, and MSP work, not new systems. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed (citation) |
|---|---|---|---|
| 1. Sign and decide | 2026-09-30 | Owner signs and dates the current SSOP and HACCP plans; flow charts updated; wireless probe calibration check started; first restore test includes cook-log retrieval | 416.12(b); 417.2(d); 417.2(a)(2); 417.4(a)(2)(i); 417.5(e)(2) |
| 2. People and procedures | 2026-10-31 | Named records app accounts and labeling PC login; owner as second reviewer; change log with reassessment decision; reassess the packaging change; manual monitoring fallback and downtime binder; P08 product hold and 418.2 steps; recall procedure update and mock trace; cold-chain escalation and cellular backup; packager cleaning steps in the SSOP; vendor accounts with MFA | 416.4(d); 416.13(c); 416.14; 416.16(a), (c); 417.2(c)(4); 417.3(b); 417.4(a)(3)(i)-(ii); 417.5(b), (c); 418.2; 418.3; CSF PR.AA-05, PR.AA-03, ID.AM-01 |
| 3. Network and resilience | 2026-11-30 | Plant network; immutable backups and offline machine settings; tabletop exercise; training | CSF PR.IR-01, PR.DS-11, RS.MA-01, PR.AT-01 |
| 4. Records integrity | 2026-12-31 | Named administrators; read-only cook-log exports with retention rule; records integrity procedure; approved cycle comparison; EDR and log review; MSP contract terms | 416.16(b); 417.2(c)(3), (c)(6); 417.5(d), (e)(1); CSF DE.CM-01, GV.SC-05 |
| 5. Replace and repeat | 2027-06-30 to 2027-07-31 | Stuffer HMI replaced; annual risk and gap review (July) | CSF PR.PS-02 |

**Progress check.** The Office Manager reports progress to the owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker. The Production Supervisor reports the FSIS items at the same meeting.

## 6. Pending regulatory changes
- **FSIS Parts 416-418:** a Federal Register API search for rules and proposed rules citing 9 CFR Parts 416, 417, and 418 (rechecked 2026-10-04) found nothing newer than the December 2020 egg products rule. The sections read on eCFR (point-in-time 2026-09-23) show their last amendments as 2020 (417.7), 2018 (417.2), and 2012 (417.4 and Part 418).
- **CIRCIA:** the final rule was not published as of 2026-09-25. If the final rule keeps the proposed size-based criterion, the company stays out of scope. If it adds a Food and Agriculture sector criterion that reaches small plants, the P08 notification matrix must add a 72-hour report to CISA.
- **Part 121:** not applicable unless the plant registers with FDA (section 1.1).

None of these is treated as a current obligation. The `pending_rule_change` column in `gap-analysis.csv` flags the CIRCIA row.

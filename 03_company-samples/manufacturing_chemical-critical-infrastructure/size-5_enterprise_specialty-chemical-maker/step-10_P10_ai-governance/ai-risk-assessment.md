# AI Governance Risk Assessment: Enterprise AI Portfolio and the Process-Optimization Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded specialty chemical formulator and packager; 14 plants in eight states) |
| Tier / Vertical | Enterprise / Chemical |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the process-optimization model, in section 6, including the proposed closed-loop pilot at PLT-01 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook; NIST AI 600-1 (Generative AI Profile) for AI-004, AI-005, and AI-010; OT context from NIST SP 800-82 Rev. 3 and the CISA-led joint guidance "Principles for the Secure Integration of Artificial Intelligence in Operational Technology" (Dec. 3, 2025, voluntary); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Data and Analytics Officer), portfolio review of 2026-08-26; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-08 (section 8) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 5, Medium 6, Low 1 |
| Status | In production 10, Pilot 1, Suspended 1 |
| Committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-006, AI-009, AI-011, AI-012 (all due 2026-11-30, POAM-019) |
| Use cases that can affect physical safety (rubric "Safety/CI") | 5: AI-001, AI-002, AI-003, AI-005, AI-012 |
| Use cases with any write path to a control system | 0 since 2026-08-27 (AI-012 had one; disabled) |

**Main findings:**
1. **An unreviewed closed-loop model was running at an acquired plant.** AI-012, built by PLT-13's former integrator, adjusted ingredient addition timing through a PLC with no documented validation, on a flat IT/OT network. It was switched to advisory mode on 2026-08-27, the day after the committee learned of it.
2. **A closed-loop pilot of AI-001 at PLT-01 was proposed and is not approved.** It would create a write path from the cloud into the GC-PCBMS, which breaks the one-way design rule (P04) and is rated High in P01 (R-026, treatment Avoid).
3. **AI-001 is least accurate on the product families it has seen least**, and at two plants it reached the margin to a DCS clamp. Recommendations are switched off for those families until retrained (section 6).
4. **Two vendor AI features were switched on through product releases** (AI-006, AI-009) without intake, and the HR resume ranking feature (AI-011) was suspended pending review.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly. Any AI use case that can affect physical safety also counts toward ER-01 (process safety).

**Members:** Chief Data and Analytics Officer (chair); Senior Vice President, Manufacturing; Vice President, Process Safety and EHS; Director of OT Security; CISO; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (workforce and HR tools); Vice President, Quality; and the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee. **Any AI that can change a setpoint, recipe, or safety function also needs MOC and a PHA of the change** (POL-05 4.7) | Local validation by plant and product family; representativeness and bias testing; safe-limit envelope coded and tested; OT security review of data paths; human review design; monitoring plan; for people-related uses, notice and adverse impact analysis |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; security and data review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products and models found at acquired plants, must be registered before use (POL-05 4.6; STD-05.3). Since 2026-09, procurement and IT change management block AI features without an inventory ID, and the integration checklist for acquisitions includes an AI and analytics inventory of the acquired plant. The GRC team owns the inventory.

**Policies:** POL-05 4.6 (approved AI tools only; no Restricted data in tools not approved for it) and 4.7 (no AI may write to a control or safety system without committee approval and MOC); POL-04 4.1 (formulations, recipes, and SSI are Restricted); POL-01 4.13 (MOC for control system changes); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| EPA RMP (40 CFR Part 68) and OSHA PSM (29 CFR 1910.119) | **Yes, indirectly** for AI-001, AI-002, and AI-005 at plants with covered processes | AI-001 recommendations must stay inside the safe upper and lower limits in the process safety information (68.65; 1910.119(d)), operating procedures must cover the consequences of deviation (68.69(a)(2); 1910.119(f)), and a change to the model's scope or limits is a change to the process that goes through MOC (68.75; 1910.119(l)). AI-002 does not change the mechanical integrity inspection schedule (68.73; 1910.119(j)) |
| OSHA Hazard Communication (29 CFR 1910.1200(g)) | Yes, for AI-005 | The company remains responsible for SDS content, whatever tool drafts it |
| USCG MTSA cybersecurity rule (C-CHEMICAL-R02) | Yes, for any AI component that is or touches a critical OT system at PLT-01 | A closed-loop AI-001 at PLT-01 would add a critical OT data path that must be in the Cybersecurity Plan and Assessment (101.650(b)(3)-(4), (e)(1)); AI-003 cameras at the dock fall under the Facility Security Plan |
| CFATS RBPS 8 (C-CHEMICAL-R01) | Voluntary benchmark | Its aim of preventing unauthorized access to process controls applies to every AI data path out of or into OT |
| Federal equal employment opportunity laws | Yes, for AI-011 | Counsel reviews adverse impact before any re-enable |
| State AI and employee monitoring laws | Check per state, for AI-003 and AI-011 | Laws differ by state and change often. The company does not operate in Colorado, so Colorado SB26-189 does not apply to its plants; counsel reviews the laws of each state where applicants or monitored workers are located before AI-011 is re-enabled or AI-003 expands |
| FTC Act Section 5 | Yes, for AI-010 | Accuracy of statements the chatbot makes to customers |
| SEC Reg S-K Item 106 | Indirectly | AI risks to OT are part of the cybersecurity risk management process described in the 10-K |
| Sector-specific federal AI rules | None identified | The vertical registry lists no chemical-sector AI rule. Federal AI executive actions (EO 14179, EO 14365) direct federal agencies, not private plant operators |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Process-optimization model (advisory setpoints) | High | In production (advisory) at 6 plants; closed-loop pilot not approved | Reviewed 2025-11-18; full re-review 2026-08-26 |
| AI-002 | Predictive maintenance for rotating equipment | Medium | In production at 9 plants | Reviewed 2026-03-17 |
| AI-003 | Computer vision for PPE and exclusion zones at racks and the dock | High | Pilot at PLT-01 and PLT-05 | Reviewed 2026-06-23 (pilot only) |
| AI-004 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-20 |
| AI-005 | SDS authoring assistant | High | In production (drafting only) | Reviewed 2026-05-12 |
| AI-006 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) |
| AI-007 | SL-1 anomaly detection and runout prediction | Medium | In production | Reviewed 2026-04-14 |
| AI-008 | QC spectral pass or fail model for raw materials | Medium | In production at 4 plants | Reviewed 2026-02-10 |
| AI-009 | ERP demand forecasting feature | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-010 | SL-1 portal customer chatbot | Medium | In production | Reviewed 2026-07-21 |
| AI-011 | Applicant resume screening and ranking | High | Suspended | Not reviewed (due 2026-11-30) |
| AI-012 | PLT-13 batch end-point prediction (inherited) | High | In production (advisory only, pending review) | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-002 is Medium, not High, because it adds alerts on top of the required mechanical integrity inspections and cannot remove one. AI-005 is High because a wrong hazard statement in an SDS reaches downstream users even though a qualified author signs it. AI-006 is Low only as long as it cannot close OT alerts on its own; that limit is a condition of its review.

## 5. MEASURE and MANAGE across the portfolio
**Bias and representativeness testing.** Most of the portfolio makes no decisions about people, so "fairness" here mostly means **representativeness**: does the model work as well for every plant, product family, season, sensor type, or customer segment as it does on average? Two use cases also involve people directly:
| Use case | Groups compared | Threshold for action |
|---|---|---|
| AI-001 | Plant; product family; season; raw material supplier | Mean absolute error more than 5 points above the overall rate for any group |
| AI-003 | Lighting and weather; PPE color; worker height; shift | Detection rate more than 5 points below the overall rate for any group |
| AI-005 | SDS section; product family | Any hazard classification error; minor error rate above 2% |
| AI-007 | Water utilities vs industrial customers; sensor type | Missed runouts at water utilities above zero in a month |
| AI-011 (before any re-enable) | Sex, race and ethnicity where available, age band | Selection-rate ratio below 0.8 for any group, then counsel review |

**Monitoring.** Each High-tier use case has quarterly performance and representativeness metrics (inventory column `monitoring`) reported to the committee; drift or threshold breaches trigger re-review.

**Incident handling.** AI incidents (unsafe recommendation, wrong SDS content, data misuse) are logged as SOC or process safety events. If an AI output contributed to a process upset, the RMP or PSM incident investigation applies (P08 section 9).

**Third parties.** AI vendors (AI-002, AI-003, AI-005, and the vendor features AI-006, AI-009, AI-011) are tier-1 in the vendor program; contracts require notice of material model changes and no training on company data.

## 6. Full assessment: AI-001 process-optimization model
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Recommend jacket temperature, agitation speed, and the timing of non-hazardous additions for blend hall batches, to shorten cycles (target 6%) and cut steam use |
| Users | Blend operators and shift supervisors (view recommendations); process engineers (review performance) at 6 plants |
| Affected people | Operators and maintenance staff; nearby communities if a recommendation contributed to an unsafe condition; customers (including toll customers) if quality drifted |
| Data | Training: 3 years of historian data, batch records, and QC results by plant and product family. Inputs: live data from the historian replicas on Cloud provider A (one-way path, P04). Outputs: recommended setpoints with a predicted batch time on a read-only dashboard. **No personal data.** Data are Restricted (formulations and toll customer recipes; toll customer data used only for that customer's own batches) |
| Build or buy | Build: company data science team on the AI/ML platform; model code and training data belong to the company |
| How output reaches the process | **No write path to any DCS.** An operator reads a recommendation and, if accepted, enters the setpoint by hand. The DCS enforces hard clamps, and the SIS at PSM and RMP Program 3 processes trips independently |
| Not intended (excluded) | Ammonia, chlorine, or hydrogen peroxide additions; any SIS setting; closed-loop control; evaluating operator performance |

### 6.2 The proposed closed-loop pilot at PLT-01
Manufacturing proposed letting AI-001 write setpoints for two Blend Hall 2 tanks at PLT-01 through the OT DMZ. The committee reviewed it on 2026-08-26 and recommends **not approving** it, for these reasons:
- It creates a write path from a cloud service into the GC-PCBMS, which breaks the one-way design rule and the P02 boundary (AC-4, SC-7).
- PLT-01 is an MTSA facility; the new path would be a critical OT connection that the Cybersecurity Plan and Assessment do not yet cover.
- The model's safe-limit envelope has existed only since 2026-08 and has not been through a PHA.
- The P07 findings on change control (POAM-001) and OT detections (POAM-022) are still open, so an unauthorized change through the new path might not be noticed.

A future proposal would need an on-premises inference design inside the OT zones with no cloud write path, MOC and a PHA of the change, SIS independence confirmed, a hardware or DCS-enforced rate and range limit, and the open POA&M items closed. The earliest re-proposal date is 2027-Q3.

### 6.3 Risk tier
High (section 4). Escalation triggers: any write path, including one-click accept; extending to hazardous additions or SIS settings; extending to a plant with a PSM process unit beyond the blend halls; retraining on new formulations or toll customer recipes; use of recommendations in operator evaluations.

### 6.4 MEASURE (2026-03-01 to 2026-08-14; 6 plants; 9,840 batches with recommendations)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Predicted vs actual batch time: mean absolute error under 10% on a 60-day hold-out per plant | 6.8% overall; 13.9% for the high-viscosity polymer family at PLT-03 and PLT-06 | **Partial.** Fails for one family |
| Safe | 100% of recommendations inside documented safe limits and at least 5% inside DCS clamps; zero recommendations for excluded variables | 0 outside safe limits; 0 for excluded variables; 11 of about 41,000 recommendations within 5% of a clamp (all in the flagged family); safe-limit envelope coded only since 2026-08-04 | **Partial.** Envelope new; near-clamp cases in the flagged family |
| Secure and resilient | One-way data path; least-privilege service accounts; model registry under change control; no network path to a DCS | One-way path confirmed (P07 AC-4 test); model registry promotions need committee approval (P04) | Yes |
| Accountable and transparent | Every recommendation logged with inputs, model version, operator decision, and value entered | Logged since 2026-03; model version tracking complete | Yes |
| Explainable and interpretable | Dashboard shows the top 3 factors and expected effect | Available at all 6 plants; operators rated it useful in 34 of 40 interviews | Yes |
| Privacy-enhanced | No personal data; operator IDs not model inputs | Confirmed | Yes |
| Fair, with harmful bias managed | (a) Representativeness by plant, family, season, supplier; (b) override rates reviewed only in aggregate, never to rate individual operators | (a) High-viscosity family flagged at 2 plants; season and supplier within 3 points. (b) Override rates highest where the flagged family runs, which reflects correct operator judgment | **Partial.** One family flagged |

**Representativeness finding.** As in the Small sample, the model is least accurate on the product family it saw least, and that is also where it came closest to a clamp. Recommendations for the high-viscosity family were switched off at PLT-03 and PLT-06 on 2026-08-27 until the model is retrained and passes a new hold-out test.

### 6.5 MANAGE
- **Human in the loop:** advisory only; the operator decides and enters any change by hand; the shift supervisor approves any recommendation outside the normal operating range; operators may ignore any recommendation without giving a reason. The DCS, SIS, and field readings always take priority.
- **Change control:** every model version, limit change, or new product family goes through the model registry with committee approval and, at plants with covered processes, through MOC.
- **Monitoring:** weekly drift and accuracy by plant and family; monthly near-clamp count; quarterly report to the committee and the Vice President, Process Safety and EHS.
- **Incidents:** if a recommendation contributes to a deviation, the plant logs a process safety near miss, the model is suspended at that plant, and the incident is investigated (P08 section 9).
- **Integrity after an OT incident:** if a plant's historian is compromised, AI-001 stays suspended there until the committee confirms the training and input data are intact (P08 section 8).
- **Decommissioning:** stop at a plant if accuracy fails the threshold two months in a row, if any recommendation falls outside safe limits, or if the one-way path cannot be assured.

## 7. Portfolio actions
| Action | Owner | Due | Link |
|---|---|---|---|
| Complete committee review of AI-006, AI-009, AI-011, and AI-012 | Chief Data and Analytics Officer | 2026-11-30 | POAM-019; P01 R-028 |
| AI-012: keep advisory mode; validate the model or retire it; include it in the PLT-13 OT integration | Vice President, Integration Management Office | 2026-11-30 | POAM-015 |
| AI-001: retrain for the high-viscosity family and repeat the hold-out test before switching it back on | Senior Vice President, Manufacturing | 2027-01-31 | P01 R-025 |
| AI-003: representativeness test at night and in rain before any expansion beyond the pilot | Vice President, Corporate Security | 2027-01-31 | None |
| AI-011: adverse impact analysis and counsel review before any re-enable | Chief Human Resources Officer | 2026-11-30 | POAM-019 |
| Add AI and analytics inventory to the acquisition due diligence checklist | Vice President, Integration Management Office | 2026-10-31 | P01 R-059 |

## 8. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the committee's recommendation of 2026-08-26:
1. **AI-001:** approved to continue in advisory mode at the 6 plants, with the high-viscosity family switched off at PLT-03 and PLT-06 until retrained.
2. **AI-001 closed-loop pilot at PLT-01:** **not approved** (P01 R-026, treatment Avoid). Re-proposal no earlier than 2027-Q3 and only on the conditions in section 6.2.
3. **AI-012:** stays in advisory mode with the PLC write path disabled until reviewed; retire if it cannot be validated by 2026-11-30.
4. **AI-006 and AI-009:** may continue in current scope until review by 2026-11-30; AI-006 must not auto-close OT alerts.
5. **AI-011:** ranking stays disabled until committee review and an adverse impact analysis are complete.
6. **AI-002, AI-003 (pilot), AI-004, AI-005, AI-007, AI-008, AI-010:** approved to continue in current scope.

# AI Risk Assessment: Process-Optimization Model (AI-001)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical formulator and packager) |
| Tier / Vertical | Small / Chemical |
| AI use case | AI-001: machine learning model that recommends setpoints (jacket temperature, agitation speed, and addition timing) for Blend Hall A batches to shorten cycle time and cut energy use. Pilot on 2 of the 8 blend tanks since May 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook. AI 600-1 (Generative AI Profile) applies to AI-002 only. OT context from NIST SP 800-82 Rev. 3 and the joint CISA-led guidance "Principles for the Secure Integration of Artificial Intelligence in Operational Technology" (Dec. 3, 2025) |
| Assessor / date | Process Engineer (business owner) with the IT Manager, Controls Engineer, and EHS Manager, 2026-08-26 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** Process Engineer. **Safety authority:** Plant Manager (RMP qualified person). **Decision authority:** the CEO, because AI-001 is High tier (POL-01 4.4 reserves High risks for the CEO).
- **How the pilot started:** the data science contractor and the Process Engineer built AI-001 without a risk assessment, security review, or approved-tools list (gap 14; P01 R-018). This assessment closes that gap.
- **Policies that apply:**
  - POL-05 4.8: approved AI tools only; AI-001 recommendations are advisory
  - POL-04 4.8: Restricted data (recipes, process data) only in approved tools
  - POL-01 4.11: any change in AI-001's scope, limits, or tanks goes through MOC
  - POL-01 4.8: security clauses for the data science contractor (POAM-022)
- **Scaled for a 162-person plant:** there is no AI committee. The Process Engineer, Plant Manager, IT Manager, and Controls Engineer review AI use cases at the monthly OT security meeting. The IT Manager keeps the AI inventory and the approved-tools list.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Recommend setpoints for jacket temperature, agitator speed, and the timing of non-hazardous additions for water treatment formulations in tanks A-3 and A-4. Goal: 8% shorter batch cycle and lower steam use |
| Users / operators | Blend operators and Shift Supervisors (view recommendations); Process Engineer (reviews performance) |
| Affected people | Operators and maintenance staff in Blend Hall A; the surrounding community if a recommendation contributed to an unsafe condition; customers if product quality drifted |
| Data (inputs, training, outputs) | Training: 3 years of historian data for 2 tanks (temperatures, pressures, flows, agitation, batch times), batch records, and QC results. Inputs: live data from the historian replica (SYS-10). Outputs: recommended setpoints with a predicted batch time, shown on a read-only dashboard in the control room. **No personal information.** Data are Restricted (POL-04) because they reveal formulations |
| Build or buy (vendor / model) | Build: gradient-boosted regression model developed by the data science contractor on the cloud tenant's managed ML platform (SYS-16). Model code and training data belong to the company |
| How output reaches the process | **No write path to the DCS.** An operator reads a recommendation and, if they accept it, enters the setpoint by hand. The DCS enforces hard high and low clamps, and the SIS independently trips on high level, high pressure, and high temperature |
| Not intended | Ammonia or hydrogen peroxide addition rates or quantities; any SIS setting; closed-loop control; evaluating operator performance. These uses are **excluded**, and enabling any of them requires re-assessment and MOC |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| EPA RMP, 40 CFR Part 68 (Program 2) | **Yes, indirectly** | Tanks A-3 and A-4 are fed from the ammonia process. Recommendations must stay inside the safe upper and lower limits in the safety information (68.48(a)(3)), and operating procedures must cover the consequences of deviation (68.52(b)(7)). A change to AI-001's scope or limits is handled through MOC. A change that alters safe operating limits is a major change needing hazard review before startup (68.50(d)) |
| CFATS RBPS 8 (C-CHEMICAL-R01) | Voluntary benchmark | AI-001 creates a new data path out of OT (historian to cloud). RBPS 8's aim of preventing unauthorized access to process controls applies to that path (P04 finding 2) |
| Sector-specific federal AI rules | None identified | The vertical registry lists no chemical-sector AI rule. The CISA-led joint guidance on AI in OT (Dec. 3, 2025) is voluntary and used here as good practice |
| State AI laws (for example Colorado SB26-189) | No | These laws target consequential decisions about people (employment, credit, housing, and similar). AI-001 makes no decisions about people, and the company operates only in Florida |
| FTC Act Section 5 | No (today) | The company makes no public claims about AI-001. Recheck if AI-assisted production is ever marketed |
| Federal AI executive actions (EO 14179, EO 14365) | No direct obligations | They direct federal agencies, not private plant operators |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the rubric puts any AI that "can affect physical safety or critical infrastructure operations" in the High tier. AI-001 influences setpoints on tanks connected to an RMP-covered ammonia process at a chemical-sector facility. A human makes the final change, but a wrong recommendation that an operator trusts could move the process toward an unsafe condition (P01 R-018).

**What keeps the residual risk acceptable:**
- advisory only, with no write path
- manual entry by an operator
- DCS clamps and an independent SIS
- ammonia and peroxide additions excluded

**Escalation triggers (re-assess before any of these):**
- any write path, including "one-click accept" to the DCS
- extending to ammonia or peroxide additions or to more tanks
- retraining on new formulations
- use of recommendations in operator evaluations
- moving model hosting outside the company tenant

## 4. MEASURE
Pilot period: May 11 to August 21, 2026, 214 batches on tanks A-3 and A-4.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Predicted vs actual batch time: mean absolute error under 10% on a hold-out set of the last 60 days; recommendation acceptance by operators tracked | Error 7.2% overall, but 14.8% on the 31 batches of the high-viscosity polymer family (under-represented in training) | **Partial.** Fails for one product family |
| Safe | 100% of recommendations inside the documented safe operating limits and at least 5% inside the DCS clamps; zero recommendations for excluded variables | 3 of 1,106 recommendations (0.3%) were within 5% of the jacket temperature clamp; 0 outside the limits; 0 for excluded variables. **No safe-limit envelope was coded in the model** until 2026-08-20 | **No.** Envelope added only after the finding |
| Secure and resilient | Historian replica integrity; least-privilege service account; model and data in the company tenant; contractor access with MFA | Replica writable by the analytics service account (P04 finding 2); contractor uses a named cloud account with MFA; no integrity check of training data | **No** (R-019) |
| Accountable and transparent | Every recommendation logged with inputs, model version, operator decision, and the value entered | Logged in the tenant; model versions not recorded before 2026-07 | Partial |
| Explainable and interpretable | Dashboard shows the top 3 factors behind each recommendation and the expected effect | Available since June 2026; operators rate it useful in 9 of 12 interviews | Yes |
| Privacy-enhanced | No personal data in inputs or outputs; operator IDs not used as features | Confirmed. Shift and crew are not model inputs | Yes |
| Fair, with harmful bias managed | (a) **Representativeness:** error by product family, season, and raw material lot; flag any group with error more than 5 points above the overall rate. (b) **Workforce fairness:** acceptance and override rates by shift are reviewed only in aggregate and must not be used to rate individual operators | (a) High-viscosity family flagged (14.8% vs 7.2%); summer and winter within 2 points. (b) Night shift overrides more often (31% vs 18%), because the night shift runs more of the flagged family, not because of operator performance | **Partial.** One group flagged |

**Bias and representativeness finding.** The model is least accurate on the product family it saw least, and it reached the safety margin there. The night shift's higher override rate was the operators correctly distrusting weak recommendations. It must never be read as a performance problem. Until the model is retrained with enough data, recommendations are **switched off** for the high-viscosity family.

## 5. MANAGE
**Human-in-the-loop design:**
- Recommendations are advisory and appear only on the read-only dashboard.
- The operator decides and enters any change by hand. The Shift Supervisor must approve any recommended jacket temperature above the normal operating range in the operating procedure.
- Operators may ignore any recommendation without giving a reason. The operating procedure states that the DCS, SIS, and field readings always take priority.
- A safe-limit envelope, taken from the RMP safety information and set 5% inside the DCS clamps, filters every output. It is under MOC and signed off by the Plant Manager.

**Monitoring:**
- Monthly performance review by the Process Engineer: error by product family, near-envelope count, and override rate by shift (aggregate only).
- **Drift triggers:** error above 10% for two weeks, or any recommendation filtered by the envelope more than 5 times in a week. Either one pauses recommendations until reviewed.
- Quarterly security check of the replica, the service account, and contractor access.

**Incident handling:**
- A recommendation that contributes to a process deviation is investigated as a process incident. If the deviation could have led to a catastrophic release, an RMP incident investigation applies (68.60).
- Suspected tampering with the replica or model follows the P08 runbook. AI-001 stays off until the Process Engineer confirms data integrity (P08 section 7).

**Decommissioning:**
- Stop and remove the dashboard if safety envelope breaches recur after retraining.
- Stop and remove it if the data science contractor's security addendum is not signed by 2026-12-31.
- Stop and remove it if one-way replication is not in place by 2027-03-31.
- Model artifacts and logs are kept for 5 years (POL-04 4.9).

## 6. Decision
**Approve with conditions.** Approved by the CEO on 2026-09-04, on the recommendation of the Process Engineer and the Plant Manager. The pilot may continue on tanks A-3 and A-4 **only if** these conditions are met:
1. The safe-limit envelope is under MOC, with Plant Manager sign-off (done 2026-08-20; MOC record by 2026-09-30).
2. Recommendations stay off for the high-viscosity family until retraining shows error under 10% on that family.
3. The replica service account is read-only and integrity checks run on training data, by 2026-10-31 (R-019). One-way replication follows with the OT DMZ (POAM-002).
4. The data science contractor signs the security addendum by 2026-12-31 (POAM-022).
5. The operating procedure for Blend Hall A states that AI-001 is advisory and lists the Shift Supervisor approval rule, by 2026-10-31. Operators are briefed.

**Expansion** beyond 2 tanks requires two consecutive months of passing the valid, safe, and fairness tests and a new assessment.

**AI-002 (enterprise generative AI assistant)** is under evaluation. It needs its own assessment with AI 600-1 before approval, and it may not receive Restricted-Security data. **AI-003 (public chatbots)** stays prohibited for company data classes other than Public (POL-05 4.8).

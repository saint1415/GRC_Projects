# AI Risk Assessment: Predictive Maintenance Model for Well Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer) |
| Tier / Vertical | Small / Mining, Quarrying, and Oil and Gas Extraction |
| AI use case | AI-001: predictive maintenance model for rod pumps and electric submersible pumps (ESPs), in pilot on 60 wells since May 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. The Generative AI Profile (AI 600-1) is not used for AI-001, which is not generative; it informs the rules for AI-002 |
| Assessor / date | Production Engineering Manager with the IT Manager and the SCADA and Automation Supervisor, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Production Engineering Manager. **Decision authority:** CFO (Medium tier), with the VP Operations' agreement because the model shapes field work. The majority owner decides if the use case is re-tiered High.
- **How the pilot started:** the Production Engineering Manager hired a data science firm and started the pilot in May 2026 without a security review or an AI risk review (gap 14 in `../00_company-facts.md`). This assessment is that review, done late.
- **Policies that apply:**
  - POL-01 4.9: supplier security schedule before a supplier receives company data
  - POL-04 4.7: no Restricted or Confidential data in AI tools without approval
  - POL-05 4.8: approved AI tools only
- **Approved-tools list:** kept by the IT Manager. It will list AI-001 (for the production engineering group) and, once chosen, one enterprise generative AI tool (AI-002).
- **Scale for a 250-person company:** there is no AI committee. The Production Engineering Manager, IT Manager, SCADA and Automation Supervisor, and CFO review AI use cases twice a year and whenever a use case changes.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Predict rod pump and ESP failures up to 30 days ahead so the engineer can schedule the 2 workover rigs and 1 pulling unit to the wells most likely to fail, before production is lost |
| Users / operators | 3 production engineers; the Panhandle rig supervisor sees the resulting work orders |
| Affected parties | Field operations (rig schedules), lease operators (visit routes), royalty owners and partners indirectly (production). No decisions are made about individuals |
| Data | Inputs: hourly historian data from the cloud replica (pump cards, motor current, runtime, pressures, rates) and 3 years of ERP work order history, with technician names removed. **No personal information.** Vehicle telematics were considered and deliberately excluded |
| Build or buy | Built by a contracted data science firm on the company's cloud machine learning workspace. The company owns the model and code |
| Connection to OT | **Read-only and indirect.** The model reads the historian replica in the cloud tenant. It has no network path to the SCADA network and cannot write setpoints, start or stop wells, or create work orders on its own |
| Not intended | Controlling equipment; deciding shut-ins; deferring inspections of safety equipment (pressure relief valves, H2S monitors, emergency shutdowns); evaluating lease operators or crews. Each of these requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules (oil and gas) | No | None identified for this vertical (`02_industry-rules/mining-oil-gas/overlay.md`) |
| State AI laws (for example Colorado SB26-189) | No | The company operates only in Florida, and the use case makes no consequential decision about a person. No Florida AI statute applicable to this use was identified in the repository's cross-sector research |
| Fla. Stat. 501.171 | Not today | The model uses no personal information. It would apply if telematics or employee data were added |
| FTC Act Section 5 | Indirectly | Applies to claims the company makes about the model, for example to lenders or partners. Describe its accuracy honestly |
| Contract with the data science firm | Yes | Must cover data use (no reuse of company data), ownership of the model, security terms, and deletion at contract end. **Not yet in the contract** (P03 GV.SC-06) |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High:** the rubric puts AI that "can affect physical safety or critical infrastructure operations" at High. AI-001 does not control or command any equipment, has no path to SCADA, and only reorders a maintenance queue that an engineer approves. If the model misses a failure, the result is the same as today without the model: the pump fails, the well stops, and the hardwired safety shutdowns and existing alarms still work. It makes no decision about any person.

**Why not Low:** it influences how field crews spend their time and which wells get attention, and its data comes from the OT environment. A systematic blind spot could leave a group of wells under-maintained (see the bias finding below).

**Escalation triggers (re-tier to High and re-assess):**
- any automatic action on equipment or SCADA (setpoints, start/stop, shut-in)
- use to defer or skip inspection of safety-critical equipment
- use of model outputs to rank, evaluate, or discipline lease operators or crews (an employment decision)
- adding personal information such as vehicle telematics

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (pilot, June-August 2026) | Pass? |
|---|---|---|---|
| Valid and reliable | Recall (failures flagged at least 3 days ahead) of at least 60%; precision (alerts that were real failures) of at least 35% | 14 failures on pilot wells; 9 flagged ahead (recall 64%). 23 alerts; 9 were real (precision 39%) | Yes, overall |
| Safe | No write path to SCADA; alerts never used to defer safety equipment inspections | Confirmed by network rule review: the ML workspace has no route to the SCADA network; inspection schedules unchanged | Yes |
| Secure and resilient | Data science firm access limited to the workspace; model files and training data in company storage; contract security terms | Access limited (P04); **no security terms or data deletion clause in the contract** | **No** |
| Accountable and transparent | Named owner; model card with purpose, data, limits, and version; engineers told what the model does not see | Owner named; model card not yet written | Partial |
| Explainable and interpretable | Each alert shows the top contributing signals (for example pump card shape change, rising motor current) | Available in the workspace report | Yes |
| Privacy-enhanced | No personal information in training or scoring data | Technician names removed from work orders; telematics excluded | Yes |
| Fair, with harmful bias managed | Compare recall and false alert rate across well groups (see plan below). Flag if a group's recall is more than 15 points below the overall rate or its false alert rate is more than 10 points above | South Florida ESP wells: recall 33% (2 of 6) vs 64% overall | **No.** Group flagged |

**Bias and representativeness testing plan.** In this use case, "harmful bias" means the model systematically serves some wells worse than others. Because rig time is limited, under-served wells fail more often and wait longer for repair.
- **Groups compared:** operating area (Panhandle vs South Florida); lift type (rod pump vs ESP); well age (drilled before vs after 1990); communications and data rate (radio sites polled every minute vs cellular sites polled every 15 minutes); sour vs sweet service.
- **Metrics:** recall, precision, and false alert rate per group, computed quarterly on a rolling 12 months of labeled failures.
- **Thresholds:** flag a group if its recall is more than 15 percentage points below overall, or its false alert rate is more than 10 points above overall. Groups with fewer than 5 failures in the window are reported but not flagged, and are watched for the next quarter.
- **Pilot finding:** South Florida ESP wells are under-represented in training (the 3-year history is 80% Panhandle rod pumps) and their cellular sites send data only every 15 minutes, so the model sees less detail. Recall for that group is 33% against 64% overall.
- **Workforce check:** the model must not be used to judge lease operators. The quarterly review confirms that no report ranks routes or people by model alerts.

## 5. MANAGE
**Human-in-the-loop design:**
- The model produces a ranked alert list only.
- A production engineer reviews each alert and the contributing signals, and decides whether to create a work order.
- Engineers can dismiss alerts with a reason; dismissals are reviewed monthly.
- The rig schedule is still set by the rig supervisor and the engineer. The model never schedules work or touches SCADA.

**Monitoring:**
- Monthly performance review against the thresholds above, tracked in the risk register (P01 R-028).
- Quarterly bias report by the groups listed above.
- Data drift check when the historian replica changes (for example the OT DMZ cutover, POAM-002) or when new wells are added.

**Security:**
- The model reads only the historian replica in the cloud tenant. Any proposal to connect it directly to the SCADA network is out of scope and would require a new assessment under POL-02 4.10.
- The data science firm's access ends with its contract, and the contract must require deletion of company data.

**Incident handling:** a security incident affecting the ML workspace or the historian replica follows P08. A model failure that contributes to a significant production loss is reviewed by the Production Engineering Manager and recorded in the risk register.

**Decommissioning:**
- Stop and archive if recall falls below 50% for two consecutive months.
- Stop if the data science firm's contract is not amended by 2026-11-30.
- Stop if the model is ever found to be used against an escalation trigger.

## 6. Decision
**Approve with conditions.** CFO, with the VP Operations' agreement, 2026-08-31. The pilot may continue on the 40 Panhandle wells **only if** these conditions are met by 2026-11-30:
1. The data science firm's contract is amended with security terms, no reuse of company data, company ownership of the model, and deletion at contract end (POL-01 4.9).
2. A model card is written and shared with the engineers.
3. The monthly performance and quarterly bias reviews are in the engineering calendar.
4. South Florida ESP wells stay in shadow mode (alerts recorded but not used) until retraining with South Florida data brings their recall within the bias threshold.

Expansion to all 74 producing wells requires two consecutive quarters with no bias flag.

**Related action for AI-002.** Publish the approved-tools list and choose an enterprise generative AI tool with data protections, so staff stop using public chatbots. Until then, public tools may be used only for Public and Internal information (POL-05 4.8). Due 2026-11-30 (P01 R-029).

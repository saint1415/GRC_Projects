# AI Risk Assessment: Pipeline Leak-Detection Anomaly Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (intrastate natural gas transmission pipeline operator) |
| Tier / Vertical | Small / Energy |
| AI use case | AI-001: pipeline leak-detection anomaly model, advisory alerts to gas controllers since 2026-07-01 (shadow mode from April 2026) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook. AI 600-1 (Generative AI Profile) does not apply because the model is not generative |
| Assessor / date | Gas Control Manager with the IT Manager and SCADA Engineer, 2026-09-14 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** Gas Control Manager.
- **Decision authority:**
  - The majority owner approves, because the use case is rated High (see section 3), following the P01 risk acceptance rules.
  - The President approves day-to-day conditions.
- **Policies that apply:**
  - POL-01 4.7: changes that could affect control room operations go through management of change
  - POL-01 4.8: supplier security requirements
  - POL-04 4.1: SCADA data is Confidential, and SCADA configurations are Restricted
  - POL-05 4.8: approved AI tools only; the leak model is advisory
- **Approved-tools list:** kept by the IT Manager. It lists AI-001 (controllers only) and AI-003. AI-002 is restricted until an enterprise tool is approved.
- **Scale for a Small operator:** there is no AI committee. The Gas Control Manager, IT Manager, SCADA Engineer, and Pipeline Safety and Compliance Manager review AI use cases each quarter.
- **Reference for critical infrastructure:** NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07. The company will review the profile when it is published. It is not used as a requirement here.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Detect possible leaks or ruptures sooner than fixed SCADA alarms by comparing pressure, flow, and temperature patterns across segments against learned normal behavior. The goal is earlier field dispatch |
| Users / operators | 6 gas controllers and the Gas Control Manager. Alerts appear on a separate business-network screen in the control room, not on the HMIs |
| Affected people | People who live, work, and travel along the 185-mile route, and customers who depend on uninterrupted supply. The model makes no decision about any individual |
| Data | Inputs: 1-minute historian data pushed one way from the DMZ replica to the cloud landing zone (P04). Outputs: an anomaly score per segment and an alert when the score passes a threshold. No personal information |
| Build or buy | Configure: the vendor's model, tuned by the vendor on 18 months of company data. The vendor deploys updates into the company's cloud workload, **currently without company approval** (P04 finding 2) |
| Not intended | Closing valves, changing setpoints, or suppressing SCADA alarms. Replacing patrols (192.705), leakage surveys (192.706), or the SCADA alarm system. Any write-back to SCADA would need a new assessment and architecture review |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| 49 CFR 192.615(a)(12), rupture identification procedures | **Yes, if used** | The procedures must "specify the sources of information, operational factors, and other criteria" that personnel use to evaluate a notification of potential rupture. If controllers use model alerts that way, the model must be named in the procedures, with how to weigh it. Today it is not |
| 49 CFR 192.631, control room management | **Yes** | The model is information given to controllers ((c)). Its alert volume counts toward controller workload, which must be monitored yearly ((e)(5)). Model changes can affect control room operations ((f)). Controllers need training on its use and limits ((h)) |
| 49 CFR 192.705 and 192.706 | Yes (unchanged) | Patrols and leakage surveys remain required. The model does not replace them |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. The company keeps the claims it relied on in the procurement file |
| State AI laws (for example Colorado SB26-189, Texas TRAIGA) | No | The model makes no consequential decision about individuals, and the company operates only in Florida |
| TSA SD Pipeline-2021-02G | No | Not designated. If designated, the analytics workload would likely be a Critical Cyber System, because its compromise could mislead controllers (readiness note, P03 G-073) |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`). The rubric rates as High any AI that "can affect physical safety or critical infrastructure operations."

The model does not act on the pipeline, but it shapes what controllers look at and when they dispatch crews. Two failure modes carry safety risk:
- **Missed leak (false negative):** controllers may be falsely reassured and slower to act.
- **Alert fatigue (false positives):** controllers may learn to ignore it, or be distracted from SCADA alarms.

**What keeps it from being worse:** it is advisory, it has no path into SCADA, and the SCADA alarm system and field methods remain primary.

**Escalation triggers (re-assess before any of these):**
- any automatic action or write-back to SCADA;
- using model alerts to close valves without a field or SCADA confirmation;
- removing or raising any SCADA alarm on the basis of model coverage;
- a new model architecture or a new data source.

## 4. MEASURE
The vendor backtested the model on 18 months of history (including 6 known events: 2 third-party damage leaks and 4 planned blowdowns) and on simulated leaks injected into historical data at 1% and 5% of segment flow. The company then compared model alerts with shift logs for July and August 2026.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Detect simulated leaks of 1% of segment flow within 30 minutes in at least 90% of cases; detect all 6 known historical events | 1% leaks: 83%. 5% leaks: 100%. Known events: 6 of 6 (4 blowdowns correctly flagged as planned when the maintenance flag was set) | **No.** Below target at 1% |
| Safe | Model cannot act on SCADA; alerts do not replace alarms; false alerts no more than 1 per 12-hour shift | One-way data path confirmed (P04). False alerts: 2.6 per shift on average (July to August) | **Partial.** Alert rate too high; fatigue risk |
| Secure and resilient | Input data path one-way; vendor changes approved; workload access limited | One-way path and limited roles confirmed. Vendor deployed 2 model updates in August without notice | **No.** Change control missing (R-026) |
| Accountable and transparent | Named owner; written controller guidance; model named in 192.615(a)(12) procedures | Owner named 2026-09-14. No guidance or procedure text yet | **No** |
| Explainable and interpretable | Dashboard shows which sensors drove each alert, so the controller can check SCADA | Available on every alert | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | Confirmed | Yes |
| Fair, with harmful bias managed | Detection and false-alert rates compared across segment groups (below) | Cellular-only segments under-detected | **No.** Disparity flagged |

**Bias and fairness testing plan.** For a model that makes no decision about individuals, the fairness question is whether the protection it adds is spread evenly along the route, or whether some communities get less early warning than others.

| Groups compared | Metric | Threshold | Result |
|---|---|---|---|
| Segments in Class 3 locations (more populated) vs Class 1 and 2 | Detection rate for 1% simulated leaks | No group more than 10 percentage points below the overall rate | Class 3: 86%; Class 1 and 2: 81%. Pass |
| Segments served by cellular-only telemetry (9 sites) vs radio | Detection rate | Same | Cellular-only: 68% vs 83% overall. **Fail** |
| Low-flow periods (nights, mild weather) vs high-flow periods | Detection rate and false-alert rate | Same; false-alert rate no more than 2 times the overall rate | Low-flow detection 79%; false alerts 1.6 times the overall rate. Pass |
| South lateral (serving two smaller towns) vs mainline | False-negative rate on historical events | Any missed known event is a fail | 0 missed. Pass |

**Bias finding.** Segments that report only over cellular (mostly on the south lateral) send data less often and drop more samples. The model therefore detects small leaks there less reliably. People along those segments get less early warning from the model than people along the mainline. The fix is better data, not a lower threshold:
- move the 4 most critical cellular sites to faster polling and second-carrier SIMs (P01 R-023);
- show controllers a coverage indicator so they know where the model is weaker;
- retest after the change.

## 5. MANAGE
**Human-in-the-loop design:**
- An alert is a prompt to look, not a finding. The controller checks the SCADA trends named on the alert. If the trends support a possible leak, the controller follows the AOC or emergency procedure and dispatches field staff.
- The controller can acknowledge and annotate every alert. The Gas Control Manager reviews annotations weekly.
- A controller may never ignore a SCADA alarm because the model shows no anomaly.
- The model cannot suppress, change, or add SCADA alarms.

**Procedures and training (192.615(a)(12) and 192.631):**
- Name the model in the rupture identification procedures as a supporting source, with the rule above.
- Add a model module to controller training: what it sees, where it is weak (cellular-only segments, low flow), and how to respond.
- Include model alert volume in the annual controller workload review (192.631(e)(5)).

**Change control:**
- Vendor model updates deploy to a staging slot. The SCADA Engineer reruns the backtest and simulated leak set.
- The Gas Control Manager approves promotion through management of change (192.631(f); POL-01 4.7).
- The contract must require 30 days' notice of model changes and immediate notice of any security incident (POAM-018).

**Monitoring (monthly, reported quarterly):**
- detection results on a fresh simulated leak set;
- false alerts per shift;
- the segment-group comparison above;
- data completeness by site.

Results are tracked in the risk register under R-025 and R-026.

**Incident handling:**
- **Model outage:** controllers continue with SCADA alarms. This is not an incident.
- **Suspected tampering** with the model, its data, or the landing zone: handle under P08 as a Severity 2 cyber incident, and take the model out of the control room until it is revalidated.

**Decommissioning:**
- Remove the alert screen if false alerts stay above 2 per shift for two months after tuning.
- Remove it if the vendor changes the model again without approval.
- Remove it if the vendor changes its data-use terms.
- On exit, the vendor must delete company historian data and confirm in writing (GV.SC-10).

## 6. Decision
**Approve with conditions.** Majority owner and President, 2026-09-24. The model may stay in the control room as an **advisory** tool **only if** these conditions are met:
1. Written controller guidance and the 192.615(a)(12) procedure text are in place by 2026-10-31.
2. Vendor deployments go through the staging slot and approval, with a contract amendment, by 2026-11-30.
3. The alert threshold is retuned to reach no more than 1 false alert per shift, without dropping 5% leak detection below 100%, by 2026-12-31.
4. The coverage indicator for cellular-only segments is on the dashboard by 2026-12-31, and the segment test is rerun after the telemetry upgrade in 2027.

Any move toward automatic action requires a new assessment, an architecture review, and management of change.

**Related actions:**
- **AI-002:** approve one enterprise generative AI tool with no training on company data. Until then, POL-05 4.8 bans Restricted information in any AI tool. Due 2026-12-31.
- **AI-003:** covered by the MSP review in P09.

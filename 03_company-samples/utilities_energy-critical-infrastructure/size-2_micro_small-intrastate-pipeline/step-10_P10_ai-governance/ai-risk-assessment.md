# AI Risk Assessment: Pipeline Leak-Detection Anomaly Module

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (small intrastate natural gas transmission pipeline operator) |
| Tier / Vertical | Micro / Energy |
| AI use case | AI-001: the hosted SCADA vendor's leak-detection anomaly module, switched on by the vendor as a free trial on 2026-06-01 and sending advisory alerts to the on-call phone |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook. AI 600-1 (Generative AI Profile) does not apply to AI-001 because the model is not generative |
| Assessor / date | Operations Manager with the Office Manager, 2026-08-28 |
| Decision | Owner, 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Operations Manager. **Decision authority:** the Owner, because the use case is rated High (section 3) and the P01 rules reserve Moderate and higher risk to the Owner.
- **Policies that apply:**
  - POL-02 A.4: no vendor service without security terms, including trials.
  - POL-02 A.6: changes that affect SCADA, including new vendor modules, need the Operations Manager's approval.
  - POL-04 4.7: Restricted information never goes into an AI tool; the leak module is the only approved AI tool, as an advisory tool under the conditions in section 6.
- **Approved-tools list:** kept by the Office Manager in POL-04 4.7.
- **Scale for a Micro operator:** there is no AI committee. The Owner, the Operations Manager, and the Office Manager review AI use at the monthly security meeting.

**How the trial started.** The SCADA vendor emailed on 2026-05-20 that the module would be switched on for "eligible customers" on 2026-06-01, at no charge for 6 months. Nobody at the company approved it. From 2026-06-01 the module sent alerts to the on-call phone by text and showed them on the SCADA screen. That broke the change rule the company has now written (POL-02 A.6), and the module is outside the vendor's SOC 2 report (P09).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Spot a possible leak or rupture sooner than fixed SCADA pressure alarms, by comparing pressure and flow patterns between the receipt station, the 3 RCV sites, and the 3 delivery stations against learned normal behavior. The goal is earlier field dispatch |
| Users | The 3 controllers: the Operations Manager at the gas control desk, and the on-call controller by phone at night |
| Affected people | People who live, work, and travel along the 26-mile route, especially the Class 3 segment near the municipal gate station, and the about 9,000 homes and businesses that depend on uninterrupted supply. The model makes no decision about any individual |
| Data | Inputs: SCADA pressure, flow, and valve data already in the vendor's historian, polled every minute at 6 sites and every 5 minutes at RCV site 2 (older RTU). Outputs: an anomaly score for each of the 4 pipeline segments and an alert when the score passes a threshold. No personal information |
| Build or buy | Buy and configure: the vendor's model, tuned by the vendor on 12 months of the company's historian data. The vendor updates the model without notice |
| Not intended | Closing valves, changing set-points, or suppressing or changing SCADA alarms. Replacing patrols (49 CFR 192.705), leakage surveys (192.706), or the SCADA alarms. Any automatic action would need a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| 49 CFR 192.615(a)(12), rupture identification procedures | **Yes** | The procedures must "specify the sources of information, operational factors, and other criteria" that personnel use to evaluate a notification of potential rupture. Controllers now receive model alerts, so the procedure must say how to treat them. Today it does not (P03 G-021) |
| 49 CFR 192.631(d), fatigue | **Yes, indirectly** | Night text alerts wake the on-call controller. False alerts add to the fatigue the company must manage under its reduced-scope control room procedures (P03 G-005, G-008) |
| 49 CFR 192.605(c) abnormal operation | Yes | A real alert is an abnormal operation notice: the controller follows the abnormal operation procedures and notifies the Operations Manager (192.605(c)(3)) |
| 49 CFR 192.705 and 192.706 | Yes (unchanged) | Patrols and leakage surveys remain required. The model does not replace them |
| 49 CFR 192.631(c), (e), (f), (h) | No | Not binding at this scope (192.631(a)(1)(ii)). The company still applies their ideas as good practice: alert volume reviewed, changes approved, controllers trained |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. The company keeps the vendor's trial notice and claims on file |
| State AI laws (for example Colorado SB26-189) | No | The model makes no consequential decision about individuals, and the company operates only in Florida |
| TSA SD Pipeline-2021-02G | No | Not designated. If designated, the module would be part of a Critical Cyber System, because its output could mislead controllers |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`). The rubric rates as High any AI that "can affect physical safety or critical infrastructure operations."

The model cannot act on the pipeline, but it shapes what the controller looks at and when they send someone to the field. Three failure modes carry safety risk:
- **Missed leak (false negative):** a quiet model may falsely reassure the controller.
- **Alert fatigue (false positives):** a controller woken often by false alerts may start to ignore them, and is more tired for real alarms.
- **Silent change:** the vendor can change the model without notice, so yesterday's test results may not describe today's model.

**What keeps it from being worse:** it is advisory, it has no path to command field devices, and the SCADA alarms and field methods remain primary.

**Re-assess before any of these:** automatic action of any kind; using an alert to close a valve without SCADA or field confirmation; changing or removing a SCADA alarm because the model "covers" it; a new data source or model type; or moving the module out of the trial into a paid service.

## 4. MEASURE
The vendor backtested the model on the company's 12 months of historian data, including 3 known events (1 third-party damage leak in 2025, below the Part 191 reporting thresholds, and 2 planned blowdowns), and on simulated leaks injected into historical data at 2% and 5% of segment flow. The company then compared every alert from 2026-06-01 to 2026-08-24 with the on-call log.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Detect simulated 2% leaks within 30 minutes in at least 85% of cases and all 5% leaks; detect all 3 known events | 2% leaks: 74%. 5% leaks: 100%. Known events: 3 of 3 (both blowdowns flagged as planned when the maintenance flag was set) | **No.** Below target at 2% |
| Safe | No path to command field devices; alerts never replace alarms; false alerts no more than 1 per week at night | Read-only confirmed with the vendor. 34 alerts in 85 days, none a real leak; 21 of them at night (about 1.7 per week) | **Partial.** Night alert rate too high |
| Secure and resilient | Vendor changes approved; module covered by assurance | Model updated twice in July without notice; module outside the SOC 2 report | **No** |
| Accountable and transparent | Named owner; written controller guidance; model named in the 192.615(a)(12) procedure | Owner named 2026-08-28; no guidance or procedure text yet | **No** |
| Explainable and interpretable | Each alert shows which sensors drove it, so the controller can check SCADA trends | Available on every alert | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | Confirmed | Yes |
| Fair, with harmful bias managed | Detection and false-alert rates compared across segment groups (below) | Under-detection on the segment with slower polling | **No.** Disparity flagged |

**Bias and fairness testing plan.** The model makes no decision about individuals, so the fairness question is whether the early warning it adds is spread evenly along the route, or whether some communities get less of it than others.

| Groups compared | Metric | Threshold | Result |
|---|---|---|---|
| Class 3 segment near the municipal gate station vs Class 1 and 2 segments | Detection rate for 2% simulated leaks | No group more than 10 percentage points below the overall rate | Class 3: 78%; Class 1 and 2: 73%. Pass |
| Segment through RCV site 2 (5-minute polling) vs segments with 1-minute polling | Detection rate for 2% simulated leaks | Same | RCV site 2 segment: 55% vs 74% overall. **Fail** |
| Low-flow periods (nights and weekends, when the plants are idle) vs normal flow | False-alert rate | No more than 2 times the overall rate | 2.4 times the overall rate. **Fail** |
| Food plant lateral (intermittent flow) vs mainline | False-alert rate | Same | 1.6 times the overall rate. Pass |

**Bias findings.**
- People along the segment through RCV site 2, which includes a rural road crossing and several homes, get less early warning from the model, because its older RTU reports every 5 minutes. The fix is better data, not a lower threshold: move the RTU to 1-minute polling (included in the field device work in P01 R-007), then retest.
- Most false alerts come at night and on weekends, when flow is low. They wake the on-call controller. Until the vendor retunes for low flow, the company will not send night text alerts (section 6).

## 5. MANAGE
**Human-in-the-loop design:**
- An alert is a prompt to look, not a finding. The controller checks the SCADA trends named on the alert. If the trends support a possible leak, the controller follows the abnormal operation or emergency procedure and sends field staff.
- The controller writes the outcome of every alert on the on-call log. The Operations Manager reviews the log weekly.
- A controller never ignores a SCADA alarm because the model shows nothing, and never closes a valve on a model alert alone.
- The model cannot suppress, change, or add SCADA alarms.

**Procedures and training:**
- Name the model in the rupture identification procedure (192.615(a)(12)) as a supporting source only, with the rules above (P03 G-021).
- Brief all 3 controllers: what the model sees, where it is weaker (RCV site 2 segment, low flow), and how to respond.
- Count any night alert response toward hours-of-service (P03 G-008).

**Data protection and vendor terms:**
- The module uses only SCADA data the vendor already holds; no new data leaves the company.
- The SCADA addendum (POAM-011) must cover the module: 30 days' notice of model changes, written confirmation that company data is not used to train models for other customers without consent, deletion of company data on exit, and a statement of the controls around the module until it enters the SOC 2 scope.

**Change control:**
- Model updates are approved by the Operations Manager (POL-02 A.6) after the vendor reruns the simulated-leak set and shares the results.

**Monitoring (monthly, reported at the security meeting):**
- alerts per week, by day and night;
- outcomes from the on-call log;
- detection results on a fresh simulated-leak set each quarter;
- the segment comparison above.

Results are tracked in the risk register under R-013 and R-014.

**Incident handling:**
- **Module outage:** controllers continue with SCADA alarms. This is not an incident.
- **Suspected tampering** with the model or its data: handle under POL-03 and the P08 runbook, and switch the module off until it is revalidated.

**Decommissioning:**
- Switch it off if night false alerts stay above 1 per week for two months after retuning, if the vendor changes the model again without notice, or if the vendor will not accept the addendum terms.
- On exit, the vendor confirms in writing that company data used by the module is deleted.

## 6. Decision
**Approve with conditions, as an advisory tool only.** Owner, 2026-09-15.

From 2026-09-15 the module stays on, **but alerts appear only on the SCADA screen at the gas control desk; night text alerts to the on-call phone are switched off.** Night alerts may return only when all of these are met:
1. The rupture identification procedure names the model as a supporting source only, and the 3 controllers are briefed (target 2026-10-31).
2. The vendor accepts the module terms in the SCADA addendum, including 30 days' notice of model changes (target 2026-12-31).
3. The vendor retunes for low flow and the night false-alert rate falls to 1 per week or less over one month.
4. RCV site 2 moves to 1-minute polling and the segment test is rerun (target 2027-03-31).

The trial ends on 2026-11-30. The company may pay for the module after the trial only if conditions 1 and 2 are met by then; otherwise it is switched off.

**Related actions:**
- **AI-002:** public generative AI chatbots stay banned for Restricted and Internal information (POL-02 C.2; POL-04 4.7).
- **AI-003:** the productivity suite's built-in AI assistant stays off until the Office Manager confirms its data terms, by 2026-12-31.

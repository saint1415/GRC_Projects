# AI Risk Assessment: Water Quality Anomaly Detection

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (investor-owned community water system) |
| Tier / Vertical | Small / Water and Wastewater Systems |
| AI use case | AI-001: water quality anomaly detection model, pilot since May 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook. AI 600-1 does not apply: the model is not generative |
| Assessor / date | Water Quality Supervisor with the IT Manager and Operations Manager, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** Water Quality Supervisor. **Decision authority:** majority owner (High tier, per POL-01 4.4), on the recommendation of the General Manager and Operations Manager.
- **Policies that apply:**
  - POL-01 4.11: nothing may weaken hardwired safeguards, SCADA alarms, or manual operation
  - POL-04 4.7 and POL-05 4.8: approved AI tools only; no Restricted data in unapproved tools
  - POL-01 4.8: security terms for vendors with access to company data
- **Approved-tools list:** kept by the IT Manager. Today it lists AI-001 (pilot, advisory only) and AI-002 (AMI alerts). General-purpose chatbots (AI-003) are not approved for Restricted or Confidential data.
- **Scale for a Small utility:** there is no AI committee. The Water Quality Supervisor, Operations Manager, and IT Manager review AI use cases quarterly and after any model change.
- **How the pilot started is itself a finding.** The model went live in May 2026 without validation, a change review, or an entry on an approved-tools list (scenario gap 15). It was caught by this assessment. From now on, any AI feature that touches process data needs this assessment before use (P09 CC3.4).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Detect unusual combinations of water quality and hydraulic readings earlier than fixed SCADA alarm limits can, for example a slow chlorine residual decline in one pressure zone, or a pH shift together with a flow change. The goal is earlier investigation, not automatic action |
| Users / operators | Water Quality Supervisor; operators in the WTP-1 control room |
| Affected people | The 46,200 people served, indirectly: a missed event could delay a response, and false alerts could lead to unnecessary flushing or notices. Operators are also affected (alert fatigue) |
| Data | Inputs: 1-minute analyzer and hydraulic values from the historian replica (no personal information). Outputs: an anomaly score per station and an alert with the contributing signals |
| Build or buy | Buy: vendor model image, baselined on 12 months of company data, running as a container in the company's cloud tenant (P04). The vendor updated the image twice during the pilot without company review (P04 finding 2) |
| Not intended | Controlling any equipment; replacing required compliance monitoring; deciding whether to issue a public notice; suppressing or delaying SCADA alarms. The design has no write path to SCADA (P04 section 2) |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| SDWA section 1433 | **Yes (indirectly)** | The RRA must assess the system's monitoring practices (42 U.S.C. 300i-2(a)(1)(A)(iii)), and the ERP must include strategies to aid detection of malevolent acts or natural hazards (300i-2(b)(4)). The model is a candidate detection strategy, so the RRA addendum and ERP must describe it accurately, including its limits (P03 G-005, G-016) |
| 40 CFR Part 141 monitoring and public notification | **Yes, unchanged** | The model does not replace any required monitoring. Public notice decisions (40 CFR 141.202) stay with the Water Quality Supervisor and General Manager, based on confirmed data |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. Keep the claims the company relied on in the procurement file |
| State AI laws (for example Colorado SB26-189, Texas TRAIGA) | No | They address consequential decisions about individuals, and the company operates only in Florida. AI-001 makes no decision about any person. State-specific AI analysis is otherwise out of scope by decision (`../scenario-facts.md`) |
| NIST AI RMF Critical Infrastructure Profile | Watch item | NIST released a concept note on 2026-04-07. Not final; re-check at the next quarterly review |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).

**Why High:** the rubric rates as High any AI that "can affect physical safety or critical infrastructure operations". AI-001 does not control anything, but operators act on its alerts, and a public drinking water system is critical infrastructure. Two failure modes reach public health: a missed event that operators have come to expect the model to catch, and a flood of false alerts that trains operators to ignore it.

**How the High-tier minimum controls apply:**
- **Human review before action:** required. No process change or notice without confirmation by a grab sample or second instrument.
- **Pre-deployment testing:** required. Section 4 sets the validation thresholds; the pilot has not met them.
- **Impact assessment:** this document.
- **Notice to affected people:** the model makes no decision about individuals, so there is no one to notify individually. Transparency is met by labeling every alert "advisory, model output" for operators, and by describing the model accurately in the ERP.
- **Ongoing monitoring:** weekly alert review and quarterly performance report.

**Escalation triggers (re-assess before any of these):**
- any write path from the model or cloud tenant to SCADA, or automatic setpoint changes
- using model output to reduce grab sampling or to support a compliance determination
- suppressing or re-prioritizing SCADA alarms based on the model
- a vendor model change that alters inputs or the alerting method

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (pilot, May-August 2026) | Pass? |
|---|---|---|---|
| Valid and reliable | Back-test on 12 months of history with 9 labeled events (2024 storm pressure losses, 3 analyzer failures, 2 chlorine residual dips, 1 main break) plus 20 injected synthetic events. Detect at least 90% of events within 30 minutes | Labeled: 7 of 9 detected (78%). Synthetic: 17 of 20 (85%). Median time to detect 22 minutes | **No.** Below the 90% threshold |
| Valid and reliable (false alerts) | No more than 5 false alerts per week across all stations | 11 per week on average | **No** |
| Safe | SCADA alarms and grab sampling stay primary; no write path to OT | Confirmed in the P04 design and the cloud network rules | Yes |
| Secure and resilient | Replica integrity check; pinned model version with change review; service identity read-only; tenant administrator MFA | Read-only identity and MFA in place; no integrity check; two unreviewed vendor updates | **Partial** |
| Accountable and transparent | Alerts labeled advisory; named owner; alert log kept | Owner named; labels added 2026-08-20; alert log in email only | Partial |
| Explainable and interpretable | Each alert lists the contributing signals and the station | Available in the alert text | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | Confirmed | Yes |
| Fair, with harmful bias managed | Compare detection rate and false-alert rate across station groups (see the bias testing plan below). Flag a gap of more than 10 percentage points in detection rate | East zone stations: 60% detection vs 88% for other stations | **No.** Disparity flagged |

**Bias and fairness testing plan.** For this model, fairness means that every neighborhood gets the same protection. The groups compared are the monitoring station groups, not individuals:
- **Groups:** (a) the 3 east zone stations served by pre-1980 cast-iron mains, versus the other 5 stations; (b) stations fed mainly by WTP-2, which is unstaffed at night, versus stations fed by WTP-1.
- **Metrics:** detection rate on labeled and injected events; false alerts per station per week; median time to detect.
- **Thresholds:** detection rate gap of 10 percentage points or less; false-alert rate within 2 times the best group.
- **Frequency:** before production, then quarterly, and after any model change.

**Bias finding.** The east zone stations have noisier analyzer signals because of older mains and more frequent flushing. The model learned a wider "normal" band there and missed more events (60% versus 88%). Older infrastructure can coincide with lower-income areas, so an unmanaged gap here would give some customers less protection than others. The vendor must re-baseline those stations, or the company must set station-specific thresholds, before production. Until then, the east zone keeps its existing fixed SCADA alarm limits and grab sampling schedule, with no reliance on the model.

## 5. MANAGE
**Human-in-the-loop design:**
- The model only sends advisory alerts. It has no write path to SCADA.
- An operator must confirm any alert with a grab sample or a second instrument before changing the process.
- Public notice decisions stay with the Water Quality Supervisor and General Manager, based on confirmed data.
- Operators may silence the model's email alerts during an incident, but never SCADA alarms.

**Change control:**
- The model version is pinned in the tenant.
- The vendor must give 10 business days' notice of any change, with release notes.
- The Water Quality Supervisor re-runs the back-test before approving an update (P04 finding 2; P09 CC8.1).

**Monitoring:**
- Weekly alert review during the pilot, tracked against P01 R-022 and R-023.
- Quarterly performance and bias report by station group.
- Daily replica reconciliation (P04 finding 3). If the replica fails reconciliation, alerts are suspended.

**Incident handling:**
- If a model alert is linked to a real event, record it and use it as a labeled event.
- A compromise of the cloud tenant or the model follows P08 and the P04 isolation design. The model is switched off first; plant operations are not affected.

**Decommissioning:**
- Stop the pilot if validation thresholds are not met by 2027-02-28.
- Stop the pilot if the vendor will not agree to change notice terms.
- Stop the pilot if false alerts stay above 10 per week for two months in a row.

## 6. Decision
**Continue the pilot as advisory only; not approved for production.** Majority owner, on the General Manager's recommendation, 2026-08-31. Conditions, due by 2026-11-30:
1. Model version pinned, with a vendor change-notice clause added to the service agreement.
2. Daily replica reconciliation running.
3. Alerts labeled "advisory, model output" and logged outside email.
4. East zone stations excluded from model reliance until the bias gap is closed.
5. Operators briefed that SCADA alarms and grab sampling remain the controls of record.

Production approval requires, at the same time:
- at least 90% detection
- no more than 5 false alerts per week
- a station-group detection gap of 10 points or less

**Related actions:**
- **AI-002 (AMI leak alerts).** Confirm the vendor contract covers customer data under Fla. Stat. 501.171. Check that customer-facing alert wording does not promise leak detection. Due 2026-12-31.
- **AI-003 (chatbots).** The approved-tools rule (POL-05 4.8) was issued 2026-09-01. Evaluate one enterprise tool with no-training terms by 2027-03-31.

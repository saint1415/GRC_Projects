# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed interstate natural gas transmission pipeline operator) |
| Tier / Vertical | Mid-Market / Energy |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. The lead use case is AI-001, the pipeline leak-detection anomaly model (registry default) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-004 only. AI-001, AI-002, AI-003, and AI-005 are not generative |
| Assessors / date | Director of Gas Control (operations and safety), vCISO and Security Manager (security), Director of Pipeline Safety and Compliance (pipeline safety rules), General Counsel (legal), 2026-08-24 to 2026-09-10 |
| Decision | Chief Operating Officer, 2026-09-17. The two High-tier decisions were noted by the Chief Executive Officer the same day, under the P01 rule that High risks are accepted only by the CEO |

## 1. Summary
Two AI tools reached the control room and the compressor stations without a security, safety, or change review (gap 14):
- **AI-001, the leak-detection model**, gives controllers advisory alerts. It works, but it is below its detection target for small leaks, it raises too many false alerts, and the vendor changes it without management of change (P01 R-025, R-027).
- **AI-002, the OEM predictive maintenance service**, collected its data through the undocumented cellular modem that P07 found at Compressor Station 4. The tool itself only recommends maintenance, but its **data path** was the most serious finding in this program (P01 R-003, Very High).

None of the tools acts on the pipeline, and none makes a decision about an individual. The risks are physical safety, OT security, and SSI leakage.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Pipeline leak-detection anomaly model | High | Approve with conditions (advisory only) |
| AI-002 | Compressor predictive maintenance (OEM) | High | Approve with conditions; data collection stays suspended until the DMZ path is live |
| AI-003 | Right-of-way imagery change detection | Medium | Continue the pilot; expand after local validation |
| AI-004 | Enterprise generative AI assistant | Medium | Approve general release with conditions by 2026-12-31 |
| AI-005 | EDR machine learning detection (MSSP) | Low | Approve; covered by the MSSP review |

Tiers: 2 High, 2 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Director of Gas Control, supported by the vCISO (STD-05 owners). Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.14: AI tools that process Restricted or SSI data, or that inform controllers, patrols, or maintenance decisions, must be approved through this process before use.
  - POL-04: SCADA data is Confidential; SCADA configurations, PLC logic, and OT network diagrams are Restricted; TSA plans are SSI.
  - POL-05 4.8: approved AI tools only; never put SSI, Restricted information, or employee personal information into a tool that is not approved for it.
  - STD-05 AI use standard: draft; due 2026-12-31 (POAM-019).
- **Approved-tools list:** kept by the Security Manager. Today it lists AI-001 (controllers only), AI-003 (GIS team), AI-004 (pilot users), and AI-005. AI-002 is listed as suspended.
- **Change control:** any change to an AI tool that could affect control room operations goes through management of change with control room participation (192.631(f); POL-01).

### 2.1 Lightweight AI governance process (Mid-Market)
The company does not need a standing AI committee. It needs a gate and a rhythm, using existing roles and meetings:

| Step | What happens | Who |
|---|---|---|
| 1. Intake | Any new AI tool, new AI feature in an existing tool, or new data source for a model is registered in the inventory before purchase or pilot | Business owner; Supply Chain Manager blocks purchase orders without an inventory ID |
| 2. Tiering | Tier with the repository rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`) | GRC lead |
| 3. Review | Medium and High: security review (data path, access, vendor), safety and operations review (Director of Gas Control for anything controllers or field crews see), legal review | AI review group: Director of Gas Control, vCISO, Security Manager, Director of Pipeline Safety and Compliance, General Counsel |
| 4. Decision | Low: Security Manager. Medium: COO. High: COO, noted by the CEO | As listed |
| 5. Monitor | Monthly metrics for High tools; quarterly review of the whole portfolio | Business owners report; the AI review group meets quarterly, right after the TSA assessment schedule review |
| 6. Change | Vendor model updates go to a staging slot, are revalidated, and are promoted through management of change | Business owner; SCADA and OT Engineering Manager |

**Re-tier triggers** for every use case: any write-back to OT; any automatic action; a new data source or a new path into or out of OT; a model architecture change; use for a decision about a person.

**Reference for critical infrastructure.** NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07. The company will review the profile when it is published; it is not used as a requirement here.

## 3. MAP
| Item | AI-001 Leak detection | AI-002 Predictive maintenance | AI-003 Imagery change detection | AI-004 Generative assistant | AI-005 EDR |
|---|---|---|---|---|---|
| Purpose | Earlier detection of leaks and ruptures than fixed SCADA alarms | Earlier detection of unit wear to avoid unplanned outages | Earlier detection of digging and encroachment between patrols | Drafting and summarizing business documents | Malware and behavior detection |
| Users | 28 controllers and 5 shift supervisors | 5 Compressor Station Supervisors; OEM engineers | GIS team; 6 Area Managers | 40 pilot users in business functions | MSSP analysts |
| Affected people | People along the 780-mile route; shippers and the homes and plants they serve | Field workers at stations; shippers (outages) | Landowners and excavators near the pipeline | Staff | Staff |
| Data | Historian data pushed one way from the DMZ replica to the OT analytics account | Unit vibration and performance data | Imagery; GIS centerline (Restricted) | Business documents the user can access | Endpoint telemetry |
| Build or buy | Configure (vendor model tuned on company data) | Buy (OEM service) | Buy (SaaS) | Buy (in the productivity suite tenant) | Buy (via the MSSP) |
| Touches OT? | Reads OT data through the DMZ; no path back | **Yes, until 2026-08-13**: modem on a unit control panel | No | No | No (business endpoints only) |

**Laws and rules that apply:**
| Rule | Applies to | Why |
|---|---|---|
| 49 CFR 192.615(a)(12), rupture identification procedures | AI-001 | The procedures "must, at a minimum, specify the sources of information, operational factors, and other criteria" personnel use to evaluate a notification of potential rupture. Controllers already look at model alerts, so the model must be named in the procedures, with how to weigh it. Today it is not (POAM-019) |
| 49 CFR 192.631 control room management (C-ENERGY-R04) | AI-001 | The model is information given to controllers ((c)). Its alert volume is part of the controller workload reviewed each year ((e)(5)). Changes to it must be coordinated with the control room ((f); P03 G-104). Controllers need training on its use and limits ((h)) |
| 49 CFR 192.705 patrols, 192.706 leakage surveys, 192.614 damage prevention | AI-001, AI-003 | Remain the required methods. Neither tool replaces them, and patrol intervals are not changed because of AI-003 |
| TSA SD Pipeline-2021-02G (C-ENERGY-R03) | AI-001, AI-002 | The OT analytics account (AI-001) was never filed as a Cybersecurity Implementation Plan amendment (Section VI; POAM-018). The OEM data path (AI-002) was an external connection to OT outside the plan (III.B.1.b, III.B.2.a; POAM-003). If AI-001 ever supports a business critical function, the OT analytics account becomes a Critical Cyber System |
| 49 CFR Part 1520 (SSI) | AI-004 | SSI may be stored and shared only as Part 1520 and STD-10 allow. The assistant is not an approved SSI location |
| FTC Act Section 5 | AI-001 to AI-004 (indirect) | Applies to vendors' accuracy claims. The company keeps the claims it relied on in each procurement file |
| State breach laws (Fla. Stat. 501.171 as the worked example) | AI-004 | Only if employee personal information were exposed through the tool |

**Laws considered and not applicable:**
- **State AI laws on consequential decisions** (for example Colorado SB26-189, effective 2027-01-01): none of the tools makes or materially influences a decision about a person in employment, credit, housing, insurance, education, health care, or government services. The company does not use AI in hiring or HR decisions; the intake gate in section 2.1 would re-tier any such use.
- **Federal AI executive orders and OMB memoranda:** they govern federal agencies and federal procurement. The company has no federal contracts.

## 4. MEASURE
### 4.1 AI-001 leak-detection model (High)
The vendor backtested the model on 24 months of historian data, including 9 known events (3 third-party damage leaks, 1 relief valve release, and 5 planned blowdowns), and on simulated leaks injected into historical data at 1% and 5% of segment flow on all 58 mainline segments. The company then compared model alerts with shift logs for June to August 2026.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Detect simulated leaks of 1% of segment flow within 30 minutes in at least 90% of cases; detect 100% of 5% leaks; detect all 4 known unplanned events | 1% leaks: 86%. 5% leaks: 100%. Known unplanned events: 4 of 4. All 5 blowdowns correctly labeled as planned when the maintenance flag was set | **No.** Below target at 1% |
| Safe | No path to SCADA; alerts never replace SCADA alarms; no more than 1 false alert per 12-hour shift | One-way data path confirmed (P04). False alerts: 1.9 per shift on average | **Partial.** Alert rate too high; fatigue risk (192.631(e)(5)) |
| Secure and resilient | Data path one-way; vendor access limited to the model namespace; vendor changes approved | Path and access confirmed. The vendor deployed 3 model updates in 2026 without notice or MOC (P01 R-027) | **No.** Change control missing |
| Accountable and transparent | Named owner; written controller guidance; model named in the 192.615(a)(12) procedures | Owner named 2026-09-10. No guidance or procedure text yet | **No** |
| Explainable and interpretable | Each alert shows which sensors and segments drove it, so the controller can check SCADA trends | Available on every alert | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | Confirmed | Yes |
| Fair, with harmful bias managed | Detection and false-alert rates compared across segment groups (below) | Cellular-only segments under-detected | **No.** Disparity flagged |

**Bias and fairness testing plan.** The model makes no decision about individuals. The fairness question is whether the protection it adds is spread evenly along the route, or whether some communities get less early warning than others.

| Groups compared | Metric | Threshold | Result |
|---|---|---|---|
| Segments in Class 3 locations (suburban areas near 4 cities) vs Class 1 and 2 | Detection rate for 1% simulated leaks | No group more than 10 percentage points below the overall rate | Class 3: 89%; Class 1 and 2: 85%. Pass |
| Segments whose nearest telemetry is cellular-only vs microwave or licensed radio | Detection rate | Same | Cellular-only: 71% vs 86% overall. **Fail** |
| Low-flow periods (nights, mild weather) vs high-flow periods | Detection rate and false-alert rate | Same; false-alert rate no more than 2 times the overall rate | Low-flow detection 82%; false alerts 1.7 times the overall rate. Pass |
| Alabama and Georgia segments vs Florida segments | Detection rate | Same | 84% vs 87%. Pass |
| Operated laterals (owned by others) | Coverage | Disclosed to the owners | **Not covered.** The model scores only the company's mainline. The OSAs do not include it, and the lateral owners must not be told or led to believe otherwise |

**Bias finding.** Segments whose telemetry reports only over cellular send data less often and drop more samples, so the model detects small leaks there less reliably. People along those segments get less early warning from the model. The fix is better data, not a lower threshold:
- second-carrier cellular service at the 15 largest delivery points (FY2027 budget; P01 R-014);
- a coverage indicator on the alert screen so controllers know where the model is weaker;
- retest after the telemetry upgrade.

### 4.2 Other use cases
| ID | Key tests | Result | Pass? |
|---|---|---|---|
| AI-002 | Data path into OT; vendor access; recommendations reviewed by a supervisor before work | The modem bypassed the DMZ (P07; Very High). Recommendations are reviewed and follow OEM procedures. The OEM's model accuracy claims (failure lead time) were not validated locally | **No** (security); validation pending |
| AI-003 | Local validation: compare 6 months of flags with patrol and one-call findings in the 3 pilot areas; target at least 90% of confirmed excavations flagged; centerline data handled under contract | 4 months of data so far: 31 of 35 confirmed excavations flagged (89%); 2 of the 4 misses were small equipment under tree cover. Vendor contract restricts centerline use to this service | **Partial.** Validation continues to 2027-03-31 (P01 R-026) |
| AI-004 | No training on company data (tenant settings and contract); data loss rules for SSI markings; user review of outputs; prompt and output logging | Tenant settings and contract confirmed. SSI marking rule not yet live (POAM-011). Pilot users reported 2 cases of fabricated regulatory citations in drafts (AI 600-1 confabulation risk) | **Partial** |
| AI-005 | MSSP detection tests; isolation limited to business endpoints | Covered by P07 SI-3 (EICAR tests passed) and the MSSP SOC 2 review (P09 VEN-01) | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** an alert is a prompt to look, not a finding. The controller checks the SCADA trends named on the alert. If they support a possible leak, the controller follows the abnormal operating or emergency procedure, including the rupture identification procedure, and dispatches field staff. A controller may never ignore or delay a response to a SCADA alarm because the model shows no anomaly. The model cannot suppress, change, or add SCADA alarms. Controllers annotate every alert; the shift supervisor reviews annotations each week.
- **AI-002:** a recommendation is reviewed by the Compressor Station Supervisor and scheduled through the work management system. Nothing is written back to unit panels.
- **AI-003:** the GIS team confirms each flag before field action. Patrols continue on schedule.
- **AI-004:** users review all output. Output used in a compliance filing, a safety document, or a personnel matter must be checked against the source by the responsible owner.

**Procedures and training (AI-001):**
- Name the model in the rupture identification procedures as a supporting source, with the rule above (192.615(a)(12)).
- Add a model module to controller training: what it sees, where it is weak (cellular-only segments, low flow, no lateral coverage), and how to respond (192.631(h)).
- Include model alert volume in the annual controller workload review (192.631(e)(5)).

**Change control:**
- AI-001 vendor updates deploy to a staging slot. The SCADA and OT Engineering Manager reruns the backtest and the simulated leak set, and the Director of Gas Control approves promotion through management of change (192.631(f)).
- The AI-001 contract must require 30 days' notice of model changes and security incident notice within 24 hours (P09 VEN-09).
- AI-002 data flows only through the DMZ historian replica to the OT analytics account; the OEM reads from there (POAM-003).

**Monitoring (monthly for AI-001 and AI-002, quarterly for the portfolio):**
- AI-001: detection results on a fresh simulated leak set, false alerts per shift, the segment-group comparison above, and data completeness by site. Tracked under P01 R-025 and R-027.
- AI-002: recommendation follow-through and unplanned unit trips.
- AI-003: flag precision and missed excavations against one-call and patrol findings (R-026).
- AI-004: data loss rule hits and user-reported errors (R-028).

**Incident handling (P08):**
- **Model outage:** controllers continue with SCADA alarms. Not an incident.
- **Suspected tampering** with a model, its data, or the OT analytics account: a cyber incident under P08 (Severity 2, or Severity 1 if any OT path is involved). Take the model out of the control room until it is revalidated. Both runbooks restore AI-001 last, after its input data is confirmed clean.
- **SSI or Restricted information entered into a tool that is not approved for it:** report at once under POL-05; handle as a possible SSI exposure under STD-10.

**Decommissioning criteria:**
- AI-001: remove the alert screen if false alerts stay above 2 per shift for two months after retuning, if the vendor changes the model again without approval, or if the vendor changes its data-use terms. On exit, the vendor deletes company historian data and confirms in writing (GV.SC-10).
- AI-002: end the service if the OEM will not accept the DMZ data path and contract security terms.
- AI-003: stop expansion if local validation stays below 90%.
- AI-004: withdraw if the vendor changes its no-training commitment.

## 6. Decisions
**AI-001: Approve with conditions.** COO, 2026-09-17; noted by the CEO. The model may stay in the control room as an **advisory** tool **only if**:
1. Written controller guidance and the 192.615(a)(12) procedure text are in place by 2026-10-31.
2. Vendor deployments go through the staging slot and MOC approval, with a contract amendment, by 2026-11-30.
3. The alert threshold is retuned to no more than 1 false alert per shift, without dropping 5% leak detection below 100%, by 2026-12-31.
4. The coverage indicator for cellular-only segments is on the alert screen by 2026-12-31, and the segment test is rerun after the telemetry upgrade.
5. The OT analytics account is included in the Cybersecurity Implementation Plan amendment request filed by 2026-10-31 (POAM-018).

Any move toward automatic action, alarm suppression, or use beyond the mainline needs a new assessment, an architecture review, management of change, and a TSA plan review.

**AI-002: Approve with conditions.** COO, 2026-09-17; noted by the CEO. Data collection stays suspended until the OEM data path runs through the DMZ and the OEM signs contract security terms (due 2026-10-31, POAM-003). Local validation of the OEM's lead-time claims on 12 months of company data is due by 2027-06-30.

**AI-003: Continue the pilot.** COO, 2026-09-17. Expand to all 6 areas only after the 6-month local validation meets the 90% target (due 2027-03-31).

**AI-004: Approve general release with conditions.** COO, 2026-09-17. By 2026-12-31: the SSI data loss rule is live (POAM-011), users complete a short module on confabulation and data rules, and public generative AI tools are blocked on company devices (P01 R-028).

**AI-005: Approve.** Security Manager, 2026-09-17.

These conditions are tracked as **POAM-019** (STD-05, AI-001 conditions 1 to 3) and POAM-003 (AI-002 data path). STD-05 is due 2026-12-31.

# AI Governance Risk Assessment: Enterprise AI Portfolio and the Pipeline Leak-Detection Anomaly Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded interstate natural gas transmission company; 9 states) |
| Tier / Vertical | Enterprise / Energy (natural gas pipeline) |
| Scope | Enterprise AI portfolio (11 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the pipeline leak-detection anomaly model, in section 6 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook; NIST AI 600-1 (Generative AI Profile) for the generative use cases (AI-005, AI-008, AI-009). AI-001 is not generative; AI 600-1 does not apply to it. Risk tiers use the repository rubric |
| Assessor / date | AI governance committee (chaired by the Vice President, Digital and Analytics), meeting of 2026-08-26; GRC team prepared the portfolio review; Director of Pipeline Integrity and Vice President, Gas Control prepared the AI-001 assessment |
| Decision | Executive risk committee, 2026-09-08 (section 8) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 11 |
| Risk tier | High 3, Medium 5, Low 3 |
| Status | In production 9, Pilot 1, Suspended 1 |
| Committee review complete | 7 of 11 |
| Not yet reviewed | 4: AI-008, AI-009, AI-011 (due 2026-11-30) and AI-010 (due 2026-12-31 with counsel); POAM-023 |
| Use cases that inform safety-related decisions | 3: AI-001 (leak detection), AI-002 (in-line inspection), AI-003 (right-of-way change detection) |
| Use cases running in or feeding Critical Cyber Systems (SD 02G) | 3: AI-001 (SYS-12 analytics platform), AI-007 (SOC), AI-011 (OT monitoring) |

**Main findings:**
1. The leak-detection model (AI-001) is advisory and isolated from SCADA, but its vendor deployed two model updates in 2026 without staging or Gas Control approval (POAM-019), it has not been validated on PS-3, and it detects small leaks less reliably on cellular-only segments.
2. Four use cases entered without review: a shipper-facing generative assistant piloted by the commercial team (AI-008), two vendor features switched on inside existing products (AI-009, AI-011), and an HR ranking feature (AI-010), now suspended.
3. Generative AI controls work: unapproved generative AI domains have been blocked at the proxy since 2026-04 (P01 R-041), and Restricted labels block SSI and CEII from the approved assistant (AI-005).

## 2. GOVERN: AI governance committee
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the risk committee of the board reviews quarterly.

**Members:** Vice President, Digital and Analytics (chair); CISO; Director of OT Security; Vice President, Gas Control; Director of Pipeline Integrity; Vice President, Pipeline Safety and Compliance; Chief Compliance Officer; a General Counsel delegate; Chief Human Resources Officer (for workforce tools); Chief Risk Officer. The Chief Audit Executive observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Validation on company data, including each pipeline system where it will be used; segment-group fairness testing; management of change with Gas Control for anything controllers see; procedure and training updates (192.615, 192.631); monitoring plan; for employment tools, counsel's adverse impact review |
| Medium | Committee vote | Human oversight design; output quality monitoring; disclosure where people interact with it; security and data handling review (POL-04) |
| Low | Committee chair (fast track) | Approved-tools listing; data handling rules |

**Intake and inventory.** Every new AI use, including AI features switched on inside existing products, must be registered before use (POL-05 4.7; STD-05.3). Procurement and change management have blocked AI features without an inventory ID since 2026-03. The GRC team owns the inventory.

**OT rule.** No AI system may write to SCADA, station controls, or field devices, or suppress, change, or add SCADA alarms. Any proposal to do so requires a new assessment, an architecture design review, a TSA plan amendment check (POL-01 4.7), and management of change.

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| 49 CFR 192.615(a)(12), rupture identification procedures | **Yes, for AI-001** | The procedures must specify the sources of information, operational factors, and other criteria personnel use to evaluate a notification of potential rupture. AI-001 is named there as a supporting source, with the rule that it never overrides SCADA alarms |
| 49 CFR 192.631, control room management | **Yes, for AI-001** | The model is information provided to controllers ((c)); its alert volume counts in the annual workload review ((e)(5)); its changes affect control room operations ((f)(3)); controllers are trained on its use and limits ((h)) |
| 49 CFR 192.705 and 192.706 | Yes (unchanged) | Patrols and leakage surveys remain required; AI-001 and AI-003 do not replace them |
| 49 CFR Part 192 integrity management | Yes, for AI-002 | Engineers remain responsible for evaluating anomalies; the model only pre-classifies |
| TSA SD Pipeline-2021-02G | **Yes, for AI-001, AI-007, AI-011** | The analytics platform hosting AI-001 is listed as a Critical Cyber System because a compromised model could mislead controllers (P04); AI-007 and AI-011 support the Section III.D monitoring measures. SD measures (patching, monitoring, access control, change amendments) apply |
| SSI and CEII (49 CFR Part 1520; 18 CFR 388.113) | Yes, for AI-005 and AI-009 | Restricted information may enter AI tools only with committee approval and no-training terms (POL-04 4.9) |
| Federal equal employment opportunity laws | Yes, for AI-010 | Counsel reviews adverse impact before any re-enable |
| FTC Act Section 5 | Indirectly | Accuracy of statements to shippers (AI-008) and vendor claims the company relies on (AI-001 to AI-003) |
| State AI laws | Reviewed by counsel | Counsel reviewed the laws of the nine operating states in 2026-07 for AI-008 and AI-010; the conclusions are in the legal file and are not restated or independently verified in this sample. AI-001 makes no decision about any individual |
| FERC-approved tariff | Yes, for AI-008 | The tariff, not the assistant, sets shippers' rights; every answer says so |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Leak-detection anomaly model (advisory alerts to controllers) | High | In production on PS-1, PS-2, and JV-1 to JV-3 | Reviewed 2025-11-12; re-reviewed 2026-08-26 |
| AI-002 | In-line inspection anomaly classification assistant | High | In production | Reviewed 2026-02-18 |
| AI-003 | Right-of-way imagery change detection | Medium | In production | Reviewed 2026-04-15 |
| AI-004 | Compressor predictive maintenance | Medium | In production | Reviewed 2025-12-10 |
| AI-005 | Enterprise generative AI assistant | Medium | In production (about 9,000 users) | Reviewed 2026-03-11 |
| AI-006 | Gas demand forecasting | Low | In production | Reviewed 2025-10-22 |
| AI-007 | SOC alert triage and detections | Low | In production | Reviewed 2026-05-20 |
| AI-008 | Shipper portal assistant (generative) | Medium | Pilot (about 40 shippers) | Not reviewed (due 2026-11-30) |
| AI-009 | Legal document review assistant (vendor feature) | Medium | In production (legal department) | Not reviewed (due 2026-11-30); SSI and CEII uploads blocked meanwhile |
| AI-010 | Applicant screening and ranking (HR software feature) | High | Suspended (ranking disabled) | Not reviewed (due 2026-12-31) |
| AI-011 | OT network monitoring anomaly detection (vendor feature) | Low | In production | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-002 is High because a missed or under-classified anomaly could delay a repair. AI-003 is Medium because every alert is verified and patrols continue. AI-004 is Medium because engineers approve every interval and manufacturer limits are enforced (P01 R-044, accepted at Low). AI-010 is High because ranking applicants is a consequential employment decision.

## 5. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; threshold breaches trigger re-review.
- **Change control:** models that inform controllers or engineers (AI-001, AI-002) are promoted only through a staging environment after backtesting and approval by the business owner, through management of change. Vendors have no production deployment rights (POAM-019 closes this for AI-001).
- **Third parties:** AI vendors are tiered as critical when their output reaches safety decisions; contracts require 30 days notice of material model changes, incident notice within 24 hours, and deletion of company data on exit (POL-01 4.8).
- **Incident handling:** suspected tampering with a model, its data, or the analytics platform is a severity-1 cyber incident under P08, and the model is taken out of the control room until revalidated. An unsafe output or bias finding is logged as an AI incident and reviewed by the committee.
- **Decommissioning:** a use case is retired if it fails its monitoring thresholds twice, if the vendor changes data-use terms, or if a vendor bypasses change control again; the inventory records retirement.

## 6. Full assessment: AI-001 pipeline leak-detection anomaly model
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Detect possible leaks or ruptures sooner than fixed SCADA alarms by comparing pressure, flow, and temperature patterns across segments with learned normal behavior, so field crews are dispatched earlier |
| Users / operators | About 150 qualified controllers at GCC-1 and GCC-2; alerts appear on a separate screen at each desk, not on the SCADA consoles |
| Affected people | People who live, work, and travel along the PS-1, PS-2, and JV pipelines, and the customers who depend on their deliveries. The model makes no decision about any individual |
| Data | Inputs: 1-minute historian data sent one way from the GCC DMZ replicas to the analytics platform on Cloud provider B (P04). Outputs: an anomaly score per segment and an alert when the score passes a threshold. No personal information. Engineering data is treated as CEII |
| Build or buy | Configure: the vendor's model, tuned on 24 months of company data. The vendor deployed two updates in 2026 directly to production (POAM-019) |
| Not intended | Closing valves, changing set-points, or suppressing SCADA alarms; replacing patrols (192.705) or leakage surveys (192.706); use on PS-3 before validation on PS-3 data |

### 6.2 Risk tier
**High.** The model does not act on the pipeline, but it shapes what controllers look at and when they dispatch crews. Two failure modes carry safety risk: a missed leak that falsely reassures a controller, and false alerts that train controllers to ignore it or distract them from SCADA alarms. What keeps it from being worse: it is advisory, has no path into SCADA, and the SCADA alarm system, patrols, and leakage surveys remain primary. Escalation triggers: any write-back or automatic action; using alerts to close valves without SCADA or field confirmation; removing or raising a SCADA alarm because of model coverage; a new model architecture or data source; extension to PS-3.

### 6.3 MEASURE
The vendor backtested the model on 24 months of history (11 known events: 3 third-party damage leaks and 8 planned blowdowns) and on simulated leaks injected into historical data at 1% and 5% of segment flow. The company compared alerts with shift logs for July and August 2026.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Detect simulated 1% leaks within 30 minutes in at least 90% of cases; detect all 5% leaks; detect all known events | 1% leaks: 91% overall; 5% leaks: 100%; known events: 11 of 11 (8 blowdowns correctly marked as planned when the maintenance flag was set) | Yes overall; **No** for cellular-only segments (below) |
| Safe | No path to SCADA; alerts never replace alarms; no more than 1 false alert per 12-hour shift | One-way path confirmed (P04, 2026-05 purple team). False alerts: 2.1 per shift on PS-1 (P01 R-042) | **No** (alert rate) |
| Secure and resilient | One-way input path; vendor changes staged and approved; workload access limited; monitored as a Critical Cyber System | Path and access confirmed; workload logs in the SIEM. Two vendor updates bypassed staging in 2026 | **No** (change control, POAM-019) |
| Accountable and transparent | Named owner; written controller guidance; model named in the 192.615(a)(12) procedures | Owner named; guidance issued 2026-06; procedures updated 2026-07 | Yes |
| Explainable and interpretable | Each alert shows which sensors drove it, so the controller can check SCADA trends | Available on every alert | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | Confirmed | Yes |
| Fair, with harmful bias managed | Detection and false-alert rates compared across segment groups (6.4) | Cellular-only segments under-detected; PS-3 not validated | **No** |

### 6.4 Fairness testing: is the protection spread evenly along the route?
For a model that makes no decision about individuals, the fairness question is whether communities along some segments get less early warning than others.

| Groups compared | Metric | Threshold | Result |
|---|---|---|---|
| Segments in Class 3 and 4 locations (more populated) vs Class 1 and 2 | Detection of 1% simulated leaks | No group more than 10 percentage points below overall | Class 3 and 4: 93%; Class 1 and 2: 90%. Pass |
| Segments relying on cellular-only telemetry vs microwave or radio | Same | Same | Cellular-only: 74% vs 91% overall. **Fail** |
| Low-flow periods (nights, mild weather) vs high-flow | Detection; false-alert rate | Same; false alerts no more than 2 times overall | Low-flow detection 87%; false alerts 1.7 times overall. Pass |
| By state crossed (PS-1, PS-2, and JV segments) | Detection of 1% simulated leaks | Same | Lowest state 86%. Pass |
| PS-3 segments | Validation on PS-3 data | Required before use | Not validated (different SCADA, data not yet in the historian). **Not in use** |

**Bias finding.** Segments whose meter and valve sites report only over cellular (part of the 140 cellular-only sites, P05) send data less often and drop more samples, so the model detects small leaks there less reliably. The fix is better data and honest display, not a lower threshold: second paths at the 40 most critical cellular sites (POAM-021), a coverage indicator on the alert screen so controllers know where the model is weaker, and a retest after each telemetry upgrade.

### 6.5 MANAGE
- **Human in the loop:** an alert is a prompt to look, not a finding. The controller checks the SCADA trends named on the alert; if they support a possible leak, the controller follows the abnormal operation or emergency procedure and dispatches field staff. Controllers annotate every alert; the shift supervisor reviews annotations weekly. A controller never discounts a SCADA alarm because the model shows no anomaly.
- **Procedures and training:** the model is named in the rupture identification procedures (192.615(a)(12)) as a supporting source; the controller training module covers what it sees and where it is weak; alert volume is part of the annual workload review (192.631(e)(5)).
- **Change control:** vendor updates deploy to a staging slot; the analytics team reruns the backtest and simulated leak set; the Vice President, Gas Control approves promotion through management of change (192.631(f)(3); POL-01 4.13). Vendor production rights are removed by 2026-10-15 and the contract amended by 2026-11-30 (POAM-019).
- **Monitoring (monthly, reported quarterly to the committee):** detection on a fresh simulated leak set; false alerts per shift; the segment-group comparison; data completeness by site. Tracked in P01 under R-039, R-040, and R-042.
- **Incidents:** a model outage is not an incident (controllers continue with SCADA alarms). Suspected tampering is a severity-1 cyber incident under P08, and the alert screen is switched off until revalidation.
- **Decommissioning:** remove the alert screen if false alerts stay above 2 per shift for two months after retuning, if the vendor changes the model again without approval, or if the vendor changes its data-use terms. On exit, the vendor deletes company data and confirms in writing.

## 7. Generative AI use cases (AI 600-1 view)
| Use case | Main AI 600-1 risks considered | Controls |
|---|---|---|
| AI-005 enterprise assistant | Information security (data leakage), confabulation | No training on company data; Restricted labels block SSI and CEII; users review outputs |
| AI-008 shipper portal assistant | Confabulation (wrong tariff answers), information integrity | Grounded on the tariff with citations; "the tariff controls" statement; weekly answer sampling; cannot act on nominations. Review due 2026-11-30 |
| AI-009 legal review assistant | Information security; data privacy of counterparties | SSI and CEII uploads blocked until review; vendor terms under review |

## 8. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the committee's recommendation of 2026-08-26:
1. **AI-001:** approved to continue as an advisory tool on PS-1, PS-2, and JV-1 to JV-3, with conditions: vendor production rights removed and the contract amended (POAM-019, by 2026-11-30); thresholds retuned to no more than 1 false alert per shift without dropping 5% leak detection below 100% (by 2026-12-31); coverage indicator for cellular-only segments on the alert screen (by 2027-03-31). Use on PS-3 requires validation on PS-3 data after the migration to the main SCADA platform (2027-06-30) and a new committee decision.
2. **AI-002 to AI-007:** approved to continue; next annual re-reviews scheduled.
3. **AI-008:** pilot may continue with the current 40 shippers until review by 2026-11-30; no expansion.
4. **AI-009 and AI-011:** may continue in current scope until review by 2026-11-30; SSI and CEII uploads to AI-009 stay blocked.
5. **AI-010:** ranking stays disabled until the committee review and counsel's adverse impact analysis are complete (by 2026-12-31).

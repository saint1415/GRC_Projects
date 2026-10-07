# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (owner and operator of 4 FERC-licensed hydroelectric projects; RMOS provider) |
| Tier / Vertical | Mid-Market / Dams |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. The registry default use case, dam-safety sensor anomaly detection, is AI-001 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook; NIST AI 600-1 (Generative AI Profile) for AI-005 |
| Assessors / date | Chief Dam Safety Engineer (dam safety), Vice President of Generation Operations (operations), Data Analytics Lead (models), OT Security Manager and vCISO (security), General Counsel (legal), 2026-08-17 to 2026-09-04 |
| Decision | Chief Operating Officer, 2026-09-17, on the recommendation of the AI review group; High-tier decisions noted by the CEO |

## 1. Summary
Two in-house models (AI-001, AI-002) went into use without validation, version control, or monitoring rules, and there was no AI policy or inventory (gap 12). AI-005 was rolled out to 300 users without review. None of the tools controls anything: every output is advice to a person. But two of them advise people on dam safety and flood operations, which is why they are High tier.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Dam-safety sensor anomaly detection | High | Approve with conditions (advisory only; manual reviews unchanged) |
| AI-002 | Reservoir inflow forecasting (BWB, CDS) | High | Approve with conditions (public forecast shown alongside; flood-peak fix) |
| AI-003 | Perimeter video analytics | Medium | Approve with conditions (night and rain testing) |
| AI-004 | Turbine predictive maintenance | Low | Approve |
| AI-005 | Enterprise generative AI assistant | Medium | Restrict until conditions are met (CEII excluded) |

Tiers: 2 High, 2 Medium, 1 Low.

**Non-negotiable across the portfolio:** no AI output may command a gate, unit, or siren, or flow back into the HCDMS. Data leaves OT one way, from the OT DMZ historian replica to the cloud (P04 finding 1). A June 2026 request to show AI-001 scores on SCADA displays was rejected for that reason.

## 2. GOVERN
- **Accountable owner for the AI program:** Chief Dam Safety Engineer (a licensed professional engineer designated under 18 CFR 12.61(a)), supported by the Data Analytics Lead and the vCISO. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.13: AI must be approved before use; no AI command path to OT.
  - POL-04 4.8: no Restricted (CEII) or Confidential data in AI tools unless the tool is approved for that level.
  - POL-05 4.6: approved tools only.
  - STD-11 AI use and model risk standard: due 2026-12-31 (POAM-019).
- **Approved-tools list:** kept by the IT Director. Today: AI-001 to AI-004 with their conditions; AI-005 for Internal data only, with the restricted library excluded. No public chatbot is approved for any company data.

### 2.1 Lightweight AI governance process
A mid-market company needs a short, reliable gate and a monthly rhythm, not a large committee.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | One-page intake for any new AI tool, AI feature, or model: purpose, users, data, decisions affected, link to OT | Requesting owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; check for any OT link (automatic High review) | OT Security Manager with the Data Analytics Lead | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, legal (data terms, no training on company data), and a business reviewer. **High:** full MAP and MEASURE like this document, with a performance and disparity test plan and a dam safety or operations reviewer | As listed | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: OT Security Manager. Medium: the **AI review group** (Chief Dam Safety Engineer, Data Analytics Lead, OT Security Manager, vCISO), 30 minutes monthly. High: the group recommends; the COO decides and informs the CEO | As listed | Monthly |
| 5. Model lifecycle | In-house models (AI-001, AI-002) are versioned in the model registry; a new version needs a back-test against the thresholds below before release; releases are logged | Data Analytics Lead | Each release |
| 6. Monitor | Owners report agreed metrics monthly; incidents go to P08 | Business owner | Ongoing |
| 7. Re-review | Annually, or on a trigger: new model version, new data source, new dam or client, proposal to reduce manual checks, or a missed event | AI review group | Annual |

**Repository tier rubric:** `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. AI that "can affect physical safety or critical infrastructure operations" is High.

## 3. MAP
| Item | AI-001 Anomaly detection | AI-002 Inflow forecasting | AI-003 Video analytics | AI-004 Predictive maintenance | AI-005 Generative assistant |
|---|---|---|---|---|---|
| Purpose | Flag developing failure modes earlier than the weekly manual trend review | Forecast reservoir inflow 24 to 72 hours ahead for release and pre-flood planning | Detect people and vehicles in restricted zones | Rank units for inspection | Draft, summarize, search documents |
| Users | 64 dam safety staff | ROC shift supervisors; scheduling desk | Security operations desk | Maintenance planners | 300 staff |
| Affected people | Downstream residents of 4 inundation zones (about 45,600 people) through dam safety; RMOS clients through reports | Downstream residents and recreation users; BA/TOP (schedules) | People on company property | None directly | Employees; anyone named in documents |
| Data | 410 instruments every 15 minutes, monthly manual reads for 7 open-standpipe piezometers, rainfall, levels | 9 river gauges, rainfall, public weather forecasts | Video from 64 cameras | Vibration, temperature, runtime | Suite content the user can reach |
| Build or buy | Build (in-house) | Build (in-house) | Buy | Buy | Buy |
| Not intended (prohibited) | Replacing trigger-point checks; deciding 12.10 reports or EAP actions; any control action | Setting gates; overriding the rule curve or minimum flows; EAP decisions | Automated enforcement; facial recognition | Control actions | Processing CEII or Security Program documents |

**Applicable laws and rules:**
| Rule | Use cases | Why |
|---|---|---|
| 18 CFR 12.10(a); 12.3(b)(4)(viii) | AI-001 | Unusual instrument readings are reportable conditions. The AI does not change that duty: a confirmed AI alert starts the 12.10 decision; an AI "all clear" never overrides a reading past a trigger point |
| FERC Security Program Rev. 3A 3.2 | AI-001 | Trigger points for action from critical instrumentation stay defined and checked by people |
| FERC Security Program Section 9 | AI-001, AI-002, AI-004 | Data comes from the Critical HCDMS. The path must stay one-way; any return path would change the Section 9 analysis |
| License operating requirements and EAP flood procedures | AI-002 | Releases follow the license rule curves and minimum flows; forecasts inform but never replace them |
| CEII (18 CFR 388.113) and Rev. 3A 3.2 OPSEC | AI-001, AI-005 | Instrument data and drawings near CEII; AI-005 must not reach the restricted library |
| FTC Act Section 5 | AI-003, AI-005 | Applies to vendor accuracy and privacy claims; keep the claims relied on in the procurement file |
| Fla. Stat. 501.171 | AI-005 | Employee personal information in documents |
| State AI laws (for example Colorado SB26-189) | None | They address consequential decisions about people (employment, lending, housing, and similar); no use case makes such a decision |

## 4. MEASURE
### 4.1 AI-001 dam-safety anomaly detection (High)
Back-test on 41 documented historical events at the 4 dams (2015-2026) and advisory results from 2026-01-01 to 2026-08-15.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Back-test recall, target at least 95% overall and 90% in every instrument group | 37 of 41 (90%) overall | **No** |
| Valid and reliable | Lead time compared with the weekly manual review | Median 4 days earlier | Yes |
| Safe | No manual check skipped or delayed because of the tool | 0 skipped in 2026; all 3 trigger-point exceedances found by the manual process (2 also flagged by the model) | Yes |
| Secure and resilient | One-way data path; access by role; models versioned | One-way path confirmed (P07); **no version control**: the running model could not be matched to a training run | **No** |
| Accountable and transparent | Every alert logged with a disposition | 486 alerts, all dispositioned; 22 confirmed real conditions (none past a trigger point) | Yes |
| Explainable and interpretable | Each alert names the instruments and readings that drove it | Yes | Yes |
| Privacy-enhanced | No personal information | None | Yes |
| Fair, with harmful bias managed | Performance across instrument types, dams, seasons, and instrument age (plan below) | Open-standpipe piezometers 4 of 7 events (57%) vs 18 of 18 vibrating-wire piezometers and 9 of 9 seepage weirs; inclinometers 6 of 7. False alarms per day: PNH 2.6 (instruments installed before 1990) vs BWB 0.8, CDS 1.1, SGR 0.4 | **No.** Disparities flagged |

### 4.2 AI-002 inflow forecasting (High)
Evaluation on 2018-2026 history and live use since 2025-10.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 24-hour forecast error (mean absolute percentage error) in normal flows | 14% (public river forecast 19%) | Yes |
| Valid and reliable | 24-hour error in the top 5% of flows (flood conditions) | 31%, with peaks underestimated by a median 18% (public forecast 22%) | **No**: worst exactly when it matters |
| Safe | Releases stayed within the rule curve and minimum flows | Yes in all 2025-2026 events; one pre-flood release started 9 hours later than the public forecast would have suggested (2026-06 storm, no harm) | Partial |
| Secure and resilient | One-way data; versioning | One-way confirmed; no version control | **No** |
| Accountable and transparent | Forecast shown to shift supervisors with its uncertainty band | Point forecast only, no band | **No** |
| Fair, with harmful bias managed | Error by season, storm type, and basin gauge coverage | Tropical-storm events (n=6) have twice the error of frontal storms | **No.** Disparity flagged |

### 4.3 AI-003, AI-004, AI-005
| Use case | Key test | Result | Action |
|---|---|---|---|
| AI-003 video analytics (Medium) | Detection rate in staged walk tests, day vs night and dry vs rain | Day 96%; night 88%; night in rain 71% | Add thermal cameras at 2 BWB gate houses; quarterly tests (P01 R-038) |
| AI-004 predictive maintenance (Low) | Agreement with vibration specialist rankings at BWB | 9 of 12 units ranked within 1 place | Approve; extend to CDS in 2027 |
| AI-005 generative assistant (Medium) | Can the assistant reach CEII? (AI 600-1 information security and data privacy risks) | Yes: test prompts returned text from 3 inundation map reports in engineering shares | Exclude the restricted library and engineering shares from the assistant index before re-enabling for those users (POAM-010, POAM-019) |

### 4.4 Bias and performance-disparity testing plan
For these use cases "bias" means a model working well for some parts of the dams, some instruments, or some storms, and poorly for others. No use case makes a decision about a person, so demographic fairness metrics do not apply to AI-001, AI-002, or AI-004. For AI-003, which watches people, the company checks that detection does not vary by clothing color or lighting in staged tests.

| Use case | Groups compared | Metric | Threshold | Frequency |
|---|---|---|---|---|
| AI-001 | Instrument type (vibrating-wire piezometers, open-standpipe piezometers, weirs, inclinometers, levels) | Recall on known and seeded events; false alarms per 100 instrument-days | Recall at least 90% in every group and 95% overall; no group's false alarm rate more than 2 times the overall rate | Before each release, then quarterly |
| AI-001 | Dam (BWB, CDS, PNH, SGR) and instrument age (before 1990, after 2010) | Recall; false alarms per day | No dam more than 5 points below overall recall; no dam above 2 times the median false alarm rate | Quarterly |
| AI-001 | Season (wet June to September vs dry) | False alarms per day; recall | Wet no more than 2 times dry; recall within 5 points | Each season |
| AI-001 | Staff reliance (automation bias) | Share of weekly manual reviews done on time; minutes per alert | 100% on time; no fall below 10 minutes per alert | Monthly |
| AI-002 | Flow percentile (normal vs top 5%) and storm type (tropical vs frontal) | Mean absolute percentage error; peak bias | Top-5% error no worse than the public forecast; peak underestimate no more than 10% | Each flood season and after each major storm |
| AI-003 | Light and weather (day, night, rain); clothing contrast | Detection rate in staged tests | At least 90% in every condition | Quarterly |

**Findings.**
- AI-001 misses events on the 7 open-standpipe piezometers because they are read only monthly, so it has too little data. The fix is not a better model: automate those 7 instruments or label them "not covered by AI" so nobody assumes they are watched. The high false alarm rate at Pine Hollow comes from old instruments and risks alert fatigue.
- AI-002 is least accurate during large storms, which are the events where it would matter most. Until the fix is proven, the public river forecast is shown alongside, and the shift supervisor uses the higher of the two for pre-flood planning.

## 5. MANAGE
**Human-in-the-loop design:**
- AI-001: every alert goes to the on-duty dam safety technician, who checks the instrument and records a disposition. The Chief Dam Safety Engineer reviews confirmed alerts and decides any action, 12.10 report, or EAP step. Weekly manual trend reviews and trigger-point checks continue unchanged; reducing them would need a new High assessment, at least 12 months of passing results, and approval by the COO and the Chief Dam Safety Engineer.
- AI-002: the ROC shift supervisor decides releases with the rule curve, the public forecast, and the model, and logs which forecast was used for pre-flood releases.
- AI-003: officers review every alert before dispatch. AI-004: planners decide work orders. AI-005: users own every output.

**Monitoring:** monthly metrics to the AI review group; quarterly disparity tests; results tracked against P01 R-035 to R-038.

**Incident handling:** a missed dam safety event found later by manual review, a forecast error that delays a release, or CEII exposure through AI-005 is logged as an AI incident and handled under P08 and POL-03. It does not change the 12.10 decision for the underlying condition.

**Decommissioning:** stop AI-001 if recall falls below 85% in a quarterly test or the one-way path cannot be kept; stop AI-002 if flood-season error stays worse than the public forecast after the 2027 fix; instrument and gauge data stay in the historian, so nothing is lost by stopping.

## 6. Decisions
**Chief Operating Officer, 2026-09-17, on the AI review group recommendation:**
1. **AI-001: approve with conditions.** Model registry and version control by 2027-01-31; the 7 open-standpipe piezometers labeled "not covered by AI" until automated (quote due 2026-12-31); Pine Hollow thresholds retuned and re-tested before 2027-06-01; manual reviews unchanged.
2. **AI-002: approve with conditions.** Uncertainty band and the public forecast shown alongside by 2026-11-30; flood-peak retraining tested against the 2026 storms before the 2027 flood season; version control by 2027-01-31.
3. **AI-003: approve with conditions.** Quarterly night and rain tests; thermal cameras at 2 BWB gate houses in 2027.
4. **AI-004: approve.**
5. **AI-005: restrict.** Restricted library and engineering shares excluded from the assistant index; re-enabled for the 300 users after a repeat CEII test passes (target 2026-12-15); public chatbots blocked.

These conditions are tracked as POAM-019 in P07.

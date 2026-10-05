# AI Risk Assessment: Water-Quality Anomaly Detection (Remote Monitoring Feature)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (privately held community water system, 2,850 population served) |
| Tier / Vertical | Micro / Water and Wastewater Systems |
| AI use case | AI-001: the anomaly detection feature of the remote monitoring service (SYS-05), on a free trial since 2026-06-15 |
| Framework | NIST AI RMF 1.0 (AI 100-1). The Generative AI Profile (AI 600-1) does not apply: the feature is not generative |
| Assessor / date | Office Manager (security and compliance coordinator) with the Chief Operator, 2026-08-25 |
| Decision | Owner and General Manager, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

**How the registry default was adapted.** The registry's use case for this industry is water-quality anomaly detection. A 7-person water system does not build or host a model. Here the use case is a feature of a SaaS service the company already pays for, which the Chief Operator turned on during a free trial. The assessment covers what the company controls: whether to use it, how operators act on it, and what the vendor may do with company data.

## 1. GOVERN
- **Accountable owner:** the Chief Operator, who runs the trial and owns the treatment process. **Decision authority:** the Owner and General Manager (High tier, section 3).
- **Policies that apply:**
  - POL-04 4.8: new tools and AI features must be approved before use; this feature is approved only as advisory under the conditions in section 6
  - POL-02 A.10: nothing may weaken the engineered safeguards, the fixed alarms, the alarm dialer, or hand operation
  - POL-02 A.5: vendor terms must cover security and use of company data
  - POL-02 B.3: MFA on the remote monitoring service
- **Approved-tools list:** kept by the Office Manager in POL-04 4.8. It has one AI entry: AI-001, advisory only.
- **Scale for a Micro water system:** there is no AI committee. The Owner, Chief Operator, and Office Manager review AI use at the monthly security meeting.
- **How the trial started is itself a finding.** The Chief Operator turned on the feature on 2026-06-15 from the vendor's in-app offer, with no review, no written purpose, and no check of the vendor's terms (P01 R-018; scenario gap 14). This assessment and POL-04 4.8 close that path.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Flag unusual combinations of readings earlier than fixed alarm limits can, for example a slow decline in chlorine residual with normal pump speed (a sign of analyzer drift or a feed problem), or a pressure drop with rising pump run time (a main break). The goal is earlier investigation by an operator, not automatic action |
| Users | The 3 licensed operators (on-call phone and app) and the Chief Operator |
| Affected people | The 2,850 people served, indirectly: a missed event could delay a response, and false alerts could cause unneeded flushing or call-outs. The operators are also affected: night alerts add to on-call fatigue for a 3-person rotation |
| Data | Inputs: entry point chlorine residual, well flows and run status, hypochlorite pump speed, ground tank and elevated tank levels, high-service pump status, and pressure at the elevated tank, sent every minute by the edge gateway. The vendor's model learns a baseline from the company's 2-year trend history. Outputs: an "anomaly" notification in the mobile app naming the signals involved and their expected range. No personal information. The data is Restricted under POL-04 because it shows how the plant runs |
| Build or buy | Buy: a vendor feature inside the remote monitoring service. The company cannot see or change the model; it can only turn the feature on or off and choose which signals are included |
| Vendor terms | The subscription terms allow the vendor to use aggregated and de-identified customer data to improve its analytics. The feature launched after the period of the vendor's SOC 2 report, so it has no independent assurance yet (P09) |
| Not intended | Controlling any equipment (the gateway's write-back is off and locked to the Chief Operator's account); replacing the continuous residual record or required grab sampling; deciding whether to issue a public notice; silencing, delaying, or replacing any fixed alarm or the alarm dialer |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Ground Water Rule compliance monitoring, 40 CFR 141.403(b)(3)(i)(A) | **Yes, unchanged** | The compliance record is the analyzer's continuous residual and the daily lowest value, with grab samples every 4 hours if the analyzer fails. The feature's output is never a compliance record and never a reason to skip a grab sample |
| Public notification, 40 CFR 141.202 | **Yes, unchanged** | Tier 1 decisions stay with the Chief Operator and the Owner, based on confirmed readings and grab samples. An anomaly alert can start an investigation; it cannot end one |
| SDWA section 1433, 42 U.S.C. 300i-2 | **No (readiness)** | Not applicable at 2,850 persons served (P03). If the population passes 3,300, the risk and resilience assessment must cover monitoring practices (300i-2(a)(1)(A)(iii)) and the emergency response plan must include detection strategies (300i-2(b)(4)). The feature would then need to be described accurately, including its limits (P03 G-004) |
| Fla. Stat. 501.171 | No | No personal information in inputs or outputs |
| State AI laws on consequential decisions | No | The feature makes no decision about any person, and the company operates only in Florida |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the rubric rates as High any AI that "can affect physical safety or critical infrastructure operations". The feature controls nothing, but operators act on its alerts, and a public drinking water system is critical infrastructure. Two failure modes reach public health: operators come to expect the feature to catch a slow problem it misses, or so many false alerts reach the on-call phone that operators start to ignore notifications from the app, including real ones.

**How the High-tier minimum controls apply at this size:**
- **Human review before action:** required. No process change, flushing, or notice on the basis of an alert without a grab sample, a second instrument, or a site check.
- **Pre-deployment testing:** required. The 60-day evaluation in section 4 is the test; the feature has not passed it.
- **Impact assessment:** this document.
- **Notice to affected people:** the feature makes no decision about individuals, so no one is notified individually. Transparency is met by telling operators, in writing and in the briefing, that alerts are advisory model output.
- **Ongoing monitoring:** every alert logged with its outcome; written result by 2026-10-31.

**Re-assess before any of these:** turning on write-back or any automatic action; using the feature to reduce grab sampling or to support a compliance record; changing which alarms reach the on-call phone because of it; a vendor change to the inputs or the alert method; buying the paid tier after the trial.

## 4. MEASURE
The Chief Operator and the Office Manager compared the feature's alerts from 2026-06-15 to 2026-08-16 (9 weeks) with the operators' daily logs.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable (detection) | Flag at least 80% of the events operators logged that needed action | 4 of 6 logged events flagged (67%): the main break on 2026-07-08, the hypochlorite day tank running low, the Well 3 pump trip, and the generator transfer during a storm outage. Missed: a slow chlorine analyzer drift and an elevated tank level sensor fault. Flagged 25 minutes before the fixed alarm in 2 cases, after it in 2 | **No** |
| Valid and reliable (false alerts) | No more than 2 alerts a week with no linked event (an on-call phone shared by 3 operators) | 41 alerts, 37 with no linked event: about 4.1 a week | **No** |
| Safe | Fixed alarms, the alarm dialer, and grab sampling stay primary; no write path to the PLC | Write-back off and locked (P07 CM-07b.[05]); the dialer is independent of the service | Yes |
| Secure and resilient | MFA on all accounts that can change the feature or the gateway; vendor assurance covering the feature | No MFA on any of the 5 accounts (POAM-004); feature outside the SOC 2 report period | **No** |
| Accountable and transparent | Named owner; alerts known to be model output; alert log | Owner named 2026-08-25; the app labels them "smart alerts" with no statement that they are model output; no log before this review | **No** |
| Explainable and interpretable | Each alert names the signals and their expected range | Yes, in the alert detail | Yes |
| Privacy-enhanced | No personal information; company data not used for other purposes without agreement | No personal information. Vendor terms allow de-identified use to improve analytics; no opt-out yet | Partial |
| Fair, with harmful bias managed | Compare detection and false-alert rates for signals from the plant with signals from the remote sites (see the plan below). Flag a detection gap of more than 10 percentage points | Plant signals: 3 of 4 events flagged (75%), 11 false alerts. Remote-site signals: 1 of 2 events flagged (50%), 26 false alerts | **No (flagged)** |

**Bias and fairness testing plan.** For this feature, fairness means every part of the service area gets the same protection. The groups compared are data sources, not people:
- **Groups:** (a) signals wired to the plant PLC (wells 1 and 2, chlorine, ground tank, high-service pumps); (b) signals from the remote sites that arrive over cellular telemetry (Well 3, elevated tank level, and the pressure at the elevated tank).
- **Metrics:** share of logged events flagged; false alerts per week; minutes before or after the fixed alarm.
- **Thresholds:** detection gap of 10 percentage points or less; false alerts per week from either group no more than 2 times the other.
- **Frequency:** at the end of the evaluation (2026-10-31), then every quarter if the feature is kept, and after any vendor change. The vendor is asked for its own per-signal performance data, because 9 weeks of a small system's events are too few to be sure.

**Bias finding.** Cellular telemetry from the remote sites has short dropouts. The feature reads each dropout as unusual, which caused most of the false alerts, and it learned a wider "normal" band for the elevated tank and missed its sensor fault. The elevated tank holds pressure for the far end of the system, including the elementary school. An unmanaged gap would give those customers less protection than customers near the plant. Until the vendor handles telemetry gaps, remote-site signals are excluded from any reliance, and the fixed tank and pressure alarms stay the only alarms that count.

## 5. MANAGE
**Data protection:**
- MFA on all 5 remote monitoring accounts by 2026-09-15 (POAM-004), and the user list reviewed quarterly (POL-02 B.6).
- Ask the vendor in writing to exclude the company's data from use for improving its analytics, and to confirm the feature will be in the next SOC 2 report. If the vendor refuses the opt-out, the Owner decides whether to keep the feature after weighing the benefit.
- No new signals (for example customer usage data from the billing system) may be added to the feature.

**Human in the loop:**
- Alerts are advisory. The operator who receives one checks the named signals on the HMI or app, then confirms with a grab sample, a second instrument, or a site visit before changing anything.
- Public notice decisions stay with the Chief Operator and the Owner, based on confirmed readings (40 CFR 141.202).
- Fixed alarm limits and the alarm dialer are the alarms of record. Operators may mute the feature's notifications during an incident or a storm, but never the fixed alarms or the dialer.
- The operator briefing and the plant binder say plainly: "Smart alerts are a model's guess. They do not replace alarms, grab samples, or rounds."

**Monitoring:**
- Every alert is written in the daily operator log with its outcome (real event, false alert, or unknown).
- The Chief Operator reviews the alert log monthly against P01 R-018 and R-015.
- Per-group results (plant versus remote sites) at the end of the evaluation and quarterly after.

**Incident handling:** an alert that turns out to be the first sign of a real event is recorded as a labeled event. A compromise of the remote monitoring service or the gateway follows the P08 runbook: the feature is turned off first; the plant does not depend on it. After any cyber incident the feature stays off until the trend data is verified (P08 section 7).

**Decommissioning:** turn the feature off and ask the vendor to confirm it has stopped processing company data for it if: the 2026-10-31 evaluation fails the thresholds below; the vendor will not agree to the data-use opt-out and the Owner does not accept that; or false alerts stay above 4 a week for 2 months in a row. The base remote monitoring service is unaffected.

## 6. Decision
**Continue the trial as advisory only, to 2026-10-31; not approved as a monitoring control.** Owner and General Manager, 2026-08-31. Conditions:
1. MFA on all 5 accounts by 2026-09-15.
2. Data-use opt-out requested and SOC 2 coverage asked about by 2026-09-30.
3. Operators briefed in writing that alerts are advisory, and every alert logged with its outcome, from 2026-09-01.
4. Remote-site signals excluded from reliance until the vendor handles telemetry gaps.
5. Written evaluation result by 2026-10-31 (P01 R-018), with the decision to keep or turn off the feature before any paid subscription.

**Keep after the trial only if all are met:** at least 80% of logged events flagged; no more than 2 false alerts a week; a plant versus remote-site detection gap of 10 points or less, or the remote-site signals removed from the feature. Even then, the feature remains a supplement to fixed alarms and grab sampling, never a replacement.

**Related actions:**
- **AI-002 (public chatbots).** Use only with Public information (POL-04 4.8; POL-02 C.2). The Office Manager reminds staff at the October 2026 training.
- **AI-003 (email security filtering).** No action beyond the existing MFA and phishing training; included so the inventory is complete.

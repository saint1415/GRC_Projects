# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Gas Transmission, Gathering and Production, Integrity Services, corporate) |
| Tier / Vertical | Multi-Sector / Energy |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the regulator-specific rules for the priority use case, the **pipeline leak-detection anomaly model** (AI-001), and the other High-tier use cases: the ILI anomaly classification model (AI-002) and proposed setpoint optimization (AI-005) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook; the Generative AI Profile (AI 600-1) for AI-007, AI-008, and AI-009. NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07; it is a concept note and is not used as a requirement here |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-09-03; presented to the board risk committee 2026-09-22 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 3 High, 5 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group OT Security Director, Group General Counsel, Vice President of Gas Control, Vice President of Field Operations Technology, Vice President of Integrity Engineering. Approves High-tier use cases and the approved-tools list |
| Division AI owners | The business owner named for each use case in the inventory; run monitoring and report monthly |
| Group CISO | AI security standard: model supply chain, prompt injection, data leakage, and where AI components sit relative to OT zones |
| Group General Counsel | Client disclosures, contract terms, state AI law screening |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-07-01, under POL-01 4.13)
1. **Register before use.** Every AI use case that informs controllers, field staff, integrity decisions, or client deliverables, or that processes Restricted information, is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). The rubric rates as High any AI that can affect physical safety or critical infrastructure operations. High tier: council approval, documented validation, and quarterly monitoring reports.
3. **Operational change control.** Any model, threshold, or display change that reaches controllers goes through the control room management of change (POL-01 4.8; 192.631(f)). Any model whose output could write to OT is a safety change and needs a safety management of change and an architecture review.
4. **Zones.** Models are trained outside OT (on SYS-G6). A scoring component inside an OT DMZ is part of that Critical Cyber System and follows its patching, access, and change rules. Model packages are signed and verified before they enter a DMZ.
5. **Data rules.** No SSI, OT configurations, or royalty owner data in generative AI tools unless the tool is approved for that class (POL-04 4.10; POL-05 4.9).
6. **Disclosure.** AI that materially shapes a client deliverable is disclosed to the client, with how a qualified person reviewed it.

**Where the program fell short in 2026.** The standard was adopted after the two High-tier models were in use. The leak-detection model showed advisory alerts on controller consoles from 2026-03 with no documented validation, and its threshold changes bypassed control room change management. The ILI model went into client deliverables in 2025-11 without disclosure or validation (scenario gap 9). Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Pipeline leak-detection anomaly model | Gas Transmission | High | Advisory; separate screen since 2026-09-08 pending validation |
| AI-002 | ILI anomaly classification model | Integrity Services | High | In client deliverables with conditions |
| AI-003 | Compressor predictive maintenance | Gas Transmission; Gathering and Production | Medium | In production |
| AI-004 | Production forecasting | Gathering and Production | Low | Approved |
| AI-005 | Automated compressor and choke setpoint optimization | Gathering and Production | High | Not approved (proposed) |
| AI-006 | Aerial methane detection | Gathering and Production | Medium | In production |
| AI-007 | SOC triage assistant (generative) | Group | Medium | Approved with conditions |
| AI-008 | Integrity report drafting assistant (generative) | Integrity Services | Medium | Pilot (40 engineers) |
| AI-009 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |

### 2.1 Leak-detection anomaly model (AI-001): pipeline safety and TSA rules
| Item | Description |
|---|---|
| Purpose | Detect possible leaks or ruptures sooner than fixed SCADA alarms and computational pipeline monitoring, by comparing segment behavior with learned normal behavior. The goal is earlier field dispatch |
| Users | About 90 gas controllers at both gas control centers |
| Data | 1-minute historian data replicated one way to SYS-G6 for training; live scoring on a server in the central OT DMZ. No personal information |
| Not intended | Closing valves, changing setpoints, suppressing or changing SCADA alarms, or replacing patrols, leakage surveys, or computational pipeline monitoring |

| Rule | Applies? | What it means for the model |
|---|---|---|
| 49 CFR 192.631(c), control room information | Yes | Alerts are information given to controllers; displays must be accurate and changes verified |
| 192.631(e)(5), controller workload | Yes | Alert volume counts toward the activity directed to each controller. The 2026-02 review predates the alerts (P03 G-100) |
| 192.631(f), change management | Yes | Model and threshold changes affect control room operations and need control room participation before they are made. **Gap:** 4 threshold changes in 2026 went through the data platform release process only (P03 G-104; POAM-026) |
| 192.631(h), controller training | Yes | Controllers need training on what the model sees, where it is weak, and how to respond |
| 192.615(a)(12), rupture identification procedures | **If used that way** | The procedures must "specify the sources of information, operational factors, and other criteria" personnel use to evaluate a notification of potential rupture. If controllers use model alerts that way, the model must be named in the procedures with how to weigh it. Today it is not |
| TSA SD 02G III.C and III.E | Yes | The scoring server sits in the central OT DMZ, inside a Critical Cyber System: access through PAM, patching under the plan methodology. A permanent change to how the DMZ hosts it may need a plan amendment (VI.B) |
| TSA SD 02G III.B | Yes | Training data leaves OT one way only; no path from SYS-G6 back into the DMZ except signed model packages through the patch relay (P01 TX-027) |
| State AI laws | No | The model makes no consequential decision about any individual |

### 2.2 ILI anomaly classification model (AI-002): client duties and claims
| Rule or commitment | Implication |
|---|---|
| Clients' 49 CFR 192.933(b) | Clients must obtain sufficient information about a condition promptly and no later than 180 days after an integrity assessment. They rely on the division's classifications to decide which conditions are discovered and when |
| Clients' 192.933(d)(1) | Immediate repair conditions require a pressure reduction or shutdown until repaired. A model that classifies an immediate condition as less severe could leave a client operating at full pressure on a pipe that needs repair |
| Client contracts | Deliverables must describe methods accurately. **Gap:** AI use not disclosed (P03 IG-17) |
| FTC Act Section 5 | Claims about the service, including accuracy and SSI handling, must be substantiated |
| SOC 2 (P09) | The model is outside the platform report; no processing accuracy commitment is made there |

### 2.3 Other division rules
| Use case | Rule | Implication |
|---|---|---|
| AI-005 setpoint optimization | Group AI Standard item 3; safety management of change; CSF 2.0 ID.RA-07 and PR.PS-01 (N21-BM) | A closed loop writing to field controllers is an OT change with safety consequences. Not approved as designed (P01 GP-009, treatment Avoid) |
| AI-006 aerial methane detection | 192.9(d)(8) and (e)(1)(vii) | Leakage surveys with leak-detection equipment remain required for Type B and Type C lines; aerial detection supplements them. Environmental reporting rules were not analyzed in this sample |
| AI-007 SOC triage | SD 01G II.C; POL-03 4.6 | People own every escalation and reporting clock. SSI-tagged alerts are excluded until the tool is approved for Restricted data |
| AI-008, AI-009 generative assistants | POL-04 4.10; POL-05 4.9; client contracts; Texas TRAIGA (intent-based prohibitions); Colorado SB26-189 | No SSI or OT configurations. TRAIGA applies to any business in Texas but its prohibitions are intent-based and none fits these uses. SB26-189 (effective 2027-01-01) covers AI that materially influences consequential decisions such as employment; AI-009 is prohibited for employment decisions, so it is not triggered |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 (shapes controller attention on a critical pipeline), AI-002 (drives client repair and pressure decisions), AI-005 (would act on OT).
- **Medium:** AI-003, AI-006, AI-007, AI-008, AI-009. People make the final decision, but outputs enter maintenance plans, repair work, security triage, client reports, or internal records.
- **Low:** AI-004.

**Re-tier and re-assess triggers:** any write-back to OT; using AI-001 alerts to close valves without SCADA or field confirmation; removing or raising a SCADA alarm because of model coverage; letting AI-002 release a classification without analyst review; new model architecture or data source; any SSI entering a generative tool.

## 4. MEASURE
Results from validation work and monitoring between 2026-03 and 2026-08.

### 4.1 Leak-detection anomaly model (AI-001)
Backtest on 24 months of history (including 9 known events: 3 third-party damage leaks and 6 planned blowdowns) and simulated leaks injected at 1% and 5% of segment flow; then comparison of alerts with shift logs for 2026-03 to 2026-08.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Detect simulated 1% leaks within 30 minutes in at least 90% of cases; detect all known events | 1% leaks: 86%. 5% leaks: 100%. Known events: 9 of 9 | **No.** Below target at 1% |
| Safe | No path to SCADA; no more than 1 false alert per console per 12-hour shift | One-way design confirmed (P04). False alerts: 3.1 per console per shift | **No.** Alert fatigue risk |
| Secure and resilient | Signed model packages; scoring server patched and accessed under the TSA plan | Signed packages verified; scoring server current | Yes |
| Accountable and transparent | Named owner; releases through control room change management; controller guidance | Owner named 2026-09-03; 4 threshold changes outside change management; no guidance | **No** |
| Explainable and interpretable | Each alert shows the segment and sensors that drove it | Available on every alert | Yes |
| Privacy-enhanced | No personal information | Confirmed | Yes |
| Fair, with harmful bias managed | Detection compared across segment groups (below) | One group below threshold | **No.** Disparity flagged |

**Fairness testing.** The model decides nothing about individuals, so the fairness question is whether early warning is spread evenly along the route.

| Groups compared | Metric | Threshold | Result |
|---|---|---|---|
| Segments in Class 3 and 4 locations vs Class 1 and 2 | Detection rate for 1% simulated leaks | No group more than 10 points below the overall rate | Class 3 and 4: 88%; Class 1 and 2: 85%. Pass |
| Segments whose meter stations poll every 5 minutes (older RTUs, 2 laterals) vs 1-minute polling | Detection rate | Same | 5-minute polling: 71% vs 86% overall. **Fail** |
| Low-flow periods vs high-flow periods | Detection and false-alert rate | Detection same; false alerts no more than 2 times overall | Detection 82%; false alerts 1.7 times. Pass |

**Bias finding.** The two laterals with slower polling serve smaller towns, so people there get less early warning from the model. The fix is better data, not a lower threshold: move those RTUs to 1-minute polling in the 2027 RTU program and show controllers a coverage indicator meanwhile.

### 4.2 ILI anomaly classification model (AI-002)
Validated against 1,480 field-verified dig results from 2021 to 2026.

| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Share of features verified as immediate repair conditions that the model classified as immediate (target at least 98%) | 58 of 61 (95%) | **No** |
| Safe | Analyst review of every feature at or near the immediate threshold before release | 2 of 40 sampled 2026 deliverables released a model classification without the required review | **No** |
| Fair across data sources | Agreement with dig results by ILI tool vendor data format; flag a gap above 5 points | Vendor C format: 89% vs 96% overall | **Flagged** |
| Accountable and transparent | Disclosure of AI use in deliverables | Not disclosed | **No** |
| Explainable | Analysts see the measured features behind each classification | Available | Yes |

### 4.3 Other use cases (summary)
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-003 predictive maintenance | Precision of failure warnings (target at least 60%) | 64% | Yes |
| AI-006 aerial methane detection | Detections confirmed by field crews | 71% confirmed; no missed leaks found by leakage surveys in the same areas | Yes |
| AI-007 SOC triage | Analyst agreement with suggested severity; SSI exclusion working | 91% agreement; 0 SSI-tagged alerts sent | Yes |
| AI-008 drafting assistant | Factual errors in sampled drafts reaching a signed report (target 0) | 0 of 50 signed reports; 7 drafts corrected by engineers | Yes |
| AI-009 enterprise assistant | Prohibited-content alerts (SSI markings, OT configurations) | 12 blocked prompts in the pilot | Yes (controls working) |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** an alert is a prompt to look, not a finding. The controller checks the SCADA trends named on the alert and follows the abnormal operating or emergency procedure if they support a leak. A controller may never ignore a SCADA alarm because the model shows nothing. The model cannot suppress, change, or add SCADA alarms.
- **AI-002:** a Level 3 analyst reviews every feature classified at or near the immediate repair threshold; the release system blocks a deliverable until the review is recorded.
- **AI-005:** advisory mode only, if ever approved; no write-back.

**Change control:** AI-001 releases go to a staging slot, the backtest and simulated leak set are rerun, and the Director of Gas Control approves promotion through the control room management of change (POAM-026). AI-002 retraining is approved by the Vice President of Integrity Engineering after validation against the dig set.

**Monitoring:** monthly metrics to owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-06, TX-009, TX-027, ES-006, ES-012, GP-009, GP-018.

**Incident handling:** suspected tampering with a model, its data, or the scoring server is a cyber incident under P08; the model is removed from the control room until revalidated. An AI-002 misclassification found after release is reported to the client the same day.

**Decommissioning:** each use case has an off switch and a fallback the BIA covers (P05): SCADA alarms and computational pipeline monitoring (AI-001), full manual analysis (AI-002), time-based maintenance (AI-003).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 leak-detection model | **Continue as advisory, on a separate screen** (council, 2026-09-03; implemented 2026-09-08) | Release gate through control room management of change by 2026-11-30; controller guidance and training module by 2026-12-31; retune to no more than 1 false alert per console per shift without dropping 5% leak detection below 100%; coverage indicator for slow-polling laterals; validation report by 2027-03-31 before any return to the main console (POAM-026). Not to be named in rupture identification procedures until validated |
| AI-002 ILI classification | **Continue with conditions** | Release block until analyst review is recorded, from 2026-10-31; disclosure in all new deliverables; validation by anomaly type and data source by 2026-12-31; re-review of 2026 deliverables for the 3 misclassified feature types with affected clients told; council approval by 2027-03-31 (POAM-023) |
| AI-005 setpoint optimization | **Not approved** | Advisory-only pilot may be proposed with a safety management of change and an architecture review |
| AI-007 SOC triage | **Approved with conditions** | SSI-tagged alerts excluded until the vendor tenant is approved for Restricted data |
| AI-008 drafting assistant | **Pilot continues** | No SSI; disclosure to clients before use beyond the pilot |
| AI-003, AI-004, AI-006, AI-009 | **Approved** | Standard monitoring; AI-009 prohibited for employment, operational, or safety decisions |

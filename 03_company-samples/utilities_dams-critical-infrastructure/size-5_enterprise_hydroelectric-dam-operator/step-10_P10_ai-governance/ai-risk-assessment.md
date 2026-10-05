# AI Governance Risk Assessment: Enterprise AI Portfolio and Dam-Safety Sensor Anomaly Detection

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hydroelectric generation company) |
| Tier / Vertical | Enterprise / Dams |
| Scope | Enterprise AI portfolio (11 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 dam-safety sensor anomaly detection in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) for AI-010 and AI-011; repository risk tier rubric. NIST's concept note for an AI RMF critical infrastructure profile is not final and is not relied on here |
| Assessor / date | AI council (chaired by the Chief Risk Officer), meeting of 2026-08-19; the GRC team prepared the portfolio review; the Vice President, Dam Safety led the AI-001 assessment |
| Decision | Executive risk committee, 2026-09-10 (section 9) |
| Registry default | Kept: "dam-safety sensor anomaly detection" fits this company, which runs the model for its own dams and sells it to SL-2 clients |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 11 |
| Risk tier | High 4, Medium 6, Low 1 |
| Status | In production 8, Pilot 2, Suspended 1 |
| Council review complete | 7 of 11 |
| Not yet reviewed | 4: AI-005, AI-008, AI-009, AI-011 (all due 2026-12-31, POAM-018) |
| Use cases that read OT data | 3 (AI-001, AI-002, AI-004), all through one-way paths; none can write to OT |
| High-tier tools with open measurement gaps | 2 (AI-001 recall by instrument type and reporting frequency; AI-004 small-basin error) |

**Main findings:** no AI output reaches a control system, and that rule held in every use case reviewed. The material risks are elsewhere: AI-001 is now relied on by 46 SL-2 clients whose own manual review practices the company cannot see; its thresholds and model versions change without formal change control (P01 R-042, POAM-019); and four use cases, including a High-tier hiring tool (AI-009, now suspended), entered through vendor features without council review.

## 2. GOVERN: AI council operating model
**Charter.** The AI council was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-09 (P01), which the safety, risk, and reliability committee reviews quarterly.

**Members:** Chief Risk Officer (chair); Vice President, Dam Safety (Chief Dam Safety Engineer); CISO; Director, OT Security; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce tools); Senior Vice President, Hydro Operations or delegate; Vice President, Dam Safety Monitoring Services; the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Council vote, then the executive risk committee; for any tool touching dam safety, the Chief Dam Safety Engineer must also approve | Back-testing and disparity testing on company data; impact assessment; human review design; confirmation that no output reaches OT; monitoring plan; notice to clients or affected people |
| Medium | Council vote | Human oversight design; output quality monitoring; disclosure where people interact with it; security and data handling review |
| Low | Council chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Non-negotiable rules (all tiers):**
1. No AI output may write to, command, or change settings in any OT system. Data leaves OT one way (P04 section 1).
2. No AI output may replace a trigger-point check, a manual reading required by an instrumentation plan, an 18 CFR 12.10 decision, or an EAP decision.
3. No Restricted information (CEII, BCSI, FERC security documents) in an AI tool unless the council approved that tool for Restricted data (POL-04 4.8). Today only AI-001 and AI-005 are approved, and only for CEII they generate.

**Intake and inventory.** Any new AI use, including AI features switched on inside vendor products, must be registered before use (POL-05 4.6; STD-05.3). Procurement and IT change management have blocked AI features without an inventory ID since 2026-03; the four unreviewed use cases predate that block or were switched on by vendors (AI-008 in 2026-05 is being investigated as a gap in the block).

**Cadence:** monthly council meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| 18 CFR 12.10(a); 12.3(b)(4)(viii) | **Yes, indirectly** (AI-001) | Unusual instrumentation readings are conditions affecting safety that must be reported as soon as practicable, preferably within 72 hours. An AI alert that staff confirm as unusual starts the 12.10 decision; an AI "all clear" never overrides a reading past a trigger point |
| FERC Security Program Rev. 3A 3.2 and Section 9 | **Yes** (AI-001, AI-002, AI-004) | Trigger points must be defined and checked by people. The one-way data path keeps these tools outside the Section 9 boundary; a return path would change the analysis |
| NERC CIP | **No direct effect** | No AI tool runs on or connects to a BES Cyber System. AI-006 reads OT sensor alerts in the SIEM, which may contain BCSI, so its data handling follows CIP-011-3 |
| CEII handling (18 CFR 388.113; POL-04) | Yes (AI-001, AI-005, AI-010, AI-011) | Alerts and imagery describing failure modes or vulnerabilities are CEII; generative tools must not index CEII libraries |
| FTC Act Section 5 | Yes (AI-001 for SL-2) | Claims to SL-2 clients about what AI-001 detects must be accurate and supported; the system description states it is advisory (P09) |
| Federal equal employment opportunity laws | Yes (AI-009) | Adverse impact analysis by counsel before any re-enable |
| State AI and privacy laws | Tracked | Counsel tracks AI-specific laws in the seven states where the company operates; none is relied on in this assessment. Florida is the worked example for applicant data breaches (Fla. Stat. 501.171) |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Council review | OT or safety interaction |
|---|---|---|---|---|---|
| AI-001 | Dam-safety sensor anomaly detection | High | In production (advisory) for company dams since 2025-11 and for SL-2 clients since 2026-03 | Reviewed 2025-10-22; re-reviewed 2026-08-19 | Reads OT data one way through diodes; no output flows back to OT |
| AI-002 | Turbine and generator condition monitoring that flags vibration and temperature trends for maintenance planning | Medium | In production (125 units) | Reviewed 2025-12-10 | One-way historian replica only |
| AI-003 | Generation dispatch and water-value optimization recommending unit commitment and reservoir drawdown for the day-ahead schedule | High | In production | Reviewed 2026-01-14 | None directly; schedules reach the HOC through the OT DMZ file transfer and operators apply them |
| AI-004 | Reservoir inflow forecasting (machine learning ensemble) used for reservoir planning ahead of storms | High | In production | Reviewed 2025-11-19 | None; forecasts shown on HOC displays as information only |
| AI-005 | Drone and camera imagery analysis that flags concrete cracking, spalling, and embankment anomalies for dam safety inspections | Medium | Pilot (6 dams) | Not reviewed (review due 2026-12-31) | None; imagery leaves through the inspection program, not OT |
| AI-006 | SOC alert triage assistant that groups and ranks security alerts | Low | In production | Reviewed 2026-02-11 | Reads OT sensor alerts in the SIEM; no OT access |
| AI-007 | Video analytics that detect people and vehicles in restricted zones at Group 1 and 2 dams | Medium | In production (23 dams) | Reviewed 2025-09-30 | None (physical security network) |
| AI-008 | Energy price forecasting that informs bilateral trading and bids | Medium | In production (vendor feature switched on 2026-05) | Not reviewed (review due 2026-12-31) | None |
| AI-009 | Seasonal hiring resume screening and ranking in the HR platform (about 900 recreation and seasonal roles a year) | High | Suspended (ranking disabled pending review) | Not reviewed (review due 2026-12-31) | None |
| AI-010 | Enterprise generative AI assistant in the productivity suite for drafting and summarizing | Medium | In production (about 6,000 users) | Reviewed 2026-03-18 | None; no OT access |
| AI-011 | Contract and regulatory document review assistant for the Legal department | Medium | Pilot (Legal only) | Not reviewed (review due 2026-12-31) | None |

**Tiering notes:** AI-001 and AI-004 are High because a missed anomaly or a bad forecast could delay a dam safety response, even though both only advise. AI-003 is High because it shapes unit commitment and reservoir drawdown on critical infrastructure; license limits enforced in SCADA keep it from causing a violation on its own. AI-005 stays Medium while engineers review every flag and Part 12D inspections are unchanged. AI-009 is High because it ranks job applicants.

## 5. Safety and OT boundary controls (portfolio)
| Control | How it is enforced | Evidence |
|---|---|---|
| One-way data only | Data diodes and the OT DMZ transfer; cloud route tables with no path to OT (P04) | Route and diode reviews; SOC alert on new routes |
| Advisory labeling | AI scores shown in a separate pane, labeled "advisory", never in alarm lists that drive operator action | Screen review 2026-08-19 |
| Manual checks preserved | Instrumentation plans unchanged; on-time completion reported monthly | Dam safety metrics |
| Change control for models and thresholds | Model registry for AI-001 and AI-004 versions; **thresholds not yet under change control (POAM-019)** | Model registry; DSMS change workflow (due 2026-12-31) |

## 6. MEASURE: performance disparity testing plan
For the safety tools, "bias" means the tool working well for some parts of the fleet (or some clients) and poorly for others. They make no decisions about people, so demographic fairness metrics do not apply; what does apply is whether any dam, instrument type, or client group is watched less well. For AI-009, classic adverse impact testing applies before any re-enable.

| Tool | Groups compared | Metric | Threshold for action |
|---|---|---|---|
| AI-001 | Instrument type; dam type (embankment, concrete); reading frequency (15-minute, hourly, monthly manual); company vs client dams; season | Recall on known and seeded events; false alarms per 100 instrument-days | Recall at least 90% in every group and 95% overall; no group's false alarm rate more than 2 times the overall rate |
| AI-004 | Basin size; storm type (tropical, frontal, convective) | Peak inflow error; timing error | Peak error no more than 15% in any group |
| AI-007 | Camera; lighting (day, night); weather | Missed detections in seeded tests; false alarms | Missed detections under 5% in every group |
| AI-009 (before any re-enable) | Sex; race and ethnicity where self-reported; age 40 and over | Selection-rate ratio | Ratio below 0.8 for any group blocks re-enable |

## 7. Full assessment: AI-001 dam-safety sensor anomaly detection
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Score readings from about 3,900 instruments at 52 company dams and about 2,600 instruments at 138 client dams for patterns that suggest a developing failure mode (rising pore pressure, seepage after rain, movement), earlier than periodic manual trend review |
| Users | About 140 company dam safety technicians and regional engineers; client dam safety staff through the SL-2 portal |
| Affected people | Nobody is the subject of a decision. The people who bear the risk are downstream residents, recreation users, and staff of company and client dams |
| Data | Inputs: readings every 15 minutes (most automated instruments), hourly (some client dataloggers), or monthly (manual instruments); rainfall; reservoir levels. Outputs: an anomaly score and the readings that drove it. Training data: company dams 2010-2026 and dams of 31 of 46 SL-2 clients that opted in under their agreements |
| Build or buy | Build: company data science team on Cloud provider B managed machine learning, with no provider training on company data |
| Not intended | Controlling gates or units; replacing trigger-point checks; deciding 12.10 reports or EAP actions; reducing manual reading frequency. These uses are **prohibited** |

### 7.2 Risk tier
High (section 4). Escalation triggers (re-assessment needed first): any proposal to reduce manual readings or reviews; any automated link from AI output to EAP notifications, 12.10 reports, or control actions; a new model version; adding new instrument types or client data sources.

### 7.3 MEASURE (back-test on 147 documented events, 2010-2026, and live results 2025-11 to 2026-07)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Back-test recall, target at least 95% overall | 138 of 147 events detected (94%) | **No** |
| Valid and reliable | Lead time vs periodic manual review on detected events | Median 4 days earlier | Yes |
| Safe | No skipped or delayed manual checks at company dams; all trigger-point exceedances handled by the manual process | 0 skipped checks; 11 exceedances found manually, 10 also flagged by AI-001 | Yes (company dams) |
| Safe | Same check for SL-2 clients | **Not observable**: the company cannot see clients' manual practices | **Open** (contract and client notice, section 7.5) |
| Secure and resilient | One-way data path; SSO with MFA; per-client keys; DR | One-way confirmed; DSMS ingestion RTO missed in test (POAM-020) | Partial |
| Accountable and transparent | Every company alert dispositioned; model and threshold changes traceable | 1,326 alerts, all dispositioned; **threshold changes not traceable** (POAM-019) | **No** |
| Explainable and interpretable | Each alert names the readings that drove it | Yes for all alerts | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | None | Yes |
| Fair, with harmful bias managed | Recall by instrument type, dam type, reading frequency, and company vs client dams | See below | **No** (disparities above threshold) |

**Disparity results:**
| Group | Recall | Threshold met? |
|---|---|---|
| Vibrating-wire piezometers (15-minute) | 97% | Yes |
| Seepage weirs (15-minute) | 95% | Yes |
| Inclinometers (15-minute) | 91% | Yes |
| Manually read instruments (monthly) | 71% | **No** |
| Client dams reporting hourly | 88% | **No** |
| Concrete dams vs embankment dams | 96% vs 93% | Yes |
| Wet-season false alarms vs dry season | 2.6 times | **No** (target 2 times or less) |

**Finding.** The model sees too little data from monthly manual instruments and hourly client dataloggers to be relied on for them. The fix is not a better model: either increase reporting frequency or exclude those instruments from AI coverage and say so plainly, so nobody assumes they are watched. Wet-season false alarms risk alert fatigue exactly when dams are most loaded.

### 7.4 What makes AI-001 different at this size
At a single-dam company, the people reviewing alerts also do the manual readings. Here, 46 clients receive AI-001 alerts and run their own surveillance programs, and the company cannot see whether they keep their manual checks. That moves part of the automation-bias risk to clients and creates a contract and reputation risk for the company (P01 R-046). It also makes change control for thresholds and models a service commitment, not just an internal practice (P09 CC8.1).

### 7.5 MANAGE
- **Human in the loop:** every company alert goes to the on-duty technician, who checks the instrument and records a disposition; the regional engineer reviews confirmed alerts; the Chief Dam Safety Engineer decides any action, 12.10 report, or EAP step.
- **Client side:** SL-2 agreements and the portal state that AI-001 is advisory and does not replace the client's trigger-point checks or instrumentation plan; clients confirm this annually. Instruments outside AI coverage are labeled "not covered by AI" in the portal.
- **Change control:** threshold and model changes through a workflow with dual approval, audit trail, back-testing, and client notice (POAM-019, due 2026-12-31).
- **Monitoring:** monthly alert statistics and automation-bias measures for company dams; quarterly disparity tests; results to the council and tracked against P01 R-060.
- **Incidents:** a missed event later found by manual review is logged as an AI incident, analyzed, and, for clients, reported to the affected client within the contract's 24-hour notice term. It does not change the 12.10 decision for the underlying condition.
- **Decommissioning:** stop using AI-001 for any group if quarterly recall falls below 85%, if the one-way path cannot be kept, or if client training-data consent is withdrawn and the model cannot be retrained without that data. Readings stay in the OT historian and the DSMS, so nothing is lost by stopping.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has quarterly performance and disparity metrics (inventory column `monitoring`) reported to the council; breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, disparity finding, data misuse) are logged as SOC or dam safety events and follow P08 where security or client data is involved.
- **Third parties:** AI vendors are tiered in the vendor program; contracts require notice of material model changes and no training on company data.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice, change data-use terms, or need a return path into OT.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the council's recommendation of 2026-08-19:
1. **AI-001:** approved to continue as advisory, with conditions: label manually read instruments and hourly-reporting client instruments "not covered by AI" by 2026-11-30; threshold and model change control by 2026-12-31 (POAM-019); client notice and annual confirmation of advisory use by 2027-01-31; wet-season threshold tuning and re-test before 2027-06-01. No reduction in manual reviews is approved.
2. **AI-004:** approved to continue; small-basin error improvement plan by 2027-03-31; output stays information only (P01 R-062).
3. **AI-005, AI-008, AI-011:** may continue in current scope until council review by 2026-12-31; no expansion. The AI-008 activation outside the intake block is investigated by the CIO.
4. **AI-009:** ranking stays disabled until council review and an adverse impact analysis are complete.
5. **AI-010:** CEII and BCSI library exclusion re-verified quarterly (P01 R-063).
6. All open items are tracked as POAM-018 (council reviews and AI-001 conditions) and POAM-019 (change control).

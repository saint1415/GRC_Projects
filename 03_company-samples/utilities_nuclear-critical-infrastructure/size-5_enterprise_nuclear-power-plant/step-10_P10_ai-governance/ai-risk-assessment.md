# AI Governance Risk Assessment: Enterprise AI Portfolio and Predictive Maintenance for Non-Safety Plant Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded nuclear generation company; four stations, seven units; FL, GA, SC, AL) |
| Tier / Vertical | Enterprise / Nuclear Reactors, Materials, and Waste |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 predictive maintenance for non-safety plant equipment in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) for the generative use cases (AI-002, AI-004, AI-008, AI-010); repository risk tier rubric. AI-001 is not generative, so AI 600-1 is not applied to it |
| Assessor / date | AI governance committee (chaired by the Senior Vice President, Nuclear Engineering), meeting of 2026-08-19; the GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 3, Medium 6, Low 3 |
| Status | In production 9, Pilot 2, Suspended 1 |
| Committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-005, AI-009, AI-011, AI-012 (all due 2026-11-30, POAM-020) |
| Use cases that touch a nuclear safety or regulatory work process | 5: AI-001 (Maintenance Rule and work management), AI-004 (corrective action program), AI-005 (outage scheduling), AI-006 (dose of record), AI-008 (work packages) |
| High-tier use cases validated only at an aggregate level | 1: AI-001 (fleet-level metrics only; P01 R-042, R-043) |

**Main findings:** four use cases entered through vendor feature releases and are running (or piloting) without committee review, including one High-tier employment tool (AI-011, now suspended) and an outage scheduling feature (AI-005) that sits next to Technical Specification surveillance scheduling. AI-001 performs well at fleet level, but it has never been tested by station or equipment class, and its Station 4 data path (wireless sensor gateways with cellular links) was installed without the 73.54(b)(1) analysis.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly. Use cases that touch nuclear safety processes are also reported to the nuclear safety oversight committee.

**Members:** Senior Vice President, Nuclear Engineering (chair); CISO; Director, Nuclear Cyber Security; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce and HR tools); Vice President, Monitoring and Diagnostics Services; a Maintenance Rule Coordinator (rotating among the four stations); Corrective Action Program Manager (fleet); Export Compliance Officer; the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Validation on company data, including subgroup testing (by station and equipment class for plant uses; adverse impact for people decisions); impact assessment; human review design; data path security review (including 73.54(b)(1) where devices sit near plant equipment); notice to affected people where they exist; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy, security, and export control review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.8; STD-05.3). Since 2026-03, procurement and IT change management block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.3 (no SGI in AI tools), POL-04 4.5 (export-controlled technology), POL-04 4.8 (no Confidential or Restricted data in AI tools without committee approval and no-training contract terms); POL-05 4.8 (approved tools only); POL-01 4.13 (no new device or data path near plant equipment without the 73.54(b)(1) analysis); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case.

**Why 4 use cases lack review.** All four arrived as features in vendor releases (EAM, ERP, HR, and IT service management platforms) before the intake block existed in 2026-03. The committee set review dates for all four (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules (NRC) | None found | No NRC regulation specific to AI use by power reactor licensees was identified. The NRC rules that govern the work processes AI feeds still apply in full: the Maintenance Rule, Technical Specification surveillance requirements, the corrective action program, and the cyber security program |
| 10 CFR 50.65 (Maintenance Rule) | Yes, as context for AI-001 and AI-005 | Licensees must monitor the performance or condition of SSCs in scope against goals (50.65(a)(1)) and must assess and manage the increase in risk from maintenance before performing it (50.65(a)(4)). Scope includes non-safety SSCs whose failure could cause a reactor scram or actuation of a safety-related system (50.65(b)(2)(iii)). AI-001 advisories feed this work but never replace it |
| 10 CFR 50.36(c)(3) (surveillance requirements) | Yes, as context for AI-005 and AI-008 | Surveillance schedules and the work packages that implement them must stay accurate; AI-005 is barred from surveillance scheduling |
| 10 CFR 73.54 | Yes, for AI-001 data paths | Sensors, gateways, or connections near plant equipment need the 73.54(b)(1) analysis and the design change cyber review (73.54(d)(3)) before installation. AI-001 receives plant data only from the historian replicas on the business side of the one-way devices at Stations 1 to 3 |
| 10 CFR Part 810 | Yes, for AI-001 (SL-1), AI-008, AI-010 | Reactor technology in documents and models must not reach unauthorized foreign persons (810.2(a)(2)); the Export Compliance Officer reviews any SL-1 expansion to plants outside the United States |
| 10 CFR 20.1501(d); 20.2106 | Yes, for AI-006 | The dose of record comes from the NVLAP-accredited process; AI-006 only flags readings for technician review |
| 10 CFR Part 50, Appendix B | Not for current uses | No AI use case is applied to safety-related SSCs or safety-related procedures. Any such use would need evaluation under the company's quality assurance program first and is prohibited until then |
| Federal equal employment opportunity laws | Yes, for AI-011 | Counsel reviews adverse impact before any re-enable |
| Colorado SB26-189 | Not today | Effective 2027-01-01; the company has no Colorado operations. It would matter for AI-011 only if the company hired for Colorado positions |
| FTC Act Section 5 | Indirectly | Accuracy of AI claims made to SL-1 clients about AI-001 advisories |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Committee review | Nuclear process touched |
|---|---|---|---|---|---|
| AI-001 | Predictive maintenance for non-safety plant equipment | High | In production (Stations 1 to 3, SL-1 clients; Station 4 suspended) | Reviewed 2025-11-12; re-reviewed 2026-08-19 | Maintenance Rule monitoring; work management |
| AI-002 | Enterprise generative AI assistant | Medium | In production (about 6,000 users) | Reviewed 2025-10-08 | None |
| AI-003 | SOC alert triage assistant | Low | In production | Reviewed 2026-02-11 | Indirect (SOC input to 73.77 decisions) |
| AI-004 | Condition report screening assistant | High | Pilot (Station 1) | Reviewed 2026-05-20 | Corrective action program |
| AI-005 | Outage schedule optimization suggestions | Medium | Pilot (test environment) | Not reviewed (due 2026-11-30) | Outage scheduling |
| AI-006 | Dosimetry reading anomaly flagging | Medium | In production | Reviewed 2026-03-18 | Dose of record processing |
| AI-007 | Energy price and load forecasting | Medium | In production | Reviewed 2025-12-10 | None |
| AI-008 | Generative AI drafting assistant for work packages and non-safety procedures | Medium | In production (about 400 users) | Reviewed 2026-01-14 | Work package preparation |
| AI-009 | Spare parts demand forecasting | Low | In production | Not reviewed (due 2026-11-30) | None |
| AI-010 | Engineering document search assistant | Medium | In production | Reviewed 2026-04-15 | Design control (information only) |
| AI-011 | Applicant resume screening and ranking | High | Suspended (ranking disabled) | Not reviewed (due 2026-11-30) | None |
| AI-012 | Employee help desk virtual agent | Low | In production | Not reviewed (due 2026-11-30) | None (kept away from access authorization and FFD records) |

**Tiering notes:**
- **AI-001 is High at this company,** although the same kind of tool can be Medium at a smaller, simpler plant. Its scope includes balance-of-plant equipment whose failure could trip a unit, which is critical infrastructure operation under the rubric. It stays advisory: a person decides every action and the model cannot write to plant systems. High tier buys the full set of controls, not a ban.
- **AI-004 is High** because a wrong significance rating could delay corrective action on a safety-significant condition. During the pilot the committee rates every report first, so the residual risk is Low (P01 R-044).
- **AI-005 is Medium** while surveillance schedules are excluded from it; letting it touch surveillance scheduling would re-tier it to High.
- **AI-008 is Medium** because qualified reviewers sign every draft and it is not used for safety-related procedures (P01 R-047).

## 5. Nuclear guardrails for every AI use case
These rules apply across the portfolio and are checked at committee review:
1. **No control, no writes.** No AI system may send commands or data to a CDA, a plant control system, or a security or emergency preparedness system. Plant data reaches AI only from the business side of the one-way data transfer devices.
2. **No new paths without analysis.** A sensor, gateway, or connection installed near plant equipment for an AI use case needs the 73.54(b)(1) analysis and design change cyber review first (POL-01 4.13). The Station 4 gateways for AI-001 broke this rule (POAM-018).
3. **Licensing basis untouched.** AI output never changes a Technical Specification surveillance interval, a preventive maintenance task, a Maintenance Rule goal, or a CAP significance level by itself. A person changes them through the normal process, with the normal reviews.
4. **Prohibited inputs.** SGI, security-related information (CSP details, CDA inventories, network diagrams), and access authorization or fitness-for-duty records never enter an AI tool. Export-controlled technology enters only tools approved for it, with US-person filtering (AI-010).
5. **Vendor features count.** An AI feature switched on in a vendor release is a new use case and goes through intake.

## 6. MEASURE: subgroup testing plan for AI-001 (station and equipment class)
**Gap.** AI-001 metrics are reported only for the fleet as a whole. The fleet mixes pressurized water reactor and boiling water reactor units, four stations with different equipment vendors and ages, and two data sources (historian replicas at Stations 1 to 3, wireless sensors at Station 4). Good fleet averages can hide a station or equipment class where the model misses failures (P01 R-042, R-043). For a model that makes no decisions about people, "bias" here means **uneven performance across groups of equipment and operating conditions**.

**Plan (POAM-020; results due 2027-01-31, thresholds and monitoring updated by 2027-03-31):**
| Group compared | Metric | Threshold for action |
|---|---|---|
| Station (1, 2, 3; Station 4 after its data path is approved) | Recall on known degradation events; precision; median lead time | Any station's recall more than 10 points below the fleet, or below 75% |
| Equipment class (large pumps, motors, fans and cooling tower equipment, compressors, heat exchangers) | Recall; precision | Any class's recall more than 10 points below the fleet; precision more than 15 points below |
| Maintenance Rule scope (50.65(b)(2)(iii) equipment versus other non-safety equipment) | Recall; lead time | Recall on (b)(2)(iii) equipment below the fleet rate at all |
| Plant type (pressurized water reactor versus boiling water reactor units) | Recall; precision | Recall gap over 10 points |
| Operating mode (at power versus outage and startup) | False-alarm rate | False-alarm rate over 50% in any mode |
| Data source and completeness | Share of expected sensor data received | Below 90% for any station or class |

**Method:** known degradation events come from corrective maintenance work orders and Maintenance Rule functional failure records for 2024 to 2026, labeled by the Maintenance Rule Coordinators. Each station's results are reviewed by its Maintenance Rule Coordinator and system engineers. If a group fails a threshold, the model is retrained or the group is excluded from advisories, and the station keeps its existing monitoring. Results go to the committee and the nuclear safety oversight committee.

## 7. Full assessment: AI-001 predictive maintenance for non-safety plant equipment
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Detect developing faults in non-safety rotating and heat transfer equipment early, estimate remaining useful life, and advise system engineers so maintenance can be planned, for example into the next outage, instead of after a failure |
| Assets in scope | About 9,600 monitored non-safety equipment points across the fleet's seven units and SL-1 client plants, including balance-of-plant equipment in Maintenance Rule scope under 50.65(b)(2)(iii) (for example, condensate and heater drain pumps, circulating water pump motors, cooling tower fans) |
| Users / operators | M&D center engineers and analysts; station system engineers; Maintenance Rule Coordinators; SL-1 client engineers for their own plants |
| Affected people | Indirectly: plant workers and the public if a missed failure leads to a transient. No decisions about individuals |
| Data | Inputs: plant process data from the historian replicas (Stations 1 to 3, received through the one-way devices); vibration and temperature from wireless sensors at Station 4 (suspended); WMS work history with technician names removed. Outputs: anomaly scores, fault class, remaining-useful-life estimate, advisory text. No personal information |
| Build or buy | Build: company models on Cloud provider B machine learning services, plus the M&D analytics vendor's anomaly service. The vendor has no security addendum or SOC report yet (POAM-016) |
| Not intended | Safety-related equipment; any write to plant systems; changing or deferring preventive maintenance tasks, surveillance intervals, or Maintenance Rule goals; evaluating technician performance. Enabling any of these requires re-assessment |

### 7.2 Risk tier
High (section 4), with these conditions: advisory only; a person decides every action; Station 4 stays suspended until its data path is analyzed and approved. **Escalation triggers** (re-assess before use): any automatic work order creation without engineer review; any use on safety-related equipment; any use of output to extend preventive maintenance intervals; any new sensor path near plant equipment.

### 7.3 MEASURE (fleet data, 2026-01-01 to 2026-06-30)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Precision (confirmed advisories / all advisories) of at least 60%; recall on known degradation events of at least 80%; median lead time of at least 14 days | 1,240 advisories, 843 confirmed (68%); 37 of 43 known events caught (86%); median lead time 21 days | Yes (fleet level only) |
| Safe | No preventive maintenance task or Maintenance Rule goal changed because of model output; every missed event reviewed | 0 changes; 6 missed events reviewed, none caused a power change (one condensate pump bearing at Station 3 led to a pump swap) | Yes |
| Secure and resilient | Plant data only from the business side of the one-way devices; no write path; 73.54(b)(1) analysis for any new sensor path; vendor assurance | Stations 1 to 3 compliant. Station 4 gateways installed without analysis, with default passwords (POAM-011, POAM-018); M&D analytics vendor without a SOC report (POAM-016) | **No** |
| Accountable and transparent | Every advisory logged with the engineer's disposition in the WMS; SL-1 clients told advisories are model-generated | 1,240 of 1,240 logged; client agreements disclose model use | Yes |
| Explainable and interpretable | Each advisory shows which signals and features drove it | Available in the M&D platform | Yes |
| Privacy-enhanced | No personal information in model inputs; technician names removed from work history | Confirmed by data review | Yes |
| Fair, with harmful bias managed | Performance by station, equipment class, Maintenance Rule scope, plant type, and operating mode (section 6) | Not yet tested | **No** (gap, POAM-020) |

### 7.4 MANAGE
- **Human in the loop:** an M&D engineer reviews every advisory before it reaches a station; the system engineer decides whether to write a work request; the work request goes through normal work management, including the 50.65(a)(4) risk assessment before the maintenance is performed. Engineers can dismiss an advisory with a reason, which feeds retraining.
- **Station 4:** advisories suspended; the wireless sensor gateways are to be disconnected from the business network by 2026-10-15 and stay off until the 73.54(b)(1) analysis and design change review are complete (POAM-018 by 2026-12-31). Any replacement design must send data outbound only and have no path toward plant control systems.
- **Monitoring:** quarterly precision, recall, and lead time by station and equipment class (after section 6 is complete); a missed-event review for every corrective maintenance failure on monitored equipment; drift alerts on input data distributions; sensor data completeness by station.
- **Incidents:** a model or data compromise is a cyber incident under P08 (the M&D platform is SYS-12); a missed failure that causes a plant transient goes into the station corrective action program and is reviewed by the committee.
- **Decommissioning:** stop advisories for a station or equipment class that fails a section 6 threshold twice in a row; retire the tool if the vendor changes data-use terms or if the Station 4 data path cannot be approved.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case has quarterly performance metrics reported to the committee (inventory column `monitoring`); drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, uneven performance, data misuse, prohibited input) are logged as SOC events or condition reports and follow P08 where security or personal information is involved.
- **Third parties:** AI vendors are tiered in the vendor program; contracts require no training on company data, notice of material model changes, and breach notice terms. Vendor feature releases are screened for new AI features before deployment.
- **Generative AI (AI 600-1):** for AI-002, AI-004, AI-008, and AI-010, the committee checks confabulation (sampled output review), information security (prompt injection and data leakage tests), and intellectual property and export control (prohibited input enforcement).
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice, change data-use terms, or lose their business owner; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the AI governance committee's recommendation of 2026-08-19:
1. **AI-001:** approved to continue with conditions at Stations 1 to 3 and for SL-1 clients: station and equipment-class testing (section 6) by 2027-01-31; Station 4 suspended until POAM-018 closes; M&D analytics vendor addendum and assurance (POAM-016).
2. **AI-004:** pilot continues at Station 1 with committee-first screening; expansion requires 6 months of agreement data and a new committee vote.
3. **AI-005, AI-009, AI-012:** may continue in current scope until committee review by 2026-11-30; no expansion. AI-005 stays in the test environment and may not touch surveillance scheduling.
4. **AI-011:** ranking stays disabled until committee review and an adverse impact analysis are complete.
5. **Intake:** the GRC team screens every vendor release note for AI features starting 2026-10-01.

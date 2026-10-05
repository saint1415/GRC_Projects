# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Water Utility, Infrastructure Construction, Environmental Services, corporate) |
| Tier / Vertical | Multi-Sector / Water and Wastewater Systems |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the rules that apply to each division's use cases, with the water-quality anomaly detection model (AI-001) as the priority use case |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1) for AI-004, AI-005, and AI-009, and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 1 High, 7 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber, operational, and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group OT Security Director, Group Chief Privacy Officer, Group General Counsel, the Water Utility VP of Water Quality and Compliance, the Construction safety director, and the Environmental Services remote monitoring general manager. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO and Group OT Security Director | AI security standard: data leakage, prompt injection for generative tools, integrity of model inputs from OT |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026, under POL-01 4.12)
1. **Register before use.** Every AI use case that supports operational decisions (treatment, pumping, compliance data), client deliverables, customer interactions, or decisions about workers is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: the council approves; a pre-deployment impact assessment and validation are required; monitoring is reported quarterly. Any AI that "can affect physical safety or critical infrastructure operations" is High, even when advisory.
3. **Advisory in OT.** No AI may write setpoints, change modes, or acknowledge alarms on any SCADA or plant control system. AI output reaches operators as information only.
4. **Data rules.** No CUI, FCI, RRA or ERP content, SCADA diagrams, or client data in an AI tool unless the council has approved that tool for that data class (POL-04; POL-05 4.6).
5. **Change gate.** A material change (new model version, retraining on new data, new site, new decision role, new provider) triggers re-assessment before release, through the owning system's change process.
6. **Approved tools only** for workforce generative AI.

**Where the program fell short in 2026.** The standard was adopted after AI-001 went live. Operators at the 6 systems were told by memo to "act on model alerts", which conflicts with the rule that SCADA and hardwired alarms are the controls of record. The model's validation was not complete at launch, and retraining has no change control. Division uses (AI-005 to AI-007) were added to the inventory only during this assessment.

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Water-quality anomaly detection | Water Utility | High | In production at 6 systems with conditions |
| AI-002 | Main-break prediction for capital planning | Water Utility | Medium | In production |
| AI-003 | AMI leak and high-usage alerts to customers | Water Utility | Medium | In production |
| AI-004 | Customer service virtual agent (generative) | Water Utility | Medium | Pilot (one region) |
| AI-005 | Generative estimating and bid assistant | Construction | Medium | In production; CUI block due |
| AI-006 | Job-site safety video analytics | Construction | Medium | Pilot at 12 sites |
| AI-007 | Client anomaly alerts in SYS-E1 | Environmental Services | Medium | In production |
| AI-008 | Route optimization | Environmental Services | Low | In production |
| AI-009 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |

### 2.1 AI-001 water-quality anomaly detection: what it is and which rules apply
**Purpose and context.** The model runs on the group data platform (SYS-G3) and scores the historian replica's turbidity, chlorine and chloramine residual, pH, and flow signals every minute for the 6 largest systems (about 1.96 million people, including RS-1). When the score passes a threshold, it sends an alert to the ROC with the contributing signals. It was built in house from 2023 to 2026 historian data. It never writes to SCADA: historian replication is outbound-only from the OT DMZ (P04), and alerts return as notifications.

| Rule or source | What it requires | What it means for AI-001 |
|---|---|---|
| SDWA section 1433, RRA (42 U.S.C. 300i-2(a)(1)(A)(iii)) | Assess the monitoring practices of the system | AI-001 is now part of the monitoring practices of 6 systems and must be described in their RRAs, including its limits |
| SDWA section 1433, ERP (300i-2(b)(4)) | Strategies to aid in detecting malevolent acts or natural hazards | AI-001 is a legitimate detection strategy, but the ERP must not depend on it alone; the hardwired alarms and sampling stay primary |
| 40 CFR 141.202 | Tier 1 notice within 24 hours after the system learns of a qualifying situation | A model alert does not decide whether a Tier 1 situation exists; the VP of Water Quality and Compliance does, on sampling and process evidence. When a confirmed alert reveals a real excursion, the learning time is recorded from the alert |
| State operator certification programs (generic) | Licensed operators are responsible for process decisions | The approved-use rule must keep decisions with licensed operators |
| NIST SP 800-82 Rev. 3 | OT security and safety | The model's input data can be spoofed by an attacker who controls a PLC or the historian; it is not an independent safety layer |
| Sector AI rules | None identified for water systems in the vertical profile | The group standard and the AI RMF are the governing documents |

### 2.2 Other division use cases
| Use case | Rule or commitment | Implication |
|---|---|---|
| AI-004 customer virtual agent | State utility commission billing and disconnection rules (generic); FTC Act Section 5 | The agent may explain bills and take requests but may not grant or deny payment arrangements or affect disconnections; customers must be told they are using AI and can reach a person. Generative risks (AI 600-1): confabulated tariff or fee answers |
| AI-005 estimating assistant | DFARS 252.204-7012; NIST SP 800-171 3.1.3 | CUI must never enter the tool. A block on CUI-marked files is due 2026-12-31 (P01 CN-010) |
| AI-006 video analytics | State employee monitoring and recording laws (generic); Colorado SB26-189 (effective 2027-01-01) covers employment decisions | Tier stays Medium only while outputs are used for safety coaching and never as the basis for discipline without human review. Using it in employment decisions would make it High under the rubric and could bring Colorado duties for Colorado workers. The law's status is unsettled (federal preemption efforts; see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`) |
| AI-007 client alerts | Client contracts; SOC 2 commitments (P09 CC3.4, CC8.1, PI1.1) | The feature must be in the system description and covered by processing commitments; clients need accuracy information |
| AI-009 enterprise assistant | POL-05 4.6 | Data rules enforced by tenant configuration and labels |

## 3. Risk tiers (repository rubric)
- **High:** AI-001. It does not make decisions, but it "can affect physical safety or critical infrastructure operations": operators were told to act on it, and a missed or false alert can shape how a treatment excursion is handled.
- **Medium:** AI-002 (influences capital decisions), AI-003 and AI-004 (interact directly with customers), AI-005 (influences bids; data leakage risk), AI-006 (affects workers; human decides), AI-007 (client-facing; human reviews), AI-009 (broad workforce use with leakage risk).
- **Low:** AI-008 (internal route optimization; dispatchers decide).

**Re-tier triggers:** any AI-001 connection that could write to SCADA (prohibited; would require a new assessment and board risk committee approval); using AI-006 output in discipline (to High); letting AI-004 decide payment arrangements or disconnections (to High); offering AI-007 alerts as a basis for client compliance decisions without operator review (to High).

## 4. MEASURE
Results are from monitoring and replay tests between 2026-03 and 2026-08.

### 4.1 AI-001 water-quality anomaly detection
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Replay of 41 labeled excursions from 2023 to 2026 historian data (including 6 simulated setpoint-tampering events): share detected within 10 minutes (target 95%) | 37 of 41 (90%) | **No** |
| Valid and reliable | Alerts per system per day (target 3 or fewer, to avoid alarm fatigue) | 14 at go-live; 6 in 2026-08 | **No** |
| Safe (automation bias) | Operator logs: cases where grab sampling was delayed waiting for model confirmation (target 0) | 3 cases | **No.** The memo telling operators to "act on alerts" is withdrawn |
| Secure and resilient | Model inputs protected against spoofing; retraining under change control | Inputs come from the historian replica, which an attacker controlling a PLC could falsify; no retraining change control | **Partial.** Keep hardwired alarms primary; add change control |
| Explainable and interpretable | Alerts show contributing signals and trend plots | In place | Yes |
| Accountable and transparent | Named owner; approved-use rule; RRA and ERP describe the model and its limits | Owner named; no approved-use rule; RRAs silent | **No** |
| Fair, with harmful bias managed | Detection rate parity across plant types, so that communities served by groundwater plants get the same protection as those served by surface water plants (flag a gap of more than 5 points) | Surface water plants 94%; groundwater plants 83% (fewer labeled events) | **Flagged.** More labeled groundwater events and per-plant thresholds |
| Privacy-enhanced | No personal data used | Confirmed | Yes |

**Incident check (P08 exercise).** In the HMI compromise scenario, AI-001 flagged the rising pH 5 minutes before the hardwired alarm. That is useful, and it is also the reason over-reliance is dangerous: an attacker who also falsified historian values would have blinded it, but not the hardwired alarm.

### 4.2 Other use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-004 virtual agent (AI 600-1 confabulation) | Answers checked against tariffs (200 sampled conversations; target 0 wrong fee or policy statements) | 4 wrong statements about late fees | **No.** Restrict to retrieved tariff text before expanding |
| AI-004 virtual agent | AI disclosure and hand-off to a person available in every session | In place | Yes |
| AI-005 estimating assistant (AI 600-1 data privacy) | Files with CUI markings uploaded (target 0) | 2 uploads found in tenant logs | **No.** CUI block due 2026-12-31 |
| AI-006 video analytics | Worker notice posted at every pilot site; human review before any action | Notice at 9 of 12 sites; no discipline cases yet | **No** (notice) |
| AI-007 client alerts | Share of forwarded alerts that clients confirmed as real (target 80%) | 71% | **No.** Tune and report to clients quarterly |
| AI-009 enterprise assistant | Prohibited data classes detected by labels (target 0) | 0 in pilot | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** alerts are advisory. On an alert, the operator checks SCADA trends and the hardwired panel and takes a grab sample within 30 minutes; any control action is based on SCADA, hardwired alarms, and sample results. The model has no path to write to SCADA.
- **AI-004:** discloses it is AI; cannot decide payment arrangements or disconnections; transfers to a person on request or when the customer mentions a medical or safety need.
- **AI-006:** alerts go to superintendents for safety coaching; no discipline without human review of the footage and the worker's account.
- **AI-007:** monitoring operators review every model alert before it reaches a client.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-07, WU-015, CN-010, CN-013, ES-010.

**Incident handling:** AI failures that affect water safety, client compliance data, or worker treatment follow P08 and POL-03. A suspected manipulation of AI-001 inputs is treated as an OT incident.

**Decommissioning:** each use case has an off switch and a fallback already covered by the BIA (P05 BP-W10 for AI-001: operators rely on SCADA and hardwired alarms).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 anomaly detection | **Continue with conditions** (council, 2026-08-27; board risk committee informed 2026-09-15) | Withdraw the "act on alerts" memo and issue an approved-use rule by 2026-11-15; validation report against labeled events with a 95% detection target and 3 or fewer alerts per day by 2026-12-31; per-plant thresholds and more groundwater training data; retraining through the data platform change process; describe the model and its limits in the 6 systems' RRAs and ERPs at their next update; no expansion to other systems until all are met (POAM-028) |
| AI-004 virtual agent | **Continue pilot; no expansion** | Answers restricted to retrieved tariff text; monthly accuracy sample of 200 conversations with 0 wrong fee statements before expansion |
| AI-005 estimating assistant | **Continue** | CUI-marked file block by 2026-12-31; tenant retention terms confirmed |
| AI-006 video analytics | **Continue pilot** | Notice at every site by 2026-10-31; written rule against discipline without human review by 2026-12-31; re-tier review before any expansion |
| AI-007 client alerts | **Continue** | Add to the SYS-E1 system description; quarterly accuracy report to clients from 2027-03-31; security review in the release pipeline (P09 CC8.1) |
| AI-002, AI-003, AI-008, AI-009 | **Approved** | Standard monitoring; AI-008 hazmat route views restricted (POAM-026); AI-009 data labels enforced |

# AI Governance Risk Assessment: Enterprise AI Portfolio and Predictive Maintenance for Well Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded independent crude oil producer; Permian, Mid-Continent, and Florida) |
| Tier / Vertical | Enterprise / Mining, Quarrying, and Oil and Gas Extraction |
| Scope | Enterprise AI portfolio (11 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the predictive maintenance model for well equipment, in section 6 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-008 and AI-010; repository risk tier rubric |
| Assessor / date | AI council (chaired by the Vice President, Data and Analytics), meeting of 2026-08-19; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 8) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 11 |
| Risk tier | High 2, Medium 6, Low 3 |
| Status | In production 9, Pilot 1, Suspended 1 |
| Council review complete | 7 of 11 |
| Not yet reviewed | 4: AI-006, AI-008, AI-009, AI-011 (all due 2026-12-31, POAM-020) |
| Use cases with any write path to OT | 0 (one closed-loop request, AI-005, refused) |
| Use cases making decisions about people | 1 (AI-009, suspended) |

**Main findings:** the predictive maintenance model (AI-001) was expanded across the Permian in May 2026 before its well group review was repeated, and the repeat review now shows one under-served group. A proposal to let the production optimization model (AI-005) write setpoints directly was refused until a safety case exists. Four use cases entered through vendor feature releases without council review, including the telematics driver ranking feature (AI-009), which is switched off.

## 2. GOVERN: AI council operating model
**Charter.** The AI council was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly.

**Members:** Vice President, Data and Analytics (chair); Vice President, Operations Technology and Automation; Director of OT Security; CISO; Chief Compliance Officer; Privacy Counsel; General Counsel's delegate; Chief Human Resources Officer (for workforce tools); Vice President, Health, Safety, and Environment; a regional operations leader; and the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Council vote, then the executive risk committee; for any OT effect, also the Chief Operating Officer | Safety case and OT change review for anything touching field equipment; impact assessment; bias or representativeness testing; human review design; notice to affected people; monitoring plan |
| Medium | Council vote | Human oversight design; output quality monitoring; representativeness testing where outputs steer field work; AI disclosure where people interact with it; security review |
| Low | Council chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**OT rule.** No AI system may write to SCADA, controllers, or drives, or create work orders automatically, without a High-tier review, a safety case signed by the Vice President, Operations Technology and Automation and the Vice President, HSE, and the OT change board's approval (STD-01.8). Models read OT data only from the historian replica, never from the SCADA network.

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.7; STD-05.3). Procurement and IT change management now block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.7 (no Restricted data in AI tools without council approval and no-training terms); POL-05 4.7 (approved tools only); POL-01 4.8 (vendor assessment and contract terms before data is shared); STD-05.3 (approved AI tools list).

**Cadence:** monthly council meetings; quarterly monitoring review for every High-tier and every Medium-tier use case that steers field work; annual re-review of every use case.

**Why 4 use cases lack review.** AI-006, AI-008, and AI-011 arrived as features in vendor products before the intake block existed (July 2026), and AI-009 is a telematics vendor feature found during the P01 analysis. All four have review dates (section 8).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules (oil and gas) | No | None identified for this vertical (`02_industry-rules/mining-oil-gas/overlay.md`) |
| NIST SP 800-82 Rev. 3 and the company's OT change control (N21-BM) | Yes, for AI-001 and AI-005 | Any AI output that changes how field equipment runs goes through the OT change process; models read only from the historian replica |
| Texas Responsible AI Governance Act (HB 149, effective 2026-01-01) | Yes, the company does business in Texas | Its prohibitions are intent-based (for example AI developed with intent to unlawfully discriminate); its disclosure duties apply to government agencies and health care providers. None of the use cases is built for a prohibited purpose |
| Colorado SB26-189 (effective 2027-01-01) | No | The company has no operations in Colorado, and no use case materially influences a consequential decision about a consumer |
| Federal equal employment opportunity laws | Yes, for AI-009 | Counsel reviews adverse impact before the ranking feature could be re-enabled |
| State breach laws (Fla. Stat. 501.171 worked example) | Yes, for AI-008, AI-009, AI-010 | Owner data, employee geolocation, or Restricted data could be exposed through these tools |
| FTC Act Section 5 | Indirectly | Accuracy of what the owner chatbot tells owners (AI-008) and of any claims the company makes about its models |
| SEC reserves disclosure rules | Context only, for AI-002 | The rules govern the reserves estimates, which engineers and the independent reserves engineer own; the model is one input |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Council review | OT write path |
|---|---|---|---|---|---|
| AI-001 | Predictive maintenance model for well equipment | Medium | In production (about 5,200 wells: Permian 3,900 after the 2026-05 expansion; legacy Mid-Continent 1,300); AQ-MC and Florida excluded | Reviewed 2025-11-12; re-reviewed 2026-08-19 (conditional) | None (read-only from the historian replica) |
| AI-002 | Production forecasting and decline curve model used as one input to reserves estimates | Medium | In production | Reviewed 2026-02-18 | None |
| AI-003 | Seismic interpretation assistant (fault and horizon picking) | Low | In production | Reviewed 2025-12-10 | None |
| AI-004 | Drilling optimization advisory (weight on bit and rotary speed recommendations) | Medium | In production (14 rigs) | Reviewed 2026-01-21 | None to company OT; rig control stays with the driller |
| AI-005 | Production optimization model that proposes ESP frequency and gas lift injection setpoints; a proposal to let it write setpoints (closed loop) is pending | High | Pilot (advisory mode on 120 Permian wells) | Reviewed 2026-08-19; closed-loop request refused until a safety case and High-tier review exist (R-040) | None; closed loop not approved |
| AI-006 | Methane and leak detection analytics on optical gas imaging and continuous sensors at facilities | Medium | In production (46 compressor stations) | Not reviewed (intake 2026-07; review due 2026-12-31, POAM-020) | None |
| AI-007 | Invoice capture and joint interest billing coding suggestions | Low | In production | Reviewed 2025-10-08 | None |
| AI-008 | Owner relations chatbot on the SL-1 portal (balances, payment dates, how-to questions) | Medium | In production (switched on in a vendor release) | Not reviewed (review due 2026-12-31, POAM-020) | None |
| AI-009 | Telematics driver safety scoring and ranking | High | Suspended (ranking disabled, R-043) | Not reviewed (review and adverse impact analysis due 2026-12-31, POAM-020) | None |
| AI-010 | Enterprise generative AI assistant for workforce productivity | Medium | In production (about 6,000 users) | Reviewed 2026-03-11 | None |
| AI-011 | SOC alert triage assistant | Low | In production | Not reviewed (review due 2026-12-31, POAM-020) | None (cannot change OT or firewall rules) |

**Tiering notes:** AI-005 is High even in advisory mode because its outputs are setpoints for field equipment, and a closed-loop version could affect safety and critical infrastructure operations directly. AI-009 is High because driver scores could become a substantial factor in employment decisions. AI-001 is Medium, not High, because it only reorders a maintenance queue an engineer approves; it cannot control equipment, and a missed failure leaves the same protections in place as having no model (hardwired safety shutdowns and alarms). AI-004 stays Medium because the driller and independent well control equipment stand between the recommendation and the rig.

## 5. MEASURE and MANAGE: portfolio controls
- **Monitoring:** each High-tier use case and each Medium-tier use case that steers field work (AI-001, AI-004, AI-005) has monthly performance metrics and a quarterly representativeness report (inventory column `monitoring`); threshold breaches trigger re-review.
- **Security:** models run on the Cloud B machine learning platform in their own account, with read-only access to the historian replica, no network route to the SCADA networks, and access through SSO with MFA (P04). Model files and training data stay in company storage.
- **Incident handling:** AI incidents (unsafe recommendation, bias finding, data misuse) are logged as SOC or HSE events and follow P08 where security or personal information is involved.
- **Third parties:** AI vendors are tiered in the vendor program; contracts require no training on company data, deletion at contract end, and notice of material model changes.
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice, change data-use terms, or are found used against an escalation trigger; the inventory records retirement.

## 6. Full assessment: AI-001 predictive maintenance model for well equipment
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Predict rod pump and ESP failures up to 30 days ahead so engineers can schedule workover rigs and pulling units to the wells most likely to fail, before production is lost |
| Users | About 45 production engineers in the Permian and legacy Mid-Continent; rig and pulling unit schedulers see the resulting work orders |
| Affected parties | Field operations (rig schedules, lease operator routes); royalty owners and partners indirectly (production). No decisions are made about individuals |
| Scale | About 5,200 wells: 1,500 Permian wells since 2024, 2,400 Permian wells added in May 2026, and 1,300 legacy Mid-Continent wells. AQ-MC (data in the seller's SCADA) and Florida (regional historian not replicated) are excluded |
| Data | Inputs: historian replica data (pump cards, motor current, runtime, pressures, rates) and work order history with technician names removed. **No personal information.** Vehicle telematics were considered and excluded |
| Build or buy | Built by the company's data science team on the Cloud B machine learning platform; the company owns the model and code |
| Connection to OT | **Read-only and indirect.** The model reads the historian replica, which receives data one way through the OT DMZ. It has no route to the SCADA networks and cannot write setpoints, start or stop wells, or create work orders |
| Not intended | Controlling equipment; deciding shut-ins; deferring inspection of safety equipment (pressure relief valves, gas detectors, emergency shutdowns); evaluating lease operators or crews |

### 6.2 Risk tier and escalation triggers
**Tier: Medium** (section 4). Re-tier to High and re-assess before any of these:
- any automatic action on equipment, SCADA, or the ERP (setpoints, start or stop, automatic work orders)
- use to defer or skip inspection of safety-critical equipment
- use of outputs to rank, evaluate, or discipline lease operators or crews (an employment decision)
- adding personal information such as vehicle telematics

### 6.3 MEASURE (June to August 2026, all 5,200 wells)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Recall (failures flagged at least 3 days ahead) at least 60%; precision (alerts that were real failures) at least 35% | 412 failures; 272 flagged ahead (recall 66%). 664 alerts; 272 real (precision 41%) | Yes, overall |
| Safe | No write path to OT or the ERP; alerts never used to defer safety equipment inspections | Network rule review (P04): the machine learning account has no route to the SCADA networks; inspection schedules unchanged | Yes |
| Secure and resilient | Access through SSO with MFA; model and data in company storage; change control for model releases | In place; model releases go through the CI/CD pipeline with approvals | Yes |
| Accountable and transparent | Named owner; model card with purpose, data, limits, and version; engineers told what the model does not see | Owner named; model card current for version 3.2 | Yes |
| Explainable and interpretable | Each alert shows the top contributing signals (for example pump card shape change, rising motor current) | Available in the alert view | Yes |
| Privacy-enhanced | No personal information in training or scoring data | Technician names removed; telematics excluded | Yes |
| Fair, with harmful bias managed | Compare recall and false alert rate across well groups; flag a group if its recall is more than 15 points below overall or its false alert rate more than 10 points above | Repeat review (August 2026) flags Permian ESP wells on cellular backhaul: recall 47% (36 of 77) against 66% overall | **No.** Group flagged |

**Representativeness and bias review.** In this use case, harmful bias means the model systematically serves some wells worse than others. Because rig time is limited, under-served wells fail more often and wait longer for repair, which means more deferred production and more work-over trips to the same sites.
- **Groups compared:** operating area (Permian core, Permian expansion area, legacy Mid-Continent); lift type (rod pump, ESP); communications path and polling rate (private LTE polled every minute, licensed radio every 2 minutes, cellular every 15 minutes); well age; sour versus sweet service.
- **What changed with the expansion:** the 2,400 wells added in May 2026 are mostly on cellular backhaul. The model was trained mainly on private LTE wells with one-minute data. The pre-expansion review in 2025 did not include cellular ESP wells because there were almost none in the training set; the review was not repeated before go-live (R-041, POAM-020).
- **Results by group:** Permian rod pumps on private LTE 71%; Permian ESPs on private LTE 68%; legacy Mid-Continent rod pumps on radio 61%; Permian ESPs on cellular 47% (flagged); Permian rod pumps on cellular 58% (watched, within threshold).
- **Workforce check:** the quarterly review confirms that no report ranks routes or people by model alerts.

### 6.4 MANAGE
- **Human in the loop:** the model produces a ranked alert list only. An engineer reviews each alert and its contributing signals and decides whether to raise a work order; dismissals carry a reason and are reviewed monthly. Rig schedules are still set by schedulers and engineers.
- **Flagged group:** Permian ESP wells on cellular backhaul move to **shadow mode** (alerts recorded but not used for scheduling) until retraining with their data brings recall within the threshold; engineers schedule those wells by the prior method meanwhile. The private APN migration (POAM-013) and polling changes will improve their data, so the group is re-tested after each change.
- **Monitoring:** monthly recall and precision; quarterly well group report to the council; data drift check when the historian replica, polling rates, or the well set changes (including the AQ-MC migration in 2027).
- **Security:** any proposal to connect the model to the SCADA networks or to let it create work orders is out of scope and requires a High-tier review.
- **Incident handling:** a security incident affecting the machine learning platform or the historian replica follows P08. A model failure that contributes to a significant production loss is reviewed by the owner and recorded in the risk register.
- **Decommissioning:** stop and archive if overall recall falls below 50% for two consecutive months, or if the model is found used against an escalation trigger.

## 7. Other portfolio actions
- **AI-005 production optimization:** stays advisory. A closed-loop request returns to the council only with a safety case, an OT change board design review, rate-of-change and range limits enforced in the controllers (not in the model), and a High-tier assessment.
- **AI-009 telematics driver scoring:** ranking stays disabled until council review and an adverse impact analysis by counsel are complete.
- **AI-006, AI-008, AI-011:** may continue in current scope until council review; no expansion.
- **AI-010 enterprise assistant:** unapproved generative AI domains are blocked enterprise-wide by 2026-12-31 (R-039).

## 8. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the council's recommendation of 2026-08-19:
1. **AI-001:** approved to continue with conditions: repeat well group review documented by 2026-10-31 (POAM-020); Permian ESP wells on cellular backhaul in shadow mode until they pass the threshold; AQ-MC and Florida stay excluded until their data reaches the historian replica and a group review is done; any expansion requires a group review before go-live.
2. **AI-005:** advisory pilot may continue on 120 Permian wells; closed-loop write refused (R-040).
3. **AI-006, AI-008, AI-011:** council reviews by 2026-12-31 (POAM-020).
4. **AI-009:** ranking disabled until review and adverse impact analysis by 2026-12-31 (R-043).
5. **Inventory:** the intake block stays in procurement and change management; the GRC team reports inventory completeness to the council monthly.

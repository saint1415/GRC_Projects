# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Transformer Manufacturing, Electric Utility, Grid Engineering, corporate) |
| Tier / Vertical | Multi-Sector / Critical Manufacturing (focus division: Transformer Manufacturing) |
| Scope | The group AI governance program (group standard, the division use-case inventory, and the rules that apply to each division), with the focus use case **demand forecasting and predictive maintenance** (AI-001 and AI-002), plus the FMS asset-health analytics (AI-003) and the Grid Engineering design assistant (AI-006) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-005, AI-006, and AI-008 |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 1 High, 7 Medium, 1 Low) |

**Why the registry default fits.** The registry use case for this vertical is "demand forecasting and predictive maintenance". At this size both are real and separate models (AI-001 and AI-002) that went live before the Group AI Standard (scenario gap 8), and the forecast now steers who gets scarce storm-restoration equipment, including the affiliated utility. That makes it the right focus.

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list each quarter |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group General Counsel, Group Chief Privacy Officer, Group OT security director, VP supply chain and demand planning, Electric Utility manager of load forecasting, Grid Engineering chief operating officer. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring and report metrics |
| Group CISO and Group OT security director | AI security: data paths from OT, model supply chain, prompt injection, leakage of designs, BCSI, and CEII |
| Group General Counsel | Customer and affiliate fairness of allocation decisions; claims made to customers |
| Group internal audit | Adds High-tier AI controls to the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-03, under POL-01 4.12)
1. **Register before use.** Every model that steers production, allocation, maintenance, grid operations, or engineering deliverables, and every generative AI tool, is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). The rubric's High tier includes AI that "can affect physical safety or critical infrastructure operations", which is the main route to High in this group, because no use case makes consequential decisions about individuals.
3. **Independent validation** before production for High-tier models, and at least every 2 years for Medium-tier models that feed operations.
4. **Change gate.** Retraining, new features, new data sources, or a new decision role trigger re-assessment and change control (POAM-019).
5. **OT data paths.** Models may read plant historian data only through the OT DMZ replica; no direct path from a plant network to the internet (Manufacturing supplement).
6. **Data rules.** No designs, BCSI, CEII, FCI, or signing material in third-party AI tools unless the tool is approved and its terms prohibit training on group data (POL-04 4.11; POL-05 4.8).

**Where the program fell short in 2026.** AI-001 and AI-002 went live in 2024 and 2025, before the standard. Neither was independently validated, AI-001 was retrained 4 times in early 2026 without change records, the storm-reserve allocation that AI-001 feeds has no written rule, and the AI-002 vendor connector at P8 sends historian data straight to the internet from a flat plant network (P01 GR-06, MF-012, MF-013, MF-014).

## 2. MAP (division use cases and the rules that apply)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Demand forecasting and storm-reserve allocation input | Transformer Manufacturing | High | In production; conditions set |
| AI-002 | Predictive maintenance of plant equipment | Transformer Manufacturing | Medium | In production at P1 to P7; P8 connector disabled |
| AI-003 | FMS transformer asset-health analytics | Transformer Manufacturing | Medium | In production (about 70 subscribers) |
| AI-004 | Load forecasting | Electric Utility | Medium | In production |
| AI-005 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |
| AI-006 | Generative AI design assistant | Grid Engineering | Medium | Pilot (120 engineers) |
| AI-007 | Weld and paint vision inspection | Transformer Manufacturing | Medium | In production at P4; P5 pilot |
| AI-008 | Coding assistant for TMU firmware | Transformer Manufacturing | Medium | Approved with conditions |
| AI-009 | Accounts payable invoice matching | Group | Low | In production |

### 2.1 The focus use case in context
| Item | AI-001 Demand forecasting | AI-002 Predictive maintenance |
|---|---|---|
| Purpose and intended use | Forecast orders by product family and region 1 to 18 months ahead to plan plant capacity, core steel purchases, and the number of storm-reserve production slots and spare units held from June to November | Predict failures of drying ovens, vacuum oil processing, winding machines, and test lab equipment so maintenance can be planned before a breakdown |
| Users / operators | Demand planners; the storm allocation committee | Maintenance planners and reliability engineers at P1 to P7 |
| Affected parties | About 700 utility customers, including the affiliated Electric Utility, whose storm restoration depends on reserved slots and spares | Plant workers (if a failure is missed on safety-relevant equipment); customers (if production stops) |
| Data | GEPS order history, customer forecasts, storm history, utility capital plans (Confidential) | Historian sensor tags and maintenance records (Internal) |
| Build or buy | Built in-house on the group data platform | Vendor models configured and trained on group data |
| Applicable rules | No AI-specific law. The customer supply agreements and the 2019 intercompany supply agreement govern allocation. Favoring the affiliate without a rule could breach customer terms and trust; it is a counsel review item, not a regulatory finding | No AI-specific law. The group OT security standard (SP 800-82 Rev. 3) governs the data path. Plant process safety controls stay independent of the model |

### 2.2 Rules that apply across the inventory
| Rule | Use cases | Implication |
|---|---|---|
| Consequential decisions about individuals (Colorado SB26-189, effective 2027-01-01; California CPPA ADMT rules; state AI employment laws) | None today | No use case makes or is a substantial factor in decisions about people. AI-005 is prohibited for HR decisions. If the applicant tracking system's AI ranking feature were ever enabled, it would be High (employment) and these laws would need review (see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`) |
| FTC Act Section 5 | AI-003, AI-005, AI-006 | Accuracy claims made to FMS subscribers must be substantiated; vendor claims checked before purchase. The FTC's July 2026 proposed AI accuracy policy statement is not final |
| Utility addenda secs. 4 and 5 | AI-008 | Generated code is part of firmware supplied to utilities; it must go through the same review, vulnerability disclosure, and signed build process |
| Client confidentiality and CIP-011-3 flow-down terms | AI-006 | No client BCSI or CEII in prompts; the model provider must not train on or retain project data |
| NERC CIP | AI-004 | The model is not a BES Cyber System and runs outside the TCC. Moving it into real-time operations would require a CIP-002 categorization review |
| SOC 2 commitments | AI-003 | Model changes are system changes for the FMS readiness (P09 CC3.4, CC8.1) |

## 3. Risk tiers (repository rubric)
- **High: AI-001.** The forecast is a substantial factor in how many storm-reserve slots and spare transformers are held and, in practice, in who receives them. That allocation affects how fast utilities restore the grid after a hurricane, which the rubric treats as affecting critical infrastructure operations.
- **Medium: AI-002, AI-003, AI-004, AI-005, AI-006, AI-007, AI-008.** Each influences business or engineering decisions, but a qualified person makes the final decision and an independent safeguard stays in place (scheduled maintenance and safety interlocks for AI-002, utility engineering review for AI-003, operator review for AI-004, engineer review and seal for AI-006, inspectors and routine tests for AI-007, code review and signing for AI-008).
- **Low: AI-009.**

**Re-tier triggers:** using AI-002 to defer or cancel scheduled maintenance (to High); subscribers automating actions on AI-003 alerts (to High); using AI-006 for protection settings calculations (to High; currently prohibited); moving AI-004 into real-time operations (to High, with a CIP-002 review).

## 4. MEASURE
Results are from monitoring, backtests, and reviews between 2026-05 and 2026-08.

### 4.1 AI-001 Demand forecasting
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Forecast error (mean absolute percentage error) at 6 months, by product family; targets 10% for distribution, 20% for power transformers | Distribution 9%; power transformers 22% | **Partial** (power transformers above target) |
| Valid and reliable (storm season) | Backtest of the 2024 and 2025 storm seasons: reserved pad-mount units against actual storm orders | 2025 season under-forecast by 31% in the two weeks after the September landfall | **No** |
| Accountable and transparent | Independent validation before production (Group AI Standard item 3) | Not done | **No** |
| Accountable and transparent | Change records for retraining (target: every release) | 4 retrainings between 2026-01 and 2026-07, none recorded; the change gate has applied since 2026-08 | **No** (POAM-019) |
| Fair, with harmful bias managed (allocation among customers) | Share of reserved storm slots given to each customer group compared with its share of contracted volume; flag a gap above 3 points without a documented reason | Affiliated Electric Utility: 41% of 2025 reserved distribution slots against a 35% share of contracted volume | **Flagged.** No written allocation rule explains it (POAM-021) |
| Secure and resilient | Model and data on the group data platform with group access controls; fallback if the GEPS is down | Access controls inherited and satisfied; no documented manual fallback for storm allocation | **Partial** |
| Explainable and interpretable | Planners can see the drivers of each forecast change | Driver report exists for distribution only | **Partial** |
| Privacy-enhanced | No personal information used | Confirmed | Yes |

### 4.2 AI-002 Predictive maintenance
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Recall on confirmed vacuum pump and drying oven failures, 2025-2026 (target 0.80) | 0.78 (39 of 50 failures flagged at least 72 hours ahead) | **Flagged** (just below target) |
| Valid and reliable | False alarms per plant per month (target 15 or fewer) | 12 | Yes |
| Safe | The model cannot defer or cancel scheduled preventive maintenance; safety interlocks independent | Confirmed in the work order system configuration and in 3 plant walkthroughs | Yes |
| Secure and resilient | Data path: historian replica in the OT DMZ only | P1 to P7 yes; **P8 connector sends tags from the flat plant network directly to the internet** | **No** (MF-014; POAM-007) |
| Accountable and transparent | Vendor contract terms: no training on group data for other customers; data return on exit | Signed | Yes |
| Explainable and interpretable | Top contributing sensors shown with each alert | In place | Yes |
| Fair, with harmful bias managed | Not applicable to individuals. Checked instead for uneven coverage across plants | P8 model trained on 4 months of data versus 3 years elsewhere | **Flagged** |
| Privacy-enhanced | No personal information | Confirmed | Yes |

### 4.3 Other Medium-tier use cases (summary)
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-003 FMS asset health | Alerts confirmed by utility dissolved gas analysis on 140 known fault cases (target recall 0.85) | 0.86 | Yes |
| AI-003 FMS asset health | Method documentation and change gate for subscribers | No method document; changes not gated until 2026-08 | **No** (P09 CC3.4, CC8.1) |
| AI-004 load forecast | Day-ahead error (target 3.5%); peak-day error (target 7%) | 2.8%; 6% | Yes |
| AI-006 design assistant (AI 600-1: data privacy, information integrity) | Prompts screened for BCSI and CEII; reviewer sign-off on every AI-assisted section | No prompt screening yet; sign-off in 18 of 20 sampled deliverables | **No** |
| AI-008 coding assistant (AI 600-1: information security) | Share of generated changes with peer review and static analysis | 100% through the pipeline | Yes |
| AI-007 vision inspection | Missed defects found at final inspection (target under 1 per 1,000 tanks) | 0.6 per 1,000 | Yes |

## 5. MANAGE
**Human-in-the-loop design (focus use case):**
- **AI-001:** planners review every forecast. Storm-reserve allocation is decided by the storm allocation committee under a **written allocation rule** (due 2026-12-31) that sets the slots per customer group from contract terms and documented need. The forecast sizes the reserve; it does not decide who gets it. The committee can override the forecast at any time and records why. Counsel reviews the rule because the affiliate is one of the customers.
- **AI-002:** maintenance planners decide every work order. The model may add or advance maintenance but may never defer or cancel scheduled preventive maintenance. Safety interlocks and operator procedures are independent of the model.

**Monitoring:** monthly metrics to the division owners (forecast error by family, storm-slot allocation shares, recall and false alarms by plant); quarterly High-tier report to the council and the board risk committee. Linked risks: P01 GR-06, MF-012, MF-013, MF-014, MF-015, EU-012, ES-004.

**Incident handling:** an AI failure that stops production, misallocates storm equipment, or exposes data follows P08 and POL-03. Compromise of the AI-002 data path is handled as an OT incident.

**Decommissioning and fallback:** each use case has an off switch and a fallback that the BIA covers (P05): planner judgment and last season's allocation table for AI-001, the scheduled preventive maintenance program for AI-002, utility engineering review for AI-003, and the prior forecasting method for AI-004.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 demand forecasting | **Continue with conditions** (council, 2026-08-27; board risk committee informed 2026-09-15) | Written storm allocation rule approved by the division president with counsel review by 2026-12-31; independent validation, including a storm-season backtest, by 2027-03-31 (POAM-021); all retraining through the change gate, in force since 2026-08 (POAM-019 closes when the first gated release is verified); until the rule is approved, the storm allocation committee records the reason for every allocation that departs from contract shares |
| AI-002 predictive maintenance | **Continue at P1 to P7; P8 connector disabled** | P8 vendor connector disabled by 2026-09-30 and reconnected only through the OT DMZ replica (POAM-007); retrain the P8 model when 12 months of data exist; recall review at the next quarterly report; change gate (POAM-019) |
| AI-003 FMS asset health | **Continue** | Method documentation for subscribers and change gate before the FMS Type 1 date (2027-03-31); decide on SOC 2 Processing Integrity before the first Type 2 period (P09) |
| AI-004 load forecast | **Continue** | Standard monitoring; CIP-002 review before any move into real-time operations |
| AI-005 enterprise assistant | **Continue pilot** | Prohibited for HR and other decisions about individuals; data loss prevention rules for designs, BCSI, and CEII before wider rollout |
| AI-006 design assistant | **Continue pilot; no expansion** | Prompt screening for BCSI and CEII and reviewer sign-off on every AI-assisted section by 2026-12-31; prohibited for protection settings |
| AI-007, AI-008, AI-009 | **Approved** | Standard monitoring; AI-008 output only through peer review and the signed build process |

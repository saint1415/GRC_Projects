# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Electric Utility, Gas Production, Engineering Services, corporate) |
| Tier / Vertical | Multi-Sector / Utilities |
| Scope | The group AI governance program (group standards, the division use-case inventory, and the rules that apply to each) and a full assessment of the focus use case, the **electric load-forecasting model** (AI-001). The two other High-tier use cases, OMS outage prediction (AI-003) and the Engineering Services design assistant (AI-006), get a shorter assessment |
| Framework | NIST AI RMF 1.0 (AI 100-1), the AI RMF Playbook, and the Generative AI Profile (AI 600-1) for AI-006 and AI-008. NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07; the council will review the profile when it is published |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-26; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 3 High, 5 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber, operational, and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group General Counsel, Group Chief Privacy Officer, Group OT security director, Electric Utility vice president of system planning, Gas Production vice president of operations, Engineering Services chief operating officer. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (data leakage, prompt injection, model supply chain) |
| Group General Counsel | Client and vendor terms for AI; regulatory review |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-03, under POL-01 4.12)
1. **Register before use.** Every AI use case that supports grid operations, power purchasing, field operations, or client deliverables, or that processes Restricted or client data, is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). In this group, "can affect physical safety or critical infrastructure operations" is the usual reason for High. High tier: council approval, pre-deployment validation, an impact assessment, and quarterly monitoring reports.
3. **Validation independent of the builder** for High-tier models, before production and after each material change.
4. **Data rules.** Restricted data, CEII, BCSI, and client documents go only to tools approved for that data, and client data only with client consent (POL-04 4.7; POL-05 4.5).
5. **Humans decide.** No AI output may operate grid or field devices, place purchases, or release client deliverables without a named person's approval.
6. **Change gate.** A new model, a new data source, or a new decision role triggers re-assessment before release.
7. **Employment decisions.** No AI use in hiring, promotion, or discipline without legal review, because state automated decision laws (for example Colorado SB26-189, effective 2027-01-01) may apply where staff work.

**Where the program fell short in 2026.** The standard was adopted after two High-tier use cases were already live. The load-forecasting model was replaced in 2025 without independent validation (scenario gap 8), and the Engineering Services design assistant pilot started with client documents before any review (gap 5). Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Electric load-forecasting model | Electric Utility | High | In production; continue with conditions |
| AI-002 | AMI tamper and theft analytics | Electric Utility | Medium | In production |
| AI-003 | OMS outage prediction | Electric Utility | High | In production |
| AI-004 | Vegetation risk model | Electric Utility | Medium | In production |
| AI-005 | Gas production forecasting and compressor predictive maintenance | Gas Production | Medium | In production |
| AI-006 | Generative AI design assistant | Engineering Services | High | Pilot; client CEII and BCSI blocked |
| AI-007 | Proposal writing assistant | Engineering Services | Low | Approved |
| AI-008 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |
| AI-009 | SOC alert triage assistant | Group | Medium | In production |

### 2.1 Electric load-forecasting model (AI-001)
**Purpose and use.** Produces hourly day-ahead and 7-day forecasts of system and substation load. Three decisions rely on it: day-ahead wholesale purchases (about 30% of the Electric Utility's energy is bought day ahead), peak-day operating plans at the DCC (conservation voltage reduction, feeder transfers, demand response calls), and storm staffing levels.

**Model.** A gradient-boosted ensemble built in-house on the group data platform (SYS-E6), replacing a 2019 regression model in 2025. Inputs: substation load history, AMI interval data aggregated to substation level, commercial weather forecasts, calendar, and rooftop solar estimates. No individual customer data reaches the model.

**People affected.** No decision about any individual. Customers are affected indirectly: an under-forecast peak can force emergency purchases or load management; an over-forecast raises costs that customers may ultimately pay.

**Applicable rules.**
| Rule or guidance | Implication |
|---|---|
| No AI-specific federal or state rule | None found for utility load forecasting |
| NERC CIP | Not applicable: SYS-E6 is not a BES Cyber System and is outside the TCC ESPs. The TCC's operations planning uses the RC's and BA's forecasts, not SYS-E6 |
| NERC EOP and reliability standards | Not directly: the forecast informs distribution operating plans, not TOP real-time assessments. If the TCC ever adopts SYS-E6 output for TOP planning, re-assess |
| State utility regulation (general) | Costs of purchases may be examined in state cost recovery proceedings, so forecast quality and governance should be documented |
| Wholesale purchase agreements | Scheduling deadlines and imbalance charges set the cost of error |
| NIST AI RMF 1.0; Critical Infrastructure Profile concept note (2026-04-07) | Voluntary framework used for this assessment |

### 2.2 OMS outage prediction (AI-003) and design assistant (AI-006): rules that differ
| Use case | Rule or commitment | Implication |
|---|---|---|
| AI-003 | DOP controls (P02); POL-02 4.11 | Predictions never operate devices; dispatchers confirm before crews roll. Storm-season accuracy matters most, so review happens after each named storm |
| AI-006 | Client contracts (confidentiality, CEII, CIP-011-3 flow-down) | Client documents may go to the tool only with client consent; CEII and BCSI uploads blocked from 2026-10-15 (POAM-022) |
| AI-006 | 18 CFR 388.113 | CEII obtained from FERC under a client's authorization must not be passed to third parties beyond that authorization |
| AI-006 | State engineering licensure (not assessed here) | A licensed engineer remains in responsible charge of sealed work; AI output is a draft only |
| AI-006 | SOC 2 commitments (P09) | The AI service is a subservice organization if the pilot becomes a production service (CC9.2) |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 and AI-003 (can affect critical infrastructure operations and crew safety through operating plans and dispatch), AI-006 (can affect clients' grid protection through design and settings work).
- **Medium:** AI-002, AI-004, AI-005, AI-008, AI-009. They influence decisions, but a person makes every decision, and they do not operate equipment.
- **Low:** AI-007.

**Re-tier triggers:** letting any model operate devices or place purchases automatically (to High with a full impact assessment); using AI-008 for employment or client deliverables (re-assess); using AI-001 output in TOP operations planning (re-assess against NERC standards).

## 4. MEASURE
Results are from monitoring and the June to August 2026 review of AI-001.

### 4.1 Load-forecasting model (AI-001)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Day-ahead mean absolute percentage error (MAPE), June to August 2026; target 3.0% or less | 3.4% | **No** |
| Valid and reliable (peaks) | Error on the 10 highest-load days; target 4.0% or less | 5.8% (under-forecast on 3 of the hottest days) | **No** |
| Validated independently | Review by someone other than the builder before production (Group AI Standard item 3) | Not done for the 2025 model | **No** (POAM-024) |
| Safe | Peak-day plans reviewed by the DCC before use; fallback similar-day method available | In place | Yes |
| Secure and resilient | Input checks on weather and AMI feeds; two weather feed outages in 2026 produced flat-line forecasts that were caught only by analysts | No automated input checks | **No** |
| Secure and resilient | Workspace access limited to the forecasting team; model and code in the group repository | In place | Yes |
| Accountable and transparent | Model documentation (purpose, data, limits, owner) | Partial: no documented limits for extreme heat | **Partial** |
| Explainable and interpretable | Feature importance available to analysts for every forecast | In place | Yes |
| Fair, with harmful bias managed | No individual decisions; checked whether error is concentrated by region, since regional under-forecasts drive feeder transfers and voltage reduction in those areas. Flag if any region's MAPE exceeds 1.5 times the system MAPE | Coastal region 6.1% vs system 3.4% (1.8 times), linked to fast rooftop solar growth | **Flagged.** Add regional solar estimates; review by 2026-11-30 |
| Drift monitored | Monthly comparison of error and input distributions with the validation baseline | Not monitored | **No** (POAM-024) |

### 4.2 Other High-tier use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-003 OMS outage prediction | Share of predicted device outages confirmed by crews (storm of 2026-08); target 85% | 81% | **Flagged.** Review device model data |
| AI-006 design assistant | Client documents uploaded without consent (pilot audit) | 46 documents from 9 projects, including CEII | **No** (POAM-022) |
| AI-006 design assistant (AI 600-1: confabulation) | Engineer review of 60 AI-checked settings calculations: errors the tool missed or introduced | 3 of 60 with a wrong reference to a client standard; all caught in review | **Partial.** Review attestation required |
| AI-006 design assistant (AI 600-1: information security) | Prompt injection test with crafted client documents | Not done | **No** |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** analysts review every forecast; the power supply manager approves purchases; the DCC approves peak-day operating plans. The fallback similar-day method is run in parallel on forecast peak days.
- **AI-003:** dispatchers confirm each prediction; predictions never operate devices.
- **AI-006:** a licensed engineer reviews and attests every AI-assisted deliverable; the tool cannot send files to clients.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-04, EU-012, and ES-008.

**Incident handling:** an AI failure that affects grid or field operations, exposes client data, or breaks a client commitment is an incident under POL-03 and P08. A forecast failure on a peak day is reported to the power supply manager and the DCC at once.

**Decommissioning:** each use case has an off switch and a fallback already covered by the BIA (P05): the similar-day forecast for AI-001, manual outage analysis for AI-003, and standard engineering review for AI-006.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 load forecasting | **Continue with conditions** (council, 2026-08-26; board risk committee informed 2026-09-15) | Independent validation by 2026-11-30; automated input checks and monthly drift reports by 2027-01-31; regional solar inputs and review of the coastal error by 2026-11-30; similar-day method run in parallel on forecast peak days until validation passes (POAM-024) |
| AI-003 OMS outage prediction | **Continue** | Device model data review by 2026-12-31; accuracy review after each named storm |
| AI-006 design assistant | **Continue pilot; client CEII and BCSI blocked** | Upload block from 2026-10-15; client consent clause and engineer attestation by 2026-12-31; prompt injection test before any production use (POAM-022) |
| AI-002, AI-004, AI-005, AI-009 | **Approved** | Standard monitoring; AI-005 data path moved through the POC DMZ by 2027-03-31 |
| AI-007, AI-008 | **Approved** | AI-008 limited to Internal data; prohibited for grid, field, client, and employment decisions |

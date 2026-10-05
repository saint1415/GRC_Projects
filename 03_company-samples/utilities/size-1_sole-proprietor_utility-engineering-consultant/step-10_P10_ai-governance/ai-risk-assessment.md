# AI Use Assessment: Electric Load-Forecasting SaaS (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent utility engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Utilities |
| AI use case | AI-001: registry default "Electric load-forecasting model", adapted to what a one-person consultancy actually uses: a **third-party AI load-forecasting SaaS** trialed for the Client C ten-year planning study (SYS-08). Trial 2026-06-01 to 2026-07-15; Client C data uploaded 2026-06-03; paused 2026-07-20 |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form. AI-001 is predictive, not generative, so AI 600-1 applies only to AI-002 |
| Assessor and decision | Owner-engineer, 2026-08-24; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
The owner uploaded three years of hourly load data for Client C's 24 feeders and annual customer counts by class (no customer names). The SaaS returned ten-year peak forecasts per feeder. The forecasts were meant to feed the planning study that tells Client C which feeders and substation transformers to upgrade, and that the owner signs and seals. The owner accepted click-through trial terms without review: **the provider may keep uploaded data and use it to improve its models.** Client C was not asked. The model is proprietary; the provider published no method, training data description, or accuracy figures. **No forecast from the tool has been used in any deliverable** (the study draft was not started when the trial was paused).

## 2. Rules that apply (Govern)
| Rule | Applies? | Why |
|---|---|---|
| Client C contract, confidentiality clause | **Yes, breached** | No sharing of Client C data with third parties without written consent (P03 G-034) |
| NERC CIP and the client flow-down terms | No for AI-001 | Client C is not subject to NERC CIP, and feeder load data is not BCSI or CEII. **AI-002 is different:** chatbot notes named Client A substations (P03 G-009) |
| Professional responsibility for sealed work | Yes | The owner must be able to verify and explain any number in a sealed study; a black-box forecast cannot be sealed as is |
| AI-specific federal or Florida law | None identified | The vertical lists no sector AI rules. State consequential-decision laws cover decisions about individuals; this forecast makes none. NIST's AI RMF Critical Infrastructure Profile is a concept note (2026-04-07), not a requirement |
| Policy | Yes | POL-01 9.5 (AI tools), 8.1 and 8.2 (Client Restricted data locations), 6.2 (vendor list). POL-04 and POL-05 point to these sections |

## 3. Risk tier (repository rubric)
**Tier: High.** The forecast would be a substantial input to decisions about critical infrastructure: an under-forecast could leave feeders overloaded (equipment damage and outages for Client C's customers), and an over-forecast wastes a small utility's capital. Rubric minimum controls: human review before action, pre-deployment testing, this impact assessment, notice to the affected party (Client C), and ongoing monitoring.

## 4. Measure
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Backtest: train on the first 2 years, forecast the third; per-feeder peak error at most 5%, and within 3 percentage points of the owner's own regression method | Not done during the trial | No |
| Safe | No forecast enters a study without the owner's independent check | No output used so far | Yes (so far) |
| Secure and resilient | Terms bar retention and training; deletion on request | Trial terms allow both | No |
| Accountable and transparent | Provider documents the model, inputs, and limits | None published | No |
| Explainable and interpretable | Owner can explain each feeder's forecast drivers (growth, weather, new loads) | Not possible with the tool's output | No |
| Privacy-enhanced | No personal data; client data shared only with consent | No names, but no consent | No |
| Fair, with harmful bias managed | Compare backtest peak error across feeder groups by dominant customer class (residential, commercial, mixed); no group's mean error more than 2 percentage points worse than the best group | Not done | No |

## 5. Manage
- **Human review:** the owner rebuilds every forecast used in a study with an independent method, explains any difference larger than 3 percentage points, and states in the study which method set each number.
- **Monitoring:** compare forecasts with each new year of actual peaks the client sends; re-run the bias comparison each time.
- **Incident handling:** an upload of client data without consent is an incident under POL-01 10.2 and the P08 matrix (client notice).
- **Decommissioning:** stop and request deletion if terms change to allow training on customer data, or if the backtest fails.

## 6. Decision: stop for client work (approved 2026-08-31)
**Do not resume AI-001.** By 2026-09-30 (P01 R-009):
1. Tell Client C in writing what was uploaded, when, and under what terms; ask for written consent or confirm the forecast will be rebuilt without the tool.
2. Send the provider a written deletion request for the uploaded data and outputs; keep the reply.
3. Rebuild the Client C forecast with the owner's own regression method.
4. Reconsider an AI forecasting tool **only** with client consent, business terms that bar retention and training, a passed backtest and bias comparison (section 4), and a re-run of this assessment.

**AI-002 (consumer chatbot), tier Low if used as allowed:** stopped for client work on 2026-07-24. The owner deleted the chat history that day and, because the notes named Client A substations, told Client A the same day under SSA-A (5). General questions with no client, utility, or substation names remain allowed (POL-01 9.5).

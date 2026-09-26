# AI Risk Assessment: Electric Load-Forecasting Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electric distribution utility) |
| Tier / Vertical | Small / Utilities |
| AI use case | AI-001: in-house load-forecasting model, in production since 2024-05 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. AI 600-1 (Generative AI Profile) does not apply because the model is not generative |
| Assessor / date | Manager of Power Supply and Rates with the IT Manager and the Manager of System Operations, 2026-08-27 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** Manager of Power Supply and Rates. **Decision authority:** President and CEO (High tier). **Technical owner:** Load Forecasting Analyst.
- **Policies that apply:**
  - POL-04 4.9: no Restricted or Confidential data in unapproved AI tools
  - POL-05 4.9: approved tools only
  - POL-01 4.3: the model's risks are in the risk register (R-018, R-019)
- **Approved-tools list:** kept by the IT Manager. It lists AI-001 (internal) and AI-002 (vendor). Public chatbots (AI-003) are not approved for Restricted or Confidential data.
- **Scale for a small utility:** there is no AI committee. The Manager of Power Supply and Rates, the Manager of System Operations, and the IT Manager review AI use cases every quarter and report to the President and CEO.
- **Change control:** new model versions currently go live without approval (P04 finding 3). From 2026-10, a new version needs a validation report and sign-off by the Manager of Power Supply and Rates.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Forecast hourly load for the next day and the next 7 days, for the whole system and for each of the 22 substations |
| How the output is used | (1) The day-ahead purchase schedule sent to the wholesale supplier each morning. (2) Peak-day operating plans: calls to the voluntary demand response program, conservation voltage reduction, and pre-staging of crews and mobile transformers. (3) Summer switching plans that move load away from substations near their limits |
| Users / operators | Load Forecasting Analyst (runs it); Manager of Power Supply and Rates (approves schedules); DCC shift supervisors (read peak-day forecasts) |
| Affected people | All 72,000 customers indirectly. A bad forecast can raise wholesale costs, which flow to rates, or can leave a substation overloaded on a peak day, causing outages or equipment damage |
| Data | SCADA substation load history (from the historian replica); AMI interval data **aggregated to substation level, with at least 100 meters per aggregate**; commercial weather forecasts; calendar and holidays; rooftop solar estimates. No individual customer records enter the model |
| Build or buy | Built in-house in 2024: a gradient-boosted regression model in the cloud analytics workspace (SYS-09), retrained monthly |
| Not intended | Automatic control of any grid device, automatic demand response dispatch, or any decision about an individual customer. These uses would require a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| NERC CIP | No | The model and the analytics workspace are not BES Cyber Systems. They do not control or protect BES Facilities, and the company's CIP scope is limited to the relays at Substation N and E (P03) |
| Federal or Florida AI-specific law | None identified | The repository's cross-sector file lists no federal AI statute that governs this use. The company operates only in Florida, and state AI laws such as Colorado SB26-189 cover consequential decisions about individuals, which this model does not make |
| Wholesale supply contract | Yes (contract) | The contract sets daily schedule deadlines and charges for imbalances. Forecast accuracy has direct cost |
| Customer data rules | Indirectly | Only aggregated usage data is used. POL-04 classifies usage data as Confidential and keeps it inside approved systems |
| NIST guidance | Voluntary | AI RMF 1.0. NIST released a concept note for an **AI RMF Critical Infrastructure Profile** on 2026-04-07; the company will review the profile when it is published |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).

**Why High:** the rubric puts any AI that "can affect physical safety or critical infrastructure operations" in the High tier. The forecast shapes peak-day operating plans and summer switching for a distribution grid. An under-forecast can leave a substation overloaded, and an over-forecast wastes money on unneeded purchases.

**What limits the risk:** the model makes no decision on its own. A person approves every schedule and every operating plan, and nothing is wired to a control system.

**Minimum controls for the High tier and how they are met:**
| Rubric control | Status |
|---|---|
| Human review before action | In place (schedule and operating plan approvals) |
| Pre-deployment testing | **Missing:** no documented validation before new versions |
| Impact assessment | This document (first one) |
| Notice to affected people | The model affects grid operations, not decisions about individuals. Notice is given to the wholesale supplier (method summary shared 2026-09) and to the board. Customers are not individually affected |
| Ongoing monitoring | **Missing:** error is tracked informally in a spreadsheet |

**Escalation triggers (re-assess before any of these):**
- using the forecast to dispatch demand response or voltage reduction automatically
- feeding it into SCADA or any control system
- using customer-level data or customer-level predictions
- selling or sharing forecasts with third parties

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (backtest 2025-06-01 to 2026-07-31) | Pass? |
|---|---|---|---|
| Valid and reliable | Day-ahead system mean absolute percentage error (MAPE) of 3.5% or less on all days, and 5.0% or less on the 20 highest-load days | 3.1% on all days; **5.8% on peak days** | **No.** Peak-day threshold missed |
| Valid and reliable (drift) | Monthly error trend; retrain if the 30-day MAPE rises above 4.0% | 30-day MAPE rose to 4.4% in 2026-04 as rooftop solar grew; retrained 3 weeks late | **No.** No automatic drift alert |
| Safe | Peak-day forecast compared with the supplier's forecast; a gap over 5% triggers manual review by the Manager of System Operations | Comparison done on 11 of 20 peak days | **No.** Not done consistently |
| Secure and resilient | Named accounts; input range checks on weather and load data; fallback to the prior day's schedule | Shared workspace key; no input checks; fallback used twice when the weather feed failed | **No** |
| Accountable and transparent | Model card, validation report, and approval record for each version | No model card; version history in the code repository only | **No** |
| Explainable and interpretable | Feature importance and a per-forecast breakdown (temperature, day type, solar) available to the analyst and the approver | Available; the approver reviews it on peak days | Yes |
| Privacy-enhanced | AMI data aggregated to at least 100 meters per substation before use | Confirmed for all 22 substation aggregates | Yes |
| Fair, with harmful bias managed | Substation-level test below | **Two substations flagged** | **No** |

**Bias and fairness testing plan.** A load forecast does not decide anything about a person. Its errors still land on neighborhoods: a substation that is under-forecast on hot days is more likely to overload, lose service, or be chosen for load relief. The test:
- **Groups compared:** the 18 distribution substations, each tagged by (a) share of residential customers enrolled in the income-qualified bill assistance program, (b) median housing age, and (c) rooftop solar share.
- **Metrics:** substation MAPE and mean signed error on the 20 highest-load days, compared with the system average.
- **Threshold:** flag any substation whose peak-day MAPE exceeds the system average by more than 2 percentage points, or whose signed error shows under-forecasting beyond 3%.
- **Frequency:** every quarter, and after each retraining.

**Bias finding.** Two substations that serve older neighborhoods with a high share of income-qualified customers are **under-forecast by 6% on hot days**. The likely cause is many window air-conditioning units, which respond to heat differently than the central systems that dominate the training data. Both substations were already near their summer limits. Actions:
- Add a heat-response feature for those areas.
- Until the fix is validated, the DCC adds a 6% margin to both substations' peak-day forecasts.
- Voltage reduction and load relief must not fall repeatedly on the same substations. The Manager of System Operations reviews the rotation each summer.

## 5. MANAGE
**Human-in-the-loop design:**
- The Load Forecasting Analyst runs the model and reviews the output against the prior day and the supplier's forecast.
- The Manager of Power Supply and Rates approves the day-ahead schedule and can override it. Overrides are logged with a reason.
- On days forecast within 5% of a substation limit, the Manager of System Operations approves the peak-day operating plan.
- If the model or its data fails, the fallback is the prior day's schedule adjusted for weather, or the supplier's forecast.

**Monitoring:**
- Daily error report and a monthly drift report, with an automatic alert when the 30-day MAPE exceeds 4.0% (P01 R-018).
- Quarterly substation fairness test (section 4).
- Input range and plausibility checks on the weather feed and load data before each run (P01 R-019).

**Security:**
- Named accounts in the analytics workspace, replacing the shared key.
- Model code and versions in the repository, with approval before release (P04 finding 3).
- The workspace must have no path into the OT network. Load history arrives only as an export from the historian replica in the OT DMZ. Removing the legacy firewall rules (P04 finding 1, POAM-003) closes the path that exists today.

**Incident handling:** a suspected data tampering or workspace compromise is handled under POL-03. A forecast error that contributes to an outage or equipment overload is reviewed like any operating event and recorded in the risk register.

**Decommissioning:** retire or roll back the model if peak-day MAPE stays above 5.0% for two summers in a row, or if a validated vendor forecast performs better at lower risk. Keep the last approved version for rollback.

## 6. Decision
**Approve with conditions.** President and CEO, 2026-09-04. The model may stay in production **only if** these conditions are met by 2026-12-31:
1. A validation report and model card for the current version, with sign-off before any new version goes live.
2. Named workspace accounts and input range checks (R-019).
3. An automatic drift alert and the daily comparison with the supplier's forecast on every peak day.
4. The heat-response fix for the two flagged substations, validated against the 2026 summer. The 6% margin stays in place until then.

The model must be re-assessed before any escalation trigger in section 3, and at least every year.

**Related actions:**
- **AI-002 (AMI tamper analytics):** review flag accuracy every quarter, including false flags by neighborhood. Keep the rule that a technician inspects every flagged meter before any action. Due 2026-12-31.
- **AI-003 (public chatbots):** prohibited for Restricted and Confidential data (POL-05 4.9). Evaluation of an enterprise tool with no-training terms is due 2026-12-31.

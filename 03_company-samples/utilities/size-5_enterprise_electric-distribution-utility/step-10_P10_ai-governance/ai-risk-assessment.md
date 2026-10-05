# AI Governance Risk Assessment: Enterprise AI Portfolio and the Electric Load-Forecasting Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded investor-owned electric utility; Florida and south Georgia) |
| Tier / Vertical | Enterprise / Utilities |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the electric load-forecasting model, in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; NIST AI 600-1 (Generative AI Profile) for AI-006 and AI-007; repository risk tier rubric |
| Assessor / date | AI council (chaired by the Chief Data and Analytics Officer), meeting of 2026-08-26; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 4, Medium 7, Low 1 |
| Status | In production 9, Pilot 1, Suspended 2 |
| Council review complete | 8 of 12 |
| Not yet reviewed | 4: AI-003, AI-006, AI-010, AI-012 (all due 2026-11-30, POAM-029) |
| High-tier uses that affect critical infrastructure operations | 2 (AI-001 load forecasting, AI-004 storm outage prediction) |
| High-tier uses that would make consequential decisions about people | 2, both suspended (AI-008 deposit risk score, Credit; AI-012 applicant screening, Employment) |

**Main findings:** four use cases reached production or pilot without council review, three of them as features switched on in vendor products (AI-003, AI-006, AI-012). The load-forecasting model, the most consequential model for grid operations, still relies on manual drift review, and its summer 2026 fairness test flagged two groups of substations. No fairness testing has been done for the AMI theft analytics (AI-003), which send technicians to customers' homes.

## 2. GOVERN: AI council operating model
**Charter.** The AI council was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the risk and reliability committee reviews quarterly.

**Members:** Chief Data and Analytics Officer (chair); CISO; Director, OT Security; Chief Privacy Officer; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce tools); Vice President, Distribution Operations; Director, Power Supply and Load Forecasting; Vice President, Customer Operations; and a customer advocacy representative. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Council vote, then the executive risk committee | Validation and bias testing on company data; impact assessment; human review design; notice to affected people where individuals are affected; monitoring plan; for OT-adjacent models, an OT Security review that the model has no path into control systems |
| Medium | Council vote | Human oversight design; output quality monitoring; AI disclosure where customers interact with it; privacy and security review |
| Low | Council chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.7; STD-05.2). Since 2026-07, procurement and IT change management block vendor AI features without an inventory ID; this did not exist when AI-003, AI-006, and AI-012 were switched on.

**Policies:** POL-04 4.8 (no Restricted or Confidential data in AI tools outside the approved list; never BCSI); POL-05 4.7 (approved tools only; register new uses); POL-01 4.3 (AI risks in the enterprise risk register); POL-03 (AI incidents follow incident response).

**Cadence:** monthly council meetings; quarterly monitoring review for every High-tier model; annual re-review of every use case.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| NERC CIP | No, by design | No model is a BES Cyber System or runs in an Electronic Security Perimeter. Models receive OT data only through one-way exports from the ADMS DMZ and have no path back into the EMS or ADMS (P04 guardrail `SC-7(21)`) |
| FCRA adverse action notices (15 U.S.C. 1681m(a)) | Yes, for AI-008 if re-enabled | Requiring a deposit based in whole or in part on a consumer report requires an adverse action notice |
| FTC Identity Theft Red Flags Rule (16 CFR 681.1) | Context for AI-008 and AI-006 | Identity verification at account opening and account changes through the contact center |
| Federal equal employment opportunity laws | Yes, for AI-012 if enabled | Counsel reviews adverse impact before any enablement |
| State call recording consent laws | Yes, for AI-006 | The contact center applies all-party consent for recorded calls in both states; Florida worked example: Fla. Stat. 934.03(2)(d) |
| State breach and data security laws | Yes, for uses with customer data | Each state where affected individuals reside; Florida worked example: Fla. Stat. 501.171 |
| FTC Act Section 5 | Indirectly | Accuracy of vendor claims (AI-003) and of public statements such as restoration estimates (AI-010) |
| State AI laws (for example, Colorado SB26-189, effective 2027-01-01) | No | The company operates only in Florida and Georgia; no Florida or Georgia AI statute covering these uses was identified |
| NIST guidance | Voluntary | AI RMF 1.0 and AI 600-1. NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07; the council will review the profile when it is published |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Council review |
|---|---|---|---|---|
| AI-001 | Electric load-forecasting model | High | In production | Reviewed 2026-02-18; full assessment 2026-08-26 |
| AI-002 | Distribution transformer and asset failure prediction | Medium | In production | Reviewed 2026-03-25 |
| AI-003 | AMI theft and tamper analytics | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-004 | Storm outage prediction for crew pre-staging | High | In production | Reviewed 2026-04-15 |
| AI-005 | Vegetation risk model | Medium | In production | Reviewed 2026-03-25 |
| AI-006 | Contact center generative AI agent assistant | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-007 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-21 |
| AI-008 | Deposit risk score | High | Suspended | Reviewed 2026-06-17 (suspension) |
| AI-009 | SOC alert triage assistant | Low | In production | Reviewed 2026-02-18 |
| AI-010 | Estimated restoration time prediction | Medium | Pilot | Not reviewed (due 2026-11-30; required before rollout) |
| AI-011 | Drone and imagery inspection defect detection | Medium | In production | Reviewed 2026-05-20 |
| AI-012 | HR applicant screening and ranking | High | Suspended | Not reviewed (due 2026-11-30; required before any enablement) |

**Tiering notes:** AI-001 and AI-004 are High because they shape grid operations and storm restoration, even though a person approves every action. AI-002 stays Medium because it ranks long-term maintenance work rather than operating the grid. AI-003 stays Medium because a technician inspects every flagged meter; if flags ever lead directly to disconnection or back-billing without inspection, it becomes High. AI-007 is Medium rather than Low because Confidential customer data is allowed in its approved tenant.

## 5. MEASURE: portfolio fairness and quality testing
| Use case | Metric | Groups compared | Threshold for action | Status |
|---|---|---|---|---|
| AI-001 load forecasting | Peak-day error and signed error by substation | Substations grouped by share of income-qualified customers, housing age, and rooftop solar share | Peak-day error more than 2 points above the system, or under-forecasting beyond 3% | Done for summer 2026 (section 7.4) |
| AI-003 theft analytics | Flag rate per 1,000 meters and confirmed-theft rate of flags | Neighborhoods by income-qualified share and housing age | Flag-rate ratio above 1.25 with a confirmed-theft rate below the system average | Planned, first test by 2027-03-31 |
| AI-004 storm outage prediction | Predicted versus actual outages by district | Urban and rural districts | Under-prediction above 5% in any district group | Done (rural floor added) |
| AI-006 contact center assistant | Suggestion accuracy | Call language; account type | Accuracy gap above 5 points | Planned with the council review |
| AI-010 restoration estimates | Estimate error | Urban and rural districts; medical-priority customers | Error gap above 30 minutes | Required before rollout |

## 6. GOVERN and MANAGE for generative AI (AI-006 and AI-007)
Using the AI 600-1 risk list, the council focused on confabulation (wrong answers about payment arrangements or disconnection rules), data privacy (customer data in prompts and transcripts), and information security (prompt injection through customer messages). Controls: agents must edit and own every suggestion; the assistant is limited to approved knowledge articles; no BCSI is allowed in any generative tool (POL-04 4.8); DLP scans prompts for SSNs and BCSI; vendor contracts prohibit training on company data. The AI-006 review will decide whether to keep payment and disconnection topics out of the assistant entirely.

## 7. Full assessment: AI-001 electric load-forecasting model
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Forecast hourly load for the next day and the next 7 days for the system (2025 peak 8,650 MW) and for each of the 418 distribution substations |
| How the output is used | (1) Day-ahead schedules to the Balancing Authority and dispatch instructions under the PPAs. (2) Peak-day operating plans at the DCC: demand response calls, conservation voltage reduction, crew and mobile transformer staging, and summer switching away from substations near their limits. (3) An input to the TCC's next-day operating studies |
| Users / operators | Load forecasting team of 4 (runs it); power supply desk (approves schedules); DCC and TCC shift supervisors (read peak-day forecasts) |
| Affected people | All 1.95 million meters indirectly. A poor forecast raises wholesale costs, which flow to rates, or leaves a substation overloaded on a peak day |
| Data | Historian load history (one-way export from the ADMS DMZ); AMI interval data aggregated to substation level with at least 100 meters per aggregate; one commercial weather feed; calendar; rooftop solar and EV estimates. No individual customer records enter the model |
| Build or buy | Built in-house; gradient-boosted regression ensemble on the Cloud provider B analytics platform; retrained monthly |
| Not intended | Automatic control of any grid device; automatic demand response dispatch; any decision about an individual customer |

### 7.2 Risk tier
**High.** The forecast shapes peak-day operating plans and summer switching for the distribution grid and feeds the TCC's next-day studies. An under-forecast can leave substations overloaded; an over-forecast wastes money on unneeded purchases. What limits the risk: a person approves every schedule and every operating plan, and nothing is wired to a control system.

**Escalation triggers (re-assess before any of these):** automatic dispatch of demand response or voltage reduction; feeding the forecast into the ADMS or EMS; use of customer-level data or predictions; sharing forecasts with third parties beyond the Balancing Authority.

### 7.3 Minimum controls for the High tier
| Rubric control | Status |
|---|---|
| Human review before action | In place (schedule and operating plan approvals; overrides logged with reasons) |
| Pre-deployment testing | In place since 2026-03: each version needs a validation report and sign-off by the Director, Power Supply and Load Forecasting |
| Impact assessment | This document |
| Notice to affected people | The model affects grid operations, not decisions about individuals. Method summaries go to the Balancing Authority and the risk and reliability committee |
| Ongoing monitoring | **Partial:** daily error report exists; drift review is manual and monthly (automated alerts due 2026-12-31, POAM-029) |

### 7.4 MEASURE (backtest 2025-06-01 to 2026-07-31)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Day-ahead system MAPE of 3.0% or less on all days and 4.5% or less on the 20 highest-load days | 2.6% on all days; 4.1% on peak days | Yes |
| Valid and reliable (drift) | Retrain if the 30-day MAPE rises above 3.5% | 30-day MAPE reached 3.9% in 2026-05 as EV charging grew; retrained 17 days later after manual review | **No** (no automatic alert) |
| Safe | Peak-day forecast compared with the Balancing Authority forecast; a gap over 4% triggers DCC review | Done on all 20 peak days | Yes |
| Secure and resilient | Named workspace accounts; input range checks; one-way data path from OT; fallback to the prior-day schedule | All in place; single weather feed (POAM-028) | **Partial** |
| Accountable and transparent | Model card, validation report, and approval for each version | In place for the 3 versions since 2026-03 | Yes |
| Explainable and interpretable | Feature contributions per forecast (temperature, day type, solar, EV) available to approvers | Available and used on peak days | Yes |
| Privacy-enhanced | AMI data aggregated to at least 100 meters per substation | Confirmed for all 418 aggregates | Yes |
| Fair, with harmful bias managed | Substation fairness test (below) | **Two groups flagged** | **No** |

**Bias and fairness testing plan.** A load forecast does not decide anything about a person, but its errors land on neighborhoods: a substation under-forecast on hot days is more likely to overload, lose service, or be chosen for load relief.
- **Groups compared:** the 418 distribution substations, tagged by (a) share of residential customers in the income-qualified bill assistance program (quartiles), (b) median housing age, and (c) rooftop solar share.
- **Metrics:** peak-day MAPE and mean signed error on the 20 highest-load days, compared with the system.
- **Thresholds:** flag any group whose peak-day MAPE exceeds the system by more than 2 percentage points, or whose signed error shows under-forecasting beyond 3%.
- **Frequency:** every quarter and after each retraining.

**Findings.**
1. Substations in the top quartile of income-qualified customers and older housing were **under-forecast by 5.2% on hot days** (system 0.4%). The likely cause is window air-conditioning units, which respond to heat differently from central systems. Eleven of these substations were within 5% of their summer limits.
2. Substations with the highest rooftop solar share were **over-forecast at midday and under-forecast at the evening ramp by 3.8%**, because the solar estimates lag new installations.

**Actions:** add a heat-response feature for the flagged areas and a monthly solar interconnection feed; until validated, the DCC adds a 5% margin to the eleven substations' peak-day forecasts; the DCC director reviews each summer that load relief (voltage reduction, switching) does not fall repeatedly on the same substations.

### 7.5 MANAGE
- **Human in the loop:** the forecaster reviews each run against the prior day and the Balancing Authority forecast; the power supply desk approves and can override schedules (overrides logged); the DCC approves peak-day operating plans for substations forecast within 5% of their limits.
- **Monitoring:** daily error report; automated drift alert at a 30-day MAPE of 3.5% (due 2026-12-31); quarterly fairness test; second weather feed with automatic switchover (POAM-028).
- **Security:** named accounts and service identities; model code and versions in the pipeline with approval (P04); no path from the analytics platform into OT; input range checks before each run.
- **Incidents:** suspected data tampering or workspace compromise follows POL-03 and P08; a forecast error that contributes to an outage or equipment overload is reviewed like any operating event and recorded in the risk register (R-045, R-046).
- **Decommissioning:** roll back to the last approved version if peak-day MAPE exceeds 4.5% for two consecutive months in summer, or retire the model if a validated alternative performs better at lower risk.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier model has quarterly performance and fairness metrics reported to the council (inventory column `monitoring`); drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, fairness finding, data misuse) are logged as SOC or operating events and follow P08 where security or customer data is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes and prohibit training on company data.
- **Decommissioning:** models are retired if they fail monitoring thresholds twice, if a vendor changes data-use terms, or if the use drifts beyond its approved purpose; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the council's recommendation of 2026-08-26:
1. **AI-001:** approved to continue with conditions: automated drift alerts by 2026-12-31 (POAM-029); second weather feed by 2027-03-31 (POAM-028); heat-response and solar fixes validated against summer 2027 data, with the 5% DCC margin kept until then.
2. **AI-003, AI-006, AI-010, AI-012:** council reviews by 2026-11-30 (POAM-029). AI-010 stays in pilot and AI-012 stays disabled until reviewed. AI-003 gets its first flag-rate test by 2027-03-31.
3. **AI-008:** stays suspended until notice logic and fairness testing are reviewed (P01 R-044).
4. **Intake control:** keep the procurement and change management block on unregistered vendor AI features; Internal Audit tests it in the 2027 audit plan.

The council re-assesses AI-001 before any escalation trigger in section 7.2, and at least every year.

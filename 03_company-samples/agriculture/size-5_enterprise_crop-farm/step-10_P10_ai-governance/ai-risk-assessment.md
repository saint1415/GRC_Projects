# AI Governance Risk Assessment: Enterprise AI Portfolio and Computer-Vision Crop Yield Prediction

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded diversified precision-agriculture crop farm; FL, GA, SC, NC) |
| Tier / Vertical | Enterprise / Agriculture, Forestry, Fishing and Hunting |
| Scope | Enterprise AI portfolio (11 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 computer-vision crop yield prediction in section 6 |
| Inventory | `ai-use-case-inventory.csv` (11 use cases), built from the AI governance committee register (EV-076), the accounts payable vendor master (EV-056), the dealer portal and e-commerce SaaS records (EV-024, EV-061), and the committee's 2026-07-15 and 2026-08-26 minutes (EV-090). The `source_evidence` column names the source of each entry. Not established at intake: AI features embedded in vendor products beyond the four in the register (intake open request), and workforce use of public AI tools on personal devices |
| Framework | NIST AI RMF 1.0 (AI 100-1); the Generative AI Profile (NIST AI 600-1) for the generative use cases (AI-008, AI-011); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Risk Officer), meeting of 2026-08-26; the GRC team and the Data Science Lead prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 8) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 11 |
| Risk tier | High 3, Medium 6, Low 2 |
| Status | In production 10, Pilot 1 |
| Committee review complete | 7 of 11 |
| Not yet reviewed | 4: AI-004, AI-009, AI-010, AI-011 (all due 2026-12-31, POAM-021) |
| Use cases that affect workers' hours or jobs | 2 (AI-001 through its outputs, AI-006 directly), both High |
| High-tier use cases with bias testing incomplete | 2 (AI-001 and AI-006: crew plan outcomes by worker group not yet tested) |

**Main findings:** AI-001 started as an agronomy tool and was assessed Medium in 2025. In 2026 its forecasts began to drive crew planning (AI-006) and the first drafts of H-2A job orders, which makes it a substantial factor in employment decisions about seasonal and H-2A workers, so the committee re-tiered it High on 2026-07-15. Its accuracy is good for most produce but weak for watermelons and early-season strawberries, and the downstream fairness testing (hours offered and crew assignments by worker group) is not done. Four use cases entered through vendor feature releases and have not been reviewed. Unapproved generative AI tools are blocked (P01 R-041).

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly.

**Members:** Chief Risk Officer (chair); CISO; Chief Privacy Officer; Chief Compliance Officer; Chief Human Resources Officer; Director of H-2A and Labor Compliance; Vice President, Digital Agronomy; Vice President, Irrigation and Water Resources; General Counsel's delegate; Data Science Lead (non-voting for use cases the data science team builds). Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Impact assessment; pre-deployment bias testing on the company's own data, including downstream effects on workers; human review design; notice to affected people; monitoring plan; for anything that can move equipment or water, a safety review by the Director of OT Security |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside vendor products (graders, dealer portals, the e-commerce SaaS), must be registered before use (POL-05 4.7; STD-05.3). Since 2026-06, procurement and the change advisory board block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.9 (no Restricted or Confidential data in AI tools without committee approval and no-training terms); POL-05 4.7 (approved tools only) and 4.8 (drone imagery not used to evaluate workers); POL-01 4.8 (vendor security terms); STD-05.3 (approved AI tools and imagery use).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case; re-review whenever a use case's outputs start feeding a new decision (the AI-001 lesson).

**Why 4 use cases lack review.** AI-004 (graders) and AI-010 (dealer telematics) arrived as vendor feature releases before the intake block existed; AI-009 is an MSSP and SIEM feature; AI-011 is a pilot inside the e-commerce SaaS. All four have review dates (section 8).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| H-2A employer obligations, 20 CFR 655.122(i) and (j)(1) | **Yes, for AI-001 and AI-006** | The company must offer each H-2A worker hours equal to at least three-fourths of the workdays in the contract period and record hours offered each day. A forecast cannot lower that floor. Over-forecasting inflates crews and job orders and raises guarantee exposure; under-forecasting leaves crops unpicked or cuts hours |
| Federal equal employment opportunity laws | Yes, for AI-006 (and AI-001 through it) | Crew assignment and hours must not disadvantage workers by national origin, sex, age, or other protected traits. Counsel reviews the bias testing design. Nationality and visa status are in the roster and are excluded from model features |
| State AI laws | **No** | No state AI law applies in Florida, Georgia, South Carolina, or North Carolina according to the repository's cross-sector register (as of 2026-09-25). Colorado SB26-189 (effective 2027-01-01) would cover employment decisions, but the company does not do business in Colorado. Federal preemption efforts (EO 14365) are tracked, not relied on |
| FTC Act Section 5 | Indirectly | Accuracy of AI claims made to customers or growers (AI-002 recommendations to SL-1 growers; AI-011 chatbot) |
| SEC disclosure controls | Indirectly, for AI-001 and AI-007 | Yield and demand forecasts used in investor guidance go through finance review; the model is not a source of record for disclosures |
| Crop insurance and USDA program reporting | Not used | Acreage and production reports use settlement and packed-out records, not model estimates (an escalation trigger in section 6.3) |
| Fla. Stat. 501.171 | Not for current uses | Imagery of people is not personal information unless linked to a name and a listed data element; POL-05 4.8 keeps it that way. Telematics location data (AI-010) is not linked to operator identity |
| FDA Produce Safety and Food Traceability Rules | Not for AI outputs | No regulated record is created by a model. AI-004 grading is quality, not food safety; food safety holds are human decisions |
| NIST AI 600-1 | Yes, as guidance for AI-008 and AI-011 | Generative use cases: confabulation, information integrity, and data privacy risks addressed in their reviews |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person (here, employment) or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Computer-vision crop yield prediction from drone imagery | High | In production | Reviewed 2025-11-12 (Medium); re-tiered High 2026-07-15; full assessment 2026-08-26 |
| AI-002 | Irrigation scheduling recommendations | Medium | In production (recommendation mode) | Reviewed 2026-02-18 |
| AI-003 | Pest and disease detection from scout photos | Medium | In production | Reviewed 2025-12-03 |
| AI-004 | Optical grader defect and size classification | Medium | In production (9 packing sites) | Not reviewed (due 2026-12-31) |
| AI-005 | Variable-rate fertilizer and seeding prescriptions | High | In production | Reviewed 2026-03-25 |
| AI-006 | Crew planning and labor demand forecasting | High | In production | Reviewed 2026-07-15 |
| AI-007 | Demand and price forecasting | Medium | In production | Reviewed 2026-04-22 |
| AI-008 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-20 |
| AI-009 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-12-31) |
| AI-010 | Equipment telematics predictive maintenance | Low | In production | Not reviewed (due 2026-12-31) |
| AI-011 | Produce box customer service chatbot | Medium | Pilot | Not reviewed (due 2026-12-31, before full launch) |

**Tiering notes:**
- **AI-001 is High** because its forecasts now set crew sizes and the first draft of H-2A job orders through AI-006. A human approves each plan, but the forecast is a substantial factor in how many workers are requested and how many hours are offered.
- **AI-005 is High** because prescriptions execute through equipment and can over-apply inputs; an agronomist approves every map and controllers enforce rate limits.
- **AI-002 stays Medium** because operators accept every schedule and the interface rejects out-of-range values before SCADA (P02 SI-10; P04). Automatic execution would make it High and needs a new assessment with the Director of OT Security.
- **AI-011 is Medium** because subscribers interact with it directly; disclosure and human escalation are required before full launch.

## 5. MEASURE: portfolio bias and accuracy gaps
**Gap.** AI-001 accuracy has been tested by crop, variety, region, and season stage, but nobody has tested what happens to workers downstream: whether crew plans built from the forecasts offer hours and assign crews evenly across worker groups. AI-006 has the same gap.

**Testing plan for crew outcomes (POAM-021, due 2027-01-31, before the spring crew planning cycle):**
| Outcome | Metric | Groups compared | Threshold for action |
|---|---|---|---|
| Hours offered | Hours offered per worker per week relative to the crew plan | H-2A and domestic workers; sex; age band; crew; region | Any group's average below 90% of the overall average |
| Crew assignment | Share of each group assigned to higher piece-rate crops | Same groups | Assignment-rate ratio below 0.8 for any group |
| Short-notice hour cuts | Share of planned hours cut within 48 hours | Same groups; forecast error band | Any group's cut rate more than 1.25 times the overall rate |
| Guarantee exposure | Workers projected below the three-fourths guarantee at mid-contract | By crew and region | Any projection below the guarantee triggers a plan change, never a lower offer |

**Data limits:** sex and age come from HR records; nationality and visa status are used only for testing, never as model features. Results go to the committee and the Chief Compliance Officer, and counsel reviews the method.

## 6. Full assessment: AI-001 computer-vision crop yield prediction
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Estimate weekly marketable yield per block, 1 to 3 weeks ahead, from fruit and flower counts detected in drone images, for harvest planning, packing capacity, sales commitments (AI-007), and crew planning (AI-006) |
| Users | Agronomists and Regional Farm Directors; packing and sales planners; the crew planning team and the Director of H-2A and Labor Compliance (through AI-006) |
| Affected people | Seasonal and H-2A workers whose crews and hours follow the plans (up to 7,300 a season); customers who buy against commitments; people who appear incidentally in field images |
| Data | **Inputs:** RGB and multispectral orthomosaics from about 140 drones (SYS-10), block boundaries, varieties, planting dates, weather, and historical block yields from tally totals (never per-worker data). **Outputs:** block-level estimates with confidence ranges and detection overlays. **Training:** company imagery and yields from 2022 to 2026 across all 6 regions; AQ-01 and AQ-02 blocks added in 2026 with only one season of history |
| Build or buy | Build: in-house models on Cloud provider B AI services under terms that bar the provider from training on company data (P04). Model versions are promoted only after committee-approved validation, and the version is recorded with each forecast |
| Not intended | Evaluating individual workers; reducing offered hours below the three-fourths guarantee; final H-2A job order numbers without human review; crop insurance or USDA program reports; driving irrigation or variable-rate application. Each would require re-assessment |

### 6.2 Risk tier
**High** (section 4). The model does not decide on its own, but through AI-006 it is a substantial factor in employment decisions about seasonal and H-2A workers. Required High-tier controls: human review before action, pre-deployment bias testing including downstream crew outcomes, this impact assessment, notice to affected workers, and ongoing monitoring.

### 6.3 Escalation triggers (re-assess)
- Job orders filed without the Director of H-2A and Labor Compliance's review, or crew hours cut automatically on a forecast change
- Use of estimates in crop insurance, USDA program, or investor guidance without finance review
- Use of imagery or model output to evaluate individual workers
- Linking forecasts to irrigation or variable-rate prescriptions that execute automatically

### 6.4 MEASURE (2025-26 season backtest and 2026 spring season, 31 weekly forecast cycles)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Mean absolute percentage error (MAPE) of 1-week-ahead block estimates; threshold 15% | Tomatoes 9%; peppers 10%; cucumbers 11%; strawberries 12%; blueberries 13%; watermelons 23% (vine canopy hides fruit) | **No for watermelons**; yes for the others |
| Safe | No connection to irrigation, equipment, or SCADA; forecasts cannot trigger any field action | Confirmed in P04 and the model's integration list | Yes |
| Secure and resilient | Imagery buckets private with time-limited links; model registry access through PAM; provider terms bar training on company data | In place (P04) | Yes |
| Accountable and transparent | Forecasts labeled "AI estimate" in planning tools; decision log for each crew plan and job order draft that used a forecast; notice to workers that crew plans use forecasts | Labels and decision log in place since 2026-07; worker notice drafted in English and Spanish, not yet issued | **Partial** |
| Explainable and interpretable | Detection overlays and per-block feature contributions available to agronomists | Available; used in 82% of sampled weeks | Yes |
| Privacy-enhanced | People in images are not detected or analyzed; imagery retention 3 seasons; POL-05 4.8 | Confirmed | Yes |
| Fair, with harmful bias managed | (a) Signed forecast error by region, variety, and season stage; flag a subgroup whose mean error differs from overall by more than 5 points. (b) Downstream crew outcomes by worker group (section 5) | (a) AQ-01 and AQ-02 blocks +9% (one season of history): **flagged**; early-season strawberries -11%: **flagged**; other subgroups within 3 points. (b) Not yet tested | **No** |

**Why the flags matter to people.** Over-estimates on AQ-01 and AQ-02 blocks lead to planning more crew hours than there is fruit to pick and then cutting hours at short notice; under-estimates in early-season strawberries lead to too few pickers and fruit left in the field. Workers bear the first effect, and the company bears guarantee exposure under 20 CFR 655.122(i).

### 6.5 MANAGE
**Human in the loop:**
- Forecasts are advice. Agronomists check each block estimate against hand counts on sample plots before it enters a crew plan.
- The Director of H-2A and Labor Compliance reviews every job order draft and sets the requested number of workers from the forecast range, prior seasons, and the guarantee, never from the point estimate alone.
- Crew leads cannot cut planned hours because of a forecast change without a Regional Farm Director's approval; hours offered never fall below the three-fourths guarantee, and every offer is recorded (20 CFR 655.122(j)(1)).
- Watermelon forecasts and AQ-01 and AQ-02 block forecasts are advisory only until their error is within 15% MAPE and the subgroup bias is within 5 points for a full season.

**Monitoring:** weekly error by block in season; monthly subgroup bias check; quarterly crew outcome metrics (section 5) once testing is live; model version recorded with each forecast; drift alert when a block's error exceeds 30% for two consecutive weeks.

**Incident handling:** a forecast failure (error over 30% against hand counts) sends that block back to hand counts and is logged as an AI incident for the committee. A data or security incident follows P08. A complaint about crew hours or assignment goes to the Director of H-2A and Labor Compliance and is reviewed against the decision log.

**Decommissioning:** forecasts are withdrawn from crew planning if bias testing is not complete by 2027-01-31, if crew outcome thresholds are breached two months in a row, or if strawberry or tomato MAPE exceeds 20% for two consecutive months.

## 7. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case reports quarterly performance and fairness metrics (inventory column `monitoring`) to the committee; threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as SOC or operational events and follow P08 where security or personal information is involved.
- **Third parties:** AI vendors are tiered in the vendor program; contracts require notice of material model changes and bar training on company data. Vendor AI features (AI-004, AI-009, AI-010, AI-011) are registered and reviewed like any other use case.
- **OT boundary:** no AI output may command irrigation, fertigation, or equipment without a new assessment and a safety review (AI-002 and AI-005 notes in section 4).
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice or if a vendor changes data-use terms; the inventory records retirement.

## 8. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the AI governance committee's recommendation of 2026-08-26:
1. **AI-001:** approved to continue with conditions: worker notice issued in English and Spanish before the 2026-27 season; watermelon and AQ-01 and AQ-02 forecasts advisory only; crew outcome bias testing complete by 2027-01-31 (POAM-021); forecasts withdrawn from crew planning if that date is missed.
2. **AI-006:** approved to continue under the same conditions; job order drafts always reviewed by the Director of H-2A and Labor Compliance.
3. **AI-002:** stays in recommendation mode; automatic execution requires a new High-tier assessment with the Director of OT Security.
4. **AI-004, AI-009, AI-010:** may continue in current scope until committee review by 2026-12-31; no expansion.
5. **AI-011:** stays a Florida-only pilot until committee review, AI disclosure, and human escalation are confirmed (by 2026-12-31).
6. **Generative AI:** unapproved tools stay blocked; AI-008 remains the approved assistant (P01 R-041).

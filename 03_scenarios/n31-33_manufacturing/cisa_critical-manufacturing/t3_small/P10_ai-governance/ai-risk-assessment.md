# AI Risk Assessment: Demand Forecasting and Predictive Maintenance

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (power and distribution transformer manufacturer, Florida) |
| Tier / Vertical | Small / Critical Manufacturing |
| AI use cases | AI-001: demand forecasting (in production since 2025-11). AI-002: predictive maintenance pilot (since 2026-04). AI-003 (public generative AI tools) is covered in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; NIST AI 600-1 for AI-003 only |
| Assessor / date | IT Manager with the Production Planning Manager, Maintenance Manager, and Controls Engineer; completed 2026-08-26 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owners:**
  - AI-001: Production Planning Manager.
  - AI-002: Maintenance Manager, with the Controls Engineer for the historian connection.
  - The IT Manager keeps the AI inventory and the approved-tools list.
- **Decision authority:** the VP Operations for Medium-tier use cases; the President for any use case re-tiered High.
- **Policies that apply:**
  - POL-05 4.8: approved tools only, human review of AI output, no Restricted data or FCI in public tools.
  - POL-04 4.11: no Restricted data or FCI in unapproved AI tools.
  - POL-01 4.7: AI service vendors are Tier 1 suppliers and need security terms and an annual review.
  - POL-02 4.8: supplier connections into the plant go through the company remote access gateway.
- **Scale for a Small company:** there is no AI committee. The owners above and the IT Manager review AI use cases quarterly with the security review (POL-01 roles). A new AI use case, a new data source, or a new connection to the plant needs a short assessment like this one before go-live.
- **What went wrong before this assessment:** both AI-001 and AI-002 went live without a risk review, and the AI-002 connector opened a new outbound internet path from the plant historian (scenario-facts gap 14; P01 R-023).

## 2. MAP
### 2.1 AI-001 Demand forecasting
| Item | Description |
|---|---|
| Purpose and intended use | Forecast monthly unit demand by product family (pad-mounted kVA classes and power transformer MVA classes) 3 to 12 months ahead. The forecast feeds the APS capacity plan, raw material purchasing (core steel, copper, oil), and the proposal for reserved storm-restoration slots |
| Users / operators | Production Planning Manager and 2 planners; Supply Chain Manager (purchasing) |
| Affected parties | The 38 utility customers and developers, through the production slots and lead times they are offered. Utilities rely on these slots to restore power after storms. No individual people are affected |
| Data | Inputs: 6 years of ERP order history by customer and segment (investor-owned, municipal, cooperative, developer), backlog, and published regional hurricane-season outlooks. Nightly extract from the ERP; no personal data. The federal contract's delivery schedule (FCI) is in the order history and stays inside the company's cloud tenant |
| Build or buy | Built by the company on the cloud tenant's managed machine learning service, using a standard time-series method, with help from an outside analytics contractor in 2025 |
| Not intended | Pricing, credit decisions about customers, or automatic slot allocation without a planner's approval |

### 2.2 AI-002 Predictive maintenance pilot
| Item | Description |
|---|---|
| Purpose and intended use | Flag developing equipment faults early from historian data: vacuum pump and heater behavior on the vapor-phase drying oven and the 2 conventional ovens, and motor current and vibration on 4 of the 14 coil winding machines |
| Users / operators | Maintenance Manager and the 10 mechanics and electricians who act on alerts |
| Affected parties | Maintenance staff and oven operators (safety); customers (delivery), indirectly |
| Data | About 140 selected historian tags (temperatures, pressures, currents, vibration), sent every minute by a vendor connector on the historian. No personal data: operator ID tags are excluded from the tag list |
| Build or buy | Buy: vendor SaaS with a vendor model trained on the company's 18 months of historian data plus the vendor's fleet data |
| Not intended | Any control action on plant equipment. The connector is read-only, and the vendor confirmed in writing that it cannot write to the historian or controllers. Not for judging individual operators' or mechanics' performance |

### 2.3 Applicable laws and rules
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules for critical manufacturing | None found | The vertical profile lists no sector AI rules. The NIST AI RMF Critical Infrastructure Profile is only a concept note (2026-04-07); watch it |
| State consequential-decision AI laws (for example Colorado SB26-189) | No | Neither use case makes or substantially informs decisions about individuals (employment, credit, housing, insurance, education, health care, government services, legal). The company operates in Florida only |
| FAR 52.204-21 | **Yes, narrowly** | FCI (the federal delivery schedule) is in AI-001's training data. It stays in the company's own cloud tenant, which is a covered contractor information system already in scope (P03 G-063). AI-003 public tools must not receive FCI ((b)(1)(iii); P03 G-066) |
| FTC Act Section 5 | Indirectly | Governs the AI-002 vendor's accuracy and security claims. Keep the claims the company relied on in the procurement file |
| Utility Supplier Cyber Security Addenda | No | Neither use case touches products or services supplied to utilities. AI-001 does affect storm-slot allocation, which is a business commitment, not a contract security term |
| EAR (C-CRITICAL-MFG-R03) | No new issue | AI-002 sends process data, not design technology, and the products are EAR99 |
| NIST SP 800-82 Rev. 3 (benchmark) | Yes | The AI-002 connector is a new external connection from the OT network (P03 G-030, G-046) |

## 3. Risk tier
Using the repository rubric (`00_universal/projects/P10_ai-governance/README.md`):

**AI-001: Medium.** It influences business decisions (capacity, purchasing, and storm-slot proposals), and a human approves the monthly plan. It is not High:
- It makes no decision about an individual.
- It does not operate critical infrastructure. Its effect on grid restoration is indirect, through production slots that a planner approves.

**AI-002: Medium.** It influences maintenance decisions, and a human decides every action. It is not High because:
- it is advisory only and cannot write to equipment;
- the time-based preventive maintenance schedule continues unchanged, so a missed alert does not remove any existing safeguard (P01 R-025, accepted Low on that basis).

**Escalation triggers (re-tier to High and re-assess):**
- AI-002 is used to extend or skip preventive maintenance on the drying ovens, vacuum system, or oil fill station. This would affect physical safety.
- Any AI-002 output is used to evaluate individual workers. This would be an employment decision.
- AI-001 slot proposals are applied automatically without planner approval, or are used to set customer-specific prices or terms.
- Any AI tool is given write access to plant systems.

## 4. MEASURE
### 4.1 AI-001 Demand forecasting (back-test and 10 months of production, 2025-11 to 2026-08)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Mean absolute percentage error (MAPE) at a 3-month horizon, by product family. Target: 15% or less | Distribution units 11%; power transformers 24% (few, lumpy orders) | **Partial.** Power forecast not reliable enough for purchasing |
| Safe | Storm-slot proposals checked against the prior 3 seasons before approval | Planner approval recorded for every monthly plan | Yes |
| Secure and resilient | Service identity with read-only access to a nightly extract (P04); model and data in the inventory; retraining under change control | Access design good; model not inventoried; retraining in 2026-03 had no change record | **Partial** |
| Accountable and transparent | Owner named; forecasts labeled as model output in the APS; model documentation (purpose, data, method, limits) | Owner named; labels present; no model documentation | **Partial** |
| Explainable and interpretable | Planners can see the drivers of each family's forecast | Driver view available in the ML service; planners not trained on it | Partial |
| Privacy-enhanced | No personal data in inputs | Contact names and emails excluded from the extract | Yes |
| Fair, with harmful bias managed | **Bias test:** signed forecast error (under- or over-forecast) by customer segment over 10 months. Flag if a segment's under-forecast exceeds the investor-owned baseline by more than 5 percentage points | Investor-owned 3% under; **municipal 14% under; cooperative 12% under** | **No.** Disparity flagged |

**Bias finding (P01 R-024).** Municipal and cooperative utilities order in smaller, irregular lots, so the model under-forecasts them. Because slot proposals follow the forecast, these utilities were offered fewer reserved storm slots and longer lead times. They are often the smallest utilities with the least spare inventory. This is a harmful bias against a customer group, and it matters for grid restoration.

### 4.2 AI-002 Predictive maintenance pilot (2026-04 to 2026-08)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Precision (confirmed faults / alerts) of 50% or more; recall of known failures in back-test of 70% or more | Precision: 9 alerts, 5 confirmed (56%). Missed one vacuum pump seal failure in July; caught by the scheduled inspection | **Partial** |
| Safe | Advisory only; no write path; preventive maintenance unchanged | Vendor written confirmation; connector account is read-only; schedule unchanged | Yes |
| Secure and resilient | Connector path reviewed; vendor security report reviewed; data-use and deletion terms in the contract | Connector opens an outbound internet path directly from the historian on the plant network; no vendor SOC 2 report reviewed; click-through terms only | **No** |
| Accountable and transparent | Every alert reviewed by the Maintenance Manager and closed with a work order or a reason | 9 of 9 alerts closed with a record | Yes |
| Explainable and interpretable | Alert shows the contributing tags and trend | Available for oven alerts; winder alerts show a score only | Partial |
| Privacy-enhanced | No personal data sent; tag list reviewed | Operator ID tags excluded; tag list approved by the Controls Engineer | Yes |
| Fair, with harmful bias managed | **Coverage test:** back-test recall by equipment group (newer versus older winding machines; vapor-phase versus conventional ovens). Flag if any group's recall is more than 20 points below the best group | Newer winders 75%; **older winders 40%**; ovens 67% | **No.** Coverage gap flagged |

**Coverage finding.** The model has little data for the older winders, so it misses their faults more often. If maintenance staff come to trust the tool, older machines would get less attention. Time-based maintenance must stay in place for them.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:**
  - The Production Planning Manager approves every monthly plan.
  - **Storm slots are allocated by a written human rule, not by the forecast alone.** Each addendum utility and each cooperative or municipal customer keeps a minimum reserved allocation based on its installed base and the prior 3 seasons. The forecast can add slots but cannot reduce a customer below its minimum.
  - Power transformer purchasing uses the planner's judgment, with the forecast shown as input only, until MAPE is 15% or less.
- **AI-002:**
  - The Maintenance Manager decides every action.
  - No preventive maintenance task may be extended or skipped because of AI-002 (escalation trigger).
  - Mechanics can raise a work order regardless of the model.

**Monitoring:**
- AI-001: monthly MAPE and signed error by segment, reported to the VP Operations quarterly. Retraining goes through change control.
- AI-002: monthly precision and recall and missed-failure reviews.
- Both use cases are reviewed every quarter in the security review.

**Security actions (with P01 and P07):**
- Move the AI-002 connector to the planned OT DMZ, reading a one-way replica of historian data, so the plant network has no direct internet path (P01 R-023, with POAM-001).
- Add the AI-002 vendor to Tier 1 supplier review (POL-01 4.7). Obtain its SOC 2 report or questionnaire. Sign terms covering data use, no training on company data for other customers without consent, deletion at exit, and incident notice.
- Add AI-001's model, training data, and job to the inventory (P04 finding 6).

**Incident handling:**
- A security incident at the AI-002 vendor or in the ML service follows P08. Disconnecting the historian connector is a documented isolation point.
- A harmful forecast error (for example a storm-slot shortfall) is handled as a quality issue by the Production Planning Manager and recorded in the risk register.

**Decommissioning:**
- AI-002: stop the pilot and require deletion of company data if the connector cannot be moved into the DMZ by 2027-03-31, or if the vendor will not sign data-use terms by 2026-12-31.
- AI-001: suspend forecast-driven slot proposals if the segment bias flag persists for two quarters after the fix.

## 6. Decision
**AI-001: approve with conditions.** VP Operations, 2026-09-04. Conditions:
1. The minimum storm-slot allocation rule is in force before the 2026 storm-order review (by 2026-10-15).
2. Segment error monitoring is in place by 2026-12-31 (P01 R-024), and the model is retrained with segment features. The bias test is rerun after retraining.
3. Model documentation and a change record for each retraining, from 2026-10.

**AI-002: continue the pilot with conditions; no expansion.** VP Operations, 2026-09-04. Conditions:
1. Vendor terms and a security review by 2026-12-31.
2. The connector moves into the OT DMZ by 2027-03-31 (P01 R-023).
3. Preventive maintenance stays unchanged.
4. Before expanding to more winders or ovens, the older-winder recall must reach 60% or more.

## 7. AI-003 Public generative AI tools
Engineers have pasted design calculations into public generative AI tools (P01 R-013). The generative AI risks most relevant here, from NIST AI 600-1, are:
- **information security and intellectual property:** trade-secret designs and FCI leave company control;
- **confabulation:** plausible but wrong engineering answers.

Decision:
- Public tools are **prohibited for Restricted data and FCI** (POL-04 4.11, POL-05 4.8), and web filtering blocks unapproved AI sites by 2026-10-31.
- An enterprise generative AI tool with no-training and data retention terms is being evaluated for approval, for **Internal and Public data only**.
- Any output used in a design, quote, or customer document must be reviewed by a qualified person (POL-05 4.8).

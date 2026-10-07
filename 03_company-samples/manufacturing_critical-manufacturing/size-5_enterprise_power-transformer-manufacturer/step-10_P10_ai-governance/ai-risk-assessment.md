# AI Governance Risk Assessment: Enterprise AI Portfolio, Demand Forecasting, and Predictive Maintenance

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded power and distribution transformer manufacturer) |
| Tier / Vertical | Enterprise / Critical Manufacturing |
| Scope | Enterprise AI portfolio (14 use cases in `ai-use-case-inventory.csv`), with full assessments of AI-001 demand forecasting (section 5) and AI-002 predictive maintenance (section 6). The registry default "demand forecasting and predictive maintenance" is kept and split into two use cases because at this size they have different owners, data, and risks |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for the generative use cases (section 7); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Technology Officer), portfolio review meeting of 2026-08-26; GRC team prepared the review; data science lead ran the tests |
| Decision | Executive risk committee, 2026-09-08 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 14 |
| Risk tier | High 2, Medium 10, Low 2 |
| Status | In production 11, Pilot 2, Suspended 1 |
| Committee review complete | 9 of 14 |
| Not yet reviewed | 5: AI-006, AI-010, AI-011, AI-012, AI-014 (all due 2026-11-30, POAM-020) |
| Use cases that can affect physical safety or critical infrastructure operations | AI-003 (High); AI-002 if it were used to change maintenance intervals (proposal refused) |
| Use cases that make or inform decisions about individuals | AI-006 (employment; suspended) |

**Main findings:**
- Five use cases run without committee review. Four arrived as vendor features switched on inside existing products (AI-006, AI-010, AI-011, AI-014), and one (AI-012) was enabled by the SOC as a tooling upgrade. AI-006, a High-tier employment tool, was switched on by the HR software vendor and has been disabled.
- AI-002 has a proposal to extend preventive maintenance intervals on the vapor-phase drying ovens. That would make it a safety-affecting, High-tier use. The committee refused the change (section 6).
- AI-001 under-forecasts municipal and cooperative utilities, which reduces the storm-restoration slots they are offered (R-045).
- AI-003 finds failing transformers made by other manufacturers less reliably than company units (R-046), and its model releases are not formally validated (P09 PI1.3).

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly.

**Members:** Chief Technology Officer (chair); CISO; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce and HR tools); Vice President, Environmental Health and Safety; Vice President, Manufacturing Engineering; Director of OT Security; Chief Supply Chain Officer; Corporate Director of Quality; and the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee. Safety-affecting uses also need the Vice President, Environmental Health and Safety and a management-of-change review | Validation on company data; bias or coverage testing; impact assessment; human review design; notice to affected people or customers; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; security and data review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.6; STD-05.3). Since 2026-09, procurement and IT change management block AI features that have no inventory ID, and vendor release notes for tier-1 SaaS are screened monthly for new AI features. The GRC team owns the inventory.

**Policies:** POL-04 4.9 (no Restricted or Confidential data in an AI tool without committee approval and a contract that bars training on company data); POL-05 4.6 (approved tools only; human review; no AI-driven changes to maintenance intervals, safety settings, or employment decisions without committee approval); POL-01 4.14 (secure development for firmware, which covers AI-assisted code); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use and for AI-001 and AI-002; annual re-review of every use case.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules for critical manufacturing | None found | The vertical profile lists no sector AI rules |
| Federal equal employment opportunity laws (Title VII disparate impact, ADA, ADEA) | Yes, for AI-006 | Applicant ranking can produce adverse impact. Counsel reviews an adverse impact analysis before any re-enable |
| State and local AI or automated employment decision laws (for example in Colorado, Illinois, and New York City) | No | The company has no operations or employees in those places. Counsel tracks new state AI laws in the six states where it operates |
| FAR 52.204-21 | Yes, narrowly | FCI (federal delivery schedules) is in AI-001 training data and stays in the enterprise data platform, a covered contractor information system. AI-007, AI-008, and AI-010 must not receive FCI (P03 G-110, G-111) |
| Utility Supplier Cyber Security Addenda | Yes, for AI-013; context for AI-003 | AI-assisted code ends up in TMU firmware and configuration software supplied to utilities (vulnerability disclosure and integrity terms, addendum secs. 4 and 5). AI-003 is part of SL-1, governed by the subscription agreements |
| SL-1 subscription agreements and SOC 2 Processing Integrity | Yes, for AI-003 | The 24-hour advisory commitment and the Processing Integrity criteria added for 2027 (P09) |
| FTC Act Section 5 | Indirectly | Accuracy of claims made to FMS subscribers about AI-003 and of vendor claims the company relies on |
| SEC disclosure rules | Indirectly | AI statements in investor materials and in the Item 106 discussion must match how AI is actually used; Investor Relations checks them with the committee |
| EAR (C-CRITICAL-MFG-R03) | No new issue | AI-004 and AI-013 process design data and source code that are EAR99; contracts keep processing in the United States |
| NIST SP 800-82 Rev. 3 (benchmark) | Yes, for AI-002 | Plant data reaches the cloud only through the read-only historian replica in each OT DMZ; no AI tool has a path into plant control systems (P04) |
| Company process safety and management-of-change procedures | Yes, for AI-002 | Any change to maintenance on drying ovens and vacuum oil systems is a process safety change |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Demand forecasting feeding the capacity plan, purchasing, and storm-restoration slots | Medium | In production | Reviewed 2025-11-12; re-reviewed 2026-08-26 |
| AI-002 | Predictive maintenance pilot (drying ovens, vacuum oil processing, winders at P2, P4, P5) | Medium (High if used to change maintenance intervals) | Pilot | Reviewed 2026-03-11; re-reviewed 2026-08-26 |
| AI-003 | FMS condition analytics driving advisories to utilities (SL-1) | High | In production | Reviewed 2025-09-17; re-reviewed 2026-08-26 |
| AI-004 | Design optimization assistant for power transformer cores and windings | Medium | In production | Reviewed 2025-12-03 |
| AI-005 | Computer-vision weld and coil inspection at P1 and P3 | Medium | In production | Reviewed 2026-01-21 |
| AI-006 | Applicant screening and ranking (applicant tracking SaaS feature) | High | Suspended | Not reviewed (due 2026-11-30) |
| AI-007 | Quote and proposal drafting assistant | Medium | In production | Reviewed 2026-02-18 |
| AI-008 | Enterprise generative AI assistant | Medium | In production | Reviewed 2025-10-08 |
| AI-009 | Supplier delivery risk prediction | Medium | In production | Reviewed 2026-04-15 |
| AI-010 | RFQ specification extraction (ERP generative AI feature) | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-011 | Accounts payable invoice capture and matching | Low | In production | Not reviewed (due 2026-11-30) |
| AI-012 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) |
| AI-013 | Code assistant for TMU firmware and configuration software | Medium | In production | Reviewed 2026-05-20 |
| AI-014 | APS scheduling optimizer | Medium | Pilot (P3) | Not reviewed (due 2026-11-30) |

**Tiering notes:**
- **AI-003 is High** because utilities use its advisories to decide how to load, inspect, or remove grid transformers, so a miss can contribute to an outage. A reliability engineer reviews every high-severity alert, but a missed alert has no human backstop.
- **AI-002 stays Medium** only while it is advisory and the fixed maintenance schedule is unchanged. Using it to extend or skip preventive maintenance would make it High.
- **AI-004 and AI-013 are Medium** because every design and every code change passes an independent human review, design review or peer review, and testing before it reaches a product. Removing that review would re-tier them to High.
- **AI-006 is High** because it ranks job applicants.

## 5. Full assessment: AI-001 demand forecasting
### 5.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Forecast monthly demand by product family (single-phase and three-phase distribution kVA classes; power transformer MVA and voltage classes) 3 to 12 months ahead. The forecast feeds the APS capacity plan across the 7 plants, purchasing of grain-oriented electrical steel, copper, and oil, and the proposal for reserved storm-restoration slots each hurricane season |
| Users | Central planning team (14 planners); purchasing; plant managers |
| Affected parties | About 650 utility customers and other customers, through the production slots and lead times they are offered. Utilities rely on reserved slots to restore power after storms. No individual people are affected |
| Data | 6 years of ERP order history by customer segment, backlog, federal delivery schedules (FCI), and published hurricane-season outlooks. Nightly extract to the enterprise data platform through a read-only service identity; no personal data |
| Build or buy | Built by the company data science team on Cloud provider B AI services |
| Not intended | Pricing, customer credit decisions, or automatic slot allocation without planner approval |

### 5.2 MEASURE (back-test and 10 months of production, 2025-11 to 2026-08)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Mean absolute percentage error (MAPE) at a 3-month horizon by product family. Target: 15% or less | Distribution 9%; power transformers 19% (few, lumpy orders) | **Partial.** Power forecast not reliable enough to drive purchasing alone |
| Safe | Storm-slot proposals checked against the prior 3 seasons before approval | Planner approval recorded for every monthly plan | Yes |
| Secure and resilient | Read-only service identity; model and data in the inventory; retraining under change control | All in place since 2026-03 | Yes |
| Accountable and transparent | Owner named; forecasts labeled as model output in the APS; model documentation (purpose, data, method, limits) | All in place | Yes |
| Explainable and interpretable | Planners can see the drivers of each family's forecast | Driver view available; 9 of 14 planners trained | Partial |
| Privacy-enhanced | No personal data in inputs | Contact names and emails excluded from the extract | Yes |
| Fair, with harmful bias managed | **Bias test:** signed forecast error by customer segment. Flag if a segment's under-forecast exceeds the investor-owned baseline by more than 5 percentage points | Investor-owned 2% under; federal power customers 4% under; developers 3% over; **municipal 11% under; cooperative 9% under** | **No.** Disparity flagged (R-045) |

**Bias finding (R-045).** Municipal utilities and cooperatives order in smaller, irregular lots, so the model under-forecasts them. Slot proposals follow the forecast, so these utilities were offered fewer reserved storm slots and longer lead times, although they are often the utilities with the fewest spare units. This is a harmful bias against a customer group, and it matters for grid restoration.

### 5.3 MANAGE
- **Human in the loop:** the central planning manager approves every monthly plan. **Storm slots are allocated by a written human rule**: each utility keeps a minimum reserved allocation based on its installed base and the prior 3 seasons. The forecast can add slots but cannot reduce a customer below its minimum (in force for the 2026 storm-order review since 2026-09-15).
- **Model fix:** retrain with segment features and order-size patterns by 2027-01-31; rerun the bias test; power transformer purchasing uses planner judgment with the forecast as input only until MAPE is 15% or less.
- **Monitoring:** monthly MAPE and signed error by segment; quarterly report to the committee.
- **Incidents:** a storm-slot shortfall caused by the forecast is handled as a quality issue by the Chief Supply Chain Officer and recorded in the risk register; a security incident in the data platform follows P08.
- **Decommissioning:** forecast-driven slot proposals are suspended if the segment bias flag persists for two quarters after retraining.

## 6. Full assessment: AI-002 predictive maintenance pilot
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Flag developing faults early: vacuum pump, heater, and condenser behavior on vapor-phase drying ovens, vacuum oil processing skids, and motor current and vibration on winding machines at P2, P4, and P5 |
| Users | Maintenance Director (corporate), plant maintenance planners, and mechanics and electricians who act on alerts |
| Affected parties | Maintenance staff and operators (safety); customers (delivery), indirectly |
| Data | About 1,900 historian tags read from the read-only historian replica in each plant's OT DMZ and sent to the enterprise data platform; work order history from the maintenance system. Operator ID tags excluded |
| Build or buy | Built by the company data science team, using OEM failure-mode data under the OEM service agreements |
| Not intended | Any control action on plant equipment (no write path exists); changing preventive maintenance intervals; judging individual workers' performance |

### 6.2 MEASURE (pilot 2026-02 to 2026-08)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Precision (confirmed faults / alerts) of 50% or more; back-test recall on known failures of 70% or more | Precision 61% (31 of 51 alerts confirmed); recall 72% overall. Missed 2 vacuum pump seal failures at P4, both caught by scheduled inspection | **Partial** |
| Safe | Advisory only; no write path; preventive maintenance unchanged | Read-only replica path confirmed by the Director of OT Security; schedule unchanged | Yes |
| Secure and resilient | Data path through the OT DMZ replica only; model and pipeline under change control | In place (P04) | Yes |
| Accountable and transparent | Every alert closed with a work order or a reason | 51 of 51 alerts closed with a record | Yes |
| Explainable and interpretable | Alert shows contributing tags and trend | Available for ovens and vacuum skids; winder alerts show a score only | Partial |
| Privacy-enhanced | No personal data; tag list approved by controls engineering | Operator ID tags excluded | Yes |
| Fair, with harmful bias managed | **Coverage test:** back-test recall by equipment group. Flag if a group's recall is more than 20 points below the best group | Vapor-phase ovens 78%; vacuum oil skids 74%; newer winders 76%; **older winders 41%** | **No.** Coverage gap flagged |

**Coverage finding.** The model has little data for older winding machines and misses their faults more often. If staff came to trust the tool, older machines would get less attention, so time-based maintenance stays in place for them.

### 6.3 The interval extension proposal (refused)
In 2026-07 the P4 maintenance team proposed extending vacuum pump and heater preventive maintenance on two vapor-phase drying ovens from 4 to 8 weeks, citing AI-002 health scores. The committee refused it on 2026-08-26:
- It would turn AI-002 into a safety-affecting use (High tier): a vacuum or heater failure during a drying cycle can cause a fire or ruin a large power transformer (R-043, High).
- The model missed 2 vacuum pump seal failures in the pilot, and recall on safety-relevant failure modes has not been measured separately.
- No management-of-change or process hazard review had been done.

**Conditions before any future proposal:** 12 months of monitoring with recall of 90% or more on safety-relevant failure modes; a management-of-change review signed by the Vice President, Environmental Health and Safety; OEM concurrence; a staged trial on one oven with independent inspection; and executive risk committee approval as a High-tier use.

### 6.4 MANAGE
- **Human in the loop:** the plant maintenance planner decides every action; mechanics can raise a work order regardless of the model; no preventive maintenance task may be extended or skipped because of AI-002 (POL-05 4.6).
- **Monitoring:** monthly precision and recall; review of every missed failure; quarterly report to the committee.
- **Security:** the replica path stays one-way; AQ-01 is excluded until its OT DMZ is live (POAM-004).
- **Incidents:** a missed failure that causes damage or a near miss is investigated by Environmental Health and Safety with the data science lead; a security event in the data path follows P08, and cutting the historian replica feed is a documented isolation point.
- **Decommissioning:** the pilot stops if the replica path is ever bypassed, or if recall on ovens falls below 60% for two consecutive months.

## 7. Generative AI uses (NIST AI 600-1)
AI-007, AI-008, AI-010, and AI-013 use generative models. The AI 600-1 risks that matter most here:
- **Information security and intellectual property:** designs, customer drawings, firmware source, and FCI leaving company control. Controls: approved tenants with no-training and retention terms; Restricted data and FCI barred from AI-007, AI-008, and AI-010 (POL-04 4.9); unapproved public tools blocked at the web gateway since 2025 (R-020); DLP alerts monthly.
- **Confabulation:** plausible but wrong ratings, clauses, or code. Controls: a qualified person reviews every output used in a design, quote, customer document, or product (POL-05 4.6); AI-010 extracted fields are checked by application engineers; AI-013 code passes peer review, static analysis, and the signed build pipeline.
- **Value chain and component integration:** vendor model changes arrive without notice. Controls: AI vendors are Tier 1 suppliers; contracts require notice of material model changes; monthly screening of vendor release notes.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use and AI-001 and AI-002 report quarterly performance and fairness or coverage metrics (inventory column `monitoring`); a threshold breach triggers re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as SOC, quality, or safety events and follow P08 where security or data is involved.
- **Third parties:** AI vendors are Tier 1 in the vendor program (STD-01.3); contracts bar training on company data and require notice of model changes.
- **Customers:** FMS subscribers are told which analytics are model-based and their known limits (AI-003 coverage of non-company units).
- **Decommissioning:** a use is retired if it fails monitoring thresholds twice or its vendor changes data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the AI governance committee's recommendation of 2026-08-26:
1. **AI-001: approved to continue with conditions.** Minimum storm-slot allocation rule in force (done 2026-09-15); retraining with segment features and a rerun bias test by 2027-01-31; planner judgment for power transformer purchasing until MAPE is 15% or less (R-045).
2. **AI-002: continue the pilot with conditions; no expansion; interval extension refused** (section 6.3; R-043). Before expansion to more plants, older-winder recall must reach 60% or more.
3. **AI-003: approved to continue with conditions.** Validation step and sign-off for every model release by 2027-03-31 (P09 PI1.3); quarterly sensitivity by manufacturer group and unit age (R-046); subscribers told of the lower coverage for non-company units in the next advisory guide.
4. **AI-006: stays disabled** until committee review and an adverse impact analysis are complete (R-044, treatment Avoid).
5. **AI-010, AI-011, AI-012, AI-014:** may continue in current scope until committee review by 2026-11-30; no expansion (POAM-020; R-047).
6. **Intake:** the procurement and change management block on unregistered AI features stays in force, with monthly screening of tier-1 SaaS release notes.

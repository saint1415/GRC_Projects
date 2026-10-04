# AI Governance Risk Assessment: Enterprise AI Portfolio and Container and Berth Scheduling Optimization

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-port marine cargo terminal operator; 8 terminals in FL, GA, SC and TX) |
| Tier / Vertical | Enterprise / Transportation and Warehousing |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 container and berth scheduling optimization in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for the generative use cases (AI-008, AI-010, AI-011); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Vice President, Data and Analytics), portfolio review of 2026-08-19; GRC team prepared the review |
| Decision | Executive risk committee, 2026-09-08 (section 9) |
| Related risks and POA&M | P01 R-028, R-029, R-030, R-043; POAM-025 |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 3, Medium 8, Low 1 |
| Status | In production 10 (AI-001 also piloting at 2 more terminals), Pilot 1, Suspended 1 |
| Committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-009, AI-010, AI-011, AI-012 (all due 2026-11-30) |
| Use cases that can affect physical safety or critical infrastructure operations | 2 High (AI-001, AI-004); 3 Medium connected to OT or the gate (AI-002, AI-003, AI-006) |
| Use cases designated or connected as critical IT or OT under Subpart F | AI-001, AI-002, AI-004 and AI-007 designated; AI-003 and AI-006 interconnected with critical OT |

**Main findings:** AI-001 is in production at 3 terminals, but the independent constraint check that blocks unsafe plans runs only at T-01, and appointment-slot fairness has never been tested. Four use cases run without committee review, including a generative chatbot that talks to customers (AI-011) and a High-tier employment feature (AI-012, now suspended). Vendor AI embedded in OT (AI-004, AI-006) is governed through OEM change notices rather than model documentation, which is acceptable only while the vendor's safety systems stay independent of the model.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-09 (P01), which the board risk committee reviews quarterly.

**Members:** Vice President, Data and Analytics (chair); CISO; Director of Maritime Cybersecurity (CySO); Chief Compliance Officer; General Counsel's delegate; Director of Enterprise Planning; Director of OT Engineering; Vice President, Maritime Security; Chief People Officer (for workforce and HR tools); Vice President, Labor Relations (for labor tools); one Terminal General Manager on a rotating basis. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Impact assessment; independent safety constraints where the output can reach equipment; fairness testing where people or companies are affected; security review and Subpart F designation by the CySO; notice to affected parties; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; security and data review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside vendor products and OEM equipment, must be registered before use (POL-05 4.7; STD-05.3). Procurement and change management block AI features without an inventory ID. The GRC team owns the inventory; the CySO adds each AI system to the Subpart F inventory with its critical IT or OT designation (101.650(b)(3)).

**Policies:** POL-04 4.8 (no Restricted, Confidential or SSI data in AI tools without committee approval and no-training terms); POL-04 4.9 (no driver license numbers in analytic datasets or AI vendors); POL-05 4.7 (approved tools only); POL-01 4.8 (vendor terms, including notice of vulnerabilities and incidents without delay); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review of every High-tier use case; annual re-review of every use case; re-review on any escalation trigger.

**Why 4 use cases lack review.** AI-010 and AI-012 arrived as vendor feature releases before the procurement block existed (2026-03). AI-009 was built by an operations analyst outside the data science team. AI-011 started as a pilot under a marketing budget. The committee set review dates for all four (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| USCG cyber rule, 33 CFR Part 101 Subpart F (N48-49-R01) | **Yes** | AI systems connected to the TOS, gates or OT must be in the inventory with their critical IT or OT designation (101.650(b)(3)); their vendors fall under the supply chain measures (101.650(f)(1)-(3)); their software must be on the approved list (101.650(b)(1)) |
| Shipping Act, 46 U.S.C. 41106 | **Yes**, for AI-001 and AI-005 | A marine terminal operator may not "give any undue or unreasonable preference or advantage or impose any undue or unreasonable prejudice or disadvantage with respect to any person." Berth windows and appointment slots set with model help must be explainable on reasonable operational grounds. The Federal Maritime Commission administers the Act |
| OSHA marine terminal standards, 29 CFR part 1917 | Indirectly | The company stays responsible for safe cargo handling, whoever proposed the plan (AI-001, AI-003, AI-004) |
| Federal equal employment opportunity laws | Yes, for AI-012 | Title VII disparate-impact liability remains by statute, although EEOC technical assistance on AI selection tools has been withdrawn. Counsel reviews adverse impact before any re-enable |
| Texas Responsible AI Governance Act (HB 149), effective 2026-01-01 | Yes, limited | The company does business and deploys AI in Texas (T-07 pilot of AI-001; AI-012 for Texas applicants). Its private-sector duties are intent-based prohibitions (for example, AI developed with intent to unlawfully discriminate); disclosure duties apply to government agencies and health care providers, not to the company. Enforcement is by the Texas Attorney General |
| Colorado SB26-189 and similar state AI laws | No | The company does not operate in Colorado. Recheck if hiring expands to new states |
| FTC Act Section 5 | Indirectly | Accuracy of claims made to customers about AI-005 predictions and the AI-011 chatbot; vendor claims the company relies on |
| State breach laws | Yes, for data handling | Driver license numbers and identity or location data linked to a driver's name are personal information in many states (Florida worked example: Fla. Stat. 501.171), so they stay out of AI datasets (POL-04 4.9) |
| SEC Item 106 | Context | Material AI-related cyber risks are part of the risk management description |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Committee review | Subpart F designation |
|---|---|---|---|---|---|
| AI-001 | Container and berth scheduling optimization | High | In production (T-01, T-03, T-04); pilot (T-06, T-07) | Reviewed 2025-11-12; re-reviewed 2026-08-19 | Critical IT |
| AI-002 | Gate OCR | Medium | In production (T-01 to T-07) | Reviewed 2025-10-08 | Critical IT (SYS-02) |
| AI-003 | Crane and RTG predictive maintenance | Medium | In production (4 terminals) | Reviewed 2026-01-21 | Interconnected with critical OT |
| AI-004 | Automated stacking crane path planning and collision avoidance (T-01) | High | In production | Reviewed 2025-12-10 | Critical OT |
| AI-005 | Truck turn-time and gate queue prediction (SL-1) | Medium | In production | Reviewed 2026-02-18 | Not critical |
| AI-006 | Reefer monitoring anomaly detection | Medium | In production (5 terminals) | Reviewed 2026-03-18 | Interconnected with critical OT |
| AI-007 | Container damage detection from gate images | Medium | In production (T-01, T-04) | Reviewed 2026-05-13 | Critical IT (SYS-02) |
| AI-008 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-14 | Not critical |
| AI-009 | Longshore labor demand forecasting | Medium | In production (3 terminals) | Not reviewed (due 2026-11-30) | Not critical |
| AI-010 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) | Not critical |
| AI-011 | SL-1 customer service chatbot | Medium | Pilot (5% of sessions) | Not reviewed (due 2026-11-30; required before expansion) | Not critical |
| AI-012 | Applicant screening and ranking (HR SaaS feature) | High | Suspended | Not reviewed (due 2026-11-30) | Not critical |

**Tiering notes:** AI-001 is High because plans it proposes can put heavy or hazardous containers in the wrong place and, at T-01, approved yard plans drive automated stacking cranes; advisory mode does not lower the tier. AI-004 is High because it moves equipment near people, even though certified safety interlocks act independently. AI-009 stays Medium because it forecasts the number of gangs, not which workers are hired; using it to select or rank individual workers would re-tier it to High (employment). AI-007 is Medium because an inspector confirms every damage flag before it affects a claim.

## 5. Portfolio controls specific to a terminal operator
| Control | What the company does | Status |
|---|---|---|
| AI output never reaches equipment without an independent check | TOS constraint engine (hazardous segregation, stack weight and height, reefer plugs, crane availability) blocks violating plans before approval | At T-01 only; T-03 and T-04 by 2026-11-30, T-06 and T-07 before pilot expansion (POAM-025) |
| Vendor AI in OT | OEM change notices and safety cases reviewed by OT Engineering; vendor access through the gateway (POAM-002 for the T-01 automation vendor) | In place, except the gateway gap |
| Subpart F inventory | Every AI system connected to the TOS, gates or OT listed with its designation | Done for the 8 reviewed use cases; AI-009 to AI-012 at review |
| SSI and data rules | No SSI in AI tools except AI-010 under SOC data handling terms (under review); no driver license numbers in any AI dataset | AI-010 terms due at review |

## 6. MEASURE: fairness testing gap and plan
**Gap.** AI-001 allocates truck appointment slots at T-01, T-03 and T-04, but no one has tested whether smaller trucking companies get worse slots than large fleets without an operational reason. Batching appointments by fleet to reduce yard moves is a known way such a model can favor large fleets. Berth window allocations across the roughly 40 carrier services were tested in 2026-07 and were within threshold.

**Testing plan (POAM-025, first run by 2026-12-31, then quarterly):**
| Item | Plan |
|---|---|
| Question | Does AI-001 give some carriers or trucking companies worse berth windows or appointment slots without an operational reason (46 U.S.C. 41106)? |
| Groups compared | (1) Each carrier service. (2) Trucking companies by fleet size: fewer than 10 trucks, 10 to 49, 50 or more. (3) Terminal, to catch local configuration effects |
| Metrics | (1) Average hours between requested and recommended berth window per carrier service. (2) Share of appointment requests fulfilled in the requested 2-hour window, per fleet-size band and terminal |
| Thresholds | (1) No carrier service more than 2 hours worse than the average of all services. (2) No band more than 10 percentage points below the best band at any terminal. A breach triggers a root-cause review within 30 days |
| Legitimate factors | Vessel size, cargo volume, contracted berth windows, hazardous cargo handling limits and customs holds. A gap explained by these is recorded, not flagged |
| Data and owner | TOS appointment and berth history compared with the model's recommendations; run by the data science team; reviewed by the Director of Enterprise Planning and the Chief Compliance Officer |

## 7. Full assessment: AI-001 container and berth scheduling optimization
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Recommend berth windows and crane splits, yard slots for arriving containers (to reduce rehandles), and truck appointment slot allocations, to raise crane productivity and shorten truck turn times |
| Users | About 60 planners at the enterprise planning center and the terminals; customer service staff who publish appointment slots |
| Affected people and organizations | About 40 carrier services (berth windows); about 4,100 trucking companies and their drivers (appointment slots); longshore workers and equipment operators who work the plans (safety); at T-01, the automated stacking cranes that execute approved yard plans |
| Data | **Inputs:** vessel schedules, bay plans, container attributes (size, weight, reefer, hazardous class), yard inventory, equipment status, move history, appointments by trucking company ID. No driver names or license numbers. **Outputs:** recommended plans written to a TOS staging area. **Training:** in-house models retrained monthly on company move history in the Cloud provider B ML platform; no external training |
| Build or buy | Built in-house by the data science team; optimization plus machine-learning predictions; deployed through the pipeline with model registry approval (P04) |
| Deployment context | Advisory mode: nothing reaches equipment, VMTs or the appointment portal until a planner approves it in the TOS. Planning can run without AI-001 (P05 BP-06) |
| Not intended | Direct dispatch to cranes, RTGs or VMTs without approval; longshore labor ordering or assignment; pricing or demurrage. **Enabling any of these requires re-assessment** |

### 7.2 Risk tier
High (section 4). **Escalation triggers:** removing planner approval at any terminal; using AI-001 outputs for labor or pricing; adding automated execution beyond T-01; a change of model type; expanding production to T-06, T-07 or T-08 before the constraint check is live there.

### 7.3 MEASURE (2026-05-01 to 2026-07-31, production terminals)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | (a) Berth plans feasible as issued (tide, draft, crane availability) for at least 98% of calls. (b) Yard rehandles at least 8% below the planner-only baseline | (a) 98.6% of 412 calls. (b) Rehandles 9% lower at T-03 and T-04, 12% lower at T-01 | Yes |
| Safe | Hard-constraint violations reaching an approved plan must be 0 | 0 reached execution. The T-01 constraint check blocked 11 violating recommendations; at T-03 and T-04 planners caught 6 (4 hazardous segregation, 2 stack weight) by review alone | **No.** At T-03 and T-04 the only control is planner vigilance |
| Secure and resilient | Security review; least-privilege service identity; model registry approval; fallback | Reviewed by the CISO and CySO 2025-11; scoped service identity with write access to the staging area only; fallback to manual planning tested | Yes |
| Accountable and transparent | Every approval or override recorded with the planner's name and a reason code | Reason codes captured at T-01 only; T-03 and T-04 record the approver but not the reason | **No** |
| Explainable and interpretable | Planner can see why a window or slot was chosen | Constraint and score explanations shown; planners rated berth explanations unclear 2 times in 10 | Partial |
| Privacy-enhanced | Minimum data; no driver identifiers | Trucking company IDs only; no driver data | Yes |
| Fair, with harmful bias managed | Section 6 plan | Berth windows within threshold; appointment slots not tested | **No** (not tested) |

### 7.4 MANAGE
- **Human in the loop:** AI-001 proposes; a planner approves. A second planner checks any plan with hazardous cargo. No plan reaches equipment, VMTs or the appointment portal without approval in the TOS.
- **Independent constraint check:** the TOS rule engine, not the model, enforces hazardous segregation, stack weight and height, reefer plug limits and crane availability. Due at T-03 and T-04 by 2026-11-30 and at T-06 and T-07 before pilot expansion (POAM-025).
- **Reason codes** for every changed recommendation at all terminals by 2026-11-30.
- **Kill switch:** the Director of Enterprise Planning or the SOC can disable the service identity at once; planning continues by hand (P05 BP-06).
- **Monitoring:** monthly feasibility, constraint blocks, overrides and reasons, and rehandles per terminal (P01 R-028); quarterly fairness tests (P01 R-029); complaints from carriers or trucking companies about berth windows or slots are logged against the model by customer service.
- **Change control:** retraining and model changes go through the model registry with data science review; material changes (new inputs, new objective weights, new terminal) need committee approval.
- **Incidents:** an unsafe plan that reaches the yard is a safety event under the operations manual, reported to the Terminal General Manager and the FSO; suspicious activity through the service identity follows the P08 runbook, including the 6.16-1 report if the TOS is affected.
- **Decommissioning triggers:** any constraint violation that reaches execution; feasibility below 95% for two months in a row; an unexplained fairness breach that persists after one fix.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case has quarterly performance and safety or fairness metrics (inventory column `monitoring`) reported to the committee; drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, fairness finding, data misuse) are logged as SOC or safety events and follow P08 where security is involved.
- **Third parties:** AI vendors with access to company data or OT are tier-1 in the vendor program; contracts require notice of material model changes and of vulnerabilities and incidents without delay (101.650(f)(2)); no training on company data.
- **Generative AI (AI 600-1):** AI-008 runs in an enterprise tenant with data loss prevention and no SSI; AI-010 and AI-011 get the same review (confabulation, information security, data privacy and human-AI configuration risks) at their committee reviews.
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice, lose vendor support, or change data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the AI governance committee's recommendation of 2026-08-19:
1. **AI-001:** approved to continue at T-01, T-03 and T-04 with conditions: constraint check and reason codes at T-03 and T-04 by 2026-11-30; first fairness test by 2026-12-31; **no production use at T-06 or T-07 until the constraint check is live there** (target 2027-01-31; POAM-025).
2. **AI-004:** approved to continue; the automation vendor's remote access moves to the gateway (POAM-002) and OT Engineering reviews every vendor model or safety-system change before deployment.
3. **AI-009 and AI-010:** may continue in current scope until committee review by 2026-11-30; no expansion. AI-010 must confirm SOC data handling terms at review.
4. **AI-011:** stays at 5% of SL-1 sessions until reviewed; it must disclose that customers are talking to an AI and offer a hand-off to staff.
5. **AI-012:** ranking stays disabled until committee review and an adverse impact analysis by counsel are complete.
6. **Inventory:** the CySO confirms the Subpart F designation of every AI system at each annual review and before the Cybersecurity Plans are submitted.

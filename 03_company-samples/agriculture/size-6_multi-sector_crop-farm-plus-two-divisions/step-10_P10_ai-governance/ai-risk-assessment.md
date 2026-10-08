# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Crop Farming, Food Processing, Farm Supply, corporate) |
| Tier / Vertical | Multi-Sector / Agriculture, Forestry, Fishing and Hunting |
| Scope | The group AI governance program (group standard and division use cases), with **computer-vision crop yield prediction (AI-001)** as the priority use case, and the regulator- and customer-specific rules for the two High-tier use cases in production or pilot (AI-006 portal prescriptions, AI-003 spray drones) and the proposed credit model (AI-007) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; the Generative AI Profile (AI 600-1) applies only to AI-008, because AI-001, AI-003, AI-004, and AI-006 are not generative models |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-28; presented to the board risk committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (10 use cases: 3 High, 5 Medium, 2 Low), built from AI tool discovery across SaaS discovery, procurement, the model registry and division AI owners' lists (EV-033), the yield model registry (EV-054), the portal release record (EV-070) and the drone fleet settings (EV-052); the `source_evidence` column names the source of each row. Not established: workforce use of public generative AI tools outside the approved tools (intake open request) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Group chief financial officer's delegate, Group VP Food Safety and Quality, and one leader from each division. Approves High-tier use cases, the approved-tools list, and model changes to priority use cases |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security requirements (model supply chain, data leakage, access to model services) |
| Group Chief Privacy Officer | Data-use reviews for grower, worker, and customer data (POL-04 4.7) |
| Group internal audit | Includes High-tier and financial-reporting AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-06; anchored in POL-01 4.13 from 2026-10-01)
1. **Register before use.** Every AI use case that supports decisions about people, controls physical equipment, feeds financial reporting, or is offered to customers is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, bias and accuracy testing, and quarterly monitoring reports.
3. **Change gate.** A new model version, new data source, new decision role, or new customer-facing claim triggers re-validation before release. For AI-001, the gate includes finance sign-off because estimates feed growing-crop valuations.
4. **Data use.** Grower, worker, and customer data may train models only where the terms allow it (POL-04 4.7); Restricted data never goes to unapproved tools (POL-04 4.9).
5. **Physical safety.** AI that can move equipment or apply products (AI-002 if automated, AI-003, AI-006) needs locked limits set by a qualified person and a human able to stop it.
6. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short in 2026.** The standard was adopted after AI-001 and AI-006 were already in production. AI-001 model versions were released without validation or change control (EV-054, EV-096; P01 GR-08), and AI-006 launched on 2026-03-01 without security, privacy, or validation review (P07 CM-4 and SA-11 findings; POAM-019).

## 2. MAP
### 2.1 Inventory
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Computer-vision crop yield prediction | Crop Farming | Medium | In production; continued with conditions (change control, validation, caps on commitments) |
| AI-002 | FMIS irrigation scheduling recommendations | Crop Farming | Medium | In production (recommendation mode only) |
| AI-003 | Spray drone spot spraying with on-board weed detection | Crop Farming | High | Pilot at 3 legacy farms; not approved for expansion |
| AI-004 | Optical sorting with machine vision on fresh-cut and peanut lines | Food Processing | Medium | In production at 4 fresh-cut plants and the peanut plant |
| AI-005 | Production volume forecasting for plant scheduling | Food Processing | Medium | In production; must consume only the validated AI-001 version |
| AI-006 | Grower Agronomy Portal AI variable-rate prescriptions | Farm Supply | High | In production since 2026-03-01; continued with conditions; new cooperative enrollments paused |
| AI-007 | Grower trade credit scoring to set limits and decisions on credit applications | Farm Supply | High | Proposed; not approved |
| AI-008 | Enterprise generative AI assistant for drafting and summarizing | Group | Medium | Pilot with 1,500 users |
| AI-009 | SOC alert triage scoring | Group | Low | In production |
| AI-010 | Coding assistant for portal engineers | Farm Supply | Low | Approved |

### 2.2 Priority use case: AI-001 computer-vision crop yield prediction
| Item | Description |
|---|---|
| Purpose and intended use | Estimate weekly marketable yield per block, 1 to 4 weeks ahead, from fruit and flower counts detected in drone orthomosaics |
| Who uses the output | **Crop Farming** crew planning and forward sales commitments to outside buyers; **Food Processing** production volume forecasts (AI-005) and grower intake planning; **Group finance** growing-crop estimates used in financial reporting |
| Affected people | Harvest crews (about 11,500 seasonal workers, about 9,000 of them H-2A workers), whose offered hours follow crew plans; buyers and Food Processing customers who receive committed volumes; investors who rely on the financial statements; people who appear incidentally in field images |
| Data | Inputs: orthomosaics from the imagery store, block boundaries, varieties, planting dates, historical block totals (never per-worker data). Outputs: block estimates with a confidence range and detection overlays |
| Build | In-house model on the group cloud; retrained each season; 4 versions released between 2025-11 and 2026-05 with no validation record |
| Not intended | Setting H-2A job order worker counts; cutting crew hours without review; evaluating individual workers; crop insurance or USDA program reporting; driving irrigation or application equipment |

**Applicable rules (AI-001):**
| Rule | Applies? | What it means |
|---|---|---|
| H-2A three-fourths guarantee, 20 CFR 655.122(i), and hours-offered records, 655.122(j)(1) | **Yes, indirectly** | Each H-2A worker must be offered hours equal to at least three-fourths of the workdays in the contract period, and hours offered are recorded. A forecast cannot lower that floor; crew plans built on over-estimates followed by short-notice cuts are the main harm to workers |
| SEC registrant financial reporting (N42-R07 context) | **Yes, indirectly** | Estimates feed growing-crop valuations used in the financial statements. Model changes are therefore changes to an input of internal control over financial reporting, which is why finance signs the change gate |
| Buyer agreements | Yes | Over-committed volumes must be reported within 24 hours when a shortfall is known (P08 matrix) |
| FTC Act Section 5 | No for AI-001 (internal use) | Applies to AI-006 claims instead |
| State AI laws (for example Colorado SB26-189) | No | No division does business in Colorado, and a yield estimate is not a consequential decision about a person. See `00_universal-framework/cross-sector/us-cross-sector-obligations.md` |

### 2.3 Other High-tier use cases: the rules that differ by division
| Use case | Rule or commitment | Implication |
|---|---|---|
| AI-006 portal prescriptions (Farm Supply) | FTC Act Section 5 (N42-R01) | Marketing says prescriptions "optimize input rates"; that claim needs substantiation (P03 FS-G15 not met) |
| AI-006 | Portal terms: grower data used only to provide the service | Training on pooled grower field data needs a data-use review and, if beyond the terms, grower consent (P03 FS-G13) |
| AI-006 | Portal terms: 72-hour cooperative incident notice | A model error that sends harmful prescriptions to many growers is treated as an incident for notice purposes |
| AI-006 | Physical effect | Prescriptions execute on growers' application equipment, so errors reach fields directly; this is why the council tiered it High under the rubric |
| AI-003 spray drones (Crop Farming) | 14 CFR Part 137 (agricultural aircraft operations, 137.1) and Part 107 as they apply | The operation's FAA requirements govern flights; the AI decides only where to spray inside an approved block |
| AI-003 | 40 CFR Part 170 (Worker Protection Standard) | Application exclusion zones and application records apply whether a person or a model triggers the nozzle |
| AI-007 credit scoring (Farm Supply, proposed) | ECOA and Regulation B: agricultural trade credit is business credit (12 CFR 1002.2); no discrimination on a prohibited basis (1002.4(a)); for trade credit, notice of the action within a reasonable time and a written statement of reasons if the applicant asks within 60 days (1002.9(a)(3)(ii)) | The model must produce specific, accurate reasons for adverse action, and its inputs and outcomes must be tested for disparate effects before any use |
| AI-004 optical sorting (Food Processing) | 21 CFR 117 and N11-R01 | Sorting settings are a process step; changes go through change control and are considered in the food defense reanalysis (POAM-015) |

## 3. Risk tiers (repository rubric)
- **High:** AI-003 and AI-006 (can affect physical operations: product application on fields) and AI-007 (substantial factor in credit decisions about individuals who personally guarantee).
- **Medium:** AI-001, AI-002, AI-004, AI-005, AI-008. Humans make the final decision, but outputs shape business decisions, worker hours, or customer-facing quality.
- **Low:** AI-009 and AI-010.

**Why AI-001 is Medium but the priority use case.** It makes no decision about a person and controls no equipment, so the rubric rates it Medium. The council made it the priority because its errors spread to three functions in two divisions and into financial reporting, it had no change control, and it indirectly shapes the hours offered to about 9,000 H-2A workers.

**Re-tier triggers:** using AI-001 to set job order worker counts or to cut hours without review (to High, Employment); enabling automatic irrigation in AI-002 (to High, Safety/CI); letting AI-006 export prescriptions outside agronomic ranges without approval (re-assessment); any automated credit decision by AI-007.

## 4. MEASURE
Results are from monitoring and audits between 2026-05 and 2026-08, recorded by the Group AI council (EV-096).

### 4.1 AI-001 yield prediction (2025-26 season, 26 weekly flights, about 1,900 block-weeks compared with harvest totals)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Mean absolute percentage error (MAPE) of 1-week-ahead block estimates; threshold 15% | Strawberries 10%; tomatoes 13%; peppers 14%; watermelons 23% (canopy hides fruit); peanuts not evaluated (below-ground crop; model uses canopy proxies, 19%) | **Partial:** watermelons and peanuts fail |
| Valid and reliable (drift) | Change in MAPE after each model version | Version 3 (2026-02) raised strawberry error from 9% to 12% for 5 weeks before anyone noticed | **No** (no release validation) |
| Fair, harmful bias managed | Signed error by subgroup: variety, region (ROC-1 to ROC-3), legacy versus acquired farms, season stage. Flag any subgroup whose mean error differs from the overall mean by more than 5 points | Overall strawberry bias +2%. New strawberry variety +13% (**flagged**); acquired farms +8% because of different row spacing (**flagged**); early season -11% (**flagged**) | **No.** Three subgroups flagged |
| Fair (worker impact) | Hours offered per worker across crews when plans change on a forecast; flag differences above 10% between crews in the same farm and week | 6 farm-weeks flagged at acquired farms, all after over-estimates; all crews stayed above the three-fourths guarantee | **Flagged** (process fix, not model) |
| Accountable and transparent | Each crew plan and sales commitment that used an estimate is logged with the model version | Logged for sales commitments; not for crew plans | **Partial** |
| Secure and resilient | Imagery store private; model service access limited to the data science team; training data lineage | Store private (P04); 9 data scientists with production deploy rights and no separation of duties | **Partial** |
| Privacy-enhanced | No worker detection; images with people deleted when not needed | Model does not detect people; no deletion rule for images with people | **Partial** |
| Financial reporting | Reconciliation of estimates used in growing-crop valuations to actual harvest, by quarter | Done by finance quarterly; no sign-off on model versions used | **Partial** |

### 4.2 AI-006 portal prescriptions
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Share of prescriptions with any zone rate outside the agronomic range for the crop and soil test (sample of 400 prescriptions) | 3.5% outside range; 4 of those above label-equivalent maximums for the product | **No** |
| Safe | Hard limits on exported rates | None before 2026-09; added as a condition | **No** |
| Fair, harmful bias managed | Error by soil region and by farm size (growers under 500 acres versus larger) | Out-of-range share 6.1% in the coastal plain region versus 2.4% elsewhere (thin training data) | **Flagged** |
| Privacy-enhanced | Training data use consistent with portal terms | Pooled grower data used without a data-use review | **No** |
| Accountable and transparent | Prescriptions labeled as AI-generated with the inputs used | Labeled; inputs not shown | **Partial** |

### 4.3 AI-003 spray drones (pilot) and AI-007 (proposed)
- **AI-003:** in 64 pilot flights, detection recall for target weeds was 91%, and 2 flights sprayed outside the intended row band by up to 1.5 m; no flight left an approved block (geofences held). Condition: off-target spray under 0.5 m before any expansion.
- **AI-007:** not deployed. Before any approval: test outcomes and inputs for disparate effects on prohibited bases (12 CFR 1002.4(a)), confirm the model can produce specific reasons for adverse action (1002.9), and confirm Social Security numbers are used only for identity matching.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** estimates are advice. Agronomists check every block estimate against hand counts on sample plots before crew plans or commitments; commitments are capped at 85% of the estimate unless hand counts confirm more; no crew hours are cut on an estimate alone, and hours offered never fall below the three-fourths guarantee; finance uses only the validated version in valuations.
- **AI-006:** prescriptions outside agronomic ranges require agronomist approval; growers review before export; hard rate limits per product.
- **AI-003:** a certificated remote pilot supervises every flight and can stop spraying; the agronomist locks products, rates, and geofences.
- **AI-007:** advisory only if ever approved; credit staff decide and write the reasons.

**Monitoring:** weekly AI-001 error tracking in season, monthly subgroup bias checks, and model version recorded with every use; monthly AI-006 out-of-range report; quarterly High-tier report to the council and the board risk committee. P01 risks: GR-08, GR-09, CF-012, FP-012, FS-004, FS-006.

**Incident handling:** an AI failure that causes crop damage, worker harm, a food safety concern, or a breach of grower commitments follows P08 and POL-03; an AI-006 failure that reaches many growers triggers the cooperative notice row.

**Decommissioning:** each use case has an off switch and a fallback the BIA covers: hand counts (AI-001), agronomist desktop prescriptions (AI-006), ground spraying (AI-003), manual scheduling (AI-002), and manual credit review (AI-007).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 yield prediction | **Continue with conditions** (council, 2026-08-28; board risk committee informed 2026-09-10) | Change gate with validation and finance sign-off live by 2026-10-31; validation of the 2026-27 season version by 2026-12-31 (POAM-021); new variety and acquired-farm calibration by hand counts; watermelon and peanut estimates advisory only until MAPE is at or below 15% for a season; crew plan decision log by 2026-11-30; deploy rights limited to 3 release managers |
| AI-006 portal prescriptions | **Continue for current users; pause new cooperative enrollments** | Hard rate limits and agronomist approval for out-of-range prescriptions by 2026-10-31; data-use review and terms decision, and claims substantiated or revised, by 2026-12-31 (POAM-019); coastal plain calibration before the 2027 season |
| AI-003 spray drones | **Pilot only; no expansion** | Off-target spray under 0.5 m in 30 consecutive flights; FAA and WPS compliance file reviewed by counsel |
| AI-007 credit scoring | **Not approved** | Disparate-effect testing, adverse action reason codes, and a Regulation B review before resubmission |
| AI-002 irrigation recommendations | **Continue in recommendation mode** | Automatic application requires a new High-tier assessment |
| AI-004, AI-005 | **Continue** | AI-005 uses only the validated AI-001 version; AI-004 settings through change control |
| AI-008 | **Pilot continues** | Prohibited for decisions about people, credit, food safety, or OT; Restricted data blocked |
| AI-009, AI-010 | **Approved** | Standard monitoring |

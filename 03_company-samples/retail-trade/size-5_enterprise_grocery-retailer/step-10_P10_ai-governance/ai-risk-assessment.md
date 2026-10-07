# AI Governance Risk Assessment: Enterprise AI Portfolio and Dynamic Pricing and Personalized Offers

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional supermarket chain; 112 stores in FL, GA, AL, SC, TN; online ordering) |
| Tier / Vertical | Enterprise / Retail Trade |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 dynamic pricing and personalized offers in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-006 and AI-009; repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Data and Analytics Officer), meeting of 2026-08-19; the GRC team prepared the portfolio review and the data science team ran the AI-001 tests (2026-07-20 to 2026-08-14) |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 2, Medium 8, Low 2 |
| Status | In production 10, Pilot 1, Suspended 1 |
| Committee review complete | 7 of 12 |
| Not yet reviewed | 5: AI-005, AI-007, AI-008, AI-010, AI-011 (all due 2026-11-30, POAM-021) |
| Tennessee data protection assessments needed and not complete | 2 use cases (AI-001 profiling; AI-004 targeted advertising), plus app precise location (POAM-019) |
| Use cases with fairness testing on the affected population | 2 of the 6 that make or shape outcomes for customers or employees (AI-003, AI-012); AI-001 tested only by store cluster |

**Main findings:** 5 use cases run (or pilot) without committee review, including both High-tier tools: AI-010, which reorders refrigeration alarms (food safety), and AI-008, an employment tool whose ranking is now disabled. The pricing and offers engine (AI-001) has strong price guardrails but has been tested for fairness only by store cluster, its emergency price freeze covers only Florida, and its Tennessee profiling assessment is not done. Facial recognition is not used anywhere, by board decision (P01 R-040).

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk and technology committee reviews quarterly.

**Members:** Chief Data and Analytics Officer (chair); Chief Privacy Officer; CISO; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (workforce and HR tools); Chief Merchandising Officer; Chief Marketing Officer; Senior Vice President, Store Operations; Director of Data Science. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Validation and fairness testing on the company's own data; impact assessment (including a Tennessee data protection assessment where one is required); human review design; notice to affected people; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where customers interact with it; privacy and security review; fairness screening where outcomes differ by person or place |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.6; STD-05.3). Since 2026-03, procurement and change management block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.7 (new uses of customer data need a privacy review and, where required, a Tennessee data protection assessment); POL-04 4.8 (sensitive data only with consent; no facial recognition or other biometric identification of customers); POL-04 4.11 (no Restricted or Confidential data in AI tools without committee approval and no-training terms); POL-05 4.6 (approved tools only); POL-01 4.18 (savings and AI claims reviewed by Legal before publication).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier and customer-facing Medium-tier use case; annual re-review of every use case.

**Why 5 use cases lack review.** Three arrived as vendor feature releases before the intake block existed (AI-005 self-checkout vision, AI-007 scheduling, AI-011 SOC triage), one is a vendor model inside the refrigeration monitoring service (AI-010), and one is the applicant tracking system's ranking feature (AI-008). The committee set review dates for all five (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, deception, 15 U.S.C. 45(a)(1) (N44-45-R02) | Yes | Savings claims, "personalized for you" statements, AI assistant answers (AI-006), and privacy statements about how purchase data is used must be truthful and substantiated |
| FTC Act Section 5, unfairness, 15 U.S.C. 45(n) (N44-45-R02) | Yes | A practice is unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits. Higher online prices or weaker offers in lower-income delivery zones, and false accusations at self-checkout, are the scenarios to guard against |
| Tennessee Information Protection Act (2023 Tenn. Pub. Acts ch. 408; bill numbering) | Yes | The company controls personal information of about 240,000 Tennessee consumers. Data protection assessments are required for targeted advertising (47-18-3206(a)(1)) and for profiling that presents a reasonably foreseeable risk of unfair treatment, disparate impact, or financial injury (47-18-3206(a)(3)). Consumers may opt out of targeted advertising and of profiling in furtherance of decisions that produce legal or similarly significant effects (47-18-3203(a)(2)(E)); the definition of those decisions includes access to basic necessities such as food and water (47-18-3201(10)). A controller may offer different prices or discounts tied to a bona fide loyalty program (47-18-3204(a)(5)) |
| SNAP equal treatment, 7 CFR 278.2(b) | Yes, for AI-001 | SNAP benefits must be accepted for eligible foods at the same prices and on the same terms as cash purchases of the same foods at the same store. Payment tender type is therefore excluded from pricing and offer features |
| Price gouging during a declared emergency, Fla. Stat. 501.160 (worked example) | Yes, for AI-001 during emergencies | Food and water are commodities under the statute; a gross disparity from the average price in the 30 days before the declaration is prima facie unconscionable unless justified by costs or market trends. The other four states have their own laws; the company applies one freeze rule in all five states |
| Federal equal employment opportunity laws | Yes, for AI-007, AI-008, AI-012 | Counsel reviews adverse impact before AI-008 ranking is re-enabled, and reviews scheduling and loss prevention outcomes by job class |
| Visa Core Rules 1.9.4.2 (ID# 0026337, contractual) | Yes, for AI-004 | Transaction information may be disclosed to third parties only for the purposes the rules allow; no payment fields enter the clean room (POAM-020) |
| FTC surveillance pricing 6(b) study (orders July 2024; staff research summaries January 2025) | Watch item | A study, not a rule. It shows FTC interest in prices or offers set from personal data (P03 section 6) |
| CCPA automated decisionmaking rules (N44-45-R06) | No | No stores, delivery, or targeted marketing in California (P03). Recheck if online sales reach California |

**Tennessee "basic necessities" note.** Because the definition of decisions with legal or similarly significant effects includes access to food, counsel reviewed two use cases. AI-001 sets prices by item, store, and time and adds loyalty discounts on top of shelf prices; it does not set a person's price or deny anyone food. AI-003 declines some online orders as suspected fraud; customers can still buy in stores, and any customer can ask for manual review. Counsel's preliminary view is that neither is such a decision, and the company will still offer a "standard offers" choice that turns off personalized offers (section 7.5).

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision (for example, employment) or able to affect physical safety or critical operations.

| ID | Use case | Tier | Status | Committee review | Tennessee assessment |
|---|---|---|---|---|---|
| AI-001 | Dynamic pricing and personalized offers: ESL markdowns, online prices within bounds, and weekly personalized digital coupons (SYS-12) | Medium | In production (112 stores for markdowns; online prices; 3.1 million members for offers) | Reviewed 2025-11-12; full assessment 2026-08-19 | Profiling assessment not complete (POAM-019) |
| AI-002 | Demand forecasting and automated store replenishment | Low | In production | Reviewed 2026-02-11 | Not required (no personal information) |
| AI-003 | Card-not-present fraud screening for online orders | Medium | In production | Reviewed 2026-03-18 | Not required (fraud prevention); counsel reviewing the basic necessities definition |
| AI-004 | Retail media audience building and closed-loop measurement in the clean room (SL-1) | Medium | In production (about 140 CPG clients) | Reviewed 2026-02-25 | Targeted advertising assessment not complete (POAM-019) |
| AI-005 | Self-checkout computer vision that detects missed scans and alerts the attendant | Medium | Pilot (24 stores) | Not reviewed (review due 2026-11-30, POAM-021) | To be decided in the committee review |
| AI-006 | Customer service virtual assistant (generative) for order status, refunds, and store information | Medium | In production | Reviewed 2026-05-20 | Not required |
| AI-007 | Workforce scheduling optimization for store associates | Medium | In production | Not reviewed (review due 2026-11-30, POAM-021) | Not applicable (employee data) |
| AI-008 | Applicant resume screening and ranking in the applicant tracking system | High | Suspended (ranking disabled pending review) | Not reviewed (review due 2026-11-30, POAM-021) | Not applicable (applicant data) |
| AI-009 | Enterprise generative AI assistant for workforce productivity | Medium | In production | Reviewed 2026-01-14 | Not required |
| AI-010 | Refrigeration anomaly detection that prioritizes alarms for the facilities team | High | In production (core stores; reordering only) | Not reviewed (review due 2026-11-30, POAM-021) | Not required (no personal information) |
| AI-011 | SOC alert triage assistant | Low | In production | Not reviewed (review due 2026-11-30, POAM-021) | Not required |
| AI-012 | Loss prevention exception-based reporting for refunds, voids, manager overrides, and SNAP EBT patterns | Medium | In production | Reviewed 2026-04-15 | Not applicable (employee data) |

**Tiering notes:** AI-010 is High because a wrongly deprioritized alarm could let unsafe food reach customers. AI-008 is High because ranking applicants is an employment decision factor. AI-001 is Medium, not High: pricing is not one of the rubric's consequential-decision categories, and merchandising bounds every price; it would re-tier to High under the triggers in section 7.3. AI-005 is Medium because the alert reaches only the attendant, who offers help; any use of alerts for stops or bans would re-tier it to High.

## 5. Tennessee Act duties for AI and data use
| Duty | What the company does | Status |
|---|---|---|
| Data protection assessment for targeted advertising (47-18-3206(a)(1)) | Assessment of offsite retail media audiences (AI-004) with outside privacy counsel | Not met: due 2026-12-15 (POAM-019) |
| Data protection assessment for profiling with foreseeable risk (47-18-3206(a)(3)) | Assessment of personalized offers and online pricing (AI-001), using the fairness results in section 7.4 | Not met: due 2026-12-15 (POAM-019) |
| Opt-outs (47-18-3203(a)(2)(E)) and disclosure of targeted advertising (47-18-3204(d)) | Privacy notice update with an opt-out link for targeted advertising; "standard offers" choice in the app and on the website | Partially met: notice update due 2026-12-31 (POAM-019, POAM-023) |
| Consent for sensitive data (47-18-3204(a)(6)) | Precise location used only at pickup check-in; consent record and withdrawal path being added; no biometric identification | Partially met: in-app consent due 2026-11-15 (POAM-019) |

These rows match P03 G-101, G-102, and G-104.

## 6. MEASURE: fairness testing gap and plan (portfolio)
**Gap.** Only AI-003 and AI-012 have outcome testing on the people they affect. AI-001 has been tested only by store cluster, which hides differences between neighborhoods served by the same store and between delivery zones. AI-005, AI-007, and AI-008 have no testing yet.

**Plan (POAM-021; company-defined screening rules, not legal standards):**
| Use case | Metric | Groups compared | Threshold for action |
|---|---|---|---|
| AI-001 prices | Price index (online price divided by shelf price, same 300-item basket) | Delivery zones; customer home ZIP codes grouped by Census median household income quintile | Any zone more than 1.0 percentage point above the lowest zone, or lower-income groups above higher-income groups |
| AI-001 offers | Average weekly offer value per active member, relative to the highest group | Home ZIP code income quintiles; stores; new versus long-tenure members | Ratio below 0.80 for any group |
| AI-005 self-checkout vision | False alert rate (alerts where the attendant found no missed scan) | Stores; time of day; lane type | Any store more than 1.5 times the chain rate |
| AI-007 scheduling | Average weekly hours offered relative to availability | Job class; age band; part-time and full-time | Ratio below 0.80 for any group |
| AI-008 resume ranking | Selection rate for interview | Groups with self-identified data from voluntary applicant surveys | Adverse impact ratio below 0.80 (counsel reviews) before any re-enable |

**Data limits:** the company does not collect race, ethnicity, or sex for customers and will not infer them. Customer tests use geography (home ZIP code income quintiles from public Census data and delivery zones) as the comparison, because geography can act as a proxy for both income and protected characteristics.

## 7. Full assessment: AI-001 dynamic pricing and personalized offers
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | **(a) Markdowns:** set electronic shelf label (ESL) markdowns for perishables near their sell-by date at the 40 ESL stores and printed markdown labels elsewhere. **(b) Online prices:** set each item's online price within plus or minus 10% of the store shelf price, by store and time, based on demand, stock, and freshness. **(c) Personalized offers:** choose weekly digital coupons for each loyalty member from purchase history |
| Users and operators | Merchandising sets bounds, cost floors, and exclusions; marketing sets offer budgets and campaigns; data science builds and monitors the models; the pricing change board approves rule changes |
| Affected people | About 3.1 million loyalty members (about 240,000 in Tennessee), about 1.4 million online shopping accounts, and every shopper at the 40 ESL stores |
| Data | Inputs: pseudonymous member ID and purchase history; store cluster; delivery zone; item cost, shelf price, stock, and sales velocity; weather and local events. **Not used:** name, contact data, precise location, payment tender type (SNAP EBT or card type), card data, or any demographic field. Checked by the data science team on 2026-08-05 against the feature list |
| Build or buy | Built by the data science team on Cloud B with a commercial optimization library; model and rule changes go through the pricing change board (P04) |
| Not intended | Individual prices for a person; price increases during a declared emergency; any use of SNAP status; any credit, employment, or eligibility decision. **Enabling person-level online prices requires a new assessment** |

### 7.2 Rules that shape the design
- **SNAP equal treatment (7 CFR 278.2(b)):** tender type is blocked at the feature store, and offers cannot be conditioned on how a customer pays.
- **Price gouging (Fla. Stat. 501.160 as the worked example):** when a state of emergency is declared for any county with a company store, the engine freezes increases above the 30-day pre-declaration average for that state's stores. Today the freeze is configured for Florida only and has not been tested (P01 R-012; P03 G-110).
- **Tennessee Act:** profiling assessment (47-18-3206(a)(3)) and a "standard offers" choice (section 5).
- **FTC Act:** "personalized savings" and reference price claims need a substantiation file (P03 G-076).

### 7.3 Risk tier
Medium (section 4). **Escalation triggers (re-tier to High and re-assess):** person-level online prices; any input that identifies or infers a protected characteristic or payment tender type; widening online bounds beyond plus or minus 10%; using offers to exclude members from staple items; expansion into a state with surveillance pricing or automated decision laws.

### 7.4 MEASURE (tests run 2026-07-20 to 2026-08-14)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Daily exception report: prices outside bounds, below item cost, or changing more than twice a day (target 0 below cost) | 0 below-cost prices; 14 items changed 3 times in a day during a cost-file delay, caught by the report | Yes |
| Safe | Emergency freeze: no increase above the 30-day pre-declaration average during a declared emergency, in every state | Configured for Florida only (2026-09); not tested; Georgia, Alabama, South Carolina, and Tennessee rely on manual steps | **No** |
| Secure and resilient | Cloud B guardrails; model and rule changes through the pricing change board; no card data in Cloud B (weekly scan) | In place | Yes |
| Accountable and transparent | Website and app explain that offers are personalized from purchase history and that online prices can differ from shelf prices | Offers disclosed; online price difference disclosed only in the help center | Partial |
| Explainable and interpretable | Factor report for each price and each offer | Available for prices and markdowns; offers show the top 3 factors only | Partial |
| Privacy-enhanced | Pseudonymous IDs; minimum features; Tennessee profiling assessment | IDs and features compliant; assessment not done | **No** |
| Fair, with harmful bias managed | Price index by delivery zone and offer value ratio by income quintile (section 6) | Store clusters within thresholds. First neighborhood analysis on July 2026 data: online price index within 0.6 points across zones (pass); offer value ratio 0.78 for the lowest-income quintile (flag) | **No** (offer value gap) |

**Why the offer gap appeared.** Members in the lowest-income quintile buy more store-brand staples, which the offer model scores as less responsive to coupons, so they received lower-value offers. The model is optimizing for redemption, not for equal benefit.

### 7.5 MANAGE
- **Human in the loop:** merchandising sets bounds and cost floors; category managers review the daily exception report; the pricing change board approves every rule or model change; material changes go to the committee.
- **Offer gap:** a minimum weekly offer value for every active member and a staples floor in the offer mix, live by 2027-01-31; monthly offer value ratio reported to the committee (POAM-021).
- **Emergency freeze:** extend to all five states, tied to emergency declaration feeds, and test before each hurricane season, by 2027-05-31 (POAM-021).
- **Choice:** a "standard offers" setting that turns off personalized offers, available to every member (not only Tennessee residents), by 2026-12-31.
- **Monitoring:** daily exception report; monthly price index by zone and offer value ratio by income quintile; quarterly committee review.
- **Incidents:** a pricing error that charges customers more than the shelf price is handled as a customer incident with refunds; a data misuse or security event follows P08.
- **Decommissioning or rollback:** revert to rule-based markdowns and standard offers if the offer value ratio stays below 0.80 for two consecutive months after the fix, or if the freeze fails a test.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier and customer-facing Medium-tier use case has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (harmful output, fairness finding, data misuse, wrong alarm priority) are logged as SOC or operations events and follow P08 where security or customer data is involved.
- **Third parties:** AI vendors are tier-1 in the third-party program; contracts require notice of material model changes and prohibit training on company data (POL-04 4.11).
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice or a vendor changes data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the AI governance committee's recommendation of 2026-08-19:
1. **AI-001:** approved to continue with conditions: minimum offer value and staples floor by 2027-01-31; Tennessee profiling assessment by 2026-12-15; "standard offers" choice by 2026-12-31; emergency freeze for all five states tested by 2027-05-31 (POAM-019, POAM-021).
2. **AI-010:** stays in reordering-only mode, with every alarm still notifying technicians; suppression stays disabled until the committee reviews it and the vendor validates it against alarm outcomes.
3. **AI-005:** pilot stays at 24 stores until the committee review; alerts go only to attendants; no expansion.
4. **AI-008:** ranking stays disabled until the committee review and an adverse impact analysis are complete.
5. **AI-007, AI-011:** may continue in current scope until review by 2026-11-30.
6. **AI-004:** Tennessee targeted advertising assessment by 2026-12-15 and the privacy notice update by 2026-12-31 (POAM-019, POAM-023).

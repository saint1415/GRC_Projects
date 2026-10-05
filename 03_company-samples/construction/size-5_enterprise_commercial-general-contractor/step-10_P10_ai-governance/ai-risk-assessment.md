# AI Governance Risk Assessment: Enterprise AI Portfolio and the AI Estimating and Bid Assistant

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded commercial and institutional building general contractor; 8 states) |
| Tier / Vertical | Enterprise / Construction |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the AI estimating and bid assistant, in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`) |
| Assessor / date | AI governance committee (chaired by the CIO), meeting of 2026-08-12; the GRC team prepared the portfolio review; Internal Audit observed |
| Decision | Executive risk committee, 2026-09-08 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 3, Medium 7, Low 2 |
| Status | In production 10, Pilot 1, Suspended 1 |
| Committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-003, AI-009, AI-010, AI-012 (all due 2026-11-30; P01 R-061) |
| Use cases allowed to receive FCI | 6 (AI-002, AI-004, AI-005, AI-008, AI-011 for federal buildings, and AI-009 for log metadata), each inside the enterprise Level 1 scope |
| Use cases allowed to receive CUI | 0. No AI tool is approved for CUI (POL-04 4.10) |
| High-tier use cases without completed review | 2 (AI-010 suspended; AI-012 in pilot) |

**Main findings:**
1. **Four use cases run without committee review.** Two entered through vendor feature releases (AI-003 in the project management platform, AI-009 in the SIEM), one is an HR pilot (AI-010), and one is a BTS pilot that changes client building setpoints (AI-012). The intake rule from 2025 did not catch features that vendors switch on inside existing products.
2. **AI-001's pooled pricing feature** put the federal price certification at risk (P01 R-056, High). It was disabled on 2026-08-05 and counsel's review found no federal bid used pooled figures (section 7.6).
3. **AI-001 accuracy and fairness** are below threshold for MEP and renovation takeoffs (R-057) and for first-time bidders in bid leveling (R-058).
4. **Federal data boundaries hold so far** but depend on settings and contracts: AI-001 receives no FCI until enterprise terms are signed, AI-003 is switched off on federal projects, and no AI tool touches the FPCE (R-060).

## 2. GOVERN: AI governance committee operating model
**Charter.** Formed in 2025 under POL-01 and reporting to the executive risk committee. Its risks roll up to enterprise risk ER-09 Responsible use of AI (P01), which the board risk committee reviews quarterly.

**Members:** CIO (chair); CISO; Chief Compliance Officer; a delegate of the General Counsel; Chief Human Resources Officer; Vice President, Preconstruction; Vice President, Safety; Vice President, Building Technology Services; Director, CMMC Program Office; Director of Government Contracts; the data science lead. Internal Audit observes and does not vote.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Pre-deployment testing on company or client data; bias or adverse impact testing where people are affected; impact assessment; human review design; notice to affected people; monitoring plan; for client building systems, client written approval |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; security, federal data, and contract review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.7; STD-05.3). From 2026-10, procurement and IT change management require an inventory ID for any AI feature, and the vendor review checklist asks whether each release adds or changes AI features. The GRC team owns the inventory.

**Federal data gate.** Before any use case may receive FCI, the Director, CMMC Program Office confirms it is inside the enterprise Level 1 scope or sits on a system with the required status (DFARS 252.204-7021(d)(2)) and that the contract allows the use (FAR 52.204-21(b)(1)(iii)). No use case may receive CUI.

**Policies:** POL-04 4.10 (no FCI, Restricted, or Confidential data in AI tools without committee approval and enterprise no-training terms; no AI for CUI); POL-05 4.7 (approved tools only) and 4.10 (no discipline from camera analytics without a High-tier assessment); POL-01 4.8 (vendor terms before data); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier and every Medium-tier use case that affects bids, payments, or people; annual re-review of every use case.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21(b)(1)(iii) | Yes, for any use case that receives FCI | The company must "verify and control/limit connections to and use of external information systems". An AI service that receives FCI must be inside the assessed scope with enterprise terms |
| DFARS 252.204-7021(d)(2) | Yes, on DoD contracts with the clause | FCI may be processed only on systems with the required CMMC status; CUI only on systems with Level 2 status (the FPCE) |
| FAR 52.203-2, Certificate of Independent Price Determination | Yes, on federal bids (AI-001) | The offeror certifies prices were arrived at independently, without "consultation, communication, or agreement with any other offeror or competitor" about prices or "the methods or factors used to calculate the prices offered" |
| FAR 15.403-4, certified cost or pricing data | When required (AI-001) | Required above the threshold for negotiated actions unless an exception applies ($2.5 million for prime contracts awarded on or after July 1, 2018, per eCFR 2026-09-23). AI-derived figures must be traceable to source records |
| FAR 52.219-8 and 52.219-9 | Yes, on federal jobs (AI-001, AI-006) | Federal policy gives small, veteran-owned, service-disabled veteran-owned, HUBZone, small disadvantaged, and women-owned small businesses "the maximum practicable opportunity to participate". 52.219-9 (subcontracting plans) does not apply to small business concerns, so it applies to this company's contracts that include it |
| Sherman Act Section 1 (15 U.S.C. 1) | Indirectly (AI-001, AI-006) | Price-fixing and bid rigging are illegal; counsel reviews any vendor feature that pools or shares pricing across contractors |
| Federal equal employment opportunity laws (Title VII disparate impact) | Yes, for AI-010; for AI-007 if used for discipline | Employment selection tools are reviewed for adverse impact before use |
| Texas Responsible AI Governance Act (HB 149) | Yes, as a baseline (the company does business in Texas; no size threshold) | Intent-based prohibitions, including AI developed or deployed with intent to unlawfully discriminate. Its disclosure duties apply to government agencies and health care service providers, not to this company. The committee records the intended purpose of each use case |
| State AI employment and ADMT laws (Colorado SB26-189, Illinois HB 3773, NYC Local Law 144, California rules) | No | The company does not operate in those jurisdictions. Rechecked yearly and before any expansion |
| FTC Act Section 5 | Indirectly | Applies to vendors' accuracy claims; the claims relied on are kept in the procurement file |
| SEC disclosure controls | Indirectly (AI-005) | Schedule forecasts are not used in financial reporting without Chief Accounting Officer review |

## 4. Risk tiering
Rubric: High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations. The rubric is repository-defined, not a regulation.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | AI estimating and bid assistant | Medium (elevated controls) | In production for non-federal bids; federal use limited | Re-assessed 2026-08-12 |
| AI-002 | Enterprise generative AI assistant | Medium | In production | Reviewed 2025-11-18 |
| AI-003 | RFI and submittal drafting assistant (vendor feature in SYS-01) | Medium (provisional) | In production; off on federal projects | Not reviewed (due 2026-11-30) |
| AI-004 | Drawing search and clash summary assistant | Low | In production | Reviewed 2026-02-17 |
| AI-005 | Schedule risk forecasting | Medium | In production | Reviewed 2026-01-27 |
| AI-006 | Subcontractor prequalification risk scoring | Medium | In production | Reviewed 2026-03-24 |
| AI-007 | Jobsite computer vision safety analytics | Medium (High if used for discipline) | In production, coaching only | Reviewed 2026-04-21 |
| AI-008 | AP document extraction and matching | Medium | In production | Reviewed 2026-05-19 |
| AI-009 | SOC alert triage assistant | Low (provisional) | In production | Not reviewed (due 2026-11-30) |
| AI-010 | Craft recruiting chatbot with applicant ranking | High | Suspended (ranking disabled) | Not reviewed (due 2026-11-30) |
| AI-011 | BTS video analytics for client buildings | High | In production (58 buildings) | Reviewed 2026-05-12 |
| AI-012 | Building automation energy optimization | High | Pilot (3 buildings) | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-011 and AI-012 are High because they act on physical security and building operations in occupied client buildings. AI-010 is High because it ranks job applicants (employment). AI-001 is Medium under the rubric because it makes no decision about a person and an estimator owns every number, but the committee applies **elevated controls** because a single error or a pooled price can create federal certification exposure or a multi-million-dollar fixed-price loss. AI-007 stays Medium only while discipline is prohibited (POL-05 4.10; P01 R-059 avoided). AI-008 is Medium because it touches payment documents; it is configured so it can never change payees or bank details (POL-01 4.13).

## 5. Portfolio controls for federal data and client systems
| Control | Applies to | Status |
|---|---|---|
| No AI tool approved for CUI; FPCE has no AI services | All | Met |
| FCI only in use cases inside the enterprise Level 1 scope with enterprise no-training terms | AI-002, AI-004, AI-005, AI-008, AI-009, AI-011 | Met; AI-001 blocked from FCI until terms are signed |
| Vendor release review for new AI features in existing products | All SaaS | Partially met: AI-003 and AI-009 arrived through releases (fixed by the 2026-10 intake rule) |
| Client written approval before AI acts on client building systems | AI-011, AI-012 | Met for AI-011; AI-012 pilot has client approval but no committee review |
| Life-safety exclusion (fire alarm, smoke control, emergency power) | AI-011, AI-012 | Met (configuration checked 2026-08) |

## 6. MEASURE: portfolio monitoring
| Use case | Metric | Threshold for action | Latest result |
|---|---|---|---|
| AI-001 | Takeoff error by trade; recommendation ratio by subcontractor group | Section 7.4 | Section 7.4 |
| AI-006 | Prequalification approval rate for certified small business groups and first-time firms divided by the rate for all others | Below 0.8 | 0.86 to 0.97 (Q2 2026); first-time firms 0.83 |
| AI-007 | Alert precision on a monthly sample; disciplinary actions citing analytics | Precision below 80%; any disciplinary citation | 84%; none found |
| AI-008 | Extraction accuracy on amounts and payee names; bank fields ignored | Below 98%; any bank field used | 99.1%; bank fields ignored in all samples |
| AI-011 | Alert precision by site; missed intrusions found in client reviews | Precision below 70%; any missed intrusion | 76%; 1 missed loitering event (tuning applied) |

## 7. Full assessment: AI-001 AI estimating and bid assistant
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Speed up estimating: (1) quantity takeoff from drawings; (2) unit pricing from the company's historical cost database and the vendor's market data; (3) subcontractor bid leveling (normalizing scope, flagging exclusions, ranking bids); (4) drafting proposal narratives |
| Users / operators | About 120 estimators in the Building Group and the Federal Group; preconstruction directors review output |
| Affected parties | Owners (the price they pay), subcontractors (whether they are selected, including small and disadvantaged businesses), the company (fixed-price exposure), and the Government (price certifications on federal bids) |
| Data | Inputs: drawings and specifications, historical costs, subcontractor bid forms. Outputs: quantities, unit prices, leveled bid tables, recommendations, draft text. The read-only connector to the estimating database is in Cloud provider A (P04) |
| Build or buy | Buy: vendor SaaS. Standard terms allowed customer data to be used to improve models; enterprise terms (no training on company data, deletion within 30 days, US data location, SSO with MFA) are under negotiation, due 2026-10-31 |
| Not intended | Automatic bid submission; subcontractor selection without an estimator's documented decision; certified cost or pricing data without human verification; any hiring, discipline, or crew-assignment use; structural or life-safety quantities |

**Is the data FCI?** It depends on the stage. Public solicitation documents posted for all bidders are not FCI, because FAR 52.204-21(a) excludes "information provided by the Government to the public". Drawings, change orders, and modifications on an **awarded** federal contract are FCI. Until enterprise terms are signed, federal project folders are blocked from the connector and estimators may not upload awarded-contract documents. CUI is never allowed: design-build and MILCON CUI drawings stay in the FPCE.

### 7.2 Risk tier
Medium with elevated controls (section 4). Escalation triggers that require a High-tier re-assessment: automatic bid submission or subcontract award; any employment use; structural, fire protection, or other life-safety quantities; or enabling any feature that pools pricing across the vendor's customers.

### 7.3 Pooled pricing and the federal price certification
- **What happened.** The vendor's "market pricing insights" feature was on by default. It blends unit prices from the vendor's other customers, which include competing contractors, into pricing suggestions.
- **Why it matters.** On a federal bid, the company certifies under FAR 52.203-2 that prices were arrived at independently, without consultation, communication, or agreement with any competitor about prices or the methods or factors used to calculate them. Counsel's view is that silently using a competitor-pooled price index creates certification and antitrust exposure (Sherman Act Section 1) the company will not accept, whatever its legal merits.
- **What was done.** The committee disabled the feature on 2026-08-05; enterprise terms must bar pooling of the company's data into other customers' suggestions; a monthly configuration check confirms the feature stays off.
- **Look-back.** Counsel and the Director of Government Contracts reviewed the 14 federal bids and 6 change order proposals priced with AI-001 support since 2026-03. None used pooled suggestions for final prices; the estimators had overwritten them with company cost data. The review is filed with the bid records.

### 7.4 MEASURE
Test basis: back-test on 40 completed bids (12 federal, 28 private), plus live monitoring of 410 bid packages (2,860 subcontractor bids) from March to August 2026.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Takeoff quantity error by trade versus the estimator's final takeoff. Threshold: within 5% for concrete, steel, and drywall; within 10% for other trades | Concrete 3%, drywall 4%, steel 4%; MEP fixture counts 13%, sitework 9%. Renovation projects averaged 11% against 4% for new construction | **No** for MEP and renovations |
| Safe | No bid leaves without estimator verification and director approval | 100% of sampled bids reviewed; 3 quantity errors caught at review | Yes |
| Secure and resilient | Vendor SOC 2 Type 2; SSO with MFA; access limited to licensed estimators | Vendor SOC 2 Type 2 reviewed (no exceptions); SSO live; 6 former estimators still had access (removed 2026-08-14) | Partial |
| Accountable and transparent | Each AI-derived figure in an estimate is tagged with its source (AI takeoff, cost database, vendor market data) | Tagging live in the estimate template since 2026-07; 92% of sampled figures tagged | **No** (target 100%) |
| Explainable and interpretable | Estimator can see what was counted on each sheet and the basis of each price suggestion | Takeoff overlays available; price suggestions show the source database rows since 2026-08 | Yes |
| Privacy-enhanced (confidentiality) | No training on company data; deletion within 30 days; US data location; no cross-customer pricing features | Pooled feature off; enterprise terms not yet signed | **No** until terms are signed |
| Fair, with harmful bias managed | Bid leveling recommendation rate for each subcontractor group divided by the rate for all others, among bids within 5% of the low price. Groups: certified small disadvantaged, women-owned, HUBZone, service-disabled veteran-owned, veteran-owned small businesses, and first-time bidders to the company. Flag any ratio below 0.8 (a heuristic borrowed from employment selection practice, not a legal threshold for subcontracting) | Certified small business groups: 0.87 to 0.96. **First-time bidders: 0.58** | **No.** Disparity flagged |

**Bias finding.** The ranking weights the company's historical performance score. First-time bidders have no history, and the model treats missing history as poor history, which pushes new firms down. Many new firms are small or disadvantaged businesses, so on federal jobs this works against the FAR 52.219-8 policy and the company's subcontracting plan goals (52.219-9), and on every job it narrows the subcontractor base. It is a missing-data problem, not a protected-status input. The fix is to score missing history as neutral and to show estimators the price-only ranking beside the model's ranking.

### 7.5 MANAGE
**Human-in-the-loop design:**
- The tool produces drafts only. An estimator verifies every takeoff for concrete, steel, drywall, MEP, and sitework against the drawings; MEP and renovation takeoffs are done manually until the tool meets the threshold for two quarters.
- Bid leveling is advisory. The estimator records the reason for each subcontractor selection in the bid file.
- On federal bids, the preconstruction director signs the price certification only after confirming that no pooled market pricing was used and that every AI-derived figure is tagged to company source records (FAR 52.203-2; FAR 15.403-4 where certified cost or pricing data are required).

**Monitoring:** quarterly accuracy by trade and project type and quarterly recommendation ratios, reported to the committee and tracked against P01 R-057 and R-058; monthly configuration check of the pooled-pricing feature (R-056); estimators report wrong outputs through the estimating issue log.

**Incident handling:** a vendor security incident, data-use change, or re-enabled pooling feature follows P08 and the contract notice terms; a material estimating error in a submitted bid is escalated to the Vice President, Preconstruction, the CFO, and counsel before award.

**Decommissioning:** stop federal use permanently and export or delete company data if enterprise terms are not signed by 2026-12-31; stop use if accuracy thresholds are still missed after two quarters; stop use if the vendor enables cross-customer pricing that cannot be turned off.

### 7.6 Decision for AI-001
**Approve with conditions** (committee 2026-08-12; executive risk committee 2026-09-08):
1. **Now:** pooled market pricing stays off, checked monthly; no FCI uploads until enterprise terms are signed (target 2026-10-31).
2. **Now:** manual takeoffs for MEP and all renovation projects.
3. **By 2026-10-31:** missing performance history scored as neutral, and the bias check rerun.
4. **By 2026-11-30:** source tagging at 100% for AI-derived figures in every estimate.
5. **Before any federal use with FCI:** signed enterprise terms, confirmation by the Director, CMMC Program Office that the tool is inside the enterprise Level 1 scope, and counsel's sign-off on the federal pricing workflow.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case and each Medium-tier use case that affects bids, payments, or people has quarterly metrics (inventory column `monitoring`) reported to the committee; threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe action on a client building, biased output, data misuse, unexpected vendor feature) are logged as SOC or safety events and follow P08 where security, personal information, or FCI is involved.
- **Third parties:** AI vendors are tier-1 in the third-party program; contracts require no training on company data, notice of material model or feature changes, and deletion on exit.
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice, change data-use terms, or move outside the federal data gate; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the committee's recommendation of 2026-08-12:
1. **AI-001:** approved with the conditions in section 7.6.
2. **AI-003 and AI-009:** may continue in current scope until review by 2026-11-30; AI-003 stays off on federal projects.
3. **AI-010:** ranking stays disabled until committee review and an adverse impact analysis are complete; chatbot scheduling may continue.
4. **AI-012:** no expansion beyond the 3 pilot buildings until a High-tier review is complete by 2026-11-30; life-safety exclusion confirmed monthly.
5. **AI-007:** discipline based on camera analytics remains prohibited (POL-05 4.10).
6. **Intake:** from 2026-10, every vendor release review asks whether AI features were added or changed, and procurement blocks AI features without an inventory ID.
